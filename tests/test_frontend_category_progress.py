"""Original category progress counts canonical lessons, independently of views."""
import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nosologyEngine import category_progress


def lesson(code, filled=False, federal=False, block='OTHER'):
    return {'id': code, 'code': code, 'state': 'filled' if filled else 'empty',
            'gold_star': {'enabled': federal}, 'block': block}


class CategoryProgressTests(unittest.TestCase):
    def test_shared_course_uses_displayed_membership_and_counts_once_per_category(self):
        inventory = {item['code']: item for item in (
            lesson('I34', filled=True, federal=True, block='I30-I52'),
            lesson('I35', federal=True, block='I30-I52'),
            lesson('I99', filled=True),
            lesson('I34.0', filled=True, federal=True),
        )}
        first = {'code': 'I05-I09', 'lessons': [
            {'code': 'I34', 'variants': [{'code': 'I05'}]},
            {'code': 'I34', 'variants': [{'code': 'I09'}]},
            {'code': 'I35'}, {'code': 'I99'}, {'code': 'I34.0'},
        ]}
        second = {'code': 'I30-I52', 'lessons': [{'code': 'I34'}]}
        before = copy.deepcopy((inventory, first, second))
        self.assertEqual(category_progress(first, inventory), {
            'federal_exam': {'filled': 1, 'total': 2, 'percent': 50.0},
            'global': {'filled': 2, 'total': 3, 'percent': 66.67},
        })
        self.assertEqual(category_progress(second, inventory), {
            'federal_exam': {'filled': 1, 'total': 1, 'percent': 100.0},
            'global': {'filled': 1, 'total': 1, 'percent': 100.0},
        })
        self.assertEqual((inventory, first, second), before)

    def test_available_display_does_not_replace_filled_inventory_state(self):
        block = {'code': 'B00-B09', 'lessons': [{'code': 'B01', 'integrated': True}]}
        inventory = {'B01': lesson('B01')}
        self.assertEqual(category_progress(block, inventory), {
            'federal_exam': {'filled': 0, 'total': 0, 'percent': 0},
            'global': {'filled': 0, 'total': 1, 'percent': 0.0},
        })
        self.assertEqual(category_progress({'code': 'EMPTY', 'lessons': []}, {}), {
            'federal_exam': {'filled': 0, 'total': 0, 'percent': 0},
            'global': {'filled': 0, 'total': 0, 'percent': 0},
        })

    def test_missing_canonical_course_is_explicit_instead_of_reducing_denominator(self):
        block = {'code': 'I30-I52', 'lessons': [{'code': 'I34'}, {'code': 'I50'}]}
        with self.assertRaisesRegex(ValueError, 'I30-I52.*I50'):
            category_progress(block, {'I34': lesson('I34', True, True)})


if __name__ == '__main__':
    unittest.main()
