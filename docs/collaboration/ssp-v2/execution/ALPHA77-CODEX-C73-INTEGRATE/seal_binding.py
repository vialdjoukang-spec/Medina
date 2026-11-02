from pathlib import Path
import json,hashlib,datetime,subprocess
D=Path(__file__).resolve().parent;R=D.parents[4];target=D/'source-binding.json'
assert not target.exists(),'Never refresh a final binding automatically.'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
validation=json.loads((D/'harness-validation.json').read_text());assert validation['technical_contract_pass']and not validation['errors']
stat=json.loads((D/'static-report.json').read_text());manifest=json.loads((D/'lesson-manifest.json').read_text());browser=json.loads((D/'browser-report.json').read_text());visual=json.loads((D/'visual-inspection.json').read_text());preview=D/'C73-apercu-autonome.html'
assert sha(preview)==browser['preview_sha256']==visual['preview_sha256']and browser['result']=='passed'
for name,expected in stat['source_files_sha256'].items():assert sha(R/name)==expected,name
for name,expected in visual['captures_inspected_final'].items():assert sha(D/name)==expected,name
for name,review in manifest['reviews'].items():assert sha(D/review['path'])==review['sha256'],name
for source in json.loads((D/'source-ledger.json').read_text())['sources']:assert sha(source['cache_external'])==source['sha256'],source['id']
catalogue=json.loads((D/'catalogue-proof.json').read_text());assert sha(R/'chapters.json')==catalogue['final_sha256']
# All frozen dossier artifacts, including historical failure proofs, are enumerated.
checks=sorted(str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and '__pycache__'not in p.parts and p.name not in {'source-binding.json','harness-completion.json'}and not p.name.startswith('.native-source'))
final_sources={**stat['source_files_sha256'],'glossary/c73.py':sha(R/'glossary/c73.py'),**{p:v['sha256']for p,v in stat['original_images'].items()}}
out=dict(code='C73',verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),preview=preview.name,preview_sha256=sha(preview),final_sources=final_sources,checks=checks,check_sha256={p:sha(D/p)for p in checks},shared_catalogue=catalogue,clinical_certification=False,human_validation=False,automatic_refresh=False)
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'explicit_final_seal':out['verified_at'],'binding_sha256':sha(target),'preview_sha256':out['preview_sha256'],'checks':len(checks),'canonical_sources':len(final_sources)},indent=2))
