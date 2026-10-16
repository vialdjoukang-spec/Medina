"""Noms d’affichage des catégories : couverture réelle, concision, sigles, idempotence."""
import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('noms_categories', ROOT / 'noms_categories.py')
NAMES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NAMES)


class NomsCategoriesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = NAMES.load_names()
        cls.inventory = NAMES.inventory(ROOT)

    def organisation(self, fid):
        return {'fragment': {'id': fid}, 'blocks': [
            {'code': code, 'id': code, 'title': block['title'], 'order': index,
             'lessons': [{'code': code_, 'title': title} for code_, title in block['lessons']]}
            for index, (code, block) in enumerate(self.inventory[fid].items(), 1)]}

    def test_every_real_block_is_named_or_explicitly_kept(self):
        self.assertEqual(set(self.table['fragments']), set(self.inventory))
        for fid, blocks in self.inventory.items():
            with self.subTest(fragment=fid):
                self.assertEqual(set(self.table['fragments'][fid]), set(blocks))
                for code, entry in self.table['fragments'][fid].items():
                    self.assertEqual(entry['official_title'], blocks[code]['title'])
                    self.assertEqual(entry['kept'], entry['display_title'] == entry['official_title'])
                    self.assertTrue(entry['rationale'].strip())

    def test_names_are_concise_unique_and_free_of_undefined_abbreviations(self):
        known = set(self.table['abbreviations'])
        for fid, blocks in self.table['fragments'].items():
            titles = [entry['display_title'].casefold() for entry in blocks.values()]
            self.assertEqual(len(titles), len(set(titles)), fid + ' : doublon de nom')
            for code, entry in blocks.items():
                with self.subTest(fragment=fid, block=code):
                    self.assertLessEqual(len(entry['display_title']), NAMES.MAX_LENGTH)
                    self.assertEqual(entry['display_title'], entry['display_title'].strip())
                    self.assertTrue(entry['display_title'][:1].isupper())
                    self.assertFalse(NAMES.abbreviations_in(entry['display_title'] + ' ' + entry['rationale']) - known)
        for key, definition in self.table['abbreviations'].items():
            self.assertTrue(definition.strip(), key)

    def test_abbreviation_detector_ignores_codes_and_eponyms(self):
        self.assertEqual(NAMES.abbreviations_in('Infection par le VIH, U07.1-U12, Gougerot-Sjögren'), {'VIH'})

    def test_apply_is_pure_idempotent_and_preserves_lessons(self):
        for fid in self.inventory:
            with self.subTest(fragment=fid):
                source = self.organisation(fid)
                before = copy.deepcopy(source)
                once = NAMES.apply_category_names(source)
                self.assertEqual(source, before)
                self.assertEqual(NAMES.apply_category_names(once), once)
                for original, block in zip(before['blocks'], once['blocks']):
                    entry = self.table['fragments'][fid][original['code']]
                    self.assertEqual(block['title'], entry['display_title'])
                    self.assertEqual(block['official_title'], original['title'])
                    self.assertEqual(block['lessons'], original['lessons'])
                    self.assertEqual({k: v for k, v in block.items() if k not in ('title', 'official_title')},
                                     {k: v for k, v in original.items() if k != 'title'})

    def test_unknown_block_or_fragment_is_left_untouched(self):
        organisation = {'fragment': {'id': 'S02'}, 'blocks': [{'code': 'X00-X00', 'title': 'Inconnu', 'lessons': []}]}
        self.assertEqual(NAMES.apply_category_names(organisation), organisation)
        organisation = {'fragment': {'id': 'ZZ'}, 'blocks': [{'code': 'J40-J47', 'title': 'Titre', 'lessons': []}]}
        self.assertEqual(NAMES.apply_category_names(organisation), organisation)

    def test_global_check_is_clean(self):
        self.assertEqual(NAMES.check(ROOT), [])


if __name__ == '__main__':
    unittest.main()
