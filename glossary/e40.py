"""Abréviations E40 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib

_existing = {}
_here = Path(__file__).resolve().parent
_dirs = [_here] + [p / 'glossary' for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()]
import sys
for _d in _dirs:
    if str(_d) not in sys.path:
        sys.path.append(str(_d))
    for _path in sorted(_d.glob('*.py')):
        if _path.stem in {'e40', '__init__'}:
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

add_if_absent('ET', [('É', 'Écart'), ('T', 'Type (écart-type)')], 'Écart-type',
              'L’écart-type mesure la dispersion des valeurs autour de la moyenne d’une population de référence. Le poids pour la taille d’un enfant s’exprime en nombre d’écarts-types (z-score) par rapport à cette moyenne : sous −3 écarts-types, la malnutrition est sévère selon l’OMS 2023.', 'e40-mas-def')
add_if_absent('OSAV', [('O', 'Office fédéral de la'), ('S', 'Sécurité'), ('A', 'Alimentaire et des affaires'), ('V', 'Vétérinaires')], 'Office fédéral de la sécurité alimentaire et des affaires vétérinaires',
              'Cet office fédéral suisse a publié en 2020, sur la base d’instructions de la Société suisse de pédiatrie, un communiqué déconseillant l’alimentation végane chez le nourrisson et le jeune enfant.', 'e40-position-suisse')
add_if_absent('SSP', [('S', 'Société'), ('S', 'Suisse de'), ('P', 'Pédiatrie')], 'Société suisse de pédiatrie',
              'Cette société savante a rédigé en 2020 des instructions sur l’alimentation végétarienne et végane des enfants en bas âge, reprises dans un communiqué de l’Office fédéral de la sécurité alimentaire et des affaires vétérinaires.', 'e40-position-suisse')
add_if_absent('ReSoMal', [('Re', 'Rehydration (réhydratation)'), ('So', 'Solution'), ('Mal', 'for Malnutrition (pour la malnutrition)')], 'Solution de réhydratation pour la malnutrition',
              'Solution de réhydratation orale adaptée à l’enfant atteint de malnutrition aiguë sévère. Elle est préférée en cas de déshydratation sans choc et n’est pas employée si un choléra est suspecté ou en cas de diarrhée aqueuse profuse.', 'e40-d-resomal')
add_if_absent('ATPE', [('A', 'Aliment'), ('T', 'Thérapeutique'), ('P', 'Prêt à l’'), ('E', 'Emploi')], 'Aliment thérapeutique prêt à l’emploi',
              'Aliment à haute densité énergétique utilisé pour la réhabilitation nutritionnelle, notamment en ambulatoire, à 150 à 185 kcal/kg/jour selon l’OMS 2023. Équivalent anglais : ready-to-use therapeutic food.', 'e40-d-atpe')
add_if_absent('E64.0', [('E', 'Chapitre des maladies endocriniennes, nutritionnelles et métaboliques'), ('64', 'numéro de catégorie'), ('.0', 'sous-catégorie : séquelles de malnutrition protéino-énergétique')], 'Code CIM-10-GM E64.0, séquelles de malnutrition protéino-énergétique',
              'Ce code est exclu du bloc de la malnutrition aiguë : il désigne les séquelles et non la maladie en cours.')
add_if_absent('T73.0', [('T', 'Chapitre des lésions traumatiques et causes externes'), ('73', 'numéro de catégorie'), ('.0', 'sous-catégorie : mort par inanition')], 'Code CIM-10-GM T73.0, effets de la privation de nourriture (mort par inanition)',
              'Ce code est exclu du bloc de la malnutrition aiguë.')
add_if_absent('HC', [('HC', 'Sigle du nom de la spécialité (Amoxicilline Spirig HC®) ; développement non précisé par la source')], 'Élément du nom de la spécialité Amoxicilline Spirig HC®',
              'Le sigle fait partie du nom commercial de l’amoxicilline orale dont l’information professionnelle suisse a été lue (mise à jour d’août 2024). Il ne désigne pas une notion médicale.', 'e40-d-amox')
add_if_absent('Roux-en-Y', [('Roux', 'nom du chirurgien qui a décrit la technique'), ('en-Y', 'en forme de Y')], 'Dérivation en Y de Roux',
              'Technique de dérivation gastrique en forme de Y utilisée en chirurgie bariatrique. Un cas publié d’adulte après cette dérivation présentait une ascite de kwashiorkor imitant une hypertension portale.', 'e40-ascite')
