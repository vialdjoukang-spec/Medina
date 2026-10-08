"""Course surface enabled fragment by fragment during the content review."""
import json
import re
from pathlib import Path


def isolate_specialty(data, fragment, chapters, completed):
    sid = fragment['specialty']
    specialty = next(s for s in data['specialties'] if s['id'] == sid)
    codes = {e['code'] for e in data['entries']}
    specialty = dict(specialty, title=fragment['nom'], entries=sorted(codes), legacyCount=0)
    data['specialties'] = [specialty]
    for entry in data['entries']:
        entry['primary'] = sid
        entry['primaryLabel'] = fragment['nom']
        entry['specialties'] = [sid]
        entry['links'] = []
    data['ssps'] = []
    data['meta']['sspVisible'] = 0
    # Old previews and the GLOBALITY catalogue are not fragment courses.
    data['legacy']['specialties'] = []
    data['legacy']['learningTopics'] = {}
    data['legacy']['profilesGroups'] = []
    data['legacy']['systemSchema'] = []
    data['legacy']['coverageAudit'] = {}
    data['legacy']['meta']['specialties'] = 1
    written = {c['code']: c for c in chapters}
    categories = [dict(group, chapters=[code for code in group['chapters'] if code in written]) for group in fragment['categories']]
    category_codes = [code for group in categories for code in group['chapters']]
    if len(category_codes) != len(set(category_codes)):
        raise ValueError('Un cours ne peut figurer dans deux anciennes rubriques.')
    missing = [code for code in written if code not in category_codes]
    if missing:
        categories.append({'id': 'cours-regroupes', 'nom': 'Cours regroupés', 'chapters': missing})
        category_codes.extend(missing)
    data['fragment'].update({
        'specialty': sid,
        'surface': fragment['surface'],
        'categories': categories,
        'courses': [dict(written[code], complete=code in completed) for code in category_codes],
    })


def category_organisation_data(source, fragment, root):
    """Expose real CIM blocks and logical courses without dropping their variants."""
    root = Path(root)
    pattern = r'<script id="medora-data" type="application/json">(.*?)</script>'
    match = re.search(pattern, source, re.S)
    if not match:
        raise ValueError('Le catalogue du fragment est absent.')
    local = json.loads(match.group(1))
    full = json.loads(re.search(pattern, (root / 'shell/medina_front.html').read_text(encoding='utf-8'), re.S).group(1))
    by_code = {entry['code']: entry for entry in full['entries']}
    fragments = json.loads((root / 'fragments.json').read_text(encoding='utf-8'))
    names = {item['id']: item for item in json.loads((root / 'organisation/fragments.json').read_text(encoding='utf-8'))}
    routes = {item['id']: 'MEDINA_' + item['id'] + '_' + item['slug'] + '.html' for item in fragments}
    explicit = {code: item['id'] for item in fragments for code in item['rattachements'] if re.fullmatch(r'[A-Z][0-9]{2}', code)}
    owners = {}
    for item in fragments:
        attached = set(item['rattachements'])
        for code, entry in by_code.items():
            if code in attached or (code not in explicit and entry.get('system') in attached):
                if code in owners and owners[code] != item['id']:
                    raise ValueError('Catégorie rattachée à plusieurs fragments : ' + code)
                owners[code] = item['id']
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
            else:
                courses[item['code']] = dict(item)
    course_by_alias = {}
    for course in courses.values():
        course.setdefault('covers', [course['code']])
        course['source_fragment_id'] = course.get('owner') or owners.get(course['code'], fragment['id'])
        for code in course['covers']:
            old = course_by_alias.get(code)
            if old and old['code'] != course['code']:
                raise ValueError('Deux cours canoniques couvrent ' + code)
            course_by_alias[code] = course
    name = names[fragment['id']]
    priority = {code: index for index, code in enumerate(name.get('priority_codes', []))}
    entries = local['entries']
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
                       for covered in (course['covers'] if course else [entry['code']]) if covered in by_code],
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
            lesson['url'] = ('#/entry/' + lesson['code']) if owner == fragment['id'] else (routes[owner] + '#/entry/' + lesson['code'])
        result.append({'id': code, 'code': code, 'title': title, 'order': index, 'lessons': ordered})
    represented = [variant['code'] for block in result for lesson in block['lessons'] for variant in lesson['variants']]
    if sorted(represented) != sorted(entry['code'] for entry in entries):
        raise ValueError('La navigation doit conserver toutes les catégories du fragment.')
    return {'fragment': {key: name[key] for key in ('id', 'label', 'specialty', 'order')}, 'version': 'CIM-10-GM 2024',
            'blocks': result, 'category_count': len(entries), 'integrated_count': len({lesson['code'] for block in result for lesson in block['lessons'] if lesson['integrated'] and lesson['source_fragment_id'] == fragment['id']}),
            'organisation_url': '../organisation.html'}


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
    payload = json.dumps(category_organisation_data(source, fragment, root), ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    category_css = (Path(root) / 'engine/category_organisation.css').read_text(encoding='utf-8')
    category_js = (Path(root) / 'engine/category_organisation.js').read_text(encoding='utf-8')
    source = source.replace('</head>', '<style id="medina-category-organisation-css">' + category_css + '</style></head>', 1)
    import base64
    faces = ''.join("@font-face{font-family:'MEDINA Serif';font-style:%s;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
                    % (style, weight, base64.b64encode((Path(root) / 'shell/fonts' / name).read_bytes()).decode())
                    for name, style, weight in (('ss-400.woff2', 'normal', '400 500'), ('ss-400i.woff2', 'italic', '400'), ('ss-600.woff2', 'normal', '600 700')))
    atlas_css = (Path(root) / 'engine/atlas_v2.css').read_text(encoding='utf-8')
    source = source.replace('</head>', '<style id="medina-atlas-v2">' + faces + atlas_css + '</style></head>', 1)
    source = source.replace('</body>', '<script id="medina-category-organisation-data" type="application/json">' + payload + '</script><script id="medina-category-organisation-runtime">' + category_js + '</script></body>', 1)
    return source
