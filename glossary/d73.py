from cardio_1 import a, G
# D73 — Maladies de la rate (H-08-Hématologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
def add(key, lit, full, definition, ref):
    if key not in G:
        a(key, lit, full, '<p>' + definition + '</p>', ref)

add('OPSI', [('O','Overwhelming'),('P','Post-'),('S','Splenectomy'),('I','Infection')], 'Infection fulminante post-splénectomie (overwhelming post-splenectomy infection)',
    'Sepsis rapidement progressif du patient asplénique, avec défaillance multiviscérale en quelques heures et une létalité d’environ 50 % (OFSP 2015). Le pneumocoque cause jusqu’à 90 % des infections menaçant la vie.', 'd73-opsi')
add('HbS', [('Hb','Hémoglobine'),('S','S (drépanocytaire)')], 'Hémoglobine S',
    'Variante de l’hémoglobine responsable de la drépanocytose. Les formes mixtes HbS/C et HbS/β-thalassémie, comme la forme homozygote, entraînent une asplénie fonctionnelle ; le trait hétérozygote asymptomatique non.', 'd73-asplenie-fonctionnelle')
add('PPV23', [('P','Pneumococcal'),('P','Polysaccharide'),('V','Vaccine'),('23','à 23 valences')], 'Vaccin pneumococcique polysaccharidique 23-valent',
    'Vaccin non conjugué ; en 2015, la Commission fédérale pour les vaccinations ne le recommandait plus à l’asplénique, à cause de l’hyporéponse induite par les polysaccharides et de l’absence de mémoire immunologique.', 'd73-asplenie-fonctionnelle')
add('MenACWY', [('Men','Méningocoque'),('A','groupe A'),('C','groupe C'),('W','groupe W'),('Y','groupe Y')], 'Méningocoque des groupes A, C, W et Y',
    'Désigne le vaccin conjugué contre ces quatre groupes. Pour l’asplénie : 2 doses à 1 mois d’intervalle, rappel tous les 5 ans (CHUV 2026).', 'd73-menquadfi')
add('MenB', [('Men','Méningocoque'),('B','groupe B')], 'Méningocoque du groupe B',
    'Désigne le vaccin contre le groupe B. Pour l’asplénie : 2 doses à 2 mois d’intervalle, rappel tous les 5 ans (CHUV 2026).', 'd73-bexsero')
add('MenQuadfi', [('MenQuadfi','nom commercial d’un vaccin, non une abréviation')], 'MenQuadfi, vaccin méningococcique conjugué ACWY',
    'Nom de spécialité suisse du vaccin conjugué des groupes A, C, W et Y (Sanofi).', 'd73-menquadfi')
add('Al-Hyari', [('Al-Hyari','nom propre d’un auteur, non une abréviation')], 'Al-Hyari, premier auteur d’une étude d’échographie splénique',
    'Auteur d’une étude allemande sur l’échographie de la rate dans l’hyposplénisme, lue par son résumé seulement.', 'd73-nosologie')
add('BSH', [('B','British'),('S','Society for'),('H','Haematology')], 'British Society for Haematology',
    'Société britannique d’hématologie, auteur d’une recommandation 2024 sur l’asplénie (résumé seul lu). Elle diffère du protocole CHUV sur la splénectomie partielle et l’embolisation.', 'd73-nosologie')
add('PDF', [('P','Portable'),('D','Document'),('F','Format')], 'Portable Document Format',
    'Format de fichier de document utilisé pour les textes officiels cités dans les références.', 'd73-nosologie')
add('CT', [('C','Computed'),('T','Tomography')], 'Tomodensitométrie (computed tomography)',
    'Imagerie par scanner. Dans SPECT-CT, elle est associée à l’imagerie isotopique pour localiser la captation splénique.', 'd73-scinti')
add('anti-GPIIb-IIIa', [('anti-','dirigé contre'),('GP','GlycoProtéine'),('IIb-IIIa','complexe des sous-unités IIb et IIIa')], 'Anticorps dirigés contre la glycoprotéine IIb-IIIa des plaquettes',
    'Auto-anticorps antiplaquettes retrouvés chez 64 % des hépatopathes chroniques dans une étude citée ; ils contribuent à la thrombopénie de l’hypersplénisme.', 'd73-sequestration')
for code, label in [('D73.0','Hyposplénisme'),('D73.1','Hypersplénisme'),('D73.2','Splénomégalie congestive chronique'),('D73.3','Abcès de la rate'),('D73.4','Kyste de la rate'),('D73.5','Infarctus de la rate'),('D73.8','Autres maladies de la rate'),('D73.9','Maladie de la rate, sans précision')]:
    add(code, [(code,'code de la CIM-10-GM 2024, non une abréviation')], code + ' — ' + label, 'Sous-code du chapitre D73 de la CIM-10-GM 2024 : ' + label.lower() + '.', 'd73-nosologie')
add('Q89.00', [('Q89.00','code de la CIM-10-GM 2024, non une abréviation')], 'Q89.00 — Splénomégalie congénitale', 'Exclue de D73.1 par la classification.', 'd73-nosologie')
add('Q89.01', [('Q89.01','code de la CIM-10-GM 2024, non une abréviation')], 'Q89.01 — Asplénie congénitale', 'Exclue de D73.0 par la classification.', 'd73-nosologie')
add('R16.1', [('R16.1','code de la CIM-10-GM 2024, non une abréviation')], 'R16.1 — Splénomégalie, non classée ailleurs', 'Splénomégalie sans précision, exclue de D73.1.', 'd73-nosologie')
add('S36.04', [('S36.04','code de la CIM-10-GM 2024, non une abréviation')], 'S36.04 — Lésion traumatique de la rate (rupture traumatique)', 'Exclue de D73.5 par la classification.', 'd73-nosologie')
