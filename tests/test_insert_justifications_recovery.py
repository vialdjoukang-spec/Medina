"""Safety and source preservation for the reconstructed contextual compiler."""
import copy
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools'))
from insert_justifications import JustificationError, compile_bank, load_course_justifications


def bank(text='Anémie'):
    return {'version': 1, 'course': {'code': 'I50', 'title': 'Insuffisance cardiaque'}, 'entries': [{
        'id': 'i50-j-anemie', 'title': 'Pourquoi l’anémie ?',
        'match': [{'file': 'I50_c.html', 'anchor': 'e-2', 'text': text}],
        'explanation': ['Une raison explicite.'], 'mechanism': ['Une chaîne causale.'],
        'implication': 'La conséquence clinique.', 'limits': ['Un contexte.'],
        'sources': [{'title': 'Publication primaire', 'url': 'https://example.org/research'}]}]}


class CompilerRecoveryTests(unittest.TestCase):
    def compile(self, source, value=None):
        return compile_bank(value or bank(), {'I50_c.html': source}, 'I50')

    def test_outer_course_template_is_targeted_and_original_is_unchanged(self):
        source = '<template id="ch-I50"><section id="e-2">Anémie : facteur aggravant.</section></template>'
        result, templates, report = self.compile(source)
        self.assertIn('data-justification="1">Anémie</button> : facteur aggravant.', result['I50_c.html'])
        self.assertEqual(source, '<template id="ch-I50"><section id="e-2">Anémie : facteur aggravant.</section></template>')
        self.assertIn('data-pop="i50-j-anemie"', templates)
        self.assertEqual((report['windows'], report['targets']), (1, 1))

    def test_entity_and_utf8_offsets_preserve_source_bytes(self):
        source = '<section id="e-2">Évaluation : Sodium &amp; potassium, puis suite.</section>'
        result, unused, unused_report = self.compile(source, bank('Sodium & potassium'))
        self.assertIn('>Sodium &amp; potassium</button>, puis suite.', result['I50_c.html'])
        self.assertTrue(result['I50_c.html'].startswith('<section id="e-2">Évaluation : '))

    def test_repeated_target_requires_explicit_occurrence(self):
        source = '<section id="e-2">Anémie. Anémie.</section>'
        with self.assertRaises(JustificationError): self.compile(source)
        b = bank(); b['entries'][0]['match'][0]['occurrence'] = 2
        result, unused, unused_report = self.compile(source, b)
        self.assertIn('>Anémie. <button', result['I50_c.html'])

    def test_occurrence_out_of_range_rejected(self):
        b = bank(); b['entries'][0]['match'][0]['occurrence'] = 2
        with self.assertRaises(JustificationError): self.compile('<section id="e-2">Anémie</section>', b)

    def test_interactive_and_popup_targets_rejected(self):
        for tag in ['<button>Anémie</button>', '<a href="/">Anémie</a>', '<span data-k="old">Anémie</span>', '<span data-ab="Hb">Anémie</span>', '<span role="button">Anémie</span>', '<template data-pop="old">Anémie</template>']:
            with self.subTest(tag=tag), self.assertRaises(JustificationError):
                self.compile('<section id="e-2">' + tag + '</section>')

    def test_anchor_scope_does_not_choose_unrelated_match(self):
        with self.assertRaises(JustificationError): self.compile('<section id="other">Anémie</section><section id="e-2">Sodium</section>')

    def test_overlapping_targets_rejected(self):
        b = bank('Sodium et potassium'); other = copy.deepcopy(b['entries'][0]); other['id'] = 'i50-j-potassium'; other['match'][0]['text'] = 'potassium'; b['entries'].append(other)
        with self.assertRaises(JustificationError): self.compile('<section id="e-2">Sodium et potassium</section>', b)

    def test_disjoint_targets_keep_text_order(self):
        b = bank(); other = copy.deepcopy(b['entries'][0]); other['id'] = 'i50-j-sodium'; other['match'][0]['text'] = 'Sodium'; b['entries'].append(other)
        result, unused, report = self.compile('<section id="e-2">Anémie puis Sodium.</section>', b)
        self.assertEqual(report['targets'], 2)
        self.assertLess(result['I50_c.html'].index('i50-j-anemie'), result['I50_c.html'].index('i50-j-sodium'))

    def test_bank_markup_is_escaped_and_sources_are_separate(self):
        b = bank(); b['entries'][0]['explanation'] = ['<script>alert(1)</script>']; b['entries'][0]['title'] = 'A "titre" <img>'
        unused, templates, unused_report = self.compile('<section id="e-2">Anémie</section>', b)
        self.assertNotIn('<script>', templates)
        self.assertIn('&lt;script&gt;', templates)
        self.assertIn('data-justification-sources="1"', templates)
        self.assertIn('rel="noopener noreferrer"', templates)

    def test_invalid_ids_sources_and_paths_rejected(self):
        mutations = [('id', 'foreign-j-id'), ('source', 'javascript:alert(1)'), ('file', '../I50_c.html'), ('source', 7)]
        for key, value in mutations:
            b = bank()
            if key == 'id': b['entries'][0]['id'] = value
            elif key == 'source': b['entries'][0]['sources'][0]['url'] = value
            else: b['entries'][0]['match'][0]['file'] = value
            with self.subTest(key=key, value=value), self.assertRaises(JustificationError): self.compile('<section id="e-2">Anémie</section>', b)

    def test_existing_popup_key_rejected(self):
        with self.assertRaises(JustificationError): self.compile('<section id="e-2">Anémie</section><template data-pop="i50-j-anemie">Ancien</template>')

    def test_missing_bank_leaves_loader_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIsNone(load_course_justifications('I50', folder))


if __name__ == '__main__': unittest.main()
