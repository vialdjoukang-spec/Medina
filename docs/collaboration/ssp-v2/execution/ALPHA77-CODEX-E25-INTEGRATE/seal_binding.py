from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
stat=json.loads((D/'static-report.json').read_text())
preview=D/'E25-apercu-autonome.html'
validation=json.loads((D/'harness-validation.json').read_text())
assert validation['technical_contract_pass'] and not validation['errors']
def save(n,v):(D/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
R=D.parents[4]
assert not (D/'source-binding.json').exists()
reviews=json.loads((D/'lesson-manifest.json').read_text())['reviews']
ck=['static-report.json','static-check.log','audit-sciences.json','browser-report.json','visual-inspection.json','coverage-14-20.json','source-ledger.json','source-cache-manifest.json','lesson-manifest.json','figure-integrity.json','review-corrections.json','harness-validation.json','binding-invalidation.json','research-gate.log','remaining-findings.json','RAPPORT-E25.md','figure-license-metadata.json','E25-apercu-autonome.bundle.json','review-inputs/E25-source.html',*['reviews/'+k+'.json' for k in reviews]]
save('source-binding.json',dict(code='E25',verified_at=now,preview=preview.name,preview_sha256=sha(preview),final_sources={**stat['source_files_sha256'],'glossary/e25.py':sha(R/'glossary/e25.py'),**stat['original_images']},checks=ck,check_sha256={p:sha(D/p) for p in ck},clinical_certification=False,automatic_refresh=False))
print('Explicit final seal after passed harness validation',sha(preview))
