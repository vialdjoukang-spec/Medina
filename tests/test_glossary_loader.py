"""Contrôles techniques du chargeur ; aucune définition clinique rédigée/modifiée."""
import builtins
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('glossary_loader_under_test', ROOT / 'tools/glossary_loader.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


BASE = """G = {}
def a(key, value):
    G[key] = {'full': value}
a('SHARED', 'base')
"""


def conditional(name, body, shared=False):
    if shared:
        return ("from cardio_1 import a, G\nfrom pathlib import Path\nimport importlib\n_ex = set(G)\n" +
                m._TEMPLATES[-1][0].replace('__MEDINA_SELF__', name) + '\n' + body)
    return ("from pathlib import Path\nimport importlib\n_existing = {}\n" +
            m._path_loop('Path(__file__).parent').replace('__MEDINA_SELF__', name) + "\nG = {}\n" +
            "def a(key, value):\n    if key not in _existing:\n        G[key] = {'full': value}\n" + body)


class TestGlossaryLoader(unittest.TestCase):
    def directory(self, files):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        for name, source in files.items():
            # Sources synthétiques exclusivement dans le répertoire de fixture.
            (directory / name).write_text(source, encoding='utf-8')
        return directory

    def priority(self, directory, names):
        manifest = {'schema_version': 1, 'kind': 'internal_glossary_overlay', 'files': [
            {'path': name, 'sha256': hashlib.sha256((directory / name).read_bytes()).hexdigest()}
            for name in names]}
        (directory / m.OVERLAY_PRIORITY_FILE).write_text(json.dumps(manifest), encoding='utf-8')
        return manifest

    def test_ordinary_order_and_final_fusion_are_preserved(self):
        directory = self.directory({
            'cardio_1.py': BASE,
            'z_update.py': "from cardio_1 import a, G\na('SHARED', 'middle')\n",
            'zz_fusion.py': "from cardio_1 import a, G\na('SHARED', 'final arbitration')\n",
            'separate.py': "G = {'SHARED': {'full': 'separate definition'}}\n",
        })
        self.assertEqual(m.load_glossary(directory)['SHARED'], {'full': 'final arbitration'})

    def test_conditionals_never_replace_ordinary_or_previous_additions(self):
        directory = self.directory({
            'cardio_1.py': BASE,
            'a_conditional.py': conditional('a_conditional', "a('SHARED', 'do not replace')\na('NEW', 'first addition')\n"),
            'z_conditional.py': conditional('z_conditional', "a('NEW', 'do not replace either')\na('OTHER', 'second addition')\n"),
        })
        result = m.load_glossary(directory)
        self.assertEqual(result, {'SHARED': {'full': 'base'}, 'NEW': {'full': 'first addition'},
                                  'OTHER': {'full': 'second addition'}})

    def test_shared_conditionals_preserve_keys_from_independent_modules(self):
        directory = self.directory({
            'cardio_1.py': BASE,
            'a_conditional.py': conditional('a_conditional', "a('NEW', 'first addition')\n"),
            'e46.py': conditional('e46', """def ac(key, value):
    if key not in _ex:
        a(key, value)
ac('SHARED', 'do not replace')
ac('NEW', 'do not replace independent addition')
ac('SHARED_NEW', 'shared addition')
""", shared=True),
        })
        result = m.load_glossary(directory)
        self.assertEqual(result['SHARED'], {'full': 'base'})
        self.assertEqual(result['NEW'], {'full': 'first addition'})
        self.assertEqual(result['SHARED_NEW'], {'full': 'shared addition'})

    def test_every_known_discovery_ast_is_replaced_without_running_it(self):
        prefix = ("from pathlib import Path\nimport importlib.util\nimport sys\n_existing = {}\n_ex = set()\n"
                  "_here = Path(__file__).parent\n_gdir = _here\n_dirs = [_here]\n_g = _here\n")
        for source, variable in m._TEMPLATES:
            with self.subTest(variable=variable, template=source.splitlines()[0]):
                directory = self.directory({'item.py': prefix + source.replace('__MEDINA_SELF__', 'item') + "\nG = {'NEW': {'full': 'unchanged'}}\n"})
                with patch.object(importlib, 'import_module', side_effect=AssertionError('Discovery must not run')), \
                        patch.object(importlib.util, 'spec_from_file_location', side_effect=AssertionError('Uncached discovery must not run')):
                    self.assertEqual(m.load_glossary(directory), {'NEW': {'full': 'unchanged'}})

    def test_unknown_dynamic_schema_fails_before_any_module_executes(self):
        directory = self.directory({
            'a_ordinary.py': "import builtins\nbuiltins._medina_test_count += 1\nG = {}\n",
            'unknown.py': "import importlib\nG = importlib.import_module('unknown').G\n",
        })
        with patch.object(builtins, '_medina_test_count', 0, create=True):
            with self.assertRaisesRegex(m.GlossaryLoadError, 'non reconnue'):
                m.load_glossary(directory)
            self.assertEqual(builtins._medina_test_count, 0)

    def test_ancestor_root_discovery_preserves_conditional_keys_without_importing(self):
        discovery = next(source for source, _ in m._TEMPLATES
                         if source.startswith('if _root is not None:'))
        source = ("from pathlib import Path\nimport importlib\nimport sys\n"
                  "_here = Path(__file__).resolve()\n"
                  "_root = next((p for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()), None)\n"
                  "_existing = {}\n" + discovery.replace('__MEDINA_SELF__', 'item') +
                  "\nG = {}\ndef add(key, value):\n"
                  "    if key not in _existing:\n        G[key] = {'full': value}\n"
                  "add('SHARED', 'must not replace')\nadd('NEW', 'root discovery addition')\n")
        directory = self.directory({'cardio_1.py': BASE, 'item.py': source})
        before = sys.path[:]
        with patch.object(importlib, 'import_module', side_effect=AssertionError('Discovery must not run')):
            self.assertEqual(m.load_glossary(directory), {
                'SHARED': {'full': 'base'}, 'NEW': {'full': 'root discovery addition'}})
        self.assertEqual(sys.path, before)

    def test_ancestor_root_discovery_with_extra_effect_is_rejected_before_execution(self):
        discovery = next(source for source, _ in m._TEMPLATES
                         if source.startswith('if _root is not None:'))
        discovery = discovery.replace('    _gdir =', "    print('unexpected side effect')\n    _gdir =")
        directory = self.directory({'item.py': discovery + '\nG = {}\n'})
        with self.assertRaisesRegex(m.GlossaryLoadError, 'non reconnue'):
            m.load_glossary(directory)

    def test_loop_with_extra_effect_is_not_silently_stripped(self):
        source = conditional('item', "a('NEW', 'value')\n")
        source = source.replace('    except Exception:', "        print('unexpected extra operation')\n    except Exception:")
        with self.assertRaisesRegex(m.GlossaryLoadError, 'non reconnue'):
            m.load_glossary(self.directory({'item.py': source}))

    def test_unrecognized_conditional_without_discovery_is_rejected(self):
        with self.assertRaisesRegex(m.GlossaryLoadError, 'schéma inconnu'):
            m.load_glossary(self.directory({'item.py': '_existing = {}\nG = {}\n'}))

    def test_ordinary_import_cycle_fails_fast_with_path(self):
        directory = self.directory({'alpha.py': 'from beta import G\n', 'beta.py': 'from alpha import G\n'})
        with self.assertRaisesRegex(m.GlossaryLoadError, 'alpha → beta → alpha'):
            m.load_glossary(directory)

    def test_shared_import_is_executed_only_once_per_load(self):
        directory = self.directory({
            'a_consumer.py': 'from cardio_1 import G\n',
            'cardio_1.py': "import builtins\nbuiltins._medina_test_count += 1\n" + BASE,
            'z_consumer.py': 'from cardio_1 import G\n',
        })
        with patch.object(builtins, '_medina_test_count', 0, create=True):
            self.assertIn('SHARED', m.load_glossary(directory))
            self.assertEqual(builtins._medina_test_count, 1)

    def test_ambient_module_cache_is_not_reused_or_polluted(self):
        directory = self.directory({'cardio_1.py': BASE, 'a_consumer.py': 'from cardio_1 import G\n'})
        ambient = types.ModuleType('cardio_1')
        ambient.G = {'POISON': 'other checkout'}
        before = set(sys.modules)
        with patch.dict(sys.modules, {'cardio_1': ambient}):
            self.assertEqual(m.load_glossary(directory), {'SHARED': {'full': 'base'}})
            self.assertIs(sys.modules['cardio_1'], ambient)
        self.assertEqual(set(sys.modules), before)

    def test_repeated_loads_and_different_roots_are_isolated(self):
        first = self.directory({'cardio_1.py': BASE})
        second = self.directory({'cardio_1.py': "G = {'OTHER': {'full': 'other checkout'}}\n"})
        self.assertEqual(m.load_glossary(first), m.load_glossary(first))
        self.assertEqual(set(m.load_glossary(second)), {'OTHER'})

    def test_historical_sys_path_changes_are_restored(self):
        source = conditional('item', "a('NEW', 'value')\n")
        source = source.replace('_existing = {}', "import sys\nsys.path.insert(0, 'fixture-path')\n_existing = {}")
        directory = self.directory({'item.py': source})
        before = sys.path[:]
        m.load_glossary(directory)
        self.assertEqual(sys.path, before)

    def test_ordinary_to_conditional_dependency_fails_explicitly(self):
        directory = self.directory({'a_ordinary.py': 'from z_conditional import G\n',
                                    'z_conditional.py': conditional('z_conditional', "a('NEW', 'value')\n")})
        with self.assertRaisesRegex(m.GlossaryLoadError, 'ordinaire importe un ajout conditionnel'):
            m.load_glossary(directory)

    def test_invalid_glossary_does_not_disappear_as_warning(self):
        with self.assertRaisesRegex(m.GlossaryLoadError, 'dictionnaire G'):
            m.load_glossary(self.directory({'item.py': 'G = []\n'}))
        with self.assertRaisesRegex(m.GlossaryLoadError, 'syntaxe invalide'):
            m.load_glossary(self.directory({'item.py': 'G = {\n'}))

    def test_verified_overlay_replays_shared_source_after_late_overwrite(self):
        directory = self.directory({
            'cardio_1.py': BASE,
            'a41.py': "from cardio_1 import a, G\na('SHARED', 'internal draft')\n",
            'zz_fusion.py': "from cardio_1 import a, G\na('SHARED', 'canonical late value')\n",
            'zz_fusion_internal_work.py': 'G = {}\n',
        })
        self.assertEqual(m.load_glossary(directory)['SHARED'], {'full': 'canonical late value'})
        self.priority(directory, ['a41.py'])
        self.assertEqual(m.load_glossary(directory)['SHARED'], {'full': 'internal draft'})

    def test_overlay_replay_order_is_explicit_not_filename_order(self):
        directory = self.directory({'a41.py': "G = {'SHARED': {'full': 'A41 internal'}}\n",
                                    'b24.py': "G = {'SHARED': {'full': 'B24 internal'}}\n"})
        self.priority(directory, ['b24.py', 'a41.py'])
        self.assertEqual(m.load_glossary(directory)['SHARED'], {'full': 'A41 internal'})

    def test_overlay_checksum_failure_precedes_all_module_execution(self):
        directory = self.directory({'a41.py': "import builtins\nbuiltins._medina_test_count += 1\nG = {}\n"})
        manifest = self.priority(directory, ['a41.py'])
        manifest['files'][0]['sha256'] = '0' * 64
        (directory / m.OVERLAY_PRIORITY_FILE).write_text(json.dumps(manifest))
        with patch.object(builtins, '_medina_test_count', 0, create=True):
            with self.assertRaisesRegex(m.GlossaryLoadError, 'Empreinte'):
                m.load_glossary(directory)
            self.assertEqual(builtins._medina_test_count, 0)

    def test_overlay_manifest_rejects_paths_duplicates_and_unknown_schema(self):
        directory = self.directory({'a41.py': 'G = {}\n'})
        original = self.priority(directory, ['a41.py'])
        cases = [
            {**original, 'schema_version': True},
            {**original, 'extra': 'not allowed'},
            {**original, 'files': []},
            {**original, 'files': original['files'] * 2},
            {**original, 'files': [{**original['files'][0], 'path': '../a41.py'}]},
            {**original, 'files': [{**original['files'][0], 'path': 'cardio_1.py'}]},
            {**original, 'files': [{**original['files'][0], 'path': 'b24.py'}]},
        ]
        for manifest in cases:
            with self.subTest(manifest=manifest):
                (directory / m.OVERLAY_PRIORITY_FILE).write_text(json.dumps(manifest))
                with self.assertRaises(m.GlossaryLoadError):
                    m.load_glossary(directory)

    def test_overlay_rejects_symlink_manifest_and_symlink_priority_source(self):
        directory = self.directory({'a41.py': 'G = {}\n'})
        self.priority(directory, ['a41.py'])
        sidecar = directory / m.OVERLAY_PRIORITY_FILE
        saved = directory / 'saved-manifest.json'
        sidecar.rename(saved)
        sidecar.symlink_to(saved)
        with self.assertRaisesRegex(m.GlossaryLoadError, 'fichier local réel'):
            m.load_glossary(directory)
        sidecar.unlink()
        saved.rename(sidecar)
        source = directory / 'a41.py'
        real_source = directory / 'real-source.data'
        source.rename(real_source)
        source.symlink_to(real_source)
        with self.assertRaisesRegex(m.GlossaryLoadError, 'non locale'):
            m.load_glossary(directory)

    def test_internal_work_filename_never_authorizes_arbitrary_exec(self):
        directory = self.directory({'a41.py': 'G = {}\n',
                                    'zz_fusion_internal_work.py': "G = {}\nexec(compile('G = {}', 'arbitrary', 'exec'))\n"})
        self.priority(directory, ['a41.py'])
        with self.assertRaisesRegex(m.GlossaryLoadError, 'non reconnue'):
            m.load_glossary(directory)

    def test_repository_glossary_sources_are_never_rewritten(self):
        directory = ROOT / 'glossary'
        files = sorted(directory.glob('*.py'))
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
        result = m.load_glossary(directory)
        self.assertGreater(len(result), 0)
        self.assertEqual(before, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in files})


if __name__ == '__main__':
    unittest.main()
