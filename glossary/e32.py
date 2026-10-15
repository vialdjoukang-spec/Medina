"""Abréviations E32 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e32', '__init__'}:
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

add_if_absent('NVALT', [('NVALT', 'sigle d’une société savante néerlandaise ; développement littéral non repris dans les sources lues')], 'Société néerlandaise auteure des recommandations sur les tumeurs épithéliales thymiques',
              'Recommandations nationales néerlandaises publiées le 8 novembre 2024 : modules imagerie, biologie et biopsie lus pour ce cours. Elles ne sont pas suisses.', 'e32-nvalt')
add_if_absent('EuroNet-PHL-C1', [('EuroNet-PHL-C1', 'nom d’un essai européen sur le lymphome de Hodgkin pédiatrique, non développable lettre à lettre')], 'Essai européen EuroNet-PHL-C1',
              'Essai de 291 enfants atteints de lymphome de Hodgkin, utilisé pour distinguer le rebond thymique de la rechute.', 'e32-euronet')
add_if_absent('CD23', [('CD', 'Cluster of Differentiation (groupe de différenciation)'), ('23', 'numéro 23')], 'Antigène CD23',
              'Marqueur exprimé par les follicules à centres germinatifs de l’hyperplasie thymique folliculaire.', 'e32-htf')
add_if_absent('CD10', [('CD', 'Cluster of Differentiation (groupe de différenciation)'), ('10', 'numéro 10')], 'Antigène CD10',
              'Marqueur exprimé par les centres germinatifs de l’hyperplasie thymique folliculaire.', 'e32-htf')
add_if_absent('CD4', [('CD', 'Cluster of Differentiation (groupe de différenciation)'), ('4', 'numéro 4')], 'Antigène CD4',
              'Marqueur d’une sous-population de lymphocytes T dosée avec les sous-populations CD4 et CD8 en cas d’infections récidivantes.', 'e32-biologie')
add_if_absent('CD8', [('CD', 'Cluster of Differentiation (groupe de différenciation)'), ('8', 'numéro 8')], 'Antigène CD8',
              'Marqueur d’une sous-population de lymphocytes T, dosée avec les CD4 en cas d’infections récidivantes.', 'e32-biologie')
add_if_absent('Bcl2', [('B', 'B-cell (lymphocyte B)'), ('cl', 'CLL/lymphoma (leucémie lymphoïde chronique / lymphome)'), ('2', 'numéro 2')], 'B-cell lymphoma 2',
              'Protéine absente des centres germinatifs de l’hyperplasie thymique folliculaire (Bcl2 négatif).', 'e32-htf')
add_if_absent('Bcl6', [('B', 'B-cell (lymphocyte B)'), ('cl', 'CLL/lymphoma (leucémie lymphoïde chronique / lymphome)'), ('6', 'numéro 6')], 'B-cell lymphoma 6',
              'Protéine exprimée par les centres germinatifs de l’hyperplasie thymique folliculaire.', 'e32-htf')
add_if_absent('LMO2', [('LMO', 'LIM domain Only (domaine LIM seul)'), ('2', 'numéro 2')], 'LIM domain only 2',
              'Marqueur exprimé par le lymphome T lymphoblastique, prolifération clonale à différencier de l’hyperplasie.', 'e32-lymphome')
add_if_absent('hCG', [('h', 'human (humaine)'), ('C', 'Chorionic (chorionique)'), ('G', 'Gonadotropin (gonadotrophine)')], 'Gonadotrophine chorionique humaine',
              'Marqueur sérique habituellement négatif, avec l’alpha-fœtoprotéine, dans les kystes thymiques.', 'e32-kyste')
add_if_absent('UH', [('U', 'Unités'), ('H', 'Hounsfield')], 'Unités Hounsfield',
              'Unité de densité au scanner : une lésion de moins de 10 UH est un kyste simple, au-delà une IRM s’impose.', 'e32-scanner')
add_if_absent('CA-125', [('CA', 'Cancer Antigen (antigène du cancer)'), ('125', 'numéro 125')], 'Antigène du cancer 125',
              'Marqueur très élevé dans un cas d’abcès thymique idiopathique rompu, et marqué dans les corpuscules de Hassall.', 'e32-abces')
add_if_absent('RyR', [('Ry', 'Ryanodine'), ('R', 'Receptor (récepteur)')], 'Récepteur de la ryanodine',
              'Cible d’anticorps rares dans l’hyperplasie folliculaire liée à la myasthénie.', 'e32-htf')
add_if_absent('MuSK', [('Mu', 'Muscle'), ('S', 'Specific (spécifique)'), ('K', 'Kinase')], 'Kinase spécifique du muscle',
              'Cible d’anticorps rares dans l’hyperplasie folliculaire liée à la myasthénie.', 'e32-htf')
add_if_absent('Cooley-Rieders', [('Cooley-Rieders', 'nom d’un auteur, non une abréviation')], 'Cooley-Rieders (auteure de la revue sur les kystes thymiques)',
              'Première auteure de la revue narrative de 2022 sur les kystes thymiques, source principale du chapitre pour les kystes.', 'e32-kyste')
add_if_absent('DeLaet', [('DeLaet', 'nom d’un auteur, non une abréviation')], 'DeLaet (auteur d’un cas d’abcès thymique)',
              'Co-auteur du cas pédiatrique d’abcès thymique à Staphylococcus aureus sensible à la méticilline.', 'e32-abces')
add_if_absent('Néo-Mercazole', [('Néo-Mercazole', 'nom commercial suisse, non une abréviation')], 'Néo-Mercazole (carbimazole 5 mg)',
              'Antithyroïdien de synthèse dont l’information professionnelle suisse fonde la posologie du chapitre.', 'e32-carbimazole')
