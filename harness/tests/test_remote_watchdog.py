"""Remote monitoring never certifies stale authors and has an explicit stop."""
import copy
import datetime as dt
import importlib.util
import sys
from pathlib import Path
import tempfile
import unittest
from unittest import mock

HERE=Path(__file__).resolve().parents[1]
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
mh=module('mh_remote_test',HERE/'medina_harness.py')
with mock.patch.dict(sys.modules,{'medina_harness':mh}):
    remote=module('remote_watchdog_test',HERE/'remote_watchdog.py')
    publisher=module('publisher_test',HERE/'watch_publish.py')

class WatchdogCase(unittest.TestCase):
    def setUp(self):
        self.now=dt.datetime(2026,11,2,7,tzinfo=dt.timezone.utc)
        self.data={'generated_at':self.now.isoformat(),'tests':{'ok':True},'gate':{'allowed':True},
                   'agents':[{'id':str(i),'activity_at':self.now.isoformat()} for i in range(4)]}

    def test_observation_does_not_mutate_activity(self):
        before=copy.deepcopy(self.data)
        self.assertTrue(remote.evaluate(self.data,self.now)['healthy'])
        self.assertEqual(self.data,before)

    def test_fresh_observer_cannot_refresh_old_source(self):
        self.data['generated_at']=(self.now-dt.timedelta(seconds=1201)).isoformat()
        self.assertFalse(remote.evaluate(self.data,self.now)['healthy'])

    def test_future_author_activity_is_not_healthy(self):
        self.data['agents'][0]['activity_at']=(self.now+dt.timedelta(seconds=1)).isoformat()
        result=remote.evaluate(self.data,self.now)
        self.assertFalse(result['healthy']);self.assertEqual(result['agents_without_recent_activity'],['0'])

    def test_incomplete_roster_and_closed_gate_report_failure(self):
        self.data['agents'].pop();self.data['gate']['allowed']=False
        self.assertGreaterEqual(len(remote.evaluate(self.data,self.now)['problems']),2)

    def test_disabled_control_never_dispatches(self):
        with mock.patch.object(remote,'file_json',return_value=({'enabled':False},'sha')),mock.patch.object(remote,'api') as call:
            remote.handoff(bootstrap=True)
            call.assert_not_called()

    def test_successor_is_same_review_branch_and_never_bootstrap(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(remote,'HOME',Path(d)),mock.patch.object(remote,'file_json',return_value=({'enabled':True},'sha')),mock.patch.object(remote,'api',return_value={'http_status':204}) as call:
            self.assertEqual(remote.handoff(bootstrap=True),0)
            payload=call.call_args.args[1]
            self.assertEqual(payload['ref'],'codex/harness-20261102')
            self.assertEqual(payload['inputs'],{'watchdog':'true','bootstrap':'false'})

    def test_api_rejects_another_repository_before_network(self):
        with self.assertRaises(ValueError):remote.api('/repos/other/project/contents/file')

    def test_closed_gate_still_publishes_alert_but_not_untested_code(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'root';target=Path(d)/'publisher';home=root/'harness';runtime=home/'runtime';runtime.mkdir(parents=True)
            (home/'status.json').write_text('{"gate":{"allowed":false}}')
            (home/'medina_harness.py').write_text('unverified candidate')
            h=mock.Mock(home=home,runtime=runtime);h.readiness.return_value={'allowed':False,'problems':['tests failed']}
            with mock.patch.object(publisher,'Harness',return_value=h),mock.patch.object(publisher.subprocess,'run',return_value=mock.Mock(returncode=0)),mock.patch.object(publisher.subprocess,'check_output',return_value=publisher.BRANCH+'\n'):
                result=publisher.run(root,target)
            self.assertTrue(result['published']);self.assertFalse(result['production_allowed'])
            self.assertTrue((target/'harness/status.json').exists())
            self.assertFalse((target/'harness/medina_harness.py').exists())

if __name__=='__main__':unittest.main()
