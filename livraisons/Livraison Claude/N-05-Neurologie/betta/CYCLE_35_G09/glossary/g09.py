"""Abréviations G09 (Séquelles d’affections inflammatoires du système nerveux central). Entrées conditionnelles : aucun terme existant dans G n’est écrasé."""
from cardio_1 import a, G
if 'SNC' not in G:
    a('SNC', [('S', 'Système'), ('N', 'Nerveux'), ('C', 'Central')], 'Système nerveux central', '<p>Le système nerveux central comprend l’encéphale et la moelle épinière. La catégorie G09 désigne les séquelles de leurs inflammations (méninges, encéphale, moelle) classées en G00–G08.</p>', 'g09-snc')
if 'OMS' not in G:
    a('OMS', [('O', 'Organisation'), ('M', 'Mondiale de la'), ('S', 'Santé')], 'Organisation mondiale de la santé', '<p>Cette agence a publié en 2025 les lignes directrices sur la méningite qui structurent le dépistage, la réhabilitation et le suivi des séquelles ; elle publie aussi la CIM-10 (version 2019).</p>', 'g09-oms')
if 'OFSP' not in G:
    a('OFSP', [('O', 'Office'), ('F', 'Fédéral de la'), ('S', 'Santé'), ('P', 'Publique')], 'Office fédéral de la santé publique', '<p>L’Office fédéral de la santé publique publie les recommandations suisses de vaccination, dont celle contre la méningo-encéphalite à tiques (rappel tous les 10 ans, état juillet 2024).</p>', 'g09-vaccin-fsme')
if 'FSME' not in G:
    a('FSME', [('F', 'Früh'), ('S', 'Sommer (début d’été)'), ('M', 'Meningo'), ('E', 'Enzephalitis (méningo-encéphalite)')], 'Méningo-encéphalite verno-estivale à tiques (Frühsommer-Meningoenzephalitis)', '<p>Infection virale du système nerveux central transmise par les tiques. Elle laisse des séquelles chez une part importante des patients, notamment fatigue, troubles du sommeil et troubles cognitifs ; aucun traitement causal n’existe.</p>', 'g09-fsme')
if 'HSV' not in G:
    a('HSV', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus')], 'Virus herpès simplex', '<p>Première cause d’encéphalite dans la série bernoise. Une encéphalite auto-immune, surtout à anticorps anti-NMDAR, peut la compliquer chez 27 % des patients d’une cohorte espagnole.</p>', 'g09-hsv-sigle')
if 'NMDA' not in G:
    a('NMDA', [('N', 'N-'), ('M', 'Méthyl-'), ('D', 'D-'), ('A', 'Aspartate')], 'N-méthyl-D-aspartate', '<p>Substance qui donne son nom au récepteur neuronal NMDA, cible des anticorps de l’encéphalite auto-immune post-herpétique.</p>', 'g09-nmda')
if 'NMDAR' not in G:
    a('NMDAR', [('NMDA', 'N-méthyl-D-aspartate'), ('R', 'Récepteur')], 'Récepteur du N-méthyl-D-aspartate', '<p>Récepteur neuronal visé par les anticorps de l’encéphalite auto-immune qui peut suivre une encéphalite à HSV.</p>', 'g09-nmda')
if 'SV2A' not in G:
    a('SV2A', [('SV', 'Synaptic Vesicle (vésicule synaptique)'), ('2', 'protéine 2'), ('A', 'isoforme A')], 'Protéine 2A de la vésicule synaptique', '<p>Cible du lévétiracétam selon l’information professionnelle suisse.</p>', 'g09-sv2a')
if 'IRM' not in G:
    a('IRM', [('I', 'Imagerie par'), ('R', 'Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique', '<p>Elle montre l’inflammation de l’endolymphe cochléaire avant l’ossification ; le scanner y est moins sensible.</p>', 'g09-pea-irm')
if 'PEA' not in G:
    a('PEA', [('P', 'Potentiels'), ('E', 'Évoqués'), ('A', 'Auditifs du tronc cérébral')], 'Potentiels évoqués auditifs du tronc cérébral', '<p>Enregistrement électrique de la voie auditive, utilisé chez l’enfant pour confirmer une surdité après dépistage comportemental.</p>', 'g09-pea-irm')
if 'CIM-10-GM' not in G:
    a('CIM-10-GM', [('CIM', 'Classification Internationale des Maladies'), ('10', 'dixième révision'), ('GM', 'German Modification (modification allemande)')], 'Classification internationale des maladies, dixième révision, modification allemande', '<p>Version de la classification adoptée en Suisse ; l’édition 2024 est celle du cours.</p>', 'g09-cim')
if 'CIM-10' not in G:
    a('CIM-10', [('CIM', 'Classification Internationale des Maladies'), ('10', 'dixième révision')], 'Classification internationale des maladies, dixième révision', '<p>Classification de l’Organisation mondiale de la santé ; la version 2019 a été lue pour G09 et les codes voisins.</p>', 'g09-codage')
if 'ACE-III' not in G:
    a('ACE-III', [('ACE', 'Addenbrooke’s Cognitive Examination'), ('III', 'troisième version')], 'Examen cognitif d’Addenbrooke, troisième version', '<p>Test de dépistage cognitif proposé, avec une preuve faible, après méningite tuberculeuse.</p>', 'g09-neuropsy')
if 'RAND-36' not in G:
    a('RAND-36', [('RAND', 'nom propre de l’organisation qui a élaboré le questionnaire, non développé'), ('36', 'nombre de questions')], 'Questionnaire de qualité de vie en 36 questions', '<p>Utilisé dans la cohorte néerlandaise de méningite pneumococcique.</p>', 'g09-neuropsy')
if 'CLCE-24' not in G:
    a('CLCE-24', [('CLCE', 'sigle du questionnaire de plainte cognitive, développement non précisé dans la source lue'), ('24', 'nombre de questions')], 'Questionnaire de plainte cognitive en 24 questions', '<p>Utilisé dans la cohorte néerlandaise de méningite pneumococcique.</p>', 'g09-neuropsy')
if 'BfArM' not in G:
    a('BfArM', [('BfArM', 'Bundesinstitut für Arzneimittel und Medizinprodukte (Institut fédéral allemand des médicaments et des dispositifs médicaux)')], 'Institut fédéral allemand des médicaments et des dispositifs médicaux', '<p>Il publie la CIM-10-GM ; son bloc G00–G09 a été lu pour la règle de codage de G09.</p>', 'g09-cim')
if 'PROFILES' not in G:
    a('PROFILES', [('PROFILES', 'nom propre du référentiel suisse, acronyme anglais non développé dans ce cours')], 'PROFILES, référentiel des objectifs de formation médicale en Suisse', '<p>Ce référentiel définit les situations cliniques de départ de l’examen fédéral suisse de médecine humaine.</p>', 'g09-codage')
if 'B90.0' not in G:
    a('B90.0', [('B', 'chapitre I de la CIM-10 (certaines maladies infectieuses et parasitaires)'), ('90.0', 'séquelles de tuberculose du système nerveux central')], 'Code CIM-10 des séquelles de tuberculose du système nerveux central', '<p>Ces séquelles se classent hors de G09 : la tuberculose est une maladie du chapitre des maladies infectieuses.</p>', 'g09-voisins')
if 'B94.1' not in G:
    a('B94.1', [('B', 'chapitre I de la CIM-10 (certaines maladies infectieuses et parasitaires)'), ('94.1', 'séquelles d’encéphalite virale')], 'Code CIM-10 des séquelles d’encéphalite virale', '<p>Ces séquelles se classent hors de G09. Le rattachement des séquelles de méningo-encéphalite à tiques à ce code est une déduction, non vérifiée dans la version 2024.</p>', 'g09-voisins')
if 'PMID' not in G:
    a('PMID', [('PM', 'PubMed'), ('ID', 'IDentifier (identifiant)')], 'Identifiant PubMed d’un article', '<p>Numéro attribué à une publication dans la base bibliographique PubMed. Il sert ici à retrouver la source lue.</p>')
if 'GTIN' not in G:
    a('GTIN', [('G', 'Global'), ('T', 'Trade'), ('I', 'Item'), ('N', 'Number')], 'Numéro mondial d’article commercial', '<p>Code qui identifie une spécialité dans la base d’informations professionnelles consultée.</p>')
if 'ISBN' not in G:
    a('ISBN', [('I', 'International'), ('S', 'Standard'), ('B', 'Book'), ('N', 'Number')], 'Numéro international normalisé du livre', '<p>Identifiant de la publication de l’Organisation mondiale de la santé citée.</p>')
if 'PDF' not in G:
    a('PDF', [('P', 'Portable'), ('D', 'Document'), ('F', 'Format')], 'Format de document portable', '<p>Format de fichier du registre de l’Office fédéral de la statistique, non relu pour ce cours.</p>')
if 'WHO' not in G:
    a('WHO', [('W', 'World'), ('H', 'Health'), ('O', 'Organization')], 'World Health Organization (Organisation mondiale de la santé)', '<p>Nom anglais de l’OMS, présent dans le titre original des lignes directrices.</p>', 'g09-oms')
if 'N-méthyl-D-aspartate' not in G:
    a('N-méthyl-D-aspartate', [('N-méthyl', 'substitution méthyle sur l’azote'), ('D', 'forme dextrogyre'), ('aspartate', 'acide aminé aspartique')], 'N-méthyl-D-aspartate', '<p>Substance qui donne son nom au récepteur NMDA.</p>', 'g09-nmda')
if 'Frühsommer-Meningoenzephalitis' not in G:
    a('Frühsommer-Meningoenzephalitis', [('Frühsommer', 'début d’été'), ('Meningo', 'méninges'), ('Enzephalitis', 'inflammation de l’encéphale')], 'Méningo-encéphalite verno-estivale (nom allemand)', '<p>Nom allemand de la méningo-encéphalite à tiques ; il a donné le sigle FSME.</p>', 'g09-fsme')
