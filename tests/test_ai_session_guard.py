"""Real Git transactions, scope fences and trusted-base regression checks."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'tools' / 'ai_session_guard.py'
spec = importlib.util.spec_from_file_location('ai_session_guard', SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.root = self.home / 'work'
        self.remote = self.home / 'remote.git'
        self.run_git(self.home, 'init', '--bare', str(self.remote))
        self.run_git(self.home, 'init', '-b', 'main', str(self.root))
        self.run_git(self.root, 'config', 'user.email', 'test@medina.invalid')
        self.run_git(self.root, 'config', 'user.name', 'Test')
        self.write('chapters/I63/I63_a.html', 'original neuro')
        self.write('chapters/N18/N18_a.html', 'original nephro')
        self.write('chapters/I50/I50_a.html', 'older system')
        self.write('chapters.json', json.dumps([{'code': 'I63', 'integrated': True}, {'code': 'I50', 'title': 'keep'}]))
        self.initial = self.commit('initial')
        cfg = dict(schema_version=1, enabled=True, code_systems={'I63': 'S08', 'N18': 'S04'},
                   shared_paths=['chapters.json'], registry_ref='refs/heads/medina/session-registry')
        self.write(guard.CONFIG, json.dumps(cfg))
        self.missions = {}
        for ident, code, role, paths in (
            ('neuro', 'I63', 'author', ['chapters/I63']),
            ('nephro', 'N18', 'author', ['chapters/N18']),
            ('integrator', 'I63', 'integrator', ['chapters/I63', 'chapters.json', guard.CONFIG, '.medina/missions']),
            ('child', 'I63', 'author', ['chapters/I63/I63_a.html']),
            ('audit', 'I63', 'audit', [guard.OUTPUTS + 'audit']),
            ('bootstrap', 'I63', 'integrator', [guard.CONFIG, '.medina/missions']),
        ):
            value = dict(schema_version=1, id=ident, state='active', actor='Any-new-AI',
                         conversation='conv-' + ident, owner='Codex', assigned_by='Claude',
                         branch='ai/' + ident, role=role, code=code, base_sha=self.initial,
                         generation=1, paths=paths)
            self.missions[ident] = value
            self.write(guard.MISSIONS + ident + '.json', json.dumps(value))
        self.base = self.commit('approve configuration and missions')
        self.run_git(self.root, 'checkout', '-b', 'medina/session-registry')
        self.write(guard.REGISTRY, json.dumps(dict(schema_version=1, reservations=[])))
        self.seed = self.commit('initialize central registry')
        self.run_git(self.root, 'checkout', 'main')
        self.run_git(self.root, 'remote', 'add', 'origin', str(self.remote))
        self.run_git(self.root, 'push', 'origin', 'main', 'medina/session-registry')

    def run_git(self, root, *args):
        result = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value)

    def commit(self, message):
        self.run_git(self.root, 'add', '.')
        self.run_git(self.root, 'commit', '-m', message)
        return self.run_git(self.root, 'rev-parse', 'HEAD')

    def candidate(self, files):
        for name, value in files.items():
            self.write(name, value)
        return self.commit('candidate')

    def check(self, head, mission='neuro', **kwargs):
        return guard.check(self.root, self.base, head, 'ai/' + mission, **kwargs)

    def test_assigned_unknown_ai_can_start_and_change_own_source(self):
        revision = guard.acquire(self.root, self.base, 'neuro')
        workspace = self.home / 'neuro-worktree'
        self.run_git(self.root, 'worktree', 'add', '-b', 'ai/neuro', str(workspace), self.base)
        report = guard.start(self.root, self.base, 'neuro', 'Any-new-AI', 'conv-neuro', registry_sha=revision, worktree=workspace)
        self.assertEqual(report['mission']['assigned_by'], 'Claude')
        head = self.candidate({'chapters/I63/I63_a.html': 'updated'})
        self.assertEqual(self.check(head)['guard'], 'passed')
        self.assertEqual(guard.check(self.root, self.base, head, 'main', integrated=True)['mission'], 'neuro')
        with self.assertRaisesRegex(guard.GuardError, 'Declared session'):
            guard.start(self.root, self.base, 'neuro', 'Other', 'conv-neuro', registry_sha=revision)

    def test_documentation_only_needs_no_mission_or_registry(self):
        head = self.candidate({'docs/planning.md': 'plan'})
        self.assertEqual(guard.check(self.root, self.base, head, 'unassigned')['guard'], 'not-applicable')

    def test_older_system_alone_is_not_blocked(self):
        head = self.candidate({'chapters/I50/I50_a.html': 'older update', 'chapters.json': json.dumps([
            {'code': 'I63', 'integrated': True}, {'code': 'I50', 'title': 'older update'}])})
        self.assertEqual(guard.check(self.root, self.base, head, 'legacy')['guard'], 'not-applicable')

    def test_mixed_older_system_change_is_outside_assigned_scope(self):
        guard.acquire(self.root, self.base, 'neuro')
        head = self.candidate({'chapters/I63/I63_a.html': 'new', 'chapters/I50/I50_a.html': 'unrelated'})
        with self.assertRaisesRegex(guard.GuardError, 'outside mission'):
            self.check(head)

    def test_no_approval_in_candidate_and_no_self_modification(self):
        unknown = dict(self.missions['neuro'], id='new', branch='ai/new')
        head = self.candidate({'chapters/I63/I63_a.html': 'new', guard.MISSIONS + 'new.json': json.dumps(unknown)})
        with self.assertRaisesRegex(guard.GuardError, 'preapproved'):
            self.check(head, 'new')
        with self.assertRaisesRegex(guard.GuardError, 'own approval'):
            head = self.candidate({guard.MISSIONS + 'neuro.json': json.dumps(dict(self.missions['neuro'], generation=2))})
            self.check(head)

    def test_config_cannot_disable_its_own_source_check(self):
        raw = json.loads((self.root / guard.CONFIG).read_text())
        raw['enabled'] = False
        head = self.candidate({guard.CONFIG: json.dumps(raw), 'chapters/I63/I63_a.html': 'unapproved'})
        with self.assertRaises(guard.GuardError):
            self.check(head)
        with self.assertRaisesRegex(guard.GuardError, 'Separate governance'):
            self.check(head, 'integrator')

    def test_shared_catalogue_requires_integrator_and_preserves_other_rows(self):
        guard.acquire(self.root, self.base, 'integrator')
        head = self.candidate({'chapters.json': json.dumps([
            {'code': 'I63', 'integrated': True, 'title': 'new'}, {'code': 'I50', 'title': 'keep'}])})
        self.assertEqual(self.check(head, 'integrator')['guard'], 'passed')
        head = self.candidate({'chapters.json': json.dumps([
            {'code': 'I63', 'title': 'new'}, {'code': 'I50', 'title': 'destroyed'}])})
        with self.assertRaisesRegex(guard.GuardError, 'unrelated course'):
            self.check(head, 'integrator')

    def test_gov_changes_need_preapproved_integrator(self):
        head = self.candidate({guard.MISSIONS + 'nephro.json': json.dumps(dict(self.missions['nephro'], generation=2))})
        with self.assertRaisesRegex(guard.GuardError, 'integrator'):
            self.check(head)
        guard.acquire(self.root, self.base, 'integrator')
        self.assertEqual(self.check(head, 'integrator')['guard'], 'passed')

    def test_release_fences_stale_generation_and_preserves_history(self):
        first = guard.acquire(self.root, self.base, 'neuro')
        head = self.candidate({'chapters/I63/I63_a.html': 'updated'})
        with self.assertRaisesRegex(guard.GuardError, 'Registry advanced'):
            guard.release(self.root, self.base, 'neuro', 1, 'conserved', expected_registry=self.seed)
        last = guard.release(self.root, self.base, 'neuro', 1, 'work preserved', expected_registry=first)
        self.assertEqual(guard.registry(self.root, last)['reservations'][0]['release_reason'], 'work preserved')
        with self.assertRaisesRegex(guard.GuardError, 'generation'):
            self.check(head)
        with self.assertRaisesRegex(guard.GuardError, 'Stale'):
            guard.acquire(self.root, self.base, 'neuro')

    def test_parent_child_collision_and_disjoint_parallel_courses(self):
        self.assertTrue(guard.overlaps('chapters/I63', 'chapters/I63/I63_a.html'))
        self.assertFalse(guard.overlaps('chapters/I63', 'chapters/I630'))
        guard.acquire(self.root, self.base, 'neuro')
        with self.assertRaises(guard.GuardError):
            guard.acquire(self.root, self.base, 'child')
        last = guard.acquire(self.root, self.base, 'nephro')
        self.assertEqual(len([r for r in guard.registry(self.root, last)['reservations'] if r['state'] == 'active']), 2)

    def test_audit_reserves_only_own_outputs_and_cannot_write_sources(self):
        guard.acquire(self.root, self.base, 'neuro')
        guard.acquire(self.root, self.base, 'audit')
        head = self.candidate({guard.OUTPUTS + 'audit/report.md': 'actual audit report'})
        self.assertEqual(self.check(head, 'audit')['guard'], 'passed')
        head = self.candidate({guard.OUTPUTS + 'neuro/report.md': 'other mission output'})
        with self.assertRaisesRegex(guard.GuardError, 'outside mission'):
            self.check(head, 'audit')
        # Reading the same course is compatible, writing the same output is not.
        left = dict(role='audit', codes=['I63'], paths=['docs/output'])
        right = dict(role='audit', codes=['I63'], paths=['docs/output/report.md'])
        self.assertTrue(guard.collides(left, right))
        right['role'] = 'author'
        self.assertTrue(guard.collides(left, right))
        bad = dict(self.missions['audit'], paths=['chapters/I63'])
        self.write(guard.MISSIONS + 'audit.json', json.dumps(bad))
        bad_base = self.commit('invalid audit assignment')
        with self.assertRaisesRegex(guard.GuardError, 'outside owned course'):
            guard.manifest(self.root, bad_base, 'audit', guard.config(self.root, bad_base))

    def test_execution_reports_require_assignment_but_planning_docs_do_not(self):
        head = self.candidate({guard.OUTPUTS + 'unknown/report.md': 'unassigned report'})
        with self.assertRaisesRegex(guard.GuardError, 'preapproved'):
            self.check(head, 'unknown')

    def test_symlink_source_is_rejected(self):
        guard.acquire(self.root, self.base, 'neuro')
        target = self.root / 'chapters/I63/I63_a.html'
        target.unlink()
        target.symlink_to('../../I50/I50_a.html')
        head = self.commit('symlink candidate')
        with self.assertRaisesRegex(guard.GuardError, 'Symlink'):
            self.check(head)

    def test_parent_symlinks_cannot_bypass_untracked_protected_children(self):
        # There is no tracked protected glossary child: replacing the parent
        # must still activate the guard rather than passing as an older system.
        glossary = self.root / 'glossary'
        glossary.symlink_to('/tmp/outside-glossary')
        head = self.commit('replace glossary parent')
        with self.assertRaisesRegex(guard.GuardError, 'preapproved'):
            self.check(head, 'unknown')
        self.run_git(self.root, 'reset', '--hard', self.base)
        output = self.root / guard.OUTPUTS.rstrip('/')
        output.parent.mkdir(parents=True, exist_ok=True)
        output.symlink_to('/tmp/outside-execution')
        head = self.commit('replace execution parent')
        with self.assertRaisesRegex(guard.GuardError, 'preapproved'):
            self.check(head, 'unknown')
        self.assertFalse(guard.is_doc(guard.OUTPUTS.rstrip('/')))
        self.assertFalse(guard.is_doc('docs/collaboration/ssp-v2'))
        self.assertTrue(guard.is_doc('docs/planning.md'))

    def test_assignment_rejects_symlink_parent_already_in_trusted_base(self):
        (self.root / 'glossary').symlink_to('/tmp/outside-glossary')
        bad = dict(self.missions['neuro'], paths=['glossary/i63.py'])
        self.write(guard.MISSIONS + 'neuro.json', json.dumps(bad))
        snapshot = self.commit('invalid assignment under symlink parent')
        with self.assertRaisesRegex(guard.GuardError, 'Symlink'):
            guard.manifest(self.root, snapshot, 'neuro', guard.config(self.root, snapshot))

    def test_start_requires_clean_worktree_exact_base_and_assigned_branch(self):
        revision = guard.acquire(self.root, self.base, 'neuro')
        with self.assertRaisesRegex(guard.GuardError, 'mission branch'):
            guard.start(self.root, self.base, 'neuro', 'Any-new-AI', 'conv-neuro', registry_sha=revision)
        workspace = self.home / 'fresh-worktree'
        self.run_git(self.root, 'worktree', 'add', '-b', 'ai/neuro', str(workspace), self.base)
        (workspace / 'untracked.txt').write_text('unrecorded start')
        with self.assertRaisesRegex(guard.GuardError, 'start clean'):
            guard.start(self.root, self.base, 'neuro', 'Any-new-AI', 'conv-neuro', registry_sha=revision, worktree=workspace)
        (workspace / 'untracked.txt').unlink()
        self.run_git(workspace, 'commit', '--allow-empty', '-m', 'diverged before start')
        with self.assertRaisesRegex(guard.GuardError, 'exact trusted base'):
            guard.start(self.root, self.base, 'neuro', 'Any-new-AI', 'conv-neuro', registry_sha=revision, worktree=workspace)

    def test_governance_bootstrap_can_approve_relay_and_renew_source_generation(self):
        # Governance-only reservations do not lock I63 merely because it is
        # their accounting code, so sources and governance can proceed together.
        guard.acquire(self.root, self.base, 'bootstrap')
        guard.acquire(self.root, self.base, 'neuro')
        relay = dict(self.missions['bootstrap'], id='relay', branch='ai/relay', conversation='conv-relay', generation=1)
        approved_head = self.candidate({guard.MISSIONS + 'relay.json': json.dumps(relay)})
        self.assertEqual(self.check(approved_head, 'bootstrap')['guard'], 'passed')
        # Simulate the reviewed approval being merged before relay acquisition.
        self.base = approved_head
        with self.assertRaisesRegex(guard.GuardError, 'collision'):
            guard.acquire(self.root, self.base, 'relay')
        guard.release(self.root, self.base, 'bootstrap', 1, 'relay approved; bootstrap work preserved')
        guard.acquire(self.root, self.base, 'relay')
        guard.release(self.root, self.base, 'neuro', 1, 'source commit preserved before generation renewal')
        renewed = dict(self.missions['neuro'], generation=2)
        retired = dict(self.missions['bootstrap'], state='closed')
        renewed_head = self.candidate({guard.MISSIONS + 'neuro.json': json.dumps(renewed),
                                       guard.MISSIONS + 'bootstrap.json': json.dumps(retired)})
        self.assertEqual(self.check(renewed_head, 'relay')['guard'], 'passed')
        self.base = renewed_head
        current = guard.acquire(self.root, self.base, 'neuro')
        reservations = guard.registry(self.root, current)['reservations']
        self.assertEqual([r['generation'] for r in reservations if r['id'] == 'neuro' and r['state'] == 'active'], [2])
        self.assertEqual(len([r for r in reservations if r['state'] == 'released']), 2)

    def test_simultaneous_separate_processes_only_one_remote_push_wins(self):
        # Both acquire from the same exact remote parent; barrier is before push.
        clone = self.home / 'clone'
        self.run_git(self.home, 'clone', str(self.remote), str(clone))
        barrier = self.home / 'barrier'
        barrier.mkdir()
        worker = self.home / 'worker.py'
        worker.write_text('''import importlib.util, pathlib, sys, time
s=importlib.util.spec_from_file_location('guard', sys.argv[1]); g=importlib.util.module_from_spec(s); s.loader.exec_module(g)
original=g.transact
barrier=pathlib.Path(sys.argv[5]); ident=sys.argv[4]
def synchronized(*args, **kwargs):
    (barrier / ident).write_text('ready')
    deadline=time.monotonic()+15
    while len(list(barrier.iterdir())) != 2:
        if time.monotonic()>deadline: raise RuntimeError('barrier timeout')
        time.sleep(.01)
    return original(*args, **kwargs)
g.transact=synchronized
try:
    print(g.acquire(sys.argv[2], sys.argv[3], ident))
except g.GuardError as e:
    print(str(e), file=sys.stderr); sys.exit(1)
''')
        processes = [subprocess.Popen([sys.executable, str(worker), str(SCRIPT), str(root), self.base, ident, str(barrier)],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                     for root, ident in ((self.root, 'neuro'), (clone, 'child'))]
        results = [(p.communicate(timeout=25), p.returncode) for p in processes]
        self.assertEqual(sorted(code for _, code in results), [0, 1], results)
        revision = guard.fetch_registry(self.root, 'origin', guard.config(self.root, self.base))
        self.assertEqual(len(guard.registry(self.root, revision)['reservations']), 1)
        loser = next(output[1] for output, code in results if code)
        self.assertTrue('rejected' in loser or 'cannot lock ref' in loser, loser)
        self.assertEqual(self.run_git(self.root, 'rev-parse', 'HEAD'), self.base)


if __name__ == '__main__':
    unittest.main()
