"""Invariant définitif de Vial (16.10.2026, « Ne change jamais ») : les cours restent sur blanc, quel que soit le thème."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = re.compile(r'(?<![\w-])--(cours-fond|ink-cours[\w-]*|titre-cours|terme[\w-]*)\s*:')


class CoursSurBlanc(unittest.TestCase):
    def test_fond_des_cours_blanc(self):
        css = (ROOT / 'engine/couleurs_premium.css').read_text(encoding='utf-8')
        valeurs = re.findall(r'(?<![\w-])--cours-fond\s*:\s*([^;}]+)', css)
        self.assertTrue(valeurs, '--cours-fond absent')
        self.assertEqual({v.strip().lower() for v in valeurs}, {'#ffffff'})
        self.assertIn('background-color:var(--cours-fond)!important', css.replace(' ', ''))

    def test_encres_noir_et_bleu(self):
        css = (ROOT / 'engine/couleurs_premium.css').read_text(encoding='utf-8')
        for nom in ('ink-cours-noir', 'ink-cours-bleu'):
            self.assertRegex(css, rf'--{nom}\s*:')
        self.assertTrue((ROOT / 'engine/encre_lecture.js').exists())

    def test_aucun_theme_ne_redefinit_les_tokens_des_cours(self):
        for f in sorted((ROOT / 'engine').glob('*.css')):
            if f.name == 'couleurs_premium.css':
                continue
            with self.subTest(fichier=f.name):
                self.assertIsNone(TOKENS.search(f.read_text(encoding='utf-8')),
                                  f'{f.name} redéfinit un token réservé aux cours')


if __name__ == '__main__':
    unittest.main()
