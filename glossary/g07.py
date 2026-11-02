"""Abréviations G07 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g07', '__init__'}:
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

for _code, _txt in [
    ('A06.6', "Code à croix de la CIM-10-GM 2024 associé à l’abcès cérébral amibien dans la catégorie G07*. Le libellé français officiel a été relu dans le fichier OFS 2024 pour la version G07 du 2 novembre 2026 ; les notes contextuelles restent à vérifier dans la classification applicable."),
    ('A54.8', "Code à croix de la CIM-10-GM 2024 associé à l’abcès cérébral gonococcique dans la catégorie G07*. Le libellé français officiel a été relu dans le fichier OFS 2024 pour la version G07 du 2 novembre 2026 ; les notes contextuelles restent à vérifier dans la classification applicable."),
    ('A17.8', "Code à croix de la CIM-10-GM 2024 associé à l’abcès cérébral tuberculeux et au tuberculome cérébral dans la catégorie G07*. Le libellé français officiel a été relu dans le fichier OFS 2024 pour la version G07 du 2 novembre 2026 ; les notes contextuelles restent à vérifier dans la classification applicable."),
    ('A17.1', "Code à croix de la CIM-10-GM 2024 associé au tuberculome méningé dans la catégorie G07*. Le libellé français officiel a été relu dans le fichier OFS 2024 pour la version G07 du 2 novembre 2026 ; les notes contextuelles restent à vérifier dans la classification applicable.")]:
    add_if_absent(_code, [(_code, 'code de classification, non une abréviation')], 'Code à croix ' + _code, _txt, 'g07-asterisque')

add_if_absent('2HRZE', [('2', 'durée de la phase en mois'), ('H', 'isoniazide'), ('R', 'rifampicine'), ('Z', 'pyrazinamide'), ('E', 'éthambutol')],
              'Phase intensive de deux mois : isoniazide, rifampicine, pyrazinamide, éthambutol',
              'Notation du guide suisse de l’OFSP : deux mois de quatre médicaments antituberculeux. Les initiales suivent la composition de l’association fixe Rimstar.', 'g07-schema')
add_if_absent('10HR', [('10', 'durée de la phase en mois'), ('H', 'isoniazide'), ('R', 'rifampicine')],
              'Phase de continuation de dix mois : isoniazide, rifampicine',
              'Notation du guide suisse de l’OFSP : dix mois de deux médicaments antituberculeux, après la phase intensive.', 'g07-schema')
add_if_absent('IFT', [('I', 'Immuno'), ('F', 'Fluorescence'), ('T', 'Test')], 'Test d’immunofluorescence',
              'Test sérologique cité avec l’ELISA comme test de dépistage de la schistosomiase dans la recommandation allemande de 2017. Ce passage historique ne fonde pas une recommandation actuelle dans cette leçon.', 'g07-schisto-meca')
add_if_absent('PET-CT', [('P', 'Positron'), ('E', 'Emission'), ('T', 'Tomography'), ('-', 'couplée à'), ('C', 'Computed'), ('T', 'Tomography')],
              'Tomographie par émission de positons couplée à la tomodensitométrie',
              'Modalité d’imagerie citée dans le dossier historique allemand 2017. Cette référence échue ne démontre pas une performance universelle ni une indication actuelle de neuroschistosomiase dans la présente leçon.', 'g07-schisto-meca')
add_if_absent('POC-CCA', [('POC', 'Point-Of-Care'), ('CCA', 'Circulating Cathodic Antigen')], 'Antigène cathodique circulant au chevet du patient',
              'Test rapide de détection d’un antigène de schistosome. La directive allemande historique de 2017 n’est pas utilisée comme recommandation actuelle dans cette leçon.', 'g07-schisto-meca')
add_if_absent('MetronidazoleSINT', [('MetronidazoleSINT', 'nom commercial, non une abréviation')], 'MetronidazoleSINT i.v., nom commercial',
              'Spécialité de métronidazole par voie intraveineuse dont l’information professionnelle suisse (février 2026) a été lue pour cette leçon.', 'g07-m-metro')

# Noms d’étude, de société et de marque employés dans la reprise G07 du 2 novembre 2026.
add_if_absent('HARVEST', [('HARVEST', 'nom propre de l’essai, non décomposé en initiales inventées')], 'Essai de rifampicine à forte dose dans la méningite tuberculeuse', 'Essai international de 2025 chez l’adulte ; son critère principal ne montre pas de bénéfice de survie du schéma à forte dose étudié.', 'g07-harvest')
add_if_absent('BASHH', [('B', 'British'), ('A', 'Association'), ('S', 'Sexual'), ('H', 'Health'), ('H', 'HIV')], 'British Association for Sexual Health and HIV', 'Société britannique de santé sexuelle ; son guide gonococcique 2025 est distingué d’une recommandation IUSTI.', 'g07-r5')
add_if_absent('SINT', [('SINT', 'élément de nom commercial, non une abréviation médicale à développer')], 'Metronidazole SINT i.v.', 'Spécialité suisse exacte de métronidazole ; le nom ne prouve pas une dose spécifique d’atteinte cérébrale amibienne.', 'g07-m-metro')
