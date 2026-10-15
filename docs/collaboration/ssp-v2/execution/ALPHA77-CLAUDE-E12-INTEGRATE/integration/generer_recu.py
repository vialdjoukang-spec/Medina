"""Reçu Alpha E12 (mission ALPHA77-CLAUDE-E12-INTEGRATE) — Agent W.

Étape 1 : python3 <ce fichier> preparer
  copie les sept fichiers finaux et les deux images dans livraison/ et écrit droits/fig*_droits.json.
Étape 2 (après commit de l'étape 1) : python3 <ce fichier> recu
  écrit organisation/alpha-publications/Claude/E12/0001.json avec source_commit = HEAD.
Le reçu n'est valide que si revue/MED.json, LANG.json et SEMIO.json portent les empreintes
des fichiers finaux (reviewed_files_sha256). Revue IA, distincte d'une validation médicale humaine.
"""
import hashlib, json, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
MID = 'ALPHA77-CLAUDE-E12-INTEGRATE'
M = f'docs/collaboration/ssp-v2/execution/{MID}'
BASE = 'abd681e5175db8c89e87dd7b83f96d0249d81cd7'
CORE = [f'chapters/E12/E12_{x}.html' for x in ('a', 'b', 'c', 'd', 'pop1', 'pop2')] + ['glossary/e12.py']
FIG = {
    'assets/img/e12/alpha/claude/e12-fig2-pancreatite-chronique-calcifiante-ct-hellerhoff.jpg': dict(
        n='fig2', original_url='https://upload.wikimedia.org/wikipedia/commons/7/7b/Chronische_Pankreatitis_mit_Verkalkungen_-_CT_axial.jpg',
        source_url='https://commons.wikimedia.org/wiki/File:Chronische_Pankreatitis_mit_Verkalkungen_-_CT_axial.jpg',
        license_url='https://creativecommons.org/licenses/by-sa/3.0/', license='CC BY-SA 3.0 Unported',
        author='Hellerhoff', credit='Hellerhoff',
        attribution='Image : Hellerhoff (flèche ajoutée par Doc James), Wikimedia Commons, licence CC BY-SA 3.0',
        license_quote='Attribution-ShareAlike 3.0 Unported', source_page='droits/fig2_source_commons.html',
        license_page='droits/licence_cc_by-sa_3.0.html', visual='revue/VISUEL_fig2.json'),
    'assets/img/e12/alpha/claude/e12-fig3-ilot-langerhans-he-polarlys.jpg': dict(
        n='fig3', original_url='https://upload.wikimedia.org/wikipedia/commons/f/f0/Langerhanssche_Insel.jpg',
        source_url='https://commons.wikimedia.org/wiki/File:Langerhanssche_Insel.jpg',
        license_url='https://creativecommons.org/licenses/by/2.5/', license='CC BY 2.5 Generic',
        author='Polarlys', credit='Polarlys',
        attribution='Image : Polarlys, Wikimedia Commons, licence CC BY 2.5',
        license_quote='Attribution 2.5 Generic', source_page='droits/fig3_source_commons.html',
        license_page='droits/licence_cc_by_2.5.html', visual='revue/VISUEL_fig3.json'),
}
RETRIEVED = {'fig2': '2026-10-15T20:56:31+00:00', 'fig3': '2026-10-15T20:57:20+00:00'}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def git_show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def dump(path, obj):
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def preparer():
    for target in CORE + list(FIG):
        dest = ROOT / M / 'livraison' / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / target, dest)
    for asset, f in FIG.items():
        rights = dict(schema_version=1, actor='Claude', code='E12', original_sha256=sha(asset),
                      transformed=False, ai_generated=False, license_verified=True,
                      author=f['author'], credit=f['credit'], retrieved_at=RETRIEVED[f['n']],
                      license_quote=f['license_quote'], license=f['license'],
                      original_url=f['original_url'], source_url=f['source_url'], license_url=f['license_url'],
                      source_page=dict(path=f'{M}/{f["source_page"]}', sha256=sha(f'{M}/{f["source_page"]}')),
                      license_page=dict(path=f'{M}/{f["license_page"]}', sha256=sha(f'{M}/{f["license_page"]}')),
                      methode='Une requête HTTPS par page (User-Agent de navigateur neutre), Retry-After respecté ; copie en octets de la réponse 200.',
                      mention='Preuve technique de droits ; ne certifie aucun jugement médical.')
        dump(f'{M}/droits/{f["n"]}_droits.json', rights)
    print('préparation écrite')


def recu():
    src = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    files = {}
    for target in CORE + list(FIG):
        prev = git_show(BASE, target)
        ref = dict(previous_sha256=hashlib.sha256(prev).hexdigest() if prev is not None else None,
                   sha256=sha(f'{M}/livraison/{target}'), source_path=f'{M}/livraison/{target}')
        assert ref['sha256'] == sha(target), 'livraison différente du fichier final : ' + target
        if target in FIG:
            f = FIG[target]
            ref['figure'] = dict(original_url=f['original_url'], source_url=f['source_url'], license_url=f['license_url'],
                                 license=f['license'], attribution=f['attribution'], ai_generated=False,
                                 original_sha256=sha(target),
                                 visual_review_report=f'{M}/{f["visual"]}', visual_review_sha256=sha(f'{M}/{f["visual"]}'),
                                 rights_evidence=dict(path=f'{M}/droits/{f["n"]}_droits.json', sha256=sha(f'{M}/droits/{f["n"]}_droits.json')))
        files[target] = ref
    audits = {k: dict(path=f'{M}/revue/{k}.json', sha256=sha(f'{M}/revue/{k}.json')) for k in ('MED', 'LANG', 'SEMIO')}
    receipt = dict(schema_version=1, actor='Claude', code='E12', fragment='S05', phase='completed',
                   medical_human_validation=False, base_commit=BASE, source_commit=src, mission=MID,
                   previous_receipt_sha256=None, files=files, audits=audits)
    dump('organisation/alpha-publications/Claude/E12/0001.json', receipt)
    print('reçu écrit, source_commit', src)


if __name__ == '__main__':
    {'preparer': preparer, 'recu': recu}[sys.argv[1]]()
