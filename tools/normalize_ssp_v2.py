#!/usr/bin/env python3
"""Normalize the bounded SSP-v2 evidence without modifying global nosology.

Portable normalizer of the four bounded evidence files. Only the five named
outputs are written. A documented edge is an editorial evidence claim, never
an audit. The output header hashes this repository script itself.
"""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCOPE = ('S08', 'S05', 'S04', 'S06')
OUTPUTS = (
    'graphe-ssp-diagnostics.json', 'graphe-ssp-diagnostics.csv',
    'couverture-265-ssp.json', 'couverture-265-ssp.csv',
    'ssp-labels-corriges.json',
)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def seq(value):
    if value is None or value == '':
        return []
    return value if isinstance(value, list) else [value]


def unique(items):
    result = []
    for item in items:
        if item is not None and item != '' and item not in result:
            result.append(item)
    return result


def first(item, *names, default=None):
    for name in names:
        if item.get(name) is not None and item.get(name) != '':
            return item[name]
    return default


def source_catalog(document):
    data = document.get('sources', {})
    if isinstance(data, dict):
        return data
    assert isinstance(data, list), 'Unsupported sources container'
    return {str(first(s, 'id', 'source_id')): s for s in data}


def limitations(item):
    return unique([entry for key in ('limit', 'limits', 'limite', 'limitation', 'limitations',
                                    'condition', 'interpretation', 'scope_limit')
                   for entry in seq(item.get(key))])


def normalize_sources(edge, document):
    catalog = source_catalog(document)
    justification = document.get('justifications', {}).get(edge.get('justification_id'), {})
    evidence = edge.get('evidence')
    if evidence is None:
        evidence = [{
            'source_id': first(edge, 'source_id', default=justification.get('source_id')),
            'url': first(edge, 'source_url', 'url'),
            'section': first(edge, 'source_section_lue', 'section_read', 'section_lue',
                             'source_section', 'section', default=justification.get('section_lue')),
        }]
    normalized = []
    for ev in seq(evidence):
        assert isinstance(ev, dict), f'Unsupported evidence: {ev!r}'
        sid = ev.get('source_id')
        source = catalog.get(str(sid), {})
        url = first(ev, 'url', 'source_url', default=source.get('url'))
        section = first(ev, 'section', 'section_read', 'section_lue', 'source_section_lue',
                        default=first(source, 'section_read', 'sections_read', 'read_sections', 'read_scope'))
        lims = unique(limitations(source) + limitations(justification) + limitations(ev))
        if not url:
            lims.append('URL absente de la preuve source ; aucune URL inventée.')
        if not section:
            lims.append('Section lue non précisée dans la preuve source.')
        role = ('referentiel_ssp' if sid == 'profiles' or (url and 'siwf.ch/' in url)
                else 'classification_cim' if sid in ('icd', 'ofs_icd') or (url and 'bfs.admin.ch/' in url)
                else 'source_diagnostique_declaree')
        normalized.append({
            'source_id': sid, 'url': url, 'section_lue': section,
            'role': role, 'limites': lims, 'trace': ev.get('trace'),
            'source_metadata_originale': source,
            'preuve_originale': ev,
        })
    return normalized, justification


def normalized_relation(raw, status):
    text = str(raw or '').lower().strip()
    if any(token in str(status).lower() for token in ('a_verifier', 'à_vérifier', 'non_admis', 'non_prouve', 'candidat', 'non_verifie')):
        return 'candidat'
    aliases = {'diagnostic': 'diagnostic', 'differentiel': 'differentiel',
               'différentiel': 'differentiel', 'differential': 'differentiel',
               'contexte': 'contexte', 'context': 'contexte',
               'candidat': 'candidat', 'candidate': 'candidat'}
    # Unknown relations are preserved as unconfirmed candidates, never promoted.
    return aliases.get(text, 'candidat')


def dump_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def dump_csv(path, fields, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            writer.writerow({k: canonical(v) if isinstance(v, (dict, list)) else v
                             for k, v in row.items() if k in fields})


def generate(repo, folder):
    protected_paths = [repo / 'nosology/reference.json', repo / 'nosology/ssp_profiles2017.json',
                       repo / 'chapters.json'] + sorted((repo / 'nosology/fragments').glob('*.json'))
    # Hash global sources before and after to assert this script never changes them.
    protected = {str(p.relative_to(repo)): digest(p.read_bytes())
                 for p in protected_paths if p.exists()}
    reference = read(repo / 'nosology/reference.json')
    entities = {e['code']: e for e in reference['entities']}
    labels_original = read(repo / 'nosology/ssp_profiles2017.json')
    assert set(labels_original) == {str(n) for n in range(1, 266)}
    methodology = read(folder / 'methodologie.json')
    repairs = methodology['source_integrity']['label_repairs']
    assert set(repairs) == {'39', '66', '93', '130', '216', '226', '227'}
    labels = dict(labels_original)
    for number, repair in repairs.items():
        assert repair.get('complete_label') and repair.get('source_url')
        labels[number] = repair['complete_label']

    edges = []
    inputs = []
    source_documents = {}
    duplicates = Counter()
    missing = []
    for fid in SCOPE:
        path = folder / f'preuves-{fid}.json'
        if not path.exists():
            missing.append(fid)
            continue
        document = read(path)
        container = next((key for key in ('graph', 'links', 'relations') if key in document), None)
        raw_edges = document.get(container)
        assert isinstance(raw_edges, list), f'Missing graph/links in {path}'
        relative = str(path.relative_to(repo))
        inputs.append({'fragment_analyse': fid, 'source_fichier': relative,
                       'sha256': digest(path.read_bytes()), 'container': container,
                       'nombre_liens_entree': len(raw_edges)})
        # Preserve source registries and all document-level reservations once.
        source_documents[relative] = {k: v for k, v in document.items() if k != container}
        for index, raw in enumerate(raw_edges):
            number = int(raw['ssp'])
            assert 1 <= number <= 265 and str(raw['ssp']).isdigit(), (path, index, raw['ssp'])
            code_input = str(first(raw, 'code3', 'code', 'category', default=''))
            assert re.fullmatch(r'[A-Z][0-9]{2}(?:\.[0-9A-Z]+)?', code_input), (path, index, code_input)
            assert code_input in entities, (path, index, 'unknown CIM code', code_input)
            code = code_input[:3]
            assert code in entities and code in reference['mapping'], (path, index, code)
            owner = reference['mapping'][code]['fragment']
            raw_owner = raw.get('owner_fragment')
            assert not raw_owner or raw_owner == owner, (path, index, 'ownership mismatch', raw_owner, owner)
            sources, justification = normalize_sources(raw, document)
            rationale = first(raw, 'justification', 'rationale',
                              default=justification.get('justification'))
            relation_source = first(raw, 'relation', 'relation_type', 'type')
            relation = normalized_relation(relation_source, raw.get('status'))
            entity = first(raw, 'diagnostic_entity', 'clinical_diagnosis', 'diagnostic_or_concept',
                           'clinical_entity', default=entities[code]['title'])
            lims = unique(limitations(raw) + limitations(justification)
                          + [lim for source in sources for lim in source['limites']])
            if not sources:
                lims.append('Aucune preuve source associée à cette relation dans le fichier original ; candidat non confirmé.')
            if relation_source not in ('diagnostic', 'differentiel', 'différentiel', 'differential',
                                       'contexte', 'context', 'candidat', 'candidate'):
                lims.append('Relation source inconnue : normalisée comme candidat sans validation.')
            # IDs do not depend on corrected SSP display labels or file ordering.
            identity = {k: v for k, v in raw.items() if not k.startswith('ssp_label')}
            key = digest(canonical({'source_fichier': relative, 'preuve': identity}).encode('utf-8'))[:20]
            duplicates[key] += 1
            edge_id = f'SSPV2-{key}' + (f'-{duplicates[key]}' if duplicates[key] > 1 else '')
            edges.append({
                'id': edge_id, 'ssp': number, 'label_officiel_corrige': labels[str(number)],
                'label_amont_original': labels_original[str(number)],
                'label_repare': str(number) in repairs,
                'code3': code, 'code_entree': code_input, 'titre_cim': entities[code]['title'],
                'fragment_proprietaire': owner, 'fragment_analyse': fid,
                'renvoi_hors_quatre_lecture_seule': owner not in SCOPE,
                'renvoi_hors_fragment_analyse': owner != fid,
                'relation': relation, 'relation_source': relation_source,
                'entite_clinique': entity, 'justification': rationale,
                'sources': sources, 'limites': lims,
                'statut_preuve_source': raw.get('status'),
                'source_fichier': relative, 'source_index': index,
                'source_json_pointer': f'/{container}/{index}',
                'source_id_original': raw.get('id'),
                'preuve_originale': raw,
                'full_clinical_audit': False, 'official_icd_crosswalk': False,
                'preuve_exhaustivite_differentiels': False,
            })

    assert len({e['id'] for e in edges}) == len(edges)
    assert len(edges) == sum(i['nombre_liens_entree'] for i in inputs)
    edges.sort(key=lambda e: (e['ssp'], e['code3'], e['relation'], e['id']))
    incidence = defaultdict(list)
    for edge in edges:
        incidence[edge['ssp']].append(edge)
    coverage = []
    for number in range(1, 266):
        subset = incidence.get(number, [])
        relations = Counter(e['relation'] for e in subset)
        if not subset:
            status = 'NON_DOCUMENTE_DANS_CE_CONTROLE'
        elif relations['diagnostic'] + relations['differentiel']:
            status = 'LIENS_DIAGNOSTIQUES_DOCUMENTES_PARTIELLEMENT'
        elif relations['contexte']:
            status = 'LIENS_CONTEXTUELS_SEULEMENT'
        else:
            status = 'CANDIDATS_SEULEMENT_A_VERIFIER'
        coverage.append({
            'ssp': number, 'label_officiel_corrige': labels[str(number)],
            'label_repare': str(number) in repairs, 'statut': status,
            'nombre_liens': len(subset),
            'diagnostic': relations['diagnostic'], 'differentiel': relations['differentiel'],
            'contexte': relations['contexte'], 'candidat': relations['candidat'],
            'codes3': sorted({e['code3'] for e in subset}),
            'fragments_proprietaires': sorted({e['fragment_proprietaire'] for e in subset}),
            'fragments_analyses': sorted({e['fragment_analyse'] for e in subset}),
            'liens_ids': [e['id'] for e in subset],
            'preuve_exhaustivite_differentiels': False, 'full_clinical_audit': False,
            'interpretation': ('Absence de lien dans cette recherche ciblée ; aucune conclusion de non-exigibilité.'
                               if not subset else 'Incidence dans le graphe ; aucune preuve d’exhaustivité des diagnostics différentiels.'),
        })
    assert len(coverage) == 265
    assert all(c['statut'] == 'NON_DOCUMENTE_DANS_CE_CONTROLE' for c in coverage if not c['nombre_liens'])
    assert sum(c['nombre_liens'] for c in coverage) == len(edges)
    assert all(not e['full_clinical_audit'] for e in edges)
    assert all(digest((repo / path).read_bytes()) == value for path, value in protected.items())
    meta = {
        'schema_version': 2, 'date': '2026-10-15', 'scope': list(SCOPE),
        'full_clinical_audit': False, 'official_icd_crosswalk': False,
        'preuve_exhaustivite_differentiels': False, 'global_sources_modified': False,
        'input_files': inputs, 'missing_evidence_fragments': missing,
        'input_set_complete': not missing,
        'counts': {'liens': len(edges), 'ssp_avec_liens': len(incidence),
                   'ssp_non_documentees': 265-len(incidence),
                   'liens_hors_candidats': sum(e['relation'] != 'candidat' for e in edges),
                   'ssp_avec_liens_hors_candidats': len({e['ssp'] for e in edges if e['relation'] != 'candidat'}),
                   'ssp_avec_diagnostic_ou_differentiel': len({e['ssp'] for e in edges if e['relation'] in ('diagnostic','differentiel')}),
                   'statuts_ssp': dict(Counter(c['statut'] for c in coverage)),
                   'relations': dict(Counter(e['relation'] for e in edges)),
                   'liens_par_fragment_analyse': dict(Counter(e['fragment_analyse'] for e in edges))},
        'meaning': 'Graphe d’incidence documentaire ciblé, pas preuve de couverture exhaustive des différentiels ni liste officielle de maladies fédérales.',
        'unlinked_status': 'NON_DOCUMENTE_DANS_CE_CONTROLE',
        'source_index_base': 0,
        'id_policy': 'SHA256 du fichier logique et de la preuve originale hors libellé SSP, tronqué à20hex ; occurrence suffixée seulement pour doublons exacts.',
        'protected_global_sources_sha256': protected,
        'normalizer_script': 'tools/normalize_ssp_v2.py',
        'normalizer_script_sha256': digest(Path(__file__).read_bytes()),
    }
    graph = {**meta, 'source_documents': source_documents, 'graph': edges}
    assert meta['counts']['ssp_non_documentees'] == sum(c['statut'] == 'NON_DOCUMENTE_DANS_CE_CONTROLE' for c in coverage)
    cover = {**meta, 'ssp': coverage}
    label_payload = {
        'schema_version': 2, 'date': '2026-10-15', 'full_clinical_audit': False,
        'global_sources_modified': False, 'language': 'en',
        'source': 'PROFILES 2017, libellés originaux ; sept compléments vérifiés dans methodologie.json',
        'input_labels_sha256': protected['nosology/ssp_profiles2017.json'],
        'methodology_sha256': digest((folder / 'methodologie.json').read_bytes()),
        'label_repairs': repairs,
        'labels': labels,
        'repair_audit': [{'ssp': int(k), 'original': labels_original[k],
                          'corrected': v['complete_label'], **{a:b for a,b in v.items() if a!='complete_label'}}
                         for k, v in sorted(repairs.items(), key=lambda x:int(x[0]))],
    }
    dump_json(folder / OUTPUTS[0], graph)
    graph_fields = ['id','ssp','label_officiel_corrige','label_repare','code3','titre_cim',
                    'fragment_proprietaire','fragment_analyse','renvoi_hors_quatre_lecture_seule',
                    'renvoi_hors_fragment_analyse','relation','entite_clinique','justification',
                    'sources','limites','statut_preuve_source','source_fichier','source_index',
                    'source_json_pointer','full_clinical_audit','preuve_exhaustivite_differentiels']
    dump_csv(folder / OUTPUTS[1], graph_fields, edges)
    dump_json(folder / OUTPUTS[2], cover)
    dump_csv(folder / OUTPUTS[3], list(coverage[0]), coverage)
    dump_json(folder / OUTPUTS[4], label_payload)
    # Cross-format verification, including CSV IDs, is part of generation.
    with (folder / OUTPUTS[1]).open(encoding='utf-8-sig', newline='') as handle:
        csv_edges = list(csv.DictReader(handle))
    with (folder / OUTPUTS[3]).open(encoding='utf-8-sig', newline='') as handle:
        csv_cover = list(csv.DictReader(handle))
    assert [row['id'] for row in csv_edges] == [e['id'] for e in edges]
    assert len(csv_cover) == 265
    assert all(not x['full_clinical_audit'] for x in (read(folder/OUTPUTS[0]), read(folder/OUTPUTS[2])))
    assert all(digest((repo/path).read_bytes()) == value for path,value in protected.items())
    return meta


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    folder = (args.output_dir or repo/'docs/collaboration/ssp-v2/2026-10-15').resolve()
    assert folder == repo/'docs/collaboration/ssp-v2/2026-10-15', 'Only assigned output directory is authorized'
    summary = generate(repo, folder)
    print(json.dumps({k:summary[k] for k in ('counts','missing_evidence_fragments','input_set_complete')}, ensure_ascii=False))
