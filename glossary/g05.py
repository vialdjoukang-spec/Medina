'Abréviations G05 (Encéphalite, myélite et encéphalomyélite au cours d’affections classées ailleurs) ; ajouts conditionnels, sans mutation des glossaires existants.'
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g05', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('HSV', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus')], 'Virus de l’herpès simplex', 'HSV peut provoquer une encéphalite ; le diagnostic associe clinique, LCR et imagerie. Une suspicion préoccupante justifie l’aciclovir sans attendre la PCR.', 'g05-hsve')
add_if_absent('EBV', [('E', 'Epstein'), ('B', 'Barr'), ('V', 'Virus')], 'Virus d’Epstein-Barr', 'Virus recherché selon le terrain, notamment immunodépression. Une détection moléculaire demande une attribution clinique ; elle ne prouve pas seule la cause de l’encéphalite.', 'g05-cmv')
add_if_absent('JCV', [('JC', 'nom d’usage du virus JC, non développé lettre à lettre dans les sources lues'), ('V', 'Virus')], 'Virus JC', 'Agent à considérer notamment dans les atteintes neurologiques de l’immunodéprimé, selon clinique et imagerie.', 'g05-pcr')
add_if_absent('HHV-6', [('H', 'Human'), ('H', 'Herpes'), ('V', 'Virus'), ('6', 'type 6')], 'Virus herpès humain de type 6', 'Recherche orientée par terrain et présentation ; un résultat positif ne se substitue pas à l’attribution clinique.', 'g05-pcr')
add_if_absent('LCMV', [('L', 'Lymphocytic'), ('C', 'Choriomeningitis'), ('M', 'Mammarenavirus (nom d’usage)'), ('V', 'Virus')], 'Virus de la chorioméningite lymphocytaire', 'Recherche spécialisée selon exposition et contexte ; pas examen systématique de toute encéphalite.', 'g05-pcr')
add_if_absent('NGS', [('N', 'Next'), ('G', 'Generation'), ('S', 'Sequencing')], 'Séquençage de nouvelle génération', 'Approche exploratoire spécialisée lorsque le bilan ciblé n’explique pas la maladie ; ne remplace pas les tests urgents.', 'g05-pcr')
add_if_absent('ADEM', [('A', 'Acute'), ('D', 'Disseminated'), ('E', 'Encephalo'), ('M', 'Myelitis')], 'Encéphalomyélite aiguë disséminée', 'Processus immunitaire post- ou para-infectieux, cité dans le diagnostic différentiel de l’encéphalite.', 'g05-graus')
add_if_absent('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft'), ('N', 'für Neurologie')], 'Société allemande de neurologie', 'Recommandations virales 2025 et neurosyphilis 2026 relues, avec distinction de leurs dates, populations et niveaux de preuve.', 'g05-criteres')
add_if_absent('SNG', [('S', 'Schweizerische'), ('N', 'Neurologische'), ('G', 'Gesellschaft')], 'Société suisse de neurologie', 'Société représentée dans l’élaboration de la recommandationDGN 2025 sur les méningo-encéphalites virales.', 'g05-criteres')
add_if_absent('MONALISA', [('MONALISA', 'nom de la cohorte nationale prospective française de listériose ; la publication lue ne fournit aucun développement littéral')], 'Cohorte française MONALISA', 'Cohorte 2009–2013 :252 formes neurologiques parmi 818 listérioses. Les associations de traitement et mortalité sont observationnelles, sans preuve causale automatique.', 'g05-listeria')
add_if_absent('GACHE', [('GACHE', 'nom d’un essai, non développé lettre à lettre dans la source lue')], 'Essai GACHE', 'Essai sur la corticothérapie de l’encéphalite herpétique discuté dans les recommandations ; les données ne justifient pas une corticothérapie systématique.', 'g05-dexa')
add_if_absent('DexEnceph', [('DexEnceph', 'nom d’un essai, non développé lettre à lettre dans la source lue')], 'Essai DexEnceph', 'L’EAN/ESCMID 2026 analyse 94 participants randomisés, sans amélioration des critères principal et secondaires rapportés. Ne plus le présenter comme simplement non publié.', 'g05-dexa')
add_if_absent('FTA-ABS', [('FTA', 'Fluorescent Treponemal Antibody'), ('ABS', 'Absorption')], 'Test tréponémique fluorescent avec absorption', 'Les tests tréponémiques peuvent rester positifs durablement après traitement ; ils ne constituent pas seuls un suivi d’activité.', 'g05-neurosyphilis')
add_if_absent('TPLA', [('TP', 'Treponema Pallidum'), ('LA', 'Latex Agglutination')], 'Agglutination de particules de latex de Treponema pallidum', 'Test tréponémique de la sérologie syphilitique, avec TPPA et TPHA.', 'g05-neurosyphilis')
add_if_absent('ROR', [('R', 'Rougeole'), ('O', 'Oreillons'), ('R', 'Rubéole')], 'Vaccin rougeole, oreillons, rubéole', 'Prévention suisse : doses à 9 et 12 mois et rattrapage selon statut ; stratégie distincte de la vaccination contre les tiques.', 'g05-fsme')
add_if_absent('ROR-V', [('R', 'Rougeole'), ('O', 'Oreillons'), ('R', 'Rubéole'), ('V', 'Varicelle')], 'Vaccin rougeole, oreillons, rubéole, varicelle', 'Vaccin combiné préféré depuis 2023 dans les recommandationsOFSP relues.', 'g05-fsme')
add_if_absent('FSME', [('F', 'Früh'), ('S', 'Sommer'), ('M', 'Meningo'), ('E', 'Enzephalitis')], 'Encéphalite à tiques (Frühsommer-Meningoenzephalitis)', 'Maladie à déclaration obligatoire en Suisse ; elle se code A84 sans lien avec G05.1*.', 'g05-fsme')
add_if_absent('PLED', [('P', 'Periodic'), ('L', 'Lateralized'), ('E', 'Epileptiform'), ('D', 'Discharges')], 'Décharges épileptiformes latéralisées périodiques', 'Aspect de l’EEG décrit dans l’encéphalite herpétique.', 'g05-eeg')
add_if_absent('GCS', [('G', 'Glasgow'), ('C', 'Coma'), ('S', 'Scale')], 'Échelle de coma de Glasgow', 'Mesure de vigilance ; un score inférieur à 12 était associé à la mortalité à 6 mois dans la cohorte danoise, sans être un pronostic individuel certain.', 'g05-hsve')
add_if_absent('anti-NMDAR', [('anti', 'dirigé contre'), ('N', 'N-'), ('M', 'Méthyl-'), ('D', 'D-'), ('A', 'Aspartate'), ('R', 'Receptor (récepteur)')], 'Anticorps dirigés contre le récepteur NMDA', 'DesIgG anti-GluN1 dans un contexte compatible soutiennent une encéphalite auto-immune ; sérum et LCR se complètent. Une rechute après HSV peut relever de ce mécanisme.', 'g05-antinmda')
add_if_absent('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'Académie européenne de neurologie', 'Recommandation conjointeEAN/ESCMID 2026 sur l’encéphalite virale adulte, réellement lue par questionsPICO et recommandations pour cette version.', 'g05-criteres')
add_if_absent('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')], 'Fédération européenne des sociétés neurologiques', 'Organisation historique citée dans la littérature ; la référence actuelle utilisée ici estEAN/ESCMID 2026.', 'g05-lacunes')
add_if_absent('Foix-Alajouanine', [('Foix-Alajouanine', 'nom propre de deux médecins, non une abréviation')], 'Syndrome de Foix-Alajouanine', 'Myélite nécrosante subaiguë, exclue de G04 par la CIM-10-GM 2024.', 'g05-codage')
for _k, _t, _w in [
    ('G04.8', 'encéphalite auto-immune (hors G05)', 'g05-graus'),
    ('G05.0', 'au cours d’infections bactériennes classées ailleurs', 'g05-codage'),
    ('G05.1', 'au cours d’infections virales classées ailleurs', 'g05-codage'),
    ('G05.2', 'au cours d’autres maladies infectieuses et parasitaires classées ailleurs', 'g05-codage'),
    ('G05.8', 'au cours d’autres maladies classées ailleurs', 'g05-codage'),
    ('G31.2', 'encéphalopathie alcoolique', 'g05-codage'),
    ('G37.3', 'myélite transverse aiguë', 'g05-codage'),
    ('G37.4', 'syndrome de Foix-Alajouanine', 'g05-codage'),
    ('G93.4', 'encéphalopathie sans précision', 'g05-codage'),
    ('A17.8', 'tuberculose', 'g05-codage'),
    ('A32.1', 'Listeria', 'g05-codage'),
    ('A39.8', 'méningocoque', 'g05-codage'),
    ('A50.4', 'syphilis congénitale', 'g05-codage'),
    ('A52.1', 'syphilis tardive', 'g05-codage'),
    ('A85.0', 'entérovirus', 'g05-codage'),
    ('A85.1', 'adénovirus', 'g05-codage'),
    ('B00.4', 'herpès simplex', 'g05-codage'),
    ('B01.1', 'varicelle', 'g05-codage'),
    ('B02.0', 'zona', 'g05-codage'),
    ('B05.0', 'rougeole', 'g05-codage'),
    ('B06.0', 'rubéole', 'g05-codage'),
    ('B26.2', 'oreillons', 'g05-codage'),
    ('B25.88', 'cytomégalovirus', 'g05-codage'),
    ('B57.4', 'maladie de Chagas chronique', 'g05-codage'),
    ('B58.2', 'toxoplasmose', 'g05-codage'),
    ('B60.2', 'Naegleria', 'g05-codage'),
    ('B83.2', 'méningo-encéphalite à éosinophiles', 'g05-codage'),
    ('J10.8', 'grippe', 'g05-codage'),
    ('J11.8', 'grippe', 'g05-codage'),
    ('M32.1', 'encéphalopathie du lupus érythémateux systémique', 'g05-lupus'),
]:
    add_if_absent(_k, [(_k, 'code de la CIM-10-GM 2024, non une abréviation')], _t,
                  'Code de la CIM-10-GM 2024 cité dans ce cours, associé à : ' + _t + '.', _w)
add_if_absent('AQP4', [('AQP4', 'Aquaporine4')], 'Aquaporine4', 'Canal hydrique ; lesIgG anti-AQP4 s’interprètent avec les critèresNMOSD et un test cellulaire sérique.', 'g05-myelite')
add_if_absent('MOG', [('MOG', 'Glycoprotéine de la myéline des oligodendrocytes')], 'Glycoprotéine de la myéline des oligodendrocytes', 'Antigène recherché par test cellulaire sérique dans les tableaux compatibles ; un faible titre discordant doit être confirmé.', 'g05-myelite')
add_if_absent('NMOSD', [('NMOSD', 'Maladies du spectre de la neuromyélite optique')], 'Maladies du spectre de la neuromyélite optique', 'Atteintes optiques, médullaires ou du tronc selon critères ; la longueur médullaire seule ne suffit pas au diagnostic.', 'g05-myelite')
add_if_absent('TMP', [('TMP', 'Triméthoprime')], 'Triméthoprime', 'Composant du cotrimoxazole ; écrire sa dose séparément de celle du sulfaméthoxazole.', 'g05-pyrimethamine')
add_if_absent('SMX', [('SMX', 'Sulfaméthoxazole')], 'Sulfaméthoxazole', 'Composant du cotrimoxazole, dans un rapport pondéral 1:5 avecTMP pour le produit décrit.', 'g05-pyrimethamine')
add_if_absent('DPD', [('DPD', 'Dihydropyrimidine déshydrogénase')], 'Dihydropyrimidine déshydrogénase', 'Enzyme inhibée par un métabolite de la brivudine ; interaction potentiellement mortelle avec fluoropyrimidines.', 'g05-brivudine')
add_if_absent('LETM', [('LETM', 'Myélite longitudinalement étendue')], 'Myélite longitudinalement étendue', 'Lésion d’au moins trois segments vertébraux contigus ; elle oriente le bilan sans définir seuleNMOSD.', 'g05-myelite')

add_if_absent('PL', [('PL', 'Ponction lombaire')], 'Ponction lombaire', 'Prélèvement du liquide cérébro-spinal après évaluation de sa sécurité ; ne doit pas retarder un traitement urgent si elle est différée.', 'g05-lcr')
add_if_absent('NFS', [('NFS', 'Numération formule sanguine')], 'Numération formule sanguine', 'Hémogramme surveillant notamment neutrophiles, hémoglobine et plaquettes sous traitements myélotoxiques.', 'g05-ganciclovir')
add_if_absent('PO', [('PO', 'Par voie orale')], 'Par voie orale', 'La voie orale ne remplace pas automatiquement la voie intraveineuse dans une infection neurologique.', 'g05-pyrimethamine')
add_if_absent('IQR', [('IQR', 'Intervalle interquartile')], 'Intervalle interquartile', 'Intervalle entre premier et troisième quartiles, décrivant la dispersion dans la cohorte citée.', 'g05-hsve')
add_if_absent('GluN1', [('GluN1', 'Sous-unité GluN1 du récepteur NMDA')], 'Sous-unité GluN1 du récepteur NMDA', 'Cible des IgG pertinentes dans l’encéphalite anti-NMDAR ; interprétation avec syndrome et sérum/LCR.', 'g05-antinmda')
add_if_absent('DHFR', [('DHFR', 'Dihydrofolate-réductase')], 'Dihydrofolate-réductase', 'Enzyme de la voie des folates inhibée notamment par la pyriméthamine ; le folinate fournit une forme réduite.', 'g05-pyrimethamine')
add_if_absent('SMC', [('SMC', 'Swiss Memory Clinics')], 'Swiss Memory Clinics', 'Document suisse2024 fournissant les repères de LCR lombaire adulte cités ; ce n’est pas un guide OFSP sur l’encéphalite.', 'g05-lcr')
add_if_absent('MEBEKO', [('MEBEKO', 'Commission des professions médicales')], 'Commission des professions médicales', 'Les exigences2026 de l’examen fédéral de médecine humaine sont utilisées pour distinguer le cadre pédagogique applicable.', 'g05-lacunes')
add_if_absent('QT', [('QT', 'Intervalle QT de l’électrocardiogramme')], 'Intervalle QT de l’électrocardiogramme', 'Sa prolongation est un enjeu de sécurité avec le foscarnet et certains troubles électrolytiques.', 'g05-foscarnet')
add_if_absent('UL97', [('UL97', 'Protéine kinase virale UL97')], 'Protéine kinase virale UL97', 'Participe à l’activation du ganciclovir dans les cellules infectées par CMV.', 'g05-ganciclovir')
add_if_absent('UL54', [('UL54', 'Polymérase virale UL54')], 'Polymérase virale UL54', 'Cible du ganciclovir activé ; certaines modifications sont associées à la résistance.', 'g05-ganciclovir')
add_if_absent('T6', [('T6', 'Sixième segment thoracique')], 'Sixième segment thoracique', 'Niveau de la coupe médullaire historique TH.VI de la figure2 ; ne désigne pas le niveau clinique de chaque myélite.', 'g05-myelite')
add_if_absent('EPA2', [('EPA2', 'Activité professionnelle confiable2 de PROFILES2017')], 'Activité professionnelle confiable2 de PROFILES2017', 'Examen clinique incluant les fonctions neurologiques et le coma dans les passages relus.', 'g05-criteres')
add_if_absent('EPA6', [('EPA6', 'Activité professionnelle confiable6 de PROFILES2017')], 'Activité professionnelle confiable6 de PROFILES2017', 'Gestes et procédures ; les correspondances de cette leçon sont pédagogiques, pas une validation de compétence.', 'g05-criteres')
add_if_absent('EPA6a', [('EPA6a', 'Sous-activité6a de PROFILES2017')], 'Sous-activité6a de PROFILES2017', 'Renvoi pédagogique au document officiel ; ne pas confondre les identifiants des versions2017 et2023.', 'g05-criteres')

add_if_absent('Sulfadiazin-Heyl', [('Sulfadiazin-Heyl', 'nom de produit, non une abréviation')], 'Sulfadiazin-Heyl 500 mg', 'Nom du produit allemand de sulfadiazine ; son RCP plafonne à 4 g/j chez l’adulte. La présence d’un RCP ne prouve pas une disponibilité suisse.', 'g05-pyrimethamine')
add_if_absent('ADIAZINE', [('ADIAZINE', 'nom de produit, non une abréviation')], 'ADIAZINE 500 mg', 'Nom du produit français de sulfadiazine ; sa posologie adulte 4–6 g/j ne se substitue pas à celle d’un autre produit.', 'g05-pyrimethamine')
add_if_absent('BioFire', [('BioFire', 'nom de produit, non une abréviation')], 'Panel moléculaire BioFire', 'Nom commercial, non développé lettre par lettre. Un panel multiplex ne remplace pas toujours une PCR ciblée HSV en cas de forte suspicion.', 'g05-pcr')
