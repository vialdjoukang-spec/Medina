from cardio_1 import a, G
# J12 — Pneumonies virales et pneumonies à micro-organismes particuliers (P-02-Pneumologie).
# Clés absentes de glossary/*.py et des dossiers de travail au 09.10.2026.
a('CMV', [('C', 'Cyto-'), ('M', 'Mégalo-'), ('V', 'Virus')], 'Cytomégalovirus',
  '<p>Virus à ADN de la famille des Herpesviridae. Chez l’immunodéprimé, en particulier après greffe, il cause des atteintes viscérales graves, dont la pneumonie, la colite et la rétinite (information professionnelle suisse du ganciclovir).</p>', 'j12-cmv')
a('VZV', [('V', 'Varicella (varicelle)'), ('Z', 'Zoster (zona)'), ('V', 'Virus')], 'Virus varicelle-zona',
  '<p>Virus de la varicelle et du zona, sensible à l’aciclovir. Sa pneumonie touche l’adulte, souvent immunodéprimé, et peut conduire à un syndrome de détresse respiratoire aiguë.</p>', 'j12-varicelle')
a('hMPV', [('h', 'human (humain)'), ('M', 'Méta-'), ('P', 'Pneumo-'), ('V', 'Virus')], 'Métapneumovirus humain',
  '<p>Virus respiratoire qui infecte à tout âge. Il cause des foyers d’infection en établissement de soins et des pneumonies graves chez le sujet âgé et le greffé.</p>', 'j12-hmpv')
a('ACE2', [('A', 'Angiotensin (de l’angiotensine)'), ('C', 'Converting (de conversion)'), ('E', 'Enzyme'), ('2', 'type 2')], 'Enzyme de conversion de l’angiotensine 2',
  '<p>Protéine de surface cellulaire qui sert de récepteur au SARS-CoV-2 et au virus du SARS de 2003 : la protéine de spicule s’y fixe avant la fusion (Hoffmann, 2020).</p>', 'j12-ace2')
a('TMPRSS2', [('TM', 'TransMembrane (transmembranaire)'), ('PRSS', 'PRotease, Serine (protéase à sérine)'), ('2', 'membre 2')], 'Protéase transmembranaire à sérine 2',
  '<p>Protéase de la surface des cellules respiratoires qui clive la protéine de spicule du SARS-CoV-2 et permet son entrée (Hoffmann, 2020). Nom de gène, développé groupe de lettres par groupe de lettres.</p>', 'j12-ace2')
a('ECIL', [('E', 'European (européenne)'), ('C', 'Conference (conférence)'), ('I', 'on Infections (sur les infections)'), ('L', 'in Leukaemia (dans les leucémies)')], 'Conférence européenne sur les infections dans les leucémies',
  '<p>Groupe d’experts européens qui publie des recommandations sur les infections des patients d’hématologie et des greffés de cellules souches (ECIL-5, publiée en 2016 ; ECIL-7, 2017 ; ECIL-10, 2024).</p>', 'j12-ecil-def')
a('ECMM', [('E', 'European (européenne)'), ('C', 'Confederation (confédération)'), ('M', 'of Medical (de médecine)'), ('M', 'Mycology (mycologique)')], 'Confédération européenne de mycologie médicale',
  '<p>Société savante européenne coautrice, avec l’ESCMID et l’ERS, de la recommandation de 2017 sur l’aspergillose, et du consensus de 2020 sur l’aspergillose associée à la COVID-19.</p>', 'j12-aspergillose')
a('ISHAM', [('I', 'International (internationale)'), ('S', 'Society for (société de)'), ('H', 'Human (humaine)'), ('A', 'and Animal (et animale)'), ('M', 'Mycology (mycologie)')], 'Société internationale de mycologie humaine et animale',
  '<p>Société savante coautrice, avec l’ECMM, du consensus de 2020 sur la définition et la prise en charge de l’aspergillose pulmonaire associée à la COVID-19.</p>', 'j12-aspergillose')
a('CFV', [('C', 'Commission'), ('F', 'Fédérale'), ('V', 'pour les Vaccinations')], 'Commission fédérale pour les vaccinations',
  '<p>Commission qui publie avec l’OFSP le Plan de vaccination suisse et les recommandations vaccinales, dont celles contre le VRS (mise à jour du 28.09.2026).</p>', 'j12-vaccin-vrs')
a('UL97', [('UL97', 'désignation du gène viral, sans développement dans les sources consultées')], 'Gène UL97 du cytomégalovirus',
  '<p>Gène du CMV qui code la kinase virale phosphorylant le ganciclovir dans la cellule infectée (information professionnelle suisse Cymevene). Ses mutations peuvent conférer une résistance ; l’ECIL-10 recommande un génotypage en cas d’infection réfractaire.</p>', 'j12-d-ganciclovir')
a('UL54', [('UL54', 'désignation du gène viral, sans développement dans les sources consultées')], 'Gène UL54 du cytomégalovirus',
  '<p>Gène du CMV dont les mutations figurent, avec celles d’UL97, dans l’algorithme de l’ECIL-10 pour l’infection à CMV réfractaire ou résistante.</p>', 'j12-cmv')
a('mRESVIA', [('m', 'messager (vaccin à ARN messager)'), ('RESVIA', 'nom commercial, non abréviatif')], 'Vaccin à ARN messager contre le VRS (Moderna)',
  '<p>Vaccin qui code la glycoprotéine F du VRS-A en conformation de préfusion ; autorisé en Suisse dès 18 ans, en une dose unique de 0,5 mL (information professionnelle, août 2026).</p>', 'j12-vaccin-vrs')
