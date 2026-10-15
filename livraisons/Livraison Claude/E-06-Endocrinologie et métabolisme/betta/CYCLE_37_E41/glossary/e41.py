"""Abréviations E41 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
import sys

_existing = {}
_here = Path(__file__).resolve().parent
_dirs = [_here] + [p / 'glossary' for p in _here.parents if (p / 'glossary' / 'cardio_1.py').exists()]
for _d in _dirs:
    if str(_d) not in sys.path:
        sys.path.append(str(_d))
    for _path in sorted(_d.glob('*.py')):
        if _path.stem in {'e41', '__init__'}:
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


add_if_absent('GLIM', [('G', 'Global'), ('L', 'Leadership'), ('I', 'Initiative on'), ('M', 'Malnutrition')],
              'Initiative mondiale de leadership sur la malnutrition',
              'Consensus de 2019 qui définit la malnutrition de l’adulte par au moins un critère de phénotype (perte de poids, indice de masse corporelle bas, masse musculaire réduite) et un critère d’étiologie (apport ou assimilation réduits, inflammation ou charge de maladie), après un dépistage positif.', 'e41-glim')
add_if_absent('ESPEN', [('E', 'European'), ('S', 'Society for'), ('P', 'Parenteral'), ('E', 'and Enteral'), ('N', 'Nutrition')],
              'Société européenne de nutrition clinique et de métabolisme (sigle issu de l’ancien nom anglais)',
              'Société savante européenne dont les définitions de 2017 distinguent la malnutrition liée à la maladie avec ou sans inflammation et la malnutrition sans maladie, et dont les recommandations de 2018 portent sur les patients polymorbides.', 'e41-espen-def')
add_if_absent('NRS', [('N', 'Nutritional'), ('R', 'Risk'), ('S', 'Screening')],
              'Dépistage du risque nutritionnel (Nutritional Risk Screening)',
              'Outil de dépistage hospitalier, publié en 2003 pour sa version « 2002 ». Un score d’au moins 3 points indique un risque nutritionnel qui justifie une évaluation et un soutien individualisé.', 'e41-nrs')
add_if_absent('EFFORT', [('EFFORT', 'nom d’essai ; développement littéral non fourni par le dossier de recherche')],
              'Essai EFFORT',
              'Essai mené dans 8 hôpitaux suisses chez 2088 patients à risque nutritionnel : le soutien nutritionnel individualisé a réduit les événements défavorables et la mortalité à 30 jours.', 'e41-effort')
add_if_absent('ReSoMal', [('Re', 'Rehydration (réhydratation)'), ('So', 'Solution'), ('Mal', 'for Malnutrition (pour la malnutrition)')],
              'Solution de réhydratation pour la malnutrition',
              'Solution de réhydratation orale adaptée à l’enfant atteint de malnutrition aiguë sévère, administrée à 5 ml/kg toutes les 30 minutes pendant 2 heures selon la revue de Dipasquale.', 'e41-resomal')
add_if_absent('IGF-1', [('I', 'Insulin-like'), ('G', 'Growth'), ('F', 'Factor'), ('1', 'numéro 1')],
              'Facteur de croissance analogue à l’insuline de type 1',
              'Médiateur de la croissance. Il baisse dans le marasme, ce qui contribue à l’arrêt de la croissance.', 'e41-adaptation')
add_if_absent('kJ', [('k', 'kilo (mille)'), ('J', 'Joule')], 'Kilojoule',
              'Unité d’énergie. Une kilocalorie vaut 4,184 kilojoules ; 4200 kJ correspondent donc à environ 1000 kcal.')
add_if_absent('HC', [('H', 'Health'), ('C', 'Care')], 'HealthCare (soins de santé)',
              'Élément du nom commercial Spirig HealthCare, titulaire de l’amoxicilline dont l’information professionnelle suisse est citée dans ce cours.')
add_if_absent('E44.0', [('E', 'Chapitre des maladies endocriniennes, nutritionnelles et métaboliques'), ('44', 'catégorie de malnutrition protéino-énergétique modérée et légère'), ('.0', 'premier sous-code')],
              'Malnutrition protéino-énergétique modérée',
              'Sous-code de la CIM-10-GM 2024 pour une malnutrition dont le poids se situe de 2 à moins de 3 écarts-types sous la moyenne de référence.')
add_if_absent('E44.1', [('E', 'Chapitre des maladies endocriniennes, nutritionnelles et métaboliques'), ('44', 'catégorie de malnutrition protéino-énergétique modérée et légère'), ('.1', 'second sous-code')],
              'Malnutrition protéino-énergétique légère',
              'Sous-code de la CIM-10-GM 2024 pour une malnutrition dont le poids se situe de 1 à moins de 2 écarts-types sous la moyenne de référence.')
