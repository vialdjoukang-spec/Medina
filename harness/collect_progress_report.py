#!/usr/bin/env python3
"""Collecte en lecture seule, références distantes exactes, aucun heartbeat auteur."""
import argparse,datetime as dt,hashlib,json,subprocess,concurrent.futures,zipfile,io
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPO='vialdjoukang-spec/Medina'
def run(args,check=True):
 p=subprocess.run(args,cwd=ROOT,capture_output=True,timeout=180)
 if check and p.returncode:raise RuntimeError(p.stderr.decode(errors='replace')[:700])
 return p
def gh(endpoint):return run(['gh','api',endpoint]).stdout
def digest(data):return hashlib.sha256(data).hexdigest()
def gitbytes(sha,path):return run(['git','show',sha+':'+path]).stdout
def main():
 p=argparse.ArgumentParser();p.add_argument('output',type=Path);p.add_argument('--previous',type=Path,action='append',default=[],help='Collection antérieure dont les versions immuables restent à relire.');a=p.parse_args();out=a.output;out.mkdir(parents=True,exist_ok=True)
 now=dt.datetime.now(dt.timezone.utc).isoformat();report={'collected_at':now,'repo':REPO,'errors':[],'branches':{},'versions':[],'active_local':[],'artifacts':[]}
 refs={line.split('\t')[1].removeprefix('refs/heads/'):line.split('\t')[0] for line in run(['git','ls-remote','--heads','origin']).stdout.decode().splitlines()}
 report['main_sha']=refs.get('main');report['remote_refs_checked_at']=dt.datetime.now(dt.timezone.utc).isoformat()
 names=['status.json','dashboard.html','plan.json','deliverables.json','REPARTITION.md','monitor.json','prompt-lock.json','agents/neurologie/orchestration.md']
 for alias,branch in [('observations','codex/harness-observations-20261102'),('infrastructure','codex/harness-20261102')]:
  sha=refs[branch];folder=out/alias;folder.mkdir(exist_ok=True);report['branches'][alias]={'branch':branch,'sha':sha,'files':{}}
  for name in names+(['rapport-08h00.html'] if alias=='observations' else []):
   path='harness/'+name
   try:
    data=run(['gh','api','repos/'+REPO+'/contents/'+path+'?ref='+sha,'-H','Accept: application/vnd.github.raw+json']).stdout
    dest=folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    report['branches'][alias]['files'][name]={'sha256':digest(data),'bytes':len(data),'url':f'https://github.com/{REPO}/blob/{sha}/{path}'}
   except Exception as e:report['errors'].append({'branch':branch,'path':path,'error':str(e)})
 status=json.loads((out/'observations/status.json').read_text());deliver=json.loads((out/'observations/deliverables.json').read_text())
 report['status_generated_at']=status['generated_at'];report['completed_lessons']=status.get('completed_lessons',[])
 candidates={}
 for row in deliver['lessons']:
  branch=row.get('branch');sha=row.get('head_observed')
  if branch and sha:candidates[(branch,sha)]=row
 for row in status.get('completed_lessons',[])+status['agents']:
  branch=row.get('branch');sha=refs.get(branch)
  if branch and sha:candidates.setdefault((branch,sha),row)
 report['previous_collections']=[]
 for previous in a.previous:
  path=previous/'collection.json' if previous.is_dir() else previous
  data=path.read_bytes();old=json.loads(data)
  if old.get('repo')!=REPO:raise ValueError('Collection antérieure issue d’un autre dépôt')
  retained=[]
  for version in old.get('versions',[]):
   branch=version.get('branch');sha=version.get('version_sha')
   if branch and sha and version.get('preview'):
    candidates.setdefault((branch,sha),{'code':version['code'],'branch':branch})
    retained.append({'code':version['code'],'branch':branch,'sha':sha})
  report['previous_collections'].append({'path':str(path),'sha256':digest(data),'collected_at':old.get('collected_at'),'retained_versions':retained,'completion_inferred':False})
 def inspect(item):
  (branch,sha),row=item;code=row.get('code') or row.get('lesson');base=f'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-{code}-INTEGRATE';v={'code':code,'branch':branch,'version_sha':sha,'remote_head':refs.get(branch),'remote_branch_exists':branch in refs,'version_is_remote_head':sha==refs.get(branch),'evidence':{},'binding_checks':[],'errors':[]}
  folder=out/'lessons'/f'{code}-{sha[:10]}';folder.mkdir(parents=True,exist_ok=True)
  if run(['git','cat-file','-e',sha],False).returncode:run(['git','fetch','--no-write-fetch-head','origin',sha])
  paths=run(['git','ls-tree','-r','--name-only',sha,'--',base]).stdout.decode().splitlines();v['file_count']=len(paths)
  for path in paths:
   relative=path[len(base)+1:]
   # Petites preuves uniquement ; jamais les textes médicaux sources complets ni captures binaires.
   if (path.endswith('.json') or path.endswith('.md')) and '/preview/' not in path and not path.endswith('.bundle.json'):
    data=gitbytes(sha,path)
    if len(data)>1500000:continue
    dest=folder/relative;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    v['evidence'][relative]={'sha256':digest(data),'bytes':len(data),'url':f'https://github.com/{REPO}/blob/{sha}/{path}'}
  preview=base+f'/{code}-apercu-autonome.html'
  if preview in paths:
   data=gitbytes(sha,preview);v['preview']={'sha256':digest(data),'bytes':len(data),'url':f'https://raw.githubusercontent.com/{REPO}/{sha}/{preview}','proof_url':f'https://github.com/{REPO}/blob/{sha}/{preview}'}
  binding=folder/'source-binding.json'
  if binding.exists():
   b=json.loads(binding.read_text());v['binding_preview_matches']=b.get('preview_sha256')==v.get('preview',{}).get('sha256')
   for path,expected in b.get('final_sources',{}).items():
    try:actual=digest(gitbytes(sha,path));v['binding_checks'].append({'path':path,'expected':expected,'actual':actual,'ok':actual==expected})
    except Exception as e:v['errors'].append(str(e))
  v['local_evidence_folder']=str(folder.relative_to(out));return v
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
  for item,result in zip(candidates,ex.map(inspect,candidates.items())):report['versions'].append(result)
 for agent in status['agents']:
  root=Path(agent['worktree']);code=agent['lesson'];base=root/f'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-{code}-INTEGRATE'
  record={k:agent.get(k) for k in ['id','lesson','stage','activity_at','started_at','message','branch','tokens_input','tokens_output','cost_usd','completed_sections']}
  record['remote_head']=refs.get(agent['branch']);record['worktree_available']=root.exists();record['current_evidence']={}
  if root.exists():
   record['local_head']=run(['git','-C',str(root),'rev-parse','HEAD']).stdout.decode().strip()
   record['dirty_paths']=run(['git','-C',str(root),'status','--porcelain']).stdout.decode().splitlines()
   for file in base.rglob('*.json'):
    if 'preview' in file.relative_to(base).parts or file.stat().st_size>1000000:continue
    data=file.read_bytes();rel=str(file.relative_to(base));dest=out/'active'/code/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    record['current_evidence'][rel]={'sha256':digest(data),'bytes':len(data)}
  report['active_local'].append(record)
 runs=json.loads(gh(f'repos/{REPO}/actions/workflows/medina-harness-watch.yml/runs?per_page=100'))['workflow_runs']
 report['workflow_runs']=[{k:r.get(k) for k in ['id','event','status','conclusion','created_at','updated_at','head_branch','head_sha','html_url']} for r in runs]
 dispatch=[r for r in runs if r['event']=='workflow_dispatch'];chosen=dispatch[:3]
 at8=[r for r in dispatch if r['created_at']>='2026-11-02T07:00:00Z']
 if at8:chosen.append(min(at8,key=lambda r:r['created_at']))
 for r in {r['id']:r for r in chosen}.values():
  artifacts=json.loads(gh(f'repos/{REPO}/actions/runs/{r["id"]}/artifacts'))['artifacts']
  for art in artifacts:
   if not art['name'].startswith('medina-independent-'):continue
   entry={k:art.get(k) for k in ['id','name','expired','created_at','size_in_bytes']};entry['run_id']=r['id'];entry['files']={}
   if not art['expired']:
    try:data=gh(f'repos/{REPO}/actions/artifacts/{art["id"]}/zip')
    except Exception:
     entry['download_error']='Téléchargement de l’artefact refusé (HTTP403 observé) ; contenu non consulté, métadonnées seules. Aucune URL signée conservée.'
     report['artifacts'].append(entry)
     continue
    with zipfile.ZipFile(io.BytesIO(data)) as z:
     for n in z.namelist():
      if Path(n).name in ['remote-dashboard.html','remote-status.json','remote-observation.json','rapport-08h00.html']:
       content=z.read(n);dest=out/'artifacts'/str(r['id'])/Path(n).name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(content);entry['files'][Path(n).name]={'sha256':digest(content),'bytes':len(content),'local':str(dest.relative_to(out))}
   report['artifacts'].append(entry)
 report['completed_at']=dt.datetime.now(dt.timezone.utc).isoformat()
 (out/'collection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'out':str(out),'versions':len(report['versions']),'completed':len(report['completed_lessons']),'artifacts':len(report['artifacts']),'errors':report['errors'],'finished':report['completed_at']},ensure_ascii=False))
if __name__=='__main__':main()
