"""Abréviations E59 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e59', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('OSAV', [('O', 'Office fédéral'), ('S', 'de la Sécurité'), ('A', 'Alimentaire (et des Affaires)'), ('V', 'Vétérinaires')],
              'Office fédéral de la sécurité alimentaire et des affaires vétérinaires',
              'L’OSAV publie les valeurs de référence nutritionnelles pour la Suisse (version de juin 2022) et l’étude de 2023 sur le statut en sélénium de la population suisse, source principale des repères épidémiologiques de ce cours.', 'e59-statut-suisse')
add_if_absent('ESPEN', [('E', 'European'), ('S', 'Society for'), ('P', 'Parenteral'), ('E', 'and Enteral'), ('N', 'Nutrition')],
              'Société européenne de nutrition clinique et de métabolisme (ancien nom : Société européenne de nutrition parentérale et entérale)',
              'Cette société savante a publié en 2022 des lignes directrices sur les micronutriments. Leur chapitre 11 sur le sélénium fournit les seuils plasmatiques, les doses et les recommandations 12.1 à 12.7 utilisés dans ce cours. Le niveau de preuve y est souvent bas.', 'e59-gradation')
add_if_absent('EFSA', [('E', 'European'), ('F', 'Food'), ('S', 'Safety'), ('A', 'Authority')],
              'Autorité européenne de sécurité des aliments',
              'Cette agence européenne a publié en 2023 un avis sur la limite supérieure d’apport tolérable en sélénium : 255 µg/jour chez l’adulte.', 'e59-ul-efsa')
add_if_absent('EUGOGO', [('EU', 'European'), ('G', 'Group'), ('O', 'On'), ('G', 'Graves’'), ('O', 'Orbitopathy')],
              'Groupe européen sur l’orbitopathie de Basedow',
              'Ce groupe européen a publié en 2021 des lignes directrices sur l’orbitopathie basedowienne. Elles retiennent une cure de sélénium de six mois dans la forme légère.', 'e59-orbitopathie')
add_if_absent('ICP-MS', [('I', 'Inductively'), ('C', 'Coupled'), ('P', 'Plasma'), ('M', 'Mass'), ('S', 'Spectrometry')],
              'Spectrométrie de masse couplée à un plasma inductif',
              'Méthode de dosage préférée des oligo-éléments, dont le sélénium plasmatique, selon les lignes directrices ESPEN 2022.', 'e59-se-plasma')
add_if_absent('D-A-CH', [('D', 'Deutschland (Allemagne)'), ('A', 'Austria, Österreich (Autriche)'), ('CH', 'Confoederatio Helvetica (Suisse)')],
              'Valeurs de référence germanophones (Allemagne, Autriche, Suisse)',
              'Valeurs de référence nutritionnelles communes aux pays germanophones. La révision de 2015 pour le sélénium est citée à propos de la grossesse et de l’allaitement.', 'e59-valeurs-suisses')
add_if_absent('LRP-8', [('L', 'Low-density lipoprotein'), ('R', 'Receptor-related'), ('P', 'Protein'), ('8', 'numéro 8')],
              'Protéine apparentée au récepteur des lipoprotéines de basse densité, numéro 8',
              'Récepteur par lequel la sélénoprotéine P délivre le sélénium aux tissus. Il porte aussi le nom d’ApoER-2.', 'e59-selenop')
add_if_absent('ApoER-2', [('Apo', 'Apolipoprotein (apolipoprotéine)'), ('E', 'E'), ('R', 'Receptor (récepteur)'), ('-2', 'numéro 2')],
              'Récepteur de l’apolipoprotéine E, numéro 2',
              'Autre nom du récepteur LRP-8, par lequel la sélénoprotéine P transporte le sélénium vers les tissus.', 'e59-selenop')
add_if_absent('E64.8', [('E', 'chapitre IV de la CIM-10-GM : maladies endocriniennes, nutritionnelles et métaboliques'), ('64', 'catégorie 64'), ('.8', 'subdivision 8 : séquelles d’autres carences nutritionnelles')],
              'Séquelles d’autres carences nutritionnelles',
              'Code qui reçoit les séquelles de carence en sélénium, exclues de E59 par la CIM-10-GM 2024.', 'e59-nosologie')
add_if_absent('E00.1', [('E', 'chapitre IV de la CIM-10-GM : maladies endocriniennes, nutritionnelles et métaboliques'), ('00', 'catégorie 00'), ('.1', 'subdivision 1 : type myxœdémateux')],
              'Syndrome d’insuffisance thyroïdienne congénitale de type myxœdémateux',
              'Code du crétinisme myxœdémateux endémique, associé à une carence combinée en iode et en sélénium. Il est distinct de E59.', 'e59-cretinisme')
add_if_absent('M12.1', [('M', 'lettre de la CIM-10-GM utilisée ici pour la rhumatologie'), ('12', 'catégorie 12'), ('.1', 'subdivision 1')],
              'Maladie de Kaschin-Beck',
              'Ostéoarthropathie endémique codée en rhumatologie, hors de E59, bien que la littérature la relie à la carence en sélénium et en iode.', 'e59-kashin')
add_if_absent('Kashin-Beck', [('Kashin-Beck', 'noms propres de deux auteurs, non une abréviation')],
              'Maladie de Kashin-Beck',
              'Ostéoarthropathie endémique des zones à carence en sélénium et en iode. La CIM-10-GM 2024 orthographie « Kaschin-Beck » et la code M12.1.', 'e59-kashin')
add_if_absent('Kaschin-Beck', [('Kaschin-Beck', 'orthographe de la CIM-10-GM, noms propres de deux auteurs, non une abréviation')],
              'Maladie de Kaschin-Beck',
              'Orthographe de la CIM-10-GM 2024 pour la maladie de Kashin-Beck, codée M12.1.', 'e59-kashin')
add_if_absent('Jenny-Burri', [('Jenny-Burri', 'nom de famille composé d’un auteur, non une abréviation')],
              'Jenny-Burri, premier auteur d’une étude suisse de 2010',
              'Cette étude de l’Office fédéral de la santé publique estime l’apport suisse de sélénium à environ 66 µg/jour en 2010.', 'e59-statut-suisse')
add_if_absent('GmbH', [('G', 'Gesellschaft'), ('m', 'mit'), ('b', 'beschränkter'), ('H', 'Haftung')],
              'Société à responsabilité limitée (forme juridique allemande)',
              'Forme juridique du titulaire de selenase®, Plavidente GmbH.', 'e59-d-selenase')
