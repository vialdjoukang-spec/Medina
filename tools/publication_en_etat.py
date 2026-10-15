"""Publication technique de sources existantes, sans validation médicale nouvelle."""
import hashlib
import argparse
import json
from pathlib import Path
import re
import subprocess

AUTHORITY = 'docs/collaboration/instructions/PUBLICATION_EN_ETAT_PARITE_2026-10-15.md'
RECEIPT = 'organisation/PUBLICATION_EN_ETAT_2026-10-15.json'
FRAGMENTS = {'S08', 'S05', 'S04', 'S06'}
HISTORY = ('organisation/fragment_status.json', 'organisation/tetrade_cycle_status.json',
           'organisation/CYCLES_CLAUDE.json', 'organisation/CYCLES_CLAUDE_journal.jsonl',
           'organisation/SCELLES.json', 'organisation/CYCLE_01_INJECTION_STOP_2026-10-12.json',
           'organisation/execution-20261014/cycles.json',
           'organisation/betta_status.json', 'organisation/progression/plan-betta-cycles.json')


class PublicationError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise PublicationError('Publication en l’état : ' + message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(tree, path):
    try:
        return json.loads(tree.read(path))
    except (ValueError, TypeError) as error:
        raise PublicationError('Publication en l’état : JSON invalide : ' + path) from error


def provenance(tree, revision, path):
    """Lit un blob d'un vrai commit disponible ; aucune référence de branche mobile."""
    require(isinstance(revision, str) and re.fullmatch(r'[0-9a-f]{40}', revision), 'SHA de provenance requis')
    require(isinstance(path, str) and path and not path.startswith('/') and
            '\\' not in path and not any(p in {'', '.', '..'} for p in path.split('/')) and
            not any(c in path for c in '\r\n\x00'), 'chemin de provenance invalide')
    commit = subprocess.run(['git', 'cat-file', '-t', revision], cwd=tree.root, capture_output=True)
    require(commit.returncode == 0 and commit.stdout.strip() == b'commit', 'commit de provenance absent')
    result = subprocess.run(['git', 'show', f'{revision}:{path}'], cwd=tree.root, capture_output=True)
    require(result.returncode == 0, 'source de provenance absente : ' + path)
    return result.stdout


def validate(before, after, changed, adopted=False):
    """True seulement pour une remise bornée, identique aux sources de provenance.

    La garde générale conserve ses contrôles ordinaires pour les autres commits.
    Le reçu décrit une publication provisoire et n'atteste aucun audit médical.
    """
    if RECEIPT not in changed:
        return False
    require(after.read(RECEIPT, required=False) is not None, 'suppression du reçu interdite')
    receipt = load(after, RECEIPT)
    require(receipt.get('schema_version') == 1 and receipt.get('authority') == AUTHORITY and
            receipt.get('authority_sha256') == digest(after.read(AUTHORITY)), 'autorité absente ou différente')
    require(receipt.get('actor') in {'Codex', 'Claude'}, 'acteur Codex ou Claude requis')
    require(receipt.get('medical_human_validation') is False, 'absence de validation humaine à déclarer')
    for path in HISTORY:
        require(before.read(path, required=False) == after.read(path, required=False), 'historique modifié : ' + path)
    courses = receipt.get('courses')
    require(isinstance(courses, list) and courses, 'cours absents')
    codes, declared = set(), set()
    for course in courses:
        code, fragment = course.get('code'), course.get('fragment_id')
        require(isinstance(code, str) and re.fullmatch(r'[A-Z][0-9]{2}', code) and code not in codes,
                'code absent ou dupliqué')
        require(fragment in FRAGMENTS, 'fragment hors des quatre systèmes')
        taxonomy = load(after, f'nosology/fragments/{fragment}.json')
        require(any(row.get('code') == code for row in taxonomy.get('lessons', [])),
                'code absent de la nosologie du fragment : ' + code)
        codes.add(code)
        files = course.get('files')
        require(isinstance(files, dict) and files, 'inventaire vide : ' + code)
        for path, ref in files.items():
            require(path.startswith(f'chapters/{code}/') or path == f'glossary/{code.lower()}.py' or
                    path.startswith('assets/img/'), 'source hors du cours : ' + path)
            require(path not in declared and isinstance(ref, dict), 'source dupliquée ou référence invalide')
            expected = ref.get('sha256')
            require(isinstance(expected, str) and re.fullmatch(r'[0-9a-f]{64}', expected), 'empreinte invalide')
            raw = after.read(path)
            previous_raw = before.read(path, required=False)
            require(previous_raw is None or previous_raw == raw,
                    'source déjà canonique modifiée : ' + path)
            require(digest(raw) == expected, 'source différente du reçu : ' + path)
            require(raw == provenance(after, ref.get('provenance_revision'), ref.get('provenance_path')),
                    'source différente de la provenance : ' + path)
            declared.add(path)
    medical = {p for p in changed if p == 'chapters.json' or p.startswith(('chapters/', 'glossary/', 'assets/img/'))}
    require(medical - {'chapters.json'} <= declared, 'modification sans provenance : ' + str(sorted(medical - declared - {'chapters.json'})))
    if not adopted:
        require(receipt.get('catalog_sha256') == digest(after.read('chapters.json')), 'catalogue différent du reçu')
    original, current = load(before, 'chapters.json'), load(after, 'chapters.json')
    require(isinstance(original, list) and isinstance(current, list), 'catalogue invalide')
    if receipt.get('catalog_entries') is not None:
        require(receipt['catalog_entries'] == [r for r in current if r.get('code') in codes],
                'lignes publiées du catalogue différentes du reçu')
    elif adopted:
        # Compatibilité d'un reçu initial déjà publié : la capture globale
        # suffit tant que le catalogue n'a pas changé. Le CLI actuel enregistre
        # les seules lignes adoptées pour permettre les ajouts ultérieurs.
        require(receipt.get('catalog_sha256') == digest(after.read('chapters.json')), 'catalogue différent du reçu historique')
    require([r for r in original if r.get('code') not in codes] ==
            [r for r in current if r.get('code') not in codes], 'cours extérieur ajouté, retiré ou modifié')
    metadata = {'integrated', 'provisional_injection', 'audit_deferred', 'publication_mode', 'publication_receipt'}
    for code in codes:
        rows = [r for r in current if r.get('code') == code]
        require(len(rows) == 1 and rows[0].get('integrated') is True and
                rows[0].get('provisional_injection') is True and rows[0].get('publication_mode') == 'en_etat' and
                rows[0].get('audit_deferred') in {'non_realise', 'apres_cycle_30'}, 'statut provisoire absent : ' + code)
        previous = [r for r in original if r.get('code') == code]
        if previous:
            require(len(previous) == 1 and {k: v for k, v in previous[0].items() if k not in metadata} ==
                    {k: v for k, v in rows[0].items() if k not in metadata}, 'contenu du catalogue modifié : ' + code)
    return True


def adopted_codes(tree):
    """Revérifie les blobs adoptés, sans promouvoir les anciens états de cycle."""
    if tree.read(RECEIPT, required=False) is None:
        return set()
    validate(tree, tree, {RECEIPT}, adopted=True)
    return {row['code'] for row in load(tree, RECEIPT)['courses']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--actor', choices=('Codex', 'Claude'), required=True)
    parser.add_argument('--provenance-revision', required=True)
    parser.add_argument('--courses', nargs='+', required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    catalog = json.loads((root / 'chapters.json').read_bytes())
    courses = []
    for code in args.courses:
        rows = [r for r in catalog if r.get('code') == code]
        require(len(rows) == 1, 'entrée de catalogue unique requise : ' + code)
        row = rows[0]
        require(row.get('owner') in FRAGMENTS and isinstance(row.get('source_dir'), str), 'fragment ou dossier source absent')
        files = list((root / 'chapters' / code).glob('*'))
        glossary = root / 'glossary' / (code.lower() + '.py')
        if glossary.is_file():
            files.append(glossary)
        # Les figures sont conservées sous les mêmes chemins relatifs que dans
        # la livraison. Inclure chaque copie publiée, pas seulement les HTML.
        source_root = root / row['source_dir']
        for source_asset in (source_root / 'assets' / 'img').rglob('*'):
            if source_asset.is_file():
                copied_asset = root / source_asset.relative_to(source_root)
                if copied_asset.is_file():
                    files.append(copied_asset)
        refs = {}
        for file in sorted(p for p in files if p.is_file()):
            path = file.relative_to(root).as_posix()
            source_path = row['source_dir'] + '/' + path
            class Source:
                pass
            tree = Source(); tree.root = root
            require(file.read_bytes() == provenance(tree, args.provenance_revision, source_path),
                    'copie différente de sa source : ' + path)
            refs[path] = dict(sha256=digest(file.read_bytes()), provenance_path=source_path,
                              provenance_revision=args.provenance_revision)
        courses.append(dict(code=code, fragment_id=row['owner'], files=refs))
    receipt = dict(schema_version=1, actor=args.actor, authority=AUTHORITY,
                   authority_sha256=digest((root / AUTHORITY).read_bytes()), medical_human_validation=False,
                   catalog_sha256=digest((root / 'chapters.json').read_bytes()), courses=courses)
    receipt['catalog_entries'] = [row for row in catalog if row.get('code') in set(args.courses)]
    destination = root / RECEIPT
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(str(destination))


if __name__ == '__main__':
    main()
