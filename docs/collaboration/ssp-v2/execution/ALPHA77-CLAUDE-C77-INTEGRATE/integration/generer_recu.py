"""Reçu Alpha C77 (mission ALPHA77-CLAUDE-C77-INTEGRATE) — Agent W.

Modèle : docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-C77-INTEGRATE/integration/generer_recu.py.

Étape 1 : python3 <ce fichier> preparer
  copie les sept fichiers finaux et l'image Alpha SEER dans livraison/. Les preuves de droits de
  l'image SEER existent déjà (revue/droits/c77-img-1_rights.json) : elles sont réutilisées
  telles quelles et seulement vérifiées.
Étape 2 (après commit de l'étape 1) : python3 <ce fichier> recu
  écrit organisation/alpha-publications/Claude/C77/0001.json avec source_commit = HEAD.
Le reçu n'est valide que si revue/MED.json, LANG.json et SEMIO.json portent les empreintes
des fichiers finaux (reviewed_files_sha256). Revue IA, distincte d'une validation médicale humaine.
"""
import hashlib, json, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
MID = 'ALPHA77-CLAUDE-C77-INTEGRATE'
M = f'docs/collaboration/ssp-v2/execution/{MID}'
BASE = 'abd681e5175db8c89e87dd7b83f96d0249d81cd7'
CORE = [f'chapters/C77/C77_{x}.html' for x in ('a', 'b', 'c', 'd', 'pop1', 'pop2')] + ['glossary/c77.py']
FIG = {
    'assets/img/c77/alpha/claude/lymph_node_regions_seer.svg': dict(
        rights='revue/droits/c77-img-1_rights.json', visual='revue/FIGURE_c77-img-1.json',
        license='Domaine public (œuvre du gouvernement fédéral des États-Unis) ; Public Domain Mark 1.0',
        # Sous-chaîne exacte de la légende visible (Figure 1, C77_c.html, #c77-s-anat).
        attribution='« Lymph node regions.svg », d’après NCI SEER Training Modules, œuvre du gouvernement fédéral des États-Unis, domaine public ; vectorisation Fred the Oyster ; via Wikimedia Commons'),
}
NOTE = ('Figure 1 : original SEER/NCI, domaine public, vectorisation humaine (Fred the Oyster). '
        'Revue IA, distincte d’une validation médicale humaine.')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def git_show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def dump(path, obj):
    (ROOT / path).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def check_rights(asset, f):
    rights = json.loads((ROOT / M / f['rights']).read_text(encoding='utf-8'))
    assert rights['original_sha256'] == sha(asset), 'droits : octets différents'
    for key in ('source_page', 'license_page'):
        assert rights[key]['sha256'] == sha(rights[key]['path']), 'droits : page modifiée ' + key
    caption = (ROOT / 'chapters/C77/C77_c.html').read_text(encoding='utf-8')
    assert caption.count(f['attribution']) == 1 and rights['credit'] in f['attribution'], 'attribution absente de la légende'
    return rights


def preparer():
    for target in CORE + list(FIG):
        dest = ROOT / M / 'livraison' / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / target, dest)
    for asset, f in FIG.items():
        check_rights(asset, f)
    print('préparation écrite (livraison/), droits existants vérifiés')


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
            rights = check_rights(target, f)
            ref['figure'] = dict(original_url=rights['original_url'], source_url=rights['source_url'],
                                 license_url=rights['license_url'], license=f['license'],
                                 attribution=f['attribution'], ai_generated=False, original_sha256=sha(target),
                                 visual_review_report=f'{M}/{f["visual"]}', visual_review_sha256=sha(f'{M}/{f["visual"]}'),
                                 rights_evidence=dict(path=f'{M}/{f["rights"]}', sha256=sha(f'{M}/{f["rights"]}')))
        files[target] = ref
    audits = {k: dict(path=f'{M}/revue/{k}.json', sha256=sha(f'{M}/revue/{k}.json')) for k in ('MED', 'LANG', 'SEMIO')}
    final = {t: r['sha256'] for t, r in files.items()}
    for k in audits:
        report = json.loads((ROOT / audits[k]['path']).read_text(encoding='utf-8'))
        assert report['reviewed_files_sha256'] == final, 'revue non liée aux fichiers finaux : ' + k
    receipt = dict(schema_version=1, actor='Claude', code='C77', fragment='S06', phase='completed',
                   medical_human_validation=False, base_commit=BASE, source_commit=src, mission=MID,
                   previous_receipt_sha256=None, files=files, audits=audits, note=NOTE)
    dump('organisation/alpha-publications/Claude/C77/0001.json', receipt)
    print('reçu écrit, source_commit', src)


if __name__ == '__main__':
    {'preparer': preparer, 'recu': recu}[sys.argv[1]]()
