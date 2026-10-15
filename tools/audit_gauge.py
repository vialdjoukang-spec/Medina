#!/usr/bin/env python3
"""Read-only remote audit gauge. Cache and optional receipts are local files only."""
import argparse,hashlib,importlib.util,json,os,re,subprocess,sys,time,urllib.error,urllib.request
from pathlib import Path
FIRST=['I63','G01','E10','E05','N17','D69','D64']
TTL=30

def git(root,*args,check=True):
 return subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,check=check).stdout.strip()
def digest(value):
 return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def read_json(root,sha,path):
 return json.loads(git(root,'show',sha+':'+path))
class NoPublicRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,request,fp,code,msg,headers,newurl):
  raise urllib.error.HTTPError(request.full_url,code,'Public run redirects refused',headers,fp)
def public_run_command(original):
 """Transport-only override for one public, read-only GitHub endpoint."""
 def command(args,*pos,**kwargs):
  if not (isinstance(args,(list,tuple)) and len(args)==3 and args[:2]==['gh','api'] and
          isinstance(args[2],str) and re.fullmatch(r'repos/vialdjoukang-spec/Medina/actions/runs/[1-9][0-9]*',args[2])):
   return original(args,*pos,**kwargs)
  url='https://api.github.com/'+args[2]
  request=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'Medina-audit-gauge'})
  opener=urllib.request.build_opener(NoPublicRedirect())
  with opener.open(request,timeout=15) as response:
   if response.status!=200 or response.geturl()!=url:raise ValueError('Public run endpoint mismatch')
   body=response.read(2*1024*1024+1)
   if len(body)>2*1024*1024:raise ValueError('Public run response too large')
   return body
 return command
def verify_closures(root,main,q,candidates):
 closed=[];errors=[]
 try:
  engine_path=Path(root)/'tools/starter_codex.py'
  if git(root,'show',main+':tools/starter_codex.py')!=engine_path.read_text().strip():raise ValueError('local engine differs from remote main')
  spec=importlib.util.spec_from_file_location('audit_starter_engine',engine_path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
  module.command=public_run_command(module.command)
  repo=module.Repository(root);repo.main=main
  checker=getattr(repo,'closure_proof',None) or repo.closure
  for item in q:
   if item['code'] not in candidates:continue
   try:checker(item);closed.append(item['code'])
   except Exception as exc:errors.append(item['code']+': '+type(exc).__name__)
 except Exception as exc:errors.append('closure_engine: '+type(exc).__name__)
 return closed,errors
def collect(root):
 reports={};errors=[];closed=[]
 remote=dict((ref,sha) for sha,ref in (line.split() for line in git(root,'ls-remote','origin','refs/heads/*').splitlines()))
 main=remote['refs/heads/main'];git(root,'fetch','--quiet','--no-tags','origin','refs/heads/main')
 cfg=read_json(root,main,'.medina/7-starter-codex.json');q=cfg['queue']
 if len(q)!=77 or len({item['code'] for item in q})!=77:raise ValueError('expected 77 unique queue entries')
 state_sha=remote.get('refs/heads/medina/7-starter-codex');state={}
 if state_sha:
  git(root,'fetch','--quiet','--no-tags','origin','refs/heads/medina/7-starter-codex')
  state=read_json(root,state_sha,'state.json')
 batch=state.get('batch',0)
 if type(batch) is not int or not 0<=batch<=10:raise ValueError('invalid campaign batch')
 current=q[batch*7:(batch+1)*7];codes=[item['code'] for item in current]
 for item in current:
  code=item['code']
  for role in ['MED','LANG']:
   try:
    ident=item['missions'][role]
    if not re.fullmatch(r'ALPHA(?:1|77)-CODEX-'+re.escape(code)+'-'+role,ident):raise ValueError('invalid mission ID')
    mission=read_json(root,main,'.medina/missions/'+ident+'.json')
    if not (mission.get('id')==ident and mission.get('owner')=='Codex' and mission.get('actor')=='Codex' and mission.get('codes')==[code]):raise ValueError('untrusted mission')
    branch=mission['branch']
    if not re.fullmatch(r'[A-Za-z0-9/_-]+',branch):raise ValueError('invalid mission branch')
    ref='refs/heads/'+branch;sha=remote.get(ref)
    if not sha:continue
    git(root,'fetch','--quiet','--no-tags','origin',ref)
    prefix='docs/collaboration/ssp-v2/execution/'+ident+'/'
    paths=git(root,'ls-tree','-r','--name-only',sha,'--',prefix).splitlines();valid=[]
    for path in paths:
     if str(Path(path).parent)!=prefix.rstrip('/') or not re.fullmatch(r'rapport[^/]*\.(json|md)',Path(path).name):continue
     try:
      body=git(root,'show',sha+':'+path)
      if not body.strip():continue
      if path.endswith('.json') and not json.loads(body):continue
     except (ValueError,subprocess.CalledProcessError):continue
     valid.append(path)
    if valid:reports[code+'-'+role]={'sha':sha,'ref':ref,'paths':valid,'mission':ident}
   except (ValueError,KeyError,subprocess.CalledProcessError) as exc:errors.append(code+'-'+role+': '+type(exc).__name__)
 claims=state.get('closed',[])
 if not isinstance(claims,list) or any(not isinstance(c,str) for c in claims):raise ValueError('invalid closure claims')
 candidates=set(claims)
 # Native workers can publish 1..6 genuine closures before the controller updates state.closed.
 for item in current:
  path=item.get('closure_path')
  if path and git(root,'ls-tree','--name-only',main,'--',path)==path:candidates.add(item['code'])
 if candidates:
  closed,proof_errors=verify_closures(root,main,q,candidates);errors.extend(proof_errors)
 return {'main_sha':main,'queue_source':'remote-main','queue_sha256':digest(q),'state_sha':state_sha,'phase':state.get('phase','UNKNOWN'),'batch':batch,'cycle_codes':codes,'reports':reports,'verified_closed':closed,'closure_errors':errors,'total_lessons':len(q),'local_snapshot':False}
def snapshot(root,local=None,cache=None,fresh=False):
 if local:
  raw=json.loads(Path(local).read_text())
  if not isinstance(raw,dict) or not raw:raise ValueError('empty/invalid snapshot')
  # Test fixtures describe reports only: unchecked completion assertions are rejected.
  raw['verified_closed']=[];raw['local_snapshot']=True
 else:
  if cache and not fresh and Path(cache).exists():
   old=json.loads(Path(cache).read_text())
   if old.get('format_version')==3 and old.get('root')==str(Path(root).resolve()) and 0<=time.time()-old.get('generated_at',0)<TTL:return old
  raw=collect(root)
 raw['format_version']=3;raw['root']=str(Path(root).resolve());raw['generated_at']=time.time();raw['nonce']=os.urandom(4).hex()
 batch=raw.get('batch',0);codes=raw.get('cycle_codes',FIRST)
 if type(batch) is not int or not 0<=batch<=10 or len(codes)!=7:raise ValueError('invalid batch snapshot')
 reports=raw.get('reports',{});n=len({k for k,v in reports.items() if k in {c+'-'+r for c in codes for r in ['MED','LANG']} and v})
 closed=set(raw.get('verified_closed',[]));first=len(closed.intersection(codes));total=len(closed)
 raw['reports_count']=n;raw['closed_cycle']=first;raw['closed_total']=total
 k=round(first/7*7)
 raw['gauge_line']=f'CODEX LOT {batch+1:02d}/11  {"█"*k}{"░"*(7-k)}  {first}/7 clôturées · {n}/14 rapports · TOTAL {total}/77 · SEMIO {first}/7 vérifiées'
 if raw.get('closure_errors'):raw['gauge_line']+=' · vérification incomplète'
 raw['snapshot_sha256']=digest(raw)
 raw['receipt_line']=f'[G:{raw["snapshot_sha256"][:8]}:{raw["nonce"]}]'
 raw['gauge_line']+=' '+raw['receipt_line']
 if cache and not local:
  Path(cache).parent.mkdir(parents=True,exist_ok=True)
  Path(cache).write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
 return raw
def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default=str(Path(__file__).resolve().parents[1]));p.add_argument('--local-snapshot');p.add_argument('--format',choices=['plain','json'],default='plain');p.add_argument('--cache',default=str(Path.home()/'.cache/medina-audit-gauge.json'));p.add_argument('--fresh',action='store_true');p.add_argument('--update-output',help='Write a local gauge receipt outside the repository')
 a=p.parse_args();Path(a.cache).parent.mkdir(parents=True,exist_ok=True)
 try:s=snapshot(a.root,a.local_snapshot,a.cache,a.fresh)
 except (ValueError,KeyError,OSError,subprocess.CalledProcessError) as exc:
  print('Gauge unavailable: '+type(exc).__name__+'; no unchecked counts emitted.',file=sys.stderr);return 2
 if a.update_output:
  out=Path(a.update_output).resolve();root=Path(a.root).resolve()
  if out==root or root in out.parents:p.error('output must be outside repository')
  out.parent.mkdir(parents=True,exist_ok=True)
  out.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(s,ensure_ascii=False,indent=2) if a.format=='json' else s['gauge_line'])
if __name__=='__main__':sys.exit(main())
