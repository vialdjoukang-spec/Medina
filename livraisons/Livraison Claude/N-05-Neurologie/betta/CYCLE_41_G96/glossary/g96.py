"""Abréviations G96 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g96', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('IRM', [('I','Imagerie'),('R','par Résonance'),('M','Magnétique')],
              'Imagerie par résonance magnétique',
              'Examen d’imagerie sans rayonnement ionisant. Dans ce cours, l’IRM cérébrale avec gadolinium et l’IRM de tout le rachis constituent la première ligne devant une céphalée orthostatique.', 'g96-irm')
add_if_absent('SLEC', [('S','Spinal'),('L','Longitudinal'),('E','Extradural'),('C','CSF (cerebrospinal fluid, liquide céphalorachidien)')],
              'Collection extradurale longitudinale spinale de liquide céphalorachidien',
              'Collection de liquide en dehors de la dure-mère, étendue en longueur le long du rachis. Sa présence ou son absence oriente le choix de la myélographie.', 'g96-slec')
add_if_absent('ICHD-3', [('I','International'),('C','Classification'),('H','of Headache'),('D','Disorders'),('-3','troisième édition')],
              'International Classification of Headache Disorders, troisième édition',
              'Classification internationale des céphalées publiée par l’International Headache Society. La rubrique 7.2 définit la céphalée attribuée à une pression basse du liquide céphalorachidien.', 'g96-ichd')
add_if_absent('CIM-10-GM', [('CIM','Classification Internationale des Maladies'),('10','dixième révision'),('GM','German Modification, modification allemande')],
              'Classification internationale des maladies, 10e révision, modification allemande',
              'Classification statistique des diagnostics utilisée comme catalogue de ce projet ; l’édition retenue est celle de 2024.')
add_if_absent('FLAIR', [('F','Fluid'),('L','(liquide)'),('A','Attenuated'),('I','Inversion'),('R','Recovery')],
              'Fluid-Attenuated Inversion Recovery',
              'Séquence d’IRM de la liste du protocole recommandé pour l’IRM cérébrale devant une suspicion d’hypotension intracrânienne.', 'g96-sequences')
add_if_absent('SWI', [('S','Susceptibility'),('W','Weighted'),('I','Imaging')],
              'Susceptibility-Weighted Imaging',
              'Séquence d’IRM sensible au sang, citée avec T2* dans le protocole cérébral ; elle sert notamment à rechercher une sidérose superficielle.', 'g96-sequences')
add_if_absent('STIR', [('S','Short'),('T','Tau'),('I','Inversion'),('R','Recovery')],
              'Short Tau Inversion Recovery',
              'Séquence d’IRM du protocole rachidien recommandé, avec T2 sagittale et axiale et 3D T2 fortement pondérée.', 'g96-sequences')
add_if_absent('T1', [('T','Temps de relaxation'),('1','pondération de premier type')],
              'Pondération T1 de l’IRM',
              'Désigne une famille de séquences d’IRM. Dans ce cours, la séquence T1 est réalisée après injection de gadolinium pour montrer la prise de contraste des méninges.', 'g96-sequences')
add_if_absent('T2', [('T','Temps de relaxation'),('2','pondération de second type')],
              'Pondération T2 de l’IRM',
              'Désigne une famille de séquences d’IRM utilisée pour le cerveau et le rachis dans le protocole recommandé.', 'g96-sequences')
add_if_absent('mSv', [('m','milli'),('Sv','sievert, unité de dose efficace d’irradiation')],
              'Millisievert',
              'Unité de dose efficace de rayonnement ionisant. La myélographie dynamique par tomodensitométrie expose à environ 19,7 mSv, celle par soustraction numérique à environ 6,6 mSv.', 'g96-myelo')
add_if_absent('Monro-Kellie', [('Monro-Kellie', 'noms propres des deux auteurs de la doctrine, non une abréviation')],
              'Doctrine de Monro-Kellie',
              'Principe selon lequel le cerveau, le sang et le liquide partagent un volume intracrânien fixe : la baisse de l’un est compensée par la hausse d’un autre.', 'g96-monro')
