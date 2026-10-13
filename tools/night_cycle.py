"""Chaîne autorisée le 14 octobre, limitée dans le temps, sans moteur autonome.

La garde conserve la chaîne de preuves historique et ses contrôles suisses.
Elle contrôle la cohérence des reçus, pas leur vérité médicale.
"""
from datetime import datetime, timezone
try:
    from tools import tetrade_cycle as C
except ModuleNotFoundError:
    import tetrade_cycle as C

REGISTRY = 'organisation/execution-20261014/cycles.json'
AUTHORITY = 'docs/collaboration/instructions/CHAINE_CYCLES_2026-10-14_EXECUTEUR.md'
PLAN = 'organisation/plan_tetrade_30_cycles.json'
CAHIER = 'organisation/execution-20261014/cahier-cycle2.json'
JOURNAL = 'organisation/execution-20261014/journal.jsonl'
DEADLINE = '2026-10-14T06:00:00+00:00'
LAST_START = '2026-10-14T05:30:00+00:00'
PROMPTS = ('PROMPT_MEDINA.md', 'PROMPT_TRANSITION.md', 'docs/STYLE_REDACTION.md', AUTHORITY, C.CLARITY_AUTHORITY)
PROOFS = ('author', 'cross_audit', 'counter_audit', 'control', 'injection', 'publication')
CROSS = {'NEUR': 'HEM', 'HEM': 'NEUR', 'ENDO': 'NEPH', 'NEPH': 'ENDO'}


def missions(tree, number):
    plan = C.read_json(tree, PLAN)
    C.require(isinstance(number, int) and 2 <= number <= 30, 'Chaîne : numéro de cycle non autorisé')
    return [(s['chapters'][number - 1][0], s['id'], s['tag']) for s in plan['systems']]


def records(tree):
    data = C.read_json(tree, REGISTRY, False)
    if data is None:
        return None
    C.require(data.get('schema_version') == 1 and data.get('authority') == AUTHORITY,
              'Chaîne : schéma ou autorité incorrect')
    C.require(data.get('authority_sha256') == C.digest(tree.read(AUTHORITY)) and
              data.get('plan_sha256') == C.digest(tree.read(PLAN)), 'Chaîne : autorité ou plan différent')
    C.require(data.get('deadline') == DEADLINE and data.get('latest_start') == LAST_START,
              'Chaîne : échéance modifiée')
    assignments = data.get('assignments')
    C.require(isinstance(assignments, list), 'Chaîne : affectations absentes')
    active = [a for a in assignments if a.get('active') is True]
    C.require(all(a.get('owner') in {'Codex', 'Claude'} and isinstance(a.get('cycle'), int) for a in assignments),
              'Chaîne : affectation invalide')
    C.require(len({a['owner'] for a in active}) == len(active), 'Chaîne : une IA ne peut avoir deux cycles actifs')
    C.require(len({a['cycle'] for a in active}) == len(active), 'Chaîne : responsabilité simultanée interdite')
    C.require(any(a.get('cycle') == 1 and a.get('owner') == 'Claude' for a in assignments) and
              not any(a.get('cycle') == 1 and a.get('owner') == 'Codex' and a.get('active') for a in assignments),
              'Chaîne : Cycle 1 réservé à Claude')
    cycles = data.get('cycles')
    C.require(isinstance(cycles, list) and cycles and [r.get('cycle') for r in cycles] == list(range(2, 2+len(cycles))),
              'Chaîne : cycles consécutifs depuis Cycle 2 requis')
    for cycle in cycles:
        n = cycle['cycle']
        C.require(cycle.get('state') in {'ACTIF', 'CLOTURE', 'ARRETE'} and cycle.get('owner') == 'Codex',
                  'Chaîne : état ou responsable invalide')
        C.require(C.dated(cycle.get('started_at')) < C.dated(LAST_START), 'Chaîne : cycle commencé après 07 h 30')
        rows = cycle.get('chapters')
        C.require(isinstance(rows, list) and len(rows) == 4, 'Chaîne : exactement quatre leçons requises')
        for row, (code, fragment, tag) in zip(rows, missions(tree, n)):
            C.require((row.get('code'), row.get('fragment_id'), row.get('production_cycle')) == (code, fragment, n),
                      'Chaîne : identité ou ordre des quatre leçons incorrect')
            C.require(row.get('writer') == f'C{n:02d}-R-{tag}' and
                      row.get('cross_reviewer') == f'C{n:02d}-R-{CROSS[tag]}' and
                      row.get('counter_reviewer') == f'C{n:02d}-CA-{tag}', 'Chaîne : indépendance des missions incorrecte')
            C.require(row.get('status') in C.STATES and all(k in row for k in PROOFS), 'Chaîne : statut ou champs de preuve absents')
        if cycle['state'] == 'ACTIF':
            C.require(any(a['owner'] == 'Codex' and a['cycle'] == n for a in active), 'Chaîne : cycle actif sans affectation exclusive')
        if cycle['state'] == 'CLOTURE':
            C.require(all(r['status'] == 'PUBLIE_VERIFIE' for r in rows), 'Chaîne : clôture prématurée')
        if n > 2:
            previous = cycles[n-3]
            elapsed = (C.dated(previous.get('closed_at')) - C.dated(previous['started_at'])).total_seconds() / 60
            C.require(elapsed > 0 and C.dated(cycle['started_at']) >= C.dated(previous['closed_at']), 'Chaîne : ordre de clôture/démarrage invalide')
            C.require(previous['state'] == 'CLOTURE', 'Chaîne : cycle précédent non clôturé')
            budget = cycle.get('budget')
            C.require(isinstance(budget, dict) and abs(budget.get('observed_previous_minutes', 0) - elapsed) < 0.01 and
                      budget.get('prudent_minutes', 0) >= budget['observed_previous_minutes'], 'Chaîne : durée prudente non justifiée')
            from datetime import timedelta
            C.require(C.dated(cycle['started_at']) + timedelta(minutes=budget['prudent_minutes']) <= C.dated(LAST_START),
                      'Chaîne : durée prudente dépasse 07 h 30')
    C.require(sum(c['state'] == 'ACTIF' for c in cycles) <= 1, 'Chaîne : deux cycles Codex actifs')
    return data


def image_proof(tree, row):
    manifest = C.proof(tree, row.get('images'), row['code'] + ' images')
    images = manifest.get('images')
    C.require(isinstance(images, list) and images, 'Images : manifeste vide')
    if row['production_cycle'] == 2:
        lesson = next(x for x in C.read_json(tree, CAHIER)['lessons'] if x['code'] == row['code'])
        expected_images = {im['id']: im for p in lesson['parts'] for im in p['images']}
        expected = set(expected_images)
        C.require(len(images) == len(expected) and {i.get('id') for i in images} == expected,
                  'Images : emplacements du cahier incomplets')
    paths = {}
    html = b'\n'.join(tree.read(row['source_dir'] + '/' + p) for p in row['files'] if p.endswith('.html')).decode('utf-8')
    from html.parser import HTMLParser
    class ImageParser(HTMLParser):
        def __init__(self):
            super().__init__(); self.images = []; self.ids = set()
        def handle_starttag(self, tag, attrs):
            data = dict(attrs)
            if data.get('id'): self.ids.add(data['id'])
            if tag == 'img': self.images.append(data)
    parsed = ImageParser(); parsed.feed(html)
    for im in images:
        for field in ('source_page_url', 'file_url', 'author', 'license', 'attribution', 'caption', 'alt', 'location', 'path', 'sha256'):
            C.require(isinstance(im.get(field), str) and im[field].strip(), 'Images : provenance incomplète ' + field)
        C.require(im['source_page_url'].startswith('https://') and im['file_url'].startswith('https://'), 'Images : URL source invalide')
        C.dated(im.get('accessed_at'))
        C.require(im.get('generated') is False and im.get('open_license_verified') is True and im.get('visual_reviewed') is True,
                  'Images : image publiée, licence ouverte et inspection réelle requises')
        if row['production_cycle'] == 2:
            C.require(im.get('anchor') == expected_images[im['id']]['anchor'] and im['anchor'] in parsed.ids, 'Images : ancre du cahier absente du cours')
        C.require(any(x.get('src', '').endswith(im['path']) and x.get('alt') == im['alt'] for x in parsed.images), 'Images : fichier et texte alternatif absents du HTML')
        prefix = f"assets/img/cycle{row['production_cycle']}/{row['code'].lower()}/"
        C.require(im['path'].startswith(prefix) and '..' not in im['path'].split('/'), 'Images : chemin hors cours')
        raw = tree.read(row['source_dir'] + '/' + im['path'])
        C.require(len(raw) > 100 and C.digest(raw) == im['sha256'], 'Images : fichier absent ou empreinte différente')
        C.require(raw.startswith((b'\x89PNG', b'\xff\xd8', b'GIF8', b'RIFF')) or b'<svg' in raw[:2000], 'Images : type de fichier invalide')
        C.require(im['path'] not in paths, 'Images : fichier dupliqué dans plusieurs emplacements')
        paths[im['path']] = im['sha256']
    return paths


def review_identities(tree, rows):
    author_ids = [C.proof(tree, r['author'], 'Auteur réel')['runtime_agent_id'] for r in rows]
    counter_ids = [C.proof(tree, r['counter_audit'], 'Contre-auditeur réel')['runtime_agent_id'] for r in rows]
    C.require(len(set(author_ids)) == 4 and len(set(counter_ids)) == 4 and not set(author_ids) & set(counter_ids),
              'Chaîne : quatre auteurs et quatre nouveaux contre-auditeurs distincts requis')
    by_actor = {r['writer']: author_ids[i] for i, r in enumerate(rows)}
    C.require(all(C.proof(tree, r['cross_audit'], 'Binôme réel')['runtime_agent_id'] == by_actor[r['cross_reviewer']] for r in rows),
              'Chaîne : identité réelle des binômes croisés différente')


def ready(tree, row, rows):
    files = C.ready(tree, row, rows=rows, prompts=PROMPTS)
    review_identities(tree, rows)
    images = image_proof(tree, row)
    for key in ('author', 'cross_audit', 'counter_audit', 'control'):
        report = C.proof(tree, row[key], row['code'] + ' ' + key)
        C.require(report.get('image_files') == images, 'Images : revue non liée aux images finales')
    return dict(files, **images)


def temporal_proofs(tree, cycle, now):
    start = C.dated(cycle['started_at'])
    C.require(start <= now, 'Chaîne : démarrage futur')
    publication_dates = []
    for row in cycle['chapters']:
        for key in PROOFS:
            if not row[key]: continue
            report = C.proof(tree, row[key], key)
            if key in {'author', 'cross_audit', 'counter_audit', 'control'}:
                dates = [report.get('entry', {}).get('checked_at'), report.get('exit', {}).get('checked_at')]
                for passage in report.get('passes', []):
                    p = C.proof(tree, passage.get('report'), 'Passe datée')
                    dates.extend([p.get('started_at'), p.get('finished_at')])
            else:
                dates = [report.get('checked_at')]
            for value in dates:
                d = C.dated(value)
                C.require(start <= d <= now and d < C.dated(DEADLINE), 'Chaîne : preuve future, antidatée ou hors autorisation')
            if key == 'publication': publication_dates.append(C.dated(report['checked_at']))
    if cycle['state'] == 'CLOTURE':
        closed = C.dated(cycle.get('closed_at'))
        C.require(len(publication_dates) == 4 and max(publication_dates) <= closed <= now and closed < C.dated(DEADLINE),
                  'Chaîne : clôture antérieure aux publications ou future')


def journal_proof(before, after, data, now):
    raw = after.read(JOURNAL)
    previous = before.read(JOURNAL, required=False)
    C.require(previous is None or raw.startswith(previous), 'Chaîne : journal historique réécrit')
    try:
        events = [C.json.loads(line) for line in raw.splitlines() if line.strip()]
    except ValueError:
        raise C.CycleError('Chaîne : journal illisible') from None
    C.require(events, 'Chaîne : journal vide')
    for event in events:
        C.require(C.dated(event.get('at')) <= now, 'Chaîne : événement futur')
    for cycle in data['cycles']:
        C.require(any(e.get('event') == 'cycle_started' and e.get('cycle') == cycle['cycle'] and
                      C.dated(e['at']) == C.dated(cycle['started_at']) and e.get('coordinator_runtime') for e in events),
                  'Chaîne : départ sans événement réel dans le journal')
        for row in cycle['chapters']:
            if row['status'] == 'EN_PRODUCTION': continue
            C.require(any(e.get('event') == 'stage_recorded' and e.get('cycle') == cycle['cycle'] and
                          e.get('code') == row['code'] and e.get('status') == row['status'] and
                          e.get('proofs') == {k: row[k] for k in PROOFS} for e in events),
                      'Chaîne : transition sans preuves dans le journal')


def validate(before, after, now=None):
    now = now or datetime.now(timezone.utc)
    old, new = records(before), records(after)
    if old is None and new is None:
        return {}, set(), set()
    C.require(new is not None, 'Chaîne : suppression du registre interdite')
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    codes = {r['code'] for cycle in new['cycles'] for r in cycle['chapters']}
    course_changes = {p for p in changed if C.managed(p, codes) or any(p.startswith(f"assets/img/cycle{c['cycle']}/") for c in new['cycles'])}
    touched = REGISTRY in changed or bool(course_changes)
    if touched:
        journal_proof(before, after, new, now)
        for cycle in new['cycles']: temporal_proofs(after, cycle, now)
        C.require(now < C.dated(DEADLINE), 'Chaîne : autorisation expirée à 08 h 00')
    if old is None:
        C.require(not course_changes and 'chapters.json' not in changed, 'Chaîne : activation sans injection requise')
        C.require(len(new['cycles']) == 1 and new['cycles'][0]['state'] == 'ACTIF' and
                  all(r['status'] == 'EN_PRODUCTION' and all(r[k] is None for k in PROOFS) for r in new['cycles'][0]['chapters']),
                  'Chaîne : activation sans revue préétablie requise')
        return {}, codes, set()
    for p in (AUTHORITY, PLAN, CAHIER):
        C.require(before.read(p) == after.read(p), 'Chaîne : instruction ou cahier modifié en cours')
    C.require(len(new['cycles']) in {len(old['cycles']), len(old['cycles'])+1}, 'Chaîne : ajout ou retrait de cycles incorrect')
    authorized, catalog_codes, injections = {}, set(), []
    for index, cycle in enumerate(new['cycles']):
        if index == len(old['cycles']):
            C.require(old['cycles'][-1]['state'] == 'CLOTURE', 'Chaîne : démarrage avant clôture')
            C.require(all(r['status'] == 'EN_PRODUCTION' and all(r[k] is None for k in PROOFS) for r in cycle['chapters']),
                      'Chaîne : nouveau cycle avec preuves préétablies')
            C.require(not course_changes, 'Chaîne : nouveau cycle avec injection simultanée')
            continue
        previous_cycle = old['cycles'][index]
        for field in ('cycle', 'owner', 'started_at', 'budget'):
            C.require(cycle.get(field) == previous_cycle.get(field), 'Chaîne : identité ou départ du cycle modifié')
        if previous_cycle['state'] in {'CLOTURE', 'ARRETE'}:
            C.require(cycle == previous_cycle, 'Chaîne : cycle clos ou arrêté immuable')
        rows = cycle['chapters']
        for previous, row in zip(previous_cycle['chapters'], rows):
            stage = C.STATES.index(row['status'])
            C.require(stage >= C.STATES.index(previous['status']), 'Chaîne : régression non tracée')
            if stage >= 1:
                C.require(all(r['author'] for r in rows), 'Chaîne : quatre auteurs avant audit croisé')
            if stage >= 2:
                C.require(all(r['cross_audit'] for r in rows), 'Chaîne : quatre audits croisés avant contre-audit')
            if stage >= 3:
                C.require(all(r['counter_audit'] for r in rows), 'Chaîne : quatre contre-audits avant contrôle')
            if 1 <= stage < 4:
                files = C.source_files(after, row)
                C.review(after, row, 'author', row['writer'], files, PROMPTS)
                if stage >= 2:
                    C.review(after, row, 'cross_audit', row['cross_reviewer'], files, PROMPTS)
                if stage >= 3:
                    C.review(after, row, 'counter_audit', row['counter_reviewer'], files, PROMPTS)
            if C.STATES.index(previous['status']) >= 5:
                C.require(all(row[k] == previous[k] for k in row if k not in {'status', 'publication'}), 'Chaîne : cours injecté modifié')
                locked = dict(previous['files'], **image_proof(before, previous))
                C.require(all(before.read(p) == after.read(p) and C.digest(after.read(p)) == sha for p, sha in locked.items()),
                          'Chaîne : source injectée modifiée')
            if stage >= 4:
                files = ready(after, row, rows)
                if C.STATES.index(previous['status']) < 5 and stage >= 5:
                    C.require(previous['status'] == 'PRET_A_INJECTER' and row['status'] == 'INJECTE' and row['publication'] is None,
                              'Chaîne : contrôle préexistant et publication distincte requis')
                    receipt = C.proof(after, row['injection'], 'Injection')
                    C.require(receipt.get('code') == row['code'] and receipt.get('files') == files and
                              receipt.get('injector') == 'Codex — coordinateur du fil', 'Chaîne : reçu injection invalide')
                    C.require(all(C.digest(after.read(p)) == sha for p, sha in files.items()), 'Chaîne : injection différente des revues')
                    injections.append((previous_cycle, row)); authorized.update(files); catalog_codes.add(row['code'])
            if stage == 6:
                pub = C.proof(after, row['publication'], 'Publication')
                C.require(pub.get('code') == row['code'] and pub.get('deployment_status') == 'success' and
                          pub.get('readback') is True and pub.get('gauges') is True and
                          C.re.fullmatch(r'[0-9a-f]{40}', pub.get('main_sha', '')) and
                          pub.get('public_url', '').startswith('https://vialdjoukang-spec.github.io/Medina/fragments/'),
                          'Chaîne : publication non vérifiée')
        if cycle['state'] == 'CLOTURE':
            closure = C.proof(after, cycle.get('closure'), 'Clôture')
            C.require(closure.get('blocking_reserves') == [] and closure.get('cycle') == cycle['cycle'], 'Chaîne : clôture avec réserves')
    C.require(len(injections) <= 1, 'Chaîne : une seule injection à la fois')
    if injections:
        prior, row = injections[0]; idx = [r['code'] for r in prior['chapters']].index(row['code'])
        C.require(all(r['status'] == 'PUBLIE_VERIFIE' for r in prior['chapters'][:idx]) and
                  all(r['status'] == 'PRET_A_INJECTER' for r in prior['chapters'][idx:]), 'Chaîne : ordre de publication ou quatre cours prêts non respecté')
        C.require(course_changes == set(authorized), 'Chaîne : fichiers injectés manquants ou supplémentaires')
        original, catalog = C.read_json(before, 'chapters.json'), C.read_json(after, 'chapters.json')
        additions = [r for r in catalog if r not in original]
        C.require(len(catalog) == len(original)+1 and all(r in catalog for r in original) and len(additions) == 1 and
                  additions[0].get('code') == row['code'] and additions[0].get('covers') == [row['code']] and
                  additions[0].get('integrated') is True, 'Chaîne : catalogue ajout unique requis')
        authorized['chapters.json'] = C.digest(after.read('chapters.json'))
    else:
        C.require(not course_changes, 'Chaîne : source sans injection contrôlée')
        if 'chapters.json' in changed:
            C.require([r for r in C.read_json(before, 'chapters.json') if r.get('code') in codes] ==
                      [r for r in C.read_json(after, 'chapters.json') if r.get('code') in codes], 'Chaîne : catalogue modifié sans injection')
    return authorized, codes, catalog_codes
