"""Reçu Alpha G45 (mission ALPHA77-CLAUDE-G45-INTEGRATE) — Agent W.

Modèle : docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-D50-INTEGRATE/integration/generer_recu.py.

Étape 1 : python3 <ce fichier> preparer
  copie les sept fichiers finaux dans livraison/ et écrit droits/inventaire_images.json.
  G45 n'ajoute aucune image Alpha (assets/img/g45/alpha/claude/ est vide) : ses neuf figures
  raster sont des images publiées existantes (assets/img/cycle2/g45/), inchangées depuis la base,
  déjà inventoriées par l'Agent P (prep/figures.json). tools/alpha_publication.py n'accepte dans un
  reçu que les actifs assets/img/g45/alpha/claude/ : ces images ne figurent donc pas dans le reçu.
  L'inventaire de droits vérifie seulement que leurs octets sont identiques à la base et à
  l'inventaire de P.
Étape 2 (après commit de l'étape 1) : python3 <ce fichier> recu
  écrit organisation/alpha-publications/Claude/G45/0001.json avec source_commit = HEAD.
Le reçu n'est valide que si revue/MED.json, LANG.json et SEMIO.json portent les empreintes
des fichiers finaux (reviewed_files_sha256). Revue IA, distincte d'une validation médicale humaine.
"""
import hashlib, json, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
MID = 'ALPHA77-CLAUDE-G45-INTEGRATE'
M = f'docs/collaboration/ssp-v2/execution/{MID}'
BASE = 'abd681e5175db8c89e87dd7b83f96d0249d81cd7'
CORE = [f'chapters/G45/G45_{x}.html' for x in ('a', 'b', 'c', 'd', 'pop1', 'pop2')] + ['glossary/g45.py']
NOTE = ('Aucune image Alpha nouvelle : les neuf figures publiées existantes (assets/img/cycle2/g45/) '
        'sont inchangées et inventoriées dans prep/figures.json. '
        'Revue IA, distincte d’une validation médicale humaine.')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def git_show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def dump(path, obj):
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def inventaire():
    figs = json.loads((ROOT / M / 'prep/figures.json').read_text(encoding='utf-8'))['figures']
    rows = []
    for f in figs:
        asset = f['image']
        prev = git_show(BASE, asset)
        current = sha(asset)
        assert prev is not None and hashlib.sha256(prev).hexdigest() == current, 'image modifiée depuis la base : ' + asset
        assert f['sha256'] == current, 'image différente de l’inventaire de P : ' + asset
        rows.append(dict(figure=f['figure'], image=asset, sha256=current, unchanged_since_base=True,
                         classe=f.get('classe'), page=f.get('page'), auteur=f.get('auteur'),
                         licence=f.get('licence'), licence_url=f.get('licence_url'),
                         inventaire='prep/figures.json'))
    return rows


def preparer():
    for target in CORE:
        dest = ROOT / M / 'livraison' / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / target, dest)
    dump(f'{M}/droits/inventaire_images.json', dict(
        schema_version=1, mission=MID, code='G45', base_commit=BASE, alpha_assets=[],
        note=('Images publiées existantes, hors arborescence Alpha ; non incluses dans le reçu '
              '(tools/alpha_publication.py). Octets vérifiés identiques à la base et à prep/figures.json.'),
        images=inventaire()))
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
    receipt = dict(schema_version=1, actor='Claude', code='G45', fragment='S08', phase='completed',
                   medical_human_validation=False, base_commit=BASE, source_commit=src, mission=MID,
                   previous_receipt_sha256=None, files=files, audits=audits, note=NOTE)
    dump('organisation/alpha-publications/Claude/G45/0001.json', receipt)
    print('reçu écrit, source_commit', src)


if __name__ == '__main__':
    {'preparer': preparer, 'recu': recu}[sys.argv[1]]()
