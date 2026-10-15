"""Garde des cycles repris ou produits par Claude (instruction de Vial du 14 octobre 2026).

Autorité : docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md.
Reprend la chaîne de preuves de tools/night_cycle.py sans échéance horaire, avec un
coordinateur Claude et quatre captures réelles par leçon. Elle contrôle la cohérence
des reçus, pas leur vérité médicale ; une revue IA n'est pas une validation humaine.
Registre absent : garde inactive.

Publication directe (cycles 3 à 30, autorité DIRECT_AUTHORITY du 14 octobre 2026) : exception bornée
sur le modèle du Cycle 1. Un cycle la déclare par ``mode: "publication_directe"`` avec ``authority`` et
``authority_sha256`` figés ; le Cycle 2 et tout cycle sans ce mode gardent la chaîne complète. Les
revues auteur et contrôle relisent PROMPTS_DIRECT : PROMPTS où l'autorité de reprise du Cycle 2 (qui
décrit audits croisés et contre-audits) est remplacée par l'autorité de publication directe, afin
qu'aucune revue n'atteste un Prompt contradictoire. États : EN_PRODUCTION, EN_CONTROLE,
PRET_A_INJECTER, INJECTE, PUBLIE_VERIFIE ; cross_audit et counter_audit restent null (aucun audit
fictif) ; le catalogue porte provisional_injection, audit_deferred="apres_cycle_30" et production_cycle.

Cycle 2 (section « Clôture immédiate du Cycle 2 et suite sans lecture croisée » de la même autorité) :
passage unique du Cycle 2 actif en publication directe, tracé au journal (événement mode_changed), tant
qu'aucune leçon n'a quitté EN_PRODUCTION ni reçu de preuve. Mêmes exigences que les cycles 3 à 30, images
selon le cahier du Cycle 2 ; les revues croisées partielles restent un historique non référencé.
"""
from datetime import datetime, timezone

try:
    from tools import tetrade_cycle as C
    from tools import night_cycle as N
    from tools import novo_cycle as V
except ModuleNotFoundError:
    import tetrade_cycle as C
    import night_cycle as N
    import novo_cycle as V

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
DIRECT_MODE = 'publication_directe'
DIRECT_AUTHORITY = 'docs/collaboration/instructions/CYCLES_03_30_PUBLICATION_DIRECTE_VIAL_2026-10-14.md'
DIRECT_CYCLES = range(3, 31)
DIRECT_DEFERRED = 'apres_cycle_30'
SWITCH_CYCLES = (2,)
PROMPTS_DIRECT = tuple(DIRECT_AUTHORITY if p == AUTHORITY else p for p in PROMPTS)
PROMPTS_NOVO = PROMPTS_DIRECT + (V.TRUTH, V.AUTHORITY)
DIRECT_FORBIDDEN = ('EN_AUDIT_CROISE', 'EN_CONTRE_AUDIT')
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


def author_prompts(row):
    """Revue auteur : le Cycle 2 a été rédigé sous l'autorité de reprise (PROMPTS) avant son passage en
    publication directe ; les cycles 3 à 30 sous PROMPTS_DIRECT. Le contrôle reste toujours en PROMPTS_DIRECT."""
    return PROMPTS_NOVO if row.get('novo') else (PROMPTS if row['production_cycle'] in SWITCH_CYCLES else PROMPTS_DIRECT)


def control_prompts(row):
    return PROMPTS_NOVO if row.get('novo') else PROMPTS_DIRECT


def cycle_numbers(cycle):
    return cycle['tetrad_cycles'] if cycle.get('novo') else [cycle['cycle']]


def direct(cycle):
    return cycle.get('mode') == DIRECT_MODE


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
    C.require(type(first) is int and first >= 2 and all(type(c.get('cycle')) is int for c in cycles),
              'Cycles Claude : cycles consécutifs requis')
    codex = C.read_json(tree, N.REGISTRY, False) or {}
    codex_cycles = {c.get('cycle'): c for c in codex.get('cycles', []) if isinstance(c, dict)}
    for index, cycle in enumerate(cycles):
        n = cycle['cycle']
        missions = (V.validate_cycle(tree, cycle) if cycle.get('novo') is not None else
                    [(code, fragment, tag, n) for code, fragment, tag in N.missions(tree, n)])
        if index:
            C.require(n == cycle_numbers(cycles[index - 1])[-1] + 1,
                      'Cycles Claude : cycles consécutifs requis')
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
            C.require(all(number not in codex_cycles for number in cycle_numbers(cycle)),
                      'Cycles Claude : cycle déjà attribué à Codex')
        if cycle.get('mode') is None:
            C.require(cycle.get('authority') is None and cycle.get('authority_sha256') is None,
                      'Cycles Claude : autorité propre sans mode déclaré')
        else:
            C.require(cycle.get('authority') == DIRECT_AUTHORITY and
                      cycle.get('authority_sha256') == C.digest(tree.read(DIRECT_AUTHORITY)),
                      'Cycles Claude : autorité de publication directe absente ou différente')
            C.require(direct(cycle), 'Cycles Claude : mode inconnu')
            if n in SWITCH_CYCLES:
                C.require(index == 0, 'Cycles Claude : Cycle 2 en publication directe par changement de mode seulement')
            else:
                C.require(n in DIRECT_CYCLES and cycle.get('transferred_from') is None,
                          'Cycles Claude : publication directe réservée aux cycles 2 à 30')
                C.require(index > 0, 'Cycles Claude : publication directe après un cycle Claude clôturé seulement')
            C.require(cycle.get('cross_phase') is None, 'Cycles Claude : phase croisée fictive en publication directe')
        rows = cycle.get('chapters')
        C.require(isinstance(rows, list) and len(rows) == len(missions),
                  'Cycles Claude : exactement douze leçons Novo requises' if cycle.get('novo') else
                  'Cycles Claude : exactement quatre leçons requises')
        for row, (code, fragment, tag, production_cycle) in zip(rows, missions):
            C.require(isinstance(row, dict) and all(k in row for k in ROW_FIELDS), 'Cycles Claude : champs de leçon absents')
            C.require((row['code'], row['fragment_id'], row['production_cycle']) == (code, fragment, production_cycle)
                      and row.get('novo') == cycle.get('novo'),
                      'Cycles Claude : identité ou ordre des quatre leçons incorrect')
            reviewers = (None, None) if direct(cycle) else (f'C{n:02d}-R-{N.CROSS[tag]}', f'C{n:02d}-CA-{tag}')
            C.require(row['writer'] == f'C{production_cycle:02d}-R-{tag}' and (row['cross_reviewer'], row['counter_reviewer']) == reviewers,
                      'Cycles Claude : indépendance des missions incorrecte')
            C.require(row['status'] in C.STATES and all(row[k] is None or isinstance(row[k], dict) for k in PROOFS),
                      'Cycles Claude : statut ou preuve invalide')
            if direct(cycle):
                C.require(row['status'] not in DIRECT_FORBIDDEN and row['cross_audit'] is None and row['counter_audit'] is None,
                          'Cycles Claude : audit croisé ou contre-audit fictif en publication directe')
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


def direct_ready(tree, row):
    """Preuves d'une leçon en publication directe : auteur, sources, images, contrôle, quatre captures."""
    files = C.source_files(tree, row, SOURCE_ROOTS)
    C.require(row['cross_audit'] is None and row['counter_audit'] is None,
              'Cycles Claude : audit croisé ou contre-audit fictif en publication directe')
    author = C.review(tree, row, 'author', row['writer'], files, author_prompts(row))
    C.source_ledger_proof(tree, row, author, files)
    if row.get('novo'):
        V.research_proof(tree, row, author)
    control = C.review(tree, row, 'control', COORDINATOR, files, control_prompts(row))
    C.require(C.dated(author['exit']['checked_at']) <= C.dated(control['entry']['checked_at']),
              'Cycles Claude : contrôle engagé avant la sortie de l’auteur')
    C.require(author['runtime_agent_id'] != control['runtime_agent_id'], 'Cycles Claude : auteur et coordinateur distincts requis')
    C.technical_proof(tree, row, control, files, CAPTURES)
    if __package__ == 'tools':
        from tools.espace import swiss_context_proof
    else:
        from espace import swiss_context_proof
    swiss_context_proof(tree, {'swiss_context': control.get('swiss_context')}, row['fragment_id'], files,
                        scope='chapter', chapter_code=row['code'])
    images = N.image_proof(tree, row)
    for report in (author, control):
        C.require(report.get('image_files') == images, 'Images : revue non liée aux images finales')
    return dict(files, **images)


def mode_change(after, previous_cycle, cycle, now):
    """Unique passage du Cycle 2 actif en publication directe, tracé au journal, sans autre changement."""
    C.require(previous_cycle.get('mode') is None and direct(cycle) and cycle['cycle'] in SWITCH_CYCLES and
              previous_cycle['state'] == 'ACTIF' and cycle['state'] == 'ACTIF', 'Cycles Claude : changement de mode non autorisé')
    for previous, row in zip(previous_cycle['chapters'], cycle['chapters']):
        C.require(previous['status'] == 'EN_PRODUCTION' and all(previous[k] is None for k in PROOFS),
                  'Cycles Claude : changement de mode après le début des revues')
        C.require(dict(row, cross_reviewer=previous['cross_reviewer'], counter_reviewer=previous['counter_reviewer']) == previous,
                  'Cycles Claude : changement de mode simultané à une autre transition')
    C.require({k: v for k, v in cycle.items() if k not in {'mode', 'authority', 'authority_sha256', 'chapters'}} ==
              {k: v for k, v in previous_cycle.items() if k not in {'mode', 'authority', 'authority_sha256', 'chapters'}},
              'Cycles Claude : changement de mode simultané à une autre transition')
    events = [C.json.loads(line) for line in after.read(JOURNAL).splitlines() if line.strip()]
    C.require(any(e.get('event') == 'mode_changed' and e.get('cycle') == cycle['cycle'] and e.get('mode') == DIRECT_MODE and
                  e.get('authority_sha256') == cycle['authority_sha256'] and e.get('coordinator_runtime') and
                  C.dated(cycle['started_at']) <= C.dated(e.get('at')) <= now for e in events),
              'Cycles Claude : changement de mode absent du journal')


def temporal_proofs(tree, cycle, now):
    start = C.dated(cycle['started_at'])
    # Un cycle repris (Cycle 2) a commencé à la remise, avant son inscription au registre :
    # ses preuves datent au plus tôt de l'autorisation, jamais de la chaîne nocturne expirée.
    floor = C.dated(NOT_BEFORE) if cycle.get('transferred_from') else max(start, C.dated(NOT_BEFORE))
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
        C.require(len(publications) == len(cycle['chapters']) and max(publications) <= closed <= now,
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
                      any(p.startswith(f"assets/img/cycle{n}/") for c in new['cycles'] for n in cycle_numbers(c))}
    if REGISTRY in changed or JOURNAL in changed or course_changes:
        N.journal_proof(before, after, new, now, journal=JOURNAL)
        for cycle in new['cycles']:
            temporal_proofs(after, cycle, now)
    if old is None:
        C.require(not course_changes and 'chapters.json' not in changed, 'Cycles Claude : activation sans injection requise')
        cycle = new['cycles'][0]
        C.require(len(new['cycles']) == 1 and cycle['state'] == 'ACTIF' and cycle.get('cross_phase') is None and
                  cycle.get('mode') is None and
                  all(r['status'] == 'EN_PRODUCTION' and all(r[k] is None for k in PROOFS) for r in cycle['chapters']),
                  'Cycles Claude : activation sans revue préétablie requise')
        return {}, codes, set()
    for key in ('schema_version', 'authority', 'coordinator', 'not_before'):
        C.require(old.get(key) == new.get(key), 'Cycles Claude : autorisation modifiée')
    C.require(before.read(CAHIER) == after.read(CAHIER), 'Cycles Claude : cahier du cycle 2 modifié')
    if any(c['state'] == 'ACTIF' for c in old['cycles'] + new['cycles']):
        for p in (AUTHORITY, PLAN):
            C.require(before.read(p) == after.read(p), 'Cycles Claude : instruction ou plan modifié pendant un cycle actif')
    if any(c.get('novo') for c in old['cycles']):
        for p in (V.PLAN, V.AUTHORITY):
            C.require(before.read(p) == after.read(p), 'Novo : instruction ou plan modifié après ouverture')
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
        for field in ('cycle', 'owner', 'started_at', 'budget', 'transferred_from', 'handover',
                      'novo', 'tetrad_cycles', 'novo_plan_sha256', 'novo_authority', 'novo_authority_sha256'):
            C.require(cycle.get(field) == previous_cycle.get(field), 'Cycles Claude : identité ou départ du cycle modifié')
        if any(cycle.get(f) != previous_cycle.get(f) for f in ('mode', 'authority', 'authority_sha256')):
            mode_change(after, previous_cycle, cycle, now)
            C.require(not course_changes, 'Cycles Claude : changement de mode avec injection simultanée')
            continue
        if previous_cycle['state'] == 'CLOTURE':
            C.require(cycle == previous_cycle, 'Cycles Claude : cycle clos immuable')
        rows = cycle['chapters']
        if previous_cycle.get('cross_phase') is not None:
            C.require(cycle.get('cross_phase') == previous_cycle['cross_phase'], 'Cycles Claude : clôture initiale croisée réécrite')
        straight = direct(cycle)
        boundary = None if straight else (cross_boundary(after, cycle, now) if any(C.STATES.index(r['status']) >= 2 for r in rows) else None)
        for previous, row in zip(previous_cycle['chapters'], rows):
            stage = C.STATES.index(row['status'])
            C.require(stage >= C.STATES.index(previous['status']), 'Cycles Claude : régression non tracée')
            if straight:
                # Publication directe : la revue auteur précède le contrôle ; aucun audit croisé n'est attendu.
                if stage == 3:
                    C.review(after, row, 'author', row['writer'], C.source_files(after, row, SOURCE_ROOTS), author_prompts(row))
            else:
                if stage >= 1:
                    C.require(all(r['author'] for r in rows), 'Cycles Claude : quatre auteurs avant audit croisé')
                if stage >= 2:
                    C.require(all(r['cross_audit'] for r in rows), 'Cycles Claude : quatre audits croisés avant contre-audit')
                if stage >= 3:
                    C.require(all(r['counter_audit'] for r in rows), 'Cycles Claude : quatre contre-audits avant contrôle')
            if not straight and 1 <= stage < 4:
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
                files = direct_ready(after, row) if straight else ready(after, row, rows, cross_completed_at=boundary)
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
                if row.get('novo'):
                    V.publication_proof(after, row, pub, files)
        if cycle['state'] == 'CLOTURE':
            closure = C.proof(after, cycle.get('closure'), 'Clôture')
            C.require(closure.get('blocking_reserves') == [] and closure.get('cycle') == cycle['cycle'],
                      'Cycles Claude : clôture avec réserves')
    batch = bool(injections and injections[0][0].get('novo'))
    C.require(len(injections) <= 1 or (batch and len(injections) <= 12 and
              all(c is injections[0][0] for c, r in injections)), 'Cycles Claude : une seule injection à la fois')
    if injections:
        prior, row = injections[0]
        deferred = direct(prior)
        idx = [r['code'] for r in prior['chapters']].index(row['code'])
        C.require(all(r['status'] in ({'INJECTE', 'PUBLIE_VERIFIE'} if batch else {'PUBLIE_VERIFIE'})
                      for r in prior['chapters'][:idx]) and
                  all(r['status'] == 'PRET_A_INJECTER' for r in prior['chapters'][idx:]),
                  'Cycles Claude : ordre de publication ou quatre cours prêts non respecté')
        expected_codes = [r['code'] for r in prior['chapters'][idx:idx + len(injections)]]
        C.require([r['code'] for c, r in injections] == expected_codes, 'Novo : injections non consécutives')
        C.require(course_changes == set(authorized), 'Cycles Claude : fichiers injectés manquants ou supplémentaires')
        original, catalog = C.read_json(before, 'chapters.json'), C.read_json(after, 'chapters.json')
        additions = [r for r in catalog if r not in original]
        expected = {r['code']: r for c, r in injections}
        if batch:
            C.require(len({a.get('code') for a in catalog}) == len(catalog) and
                      not set(expected).intersection(a.get('code') for a in original),
                      'Novo : code déjà présent ou catalogue dupliqué')
        C.require(len(catalog) == len(original) + len(injections) and all(r in catalog for r in original) and
                  len(additions) == len(injections) and [a.get('code') for a in additions] == expected_codes and
                  all(a.get('covers') == [a['code']] and a.get('integrated') is True and
                      a.get('production_cycle') == expected[a['code']]['production_cycle'] for a in additions),
                  'Cycles Claude : catalogue ajout unique requis')
        if deferred:
            C.require(all(a.get('provisional_injection') is True and a.get('audit_deferred') == DIRECT_DEFERRED for a in additions),
                      'Cycles Claude : publication directe sans mention d’audit différé')
        authorized['chapters.json'] = C.digest(after.read('chapters.json'))
    else:
        C.require(not course_changes, 'Cycles Claude : source sans injection contrôlée')
        if 'chapters.json' in changed:
            C.require([r for r in C.read_json(before, 'chapters.json') if r.get('code') in codes] ==
                      [r for r in C.read_json(after, 'chapters.json') if r.get('code') in codes],
                      'Cycles Claude : catalogue modifié sans injection')
    return authorized, codes, catalog_codes
