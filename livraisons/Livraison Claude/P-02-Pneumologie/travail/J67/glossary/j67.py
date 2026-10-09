from cardio_1 import a, G
# J67 — Pneumopathies d’hypersensibilité et maladies des poussières organiques (P-02-Pneumologie).
# Clés absentes de glossary/*.py et des dossiers de travail livraisons/Livraison Claude/*/travail/*/glossary au 09.10.2026.
a('PHS', [('P', 'Pneumopathie'), ('H', 'd’Hyper-'), ('S', 'Sensibilité')], 'Pneumopathie d’hypersensibilité',
  '<p>Maladie inflammatoire et/ou fibrosante du parenchyme pulmonaire et des petites voies aériennes, due à une réaction immunitaire contre un antigène inhalé chez un sujet sensibilisé (ATS/JRS 2020 ; recommandation allemande S2k 2024). Ancien nom : alvéolite allergique extrinsèque.</p>', 'j67-definition')
a('ODTS', [('O', 'Organic (organique)'), ('D', 'Dust (poussière)'), ('T', 'Toxic (toxique)'), ('S', 'Syndrome')], 'Syndrome toxique des poussières organiques (organic dust toxic syndrome)',
  '<p>Réaction fébrile non infectieuse, sans sensibilisation, qui survient quelques heures après l’inhalation massive de poussières organiques riches en endotoxines ou en mycotoxines. Elle guérit spontanément et ne laisse pas de séquelle fonctionnelle.</p>', 'j67-odts')
a('Th1', [('T', 'T (lymphocyte T)'), ('h', 'helper (auxiliaire)'), ('1', 'de type 1')], 'Lymphocyte T auxiliaire de type 1',
  '<p>Sous-population de lymphocytes T CD4 qui produit l’interféron gamma et favorise l’activation des macrophages et la formation de granulomes. Elle domine la phase aiguë de la pneumopathie d’hypersensibilité.</p>', 'j67-sci-immuno')
a('FFP2', [('F', 'Filtering (filtrante)'), ('F', 'Face (faciale)'), ('P', 'Piece (pièce)'), ('2', 'classe de protection 2')], 'Demi-masque filtrant contre les particules, classe 2',
  '<p>Masque respiratoire jetable de classe 2 selon la norme européenne des demi-masques filtrants. Dans la pneumopathie d’hypersensibilité, il réduit l’exposition sans remplacer l’éviction de l’antigène (recommandation allemande S2k 2024).</p>', 'j67-protection')
a('OLAA', [('O', 'Ordonnance'), ('L', 'sur L’'), ('A', 'Assurance-'), ('A', 'Accidents')], 'Ordonnance sur l’assurance-accidents (RS 832.202)',
  '<p>Ordonnance fédérale suisse d’application de la loi sur l’assurance-accidents. Son annexe 1 dresse la liste des substances nocives et des affections dues à certains travaux reconnues comme maladies professionnelles, dont les affections respiratoires dues aux poussières organiques.</p>', 'j67-suva')
a('LAA', [('L', 'Loi fédérale sur l’'), ('A', 'Assurance-'), ('A', 'Accidents')], 'Loi fédérale sur l’assurance-accidents (RS 832.20)',
  '<p>Loi suisse qui régit l’assurance obligatoire contre les accidents et les maladies professionnelles. Son article 9 définit la maladie professionnelle.</p>', 'j67-suva')
a('RELIEF', [('RELIEF', 'nom propre de l’essai allemand de la pirfénidone dans les fibroses progressives autres que la fibrose idiopathique, non développable lettre à lettre')], 'Essai RELIEF (pirfénidone, 2021)',
  '<p>Essai randomisé allemand de phase 2b, 127 patients, arrêté prématurément pour recrutement lent ; près de la moitié des patients avaient une pneumopathie d’hypersensibilité chronique. Le déclin de la capacité vitale forcée était moindre sous pirfénidone.</p>', 'j67-d-pirfenidone')
a('S2k', [('S2', 'Stufe 2 (niveau 2 de la classification allemande des recommandations)'), ('k', 'konsensbasiert (fondé sur un consensus formel d’experts)')], 'Niveau S2k des recommandations allemandes',
  '<p>Recommandation élaborée par un groupe représentatif selon une procédure formelle de consensus, sans revue systématique complète de la littérature. La recommandation S2k 2024 sur la pneumopathie d’hypersensibilité émane des sociétés allemandes de pneumologie et d’allergologie.</p>', 'j67-s2k')
