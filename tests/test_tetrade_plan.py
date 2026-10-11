"""Contrat de la planification ; aucune validation clinique implicite."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TetradePlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'organisation/progression/plan-tetrade-30-cycles.json').read_text())

    def test_tetrade_received_in_image_and_exact_allocation(self):
        cycles = self.data['cycles']
        self.assertEqual(len(cycles), 30)
        expected = {'S08', 'S05', 'S04', 'S06'}
        for i, cycle in enumerate(cycles, 1):
            self.assertEqual(cycle['number'], i)
            self.assertEqual(len(cycle['chapters']), 4)
            self.assertEqual({c['fragment'] for c in cycle['chapters']}, expected)
        all_chapters = [ch for c in cycles for ch in c['chapters']]
        self.assertEqual(len({c['code'] for c in all_chapters}), 120)
        self.assertEqual(len({c['author'] for c in all_chapters}), 120)
        authors = {c['author'] for c in all_chapters}
        for c in all_chapters:
            self.assertNotEqual(c['author'], c['auditor'])
            self.assertNotIn(c['counter'], authors)

    def test_exhaustive_inventory_distinguishes_planned_and_remaining(self):
        inventory = self.data['inventories']
        self.assertEqual([len(i['rows']) for i in inventory], [116, 77, 33, 44])
        rows = [r for i in inventory for r in i['rows']]
        self.assertEqual(len({r['code'] for r in rows}), 270)
        self.assertEqual(sum(r['cycle'] is not None for r in rows), 120)
        self.assertEqual(sum(r['cycle'] is None for r in rows), 150)

    def test_frequent_selection_fully_planned_and_brouillons_preserved(self):
        summary = self.data['summaries']
        self.assertEqual(sum(s['freq_total'] for s in summary), 21)
        self.assertEqual(sum(s['freq_new'] for s in summary), 21)
        self.assertEqual(sum(s['federal_new'] for s in summary), 117)
        self.assertEqual(sum(s['present'] for s in summary), 0)
        chapters = [ch for cycle in self.data['cycles'] for ch in cycle['chapters']]
        drafts = {ch['code']: ch['drafts'] for ch in chapters if ch['drafts']}
        self.assertEqual(set(drafts), {'E11', 'D50'})
        for paths in drafts.values():
            self.assertTrue(all((ROOT / p).is_file() for p in paths))

    def test_initial_plan_has_no_production_or_validation_claim(self):
        self.assertEqual(self.data['plan']['state'], 'PLANIFIE_NON_DEMARRE')
        self.assertEqual(len(self.data['stages']), 8)
        self.assertEqual(len(self.data['gates']), 4)
        page = (ROOT / 'organisation/progression/plan-tetrade-30-cycles.html').read_text()
        self.assertIn('height:0.5cm', page)
        self.assertIn('Atkinson Hyperlegible Next', page)
        self.assertNotIn('data-stage="injected" checked', page)
        self.assertIn('Aucun texte médical futur n’est présumé lu', page)


if __name__ == '__main__':
    unittest.main()
