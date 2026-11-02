#!/usr/bin/env python3
"""Reconstruire et vérifier les octets D63 ; aucune publication ni relecture fictive."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def main():
 receipt={'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'code':'D63','checks':[],'clinical_certification':False,'closure':False}
 commands=[
 ('static',[sys.executable,'test_v7.py','--static','D63']),
 ('sciences',[sys.executable,'tests/audit_sciences.py','--base','8a512893acbab9caa0dcfdd0e8682a44ea72fda6','--codes','D63','--out',str(OUT/'sciences-final.json')]),
 ('verite',[sys.executable,'tools/betta_verite.py',str(OUT/'recherche_D63')]),
 ('build',[sys.executable,'build_front.py','--fragment','S06']),
 ('bundle',[sys.executable,'/workspace/Medina-harness/harness/bundle_native.py',str(OUT/'preview/fragments/MEDINA_S06_hematopoietique-lymphatique.html'),str(ROOT),'D63',str(OUT/'D63-apercu-autonome.html')]),
 ('browser',[sys.executable,str(OUT/'browser_probe.py')])]
 for label,command in commands:
  result=subprocess.run(command,cwd=ROOT,env={**os.environ,'MEDINA_OUT':str(OUT/'preview')},capture_output=True,text=True,timeout=300)
  (OUT/(label+'-verification.log')).write_text(result.stdout+result.stderr);receipt['checks'].append({'check':label,'exit_code':result.returncode,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
  if result.returncode:
   (OUT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n');raise SystemExit(label+' failed; inspect log')
 paths=[*sorted((ROOT/'chapters/D63').glob('*.html')),ROOT/'glossary/d63.py',*sorted((ROOT/'assets/img/d63/alpha/codex').glob('*'))]
 receipt['final_sources']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()};receipt['preview_sha256']=hashlib.sha256((OUT/'D63-apercu-autonome.html').read_bytes()).hexdigest();receipt['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();receipt['ok']=True
 (OUT/'verification.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'ok':True,'checks':len(commands),'preview_sha256':receipt['preview_sha256'],'closure':False}))
if __name__=='__main__':main()
