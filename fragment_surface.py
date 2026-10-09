"""Frontend ownership and isolated course surfaces for all 22 specialties.

The historic anatomy-based catalogue remains documentary input. Frontends use
the specialty classification and local canonical courses, without importing
courses, glossaries or references from another fragment.
"""
import html
import json
import re
from pathlib import Path


SPECIALTY_BY_FRAGMENT = {
    'S01': 'cardiologie', 'S02': 'pneumologie', 'S03': 'gastroenterologie',
    'S04': 'nephrologie', 'S05': 'endocrinologie', 'S06': 'hematologie',
    'S07': 'immunologie', 'S08': 'neurologie', 'S10': 'rhumatologie',
    'S11': 'dermatologie', 'S12': 'orl', 'S13': 'ophtalmologie',
    'S14': 'gynecologie', 'S15': 'urologie', 'S16': 'obstetrique',
    'T1': 'infectiologie', 'T2': 'medecine-ages', 'T3': 'urgences',
    'T4': 'oncologie', 'T5': 'diagnostic', 'T6': 'medecine-famille', 'T7': 'ethique',
}
PRIMARY_FRAGMENT = {sid: ident for ident, sid in SPECIALTY_BY_FRAGMENT.items()}
PRIMARY_FRAGMENT.update({
    'angiologie': 'S01', 'chirurgie-cardiaque': 'S01', 'chirurgie-vasculaire': 'S01',
    'chirurgie-thoracique': 'S02', 'hepatologie': 'S03', 'chirurgie-generale': 'S03',
    'nutrition': 'S05', 'allergologie': 'S07', 'orthopedie': 'S10',
    'neurochirurgie': 'S08', 'chirurgie-maxillofaciale': 'S12',
    'reproduction': 'S15', 'neonatologie': 'S16', 'microbiologie': 'T1',
    'pediatrie': 'T2', 'geriatrie': 'T2', 'toxicologie': 'T3',
    'soins-intensifs': 'T3', 'anesthesiologie': 'T3', 'medecine-legale': 'T3',
    'genetique': 'T4', 'soins-palliatifs': 'T4', 'anatomopathologie': 'T5',
    'radiologie': 'T5', 'biologie-medicale': 'T5', 'medecine-nucleaire': 'T5',
    'sante-publique': 'T6', 'medecine-travail': 'T6',
})
FRAGMENT_ACCENTS = {
    'S01': '#b64b43', 'S02': '#3d7184', 'T1': '#317765', 'S03': '#967143',
    'S08': '#6a5e91', 'S05': '#926a45', 'S04': '#3c7a88', 'S06': '#a55768',
    'T4': '#765e7a', 'S14': '#9a657d', 'S16': '#a87258', 'T2': '#727d48',
    'S07': '#647c50', 'S10': '#7c704b', 'S15': '#527b85', 'S11': '#9a735d',
    'S12': '#4e7a71', 'S13': '#677ea0', 'T3': '#a76145', 'T5': '#687e78',
    'T6': '#718359', 'T7': '#81738e',
}
DATA_PATTERN = r'(<script id="medora-data" type="application/json">)(.*?)(</script>)'


def frontend_catalog(root):
    """Return frontend owners and integrated canonical courses, without writes.

    Explicit course assignments take precedence. Primary medical specialties
    correct anatomy-only misclassifications (notably A43, B18 and A04).
    Generic internal-medicine entries retain their anatomical ownership.
    Variants of an integrated course stay with that canonical course.
    """
    root = Path(root)
    source = (root / 'shell/medina_front.html').read_text(encoding='utf-8')
    full = json.loads(re.search(DATA_PATTERN, source, re.S).group(2))
    from nosologyEngine import augment_catalog
    full, nosology_owners = augment_catalog(full, root)
    fragments = json.loads((root / 'fragments.json').read_text(encoding='utf-8'))
    ids = {fragment['id'] for fragment in fragments}
    explicit, systems = {}, {}
    for fragment in fragments:
        for attachment in fragment['rattachements']:
            target = explicit if re.fullmatch(r'[A-Z][0-9]{2}', attachment) else systems
            if attachment in target and target[attachment] != fragment['id']:
                raise ValueError('Rattachement documentaire ambigu : ' + attachment)
            target[attachment] = fragment['id']
    owners = {}
    for entry in full['entries']:
        owner = explicit.get(entry['code']) or PRIMARY_FRAGMENT.get(entry.get('primary')) or systems.get(entry.get('system'))
        if owner in ids:
            owners[entry['code']] = owner
    owners.update(nosology_owners)
    courses = {item['code']: dict(item) for item in json.loads((root / 'chapters.json').read_text(encoding='utf-8')) if item.get('integrated')}
    groups_path = root / 'organisation/course_groups.json'
    if groups_path.exists():
        groups = json.loads(groups_path.read_text(encoding='utf-8'))
        if isinstance(groups, dict):
            groups = groups.get('groups', groups.get('courses', []))
        for item in groups:
            if item['code'] in courses:
                courses[item['code']].update(item)
                courses[item['code']]['integrated'] = True
    aliases = {}
    for course in courses.values():
        owner = course.get('owner') or owners.get(course['code'])
        if owner not in ids:
            raise ValueError('Cours intégré sans spécialité propriétaire : ' + course['code'])
        course['source_fragment_id'] = owner
        course.setdefault('covers', [course['code']])
        for code in set(course['covers']) | {course['code']}:
            if code in aliases and aliases[code] != course['code']:
                raise ValueError('Deux cours canoniques couvrent ' + code)
            aliases[code] = course['code']
            owners[code] = owner
    return full, owners, courses


def frontend_entries(fragment, entries, root):
    """Select the entries of this specialty, independently of legacy systems."""
    _, owners, _ = frontend_catalog(root)
    return [entry for entry in entries if owners.get(entry['code']) == fragment['id']]


def fragment_chapters(fragment, entries, root):
    """Integrated courses owned by a fragment; no cross-specialty references."""
    _, owners, courses = frontend_catalog(root)
    codes = {entry['code'] for entry in entries}
    return [dict(course, covers=[code for code in course['covers'] if owners.get(code) == fragment['id']])
            for course in courses.values() if course['source_fragment_id'] == fragment['id'] and
            (course['code'] in codes or codes.intersection(course['covers']))]


def presentation(fragment, root):
    names = json.loads((Path(root) / 'organisation/fragments.json').read_text(encoding='utf-8'))
    name = next(item for item in names if item['id'] == fragment['id'])
    display_name = name['specialty']
    return {key: name[key] for key in ('id', 'label', 'specialty', 'order')} | {
        'display_name': display_name, 'accent': FRAGMENT_ACCENTS[fragment['id']],
        'description': 'Parcourez les catégories et les cours de cette spécialité.',
    }


def isolate_specialty(data, fragment, chapters, completed):
    sid = fragment.get('specialty') or SPECIALTY_BY_FRAGMENT[fragment['id']]
    display_name = fragment.get('display_name') or re.sub(r'^[A-Z]-\d{2}-', '', fragment['nom'])
    specialty = next((s for s in data['specialties'] if s['id'] == sid), {'id': sid, 'rank': fragment.get('production_order', 1)})
    codes = {e['code'] for e in data['entries']}
    specialty = dict(specialty, title=display_name, entries=sorted(codes), legacyCount=0)
    data['specialties'] = [specialty]
    for entry in data['entries']:
        entry['primary'] = sid
        entry['primaryLabel'] = display_name
        entry['specialties'] = [sid]
        entry['links'] = []
    data['ssps'] = []
    data['meta']['entries'] = len(codes)
    data['meta']['sspVisible'] = 0
    # Old previews and the GLOBALITY catalogue are not fragment courses.
    data['legacy']['specialties'] = []
    data['legacy']['families'] = []
    data['legacy']['references'] = {}
    data['legacy']['learningTopics'] = {}
    data['legacy']['profilesGroups'] = []
    data['legacy']['systemSchema'] = {}
    data['legacy']['coverageAudit'] = {}
    data['legacy']['meta']['specialties'] = 1
    data['legacy']['meta']['chapters'] = len(codes)
    data['legacy']['meta']['systems'] = len({entry.get('system') for entry in data['entries']})
    data['profiles'] = {key: value for key, value in data['profiles'].items()
                        if key == 'symptom' or any(key in (entry.get('organ'), entry.get('profile')) for entry in data['entries'])}
    data['focus'] = {key: value for key, value in data['focus'].items() if key in codes}
    written = {c['code']: dict(c, covers=[code for code in c.get('covers', [c['code']]) if code in codes])
               for c in chapters if c['code'] in codes}
    data['legacy']['meta']['fullCourses'] = len(written)
    categories = [dict(group, chapters=[code for code in group['chapters'] if code in written]) for group in fragment.get('categories', [])]
    category_codes = [code for group in categories for code in group['chapters']]
    if len(category_codes) != len(set(category_codes)):
        raise ValueError('Un cours ne peut figurer dans deux anciennes rubriques.')
    missing = [code for code in written if code not in category_codes]
    if missing:
        categories.append({'id': 'cours-regroupes', 'nom': 'Cours regroupés', 'chapters': missing})
        category_codes.extend(missing)
    data['fragment'].update({
        'name': display_name,
        'display_name': display_name,
        'accent': FRAGMENT_ACCENTS[fragment['id']],
        'specialty': sid,
        'surface': fragment.get('surface', 'categories-v1'),
        'categories': categories,
        'courses': [dict(written[code], complete=code in completed) for code in category_codes],
    })


def fragment_motif(ident):
    """Motif de la spécialité (icône de l'accueil), en filigrane blanc dans la couverture."""
    from urllib.parse import quote
    from build_index import ICONS
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="#ffffff" stroke-opacity=".55" '
           'stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round">' + ICONS.get(ident, '') + '</svg>')
    return 'html[data-medina-fragment]{--frag-motif:url("data:image/svg+xml,' + quote(svg) + '")}'


def category_organisation_data(source, fragment, root):
    """Expose real CIM blocks and logical courses without dropping their variants."""
    root = Path(root)
    pattern = r'<script id="medora-data" type="application/json">(.*?)</script>'
    match = re.search(pattern, source, re.S)
    if not match:
        raise ValueError('Le catalogue du fragment est absent.')
    local = json.loads(match.group(1))
    full, owners, all_courses = frontend_catalog(root)
    by_code = {entry['code']: entry for entry in full['entries']}
    names = {item['id']: item for item in json.loads((root / 'organisation/fragments.json').read_text(encoding='utf-8'))}
    courses = {code: course for code, course in all_courses.items() if course['source_fragment_id'] == fragment['id']}
    course_by_alias = {}
    for course in courses.values():
        course.setdefault('covers', [course['code']])
        for code in course['covers']:
            old = course_by_alias.get(code)
            if old and old['code'] != course['code']:
                raise ValueError('Deux cours canoniques couvrent ' + code)
            course_by_alias[code] = course
    name = names[fragment['id']]
    priority = {code: index for index, code in enumerate(name.get('priority_codes', []))}
    entries = [entry for entry in local['entries'] if owners.get(entry['code']) == fragment['id']]
    ranks = {entry['code']: index + 1 for index, entry in enumerate(sorted(entries, key=lambda entry: (priority.get(entry['code'], 10000), entry['code'])))}
    blocks = {}
    for entry in entries:
        block = blocks.setdefault((entry['block'], entry['blockTitle']), {})
        course = course_by_alias.get(entry['code'])
        code = course['code'] if course else entry['code']
        lesson = block.setdefault(code, {
            'code': code, 'title': course['title'] if course else entry['title'],
            'integrated': bool(course and course.get('integrated')),
            'source_fragment_id': course['source_fragment_id'] if course else fragment['id'],
            'variants': [], 'production_order': ranks[entry['code']],
            'covers': [{'code': covered, 'title': by_code[covered]['title'], 'subcodes': by_code[covered].get('subcodes', [])}
                       for covered in (course['covers'] if course else [entry['code']])
                       if covered in by_code and owners.get(covered) == fragment['id']],
        })
        lesson['production_order'] = min(lesson['production_order'], ranks[entry['code']])
        lesson['variants'].append({'code': entry['code'], 'title': entry['title'], 'subcodes': entry.get('subcodes', [])})
    result = []
    for index, ((code, title), lessons) in enumerate(sorted(blocks.items()), 1):
        ordered = sorted(lessons.values(), key=lambda lesson: (lesson['production_order'], lesson['code']))
        for rank, lesson in enumerate(ordered, 1):
            lesson['order'] = rank
            lesson['variants'].sort(key=lambda variant: variant['code'])
            lesson['reference'] = lesson['code'] not in {variant['code'] for variant in lesson['variants']}
            owner = lesson['source_fragment_id']
            lesson['source_fragment_label'] = names[owner]['label']
            if owner != fragment['id']:
                raise ValueError('Cours étranger dans le frontend : ' + lesson['code'])
            lesson['url'] = '#/entry/' + lesson['code']
        result.append({'id': code, 'code': code, 'title': title, 'order': index, 'lessons': ordered})
    represented = [variant['code'] for block in result for lesson in block['lessons'] for variant in lesson['variants']]
    if sorted(represented) != sorted(entry['code'] for entry in entries):
        raise ValueError('La navigation doit conserver toutes les catégories du fragment.')
    result_data = {'fragment': presentation(fragment, root), 'version': 'CIM-10-GM 2024',
            'blocks': result, 'category_count': len(entries), 'integrated_count': len({lesson['code'] for block in result for lesson in block['lessons'] if lesson['integrated'] and lesson['source_fragment_id'] == fragment['id']}),
            'courses': [{'code': course['code'], 'title': course['title'],
                         'covers': [code for code in course['covers'] if owners.get(code) == fragment['id']],
                         'source_fragment_id': fragment['id'], 'url': '#/entry/' + course['code']}
                        for course in courses.values()],
            'organisation_url': '../organisation.html'}
    from nosologyEngine import attach_surface
    return attach_surface(result_data, root)


def isolated_glossary(source, glossary):
    """Keep definitions used by local course/popup templates and their links."""
    local_content = re.sub(r'<script\b[^>]*\bid="medina-glossary"[^>]*>.*?</script>', '', source, flags=re.S)
    keys = {html.unescape(key) for key in re.findall(r'\bdata-ab=["\']([^"\']+)["\']', local_content)}
    pattern = re.compile(r'(?<![A-Za-zÀ-ÿ0-9₀-₉⁺′])(' + '|'.join(re.escape(key) for key in sorted(glossary, key=len, reverse=True)) + r')(?![A-Za-zÀ-ÿ0-9₀-₉⁺′])') if glossary else None
    selected = {}
    pending = keys.intersection(glossary)
    popup_keys = set(re.findall(r'<template\b[^>]*\bdata-pop=["\']([^"\']+)["\']', source))
    while pending:
        key = sorted(pending)[0]
        pending.remove(key)
        definition = dict(glossary[key])
        if definition.get('ref') not in popup_keys:
            definition['ref'] = None
        selected[key] = definition
        text = ' '.join((definition.get('full', ''), definition.get('def', ''),
                         ' '.join(str(value) for part in definition.get('lit', []) for value in part)))
        if pattern:
            pending.update(set(pattern.findall(html.unescape(text))) - selected.keys())
    return selected


def isolate_generated_data(source, fragment, root):
    """Final boundary for every fragment, including the historical T surfaces."""
    match = re.search(DATA_PATTERN, source, re.S)
    if not match:
        raise ValueError('Le catalogue du fragment est absent.')
    data = json.loads(match.group(2))
    full, owners, _ = frontend_catalog(root)
    data['entries'] = [dict(entry) for entry in full['entries'] if owners.get(entry['code']) == fragment['id']]
    info = presentation(fragment, root)
    local_fragment = dict(fragment, display_name=info['display_name'])
    chapters = fragment_chapters(fragment, data['entries'], root)
    completed_match = re.search(r'window\.MEDINA_COMPLETE=(.*?);</script>', source, re.S)
    completed = json.loads(completed_match.group(1)) if completed_match else []
    isolate_specialty(data, local_fragment, chapters, completed)
    # Anatomical associations remain in the documentary source, rather than
    # embedding another specialty's legacy clinical profiles in this frontend.
    data['profiles'] = {}
    data['focus'] = {}
    for entry in data['entries']:
        entry['system'] = info['display_name']
    data['fragment']['systems'] = [info['display_name']] if data['entries'] else []
    data['fragment']['description'] = info['description']
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    source = source[:match.start()] + match.group(1) + payload + match.group(3) + source[match.end():]
    own_codes = {chapter['code'] for chapter in chapters}
    present = set(re.findall(r'<template\b[^>]*\bid=["\']ch-([^"\']+)', source))
    if present != own_codes:
        raise ValueError('Templates de cours hors périmètre ou absents : ' + ', '.join(sorted(present ^ own_codes)))
    foreign_popup = [key for key in re.findall(r'<template\b[^>]*\bdata-pop=["\']([^"\']+)', source)
                     if re.match(r'[a-z]\d{2}[-_]', key) and key[:3].upper() not in own_codes]
    if foreign_popup:
        raise ValueError('Fenêtres de cours étrangers : ' + ', '.join(foreign_popup))

    def update_script(match):
        attrs, body = match.group(1), match.group(2)
        if re.search(r'\bid="medina-glossary"', attrs):
            body = json.dumps(isolated_glossary(source, json.loads(body)), ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
        elif body.startswith('window.MEDINA_ALIAS='):
            aliases = json.loads(body[len('window.MEDINA_ALIAS='):].rstrip(';'))
            body = 'window.MEDINA_ALIAS=' + json.dumps({code: target for code, target in aliases.items()
                                                       if owners.get(code) == fragment['id'] and target in own_codes})
        elif body.startswith('window.MEDINA_COMPLETE='):
            body = 'window.MEDINA_COMPLETE=' + json.dumps([code for code in completed if code in own_codes]) + ';'
        elif 'an editorial outline generator' in body:
            # Preserve the shell's structural API without embedding generic
            # clinical plans that have not been written for this specialty.
            body = body.split('function buildPlan(e){', 1)[0] + '''
function buildPlan(){return Object.fromEntries(TAB_INFO.map(([key])=>[key,Object.fromEntries((SUB_INFO[key]||[['general']]).map(([sub])=>[sub,[]]))]))}
function flattenPlan(){return []}
function planCounts(){return {objectives:0,sections:0,plan:buildPlan()}}
'''
        elif body.startswith('window.MEDINA_FRAGMENT_SIDEBAR='):
            sidebar = json.loads(body[len('window.MEDINA_FRAGMENT_SIDEBAR='):].rstrip(';'))
            own_entries = {entry['code'] for entry in data['entries']}
            sidebar = [dict(group, items=[item for item in group['items'] if item['code'] in own_entries])
                       for group in sidebar if 'items' in group]
            sidebar = [group for group in sidebar if group['items']]
            if not own_codes:
                sidebar = [{'empty': "Aucun chapitre rédigé pour l'instant"}]
            body = 'window.MEDINA_FRAGMENT_SIDEBAR=' + json.dumps(sidebar, ensure_ascii=False).replace('<', '\\u003c') + ';'
        elif body.startswith('window.MDN_DATA='):
            position = body.index(';window.MDN_ECG=')
            mdn = json.loads(body[len('window.MDN_DATA='):position])
            local_courses = [{'code': chapter['code'], 'title': chapter['title'], 'complete': chapter['code'] in completed} for chapter in chapters]
            covered = len({code for chapter in chapters for code in chapter['covers']})
            mdn.update(systems=[{'n': info['order'], 't': info['display_name'], 'title': info['display_name'],
                                'cat': len(data['entries']), 'total': len(data['entries']),
                                'covered': covered, 'pct': round(100 * covered / len(data['entries'])) if data['entries'] else 0,
                                'prio': False, 'done': False,
                                'ch': local_courses, 'courses': local_courses, 'plan': []}] if local_courses else [],
                       news=[item for item in mdn.get('news', []) if item['code'] in own_codes],
                       doneNames=[], complete=[code for code in completed if code in own_codes])
            if fragment['id'] != 'S01':
                mdn['ecgCat'] = {}
            body = 'window.MDN_DATA=' + json.dumps(mdn, ensure_ascii=False).replace('<', '\\u003c') + body[position:]
        return '<script' + attrs + '>' + body + '</script>'

    source = re.sub(r'<script([^>]*)>(.*?)</script>', update_script, source, flags=re.S)
    source = re.sub(r'<title>.*?</title>', '<title>Medina · ' + html.escape(info['display_name']) + '</title>', source, count=1, flags=re.S)
    source = source.replace('<strong>' + html.escape(fragment['nom']) + '</strong>', '<strong>' + html.escape(info['display_name']) + '</strong>', 1)
    source = source.replace('<small>FRAGMENT ' + fragment['id'] + '</small>', '<small>COURS DE MÉDECINE</small>', 1)
    return source


def finish_surface(source, fragment, root):
    # Keep the historical shell in the repository; generated course fragments drop module
    # loaders whose catalogues concern the complete atlas.
    removed_ids = {'medina-portable-resources', 'medina-portable-runtime',
                   'medora-v7-federal-integration', 'medora-globality-ux-v74'}
    removed_sources = {'assets/lesson-reader.js', 'assets/v73-runtime.8d86f32f.js',
                       'assets/system-atlas.js'}

    def strip(match):
        attrs, body = match.group(1), match.group(2)
        identifier = re.search(r'\bid="([^"]+)"', attrs)
        asset = re.search(r'\bdata-medina-source="([^"]+)"', attrs)
        if ((identifier and identifier.group(1) in removed_ids) or
                (asset and asset.group(1) in removed_sources) or
                body.strip() == 'MEDINA_LESSONS.init();'):
            return ''
        return match.group(0)

    source = re.sub(r'<script([^>]*)>(.*?)</script>', strip, source, flags=re.S)
    source = source.replace('<html ', '<html data-medina-fragment="' + fragment['id'] + '" ', 1)
    # A separate namespace preserves notebooks from the full atlas.
    for key in ('medora.atlas.v3', 'medora.atlas.v1'):
        source = source.replace("'" + key + "'", "'medina.fragment." + fragment['id'] + ".atlas'")
    nav = ('<nav class="nav-main"><a href="#/home">Accueil · catégories</a>'
           + ('<a href="#/clinical-skills">Sémiologie CS</a>' if fragment['id'] == 'S01' else '') +
           '<a href="#/search">Rechercher un chapitre</a>'
           '<a href="#/notebook">Carnet du fragment</a>'
           '<a href="#/method">Règle d’or et sources</a></nav>')
    source, count = re.subn(r'<nav class="nav-main">.*?</nav>', lambda _: nav, source, count=1, flags=re.S)
    assert count == 1
    source = source.replace('aria-label="Liste des spécialités"', 'aria-label="Cours par catégorie"')
    source = source.replace('placeholder="Code CIM, pathologie, système…"', 'placeholder="Rechercher un chapitre dans ce fragment…"')
    source = source.replace('aria-label="Rechercher dans Medina"', 'aria-label="Rechercher un cours du fragment"')
    css = (Path(root) / 'shell/fragment.css').read_text(encoding='utf-8')
    js = ((Path(root) / 'shell/fragment.js').read_text(encoding='utf-8') if fragment.get('surface') == 'courses-v1' else '')
    source = source.replace('</head>', '<style id="medina-fragment-css">' + css + '</style></head>', 1)
    if fragment['id'] == 'S01':
        module = Path(root) / 'modules'
        cs_css = (module / 'cardiovascular_cs.css').read_text(encoding='utf-8')
        cs_html = (module / 'cardiovascular_cs.html').read_text(encoding='utf-8')
        cs_js = (module / 'cardiovascular_cs.js').read_text(encoding='utf-8')
        source = source.replace('</head>', '<style id="medina-cs-css">' + cs_css + '</style></head>', 1)
        source = source.replace('</body>', cs_html + '<script id="medina-cs-runtime">' + cs_js + '</script></body>', 1)
    source = source.replace('</body>', '<script id="medina-fragment-runtime">' + js + '</script></body>', 1)
    source = isolate_generated_data(source, fragment, root)
    own_data = json.loads(re.search(DATA_PATTERN, source, re.S).group(2))
    sidebar_note = (str(len(own_data['entries'])) + ' catégories CIM intégrées.<br>' +
                    str(len(own_data['fragment']['courses'])) + ' cours rédigés.<br>Votre spécialité.')
    source = re.sub(r'<div class="sidebar-note">.*?</div>', '<div class="sidebar-note">' + sidebar_note + '</div>', source, count=1, flags=re.S)
    payload = json.dumps(category_organisation_data(source, fragment, root), ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    category_css = (Path(root) / 'engine/category_organisation.css').read_text(encoding='utf-8')
    category_js = (Path(root) / 'engine/category_organisation.js').read_text(encoding='utf-8')
    source = source.replace('</head>', '<style id="medina-category-organisation-css">' + category_css + '</style></head>', 1)
    import base64
    faces = ''.join("@font-face{font-family:'Atkinson Hyperlegible Next';font-style:%s;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
                    % (style, weight, base64.b64encode((Path(root) / 'shell/fonts' / name).read_bytes()).decode())
                    for name, style, weight in (('ahn-400.woff2', 'normal', '400'), ('ahn-400i.woff2', 'italic', '400'),
                                                ('ahn-600.woff2', 'normal', '600'), ('ahn-700.woff2', 'normal', '700')))
    atlas_css = (Path(root) / 'engine/atlas_v2.css').read_text(encoding='utf-8') + (Path(root) / 'engine/atlas_v3.css').read_text(encoding='utf-8') + (Path(root) / 'engine/atlas_v4.css').read_text(encoding='utf-8') + fragment_motif(fragment['id'])
    source = source.replace('</head>', '<style id="medina-atlas-v2">' + faces + atlas_css + '</style></head>', 1)
    reading_css = ''.join((Path(root) / 'engine' / name).read_text(encoding='utf-8')
                          for name in ('frontend_v3.css', 'reading_v3.css'))
    source = source.replace('</head>', '<style id="medina-reading-v3">' + reading_css + '</style></head>', 1)
    source = source.replace('</body>', '<script id="medina-category-organisation-data" type="application/json">' + payload + '</script><script id="medina-category-organisation-runtime">' + category_js + '</script><script id="medina-atlas-v2-runtime">' + (Path(root) / 'engine/atlas_v2.js').read_text(encoding='utf-8') + '</script></body>', 1)
    return source
