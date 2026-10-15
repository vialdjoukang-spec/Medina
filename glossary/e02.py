"""Abréviations E02 (cycle Betta 32) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
_gdir = next((p / 'glossary' for p in [_here] + list(_here.parents)
              if (p / 'glossary' / 'cardio_1.py').exists()), _here)
if str(_gdir) not in sys.path:
    sys.path.insert(0, str(_gdir))
_existing = {}
for _path in sorted(_gdir.glob('*.py')):
    if _path.stem in {'e02', '__init__'}:
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

add_if_absent('HIC', [('H', 'Hypothyroïdie'), ('I', 'Infra'), ('C', 'Clinique')],
              'Hypothyroïdie infraclinique',
              'TSH élevée avec T4 libre et T3 libre dans l’intervalle de référence. Dans E02, elle est attribuée à une carence en iode.', 'e02-hic')
add_if_absent('ETA', [('E', 'European'), ('T', 'Thyroid'), ('A', 'Association')],
              'European Thyroid Association (Association européenne de la thyroïde)',
              'Société savante européenne dont les recommandations de 2013 (adulte non enceinte) et de 2014 (grossesse et enfant) fondent la conduite devant une hypothyroïdie infraclinique.', 'e02-s-eta')
add_if_absent('UNICEF', [('U', 'United'), ('N', 'Nations'), ('I', 'International'), ('C', 'Children’s'), ('E', 'Emergency'), ('F', 'Fund')],
              'Fonds des Nations unies pour l’enfance',
              'Co-auteur, avec l’OMS et l’ICCIDD, du guide 2007 sur l’évaluation des troubles dus à la carence en iode.', 'e02-s-oms')
add_if_absent('ICCIDD', [('I', 'International'), ('C', 'Council'), ('C', 'for the Control of'), ('I', 'Iodine'), ('D', 'Deficiency'), ('D', 'Disorders')],
              'Conseil international pour la lutte contre les troubles dus à la carence en iode',
              'Co-auteur, avec l’OMS et l’UNICEF, du guide 2007 sur l’évaluation des troubles dus à la carence en iode.', 'e02-s-oms')
add_if_absent('OSAV', [('O', 'Office fédéral'), ('S', 'de la Sécurité'), ('A', 'Alimentaire'), ('V', 'et des affaires Vétérinaires')],
              'Office fédéral de la sécurité alimentaire et des affaires vétérinaires',
              'Cet office publie les recommandations suisses sur le sel iodé et désigne les groupes à risque de carence en iode.', 'e02-s-osav')
add_if_absent('EFSA', [('E', 'European'), ('F', 'Food'), ('S', 'Safety'), ('A', 'Authority')],
              'Autorité européenne de sécurité des aliments',
              'Elle a publié en 2014 des valeurs de référence alimentaires pour l’iode : 150 µg/j chez l’adulte, 200 µg/j en grossesse et allaitement.', 'e02-s-efsa')
add_if_absent('NDA', [('NDA', 'Panel on Dietetic Products, Nutrition and Allergies : nom du panel de l’EFSA, développé à partir de l’anglais')],
              'Panel de l’EFSA sur les produits diététiques, la nutrition et les allergies',
              'Ce panel a rédigé l’avis scientifique 2014 sur les valeurs de référence alimentaires pour l’iode.', 'e02-s-efsa')
add_if_absent('TPO', [('T', 'Thyro'), ('P', 'Per'), ('O', 'Oxydase')],
              'Thyropéroxydase (peroxydase thyroïdienne)',
              'Enzyme thyroïdienne contre laquelle les anticorps anti-TPO sont dirigés. Leur recherche cherche une auto-immunité thyroïdienne.', 'e02-antitpo')
add_if_absent('NIS', [('N', 'Sodium'), ('I', 'Iodide'), ('S', 'Symporter')],
              'Sodium/Iodide Symporter (symporteur sodium/iodure)',
              'Transporteur qui permet à la glande mammaire de concentrer l’iode et d’en apporter au lait maternel.', 'e02-nis')
add_if_absent('TRH', [('T', 'Thyrotropin'), ('R', 'Releasing'), ('H', 'Hormone')],
              'Thyrotropin-Releasing Hormone (hormone de libération de la thyréotropine)',
              'L’information professionnelle d’Euthyrox cite le test à la TRH, avec la scintigraphie de freinage, pour exclure une autonomie thyroïdienne avant traitement.', 'e02-levo')
add_if_absent('HTA', [('H', 'Health'), ('T', 'Technology'), ('A', 'Assessment')],
              'Health Technology Assessment (évaluation des technologies de la santé)',
              'Type de rapport publié par l’OFSP en 2022 sur l’usage de la lévothyroxine dans l’hypothyroïdie légère.', 'e02-ofsp')
add_if_absent('D-A-CH', [('D', 'Deutschland (Allemagne)'), ('A', 'Austria (Autriche)'), ('CH', 'Confoederatio Helvetica (Suisse)')],
              'Valeurs de référence communes Allemagne, Autriche, Suisse',
              'Ces valeurs n’ont pas été lues dans un document officiel : le cours ne les utilise pas.', 'e02-apports')
add_if_absent('E01.8', [('E01.8', 'code CIM-10 de l’hypothyroïdie acquise par carence iodée non précisée, sous-catégorie de E01 ; non une abréviation')],
              'Hypothyroïdie acquise par carence iodée non précisée',
              'Code de reclassement lorsque la T4 libre devient basse : l’hypothyroïdie n’est plus infraclinique.', 'e02-nomenclature')
add_if_absent('E89.0', [('E89.0', 'code CIM-10 de l’hypothyroïdie post-procédurale ; non une abréviation')],
              'Hypothyroïdie post-procédurale',
              'Cette catégorie est exclue de E03 et ne relève pas de E02.', 'e02-nomenclature')
