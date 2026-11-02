import importlib.util
from pathlib import Path
import re
import unittest
from unittest.mock import Mock

spec=importlib.util.spec_from_file_location('registry_guard_under_test',Path(__file__).resolve().parents[1]/'registry_guard.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class IsolatedRegistryFetch(unittest.TestCase):
    def fake(self):
        guard=Mock();guard.re=re
        def require(ok,message):
            if not ok:raise ValueError(message)
        guard.require=require
        guard.commit=lambda root,sha:sha
        guard.git.side_effect=lambda root,*a,**kw: (b'a'*40+b'\n') if a[0]=='rev-parse' else b''
        return guard

    def test_distinct_refs_and_no_fetch_head(self):
        g=self.fake()
        self.assertEqual(module.isolated_fetch(g,'/task','origin',{'registry_ref':'refs/heads/medina/session-registry'}),'a'*40)
        module.isolated_fetch(g,'/task','origin',{'registry_ref':'refs/heads/medina/session-registry'})
        calls=[c.args for c in g.git.call_args_list]
        fetches=[c for c in calls if c[1]=='fetch']
        self.assertEqual(len(fetches),2)
        self.assertNotEqual(fetches[0][-1],fetches[1][-1])
        self.assertTrue(all('--no-write-fetch-head' in c for c in fetches))
        self.assertFalse(any('FETCH_HEAD' in part for c in calls for part in c))
        deletes=[c for c in calls if c[1]=='update-ref']
        self.assertEqual([c[-1] for c in deletes],[c[-1].split(':')[1] for c in fetches])

    def test_failure_never_reuses_stale_head(self):
        g=self.fake()
        def fail(root,*args,**kwargs):
            if args[0]=='fetch':raise RuntimeError('network failure')
            return b''
        g.git.side_effect=fail
        with self.assertRaisesRegex(RuntimeError,'network failure'):
            module.isolated_fetch(g,'/task','origin',{'registry_ref':'refs/heads/medina/session-registry'})
        self.assertEqual([c.args[1] for c in g.git.call_args_list],['fetch','update-ref'])

    def test_remote_validation_precedes_fetch(self):
        g=self.fake()
        with self.assertRaises(ValueError):module.isolated_fetch(g,'/task','--upload-pack=bad',{'registry_ref':'refs/heads/medina/session-registry'})
        g.git.assert_not_called()

if __name__=='__main__':unittest.main()
