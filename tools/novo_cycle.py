"""Contrat Novo_12 : un lot de préparation, douze preuves et un déploiement possible.

Ce module ne rédige, ne copie et ne publie aucun cours. Les quatre-leçons
historiques restent inchangées ; seul un cycle portant explicitement ``novo``
utilise ce contrat, après clôture du cycle précédent.
"""
try:
    from tools import tetrade_cycle as C
    from tools import night_cycle as N
    from tools.betta_verite import controler_contenu
except ModuleNotFoundError:
    import tetrade_cycle as C
    import night_cycle as N
    from betta_verite import controler_contenu

PLAN = 'organisation/novo_12/PLAN_NOVO_12.json'
AUTHORITY = 'docs/collaboration/instructions/NOVO12_EXECUTION_VIAL_2026-10-15.md'
TRUTH = 'docs/collaboration/betta/PROMPT_VERITE.md'


def specification(tree, number):
    """Valide les 108 attributions contre le plan original, sans les modifier."""
    plan = C.read_json(tree, PLAN)
    original = C.read_json(tree, N.PLAN)
    C.require(type(number) is int and 1 <= number <= 9, 'Novo : numéro de lot invalide')
    batches = plan.get('cycles', [])
    C.require(plan.get('id') == 'NOVO_12' and len(batches) == 9, 'Novo : plan de neuf lots requis')
    seen = set()
    result = None
    for index, batch in enumerate(batches, 1):
        cycles = list(range(4 + 3 * (index - 1), 7 + 3 * (index - 1)))
        C.require(batch.get('novo') == index and batch.get('tetrad_cycles') == cycles,
                  'Novo : ordre des cycles modifié')
        systems = batch.get('systems', [])
        C.require(len(systems) == 4, 'Novo : quatre systèmes requis')
        for system, old in zip(systems, original['systems']):
            expected = [old['chapters'][n - 1][0] for n in cycles]
            C.require((system.get('id'), system.get('tag'), system.get('lessons')) ==
                      (old['id'], old['tag'], expected), 'Novo : attribution différente du plan original')
            C.require(not seen.intersection(expected), 'Novo : leçon dupliquée')
            seen.update(expected)
        if index == number:
            missions = [(s['lessons'][i], s['id'], s['tag'], n)
                        for i, n in enumerate(cycles) for s in systems]
            result = cycles, missions
    C.require(len(seen) == 108, 'Novo : 108 leçons distinctes requises')
    return result


def validate_cycle(tree, cycle):
    cycles, missions = specification(tree, cycle.get('novo'))
    C.require(cycle.get('cycle') == cycles[0] and cycle.get('tetrad_cycles') == cycles,
              'Novo : identité de lot incorrecte')
    C.require(cycle.get('novo_plan_sha256') == C.digest(tree.read(PLAN)) and
              cycle.get('novo_authority') == AUTHORITY and
              cycle.get('novo_authority_sha256') == C.digest(tree.read(AUTHORITY)),
              'Novo : autorité ou plan différent')
    C.require(cycle.get('mode') == 'publication_directe' and not cycle.get('transferred_from'),
              'Novo : production Claude en publication directe seulement')
    return missions


def research_proof(tree, row, author):
    """Même porte de complétude que Betta, contrôlée sur l'arbre exact livré."""
    root = row['source_dir'].rstrip('/')
    text = tree.read(root + '/recherche.md').decode('utf-8')
    sources = C.read_json(tree, root + '/sources.json')
    errors = controler_contenu(text, sources.get('sources', []), row['code'])
    C.require(not errors, 'Novo : porte de vérité : ' + '; '.join(errors))
    expected = {p: C.digest(tree.read(p)) for p in (root + '/recherche.md', root + '/sources.json')}
    for gate in ('entry', 'exit'):
        evidence = {e.get('path'): e.get('sha256') for c in author.get(gate, {}).get('checks', [])
                    if c.get('id') == 'sources_lues' for e in c.get('evidence', [])}
        C.require(all(evidence.get(p) == sha for p, sha in expected.items()),
                  'Novo : recherche non figée dans les relevés auteur entrée/sortie')


def publication_proof(tree, row, publication, files):
    """Lie le reçu individuel au manifeste téléchargé et au même déploiement."""
    injection = C.proof(tree, row['injection'], 'Novo injection')
    C.require(C.dated(publication.get('checked_at')) >= C.dated(injection.get('checked_at')),
              'Novo : publication antérieure à injection')
    manifest = C.proof(tree, publication.get('site_manifest'), 'Novo manifeste public')
    C.require(manifest.get('git_commit') == publication.get('main_sha'), 'Novo : SHA publié différent du manifeste')
    course = (manifest.get('courses') or {}).get(row['code'], {})
    C.require(course.get('source_files') == row['files'], 'Novo : sources publiées différentes des sources contrôlées')
    run = publication.get('pages_run') or {}
    C.require(type(run.get('id')) is int and run['id'] > 0 and run.get('conclusion') == 'success' and
              run.get('head_sha') == publication.get('main_sha'), 'Novo : déploiement non lié au SHA publié')
    C.require(publication.get('published_files') == files and publication.get('public_images_http_200') is True,
              'Novo : relecture des sources ou images publiées non tracée')
