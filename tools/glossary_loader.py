"""Charge les glossaires sans leur découverte récursive, sans modifier les sources.

Les modules ordinaires conservent leur ordre alphabétique et leurs imports locaux
partagés (notamment cardio_1 et l'arbitrage final zz_fusion). Ils sont exécutés une
seule fois par chargement. Les ajouts explicitement conditionnels viennent ensuite
par ordre alphabétique ; ils ne remplacent jamais une clé déjà présente.

Seules les boucles de découverte dont l'AST correspond exactement aux schémas
historiques ci-dessous sont remplacées EN MÉMOIRE par un jeu figé de clés. Les
définitions, appels d'enregistrement et fichiers d'origine restent intacts. Un
schéma dynamique inconnu ou un cycle ordinaire provoque une erreur explicite.
Ce chargeur n'évalue ni l'exactitude clinique ni la complétude des définitions.
"""
import ast
import builtins
from pathlib import Path
import sys
import types


class GlossaryLoadError(RuntimeError):
    pass


_UPDATE = "_existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))"


def _path_loop(expression, guarded=True):
    statement = ('try:\n        ' + _UPDATE + '\n    except Exception:\n        pass'
                 if guarded else _UPDATE)
    return (f"for _path in sorted({expression}.glob('*.py')):\n"
            "    if _path.stem in {'__MEDINA_SELF__', '__init__'}:\n"
            "        continue\n    " + statement)


def _indent(text, count=4):
    return '\n'.join(' ' * count + line for line in text.splitlines())


_TEMPLATES = [
    (_path_loop('Path(__file__).parent', False), '_existing'),
    (_path_loop('Path(__file__).parent'), '_existing'),
    (_path_loop('_gdir'), '_existing'),
    ("for _d in _dirs:\n"
     "    if str(_d) not in sys.path:\n"
     "        sys.path.append(str(_d))\n" + _indent(_path_loop('_d')), '_existing'),
    ("if _gdir is not None:\n"
     "    if str(_gdir) not in sys.path:\n"
     "        sys.path.insert(0, str(_gdir))\n" + _indent(_path_loop('_gdir')), '_existing'),
    ("if _g is not None:\n"
     "    sys.path.insert(0, str(_g))\n" + _indent(_path_loop('_g')), '_existing'),
    ("""for _dir in (Path(__file__).resolve().parent, Path(__file__).resolve().parents[8] / 'glossary' if len(Path(__file__).resolve().parents) > 8 else None):
    if _dir is None or not _dir.is_dir():
        continue
    for _path in sorted(_dir.glob('*.py')):
        if _path.stem in {'__MEDINA_SELF__', '__init__'}:
            continue
        try:
            _spec = importlib.util.spec_from_file_location('_g_' + _path.stem, _path)
            _mod = importlib.util.module_from_spec(_spec)
            _spec.loader.exec_module(_mod)
            _existing.update(getattr(_mod, 'G', {}))
        except Exception:
            pass""", '_existing'),
    ("""for _p in sorted(Path(__file__).parent.glob('*.py')):
    if _p.stem in {'__MEDINA_SELF__', '__init__', 'cardio_1'}:
        continue
    try:
        _ex |= set(getattr(importlib.import_module(_p.stem), 'G', {}))
    except Exception:
        pass""", '_ex'),
]
_PATTERNS = {ast.dump(ast.parse(source).body[0]): variable for source, variable in _TEMPLATES}
_DYNAMIC_CALLS = {'import_module', 'spec_from_file_location', 'module_from_spec', 'exec_module',
                  '__import__', 'eval', 'exec', 'compile'}


class _SelfName(ast.NodeTransformer):
    def __init__(self, stem):
        self.stem = stem

    def visit_Constant(self, node):
        if node.value == self.stem:
            return ast.copy_location(ast.Constant('__MEDINA_SELF__'), node)
        return node


def _has_dynamic_call(node):
    return any(isinstance(child, ast.Call) and
               ((isinstance(child.func, ast.Attribute) and child.func.attr in _DYNAMIC_CALLS) or
                (isinstance(child.func, ast.Name) and child.func.id in _DYNAMIC_CALLS))
               for child in ast.walk(node))


def _prepare(path):
    try:
        tree = ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    except (OSError, SyntaxError) as exc:
        raise GlossaryLoadError(f'Glossaire illisible ou syntaxe invalide : {path.name}') from exc
    conditional = None
    for index, node in enumerate(tree.body):
        if not _has_dynamic_call(node):
            continue
        # La normalisation porte uniquement sur le nom propre du fichier ; elle
        # ne tolère aucune autre différence avec la boucle attestée.
        import copy
        normalized = _SelfName(path.stem).visit(copy.deepcopy(node))
        variable = _PATTERNS.get(ast.dump(normalized))
        if variable is None or conditional is not None:
            raise GlossaryLoadError(f'Découverte dynamique de glossaires non reconnue : {path.name}')
        conditional = variable
        replacement = ast.Assign(targets=[ast.Name(id=variable, ctx=ast.Store())],
                                 value=ast.Name(id='__medina_existing_keys__', ctx=ast.Load()))
        tree.body[index] = ast.copy_location(replacement, node)
    if conditional is None and any(isinstance(node, ast.Name) and node.id in ('_existing', '_ex')
                                   for node in ast.walk(tree)):
        raise GlossaryLoadError(f'Ajout conditionnel de schéma inconnu : {path.name}')
    return compile(ast.fix_missing_locations(tree), str(path), 'exec'), conditional


def load_glossary(directory):
    directory = Path(directory).resolve()
    paths = sorted(path for path in directory.glob('*.py') if path.stem != '__init__')
    if not paths:
        raise GlossaryLoadError(f'Aucun glossaire Python dans {directory}')
    prepared = {path.stem: _prepare(path) for path in paths}
    files = {path.stem: path for path in paths}
    modules, loading, result = {}, [], {}
    phase = 'ordinary'

    def local_import(name, globals=None, locals=None, fromlist=(), level=0):
        if level == 0 and name in prepared:
            return load(name)
        return builtins.__import__(name, globals, locals, fromlist, level)

    def load(name):
        if name in loading:
            raise GlossaryLoadError('Cycle d’import de glossaires : ' + ' → '.join(loading + [name]))
        if name in modules:
            return modules[name]
        code, conditional = prepared[name]
        if conditional and phase == 'ordinary':
            raise GlossaryLoadError(f'Un glossaire ordinaire importe un ajout conditionnel : {name}')
        module = types.ModuleType(name)
        module.__file__ = str(files[name])
        module.__dict__['__builtins__'] = {**vars(builtins), '__import__': local_import}
        module.__dict__['__medina_existing_keys__'] = frozenset(result)
        loading.append(name)
        try:
            exec(code, module.__dict__)
            if not isinstance(getattr(module, 'G', None), dict):
                raise GlossaryLoadError(f'Le glossaire {name} n’exporte pas de dictionnaire G')
        except GlossaryLoadError:
            raise
        except Exception as exc:
            raise GlossaryLoadError(f'Échec du chargement du glossaire {name}: {type(exc).__name__}') from exc
        finally:
            loading.pop()
        modules[name] = module
        return module

    # Certains anciens préambules modifient sys.path pour retrouver cardio_1.
    # Le chargeur route les imports locaux lui-même et restaure ces modifications.
    previous_path = sys.path[:]
    try:
        for name, (_, conditional) in prepared.items():
            if not conditional:
                load(name)
        for name, (_, conditional) in prepared.items():
            if not conditional:
                result.update(modules[name].G)
        phase = 'conditional'
        for name, (_, conditional) in prepared.items():
            if conditional:
                module = load(name)
                for key, value in module.G.items():
                    result.setdefault(key, value)
        return result
    finally:
        sys.path[:] = previous_path
