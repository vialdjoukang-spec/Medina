"""Garde des cycles repris ou produits par Claude (instruction de Vial du 14 octobre 2026).

Autorité : docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md.
Reprend la chaîne de preuves de tools/night_cycle.py sans échéance horaire, avec un
coordinateur Claude et quatre captures réelles par leçon. Elle contrôle la cohérence
des reçus, pas leur vérité médicale ; une revue IA n'est pas une validation humaine.
Registre absent : garde inactive.
"""
from datetime import datetime, timezone

try:
    from tools import tetrade_cycle as C
    from tools import night_cycle as N
except ModuleNotFoundError:
    import tetrade_cycle as C
    import night_cycle as N

REGISTRY = 'organisation/CYCLES_CLAUDE.json'
JOURNAL = 'organisation/CYCLES_CLAUDE_journal.jsonl'
AUTHORITY = 'docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md'
PLAN = N.PLAN
CAHIER = N.CAHIER
COORDINATOR = 'Claude — coordinateur'
NOT_BEFORE = '2026-10-14T20:29:00+00:00'
PROMPTS = ('PROMPT_MEDINA.md', 'PROMPT_TRANSITION.md', 'docs/STYLE_REDACTION.md', AUTHORITY, C.CLARITY_AUTHORITY)
PROOFS = N.PROOFS
CAPTURES = 4
SOURCE_ROOTS = ('livraisons/Livraison Codex/', 'livraisons/Livraison Claude/')
ROW_FIELDS = ('code', 'fragment_id', 'production_cycle', 'writer', 'cross_reviewer', 'counter_reviewer',
              'status', 'source_dir', 'files', 'images') + PROOFS


def transferred_cycles(tree):
    """Numéros des cycles Codex déclarés repris par Claude dans ``tree`` (registre présent seulement).

    Seule entrée utilisée par night_cycle ; la validité complète du registre relève de validate().
    """
    data = C.read_json(tree, REGISTRY, False)
    if not isinstance(data, dict) or not isinstance(data.get('cycles'), list):
        return set()
    return {c['cycle'] for c in data['cycles'] if isinstance(c, dict) and isinstance(c.get('cycle'), int)
            and c.get('owner') == 'Claude' and c.get('transferred_from') == 'Codex'}


def records(tree):
    data = C.read_json(tree, REGISTRY, False)
    if data is None:
        return None
    C.require(isinstance(data, dict) and data.get('schema_version') == 1 and data.get('authority') == AUTHORITY,
              'Cycles Claude : schéma ou autorité incorrect')
    C.require(data.get('authority_sha256') == C.digest(tree.read(AUTHORITY)) and
              data.get('plan_sha256') == C.digest(tree.read(PLAN)), 'Cycles Claude : autorité ou plan différent')
    C.require(data.get('coordinator') == COORDINATOR and data.get('not_before') == NOT_BEFORE,
              'Cycles Claude : coordinateur ou date d’autorisation modifiés')
    cycles = data.get('cycles')
    C.require(isinstance(cycles, list) and cycles and all(isinstance(c, dict) for c in cycles), 'Cycles Claude : cycles absents')
    first = cycles[0].get('cycle')
    C.require(isinstance(first, int) and first >= 2 and [c.get('cycle') for c in cycles] == list(range(first, first + len(cycles))),
              'Cycles Claude : cycles consécutifs requis')
    codex = C.read_json(tree, N.REGISTRY, False) or {}
    codex_cycles = {c.get('cycle'): c for c in codex.get('cycles', []) if isinstance(c, dict)}
    for index, cycle in enumerate(cycles):
        n = cycle['cycle']
        C.require(cycle.get('owner') == 'Claude' and cycle.get('state') in {'ACTIF', 'CLOTURE'} and cycle.get('budget') is None,
                  'Cycles Claude : responsable, état ou budget invalide')
        C.require(C.dated(cycle.get('started_at')) >= C.dated(NOT_BEFORE), 'Cycles Claude : départ antérieur à l’autorisation')
        if cycle.get('transferred_from') == 'Codex':
            C.require(index == 0, 'Cycles Claude : seul le premier cycle peut être repris')
            C.require(n in codex_cycles and codex_cycles[n].get('owner') == 'Codex' and codex_cycles[n].get('state') != 'CLOTURE',
                      'Cycles Claude : reprise d’un cycle Codex inexistant ou clos')
            C.proof(tree, cycle.get('handover'), 'Remise Codex vers Claude')
        else:
            C.require(cycle.get('transferred_from') is None and cycle.get('handover') is None,
                      'Cycles Claude : reprise non déclarée correctement')
            C.require(n not in codex_cycles, 'Cycles Claude : cycle déjà attribué à Codex')
        rows = cycle.get('chapters')
        C.require(isinstance(rows, list) and len(rows) == 4, 'Cycles Claude : exactement quatre leçons requises')
        for row, (code, fragment, tag) in zip(rows, N.missions(tree, n)):
            C.require(isinstance(row, dict) and all(k in row for k in ROW_FIELDS), 'Cycles Claude : champs de leçon absents')
            C.require((row['code'], row['fragment_id'], row['production_cycle']) == (code, fragment, n),
                      'Cycles Claude : identité ou ordre des quatre leçons incorrect')
            C.require(row['writer'] == f'C{n:02d}-R-{tag}' and row['cross_reviewer'] == f'C{n:02d}-R-{N.CROSS[tag]}' and
                      row['counter_reviewer'] == f'C{n:02d}-CA-{tag}', 'Cycles Claude : indépendance des missions incorrecte')
            C.require(row['status'] in C.STATES and all(row[k] is None or isinstance(row[k], dict) for k in PROOFS),
                      'Cycles Claude : statut ou preuve invalide')
        if cycle['state'] == 'CLOTURE':
            C.require(all(r['status'] == 'PUBLIE_VERIFIE' for r in rows), 'Cycles Claude : clôture prématurée')
            C.dated(cycle.get('closed_at'))
        else:
            C.require(cycle.get('closed_at') is None and cycle.get('closure') is None, 'Cycles Claude : clôture d’un cycle actif')
        if index:
            previous = cycles[index - 1]
            C.require(previous['state'] == 'CLOTURE', 'Cycles Claude : cycle précédent non clôturé')
            C.require(C.dated(cycle['started_at']) >= C.dated(previous['closed_at']), 'Cycles Claude : démarrage avant clôture')
    C.require(sum(c['state'] == 'ACTIF' for c in cycles) <= 1, 'Cycles Claude : deux cycles actifs')
    return data


def cross_boundary(tree, cycle, now):
    completed = N.cross_boundary(tree, cycle, now, deadline=None)
    C.require(completed >= C.dated(cycle['started_at']), 'Cycles Claude : clôture croisée antérieure au cycle')
    return completed


def ready(tree, row, rows, cross_completed_at=None):
    files = C.ready(tree, row, rows=rows, prompts=PROMPTS, cross_completed_at=cross_completed_at,
                    control_actor=COORDINATOR, captures=CAPTURES, source_roots=SOURCE_ROOTS)
    N.review_identities(tree, rows)
    images = N.image_proof(tree, row)
    for key in ('author', 'cross_audit', 'counter_audit', 'control'):
        report = C.proof(tree, row[key], row['code'] + ' ' + key)
        C.require(report.get('image_files') == images, 'Images : revue non liée aux images finales')
    return dict(files, **images)


def temporal_proofs(tree, cycle, now):
    start = C.dated(cycle['started_at'])
    floor = max(start, C.dated(NOT_BEFORE))
    C.require(start <= now, 'Cycles Claude : démarrage futur')

    def within(value):
        C.require(floor <= C.dated(value) <= now, 'Cycles Claude : preuve future, antidatée ou antérieure à l’autorisation')

    def review_dates(report):
        within(report.get('entry', {}).get('checked_at'))
        within(report.get('exit', {}).get('checked_at'))
        for passage in report.get('passes', []):
            p = C.proof(tree, passage.get('report'), 'Passe datée')
            within(p.get('started_at')); within(p.get('finished_at'))

    publications = []
    for row in cycle['chapters']:
        for key in PROOFS:
            if not row[key]:
                continue
            report = C.proof(tree, row[key], key)
            if key in {'author', 'cross_audit', 'counter_audit', 'control'}:
                review_dates(report)
                if report.get('corrections_recheck'):
                    within(C.proof(tree, report['corrections_recheck'], 'Relecture des corrections').get('checked_at'))
            else:
                within(report.get('checked_at'))
            if key == 'publication':
                publications.append(C.dated(report['checked_at']))
    if cycle.get('cross_phase'):
        phase = C.proof(tree, cycle['cross_phase'], 'Clôture initiale des audits croisés')
        within(phase.get('completed_at'))
        for item in phase.get('reviews') or []:
            review_dates(C.proof(tree, item.get('review'), 'Revue croisée initiale archivée'))
    if cycle['state'] == 'CLOTURE':
        closed = C.dated(cycle['closed_at'])
        C.require(len(publications) == 4 and max(publications) <= closed <= now,
                  'Cycles Claude : clôture antérieure aux publications ou future')


def validate(before, after, now=None):
    now = now or datetime.now(timezone.utc)
    old, new = records(before), records(after)
    if old is None and new is None:
        return {}, set(), set()
    C.require(new is not None, 'Cycles Claude : suppression du registre interdite')
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    codes = {r['code'] for cycle in new['cycles'] for r in cycle['chapters']}
    course_changes = {p for p in changed if C.managed(p, codes) or
                      any(p.startswith(f"assets/img/cycle{c['cycle']}/") for c in new['cycles'])}
    if REGISTRY in changed or JOURNAL in changed or course_changes:
        N.journal_proof(before, after, new, now, journal=JOURNAL)
        for cycle in new['cycles']:
            temporal_proofs(after, cycle, now)
    if old is None:
        C.require(not course_changes and 'chapters.json' not in changed, 'Cycles Claude : activation sans injection requise')
        cycle = new['cycles'][0]
        C.require(len(new['cycles']) == 1 and cycle['state'] == 'ACTIF' and cycle.get('cross_phase') is None and
                  all(r['status'] == 'EN_PRODUCTION' and all(r[k] is None for k in PROOFS) for r in cycle['chapters']),
                  'Cycles Claude : activation sans revue préétablie requise')
        return {}, codes, set()
    for key in ('schema_version', 'authority', 'coordinator', 'not_before'):
        C.require(old.get(key) == new.get(key), 'Cycles Claude : autorisation modifiée')
    C.require(before.read(CAHIER) == after.read(CAHIER), 'Cycles Claude : cahier du cycle 2 modifié')
    if any(c['state'] == 'ACTIF' for c in old['cycles'] + new['cycles']):
        for p in (AUTHORITY, PLAN):
            C.require(before.read(p) == after.read(p), 'Cycles Claude : instruction ou plan modifié pendant un cycle actif')
    C.require(len(new['cycles']) in {len(old['cycles']), len(old['cycles']) + 1} and
              new['cycles'][0]['cycle'] == old['cycles'][0]['cycle'], 'Cycles Claude : ajout ou retrait de cycles incorrect')
    authorized, catalog_codes, injections = {}, set(), []
    for index, cycle in enumerate(new['cycles']):
        if index == len(old['cycles']):
            C.require(old['cycles'][-1]['state'] == 'CLOTURE', 'Cycles Claude : démarrage avant clôture')
            C.require(cycle.get('cross_phase') is None and
                      all(r['status'] == 'EN_PRODUCTION' and all(r[k] is None for k in PROOFS) for r in cycle['chapters']),
                      'Cycles Claude : nouveau cycle avec preuves préétablies')
            C.require(not course_changes, 'Cycles Claude : nouveau cycle avec injection simultanée')
            continue
        previous_cycle = old['cycles'][index]
        for field in ('cycle', 'owner', 'started_at', 'budget', 'transferred_from', 'handover'):
            C.require(cycle.get(field) == previous_cycle.get(field), 'Cycles Claude : identité ou départ du cycle modifié')
        if previous_cycle['state'] == 'CLOTURE':
            C.require(cycle == previous_cycle, 'Cycles Claude : cycle clos immuable')
        rows = cycle['chapters']
        if previous_cycle.get('cross_phase') is not None:
            C.require(cycle.get('cross_phase') == previous_cycle['cross_phase'], 'Cycles Claude : clôture initiale croisée réécrite')
        boundary = cross_boundary(after, cycle, now) if any(C.STATES.index(r['status']) >= 2 for r in rows) else None
        for previous, row in zip(previous_cycle['chapters'], rows):
            stage = C.STATES.index(row['status'])
            C.require(stage >= C.STATES.index(previous['status']), 'Cycles Claude : régression non tracée')
            if stage >= 1:
                C.require(all(r['author'] for r in rows), 'Cycles Claude : quatre auteurs avant audit croisé')
            if stage >= 2:
                C.require(all(r['cross_audit'] for r in rows), 'Cycles Claude : quatre audits croisés avant contre-audit')
            if stage >= 3:
                C.require(all(r['counter_audit'] for r in rows), 'Cycles Claude : quatre contre-audits avant contrôle')
            if 1 <= stage < 4:
                files = C.source_files(after, row, SOURCE_ROOTS)
                C.review(after, row, 'author', row['writer'], files, PROMPTS)
                if stage >= 2:
                    C.review(after, row, 'cross_audit', row['cross_reviewer'], files, PROMPTS)
                if stage >= 3:
                    C.review(after, row, 'counter_audit', row['counter_reviewer'], files, PROMPTS)
            if C.STATES.index(previous['status']) >= 5:
                C.require(all(row[k] == previous[k] for k in row if k not in {'status', 'publication'}),
                          'Cycles Claude : cours injecté modifié')
                locked = dict(previous['files'], **N.image_proof(before, previous))
                C.require(all(before.read(p) == after.read(p) and C.digest(after.read(p)) == sha for p, sha in locked.items()),
                          'Cycles Claude : source injectée modifiée')
            if stage >= 4:
                files = ready(after, row, rows, cross_completed_at=boundary)
                if C.STATES.index(previous['status']) < 5 and stage >= 5:
                    C.require(previous['status'] == 'PRET_A_INJECTER' and row['status'] == 'INJECTE' and row['publication'] is None,
                              'Cycles Claude : contrôle préexistant et publication distincte requis')
                    receipt = C.proof(after, row['injection'], 'Injection')
                    C.require(receipt.get('code') == row['code'] and receipt.get('files') == files and
                              receipt.get('injector') == COORDINATOR, 'Cycles Claude : reçu injection invalide')
                    C.require(all(C.digest(after.read(p)) == sha for p, sha in files.items()),
                              'Cycles Claude : injection différente des revues')
                    injections.append((previous_cycle, row)); authorized.update(files); catalog_codes.add(row['code'])
            if stage == 6:
                pub = C.proof(after, row['publication'], 'Publication')
                C.require(pub.get('code') == row['code'] and pub.get('deployment_status') == 'success' and
                          pub.get('readback') is True and pub.get('gauges') is True and
                          C.re.fullmatch(r'[0-9a-f]{40}', pub.get('main_sha', '')) and
                          pub.get('public_url', '').startswith('https://vialdjoukang-spec.github.io/Medina/fragments/'),
                          'Cycles Claude : publication non vérifiée')
        if cycle['state'] == 'CLOTURE':
            closure = C.proof(after, cycle.get('closure'), 'Clôture')
            C.require(closure.get('blocking_reserves') == [] and closure.get('cycle') == cycle['cycle'],
                      'Cycles Claude : clôture avec réserves')
    C.require(len(injections) <= 1, 'Cycles Claude : une seule injection à la fois')
    if injections:
        prior, row = injections[0]
        idx = [r['code'] for r in prior['chapters']].index(row['code'])
        C.require(all(r['status'] == 'PUBLIE_VERIFIE' for r in prior['chapters'][:idx]) and
                  all(r['status'] == 'PRET_A_INJECTER' for r in prior['chapters'][idx:]),
                  'Cycles Claude : ordre de publication ou quatre cours prêts non respecté')
        C.require(course_changes == set(authorized), 'Cycles Claude : fichiers injectés manquants ou supplémentaires')
        original, catalog = C.read_json(before, 'chapters.json'), C.read_json(after, 'chapters.json')
        additions = [r for r in catalog if r not in original]
        C.require(len(catalog) == len(original) + 1 and all(r in catalog for r in original) and len(additions) == 1 and
                  additions[0].get('code') == row['code'] and additions[0].get('covers') == [row['code']] and
                  additions[0].get('integrated') is True and additions[0].get('production_cycle') == row['production_cycle'],
                  'Cycles Claude : catalogue ajout unique requis')
        authorized['chapters.json'] = C.digest(after.read('chapters.json'))
    else:
        C.require(not course_changes, 'Cycles Claude : source sans injection contrôlée')
        if 'chapters.json' in changed:
            C.require([r for r in C.read_json(before, 'chapters.json') if r.get('code') in codes] ==
                      [r for r in C.read_json(after, 'chapters.json') if r.get('code') in codes],
                      'Cycles Claude : catalogue modifié sans injection')
    return authorized, codes, catalog_codes
