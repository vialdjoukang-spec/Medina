"""Reference coverage, honest progress, deduplication and immutable originals."""
import copy
import csv
import io
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from nosologyEngine import BASE_PLAN, gauges, generate, progress, read_json, reference, sha256


class NosologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ref = reference(str(ROOT))

    def test_ofs_archive_hashes_and_exact_csv_code_inventory(self):
        for key, name in [('csv', 'ofs-cim10gm2024-fr-csv.zip'), ('claml', 'ofs-cim10gm2024-fr-claml.zip'), ('profiles', 'profiles2017.pdf')]:
            self.assertEqual(sha256(ROOT / 'nosology/sources' / name), self.ref['sources'][key]['sha256'])
        with zipfile.ZipFile(ROOT / 'nosology/sources/ofs-cim10gm2024-fr-csv.zip') as archive:
            data = archive.read(next(name for name in archive.namelist() if '_codes_' in name)).decode('utf-8-sig')
        rows = list(csv.reader(io.StringIO(data), delimiter=';'))
        self.assertEqual({row[6] for row in rows}, {item['code'] for item in self.ref['entities']})
        self.assertEqual(len(rows), len(self.ref['entities']))
        titles = {row[6]: row[8] for row in rows}
        for item in self.ref['entities']:
            self.assertEqual(item['title'], titles[item['code']])

    def test_file_loaded_surface_resolves_sibling_engine_in_isolated_process(self):
        script = '''import importlib.util, sys
from pathlib import Path
root = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location('isolated_surface', root / 'fragment_surface.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
data, owners, courses = module.frontend_catalog(root)
assert len(data['entries']) == 1636
assert len(owners) == 1636
'''
        with tempfile.TemporaryDirectory() as cwd:
            result = subprocess.run([sys.executable, '-I', '-c', script, str(ROOT)], cwd=cwd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_every_active_category_has_one_owner_and_exact_chapter_and_block(self):
        active = [item for item in self.ref['entities'] if not item['excluded']]
        categories = {item['code'] for item in active if len(item['code']) == 3}
        self.assertEqual(categories, set(self.ref['mapping']))
        self.assertEqual(len(categories), 1636)
        self.assertEqual(len(active), 15835)
        self.assertEqual(len(self.ref['chapters']), 22)
        fragments = {item['id'] for item in read_json(ROOT / 'organisation/fragments.json')}
        for item in active:
            self.assertIn(item['chapter'], self.ref['chapters'])
            self.assertIn(item['block'], self.ref['blocks'])
            self.assertIn(self.ref['mapping'][item['code'][:3]]['fragment'], fragments)

    def test_subcategory_and_multiple_versions_are_not_rewritten(self):
        for name, digest in read_json(ROOT / 'nosology/integrity.json').items():
            self.assertTrue((ROOT / name).is_file(), name)
            self.assertEqual(sha256(ROOT / name), digest, name)
        for path in (ROOT / 'nosology/fragments').glob('*.json'):
            inventory = read_json(path)
            for course in inventory.get('preserved_courses', []):
                for name in course['versions']:
                    self.assertIn(name, read_json(ROOT / 'nosology/integrity.json'))

    def test_existing_course_aliases_deduplicate_without_filling_empty_children(self):
        course = {'code': 'I25', 'title': 'Titre existant conservé', 'covers': ['I20', 'I25'], 'has_content': True}
        result = generate(['I20', 'I25', 'I20.0', 'I20.0'], 'S01', ROOT, {'I25': course})
        self.assertEqual([item['code'] for item in result['lessons']], ['I20.0', 'I25'])
        self.assertEqual(result['progress'], {'filled': 1, 'total': 2, 'percent': 50.0})
        self.assertEqual(result['lessons'][1]['title'], course['title'])
        self.assertEqual(result['lessons'][0]['state'], 'empty')

    def test_generated_shells_are_empty_with_adaptive_plan_and_fixed_stars(self):
        result = generate(['I20.0'], 'S01', ROOT)
        lesson = result['lessons'][0]
        self.assertEqual(tuple(section['title'] for section in lesson['plan'][:8]), BASE_PLAN)
        self.assertTrue(all(section['content'] == '' for section in lesson['plan']))
        self.assertEqual(result['progress']['filled'], 0)
        self.assertTrue(lesson['gold_star']['permanent'])
        self.assertTrue(lesson['gold_star']['enabled'])
        self.assertFalse(lesson['gold_star']['official_icd_crosswalk'])

    def test_partial_rerun_preserves_authored_shells_and_other_records(self):
        previous = generate(['I20.0', 'I20.1'], 'S01', ROOT)
        for section in previous['lessons'][0]['plan']:
            section['content'] = 'Contenu de test préexistant'
        previous['lessons'][0]['notes'] = 'Version préexistante'
        baseline = copy.deepcopy(previous)
        result = generate(['I20.0'], 'S01', ROOT, previous=previous)
        self.assertEqual(previous, baseline)
        self.assertEqual(result['lessons'][0]['plan'], previous['lessons'][0]['plan'])
        self.assertEqual(result['lessons'][0]['notes'], 'Version préexistante')
        self.assertEqual(len(result['lessons']), 2)
        self.assertEqual(result['progress']['filled'], 1)

    def test_unknown_foreign_psychological_and_reserved_codes_are_rejected(self):
        result = generate(['FAKE', 'F20', 'U13', 'U63', 'J45'], 'S01', ROOT)
        self.assertEqual(len(result['unattached']), 5)
        self.assertEqual(result['progress']['total'], 0)

    def test_inventories_represent_each_code_once_without_alias_duplication(self):
        seen, lesson_ids = set(), set()
        for path in (ROOT / 'nosology/fragments').glob('*.json'):
            inventory = read_json(path)
            self.assertEqual(inventory['progress'], progress(inventory['lessons']))
            for lesson in inventory['lessons']:
                self.assertNotIn(lesson['id'], lesson_ids)
                lesson_ids.add(lesson['id'])
                self.assertEqual(lesson['fragment'], inventory['fragment'])
                self.assertTrue(lesson['gold_star']['permanent'])
                for code in lesson['icd10gm']['codes']:
                    self.assertNotIn(code, seen)
                    seen.add(code)
                    self.assertEqual(self.ref['mapping'][code[:3]]['fragment'], inventory['fragment'])
                if not lesson['existing_course']:
                    self.assertTrue(all(section['content'] == '' for section in lesson['plan']))
        state = read_json(ROOT / 'nosology/queue.json')
        if all(value == 'completed' for value in state.values()):
            self.assertEqual(seen, {item['code'] for item in self.ref['entities'] if not item['excluded']})
            self.assertEqual(len(state), 22)
            self.assertNotIn('- [ ]', (ROOT / 'QUEUE.md').read_text())

    def test_progress_does_not_count_duplicated_or_empty_lessons_as_filled(self):
        lessons = [{'id': 'a', 'state': 'filled'}, {'id': 'b', 'state': 'empty'}, {'id': 'a', 'state': 'filled'}]
        self.assertEqual(progress(lessons), {'filled': 1, 'total': 2, 'percent': 50.0})

    def test_three_gauges_keep_frequency_exam_and_global_separate(self):
        course = {'code': 'I25', 'title': 'Cours', 'covers': ['I20', 'I25'], 'has_content': True}
        result = generate(['I20', 'I25', 'I20.0', 'I99'], 'S01', ROOT, {'I25': course})
        stats = gauges(result['lessons'], ['I20'])
        self.assertEqual(stats['frequent'], {'filled': 1, 'total': 1, 'percent': 100.0})
        # Les sous-codes (I20.0) ne comptent pas : les cours sont rédigés par catégorie.
        self.assertEqual(stats['federal_exam'], {'filled': 1, 'total': 1, 'percent': 100.0})
        self.assertEqual(stats['global'], {'filled': 1, 'total': 2, 'percent': 50.0})
        self.assertEqual(gauges([], [])['frequent'], {'filled': 0, 'total': 0, 'percent': 0})


if __name__ == '__main__': unittest.main()
