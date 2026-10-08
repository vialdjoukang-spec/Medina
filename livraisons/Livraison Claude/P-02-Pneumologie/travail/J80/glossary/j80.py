from cardio_1 import a, G
# Glossaire du cours J80 — Syndrome de détresse respiratoire aiguë (P-02-Pneumologie).
# Clés nouvelles uniquement. SDRA, ECMO, ESICM, ATS, SCCM, PaO₂, FiO₂, SpO₂, PaCO₂, CO₂, H₂O,
# RECOVERY, COVID-19, SARS-CoV-2, CIM-10-GM, ADN et kPa existent déjà et ne sont pas redéfinies.

a('PEP', [('P', 'Pression'), ('E', 'Expiratoire'), ('P', 'Positive')], 'Pression expiratoire positive',
  '<p>Pression maintenue dans les voies aériennes en fin d’expiration par le ventilateur. Dans le syndrome de détresse respiratoire aiguë, elle garde ouvertes les alvéoles instables, réduit le shunt et limite les lésions d’ouverture-fermeture cycliques ; excessive, elle surdistend les zones saines et gêne le ventricule droit.</p>',
  'j80-contentieux-pep')

for code, title, d in [
    ('J80.0', 'Syndrome de détresse respiratoire aiguë de l’enfant, de l’adolescent et de l’adulte',
     '<p>Catégorie CIM-10-GM 2024 subdivisée par un cinquième caractère qui code la gravité : selon Berlin à partir de 18 ans, selon la PALICC entre 1 et moins de 18 ans.</p>'),
    ('J80.01', 'Syndrome de détresse respiratoire aiguë léger de l’adulte',
     '<p>PaO₂/FiO₂ &gt; 200 et ≤ 300 mmHg sous PEP ≥ 5 cm H₂O, personne de 18 ans ou plus.</p>'),
    ('J80.02', 'Syndrome de détresse respiratoire aiguë modéré de l’adulte',
     '<p>PaO₂/FiO₂ &gt; 100 et ≤ 200 mmHg sous PEP ≥ 5 cm H₂O, personne de 18 ans ou plus.</p>'),
    ('J80.03', 'Syndrome de détresse respiratoire aiguë sévère de l’adulte',
     '<p>PaO₂/FiO₂ ≤ 100 mmHg sous PEP ≥ 5 cm H₂O, personne de 18 ans ou plus.</p>'),
    ('J80.04', 'Syndrome de détresse respiratoire aiguë léger de l’enfant et de l’adolescent',
     '<p>Indice d’oxygénation de 4 à moins de 8, ou indice de saturation en oxygène de 5 à moins de 7,5 ; personne de 1 an à moins de 18 ans.</p>'),
    ('J80.05', 'Syndrome de détresse respiratoire aiguë modéré de l’enfant et de l’adolescent',
     '<p>Indice d’oxygénation de 8 à moins de 16, ou indice de saturation en oxygène de 7,5 à moins de 12,3.</p>'),
    ('J80.06', 'Syndrome de détresse respiratoire aiguë sévère de l’enfant et de l’adolescent',
     '<p>Indice d’oxygénation d’au moins 16, ou indice de saturation en oxygène d’au moins 12,3.</p>'),
    ('J80.09', 'Syndrome de détresse respiratoire aiguë, gravité non précisée',
     '<p>Cinquième caractère 9 : le degré de gravité n’est pas documenté dans le dossier.</p>'),
    ('P22.0', 'Syndrome de détresse respiratoire du nouveau-né',
     '<p>Code exclu de J80 : détresse respiratoire du prématuré liée à un déficit de surfactant, distincte du syndrome lésionnel de l’enfant plus âgé et de l’adulte.</p>'),
]:
    a(code, [(code, 'code CIM-10-GM 2024')], title, d)

a('PALICC', [('P', 'Pediatric'), ('A', 'Acute'), ('L', 'Lung'), ('I', 'Injury'), ('C', 'Consensus'), ('C', 'Conference')],
  'Conférence de consensus sur la lésion pulmonaire aiguë pédiatrique',
  '<p>Conférence internationale qui définit le syndrome de détresse respiratoire aiguë pédiatrique, gradué par l’indice d’oxygénation, qui intègre la pression moyenne des voies aériennes. Sa définition sert au codage de J80.04 à J80.06.</p>')
a('PALICC-2', [('PALICC', 'Pediatric Acute Lung Injury Consensus Conference'), ('2', 'deuxième édition')],
  'Deuxième conférence de consensus sur la lésion pulmonaire aiguë pédiatrique (2023)',
  '<p>Recommandations internationales de 2023 pour le diagnostic et la prise en charge du syndrome de détresse respiratoire aiguë de l’enfant : 146 recommandations et déclarations, publiées dans Pediatric Critical Care Medicine.</p>')
a('ARDSNet', [('ARDS', 'Acute Respiratory Distress Syndrome (syndrome de détresse respiratoire aiguë)'), ('Net', 'Network (réseau)')],
  'Réseau américain d’essais cliniques sur le syndrome de détresse respiratoire aiguë',
  '<p>Réseau financé par l’institut américain du cœur, du poumon et du sang. Son essai de 2000 a démontré la baisse de mortalité obtenue avec un volume courant de 6 mL/kg de poids prédit ; son protocole fournit la formule du poids prédit et les cibles d’oxygénation.</p>',
  'j80-ardsnet')
a('PROSEVA', [('PRO', 'PROne positioning (décubitus ventral)'), ('SEV', 'in SEVere (dans le SDRA sévère)'), ('A', 'ARDS (syndrome de détresse respiratoire aiguë)')],
  'Essai PROSEVA (2013)',
  '<p>Essai français de 466 patients : décubitus ventral précoce d’au moins 16 heures par séance dans le syndrome sévère ; mortalité à 28 jours 16,0 % contre 32,8 %.</p>',
  'j80-proseva')
a('EOLIA', [('EOLIA', 'ECMO to rescue Lung Injury in severe ARDS : acronyme non développable lettre à lettre')],
  'Essai EOLIA (2018)',
  '<p>Essai international de 249 patients : oxygénation extracorporelle veino-veineuse précoce dans le syndrome très sévère ; mortalité à 60 jours 35 % contre 46 %, différence non significative. Ses critères d’inclusion servent de critères d’indication.</p>',
  'j80-eolia')
a('ACURASYS', [('ACURASYS', 'ARDS et CURArisation SYStématique : acronyme non développable lettre à lettre')],
  'Essai ACURASYS (2010)',
  '<p>Essai français de 340 patients : cisatracurium pendant 48 heures dans le syndrome sévère précoce ; rapport de risque ajusté de décès à 90 jours 0,68.</p>',
  'j80-contentieux-curares')
a('ROSE', [('R', 'Reevaluation'), ('O', 'Of'), ('S', 'Systemic'), ('E', 'Early neuromuscular blockade')],
  'Essai ROSE (2019)',
  '<p>Essai américain de 1 006 patients : curarisation continue précoce contre sédation légère, avec PEP élevée dans les deux groupes ; mortalité à 90 jours identique (42,5 % contre 42,8 %).</p>',
  'j80-contentieux-curares')
a('FACTT', [('F', 'Fluid'), ('A', 'And'), ('C', 'Catheter'), ('T', 'Treatment'), ('T', 'Trial')],
  'Essai FACTT (2006)',
  '<p>Essai de 1 000 patients : stratégie hydrique conservatrice contre libérale après la phase de choc ; plus de jours sans ventilation, mortalité non significativement différente.</p>',
  'j80-factt')
a('DEXA-ARDS', [('DEXA', 'DEXAméthasone'), ('ARDS', 'Acute Respiratory Distress Syndrome (syndrome de détresse respiratoire aiguë)')],
  'Essai DEXA-ARDS (2020)',
  '<p>Essai espagnol de 277 patients au syndrome modéré à sévère : dexaméthasone 20 mg par jour pendant 5 jours puis 10 mg pendant 5 jours ; mortalité à 60 jours 21 % contre 36 %.</p>',
  'j80-dexamethasone')
a('LUNG SAFE', [('LUNG SAFE', 'Large observational study to UNderstand the Global impact of Severe Acute respiratory FailurE : acronyme non développable lettre à lettre')],
  'Étude LUNG SAFE (2014, publiée en 2016)',
  '<p>Cohorte prospective de 459 unités de soins intensifs dans 50 pays : le syndrome concernait 10,4 % des admissions et 23,4 % des patients ventilés, avec une mortalité hospitalière de 35 à 46 % selon la gravité.</p>',
  'j80-lung-safe')
