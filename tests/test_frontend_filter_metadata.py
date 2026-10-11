"""Frontend filters use existing gauge membership without rewriting lessons."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nosologyEngine import attach_surface, category_selections, gauges


class FrontendFilterMetadataTests(unittest.TestCase):
    def test_alias_membership_and_empty_selections_preserve_input(self):
        lessons = [
            {'id': 'I25', 'code': 'I25', 'state': 'filled',
             'icd10gm': {'codes': ['I20', 'I25']}, 'gold_star': {'enabled': True}},
            {'id': 'I20.0', 'code': 'I20.0', 'state': 'empty',
             'icd10gm': {'codes': ['I20.0']}, 'gold_star': {'enabled': True}},
            {'id': 'I99', 'code': 'I99', 'state': 'empty',
             'icd10gm': {'codes': ['I99']}, 'gold_star': {'enabled': False}},
        ]
        before = copy.deepcopy(lessons)
        selected = category_selections(lessons, ['I20'])
        self.assertEqual([item['code'] for item in selected['frequent']], ['I25'])
        self.assertEqual([item['code'] for item in selected['federal_exam']], ['I25'])
        self.assertEqual(lessons, before)
        self.assertEqual(category_selections([], []),
                         {'frequent': [], 'federal_exam': [], 'global': []})

    def test_all_fragment_filters_match_existing_gauge_membership(self):
        frequency = set(json.loads((ROOT / 'nosology/frequency.json').read_text())['codes'])
        for path in sorted((ROOT / 'nosology/fragments').glob('*.json')):
            original_bytes = path.read_bytes()
            inventory = json.loads(original_bytes)
            categories = [lesson for lesson in inventory['lessons'] if '.' not in lesson['code']]
            expected = {
                'frequent': [lesson['code'] for lesson in categories
                             if frequency.intersection(lesson['icd10gm']['codes'])],
                'federal_exam': [lesson['code'] for lesson in categories
                                 if lesson['gold_star']['enabled']],
            }
            organisation = {'fragment': {'id': path.stem}, 'blocks': []}
            actual = attach_surface(organisation, ROOT)['nosology']
            with self.subTest(fragment=path.stem):
                self.assertEqual(actual['filters'], expected)
                self.assertEqual(actual['gauges'], gauges(inventory['lessons'], frequency))
                for key, codes in actual['filters'].items():
                    self.assertEqual(len(codes), actual['gauges'][key]['total'])
                    self.assertEqual(len(codes), len(set(codes)))
                self.assertEqual(actual['lessons'], inventory['lessons'])
                self.assertEqual(path.read_bytes(), original_bytes)


if __name__ == '__main__':
    unittest.main()
