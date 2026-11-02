"""Regression: an author transition must not freeze an outdated lesson preview."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import sys

HOME=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HOME))
SPEC=importlib.util.spec_from_file_location('deliverables_target',HOME/'make_deliverables.py')
index=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(index)

class DeliverablesCase(unittest.TestCase):
    def test_completed_preview_is_refreshed_after_author_moves(self):
        with tempfile.TemporaryDirectory() as td:
            home=Path(td);(home/'runtime').mkdir()
            old=home/'old';new=home/'new';old.mkdir();new.mkdir()
            rel='docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-G02-INTEGRATE/G02-apercu-autonome.html'
            preview=old/rel;preview.parent.mkdir(parents=True);preview.write_text('actual final bytes')
            (home/'runtime/state.json').write_text(json.dumps({'completed_lessons':[{'code':'G02','agent':'neuro','branch':'review-g02','worktree':str(old)}],'agents':{'neuro':{'lesson':'G05','branch':'review-g05','worktree':str(new)}}}))
            (home/'deliverables.json').write_text(json.dumps({'lessons':[{'code':'G02','sha256':'stale','exists':True}]}))
            with mock.patch.object(index,'HERE',home),mock.patch.object(index.subprocess,'check_output',return_value='d'*40+'\n'),contextlib.redirect_stdout(io.StringIO()):
                index.main()
            lessons={x['code']:x for x in json.loads((home/'deliverables.json').read_text())['lessons']}
            self.assertEqual(set(lessons),{'G02','G05'})
            self.assertEqual(lessons['G02']['sha256'],index.hashlib.sha256(preview.read_bytes()).hexdigest())
            self.assertEqual(lessons['G02']['head_observed'],'d'*40)
            self.assertIn('completion',lessons['G02'])
            self.assertFalse(lessons['G05']['exists'])

if __name__=='__main__':unittest.main()
