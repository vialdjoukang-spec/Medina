"""Fixtures strictement techniques : aucune lecture clinique ou publication réelle simulée."""
import copy
from datetime import datetime, timedelta
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from tools import cycle_claude as G
from tools import novo_cycle as V
from tools import tetrade_cycle as C
from tools import night_cycle as N
from tests.test_tetrade_cycle import Tree, encode
from tests.test_cycle_claude import DirectFixture, T

NOW = datetime.fromisoformat('2026-10-15T02:00:00+00:00')


class NovoFixture(DirectFixture):
    def setUp(self):
        super().setUp()
        # Clôture technique de la fixture historique, sans changer son contrat.
        self.ready_cycle()
        for i in range(4):
            self.inject(i); self.guard(); self.snapshot()
            self.publish(i); self.guard(); self.snapshot()
        self.cycle3.update(state='CLOTURE', closed_at=T('22:40'),
                           closure=self.write('preuves/c3-cloture.json', {'cycle': 3, 'blocking_reserves': []}))
        self.guard(); self.snapshot()
        root = Path(__file__).resolve().parents[1]
        for p in (V.PLAN, V.AUTHORITY, V.TRUTH):
            self.files[p] = (root / p).read_bytes()
        cycles, missions = V.specification(Tree(self.files), 1)
        rows = [dict(code=code, fragment_id=fragment, production_cycle=n, novo=1,
                     writer=f'C{n:02d}-R-{tag}', cross_reviewer=None, counter_reviewer=None,
                     status='EN_PRODUCTION', source_dir=None, files={}, images=None,
                     **{key: None for key in G.PROOFS}) for code, fragment, tag, n in missions]
        self.cycle3 = dict(cycle=4, novo=1, tetrad_cycles=cycles, owner='Claude', state='ACTIF',
                          started_at=T('22:45'), closed_at=None, closure=None, budget=None,
                          mode=G.DIRECT_MODE, authority=G.DIRECT_AUTHORITY,
                          authority_sha256=C.digest(self.files[G.DIRECT_AUTHORITY]),
                          novo_plan_sha256=C.digest(self.files[V.PLAN]), novo_authority=V.AUTHORITY,
                          novo_authority_sha256=C.digest(self.files[V.AUTHORITY]),
                          transferred_from=None, handover=None, cross_phase=None, chapters=rows)
        self.state['cycles'].append(self.cycle3)
        self.events.append(dict(event='cycle_started', cycle=4, at=T('22:45'), coordinator_runtime='fixture'))
        self.prompts = G.PROMPTS_NOVO
        self.guard(now=NOW)
        self.snapshot()

    def event(self, n, row, at=T('22:30')):
        if row.get('novo'):
            n, at = 4, T('23:30')
        return super().event(n, row, at)

    def produce(self, i, **kwargs):
        if not self.rows[i].get('novo'):
            return super().produce(i, **kwargs)
        shifted = lambda clock: (datetime.fromisoformat(T(clock)) + timedelta(hours=1)).isoformat()
        with patch('tests.test_cycle_claude.T', side_effect=shifted):
            super().produce(i, **kwargs)
        row = self.rows[i]
        research = row['source_dir'] + '/recherche.md'
        text = '## Matrice de complétude\n| rubrique | statut | sources |\n|---|---|---|\n'
        text += ''.join(f'| {n}. Fixture {row["code"]}.0 | ✔ | [S1] |\n' for n in range(1, 21))
        self.files[research] = text.encode()
        sources = row['source_dir'] + '/sources.json'
        self.files[sources] = encode({'sources': [dict(id='S1', url='https://www.swissmedic.ch/', titre='Fixture',
            editeur='Fixture suisse', version_annee='2026', date_consultation='2026-10-14', section_page='Fixture')]})
        author = json.loads(self.files[row['author']['path']])
        for gate in ('entry', 'exit'):
            check = next(c for c in author[gate]['checks'] if c['id'] == 'sources_lues')
            check['evidence'] += [dict(path=p, sha256=C.digest(self.files[p]), explanation='Fixture technique')
                                  for p in (research, sources)]
        row['author'] = self.write(row['author']['path'], author)
        self.events.append(self.event(4, row))

    def inject(self, i, **kwargs):
        if not self.rows[i].get('novo'):
            return super().inject(i, **kwargs)
        with patch('tests.test_cycle_claude.T', side_effect=lambda clock:
                   (datetime.fromisoformat(T(clock)) + timedelta(hours=1)).isoformat()):
            super().inject(i, **kwargs)

    def publish(self, i):
        if not self.rows[i].get('novo'):
            return super().publish(i)
        with patch('tests.test_cycle_claude.T', side_effect=lambda clock:
                   (datetime.fromisoformat(T(clock)) + timedelta(hours=1)).isoformat()):
            super().publish(i)
        row = self.rows[i]
        pub = json.loads(self.files[row['publication']['path']])
        manifest = {'git_commit': pub['main_sha'], 'courses': {row['code']: {'source_files': row['files']}}}
        pub.update(site_manifest=self.write('preuves/public-manifest-' + row['code'] + '.json', manifest),
                   pages_run={'id': 123, 'head_sha': pub['main_sha'], 'conclusion': 'success'},
                   public_images_http_200=True, published_files=dict(row['files'], **{
                       im['path']: im['sha256'] for im in json.loads(self.files[row['images']['path']])['images']}))
        row['publication'] = self.write(row['publication']['path'], pub)
        self.events.append(self.event(4, row))

    def ready_novo(self):
        for i in range(12):
            self.produce(i)
        self.guard(now=NOW); self.snapshot()

    def checked(self):
        return self.guard(now=NOW)


class NovoTests(NovoFixture, unittest.TestCase):
    def test_plan_has_108_exact_assignments(self):
        codes = []
        for n in range(1, 10):
            cycles, rows = V.specification(Tree(self.files), n)
            self.assertEqual(len(cycles), 3); self.assertEqual(len(rows), 12)
            codes += [row[0] for row in rows]
        self.assertEqual(len(set(codes)), 108)

    def test_wrong_assignment_rejected(self):
        plan = json.loads(self.files[V.PLAN]); plan['cycles'][0]['systems'][0]['lessons'][0] = 'G45'
        self.files[V.PLAN] = encode(plan)
        with self.assertRaisesRegex(C.CycleError, 'attribution'):
            V.specification(Tree(self.files), 1)

    def test_two_other_subcycles_cannot_overlap_codex(self):
        for n in (5, 6):
            self.files[N.REGISTRY] = encode({'cycles': [{'cycle': n, 'owner': 'Codex'}]})
            with self.subTest(n=n), self.assertRaisesRegex(C.CycleError, 'attribué à Codex'):
                self.checked()

    def test_twelve_required_not_four(self):
        self.rows.pop()
        with self.assertRaisesRegex(C.CycleError, 'douze'):
            self.checked()

    def test_batch_twelve_injections_accepted(self):
        self.ready_novo()
        for i in range(12): self.inject(i)
        authorized, codes, catalogue = self.checked()
        self.assertEqual(len(codes), 20)  # 8 historiques + 12 nouvelles
        self.assertEqual(len(catalogue), 12)
        self.assertEqual(len(authorized), 97)  # 7 sources + 1 image par leçon, catalogue

    def test_preparation_date_common_to_three_subcycles(self):
        self.ready_novo()
        self.assertEqual({r['production_cycle'] for r in self.rows}, {4, 5, 6})
        self.checked()  # Le même départ 22:45 couvre honnêtement les trois.

    def test_actual_antidating_is_still_rejected(self):
        self.produce(8)
        row = self.rows[8]; author = json.loads(self.files[row['author']['path']])
        author['entry']['checked_at'] = T('22:40')
        row['author'] = self.write(row['author']['path'], author)
        self.events.append(self.event(4, row))
        with self.assertRaisesRegex(C.CycleError, 'antidatée'):
            self.checked()

    def test_all_twelve_must_be_ready(self):
        self.produce(0); self.snapshot(); self.inject(0)
        with self.assertRaisesRegex(C.CycleError, 'cours prêts'):
            self.checked()

    def test_hole_in_batch_is_rejected(self):
        self.ready_novo(); self.inject(0); self.inject(2)
        with self.assertRaisesRegex(C.CycleError, 'non consécutives'):
            self.checked()

    def test_next_prefix_does_not_wait_for_12_deployments(self):
        self.ready_novo(); self.inject(0); self.inject(1); self.checked(); self.snapshot()
        self.inject(2); self.checked()

    def test_added_extra_source_rejected(self):
        self.ready_novo(); self.inject(0)
        self.files['chapters/G40/G40_extra.html'] = b'Fixture non autorisee'
        with self.assertRaisesRegex(C.CycleError, 'supplémentaires'):
            self.checked()

    def test_no_duplicate_catalogue_code(self):
        self.ready_novo()
        self.files['chapters.json'] = encode([{'code': self.rows[0]['code'], 'integrated': False}])
        self.snapshot(); self.inject(0)
        with self.assertRaisesRegex(C.CycleError, 'déjà présent|dupliqué'):
            self.checked()

    def test_truth_prompt_and_research_must_be_frozen(self):
        self.produce(0); row = self.rows[0]
        self.files[row['source_dir'] + '/recherche.md'] += b'\nModification apres revue.'
        with self.assertRaises(C.CycleError): self.checked()

    def test_missing_truth_matrix_rejected(self):
        self.produce(0); row = self.rows[0]
        self.files[row['source_dir'] + '/recherche.md'] = b'Fixture incomplete'
        with self.assertRaises(C.CycleError): self.checked()

    def test_individual_publication_receipts_required(self):
        self.ready_novo()
        for i in range(12): self.inject(i)
        self.checked(); self.snapshot()
        for i in range(12): self.publish(i)
        self.checked()

    def test_publication_cannot_precede_injection(self):
        self.ready_novo(); self.inject(0); self.checked(); self.snapshot(); self.publish(0)
        row = self.rows[0]; pub = json.loads(self.files[row['publication']['path']])
        pub['checked_at'] = T('23:15')
        row['publication'] = self.write(row['publication']['path'], pub); self.events.append(self.event(4, row))
        with self.assertRaisesRegex(C.CycleError, 'antérieure à injection'):
            self.checked()

    def test_manifest_must_match_exact_published_sources(self):
        self.ready_novo(); self.inject(0); self.checked(); self.snapshot(); self.publish(0)
        row = self.rows[0]; pub = json.loads(self.files[row['publication']['path']])
        manifest = json.loads(self.files[pub['site_manifest']['path']]); manifest['courses'][row['code']]['source_files'] = {}
        pub['site_manifest'] = self.write(pub['site_manifest']['path'], manifest)
        row['publication'] = self.write(row['publication']['path'], pub); self.events.append(self.event(4, row))
        with self.assertRaisesRegex(C.CycleError, 'sources publiées'):
            self.checked()

    def test_closed_historical_sources_unchanged(self):
        self.files['chapters/I61/I61_a.html'] = b'Modification historique interdite'
        with self.assertRaises(C.CycleError): self.checked()


if __name__ == '__main__':
    unittest.main()
