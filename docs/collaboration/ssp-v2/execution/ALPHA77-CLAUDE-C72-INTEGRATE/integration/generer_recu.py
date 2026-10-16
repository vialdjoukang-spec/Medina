"""Reçu Alpha C72 (mission ALPHA77-CLAUDE-C72-INTEGRATE) — Agent P.

Modèle : docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-G45-INTEGRATE/integration/generer_recu.py.

Étape 1 : python3 <ce fichier> preparer
  copie les sept fichiers finaux dans livraison/ et écrit droits/inventaire_images.json.
  C72 n'ajoute aucune image Alpha (assets/img/c72/alpha/claude/ n'existe pas) et la leçon ne
  référence aucune image raster : ses figures sont des schémas SVG en ligne, non anatomiques.
  Les figures 1 et 3 (anatomie dessinée par IA) ont été retirées sans remplacement (MAJ-06).
Étape 2 (après commit de l'étape 1) : python3 <ce fichier> recu
  écrit organisation/alpha-publications/Claude/C72/0001.json avec source_commit = HEAD.
Le reçu n'est valide que si revue/MED.json, LANG.json et SEMIO.json portent les empreintes
des fichiers finaux (reviewed_files_sha256). Revue IA, distincte d'une validation médicale humaine.
"""
import hashlib, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
MID = 'ALPHA77-CLAUDE-C72-INTEGRATE'
M = f'docs/collaboration/ssp-v2/execution/{MID}'
BASE = '523832d9ef6097607d3443f4398deee9cd0add11'
CORE = [f'chapters/C72/C72_{x}.html' for x in ('a', 'b', 'c', 'd', 'pop1', 'pop2')] + ['glossary/c72.py']
NOTE = ('Aucune image Alpha : la leçon ne contient que des schémas SVG en ligne, non anatomiques. '
        'Les figures 1 et 3, anatomie dessinée par IA, ont été retirées sans remplacement (décision de Vial) ; '
        'la discipline Anatomie reste sans figure, lacune déclarée (original réel à sourcer). '
        'Revue IA, distincte d’une validation médicale humaine.')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def git_show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def dump(path, obj):
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def sans_image():
    for target in CORE:
        if target.endswith('.html'):
            text = (ROOT / target).read_text(encoding='utf-8')
            assert not re.search(r'<img\b|assets/img/', text), 'image raster inattendue : ' + target
    assert not (ROOT / 'assets/img/c72/alpha/claude').exists(), 'actif Alpha inattendu'


def preparer():
    sans_image()
    for target in CORE:
        dest = ROOT / M / 'livraison' / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / target, dest)
    dump(f'{M}/droits/inventaire_images.json', dict(
        schema_version=1, mission=MID, code='C72', base_commit=BASE, alpha_assets=[], images=[],
        note=('Aucune image raster ni actif Alpha dans les sept fichiers finaux ; figures en SVG en ligne, '
              'non anatomiques. Figures anatomiques dessinées par IA retirées (MAJ-06).')))
    print('préparation écrite (livraison/, droits/inventaire_images.json)')


def recu():
    src = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    sans_image()
    files = {}
    for target in CORE:
        prev = git_show(BASE, target)
        ref = dict(previous_sha256=hashlib.sha256(prev).hexdigest() if prev is not None else None,
                   sha256=sha(f'{M}/livraison/{target}'), source_path=f'{M}/livraison/{target}')
        assert ref['sha256'] == sha(target), 'livraison différente du fichier final : ' + target
        files[target] = ref
    audits = {k: dict(path=f'{M}/revue/{k}.json', sha256=sha(f'{M}/revue/{k}.json')) for k in ('MED', 'LANG', 'SEMIO')}
    final = {t: r['sha256'] for t, r in files.items()}
    for k in audits:
        report = json.loads((ROOT / audits[k]['path']).read_text(encoding='utf-8'))
        assert report['reviewed_files_sha256'] == final, 'revue non liée aux fichiers finaux : ' + k
    receipt = dict(schema_version=1, actor='Claude', code='C72', fragment='S08', phase='completed',
                   medical_human_validation=False, base_commit=BASE, source_commit=src, mission=MID,
                   previous_receipt_sha256=None, files=files, audits=audits, note=NOTE)
    dump('organisation/alpha-publications/Claude/C72/0001.json', receipt)
    print('reçu écrit, source_commit', src)


if __name__ == '__main__':
    {'preparer': preparer, 'recu': recu}[sys.argv[1]]()
