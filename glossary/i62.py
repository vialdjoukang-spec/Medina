"""Abréviations I62 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'i62', '__init__'}:
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

add_if_absent('HSDC', [('H','Hématome'),('S','Sous-'),('D','Dural'),('C','Chronique')],
              'Hématome sous-dural chronique',
              'Collection encapsulée de liquide et de produits de dégradation du sang entre la dure-mère et l’arachnoïde, constituée en trois semaines ou plus. Elle est spontanée ou post-traumatique et se manifeste surtout chez la personne âgée.', 'i62-hsdc')
add_if_absent('GCS', [('G','Glasgow'),('C','Coma'),('S','Scale')],
              'Glasgow Coma Scale (score de coma de Glasgow)',
              'Score de conscience dont une valeur basse à l’admission est associée à un mauvais pronostic dans l’enquête suisse sur l’hématome sous-dural chronique opéré.', 'i62-conscience')
add_if_absent('mRS', [('m','modified'),('R','Rankin'),('S','Scale')],
              'Modified Rankin Scale (échelle de Rankin modifiée)',
              'Échelle de 0 à 6 qui mesure le handicap et la dépendance après une maladie neurologique. Elle sert de critère principal dans les essais Dex-CSDH et DECSA.', 'i62-mrs')
add_if_absent('Dex-CSDH', [('Dex','Dexaméthasone'),('CSDH','Chronic SubDural Hematoma, hématome sous-dural chronique')],
              'Essai de la dexaméthasone dans l’hématome sous-dural chronique',
              'Essai randomisé britannique de 748 patients (2020) : la dexaméthasone adjuvante a réduit les réopérations mais n’a pas amélioré l’issue favorable à six mois.', 'i62-dexa')
add_if_absent('DECSA', [('DECSA','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai néerlandais de la dexaméthasone contre la chirurgie',
              'Essai de 252 patients arrêté précocement : la non-infériorité de la dexaméthasone seule face à la trépanation n’a pas été démontrée.', 'i62-dexa')
add_if_absent('SECA', [('SECA','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai suisse sur la poursuite de l’aspirine',
              'Essai randomisé de six centres suisses (155 patients) comparant la poursuite de l’aspirine à un placebo pendant les 12 jours périopératoires.', 'i62-aspirine')
add_if_absent('ATOCH', [('ATOCH','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai chinois de l’atorvastatine',
              'Essai de phase II de 200 patients : atorvastatine 20 mg par jour pendant 8 semaines. Données chinoises présentées comme hypothèse.', 'i62-atorva')
add_if_absent('TORCH', [('TORCH','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai néerlandais de l’acide tranexamique',
              'Essai prévu de 140 patients (500 mg deux fois par jour pendant 28 jours) ; ses résultats n’ont pas été trouvés.', 'i62-txa')
add_if_absent('EMBOLISE', [('EMBOLISE','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai d’embolisation de l’artère méningée moyenne associée à la chirurgie',
              'Essai randomisé de 400 patients (2024) : réopération 4,1 % contre 11,3 %.', 'i62-embol')
add_if_absent('MAGIC-MT', [('MAGIC-MT','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai chinois d’embolisation de l’artère méningée moyenne',
              'Essai randomisé de 722 patients (2024) : différence de récidive ou de progression non significative.', 'i62-embol')
add_if_absent('STEM', [('STEM','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai d’embolisation de l’artère méningée moyenne',
              'Essai randomisé de 310 patients (2025) : échec thérapeutique composite 16 % contre 36 %.', 'i62-embol')
add_if_absent('REVERSE-AD', [('REVERSE-AD','nom d’essai, non développé lettre à lettre dans les sources lues')],
              'Essai de l’idarucizumab dans le traitement d’un saignement sous dabigatran',
              'Étude de 503 patients, dont 53 avec hémorragie intracrânienne.', 'i62-idarucizumab')
