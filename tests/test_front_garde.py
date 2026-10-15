"""Tests des fonctions de calcul de tools/front_garde.py (sans navigateur)."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools import front_garde as fg  # noqa: E402


class ContrasteTest(unittest.TestCase):
    def test_extremes_wcag(self):
        self.assertAlmostEqual(fg.rapport_contraste((0, 0, 0), (255, 255, 255)), 21.0, places=2)
        self.assertAlmostEqual(fg.rapport_contraste((255, 255, 255), (255, 255, 255)), 1.0, places=6)

    def test_valeurs_de_reference(self):
        # #767676 sur blanc : 4,54:1, la plus claire des teintes grises conformes AA.
        self.assertAlmostEqual(fg.rapport_contraste((0x76, 0x76, 0x76), (255, 255, 255)), 4.54, places=2)
        # Orange #e0613f de l'Accueil sur #e9f7ff : 3,23:1 (constat « avant »).
        self.assertAlmostEqual(fg.rapport_contraste((224, 97, 63), (233, 247, 255)), 3.23, places=2)

    def test_symetrie_et_luminance(self):
        a, b = (31, 52, 40), (250, 250, 245)
        self.assertEqual(fg.rapport_contraste(a, b), fg.rapport_contraste(b, a))
        self.assertAlmostEqual(fg.luminance_relative((255, 255, 255)), 1.0)
        self.assertAlmostEqual(fg.luminance_relative((0, 0, 0)), 0.0)

    def test_composition_alpha(self):
        self.assertEqual(fg.composer((0, 0, 0, 0.5), (255, 255, 255)), (127.5, 127.5, 127.5))
        self.assertEqual(fg.fond_effectif([]), (255.0, 255.0, 255.0))
        self.assertEqual(fg.fond_effectif([(0, 0, 0, 1), (255, 0, 0, 0.0)]), (0.0, 0.0, 0.0))

    def test_degrade_pire_cas(self):
        fonds = fg.fonds_possibles([{"couleur": (0, 0, 0, 1)}, {"degrade": [(255, 255, 255, 1), (0, 0, 0, 0.5)]}])
        self.assertIn((255.0, 255.0, 255.0), fonds)
        self.assertIn((0.0, 0.0, 0.0), fonds)

    def test_analyse_echantillon(self):
        ech = [
            {"chemin": "p", "texte": "gris", "couleur": [118, 118, 118, 1], "couches": [], "indetermine": False, "taille": 16, "graisse": 400},
            {"chemin": "span", "texte": "pâle", "couleur": [11, 37, 69, 0.35], "couches": [], "indetermine": False, "taille": 12, "graisse": 400},
            {"chemin": "h1", "texte": "image", "couleur": [0, 0, 0, 1], "couches": [], "indetermine": True, "taille": 30, "graisse": 700},
        ]
        r = fg.analyser_contraste(ech)
        self.assertEqual((r["mesures"], r["indetermines"]), (2, 1))
        self.assertEqual([e["chemin"] for e in r["echecs"]], ["span"])

    def test_grand_texte_optionnel(self):
        ech = [{"chemin": "h2", "texte": "titre", "couleur": [224, 97, 63, 1], "couches": [{"couleur": [233, 247, 255, 1]}],
                "indetermine": False, "taille": 28, "graisse": 700}]
        self.assertEqual(len(fg.analyser_contraste(ech)["echecs"]), 1)
        self.assertEqual(len(fg.analyser_contraste(ech, grand_texte_wcag=True)["echecs"]), 0)


class SaturationTest(unittest.TestCase):
    def test_hsl(self):
        self.assertEqual(fg.rgb_vers_hsl((255, 0, 0)), (0.0, 1.0, 0.5))
        h, s, l = fg.rgb_vers_hsl((31, 52, 40))  # vert Medina #1f3428
        self.assertAlmostEqual(h, 145.7, places=1)
        self.assertLess(l, 0.3)

    def test_seuil_eblouissant(self):
        self.assertTrue(fg.couleur_eblouissante((255, 0, 0)))
        self.assertTrue(fg.couleur_eblouissante((255, 201, 60)))     # jaune vif
        self.assertFalse(fg.couleur_eblouissante((31, 52, 40)))      # vert sombre
        self.assertFalse(fg.couleur_eblouissante((250, 250, 245)))   # fond clair
        self.assertFalse(fg.couleur_eblouissante((128, 128, 128)))   # gris

    def test_surface_minimale(self):
        surfaces = [{"chemin": "badge", "aire": 900, "couleurs": [[255, 0, 0, 1]]},
                    {"chemin": "bandeau", "aire": 50000, "couleurs": [[250, 250, 245, 1], [255, 0, 0, 1]]}]
        self.assertEqual([e["chemin"] for e in fg.analyser_saturation(surfaces)], ["bandeau"])


class CartesEtDureesTest(unittest.TestCase):
    def test_ratio(self):
        self.assertAlmostEqual(fg.rapport_max_min([100, 110, 120]), 1.2)
        self.assertIsNone(fg.rapport_max_min([100]))
        self.assertIsNone(fg.rapport_max_min([0, 100]))

    def test_durees(self):
        self.assertEqual(fg.durees_css_ms("0.3s, 200ms"), [300.0, 200.0])
        self.assertEqual(fg.durees_css_ms(""), [])
        self.assertEqual(fg.totaux_transitions_ms("0.2s, 0.1s, 0.4s", "0.05s, 0s"), [250.0, 100.0, 450.0])

    def test_mouvement(self):
        donnees = {"scroll": "smooth", "elements": [
            {"chemin": "a", "type": "transition", "durees": "0.25s", "delais": "0s", "proprietes": "color"},
            {"chemin": "toast", "type": "transition", "durees": "0.4s", "delais": "0s", "proprietes": "all"},
            {"chemin": "spin", "type": "animation", "durees": "1s", "delais": "0s", "nom": "tourne", "iterations": "infinite"}]}
        self.assertEqual([e["chemin"] for e in fg.analyser_mouvement(donnees)], ["toast"])
        reduit = fg.analyser_mouvement(donnees, reduit=True)
        self.assertEqual({e["chemin"] for e in reduit}, {"a", "toast", "spin", "html"})


class PoliceEtFocusTest(unittest.TestCase):
    def test_police_principale(self):
        self.assertEqual(fg.police_principale('"Atkinson Hyperlegible Next", system-ui'), fg.POLICE_ATTENDUE)
        self.assertEqual(fg.police_principale("Georgia, serif"), "georgia")
        self.assertTrue(fg.est_monospace("ui-monospace, Menlo, monospace"))

    def test_focus(self):
        avant = {"outlineStyle": "none", "outlineWidth": "0px", "outlineRgba": [0, 0, 0, 0], "boxShadow": "none",
                 "backgroundColor": "rgba(0, 0, 0, 0)", "borderColor": "rgb(0, 0, 0)", "textDecorationLine": "none", "color": "rgb(0, 0, 0)"}
        self.assertFalse(fg.indicateur_focus_visible(avant, dict(avant)))
        contour = dict(avant, outlineStyle="solid", outlineWidth="3px", outlineRgba=[15, 90, 58, 1])
        self.assertTrue(fg.indicateur_focus_visible(avant, contour))
        transparent = dict(avant, outlineStyle="solid", outlineWidth="3px", outlineRgba=[0, 0, 0, 0])
        self.assertFalse(fg.indicateur_focus_visible(avant, transparent))
        self.assertTrue(fg.indicateur_focus_visible(avant, dict(avant, boxShadow="rgb(0, 0, 0) 0px 0px 0px 3px")))


class CliTest(unittest.TestCase):
    def test_dossier_absent_code_2(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(fg.main(["--out", str(Path(d) / "absent")]), 2)
            self.assertEqual(fg.main(["--out", d]), 2)  # ni index.html ni MEDINA.html


if __name__ == "__main__":
    unittest.main()
