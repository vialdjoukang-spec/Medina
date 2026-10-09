from cardio_1 import a, G
# Glossaire du cours J67 — Pneumopathies d’hypersensibilité et maladies des poussières organiques (P-02-Pneumologie).
# Ajouts conditionnels : une clé déjà définie par un autre glossaire n’est jamais écrasée (S2k existe dans t78.py,
# chargé après ce fichier, qui la redéfinit de toute façon). Les clés génériques (Th1, FFP2, S2k, LAA, OLAA) portent
# des définitions valables hors de ce cours. Vérification des collisions le 09.10.2026. Revue IA ; ne vaut pas
# validation médicale.

def _a(k, *args):
    if k not in G:
        a(k, *args)

_a('PHS', [('P', 'Pneumopathie'), ('H', 'd’Hyper-'), ('S', 'Sensibilité')], 'Pneumopathie d’hypersensibilité',
   '<p>Maladie inflammatoire et/ou fibrosante du parenchyme pulmonaire et des petites voies aériennes, due à une réaction immunitaire non médiée par les IgE contre un antigène inhalé, chez un sujet sensibilisé et prédisposé (recommandation allemande S2k 2024). Ancien nom : alvéolite allergique extrinsèque.</p>', 'j67-definition')
_a('ODTS', [('O', 'Organic (organique)'), ('D', 'Dust (poussière)'), ('T', 'Toxic (toxique)'), ('S', 'Syndrome')], 'Syndrome toxique des poussières organiques (organic dust toxic syndrome)',
   '<p>Maladie fébrile non infectieuse, sans sensibilisation, qui survient environ trois à douze heures après l’inhalation de poussières organiques riches en endotoxines ou en mycotoxines. Elle ne s’accompagne habituellement ni d’IgG spécifiques élevées, ni de trouble fonctionnel, ni d’anomalie radiographique (recommandation allemande S2k 2024).</p>', 'j67-odts')
_a('Th1', [('T', 'T (lymphocyte T)'), ('h', 'helper (auxiliaire)'), ('1', 'de type 1')], 'Lymphocyte T auxiliaire de type 1',
   '<p>Sous-population de lymphocytes T CD4 auxiliaires qui produit notamment l’interféron gamma et le TNF-α ; elle oriente la réponse vers l’immunité cellulaire et la formation de granulomes.</p>')
_a('FFP2', [('F', 'Filtering (filtrante)'), ('F', 'Face (faciale)'), ('P', 'Piece (pièce)'), ('2', 'classe de protection 2')], 'Demi-masque filtrant contre les particules, classe 2',
   '<p>Appareil de protection respiratoire individuel filtrant contre les particules, de classe de protection 2. Il réduit l’exposition sans la supprimer.</p>')
_a('OLAA', [('O', 'Ordonnance'), ('L', 'sur L’'), ('A', 'Assurance-'), ('A', 'Accidents')], 'Ordonnance sur l’assurance-accidents (RS 832.202)',
   '<p>Ordonnance fédérale suisse d’application de la loi sur l’assurance-accidents. Son annexe 1 dresse la liste des substances nocives et des affections dues à certains travaux reconnues comme maladies professionnelles.</p>', 'j67-suva')
_a('LAA', [('L', 'Loi fédérale sur l’'), ('A', 'Assurance-'), ('A', 'Accidents')], 'Loi fédérale sur l’assurance-accidents (RS 832.20)',
   '<p>Loi suisse qui régit l’assurance contre les accidents et les maladies professionnelles : obligatoire pour les travailleurs occupés en Suisse (art. 1a), facultative pour les indépendants (art. 4) ; son article 9 définit la maladie professionnelle.</p>', 'j67-suva')
_a('RELIEF', [('RELIEF', 'nom propre de l’essai, non développable lettre à lettre')], 'Essai RELIEF (pirfénidone, 2021)',
   '<p>Essai randomisé allemand de phase 2b, 127 patients atteints de quatre PID fibrosantes progressives autres que la FPI, dont près de la moitié de pneumopathies d’hypersensibilité chroniques ; arrêté prématurément pour recrutement lent. Le déclin de la capacité vitale forcée était moindre sous pirfénidone.</p>', 'j67-d-pirfenidone')
_a('S2k', [('S2', 'Stufe 2 (niveau 2 de la classification allemande des recommandations)'), ('k', 'konsensbasiert (fondé sur un consensus formel d’experts)')], 'Niveau S2k des recommandations allemandes',
   '<p>Recommandation allemande élaborée par un groupe représentatif selon une procédure formelle de consensus (système de l’AWMF), sans revue systématique complète de la littérature.</p>')
_a('STOP', [('S', 'Substitution'), ('T', 'mesures Techniques'), ('O', 'mesures Organisationnelles'), ('P', 'Protection individuelle (personnelle)')], 'Hiérarchie des mesures de prévention au poste de travail',
   '<p>Ordre de priorité des mesures de prévention : substitution de la source, mesures techniques, mesures organisationnelles, puis protection individuelle en dernier recours (recommandation allemande S2k 2024 sur la pneumopathie d’hypersensibilité).</p>', 'j67-stop')
