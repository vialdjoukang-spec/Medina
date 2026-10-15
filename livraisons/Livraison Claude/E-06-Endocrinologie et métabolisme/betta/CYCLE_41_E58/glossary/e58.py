from cardio_1 import a, G
# E58 — Carence alimentaire en calcium (E-06-Endocrinologie et métabolisme). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'OSAV' not in G:
    a('OSAV', [('O', 'Office fédéral'), ('S', 'de la Sécurité'), ('A', 'Alimentaire (et des Affaires)'), ('V', 'Vétérinaires')], 'Office fédéral de la sécurité alimentaire et des affaires vétérinaires', '<p>L’OSAV publie les valeurs de référence nutritionnelles pour la Suisse (version de juin 2022) et cosigne les recommandations nutritionnelles suisses de 2024 avec la Société suisse de nutrition.</p>')
if 'SSN' not in G:
    a('SSN', [('S', 'Société'), ('S', 'Suisse de'), ('N', 'Nutrition')], 'Société suisse de nutrition', '<p>La Société suisse de nutrition publie, avec l’OSAV, les recommandations nutritionnelles et la pyramide alimentaire suisses (version 2024).</p>')
if 'PTH' not in G:
    a('PTH', [('P', 'Para'), ('T', 'Thyroid (thyroïdienne)'), ('H', 'Hormone')], 'Parathormone', '<p>La PTH, sécrétée par les glandes parathyroïdes, règle la réabsorption rénale du calcium, stimule la résorption osseuse et la 1α-hydroxylase rénale qui fabrique le calcitriol. Elle s’élève lorsque l’apport calcique est insuffisant (hyperparathyroïdie secondaire). Abréviation de l’anglais parathyroid hormone.</p>', 'e58-pth')
if 'EFSA' not in G:
    a('EFSA', [('E', 'European'), ('F', 'Food'), ('S', 'Safety'), ('A', 'Authority')], 'Autorité européenne de sécurité des aliments', '<p>Agence européenne qui publie des avis scientifiques sur les valeurs de référence nutritionnelles. Son avis de 2015 sur le phosphore est cité dans ce chapitre ; son avis sur le calcium n’a pas pu être lu.</p>')
if 'ESPE' not in G:
    a('ESPE', [('E', 'European'), ('S', 'Society for'), ('P', 'Paediatric'), ('E', 'Endocrinology')], 'Société européenne d’endocrinologie pédiatrique', '<p>Elle a initié le consensus mondial de 2016 sur la prévention et la prise en charge du rachitisme nutritionnel.</p>')
if 'EAPC' not in G:
    a('EAPC', [('E', 'European'), ('A', 'Association of'), ('P', 'Preventive'), ('C', 'Cardiology')], 'Association européenne de cardiologie préventive', '<p>Association de la Société européenne de cardiologie. Sa prise de position de 2025 sur l’alimentation et la prévention cardiovasculaire est citée à propos de la supplémentation calcique.</p>')
if 'EMS' not in G:
    a('EMS', [('E', 'Établissement'), ('M', 'Médico-'), ('S', 'Social')], 'Établissement médico-social', '<p>Structure d’hébergement de personnes âgées. Les essais calcium et vitamine D y montrent l’effet maximal sur les fractures.</p>')
if 'EPIC' not in G:
    a('EPIC', [('E', 'European'), ('P', 'Prospective'), ('I', 'Investigation into'), ('C', 'Cancer and nutrition')], 'Investigation prospective européenne sur le cancer et la nutrition', '<p>Cohorte européenne ; sa branche d’Oxford (EPIC-Oxford) inclut des végétariens et des véganes et rapporte un risque de fracture accru chez les véganes.</p>')
if 'D-A-CH' not in G:
    a('D-A-CH', [('D', 'Deutschland (Allemagne)'), ('A', 'Austria, Österreich (Autriche)'), ('CH', 'Confoederatio Helvetica (Suisse)')], 'Valeurs de référence germanophones (Allemagne, Autriche, Suisse)', '<p>Valeurs de référence nutritionnelles communes aux pays germanophones. Certaines valeurs suisses de 2022 en sont reprises, selon l’OSAV.</p>')
if 'D3' not in G:
    a('D3', [('D', 'vitamine D'), ('3', 'forme numéro 3, le cholécalciférol')], 'Vitamine D3 (cholécalciférol)', '<p>Forme de vitamine D d’origine cutanée et alimentaire, hydroxylée dans le foie puis dans le rein.</p>')
if 'Calcimagon-D3' not in G:
    a('Calcimagon-D3', [('Calcimagon-D3', 'nom commercial suisse d’une association de calcium et de vitamine D3, non développable lettre à lettre')], 'Calcimagon-D3®', '<p>Préparation suisse (Swissmedic n° 53929) : 500 mg de calcium élément et 400 UI de vitamine D3 par comprimé, avec les formes Forte (1000 mg et 800 UI) et 500/800. Voir la monographie dans l’onglet Pharmacologie.</p>', 'e58-d-calcimagon')
if 'menuCH' not in G:
    a('menuCH', [('menu', 'enquête alimentaire (menu)'), ('CH', 'Confoederatio Helvetica (Suisse)')], 'Enquête nationale suisse sur l’alimentation', '<p>Enquête nationale menuCH (2014-2015, 2086 adultes de 18 à 75 ans) ; les aliments fermentés y fournissent plus de 30 % du calcium quotidien.</p>', 'e58-menuch')
