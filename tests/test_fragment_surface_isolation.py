"""Frontend isolation against the actual catalogue, without medical source edits."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('fragment_surface', ROOT / 'fragment_surface.py')
SURFACE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SURFACE)


class FragmentSurfaceIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full, cls.owners, cls.courses = SURFACE.frontend_catalog(ROOT)
        cls.fragments = json.loads((ROOT / 'fragments.json').read_text())
        names = {name['id']: name for name in json.loads((ROOT / 'organisation/fragments.json').read_text())}
        for fragment in cls.fragments:
            fragment['nom'] = names[fragment['id']]['label']
            fragment['production_order'] = names[fragment['id']]['order']

    def fragment(self, ident):
        return next(fragment for fragment in self.fragments if fragment['id'] == ident)

    def source(self, fragment):
        # Deliberately start with the entire atlas catalogue, even for the empty
        # transversal frontends: finish_surface itself must enforce the boundary.
        data = copy.deepcopy(self.full)
        data['fragment'] = {'id': fragment['id'], 'name': fragment['nom'], 'systems': []}
        courses = SURFACE.fragment_chapters(fragment, self.full['entries'], ROOT)
        templates = ''.join('<template id="ch-' + course['code'] + '"><p>Fixture technique</p></template>' for course in courses)
        return ('<html lang="fr"><head><title>Medina · Atlas médical</title>'
                '<script id="medora-data" type="application/json">' + json.dumps(data) + '</script>'
                '<script>window.MEDINA_ALIAS=' + json.dumps({code: course['code'] for course in self.courses.values() for code in course['covers']}) + '</script>'
                '<script>window.MEDINA_COMPLETE=[];</script>'
                '<script>window.MEDINA_FRAGMENT_SIDEBAR=[];</script></head><body>'
                '<nav class="nav-main"><a href="#/home">Accueil</a></nav>'
                '<div class="sidebar-note">Ancien compte</div>' + templates +
                '<script id="medina-glossary" type="application/json">{}</script></body></html>')

    def catalogue(self, source, identifier):
        return json.loads(re.search(r'<script id="' + identifier + r'"[^>]*>(.*?)</script>', source, re.S).group(1))

    def test_infection_entries_do_not_follow_old_anatomical_misclassification(self):
        infectious = {entry['code'] for entry in SURFACE.frontend_entries(self.fragment('T1'), self.full['entries'], ROOT)}
        cardiac = {entry['code'] for entry in SURFACE.frontend_entries(self.fragment('S01'), self.full['entries'], ROOT)}
        digestive = {entry['code'] for entry in SURFACE.frontend_entries(self.fragment('S03'), self.full['entries'], ROOT)}
        self.assertTrue({'A43', 'B18', 'A04'}.issubset(infectious))
        self.assertNotIn('A43', cardiac)
        self.assertTrue({'A04', 'B18'}.isdisjoint(digestive))

    def test_each_category_has_one_frontend_owner_and_grouped_courses_stay_local(self):
        seen = set()
        for fragment in self.fragments:
            codes = {entry['code'] for entry in SURFACE.frontend_entries(fragment, self.full['entries'], ROOT)}
            self.assertTrue(seen.isdisjoint(codes))
            seen.update(codes)
            for course in SURFACE.fragment_chapters(fragment, self.full['entries'], ROOT):
                self.assertEqual(course['source_fragment_id'], fragment['id'])
                self.assertTrue(set(course['covers']).issubset(codes))
        self.assertEqual(seen, {entry['code'] for entry in self.full['entries']})

    def test_all_22_finish_surfaces_remove_foreign_catalogues_and_templates(self):
        for fragment in self.fragments:
            with self.subTest(fragment=fragment['id']):
                source = SURFACE.finish_surface(self.source(fragment), fragment, ROOT)
                data = self.catalogue(source, 'medora-data')
                organised = self.catalogue(source, 'medina-category-organisation-data')
                expected = {entry['code'] for entry in SURFACE.frontend_entries(fragment, self.full['entries'], ROOT)}
                self.assertEqual({entry['code'] for entry in data['entries']}, expected)
                self.assertEqual(len(data['specialties']), 1)
                self.assertEqual(data['ssps'], [])
                self.assertEqual(data['profiles'], {})
                self.assertEqual(data['focus'], {})
                for field in ('specialties', 'families', 'references', 'learningTopics', 'profilesGroups', 'systemSchema', 'coverageAudit'):
                    self.assertFalse(data['legacy'][field])
                own_courses = {course['code'] for course in SURFACE.fragment_chapters(fragment, self.full['entries'], ROOT)}
                self.assertEqual(set(re.findall(r'<template id="ch-([^"]+)"', source)), own_courses)
                self.assertEqual(organised['integrated_count'], len(own_courses))
                self.assertEqual({course['code'] for course in organised['courses']}, own_courses)
                for block in organised['blocks']:
                    for lesson in block['lessons']:
                        self.assertEqual(lesson['source_fragment_id'], fragment['id'])
                        self.assertEqual(lesson['url'], '#/entry/' + lesson['code'])
                        self.assertTrue({variant['code'] for variant in lesson['variants']}.issubset(expected))
                self.assertEqual(organised['fragment']['display_name'], SURFACE.presentation(fragment, ROOT)['specialty'])
                self.assertNotRegex(organised['fragment']['display_name'], r'^[A-Z]-\d{2}-')
                self.assertRegex(organised['fragment']['accent'], r'^#[0-9a-f]{6}$')

    def test_foreign_chapter_or_prefixed_popup_fails_the_final_boundary(self):
        fragment = self.fragment('T1')
        source = self.source(fragment)
        for injected in ('<template id="ch-I50">CONTENU CARDIOLOGIQUE ÉTRANGER</template>',
                         '<template data-pop="i50-fenetre">FENÊTRE ÉTRANGÈRE</template>'):
            with self.subTest(template=injected[:35]):
                with self.assertRaisesRegex(ValueError, 'hors périmètre|étrangers'):
                    SURFACE.finish_surface(source.replace('</body>', injected + '</body>'), fragment, ROOT)

    def test_foreign_alias_is_removed_even_if_present_in_input(self):
        fragment = self.fragment('T1')
        source = SURFACE.finish_surface(self.source(fragment), fragment, ROOT)
        aliases = json.loads(re.search(r'window\.MEDINA_ALIAS=(.*?)(?:;)?</script>', source).group(1))
        # Attendu : les seuls cours canoniques de T1 et leurs catégories couvertes.
        expected = {code: course['code']
                    for course in SURFACE.fragment_chapters(fragment, self.full['entries'], ROOT)
                    for code in set(course['covers']) | {course['code']}}
        self.assertEqual(aliases, expected)
        self.assertIn('A41', aliases)
        self.assertNotIn('I50', aliases)

    def test_glossary_preserves_local_window_and_definition_dependencies(self):
        glossary = {
            'LOCAL': {'lit': [['L', 'Local']], 'full': 'Terme DEP', 'def': '<p>Définition de fixture</p>', 'ref': 'a41-local'},
            'DEP': {'lit': [], 'full': 'Dépendance', 'def': '<p>Définition de fixture</p>', 'ref': 'i50-autre'},
            'FOREIGN': {'lit': [], 'full': 'Autre spécialité', 'def': '<span data-ab="FOREIGN">FOREIGN</span>', 'ref': 'i50-autre'},
        }
        source = ('<template id="ch-A41"><span data-ab="LOCAL">LOCAL</span></template>'
                  '<template data-pop="a41-local"><p>Fenêtre propre</p></template>'
                  '<script id="medina-glossary" type="application/json">' + json.dumps(glossary) + '</script>')
        sliced = SURFACE.isolated_glossary(source, glossary)
        self.assertEqual(set(sliced), {'LOCAL', 'DEP'})
        self.assertEqual(sliced['LOCAL']['ref'], 'a41-local')
        self.assertIsNone(sliced['DEP']['ref'])
        self.assertEqual(glossary['DEP']['ref'], 'i50-autre')


if __name__ == '__main__':
    unittest.main()
