#!/usr/bin/env python3
"""Reproduce the four-system V2 editorial plan; no clinical source writes."""
from pathlib import Path
from collections import Counter,defaultdict
import json,copy,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/collaboration/ssp-v2/2026-10-15'
old=json.loads((ROOT/'docs/collaboration/alpha/2026-10-15/plan.json').read_text())
from itertools import product
FIXED_C={'audit':{'I63','N17'},'production':{'G00','N00'},'reserve':set()}
FIXED_L={'audit':{'E11','D50'},'production':{'E03','C91'},'reserve':set()}
def subset(rows, n, mode):
    required = [r for r in rows if r['code'] in FIXED_C[mode]]
    excluded = FIXED_L[mode]
    candidates = [r for r in rows if r['code'] not in FIXED_C[mode] | excluded]
    k = n-len(required)
    if not 0 <= k <= len(candidates): return None
    # Quantized integer weights keep the exact-count subset search bounded.
    weights = {r['code']: max(1, round(r['effort_proxy']/4)) for r in rows}
    fixed_weight = sum(weights[r['code']] for r in required)
    states = [dict() for _ in range(k+1)]
    states[0][0] = ()
    for i,r in enumerate(candidates):
        w = weights[r['code']]
        for count in range(min(k,i+1),0,-1):
            for total,codes in list(states[count-1].items()):
                states[count].setdefault(total+w, codes+(r['code'],))
    if not states[k]: return None
    target = sum(weights.values())/2
    total,codes = min(states[k].items(), key=lambda item:(abs(item[0]+fixed_weight-target),item[1]))
    chosen = set(codes) | {r['code'] for r in required}
    return chosen, sum(r['effort_proxy'] for r in rows if r['code'] in chosen)

def allocate(rows, target, mode):
    groups = defaultdict(list)
    for r in rows: groups[r['chapter']].append(r)
    options=[]
    for chapter,items in sorted(groups.items()):
        choices=[]
        for n in sorted({len(items)//2,(len(items)+1)//2}):
            candidate=subset(items,n,mode)
            if candidate is not None: choices.append((n,*candidate))
        if not choices: raise ValueError(('quota impossible',chapter,mode))
        options.append(choices)
    combinations=[c for c in product(*options) if sum(x[0] for x in c)==target]
    if not combinations: raise ValueError(('quota système impossible',target,mode))
    half=sum(r['effort_proxy'] for r in rows)/2
    best=min(combinations,key=lambda c:(abs(sum(x[2] for x in c)-half),tuple(sorted(code for x in c for code in x[1]))))
    chosen=set().union(*(x[1] for x in best))
    for r in rows: r['owner']='Codex' if r['code'] in chosen else 'Claude'
    assert sum(r['owner']=='Codex' for r in rows)==target
    return rows

ADDS={'S08':['D32','G10','G12'],'S05':['D34','E15','E16','E80','E83','E88','E89'],'S04':[],'S06':['D47']}
ALL_ADDS=set(sum(ADDS.values(),[]))
p=copy.deepcopy(old);p['schema_version']=2;p['title']='MEDINA — Audit Alpha, production et prévention des conflits — V2 SSP'
p['inventory_method']='Périmètre conservatoire : 247 catégories historiques maintenues + 11 ajouts avec liens diagnostiques documentés. Ni liste officielle ni validation exhaustive des catégories.'
p['audit']=copy.deepcopy(old['audit']);p['production']=copy.deepcopy(old['production'])+[copy.deepcopy(r) for r in old['reserve'] if r['code'] in ALL_ADDS];p['reserve']=[copy.deepcopy(r) for r in old['reserve'] if r['code'] not in ALL_ADDS]
PROD_Q={'S08':25,'S05':25,'S04':13,'S06':14};RES_Q={'S08':4,'S05':1,'S04':0,'S06':1}
for mode,quota in [('production',PROD_Q),('reserve',RES_Q)]:
 for s in p['scope']:allocate([r for r in p[mode] if r['fragment']==s],quota[s],mode)
for mode in ['audit','production','reserve']:
 for r in p[mode]:
  ident=f"SSPV2-{mode.upper()}-{r['fragment']}-{r['code']}-{r['owner'].upper()}"
  r.update(mode=mode,assignment_id=ident,generation=0,status='PLANIFIE_NON_LANCE',branch_template=f"{r['owner'].lower()}/ssp-v2/{mode}/{r['code'].lower()}-SESSION-GENERATION",worktree_template=f"../medina-ssp-v2/{ident}/SESSION-GENERATION")
  r['legacy_ssp_unvalidated']=r.pop('ssp',[]) or [];r['evidence_edges']=[];r['ssp_documented']=[]
  r['evidence_status']='historique_a_revalider' if r['code'] not in ALL_ADDS else 'ajout_avec_lien_documente_partiel'
  r['write_paths']=[f"docs/collaboration/ssp-v2/execution/{ident}"]
  if mode=='production':r['write_paths']+=[f"chapters/{r['code']}",f"glossary/{r['code'].lower()}.py"]
  r['report_path']=r['write_paths'][0]+'/rapport.json'
  r['correction_gate']='Mission distincte même responsable, approuvée dans main, génération et réservation courantes. Les anciens reçus restent attachés à leurs versions ; chemin de correction médicale et preuve de publication requis.'
  r['federal_mapping']='PEDAGOGIQUE_NON_OFFICIEL_RECONTROLE_PARTIEL'
  for k in ['correction_paths','correction_mission_id']:r.pop(k,None)
# Evidence records remain authoritative in original per-system schemas.
normalized=json.loads((OUT/'graphe-ssp-diagnostics.json').read_text())
for r in p['audit']+p['production']+p['reserve']:
 edges=[e for e in normalized['graph'] if e['code3']==r['code'] and e['fragment_proprietaire']==r['fragment']]
 r['evidence_edges']=[e['id'] for e in edges]
 r['ssp_documented']=sorted({e['ssp'] for e in edges if e['relation']!='candidat'})
 r['ssp_diagnostic_documented']=sorted({e['ssp'] for e in edges if e['relation'] in {'diagnostic','differentiel'}})
 if r['ssp_diagnostic_documented'] and r['code'] not in ALL_ADDS:r['evidence_status']='liens_diagnostiques_documentes_partiellement'
 r['full_category_revalidated']=False
p['graph_counts']=normalized['counts']
p['graph_sha256']=hashlib.sha256((OUT/'graphe-ssp-diagnostics.json').read_bytes()).hexdigest()
p['systems']=[]
for s in p['scope']:
 prev=next(x for x in old['systems'] if x['id']==s)
 q={k:prev[k] for k in ['id','name','fragment_label','raw_gold_count']};q['historical_star_categories']=prev['gold_categories'];q['conservative_categories']=prev['gold_categories']+len(ADDS[s]);q['gold_categories']=q['conservative_categories'];q['added_categories']=ADDS[s]
 for mode in ['audit','production','reserve']:
  rows=[r for r in p[mode] if r['fragment']==s];q[mode+'_count']=len(rows);q[mode+'_split']=dict(Counter(r['owner'] for r in rows));q[mode+'_effort']={o:sum(r['effort_proxy'] for r in rows if r['owner']==o) for o in ['Codex','Claude']}
 p['systems'].append(q)
p['chapter_summary']=[]
for s in p['scope']:
 for ch in sorted(set(r['chapter'] for m in ['audit','production','reserve'] for r in p[m] if r['fragment']==s)):
  q={'fragment':s,'chapter':ch,'title':next(r['chapter_title'] for m in ['audit','production','reserve'] for r in p[m] if r['fragment']==s and r['chapter']==ch)}
  for m in ['audit','production','reserve']:
   rows=[r for r in p[m] if r['fragment']==s and r['chapter']==ch];q[m]=len(rows)
   for o in ['Codex','Claude']:q[m+'_'+o]=sum(r['owner']==o for r in rows)
   assert abs(q[m+'_Codex']-q[m+'_Claude'])<=1
  p['chapter_summary'].append(q)
p['totals']={'ssp':265,'existing':104,'audit_Codex':52,'audit_Claude':52,'historical_starred':247,'additions_documented':11,'conservative_target':258,'new_starred':154,'production_Codex':77,'production_Claude':77,'mapping_reserve':12,'reserve_Codex':6,'reserve_Claude':6,'potential_new_all_categories':166,'all_categories':270}
p['definitions'].update(federal=p['inventory_method'],empty_subcodes='1967 lignes historiques étoilées vides = 143 catégories racines + 1824 sous-codes. Ce compteur V1 ne mesure pas les besoins V2.',reserve='12 catégories non exclues, correspondance et choix éditorial encore à arbitrer.',equal_share='Audit52/52 ; production154=77/77 ; réserve12=6/6. Un cours reste entier et attribué à un seul responsable.',capacity='Pilote4 puis au plus2 missions source simultanées par responsable au départ ; lectures indépendantes possibles ; mutations partagées intégrées séquentiellement.')
p['implementation_gates']=[{'id':'G1','state':'IMPLEMENTE_TESTE','title':'Réservation Git distante à avance rapide et génération','requirement':'Registre initialisé séparément, manifeste actif dans la base approuvée, 18 tests locaux dont deux processus.'},{'id':'G2','state':'IMPLEMENTE_A_IMPOSER_SERVEUR','title':'CI de confiance mission/périmètre','requirement':'Activer protection main PR+contrôle obligatoire strict et sans bypass. AccèsAdministration actuel insuffisant (403).'}, {'id':'G3','state':'PREPARATION_SEULE','title':'Audit Alpha sans croisement','requirement':'Aucune rédaction/audit de104leçons démarré. Attributionplanifiée, sourcefixée, preuvesconstats réels avantstatut.'},{'id':'G4','state':'A_COMPLETER_AVANT_CORRECTION','title':'Publication des versions médicalement corrigées','requirement':'Le reçu en état conserve les octets historiques. Toute correction exige reçu scoped de version, adaptation des anciennes gardes et tests ; ne pas désactiver les contrôles.'}]
p['audit_lots']=[];p['production_lots']=[]
for mode in ['audit','production']:
 for s in p['scope']:
  for o in ['Codex','Claude']:
   rows=sorted([r for r in p[mode] if r['fragment']==s and r['owner']==o],key=lambda r:(r['priority'],r['code']))
   for j in range(0,len(rows),4):
    lot={'id':f'V2-{mode}-{s}-{o}-{j//4+1:02}','fragment':s,'owner':o,'codes':[r['code'] for r in rows[j:j+4]],'status':'PLANIFIE_NON_LANCE','lesson_count':len(rows[j:j+4])};p[mode+'_lots'].append(lot)
    for r in rows[j:j+4]:r['lot']=lot['id']
for m in ['audit','production','reserve']:
 assert len({r['code'] for r in p[m]})==len(p[m])
assert sum(len(p[m]) for m in ['audit','production','reserve'])==270
assert Counter(r['owner'] for r in p['production'])=={'Codex':77,'Claude':77}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'plan-v2.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
for m in ['audit','production','reserve']:
 with (OUT/f'attributions-{m}.csv').open('w',newline='') as f:
  fields=['assignment_id','fragment','chapter','code','title','owner','status','evidence_status','ssp_documented','legacy_ssp_unvalidated','write_paths','report_path'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for r in p[m]:w.writerow({k:r.get(k) if not isinstance(r.get(k),list) else '|'.join(map(str,r[k])) for k in fields})
 for r in p[m]:
  dest=OUT/'missions-planifiees';dest.mkdir(exist_ok=True);(dest/(r['assignment_id']+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(p['totals'],ensure_ascii=False));print([(s['id'],s['production_split']) for s in p['systems']])
