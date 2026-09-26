# Glossaire MEDINA — arbitrage de la fusion des branches Claude et Alpha (26.09.2026)
#
# Rôle : ce fichier est chargé en DERNIER (ordre alphabétique des fichiers de glossary/, après cardio_1).
# Le dictionnaire G étant partagé, chaque a() ci-dessous fixe la valeur FINALE d’une clé définie dans
# plusieurs fichiers, ou dont la valeur finale différait entre les branches Claude et Alpha.
# Règles appliquées (voir audits/FUSION_GLOSSAIRE.md) :
#   - développement lettre à lettre le plus littéral et exact ; libellé complet exact ;
#   - définition générale, valable dans tous les chapitres qui emploient la clé, fusionnant les
#     informations exactes des définitions candidates (aucun chiffre nouveau non vérifié) ;
#   - fenêtre « ref » conservée seulement si elle existe (data-pop vérifié) et si elle est pertinente
#     pour l’ensemble des emplois de la clé ; sinon None.
# Les collisions de SENS (même sigle, deux sens) ne sont pas arbitrées ici : elles sont résolues à la source
# (PRES/PReS, REDUCE/Gore REDUCE, ABCDE, HOPE ; voir le rapport).
# Ne pas ajouter de clé nouvelle dans ce fichier : il ne sert qu’à l’arbitrage.
from cardio_1 import a, G

# ---------------------------------------------------------------- démarche clinique
# ABCDE : t78 (approche du patient grave, 6 emplois I44, I46, T78) contre i10 (aide-mémoire des causes
# d’hypertension secondaire). Collision de sens résolue à la source ; ici, définition enrichie de l’approche.
a('ABCDE',[('A','Airway (voies aériennes)'),('B','Breathing (respiration)'),('C','Circulation'),('D','Disability (état neurologique)'),('E','Exposure (exposition : examen de toute la peau, température)')],'Approche ABCDE du patient grave',
 '<p>Évaluation et traitement structurés du patient grave, dans l’ordre des menaces vitales : voies aériennes, respiration, circulation, état neurologique, exposition. Chaque anomalie est traitée avant de passer à la lettre suivante, avec réévaluation régulière.</p>')

# ---------------------------------------------------------------- électrocardiogramme
# aVL, DI, V3, V5, V6 : i10 (critères d’hypertrophie) et i21 (territoires) ; même sens. Fusion des deux
# définitions ; position anatomique selon la convention « au niveau horizontal de V4 » (i21). Fenêtre
# i21-ecg-terr (territoires électriques) conservée pour V3, V5, V6.
a('aVL',[('a','augmented (augmentée)'),('V','Voltage (dérivation unipolaire)'),('L','Left (bras gauche)')],'Dérivation unipolaire augmentée du bras gauche',
 '<p>Dérivation frontale qui explore, avec DI, la paroi latérale haute. Une onde R ≥ 11 mm y est un critère d’hypertrophie ventriculaire gauche ; un sous-décalage du segment ST y est un miroir précoce de l’infarctus inférieur.</p>')
a('DI',[('D','Dérivation'),('I','I : première dérivation bipolaire des membres (bras gauche par rapport au bras droit)')],'Dérivation I (DI) de l’électrocardiogramme',
 '<p>Dérivation frontale bipolaire qui enregistre la différence de potentiel entre le bras gauche et le bras droit ; avec aVL, elle explore la paroi latérale haute.</p>')
a('V3',[('V','Voltage (dérivation précordiale unipolaire)'),('3','précordiale n° 3 : à mi-distance entre V2 et V4')],'Dérivation précordiale V3',
 '<p>Électrode placée à mi-distance entre V2 (4e espace intercostal, bord gauche du sternum) et V4 (5e espace intercostal, ligne médioclaviculaire). Zone habituelle de transition du QRS ; utilisée dans l’indice de Cornell (onde S en V3).</p>','i21-ecg-terr')
a('V5',[('V','Voltage (dérivation précordiale unipolaire)'),('5','précordiale n° 5 : ligne axillaire antérieure, au niveau horizontal de V4')],'Dérivation précordiale V5',
 '<p>Électrode placée sur la ligne axillaire antérieure, au niveau horizontal de V4 ; explore la paroi latérale basse. Utilisée dans l’indice de Sokolow-Lyon.</p>','i21-ecg-terr')
a('V6',[('V','Voltage (dérivation précordiale unipolaire)'),('6','précordiale n° 6 : ligne axillaire moyenne, au niveau horizontal de V4')],'Dérivation précordiale V6',
 '<p>Électrode placée sur la ligne axillaire moyenne, au niveau horizontal de V4 ; explore la paroi latérale basse. Utilisée dans l’indice de Sokolow-Lyon.</p>','i21-ecg-terr')

# ---------------------------------------------------------------- imagerie et mesures
# ITV : i34 (fenêtre PISA) contre i35 (fenêtre équation de continuité). Même sens ; fenêtre i35-continuite
# retenue (15 emplois sur 18 dans I35 ; explication générale de l’ITV).
a('ITV',[('I','Intégrale'),('T','Temps-'),('V','Vitesse')],'Intégrale temps-vitesse',
 '<p>Surface sous la courbe de vitesse Doppler d’un flux pendant un cycle, exprimée en centimètres : distance parcourue par le sang pendant l’éjection. Multipliée par une surface de section, elle donne un volume par battement : volume d’éjection (équation de continuité) ou volume régurgité (surface de l’orifice régurgitant × ITV du jet).</p>','i35-continuite')
# TEP : i25 (perfusion, fenêtre i25-stressimg) et i33 (FDG, fenêtre i33-tep). Fusion ; la fenêtre FDG est portée
# par la clé FDG, la clé TEP garde la fenêtre comparative de l’imagerie de stress (valeur finale d’origine).
a('TEP',[('T','Tomographie'),('E','par Émission de'),('P','Positons')],'Tomographie par émission de positons',
 '<p>Imagerie nucléaire fonctionnelle qui détecte la distribution d’un traceur émetteur de positons, le plus souvent couplée à la tomodensitométrie. Avec un traceur de perfusion, elle mesure le débit myocardique absolu (mL/min/g) et la réserve de débit : utile dans l’ischémie équilibrée et la dysfonction microvasculaire. Avec le FDG, elle détecte l’inflammation et l’infection (endocardite sur prothèse, sarcoïdose, myocardite, vascularite des gros vaisseaux) et les tumeurs.</p>','i25-stressimg')
# FDG : i33 (riche, fenêtre i33-tep) contre m31 (courte). Fusion ; fenêtre i33-tep conservée (principe et préparation).
a('FDG',[('F','Fluoro- (fluor 18, émetteur de positons)'),('D','Désoxy-'),('G','Glucose')],'Fluorodésoxyglucose marqué au fluor 18',
 '<p>Analogue du glucose marqué au fluor 18, traceur le plus employé en tomographie par émission de positons : il s’accumule dans les cellules à métabolisme glucidique élevé (inflammation, infection, tumeurs). Pour rechercher une inflammation cardiaque, une préparation pauvre en glucides et riche en graisses supprime la captation myocardique physiologique.</p>','i33-tep')
# Cockcroft-Gault : i48 (fenêtre i48-cg, définition vide) et i80 (définition courte). Fusion.
a('Cockcroft-Gault',[('Cockcroft-Gault','noms des deux auteurs de la formule (Donald Cockcroft et Henry Gault, 1976), non une abréviation')],'Formule de Cockcroft-Gault (clairance de la créatinine)',
 '<p>Estimation de la clairance de la créatinine (mL/min) à partir de l’âge, du poids, du sexe et de la créatininémie ; non indexée à la surface corporelle, elle sert de référence pour adapter la dose des anticoagulants oraux directs.</p>','i48-cg')

# ---------------------------------------------------------------- biologie, immunologie
# ADN : i30 (lupus) et i33 (biofilms) ; même sens, fusion.
a('ADN',[('A','Acide'),('D','Désoxyribo-'),('N','Nucléique')],'Acide désoxyribonucléique',
 '<p>Support de l’information génétique. Les anticorps anti-ADN natif sont très spécifiques du lupus érythémateux disséminé ; l’ADN extracellulaire participe à la matrice des biofilms bactériens.</p>')
# CD28, CD80, CD86 : i40 (riches) contre m06 (courtes, valeur finale). Fusion sur i40. La fenêtre i40-d-2l
# (immunosuppression de seconde ligne de la myocardite sous immunothérapie) n’est pas retenue pour CD80 et CD86 :
# trop spécifique d’un chapitre pour une définition générale (emplois aussi dans M06).
a('CD28',[('CD','Cluster of Differentiation (classe de différenciation)'),('28','numéro 28')],'Récepteur de costimulation CD28',
 '<p>Récepteur activateur des lymphocytes T ; sa liaison à CD80 ou CD86 des cellules présentatrices d’antigène fournit le second signal nécessaire à l’activation complète du lymphocyte T. CTLA-4 entre en compétition avec lui pour ces ligands.</p>')
a('CD80',[('CD','Cluster of Differentiation (classe de différenciation)'),('80','numéro 80')],'Molécule de costimulation CD80',
 '<p>Molécule des cellules présentatrices d’antigène, ligand de CD28 (activation) et de CTLA-4 (inhibition) ; bloquée par l’abatacept, protéine de fusion CTLA-4–immunoglobuline.</p>')
a('CD86',[('CD','Cluster of Differentiation (classe de différenciation)'),('86','numéro 86')],'Molécule de costimulation CD86',
 '<p>Second ligand, avec CD80, de CD28 et de CTLA-4, porté par les cellules présentatrices d’antigène ; bloquée par l’abatacept.</p>')
# CTLA-4 : d84 (« Antigen ») contre i40 (« Associated », valeur finale). Développement exact : Cytotoxic
# T-Lymphocyte-Associated protein 4 (nom officiel du gène). Fusion ; fenêtre i40-d-2l conservée (abatacept =
# CTLA-4–immunoglobuline ; 11 emplois sur 14 dans I40).
a('CTLA-4',[('C','Cytotoxic (cytotoxique)'),('T','T- (lymphocyte T)'),('L','Lymphocyte'),('A','Associated protein (protéine associée)'),('4','numéro 4')],'Protéine 4 associée aux lymphocytes T cytotoxiques',
 '<p>Récepteur inhibiteur (point de contrôle immunitaire) des lymphocytes T : il entre en compétition avec CD28 pour les ligands CD80 et CD86 et freine l’activation lymphocytaire. Cible de l’ipilimumab ; l’abatacept, protéine de fusion CTLA-4–immunoglobuline, en reproduit l’effet. Son haplo-insuffisance cause un déficit immunitaire avec dysrégulation, traité notamment par abatacept.</p>','i40-d-2l')
# PD-L1 : i40 (riche) contre m31 (courte, valeur finale). Fusion.
a('PD-L1',[('P','Programmed (programmée)'),('D','Death (mort cellulaire)'),('L','Ligand'),('1','numéro 1')],'Ligand 1 du récepteur de mort cellulaire programmée',
 '<p>Ligand du récepteur inhibiteur PD-1 (point de contrôle immunitaire), exprimé par de nombreux tissus, dont les cardiomyocytes et les cellules dendritiques, et par de nombreuses tumeurs ; il freine les lymphocytes T. Cible de l’atézolizumab et du durvalumab. Un défaut de son expression par les cellules dendritiques de la paroi artérielle participe à l’artérite à cellules géantes.</p>')
# PR3 : i33 contre m31 (valeur finale, développement « R = sérine protéase » inexact). PR = PRotéinase.
a('PR3',[('PR','PRotéinase'),('3','numéro 3')],'Protéinase 3',
 '<p>Sérine protéase des granules azurophiles des polynucléaires neutrophiles ; cible antigénique des ANCA de fluorescence cytoplasmique, associés surtout à la granulomatose avec polyangéite. Des anti-PR3 s’observent aussi, sans vascularite, dans l’endocardite infectieuse.</p>','m31-anca')
# RANKL : i35 (développement exact) contre m06 (valeur finale, développement décalé). Fusion.
a('RANKL',[('R','Receptor (récepteur)'),('A','Activator of (activateur du)'),('N','Nuclear factor (facteur nucléaire)'),('K','Kappa B'),('L','Ligand')],'Ligand du récepteur activateur du facteur nucléaire kappa B',
 '<p>Cytokine de la famille du facteur de nécrose tumorale qui active la différenciation et l’activité des ostéoclastes ; son antagoniste naturel est l’ostéoprotégérine. Elle participe aux érosions osseuses de la polyarthrite rhumatoïde et favorise la minéralisation de la valve aortique. Cible du dénosumab.</p>')
# TPMT : i40 (développement exact) contre m32 (valeur finale, « P = (S-) » inexact). Fusion.
a('TPMT',[('T','Thio-'),('P','purine'),('M','S-Méthyl-'),('T','transférase')],'Thiopurine S-méthyltransférase',
 '<p>Enzyme qui inactive l’azathioprine et la 6-mercaptopurine. Une activité faible ou nulle, d’origine génétique, expose à une toxicité médullaire grave (aplasie) : on la détermine avant le traitement.</p>','i40-d-aza')
# VEGF : i10 contre m31 (valeur finale). Fusion ; précision : le sunitinib est un inhibiteur de tyrosine kinase
# des récepteurs du VEGF, non un anticorps anti-VEGF.
a('VEGF',[('V','Vascular (vasculaire)'),('E','Endothelial (endothélial)'),('G','Growth (de croissance)'),('F','Factor (facteur)')],'Facteur de croissance de l’endothélium vasculaire',
 '<p>Facteur qui stimule l’angiogenèse et augmente la perméabilité vasculaire. Les anticorps anti-VEGF (bévacizumab) et les inhibiteurs de tyrosine kinase de ses récepteurs (sunitinib) provoquent fréquemment une hypertension et une protéinurie, et exposent à l’ischémie et à la thrombose artérielles.</p>')
# SARS-CoV-2 : i30 contre m31 (valeur finale). Fusion (myocardite, péricardite, syndrome inflammatoire pédiatrique).
a('SARS-CoV-2',[('S','Severe (sévère)'),('A','Acute (aigu)'),('R','Respiratory (respiratoire)'),('S','Syndrome'),('Co','Corona-'),('V','Virus'),('2','numéro 2')],'Coronavirus 2 du syndrome respiratoire aigu sévère',
 '<p>Virus responsable de la COVID-19 ; cause possible de myocardite et de péricardite, comme, plus rarement, les vaccins à ARN messager dirigés contre lui. Chez l’enfant, l’infection peut être suivie d’un syndrome inflammatoire multisystémique pédiatrique.</p>')
# DRESS : i40 (fenêtre i40-eos) contre t78 (valeur finale). Fusion ; fenêtre non retenue (causes des myocardites
# à éosinophiles, trop spécifique : 7 emplois sur 10 dans T78).
a('DRESS',[('D','Drug (médicamenteuse)'),('R','Reaction (réaction)'),('E','with Eosinophilia (avec éosinophilie)'),('S','and Systemic (et systémiques)'),('S','Symptoms (symptômes)')],'Réaction médicamenteuse avec éosinophilie et symptômes systémiques (syndrome DRESS)',
 '<p>Toxidermie grave retardée, 2 à 8 semaines après l’introduction du médicament : éruption étendue, fièvre, éosinophilie, atteinte viscérale (foie, rein, cœur, poumon). La réintroduction du médicament responsable et les tests de provocation sont contre-indiqués.</p>')

# ---------------------------------------------------------------- lipides, métabolisme
# LDL : i10, i21 et i70 (valeur finale, « principal lipide », inexact). Fusion sur la lipoprotéine.
a('LDL',[('L','Low (basse)'),('D','Density (densité)'),('L','Lipoprotein (lipoprotéine)')],'Lipoprotéine de basse densité',
 '<p>Principale lipoprotéine athérogène. La cible du cholestérol LDL dépend du risque cardiovasculaire ; à très haut risque, notamment après un syndrome coronarien aigu : &lt; 1,4 mmol/L et baisse d’au moins 50 % par rapport à la valeur initiale (recommandations ESC/EAS).</p>')
# PCSK9 : i21 (fenêtre i21-d-pcsk9) contre i70 (valeur finale). Fusion.
a('PCSK9',[('P','Proprotein (proprotéine)'),('C','Convertase'),('S','Subtilisin (subtilisine)'),('K','Kexin (kexine)'),('9','type 9')],'Proprotéine convertase subtilisine/kexine de type 9',
 '<p>Protéine hépatique qui se lie au récepteur des LDL et en provoque la dégradation. Cible des anticorps monoclonaux évolocumab et alirocumab, et de l’inclisiran, petit ARN interférent qui en bloque la synthèse.</p>','i21-d-pcsk9')
# SGLT2 : cardio_1 (fenêtre d-sglt2 ; « T = coTransporteur », mélange de langues) contre i70 (valeur finale). Fusion.
a('SGLT2',[('S','Sodium-'),('GL','GLucose'),('T','coTransporter (cotransporteur)'),('2','de type 2')],'Cotransporteur sodium-glucose de type 2',
 '<p>Transporteur du tube contourné proximal qui réabsorbe, couplé au sodium, environ 90 % du glucose filtré. Cible des gliflozines (dapagliflozine, empagliflozine), à bénéfice cardiovasculaire et rénal.</p>','d-sglt2')
# GLP-1 : cardio_1 (ICFEp) contre i70 (valeur finale, événements cardiovasculaires). Fusion.
a('GLP-1',[('G','Glucagon-'),('L','Like'),('P','Peptide'),('-1','de type 1')],'Peptide apparenté au glucagon de type 1',
 '<p>Incrétine intestinale qui stimule la sécrétion d’insuline de façon glucose-dépendante. Ses agonistes (sémaglutide, liraglutide) réduisent le poids et les événements cardiovasculaires majeurs chez les patients à haut risque, et améliorent les symptômes de l’ICFEp chez l’obèse (classe IIa, ESC 2026).</p>')

# ---------------------------------------------------------------- génétique des aortopathies
# i35 (définitions riches, fenêtre i35-marfan « Syndrome de Marfan et aortopathies héréditaires ») contre
# i71 (valeurs finales, très courtes) et i34. Fusion sur i35 ; fenêtre conservée (pertinente, elle cite ces gènes).
a('FBN1',[('FBN','FiBrilliNe (fibrillin)'),('1','type 1')],'Gène de la fibrilline 1',
 '<p>Gène de la fibrilline 1, protéine des microfibrilles de la matrice élastique qui séquestre le TGF-β. Ses variants pathogènes causent le syndrome de Marfan : dilatation de la racine aortique, ectopie du cristallin, prolapsus valvulaire mitral.</p>','i35-marfan')
a('COL3A1',[('COL','COLlagène'),('3','de type III'),('A1','chaîne alpha 1')],'Gène de la chaîne alpha 1 du collagène de type III',
 '<p>Gène du syndrome d’Ehlers-Danlos vasculaire : ruptures artérielles et digestives, fragilité tissulaire majeure.</p>','i35-marfan')
a('ACTA2',[('ACT','ACTine'),('A2','alpha 2 (muscle lisse)')],'Gène de l’actine alpha 2 du muscle lisse',
 '<p>Gène le plus fréquemment en cause dans les anévrismes et dissections familiaux non syndromiques de l’aorte thoracique.</p>')
a('SMAD3',[('SMAD','fusion de Sma (nématode) et MAD (Mothers Against Decapentaplegic, drosophile)'),('3','membre 3')],'Gène SMAD3',
 '<p>Médiateur intracellulaire de la signalisation du TGF-β ; ses variants causent une forme de syndrome de Loeys-Dietz avec arthrose précoce.</p>','i35-marfan')
a('TGFB2',[('TGFB','Transforming Growth Factor Beta (facteur de croissance transformant bêta)'),('2','isoforme 2')],'Gène du TGF-β2',
 '<p>Gène d’une forme de syndrome de Loeys-Dietz.</p>','i35-marfan')
a('TGFBR1',[('TGFB','Transforming Growth Factor Beta (facteur de croissance transformant bêta)'),('R','Receptor (récepteur)'),('1','de type 1')],'Gène du récepteur de type 1 du TGF-β',
 '<p>Gène du syndrome de Loeys-Dietz.</p>','i35-marfan')
a('TGFBR2',[('TGFB','Transforming Growth Factor Beta (facteur de croissance transformant bêta)'),('R','Receptor (récepteur)'),('2','de type 2')],'Gène du récepteur de type 2 du TGF-β',
 '<p>Gène du syndrome de Loeys-Dietz ; dissections possibles à de petits diamètres.</p>','i35-marfan')
# TGF-β : i34 (valeur finale) et i35 (fenêtre i35-marfan). Fusion.
a('TGF-β',[('T','Transforming (de transformation)'),('G','Growth (croissance)'),('F','Factor (facteur)'),('β','bêta')],'Facteur de croissance transformant bêta',
 '<p>Cytokine qui régule la synthèse de la matrice extracellulaire et favorise la fibrose. Sa signalisation excessive intervient dans la paroi aortique du syndrome de Marfan et du syndrome de Loeys-Dietz, dans la dégénérescence myxoïde valvulaire et dans la fibrose valvulaire induite par la sérotonine.</p>','i35-marfan')
a('Loeys-Dietz',[('Loeys-Dietz','noms propres : Bart Loeys et Harry Dietz, généticiens, 2005')],'Syndrome de Loeys-Dietz',
 '<p>Aortopathie héréditaire autosomique dominante de la voie du TGF-β (<i>TGFBR1</i>, <i>TGFBR2</i>, <i>SMAD3</i>, <i>TGFB2</i>…) : dissections à de petits diamètres, tortuosité artérielle.</p>','i35-marfan')
# Ehlers-Danlos : i35 (fenêtre) contre m31 (valeur finale) ; I49 emploie la forme hypermobile : définition
# générale couvrant les deux formes citées dans les cours.
a('Ehlers-Danlos',[('Ehlers-Danlos','noms propres : Edvard Ehlers et Henri-Alexandre Danlos, dermatologues, début du XXe siècle')],'Syndrome d’Ehlers-Danlos',
 '<p>Groupe de maladies héréditaires du tissu conjonctif (classification internationale de 2017). La forme vasculaire (<i>COL3A1</i>) expose aux ruptures artérielles et digestives ; la forme hypermobile, la plus fréquente et sans gène identifié, repose sur des critères cliniques, dont l’hypermobilité articulaire généralisée.</p>','i35-marfan')

# ---------------------------------------------------------------- codes
# D86.8 : i40 et i42 (valeur finale) ; même sens. Développement en deux segments (i40), définition i42.
a('D86.8',[('D86','catégorie CIM-10 de la sarcoïdose'),('.8','sarcoïdose d’autres localisations et de localisations associées')],'Code CIM-10 D86.8 : sarcoïdose d’autres localisations et de localisations associées',
 '<p>Code étiologique utilisé avec I43.8 pour la cardiomyopathie sarcoïdosique et avec I41.8 pour la myocardite sarcoïdosique.</p>','i42-sarcoid')

# ---------------------------------------------------------------- sociétés savantes et revues
# ERS : j18 (valeur finale actuelle et Alpha) contre q21 (valeur finale Claude, fenêtre q21-htap). Libellé complet
# de q21 ; définition générale couvrant I26, J18, J44, J45 et Q21 ; fenêtre q21-htap non retenue (spécifique Q21).
a('ERS',[('E','European'),('R','Respiratory'),('S','Society')],'European Respiratory Society (Société européenne de pneumologie)',
 '<p>Société savante européenne de pneumologie. Elle publie, seule ou avec d’autres sociétés, des recommandations et des normes techniques : avec l’ESC, l’embolie pulmonaire aiguë (2019) et l’hypertension pulmonaire (2022) ; avec l’American Thoracic Society, la réalisation et l’interprétation des explorations fonctionnelles respiratoires ; avec l’ESICM, l’ESCMID et l’ALAT, la pneumonie communautaire sévère (2023).</p>')
# ESICM : i46, i49 (valeur finale Claude, fenêtre i49-rosc) et j18 (valeur finale actuelle et Alpha, courte).
# Fenêtre i49-rosc conservée : 23 emplois sur 24 concernent les recommandations ERC-ESICM post-réanimation.
a('ESICM',[('E','European'),('S','Society of'),('I','Intensive'),('C','Care'),('M','Medicine')],'European Society of Intensive Care Medicine (Société européenne de médecine intensive)',
 '<p>Société savante européenne de médecine intensive. Coautrice, avec l’ERC, des recommandations sur les soins après réanimation (2021, mise à jour 2025) et, avec l’ERS, l’ESCMID et l’ALAT, des recommandations 2023 sur la pneumonie communautaire sévère.</p>','i49-rosc')
# SSI : i33 (valeur finale Claude, fenêtre i33-prophy) contre j18 (valeur finale actuelle et Alpha, développement
# anglais). Développement français littéral (Société Suisse d’Infectiologie) ; fenêtre non retenue (29 emplois
# sur 30 dans J18, hors antibioprophylaxie).
a('SSI',[('S','Société'),('S','Suisse d’'),('I','Infectiologie')],'Société suisse d’infectiologie',
 '<p>Société savante suisse des maladies infectieuses. Elle publie les recommandations suisses de prise en charge des infections, dont les infections respiratoires aiguës et la pneumonie communautaire de l’adulte, et, avec la Société suisse de cardiologie et les sociétés pédiatriques, les recommandations d’antibioprophylaxie de l’endocardite (2021).</p>')
# JAMA : i30 (mention de l’essai AIRTRIP, propre à un chapitre) contre t78 (valeur finale, « Revue JAMA »).
# Définition générale ; mention des revues de spécialité (T78 cite JAMA Internal Medicine).
a('JAMA',[('J','Journal of the'),('A','American'),('M','Medical'),('A','Association')],'JAMA (Journal of the American Medical Association)',
 '<p>Revue médicale généraliste à comité de lecture, publiée par l’American Medical Association (Association médicale américaine) ; le même éditeur publie les revues de spécialité du réseau JAMA, comme <i>JAMA Internal Medicine</i>.</p>')

# ---------------------------------------------------------------- essais
# CAPRIE : i25 (fenêtre i25-d-clopi) contre i70 (valeur finale). Fusion.
a('CAPRIE',[('C','Clopidogrel versus'),('A','Aspirin in'),('P','Patients at'),('R','Risk of'),('I','Ischaemic'),('E','Events')],'Essai CAPRIE (1996)',
 '<p>Clopidogrel 75 mg par jour comparé à l’acide acétylsalicylique 325 mg par jour chez des patients vasculaires (accident vasculaire cérébral ischémique récent, infarctus récent ou artériopathie périphérique symptomatique) : réduction relative modeste des événements ischémiques, plus marquée dans le sous-groupe de l’artériopathie périphérique (analyse de sous-groupe).</p>','i25-d-clopi')
# COMPASS : i21 (2017, fenêtre i21-dapt) contre i70 (2018, valeur finale). Publication princeps : N Engl J Med
# 2017;377:1319-30 → 2017. La fenêtre i21-dapt ne traite pas de COMPASS : remplacée par i25-d-riva
# (« Rivaroxaban à dose vasculaire », qui décrit l’essai COMPASS 2017).
a('COMPASS',[('C','Cardiovascular'),('OM','OutcoMes for'),('P','People using'),('A','Anticoagulation'),('SS','StrategieS')],'Essai COMPASS (2017)',
 '<p>Maladie coronaire ou artériopathie périphérique stables : rivaroxaban 2,5 mg deux fois par jour associé à l’acide acétylsalicylique 100 mg par jour, comparé à l’acide acétylsalicylique seul, a réduit les décès cardiovasculaires, les accidents vasculaires cérébraux et les infarctus, ainsi que les événements ischémiques majeurs des membres, au prix d’une hausse des hémorragies majeures, sans hausse des hémorragies mortelles ou intracrâniennes.</p>','i25-d-riva')
# ASTRAL, CORAL : i10 (développement lettre à lettre, fenêtre i10-sar) contre i70 (valeur finale). Fusion.
a('ASTRAL',[('A','Angioplasty (angioplastie)'),('ST','and STenting (et endoprothèse)'),('R','for Renal (rénale)'),('A','Artery (artère)'),('L','Lesions (lésions)')],'Essai ASTRAL (2009)',
 '<p>Sténose athéromateuse de l’artère rénale : la revascularisation associée au traitement médical, comparée au traitement médical seul, n’apporte pas de bénéfice sur la fonction rénale ni sur les événements rénaux et cardiovasculaires.</p>','i10-sar')
a('CORAL',[('C','Cardiovascular'),('O','Outcomes in'),('R','Renal'),('A','Atherosclerotic'),('L','Lesions')],'Essai CORAL (2014)',
 '<p>Sténose athéromateuse de l’artère rénale avec hypertension ou maladie rénale chronique : l’endoprothèse ajoutée au traitement médical optimal ne réduit pas les événements cardiovasculaires et rénaux ; résultat concordant avec ASTRAL.</p>','i10-sar')
# FOURIER : i21 (fenêtre i21-d-pcsk9) contre i70 (valeur finale). Fusion.
a('FOURIER',[('FOURIER','Further cardiOvascular OUtcomes Research with PCSK9 Inhibition in subjects with Elevated Risk, non strictement lettre à lettre')],'Essai FOURIER (2017)',
 '<p>Évolocumab contre placebo chez des patients athéroscléreux (antécédent d’infarctus, d’accident vasculaire cérébral ischémique ou artériopathie périphérique symptomatique) traités par statine : réduction des événements cardiovasculaires majeurs, y compris des événements ischémiques des membres.</p>','i21-d-pcsk9')
# AMPLIFY : i26 (Alpha, enrichie à 12:59 : effectif et taux) contre i80 (valeur finale Claude). Développement
# vérifié (American College of Cardiology ; Journal of the American Heart Association 2015). Fusion ; chiffres
# conformes à la publication princeps (Agnelli et coll., N Engl J Med 2013).
a('AMPLIFY',[('AMPLIFY','Apixaban for the Initial Management of Pulmonary Embolism and Deep-Vein Thrombosis as First-Line Therapy, non strictement lettre à lettre')],'Essai AMPLIFY (2013)',
 '<p>Apixaban oral d’emblée comparé à l’énoxaparine relayée par la warfarine, pendant 6 mois, chez 5 395 adultes présentant une thrombose veineuse profonde proximale ou une embolie pulmonaire symptomatique : non-infériorité sur la récidive thromboembolique ou le décès lié (2,3 % contre 2,7 %) et moins d’hémorragies majeures (0,6 % contre 1,8 %).</p>')
# MIRRA : i40 (fenêtre i40-d-eos) contre m31 (valeur finale). Développement vérifié : Mepolizumab In Relapsing
# or Refractory EGPA. Fusion.
a('MIRRA',[('MIRRA','Mepolizumab In Relapsing or Refractory EGPA (granulomatose éosinophilique avec polyangéite), non strictement lettre à lettre')],'Essai MIRRA (2017)',
 '<p>Essai randomisé de phase 3 : le mépolizumab 300 mg par voie sous-cutanée toutes les 4 semaines, ajouté au traitement standard, augmente la durée de rémission et réduit la dose de corticoïdes dans la granulomatose éosinophilique avec polyangéite récidivante ou réfractaire.</p>','i40-d-eos')

# ---------------------------------------------------------------- clés de j44.py (fusion J44 en cours par un autre agent)
# Contrôle final de j44.py (version du 26.09.2026, 12:36) : seule clé qui écrase une définition d’un autre fichier.
# VNI : cardio_1 (œdème pulmonaire, 2 emplois I50) écrasée par j44 (exacerbation de BPCO, 14 emplois, fenêtre j44-vni).
# Définition générale fusionnée ; fenêtre j44-vni conservée (indications, contre-indications et suivi de la VNI).
a('VNI',[('V','Ventilation'),('N','Non'),('I','Invasive')],'Ventilation non invasive',
 '<p>Ventilation en pression positive délivrée par un masque, sans intubation. Elle réduit le travail respiratoire ; dans l’œdème pulmonaire cardiogénique, elle diminue aussi la précharge et la postcharge du ventricule gauche. Indication clé : acidose respiratoire de l’exacerbation de BPCO ; au long cours, à domicile, dans l’hypercapnie persistante après une exacerbation.</p>','j44-vni')
