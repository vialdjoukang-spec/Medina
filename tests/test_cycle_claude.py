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
            self.author_dates('2026-10-14T20:00:00+00:00', '2026-10-14T21:30:00+00:00')

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


# ---------------------------------------------------------------------------
# Publication directe des cycles 3 à 30 (autorité du 14 octobre 2026).
# Preuves techniques simulées : aucune revue réelle ni validation clinique.
# ---------------------------------------------------------------------------
T = '2026-10-14T{}:00+00:00'.format
START3 = T('21:40')
CHECKS = ('autorisation', 'perimetre_provenance', 'sources_lues', 'contexte_suisse', 'independance', 'contrat_cours', 'honnetete')
_IMAGE_PROOF = N.image_proof


def _image_proof(tree, row):
    # Le Cycle 2 clos de la fixture n'a pas d'images : seules ses preuves de publication sont simulées.
    return {} if row.get('images') is None else _IMAGE_PROOF(tree, row)


class DirectFixture:
    prompts = G.PROMPTS_DIRECT
    boundary = NOW

    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        paths = {G.AUTHORITY, G.PLAN, G.CAHIER, G.DIRECT_AUTHORITY, *G.PROMPTS, *G.PROMPTS_DIRECT}
        self.files = {p: (root / p).read_bytes() for p in paths}
        self.files[N.REGISTRY] = encode({'cycles': []})
        self.files['chapters.json'] = b'[]\n'
        self.files['preuves/evidence.txt'] = b'Fixture technique non clinique'
        self.events = [dict(event='cycle_started', cycle=2, at=START, coordinator_runtime='fixture')]
        rows2 = rows_for(Tree(self.files), 2)
        for row in rows2:
            p = f"preuves/c2-{row['code']}.json"
            self.files[p] = encode(dict(code=row['code'], entry={'checked_at': T('21:10')}, exit={'checked_at': T('21:15')},
                                        checked_at=T('21:20'), deployment_status='success', readback=True, gauges=True,
                                        main_sha='a' * 40, public_url='https://vialdjoukang-spec.github.io/Medina/fragments/x.html'))
            row.update(status='PUBLIE_VERIFIE', **{k: self.ref(p) for k in G.PROOFS})
            self.events.append(self.event(2, row))
        self.files['preuves/c2-cloture.json'] = encode(dict(cycle=2, blocking_reserves=[]))
        cycle2 = dict(cycle=2, owner='Claude', state='CLOTURE', started_at=START, transferred_from=None, handover=None,
                      cross_phase=None, closed_at=T('21:30'), closure=self.ref('preuves/c2-cloture.json'), budget=None, chapters=rows2)
        rows3 = rows_for(Tree(self.files), 3)
        for row in rows3:
            row.update(cross_reviewer=None, counter_reviewer=None)
        self.cycle3 = dict(cycle=3, owner='Claude', state='ACTIF', started_at=START3, mode=G.DIRECT_MODE,
                           authority=G.DIRECT_AUTHORITY, authority_sha256=C.digest(self.files[G.DIRECT_AUTHORITY]),
                           transferred_from=None, handover=None, cross_phase=None, closed_at=None, closure=None,
                           budget=None, chapters=rows3)
        self.events.append(dict(event='cycle_started', cycle=3, at=START3, coordinator_runtime='fixture', mode=G.DIRECT_MODE))
        self.state = dict(schema_version=1, authority=G.AUTHORITY, authority_sha256=C.digest(self.files[G.AUTHORITY]),
                          plan_sha256=C.digest(self.files[G.PLAN]), coordinator=G.COORDINATOR, not_before=G.NOT_BEFORE,
                          cycles=[cycle2, self.cycle3])
        self.snapshot()

    rows = property(lambda self: self.cycle3['chapters'])

    def ref(self, path):
        return {'path': path, 'sha256': C.digest(self.files[path])}

    def event(self, n, row, at=T('22:30')):
        return dict(event='stage_recorded', cycle=n, code=row['code'], status=row['status'],
                    proofs={k: row[k] for k in G.PROOFS}, runtime_agent_id='fixture', at=at)

    def save(self):
        self.files[G.REGISTRY] = encode(self.state)
        self.files[G.JOURNAL] = b''.join(encode(e) for e in self.events)

    def snapshot(self):
        self.save(); self.before = Tree(copy.deepcopy(self.files))

    def write(self, path, data):
        self.files[path] = encode(data) if not isinstance(data, bytes) else data
        return self.ref(path)

    def gate(self, actor, at):
        return dict(actor=actor, verdict='conforme', checked_at=at,
                    prompt_files={p: C.digest(self.files[p]) for p in self.prompts},
                    checks=[dict(id=c, status='conforme', evidence=[dict(path='preuves/evidence.txt', explanation='Fixture',
                                                                          sha256=C.digest(self.files['preuves/evidence.txt']))])
                            for c in CHECKS])

    def produce(self, i, captures=4, prompts=None, technical_extra=None, ledger_extra=None):
        """Leçon i prête : sources livrées, registre des sources, images, auteur, contrôle et captures simulés."""
        row = self.rows[i]; code = row['code']; lc = code.lower(); n = row['production_cycle']
        src = f'livraisons/Livraison Claude/C-{n:02d}/CYCLE_{n:02d}_{code}'
        if n == 2:
            lesson = next(x for x in json.loads(self.files[G.CAHIER])['lessons'] if x['code'] == code)
            slots = [(im['id'], im['anchor']) for part in lesson['parts'] for im in part['images']]
        else:
            slots = [('fig1', f'{lc}-figure')]
        figures, manifest_rows, images = [], [], {}
        for k, (ident, anchor) in enumerate(slots):
            image = f'assets/img/cycle{n}/{lc}/figure-{k}.png'
            self.files[src + '/' + image] = PNG + bytes([i, k]) * 300
            images[image] = C.digest(self.files[src + '/' + image])
            figures.append(f'<div id="{anchor}"><img src="../../{image}" alt="Figure {code} {k}"></div>')
            manifest_rows.append(dict(
                id=ident, anchor=anchor, source_page_url='https://commons.wikimedia.org/x', file_url='https://upload.wikimedia.org/x.png',
                author='Fixture', license='CC BY 4.0', attribution='Fixture', caption='Fixture', alt=f'Figure {code} {k}',
                location='a', path=image, sha256=images[image], accessed_at=T('21:45'), generated=False,
                open_license_verified=True, visual_reviewed=True))
        sources = {f'chapters/{code}/{code}_{s}.html': f'<p id="{lc}-{s}">Fixture</p>'.encode() for s in ('b', 'c', 'd', 'pop1', 'pop2')}
        sources[f'chapters/{code}/{code}_a.html'] = ''.join(figures).encode()
        sources[f'glossary/{lc}.py'] = b'# Fixture\n'
        for p, raw in sources.items():
            self.files[src + '/' + p] = raw
        files = {p: C.digest(raw) for p, raw in sources.items()}
        manifest = self.write(f'preuves/{lc}-images.json', {'images': manifest_rows})
        ledger = self.write(f'preuves/{lc}-sources.json', dict(code=code, final_files=files, unverified_claims=[],
                            covered_files=list(files), claims=[dict(
                                claim='Fixture', location='a', source_url='https://www.swissmedicinfo.ch/', source_title='Fixture',
                                version_date='2026-01-01', section='1', source_passage_summary='Fixture', population='Adultes',
                                limits='Fixture', accessed_on='2026-10-14', download_sha256='b' * 64)]) | (ledger_extra or {}))
        common = dict(code=code, medical_human_validation=False, final_files=files, blocking_reserves=[], image_files=images)
        prompts = prompts or getattr(self, 'author_default', None) or self.prompts
        author_gate = lambda at: dict(self.gate(row['writer'], at), prompt_files={p: C.digest(self.files[p]) for p in prompts})
        author = self.write(f'preuves/{lc}-auteur.json', dict(common, actor=row['writer'], runtime_agent_id='agent-' + row['writer'],
                            entry=author_gate(T('21:50')), exit=author_gate(T('22:00')), source_ledger=ledger))
        if row['cross_reviewer']:
            row['cross_audit'] = self.cross_review(row, common, files)
        shots = []
        for k, kind in enumerate(('ouverture', 'fenetre', 'figure', 'mobile')[:captures]):
            p = f'preuves/{lc}-capture-{k}.png'
            shots.append(dict(kind=kind, **self.write(p, PNG + bytes([i * 10 + k]) * 6000)))
        technical = self.write(f'preuves/{lc}-technique.json', dict(final_files=files, result='passed', desktop=True, mobile=True,
                               missing_windows=[], javascript_errors=[], uncovered_abbreviations=[], horizontal_overflow=False,
                               captures=shots) | (technical_extra or {}))
        control = self.write(f'preuves/{lc}-controle.json', dict(common, actor=G.COORDINATOR, runtime_agent_id='coordinateur',
                             entry=self.gate(G.COORDINATOR, T('22:05')), exit=self.gate(G.COORDINATOR, T('22:10')),
                             technical_checks=technical, swiss_context={'verdict': 'conforme'}))
        row.update(source_dir=src, files=files, images=manifest, author=author, control=control, status='PRET_A_INJECTER')
        self.events.append(self.event(n, row))

    def cross_review(self, row, common, files):
        actor, lc = row['cross_reviewer'], row['code'].lower()
        passes = []
        for number, (start, end) in enumerate(((T('22:01'), T('22:02')), (T('22:03'), T('22:04'))), 1):
            report = dict(actor=actor, code=row['code'], **{'pass': number}, started_at=start, finished_at=end,
                          dimensions={d: 'Fixture' for d in C.DIMENSIONS},
                          numerical_checks=[dict(claim=f'Donnée {k}', source='Fixture', section='1', passage='Fixture', finding='Conforme')
                                            for k in range(10)],
                          verdict='favorable', blocking_reserves=[], final_files=files, score=20)
            passes.append(dict(number=number, report=self.write(f'preuves/{lc}-croise-{number}.json', report)))
        return self.write(f'preuves/{lc}-croise.json', dict(common, actor=actor, runtime_agent_id='agent-' + actor,
                          entry=self.gate(actor, T('22:01')), exit=self.gate(actor, T('22:05')), passes=passes))

    def inject(self, i, catalog_extra=None):
        row = self.rows[i]
        row['status'] = 'INJECTE'
        locked = dict(row['files'], **{im['path']: im['sha256'] for im in json.loads(self.files[row['images']['path']])['images']})
        for p in locked:
            self.files[p] = self.files[row['source_dir'] + '/' + p]
        row['injection'] = self.write(f"preuves/{row['code'].lower()}-injection.json",
                                      dict(code=row['code'], files=locked, injector=G.COORDINATOR, checked_at=T('22:20')))
        entry = dict(code=row['code'], covers=[row['code']], integrated=True, production_cycle=row['production_cycle'],
                     provisional_injection=True, audit_deferred=G.DIRECT_DEFERRED)
        entry.update(catalog_extra or {})
        self.files['chapters.json'] = encode(json.loads(self.files['chapters.json']) + [entry])
        self.events.append(self.event(row['production_cycle'], row))

    def publish(self, i):
        row = self.rows[i]; row['status'] = 'PUBLIE_VERIFIE'
        row['publication'] = self.write(f"preuves/{row['code'].lower()}-publication.json", dict(
            code=row['code'], checked_at=T('22:25'), deployment_status='success', readback=True, gauges=True,
            main_sha='c' * 40, public_url='https://vialdjoukang-spec.github.io/Medina/fragments/x.html'))
        self.events.append(self.event(row['production_cycle'], row))

    def guard(self, now=NOW):
        self.save()
        with patch.object(G, 'ready', side_effect=lambda tree, row, rows, **kw: row['files']), \
                patch.object(G, 'cross_boundary', return_value=self.boundary), \
                patch.object(N, 'image_proof', side_effect=_image_proof), \
                patch('tools.espace.swiss_context_proof') as swiss:
            result = G.validate(self.before, Tree(self.files), now=now)
        self.swiss_calls = swiss.call_count
        return result

    def ready_cycle(self):
        for i in range(4):
            self.produce(i)
        self.snapshot()


class DirectPublicationTests(DirectFixture, unittest.TestCase):
    def test_prompts_direct_replace_cycle2_authority(self):
        self.assertIn(G.DIRECT_AUTHORITY, G.PROMPTS_DIRECT)
        self.assertNotIn(G.AUTHORITY, G.PROMPTS_DIRECT)
        self.assertEqual(len(G.PROMPTS_DIRECT), len(G.PROMPTS))

    def test_ready_transition_accepted_without_cross_audit(self):
        for i in range(4):
            self.produce(i)
        self.assertEqual(self.guard()[0], {})
        self.assertEqual(self.swiss_calls, 4)

    def test_direct_injection_accepted(self):
        self.ready_cycle(); self.inject(0)
        authorized, codes, catalog = self.guard()
        row = self.rows[0]
        self.assertEqual(set(authorized), set(row['files']) | {'assets/img/cycle3/i61/figure-0.png', 'chapters.json'})
        self.assertEqual(catalog, {'I61'})
        self.assertIn('I61', codes)

    def test_full_cycle_and_next_start(self):
        self.ready_cycle()
        for i in range(4):
            self.inject(i); self.guard(); self.snapshot()
            self.publish(i); self.guard(); self.snapshot()
        self.files['preuves/c3-cloture.json'] = encode(dict(cycle=3, blocking_reserves=[]))
        self.cycle3.update(state='CLOTURE', closed_at=T('22:40'), closure=self.ref('preuves/c3-cloture.json'))
        self.guard(); self.snapshot()
        rows4 = [dict(r, cross_reviewer=None, counter_reviewer=None) for r in rows_for(Tree(self.files), 4)]
        self.state['cycles'].append(dict(self.cycle3, cycle=4, state='ACTIF', started_at=T('22:45'), closed_at=None,
                                         closure=None, chapters=rows4))
        self.events.append(dict(event='cycle_started', cycle=4, at=T('22:45'), coordinator_runtime='fixture'))
        self.guard()

    def test_without_control_rejected(self):
        self.produce(0); self.rows[0]['control'] = None; self.events.append(self.event(3, self.rows[0]))
        with self.assertRaisesRegex(C.CycleError, 'control : preuve absente'):
            self.guard()

    def test_without_four_captures_rejected(self):
        self.produce(0, captures=3)
        with self.assertRaisesRegex(C.CycleError, '4 captures'):
            self.guard()

    def test_technical_failure_rejected(self):
        for extra in ({'javascript_errors': ['x']}, {'missing_windows': ['w']}, {'mobile': False},
                      {'uncovered_abbreviations': ['ABC']}, {'horizontal_overflow': True}, {'result': 'failed'}):
            self.setUp(); self.produce(0, technical_extra=extra)
            with self.subTest(extra=extra), self.assertRaisesRegex(C.CycleError, 'Contrôle final'):
                self.guard()

    def test_unverified_claim_rejected(self):
        for extra in ({'unverified_claims': ['x']}, {'covered_files': ['chapters/I61/I61_a.html']}, {'claims': []}):
            self.setUp(); self.produce(0, ledger_extra=extra)
            with self.subTest(extra=extra), self.assertRaisesRegex(C.CycleError, 'Registre des sources'):
                self.guard()

    def test_cycle2_prompts_rejected_in_direct_mode(self):
        self.produce(0, prompts=G.PROMPTS)
        with self.assertRaisesRegex(C.CycleError, 'Prompt'):
            self.guard()

    def test_fictitious_audit_rejected(self):
        for action in ('cross', 'counter', 'state', 'reviewer'):
            files, state, events = copy.deepcopy(self.files), copy.deepcopy(self.state), copy.deepcopy(self.events)
            self.cycle3 = self.state['cycles'][1]
            self.produce(0)
            row = self.rows[0]
            if action == 'cross': row['cross_audit'] = row['author']
            elif action == 'counter': row['counter_audit'] = row['control']
            elif action == 'state': row['status'] = 'EN_CONTRE_AUDIT'
            else: row['cross_reviewer'] = 'C03-R-HEM'
            self.events.append(self.event(row['production_cycle'], row))
            with self.subTest(action=action), self.assertRaisesRegex(C.CycleError, 'fictif|indépendance'):
                self.guard()
            self.files, self.state, self.events = files, state, events
            self.cycle3 = self.state['cycles'][1]

    def test_order_and_double_injection_rejected(self):
        self.ready_cycle(); self.inject(1)
        with self.assertRaisesRegex(C.CycleError, 'ordre de publication'):
            self.guard()
        self.setUp(); self.ready_cycle(); self.inject(0); self.inject(1)
        with self.assertRaisesRegex(C.CycleError, 'une seule injection'):
            self.guard()

    def test_catalogue_without_deferred_audit_rejected(self):
        for extra in ({'audit_deferred': None}, {'provisional_injection': False}, {'production_cycle': 2}):
            self.setUp(); self.ready_cycle(); self.inject(0, catalog_extra=extra)
            with self.subTest(extra=extra), self.assertRaisesRegex(C.CycleError, 'catalogue|audit différé'):
                self.guard()

    def test_injected_course_immutable(self):
        self.ready_cycle(); self.inject(0); self.guard(); self.snapshot()
        self.files['chapters/I61/I61_b.html'] = b'Correction sans exception'
        with self.assertRaisesRegex(C.CycleError, 'source injectée modifiée'):
            self.guard()

    def test_proof_before_cycle_start_rejected(self):
        self.produce(0)
        author = json.loads(self.files['preuves/i61-auteur.json']); author['entry']['checked_at'] = T('21:35')
        self.rows[0]['author'] = self.write('preuves/i61-auteur.json', author)
        self.events.append(self.event(3, self.rows[0]))
        with self.assertRaisesRegex(C.CycleError, 'antidatée'):
            self.guard()

    def test_mode_cannot_be_added_or_removed(self):
        self.cycle3.pop('mode')
        with self.assertRaisesRegex(C.CycleError, 'autorité propre'):
            self.guard()

    def test_direct_start_requires_closed_previous_cycle(self):
        self.state['cycles'][0].update(state='ACTIF', closed_at=None, closure=None)
        with self.assertRaisesRegex(C.CycleError, 'non clôturé'):
            self.guard()

    def test_cycle2_mode_cannot_be_rewritten_after_closure(self):
        cycle2 = self.state['cycles'][0]
        cycle2.update(mode=G.DIRECT_MODE, authority=G.DIRECT_AUTHORITY, authority_sha256=self.cycle3['authority_sha256'])
        with self.assertRaisesRegex(C.CycleError, 'indépendance|mode'):
            self.guard()
        self.assertFalse(G.direct({'cycle': 2}))


class DirectChainCycle2Tests(ClaudeFixture, unittest.TestCase):
    def test_cycle2_control_without_cross_audits_rejected(self):
        row = self.state['cycles'][0]['chapters'][0]
        row.update(status='EN_CONTROLE', author={'path': 'x'})
        with patch.object(G, 'temporal_proofs'), patch.object(N, 'journal_proof'), \
                self.assertRaisesRegex(C.CycleError, 'quatre auteurs|audits croisés'):
            self.guard()


class Cycle2DirectFixture(DirectFixture):
    """Cycle 2 repris, passé une seule fois en publication directe (clôture immédiate demandée par Vial)."""
    author_default = G.PROMPTS

    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.files = {p: (root / p).read_bytes() for p in {G.AUTHORITY, G.PLAN, G.CAHIER, *G.PROMPTS, *G.PROMPTS_DIRECT}}
        self.files[N.REGISTRY] = encode({'cycles': [{'cycle': 2, 'owner': 'Codex', 'state': 'ACTIF'}]})
        self.files['transmission/manifeste.json'] = encode({'cycle': 2, 'fixture': 'technique'})
        self.files['chapters.json'] = b'[]\n'
        self.files['preuves/evidence.txt'] = b'Fixture technique non clinique'
        self.events = [dict(event='cycle_started', cycle=2, at=START, coordinator_runtime='fixture')]
        self.cycle3 = dict(cycle=2, owner='Claude', state='ACTIF', started_at=START, transferred_from='Codex',
                           handover=self.ref('transmission/manifeste.json'), cross_phase=None, closed_at=None,
                           closure=None, budget=None, chapters=rows_for(Tree(self.files), 2))
        self.state = dict(schema_version=1, authority=G.AUTHORITY, authority_sha256=C.digest(self.files[G.AUTHORITY]),
                          plan_sha256=C.digest(self.files[G.PLAN]), coordinator=G.COORDINATOR, not_before=G.NOT_BEFORE,
                          cycles=[self.cycle3])
        self.snapshot()
        self.complete = self.before
        self.switch()
        self.snapshot()

    def switch(self, event=True):
        sha = C.digest(self.files[G.DIRECT_AUTHORITY])
        self.cycle3.update(mode=G.DIRECT_MODE, authority=G.DIRECT_AUTHORITY, authority_sha256=sha)
        for row in self.rows:
            row['cross_reviewer'] = row['counter_reviewer'] = None
        if event:
            self.events.append(dict(event='mode_changed', cycle=2, mode=G.DIRECT_MODE, authority=G.DIRECT_AUTHORITY,
                                    authority_sha256=sha, coordinator_runtime='fixture', at=T('21:30')))


class Cycle2DirectTests(Cycle2DirectFixture, unittest.TestCase):
    def test_mode_change_accepted_once_with_journal(self):
        self.before = self.complete
        self.assertEqual(self.guard()[0], {})

    def test_mode_change_without_journal_rejected(self):
        self.before = self.complete
        self.events = [e for e in self.events if e['event'] != 'mode_changed']
        with self.assertRaisesRegex(C.CycleError, 'journal'):
            self.guard()

    def test_mode_change_with_other_transition_rejected(self):
        self.before = self.complete
        self.produce(0)
        with self.assertRaisesRegex(C.CycleError, 'simultané'):
            self.guard()

    def test_mode_change_after_reviews_started_rejected(self):
        state = json.loads(self.complete.files[G.REGISTRY])
        state['cycles'][0]['chapters'][0].update(status='EN_AUDIT_CROISE', author={'path': 'preuves/evidence.txt', 'sha256': 'x'})
        files = dict(self.complete.files); files[G.REGISTRY] = encode(state)
        self.before = Tree(files)
        with self.assertRaisesRegex(C.CycleError, 'début des revues'):
            self.guard()

    def test_mode_cannot_be_reverted_or_keep_reviewers(self):
        for action in ('revert', 'cross', 'counter'):
            self.setUp()
            if action == 'revert':
                for k in ('mode', 'authority', 'authority_sha256'):
                    self.cycle3.pop(k)
            else:
                self.rows[0][action + '_reviewer'] = 'C02-R-HEM'
            with self.subTest(action=action), self.assertRaises(C.CycleError):
                self.guard()

    def test_activation_with_mode_rejected(self):
        old = copy.deepcopy(self.files); old.pop(G.REGISTRY); old.pop(G.JOURNAL)
        self.save()
        with self.assertRaisesRegex(C.CycleError, 'activation'):
            G.validate(Tree(old), Tree(self.files), now=NOW)

    def test_direct_injection_with_cahier_images_accepted(self):
        self.ready_cycle(); self.inject(0)
        authorized, codes, catalog = self.guard()
        self.assertEqual(catalog, {'G45'})
        self.assertEqual(sum(p.startswith('assets/img/cycle2/g45/') for p in authorized), 9)
        entry = json.loads(self.files['chapters.json'])[0]
        self.assertEqual((entry['audit_deferred'], entry['production_cycle']), (G.DIRECT_DEFERRED, 2))

    def test_missing_cahier_image_rejected(self):
        self.produce(0)
        manifest = json.loads(self.files['preuves/g45-images.json']); manifest['images'].pop()
        self.rows[0]['images'] = self.write('preuves/g45-images.json', manifest)
        self.events.append(self.event(2, self.rows[0]))
        with self.assertRaisesRegex(C.CycleError, 'cahier'):
            self.guard()

    def test_fictitious_cross_or_counter_audit_rejected(self):
        for key, status in (('cross_audit', None), ('counter_audit', None), (None, 'EN_AUDIT_CROISE')):
            self.setUp(); self.produce(0)
            row = self.rows[0]
            if key: row[key] = row['author']
            else: row['status'] = status
            self.events.append(self.event(2, row))
            with self.subTest(key=key, status=status), self.assertRaisesRegex(C.CycleError, 'fictif'):
                self.guard()

    def test_three_captures_rejected(self):
        self.produce(0, captures=3)
        with self.assertRaisesRegex(C.CycleError, '4 captures'):
            self.guard()

    def test_catalogue_without_deferred_audit_rejected(self):
        self.ready_cycle(); self.inject(0, catalog_extra={'audit_deferred': None})
        with self.assertRaisesRegex(C.CycleError, 'audit différé'):
            self.guard()

    def test_only_cycle2_can_switch(self):
        self.assertEqual(G.SWITCH_CYCLES, (2,))
        self.assertNotIn(2, G.DIRECT_CYCLES)


class GateAndControlToolTests(unittest.TestCase):
    def test_gate_prompt_sets_match_guard(self):
        from tools import claude_cycle_gate as gate
        self.assertEqual(gate.PROMPT_SETS['direct'], G.PROMPTS_DIRECT)
        self.assertEqual(gate.PROMPT_SETS['reprise'], G.PROMPTS)
        entries = [(c, 'PROMPT_MEDINA.md', 'Fixture') for c in gate.CHECKS]
        made = gate.make_gate(G.COORDINATOR, entries, 'direct')
        self.assertEqual(set(made['prompt_files']), set(G.PROMPTS_DIRECT))
        with self.assertRaises(ValueError):
            gate.make_gate(G.COORDINATOR, entries[:-1], 'direct')

    def test_control_tool_requires_four_capture_kinds(self):
        from tools import cycle_claude_control as tool
        self.assertEqual(len(tool.CAPTURE_KINDS), G.CAPTURES)
        self.assertEqual(tool.VIEWPORTS['desktop']['width'], 1440)
        self.assertEqual(tool.VIEWPORTS['mobile']['width'], 390)


class NightPreviewRootsTests(unittest.TestCase):
    def test_claude_delivery_allowed_from_cycle3_only(self):
        from tools import night_preview as preview
        root = Path(__file__).resolve().parents[1]
        claude = root / 'livraisons/Livraison Claude/N-05-Neurologie/travail/CYCLE_03_I61'
        codex = root / 'livraisons/Livraison Codex/N-05-Neurologie/travail/CYCLE_02_G45'
        self.assertTrue(preview.allowed_source(root, claude, 3, 'I61'))
        self.assertFalse(preview.allowed_source(root, claude.with_name('CYCLE_02_G45'), 2, 'G45'))
        self.assertTrue(preview.allowed_source(root, codex, 2, 'G45'))
        self.assertFalse(preview.allowed_source(root, root / 'docs/CYCLE_03_I61', 3, 'I61'))
        self.assertFalse(preview.allowed_source(root, claude, 3, 'E05'))


class Cycle2AuthorPromptsTests(Cycle2DirectFixture, unittest.TestCase):
    def test_cycle2_author_uses_reprise_prompts_and_control_direct(self):
        self.assertEqual(G.author_prompts({'production_cycle': 2}), G.PROMPTS)
        self.assertEqual(G.author_prompts({'production_cycle': 3}), G.PROMPTS_DIRECT)
        self.ready_cycle(); self.inject(0)
        self.assertEqual(self.guard()[2], {'G45'})

    def test_cycle2_author_with_direct_prompts_rejected(self):
        self.produce(0, prompts=G.PROMPTS_DIRECT)
        with self.assertRaisesRegex(C.CycleError, 'Prompt'):
            self.guard()

    def test_cycle2_control_with_reprise_prompts_rejected(self):
        self.prompts = G.PROMPTS
        self.produce(0, prompts=G.PROMPTS)
        with self.assertRaisesRegex(C.CycleError, 'contrôle|control|Prompt'):
            self.guard()

    def test_cycle3_author_with_reprise_prompts_still_rejected(self):
        self.assertNotEqual(G.author_prompts({'production_cycle': 3}), G.PROMPTS)
