"""Fixtures techniques de la garde des cycles Claude ; aucune revue ni validation clinique simulée."""
import copy
import json
from datetime import datetime
from pathlib import Path
import unittest
from unittest.mock import patch

from tools import cycle_claude as G
from tools import night_cycle as N
from tools import tetrade_cycle as C
from tests.test_tetrade_cycle import Tree, encode
from tests import test_night_cycle as TN

NOW = datetime.fromisoformat('2026-10-14T23:00:00+00:00')
START = '2026-10-14T21:00:00+00:00'
PNG = b'\x89PNG\r\n\x1a\n'


def rows_for(tree, n):
    return [dict(code=code, fragment_id=fragment, production_cycle=n, writer=f'C{n:02d}-R-{tag}',
                 cross_reviewer=f'C{n:02d}-R-{N.CROSS[tag]}', counter_reviewer=f'C{n:02d}-CA-{tag}',
                 status='EN_PRODUCTION', source_dir=None, files={}, images=None, **{k: None for k in G.PROOFS})
            for code, fragment, tag in N.missions(tree, n)]


class ClaudeFixture:
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.files = {p: (root / p).read_bytes() for p in (G.AUTHORITY, G.PLAN, G.CAHIER)}
        self.files[N.REGISTRY] = encode({'cycles': [{'cycle': 2, 'owner': 'Codex', 'state': 'ACTIF'}]})
        self.files['transmission/manifeste.json'] = encode({'cycle': 2, 'fixture': 'technique'})
        self.files['chapters.json'] = b'[]\n'
        self.state = dict(schema_version=1, authority=G.AUTHORITY, authority_sha256=C.digest(self.files[G.AUTHORITY]),
                          plan_sha256=C.digest(self.files[G.PLAN]), coordinator=G.COORDINATOR, not_before=G.NOT_BEFORE,
                          cycles=[dict(cycle=2, owner='Claude', state='ACTIF', started_at=START, transferred_from='Codex',
                                       handover=self.ref('transmission/manifeste.json'), cross_phase=None, closed_at=None,
                                       closure=None, budget=None, chapters=rows_for(Tree(self.files), 2))])
        self.files[G.JOURNAL] = encode(dict(event='cycle_started', cycle=2, at=START, coordinator_runtime='fixture-technique'))
        self.save()
        self.before = Tree(copy.deepcopy(self.files))

    def ref(self, path):
        return {'path': path, 'sha256': C.digest(self.files[path])}

    def save(self):
        self.files[G.REGISTRY] = encode(self.state)

    def guard(self, now=NOW):
        self.save()
        return G.validate(self.before, Tree(self.files), now=now)


class ClaudeCycleTests(ClaudeFixture, unittest.TestCase):
    def test_absent_registry_is_inactive(self):
        files = copy.deepcopy(self.files); files.pop(G.REGISTRY)
        self.assertEqual(G.validate(Tree(files), Tree(files), now=NOW), ({}, set(), set()))
        self.assertEqual(G.transferred_cycles(Tree(files)), set())

    def test_activation_has_four_courses(self):
        old = copy.deepcopy(self.files); old.pop(G.REGISTRY); old.pop(G.JOURNAL)
        self.assertEqual(G.validate(Tree(old), Tree(self.files), now=NOW), ({}, {'G45', 'E10', 'N18', 'D64'}, set()))
        self.assertEqual(G.transferred_cycles(Tree(self.files)), {2})

    def test_activation_without_journal_rejected(self):
        old = copy.deepcopy(self.files); old.pop(G.REGISTRY); old.pop(G.JOURNAL)
        self.files.pop(G.JOURNAL)
        with self.assertRaises(C.CycleError):
            G.validate(Tree(old), Tree(self.files), now=NOW)

    def test_activation_with_injection_rejected(self):
        old = copy.deepcopy(self.files); old.pop(G.REGISTRY); old.pop(G.JOURNAL)
        self.files['chapters/G45/G45_a.html'] = b'Fixture'
        with self.assertRaisesRegex(C.CycleError, 'activation'):
            G.validate(Tree(old), Tree(self.files), now=NOW)

    def test_identity_order_and_count(self):
        for action in ('extra', 'swap', 'owner', 'writer'):
            state = copy.deepcopy(self.state)
            rows = self.state['cycles'][0]['chapters']
            if action == 'extra': rows.append(copy.deepcopy(rows[0]))
            elif action == 'swap': rows.reverse()
            elif action == 'owner': self.state['cycles'][0]['owner'] = 'Codex'
            else: rows[0]['cross_reviewer'] = rows[0]['writer']
            with self.subTest(action=action), self.assertRaises(C.CycleError):
                self.guard()
            self.state = state

    def test_start_before_authorization_rejected(self):
        self.state['cycles'][0]['started_at'] = '2026-10-14T20:28:00+00:00'
        with self.assertRaisesRegex(C.CycleError, 'antérieur'):
            self.guard()

    def test_future_start_rejected(self):
        self.state['cycles'][0]['started_at'] = '2026-10-15T01:00:00+00:00'
        self.files[G.JOURNAL] += encode(dict(event='cycle_started', cycle=2, at='2026-10-15T01:00:00+00:00', coordinator_runtime='x'))
        with self.assertRaises(C.CycleError):
            self.guard()

    def test_transfer_requires_codex_cycle_and_handover(self):
        for action in ('handover', 'codex'):
            files, state = copy.deepcopy(self.files), copy.deepcopy(self.state)
            if action == 'handover': self.state['cycles'][0]['handover'] = None
            else: self.files[N.REGISTRY] = encode({'cycles': []})
            with self.subTest(action=action), self.assertRaises(C.CycleError):
                self.guard()
            self.files, self.state = files, state

    def test_own_cycle_cannot_reuse_codex_cycle_number(self):
        self.state['cycles'][0].update(transferred_from=None, handover=None)
        with self.assertRaisesRegex(C.CycleError, 'attribué à Codex'):
            self.guard()

    def test_second_cycle_before_closure_rejected(self):
        self.state['cycles'].append(dict(cycle=3, owner='Claude', state='ACTIF', started_at=START, transferred_from=None,
                                         handover=None, cross_phase=None, closed_at=None, closure=None, budget=None,
                                         chapters=rows_for(Tree(self.files), 3)))
        with self.assertRaisesRegex(C.CycleError, 'non clôturé'):
            self.guard()

    def test_canonical_or_image_without_injection_rejected(self):
        for path in ('chapters/G45/G45_a.html', 'glossary/e10.py', 'assets/img/cycle2/n18/x.png'):
            files = copy.deepcopy(self.files)
            self.files[path] = b'Fixture'
            with self.subTest(path=path), self.assertRaisesRegex(C.CycleError, 'sans injection'):
                with patch.object(G, 'temporal_proofs'), patch.object(N, 'journal_proof'):
                    self.guard()
            self.files = files

    def test_catalogue_without_injection_rejected(self):
        self.files['chapters.json'] = encode([dict(code='G45', covers=['G45'], integrated=True)])
        with self.assertRaisesRegex(C.CycleError, 'catalogue modifié'):
            self.guard()

    def test_authority_change_rejected(self):
        self.files[G.AUTHORITY] += b'Fixture altered'
        with self.assertRaisesRegex(C.CycleError, 'autorité ou plan'):
            self.guard()

    def test_journal_cannot_be_rewritten(self):
        self.files[G.JOURNAL] = encode(dict(event='cycle_started', cycle=2, at=START, coordinator_runtime='autre'))
        with self.assertRaisesRegex(C.CycleError, 'journal historique'):
            self.guard()

    def test_registry_cannot_be_deleted(self):
        self.files.pop(G.REGISTRY)
        with self.assertRaisesRegex(C.CycleError, 'suppression'):
            G.validate(self.before, Tree(self.files), now=NOW)


class ClaudeTemporalTests(ClaudeFixture, unittest.TestCase):
    def author_dates(self, entry, exit):
        self.files['preuves/auteur.json'] = encode({'entry': {'checked_at': entry}, 'exit': {'checked_at': exit}})
        cycle = self.state['cycles'][0]
        cycle['chapters'][0]['author'] = self.ref('preuves/auteur.json')
        return G.temporal_proofs(Tree(self.files), cycle, NOW)

    def test_proof_dates_inside_cycle_accepted(self):
        self.author_dates('2026-10-14T21:05:00+00:00', '2026-10-14T21:30:00+00:00')

    def test_proof_before_not_before_rejected(self):
        self.state['cycles'][0]['started_at'] = G.NOT_BEFORE
        with self.assertRaisesRegex(C.CycleError, 'antérieure'):
            self.author_dates('2026-10-14T20:00:00+00:00', '2026-10-14T21:30:00+00:00')

    def test_proof_before_cycle_start_rejected(self):
        with self.assertRaisesRegex(C.CycleError, 'antidatée'):
            self.author_dates('2026-10-14T20:45:00+00:00', '2026-10-14T21:30:00+00:00')

    def test_future_proof_rejected(self):
        with self.assertRaisesRegex(C.CycleError, 'future'):
            self.author_dates('2026-10-14T21:05:00+00:00', '2026-10-15T01:00:00+00:00')

    def test_no_hourly_deadline(self):
        cycle = self.state['cycles'][0]
        self.files['preuves/auteur.json'] = encode({'entry': {'checked_at': '2026-10-16T08:00:00+00:00'},
                                                    'exit': {'checked_at': '2026-10-16T09:00:00+00:00'}})
        cycle['chapters'][0]['author'] = self.ref('preuves/auteur.json')
        G.temporal_proofs(Tree(self.files), cycle, datetime.fromisoformat('2026-10-17T00:00:00+00:00'))


class ClaudeInjectionTests(ClaudeFixture, unittest.TestCase):
    def prepared(self):
        for row in self.state['cycles'][0]['chapters']:
            row['status'] = 'PRET_A_INJECTER'
            row['files'] = {f"chapters/{row['code']}/{row['code']}_a.html": C.digest(b'Fixture')}
            for k in ('author', 'cross_audit', 'counter_audit', 'control'):
                row[k] = {'path': 'Fixture technique non clinique'}
        self.save(); self.before = Tree(copy.deepcopy(self.files))

    def inject(self, i, injector=G.COORDINATOR):
        row = self.state['cycles'][0]['chapters'][i]; row['status'] = 'INJECTE'
        p = f'preuves/injection-{i}.json'
        self.files[p] = encode(dict(code=row['code'], files=row['files'], injector=injector))
        row['injection'] = self.ref(p)
        for f in row['files']:
            self.files[f] = b'Fixture'
        catalog = json.loads(self.files['chapters.json'])
        catalog.append(dict(code=row['code'], covers=[row['code']], integrated=True, production_cycle=2))
        self.files['chapters.json'] = encode(catalog)

    def mocked(self):
        with patch.object(G, 'ready', side_effect=lambda tree, row, rows, **kw: row['files']), \
                patch.object(G, 'temporal_proofs'), patch.object(N, 'journal_proof'), \
                patch.object(G, 'cross_boundary', return_value=NOW), patch.object(N, 'image_proof', return_value={}):
            return self.guard()

    def test_exact_single_injection(self):
        self.prepared(); self.inject(0)
        authorized, codes, catalog = self.mocked()
        self.assertEqual(set(authorized), {'chapters/G45/G45_a.html', 'chapters.json'})
        self.assertEqual(catalog, {'G45'})
        self.assertEqual(codes, {'G45', 'E10', 'N18', 'D64'})

    def test_codex_injector_rejected(self):
        self.prepared(); self.inject(0, injector='Codex — coordinateur du fil')
        with self.assertRaisesRegex(C.CycleError, 'reçu injection'):
            self.mocked()

    def test_double_injection_rejected(self):
        self.prepared(); self.inject(0); self.inject(1)
        with self.assertRaisesRegex(C.CycleError, 'une seule injection'):
            self.mocked()

    def test_order_rejected(self):
        self.prepared(); self.inject(1)
        with self.assertRaisesRegex(C.CycleError, 'ordre de publication'):
            self.mocked()

    def test_extra_catalogue_row_rejected(self):
        self.prepared(); self.inject(0)
        rows = json.loads(self.files['chapters.json']); rows.append(dict(code='J45', covers=['J45'], integrated=True))
        self.files['chapters.json'] = encode(rows)
        with self.assertRaisesRegex(C.CycleError, 'ajout unique'):
            self.mocked()

    def test_extra_image_change_rejected(self):
        self.prepared(); self.inject(0); self.files['assets/img/cycle2/e10/unreviewed.png'] = b'Fixture'
        with self.assertRaisesRegex(C.CycleError, 'supplémentaires'):
            self.mocked()

    def test_injected_source_is_locked(self):
        self.prepared(); self.inject(0); self.mocked()
        self.before = Tree(copy.deepcopy(self.files))
        self.files['chapters/G45/G45_a.html'] = b'Fixture modifiee'
        with self.assertRaisesRegex(C.CycleError, 'source injectée modifiée'):
            self.mocked()

    def test_injected_row_record_is_locked(self):
        self.prepared(); self.inject(0); self.mocked()
        self.before = Tree(copy.deepcopy(self.files))
        self.state['cycles'][0]['chapters'][0]['author'] = {'path': 'Autre fixture'}
        with self.assertRaisesRegex(C.CycleError, 'cours injecté modifié'):
            self.mocked()


class CaptureTests(unittest.TestCase):
    def tree(self, n):
        files, captures = {}, []
        for i, kind in enumerate(('opening', 'window', 'figure', 'table', 'quiz')[:n]):
            path = f'captures/{i}.png'; files[path] = PNG + bytes([i]) * 6000
            captures.append({'kind': kind, 'path': path, 'sha256': C.digest(files[path])})
        return Tree(files), captures

    def test_four_distinct_captures_accepted(self):
        tree, captures = self.tree(4)
        C.capture_proof(tree, captures, G.CAPTURES)

    def test_fewer_than_four_rejected(self):
        tree, captures = self.tree(3)
        with self.assertRaisesRegex(C.CycleError, '4 captures'):
            C.capture_proof(tree, captures, G.CAPTURES)

    def test_duplicate_kind_or_file_rejected(self):
        tree, captures = self.tree(4)
        for field in ('kind', 'path'):
            bad = copy.deepcopy(captures); bad[3][field] = bad[0][field]
            if field == 'path': bad[3]['sha256'] = bad[0]['sha256']
            with self.subTest(field=field), self.assertRaises(C.CycleError):
                C.capture_proof(tree, bad, G.CAPTURES)

    def test_small_or_non_png_rejected(self):
        tree, captures = self.tree(4)
        tree.files[captures[2]['path']] = PNG + b'x'
        captures[2]['sha256'] = C.digest(tree.files[captures[2]['path']])
        with self.assertRaisesRegex(C.CycleError, 'PNG'):
            C.capture_proof(tree, captures, G.CAPTURES)

    def test_default_remains_two_captures(self):
        tree, captures = self.tree(2)
        captures[1]['kind'] = 'explanation'
        C.capture_proof(tree, captures)
        tree4, four = self.tree(4)
        with self.assertRaisesRegex(C.CycleError, 'Deux captures'):
            C.capture_proof(tree4, four)


class NightDelegationTests(unittest.TestCase):
    """night_cycle ignore seulement les cycles déclarés repris par Claude."""
    setUp = TN.NightGuardTests.setUp
    save = TN.NightGuardTests.save
    guard = TN.NightGuardTests.guard

    def claude_registry(self, cycle, transferred_from='Codex'):
        return encode({'cycles': [{'cycle': cycle, 'owner': 'Claude', 'transferred_from': transferred_from}]})

    def test_transferred_cycle_sources_left_to_claude_guard(self):
        self.files[G.REGISTRY] = self.before.files[G.REGISTRY] = self.claude_registry(2)
        self.before = Tree(self.before.files)
        self.files['chapters/G45/G45_a.html'] = b'Fixture'
        self.files['assets/img/cycle2/g45/x.png'] = b'Fixture'
        authorized, codes, catalog = self.guard(datetime.fromisoformat('2026-10-14T23:00:00+00:00'))
        self.assertEqual((authorized, codes, catalog), ({}, set(), set()))

    def test_untransferred_codex_cycle_still_guarded(self):
        for registry in (None, self.claude_registry(3), self.claude_registry(2, transferred_from=None)):
            files = copy.deepcopy(self.files)
            if registry is not None:
                self.files[G.REGISTRY] = registry
            self.files['chapters/G45/G45_a.html'] = b'Fixture'
            with self.subTest(registry=registry), self.assertRaisesRegex(C.CycleError, 'sans injection'):
                self.guard()
            self.files = files

    def test_codex_registry_of_transferred_cycle_stays_immutable(self):
        self.files[G.REGISTRY] = self.claude_registry(2)
        self.state['cycles'][0]['chapters'][0]['status'] = 'EN_AUDIT_CROISE'
        with self.assertRaises(C.CycleError):
            self.guard(datetime.fromisoformat('2026-10-14T23:00:00+00:00'))
        with patch.object(N, 'journal_proof'), patch.object(N, 'temporal_proofs'), self.assertRaisesRegex(C.CycleError, 'immuable'):
            self.guard()


if __name__ == '__main__':
    unittest.main()


class ClaudeReadyParametersTests(unittest.TestCase):
    def test_ready_uses_claude_coordinator_prompts_roots_and_four_captures(self):
        row = {'code': 'G45', **{k: None for k in ('author', 'cross_audit', 'counter_audit', 'control')}}
        with patch.object(C, 'ready', return_value={'a': '1'}) as ready, patch.object(N, 'review_identities'), \
                patch.object(N, 'image_proof', return_value={'img': '2'}), patch.object(C, 'proof', return_value={'image_files': {'img': '2'}}):
            self.assertEqual(G.ready(None, row, [row]), {'a': '1', 'img': '2'})
        kwargs = ready.call_args.kwargs
        self.assertEqual((kwargs['control_actor'], kwargs['captures'], kwargs['prompts'], kwargs['source_roots']),
                         (G.COORDINATOR, 4, G.PROMPTS, G.SOURCE_ROOTS))
        self.assertIn(G.AUTHORITY, G.PROMPTS)
        self.assertNotIn(N.AUTHORITY, G.PROMPTS)
