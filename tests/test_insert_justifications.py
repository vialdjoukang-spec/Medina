#!/usr/bin/env python3
"""Contrôles des cibles exactes ; aucune certification du contenu médical."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from insert_justifications import JustificationError, compile_bank, load_course_justifications


def bank(text='Anémie', anchor='bilan'):
    return {'version': 1, 'course': {'code': 'I50', 'title': 'Insuffisance cardiaque'},
            'entries': [{'id': 'i50-j-anemie', 'title': 'Pourquoi rechercher une anémie ?',
                         'match': [{'file': 'I50_c.html', 'anchor': anchor, 'text': text}],
                         'explanation': ['Explication <test> & contexte.'],
                         'mechanism': ['Première étape.', 'Deuxième étape.'],
                         'implication': 'Conséquence clinique.', 'limits': ['Limite du contexte.'],
                         'sources': [{'title': 'Source primaire', 'url': 'https://example.org/source'}]}]}


class JustificationTargets(unittest.TestCase):
    def compile(self, source, content=None):
        return compile_bank(content or bank(), {'I50_c.html': source}, 'I50')

    def test_scope_and_immutable_input(self):
        source = '<p>Anémie</p><section id="bilan"><p>Anémie</p></section>'
        sources = {'I50_c.html': source}
        content = bank()
        snapshot = copy.deepcopy(content)
        compiled, templates, report = compile_bank(content, sources, 'I50')
        self.assertTrue(compiled['I50_c.html'].startswith('<p>Anémie</p>'))
        self.assertEqual(compiled['I50_c.html'].count('data-justification="1"'), 1)
        self.assertIn('data-k="i50-j-anemie"', compiled['I50_c.html'])
        self.assertEqual(sources['I50_c.html'], source)
        self.assertEqual(content, snapshot)
        self.assertEqual((report['windows'], report['targets']), (1, 1))
        self.assertFalse(report['exhaustive_review'])
        self.assertIn('data-pop="i50-j-anemie"', templates)

    def test_entity_is_preserved(self):
        compiled, _, _ = self.compile('<p id="bilan">Sodium &amp; potassium</p>', bank('Sodium & potassium'))
        self.assertIn('>Sodium &amp; potassium</button>', compiled['I50_c.html'])

    def test_ambiguous_target_requires_explicit_occurrence(self):
        source = '<p id="bilan">Anémie, puis Anémie</p>'
        with self.assertRaises(JustificationError):
            self.compile(source)
        content = bank()
        content['entries'][0]['match'][0]['occurrence'] = 2
        compiled, _, _ = self.compile(source, content)
        self.assertIn('Anémie, puis <button', compiled['I50_c.html'])

    def test_existing_interaction_is_not_rewritten(self):
        for source in ['<p id="bilan"><button data-k="existing">Anémie</button></p>',
                       '<p id="bilan"><a href="#">Anémie</a></p>',
                       '<p id="bilan"><span data-ab="Hb">Anémie</span></p>']:
            with self.subTest(source=source), self.assertRaises(JustificationError):
                self.compile(source)

    def test_chapter_template_is_allowed_and_popup_template_is_excluded(self):
        source = '<template id="ch-I50"><p id="bilan">Anémie</p></template>'
        compiled, _, _ = self.compile(source)
        self.assertIn('<button', compiled['I50_c.html'])
        with self.assertRaises(JustificationError):
            self.compile('<template data-pop="example"><p id="bilan">Anémie</p></template>')

    def test_missing_anchor_and_file_fail(self):
        with self.assertRaises(JustificationError):
            self.compile('<p id="ailleurs">Anémie</p>')
        with self.assertRaises(JustificationError):
            compile_bank(bank(), {}, 'I50')

    def test_existing_key_fails(self):
        source = '<p id="bilan">Anémie</p><template data-pop="i50-j-anemie"></template>'
        with self.assertRaises(JustificationError):
            self.compile(source)

    def test_overlapping_targets_fail(self):
        content = bank()
        second = copy.deepcopy(content['entries'][0])
        second['id'] = 'i50-j-anemie-second'
        content['entries'].append(second)
        with self.assertRaises(JustificationError):
            self.compile('<p id="bilan">Anémie</p>', content)

    def test_unsafe_source_urls_fail(self):
        for url in ['javascript:alert(1)', 'https://name:secret@example.org/paper', 'http://example.org/paper']:
            content = bank()
            content['entries'][0]['sources'][0]['url'] = url
            with self.subTest(url=url), self.assertRaises(JustificationError):
                self.compile('<p id="bilan">Anémie</p>', content)

    def test_popup_text_is_escaped(self):
        _, templates, _ = self.compile('<p id="bilan">Anémie</p>')
        self.assertIn('Explication &lt;test&gt; &amp; contexte.', templates)
        self.assertNotIn('<test>', templates)

    def test_native_potassium_target_is_protected_from_glossary_wrapping(self):
        import build_medina as build
        compiled, _, _ = self.compile('<p id="bilan">K⁺</p>', bank('K⁺'))
        transformed = build.wrap_html(build.transform(compiled['I50_c.html']))
        self.assertRegex(transformed, r'<button\b[^>]*data-k="i50-j-anemie"[^>]*data-justification="1">K⁺</button>')
        self.assertNotIn('data-ab=', transformed)

    def test_missing_bank_returns_none(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIsNone(load_course_justifications('I50', folder))

    def test_short_target_does_not_match_inside_another_word(self):
        with self.assertRaises(JustificationError):
            self.compile('<p id="bilan">Nature du bilan</p>', bank('Na'))


if __name__ == '__main__':
    unittest.main()
