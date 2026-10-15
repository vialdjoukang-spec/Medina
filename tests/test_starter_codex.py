import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / 'tools/starter_codex.py'
spec = importlib.util.spec_from_file_location('starter', MODULE)
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)


def configuration():
    codes = s.FIRST + ['G%02d' % n for n in range(2, 76) if 'G%02d' % n not in s.FIRST][:70]
    return {'schema_version': 1, 'queue': [dict(code=c, owner='Codex', mode='existing' if i < 52 else 'production',
        closure_path='docs/collaboration/ssp-v2/execution/' + c + '-INTEGRATE/closure.json', production_receipt='production/' + c + '.json',
        missions={r: c + '-' + r for r in ('MED', 'LANG', 'INTEGRATE', 'PRODUCE')}) for i, c in enumerate(codes)],
        'batches': [{'coordinator_mission': 'COORD-%s' % i} for i in range(11)],
        'image_tasks_done': [{'path': 'images-done.json', 'sha256': '0' * 64}]}


class MemoryRepository:
    def __init__(self):
        self.main = 'a' * 40
        self.value = {'schema_version': 1, 'closed': [], 'batch': 0, 'phase': 'IDLE', 'workers': []}
        self.closed = set()
        self.prepared = 0
        self.writes = 0

    def refresh(self):
        return self.main

    def state(self):
        return str(self.writes), self.value.copy()

    def cas(self, revision, state):
        if revision != str(self.writes):
            raise s.Blocked('race')
        self.writes += 1
        self.value = state.copy()
        return str(self.writes)

    def closure(self, item):
        if item['code'] not in self.closed:
            raise s.Blocked('reports exist but no final proof')

    def mission(self, ident, codes, role=None):
        return {'id': ident, 'requested_model': 'GPT6.1', 'requested_effort': 'medium' if ident.endswith('-LANG') else 'high'}

    def prepare(self, mission, directory):
        self.prepared += 1

    def checked_blob(self, revision, receipt):
        return b'{"owner":"Codex","complete":true}'


class EngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cfg = configuration()
        self.repo = MemoryRepository()
        self.engine = s.Engine(self.repo, self.cfg, self.tmp.name)

    def test_77_includes_first_seven(self):
        self.assertEqual(len(s.validate_config(self.cfg)['queue']), 77)
        self.cfg['queue'].append(self.cfg['queue'][0])
        with self.assertRaises(s.Blocked):
            s.validate_config(self.cfg)

    def test_claude_never_enters_queue_or_paths(self):
        self.cfg['queue'][7]['owner'] = 'Claude'
        with self.assertRaises(s.Blocked):
            s.validate_config(self.cfg)
        with self.assertRaises(s.Blocked):
            s.safe_path('livraisons/Livraison Claude/report.json')

    def test_reports_do_not_close_or_advance(self):
        with patch.object(self.engine, 'worker', return_value={'phase': 'RUNNING'}) as worker:
            self.engine.tick()
        self.assertEqual(self.repo.value['closed'], [])
        self.assertEqual(self.repo.value['batch'], 0)
        self.assertIn('do not redispatch the same unchanged audits', worker.call_args.args[-1])

    def test_seven_real_closures_required_before_next_batch(self):
        self.repo.closed.update(s.FIRST[:6])
        with patch.object(self.engine, 'worker', return_value={}):
            self.engine.tick()
        self.assertEqual(self.repo.value['batch'], 0)
        self.repo.value['phase'] = 'IDLE'
        self.repo.closed.add(s.FIRST[-1])
        with patch.object(self.engine, 'worker', return_value={}):
            self.engine.tick()
        self.assertEqual(self.repo.value['batch'], 1)

    def test_ambiguous_spawn_never_replays(self):
        with patch.object(self.engine, 'worker', side_effect=OSError('crash')):
            self.engine.tick()
        self.assertEqual(self.repo.value['phase'], 'NEEDS_RECONCILIATION')
        self.engine.tick()
        self.assertEqual(self.repo.prepared, 1)

    def test_duplicate_tick_does_not_spawn(self):
        self.repo.value['phase'] = 'SPAWN_INTENT'
        self.engine.tick()
        self.assertEqual(self.repo.prepared, 0)

    def test_control_file_tracks_committed_terminal_and_cannot_reenable(self):
        self.repo.closed.update(i['code'] for i in self.cfg['queue'])
        self.engine.tick()
        control=Path(self.tmp.name)/'control.json'
        self.assertFalse(json.loads(control.read_text())['image_execution_enabled'])
        state=self.repo.value.copy();state['phase']='IDLE';state['image_execution_enabled']=True
        self.engine.write_control(state)
        self.assertFalse(json.loads(control.read_text())['image_execution_enabled'])

    def test_terminal_requires_images_then_disables_both(self):
        self.repo.closed.update(i['code'] for i in self.cfg['queue'])
        with patch.object(self.repo, 'checked_blob', return_value=b'{"complete":false}'):
            with self.assertRaises(s.Blocked):
                self.engine.tick()
        state = self.engine.tick()
        self.assertEqual(state['phase'], 'STOPPED')
        self.assertFalse(state['campaign_execution_enabled'])
        self.assertFalse(state['image_execution_enabled'])
        self.assertEqual(len(state['closed']), 77)
        self.assertEqual(self.repo.prepared, 0)

    def test_closure_requires_postpublication_not_reports(self):
        repo = s.Repository(self.tmp.name)
        report_only = {'schema_version': 1, 'code': 'I63', 'owner': 'Codex', 'complete': True,
                       'blocking_reserves': 0, 'final_files': {'chapters/I63/a.html': '0' * 64},
                       'reports': {'MED': {}, 'LANG': {}}}
        repo.main = 'a' * 40
        with patch.object(repo, 'json', return_value=report_only), patch.object(repo, 'checked_blob', return_value=b'{}'):
            with self.assertRaises((s.Blocked, KeyError)):
                repo.closure(self.cfg['queue'][0])

    def test_external_handoff_is_durable_and_never_dispatches_ia_itself(self):
        self.cfg['worker_backend']='native_handoff'
        with patch.object(self.engine,'worker') as worker:
            state=self.engine.tick()
            self.assertEqual(state['phase'],'NATIVE_REQUESTED')
            self.assertEqual(state['handoff']['dispatch_status'],'pending_native_attach')
            self.engine.tick()
            self.assertEqual(self.repo.prepared,1)
            worker.assert_not_called()

    def test_native_nonce_and_completion_require_real_seven_closures(self):
        self.cfg['worker_backend']='native_handoff'
        state=self.engine.tick()
        nonce=state['request_id']
        with self.assertRaises(s.Blocked):
            self.engine.native('attach-native','wrong','agent-1')
        self.engine.native('attach-native',nonce,'agent-1')
        with self.assertRaises(s.Blocked):
            self.engine.native('attach-native',nonce,'agent-2')
        with self.assertRaises(s.Blocked):
            self.engine.native('complete-native',nonce,'agent-1')
        self.repo.closed.update(s.FIRST)
        with self.assertRaises(s.Blocked):
            self.engine.native('complete-native',nonce,'agent-2')
        result=self.engine.native('complete-native',nonce,'agent-1')
        self.assertEqual(result['phase'],'IDLE')
        self.assertEqual(result['closed'],s.FIRST)

    def test_native_rejects_changed_config(self):
        self.cfg['worker_backend']='native_handoff'
        state=self.engine.tick()
        self.cfg['queue'][10]['title']='changed'
        with self.assertRaises(s.Blocked):
            self.engine.native('attach-native',state['request_id'],'agent-1')

    def test_same_thread_resume_requires_explicit_exact_remaining_receipt(self):
        state={'batch':0,'resume_count':0}
        record={'returncode':0,'thread_id':'known-thread'}
        directory=Path(self.tmp.name)
        path=directory/'docs/collaboration/ssp-v2/execution/COORD-0/continuation.json'
        path.parent.mkdir(parents=True)
        receipt={'schema_version':1,'status':'resumable','thread_id':'known-thread','coordinator_mission':'COORD-0',
                 'batch':0,'turn_complete':True,'resume_number':1,'remaining_codes':s.FIRST,'reason':'remaining integration'}
        path.write_text(json.dumps(receipt))
        self.assertIsNotNone(self.engine.continuation(state,directory,record))
        state['resume_count']=3
        self.assertIsNone(self.engine.continuation(state,directory,record))
        state['resume_count']=0
        record['returncode']=1
        self.assertIsNone(self.engine.continuation(state,directory,record))
        record['returncode']=0
        receipt['thread_id']='different-thread'
        path.write_text(json.dumps(receipt))
        self.assertIsNone(self.engine.continuation(state,directory,record))


class ClosureProofTests(unittest.TestCase):
    def proof(self):
        files = {f'chapters/I63/I63_{p}.html': '0' * 64 for p in ('a','b','c','d','pop1','pop2')}
        files['glossary/i63.py'] = '0' * 64
        prefix = 'docs/collaboration/ssp-v2/execution/I63-INTEGRATE/'
        probe = {'url': s.PAGES_ORIGIN + 'MEDINA.html', 'sha256': s.hashlib.sha256(b'public').hexdigest()}
        proof = {'schema_version': 1, 'code': 'I63', 'owner': 'Codex', 'complete': True,
                 'medical_human_validation': False, 'blocking_reserves': 0, 'final_files': files,
                 'reports': {r: {'mission': 'I63-' + r, 'path': prefix + r + '.json', 'sha256': '0' * 64, 'final_files': files}
                             for r in ('MED', 'LANG')},
                 'figure_validation': {'status': 'passed', 'path': prefix + 'figures.json', 'sha256': '0' * 64, 'final_files': files},
                 'alpha_receipt': {'path': 'organisation/alpha-publications/Codex/I63/0001.json', 'sha256': '0' * 64},
                 'requirement_evidence':{'semiology':{'path':prefix+'semio.json','sha256':'0'*64}},
                 'integration': {'pr': 1, 'merge_sha': 'a' * 40},
                 'publication': {'main_sha': 'b' * 40, 'manifest_path': 'publication.json', 'manifest_sha256': '0' * 64,
                                 'probes': [probe]}}
        manifest = {'main_sha': 'b' * 40, 'final_files': files, 'probes': [probe]}
        alpha = {'schema_version': 1, 'actor': 'Codex', 'code': 'I63', 'phase': 'completed',
                 'mission': 'I63-INTEGRATE', 'medical_human_validation': False, 'source_commit': 'b'*40,
                 'files': {p: {'sha256': h,'previous_sha256':h} for p,h in files.items()},
                 'audits': {r: {'path': proof['reports'][r]['path'], 'sha256': '0'*64} for r in ('MED','LANG')}}
        alpha['audits']['SEMIO']=proof['requirement_evidence']['semiology']
        blobs = {proof['alpha_receipt']['path']: alpha, 'publication.json': manifest,
                 prefix+'figures.json': {'actor': 'Codex','code':'I63','status':'passed','complete':True,'pending':[],
                    'reviewed_files_sha256':files,'medical_human_validation':False,'evidence':['actual figure provenance and visual review']}}
        for role in ('MED','LANG'):
            blobs[prefix+role+'.json'] = {'actor':'Codex','code':'I63','kind':role,'status':'closed',
                 'medical_human_validation':False,'reviewed_files_sha256':files,'source_files_sha256':files,'unresolved_blockers':[],
                 'findings':[], 'requirements_reviewed':{'fundamental_analytical_semiology':True}, 'evidence':['actual source review']}
        return proof, manifest, blobs

    def test_full_proof_only_closes_when_public_probe_matches(self):
        proof, manifest, blobs = self.proof()
        repo = s.Repository('/tmp')
        repo.main = 'c' * 40
        class Response:
            status = 200
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def geturl(self): return s.PAGES_ORIGIN + 'MEDINA.html'
            def read(self, size): return b'public'
        mission = {'id':'I63-INTEGRATE','codes':['I63'], 'paths':['organisation/alpha-publications/Codex/I63','docs/collaboration/ssp-v2/execution/I63-INTEGRATE']}
        with patch.object(repo, 'json', return_value=proof), patch.object(repo, 'mission',return_value=mission), \
             patch.object(repo, 'checked_blob', side_effect=lambda rev,e: s.canonical(blobs.get(e['path'],{}))), \
             patch.object(repo, 'read', side_effect=lambda rev,p: s.canonical(blobs.get(p,{}))), \
             patch.object(repo, 'git', return_value=b''), patch.object(repo, 'merged_pr'), patch.object(repo, 'pages_run'), patch.object(repo, 'semiology'), \
             patch.object(s.urllib.request, 'urlopen', return_value=Response()):
            self.assertEqual(repo.closure(configuration()['queue'][0]), proof)
            probe = proof['publication']['probes'][0]
            old = probe['sha256']
            probe['sha256'] = 'f' * 64
            with self.assertRaises(s.Blocked):
                repo.closure(configuration()['queue'][0])
            probe['sha256'] = old
            blobs[proof['alpha_receipt']['path']]['phase'] = 'provisional'
            with self.assertRaises(s.Blocked):
                repo.closure(configuration()['queue'][0])
            blobs[proof['alpha_receipt']['path']]['phase'] = 'completed'
            blobs[proof['reports']['MED']['path']]['reviewed_files_sha256'] = {'unrelated': '0'*64}
            with self.assertRaises(s.Blocked):
                repo.closure(configuration()['queue'][0])

    def test_missing_core_and_unrelated_sources_rejected(self):
        proof, _, _ = self.proof()
        repo = s.Repository('/tmp')
        repo.main='c'*40
        with patch.object(repo,'json',return_value=proof):
            del proof['final_files']['glossary/i63.py']
            with self.assertRaises(s.Blocked): repo.closure(configuration()['queue'][0])
            proof['final_files']['glossary/i63.py']='0'*64
            proof['final_files']['chapters/E10/E10_a.html']='0'*64
            with self.assertRaises(s.Blocked): repo.closure(configuration()['queue'][0])

    def test_actual_semiology_panel_clinical_marker_and_sources_required(self):
        repo=s.Repository('/tmp');repo.main='a'*40
        item=configuration()['queue'][0]
        files={'source':'hash'}
        prefix='docs/collaboration/ssp-v2/execution/I63-INTEGRATE/'
        proof={'requirement_evidence':{'semiology':{'path':prefix+'semiology.json','sha256':'0'*64}}}
        audit={'kind':'SEMIO','requirement':'fundamental_analytical_semiology','actor':'Codex','code':'I63','status':'closed','unresolved_blockers':[],
               'reviewed_files_sha256':files,'tab_id':'i63-s-semio','source_path':'chapters/I63/I63_c.html',
               'evidence':['examined cited sources'],'findings':[],'source_files_sha256':{},'medical_human_validation':False}
        sections=''.join('<section class="ilot" data-semiology="'+name+'"><h3>Section</h3>Clinical causal discussion</section>' for name in
                         ('normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits'))
        c=('<div id="pS">'+''.join('<button data-s="old%d">Existing</button>'%i for i in range(5))+
           '<button role="tab" id="i63-tab-semio" aria-controls="i63-s-semio" data-s="i63-s-semio">Sémiologie fondamentale et analytique</button><div class="sci" id="i63-s-semio" aria-labelledby="i63-tab-semio">'+
           sections+'<section class="ilot" data-semiology="sources"><h3>Sources</h3><a href="https://source.example/guideline">Guideline evidence</a></section></div></div>')
        a='<div id="pA"><section data-semiology-clinical="I63">Actual clinical signs and examination</section></div>'
        with patch.object(repo,'checked_blob',return_value=s.canonical(audit)), \
             patch.object(repo,'read',side_effect=lambda rev,p:c.encode() if p.endswith('_c.html') else a.encode()):
            repo.semiology(item,proof,files,prefix)
            c=c.replace('data-semiology="mechanisms"','data-semiology="wrong"')
            with self.assertRaises(s.Blocked):repo.semiology(item,proof,files,prefix)

    def test_pages_run_requires_trusted_workflow_exact_sha_and_success(self):
        repo=s.Repository('/tmp')
        pub={'run_id':1,'main_sha':'b'*40}
        value={'workflow_id':s.PAGES_WORKFLOW,'path':'.github/workflows/pages.yml',
            'repository':{'full_name':s.PAGES_REPOSITORY},'head_repository':{'full_name':s.PAGES_REPOSITORY},
            'head_sha':'b'*40,'head_branch':'main','status':'completed','conclusion':'success'}
        with patch.object(s,'command',side_effect=lambda *args:s.canonical(value)):
            repo.pages_run(pub)
            value['head_sha']='a'*40
            with self.assertRaises(s.Blocked):repo.pages_run(pub)
            value['head_sha']='b'*40
            value['workflow_id']=1
            with self.assertRaises(s.Blocked):repo.pages_run(pub)
            value['workflow_id']=s.PAGES_WORKFLOW
            value['conclusion']='failure'
            with self.assertRaises(s.Blocked):repo.pages_run(pub)

    def test_pr_must_be_merged_and_ci_successful(self):
        repo = s.Repository('/tmp')
        repo.main = 'c' * 40
        payload = {'state': 'MERGED', 'baseRefName': 'main', 'mergeCommit': {'oid': 'a' * 40},
                   'statusCheckRollup': [{'status': 'COMPLETED', 'conclusion': 'FAILURE'}]}
        with patch.object(s, 'command', return_value=s.canonical(payload)), patch.object(repo, 'git'):
            with self.assertRaises(s.Blocked):
                repo.merged_pr({'pr': 1, 'merge_sha': 'a' * 40})
            payload['statusCheckRollup'][0]['conclusion'] = 'SUCCESS'
        with patch.object(s, 'command', return_value=s.canonical(payload)), patch.object(repo, 'git'):
            repo.merged_pr({'pr': 1, 'merge_sha': 'a' * 40})


class GitCASTests(unittest.TestCase):
    def test_two_independent_clones_racing_cannot_both_publish(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.run(['git', *map(str, args)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            git('init', '--bare', root / 'remote')
            git('clone', root / 'remote', root / 'one')
            git('clone', root / 'remote', root / 'two')
            one, two = s.Repository(root / 'one'), s.Repository(root / 'two')
            first = {'closed': [], 'phase': 'IDLE'}
            winner = one.cas(None, first)
            with self.assertRaises(s.Blocked):
                two.cas(None, {'closed': ['I63'], 'phase': 'RUNNING'})
            revision, state = two.state()
            self.assertEqual(revision, winner)
            old = revision
            one.cas(old, {'closed': [], 'phase': 'SPAWN_INTENT'})
            with self.assertRaises(s.Blocked):
                two.cas(old, {'closed': [], 'phase': 'SPAWN_INTENT'})


if __name__ == '__main__':
    unittest.main()
