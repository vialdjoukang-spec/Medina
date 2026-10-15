"""Abréviations G52 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g52', '__init__'}:
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

add_if_absent('ICHD-3', [('I', 'International'), ('C', 'Classification of'), ('H', 'Headache'), ('D', 'Disorders'), ('-3', 'troisième édition')],
              'International Classification of Headache Disorders, 3e édition',
              'Cette classification de la Société internationale des céphalées définit la névralgie glossopharyngienne (rubrique 13.2.1) et la neuropathie glossopharyngienne douloureuse (13.2.2). Elle classe les douleurs ; elle ne recommande aucun traitement.', 'g52-ichd')
add_if_absent('Collet-Sicard', [('Collet-Sicard', 'noms propres de deux auteurs, non une abréviation')],
              'Syndrome de Collet-Sicard',
              'Ce syndrome désigne la paralysie unilatérale des nerfs crâniens IX, X, XI et XII. L’ajout d’une atteinte de la chaîne sympathique cervicale correspond au syndrome de Villaret.', 'g52-collet')
add_if_absent('Aguilera-Pena', [('Aguilera-Pena', 'nom d’auteur, non une abréviation')],
              'Aguilera-Pena, premier auteur de la revue de portée sur le syndrome de Collet-Sicard',
              'Cette revue de 2023 rapporte 135 patients ; seul le résumé a été lu.', 'g52-collet')
add_if_absent('Arnold-Chiari', [('Arnold-Chiari', 'noms propres de deux auteurs, non une abréviation')],
              'Malformation d’Arnold-Chiari',
              'Cette malformation figure parmi les causes rapportées de névralgie glossopharyngienne secondaire, dans des rapports isolés.', 'g52-ngp')
add_if_absent('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')],
              'European Academy of Neurology (Académie européenne de neurologie)',
              'Cette académie a publié en 2023, avec la Peripheral Nerve Society, la recommandation sur le syndrome de Guillain-Barré. Seul le résumé a été lu.', 'g52-gbs')
add_if_absent('PNS', [('P', 'Peripheral'), ('N', 'Nerve'), ('S', 'Society')],
              'Peripheral Nerve Society (Société des nerfs périphériques)',
              'Cette société est co-autrice de la recommandation européenne de 2023 sur le syndrome de Guillain-Barré.', 'g52-gbs')
add_if_absent('GOS', [('G', 'Glasgow'), ('O', 'Outcome'), ('S', 'Scale')],
              'Glasgow Outcome Scale (échelle de devenir de Glasgow)',
              'Dans la méta-analyse sur Collet-Sicard, un score d’au moins 4 définit une issue favorable, observée chez 71,2 % des patients.', 'g52-collet')
add_if_absent('TDI', [('T', 'Threshold (seuil)'), ('D', 'Discrimination'), ('I', 'Identification')],
              'Score composite Threshold, Discrimination, Identification',
              'Ce score regroupe les trois composantes d’un test olfactif psychophysique tel que les Sniffin’ Sticks. Il se lit toujours selon les normes du test utilisé.', 'g52-tdi')
add_if_absent('HLA-B*1502', [('HLA', 'Human Leukocyte Antigen (antigène leucocytaire humain)'), ('-B', 'locus B'), ('*1502', 'allèle 15:02')],
              'Allèle HLA-B*15:02',
              'Cet allèle est fortement corrélé au syndrome de Stevens-Johnson et à la nécrolyse épidermique toxique sous carbamazépine ; son dépistage est demandé avant le traitement chez les patients d’origine à risque.', 'g52-hla')
add_if_absent('HLA-A*3101', [('HLA', 'Human Leukocyte Antigen (antigène leucocytaire humain)'), ('-A', 'locus A'), ('*3101', 'allèle 31:01')],
              'Allèle HLA-A*31:01',
              'Cet allèle est aussi associé aux réactions cutanées sévères sous carbamazépine, selon l’information professionnelle suisse.', 'g52-hla')
add_if_absent('H47.0', [('H47.0', 'code de la CIM-10-GM 2024')],
              'Code H47.0 de la CIM-10-GM 2024',
              'Ce code est cité parmi les exclusions de G 52 (nerf optique). Le libellé complet n’a pas été relu pour ce cours.', 'g52-perimetre')
add_if_absent('H93.3', [('H93.3', 'code de la CIM-10-GM 2024')],
              'Code H93.3 de la CIM-10-GM 2024',
              'Ce code est cité parmi les exclusions de G 52 (nerf vestibulocochléaire). Le libellé complet n’a pas été relu pour ce cours.', 'g52-perimetre')
add_if_absent('H49.0', [('H49.0', 'code de la CIM-10-GM 2024')],
              'Code H49.0 de la CIM-10-GM 2024',
              'Ce code est cité parmi les exclusions de G 52 (paralysie des nerfs oculomoteurs). Le libellé complet n’a pas été relu pour ce cours.', 'g52-perimetre')
add_if_absent('H49.2', [('H49.2', 'code de la CIM-10-GM 2024')],
              'Code H49.2 de la CIM-10-GM 2024',
              'Ce code est cité parmi les exclusions de G 52 (paralysie des nerfs oculomoteurs). Le libellé complet n’a pas été relu pour ce cours.', 'g52-perimetre')
