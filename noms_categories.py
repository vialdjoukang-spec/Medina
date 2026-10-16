"""Noms d’affichage concis des catégories (blocs CIM-10-GM) de chaque fragment.

Le libellé officiel OFS reste intact dans ``official_title`` (info-bulle, aria) ;
seul ``title`` reçoit le nom d’affichage. Aucune leçon ni aucun code ne change.

Usage :
    python3 noms_categories.py            # contrôle complet (couverture, longueur, doublons…)
    python3 noms_categories.py --tableau  # tableau avant / après, en Markdown
"""
import copy
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'organisation' / 'noms_categories.json'
MAX_LENGTH = 40


@lru_cache(maxsize=None)
def _names(path=str(DATA)):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def load_names(path=DATA):
    """Table des noms (copie défensive, la source reste en cache)."""
    return copy.deepcopy(_names(str(path)))


def apply_category_names(organisation, names=None):
    """Retourne une copie où chaque bloc porte son nom d’affichage.

    Pure et idempotente : ``official_title`` n’est jamais écrasé une fois posé,
    et un second passage ne change rien. Un bloc absent de la table garde son titre.
    """
    table = (names or _names(str(DATA)))['fragments'].get(organisation['fragment']['id'], {})
    result = copy.deepcopy(organisation)
    for block in result['blocks']:
        entry = table.get(block['code'])
        if not entry:
            continue
        block.setdefault('official_title', entry['official_title'])
        block['title'] = entry['display_title']
    return result


def inventory(root=ROOT):
    """Recensement réel : {fragment: {bloc: {'title': libellé OFS, 'lessons': [[code, titre], …]}}}.

    Même source et même filtre de propriété que ``category_organisation_data``.
    """
    root = str(Path(root).resolve())
    if root not in sys.path:
        sys.path.insert(0, root)
    from fragment_surface import frontend_catalog
    full, owners, _ = frontend_catalog(root)
    fragments = json.loads((Path(root) / 'fragments.json').read_text(encoding='utf-8'))
    result = {fragment['id']: {} for fragment in fragments}
    for entry in full['entries']:
        owner = owners.get(entry['code'])
        if owner not in result:
            continue
        block = result[owner].setdefault(entry['block'], {'title': entry['blockTitle'], 'lessons': []})
        if block['title'] != entry['blockTitle']:
            raise ValueError('Libellé de bloc incohérent : ' + entry['block'])
        block['lessons'].append([entry['code'], entry['title']])
    for blocks in result.values():
        for block in blocks.values():
            block['lessons'].sort()
    return {fid: dict(sorted(blocks.items())) for fid, blocks in result.items()}


def abbreviations_in(text):
    """Sigles : mots contenant au moins deux majuscules consécutives (les codes CIM n’en ont pas)."""
    return {word for word in re.split(r'[\s,;:.()«»’\']+', text) if re.search(r'[A-ZÀ-Ý]{2,}', word)}


def check(root=ROOT, names=None):
    """Liste des anomalies (vide si tout est conforme)."""
    names = names or _names(str(DATA))
    inv = inventory(root)
    known = set(names.get('abbreviations', {}))
    errors = []
    for fid in sorted(set(inv) | set(names['fragments'])):
        table, blocks = names['fragments'].get(fid, {}), inv.get(fid, {})
        for code in sorted(set(blocks) - set(table)):
            errors.append(f'{fid} {code} : bloc non couvert')
        for code in sorted(set(table) - set(blocks)):
            errors.append(f'{fid} {code} : bloc inexistant')
        seen = {}
        for code, entry in table.items():
            display = entry['display_title']
            if code in blocks and entry['official_title'] != blocks[code]['title']:
                errors.append(f'{fid} {code} : libellé officiel divergent')
            if entry['kept'] != (display == entry['official_title']):
                errors.append(f'{fid} {code} : drapeau « kept » incohérent')
            if len(display) > MAX_LENGTH:
                errors.append(f'{fid} {code} : {len(display)} caractères')
            if display != display.strip() or '  ' in display or not display[:1].isupper():
                errors.append(f'{fid} {code} : typographie')
            if not entry.get('rationale'):
                errors.append(f'{fid} {code} : justification absente')
            for word in abbreviations_in(display + ' ' + entry.get('rationale', '')) - known:
                errors.append(f'{fid} {code} : abréviation non définie « {word} »')
            key = display.casefold()
            if key in seen:
                errors.append(f'{fid} {code} : doublon avec {seen[key]}')
            seen[key] = code
    return errors


def table_markdown(root=ROOT, names=None):
    names = names or _names(str(DATA))
    inv = inventory(root)
    lines = ['| Fragment | Bloc | Avant (OFS) | Après | Leçons |', '|---|---|---|---|---|']
    for fid, blocks in inv.items():
        for code, block in blocks.items():
            entry = names['fragments'][fid][code]
            after = '(conservé)' if entry['kept'] else entry['display_title']
            lines.append(f"| {fid} | {code} | {block['title']} | {after} | {len(block['lessons'])} |")
    return '\n'.join(lines)


if __name__ == '__main__':
    if '--tableau' in sys.argv:
        print(table_markdown())
        sys.exit(0)
    problems = check()
    total = sum(len(v) for v in _names(str(DATA))['fragments'].values())
    kept = sum(e['kept'] for v in _names(str(DATA))['fragments'].values() for e in v.values())
    print('\n'.join(problems) or f'NOMS OK : {total} blocs, {total - kept} renommés, {kept} conservés.')
    sys.exit(1 if problems else 0)
