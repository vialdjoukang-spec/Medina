"""Abréviations G92 ; entrées conditionnelles, sans mutation des glossaires existants."""
from cardio_1 import a, G
if 'ASTCT' not in G:
    a('ASTCT', [('A', 'American'), ('S', 'Society for'), ('T', 'Transplantation and'), ('CT', 'Cellular Therapy')], 'American Society for Transplantation and Cellular Therapy', '<p>Société américaine dont le consensus de 2019 définit les grades du syndrome de relargage de cytokines et de la neurotoxicité des cellules effectrices immunitaires. Les sources européennes lues reprennent ces grades.</p>', 'g92-grade')
if 'BfArM' not in G:
    a('BfArM', [('B', 'Bundesinstitut'), ('f', 'für'), ('Ar', 'Arzneimittel und'), ('M', 'Medizinprodukte')], 'Bundesinstitut für Arzneimittel und Medizinprodukte', '<p>Institut fédéral allemand des médicaments et dispositifs médicaux, éditeur de la CIM-10-GM. Il n’est pas une source de conduite thérapeutique.</p>')
if 'CAPD' not in G:
    a('CAPD', [('C', 'Cornell'), ('A', 'Assessment of'), ('P', 'Pediatric'), ('D', 'Delirium')], 'Cornell Assessment of Pediatric Delirium', '<p>Échelle de huit items qui remplace le score ICE chez l’enfant de moins de 12 ans ; un score de 9 ou plus indique un délire probable.</p>', 'g92-ice')
if 'CAR-T' not in G:
    a('CAR-T', [('CAR', 'Chimeric Antigen Receptor'), ('T', 'lymphocytes T')], 'Lymphocytes T à récepteur chimérique pour l’antigène', '<p>Lymphocytes T prélevés ou donnés, modifiés pour reconnaître un antigène tumoral, puis perfusés. Ils peuvent provoquer un syndrome de relargage de cytokines et un ICANS.</p>', 'g92-crs')
if 'CARTOX-10' not in G:
    a('CARTOX-10', [('CAR', 'CAR-T-cell therapy'), ('TOX', 'TOXicity'), ('10', 'dix points')], 'Échelle de toxicité associée aux CAR-T sur dix points', '<p>Échelle de dépistage dont le score ICE est dérivé, avec des éléments du MMSE.</p>', 'g92-ice')
if 'CD4' not in G:
    a('CD4', [('CD', 'Cluster of Differentiation'), ('4', 'numéro 4')], 'Groupe de différenciation 4', '<p>Marqueur des lymphocytes T auxiliaires. Dans la revue européenne, la prophylaxie anti-Pneumocystis est poursuivie jusqu’à ce que les CD4 dépassent 200/µL.</p>')
if 'CIBMTR' not in G:
    a('CIBMTR', [('C', 'Center for'), ('I', 'International'), ('B', 'Blood and'), ('M', 'Marrow'), ('T', 'Transplant'), ('R', 'Research')], 'Center for International Blood and Marrow Transplant Research', '<p>Registre américain cité pour les délais d’apparition des événements après lisocabtagène maraleucel ; données descriptives.</p>')
if 'CIM-10-GM' not in G:
    a('CIM-10-GM', [('CIM', 'Classification Internationale des Maladies,'), ('10', 'dixième révision,'), ('GM', 'German Modification')], 'Classification internationale des maladies, 10e révision, modification allemande', '<p>Classification utilisée en Suisse pour le catalogue des diagnostics ; version 2024 du BfArM.</p>')
if 'CMV' not in G:
    a('CMV', [('C', 'Cyto'), ('M', 'Méga'), ('V', 'Virus')], 'Cytomégalovirus', '<p>Virus dont la PCR dans le liquide cérébrospinal exclut une infection du système nerveux central en cas de doute.</p>', 'g92-lemp')
if 'COVID-19' not in G:
    a('COVID-19', [('CO', 'COrona'), ('VI', 'VIrus'), ('D', 'Disease'), ('19', '2019')], 'Maladie à coronavirus 2019', '<p>Maladie dont la forme grave en réanimation s’accompagne souvent d’une encéphalopathie aiguë.</p>')
if 'CRES' not in G:
    a('CRES', [('C', 'CAR-T-cell-'), ('R', 'Related'), ('E', 'Encephalopathy'), ('S', 'Syndrome')], 'Syndrome d’encéphalopathie associé aux CAR-T', '<p>Ancien terme remplacé par ICANS.</p>', 'g92-icans')
if 'EBMT-JACIE-EHA' not in G:
    a('EBMT-JACIE-EHA', [('EBMT', 'European Society for Blood and Marrow Transplantation'), ('JACIE', 'Joint Accreditation Committee ISCT-Europe and EBMT'), ('EHA', 'European Hematology Association')], 'Recommandations européennes de 2021 sur les CAR-T', '<p>Recommandations dont le texte intégral n’a pas été lu ; seul le résumé est utilisé.</p>')
if 'EBV' not in G:
    a('EBV', [('E', 'Epstein-'), ('B', 'Barr'), ('V', 'Virus')], 'Virus d’Epstein-Barr', '<p>Virus recherché par PCR dans le liquide cérébrospinal en cas de doute infectieux.</p>', 'g92-lemp')
if 'EEG' not in G:
    a('EEG', [('É', 'Électro'), ('E', 'Encéphalo'), ('G', 'Gramme')], 'Électroencéphalogramme', '<p>Examen indiqué pour tout ICANS de grade 2 ou plus afin de détecter des crises non convulsives.</p>', 'g92-eeg')
if 'ESMO' not in G:
    a('ESMO', [('E', 'European'), ('S', 'Society for'), ('M', 'Medical'), ('O', 'Oncology')], 'European Society for Medical Oncology', '<p>Société européenne dont les recommandations de 2022 n’ont pas pu être lues en texte intégral.</p>')
if 'FLAIR' not in G:
    a('FLAIR', [('FL', 'FLuid'), ('A', 'Attenuated'), ('I', 'Inversion'), ('R', 'Recovery')], 'Séquence d’IRM à inversion-récupération avec atténuation du liquide', '<p>Séquence d’IRM où un hypersignal de la substance blanche évoque une leucoencéphalopathie.</p>', 'g92-irm')
if 'HHV-6' not in G:
    a('HHV-6', [('H', 'Human'), ('H', 'Herpes'), ('V', 'Virus'), ('6', 'type 6')], 'Herpèsvirus humain de type 6', '<p>Virus opportuniste à évoquer devant tout événement neurologique après CAR-T.</p>', 'g92-lemp')
if 'HSV' not in G:
    a('HSV', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus')], 'Virus herpès simplex', '<p>Virus recherché par PCR dans le liquide cérébrospinal.</p>', 'g92-lemp')
if 'ICANS' not in G:
    a('ICANS', [('I', 'Immune effector'), ('C', 'Cell-'), ('A', 'Associated'), ('N', 'Neurotoxicity'), ('S', 'Syndrome')], 'Syndrome de neurotoxicité associé aux cellules effectrices immunitaires', '<p>Atteinte du système nerveux central après une immunothérapie qui active des lymphocytes T ou d’autres cellules effectrices. C’est le contenu de G92.0.</p>', 'g92-icans')
if 'ICE' not in G:
    a('ICE', [('I', 'Immune effector'), ('C', 'Cell-associated'), ('E', 'Encephalopathy')], 'Encéphalopathie associée aux cellules effectrices immunitaires', '<p>Score de dépistage sur dix points : orientation, dénomination, exécution d’ordres, écriture, attention.</p>', 'g92-ice')
if 'IRM' not in G:
    a('IRM', [('I', 'Imagerie par'), ('R', 'Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique', '<p>Examen qui montre l’œdème, exclut un accident vasculaire et caractérise une leucoencéphalopathie.</p>', 'g92-irm')
if 'LEMP' not in G:
    a('LEMP', [('L', 'Leuco'), ('E', 'Encéphalopathie'), ('M', 'Multifocale'), ('P', 'Progressive')], 'Leucoencéphalopathie multifocale progressive', '<p>Infection opportuniste du système nerveux central à exclure devant un événement neurologique après CAR-T.</p>', 'g92-lemp')
if 'MMSE' not in G:
    a('MMSE', [('M', 'Mini-'), ('M', 'Mental'), ('S', 'State'), ('E', 'Examination')], 'Mini-Mental State Examination', '<p>Échelle cognitive dont certains éléments se retrouvent dans l’échelle CARTOX-10.</p>', 'g92-ice')
if 'NMDA' not in G:
    a('NMDA', [('N', 'N-'), ('M', 'Méthyl-'), ('D', 'D-'), ('A', 'Aspartate')], 'N-méthyl-D-aspartate', '<p>Récepteur du glutamate dont les agonistes sont élevés dans le liquide cérébrospinal de l’ICANS ; leur rôle est discuté.</p>')
if 'PCR' not in G:
    a('PCR', [('P', 'Polymerase'), ('C', 'Chain'), ('R', 'Reaction')], 'Réaction en chaîne par polymérase', '<p>Technique qui détecte le génome d’un virus dans le liquide cérébrospinal.</p>')
if 'POLG' not in G:
    a('POLG', [('POL', 'POLymérase'), ('G', 'Gamma')], 'Polymérase gamma (gène)', '<p>Gène des maladies mitochondriales (syndrome d’Alpers-Huttenlocher) qui exposent à une insuffisance hépatique fatale sous valproate.</p>', 'g92-valproate')
if 'SRC' not in G:
    a('SRC', [('S', 'Syndrome de'), ('R', 'Relargage de'), ('C', 'Cytokines')], 'Syndrome de relargage de cytokines', '<p>Cascade inflammatoire déclenchée par les CAR-T ; le tocilizumab le traite.</p>', 'g92-crs')
if 'VZV' not in G:
    a('VZV', [('V', 'Varicella-'), ('Z', 'Zoster'), ('V', 'Virus')], 'Virus varicelle-zona', '<p>Virus recherché par PCR dans le liquide cérébrospinal.</p>', 'g92-lemp')
if 'ZUMA-1' not in G:
    a('ZUMA-1', [('ZUMA-1', 'nom d’essai, non développable lettre à lettre')], 'Essai ZUMA-1', '<p>Essai pivot de l’axicabtagène ciloleucel cité par l’information professionnelle de Yescarta.</p>')
if 'ZUMA-5' not in G:
    a('ZUMA-5', [('ZUMA-5', 'nom d’essai, non développable lettre à lettre')], 'Essai ZUMA-5', '<p>Essai de l’axicabtagène ciloleucel dans le lymphome folliculaire, cité par l’information professionnelle de Yescarta.</p>')
if 'ZUMA-7' not in G:
    a('ZUMA-7', [('ZUMA-7', 'nom d’essai, non développable lettre à lettre')], 'Essai ZUMA-7', '<p>Essai de l’axicabtagène ciloleucel cité par l’information professionnelle de Yescarta.</p>')
