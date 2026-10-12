"""Publication provisoire ciblée, sur l'ordre explicite injection puis STOP.

Les contre-audits et le contrôle final ne sont pas prétendus réalisés.
La garde conserve les sources exactes et les audits croisés effectivement clos.
"""
import hashlib
import json

RECEIPT = 'organisation/CYCLE_01_INJECTION_STOP_2026-10-12.json'
AUTHORITY = 'docs/collaboration/instructions/INJECTION_IMMEDIATE_STOP_VIAL_2026-10-12.md'
CODES = ('I63', 'E11', 'N17', 'D50')


def validate(before, after):
    try:
        from tetrade_cycle import CycleError, records, source_files, review
    except ModuleNotFoundError:
        from tools.tetrade_cycle import CycleError, records, source_files, review
    raw = after.read(RECEIPT, required=False)
    previous_raw = before.read(RECEIPT, required=False)
    if raw is None:
        if previous_raw is not None:
            raise CycleError('Ordre STOP : reçu supprimé.')
        return None
    def need(condition, message):
        if not condition:
            raise CycleError('Injection STOP : ' + message)
    data = json.loads(raw)
    instruction = after.read(AUTHORITY)
    need(data.get('schema_version') == 1 and data.get('authority') == AUTHORITY,
         'autorité ciblée absente.')
    need(data.get('authority_sha256') == hashlib.sha256(instruction).hexdigest(), 'instruction différente.')
    need(b'injecte' in instruction and b'STOP' in instruction and b'MAINTENANT' in instruction,
         'ordre direct incomplet.')
    need(data.get('state') == 'INJECTE_PROVISOIRE_STOP' and data.get('execution_stopped') is True,
         'état provisoire et arrêt requis.')
    need(data.get('counter_audits_performed') is False and data.get('final_control_performed') is False
         and data.get('medical_human_validation') is False, 'qualification des audits incorrecte.')
    state = records(after)
    need(state.get('execution_stopped') is True, 'cycle non arrêté.')
    authorised = {}
    for row in state['chapters']:
        files = source_files(after, row)
        review(after, row, 'author', row['writer'], files)
        review(after, row, 'cross_audit', row['cross_reviewer'], files)
        need(row['counter_audit'] is None and row['control'] is None, 'étapes non effectuées présentées comme réalisées.')
        for path, sha in files.items():
            need(hashlib.sha256(after.read(path)).hexdigest() == sha, 'source canonique différente : ' + path)
            authorised[path] = sha
    need(data.get('files') == authorised, 'périmètre différent des quatre remises finales.')
    current = json.loads(after.read('chapters.json'))
    existing = json.loads(before.read('chapters.json'))
    if previous_raw is None:
        additions = [item for item in current if item not in existing]
        need(len(current) == len(existing) + 4 and all(item in current for item in existing),
             'quatre ajouts seuls sont autorisés.')
        need({item.get('code') for item in additions} == set(CODES)
             and all(item.get('covers') == [item['code']] and item.get('integrated') is True
                     and item.get('provisional_injection') is True for item in additions),
             'catégorie unique et qualification provisoire requises.')
        changed = {p for p in before.entries.keys() | after.entries.keys()
                   if before.entries.get(p) != after.entries.get(p)}
        source_changes = {p for p in changed if any(p.startswith('chapters/' + code + '/')
                          or p == 'glossary/' + code.lower() + '.py' for code in CODES)}
        need(source_changes == set(authorised), 'fichiers supplémentaires ou manquants.')
    else:
        need(raw == previous_raw and instruction == before.read(AUTHORITY), 'reçu ou ordre STOP modifié.')
        need(current == existing, 'catalogue modifié après STOP.')
        need(all(before.read(p) == after.read(p) for p in authorised), 'source modifiée après STOP.')
    authorised['chapters.json'] = hashlib.sha256(after.read('chapters.json')).hexdigest()
    return authorised, set(CODES)
