"""Tests de tools/front_pipeline.py : cartographie N0, cache N1, plan N2, résumé N3 (sans navigateur)."""
import json
import os
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace

from tools import front_pipeline as P

FRAGMENTS = ['S01', 'S04', 'S07', 'S08']


def contexte(base=None, tete=None, **extra):
    base = base or {}
    tete = tete or {}
    return P.Contexte(fragments=list(FRAGMENTS), slugs={f: f.lower() for f in FRAGMENTS},
                      proprietaire={'I63': 'S08', 'G45': 'S08', 'I50': 'S01', 'N18': 'S04', 'M31': 'S07'},
                      contenu_base=lambda c: base.get(c), contenu_tete=lambda c: tete.get(c), **extra)


def tous_fragments():
    return {'fragment:' + f for f in FRAGMENTS}


class CartographieTests(unittest.TestCase):
    def test_moteur_commun_reconstruit_tout(self):
        plan = P.classer([('M', 'engine/atlas_v4.css')], contexte())
        self.assertEqual(set(plan.cibles), {'atlas', 'index', 'organisation', 'apercu'} | tous_fragments())

    def test_fenetre_de_cours_cible_son_seul_fragment(self):
        plan = P.classer([('M', 'chapters/I63/I63_pop1.html')], contexte())
        self.assertEqual(set(plan.cibles), {'atlas', 'fragment:S08', 'index'})
        self.assertEqual(plan.lecons, {'S08': ['I63']})
        self.assertEqual(plan.declencheurs['chapters/I63/I63_pop1.html'], ['atlas', 'fragment:S08', 'index'])

    def test_onglet_modifie_sans_basculer_reste_local(self):
        chemin = 'chapters/G45/G45_a.html'
        plan = P.classer([('M', chemin)], contexte({chemin: b'<p>ancien</p>'}, {chemin: b'<p>nouveau</p>'}))
        self.assertEqual(set(plan.cibles), {'atlas', 'fragment:S08', 'index'})

    def test_onglet_vide_devenu_rempli_change_la_jauge_globale(self):
        chemin = 'chapters/G45/G45_b.html'
        plan = P.classer([('A', chemin)], contexte({}, {chemin: b'<p>texte</p>'}))
        self.assertTrue(tous_fragments() <= set(plan.cibles))
        self.assertIn('jauge globale', ' '.join(plan.cibles['fragment:S01']))

    def test_cours_sans_proprietaire_est_conservateur(self):
        plan = P.classer([('A', 'chapters/Z99/Z99_pop.html')], contexte())
        self.assertTrue(tous_fragments() <= set(plan.cibles))

    def test_documentation_sans_effet(self):
        plan = P.classer([('M', 'docs/frontend/outils/README.md'), ('M', 'REPRISE_SESSION.md'),
                          ('M', '.github/workflows/pages.yml')], contexte())
        self.assertEqual(plan.cibles, {})
        self.assertEqual(len(plan.ignores), 3)

    def test_chapters_json_titre_modifie_reste_local(self):
        avant = json.dumps([{'code': 'I63', 'title': 'A', 'integrated': True}, {'code': 'I50', 'title': 'B', 'integrated': True}]).encode()
        apres = json.dumps([{'code': 'I63', 'title': 'A2', 'integrated': True}, {'code': 'I50', 'title': 'B', 'integrated': True}]).encode()
        plan = P.classer([('M', 'chapters.json')], contexte({'chapters.json': avant}, {'chapters.json': apres}))
        self.assertEqual(set(plan.cibles), {'atlas', 'fragment:S08', 'index'})

    def test_chapters_json_couvertures_modifiees_touche_tous_les_fragments(self):
        avant = json.dumps([{'code': 'I63', 'covers': ['I63']}]).encode()
        apres = json.dumps([{'code': 'I63', 'covers': ['I63', 'I64']}]).encode()
        plan = P.classer([('M', 'chapters.json')], contexte({'chapters.json': avant}, {'chapters.json': apres}))
        self.assertTrue(tous_fragments() <= set(plan.cibles))

    def test_chapters_json_illisible_reconstruit_tout(self):
        plan = P.classer([('M', 'chapters.json')], contexte({'chapters.json': b'['}, {'chapters.json': b'[]'}))
        self.assertIn('organisation', plan.cibles)

    def test_inventaire_nosologique(self):
        lecon = {'id': 'x', 'code': 'N18', 'existing_course': 'N18', 'state': 'empty', 'plan': []}
        avant = json.dumps({'lessons': [lecon]}).encode()
        meme = json.dumps({'lessons': [{**lecon, 'state': 'filled', 'plan': [{'content': 'x'}]}]}).encode()
        chemin = 'nosology/fragments/S04.json'
        plan = P.classer([('M', chemin)], contexte({chemin: avant}, {chemin: meme}))
        self.assertEqual(set(plan.cibles), {'fragment:S04', 'index'})
        autre = json.dumps({'lessons': [lecon, {**lecon, 'id': 'y', 'code': 'N19'}]}).encode()
        plan = P.classer([('M', chemin)], contexte({chemin: avant}, {chemin: autre}))
        self.assertTrue(tous_fragments() <= set(plan.cibles))

    def test_modules_et_outils_de_controle(self):
        plan = P.classer([('M', 'modules/ecg.json')], contexte())
        self.assertEqual(set(plan.cibles), {'atlas', 'fragment:S01', 'index'})
        plan = P.classer([('M', 'tools/front_garde.py')], contexte())
        self.assertEqual(plan.cibles, {})
        self.assertIn('@garde', plan.drapeaux)

    def test_fichier_inconnu_code_conservateur_autre_ignore(self):
        plan = P.classer([('A', 'tools/nouveau.py'), ('A', 'photos/x.png')], contexte())
        self.assertEqual(plan.conservateurs, ['tools/nouveau.py'])
        self.assertIn('photos/x.png', plan.ignores)
        self.assertTrue(tous_fragments() <= set(plan.cibles))

    def test_dependance_tracee_remplace_la_prudence(self):
        ctx = contexte(index_deps={'tools/aide_build.py': ['fragment:S04']})
        plan = P.classer([('M', 'tools/aide_build.py')], ctx)
        self.assertEqual(set(plan.cibles), {'fragment:S04', 'index'})
        self.assertEqual(plan.conservateurs, [])

    def test_exclusion_des_onglets_et_inventaires_etrangers(self):
        deps = ['r:chapters/I63/I63_a.html', 'r:chapters/I50/I50_a.html', 'r:chapters/I50/I50_pop.html',
                'r:nosology/fragments/S08.json', 'r:nosology/fragments/S01.json', 'r:engine/x.css']
        gardes, exclu = P.deps_effectives('fragment:S08', deps, contexte().proprietaire)
        self.assertTrue(exclu)
        self.assertEqual(gardes, ['r:chapters/I63/I63_a.html', 'r:chapters/I50/I50_pop.html',
                                  'r:nosology/fragments/S08.json', 'r:engine/x.css'])
        self.assertEqual(P.deps_effectives('atlas', deps, contexte().proprietaire), (deps, False))


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.root, self.out = base / 'depot', base / 'site'
        (self.root / 'src').mkdir(parents=True)
        self.out.mkdir()
        (self.root / 'src/a.txt').write_text('alpha', encoding='utf-8')
        (self.root / 'construire.py').write_text(
            'import glob, os, pathlib\n'
            'texte = open("src/a.txt", encoding="utf-8").read()\n'
            'noms = sorted(p.name for p in pathlib.Path("src").glob("*.txt"))\n'
            'sortie = pathlib.Path(os.environ["MEDINA_OUT"]) / "page.html"\n'
            'sortie.write_text(texte + ",".join(noms), encoding="utf-8")\n', encoding='utf-8')
        self.ancien_root = P.ROOT
        P.ROOT = self.root
        self.cache = P.Cache(base / 'cache')
        self.cible = P.Cible('atlas', 'construire.py', [], ['page.html'])
        self.ctx = P.Contexte(fragments=[], slugs={}, proprietaire={})

    def tearDown(self):
        P.ROOT = self.ancien_root
        self.tmp.cleanup()

    def decision(self, plan=None):
        return P.decider(plan or P.Plan(), {'atlas': self.cible}, self.cache, self.out, self.ctx, None)['atlas']

    def construire(self):
        return P.construire(self.cible, self.cache, self.out, self.ctx, None, self.out.parent / 'journaux')

    def test_trace_puis_saut_puis_reconstruction(self):
        self.assertEqual(self.decision().action, 'hors_plan')
        plan = P.Plan(cibles={'atlas': ['test']})
        self.assertEqual(self.decision(plan).action, 'construire')
        res = self.construire()
        self.assertEqual(res['statut'], 'ok', res)
        entree = self.cache.entree('atlas')
        self.assertIn('r:src/a.txt', entree['deps'])
        self.assertIn('r:construire.py', entree['deps'])
        self.assertNotIn('o:page.html', entree['deps'])
        self.assertIn('r:src', entree['dossiers'])
        self.assertEqual(self.decision(plan).action, 'a_jour')
        # Entrée lue modifiée : l'empreinte change.
        time.sleep(0.01)
        (self.root / 'src/a.txt').write_text('beta', encoding='utf-8')
        self.assertEqual(self.decision().action, 'construire')
        self.construire()
        self.assertEqual(self.decision().action, 'a_jour')
        # Nouveau fichier dans un dossier parcouru : l'empreinte change aussi.
        (self.root / 'src/b.txt').write_text('x', encoding='utf-8')
        self.assertEqual(self.decision().action, 'construire')

    def test_agregat_reevalue_quand_un_prerequis_est_reconstruit(self):
        (self.root / 'portail.py').write_text(
            'import os, pathlib\n'
            'out = pathlib.Path(os.environ["MEDINA_OUT"])\n'
            '(out / "index.html").write_text("portail:" + (out / "page.html").read_text(encoding="utf-8"), encoding="utf-8")\n',
            encoding='utf-8')
        index = P.Cible('index', 'portail.py', [], ['index.html'], ['atlas'])
        cibles = {'atlas': self.cible, 'index': index}
        self.construire()
        P.construire(index, self.cache, self.out, self.ctx, None, self.out.parent / 'journaux')
        self.assertIn('o:page.html', self.cache.entree('index')['deps'])
        decisions = P.decider(P.Plan(), cibles, self.cache, self.out, self.ctx, None)
        self.assertEqual({c: d.action for c, d in decisions.items()}, {'atlas': 'a_jour', 'index': 'a_jour'})
        (self.root / 'src/a.txt').write_text('gamma', encoding='utf-8')
        decisions = P.decider(P.Plan(), cibles, self.cache, self.out, self.ctx, None)
        self.assertEqual(decisions['atlas'].action, 'construire')
        self.assertEqual((decisions['index'].action, decisions['index'].raison), ('construire', P.REEVALUER))
        self.construire()
        self.assertNotEqual(P.empreinte_entree(index, self.cache.entree('index'), self.cache, self.out, self.ctx, None),
                            self.cache.entree('index')['empreinte'])

    def test_restauration_depuis_les_objets(self):
        self.construire()
        (self.out / 'page.html').unlink()
        self.assertEqual(self.decision().action, 'restaurer')
        P.restaurer(self.cible, self.cache, self.out)
        self.assertEqual((self.out / 'page.html').read_text(encoding='utf-8'), 'alphaa.txt')
        self.assertEqual(self.decision().action, 'a_jour')

    def test_cle_des_controles_reussis(self):
        controle = P.Controle('front_garde:X', ['node', 'construire.py'], {'MEDINA_QA_OUT': '/q'}, '', ['atlas'], 'garde', True)
        self.assertIsNone(P.cle_controle(controle, self.cache, self.out))
        self.construire()
        cle = P.cle_controle(controle, self.cache, self.out)
        self.assertIsNotNone(cle)
        self.assertEqual(P.cle_controle(controle, self.cache, self.out), cle)
        autre = P.Controle('front_garde:X', ['node', 'construire.py'], {'MEDINA_QA_OUT': '/autre'}, '', ['atlas'], 'garde', True)
        self.assertEqual(P.cle_controle(autre, self.cache, self.out), cle)
        (self.out / 'page.html').write_text('modifiée', encoding='utf-8')
        self.assertIsNone(P.cle_controle(controle, self.cache, self.out))
        poids = P.Controle('front_poids', [], {}, '', ['atlas'], 'front_poids')
        self.assertIsNone(P.cle_controle(poids, self.cache, self.out))

    def test_echec_de_construction_rapporte_un_extrait(self):
        (self.root / 'construire.py').write_text('raise SystemExit("cassé")\n', encoding='utf-8')
        res = self.construire()
        self.assertEqual(res['statut'], 'echec')
        self.assertIn('cassé', '\n'.join(res['extrait']))
        self.assertIsNone(self.cache.entree('atlas'))

    def test_memo_des_empreintes_de_fichiers(self):
        chemin = self.root / 'src/a.txt'
        premier = self.cache.sha(chemin)
        self.assertIn(str(chemin), self.cache.memo)
        self.assertEqual(self.cache.sha(chemin), premier)
        self.assertIsNone(self.cache.sha(self.root / 'absent'))
        self.cache.sauver()
        self.assertEqual(P.Cache(self.cache.dossier).memo[str(chemin)][3], premier)

    def test_valeurs_derivees_seulement_si_exclusion(self):
        entree = {'deps': ['r:src/a.txt'], 'dossiers': []}
        a = P.empreinte_entree(self.cible, entree, self.cache, self.out, self.ctx, {'jauge': 1})
        b = P.empreinte_entree(self.cible, entree, self.cache, self.out, self.ctx, {'jauge': 2})
        self.assertEqual(a, b)
        fragment = P.Cible('fragment:S08', 'construire.py', [], ['page.html'])
        ctx = P.Contexte(fragments=['S08'], slugs={}, proprietaire={'I50': 'S01'})
        entree = {'deps': ['r:src/a.txt', 'r:chapters/I50/I50_a.html'], 'dossiers': []}
        a = P.empreinte_entree(fragment, entree, self.cache, self.out, ctx, {'jauge': 1})
        b = P.empreinte_entree(fragment, entree, self.cache, self.out, ctx, {'jauge': 2})
        self.assertNotEqual(a, b)

    def test_normaliser(self):
        self.assertEqual(P.normaliser(str(self.root / 'src/a.txt'), self.out), 'r:src/a.txt')
        self.assertEqual(P.normaliser(str(self.out / 'fragments/x.html'), self.out), 'o:fragments/x.html')
        self.assertEqual(P.normaliser(str(self.root / 'tools/__pycache__/m.cpython-312.pyc'), self.out), 'r:tools/m.py')
        self.assertIsNone(P.normaliser('/usr/lib/python3/json/__init__.py', self.out))


class ControlesTests(unittest.TestCase):
    def options(self, **kw):
        return SimpleNamespace(**{"poids_navigateur": False, "garde_max": 2, "garde_args": "", **kw})

    def test_controles_filtres_sur_les_fragments_touches(self):
        ctx = contexte()
        plan = P.classer([('M', 'chapters/I63/I63_pop1.html'), ('M', 'chapters/N18/N18_pop.html')], ctx)
        controles = P.planifier_controles(plan, ['chapters/I63/I63_pop1.html'], [], Path('/o'), Path('/q'), ctx, self.options())
        par_id = {c.id: c for c in controles}
        self.assertEqual(par_id['verify_category_progress'].env['MEDINA_CATEGORY_FRAGMENT_IDS'], 'S04,S08')
        self.assertEqual(par_id['verify_fragment_bootstrap'].env['MEDINA_QA_FRAGMENTS'], 'S04,S08')
        self.assertNotIn('verify_fragment_filters', par_id)
        self.assertNotIn('verify_categories', par_id)  # hors pages.yml, en échec sur main : opt-in
        avec = P.planifier_controles(plan, [], [], Path('/o'), Path('/q'), ctx, self.options(verify_categories=True))
        self.assertIn('verify_categories', [c.id for c in avec])
        gardes = [c for c in controles if c.famille == 'garde']
        self.assertEqual([c.id for c in gardes], ['front_garde:S04', 'front_garde:S08'])
        self.assertIn('--lecon', gardes[1].commande)
        self.assertEqual(gardes[1].commande[gardes[1].commande.index('--lecon') + 1], 'I63')

    def test_filtres_et_garde_par_defaut(self):
        ctx = contexte()
        fichiers = ['engine/category_organisation.js']
        plan = P.classer([('M', f) for f in fichiers], ctx)
        ids = [c.id for c in P.planifier_controles(plan, fichiers, [], Path('/o'), Path('/q'), ctx, self.options(garde_max=1))]
        self.assertIn('verify_fragment_filters', ids)
        self.assertEqual([i for i in ids if i.startswith('front_garde')], ['front_garde:S01'])
        plan = P.classer([('M', 'tools/front_garde.py')], ctx)
        ids = [c.id for c in P.planifier_controles(plan, ['tools/front_garde.py'], [], Path('/o'), Path('/q'), ctx, self.options())]
        self.assertEqual(ids, ['tests-python', 'front_garde:S08'])

    def test_documentation_seule_aucun_controle(self):
        ctx = contexte()
        plan = P.classer([('M', 'docs/a.md')], ctx)
        self.assertEqual(P.planifier_controles(plan, ['docs/a.md'], [], Path('/o'), Path('/q'), ctx, self.options()), [])

    def test_tests_python_lies(self):
        self.assertEqual(P.tests_python_lies(['tools/front_garde.py', 'tests/test_front_pipeline.py', 'docs/x.md']),
                         ['tests/test_front_garde.py', 'tests/test_front_pipeline.py'])

    def test_budget_filtre(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, 'index.html').write_text('x')
            budget = {'max': {'site.total.brut': 1, 'pages.[index.html].total.gzip': 2,
                              'pages.[MEDINA.html].total.brut': 3, 'temps.accueil.http-mobile.fcp_ms': 4}}
            self.assertEqual(P.budget_filtre(budget, Path(d), False)['max'],
                             {'site.total.brut': 1, 'pages.[index.html].total.gzip': 2})
            self.assertIn('temps.accueil.http-mobile.fcp_ms', P.budget_filtre(budget, Path(d), True)['max'])

    def test_extraction_des_echecs_de_front_garde(self):
        with tempfile.TemporaryDirectory() as d:
            rapport = Path(d, 'g.json')
            rapport.write_text(json.dumps({'resultats': [
                {'page': 'fragment', 'largeur': 390, 'controle': 'contraste', 'statut': 'echec',
                 'detail': {'echecs': [{'rapport': 2.1}, {'rapport': 2.5}, {'rapport': 3}]}},
                {'page': 'fragment', 'largeur': 390, 'controle': 'police', 'statut': 'ok', 'detail': {}}]}))
            controle = P.Controle('front_garde:S08', [], {}, '', [], 'garde', True, str(rapport))
            echecs = P.echecs_detail(controle, 1, '')
            self.assertEqual(echecs, [{'controle': 'garde:contraste', 'page': 'fragment', 'largeur': 390,
                                       'exemples': [{'rapport': 2.1}, {'rapport': 2.5}]}])
            self.assertEqual(P.niveau_ia(echecs), 'opus')
            self.assertEqual(P.niveau_ia([{'controle': 'front_poids'}, {'controle': 'garde:transitions'}]), 'leger')


class RapportTests(unittest.TestCase):
    def test_resume_en_cinq_lignes(self):
        rapport = {'base': 'abc', 'tete': None, 'dry_run': False, 'fichiers': [{'statut': 'M', 'chemin': 'x'}],
                   'ignores': [], 'conservateurs': [], 'plan': {'atlas': ['r']},
                   'constructions': {'atlas': {'decision': 'construire'}, 'index': {'decision': 'a_jour'}},
                   'controles': [{'id': 'front_poids', 'statut': 'ok'}, {'id': 'front_garde:S08', 'statut': 'echec'}],
                   'economie': {'construction_realisee_s': 10, 'construction_evitee_s': 400},
                   'ia': {'niveau': 'opus', 'paquet': '/tmp/p.txt'}}
        lignes = P.resume_cinq_lignes(rapport)
        self.assertEqual(len(lignes), 5)
        self.assertIn('400 s évités', lignes[2])
        self.assertIn('échec : front_garde:S08', lignes[3])
        self.assertIn('IA requise', lignes[4])
        rapport['ia'] = None
        self.assertEqual(P.resume_cinq_lignes(rapport)[4], 'N3 : aucune IA nécessaire')

    def test_plan_a_blanc_sur_le_depot_reel(self):
        with tempfile.TemporaryDirectory() as d:
            code = P.principal(['--dry-run', '--cache', d, '--fichiers', 'docs/frontend/outils/MOTORISATION.md'])
            self.assertEqual(code, 0)
            rapport = json.loads(Path(d, 'dernier/rapport.json').read_text(encoding='utf-8'))
            self.assertEqual(rapport['plan'], {})
            self.assertEqual(len(rapport['resume']), 5)
            self.assertFalse(Path(d, 'site').exists())


if __name__ == '__main__':
    unittest.main()
