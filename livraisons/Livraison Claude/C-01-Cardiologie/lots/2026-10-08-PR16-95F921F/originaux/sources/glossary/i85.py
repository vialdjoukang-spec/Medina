# Glossaire MEDINA — I85 — Varices œsophagiennes et varices d’autres localisations (C-01-Cardiologie)
from cardio_1 import a, G

a('HVPG', [('H', 'Hepatic (hépatique)'), ('V', 'Venous (veineux)'), ('P', 'Pressure (de pression)'), ('G', 'Gradient')], 'Gradient de pression veineuse hépatique',
  '<p>Différence entre la pression sus-hépatique bloquée et la pression sus-hépatique libre, mesurée par cathétérisme jugulaire. Normal de 1 à 5 mmHg ; une valeur d’au moins 10 mmHg définit l’hypertension portale cliniquement significative.</p>', 'i85-hvpg')
a('TIPS', [('T', 'Transjugular (transjugulaire)'), ('I', 'Intrahepatic (intrahépatique)'), ('P', 'Portosystemic (portosystémique)'), ('S', 'Shunt (dérivation)')], 'Shunt portosystémique intrahépatique transjugulaire',
  '<p>Prothèse couverte placée par voie jugulaire entre une veine sus-hépatique et une branche portale ; elle court-circuite la résistance hépatique et abaisse le gradient portocave.</p>', 'i85-tips')
a('MELD', [('M', 'Model (modèle)'), ('E', 'for End-stage (de la phase terminale)'), ('L', 'Liver (du foie)'), ('D', 'Disease (de la maladie)')], 'Model for End-stage Liver Disease (score de maladie hépatique terminale)',
  '<p>Score calculé à partir de la bilirubine, de l’INR et de la créatinine ; il prédit la mortalité à trois mois et ordonne la liste de transplantation hépatique.</p>', 'i85-meld')
a('GOV1', [('G', 'Gastro-'), ('O', 'Oesophageal (œsophagienne)'), ('V', 'Varix (varice)'), ('1', 'type 1')], 'Varice gastro-œsophagienne de type 1 (Sarin)',
  '<p>Varice œsophagienne qui se prolonge sous le cardia le long de la petite courbure ; elle se traite comme une varice œsophagienne.</p>', 'i85-sarin')
a('GOV2', [('G', 'Gastro-'), ('O', 'Oesophageal (œsophagienne)'), ('V', 'Varix (varice)'), ('2', 'type 2')], 'Varice gastro-œsophagienne de type 2 (Sarin)',
  '<p>Varice œsophagienne qui se prolonge vers le fundus ; son hémorragie relève de la colle de cyanoacrylate ou de l’échoendoscopie, puis du TIPS.</p>', 'i85-sarin')
a('IGV1', [('I', 'Isolated (isolée)'), ('G', 'Gastric (gastrique)'), ('V', 'Varix (varice)'), ('1', 'type 1')], 'Varice gastrique isolée de type 1 (Sarin)',
  '<p>Varice isolée du fundus, sans varice œsophagienne ; elle fait rechercher une thrombose de la veine splénique.</p>', 'i85-sarin')
a('IGV2', [('I', 'Isolated (isolée)'), ('G', 'Gastric (gastrique)'), ('V', 'Varix (varice)'), ('2', 'type 2')], 'Varice gastrique isolée de type 2 (Sarin)',
  '<p>Varice gastrique isolée située ailleurs que dans le fundus.</p>', 'i85-sarin')
a('AASLD', [('A', 'American (américaine)'), ('A', 'Association'), ('S', 'for the Study (pour l’étude)'), ('L', 'of Liver (du foie)'), ('D', 'Diseases (des maladies)')], 'American Association for the Study of Liver Diseases (Association américaine pour l’étude des maladies du foie)',
  '<p>Société savante américaine d’hépatologie ; sa practice guidance de 2024 traite de l’hypertension portale et des varices.</p>')
a('ESGE', [('E', 'European (européenne)'), ('S', 'Society of (Société d’)'), ('G', 'Gastrointestinal (gastro-intestinale)'), ('E', 'Endoscopy (endoscopie)')], 'European Society of Gastrointestinal Endoscopy (Société européenne d’endoscopie gastro-intestinale)',
  '<p>Société savante européenne d’endoscopie digestive ; elle avalise le consensus Baveno VIII.</p>', 'i85-baveno')
a('PREDESCI', [('PREDESCI', 'nom d’essai formé sur « prévention de la décompensation de la cirrhose » ; non strictement lettre à lettre')], 'Essai PREDESCI (2019)',
  '<p>Essai randomisé espagnol de 201 patients compensés porteurs d’une hypertension portale cliniquement significative : le bêtabloquant a réduit la décompensation ou le décès de 27 % à 16 %.</p>', 'i85-predesci')
a('PTFE', [('P', 'Poly-'), ('T', 'Tétra-'), ('F', 'Fluoro-'), ('E', 'Éthylène')], 'Polytétrafluoroéthylène',
  '<p>Polymère qui recouvre les prothèses de TIPS ; la couverture réduit l’occlusion du shunt par rapport aux prothèses nues.</p>', 'i85-tips')
a('CHC', [('C', 'Carcinome'), ('H', 'Hépato-'), ('C', '-Cellulaire')], 'Carcinome hépatocellulaire',
  '<p>Cancer primitif du foie, développé le plus souvent sur une cirrhose ; il se dépiste par une échographie tous les six mois chez le cirrhotique.</p>')
a('MASLD', [('M', 'Metabolic dysfunction (dysfonction métabolique)'), ('A', 'Associated (associée)'), ('S', 'Steatotic (stéatosique)'), ('L', 'Liver (du foie)'), ('D', 'Disease (maladie)')], 'Maladie stéatosique du foie associée à une dysfonction métabolique',
  '<p>Nouveau nom de la stéatose hépatique non alcoolique ; elle associe une stéatose à au moins un facteur de risque cardiométabolique.</p>')
a('SVP', [('S', 'Symptoms (symptômes)'), ('V', 'Varices'), ('P', 'Pathophysiology (physiopathologie)')], 'Classification SVP des troubles veineux pelviens',
  '<p>Classification de 2021 qui décrit les troubles veineux pelviens selon les symptômes, les varices et la physiopathologie (anatomie, hémodynamique, étiologie).</p>', 'i85-svp')
a('ANTICIPATE', [('ANTICIPATE', 'nom propre d’un modèle prédictif de l’hypertension portale cliniquement significative ; nom non développable lettre à lettre')], 'Modèle ANTICIPATE',
  '<p>Modèle qui estime la probabilité d’une hypertension portale cliniquement significative à partir de l’élasticité hépatique et des plaquettes.</p>', 'i85-anticipate')
a('AUDIT', [('A', 'Alcohol (alcool)'), ('U', 'Use (consommation)'), ('D', 'Disorders (troubles)'), ('I', 'Identification (repérage)'), ('T', 'Test')], 'Alcohol Use Disorders Identification Test (test de repérage des troubles liés à l’alcool)',
  '<p>Questionnaire de dix questions de l’Organisation mondiale de la santé qui repère une consommation d’alcool à risque ou une dépendance.</p>', 'i85-alcool')
a('SSG', [('S', 'Société'), ('S', 'Suisse de'), ('G', 'Gastroentérologie')], 'Société suisse de gastroentérologie',
  '<p>Société savante suisse de gastroentérologie et d’hépatologie. Aucune recommandation nationale spécifique sur les varices n’a été retrouvée ; la pratique suisse suit les consensus Baveno et l’EASL.</p>', 'i85-baveno')
a('Mallory-Weiss', [('Mallory-Weiss', 'nom propre : George Kenneth Mallory et Soma Weiss')], 'Syndrome de Mallory-Weiss',
  '<p>Déchirure longitudinale de la muqueuse du cardia provoquée par des efforts de vomissement ; cause d’hémorragie digestive haute.</p>', 'i85-mallory')
a('Sengstaken-Blakemore', [('Sengstaken-Blakemore', 'nom propre : Robert Sengstaken et Arthur Blakemore')], 'Sonde de Sengstaken-Blakemore',
  '<p>Sonde à deux ballonnets, gastrique et œsophagien, qui comprime les varices ; elle sert de pont vers le TIPS, mais Baveno VIII préfère une prothèse œsophagienne couverte.</p>', 'i85-tamponnement')
a('Cruveilhier-Baumgarten', [('Cruveilhier-Baumgarten', 'nom propre : Jean Cruveilhier et Paul Clemens von Baumgarten')], 'Souffle de Cruveilhier-Baumgarten',
  '<p>Souffle veineux continu péri-ombilical dû à la recanalisation de la veine paraombilicale dans l’hypertension portale.</p>', 'i85-cruveilhier')
a('K74.6', [('K74.6', 'code de la Classification internationale des maladies, 10e révision, modification allemande')], 'Cirrhose du foie, autre et sans précision',
  '<p>Code CIM-10-GM 2024 ; porte la croix lorsque des varices associées se codent avec l’astérisque I98.2* ou I98.3*.</p>', 'i85-codage')
a('K70.3', [('K70.3', 'code de la Classification internationale des maladies, 10e révision, modification allemande')], 'Cirrhose alcoolique du foie',
  '<p>Code CIM-10-GM 2024 ; porte la croix lorsque des varices associées se codent avec l’astérisque I98.2* ou I98.3*.</p>', 'i85-codage')
a('O22.1', [('O22.1', 'code de la Classification internationale des maladies, 10e révision, modification allemande')], 'Varices génitales au cours de la grossesse',
  '<p>Code CIM-10-GM 2024 ; les varices vulvaires survenant pendant la grossesse se codent ici et non en I86.3.</p>', 'i85-codage')
a('NH₃', [('N', 'azote (symbole chimique N)'), ('H₃', 'trois atomes d’hydrogène')], 'Ammoniac',
  '<p>Molécule produite surtout dans l’intestin et éliminée par le cycle de l’urée hépatique ; son accumulation contribue à l’encéphalopathie hépatique.</p>', 'i85-encephalopathie')
a('NH₄⁺', [('N', 'azote (symbole chimique N)'), ('H₄', 'quatre atomes d’hydrogène'), ('⁺', 'charge positive')], 'Ion ammonium',
  '<p>Forme ionisée de l’ammoniac, non absorbable par la muqueuse colique ; le lactulose favorise sa formation en acidifiant le côlon.</p>', 'i85-d-lactulose')
a('NG50', [('NG', 'NICE Guideline (recommandation du NICE)'), ('50', 'numéro 50')], 'Recommandation NICE 50 sur la cirrhose',
  '<p>Recommandation britannique sur l’évaluation et la prise en charge de la cirrhose chez les personnes de 16 ans et plus ; elle cite la dose initiale de carvédilol de 6,25 mg par jour.</p>', 'i85-d-carve')
a('García-Pagán', [('García-Pagán', 'nom propre : Juan Carlos García-Pagán, hépatologue à Barcelone')], 'Essai de García-Pagán (2010) sur le TIPS précoce',
  '<p>Essai randomisé de 63 patients cirrhotiques à haut risque : le TIPS posé dans les 72 heures a porté la survie à un an à 86 %, contre 61 % avec le traitement médical et endoscopique.</p>', 'i85-tips')
a('Favre-Bulle', [('Favre-Bulle', 'nom propre : Timothée Favre-Bulle, premier auteur')], 'Étude suisse des hospitalisations pour cirrhose (2024)',
  '<p>Étude transversale nationale des hospitalisations liées à la cirrhose en Suisse de 1998 à 2020, fondée sur la statistique médicale des hôpitaux.</p>')
a('Baveno VIII', [('Baveno', 'nom propre : ville italienne où se tiennent les conférences de consensus'), ('VIII', 'huitième (chiffres romains), édition de 2026')], 'Conférence de consensus Baveno VIII sur l’hypertension portale (2026)',
  '<p>Conférence tenue en mars 2026, publiée en version acceptée le 31.07.2026 dans le <i>Journal of Hepatology</i> et avalisée par l’EASL et l’ESGE ; 272 déclarations ont obtenu plus de 80 % d’accord. Le nombre romain désigne l’édition et non le facteur VIII de la coagulation.</p>', 'i85-baveno')
a('Baveno VII', [('Baveno', 'nom propre : ville italienne où se tiennent les conférences de consensus'), ('VII', 'septième (chiffres romains), édition de 2021 publiée en 2022')], 'Conférence de consensus Baveno VII sur l’hypertension portale (2022)',
  '<p>Consensus publié en 2022 dans le <i>Journal of Hepatology</i> (76:959–974) ; ses déclarations non révisées par Baveno VIII restent valables, notamment sur le HVPG.</p>', 'i85-baveno')
a('Baveno VI', [('Baveno', 'nom propre : ville italienne où se tiennent les conférences de consensus'), ('VI', 'sixième (chiffres romains), édition de 2015')], 'Conférence de consensus Baveno VI sur l’hypertension portale (2015)',
  '<p>Consensus de 2015 qui a introduit les critères non invasifs permettant d’éviter l’endoscopie de dépistage (élasticité &lt; 20 kPa et plaquettes ≥ 150 G/L).</p>', 'i85-baveno')
