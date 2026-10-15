"""Abréviations I64 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'i64', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('AVC', [('A', 'Accident'), ('V', 'Vasculaire'), ('C', 'Cérébral')],
              'Accident vasculaire cérébral',
              'Déficit neurologique brutal d’origine vasculaire. Le code I64 le désigne lorsque sa nature, infarctus ou hémorragie, n’est pas établie.', 'i64-cim')
add_if_absent('CIM-10-GM', [('CIM', 'Classification Internationale des Maladies'), ('10', 'dixième révision'), ('GM', 'German Modification, modification allemande')],
              'Classification internationale des maladies, 10e révision, modification allemande',
              'Version 2024 utilisée pour le catalogue de MEDINA et par l’Office fédéral de la statistique. Elle ne se confond pas avec la CIM-11.', 'i64-cim')
add_if_absent('ESO', [('E', 'European'), ('S', 'Stroke'), ('O', 'Organisation')],
              'European Stroke Organisation',
              'Société européenne qui publie les recommandations sur l’AVC (thrombolyse 2021, pression artérielle 2025, hémorragie intracérébrale 2025).', 'i64-thrombolyse-resume')
add_if_absent('ESMINT', [('E', 'European'), ('S', 'Society'), ('M', 'of Minimally'), ('I', 'Invasive'), ('N', 'Neurological'), ('T', 'Therapy')],
              'European Society of Minimally Invasive Neurological Therapy',
              'Société européenne partenaire de l’ESO dans les recommandations de thrombectomie mécanique de 2019 et de l’occlusion basilaire de 2024. Développement lexical : il ne figure pas dans le dossier de lecture.', 'i64-thrombectomie')
add_if_absent('EANS', [('E', 'European'), ('A', 'Association'), ('N', 'of Neurosurgical'), ('S', 'Societies')],
              'European Association of Neurosurgical Societies',
              'Association européenne de neurochirurgie, coautrice avec l’ESO de la recommandation 2025 sur l’hémorragie intracérébrale spontanée. Développement lexical : il ne figure pas dans le dossier de lecture.', 'i64-expansion')
add_if_absent('SFCNS', [('S', 'Swiss'), ('F', 'Federation'), ('C', 'of Clinical'), ('N', 'Neuro-'), ('S', 'Societies')],
              'Fédération suisse des sociétés cliniques de neurologie',
              'Elle coordonne la certification des Stroke Units et Stroke Centers ; ses critères du 18 novembre 2021 sont en vigueur mais n’ont pas été lus. Développement lexical : il ne figure pas dans le dossier de lecture.', 'i64-stroke-unit')
add_if_absent('IVHSM', [('IVHSM', 'sigle de l’Interkantonale Vereinbarung über die hochspezialisierte Medizin, convention intercantonale sur la médecine hautement spécialisée')],
              'Convention intercantonale sur la médecine hautement spécialisée',
              'Elle donne mandat à la SFCNS pour la certification des Stroke Centers. Sigle allemand, non développé lettre à lettre dans le dossier de lecture.', 'i64-stroke-unit')
add_if_absent('SwissDRG', [('Swiss', 'suisse'), ('DRG', 'Diagnosis Related Groups, groupes homogènes de diagnostics')],
              'Swiss Diagnosis Related Groups',
              'Système suisse de forfaits par cas, introduit en 2012. Il a rendu le codage des diagnostics plus systématique, ce qui explique en partie la hausse des AVC enregistrés.', 'i64-epidemio')
add_if_absent('BfArM', [('BfArM', 'sigle du Bundesinstitut für Arzneimittel und Medizinprodukte, institut fédéral allemand des médicaments et des dispositifs médicaux')],
              'Institut fédéral allemand des médicaments et des dispositifs médicaux',
              'Éditeur de la version allemande de la CIM-10-GM 2024 consultée. Sigle allemand, non développé lettre à lettre.', 'i64-cim')
add_if_absent('AMM', [('A', 'Autorisation'), ('M', 'de Mise'), ('M', 'sur le Marché')],
              'Autorisation de mise sur le marché',
              'En Suisse, l’autorisation est délivrée par Swissmedic ; l’information professionnelle en fixe les indications et contre-indications.', 'i64-actilyse')
add_if_absent('NIHSS', [('N', 'National'), ('I', 'Institutes'), ('H', 'of Health'), ('S', 'Stroke'), ('S', 'Scale')],
              'National Institutes of Health Stroke Scale',
              'Score de sévérité neurologique de l’AVC. Il mesure la gravité et non la nature, hémorragique ou ischémique.', 'i64-nihss')
add_if_absent('INR', [('I', 'International'), ('N', 'Normalized'), ('R', 'Ratio')],
              'Rapport international normalisé',
              'Mesure de la coagulation sous antivitamine K. Seuils : 1,7 selon l’ESO 2021, 1,3 selon les informations professionnelles suisses.', 'i64-inr')
add_if_absent('AVK', [('A', 'Anti'), ('V', 'Vitamine'), ('K', 'K')],
              'Antivitamine K',
              'Anticoagulant oral dont l’effet se surveille par l’INR.', 'i64-inr')
add_if_absent('IRM', [('I', 'Imagerie par'), ('R', 'Résonance'), ('M', 'Magnétique')],
              'Imagerie par résonance magnétique',
              'Elle fournit la discordance DWI-FLAIR et la perfusion, utiles aux fenêtres tardives.', 'i64-imagerie')
add_if_absent('DWI-FLAIR', [('DWI', 'Diffusion-Weighted Imaging, imagerie pondérée en diffusion'), ('FLAIR', 'Fluid-Attenuated Inversion Recovery, inversion-récupération à atténuation de liquide')],
              'Discordance entre les séquences de diffusion et FLAIR de l’IRM',
              'Une lésion visible en diffusion mais pas encore en FLAIR suggère un infarctus récent ; elle sélectionne la thrombolyse au réveil.', 'i64-penombre')
add_if_absent('anti-Xa', [('anti', 'contre'), ('Xa', 'facteur X activé')],
              'Activité anti-facteur Xa',
              'Dosage utilisé sous anticoagulant oral direct ; en dessous de 0,5 U/ml, la thrombolyse est possible par consensus (ESO 2021).', 'i64-inr')
add_if_absent('ASPECTS', [('ASPECTS', 'sigle de l’échelle d’imagerie cérébrale précoce, développement non consigné dans le dossier de lecture')],
              'Score d’imagerie précoce de l’infarctus',
              'Un score d’au moins 6 est cité parmi les critères de sélection de la thrombectomie dans les 6 heures.', 'i64-thrombectomie')
add_if_absent('DAWN', [('DAWN', 'nom d’essai, non développé lettre à lettre dans le dossier de lecture')],
              'Essai DAWN',
              'Essai dont les critères d’imagerie et de clinique sélectionnent la thrombectomie entre 6 et 24 heures.', 'i64-thrombectomie')
add_if_absent('DEFUSE-3', [('DEFUSE', 'nom d’essai, non développé lettre à lettre dans le dossier de lecture'), ('3', 'troisième essai')],
              'Essai DEFUSE-3',
              'Second ensemble de critères d’imagerie pour la thrombectomie entre 6 et 24 heures.', 'i64-thrombectomie')
add_if_absent('AcT', [('AcT', 'nom d’essai, non développé lettre à lettre dans le dossier de lecture')],
              'Essai AcT',
              'Ténectéplase 0,25 mg/kg non inférieure à l’altéplase (mRS 0–1 : 36,9 % contre 34,8 %).', 'i64-metalyse')
add_if_absent('mRS', [('m', 'modified'), ('R', 'Rankin'), ('S', 'Scale')],
              'Échelle de Rankin modifiée',
              'Échelle de dépendance fonctionnelle de 0 à 6 ; un score de 0 ou 1 signifie l’absence de handicap significatif.', 'i64-metalyse')
add_if_absent('NINDS', [('N', 'National'), ('I', 'Institute'), ('N', 'of Neurological'), ('D', 'Disorders'), ('S', 'and Stroke')],
              'Essai NINDS',
              'Essai de l’altéplase dans lequel l’hémorragie intracrânienne atteignait 15,4 %, toutes hémorragies confondues.', 'i64-actilyse')
add_if_absent('ECASS', [('E', 'European'), ('C', 'Cooperative'), ('A', 'Acute'), ('S', 'Stroke'), ('S', 'Study')],
              'Étude ECASS',
              'L’essai ECASS III rapporte une hémorragie intracrânienne de 14,1 %, toutes hémorragies confondues.', 'i64-actilyse')
add_if_absent('INTERACT4', [('INTERACT', 'nom d’essai, non développé lettre à lettre dans le dossier de lecture'), ('4', 'quatrième essai')],
              'Essai INTERACT4',
              'Abaissement tensionnel préhospitalier à l’urapidil chez 2303 patients : effet global nul, préjudice possible dans l’infarctus.', 'i64-tension-nature')
add_if_absent('RIGHT-2', [('RIGHT', 'nom d’essai, non développé lettre à lettre dans le dossier de lecture'), ('2', 'deuxième essai')],
              'Essai RIGHT-2',
              'Trinitrine transdermique : l’expansion de l’hématome était de 46 % contre 27 % dans l’hémorragie.', 'i64-tension-nature')
