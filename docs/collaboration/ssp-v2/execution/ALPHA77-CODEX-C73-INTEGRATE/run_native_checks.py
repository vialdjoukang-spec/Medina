from pathlib import Path
import json,hashlib,datetime,subprocess,os,shutil
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent
assert not(D/'source-binding.json').exists()
files=sorted((R/'chapters/C73').glob('*.html'))+[R/'glossary/c73.py']+sorted((R/'assets/img/c73/alpha/codex').glob('*'))
(D/'production.json').write_text(json.dumps({'schema_version':1,'complete':True,'mission':'ALPHA77-CODEX-C73-INTEGRATE','code':'C73','assembled_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_sha':'8a512893acbab9caa0dcfdd0e8682a44ea72fda6','final_files':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files},'scope':'Assembly receipt only, no clinical certification.','human_validation':False},indent=2)+'\n')
env={**os.environ,'PYTHONPATH':'/tmp/medina-n29-pydeps','MEDINA_OUT':'/tmp/medina-c73-native'}
cmds=[('static-check.log',['python3','test_v7.py','--static','C73']),('static-report.log',['python3',str(D/'static_checks.py')]),('audit-sciences.log',['python3','tests/audit_sciences.py','--base','8a512893acbab9caa0dcfdd0e8682a44ea72fda6','--codes','C73','--out',str(D/'audit-sciences.json')]),('native-build.log',['python3','build_front.py','--fragment','S05'])]
def run(row):
 name,cmd=row;r=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True);(D/name).write_text(r.stdout+r.stderr);return name,r.returncode,(r.stdout+r.stderr)[-700:]
with ThreadPoolExecutor(max_workers=4)as ex:
 for name,code,out in ex.map(run,cmds):print(name,code,out,flush=True);assert code==0
native=D/'.native-source-S05.html';shutil.copyfile('/tmp/medina-c73-native/fragments/MEDINA_S05_endocrinien-metabolique.html',native)
r=subprocess.run(['python3','/workspace/Medina-harness/harness/bundle_native.py',str(native),str(R),'C73',str(D/'C73-apercu-autonome.html')],cwd=R,env=env,capture_output=True,text=True);(D/'native-bundle.log').write_text(r.stdout+r.stderr);print('bundle',r.returncode,r.stdout[-1200:],flush=True);assert r.returncode==0,r.stderr

assert hashlib.sha256(native.read_bytes()).hexdigest()==hashlib.sha256(Path('/tmp/medina-c73-native/fragments/MEDINA_S05_endocrinien-metabolique.html').read_bytes()).hexdigest();native.unlink()
