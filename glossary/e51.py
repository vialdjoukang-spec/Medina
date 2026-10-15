"""Abréviations E51 — Carence en thiamine ; entrées conditionnelles, aucun terme existant n’est écrasé."""
from cardio_1 import a, G
if 'ThDP' not in G:
    a('ThDP', [('Th', 'Thiamine'), ('D', 'Di'), ('P', 'Phosphate (pyrophosphate)')], 'Pyrophosphate de thiamine', '<p>Forme active de la vitamine B1 et cofacteur de la pyruvate déshydrogénase, de l’α-cétoglutarate déshydrogénase et de la transcétolase. Environ 80 % de la thiamine corporelle est sous cette forme. On la dose dans le sang total ou les érythrocytes.</p>', 'e51-thdp')
if 'ThMP' not in G:
    a('ThMP', [('Th', 'Thiamine'), ('M', 'Mono'), ('P', 'Phosphate')], 'Monophosphate de thiamine', '<p>Forme phosphorylée intermédiaire de la thiamine, à côté du ThDP et du ThTP.</p>', 'e51-thdp')
if 'ThTP' not in G:
    a('ThTP', [('Th', 'Thiamine'), ('T', 'Tri'), ('P', 'Phosphate')], 'Triphosphate de thiamine', '<p>Forme triphosphorylée de la thiamine, présente en faible quantité dans la cellule.</p>', 'e51-thdp')
if 'ETKAC' not in G:
    a('ETKAC', [('E', 'Erythrocyte (érythrocytaire)'), ('T', 'Trans'), ('K', 'Ketolase (cétolase)'), ('AC', 'ACtivation Coefficient (coefficient d’activation)')], 'Coefficient d’activation de la transcétolase érythrocytaire', '<p>Rapport de l’activité de la transcétolase des globules rouges avant et après ajout de ThDP. Il est supérieur à 1,25 en cas de risque élevé de carence.</p>', 'e51-etkac')
if 'EFNS' not in G:
    a('EFNS', [('E', 'European (européenne)'), ('F', 'Federation of'), ('N', 'Neurological (neurologiques)'), ('S', 'Societies (sociétés)')], 'Fédération européenne des sociétés de neurologie', '<p>Elle a publié en 2010 des lignes directrices sur le diagnostic, le traitement et la prévention de l’encéphalopathie de Wernicke.</p>', 'e51-efns')
if 'ESPEN' not in G:
    a('ESPEN', [('E', 'European (européenne)'), ('S', 'Society for'), ('P', 'Parenteral (parentérale)'), ('E', 'and Enteral (et entérale)'), ('N', 'Nutrition')], 'Société européenne de nutrition clinique et métabolisme', '<p>Elle a publié en 2022 les lignes directrices sur les micronutriments, source des doses de thiamine de cette leçon, et en 2019 celles sur la nutrition dans les maladies du foie.</p>', 'e51-sources')
if 'DGE' not in G:
    a('DGE', [('D', 'Deutsche (allemande)'), ('G', 'Gesellschaft für'), ('E', 'Ernährung (nutrition)')], 'Société allemande de nutrition', '<p>Elle publie les valeurs de référence D-A-CH pour les apports en nutriments. La page sur la thiamine date de la dérivation 2015.</p>', 'e51-sources')
if 'SMOB' not in G:
    a('SMOB', [('SMOB', 'sigle de la société suisse de chirurgie de l’obésité ; son développement n’est pas repris dans les sources lues')], 'Société suisse de chirurgie de l’obésité (SMOB)', '<p>Ses directives pour le traitement chirurgical de l’obésité, en vigueur dès le 1er juillet 2023, prévoient une supplémentation à long terme en multivitamines après chirurgie bariatrique et un bilan annuel du statut vitaminique.</p>', 'e51-bariatrique')
if 'HPLC' not in G:
    a('HPLC', [('H', 'High (haute)'), ('P', 'Performance'), ('L', 'Liquid (liquide)'), ('C', 'Chromatography (chromatographie)')], 'Chromatographie liquide à haute performance', '<p>Méthode de séparation et de dosage utilisée pour le ThDP du sang total, avec ou sans spectrométrie de masse.</p>', 'e51-thdp-dosage')
if 'THTR1' not in G:
    a('THTR1', [('THTR', 'THiamine TRansporter (transporteur de la thiamine)'), ('1', 'de type 1, basolatéral')], 'Transporteur de la thiamine de type 1', '<p>Transporteur du pôle basolatéral de l’entérocyte, qui fait passer la thiamine de la cellule vers le sang.</p>', 'e51-thdp')
if 'THTR2' not in G:
    a('THTR2', [('THTR', 'THiamine TRansporter (transporteur de la thiamine)'), ('2', 'de type 2, apical')], 'Transporteur de la thiamine de type 2', '<p>Transporteur du pôle apical de l’entérocyte, qui fait entrer la thiamine alimentaire dans la cellule.</p>', 'e51-thdp')
if 'FAERS' not in G:
    a('FAERS', [('F', 'FDA'), ('A', 'Adverse'), ('E', 'Event'), ('R', 'Reporting'), ('S', 'System')], 'Système de déclaration des événements indésirables de la FDA', '<p>Base de pharmacovigilance américaine utilisée par l’étude de 2026 sur les agonistes du GLP-1. Elle permet de détecter un signal, non de prouver une causalité.</p>', 'e51-epidemio')
if 'FDA' not in G:
    a('FDA', [('F', 'Food and'), ('D', 'Drug'), ('A', 'Administration')], 'Administration américaine des denrées alimentaires et des médicaments', '<p>Agence américaine ; son système de pharmacovigilance a servi de base à l’étude de 2026 sur les agonistes du GLP-1.</p>', 'e51-epidemio')
if 'IC' not in G:
    a('IC', [('I', 'Intervalle de'), ('C', 'Confiance')], 'Intervalle de confiance', '<p>Plage de valeurs compatible avec l’estimation d’un effet dans l’échantillon étudié. Ici, un intervalle de confiance à 95 % de 1,38 à 4,01 accompagne un rapport de 2,35.</p>', 'e51-epidemio')
if 'CRRT' not in G:
    a('CRRT', [('C', 'Continuous (continue)'), ('R', 'Renal'), ('R', 'Replacement (de suppléance)'), ('T', 'Therapy (thérapie)')], 'Épuration extra-rénale continue', '<p>Technique de suppléance rénale continue en soins intensifs, qui élimine environ 4 à 5 mg de thiamine par jour.</p>', 'e51-soins-intensifs')
if 'TDD' not in G:
    a('TDD', [('T', 'Thiamine'), ('D', 'Deficiency'), ('D', 'Disorders (troubles)')], 'Troubles liés à la carence en thiamine', '<p>Terme anglais qui regroupe l’ensemble des présentations chevauchantes de la carence en thiamine au cours de la vie.</p>', 'e51-codage')
if 'HUG' not in G:
    a('HUG', [('H', 'Hôpitaux'), ('U', 'Universitaires de'), ('G', 'Genève')], 'Hôpitaux universitaires de Genève', '<p>Auteurs de l’article de la Revue Médicale Suisse de 2022 sur la thiamine.</p>', 'e51-fi-benerva')
if 'RMS' not in G:
    a('RMS', [('R', 'Revue'), ('M', 'Médicale'), ('S', 'Suisse')], 'Revue Médicale Suisse', '<p>Revue qui a publié en 2022 l’article « Thiamine : une simple vitamine ? ».</p>', 'e51-sources')
if 'ROR' not in G:
    a('ROR', [('R', 'Reporting'), ('O', 'Odds'), ('R', 'Ratio (rapport de cotes de déclaration)')], 'Rapport de disproportionnalité des déclarations', '<p>Mesure de pharmacovigilance : un ROR de 2,35 signifie que l’événement est déclaré plus souvent avec le médicament qu’avec les autres, sans prouver une causalité.</p>', 'e51-epidemio')
if 'AIPS' not in G:
    a('AIPS', [('A', 'Arzneimittel (médicaments)'), ('I', 'Informations'), ('P', 'Publikations (de publication)'), ('S', 'System (système)')], 'Système de publication des informations sur les médicaments', '<p>Il rassemble les informations professionnelles des médicaments autorisés en Suisse, dont Benerva®.</p>', 'e51-fi-benerva')
if 'Gayet-Wernicke' not in G:
    a('Gayet-Wernicke', [('Gayet-Wernicke', 'noms des deux auteurs éponymes de l’encéphalopathie, non une abréviation')], 'Encéphalopathie de Gayet-Wernicke', '<p>Manifestation cérébrale aiguë de la carence en thiamine, associant troubles de la conscience ou de la mémoire, troubles oculomoteurs et ataxie.</p>', 'e51-wernicke')
if 'Wernicke-Korsakoff' not in G:
    a('Wernicke-Korsakoff', [('Wernicke-Korsakoff', 'noms des auteurs éponymes, non une abréviation')], 'Syndrome de Wernicke-Korsakoff', '<p>Association de l’encéphalopathie aiguë de Wernicke et du syndrome amnésique chronique de Korsakoff qui peut lui succéder.</p>', 'e51-korsakoff')
if 'Refeeding-Syndrom' not in G:
    a('Refeeding-Syndrom', [('Refeeding-Syndrom', 'titre allemand d’un article, non une abréviation')], 'Syndrome de renutrition (titre allemand : Refeeding-Syndrom)', '<p>Titre d’un article suisse de 2022 sur le syndrome de renutrition.</p>', 'e51-renutrition')
if 'Schack-Waxler' not in G:
    a('Schack-Waxler', [('Schack-Waxler', 'noms des auteurs d’une méthode de dosage, non une abréviation')], 'Méthode de Schack et Waxler', '<p>Méthode de dosage de la théophylline que la thiamine peut fausser, selon l’information professionnelle suisse.</p>', 'e51-fi-benerva')
if '2-hydroxyacyl-CoA' not in G:
    a('2-hydroxyacyl-CoA', [('2-hydroxyacyl', 'groupe acyle porteur d’un hydroxyle en position 2'), ('CoA', 'Coenzyme A')], '2-hydroxyacyl-coenzyme A', '<p>Substrat de la 2-hydroxyacyl-CoA lyase, enzyme à ThDP.</p>', 'e51-thdp')
if 'D-A-CH' not in G:
    a('D-A-CH', [('D', 'Deutschland (Allemagne)'), ('A', 'Austria (Autriche)'), ('CH', 'Confoederatio Helvetica (Suisse)')], 'Allemagne, Autriche, Suisse', '<p>Référentiel commun de valeurs nutritionnelles de référence. Pour la thiamine, la page lue est celle de la DGE ; son adoption par la Société suisse de nutrition n’a pas été vérifiée.</p>', 'e51-sources')
if 'E51.0' not in G:
    a('E51.0', [('E51.0', 'code CIM-10-GM, non une abréviation')], 'Code E51.0 (absent du relevé local)', '<p>Le relevé local de la CIM-10-GM 2024 ne contient pas de sous-code E51.0.</p>', 'e51-codage')
if 'E51.1' not in G:
    a('E51.1', [('E51.1', 'code CIM-10-GM, non une abréviation')], 'Béribéri', '<p>Sous-code CIM-10-GM 2024 de la carence en thiamine pour le béribéri.</p>', 'e51-codage')
if 'E51.2' not in G:
    a('E51.2', [('E51.2', 'code CIM-10-GM, non une abréviation')], 'Encéphalopathie de Wernicke', '<p>Sous-code CIM-10-GM 2024 de la carence en thiamine pour l’encéphalopathie de Wernicke.</p>', 'e51-codage')
if 'E51.8' not in G:
    a('E51.8', [('E51.8', 'code CIM-10-GM, non une abréviation')], 'Autres manifestations de la carence en thiamine', '<p>Sous-code CIM-10-GM 2024.</p>', 'e51-codage')
if 'E51.9' not in G:
    a('E51.9', [('E51.9', 'code CIM-10-GM, non une abréviation')], 'Carence en thiamine, sans précision', '<p>Sous-code CIM-10-GM 2024.</p>', 'e51-codage')
