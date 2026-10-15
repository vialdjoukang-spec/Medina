"""Abréviations E56 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e56', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('ESPEN', [('ESPEN', 'sigle conservé de l’ancien nom de la société ; son nom actuel est European Society for Clinical Nutrition and Metabolism')],
              'European Society for Clinical Nutrition and Metabolism (société européenne de nutrition clinique et de métabolisme)',
              'Cette société savante publie des directives de nutrition clinique. Celle de 2022 sur les micronutriments fonde les seuils de vitamine E et K de ce chapitre.', 'e56-sources-guides')
add_if_absent('ECFS', [('E', 'European'), ('C', 'Cystic'), ('F', 'Fibrosis'), ('S', 'Society')],
              'European Cystic Fibrosis Society (société européenne de mucoviscidose)',
              'Cette société a co-signé en 2016 avec ESPEN et ESPGHAN le guide nutritionnel de la mucoviscidose, source des doses de vitamines E et K chez ces patients.', 'e56-sources-guides')
add_if_absent('DGE', [('D', 'Deutsche'), ('G', 'Gesellschaft für'), ('E', 'Ernährung')],
              'Deutsche Gesellschaft für Ernährung (société allemande de nutrition)',
              'Cette société publie des valeurs de référence d’apport en vitamines. Ses valeurs pour les vitamines E et K sont citées sans valeur de recommandation suisse.', 'e56-sources-guides')
add_if_absent('SMOB', [('SMOB', 'sigle officiel de la Swiss Society for the Study of Morbid Obesity and Metabolic Disorders, non développé lettre à lettre dans la source')],
              'Swiss Society for the Study of Morbid Obesity and Metabolic Disorders',
              'Cette société suisse publie des directives pour le traitement chirurgical de l’obésité ; la version en vigueur dès le 1er juillet 2023 prévoit un suivi vitaminique annuel.', 'e56-bariatrique')
add_if_absent('VLDL', [('V', 'Very'), ('L', 'Low'), ('D', 'Density'), ('L', 'Lipoprotein')],
              'Very low density lipoprotein (lipoprotéine de très basse densité)',
              'Cette lipoprotéine transporte les lipides synthétisés par le foie. L’α-TTP y transfère l’α-tocophérol pour sa distribution aux tissus.', 'e56-attp')
add_if_absent('TTP', [('T', 'Tocopherol'), ('T', 'Transfer'), ('P', 'Protein')],
              'Tocopherol transfer protein (protéine de transfert de l’α-tocophérol)',
              'Cette protéine hépatique récupère l’α-tocophérol absorbé et le transfère aux lipoprotéines ; l’écriture α-TTP désigne la protéine dans le texte.', 'e56-attp')
add_if_absent('TTPA', [('TTPA', 'nom du gène codant l’α-TTP, non une abréviation à développer lettre à lettre')],
              'Gène TTPA (protéine de transfert de l’α-tocophérol)',
              'Ce gène code la protéine de transfert de l’α-tocophérol ; ses mutations causent l’ataxie avec carence en vitamine E, de transmission autosomique récessive.', 'e56-attp')
add_if_absent('MTTP', [('MTTP', 'nom du gène de la protéine microsomale de transfert des triglycérides, non développé lettre à lettre')],
              'Gène MTTP (protéine microsomale de transfert des triglycérides)',
              'Ses mutations causent l’abêtalipoprotéinémie, qui prive l’organisme des lipoprotéines transportant la vitamine E.', 'e56-attp')
add_if_absent('SAR1B', [('SAR1B', 'nom du gène de la maladie de rétention des chylomicrons, non développé lettre à lettre')],
              'Gène SAR1B',
              'Ses mutations causent la maladie de rétention des chylomicrons, qui entraîne une carence en vitamine E.', 'e56-attp')
add_if_absent('PIVKA', [('P', 'Protein'), ('I', 'Induced by'), ('V', 'Vitamin'), ('K', 'K'), ('A', 'Absence or antagonism')],
              'Protein induced by vitamin K absence or antagonism (protéine induite par l’absence ou l’antagonisme de la vitamine K)',
              'Ce terme désigne les formes incomplètement carboxylées des protéines vitamine K-dépendantes, inactives en coagulation.', 'e56-pivka')
add_if_absent('PIVKA-II', [('PIVKA', 'Protein induced by vitamin K absence or antagonism'), ('II', 'prothrombine, ou facteur II')],
              'Prothrombine sous-carboxylée',
              'La PIVKA-II est la prothrombine sous-carboxylée ; son élévation signale un déficit fonctionnel en vitamine K.', 'e56-pivka')
add_if_absent('FII', [('F', 'Facteur'), ('II', 'deux, prothrombine')],
              'Facteur II mesuré par le réactif du temps de prothrombine',
              'Il est comparé au facteur mesuré par l’écarine (FIIE) pour évoquer une carence en vitamine K.', 'e56-fii')
add_if_absent('FIIE', [('F', 'Facteur'), ('II', 'deux, prothrombine'), ('E', 'Écarine')],
              'Facteur II mesuré par l’écarine',
              'Il ne détecte que la prothrombine carboxylée active ; un rapport FII/FIIE inférieur à 0,86 évoque une carence.', 'e56-fii')
add_if_absent('TPGS', [('T', 'Tocophérol'), ('P', 'Polyéthylène'), ('G', 'Glycol'), ('S', 'Succinate')],
              'Succinate de tocophérol-polyéthylène glycol',
              'Forme hydrosoluble de vitamine E qui forme elle-même ses micelles, utile en cholestase.', 'e56-tpgs')
add_if_absent('RRR', [('RRR', 'désignation stéréochimique des trois centres du RRR-α-tocophérol naturel')],
              'RRR-α-tocophérol (forme naturelle de la vitamine E)',
              'Le préfixe RRR décrit la configuration des centres asymétriques de la forme naturelle ; son activité vaut le double de celle de la forme synthétique all-rac, à poids égal.', 'e56-vite-formes')
add_if_absent('K1', [('K1', 'vitamine K de type 1, phylloquinone')],
              'Vitamine K1 (phylloquinone)',
              'Forme végétale de la vitamine K, utilisée en supplémentation.', 'e56-vitk-formes')
add_if_absent('K2', [('K2', 'vitamine K de type 2, ménaquinones')],
              'Vitamine K2 (ménaquinones)',
              'Formes synthétisées par le microbiote intestinal et présentes dans les aliments fermentés et animaux.', 'e56-vitk-formes')
add_if_absent('K3', [('K3', 'vitamine K de type 3, ménadione')],
              'Vitamine K3 (ménadione)',
              'Provitamine de synthèse, toxique, indisponible.', 'e56-d-menadione')
add_if_absent('MK-2', [('MK', 'Ménaquinone'), ('2', 'longueur de la chaîne latérale')],
              'Ménaquinone-2',
              'Plus courte des ménaquinones citées (de MK-2 à MK-14).', 'e56-vitk-formes')
add_if_absent('MK-14', [('MK', 'Ménaquinone'), ('14', 'longueur de la chaîne latérale')],
              'Ménaquinone-14',
              'Plus longue des ménaquinones citées (de MK-2 à MK-14).', 'e56-vitk-formes')
add_if_absent('ATC', [('A', 'Anatomique'), ('T', 'Thérapeutique'), ('C', 'Chimique')],
              'Classification anatomique, thérapeutique et chimique',
              'Système de classement des médicaments dont le code accompagne l’information professionnelle.', 'e56-d-konakion')
add_if_absent('A11HA03', [('A11HA03', 'code ATC de l’acétate d’α-tocophéryle, non une abréviation')],
              'Code ATC A11HA03',
              'Code ATC d’Ephynal.', 'e56-d-ephynal')
add_if_absent('B02BA01', [('B02BA01', 'code ATC de la phytoménadione, non une abréviation')],
              'Code ATC B02BA01',
              'Code ATC de Konakion.', 'e56-d-konakion')
add_if_absent('E56.0', [('E56.0', 'code CIM-10-GM : carence en vitamine E')],
              'Code E56.0',
              'Sous-code de la catégorie E56.', 'e56-codes')
add_if_absent('E56.1', [('E56.1', 'code CIM-10-GM : carence en vitamine K')],
              'Code E56.1',
              'Sous-code de la catégorie E56.', 'e56-codes')
add_if_absent('E56.8', [('E56.8', 'code CIM-10-GM : carence en autres vitamines')],
              'Code E56.8',
              'Sous-code de la catégorie E56 dont le contenu n’est pas détaillé dans les sources lues.', 'e56-codes')
add_if_absent('E56.9', [('E56.9', 'code CIM-10-GM : avitaminose, sans précision')],
              'Code E56.9',
              'Sous-code de la catégorie E56.', 'e56-codes')
add_if_absent('E64.8', [('E64.8', 'code CIM-10-GM : séquelles d’autres avitaminoses')],
              'Code E64.8',
              'Code exclu de la catégorie E56.', 'e56-codes')
add_if_absent('D68.4', [('D68.4', 'code CIM-10-GM : carence acquise en facteurs de la coagulation')],
              'Code D68.4',
              'Code exclu de E56.1.', 'e56-codes')
add_if_absent('SpiGes', [('SpiGes', 'sigle officiel du relevé suisse des séjours hospitaliers stationnaires, non développé lettre à lettre dans la source')],
              'SpiGes (relevé suisse des séjours hospitaliers stationnaires)',
              'Relevé des séjours stationnaires, codé en CIM-10-GM 2024 en français depuis le 1er janvier 2025.', 'e56-spiges')
add_if_absent('SL', [('S', 'Spécialités'), ('L', 'Liste')],
              'Liste des spécialités (SL) de l’assurance de base',
              'Liste fédérale des médicaments pris en charge par l’assurance obligatoire des soins.', 'e56-sl')
add_if_absent('SSP', [('S', 'Situations'), ('S', 'as'), ('P', 'Starting Points')],
              'Situations as Starting Points (situations de départ de la liste PROFILES)',
              'Motif de consultation que le futur médecin doit savoir aborder ; ce chapitre se rattache pédagogiquement aux situations 16, 138 et 170.', 'e56-profiles')
add_if_absent('PROFILES', [('PROFILES', 'nom du catalogue suisse d’objectifs de formation médicale, non développé lettre à lettre dans la source')],
              'PROFILES (catalogue suisse d’objectifs de la formation médicale)',
              'Catalogue d’objectifs d’apprentissage de la formation médicale suisse.', 'e56-profiles')
add_if_absent('U69.11', [('U69.11', 'code supplémentaire CIM-10-GM : trouble durablement acquis')],
              'Code U69.11!', 'Code supplémentaire de D68.4 pour un trouble durablement acquis.', 'e56-codes')
add_if_absent('U69.12', [('U69.12', 'code supplémentaire CIM-10-GM : trouble provisoire')],
              'Code U69.12!', 'Code supplémentaire de D68.4 pour un trouble provisoire.', 'e56-codes')
