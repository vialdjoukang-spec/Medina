"""Tests des fonctions de calcul de tools/front_poids.py (sans navigateur)."""
import base64
import gzip
import json
import tempfile
import unittest
from pathlib import Path

from tools import front_poids as F


class CompressionTests(unittest.TestCase):
    def test_mesures_brut_et_gzip(self):
        data = b'a' * 10000
        m = F.mesures(data)
        self.assertEqual(m['brut'], 10000)
        self.assertEqual(m['gzip'], len(gzip.compress(data, 6, mtime=0)))
        self.assertLess(m['gzip'], 200)

    def test_sans_compression_reprend_le_brut(self):
        m = F.mesures(b'\x89PNG' * 10, compresser=False)
        self.assertEqual(m['gzip'], 40)

    def test_additionner_propage_brotli_absent(self):
        total = F.additionner({'brut': 1, 'gzip': 1, 'brotli': None}, {'brut': 2, 'gzip': 2, 'brotli': 2})
        self.assertEqual(total, {'brut': 3, 'gzip': 3, 'brotli': None})


class ClassificationTests(unittest.TestCase):
    def test_categories_fichiers(self):
        self.assertEqual(F.categorie_fichier('a/b.WOFF2'), 'polices')
        self.assertEqual(F.categorie_fichier('x.png'), 'images')
        self.assertEqual(F.categorie_fichier('x.html'), 'html')
        self.assertEqual(F.categorie_fichier('x.bin'), 'autres')
        self.assertEqual(F.categorie_data_uri('font/woff2'), 'polices')
        self.assertEqual(F.categorie_data_uri('application/font-woff'), 'polices')
        self.assertEqual(F.categorie_data_uri('image/svg+xml'), 'images')

    def test_decomposer_page_autonome(self):
        police = base64.b64encode(b'W' * 300).decode()
        page = ('<html><head><style>@font-face{src:url(data:font/woff2;base64,' + police + ')}body{color:red}</style>'
                '<script>let x=1;</script><script type="application/json" id="d">{"a":1}</script>'
                '<script id="p" type="application/octet-stream">QUJD</script></head>'
                '<body><img src="data:image/png;base64,QUJD"><template id="t"><p>gabarit</p></template></body></html>')
        parts = F.decomposer_html(page)
        self.assertEqual(''.join(parts['js']), 'let x=1;')
        self.assertEqual(''.join(parts['donnees']), '{"a":1}QUJD')
        self.assertIn('body{color:red}', ''.join(parts['css']))
        self.assertNotIn('base64', ''.join(parts['css']))
        self.assertIn(police, ''.join(parts['polices']))
        self.assertIn('data:image/png', ''.join(parts['images']))
        self.assertIn('<p>gabarit</p>', ''.join(parts['html']))
        self.assertEqual([c for c, _, _ in parts['_incorporees']], ['polices', 'images'])
        self.assertEqual(parts['_incorporees'][0][2], b'W' * 300)
        # Rien n'est perdu ni compté deux fois.
        total = sum(len(''.join(parts[c])) for c in F.CATEGORIES)
        self.assertEqual(total, len(page))

    def test_audit_polices(self):
        css = ("@font-face{font-family:'A';font-display:swap;src:url(data:font/woff2;base64,QUJD)}"
               "@font-face{font-family:B;font-style:italic;src:url(fonts/b.woff2)}")
        audit = F.audit_polices('<style>' + css + '</style>')
        self.assertEqual(audit['font_face'][0], {'famille': 'A', 'style': 'normal', 'font_display': 'swap',
                                                 'source': 'incorporee', 'octets': 3})
        self.assertEqual(audit['font_face'][1]['source'], 'fonts/b.woff2')
        self.assertEqual(len(audit['alertes']), 2)
        prechargee = F.audit_polices('<link rel="preload" as="font" href="fonts/b.woff2"><style>' + css + '</style>')
        self.assertEqual(len(prechargee['prechargements']), 1)
        self.assertEqual(prechargee['alertes'], ['1 @font-face sans font-display'])


class InventaireTests(unittest.TestCase):
    def test_plus_gros_et_doublons(self):
        fichiers = [{'chemin': f'f{i}', 'brut': i} for i in range(15)]
        self.assertEqual([f['chemin'] for f in F.plus_gros(fichiers, 3)], ['f14', 'f13', 'f12'])
        groupes = F.doublons([('a.png', 'h1', 100), ('b/a.png', 'h1', 100), ('c.png', 'h2', 50),
                              ('d', 'h3', 10), ('e', 'h3', 10), ('f', 'h3', 10)])
        self.assertEqual([(g['sha256'], g['copies'], g['octets_redondants']) for g in groupes],
                         [('h1', 2, 100), ('h3', 3, 20)])

    def test_incorporees_repetees_dans_une_meme_page(self):
        groupes = F.regrouper_incorporees([('p.html [font/woff2]', 'h', 10), ('p.html [font/woff2]', 'h', 10),
                                           ('q.html [font/woff2]', 'h', 10), ('q.html [x]', 'u', 5)])
        self.assertEqual(len(groupes), 1)
        self.assertEqual((groupes[0]['occurrences'], groupes[0]['nb_pages'], groupes[0]['octets_redondants']), (3, 2, 20))

    def test_inventaire_dossier(self):
        with tempfile.TemporaryDirectory() as d:
            racine = Path(d)
            (racine / 'img').mkdir()
            (racine / 'img' / 'a.png').write_bytes(b'\x89PNG' + b'x' * 100)
            (racine / 'img' / 'copie.png').write_bytes(b'\x89PNG' + b'x' * 100)
            (racine / 'index.html').write_text('<html><style>p{}</style><img src="img/a.png"></html>', encoding='utf-8')
            r = F.inventaire(racine, journal=lambda m: None)
            self.assertEqual(r['site']['fichiers'], 3)
            page = r['pages']['index.html']
            self.assertEqual(page['ressources_externes'][0]['chemin'], 'img/a.png')
            self.assertEqual(page['avec_ressources']['brut'], page['total']['brut'] + 104)
            self.assertEqual(r['doublons']['fichiers'][0]['chemins'], ['img/a.png', 'img/copie.png'])
            self.assertEqual(r['site']['par_categorie']['images']['fichiers'], 2)


class CouvertureTests(unittest.TestCase):
    def test_fusion_intervalles(self):
        self.assertEqual(F.fusionner_intervalles([(5, 10), (0, 3), (2, 6), (12, 12)]), [(0, 10)])
        self.assertEqual(F.octets_couverts([(0, 4), (10, 12), (3, 5)]), 7)

    def test_js_blocs_imbriques(self):
        # Script de 100 octets : fonction exécutée [0,100), bloc non exécuté [20,50),
        # dans lequel un sous-bloc exécuté [30,40) (le plus interne gagne).
        fonctions = [
            {'ranges': [{'startOffset': 0, 'endOffset': 100, 'count': 1},
                        {'startOffset': 20, 'endOffset': 50, 'count': 0},
                        {'startOffset': 30, 'endOffset': 40, 'count': 1}]},
            {'ranges': [{'startOffset': 60, 'endOffset': 80, 'count': 0}]},
        ]
        self.assertEqual(F.intervalles_js_utilises(fonctions), [(0, 20), (30, 40), (50, 60), (80, 100)])
        self.assertEqual(F.octets_couverts(F.intervalles_js_utilises(fonctions)), 60)

    def test_js_jamais_execute(self):
        self.assertEqual(F.intervalles_js_utilises([{'ranges': [{'startOffset': 0, 'endOffset': 50, 'count': 0}]}]), [])

    def test_css_hors_font_face(self):
        texte = 'a{}' + '@font-face{src:url(data:x)}' + 'b{}c{}'
        faces = F.plages_font_face(texte)
        self.assertEqual(faces, [(3, 30)])
        # a{} utilisé, la règle @font-face « utilisée » ne compte pas, c{} utilisé.
        total, utilise, exclu = F.couverture_css(len(texte), [(0, 3), (3, 30), (33, 36)], faces)
        self.assertEqual((total, utilise, exclu), (9, 6, 27))

    def test_bilan(self):
        b = F.bilan_couverture([{'nom': 'a', 'total': 100, 'utilise': 25}, {'nom': 'b', 'total': 100, 'utilise': 100}])
        self.assertEqual((b['total'], b['inutilise'], b['pct_inutilise']), (200, 75, 37.5))
        self.assertEqual(b['principaux'][0]['nom'], 'a')
        self.assertEqual(F.bilan_couverture([])['pct_inutilise'], 0.0)


class TempsTests(unittest.TestCase):
    def test_tti_sans_tache_longue(self):
        self.assertEqual(F.calculer_tti(100, [], 80), 100)
        self.assertEqual(F.calculer_tti(100, [], 300), 300)
        self.assertIsNone(F.calculer_tti(None, [(0, 100)], 10))

    def test_tti_fin_de_derniere_tache_avant_fenetre_calme(self):
        taches = [(50, 60), (200, 100), (1000, 500), (8000, 200)]
        # 8000 - 1500 >= 5000 : la tâche de 8000 ms vient après la fenêtre calme.
        self.assertEqual(F.calculer_tti(120, taches, 90), 1500)

    def test_tti_tache_chevauchant_le_fcp(self):
        self.assertEqual(F.calculer_tti(100, [(50, 400)], 0), 450)


class BudgetTests(unittest.TestCase):
    rapport = {'site': {'total': {'brut': 1000}},
               'pages': {'MEDINA.html': {'total': {'brut': 500, 'gzip': 300}}},
               'temps': {'lecon': {'file-mobile': {'fcp_ms': 1234, 'tti_ms': None}}}}

    def test_lire_metrique_avec_cle_pointee(self):
        self.assertEqual(F.lire_metrique(self.rapport, 'pages.[MEDINA.html].total.gzip'), 300)
        self.assertIsNone(F.lire_metrique(self.rapport, 'pages.[MEDINA.html].total.brotli'))
        self.assertIsNone(F.lire_metrique(self.rapport, 'temps.lecon.file-mobile.tti_ms'))

    def test_verifier_budget(self):
        b = F.verifier_budget(self.rapport, {'max': {'site.total.brut': 900, 'pages.[MEDINA.html].total.brut': 600,
                                                     'temps.lecon.file-mobile.tti_ms': 10}})
        self.assertEqual(b['verifies'], 2)
        self.assertEqual(b['depassements'], [{'metrique': 'site.total.brut', 'valeur': 1000, 'limite': 900, 'exces_pct': 11.1}])
        self.assertEqual(b['non_mesurees'], ['temps.lecon.file-mobile.tti_ms'])

    def test_proposer_budget_puis_le_respecter(self):
        budget = F.proposer_budget(self.rapport, 0.10, 0.25)
        self.assertEqual(budget['max']['temps.lecon.file-mobile.fcp_ms'], 1600)
        self.assertEqual(budget['max']['pages.[MEDINA.html].total.brut'], 100000)
        self.assertEqual(F.verifier_budget(self.rapport, budget)['depassements'], [])
        self.assertEqual(F.arrondir_haut(1.01e6, 1e6), 2e6)

    def test_code_retour_budget_depasse(self):
        with tempfile.TemporaryDirectory() as d:
            racine = Path(d) / 'site'
            racine.mkdir()
            (racine / 'index.html').write_text('<html>' + 'x' * 2000 + '</html>', encoding='utf-8')
            budget = Path(d) / 'b.json'
            budget.write_text(json.dumps({'max': {'site.total.brut': 100}}), encoding='utf-8')
            sortie = Path(d) / 'r.json'
            args = ['--out', str(racine), '--sans-navigateur', '--json', str(sortie)]
            from contextlib import redirect_stdout, redirect_stderr
            import io
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(F.principal(args + ['--budget', str(budget)]), 1)
                budget.write_text(json.dumps({'max': {'site.total.brut': 10 ** 6}}), encoding='utf-8')
                self.assertEqual(F.principal(args + ['--budget', str(budget)]), 0)
            self.assertEqual(json.loads(sortie.read_text(encoding='utf-8'))['budget']['verifies'], 1)


if __name__ == '__main__':
    unittest.main()
