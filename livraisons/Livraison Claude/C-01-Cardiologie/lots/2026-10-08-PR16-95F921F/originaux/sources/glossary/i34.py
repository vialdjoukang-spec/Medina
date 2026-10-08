# Glossaire MEDINA — chapitre I34 (valvulopathies mitrales, tricuspides et pulmonaires : I34, I36, I37, I05, I07, I08, I09)
from cardio_1 import a, G

# ---- quantification échocardiographique
a('SOR',[('S','Surface de'),('O','l’Orifice'),('R','Régurgitant')],'Surface de l’orifice régurgitant',
 '<p>Surface effective de l’orifice par lequel le sang reflue, calculée le plus souvent par la méthode PISA (débit de convergence / vitesse maximale du jet). Fuite mitrale primaire sévère : ≥ 40 mm². Équivalent anglais : EROA (<i>effective regurgitant orifice area</i>).</p>','i34-pisa')
a('PISA',[('P','Proximal (en amont de l’orifice)'),('I','Isovelocity (d’isovitesse)'),('S','Surface'),('A','Area (aire)')],'Proximal isovelocity surface area (surface d’isovitesse proximale)',
 '<p>Méthode de quantification d’une fuite fondée sur la conservation du débit : le débit à travers l’hémisphère de convergence de rayon r, à la vitesse de repliement, égale le débit à travers l’orifice régurgitant.</p>','i34-pisa')
a('PHT',[('P','Pressure (pression)'),('H','Half (demi-)'),('T','Time (temps)')],'Pressure half-time (temps de demi-pression)',
 '<p>Temps nécessaire pour que le gradient transmitral maximal diminue de moitié. Surface mitrale ≈ 220 / PHT (ms). Un PHT ≥ 220 ms correspond à une surface ≤ 1,0 cm².</p>','i34-pht')
a('ITV',[('I','Intégrale'),('T','Temps-'),('V','Vitesse')],'Intégrale temps-vitesse',
 '<p>Surface sous la courbe de vitesse Doppler d’un flux pendant un cycle (en cm) : distance parcourue par le sang. Multipliée par une surface, elle donne un volume par battement (volume régurgité = SOR × ITV du jet).</p>','i34-pisa')
a('PAPs',[('P','Pression'),('A','Artérielle'),('P','Pulmonaire'),('s','systolique')],'Pression artérielle pulmonaire systolique',
 '<p>Estimée en échocardiographie par 4 × (vitesse de la fuite tricuspide)² + pression de l’oreillette droite. Une valeur au repos &gt; 50 mmHg est un critère opératoire dans la fuite mitrale primaire et le rétrécissement mitral. Sous-estimée dans la fuite tricuspide torrentielle.</p>','i34-bernoulli')
a('P1',[('P','feuillet mitral Postérieur'),('1','segment 1, latéral (côté de la commissure antérolatérale)')],'Segment latéral du feuillet mitral postérieur (nomenclature de Carpentier)',
 '<p>Premier des trois segments du feuillet postérieur, voisin de la commissure antérolatérale.</p>','i34-sa-app')
a('P2',[('P','feuillet mitral Postérieur'),('2','segment 2, moyen')],'Segment moyen du feuillet mitral postérieur (nomenclature de Carpentier)',
 '<p>Segment le plus souvent atteint par le prolapsus et la rupture de cordage, notamment dans la déficience fibroélastique ; lésion la plus facilement réparable.</p>','i34-sa-app')
a('P3',[('P','feuillet mitral Postérieur'),('3','segment 3, médial (côté de la commissure postéromédiale)')],'Segment médial du feuillet mitral postérieur (nomenclature de Carpentier)',
 '<p>Troisième segment du feuillet postérieur, voisin de la commissure postéromédiale.</p>','i34-sa-app')
a('EAE',[('E','European'),('A','Association of'),('E','Echocardiography')],'European Association of Echocardiography (Association européenne d’échocardiographie)',
 '<p>Ancienne association de l’ESC, devenue l’EACVI. Elle a publié avec l’ASE en 2009 les recommandations d’évaluation échocardiographique des sténoses valvulaires.</p>')

# ---- essais et scores
a('MITRA-FR',[('MITRA','nom d’essai : reprend « mitral » et le dispositif MitraClip ; non développable lettre à lettre'),('FR','France (essai français)')],'Essai MITRA-FR (2018)',
 '<p>Essai randomisé français : réparation mitrale bord à bord percutanée dans la fuite mitrale secondaire sévère avec FEVG 15–40 % ; aucun bénéfice à 12 mois sur décès ou réhospitalisation.</p>','i34-mitrafr')
a('RESHAPE-HF2',[('RESHAPE-HF','nom d’essai : acronyme anglais non développable lettre à lettre (« remodeler », Heart Failure : insuffisance cardiaque)'),('2','deuxième essai de la série')],'Essai RESHAPE-HF2 (2024)',
 '<p>Essai randomisé européen : réparation mitrale bord à bord percutanée dans la fuite mitrale secondaire modérée à sévère ou sévère ; réduction des hospitalisations pour insuffisance cardiaque et amélioration de la qualité de vie, sans effet sur la mortalité totale.</p>','i34-reshape')
a('TRILUMINATE',[('TRILUMINATE','nom d’essai : Trial to Evaluate Cardiovascular Outcomes in Patients Treated With the Tricuspid Valve Repair System Pivotal ; acronyme non développable lettre à lettre')],'Essai TRILUMINATE Pivotal (2023)',
 '<p>Essai randomisé : réparation tricuspide bord à bord percutanée contre traitement médical dans la fuite tricuspide sévère ; bénéfice sur un critère hiérarchique porté par la qualité de vie, sans effet sur la mortalité.</p>','i34-trilum')
a('TRISCEND II',[('TRISCEND','nom d’essai : « TRI » pour tricuspide ; le reste de l’acronyme, commercial, n’est pas développable lettre à lettre'),('II','deuxième essai de la série')],'Essai TRISCEND II (2024)',
 '<p>Essai randomisé : remplacement tricuspide percutané contre traitement médical dans la fuite tricuspide sévère ; rapport de gains 2,02, qualité de vie améliorée, au prix d’hémorragies et de stimulateurs.</p>','i34-triscend')
a('TRI-SCORE',[('TRI','TRIcuspide'),('SCORE','score de risque')],'Score de risque de la chirurgie tricuspide isolée',
 '<p>Score de 0 à 12 points (âge, classe NYHA, insuffisance cardiaque droite, dose de furosémide, DFG, bilirubine, FEVG, fonction ventriculaire droite) qui prédit la mortalité hospitalière après chirurgie tricuspide isolée.</p>','i34-triscore')
a('KCCQ',[('K','Kansas'),('C','City'),('C','Cardiomyopathy'),('Q','Questionnaire')],'Kansas City Cardiomyopathy Questionnaire',
 '<p>Questionnaire de qualité de vie spécifique de l’insuffisance cardiaque, coté de 0 à 100 ; une variation de 5 points est considérée comme cliniquement perceptible.</p>')
a('PRIME',[('PRIME','nom d’essai : Pharmacological Reduction of functional, Ischemic Mitral rEgurgitation ; acronyme non développable lettre à lettre')],'Essai PRIME (2019)',
 '<p>Essai randomisé : dans la fuite mitrale secondaire ischémique, le sacubitril/valsartan réduisait davantage la surface de l’orifice régurgitant que le valsartan à 12 mois.</p>')

# ---- biologie moléculaire et génétique
a('5-HT2B',[('5-HT','5-hydroxytryptamine (sérotonine)'),('2B','récepteur de sous-type 2B')],'Récepteur sérotoninergique de sous-type 2B',
 '<p>Récepteur couplé à la protéine Gq, exprimé par les cellules interstitielles valvulaires. Sa stimulation (sérotonine carcinoïde, norfenfluramine, pergolide, cabergoline, ergot, ecstasy) provoque une fibrose valvulaire restrictive.</p>','i34-medic')
a('TGF-β',[('T','Transforming (de transformation)'),('G','Growth (croissance)'),('F','Factor (facteur)'),('β','bêta')],'Facteur de croissance transformant bêta',
 '<p>Cytokine profibrosante. Son activation excessive intervient dans le syndrome de Marfan, dans la dégénérescence myxoïde et dans la fibrose valvulaire induite par la sérotonine.</p>')
a('FBN1',[('FBN','FiBrilliNe'),('1','type 1')],'Gène de la fibrilline 1',
 '<p>Gène dont les variants causent le syndrome de Marfan : prolapsus mitral, dilatation de la racine aortique, ectopie du cristallin.</p>')
a('FLNA',[('FLN','FiLamiNe'),('A','A')],'Gène de la filamine A',
 '<p>Gène lié à l’X, codant une protéine du cytosquelette ; certains variants causent une dystrophie valvulaire myxoïde familiale.</p>')
a('DCHS1',[('DCHS','Dachsous (gène de polarité cellulaire, nom issu de la drosophile)'),('1','homologue 1')],'Gène Dachsous 1',
 '<p>Gène de la polarité planaire des cellules ; ses variants perturbent le développement valvulaire et causent des prolapsus mitraux familiaux.</p>')
a('DZIP1',[('D','DAZ (gène « Deleted in AZoospermia »)'),('Z','Zinc finger (doigt de zinc)'),('IP','Interacting Protein (protéine d’interaction)'),('1','de type 1')],'Protéine à doigt de zinc interagissant avec DAZ, de type 1',
 '<p>Protéine du cil primaire ; ses variants ont été identifiés dans des prolapsus mitraux familiaux non syndromiques.</p>')
a('DAZ',[('D','Deleted in (délété dans)'),('AZ','AZoospermia (azoospermie)')],'Gène « Deleted in azoospermia »',
 '<p>Famille de gènes du chromosome Y impliqués dans la spermatogenèse ; donne son nom à la protéine DZIP1.</p>')
a('PTPN11',[('PTP','Protein Tyrosine Phosphatase (protéine tyrosine phosphatase)'),('N','Non récepteur'),('11','type 11')],'Gène de la tyrosine phosphatase non récepteur de type 11',
 '<p>Gène le plus souvent muté dans le syndrome de Noonan, qui associe rétrécissement pulmonaire à valve dysplasique et cardiomyopathie hypertrophique.</p>','i34-noonan')
a('MESC',[('M','Mobilité des feuillets'),('E','Épaississement des feuillets'),('S','appareil Sous-valvulaire'),('C','Calcification')],'Moyen mnémotechnique des quatre items du score de Wilkins',
 '<p>Aide pédagogique, non critère officiel : chaque item est coté de 1 à 4 ; un total ≤ 8 est favorable à la commissurotomie mitrale percutanée.</p>','i34-mnemo-mesc')
a('MATTERHORN',[('MATTERHORN','nom d’essai : acronyme anglais tiré de lettres choisies du titre (Mitral vAlve reconsTrucTion for advancEd insufficiency of functional or iscHemic ORigiN) ; non développable lettre à lettre')],'Essai MATTERHORN (2024)',
 '<p>Essai randomisé allemand de non-infériorité : chez des patients opérables avec fuite mitrale secondaire, la réparation bord à bord percutanée n’était pas inférieure à la chirurgie mitrale à un an, avec moins de complications.</p>','i34-matterhorn')
