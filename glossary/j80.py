from cardio_1 import a, G
# Glossaire du cours J80 — Syndrome de détresse respiratoire aiguë de l’adulte (P-02-Pneumologie).
# Clés nouvelles uniquement. SDRA, ECMO, EOLIA, ESICM, ATS, SCCM, ERS, ESCMID, ALAT, PaO₂, FiO₂, SpO₂,
# PaCO₂, CO₂, H₂O, pH, VNI, CPAP, BNP, RECOVERY, COVID-19, ADN, kPa, AIPS et AmiKo existent déjà.
# « PEP » est réservée à la prophylaxie postexposition (glossary/b24.py) : ce cours emploie donc « PEEP ».
# Revue IA du 09.10.2026 ; ne vaut pas validation médicale.

def _a(k, *args):
    if k not in G:
        a(k, *args)

_a('PEEP', [('P', 'Positive'), ('E', 'End-'), ('E', 'Expiratory'), ('P', 'Pressure')],
   'Pression expiratoire positive (positive end-expiratory pressure)',
   '<p>Pression maintenue dans les voies aériennes en fin d’expiration par le ventilateur. Dans le syndrome de détresse respiratoire aiguë, elle garde ouvertes les alvéoles recrutables et réduit le shunt ; excessive, elle surdistend les zones saines et gêne la circulation.</p>',
   'j80-contentieux-pep')
_a('PALICC', [('P', 'Pediatric'), ('A', 'Acute'), ('L', 'Lung'), ('I', 'Injury'), ('C', 'Consensus'), ('C', 'Conference')],
   'Conférence de consensus sur la lésion pulmonaire aiguë pédiatrique',
   '<p>Conférence internationale qui définit le syndrome de détresse respiratoire aiguë de l’enfant à partir de l’indice d’oxygénation, lequel intègre la pression moyenne des voies aériennes.</p>')
_a('PALICC-2', [('PALICC', 'Pediatric Acute Lung Injury Consensus Conference'), ('2', 'deuxième édition')],
   'Deuxième conférence de consensus sur la lésion pulmonaire aiguë pédiatrique (2023)',
   '<p>Recommandations internationales de 2023 pour le diagnostic et la prise en charge du syndrome de détresse respiratoire aiguë de moins de 18 ans, hors maladie pulmonaire périnatale.</p>')
_a('ARDSNet', [('ARDS', 'Acute Respiratory Distress Syndrome (syndrome de détresse respiratoire aiguë)'), ('Net', 'Network (réseau)')],
   'Réseau américain d’essais cliniques sur le syndrome de détresse respiratoire aiguë',
   '<p>Réseau d’essais financé par l’institut national américain du cœur, du poumon et du sang. Son essai de 2000 a démontré la baisse de mortalité obtenue avec un volume courant de 6 mL/kg de poids prédit ; son protocole fournit la formule du poids prédit et les cibles de pH et d’oxygénation.</p>',
   'j80-ardsnet')
_a('PROSEVA', [('PROSEVA', 'nom propre d’essai sur le décubitus ventral dans le syndrome sévère ; acronyme non développé lettre à lettre dans ce cours')],
   'Essai PROSEVA (2013)',
   '<p>Essai français de 466 patients : décubitus ventral précoce d’au moins 16 heures par séance dans le syndrome sévère ; mortalité à 28 jours 16,0 % contre 32,8 %.</p>',
   'j80-proseva')
_a('ACURASYS', [('ACURASYS', 'nom propre d’essai sur la curarisation dans le syndrome sévère ; acronyme non développé lettre à lettre dans ce cours')],
   'Essai ACURASYS (2010)',
   '<p>Essai français de 340 patients : cisatracurium pendant 48 heures dans le syndrome sévère précoce ; rapport de risque ajusté de décès à 90 jours 0,68.</p>',
   'j80-contentieux-curares')
_a('ROSE', [('ROSE', 'nom propre d’essai sur la curarisation précoce ; acronyme non développé lettre à lettre dans ce cours')],
   'Essai ROSE (2019)',
   '<p>Essai de 1 006 patients : curarisation continue précoce contre sédation légère, avec PEEP élevée dans les deux groupes ; mortalité à 90 jours 42,5 % contre 42,8 %.</p>',
   'j80-contentieux-curares')
_a('FACTT', [('FACTT', 'nom propre d’essai sur la gestion hydrique ; acronyme non développé lettre à lettre dans ce cours')],
   'Essai FACTT (2006)',
   '<p>Essai de 1 000 patients : stratégie hydrique conservatrice contre libérale après la résolution du choc ; plus de jours sans ventilation, mortalité non significativement différente.</p>',
   'j80-factt')
_a('DEXA-ARDS', [('DEXA', 'DEXAméthasone'), ('ARDS', 'Acute Respiratory Distress Syndrome (syndrome de détresse respiratoire aiguë)')],
   'Essai DEXA-ARDS (2020)',
   '<p>Essai espagnol ouvert de 277 patients au syndrome modéré à sévère : dexaméthasone 20 mg par jour pendant 5 jours puis 10 mg pendant 5 jours ; mortalité à 60 jours 21 % contre 36 %.</p>',
   'j80-dexamethasone')
_a('LUNG SAFE', [('LUNG SAFE', 'Large observational study to UNderstand the Global impact of Severe Acute respiratory FailurE : acronyme formé sur le titre anglais, non développable lettre à lettre')],
   'Étude LUNG SAFE (hiver 2014, publiée en 2016)',
   '<p>Cohorte prospective de 459 unités de soins intensifs dans 50 pays, menée avec le groupe d’essais de l’ESICM : le syndrome concernait 10,4 % des admissions et 23,4 % des patients ventilés, avec une mortalité hospitalière de 35 à 46 % selon la gravité.</p>',
   'j80-lung-safe')
_a('LOCO2', [('LOCO2', 'nom propre d’essai sur la cible d’oxygénation ; acronyme non développé lettre à lettre dans ce cours')],
   'Essai LOCO2 (2020)',
   '<p>Essai français de 205 patients : cible d’oxygénation basse contre libérale ; arrêt prématuré pour raisons de sécurité, mortalité à 90 jours 44,4 % contre 30,4 % dans le groupe à cible basse.</p>',
   'j80-cible-oxygene')
_a('BALTI-2', [('BALTI-2', 'nom propre d’essai britannique sur le salbutamol intraveineux ; acronyme non développé lettre à lettre dans ce cours')],
   'Essai BALTI-2 (2012)',
   '<p>Essai britannique de 326 patients : le salbutamol intraveineux a augmenté la mortalité à 28 jours (34 % contre 23 %).</p>',
   'j80-sans-benefice')
_a('TRALI', [('T', 'Transfusion-'), ('R', 'Related'), ('A', 'Acute'), ('L', 'Lung'), ('I', 'Injury')],
   'Lésion pulmonaire aiguë post-transfusionnelle',
   '<p>Œdème pulmonaire lésionnel survenant pendant une transfusion ou dans les six heures qui suivent ; à déclarer au système suisse d’hémovigilance.</p>',
   'j80-trali')
_a('TACO', [('T', 'Transfusion-'), ('A', 'Associated'), ('C', 'Circulatory'), ('O', 'Overload')],
   'Surcharge circulatoire associée à la transfusion',
   '<p>Œdème pulmonaire hydrostatique dû au volume transfusé ; en Suisse, il est déclaré bien plus souvent que la lésion pulmonaire aiguë post-transfusionnelle.</p>',
   'j80-trali')
_a('SSMI', [('S', 'Société'), ('S', 'Suisse'), ('M', 'de Médecine'), ('I', 'Intensive')],
   'Société suisse de médecine intensive',
   '<p>Société savante suisse des soins intensifs ; elle publie notamment des recommandations « Choosing wisely » pour les soins intensifs.</p>')
