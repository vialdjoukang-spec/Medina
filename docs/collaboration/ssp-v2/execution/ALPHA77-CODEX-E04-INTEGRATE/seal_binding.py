from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent;R=D.parents[4]
assert not (D/'source-binding.json').exists(),'Never refresh a final binding automatically.'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
validation=json.loads((D/'harness-validation.json').read_text());assert validation['technical_contract_pass'] and not validation['errors']
stat=json.loads((D/'static-report.json').read_text());preview=D/'E04-apercu-autonome.html';reviews=json.loads((D/'lesson-manifest.json').read_text())['reviews']
for p,h in stat['source_files_sha256'].items():assert sha(R/p)==h,p
ck=['static-report.json','production.json','catalogue-proof.json','strict-semiology-final.json','strict-semiology-initial-failure.json','static-check.log','audit-sciences.json','browser-report.json','visual-inspection.json','coverage-14-20.json','source-ledger.json','source-cache-manifest.json','lesson-manifest.json','figure-integrity.json','figure-inventory-before-after.json','review-corrections.json','harness-validation.json','research-gate.log','remaining-findings.json','RAPPORT-E04.md','figure-license-metadata.json','E04-apercu-autonome.bundle.json','review-inputs/E04-source.html',*['reviews/'+k+'.json' for k in reviews]]
out=dict(code='E04',verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),preview=preview.name,preview_sha256=sha(preview),final_sources={**stat['source_files_sha256'],'glossary/e04.py':sha(R/'glossary/e04.py'),**stat['original_images']},checks=ck,check_sha256={p:sha(D/p) for p in ck},clinical_certification=False,automatic_refresh=False)
catalogue=json.loads((D/'catalogue-proof.json').read_text());assert sha(R/'chapters.json')==catalogue['final_sha256'];out['shared_catalogue']=catalogue
(D/'source-binding.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('Explicit final seal after technical validation',sha(preview))
