"""Abréviations D77 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'d77', '__init__'}:
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

# --- Schistosomose et sciences associées ---
add_if_absent('HSS', [('H','Hepato- (hépato-)'),('S','Splenic (splénique)'),('S','Schistosomiasis (schistosomose)')],
              'Schistosomose hépatosplénique (hepatosplenic schistosomiasis)',
              'Forme chronique grave de la schistosomose : fibrose périportale, hypertension portale, varices œsophagiennes et splénomégalie avec hypersplénisme. Elle touche 4 à 8 % des personnes infectées (série européenne TIPS 2021).', 'd77-hss')
add_if_absent('CCA', [('C','Circulating (circulant)'),('C','Cathodic (cathodique)'),('A','Antigen (antigène)')],
              'Antigène cathodique circulant',
              'Antigène du parasite détecté dans l’urine ; le Swiss TPH l’a utilisé pour dépister Schistosoma mansoni chez des réfugiés érythréens (40,2 % de tests positifs).', 'd77-cca')
add_if_absent('TPH', [('T','Tropical'),('P','and Public (et de santé publique)'),('H','Health (santé)')],
              'Institut tropical et de santé publique suisse (Swiss Tropical and Public Health Institute, Bâle)',
              'Institut de recherche bâlois dont l’étude de 2018 a mesuré la schistosomose chez des réfugiés érythréens arrivés récemment en Suisse.')
add_if_absent('PSVD', [('P','Porto-'),('S','Sinusoidal (sinusoïdal)'),('V','Vascular (vasculaire)'),('D','Disorder (trouble)')],
              'Trouble vasculaire porto-sinusoïdal (porto-sinusoidal vascular disorder)',
              'Hypertension portale sans cirrhose, dont le diagnostic exige l’exclusion de la cirrhose et des autres causes d’hypertension portale (Baveno VII).', 'd77-psvd')
add_if_absent('BBNS', [('B','Bêta'),('B','Bloquants'),('N','Non'),('S','Sélectifs')],
              'Bêtabloquants non sélectifs',
              'Médicaments qui abaissent la pression portale ; en Suisse, le propranolol est celui dont l’information professionnelle mentionne les varices œsophagiennes.', 'd77-bbns')
add_if_absent('UE', [('U','Union'),('E','Européenne')], 'Union européenne', 'Cadre géographique du dépistage de l’ECDC 2018.')
add_if_absent('EEE', [('E','Espace'),('E','Économique'),('E','Européen')], 'Espace économique européen', 'Cadre géographique du dépistage de l’ECDC 2018, avec l’Union européenne.')
add_if_absent('MCV', [('M','Meningococcal (méningococcique)'),('C','Conjugate (conjugué)'),('V','Vaccine (vaccin)')],
              'Vaccin méningococcique conjugué', 'Dans MCV-ACWY, vaccin conjugué contre les sérogroupes A, C, W et Y (Menveo), recommandé en deux doses après splénectomie.', 'd77-vaccins')
add_if_absent('ACWY', [('A','sérogroupe A'),('C','sérogroupe C'),('W','sérogroupe W'),('Y','sérogroupe Y')],
              'Sérogroupes méningococciques A, C, W et Y', 'Sérogroupes couverts par le vaccin conjugué.', 'd77-vaccins')
add_if_absent('MenB', [('Men','Méningocoque'),('B','de sérogroupe B')], 'Méningocoque de sérogroupe B',
              'Vaccin Bexsero : deux doses à deux mois d’intervalle, rappel tous les 5 ans après splénectomie.', 'd77-vaccins')
add_if_absent('PAL', [('P','Phosphatases'),('AL','ALcalines')], 'Phosphatases alcalines',
              'Enzyme de cholestase dont l’élévation accompagne celle des GGT et de la bilirubine dans les formes avancées de bilharziose.')
add_if_absent('LAMP', [('L','Loop-mediated (médiée par une boucle)'),('AMP','isothermal AMPlification (amplification isotherme)')],
              'Amplification isotherme médiée par boucle', 'Technique moléculaire de détection de l’ADN du parasite, disponible surtout en centre de référence.')
add_if_absent('BIA', [('B','British'),('I','Infection'),('A','Association')], 'Association britannique des infections',
              'Auteur de la directive 2024 sur l’éosinophilie des voyageurs et migrants, lue en résumé seulement et non utilisée pour une conduite.')
add_if_absent('HC', [('H','Health'),('C','Care')], 'HealthCare (soins de santé)', 'Élément du nom du titulaire Spirig HealthCare AG, de l’information professionnelle du carvédilol consultée.')
add_if_absent('Gamna-Gandy', [('Gamna','nom propre'),('Gandy','nom propre')], 'Corps de Gamna-Gandy (éponyme)',
              'Nodules sidérotiques de la rate d’hypertension portale : foyers ponctués en hyposignal T1 et T2 en IRM, liés à l’hémosidérine des macrophages.')
add_if_absent('Échographie-Doppler', [('Écho','Écho-'),('graphie','graphie'),('Doppler','mesure du flux par effet Doppler')], 'Échographie avec mesure Doppler des flux',
              'Examen qui mesure la longueur de la rate, la taille du foie, le flux portal et la texture dans le bilan d’une bilharziose hépatosplénique.')
add_if_absent('Proche-Orient', [('Proche','Proche'),('Orient','Orient')], 'Proche-Orient', 'Région où <i>Schistosoma haematobium</i> est présent.')
for _k, _t in [('D73.0','Hyposplénisme, dont l’asplénie après splénectomie'),('D73.1','Hypersplénisme'),('D73.2','Splénomégalie congestive chronique'),('D73.8','Autres maladies de la rate, dont la fibrose de la rate sans cause classée ailleurs')]:
    add_if_absent(_k, [(_k[:3],'Rubrique des maladies de la rate (CIM-10-GM 2024)'),(_k[3:],_t)], _t, 'Code CIM-10-GM 2024 voisin de D77* : ' + _t + '.')
for _k, _t in [('B65.0','Schistosoma haematobium, forme urogénitale'),('B65.1','Schistosoma mansoni, forme intestinale'),('B65.2','Schistosoma japonicum, forme asiatique'),('B65.3','dermatite cercarienne'),('B65.8','autres schistosomiases (S. intercalatum, S. mattheei, S. mekongi)'),('B65.9','schistosomiase sans précision')]:
    add_if_absent(_k, [(_k[:3],'Rubrique de la schistosomiase [bilharziose] (CIM-10-GM 2024)'),(_k[3:],_t)], 'Schistosomiase : ' + _t, 'Code étiologique (dague) sous lequel D77* se code : ' + _t + '.', 'd77-codage')
