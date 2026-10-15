"""Abréviations G55 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g55', '__init__'}:
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

add_if_absent('L5', [('L', 'Lombaire'), ('5', 'cinquième')],
              'Cinquième racine lombaire',
              'Cette racine innerve notamment le tibial antérieur, les extenseurs des orteils et les péroniers. Son atteinte donne un steppage et rend la marche sur les talons impossible ; ses réflexes restent intacts. Elle est avec la première racine sacrée la racine la plus souvent atteinte par une hernie discale lombaire.', 'g55-racines-lombaires')
add_if_absent('G55.0', [('G', 'Chapitre des maladies du système nerveux, code'), ('55.0', 'sous-code zéro du code 55')],
              'Code G55.0* de la CIM-10-GM 2024',
              'Ce code de manifestation, marqué d’un astérisque, désigne la compression des racines et des plexus nerveux au cours de maladies tumorales. Il est associé aux codes marqués d’une croix de C00 à D48.', 'g55-codage')
add_if_absent('G55.1', [('G', 'Chapitre des maladies du système nerveux, code'), ('55.1', 'sous-code un du code 55')],
              'Code G55.1* de la CIM-10-GM 2024',
              'Ce code de manifestation désigne la compression des racines et des plexus nerveux au cours d’atteintes des disques intervertébraux, associée aux codes marqués d’une croix M50 à M51.', 'g55-codage')
add_if_absent('G55.2', [('G', 'Chapitre des maladies du système nerveux, code'), ('55.2', 'sous-code deux du code 55')],
              'Code G55.2* de la CIM-10-GM 2024',
              'Ce code de manifestation désigne la compression des racines et des plexus nerveux au cours de spondylarthroses, associée au code marqué d’une croix M47.-.', 'g55-codage')
add_if_absent('G55.3', [('G', 'Chapitre des maladies du système nerveux, code'), ('55.3', 'sous-code trois du code 55')],
              'Code G55.3* de la CIM-10-GM 2024',
              'Ce code de manifestation désigne la compression des racines et des plexus nerveux au cours d’autres dorsopathies, associée aux codes marqués d’une croix M45–M46, M48.- et M53–M54.', 'g55-codage')
add_if_absent('G55.8', [('G', 'Chapitre des maladies du système nerveux, code'), ('55.8', 'sous-code huit du code 55')],
              'Code G55.8* de la CIM-10-GM 2024',
              'Ce code de manifestation désigne la compression des racines et des plexus nerveux au cours d’autres maladies classées ailleurs. La classification ne liste aucun code marqué d’une croix associé.', 'g55-codage')
add_if_absent('NG59', [('NG', 'NICE Guideline (recommandation du National Institute for Health and Care Excellence)'), ('59', 'numéro 59')],
              'NICE Guideline 59, lombalgie et sciatique chez les plus de 16 ans',
              'Cette recommandation britannique évalue et prend en charge la lombalgie et la sciatique de la personne de plus de 16 ans. Elle déconseille notamment les gabapentinoïdes et les corticoïdes oraux dans la sciatique.', 'g55-conservateur-nice')
add_if_absent('NG234', [('NG', 'NICE Guideline (recommandation du National Institute for Health and Care Excellence)'), ('234', 'numéro 234')],
              'NICE Guideline 234, métastases rachidiennes et compression médullaire métastatique',
              'Cette recommandation britannique décrit la reconnaissance, l’imagerie et le traitement urgent de la compression médullaire métastatique chez l’adulte atteint de cancer.', 'g55-nice-msc')
add_if_absent('Parsonage-Turner', [('Parsonage-Turner', 'noms de deux auteurs, non une abréviation')],
              'Parsonage et Turner, auteurs de la description d’une plexopathie brachiale aiguë',
              'Ce syndrome désigne une plexopathie cervicale aiguë avec douleur intense d’épaule, amyotrophie et faiblesse.', 'g55-parsonage')
add_if_absent('HC', [('HC', 'élément du nom de produit Prégabaline Spirig HC, non développé par la source lue')],
              'Élément du nom commercial Prégabaline Spirig HC',
              'Ce sigle fait partie du nom de la spécialité dont l’information professionnelle suisse a été lue ; la source ne le développe pas.', 'g55-d-pregabaline')
add_if_absent('Ibuprofen-Mepha', [('Ibuprofen-Mepha', 'nom commercial de la spécialité, non une abréviation')],
              'Ibuprofen-Mepha Teva, spécialité d’ibuprofène',
              'Ce nom désigne la spécialité dont l’information professionnelle suisse a été lue pour les comprimés pelliculés.', 'g55-d-ibuprofene')
