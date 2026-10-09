#!/usr/bin/env python3
"""Recalcule les jauges depuis les cours réellement présents dans main.

Non destructif : ne touche ni aux cours (chapters/), ni à chapters.json, ni à
integrity.json, ni à queue.json/QUEUE.md. Pour chaque fragment, les leçons
couvertes par un cours intégré deviennent « filled » si ses quatre onglets ont
du contenu ; les coquilles vides absorbées par un cours (alias, ex. K26/K27
sous K25) sont retirées pour ne compter chaque code qu'une fois. Une coquille
contenant du texte rédigé n'est jamais retirée. Idempotent.

    python3 tools/refresh_gauges.py          # écrit
    python3 tools/refresh_gauges.py --check  # code 1 si les jauges sont périmées
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fragment_surface import frontend_catalog
from nosologyEngine import gauges, generate, progress, read_json, reference


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n')


def authored(lesson):
    return any(section.get('content', '').strip() for section in lesson.get('plan', [])) or lesson.get('notes')


def courses_in_main():
    _, _, courses = frontend_catalog(ROOT)
    for course in courses.values():
        course['covers'] = course.get('covers') or [course['code']]
        files = [ROOT / 'chapters' / course['code'] / (course['code'] + '_' + tab + '.html') for tab in 'abcd']
        course['has_content'] = all(file.is_file() and re.sub('<[^>]*>', '', file.read_text(encoding='utf-8')).strip()
                                    for file in files)
    return courses


def refresh(ident, ref, courses, frequent):
    path = ROOT / 'nosology/fragments' / (ident + '.json')
    previous = read_json(path)
    codes = [entity['code'] for entity in ref['entities'] if not entity['excluded']
             and ref['mapping'][entity['code'][:3]]['fragment'] == ident]
    built = generate(codes, ident, ROOT, courses, previous)
    absorbed = {code: lesson['id'] for lesson in built['lessons'] if lesson['existing_course']
                for code in lesson['icd10gm']['codes'] if code != lesson['id']}
    lessons = []
    for lesson in built['lessons']:
        if lesson['id'] in absorbed and not lesson['existing_course']:
            if authored(lesson):
                raise ValueError(f'{ident} {lesson["id"]} : coquille rédigée sous le cours {absorbed[lesson["id"]]}')
            continue
        lessons.append(lesson)
    inventory = dict(previous)
    inventory.update({'lessons': lessons, 'progress': progress(lessons),
                      'gold_stars': sum(item['gold_star']['enabled'] for item in lessons),
                      'exam_unresolved': [item['code'] for item in lessons if not item['gold_star']['enabled']],
                      'gauges': gauges(lessons, frequent)})
    return path, previous, inventory


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    ref = reference(str(ROOT))
    courses = courses_in_main()
    frequent = read_json(ROOT / 'nosology/frequency.json')['codes']
    ids = [item['id'] for item in sorted(read_json(ROOT / 'organisation/fragments.json'), key=lambda item: item['order'])]
    stale, per_fragment, all_lessons = [], {}, []
    for ident in ids:
        path, previous, inventory = refresh(ident, ref, courses, frequent)
        if inventory != previous:
            stale.append(ident)
            if not args.check:
                save(path, inventory)
        per_fragment[ident] = inventory['progress']
        all_lessons += inventory['lessons']
    totals = {'global': progress(all_lessons), 'fragments': per_fragment}
    progress_path = ROOT / 'nosology/progress.json'
    if read_json(progress_path) != totals:
        stale.append('progress.json')
        if not args.check:
            save(progress_path, totals)
    print(('Jauges périmées : ' if args.check else 'Mis à jour : ') + (', '.join(stale) or 'aucun'))
    return 1 if args.check and stale else 0


if __name__ == '__main__':
    sys.exit(main())
