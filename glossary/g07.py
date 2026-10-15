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
    ('A06.6', "Code à croix de la CIM-10-GM 2024 associé à l’abcès cérébral amibien dans la catégorie G07*. Le libellé français officiel n’a pas été relu dans le fichier de l’OFS."),
    ('A54.8', "Code à croix de la CIM-10-GM 2024 associé à l’abcès cérébral gonococcique dans la catégorie G07*. Le libellé français officiel n’a pas été relu dans le fichier de l’OFS."),
    ('A17.8', "Code à croix de la CIM-10-GM 2024 associé à l’abcès cérébral tuberculeux et au tuberculome cérébral dans la catégorie G07*. Le libellé français officiel n’a pas été relu dans le fichier de l’OFS."),
    ('A17.1', "Code à croix de la CIM-10-GM 2024 associé au tuberculome méningé dans la catégorie G07*. Le libellé français officiel n’a pas été relu dans le fichier de l’OFS.")]:
    add_if_absent(_code, [(_code, 'code de classification, non une abréviation')], 'Code à croix ' + _code, _txt, 'g07-asterisque')

add_if_absent('2HRZE', [('2', 'durée de la phase en mois'), ('H', 'isoniazide'), ('R', 'rifampicine'), ('Z', 'pyrazinamide'), ('E', 'éthambutol')],
              'Phase intensive de deux mois : isoniazide, rifampicine, pyrazinamide, éthambutol',
              'Notation du guide suisse de l’OFSP : deux mois de quatre médicaments antituberculeux. Les initiales suivent la composition de l’association fixe Rimstar.', 'g07-schema')
add_if_absent('10HR', [('10', 'durée de la phase en mois'), ('H', 'isoniazide'), ('R', 'rifampicine')],
              'Phase de continuation de dix mois : isoniazide, rifampicine',
              'Notation du guide suisse de l’OFSP : dix mois de deux médicaments antituberculeux, après la phase intensive.', 'g07-schema')
add_if_absent('IFT', [('I', 'Immuno'), ('F', 'Fluorescence'), ('T', 'Test')], 'Test d’immunofluorescence',
              'Test sérologique cité avec l’ELISA comme test de dépistage de la schistosomiase dans la recommandation allemande de 2017. Deux tests différents sont recommandés.', 'g07-schisto-meca')
add_if_absent('PET-CT', [('P', 'Positron'), ('E', 'Emission'), ('T', 'Tomography'), ('-', 'couplée à'), ('C', 'Computed'), ('T', 'Tomography')],
              'Tomographie par émission de positons couplée à la tomodensitométrie',
              'Examen d’imagerie décrit comme sensible dans la neuroschistosomiase par la recommandation allemande de 2017.', 'g07-schisto-meca')
add_if_absent('POC-CCA', [('POC', 'Point-Of-Care'), ('CCA', 'Circulating Cathodic Antigen')], 'Antigène cathodique circulant au chevet du patient',
              'Test rapide de détection d’un antigène de schistosome. La recommandation allemande de 2017 le réserve à des cas choisis.', 'g07-schisto-meca')
add_if_absent('MetronidazoleSINT', [('MetronidazoleSINT', 'nom commercial, non une abréviation')], 'MetronidazoleSINT i.v., nom commercial',
              'Spécialité de métronidazole par voie intraveineuse dont l’information professionnelle suisse (février 2026) a été lue pour cette leçon.', 'g07-m-metro')
