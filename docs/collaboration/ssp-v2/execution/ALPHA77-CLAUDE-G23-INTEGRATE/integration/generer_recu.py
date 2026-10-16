"""Reçu Alpha G23 (mission ALPHA77-CLAUDE-G23-INTEGRATE) — Agent P.

Modèle : docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-G45-INTEGRATE/integration/generer_recu.py.

Étape 1 : python3 <ce fichier> preparer
  copie les sept fichiers finaux dans livraison/ et écrit droits/inventaire_images.json.
  G23 ne contient aucune image raster et n'ajoute aucune image Alpha (assets/img/g23/alpha/claude/
  absent) : ses figures sont des schémas SVG non anatomiques intégrés au HTML. L'inventaire de
  droits le vérifie (aucune balise <img> dans les sept fichiers finaux).
Étape 2 (après commit de l'étape 1) : python3 <ce fichier> recu
  écrit organisation/alpha-publications/Claude/G23/0001.json avec source_commit = HEAD.
Le reçu n'est valide que si revue/MED.json, LANG.json et SEMIO.json portent les empreintes
des fichiers finaux (reviewed_files_sha256). Revue IA, distincte d'une validation médicale humaine.
"""
import hashlib, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
MID = 'ALPHA77-CLAUDE-G23-INTEGRATE'
M = f'docs/collaboration/ssp-v2/execution/{MID}'
BASE = '523832d9ef6097607d3443f4398deee9cd0add11'
CORE = [f'chapters/G23/G23_{x}.html' for x in ('a', 'b', 'c', 'd', 'pop1', 'pop2')] + ['glossary/g23.py']
NOTE = ('Aucune image raster ni image Alpha : figures en SVG non anatomiques, aucune retirée '
        '(aucune classée ANATOMIQUE_IA) ; réserve LANG sur la provenance des figures 4 et 5. '
        'Lacunes déclarées : rubrique 16 (spécificités suisses), prise en charge urologique sans source '
        'suisse ou européenne lue. Revue IA, distincte d’une validation médicale humaine.')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def git_show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def dump(path, obj):
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def inventaire():
    rows = []
    for target in CORE:
        if target.endswith('.html'):
            text = (ROOT / target).read_text(encoding='utf-8')
            assert not re.search(r'<img\b', text), 'image raster inattendue : ' + target
            rows.append(dict(fichier=target, img=0, svg=len(re.findall(r'<svg\b', text))))
    assert not (ROOT / 'assets/img/g23/alpha/claude').exists() or not any((ROOT / 'assets/img/g23/alpha/claude').iterdir())
    return rows


def preparer():
    for target in CORE:
        dest = ROOT / M / 'livraison' / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / target, dest)
    dump(f'{M}/droits/inventaire_images.json', dict(
        schema_version=1, mission=MID, code='G23', base_commit=BASE, alpha_assets=[],
        note=('Aucune image raster dans les sept fichiers finaux ; figures en SVG non anatomiques '
              'intégrées au HTML, sans actif à inclure dans le reçu (tools/alpha_publication.py).'),
        fichiers=inventaire()))
    print('préparation écrite (livraison/, droits/inventaire_images.json)')


def recu():
    src = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    inventaire()
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
    receipt = dict(schema_version=1, actor='Claude', code='G23', fragment='S08', phase='completed',
                   medical_human_validation=False, base_commit=BASE, source_commit=src, mission=MID,
                   previous_receipt_sha256=None, files=files, audits=audits, note=NOTE)
    dump('organisation/alpha-publications/Claude/G23/0001.json', receipt)
    print('reçu écrit, source_commit', src)


if __name__ == '__main__':
    {'preparer': preparer, 'recu': recu}[sys.argv[1]]()
