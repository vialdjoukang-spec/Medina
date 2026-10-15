"""Contrats locaux de sessions : vrais dépôts Git, worktrees et processus concurrents."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from tools import conversation_workspace as W


SCRIPT = Path(W.__file__).resolve()


class ConversationWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.remote = self.directory / 'remote.git'
        self.repo = self.directory / 'repo'
        subprocess.run(['git', 'init', '--bare', '--initial-branch=main', str(self.remote)],
                       check=True, capture_output=True)
        subprocess.run(['git', 'clone', str(self.remote), str(self.repo)], check=True, capture_output=True)
        W.git(self.repo, 'config', 'user.name', 'Fixture')
        W.git(self.repo, 'config', 'user.email', 'fixture@example.invalid')
        (self.repo / 'README').write_text('base\n')
        for code in ('I63', 'E11'):
            path = self.repo / 'chapters' / code
            path.mkdir(parents=True)
            (path / (code + '_a.html')).write_text('contenu ' + code)
        W.git(self.repo, 'add', '.')
        W.git(self.repo, 'commit', '-m', 'fixture')
        W.git(self.repo, 'push', 'origin', 'main')

    def begin(self, conversation='conv-1', code='I63', actor='Codex', **kwargs):
        return W.begin(self.repo, actor=actor, conversation=conversation, code=code,
                       worktree=self.directory / conversation,
                       files=kwargs.pop('files', ['chapters/' + code]), **kwargs)

    def test_same_ai_two_conversations_independent_worktrees(self):
        before = W.git(self.repo, 'rev-parse', 'HEAD')
        (self.repo / 'README').write_text('travail concurrent conserve\n')
        first = self.begin()
        second = self.begin('conv-2', 'E11')
        self.assertNotEqual(first['branch'], second['branch'])
        self.assertTrue(first['branch'].startswith('codex/conversations/'))
        self.assertEqual(first['base_sha'], second['base_sha'])
        self.assertEqual(W.git(self.repo, 'rev-parse', 'HEAD'), before)
        self.assertEqual(W.git(self.repo, 'branch', '--show-current'), 'main')
        self.assertEqual((self.repo / 'README').read_text(), 'travail concurrent conserve\n')
        self.assertFalse((self.repo / 'organisation').exists())

    def test_begin_fetches_actual_main(self):
        other = self.directory / 'other'
        subprocess.run(['git', 'clone', str(self.remote), str(other)], check=True, capture_output=True)
        W.git(other, 'config', 'user.name', 'Fixture')
        W.git(other, 'config', 'user.email', 'fixture@example.invalid')
        (other / 'README').write_text('nouvelle tete\n')
        W.git(other, 'commit', '-am', 'nouvelle base')
        W.git(other, 'push', 'origin', 'main')
        mission = self.begin()
        self.assertEqual(mission['base_sha'], W.git(other, 'rev-parse', 'HEAD'))
        self.assertNotEqual(mission['base_sha'], W.git(self.repo, 'rev-parse', 'HEAD'))

    def test_overlaps_and_expired_bail_still_refused(self):
        first = self.begin()
        state = W.state_directory(self.repo)
        first['expires_at'] = '2000-01-01T00:00:00+00:00'
        W.save(state, first)
        with self.assertRaisesRegex(W.WorkspaceError, 'Bail'):
            self.begin('conv-2', files=['chapters/I63/I63_a.html'])
        self.assertTrue(W.status(self.repo)[0]['expired'])
        with self.assertRaises(W.WorkspaceError):
            W.close(self.repo, first['id'], abandon=True)
        W.close(self.repo, first['id'], abandon=True, reason='Auteur arrêté explicitement')
        replacement = self.begin('conv-3')
        self.assertEqual(replacement['state'], 'active')
        self.assertTrue(Path(first['worktree']).exists())

    def test_two_real_processes_cannot_claim_same_path(self):
        processes = [subprocess.Popen([sys.executable, str(SCRIPT), '--repo', str(self.repo), 'begin',
                        '--actor', 'Codex', '--conversation', 'process-' + str(i), '--code', 'I63',
                        '--worktree', str(self.directory / ('process-' + str(i))), '--path', 'chapters/I63'],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for i in range(2)]
        results = [(p.communicate(timeout=30), p.returncode) for p in processes]
        self.assertEqual(sorted(result[1] for result in results), [0, 1])
        self.assertEqual(len(W.status(self.repo)), 1)

    def test_global_escaping_and_similar_prefix_paths_rejected(self):
        for path in ('chapters.json', 'organisation/status.json', 'chapters',
                     '../chapters/I63', '/chapters/I63', 'chapters/I63evil',
                     'chapters/I63/../E11', 'chapters/I63//x', 'glossary/e11.py'):
            with self.subTest(path=path), self.assertRaises(W.WorkspaceError):
                W.allowed_paths('I63', [path])
        self.assertEqual(W.allowed_paths('I63', ['assets/img/i63', 'assets/img/cycle2/i63']),
                         ['assets/img/cycle2/i63', 'assets/img/i63'])
        with self.assertRaises(W.WorkspaceError):
            W.allowed_paths('I63', ['assets/img/cycle2'])

    def test_git_symlink_ancestor_rejected(self):
        (self.repo / 'chapters' / 'I64').symlink_to('../I63', target_is_directory=True)
        W.git(self.repo, 'add', '.')
        W.git(self.repo, 'commit', '-m', 'symlink fixture')
        W.git(self.repo, 'push', 'origin', 'main')
        with self.assertRaisesRegex(W.WorkspaceError, 'symbolique'):
            self.begin(code='I64')

    def test_existing_or_nested_worktree_refused(self):
        for destination in (self.repo, self.repo / 'new', W.state_directory(self.repo) / 'new'):
            with self.subTest(destination=destination), self.assertRaises(W.WorkspaceError):
                W.begin(self.repo, actor='Codex', conversation='x', code='I63',
                        worktree=destination, files=['chapters/I63'])
        mission = self.begin()
        with self.assertRaisesRegex(W.WorkspaceError, 'imbriqué'):
            W.begin(mission['worktree'], actor='Claude', conversation='nested', code='E11',
                    worktree=self.repo / 'nested-from-another-worktree', files=['chapters/E11'])

    def test_status_detects_untracked_and_committed_outside_scope(self):
        mission = self.begin()
        worktree = Path(mission['worktree'])
        (worktree / 'README').write_text('hors perimetre')
        W.git(worktree, 'commit', '-am', 'hors contrat')
        (worktree / 'new-global').write_text('hors perimetre non suivi')
        report = W.status(self.repo)[0]
        self.assertEqual(report['unauthorized_files'], ['README', 'new-global'])
        with self.assertRaisesRegex(W.WorkspaceError, 'contrat'):
            W.close(self.repo, mission['id'])

    def test_clean_scoped_commit_can_close_without_removing_work(self):
        mission = self.begin()
        worktree = Path(mission['worktree'])
        (worktree / 'chapters/I63/I63_a.html').write_text('revision')
        with self.assertRaisesRegex(W.WorkspaceError, 'Committer'):
            W.close(self.repo, mission['id'])
        W.git(worktree, 'commit', '-am', 'scoped change')
        result = W.close(self.repo, mission['id'])
        self.assertEqual(result['state'], 'closed')
        self.assertTrue(worktree.exists())
        self.assertEqual(W.git(self.repo, 'show', 'main:chapters/I63/I63_a.html'), 'contenu I63')

    def test_audit_requires_other_ai_and_clean_author(self):
        mission = self.begin()
        with self.assertRaisesRegex(W.WorkspaceError, 'indépendant'):
            self.begin('audit-1', role='audit', author_mission=mission['id'])
        worktree = Path(mission['worktree'])
        (worktree / 'chapters/I63/I63_a.html').write_text('modification non commise')
        with self.assertRaisesRegex(W.WorkspaceError, 'committer'):
            self.begin('audit-2', actor='Claude', role='audit', author_mission=mission['id'])
        W.git(worktree, 'commit', '-am', 'source audit')
        audit = self.begin('audit-3', actor='Claude', role='audit', author_mission=mission['id'])
        self.assertEqual(audit['base_sha'], W.git(worktree, 'rev-parse', 'HEAD'))
        self.assertEqual(W.git(audit['worktree'], 'branch', '--show-current'), '')
        self.assertEqual(audit['access'], 'read_only_contract')
        (Path(audit['worktree']) / 'chapters/I63/I63_a.html').write_text('interdit')
        with self.assertRaisesRegex(W.WorkspaceError, 'contrat'):
            W.close(self.repo, audit['id'])
        self.assertEqual((worktree / 'chapters/I63/I63_a.html').read_text(), 'modification non commise')

    def test_no_remote_mutation(self):
        before = W.git(self.repo, 'ls-remote', 'origin')
        mission = self.begin()
        W.close(self.repo, mission['id'])
        self.assertEqual(W.git(self.repo, 'ls-remote', 'origin'), before)

    def test_closed_mission_readable_after_worktree_removed(self):
        mission = self.begin()
        closed = W.close(self.repo, mission['id'])
        W.git(self.repo, 'worktree', 'remove', mission['worktree'])
        report = W.status(self.repo)[0]
        self.assertEqual(report['state'], 'closed')
        self.assertIn('worktree_error', report)
        audit = self.begin('audit-closed', actor='Claude', role='audit', author_mission=mission['id'])
        self.assertEqual(audit['base_sha'], closed['final_sha'])

    def test_staged_only_global_change_detected(self):
        mission = self.begin()
        worktree = Path(mission['worktree'])
        (worktree / 'README').write_text('staged only')
        W.git(worktree, 'add', 'README')
        self.assertEqual(W.git(worktree, 'diff', '--name-only'), '')
        self.assertEqual(W.status(self.repo)[0]['unauthorized_files'], ['README'])

    def test_failed_worktree_creation_keeps_visible_exclusive_bail(self):
        original = W.git
        def fail_creation(root, *args):
            if args[:2] == ('worktree', 'add'):
                raise W.WorkspaceError('Échec fixture avant création')
            return original(root, *args)
        with patch.object(W, 'git', side_effect=fail_creation):
            with self.assertRaisesRegex(W.WorkspaceError, 'bail conservé'):
                self.begin()
        mission = W.status(self.repo)[0]
        self.assertFalse(mission['provisioned'])
        self.assertIn('worktree_error', mission)
        with self.assertRaisesRegex(W.WorkspaceError, 'Bail'):
            self.begin('conv-2')
        W.close(self.repo, mission['id'], abandon=True, reason='Création échouée examinée')


if __name__ == '__main__':
    unittest.main()
