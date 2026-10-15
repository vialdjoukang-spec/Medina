"""Transactional injection fixtures, without real course content or network."""
import copy
import hashlib
import json
import os
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import betta_cycle as G
from tools import betta_injecter as I
from tools import publication_en_etat as P
from tests import test_betta_cycle as fixtures
from tests.test_betta_cycle import encode, lesson


class Novo12InjectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='medina-novo-injection-test-')
        self.root = Path(self.tmp.name)
        self.fixture = fixtures.Novo12GuardTests(); self.fixture.setUp(); self.fixture.inject()
        self.files = self.fixture.files
        for row in self.fixture.status['cycles']['42']['lessons'].values():
            row['state'] = 'LIVRE'
            for path in row.pop('canonical'):
                self.files.pop(path)
        self.fixture.status['cycles']['42']['state'] = 'LIVRE'
        self.files['chapters.json'] = b'[]'
        self.files['nosology/integrity.json'] = encode({'chapters.json': hashlib.sha256(b'[]').hexdigest()})
        self.flush()
        (self.root / 'chapters').mkdir()
        (self.root / 'glossary').mkdir()
        self.root_patch = patch.object(I, 'ROOT', self.root); self.root_patch.start()

    def tearDown(self):
        self.root_patch.stop(); self.tmp.cleanup()

    def flush(self):
        self.fixture.save()
        for path, raw in self.files.items():
            destination = self.root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def assert_refused_without_changes(self, selected):
        before = self.snapshot()
        with self.assertRaises(SystemExit):
            I.main(selected, novo=True)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse(any((self.root / 'chapters').iterdir()))
        self.assertFalse(any((self.root / 'glossary').iterdir()))

    def adopt_r25_with_real_provenance(self):
        source = self.fixture.row()['dir'] + '/chapters/R25/R25_a.html'
        canonical = 'chapters/R25/R25_a.html'
        self.files[canonical] = self.files[source]
        self.fixture.status['cycles']['42']['lessons']['R25'] = 'A_FAIRE'
        rows = [dict(code='R25', title='Existing technical fixture', owner='S08', covers=['R25'],
                     integrated=True, publication_mode='en_etat', provisional_injection=True,
                     audit_deferred='non_realise')]
        self.files['chapters.json'] = encode(rows)
        self.files[P.AUTHORITY] = (Path(I.__file__).resolve().parents[1] / P.AUTHORITY).read_bytes()
        self.files['nosology/fragments/S08.json'] = encode({'lessons': [{'code': 'R25'}]})
        self.flush()
        def git(*args):
            return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()
        git('init', '-q'); git('config', 'user.name', 'Technical fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        git('add', '.'); git('-c', 'core.hooksPath=/dev/null', 'commit', '-qm', 'Actual provenance fixture')
        self.files[P.RECEIPT] = encode(dict(schema_version=1, actor='Codex', authority=P.AUTHORITY,
            authority_sha256=P.digest(self.files[P.AUTHORITY]), medical_human_validation=False,
            catalog_sha256=P.digest(self.files['chapters.json']), catalog_entries=rows,
            courses=[dict(code='R25', fragment_id='S08', files={canonical: dict(
                sha256=P.digest(self.files[canonical]), provenance_path=source,
                provenance_revision=git('rev-parse', 'HEAD'))})]))
        self.flush()
        return canonical, rows[0]

    def test_mixed_batch_preserves_real_adoption_without_promoting_its_status(self):
        canonical, adopted_row = self.adopt_r25_with_real_provenance()
        original = (self.root / canonical).read_bytes()
        I.main({'R25', 'E63'}, novo=True)
        self.assertEqual((self.root / canonical).read_bytes(), original)
        rows = json.loads((self.root / 'chapters.json').read_bytes())
        self.assertEqual(rows[0], adopted_row)
        self.assertEqual([r['code'] for r in rows], ['R25', 'E63'])
        state = json.loads((self.root / G.NOVO_STATUS).read_bytes())
        self.assertEqual(state['cycles']['42']['lessons']['R25'], 'A_FAIRE')
        self.assertEqual(state['cycles']['42']['lessons']['E63']['state'], 'INJECTE')
        self.assertEqual(state['cycles']['42']['state'], 'EN_COURS')
        tree = I._Tree(self.snapshot())
        self.assertEqual(P.adopted_codes(tree), {'R25'})
        before = I._Tree(self.files)
        self.assertEqual(G.validate(before, tree, publication_in_state_codes=P.adopted_codes(tree))[1], {'R25', 'E63'})

    def test_mixed_batch_rechecks_real_provenance_before_copy(self):
        canonical, _ = self.adopt_r25_with_real_provenance()
        receipt = json.loads((self.root / P.RECEIPT).read_bytes())
        receipt['courses'][0]['files'][canonical]['provenance_revision'] = 'f' * 40
        (self.root / P.RECEIPT).write_bytes(encode(receipt))
        before = self.snapshot()
        with self.assertRaises(SystemExit): I.main({'E63'}, novo=True)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / 'chapters/E63').exists())

    def test_catalogue_flag_without_verified_receipt_never_skips_a_lesson(self):
        canonical, _ = self.adopt_r25_with_real_provenance()
        (self.root / P.RECEIPT).unlink()
        before = self.snapshot()
        with self.assertRaises(SystemExit):
            I.main({'E63'}, novo=True)
        self.assertEqual(self.snapshot(), before)
        self.assertTrue((self.root / canonical).exists())
        self.assertFalse((self.root / 'chapters/E63').exists())

    def test_full_declared_batch_is_compatible_with_pr99(self):
        I.main(set(), novo=True)
        rows = json.loads((self.root / 'chapters.json').read_text())
        self.assertEqual([r['code'] for r in rows], ['R25', 'E63'])
        self.assertTrue(all(r['novo12'] and r['production_cycle'] == 42 and r['audit_status'] == 'audit_differe_non_effectue' for r in rows))
        state = json.loads((self.root / G.NOVO_STATUS).read_text())
        self.assertEqual(state['cycles']['42']['state'], 'INJECTE')
        for code, row in state['cycles']['42']['lessons'].items():
            for path, digest in row['canonical'].items():
                self.assertEqual(hashlib.sha256((self.root / path).read_bytes()).hexdigest(), digest)
        integrity = json.loads((self.root / 'nosology/integrity.json').read_text())
        self.assertEqual(integrity['chapters.json'], hashlib.sha256((self.root / 'chapters.json').read_bytes()).hexdigest())

    def test_partial_or_unknown_selection_never_copies(self):
        for selected in ({'R25'}, {'UNKNOWN'}):
            with self.subTest(selected=selected): self.assert_refused_without_changes(selected)

    def test_missing_popup_never_copies_any_lesson(self):
        path = self.fixture.row('E63')['dir'] + '/chapters/E63/E63_pop2.html'
        (self.root / path).unlink()
        self.assert_refused_without_changes(set())

    def test_missing_manifest_never_copies(self):
        self.fixture.row().pop('files'); self.flush()
        self.assert_refused_without_changes(set())

    def test_changed_source_never_copies(self):
        path = self.fixture.row('E63')['dir'] + '/rapport.md'
        (self.root / path).write_text('changed after source manifest')
        self.assert_refused_without_changes(set())

    def test_truth_failure_never_copies(self):
        path = self.fixture.row('E63')['dir'] + '/recherche.md'
        self.files[path] = b'No matrix in this fixture'
        self.fixture.row('E63')['files'][path] = hashlib.sha256(self.files[path]).hexdigest()
        self.flush()
        self.assert_refused_without_changes(set())

    def test_corrupt_integrity_is_detected_before_copy(self):
        (self.root / 'nosology/integrity.json').write_text('{')
        self.assert_refused_without_changes(set())

    def test_existing_covered_code_never_overwritten(self):
        (self.root / 'chapters.json').write_bytes(encode([{'code': 'R29', 'covers': ['R25']}]))
        self.assert_refused_without_changes(set())

    def test_symlink_source_never_copies(self):
        path = self.root / self.fixture.row()['dir'] / 'rapport.md'
        target = path.with_name('external.txt'); target.write_text('fixture linked file')
        path.unlink(); path.symlink_to(target)
        self.assert_refused_without_changes(set())

    def test_not_all_lessons_livre_never_copies(self):
        self.fixture.status['cycles']['42']['lessons']['E63'] = 'A_FAIRE'; self.flush()
        self.assert_refused_without_changes(set())

    def test_multiple_ready_cycles_never_copy(self):
        self.fixture.plan['last'] = 43; self.fixture.plan['total_lessons'] = 3
        l = lesson('E64', 'S05', 'E-06-Endocrinologie et métabolisme')
        self.fixture.plan['cycles'].append({'number': 43, 'lessons': 1, 'agents': [
            {'fragment': l['fragment'], 'label': l['label'], 'lessons': [l]}]})
        self.fixture.status['cycles']['43'] = {'state': 'LIVRE', 'lessons': {'E64': {'state': 'LIVRE'}}}
        self.flush()
        self.assert_refused_without_changes(set())

    def test_io_failure_rolls_back_new_sources_and_metadata(self):
        before = self.snapshot()
        link = os.link
        def transient_failure(source, destination, **kwargs):
            if Path(source).parts[-2:] == ('new', 'chapters.json'):
                raise OSError('fixture single I/O failure')
            return link(source, destination, **kwargs)
        with patch.object(I.os, 'link', side_effect=transient_failure), self.assertRaises(OSError):
            I.main(set(), novo=True)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse(any((self.root / 'chapters').iterdir()))
        self.assertFalse(any((self.root / 'glossary').iterdir()))

    def test_rollback_preserves_a_concurrent_added_file(self):
        original_status = (self.root / G.NOVO_STATUS).read_bytes()
        link = os.link
        def concurrent_write_and_failure(source, destination, **kwargs):
            if Path(source).parts[-2:] == ('new', 'chapters.json'):
                (self.root / 'chapters/R25/concurrent.txt').write_text('another producer owns this')
                raise OSError('fixture I/O failure after concurrent write')
            return link(source, destination, **kwargs)
        with patch.object(I.os, 'link', side_effect=concurrent_write_and_failure), \
                self.assertRaisesRegex(RuntimeError, 'travail concurrent préservé'):
            I.main(set(), novo=True)
        self.assertEqual((self.root / 'chapters/R25/concurrent.txt').read_text(), 'another producer owns this')
        self.assertEqual((self.root / G.NOVO_STATUS).read_bytes(), original_status)
        self.assertFalse((self.root / 'chapters/R25/R25_a.html').exists())
        self.assertFalse((self.root / 'chapters/E63').exists())

    def test_stale_preparation_preserves_changed_plan_source_and_metadata(self):
        for changed in (G.NOVO_PLAN, 'chapters.json', self.fixture.row()['dir'] + '/rapport.md'):
            with self.subTest(changed=changed):
                prepared = I._novo_prepare(set(), self.fixture.plan, self.fixture.status, [])
                path = self.root / changed
                original = path.read_bytes()
                path.write_bytes(original + b' concurrent change')
                before = self.snapshot()
                with self.assertRaisesRegex(RuntimeError, 'modifiées pendant la préparation'):
                    I._novo_commit(prepared)
                self.assertEqual(self.snapshot(), before)
                path.write_bytes(original)

    def test_new_glossary_created_after_initial_check_is_not_overwritten(self):
        link = os.link
        path = self.root / 'glossary/r25.py'
        def concurrent_source(source, destination, **kwargs):
            if Path(destination) == path and not path.exists():
                path.write_text('concurrent glossary')
            return link(source, destination, **kwargs)
        with patch.object(I.os, 'link', side_effect=concurrent_source), self.assertRaises(FileExistsError):
            I.main(set(), novo=True)
        self.assertEqual(path.read_text(), 'concurrent glossary')
        self.assertFalse((self.root / 'chapters/R25').exists())

    def test_metadata_changed_just_before_capture_is_restored_unchanged(self):
        rename = os.rename
        path = self.root / G.NOVO_STATUS
        original_catalog = (self.root / 'chapters.json').read_bytes()
        def concurrent_metadata(source, destination):
            if Path(source) == path:
                path.write_text('concurrent status before capture')
            return rename(source, destination)
        with patch.object(I.os, 'rename', side_effect=concurrent_metadata), \
                self.assertRaisesRegex(RuntimeError, 'Métadonnées modifiées'):
            I.main(set(), novo=True)
        self.assertEqual(path.read_text(), 'concurrent status before capture')
        self.assertEqual((self.root / 'chapters.json').read_bytes(), original_catalog)
        self.assertFalse(any((self.root / 'chapters').iterdir()))

    def test_metadata_recreated_after_capture_is_preserved_with_original_backup(self):
        link = os.link
        path = self.root / 'chapters.json'
        original = path.read_bytes()
        def concurrent_metadata(source, destination, **kwargs):
            if Path(source).parts[-2:] == ('new', 'chapters.json'):
                path.write_text('concurrent catalogue recreated during commit')
            return link(source, destination, **kwargs)
        with patch.object(I.os, 'link', side_effect=concurrent_metadata), \
                self.assertRaisesRegex(RuntimeError, 'sauvegardes'):
            I.main(set(), novo=True)
        self.assertEqual(path.read_text(), 'concurrent catalogue recreated during commit')
        saved = list(self.root.glob('.novo-injection-*/original-*'))
        self.assertTrue(any(p.read_bytes() == original for p in saved))
        self.assertFalse(any((self.root / 'chapters').iterdir()))

    def test_rollback_captures_concurrent_edit_instead_of_unlinking_it(self):
        link, rename = os.link, os.rename
        path = self.root / 'chapters/R25/R25_a.html'
        def failure(source, destination, **kwargs):
            if Path(source).parts[-2:] == ('new', 'chapters.json'):
                raise OSError('trigger rollback')
            return link(source, destination, **kwargs)
        def concurrent_edit(source, destination):
            if Path(source) == path:
                path.write_text('concurrent source at rollback capture')
            return rename(source, destination)
        with patch.object(I.os, 'link', side_effect=failure), \
                patch.object(I.os, 'rename', side_effect=concurrent_edit), \
                self.assertRaisesRegex(RuntimeError, 'travail concurrent préservé'):
            I.main(set(), novo=True)
        self.assertEqual(path.read_text(), 'concurrent source at rollback capture')

    def test_no_ready_lesson_is_a_non_mutating_noop(self):
        self.fixture.status['cycles']['42']['lessons'] = {'R25': 'A_FAIRE', 'E63': 'A_FAIRE'}; self.flush()
        before = self.snapshot(); I.main(set(), novo=True)
        self.assertEqual(self.snapshot(), before)

    def test_legacy_injector_refuses_explicitly_transferred_missions(self):
        before = self.snapshot()
        with self.assertRaisesRegex(SystemExit, 'transférées'):
            I.main({'R25'}, novo=False)
        self.assertEqual(self.snapshot(), before)

    def test_explicit_other_legacy_code_is_not_blocked_by_transferred_livre(self):
        old_plan = json.loads((self.root / G.PLAN).read_text())
        old_plan['cycles'].insert(0, {'number': 41, 'agents': [{'lessons': [lesson('G96')]}]})
        source = 'livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_41_G96'
        self.fixture.legacy['cycles']['41'] = {'state': 'LIVRE', 'lessons': {
            'G96': {'state': 'LIVRE', 'dir': source}}}
        self.fixture.legacy['cycles']['42']['lessons']['R25'] = {'state': 'LIVRE', 'dir': 'not-selected'}
        self.files[G.PLAN] = encode(old_plan)
        self.files[source + '/rapport.md'] = b'Legacy technical fixture'
        self.files[source + '/glossary/g96.py'] = b'G = {}'
        for suffix in 'abcd':
            self.files[source + f'/chapters/G96/G96_{suffix}.html'] = b'<!-- Technical fixture -->'
        self.flush()
        I.main({'G96'}, novo=False)
        self.assertTrue((self.root / 'chapters/G96/G96_a.html').is_file())
        self.assertFalse((self.root / 'chapters/R25').exists())
        state = json.loads((self.root / G.STATUS).read_text())
        self.assertEqual(state['cycles']['42']['lessons']['R25']['state'], 'LIVRE')


class LegacyInjectionCompatibilityTests(unittest.TestCase):
    def test_ordinary_betta_delivery_keeps_historical_contract(self):
        with tempfile.TemporaryDirectory(prefix='medina-legacy-injection-test-') as temporary:
            root = Path(temporary); code = 'G96'
            source = 'livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_41_G96'
            l = lesson(code)
            files = {G.PLAN: encode({'cycles': [{'number': 41, 'agents': [{'lessons': [l]}]}]}),
                     G.STATUS: encode({'cycles': {'41': {'state': 'LIVRE', 'lessons': {code: {'state': 'LIVRE', 'dir': source}}}}}),
                     'chapters.json': b'[]', 'nosology/integrity.json': b'{}',
                     source + '/rapport.md': b'Historical technical fixture',
                     source + '/glossary/g96.py': b'G = {}'}
            files.update({source + f'/chapters/G96/G96_{s}.html': b'<!-- Technical fixture -->' for s in 'abcd'})
            for path, raw in files.items():
                p = root / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(raw)
            (root / 'chapters').mkdir(); (root / 'glossary').mkdir()
            with patch.object(I, 'ROOT', root): I.main(set(), novo=False)
            self.assertEqual(json.loads((root / 'chapters.json').read_text())[0]['betta'], True)
            self.assertTrue((root / 'chapters/G96/G96_a.html').is_file())


if __name__ == '__main__':
    unittest.main()
