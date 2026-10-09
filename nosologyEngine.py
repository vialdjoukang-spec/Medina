"""CIM-10-GM 2024 OFS: additive, deterministic lesson-shell generation.

No clinical course text is generated. Existing courses are references, never
rewritten; a category covered by an existing course is not a second lesson.
Detailed entities remain empty until explicitly authored, even under a course.
"""
from __future__ import annotations

import copy
import hashlib
import json
from functools import lru_cache
from pathlib import Path

BASE_PLAN = ('Définition', 'Épidémiologie', 'Physiopathologie', 'Clinique',
             'Examens complémentaires', 'Diagnostic différentiel', 'Traitement',
             'Complications/Pronostic')
EXTRA_PLAN = {
    'S01': ('Imagerie et explorations fonctionnelles', 'Classification et scores'),
    'S02': ('Imagerie et explorations fonctionnelles respiratoires', 'Classification et scores'),
    'T1': ('Microbiologie', 'Classification'),
    'S03': ('Imagerie et endoscopie', 'Classification et scores'),
    'S08': ('Imagerie et neurophysiologie', 'Classification et scores'),
    'S05': ('Explorations hormonales et métaboliques', 'Classification'),
    'S04': ('Imagerie et histologie rénale', 'Classification et scores'),
    'S06': ('Morphologie et immunophénotypage', 'Classification'),
    'T4': ('Histologie et biologie moléculaire', 'Classification et stadification', 'Soins palliatifs'),
    'S14': ('Imagerie et classification',),
    'S16': ('Surveillance maternelle et fœtale', 'Classification et scores néonataux'),
    'T2': ('Croissance, développement et autonomie',),
    'S07': ('Explorations immunologiques et allergologiques', 'Classification'),
    'S10': ('Imagerie', 'Classification et scores fonctionnels'),
    'S15': ('Imagerie et explorations fonctionnelles', 'Classification'),
    'S11': ('Dermoscopie et histologie', 'Classification'),
    'S12': ('Imagerie et explorations sensorielles', 'Classification'),
    'S13': ('Imagerie et explorations ophtalmologiques', 'Classification'),
    'T3': ('Évaluation initiale et scores de gravité', 'Imagerie'),
    'T5': ('Modalités et interprétation des examens',),
    'T6': ('Prévention et parcours de soins',),
    'T7': ('Consentement et cadre juridique',),
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


@lru_cache(maxsize=8)
def reference(root):
    return read_json(Path(root) / 'nosology/reference.json')


def adaptive_plan(fragment, chapter):
    # Administrative factors and external circumstances still receive the
    # requested monographic skeleton; optional additions remain empty too.
    labels = list(BASE_PLAN) + list(EXTRA_PLAN.get(fragment, ()))
    if chapter == 'XVII' and fragment != 'T4':
        labels.append('Génétique et conseil génétique')
    return [{'title': label, 'content': ''} for label in labels]


def progress(lessons):
    unique = {lesson['id']: lesson for lesson in lessons}
    filled = sum(lesson.get('state') == 'filled' for lesson in unique.values())
    total = len(unique)
    return {'filled': filled, 'total': total,
            'percent': round(100 * filled / total, 2) if total else 0}


def gauges(lessons, frequent_codes):
    frequent_codes = set(frequent_codes)
    frequent = [lesson for lesson in lessons if not '.' in lesson['code']
                and frequent_codes.intersection(lesson['icd10gm']['codes'])]
    federal = [lesson for lesson in lessons if lesson['gold_star']['enabled']]
    return {'frequent': progress(frequent), 'federal_exam': progress(federal), 'global': progress(lessons)}


def lesson_is_filled(lesson):
    if lesson.get('existing_course'):
        return lesson.get('state') == 'filled'
    return all(section.get('content', '').strip() for section in lesson.get('plan', [])) and bool(lesson.get('plan'))


def generate(codes, fragment, root, existing_courses=None, previous=None):
    """Accept actual OFS codes; reject unknown/excluded/foreign codes.

    A previous user-authored shell is retained byte-for-byte as JSON values.
    No localStorage/user preference can change the read-only gold-star field.
    """
    ref = reference(str(Path(root).resolve()))
    entities = {item['code']: item for item in ref['entities']}
    assignments = ref['mapping']
    courses = existing_courses or {}
    aliases = {code: course for course in courses.values()
               for code in set(course.get('covers', [])) | {course['code']}}
    old = {item['id']: item for item in (previous or {}).get('lessons', [])}
    lessons, seen, rejected = [], set(), []
    for code in sorted(set(codes)):
        entity = entities.get(code)
        if not entity or entity.get('excluded'):
            rejected.append({'code': code, 'reason': entity.get('excluded') if entity else 'Code absent du référentiel OFS'})
            continue
        owner = assignments[code[:3]]['fragment']
        if owner != fragment:
            rejected.append({'code': code, 'reason': 'Autre fragment : ' + owner})
            continue
        course = aliases.get(code) if len(code) == 3 else None
        if course:
            entity = entities.get(course['code'], entity)
        key = course['code'] if course else code
        if key in seen:
            continue
        seen.add(key)
        covered = sorted(set(course.get('covers', [])) | {key}) if course else [code]
        evidence = {number for category in covered
                    for number in ref['exam_mapping'].get(category[:3], [])}
        star = {'permanent': True, 'enabled': bool(evidence), 'ssp': sorted(evidence),
                'reference': 'PROFILES 2017 / SSP', 'source': ref['sources']['profiles']['url'],
                'basis': 'correspondance pédagogique explicite' if evidence else 'correspondance à arbitrer',
                'official_icd_crosswalk': False}
        item = {'id': key, 'code': key, 'title': course['title'] if course else entity['title'],
                'fragment': fragment, 'chapter': entity['chapter'], 'block': entity['block'],
                'category': entity['code'][:3], 'parent': entity.get('parent'),
                'icd10gm': {'version': '2024', 'language': 'fr', 'publisher': 'OFS',
                            'codes': covered, 'marker': entity.get('marker', ''),
                            'source': ref['sources']['csv']['url']},
                'state': 'filled' if course and course.get('has_content') else 'empty',
                'existing_course': course['code'] if course else None,
                'plan': [] if course else adaptive_plan(fragment, entity['chapter']),
                'gold_star': star}
        if key in old:
            # Metadata updates do not reset an authored plan or authored content.
            prior = copy.deepcopy(old[key])
            for field in ('plan', 'content', 'notes'):
                if field in prior:
                    item[field] = prior[field]
            if not course:
                item['state'] = 'filled' if lesson_is_filled(item) else 'empty'
        lessons.append(item)
    # Keep prior records even if the caller sends a partial list of codes.
    lessons.extend(copy.deepcopy(item) for key, item in old.items() if key not in seen)
    lessons.sort(key=lambda item: item['id'])
    return {'fragment': fragment, 'version': 'CIM-10-GM 2024 OFS fr', 'lessons': lessons,
            'progress': progress(lessons), 'unattached': rejected,
            'gold_stars': sum(item['gold_star']['enabled'] for item in lessons),
            'exam_unresolved': [item['code'] for item in lessons if not item['gold_star']['enabled']]}


def augment_catalog(full, root):
    """Enrich catalogue metadata from OFS without changing course source files."""
    path = Path(root) / 'nosology/reference.json'
    if not path.exists():
        return full, {}
    ref = reference(str(Path(root).resolve()))
    official = {item['code']: item for item in ref['entities'] if not item.get('excluded')}
    children = {}
    for code, item in official.items():
        if len(code) > 3:
            children.setdefault(code[:3], []).append({'code': code, 'title': item['title'], 'marker': item.get('marker', '')})
    full = copy.deepcopy(full)
    seen = set()
    for entry in full['entries']:
        code = entry['code']; seen.add(code)
        entity = official.get(code)
        if not entity:
            continue
        # Existing lesson labels and existing detailed variants are immutable.
        entry['ofsTitle'] = entity['title']
        entry['chapter'] = entity['chapter']
        entry['block'] = entity['block']
        entry['blockTitle'] = ref['blocks'][entity['block']]['title']
        entry['source'] = ref['sources']['csv']['url']
        entry['icd10gm'] = {'code': code, 'version': '2024', 'publisher': 'OFS', 'language': 'fr'}
        old_subcodes = {item['code']: item for item in entry.get('subcodes', [])}
        for item in children.get(code, []):
            old_subcodes.setdefault(item['code'], item)
        entry['subcodes'] = sorted(old_subcodes.values(), key=lambda item: item['code'])
    missing = {code for code in official if len(code) == 3} - seen
    if missing:
        raise ValueError('Catégories OFS absentes du catalogue documentaire : ' + ', '.join(sorted(missing)))
    full['meta']['nosologySource'] = ref['sources']['csv']
    return full, {code: item['fragment'] for code, item in ref['mapping'].items()}


def attach_surface(organisation, root):
    path = Path(root) / 'nosology/fragments' / (organisation['fragment']['id'] + '.json')
    if not path.exists():
        return organisation
    inventory = read_json(path)
    by_code = {item['code']: item for item in inventory['lessons']}
    organisation['nosology'] = inventory
    organisation['nosology']['global_progress'] = read_json(Path(root) / 'nosology/progress.json')['global']
    frequency = read_json(Path(root) / 'nosology/frequency.json')
    organisation['nosology']['gauges'] = gauges(inventory['lessons'], frequency['codes'])
    fragments = {item['id']: item for item in read_json(Path(root) / 'fragments.json')}
    for link in inventory.get('secondary_references', []):
        target = fragments[link['fragment']]
        link['url'] = 'MEDINA_' + target['id'] + '_' + target['slug'] + '.html#/entry/' + link['code']
    for block in organisation['blocks']:
        for lesson in block['lessons']:
            shell = by_code.get(lesson['code'])
            if shell:
                lesson['plan'] = shell['plan']
                lesson['gold_star'] = shell['gold_star']
            lesson['entities'] = [item for item in inventory['lessons']
                                  if len(item['code']) > 3 and item['category'] in {v['code'] for v in lesson['variants']}]
    return organisation


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
