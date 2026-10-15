import json,hashlib,subprocess,datetime,re
from pathlib import Path
root=Path(__file__).resolve().parents[5]; code='N17'; out=Path(__file__).parent
base='3131a5cbf6cc003ead358e25152073959c53c4d9'
core=[f'chapters/{code}/{code}_{x}.html' for x in ['a','b','c','d','pop1','pop2']]+['glossary/n17.py']
sha=lambda b:hashlib.sha256(b).hexdigest()
source={p:sha(subprocess.check_output(['git','show',base+':'+p],cwd=root)) for p in core}
paths=core+[str(p.relative_to(root)) for p in sorted((root/'assets/img/n17/alpha/codex').glob('*')) if p.is_file()]
reviewed={p:sha((root/p).read_bytes()) for p in paths}
passages=json.loads((out/'passages-lus.json').read_text())['records']
notice='Révision Alpha en cours : des réserves sur les sources héritées et le protocole de calcium restent à vérifier ; les audits finaux de cette version ne sont pas clos.'
common=dict(schema_version=1,actor='Codex',code=code,status='provisional',medical_human_validation=False,reviewer='Distinct final reviewer /root/med_final_renal_hemo; not the candidate author',reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),base_sha=base,source_files_sha256=source,reviewed_files_sha256=reviewed,requirements_reviewed={'fundamental_analytical_semiology':True},unresolved_blockers=[notice])
evidence=[dict(type='consulted_source_passage',**p) for p in passages]
evidence += [dict(type='adopted_prior_audits',path=str((out/'adoption-audits.json').relative_to(root)),detail='Historical MED and LANG reviewed; adopted corrections compared against candidate. Historical reports are not promoted to final reports.'),dict(type='final_sciences_check',path=str((out/'final-sciences.json').relative_to(root)),result='passed; 6 disciplines, 4342 words, 7 figures; shared test unchanged'),dict(type='adopted_browser_evidence',path=str((out/'frontend-checks.json').relative_to(root)),detail='Desktop1440/mobile390, Enter/Space, popup, exclusive selection, Book24px; browser evidence predates the three language-only changes reviewed in lang-retouches-med-check.json; independent source-structure review performed.'),dict(type='independent_visual_review',detail='Both original assets inspected in final review. OpenStax nephron transport schematic and five-panel2018 biopsy correspond to caption; biopsy causality/IF limits retained. Other historical figure origin is not certified.')]
findings=[dict(id='N17-M01-M04',status='resolved',evidence='Compared candidate tables to S1/S3/S6 passages: immediate shock/urology, discussion as soon as possible≤24h, after-intervention reassessment, free light-chain assay and no single-test exclusion present.'),dict(id='N17-M05-FIG04-FIG05-FIG07',status='resolved',evidence='S7 biopsy passage:9 glomeruli/3 sclerosed, negative listed IF markers and noncausal case. Original OpenStax/2018 image rights and visual records adopted; IA structure drawings removed; figure7 now nonanatomical causal diagram.'),dict(id='N17-M06-M08',status='resolved',evidence='S8 exact Lokelma FI: tacrolimus≥2h, sodium400mg/5g so2400mg/day calculated; S9 Ventolin solution5mg/mL and UKKA10–20mg adjunct/offlabel distinguished; calcium redose linked to recurrent/persistentECG toxicity.'),dict(id='N17-CH-CALCIUM',status='unresolved',evidence='Swiss FI for exact imported calcium product unavailable in supplied evidence; HUG0.45mmol/min vs UKKA faster regimen remain attributed, unresolved. Foreign FI is not Swiss authorization.'),dict(id='N17-ERC-INHERITED',status='unresolved',evidence='ERC2025 original PDF not actually read; inherited400mL/day and other ERC-specific claims are not certified. Published2012 vs draft2026 KDIGO status passage is read and resolved.'),dict(id='N17-INHERITED-SCOPE',status='unresolved',evidence='Full inheritance not independently recertified claim-by-claim; detailed bedside gestures, other drugs/exact SwissFI, scientific figures of unknown provenance and OFS2026 remain outside demonstrated closure. Honest provisional notice retained.')]
for kind in ['MED','SEMIO']:
 r=dict(common,kind=kind,evidence=evidence)
 if kind=='MED':r['findings']=findings
 else:
  r['requirement']='fundamental_analytical_semiology'
  r['findings']=[dict(id='SEMIO-9-SECTIONS',status='resolved',evidence='Read substantive normal/signs/mechanisms/examination/interpretation/differentials/urgency/limits/sources in n17-s-semio; S1/S2/S3/S4/S5/S11 mappings traced to real excerpts. First tab, first exact h3, roles/aria and clinical pA marker verified.'),dict(id='SEMIO-LIMITS',status='non_blocking',evidence='No drug dose prescribed by new semiology; no unproved diagnostic performance. Source scope, adult/pediatric limits and CH/international distinctions explicit.'),dict(id='COURSE-PROVISIONAL',status='unresolved',evidence='SEMIO content requirement reviewed; whole-course publication remains provisional because calcium and inherited source-review blockers remain open; same visible notice.')]
 (out/(kind+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
manifest=dict(code=code,base_sha=base,source_files_sha256=source,reviewed_files_sha256=reviewed,unresolved_blockers=[notice],medical_human_validation=False)
(out/'final-hashset.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Refresh delivery snapshots, without changing source content.
for p in paths:
 dest=out/'final-source-snapshot'/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((root/p).read_bytes())
print(json.dumps({'files':len(reviewed),'reports':['MED.json','SEMIO.json'],'blockers':[notice]},ensure_ascii=False))
