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

    def test_other_ai_cannot_release(self):
        release = dict(id='r1', event='release', actor='Claude', at=self.veto['at'], reason='Désaccord', veto_id='v1')
        with self.assertRaisesRegex(G.GovernanceError, 'ne peut lever'):
            G.events(encode(self.veto) + encode(release))

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
