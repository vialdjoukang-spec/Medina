"""Opt-in course surface: only S01 enables it during the first fragment review."""
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
    category_codes = [code for group in fragment['categories'] for code in group['chapters']]
    if len(category_codes) != len(set(category_codes)) or set(category_codes) != set(written):
        raise ValueError('Chaque cours du fragment doit avoir exactement une catégorie.')
    data['fragment'].update({
        'specialty': sid,
        'surface': fragment['surface'],
        'categories': fragment['categories'],
        'courses': [dict(written[code], complete=code in completed) for code in category_codes],
    })


def finish_surface(source, fragment, root):
    # Keep the historical shell in the repository; generated S01 drops module
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
    nav = ('<nav class="nav-main"><a href="#/home">Accueil · cours</a>'
           '<a href="#/search">Rechercher un cours</a>'
           '<a href="#/notebook">Carnet du fragment</a>'
           '<a href="#/method">Règle d’or et sources</a></nav>')
    source, count = re.subn(r'<nav class="nav-main">.*?</nav>', lambda _: nav, source, count=1, flags=re.S)
    assert count == 1
    source = source.replace('aria-label="Liste des spécialités"', 'aria-label="Cours par catégorie"')
    source = source.replace('placeholder="Code CIM, pathologie, système…"', 'placeholder="Rechercher parmi les cours cardiovasculaires…"')
    source = source.replace('aria-label="Rechercher dans Medina"', 'aria-label="Rechercher un cours cardiovasculaire"')
    css = (Path(root) / 'shell/fragment.css').read_text(encoding='utf-8')
    js = (Path(root) / 'shell/fragment.js').read_text(encoding='utf-8')
    source = source.replace('</head>', '<style id="medina-fragment-css">' + css + '</style></head>', 1)
    source = source.replace('</body>', '<script id="medina-fragment-runtime">' + js + '</script></body>', 1)
    return source
