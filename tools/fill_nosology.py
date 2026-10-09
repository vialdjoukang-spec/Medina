#!/usr/bin/env python3
"""One fragment per invocation; resumable queue, additive shells, honest gauges."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fragment_surface import frontend_catalog
from nosologyEngine import gauges, generate, progress, read_json, reference, sha256


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n')


def protected_inventory():
    path = ROOT / 'nosology/integrity.json'
    if not path.exists():
        files = [file for directory in ('chapters', 'glossary', 'livraisons')
                 for file in (ROOT / directory).rglob('*') if file.is_file() and '__pycache__' not in file.parts]
        files += [ROOT / name for name in ('chapters.json', 'fragments.json', 'organisation/course_groups.json', 'shell/medina_front.html')]
        save(path, {str(file.relative_to(ROOT)): sha256(file) for file in sorted(files)})
    protected = read_json(path)
    for name, digest in protected.items():
        file = ROOT / name
        if not file.exists() or sha256(file) != digest:
            raise ValueError('Source préexistante modifiée ou supprimée : ' + name)
    return protected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fragment', required=True)
    parser.add_argument('--complete', action='store_true')
    args = parser.parse_args()
    protected_inventory()
    names = sorted(read_json(ROOT / 'organisation/fragments.json'), key=lambda item: item['order'])
    ids = [item['id'] for item in names]
    if args.fragment not in ids:
        raise ValueError('Fragment inconnu : ' + args.fragment)
    state_path = ROOT / 'nosology/queue.json'
    state = read_json(state_path) if state_path.exists() else {ident: 'pending' for ident in ids}
    first = next((ident for ident in ids if state[ident] != 'completed'), None)
    if args.fragment != first and state[args.fragment] != 'completed':
        raise ValueError('Un seul fragment à la fois ; prochain : ' + str(first))
    _, _, courses = frontend_catalog(ROOT)
    for course in courses.values():
        files = [ROOT / 'chapters' / course['code'] / (course['code'] + '_' + tab + '.html') for tab in 'abcd']
        course['has_content'] = all(file.is_file() and re.sub('<[^>]*>', '', file.read_text()).strip() for file in files)
        course['versions'] = sorted(str(file.relative_to(ROOT)) for file in (ROOT / 'chapters' / course['code']).rglob('*') if file.is_file())
    ref = reference(str(ROOT))
    codes = [entity['code'] for entity in ref['entities'] if not entity['excluded']
             and ref['mapping'][entity['code'][:3]]['fragment'] == args.fragment]
    file = ROOT / 'nosology/fragments' / (args.fragment + '.json')
    previous = read_json(file) if file.exists() else None
    inventory = generate(codes, args.fragment, ROOT, courses, previous)
    inventory['gauges'] = gauges(inventory['lessons'], read_json(ROOT / 'nosology/frequency.json')['codes'])
    inventory['preserved_courses'] = [{key: course[key] for key in ('code', 'title', 'covers', 'versions')}
                                     for course in courses.values() if course['source_fragment_id'] == args.fragment]
    inventory['secondary_references'] = [
        {'code': code, 'fragment': mapping['fragment'], 'url': '#/entry/' + code}
        for code, mapping in ref['mapping'].items() if args.fragment in mapping['secondary_fragments']]
    save(file, inventory)
    state[args.fragment] = 'completed' if args.complete else 'in_progress'
    save(state_path, state)
    # Compute all denominators from the same reference, including pending
    # fragments. Existing courses count once; empty children count zero filled.
    per_fragment, all_lessons = {}, []
    for ident in ids:
        local_path = ROOT / 'nosology/fragments' / (ident + '.json')
        local = read_json(local_path) if local_path.exists() else generate(
            [entity['code'] for entity in ref['entities'] if not entity['excluded']
             and ref['mapping'][entity['code'][:3]]['fragment'] == ident], ident, ROOT, courses)
        per_fragment[ident] = local['progress']
        all_lessons.extend(local['lessons'])
    save(ROOT / 'nosology/progress.json', {'global': progress(all_lessons), 'fragments': per_fragment})
    lines = ['# QUEUE — CIM-10-GM 2024 OFS française', '',
             'Remplissage nosologique uniquement. Cours, sous-leçons et versions préexistants conservés.',
             'Reprise : premier fragment non coché. Une spécialité à la fois.', '',
             'Terminé = inventaire et coquilles générés, contrôles locaux passés ; les cours vides restent vides.', '']
    for item in names:
        value = state[item['id']]
        label = 'fait' if value == 'completed' else 'en cours' if value == 'in_progress' else 'restant'
        lines.append(f"- [{'x' if value == 'completed' else ' '}] {item['order']:02d}. {item['label']} (`{item['id']}`) — {label}")
    (ROOT / 'QUEUE.md').write_text('\n'.join(lines) + '\n')
    aliases = sum(len(course.get('covers', [])) - 1 for course in inventory['preserved_courses'])
    report = {'fragment': args.fragment, 'codes': len(codes), 'category_count': sum(len(code) == 3 for code in codes),
              'lessons': len(inventory['lessons']), 'empty_shells': sum(item['state'] == 'empty' for item in inventory['lessons']),
              'existing_courses_preserved': len(inventory['preserved_courses']), 'aliases_deduplicated': aliases,
              'gold_stars': inventory['gold_stars'], 'progress': inventory['progress'],
              'gauges': inventory['gauges'],
              'unattached': inventory['unattached'], 'exam_unresolved': inventory['exam_unresolved'],
              'mapping_arbitration': [code for code in codes if len(code) == 3 and code[0] in 'RZST'
                                      and 'transversale' in ref['mapping'][code]['basis']],
              'preserved_source_files': len(read_json(ROOT / 'nosology/integrity.json'))}
    save(ROOT / 'docs/nosology' / (args.fragment + '.json'), report)
    print(args.fragment, report['codes'], 'codes,', report['empty_shells'], 'coquilles vides,', report['gold_stars'], 'étoiles,', report['progress'])


if __name__ == '__main__': main()
