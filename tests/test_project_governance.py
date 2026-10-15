"""Veto déclaratifs de projet et rejeu de vrais commits temporaires."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import espace as E
from tools import project_governance as G
from tools import sceller as S
from tests.test_tetrade_cycle import Tree, encode


class VetoTests(unittest.TestCase):
    def setUp(self):
        self.veto = dict(id='v1', actor='Codex', event='veto', at='2026-10-15T12:00:00+00:00',
                         reason='Conflit de branche à résoudre', scope='chapters', operations=['change', 'publish'])

    def test_both_actors_can_block_changes(self):
        for actor in ('Codex', 'Claude'):
            veto = dict(self.veto, actor=actor)
            before = Tree({G.JOURNAL: encode(veto), 'chapters/I63/a.html': b'avant'})
            after = Tree({G.JOURNAL: encode(veto), 'chapters/I63/a.html': b'apres'})
            with self.subTest(actor=actor), self.assertRaisesRegex(G.GovernanceError, actor):
                G.check(before, after)

    def test_scoped_veto_allows_unrelated_technical_change(self):
        before = Tree({G.JOURNAL: encode(self.veto), 'README.md': b'avant'})
        after = Tree({G.JOURNAL: encode(self.veto), 'README.md': b'apres'})
        G.check(before, after)

    def test_publish_veto_blocks_even_without_new_changes(self):
        tree = Tree({G.JOURNAL: encode(self.veto)})
        with self.assertRaisesRegex(G.GovernanceError, 'Veto v1'):
            G.check(tree, tree, 'publish')

    def release(self, **changes):
        row = dict(id='r1', event='release', actor='Claude', at=self.veto['at'],
                   reason='Le veto Codex ralentit la livraison indépendante Claude', veto_id='v1',
                   authority=copy.deepcopy(G.CLAUDE_RELEASE_AUTHORITY))
        row.update(changes)
        return row

    def order_files(self):
        path = G.CLAUDE_RELEASE_AUTHORITY['path']
        return {path: (G.ROOT / path).read_bytes()}

    def test_claude_releases_codex_veto_under_own_name(self):
        raw = encode(self.veto)
        release = self.release()
        before = Tree({**self.order_files(), G.JOURNAL: raw})
        after = Tree({**self.order_files(), G.JOURNAL: raw + encode(release)})
        G.check(before, after)
        data, active = G.events(after.read(G.JOURNAL))
        self.assertEqual(active, {})
        self.assertEqual(data[-1]['actor'], 'Claude')

    def test_claude_release_requires_exact_human_delegation(self):
        wrong_hash = dict(G.CLAUDE_RELEASE_AUTHORITY, sha256='0' * 64)
        wrong_path = dict(G.CLAUDE_RELEASE_AUTHORITY, path='README.md')
        for authority in (None, {}, wrong_hash, wrong_path):
            with self.subTest(authority=authority), self.assertRaisesRegex(G.GovernanceError, 'délégation Vial exacte'):
                G.events(encode(self.veto) + encode(self.release(authority=authority)))

    def test_changed_order_bytes_cannot_authorize_release(self):
        raw = encode(self.veto)
        before = Tree({**self.order_files(), G.JOURNAL: raw})
        after = Tree({G.CLAUDE_RELEASE_AUTHORITY['path']: b'instruction altered',
                      G.JOURNAL: raw + encode(self.release())})
        with self.assertRaisesRegex(G.GovernanceError, 'Instruction humaine différente'):
            G.check(before, after)

    def test_claude_release_does_not_authorize_combined_operation(self):
        raw = encode(self.veto)
        before = Tree({**self.order_files(), G.JOURNAL: raw, 'chapters/I63/a.html': b'avant'})
        released = Tree({**before.files, G.JOURNAL: raw + encode(self.release())})
        operated = Tree({**released.files, 'chapters/I63/a.html': b'after'})
        G.check(before, released)
        with self.assertRaisesRegex(G.GovernanceError, 'commit distinct'):
            G.check(before, operated)
        G.check(released, operated)

    def test_order_does_not_grant_codex_a_new_right_over_claude(self):
        veto = dict(self.veto, actor='Claude')
        with self.assertRaisesRegex(G.GovernanceError, 'ne peut lever'):
            G.events(encode(veto) + encode(self.release(actor='Codex')))

    def test_cli_claude_attaches_order_and_preserves_history(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for path, data in self.order_files().items():
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            journal = root / G.JOURNAL
            journal.parent.mkdir(parents=True)
            raw = encode(self.veto)
            journal.write_bytes(raw)
            args = ['project_governance.py', 'release', '--actor', 'Claude', '--veto-id', 'v1',
                    '--reason', 'Ce blocage Codex ralentit mon travail']
            with patch.object(G, 'ROOT', root), patch('sys.argv', args):
                self.assertEqual(G.main(), 0)
            result = journal.read_bytes()
            self.assertTrue(result.startswith(raw))
            data, active = G.events(result)
            self.assertEqual(active, {})
            self.assertEqual(data[-1]['actor'], 'Claude')
            self.assertEqual(data[-1]['authority'], G.CLAUDE_RELEASE_AUTHORITY)

    def test_owner_release_requires_distinct_commit(self):
        raw = encode(self.veto)
        release = dict(id='r1', event='release', actor='Codex', at=self.veto['at'], reason='Conflit résolu', veto_id='v1')
        before = Tree({G.JOURNAL: raw, 'chapters/I63/a.html': b'avant'})
        after = Tree({G.JOURNAL: raw + encode(release), 'chapters/I63/a.html': b'avant'})
        G.check(before, after)
        after.files['chapters/I63/a.html'] = b'apres'
        after = Tree(after.files)
        with self.assertRaisesRegex(G.GovernanceError, 'commit distinct'):
            G.check(before, after)

    def test_historical_veto_cannot_be_removed(self):
        with self.assertRaisesRegex(G.GovernanceError, 'historique'):
            G.check(Tree({G.JOURNAL: encode(self.veto)}), Tree({G.JOURNAL: b''}))

    def test_shared_fingerprint_registry_accepts_both_actors(self):
        for actor in ('Codex', 'Claude'):
            registry = dict(autorite=S.COMMON_AUTHORITY, injecteur=actor, scelle=True, fichiers={'chapters/I63/a.html': 'a' * 64})
            self.assertEqual(S.guard(registry, registry, set(), lambda path: b''), registry['fichiers'])

    def test_historical_fingerprint_registry_is_still_readable(self):
        registry = dict(autorite=S.AUTHORITY, injecteur='Claude', scelle=True, fichiers={'chapters/I63/a.html': 'a' * 64})
        self.assertEqual(S.guard(registry, registry, set(), lambda path: b''), registry['fichiers'])


class CommitReplayTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test technique')
        self.git('config', 'user.email', 'test@example.invalid')
        self.write('chapters/I63/a.html', b'Contenu initial de fixture')
        self.first = self.commit()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL).decode().strip()

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'Fixture technique')
        return self.git('rev-parse', 'HEAD')

    def test_accepts_separate_technical_commits(self):
        self.write('README.md', b'A'); second = self.commit()
        self.write('README.md', b'B'); third = self.commit()
        self.assertEqual(E.guard_transitions(self.root, self.first, third), [(self.first, second), (second, third)])
        with patch.object(E, 'R', self.root):
            self.assertEqual(E.garde(self.first, third), 0)

    def test_rejects_unauthorized_intermediate_content_even_if_reverted(self):
        self.write('chapters/I63/a.html', b'Modification sans preuve'); self.commit()
        self.write('chapters/I63/a.html', b'Contenu initial de fixture'); final = self.commit()
        with patch.object(E, 'R', self.root):
            self.assertEqual(E.garde(self.first, final), 1)

    def test_comparison_across_branches_stays_aggregate(self):
        self.git('checkout', '-qb', 'other')
        self.write('README.md', b'autre'); other = self.commit()
        self.git('checkout', '-q', '-'); self.write('README.md', b'original'); current = self.commit()
        self.assertEqual(E.guard_transitions(self.root, other, current), [(other, current)])
