import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K74', 'Fibrose et cirrhose du foie',
    'K74 — Fibrose et cirrhose du foie · CIM-10-GM 2024 · Foie',
    'Adulte · dépistage non invasif de la fibrose, maladie hépatique chronique avancée compensée, hypertension portale cliniquement significative, prévention de la décompensation · rédaction du 09.10.2026 · référentiels Baveno VII (2022), EASL tests non invasifs 2021, EASL cirrhose décompensée 2018, informations professionnelles suisses',
    'Pharmacologie de la cirrhose compensée')
w = C.w
BAV = ('de Franchis R. et al., Baveno VII — Renewing consensus in portal hypertension, J Hepatol 2022;76:959-974', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11090185/')
NIT = ('EASL Clinical Practice Guidelines on non-invasive tests for evaluation of liver disease severity and prognosis — 2021 update, J Hepatol 2021;75:659-689', 'https://easl.eu/wp-content/uploads/2021/06/EASL-Clinical-Practice-Guidelines-on-non-invasive-tests-for-evaluation-of-liver-disease-severity-and-prognosis-%E2%80%93-2021-update.pdf')
DEC = ('EASL Clinical Practice Guidelines for the management of patients with decompensated cirrhosis, J Hepatol 2018;69:406-460', 'https://doi.org/10.1016/j.jhep.2018.03.024')
PUGH = ('Pugh R. N. H. et al., Transection of the oesophagus for bleeding oesophageal varices, Br J Surg 1973;60:646-649 (score de Child-Pugh)', 'https://doi.org/10.1002/bjs.1800600817')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS via AmiKo), consultée le 09.10.2026', 'https://amiko.oddb.org/fr')

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 61 ans, diabétique de type 2 et en surpoids, boit environ trois verres de vin par jour. Son médecin de famille note des transaminases discrètement élevées et des plaquettes à 138 G/l. Or, il ne se plaint de rien. <b>La question est donc de savoir s’il a une fibrose avancée, voire une cirrhose silencieuse, et si une hypertension portale menace déjà de le décompenser.</b>',
 'Pour répondre à cette question, le médecin doit savoir : calculer le ' + w('k74-fib4', 'score FIB-4') + ' et interpréter une ' + w('k74-elasto', 'élastographie impulsionnelle') + ' ; reconnaître une ' + w('k74-cacld', 'maladie hépatique chronique avancée compensée') + ' ; identifier l’' + w('k74-csph', 'hypertension portale cliniquement significative') + ' sans geste invasif ; supprimer la cause ; enfin, prévenir la ' + w('k74-decompensation', 'décompensation') + ' par un bêtabloquant non sélectif quand il est indiqué.')
 + key(w('k74-fib4', 'FIB-4') + ' puis ' + w('k74-elasto', 'élastographie') + ' pour dépister ; ' + w('k74-csph', 'hypertension portale cliniquement significative') + ' pour décider du traitement préventif.', 'Point de départ.'))

C.a(1, 'Définition et stades', P(
 'La fibrose est l’accumulation de matrice extracellulaire dans le foie au cours d’une agression chronique ; la cirrhose en est le stade ultime, où des septa fibreux entourent des nodules de régénération. Cependant, la fibrose sévère et la cirrhose forment un continuum chez le patient asymptomatique, et les distinguer cliniquement est souvent impossible. C’est pourquoi Baveno VII retient le terme de ' + w('k74-cacld', 'maladie hépatique chronique avancée compensée') + ' (cACLD), défini de façon pragmatique par l’élastographie ; de plus, « cACLD » et « cirrhose compensée » sont tous deux acceptés.',
 'À partir de cette définition, l’évolution se découpe en stades. Ainsi, la cirrhose compensée se définit par l’absence de complication présente ou passée ; elle comporte deux stades, selon l’absence ou la présence d’une hypertension portale cliniquement significative (Baveno VII, 5.1-5.2). En revanche, la ' + w('k74-decompensation', 'décompensation') + ' est marquée par une ascite manifeste, une encéphalopathie hépatique manifeste ou une hémorragie variqueuse ; or, ce passage augmente nettement le risque de décès.')
 + table(['Stade', 'Critère', 'Enjeu'], [
   ['Fibrose non avancée', 'Élastographie < 8 kPa ou FIB-4 < 1,3', 'Traiter la cause, retester'],
   ['cACLD sans hypertension portale significative', 'Élastographie ≥ 10 kPa ; ≤ 15 kPa avec plaquettes ≥ 150 G/l', 'Traiter la cause, surveiller'],
   ['cACLD avec hypertension portale significative', 'Élastographie ≥ 25 kPa, ou gradient porto-hépatique ≥ 10 mmHg', 'Prévenir la décompensation (bêtabloquant)'],
   ['Cirrhose décompensée', 'Ascite, encéphalopathie, hémorragie variqueuse', 'Traiter la complication, discuter la transplantation']])
 + C.img('k74_cirrhose_macro.gif', 'Photographie d’un foie entier à surface finement granuleuse, faite de petits nodules réguliers.', 'Cirrhose micronodulaire d’origine alcoolique, vue macroscopique. La surface est hérissée de nodules de moins de 3 mm, séparés par des sillons fibreux.', credit({'auteur': 'Amadalvarez', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Cirrosi_micronodular.1427.jpg'}))
 + P('Le tableau se lit de haut en bas : en effet, chaque stade ajoute un risque, si bien que l’objectif passe de la suppression de la cause à la prévention des complications.')
 + key('La fibrose et la cirrhose forment un continuum : la cACLD évolue vers une cirrhose compensée sans, puis avec hypertension portale significative, et enfin vers la décompensation (ascite, encéphalopathie, hémorragie).')
 + src(BAV, NIT))

C.a(2, 'Étiologies et facteurs aggravants', P(
 'Après la définition, la cause oriente toute la suite. Ainsi, les causes principales sont la consommation d’alcool, les hépatites virales chroniques B et C et la maladie stéatosique métabolique ; plus rarement, il s’agit d’une cholangite biliaire primitive, d’une hépatite auto-immune ou d’une maladie génétique. De plus, Baveno VII souligne que le surpoids, l’obésité, le diabète et l’alcool font progresser la maladie même après la suppression de la cause principale (énoncé 3.3).',
 'Par ailleurs, une agression surajoutée peut précipiter la décompensation : hépatite alcoolique aiguë, hépatite virale aiguë A ou E, poussée d’hépatite B ou atteinte médicamenteuse (énoncé 5.12). En outre, les infections bactériennes sont fréquentes chez le patient avec hypertension portale significative et peuvent déclencher une décompensation (énoncé 5.10).')
 + trap('Aucune donnée nationale suisse de prévalence de la cirrhose n’a été retrouvée lors de la rédaction ; aucun chiffre n’est donc avancé.', 'Lacune documentaire')
 + key('L’alcool, les virus B et C et la maladie métabolique en sont les causes. Les cofacteurs (obésité, diabète, alcool) se traitent même après la suppression de la cause, car ils entretiennent la fibrose. Une agression surajoutée ou une infection précipitent la décompensation.')
 + src(BAV))

C.a(3, 'Physiopathologie : de la fibrose à l’hypertension portale', P(
 'Pour comprendre la gravité, il faut suivre la conséquence hémodynamique de la fibrose. Normalement, le sang portal traverse les sinusoïdes avec une faible résistance. Or, la fibrose et les nodules augmentent cette résistance ; dès lors, la pression portale s’élève. Ainsi, un ' + w('k74-hvpg', 'gradient de pression porto-hépatique') + ' supérieur à 5 mmHg définit l’hypertension portale sinusoïdale, et un gradient d’au moins 10 mmHg définit l’hypertension portale cliniquement significative (Baveno VII, 1.9-1.10).',
 'Ensuite, une vasodilatation splanchnique augmente le débit portal, ce qui entretient l’hypertension. Par conséquent, des collatérales porto-systémiques s’ouvrent, dont les varices œsophagiennes ; de plus, l’hypertension portale favorise l’ascite et l’encéphalopathie. Enfin, la réduction de la masse hépatique fonctionnelle altère la synthèse (albumine, facteurs de coagulation) et l’excrétion de la bilirubine.')
 + C.img('k74_trichrome.gif', 'Coupe histologique de foie en coloration trichrome : bandes de fibrose colorées en bleu entourant des nodules d’hépatocytes roses.', 'Cirrhose alcoolique chronique, coloration trichrome. Les septa fibreux, colorés en bleu, isolent des nodules de régénération : c’est cette architecture qui augmente la résistance intrahépatique au flux portal.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Trichrome_stain_of_chronic_alcoholic_cirrhosis.jpg'}))
 + key('La fibrose augmente la résistance sinusoïdale, et le gradient dépasse 5 mmHg ; à partir de 10 mmHg, l’hypertension portale devient cliniquement significative. La vasodilatation splanchnique et les collatérales en découlent.')
 + src(BAV))

C.a(4, 'Présentation clinique', P(
 'La démarche commence donc par la recherche d’une maladie souvent muette. En effet, la cirrhose compensée est fréquemment asymptomatique ; elle est alors découverte devant des transaminases anormales, une thrombopénie, une imagerie évocatrice ou une élastographie élevée. Cependant, l’examen peut montrer des signes d’insuffisance hépatocellulaire, comme des ' + w('k74-angiome', 'angiomes stellaires') + ' ou une érythrose palmaire, et des signes d’hypertension portale, comme une splénomégalie ou une circulation veineuse collatérale abdominale.',
 'À l’inverse, la décompensation est bruyante : ascite, encéphalopathie, hémorragie digestive, ictère. Par conséquent, l’examen recherche aussi les facteurs de décompensation, notamment une infection, une hépatite alcoolique surajoutée ou une prise médicamenteuse.')
 + C.img('k74_angiome_stellaire.gif', 'Photographies cutanées : lésions vasculaires rouges centrées par un point artériolaire, avec des ramifications radiaires.', 'Angiomes stellaires géants chez un patient de 47 ans atteint d’une cirrhose prouvée par biopsie, avec ictère et ascite. L’artériole centrale et ses ramifications pâlissent à la pression.', credit({'auteur': 'Herbert L. Fred, MD et Hendrik A. van Dijk', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Spider_nevus.jpg'}))
 + key('La cirrhose compensée reste souvent muette et se révèle par une thrombopénie, des transaminases ou une élastographie. L’examen recherche des angiomes stellaires, une érythrose palmaire, une splénomégalie et une circulation collatérale.')
 + src(BAV))

C.a(5, 'Dépistage de la fibrose avancée en médecine de premier recours', P(
 'Au terme de l’examen, la question est de savoir qui adresser au spécialiste. Ainsi, chez un patient qui a des cofacteurs métaboliques ou une consommation d’alcool, l’EASL 2021 propose de calculer d’abord le ' + w('k74-fib4', 'FIB-4') + ', à partir de l’âge, de l’ASAT, de l’ALAT et des plaquettes. En effet, un FIB-4 inférieur à 1,30 définit un faible risque : le patient reste en premier recours, modifie son mode de vie et sera retesté dans 1 à 3 ans.',
 'En revanche, un FIB-4 d’au moins 1,30 conduit à une ' + w('k74-elasto', 'élastographie impulsionnelle') + ' ou à un test sérique breveté. Par conséquent, une élasticité inférieure à 8 kPa confirme le faible risque, alors qu’une valeur d’au moins 8 kPa justifie l’adresse au spécialiste. De plus, chez le patient atteint de maladie alcoolique, une élastographie inférieure à 8 kPa exclut la fibrose avancée, et une valeur d’au moins 12 à 15 kPa la confirme, après avoir écarté les causes de faux positifs (EASL 2021, recommandations fortes).')
 + quiz('Le patient du début a un FIB-4 à 2,1. Que faire ?',
   [('Rassurer et retester dans 3 ans', False), ('Élastographie impulsionnelle', True), ('Biopsie hépatique d’emblée', False)],
   'Un FIB-4 ≥ 1,30 n’exclut pas la fibrose avancée ; l’élastographie impulsionnelle est l’étape suivante, et une valeur ≥ 8 kPa conduit au spécialiste (EASL 2021).')
 + key('Un FIB-4 < 1,30 signale un faible risque, et l’on refait le test à 1-3 ans. Un FIB-4 ≥ 1,30 impose une élastographie : sous 8 kPa, le risque est faible, alors qu’à partir de 8 kPa, le patient est adressé au spécialiste.')
 + src(NIT))

C.a(6, 'Reconnaître la cACLD et évaluer le pronostic', P(
 'Chez le spécialiste, l’élastographie classe ensuite la maladie. Ainsi, selon Baveno VII, une valeur inférieure à 10 kPa, en l’absence d’autre signe clinique ou d’imagerie, exclut la cACLD ; entre 10 et 15 kPa, elle la suggère ; au-delà de 15 kPa, elle la suggère fortement (énoncé 2.4). De plus, un patient en dessous de 10 kPa a un risque de décompensation ou de décès hépatique à 3 ans négligeable, inférieur ou égal à 1 % (énoncé 2.5).',
 'Cependant, l’élastographie peut donner des faux positifs. C’est pourquoi une première valeur d’au moins 10 kPa doit être répétée à jeun ou complétée par un marqueur sérique, par exemple un FIB-4 d’au moins 2,67 (énoncé 2.11). Par ailleurs, la ' + w('k74-regle5', 'règle des 5') + ' (10, 15, 20, 25 kPa) signale des risques relatifs croissants de décompensation et de décès, quelle que soit la cause (énoncé 2.9). Enfin, l’élastographie peut être répétée tous les 12 mois pour suivre l’évolution (énoncé 2.12).')
 + C.img('k74_elastographie.gif', 'Photographie d’un examen d’élastographie impulsionnelle : une soignante gantée applique la sonde sur le flanc droit d’un patient allongé, devant l’écran de l’appareil.', 'Réalisation d’une élastographie impulsionnelle du foie : la sonde est posée dans un espace intercostal droit, et l’appareil mesure la vitesse de propagation d’une onde de cisaillement, convertie en élasticité (kPa).', credit({'auteur': 'Goleisureintl', 'licence': 'CC BY 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Liver_Transient_Elastography_(FibroScan)_result_showing_Liver_Stiffness_Measurement_(LSM)_and_Controlled_Attenuation_Parameter_(CAP).jpg'}))
 + key('Sous 10 kPa, la cACLD est exclue et le risque à 3 ans est ≤ 1 % ; entre 10 et 15 kPa, elle est suggérée, et au-delà de 15 kPa, fortement suggérée. Une valeur ≥ 10 kPa se confirme à jeun ou par un FIB-4 ≥ 2,67, et la règle des 5 gradue le risque.')
 + src(BAV, NIT))

C.a(7, 'Identifier l’hypertension portale cliniquement significative', P(
 'Une fois la cACLD établie, la question décisive est celle de l’hypertension portale. Or, si le gradient porto-hépatique reste la référence, Baveno VII juge les tests non invasifs suffisamment précis en pratique (énoncé 2.14). Ainsi, une élastographie d’au plus 15 kPa avec des plaquettes d’au moins 150 G/l exclut l’hypertension portale significative (énoncé 2.15). À l’inverse, une élastographie d’au moins 25 kPa suffit à l’affirmer dans les causes virales et alcooliques et chez le patient non obèse atteint de maladie métabolique (énoncé 2.16).',
 'Entre ces deux seuils, le ' + w('k74-anticipate', 'modèle ANTICIPATE') + ' estime le risque. Par exemple, une élastographie de 20 à 25 kPa avec des plaquettes inférieures à 150 G/l, ou de 15 à 20 kPa avec des plaquettes inférieures à 110 G/l, comporte un risque d’hypertension portale significative d’au moins 60 % (énoncé 2.17). De plus, chez le patient porteur d’une hépatite virale, l’élasticité splénique peut aider (énoncé 2.21).')
 + quiz('Un patient atteint d’une cirrhose alcoolique abstinente a une élastographie à 27 kPa et des plaquettes à 160 G/l. Hypertension portale significative ?',
   [('Exclue, car les plaquettes sont normales', False), ('Affirmée, car l’élastographie est ≥ 25 kPa', True), ('Indéterminée sans gradient porto-hépatique', False)],
   'Dans une cause alcoolique ou virale, une élastographie ≥ 25 kPa suffit à affirmer l’hypertension portale cliniquement significative (Baveno VII, 2.16) ; l’exclusion exige ≤ 15 kPa et plaquettes ≥ 150 G/l.')
 + key('L’hypertension portale significative est exclue si l’élastographie est ≤ 15 kPa avec des plaquettes ≥ 150 G/l, et affirmée à partir de 25 kPa (causes virale, alcoolique et métabolique sans obésité). Entre les deux, on utilise le modèle ANTICIPATE.')
 + src(BAV))

C.a(8, 'Traiter la cause', P(
 'Le stade établi, le premier traitement est étiologique. En effet, Baveno VII définit la suppression de la cause par la réponse virologique soutenue dans l’hépatite C, la suppression virale dans l’hépatite B sans co-infection delta et l’abstinence prolongée dans la maladie alcoolique (énoncé 3.1). Or, cette suppression fait baisser le gradient porto-hépatique chez la plupart des patients et réduit fortement le risque de décompensation (énoncé 3.4).',
 'De plus, la disparition de l’hypertension portale significative après suppression de la cause prévient la décompensation (énoncé 3.5). Par conséquent, un patient guéri de l’hépatite C, sans cofacteur, dont l’élastographie reste inférieure à 12 kPa et les plaquettes supérieures à 150 G/l peut sortir de la surveillance de l’hypertension portale (énoncé 3.7). Toutefois, l’obésité, le diabète et l’alcool doivent toujours être pris en charge (énoncé 3.3).')
 + trap('La surveillance du carcinome hépatocellulaire chez le patient cirrhotique n’est pas détaillée dans les sources lues pour ce cours ; elle sera traitée dans le cours C22 — Tumeur maligne du foie. TODO : source EASL CHC à intégrer.', 'Renvoi')
 + key('Supprimer la cause (réponse virologique C, suppression B, abstinence) fait baisser la pression portale et la décompensation ; traiter obésité, diabète et alcool.')
 + src(BAV))

C.a(9, 'Prévenir la décompensation', P(
 'Si l’hypertension portale significative persiste, le risque de décompensation justifie un traitement préventif. Ainsi, Baveno VII propose un ' + w('k74-bbns', 'bêtabloquant non sélectif') + ' (propranolol, nadolol ou carvédilol) pour prévenir la décompensation chez le patient avec hypertension portale significative (énoncé 5.14). De plus, le ' + w('k74-d-carvedilol', 'carvédilol') + ' est préféré : en effet, il baisse davantage le gradient grâce à son effet alpha-bloquant vasodilatateur, il est mieux toléré et il améliore la survie par rapport à l’absence de traitement (énoncé 5.15).',
 'Par conséquent, le patient traité par bêtabloquant n’a pas besoin d’une endoscopie de dépistage des varices (énoncé 5.17). En revanche, sans hypertension portale significative, aucun bêtabloquant n’est indiqué (énoncé 5.20). Enfin, chez le patient qui ne peut pas recevoir de bêtabloquant, une ' + w('k74-endoscopie', 'endoscopie de dépistage') + ' est faite si l’élastographie atteint 20 kPa ou si les plaquettes sont au plus de 150 G/l (énoncé 2.19) ; sinon, l’élastographie et les plaquettes sont contrôlées chaque année (énoncé 2.20).')
 + key('En cas d’hypertension portale significative, on donne un bêtabloquant non sélectif, de préférence le carvédilol, sans endoscopie de dépistage. Sans elle, on n’en donne pas. Si le bêtabloquant est contre-indiqué, on fait une endoscopie quand l’élastographie est ≥ 20 kPa ou les plaquettes ≤ 150 G/l.')
 + C.pareto('pareto-k74-clinique', 'Fibrose et cirrhose', ['k74-1', 'k74-5', 'k74-6', 'k74-7', 'k74-8', 'k74-9'],
     ['FIB-4 < 1,30 : faible risque ; ≥ 1,30 : élastographie.',
      'Une élastographie < 10 kPa exclut la cACLD, et une valeur > 15 kPa la rend probable.',
      'Hypertension portale exclue : ≤ 15 kPa et plaquettes ≥ 150 G/l.',
      'Hypertension portale affirmée : ≥ 25 kPa.',
      'Supprimer la cause : abstinence, antiviraux.',
      'Hypertension portale significative : carvédilol, sans endoscopie de dépistage.'])
 + src(BAV))

C.a(10, 'Traitements non étiologiques et comorbidités', P(
 'Au-delà du bêtabloquant, d’autres traitements modifient l’évolution. Ainsi, les ' + w('k74-statines', 'statines') + ' doivent être encouragées chez le patient cirrhotique qui a une indication reconnue, car elles peuvent baisser la pression portale et améliorer la survie (Baveno VII, 4.1). Cependant, en cirrhose Child-Pugh B ou C, la dose est réduite (simvastatine au plus 20 mg/j) et la toxicité musculaire et hépatique est surveillée ; de plus, en classe C, leur bénéfice n’est pas démontré (énoncé 4.2).',
 'De même, l’aspirine ne doit pas être découragée quand elle est indiquée (énoncé 4.3), et l’anticoagulation ne doit pas l’être non plus en cas d’indication reconnue (énoncé 4.11). Enfin, les comorbidités non hépatiques sont fréquentes et pèsent sur le pronostic ; c’est pourquoi elles doivent être prises en charge spécifiquement (énoncé 5.8).')
 + key('Statines si indication (simvastatine ≤ 20 mg/j en Child B ou C) ; aspirine et anticoagulants non découragés si indiqués ; comorbidités à traiter.')
 + src(BAV))

C.a(11, 'Pronostic : scores de Child-Pugh et MELD', P(
 'Pour suivre le patient, deux scores résument la fonction hépatique. D’abord, le ' + w('k74-child', 'score de Child-Pugh') + ' associe la bilirubine, l’albumine, le temps de prothrombine, l’ascite et l’encéphalopathie ; il classe la cirrhose en A, B ou C. Ensuite, le ' + w('k74-meld', 'score MELD') + ', fondé sur la bilirubine, l’INR et la créatinine, est le score le plus utilisé pour prédire la survie et prioriser la transplantation (EASL 2018).',
 'Cependant, ces scores ne remplacent pas l’évaluation de l’hypertension portale. En effet, un patient Child-Pugh A peut avoir une hypertension portale significative et un risque de décompensation élevé. Par conséquent, la stratégie de Baveno VII repose d’abord sur l’élastographie et les plaquettes, puis sur les scores, qui restent indispensables dès la décompensation.')
 + key('Child-Pugh (A, B, C) et MELD mesurent la fonction ; l’élastographie et les plaquettes mesurent le risque portal : les deux sont complémentaires.')
 + src(DEC, PUGH, BAV))

C.a(12, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons le patient du début. Son FIB-4 vaut 2,1 ; par conséquent, une élastographie est faite et montre 21 kPa, confirmée à jeun. Il s’agit donc d’une cACLD. Or, avec des plaquettes à 138 G/l et une élasticité entre 20 et 25 kPa, le modèle ANTICIPATE estime un risque d’hypertension portale significative d’au moins 60 %.',
 'Dès lors, la conduite associe trois mesures. D’abord, l’abstinence d’alcool, la perte de poids et l’optimisation du diabète traitent les causes et les cofacteurs. Ensuite, le carvédilol est discuté pour prévenir la décompensation, en tenant compte de son statut hors indication en Suisse. Enfin, l’élastographie est répétée chaque année, et toute ascite, hémorragie ou confusion conduit à une hospitalisation.')
 + key('FIB-4 → élastographie → cACLD → risque portal (ANTICIPATE) → cause, cofacteurs, carvédilol, suivi annuel.')
 + src(BAV, NIT))

C.a(13, 'Critères formels et paramètres clés', alert(
 '<p>La <b>cACLD</b> est exclue sous 10 kPa, suggérée entre 10 et 15 kPa et fortement suggérée au-delà de 15 kPa. L’<b>hypertension portale cliniquement significative</b> correspond à un gradient porto-hépatique ≥ 10 mmHg ; elle est exclue si l’élastographie est ≤ 15 kPa avec des plaquettes ≥ 150 G/l, et affirmée à partir de 25 kPa. La <b>décompensation</b> se définit par une ascite manifeste, une encéphalopathie de grade West Haven ≥ II ou une hémorragie variqueuse.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Le FIB-4 exclut sous 1,30 et confirme à partir de 2,67. L’élastographie utilise 8 kPa au premier recours et 10, 15, 20 et 25 kPa selon la règle des 5. On fait une endoscopie si le bêtabloquant est impossible et que l’élastographie est ≥ 20 kPa ou les plaquettes ≤ 150 G/l. En Child B ou C, la simvastatine ne dépasse pas 20 mg/j, et en cas d’ascite sévère, le propranolol ne dépasse pas 80 mg/j.</div>'
 + src(BAV, NIT, DEC))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Place'], [
   ['Risque de fibrose avancée ?', w('k74-fib4', 'FIB-4'), 'Premier recours, premier test'],
   ['Fibrose avancée ou cACLD ?', w('k74-elasto', 'Élastographie impulsionnelle'), 'Si FIB-4 ≥ 1,30 ; spécialiste'],
   ['Hypertension portale significative ?', 'Élastographie + plaquettes ; ' + w('k74-anticipate', 'ANTICIPATE'), 'cACLD'],
   ['Varices à traiter ?', w('k74-endoscopie', 'Gastroscopie'), 'Si bêtabloquant impossible et ≥ 20 kPa ou plaquettes ≤ 150 G/l'],
   ['Mesure de référence de la pression portale ?', w('k74-hvpg', 'Gradient porto-hépatique'), 'Centres de référence, cas sélectionnés'],
   ['Cause ou stade incertain ?', w('k74-biopsie', 'Biopsie hépatique'), 'Cas sélectionnés']])
 + P('Le tableau se lit de haut en bas : ainsi, les examens invasifs sont réservés aux cas où les tests simples ne suffisent pas.')
 + key('On calcule d’abord le FIB-4, puis on fait une élastographie, puis on combine élastographie et plaquettes pour juger la pression portale ; la gastroscopie, le gradient et la biopsie sont réservés à des cas sélectionnés.')
 + src(NIT, BAV))

C.e(2, 'Interpréter une élastographie impulsionnelle', P(
 'L’élastographie mesure la dureté du foie en kilopascals ; cependant, la dureté ne dépend pas que de la fibrose. En effet, une inflammation, une cholestase, une congestion ou un repas récent peuvent l’augmenter. C’est pourquoi l’examen est fait à jeun, et une valeur élevée inattendue est contrôlée. De plus, l’EASL 2021 signale qu’en présence d’une inflammation biologique marquée (ASAT ou GGT supérieures à deux fois la normale), l’élasticité surestime la fibrose.',
 'Ensuite, l’interprétation suit des seuils hiérarchisés : 8 kPa en premier recours, 10 et 15 kPa pour la cACLD, 25 kPa pour l’hypertension portale, et la règle des 5 pour le pronostic. Enfin, une baisse cliniquement significative se définit par une diminution d’au moins 20 % avec une valeur inférieure à 20 kPa, ou par toute baisse sous 10 kPa (Baveno VII, 2.13).')
 + quiz('Un patient alcoolique hospitalisé pour hépatite alcoolique (ASAT 4 fois la normale) a une élastographie à 18 kPa. Conclusion ?',
   [('Cirrhose certaine', False), ('Valeur probablement surestimée par l’inflammation : contrôler à distance', True), ('Hypertension portale affirmée', False)],
   'L’inflammation hépatique augmente la dureté ; l’EASL 2021 demande d’en tenir compte et de répéter la mesure après correction, par exemple après abstinence.')
 + key('L’élastographie se fait à jeun, car l’inflammation, la cholestase et la congestion la surestiment. Ses seuils sont 8, 10, 15 et 25 kPa. Une baisse est significative si elle atteint ≥ 20 % avec une valeur < 20 kPa, ou si la valeur passe sous 10 kPa.')
 + C.pareto('pareto-k74-examens', 'Examens', ['k74-e-1', 'k74-e-2'],
     ['FIB-4 < 1,30 : faible risque.',
      'Élastographie < 8 kPa en premier recours : faible risque.',
      '≥ 10 kPa : confirmer à jeun ou par FIB-4 ≥ 2,67.',
      'À partir de 25 kPa, l’hypertension portale est significative.',
      'L’inflammation surestime l’élastographie.'])
 + src(NIT, BAV))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : le système porte et ses collatérales', P(
 'La veine porte naît de la confluence de la veine splénique et de la veine mésentérique supérieure ; ainsi, elle draine le sang de l’intestin et de la rate vers le foie. Or, quand la résistance hépatique augmente, le sang emprunte les anastomoses porto-caves : veines gastriques et œsophagiennes, veine ombilicale reperméabilisée, plexus rectaux. Par conséquent, les varices œsophagiennes, la circulation collatérale abdominale et la splénomégalie sont les traductions anatomiques de l’hypertension portale.')
 + key('C’est pourquoi la splénomégalie et la thrombopénie (hypersplénisme) font partie des signes d’hypertension portale utilisés par les tests non invasifs.', 'Science → examen.'))
C.s('histo', 'Histologie', 'Histologie : septa et nodules', P(
 'Dans la fibrose, les cellules étoilées du foie, activées par l’agression chronique, se transforment en myofibroblastes et produisent du collagène. Ainsi, la fibrose débute autour des espaces portes ou des veines centrolobulaires selon la cause ; ensuite, des septa relient ces structures. Enfin, la cirrhose associe des septa annulaires et des nodules de régénération, visibles en bleu à la coloration trichrome. Toutefois, cette architecture peut partiellement régresser lorsque la cause est supprimée.')
 + key('C’est pourquoi l’élastographie baisse après abstinence ou guérison virale : la fibrose n’est pas figée.', 'Science → clinique.'))
C.s('phys', 'Physiologie', 'Physiologie : résistance, débit et gradient', P(
 'Comme dans tout circuit, la pression portale est le produit de la résistance et du débit. Ainsi, la fibrose et la contraction des cellules étoilées augmentent la résistance intrahépatique ; de plus, la vasodilatation splanchnique augmente le débit portal. Par conséquent, deux leviers existent : réduire le débit, ce que font les bêtabloquants non sélectifs par leurs effets bêta-1 (débit cardiaque) et bêta-2 (vasoconstriction splanchnique), et réduire la résistance, ce qu’ajoute l’effet alpha-bloquant du carvédilol.')
 + key('Le bêtabloquant non sélectif baisse le débit portal, et le carvédilol baisse en plus la résistance intrahépatique par son effet alpha-bloquant.', 'Science → traitement.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : le foie cirrhotique et les médicaments', P(
 'Le foie cirrhotique métabolise moins bien les médicaments à fort premier passage hépatique ; de plus, les shunts porto-systémiques les font passer directement dans la circulation. Ainsi, l’information professionnelle suisse du carvédilol rapporte une exposition multipliée par 6,8 chez le patient cirrhotique. Par conséquent, les doses sont réduites et titrées, et les médicaments hépatotoxiques ou sédatifs sont utilisés avec prudence.')
 + key('Le premier passage réduit et les shunts augmentent l’exposition ; c’est pourquoi on titre prudemment les bêtabloquants et les statines.', 'Science → traitement.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, le premier traitement est celui de la cause. En pratique, les médicaments propres à la cirrhose compensée visent donc surtout la pression portale.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Bêtabloquant non sélectif à effet alpha', 'Carvédilol', 'Prévention de la décompensation si hypertension portale significative', w('k74-d-carvedilol', 'Monographie')],
   ['Bêtabloquant non sélectif', 'Propranolol', 'Alternative', w('k74-bbns', 'Fiche')],
   ['Statine', 'Simvastatine', 'Indication reconnue ; dose réduite en Child B ou C', w('k74-statines', 'Fiche')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, aucun bêtabloquant n’est prescrit sans hypertension portale cliniquement significative.')
 + key('En cas d’hypertension portale significative, on préfère le carvédilol, avec le propranolol en alternative, et l’on donne des statines si elles sont indiquées.')
 + src(BAV))

C.p(2, 'Doses et statut réglementaire', P('Les éléments suivants proviennent de Baveno VII, de l’EASL 2018 et des informations professionnelles suisses ; de plus, les lacunes sont signalées.')
 + table(['Médicament', 'Situation', 'Dose ou règle', 'Source'], [
   ['Carvédilol', 'Hypertension portale significative', 'TODO : posologie hépatologique non retrouvée dans les sources lues ; titration prudente', 'Baveno VII 5.15 ; FI Carvédilol Sandoz®'],
   ['Propranolol', 'Ascite sévère ou réfractaire', 'Éviter les doses élevées (> 80 mg/j)', 'EASL 2018'],
   ['Carvédilol', 'Ascite réfractaire', 'Non recommandé à ce jour', 'EASL 2018'],
   ['Simvastatine', 'Child-Pugh B ou C', 'Au plus 20 mg/j, surveillance musculaire et hépatique', 'Baveno VII 4.2']])
 + trap('Le carvédilol n’est autorisé en Suisse que dans l’hypertension artérielle, l’angor et l’insuffisance cardiaque ; son information professionnelle le contre-indique en cas d’insuffisance hépatique cliniquement manifeste. Son usage dans l’hypertension portale est donc hors indication, à arbitrer à l’audit.', 'Point à valider')
 + P('Par exemple, chez le patient du début, compensé, le carvédilol serait débuté à faible dose sous surveillance de la pression artérielle et du pouls, après discussion du statut hors indication ; à l’inverse, l’apparition d’une ascite réfractaire ferait reconsidérer le traitement.')
 + key('Carvédilol : préféré par Baveno VII, hors indication en Suisse, contre-indiqué si insuffisance hépatique manifeste. Ascite sévère : propranolol ≤ 80 mg/j.')
 + src(BAV, DEC, FI('Carvédilol Sandoz®')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'Les bêtabloquants exposent à l’hypotension, à la bradycardie et à la fatigue ; c’est pourquoi la pression artérielle et le pouls sont surveillés. De plus, en cas d’hémorragie, de sepsis, d’infection du liquide d’ascite ou d’insuffisance rénale aiguë, l’EASL 2018 conseille de réduire ou de suspendre temporairement le bêtabloquant.', 'Sécurité.')
 + P('Au long cours, la surveillance porte aussi sur la fonction hépatique, car l’exposition au carvédilol augmente dans la cirrhose. Par ailleurs, les statines exigent une surveillance musculaire et hépatique en classe B ou C. Enfin, tout médicament sédatif ou néphrotoxique est évité, car il peut déclencher une encéphalopathie ou une insuffisance rénale.')
 + key('Sous bêtabloquant, on surveille la pression artérielle et le pouls, et l’on suspend temporairement le traitement en cas d’hémorragie, de sepsis, de péritonite ou d’insuffisance rénale aiguë. On reste prudent avec les sédatifs et les néphrotoxiques.')
 + C.pareto('pareto-k74-pharma', 'Pharmacologie', ['k74-p-1', 'k74-p-2', 'k74-p-3'],
     ['Pas de bêtabloquant sans hypertension portale significative.',
      'Carvédilol préféré (Baveno VII), hors indication en Suisse.',
      'Ascite sévère : propranolol ≤ 80 mg/j.',
      'Simvastatine ≤ 20 mg/j en Child B ou C.',
      'Suspendre le bêtabloquant si sepsis, hémorragie ou insuffisance rénale aiguë.'])
 + src(DEC, BAV, FI('Carvédilol Sandoz®')))

# ---------------- Fenêtres
L = lab
C.pop('k74-fib4', 'Score FIB-4', L(('Variables', 'Le score combine l’âge, l’ASAT, l’ALAT et les plaquettes, car la fibrose fait monter l’ASAT et baisser les plaquettes.'), ('Seuils', '< 1,30 : faible risque de fibrose avancée (EASL 2021) ; ≥ 2,67 : confirme une élastographie ≥ 10 kPa (Baveno VII, 2.11).'), ('Limite', 'Ne pas l’utiliser seul comme unique critère de décision (EASL 2021).')) + src(NIT, BAV))
C.pop('k74-elasto', 'Élastographie impulsionnelle', L(('Principe', 'Mesure de la vitesse d’une onde de cisaillement dans le foie, convertie en dureté (kPa).'), ('Seuils', 'Le seuil de 8 kPa sert au premier recours, ceux de 10 et 15 kPa classent la cACLD, et celui de 25 kPa affirme l’hypertension portale significative.'), ('Pièges', 'Un repas, une inflammation, une cholestase ou une congestion surestiment la mesure, car ils rigidifient le foie sans fibrose.')) + src(NIT, BAV) + C.img('k74_elastographie.gif', 'Examen d’élastographie impulsionnelle : sonde appliquée sur le flanc droit.', 'La sonde envoie une onde de cisaillement et mesure sa vitesse dans le foie ; plus le foie est fibreux, plus l’onde va vite et plus la valeur en kPa monte.', credit({'auteur': 'Goleisureintl', 'licence': 'CC BY 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Liver_Transient_Elastography_(FibroScan)_result_showing_Liver_Stiffness_Measurement_(LSM)_and_Controlled_Attenuation_Parameter_(CAP).jpg'})))
C.pop('k74-cacld', 'Maladie hépatique chronique avancée compensée (cACLD)', L(('Définition', 'La cACLD couvre le spectre de la fibrose sévère à la cirrhose chez un patient compensé, qui risque une hypertension portale significative.'), ('Critères (Baveno VII)', '< 10 kPa : exclue ; 10-15 kPa : suggestive ; > 15 kPa : fortement suggestive.'), ('Conduite', 'Adresse au spécialiste (énoncé 2.6).')) + src(BAV) + C.img('k74_cirrhose_macro.gif', 'Foie entier à surface finement nodulaire.', 'La surface est faite de petits nodules réguliers, car les hépatocytes se régénèrent entre des cloisons fibreuses ; c’est cette architecture qui augmente la résistance au flux portal.', credit({'auteur': 'Amadalvarez', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Cirrosi_micronodular.1427.jpg'})))
C.pop('k74-csph', 'Hypertension portale cliniquement significative', L(('Définition', 'Gradient de pression porto-hépatique ≥ 10 mmHg.'), ('Non invasif', 'On l’exclut si l’élastographie est ≤ 15 kPa avec des plaquettes ≥ 150 G/l, et on l’affirme si elle est ≥ 25 kPa.'), ('Conséquence', 'Elle augmente le risque de décompensation et justifie donc un bêtabloquant non sélectif.')) + src(BAV))
C.pop('k74-decompensation', 'Décompensation de la cirrhose', L(('Événements (Baveno VII, 5.4)', 'La décompensation se définit par une ascite manifeste (ou un hydrothorax avec un gradient d’albumine > 1,1 g/dl), une encéphalopathie manifeste (West Haven ≥ II) ou une hémorragie variqueuse.'), ('Précipitants', 'Infection, hépatite surajoutée, médicament, carcinome, chirurgie majeure.')) + src(BAV))
C.pop('k74-hvpg', 'Gradient de pression porto-hépatique', L(('Mesure', 'Par cathétérisme, on soustrait la pression veineuse sus-hépatique libre de la pression bloquée.'), ('Seuils', 'Au-delà de 5 mmHg, l’hypertension portale est sinusoïdale ; à partir de 10 mmHg, elle est cliniquement significative.'), ('Limite', 'Il sous-estime la pression dans la cholangite biliaire primitive, car l’obstacle y est en partie présinusoïdal.')) + src(BAV))
C.pop('k74-angiome', 'Angiome stellaire', L(('Aspect', 'Artériole centrale avec ramifications radiaires, qui blanchit à la pression.'), ('Signification', 'Il signale une insuffisance hépatocellulaire chronique, car le foie dégrade moins les œstrogènes vasodilatateurs.')) + C.img('k74_angiome_stellaire.gif', 'Photographies cutanées : angiomes stellaires centrés par une artériole.', 'Le point central est une artériole dilatée d’où partent des vaisseaux radiaires ; la pression sur le centre efface l’angiome, ce qui le distingue d’un pétéchie.', credit({'auteur': 'Herbert L. Fred, MD et Hendrik A. van Dijk', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Spider_nevus.jpg'})))
C.pop('k74-regle5', 'Règle des 5 (Baveno VII, 2.9)', L(('Seuils', 'Les seuils sont 10, 15, 20 et 25 kPa ; chaque palier de 5 kPa augmente le risque.'), ('Signification', 'Risques relatifs croissants de décompensation et de décès hépatique, quelle que soit la cause.')) + src(BAV))
C.pop('k74-anticipate', 'Modèle ANTICIPATE', L(('Variables', 'Le modèle combine l’élastographie et les plaquettes.'), ('Exemples (Baveno VII, 2.17)', '20-25 kPa et plaquettes < 150 G/l, ou 15-20 kPa et plaquettes < 110 G/l : risque d’hypertension portale significative ≥ 60 %.'), ('Domaine', 'Il s’applique aux causes virales, alcooliques et métaboliques sans obésité.')) + src(BAV))
C.pop('k74-bbns', 'Bêtabloquants non sélectifs', L(('Molécules', 'Propranolol, nadolol, carvédilol.'), ('Indication', 'On les donne pour prévenir la décompensation en cas d’hypertension portale significative (Baveno VII, 5.14), car ils baissent le débit portal.'), ('Non indiqués', 'Sans hypertension portale significative (5.20).')) + src(BAV))
C.pop('k74-d-carvedilol', 'Carvédilol', L(('Place (Baveno VII, 5.15)', 'Baveno VII le préfère dans la cirrhose compensée, car il baisse davantage le gradient, est mieux toléré et améliore la survie.'), ('Statut suisse', 'Autorisé dans l’hypertension artérielle, l’angor et l’insuffisance cardiaque ; contre-indiqué si insuffisance hépatique manifeste ; exposition × 6,8 dans la cirrhose.'), ('Ascite réfractaire', 'Non recommandé (EASL 2018).')) + src(BAV, DEC, FI('Carvédilol Sandoz®')))
C.pop('k74-endoscopie', 'Endoscopie de dépistage des varices', L(('Indication (Baveno VII, 2.19)', 'Patient ne pouvant recevoir de bêtabloquant, avec élastographie ≥ 20 kPa ou plaquettes ≤ 150 G/l.'), ('Sinon', 'Sinon, on répète l’élastographie et les plaquettes chaque année (2.20).'), ('Sous bêtabloquant', 'Elle n’est pas nécessaire sous bêtabloquant (5.17), car le traitement ne changerait pas.')) + src(BAV))
C.pop('k74-statines', 'Statines dans la cirrhose', L(('Indication', 'Indication reconnue : à encourager (Baveno VII, 4.1).'), ('Child-Pugh B ou C', 'On ne dépasse pas 20 mg/j de simvastatine et l’on surveille les muscles et le foie (4.2), car le foie malade l’élimine moins bien.'), ('Child-Pugh C', 'Bénéfice non démontré, usage restrictif.')) + src(BAV))
C.pop('k74-child', 'Score de Child-Pugh', L(('Critères (1, 2 ou 3 points)', 'La bilirubine vaut 1, 2 ou 3 points pour < 2, 2-3 ou > 3 mg/dl ; l’albumine pour > 35, 28-35 ou < 28 g/l ; l’INR pour < 1,7, 1,7-2,3 ou > 2,3 ; l’ascite selon qu’elle est absente, légère ou modérée à importante ; l’encéphalopathie selon qu’elle est absente, de grade 1-2 ou de grade 3-4.'), ('Classes', 'A : 5-6 ; B : 7-9 ; C : 10-15.'), ('Note', 'La version usuelle utilise l’INR, alors que le score original utilisait l’allongement du temps de prothrombine.')) + src(PUGH))
C.pop('k74-meld', 'Score MELD', L(('Variables', 'Il combine la bilirubine, l’INR et la créatinine, et ses variantes ajoutent le sodium (MELD-Na).'), ('Usage', 'C’est le score pronostique le plus utilisé, et il priorise la transplantation (EASL 2018).')) + src(DEC))
C.pop('k74-biopsie', 'Biopsie hépatique', L(('Place', 'Démarche individualisée en centre de référence (Baveno VII, 2.7).'), ('Indications', 'On la fait quand la cause est incertaine ou que les tests non invasifs sont discordants.')) + src(BAV) + C.img('k74_trichrome.gif', 'Histologie en trichrome : fibrose bleue entourant des nodules d’hépatocytes.', 'Le trichrome colore le collagène en bleu ; ainsi, les cloisons qui encerclent les nodules montrent la cirrhose, que la biopsie confirme quand les tests non invasifs divergent.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Trichrome_stain_of_chronic_alcoholic_cirrhosis.jpg'})))

C.termes = [
 (r'FIB-4', 'k74-fib4'), (r'élastographie', 'k74-elasto'), (r'cACLD', 'k74-cacld'), (r'hypertension portale significative', 'k74-csph'),
 (r'gradient porto-hépatique', 'k74-hvpg'), (r'carvédilol', 'k74-d-carvedilol'), (r'propranolol', 'k74-bbns'), (r'bêtabloquant', 'k74-bbns'),
 (r'ANTICIPATE', 'k74-anticipate'), (r'Child-Pugh', 'k74-child'), (r'MELD', 'k74-meld'), (r'statines?', 'k74-statines'), (r'simvastatine', 'k74-statines'),
 (r'décompensation', 'k74-decompensation'), (r'règle des 5', 'k74-regle5'), (r'angiomes? stellaires?', 'k74-angiome'), (r'biopsie', 'k74-biopsie'),
]

C.write()
