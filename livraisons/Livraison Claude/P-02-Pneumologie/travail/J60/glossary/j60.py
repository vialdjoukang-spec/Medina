from cardio_1 import a, G
# J60 — Pneumoconioses (P-02-Pneumologie).
# Clés absentes de glossary/*.py et des dossiers de travail au 09.10.2026.
a('BIT', [('B', 'Bureau'), ('I', 'International'), ('T', 'du Travail')], 'Bureau international du Travail',
  '<p>Secrétariat de l’Organisation internationale du Travail. Il publie la classification internationale des radiographies de pneumoconiose, révisée en 2022 pour les images numériques, qui code la forme, la taille et la profusion des opacités par comparaison à des clichés types.</p>', 'j60-bit')
a('ICOERD', [('I', 'International (internationale)'), ('C', 'Classification (classification)'), ('O', 'of Occupational (des maladies professionnelles)'), ('E', 'and Environmental (et environnementales)'), ('R', 'Respiratory (respiratoires)'), ('D', 'Diseases (maladies)')], 'Classification internationale des maladies respiratoires professionnelles et environnementales en TDM',
  '<p>Système de lecture standardisée de la TDM thoracique par comparaison à des examens de référence ; il attribue des grades par région aux opacités et aux lésions pleurales. Les critères d’Helsinki 2014 en recommandent l’usage, et la recommandation AWMF 2026 y fonde les seuils de déclaration de la silicose.</p>', 'j60-tdm-icoerd')
a('IGRA', [('I', 'Interferon-Gamma (interféron gamma)'), ('R', 'Release (libération)'), ('A', 'Assay (test)')], 'Test de libération d’interféron gamma',
  '<p>Test sanguin qui mesure l’interféron gamma libéré par les lymphocytes en présence de peptides spécifiques de Mycobacterium tuberculosis ; il détecte une infection tuberculeuse, sans distinguer infection et maladie (guide suisse de la tuberculose, 2024).</p>', 'j60-igra')
a('AWMF', [('A', 'Arbeitsgemeinschaft (association)'), ('W', 'der Wissenschaftlichen (des sociétés scientifiques)'), ('M', 'Medizinischen (médicales)'), ('F', 'Fachgesellschaften (spécialisées)')], 'Association des sociétés scientifiques médicales d’Allemagne',
  '<p>Organisme qui encadre les recommandations des sociétés médicales allemandes. Sa recommandation S2k sur le diagnostic et l’expertise de la silicose, menée par la Société allemande de pneumologie, a été publiée en anglais en 2026 (Preisser et al., Respiration).</p>', 'j60-silicotuberculose')
a('EFA', [('E', 'Entschädigungsfonds (fonds d’indemnisation)'), ('F', 'für (des)'), ('A', 'Asbestopfer (victimes de l’amiante)')], 'Fondation Fonds d’indemnisation des victimes de l’amiante',
  '<p>Fondation suisse créée en 2017 qui conseille et soutient financièrement les personnes atteintes d’un mésothéliome contracté en Suisse lorsqu’elles ne sont pas couvertes par l’assurance-accidents.</p>', 'j60-efa')
a('NLST', [('N', 'National (national)'), ('L', 'Lung (pulmonaire)'), ('S', 'Screening (de dépistage)'), ('T', 'Trial (essai)')], 'Essai NLST (dépistage du cancer bronchique, 2011)',
  '<p>Essai randomisé américain qui a montré qu’un dépistage annuel par TDM à faible dose réduit la mortalité par cancer bronchique et la mortalité globale chez les grands fumeurs de 55 à 74 ans. La Suva et les critères d’Helsinki 2014 s’en inspirent pour le dépistage des exposés à l’amiante.</p>', 'j60-depistage-tdm')
a('HLA-DPB1', [('HLA', 'Human Leukocyte Antigen (antigène leucocytaire humain)'), ('DP', 'locus DP'), ('B1', 'gène de la chaîne bêta 1')], 'Gène HLA-DPB1',
  '<p>Gène qui code la chaîne bêta de la molécule HLA-DP. Son variant codant un acide glutamique en position 69 (Glu69) augmente le risque de sensibilisation au béryllium et de bérylliose chronique (Suva, 2012 ; Marchand-Adam, 2008).</p>', 'j60-hla-glu69')
# Noms d’auteurs composés cités dans le texte et les références (précédent : Funke-Chambour, j84).
a('Marchand-Adam', [('Marchand-Adam', 'S. Marchand-Adam, premier auteur')], 'Marchand-Adam et al., Eur Respir J 2008',
  '<p>Série de huit béryllioses chroniques sévères traitées par corticoïdes après l’arrêt de l’exposition, suivies 69 mois en médiane.</p>', 'j60-d-corticoides')
a('Mora-Cuesta', [('Mora-Cuesta', 'V. M. Mora-Cuesta, premier auteur')], 'Mora-Cuesta et al., Respirology 2026',
  '<p>Étude cas-témoins de sept centres espagnols : 81 transplantations pulmonaires pour pneumoconiose, survie comparable à celle des témoins.</p>', 'j60-transplantation')
a('Müller-Quernheim', [('Müller-Quernheim', 'J. Müller-Quernheim, premier auteur')], 'Müller-Quernheim et al., Eur Respir J 2006',
  '<p>Étude prospective : chez 84 patients étiquetés sarcoïdose, une bérylliose chronique a été diagnostiquée 34 fois après recherche de l’exposition et du test au béryllium.</p>', 'j60-berylliose')
a('Vu-Duc', [('Vu-Duc', 'T. Vu-Duc, premier auteur')], 'Vu-Duc et Guillemin, Soz Praventivmed 1999',
  '<p>Revue de l’histoire de la silicose en Suisse fondée sur les données de la Suva : 200 à 300 nouveaux cas par an des années 1940 aux années 1960, une centaine dès 1974, 30 à 50 dès 1989.</p>')
