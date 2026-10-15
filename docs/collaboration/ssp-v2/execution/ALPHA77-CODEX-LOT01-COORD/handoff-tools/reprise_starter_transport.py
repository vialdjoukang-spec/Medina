import sys,json,subprocess,tempfile,os,importlib.util,uuid,hashlib,time
from pathlib import Path
if sys.stdin.isatty():
    import tty
    tty.setraw(sys.stdin.fileno())
ROOT=Path('/workspace/Medina-7-starter-codex')
BASE='3131a5cbf6cc003ead358e25152073959c53c4d9'
sys.path.insert(0,str(ROOT/'tools'))
import starter_codex as starter
import ai_session_guard as guard
def rpc(action,**kw):
    print(json.dumps(dict(action=action,**kw)),flush=True)
    response=json.loads(input())
    if response.get('error'): raise RuntimeError(response['error'])
    return response['result']
def import_commit(meta, state=None,path=None,parent=None):
    if state is not None:
        with tempfile.TemporaryDirectory() as tmp:
            env=dict(os.environ,GIT_INDEX_FILE=tmp+'/index')
            guard.git(ROOT,'read-tree',parent if parent else '--empty',env=env)
            raw=guard.canonical(state) if path=='registry.json' else starter.canonical(state)
            blob=guard.git(ROOT,'hash-object','-w','--stdin',data=raw).decode().strip()
            guard.git(ROOT,'update-index','--add','--cacheinfo','100644',blob,path,env=env)
            tree=guard.git(ROOT,'write-tree',env=env).decode().strip()
            assert tree==meta['tree']['sha']
    f=Path('/workspace/scratch/native-import-current.json');f.write_text(json.dumps(meta))
    subprocess.run(['python3','/workspace/scratch/import_native_commit.py',str(f),'--root',str(ROOT)],check=True,stdout=subprocess.DEVNULL)
    return meta['sha']
def fetch_registry(root,remote,cfg):
    sha=rpc('head',branch=cfg['registry_ref'].removeprefix('refs/heads/'))
    guard.commit(root,sha)
    return sha
def transact(root,remote,cfg,expected,state,message):
    parent_tree=guard.git(ROOT,'rev-parse',expected+'^{tree}').decode().strip()
    meta=rpc('cas',branch=cfg['registry_ref'].removeprefix('refs/heads/'),expected=expected,path='registry.json',content=guard.canonical(state).decode(),base_tree=parent_tree,message=message)
    return import_commit(meta,state,'registry.json',expected)
guard.fetch_registry=fetch_registry
guard.transact=transact
class Repo(starter.Repository):
    def refresh(self):
        self.main=rpc('head',branch='main');guard.commit(self.root,self.main);self.public_cache={};return self.main
    def state(self):
        response=rpc('state',branch='medina/7-starter-codex')
        return response['sha'],response['state']
    def cas(self,expected,state):
        meta=rpc('cas',branch='medina/7-starter-codex',expected=expected,path='state.json',content=starter.canonical(state).decode(),base_tree=None,message='7 Starter Codex transaction')
        return meta['sha']
    def prepare(self,mission,directory):
        self.git('merge-base','--is-ancestor',mission['base_sha'],self.main)
        acquired=guard.acquire(self.root,self.main,mission['id'])
        self.git('worktree','add','-b',mission['branch'],str(directory),self.main)
        started=guard.start(self.root,self.main,mission['id'],mission['actor'],mission['conversation'],registry_sha=acquired,worktree=directory)
        Path('/workspace/scratch/native-coord-start.json').write_text(json.dumps(started,ensure_ascii=False,indent=2))

_original_command=starter.command
def bridged_command(args,*a,**kw):
    if args[:3]==['gh','pr','view'] and len(args)>3 and args[3].isdigit():
        return json.dumps(rpc('pr',number=int(args[3]))).encode()
    if args[:2]==['gh','api'] and len(args)==3:
        return json.dumps(rpc('api',path=args[2])).encode()
    return _original_command(args,*a,**kw)
starter.command=bridged_command
# Public Git reads and normal pushes are authenticated and working. Keep the
# published Repository transport and strict closure validator unchanged except
# the two read-only gh JSON responses obtained from the connected GitHub app.
repo=starter.Repository(ROOT)
repo.refresh()
cfg=repo.json(repo.main,'.medina/7-starter-codex.json')
engine=starter.Engine(repo,cfg,'/workspace/scratch/starter-native-runtime')
action=sys.argv[1]
if action=='status':
    revision,state=repo.state();print(json.dumps({'done':{'revision':revision,'state':state}}),flush=True)
elif action=='verify-current':
    revision,state=repo.state();batch=cfg['queue'][state['batch']*7:(state['batch']+1)*7];results=[]
    for item in batch:
        try:repo.closure(item);results.append({'code':item['code'],'closed':True})
        except Exception as e:results.append({'code':item['code'],'closed':False,'reason_type':type(e).__name__})
    print(json.dumps({'done':{'main_sha':repo.main,'revision':revision,'results':results}}),flush=True)
elif action=='complete':
    revision,state=repo.state()
    starter.need(state['native_agent_id']=='/root/reprise_controleur','Controller attachment changed')
    state=engine.native('complete-native',state['request_id'],'/root/reprise_controleur')
    print(json.dumps({'done':state}),flush=True)
elif action=='test-pr':
    repo.merged_pr({'pr':int(sys.argv[2]),'merge_sha':sys.argv[3]})
    print(json.dumps({'done':{'validated_pr':int(sys.argv[2]),'real_ci':True,'main_sha':repo.main}}),flush=True)
else:raise ValueError('Unknown read/complete action')
