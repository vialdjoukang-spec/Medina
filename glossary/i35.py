# Glossaire MEDINA — chapitre I35 (valvulopathies aortiques, I35 et I06)
from cardio_1 import a, G

def b(k, *args):
    """Ajoute la clé seulement si un autre chapitre ne l'a pas déjà définie."""
    if k not in G: a(k, *args)

# ---- maladies et mesures
a('RA',[('R','Rétrécissement'),('A','Aortique')],'Rétrécissement aortique',
 '<p>Obstacle valvulaire à l’éjection du ventricule gauche, par réduction de l’ouverture des cuspides (synonyme : sténose aortique). Sévère si Vmax ≥ 4 m/s, gradient moyen ≥ 40 mmHg et surface &lt; 1 cm².</p>','i35-grades')
a('IA',[('I','Insuffisance'),('A','Aortique')],'Insuffisance aortique',
 '<p>Fermeture incomplète de la valve aortique en diastole, avec reflux de sang de l’aorte vers le ventricule gauche. Cause valvulaire (cuspides) ou aortique (racine dilatée) ; forme aiguë ou chronique.</p>','i35-iaquant')
a('RVA',[('R','Remplacement'),('V','Valvulaire'),('A','Aortique')],'Remplacement valvulaire aortique (chirurgical)',
 '<p>Excision de la valve native et implantation d’une prothèse mécanique ou biologique sous circulation extracorporelle. Préféré avant 70 ans chez le patient à faible risque (ESC/EACTS 2025).</p>','i35-rva')
a('SVA',[('S','Surface'),('V','Valvulaire'),('A','Aortique')],'Surface valvulaire aortique',
 '<p>Surface de l’orifice aortique en systole, calculée par l’équation de continuité. Normale 3 à 4 cm² ; RA sévère si &lt; 1,0 cm² (indexée &lt; 0,6 cm²/m²).</p>','i35-continuite')
a('Vmax',[('V','Vitesse'),('max','maximale')],'Vitesse maximale transvalvulaire aortique',
 '<p>Vitesse la plus élevée du flux à travers la valve aortique, mesurée au Doppler continu. RA sévère si ≥ 4,0 m/s ; très sévère au-delà de 5 à 5,5 m/s selon la source.</p>','i35-bernoulli')
a('VESi',[('V','Volume'),('E','d’Éjection'),('S','Systolique'),('i','indexé')],'Volume d’éjection systolique indexé',
 '<p>Volume éjecté à chaque systole rapporté à la surface corporelle, mesuré dans la chambre de chasse du ventricule gauche. Bas débit si ≤ 35 mL/m².</p>','i35-discord')
a('CCVG',[('C','Chambre de'),('C','Chasse du'),('V','Ventricule'),('G','Gauche')],'Chambre de chasse du ventricule gauche',
 '<p>Segment du ventricule gauche situé juste sous la valve aortique. Son diamètre, élevé au carré, entre dans l’équation de continuité : c’est la principale source d’erreur du calcul de la surface.</p>','i35-continuite')
b('ITV',[('I','Intégrale'),('T','Temps-'),('V','Vitesse')],'Intégrale temps-vitesse',
 '<p>Surface sous la courbe de vitesse Doppler d’un flux pendant un cycle, exprimée en centimètres : distance parcourue par le sang pendant l’éjection. Multipliée par une surface de section, elle donne un volume.</p>','i35-continuite')
a('DTSVG',[('D','Diamètre'),('T','Télé-'),('S','Systolique du'),('V','Ventricule'),('G','Gauche')],'Diamètre télésystolique du ventricule gauche',
 '<p>Diamètre du ventricule gauche en fin de systole. Dans l’IA asymptomatique, chirurgie recommandée si &gt; 50 mm ou &gt; 25 mm/m² ; à discuter si &gt; 22 mm/m² (ESC/EACTS 2025).</p>','i35-mnemo-ia-seuils')
a('Lp(a)',[('L','Lipo-'),('p','protéine'),('(a)','petit a : porteuse de l’apolipoprotéine(a)')],'Lipoprotéine(a)',
 '<p>Lipoprotéine proche du LDL, liée à l’apolipoprotéine(a), dont le taux est surtout génétique. Facteur de risque d’athérosclérose et de RA calcifié.</p>','i35-lpa')
a('mWHO',[('m','modified (modifiée)'),('W','World'),('H','Health'),('O','Organization')],'Classification de risque maternel de l’Organisation mondiale de la santé modifiée',
 '<p>Classe les cardiopathies de I (risque non augmenté) à IV (grossesse déconseillée). L’ESC 2025 la complète (mWHO 2.0) par des modificateurs de risque.</p>','i35-grossesse')
a('Q23.1',[('Q23.1','code CIM-10 : Q = malformations congénitales ; Q23 = malformations congénitales des valves aortique et mitrale ; .1 = insuffisance congénitale de la valve aortique')],'Code CIM-10 Q23.1 : insuffisance congénitale de la valve aortique',
 '<p>Code qui inclut la valve aortique bicuspide.</p>')
a('VARC-3',[('V','Valve'),('A','Academic'),('R','Research'),('C','Consortium'),('3','troisième version')],'Valve Academic Research Consortium, troisième version (2021)',
 '<p>Définitions standardisées des critères de jugement des essais de TAVI et de prothèses valvulaires (désaccord patient-prothèse, dégénérescence, complications).</p>','i35-ppm')
a('CARPREG II',[('CAR','CARdiac disease (cardiopathie)'),('PREG','in PREGnancy (pendant la grossesse)'),('II','deuxième version')],'Score de risque cardiaque maternel CARPREG II',
 '<p>Score canadien qui estime le risque d’événement cardiaque maternel pendant la grossesse ; ses modificateurs enrichissent la classification mWHO 2.0 (ESC 2025).</p>','i35-grossesse')
a('SwissTAVI',[('Swiss','suisse'),('TAVI','Transcatheter Aortic Valve Implantation (implantation valvulaire aortique percutanée)')],'Registre national suisse des TAVI',
 '<p>Registre prospectif national qui recueille, depuis 2011, les données des patients traités par TAVI en Suisse.</p>')

# ---- noms propres composés
a('Williams-Beuren',[('Williams-Beuren','noms propres : J. C. P. Williams (Nouvelle-Zélande) et A. J. Beuren (Allemagne), 1961–1962')],'Syndrome de Williams-Beuren',
 '<p>Microdélétion 7q11.23 emportant le gène de l’élastine : sténose aortique supravalvulaire, faciès particulier, hypercalcémie, profil cognitif spécifique.</p>')
a('Loeys-Dietz',[('Loeys-Dietz','noms propres : Bart Loeys et Harry Dietz, généticiens, 2005')],'Syndrome de Loeys-Dietz',
 '<p>Aortopathie héréditaire autosomique dominante de la voie du TGF-β (<i>TGFBR1</i>, <i>TGFBR2</i>, <i>SMAD3</i>, <i>TGFB2</i>…) : dissections à de petits diamètres, tortuosité artérielle.</p>','i35-marfan')
a('Ehlers-Danlos',[('Ehlers-Danlos','noms propres : Edvard Ehlers et Henri-Alexandre Danlos, dermatologues, début du XXe siècle')],'Syndrome d’Ehlers-Danlos',
 '<p>Groupe de maladies héréditaires du tissu conjonctif ; la forme vasculaire (<i>COL3A1</i>) expose aux ruptures artérielles et digestives.</p>','i35-marfan')
a('Sokolow-Lyon',[('Sokolow-Lyon','noms propres : Maurice Sokolow et Thomas Lyon, cardiologues, 1949')],'Indice de Sokolow-Lyon',
 '<p>Critère ECG d’hypertrophie ventriculaire gauche : onde S en V1 + onde R en V5 ou V6 &gt; 35 mm.</p>')

# ---- biologie moléculaire et gènes
b('TGF-β',[('T','Transforming'),('G','Growth'),('F','Factor'),('β','bêta')],'Facteur de croissance transformant bêta',
 '<p>Cytokine qui régule la synthèse de la matrice extracellulaire. Sa signalisation excessive dans la paroi aortique participe au syndrome de Marfan et au syndrome de Loeys-Dietz.</p>','i35-marfan')
b('FBN1',[('FBN','FiBrilliNe'),('1','type 1')],'Gène de la fibrilline 1',
 '<p>Gène du syndrome de Marfan. La fibrilline 1 forme les microfibrilles de la matrice élastique et séquestre le TGF-β.</p>','i35-marfan')
a('TGFBR1',[('TGFB','Transforming Growth Factor Bêta'),('R','Récepteur'),('1','de type 1')],'Gène du récepteur de type 1 du TGF-β','<p>Gène du syndrome de Loeys-Dietz.</p>','i35-marfan')
a('TGFBR2',[('TGFB','Transforming Growth Factor Bêta'),('R','Récepteur'),('2','de type 2')],'Gène du récepteur de type 2 du TGF-β','<p>Gène du syndrome de Loeys-Dietz ; dissections possibles à de petits diamètres.</p>','i35-marfan')
a('TGFB2',[('TGFB','Transforming Growth Factor Bêta'),('2','isoforme 2')],'Gène du TGF-β2','<p>Gène d’une forme de syndrome de Loeys-Dietz.</p>','i35-marfan')
a('SMAD3',[('SMAD','fusion de Sma (nématode) et MAD (Mothers Against Decapentaplegic, drosophile)'),('3','membre 3')],'Gène SMAD3',
 '<p>Médiateur intracellulaire de la signalisation du TGF-β ; ses variants causent une forme de syndrome de Loeys-Dietz avec arthrose précoce.</p>','i35-marfan')
a('COL3A1',[('COL','COLlagène'),('3','de type III'),('A1','chaîne alpha 1')],'Gène de la chaîne alpha 1 du collagène de type III',
 '<p>Gène du syndrome d’Ehlers-Danlos vasculaire.</p>','i35-marfan')
a('ACTA2',[('ACT','ACTine'),('A2','alpha 2 (musculaire lisse)')],'Gène de l’actine alpha 2 du muscle lisse',
 '<p>Gène le plus fréquent des anévrismes familiaux non syndromiques de l’aorte thoracique.</p>')
a('NOTCH1',[('NOTCH','« encoche » : nom du gène découvert chez la drosophile, dont les mutants ont des ailes échancrées'),('1','membre 1')],'Gène NOTCH1',
 '<p>Récepteur de signalisation du développement ; ses variants perte de fonction associent bicuspidie aortique familiale et calcification valvulaire précoce.</p>')
a('NF-κB',[('N','Nuclear (nucléaire)'),('F','Factor (facteur)'),('κ','kappa : amplificateur de la chaîne légère kappa (kappa-light-chain enhancer)'),('B','des lymphocytes B activés')],'Facteur nucléaire kappa B',
 '<p>Facteur de transcription central de l’inflammation ; activé dans les cellules interstitielles valvulaires par les phospholipides oxydés.</p>','i35-calcif')
a('Runx2',[('Run','Runt (famille de gènes « runt »)'),('x','related (apparenté)'),('2','membre 2')],'Facteur de transcription Runx2',
 '<p>Régulateur principal de la différenciation ostéoblastique ; exprimé par les cellules valvulaires qui calcifient.</p>','i35-calcif')
a('BMP2',[('B','Bone (os)'),('M','Morphogenetic (morphogénétique)'),('P','Protein (protéine)'),('2','type 2')],'Protéine morphogénétique osseuse de type 2',
 '<p>Facteur ostéogénique impliqué dans la calcification valvulaire.</p>','i35-calcif')
a('RANKL',[('R','Receptor (récepteur)'),('A','Activator of (activateur du)'),('N','Nuclear factor'),('K','Kappa B'),('L','Ligand')],'Ligand du récepteur activateur du facteur nucléaire kappa B',
 '<p>Cytokine du remodelage osseux ; dans la valve, elle favorise la minéralisation. Son antagoniste naturel est l’ostéoprotégérine.</p>')
a('OPG',[('O','Ostéo-'),('P','Protégé-'),('G','-rine')],'Ostéoprotégérine','<p>Récepteur leurre qui neutralise le RANKL et freine la minéralisation.</p>')
a('MGP',[('M','Matrix (matrice)'),('G','Gla (acide gamma-carboxyglutamique)'),('P','Protein (protéine)')],'Protéine Gla de la matrice',
 '<p>Inhibiteur naturel de la calcification des tissus mous, actif après une carboxylation dépendante de la vitamine K ; les antivitamines K réduisent cette activation.</p>')
a('ADAMTS13',[('A','A'),('DAM','Disintegrin And Metalloproteinase (désintégrine et métalloprotéase)'),('TS','with ThromboSpondin motifs (à motifs de thrombospondine)'),('13','membre 13')],'Protéase ADAMTS13',
 '<p>Enzyme qui clive le facteur von Willebrand ; dans le RA sévère, elle coupe les grands multimères dépliés par le cisaillement (syndrome de Heyde).</p>','i35-heyde')

# ---- essais cliniques (noms d’essais : développement honnête)
a('SALTIRE',[('SALTIRE','nom d’essai arrangé à partir de « Scottish Aortic stenosis and Lipid lowering Trial, Impact on REgression », non strictement lettre à lettre')],'Essai SALTIRE (2005)',
 '<p>Atorvastatine 80 mg contre placebo dans le RA calcifié : pas de ralentissement de la progression.</p>','i35-d-statine')
a('SEAS',[('S','Simvastatin'),('E','and Ezetimibe in'),('A','Aortic'),('S','Stenosis')],'Essai SEAS (2008)',
 '<p>Simvastatine et ézétimibe dans le RA léger à modéré : pas d’effet sur les événements valvulaires, réduction des événements ischémiques.</p>','i35-d-statine')
a('ASTRONOMER',[('ASTRONOMER','nom d’essai arrangé à partir de « Aortic Stenosis Progression Observation: Measuring Effects of Rosuvastatin », non strictement lettre à lettre')],'Essai ASTRONOMER (2010)',
 '<p>Rosuvastatine 40 mg dans le RA léger à modéré : pas de ralentissement de la progression.</p>','i35-d-statine')
a('EARLY TAVR',[('EARLY','précoce'),('T','Transcatheter'),('A','Aortic'),('V','Valve'),('R','Replacement')],'Essai EARLY TAVR (2024)',
 '<p>TAVI précoce contre surveillance clinique chez 901 patients porteurs d’un RA sévère asymptomatique : moins de décès, d’AVC ou d’hospitalisations cardiovasculaires non programmées, sans différence de mortalité.</p>','i35-early')
a('AVATAR',[('AVATAR','nom d’essai arrangé à partir de « Aortic Valve replAcemenT versus conservative treatment in Asymptomatic seveRe aortic stenosis », non strictement lettre à lettre')],'Essai AVATAR (2022)',
 '<p>Chirurgie précoce contre traitement conservateur dans le RA sévère asymptomatique à épreuve d’effort normale : réduction du critère composite.</p>','i35-early')
a('RECOVERY',[('RECOVERY','nom d’essai arrangé à partir de « Randomized Comparison of Early Surgery versus Conventional Treatment in Very Severe Aortic Stenosis », non strictement lettre à lettre')],'Essai RECOVERY (2020)',
 '<p>Chirurgie précoce contre traitement conventionnel dans le RA très sévère asymptomatique : moins de décès opératoires ou cardiovasculaires.</p>','i35-early')
a('EVOLVED',[('EVOLVED','nom d’essai arrangé à partir de « Early Valve Replacement Guided by Biomarkers of Left Ventricular Decompensation in Asymptomatic Patients With Severe Aortic Stenosis », non strictement lettre à lettre')],'Essai EVOLVED (2024)',
 '<p>Intervention précoce chez des patients porteurs d’un RA sévère asymptomatique avec fibrose myocardique à l’IRM : pas de réduction significative du critère principal.</p>','i35-early')
a('PARTNER',[('PARTNER','nom d’essai arrangé à partir de « Placement of AoRTic TraNscathetER Valves » (mise en place de valves aortiques par cathéter), non strictement lettre à lettre')],'Programme d’essais PARTNER (Placement of AoRTic TraNscathetER Valves)',
 '<p>Essais du TAVI par valve expansible par ballonnet. Cohorte B (2010) : chez les patients inopérables, mortalité à un an d’environ 50 % sous traitement médical contre environ 30 % après TAVI.</p>','i35-tavi')
a('PARTNER 3',[('PARTNER','Placement of AoRTic TraNscathetER Valves'),('3','troisième essai')],'Essai PARTNER 3 (2019)',
 '<p>TAVI contre chirurgie chez des patients à faible risque opératoire : TAVI supérieur pour le critère composite décès, AVC ou réhospitalisation à un an ; différence atténuée au suivi à cinq ans.</p>','i35-tavi')
a('Evolut Low Risk',[('Evolut','nom commercial de la valve auto-expansible évaluée'),('Low Risk','faible risque opératoire')],'Essai Evolut Low Risk (2019)',
 '<p>TAVI par valve auto-expansible contre chirurgie chez des patients à faible risque : non-infériorité.</p>','i35-tavi')
a('NOTION',[('NOTION','nom d’essai arrangé à partir de « NOrdic aorTIc valve interventiON » (intervention valvulaire aortique nordique), non strictement lettre à lettre')],'Essai NOTION (Nordic Aortic Valve Intervention)',
 '<p>Premier essai randomisé TAVI contre chirurgie chez des patients à faible risque ; suivi à dix ans sans différence de défaillance des bioprothèses.</p>','i35-tavi')
a('NOTION-2',[('NOTION','Nordic Aortic Valve Intervention'),('2','deuxième essai')],'Essai NOTION-2 (2024)',
 '<p>TAVI contre chirurgie chez des patients de 75 ans ou moins à faible risque, incluant des valves bicuspides : résultats comparables pour la valve tricuspide, signal défavorable au TAVI dans la bicuspidie.</p>','i35-tavi')
a('NOTION-3',[('NOTION','Nordic Aortic Valve Intervention'),('3','troisième essai')],'Essai NOTION-3 (2024)',
 '<p>Chez des patients candidats au TAVI avec une maladie coronaire fonctionnellement significative, l’angioplastie a réduit les événements cardiovasculaires majeurs par rapport au traitement conservateur.</p>','i35-coro')
a('DEDICATE',[('DEDICATE','nom d’essai non développé par ses auteurs ; le suffixe DZHK6 désigne le sixième essai du Deutsches Zentrum für Herz-Kreislauf-Forschung (Centre allemand de recherche cardiovasculaire)')],'Essai DEDICATE (2024)',
 '<p>Essai allemand : TAVI non inférieur à la chirurgie pour décès ou AVC à un an chez des patients de 65 ans et plus à risque faible ou intermédiaire (âge moyen 74 ans).</p>','i35-tavi')
a('GALILEO',[('GALILEO','nom d’essai arrangé à partir de « Global study comparing a rivAroxaban-based antithrombotic strategy to an antipLatelet-based strategy after TAVR to optimIze clinical outcomEs », non strictement lettre à lettre')],'Essai GALILEO (2020)',
 '<p>Rivaroxaban systématique après TAVI sans indication d’anticoagulation : plus de décès et d’hémorragies que la stratégie antiplaquettaire.</p>','i35-halt')
a('ATLANTIS',[('ATLANTIS','nom d’essai arrangé à partir de « Anti-Thrombotic strategy to Lower all cardiovascular and Neurologic ischemic and hemorrhagic events after Trans-aortic valve Implantation for aortic Stenosis », non strictement lettre à lettre')],'Essai ATLANTIS (2022)',
 '<p>Apixaban contre traitement standard après TAVI : pas de bénéfice clinique global.</p>','i35-halt')
a('POPular TAVI',[('POPular','nom d’essai arrangé à partir de « antiPlatelet therapy fOr Patients undergoing … », non strictement lettre à lettre'),('TAVI','Transcatheter Aortic Valve Implantation')],'Essai POPular TAVI (antiPlatelet therapy fOr Patients undergoing Transcatheter Aortic Valve Implantation, 2020)',
 '<p>Cohorte A : aspirine seule contre aspirine et clopidogrel après TAVI, moins d’hémorragies. Cohorte B : anticoagulant seul contre anticoagulant et clopidogrel, moins d’hémorragies.</p>','i35-d-asa')
a('PROACT Xa',[('PROACT','Prospective Randomized On-X Anticoagulation Clinical Trial'),('Xa','facteur X activé (apixaban)')],'Essai PROACT Xa (2023)',
 '<p>Apixaban contre warfarine chez des porteurs de prothèse aortique mécanique On-X : arrêt prématuré pour excès d’événements thromboemboliques sous apixaban.</p>','i35-inr')
a('COMPARE',[('COMPARE','nom d’essai arrangé à partir de « COzaar in Marfan PAtients Reduces aortic Enlargement », non strictement lettre à lettre')],'Essai COMPARE (2013)',
 '<p>Losartan ajouté au traitement habituel chez l’adulte atteint d’un syndrome de Marfan : ralentissement de la dilatation aortique.</p>','i35-d-aorte')
a('On-X',[('On-X','nom commercial d’une prothèse mécanique à double ailette en carbone pyrolytique ; non développable')],'Prothèse mécanique On-X',
 '<p>Prothèse à double ailette de faible thrombogénicité. L’ACC/AHA 2020 admet pour elle un INR de 1,5 à 2,0 en position aortique après trois mois ; l’apixaban y a échoué (PROACT Xa).</p>','i35-inr')
