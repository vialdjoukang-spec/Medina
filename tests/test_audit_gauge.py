import json,tempfile,time,unittest
from unittest.mock import patch
from pathlib import Path
try:
 from tools.audit_gauge import snapshot,digest,collect,FIRST,public_run_command
 from tools.audit_response_gate import validate,stop_decision
 MODULE='tools.audit_gauge'
except ModuleNotFoundError:
 from audit_gauge import snapshot,digest,collect,FIRST,public_run_command
 from audit_response_gate import validate,stop_decision
 MODULE='audit_gauge'
class GaugeTests(unittest.TestCase):
 def fixture(self,value):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'source.json';p.write_text(json.dumps(value));return snapshot(d,str(p))
 def test_reports_are_not_closures(self):
  s=self.fixture({'reports':{'I63-MED':{'sha':'a'},'I63-LANG':{'sha':'b'}},'closed':['I63'],'verified_closed':['I63']})
  self.assertEqual(s['reports_count'],2);self.assertEqual(s['closed_total'],0)
 def test_verification_errors_are_explicit(self):
  s=self.fixture({'reports':{},'closure_errors':['I63: auth unavailable']})
  self.assertIn('vérification incomplète',s['gauge_line'])
 def test_fake_closure(self):
  s=self.fixture({'complete':True,'closed':['I63'],'verified_closed':['I63']});self.assertEqual(s['closed_cycle'],0)
 def test_empty(self):
  with self.assertRaises(ValueError):self.fixture({})
 def test_gate(self):
  s=self.fixture({'reports':{}});draft=s['gauge_line']+'\n'+s['receipt_line']
  self.assertTrue(validate(draft,s)[0]);self.assertFalse(validate('Texte sans jauge',s)[0]);self.assertFalse(validate(draft.replace('0/14','14/14'),s)[0]);self.assertFalse(validate(draft,s,now=s['generated_at']+31)[0])
 def test_changed_hash(self):
  s=self.fixture({'reports':{}});draft=s['gauge_line']+'\n'+s['receipt_line'];s['closed_total']=77;self.assertFalse(validate(draft,s)[0])
 def remote_fixture(self,empty_md=False,partial=False):
  codes=FIRST+['X'+str(i) for i in range(70)]
  q=[{'code':c,'missions':{r:('ALPHA1' if c in FIRST else 'ALPHA77')+'-CODEX-'+c+'-'+r for r in ['MED','LANG']}} for c in codes]

  for item in q:item['closure_path']='closures/'+item['code']+'.json'
  current=q[7:14];refs={'refs/heads/main':'main','refs/heads/medina/7-starter-codex':'state'}
  for item in current:
   for role in ['MED','LANG']:refs['refs/heads/custom/'+item['code']+'-'+role]=item['code']+role
  def fake_git(root,*args,**kwargs):
   if args[0]=='ls-remote':return '\n'.join(sha+' '+ref for ref,sha in refs.items())
   if args[0]=='fetch':return ''
   if args[0]=='show':
    sha,path=args[1].split(':',1)
    if path=='.medina/7-starter-codex.json':return json.dumps({'queue':q})
    if path=='state.json':return json.dumps({'batch':1,'phase':'AUDITING','closed':[]})
    if path.startswith('.medina/missions/'):
     ident=Path(path).stem;parts=ident.split('-');code,role=parts[2:]
     return json.dumps({'id':ident,'owner':'Codex','actor':'Codex','codes':[code],'branch':'custom/'+code+'-'+role})
    if path.endswith('.md'):return '   ' if empty_md and sha=='X0MED' else 'Rapport réellement commité'
    return '{}'
   if args[0]=='ls-tree' and args[1]=='--name-only':return args[-1] if partial and args[-1]=='closures/X0.json' else ''
   if args[0]=='ls-tree':return args[-1]+('rapport.md' if args[3].endswith('MED') else 'rapport.json')
   raise AssertionError(args)
  def verifier(root,main,queue,candidates):
   self.assertEqual(candidates,{'X0'});return ['X0'],[]
  with patch(MODULE+'.git',fake_git),patch(MODULE+'.verify_closures',side_effect=verifier):return collect('/unused')
 def test_cycle_two_manifest_branches_and_empty_json(self):
  raw=self.remote_fixture();self.assertEqual(len(raw['reports']),7)
  self.assertEqual(raw['batch'],1);self.assertEqual(raw['cycle_codes'],['X'+str(i) for i in range(7)])
  s=self.fixture(raw);self.assertIn('LOT 02/11',s['gauge_line']);self.assertEqual(s['reports_count'],7)
 def test_partial_main_closure_without_state_claim(self):
  raw=self.remote_fixture(partial=True)
  self.assertEqual(raw['verified_closed'],['X0'])
  with patch(MODULE+'.collect',return_value=raw):s=snapshot('/unused',fresh=True)
  self.assertEqual(s['closed_cycle'],1);self.assertEqual(s['closed_total'],1)
 def test_empty_md_not_report(self):
  self.assertEqual(len(self.remote_fixture(empty_md=True)['reports']),6)
 def test_actual_native_closure_engine_rejects_unproved_complete(self):
  try:
   from tools import starter_codex as engine
  except ImportError:self.skipTest('requires repository starter engine')
  repo=engine.Repository('/unused');repo.main='a'*40
  with patch.object(repo,'json',return_value={'complete':True,'code':'I63'}):
   with self.assertRaises(engine.Blocked):repo.closure({'code':'I63','closure_path':'closure.json'})
 def test_stop_invalid_structured_json_blocks(self):
  import subprocess,sys
  r=subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/'tools/audit_response_gate.py'),'--stop-hook'],input='{',capture_output=True,text=True)
  self.assertEqual(r.returncode,0);self.assertEqual(json.loads(r.stdout)['decision'],'block')
 def test_public_run_transport_exact_endpoint_only(self):
  from unittest.mock import Mock
  original=Mock(return_value=b'original');wrapped=public_run_command(original)
  for endpoint in ['repos/other/Medina/actions/runs/1','repos/vialdjoukang-spec/Medina/actions/runs/0','repos/vialdjoukang-spec/Medina/actions/runs/1?x=2','repos/vialdjoukang-spec/Medina/actions/runs/1/../2']:
   self.assertEqual(wrapped(['gh','api',endpoint],'/repo'),b'original')
  self.assertEqual(original.call_count,4)
  response=Mock();response.status=200;response.geturl.return_value='https://api.github.com/repos/vialdjoukang-spec/Medina/actions/runs/123';response.read.return_value=b'{"conclusion":"failure"}'
  response.__enter__=Mock(return_value=response);response.__exit__=Mock(return_value=False)
  opener=Mock();opener.open.return_value=response
  with patch(MODULE+'.urllib.request.build_opener',return_value=opener):
   self.assertEqual(wrapped(['gh','api','repos/vialdjoukang-spec/Medina/actions/runs/123'],'/repo'),b'{"conclusion":"failure"}')
  req=opener.open.call_args.args[0];self.assertEqual(req.full_url,response.geturl.return_value);self.assertNotIn('Authorization',req.headers);self.assertEqual(opener.open.call_args.kwargs['timeout'],15)
 def test_public_transport_auth_failure_propagates(self):
  import urllib.error
  from unittest.mock import Mock
  opener=Mock();opener.open.side_effect=urllib.error.HTTPError('https://api.github.com/',401,'Unauthorized',{},None)
  with patch(MODULE+'.urllib.request.build_opener',return_value=opener):
   with self.assertRaises(urllib.error.HTTPError):public_run_command(Mock())(['gh','api','repos/vialdjoukang-spec/Medina/actions/runs/123'],'/repo')
 def test_original_pages_run_rejects_workflow_failure(self):
  from tools import starter_codex as engine
  value={'workflow_id':engine.PAGES_WORKFLOW,'path':'.github/workflows/pages.yml','repository':{'full_name':engine.PAGES_REPOSITORY},'head_repository':{'full_name':engine.PAGES_REPOSITORY},'head_sha':'a'*40,'head_branch':'main','status':'completed','conclusion':'failure'}
  with patch.object(engine,'command',return_value=json.dumps(value).encode()):
   with self.assertRaises(engine.Blocked):engine.Repository('/unused').pages_run({'run_id':123,'main_sha':'a'*40})
 def test_stop_adapter(self):
  s=self.fixture({'reports':{}})
  for active in [False,True]:
   result=stop_decision({'hook_event_name':'Stop','last_assistant_message':'sans jauge','stop_hook_active':active},s)
   self.assertEqual(result['decision'],'block')
  self.assertEqual(stop_decision({'hook_event_name':'Stop','last_assistant_message':s['gauge_line']+'\n'+s['receipt_line']},s),{})
 def test_tampered_gauge(self):
  s=self.fixture({'reports':{}});s['gauge_line']='CODEX  FAUX';self.assertFalse(validate(s['gauge_line']+'\n'+s['receipt_line'],s)[0])
 def test_invalid_missions(self):
  s=self.fixture({'reports':{'CLAUDE-I63-MED':True,'I63-PROOF':True,'I63-MED':True}});self.assertEqual(s['reports_count'],1)
if __name__=='__main__':unittest.main()
