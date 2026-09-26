# Glossaire MEDINA — chapitre I10 Hypertension artérielle
from cardio_1 import a, G

# Sociétés, classifications, scores
a('ESH',[('E','European (européenne)'),('S','Society of (Société d’)'),('H','Hypertension')],'European Society of Hypertension (Société européenne d’hypertension)',
 '<p>Société savante européenne ; ses recommandations 2023 conservent la classification en grades et les bêtabloquants en première ligne. Des auteurs suisses en ont coordonné la rédaction.</p>')
a('KDIGO',[('K','Kidney (rein)'),('D','Disease (maladie) :'),('I','Improving (améliorer les)'),('G','Global (globaux)'),('O','Outcomes (résultats)')],'Kidney Disease: Improving Global Outcomes',
 '<p>Fondation internationale qui publie les recommandations de néphrologie, dont la classification de la maladie rénale chronique selon le débit de filtration (G1 à G5) et l’albuminurie (A1 à A3).</p>')
a('ISSHP',[('I','International'),('S','Society for the'),('S','Study of'),('H','Hypertension in'),('P','Pregnancy')],'Société internationale pour l’étude de l’hypertension de la grossesse',
 '<p>Auteur de la définition actuelle de la prééclampsie (2018, mise à jour 2021).</p>','i10-preec')
a('SCORE2',[('S','Systematic (systématique)'),('CO','COronary (coronaire)'),('R','Risk (du risque)'),('E','Evaluation (évaluation)'),('2','deuxième version, 2021')],'Score européen du risque cardiovasculaire à dix ans (40 à 69 ans)',
 '<p>Estime le risque à dix ans d’événement cardiovasculaire mortel ou non mortel à partir de l’âge, du sexe, du tabagisme, de la pression systolique et du cholestérol non HDL, selon la région de risque. La Suisse est une région à faible risque.</p>','i10-score2')
a('SCORE2-OP',[('SCORE2','Systematic COronary Risk Evaluation 2'),('OP','Older Persons (personnes âgées de 70 ans et plus)')],'Version de SCORE2 pour les personnes de 70 ans et plus',
 '<p>Tient compte du risque concurrent de décès non cardiovasculaire.</p>','i10-score2')
a('SCORE2-Diabetes',[('SCORE2','Systematic COronary Risk Evaluation 2'),('Diabetes','version pour le diabète de type 2')],'Version de SCORE2 pour le diabétique de type 2',
 '<p>Ajoute l’âge au diagnostic du diabète, l’HbA1c et le débit de filtration.</p>','i10-score2')
a('STOP-BANG',[('S','Snoring : ronflement'),('T','Tiredness : fatigue diurne'),('O','Observed apnea : apnées observées'),('P','Pressure : hypertension'),('B','BMI : indice de masse corporelle > 35'),('A','Age : âge > 50 ans'),('N','Neck : tour de cou élevé'),('G','Gender : sexe masculin')],'Questionnaire de dépistage des apnées obstructives du sommeil',
 '<p>Un point par item ; un score ≥ 3 indique un risque intermédiaire à élevé et justifie une polygraphie ventilatoire.</p>','i10-saos')
a('ABCDE',[('A','Accuracy, Apnea, Aldosteronism'),('B','Bruits, Bad kidneys'),('C','Catecholamines, Coarctation, Cushing'),('D','Drugs, Diet'),('E','Erythropoietin, Endocrine')],'Aide-mémoire des causes d’hypertension secondaire',
 '<p>Aide pédagogique, non critère officiel.</p>','i10-mnemo-abcde')
a('MAPA',[('M','Mesure'),('A','Ambulatoire de la'),('P','Pression'),('A','Artérielle')],'Mesure ambulatoire de la pression artérielle sur 24 heures',
 '<p>Référence diagnostique de l’hypertension ; seuils : 24 heures ≥ 130/80, jour ≥ 135/85, nuit ≥ 120/70 mmHg.</p>','i10-mapa')
a('A1',[('A','catégorie d’Albuminurie'),('1','1 : normale à légèrement augmentée')],'Albuminurie de catégorie A1 (KDIGO)','<p>Rapport albumine/créatinine &lt; 3 mg/mmol.</p>','i10-alb')
a('A2',[('A','catégorie d’Albuminurie'),('2','2 : modérément augmentée')],'Albuminurie de catégorie A2 (KDIGO)','<p>Rapport albumine/créatinine de 3 à 30 mg/mmol.</p>','i10-alb')
a('A3',[('A','catégorie d’Albuminurie'),('3','3 : sévèrement augmentée')],'Albuminurie de catégorie A3 (KDIGO)','<p>Rapport albumine/créatinine &gt; 30 mg/mmol.</p>','i10-alb')

# Biologie, physiologie, imagerie
a('ACTH',[('A','Adréno-'),('C','Cortico-'),('T','Trophique'),('H','Hormone')],'Hormone adrénocorticotrope (corticotrophine)',
 '<p>Hormone hypophysaire qui stimule la sécrétion de cortisol par la zone fasciculée. Basse dans le Cushing surrénalien, normale ou haute dans le Cushing hypophysaire ou ectopique.</p>','i10-cushing')
a('HDL',[('H','High (haute)'),('D','Density (densité)'),('L','Lipoprotein (lipoprotéine)')],'Lipoprotéine de haute densité',
 '<p>Le cholestérol « non HDL » (cholestérol total moins cholestérol HDL) regroupe les lipoprotéines athérogènes ; il est utilisé dans SCORE2.</p>')
a('LDL',[('L','Low (basse)'),('D','Density (densité)'),('L','Lipoprotein (lipoprotéine)')],'Lipoprotéine de basse densité','<p>Principale lipoprotéine athérogène ; sa cible dépend du risque cardiovasculaire.</p>')
a('ENaC',[('E','Epithelial (épithélial)'),('Na','canal sodique (Natrium)'),('C','Channel (canal)')],'Canal sodique épithélial',
 '<p>Canal de la membrane apicale des cellules principales du tube collecteur ; activé par l’aldostérone, bloqué par l’amiloride ; suractif dans le syndrome de Liddle.</p>','i10-d-amil')
a('NCC',[('N','Na (sodium)'),('C','Cl (chlorure)'),('C','Cotransporteur')],'Cotransporteur sodium-chlorure du tube contourné distal',
 '<p>Cible des diurétiques thiazidiques ; suractivé dans le syndrome de Gordon.</p>','i10-d-thz')
a('AT2',[('AT','récepteur de l’AngioTensine II'),('2','de type 2')],'Récepteur de type 2 de l’angiotensine II',
 '<p>Effets globalement opposés au récepteur AT1 (vasodilatation, antiprolifération) ; stimulé par l’angiotensine II en excès sous ARA II.</p>')
a('DOPA',[('D','Di-'),('O','hydrOxy-'),('P','Phényl-'),('A','Alanine')],'Dihydroxyphénylalanine',
 '<p>Précurseur des catécholamines, produit à partir de la tyrosine par la tyrosine hydroxylase.</p>')
a('sFlt-1',[('s','soluble'),('Flt','Fms-Like Tyrosine kinase (récepteur de type tyrosine kinase apparenté à Fms)'),('1','1 : récepteur 1 du VEGF')],'Récepteur soluble 1 du facteur de croissance de l’endothélium vasculaire',
 '<p>Facteur antiangiogénique libéré en excès par le placenta ischémique dans la prééclampsie ; il capte le VEGF et le PlGF.</p>','i10-sflt')
a('PlGF',[('Pl','Placental (placentaire)'),('G','Growth (de croissance)'),('F','Factor (facteur)')],'Facteur de croissance placentaire',
 '<p>Facteur proangiogénique abaissé dans la prééclampsie ; le rapport sFlt-1/PlGF aide au diagnostic.</p>','i10-sflt')
a('VEGF',[('V','Vascular (vasculaire)'),('E','Endothelial (endothélial)'),('G','Growth (de croissance)'),('F','Factor (facteur)')],'Facteur de croissance de l’endothélium vasculaire',
 '<p>Les antiangiogéniques anti-VEGF (bévacizumab, sunitinib) provoquent fréquemment une hypertension et une protéinurie.</p>')
a('HELLP',[('H','Hemolysis (hémolyse)'),('EL','Elevated Liver enzymes (enzymes hépatiques élevées)'),('LP','Low Platelets (plaquettes basses)')],'Syndrome associant hémolyse, cytolyse hépatique et thrombopénie',
 '<p>Forme grave de prééclampsie ; urgence obstétricale.</p>','i10-hellp')
a('PRES',[('P','Posterior (postérieure)'),('R','Reversible (réversible)'),('E','Encephalopathy (encéphalopathie)'),('S','Syndrome')],'Syndrome d’encéphalopathie postérieure réversible',
 '<p>Œdème vasogénique à prédominance pariéto-occipitale : hypertension sévère, éclampsie, immunosuppresseurs.</p>','i10-pres')
a('FLAIR',[('FL','FLuid (liquide)'),('A','Attenuated (atténué)'),('I','Inversion'),('R','Recovery (récupération)')],'Séquence d’IRM en inversion-récupération à liquide atténué',
 '<p>Séquence pondérée en T2 où le signal du liquide cérébrospinal est supprimé ; elle montre bien l’œdème et les lésions de la substance blanche.</p>')
a('mTOR',[('m','mechanistic (mécanistique ; autrefois « mammalian », des mammifères)'),('T','Target (cible)'),('O','Of (de la)'),('R','Rapamycin (rapamycine)')],'Cible mécanistique (autrefois « mammalian », des mammifères) de la rapamycine','<p>Kinase inhibée par l’évérolimus et le sirolimus ; associés à un IEC, ces inhibiteurs augmentent le risque d’angiœdème.</p>')
a('DI',[('D','Dérivation'),('I','I (première dérivation bipolaire des membres)')],'Dérivation I de l’ECG','<p>Enregistre la différence de potentiel entre le bras gauche et le bras droit.</p>')
a('aVL',[('a','augmented (augmentée)'),('V','Voltage (dérivation unipolaire de Wilson)'),('L','Left (bras gauche)')],'Dérivation unipolaire augmentée du bras gauche','<p>Explore la paroi latérale haute ; une onde R ≥ 11 mm y est un critère d’hypertrophie ventriculaire gauche.</p>')
a('V3',[('V','Voltage (dérivation unipolaire de Wilson)'),('3','précordiale 3 : à mi-distance des électrodes précordiales 2 et 4')],'Dérivation précordiale V3','<p>Utilisée dans l’indice de Cornell (onde S en V3).</p>')
a('V5',[('V','Voltage (dérivation unipolaire de Wilson)'),('5','précordiale 5 : ligne axillaire antérieure, 5e espace intercostal')],'Dérivation précordiale V5','<p>Utilisée dans l’indice de Sokolow et Lyon.</p>')
a('V6',[('V','Voltage (dérivation unipolaire de Wilson)'),('6','précordiale 6 : ligne axillaire moyenne, 5e espace intercostal')],'Dérivation précordiale V6','<p>Utilisée dans l’indice de Sokolow et Lyon.</p>')
a('V1',[('V','Voltage (dérivation unipolaire de Wilson)'),('1','précordiale 1 : 4e espace intercostal, bord droit du sternum')],'Dérivation précordiale V1','<p>Onde S en V1 : premier terme de l’indice de Sokolow et Lyon.</p>')
a('QU',[('Q','début de l’onde Q'),('U','fin de l’onde U')],'Intervalle QU de l’ECG','<p>Mesuré à la place du QT quand une onde U fusionne avec l’onde T, notamment dans l’hypokaliémie.</p>')

# Gènes
a('SCNN1B',[('S','Sodium'),('C','Channel (canal)'),('NN','Non-voltage-gated (non voltage-dépendant)'),('1','type 1'),('B','sous-unité Bêta')],'Gène de la sous-unité β du canal sodique épithélial','<p>Variants activateurs : syndrome de Liddle.</p>','i10-mono')
a('SCNN1G',[('S','Sodium'),('C','Channel (canal)'),('NN','Non-voltage-gated (non voltage-dépendant)'),('1','type 1'),('G','sous-unité Gamma')],'Gène de la sous-unité γ du canal sodique épithélial','<p>Variants activateurs : syndrome de Liddle.</p>','i10-mono')
a('CYP11B1',[('CYP','CYtochrome P450'),('11','famille 11'),('B','sous-famille B'),('1','membre 1 : 11β-hydroxylase')],'Gène de la 11β-hydroxylase','<p>Synthèse du cortisol dans la zone fasciculée ; son déficit donne une hyperplasie congénitale des surrénales avec hypertension.</p>','i10-mono')
a('CYP11B2',[('CYP','CYtochrome P450'),('11','famille 11'),('B','sous-famille B'),('2','membre 2 : aldostérone synthase')],'Gène de l’aldostérone synthase','<p>Exprimé dans la zone glomérulée ; le gène chimère avec <i>CYP11B1</i> cause l’hyperaldostéronisme familial de type 1.</p>','i10-mono')
a('KCNJ5',[('KCN','famille des canaux potassiques (K⁺ ChaNnel)'),('J','sous-famille J : canaux à rectification entrante'),('5','membre 5')],'Gène d’un canal potassique à rectification entrante de la zone glomérulée','<p>Mutations somatiques dans de nombreux adénomes de Conn ; mutations germinales dans l’hyperaldostéronisme familial de type 3.</p>','i10-mono')
a('WNK1',[('W','With (avec)'),('N','No (aucune)'),('K','K : lysine, code à une lettre'),('1','membre 1')],'Gène de la kinase WNK1 (kinase sans lysine catalytique classique)','<p>Régule le cotransporteur NCC ; variants responsables du syndrome de Gordon.</p>','i10-mono')
a('WNK4',[('W','With (avec)'),('N','No (aucune)'),('K','K : lysine, code à une lettre'),('4','membre 4')],'Gène de la kinase WNK4 (kinase sans lysine catalytique classique)','<p>Régule le cotransporteur NCC ; variants responsables du syndrome de Gordon.</p>','i10-mono')
a('KLHL3',[('KLHL','KeLcH-Like (apparentée à la protéine Kelch)'),('3','membre 3')],'Gène de la protéine KLHL3 (famille apparentée à Kelch)','<p>Adaptateur de la dégradation des kinases WNK ; variants : syndrome de Gordon.</p>','i10-mono')
a('CUL3',[('CUL','CULline'),('3','3')],'Gène de la culline 3','<p>Ubiquitine ligase qui dégrade les kinases WNK ; variants : forme sévère du syndrome de Gordon.</p>','i10-mono')
a('HSD11B2',[('HSD','Hydroxy-Stéroïde Déshydrogénase'),('11B','11-Bêta'),('2','type 2')],'Gène de la 11β-hydroxystéroïde déshydrogénase de type 2','<p>Déficit : excès apparent de minéralocorticoïdes ; l’enzyme est inhibée par la réglisse.</p>','i10-pseudo')
a('SDHB',[('S','Succinate'),('DH','DésHydrogénase'),('B','sous-unité B')],'Gène de la sous-unité B de la succinate déshydrogénase','<p>Variants germinaux : paragangliomes à risque métastatique élevé.</p>','i10-pheo')
a('VHL',[('V','Von'),('H','Hippel'),('L','Lindau')],'Gène de la maladie de von Hippel et Lindau','<p>Gène suppresseur de tumeur ; phéochromocytomes, hémangioblastomes, cancers rénaux à cellules claires.</p>','i10-pheo')
a('RET',[('RE','REarranged (réarrangé)'),('T','during Transfection (pendant la transfection)')],'Proto-oncogène RET','<p>Variants activateurs : néoplasie endocrinienne multiple de type 2 (carcinome médullaire de la thyroïde, phéochromocytome, hyperparathyroïdie).</p>','i10-pheo')
a('NF1',[('N','Neuro-'),('F','Fibromine'),('1','1')],'Gène de la neurofibromine 1','<p>Neurofibromatose de type 1 : taches café au lait, neurofibromes, phéochromocytome, sténose de l’artère rénale.</p>','i10-pheo')
a('APOL1',[('APO','APOlipoprotéine'),('L','L'),('1','1')],'Gène de l’apolipoprotéine L1','<p>Deux variants fréquents chez les personnes d’ascendance ouest-africaine augmentent le risque de néphropathie, souvent attribuée à tort à l’hypertension.</p>','i10-nephroangio')

# Essais
def t(k, lit, full, d, ref=None):
    a(k, lit, full, d, ref)
t('SPRINT',[('S','Systolic (systolique)'),('PR','blood PRessure (pression artérielle)'),('IN','INtervention'),('T','Trial (essai)')],'Essai SPRINT (2015)',
 '<p>Systolic Blood Pressure Intervention Trial : cible &lt; 120 contre &lt; 140 mmHg chez des non-diabétiques à haut risque ; réduction d’environ 25 % du critère cardiovasculaire principal et de la mortalité, au prix de plus d’hypotensions et d’insuffisances rénales aiguës. Mesure automatisée sans surveillance.</p>')
t('STEP',[('ST','STrategy of blood pressure intervention in the'),('E','Elderly hypertensive'),('P','Patients')],'Essai STEP (2021)',
 '<p>Patients chinois de 60 à 80 ans : cible systolique de 110 à 130 contre 130 à 150 mmHg ; réduction d’environ un quart des événements cardiovasculaires.</p>')
t('ESPRIT',[('ESPRIT','acronyme arrangé de « Effects of intensive Systolic blood PRessure lowering treatment in reducing RIsk of vascular evenTs », non strictement lettre à lettre')],'Essai ESPRIT (2024)',
 '<p>Patients chinois à haut risque, diabétiques inclus : cible &lt; 120 contre &lt; 140 mmHg ; réduction des événements vasculaires majeurs.</p>')
t('PATHWAY-2',[('PATHWAY','Prevention And Treatment of Hypertension With Algorithm-based therapY'),('2','deuxième essai du programme')],'Essai PATHWAY-2 (2015)',
 '<p>Hypertension résistante : la spironolactone est plus efficace que le bisoprolol, la doxazosine et le placebo.</p>','i10-d-spiro')
t('ACCOMPLISH',[('ACCOMPLISH','acronyme arrangé de « Avoiding Cardiovascular events through COMbination therapy in Patients LIving with Systolic Hypertension », non strictement lettre à lettre')],'Essai ACCOMPLISH (2008)',
 '<p>Bénazépril + amlodipine contre bénazépril + hydrochlorothiazide : réduction d’environ 20 % des événements cardiovasculaires avec l’association à l’inhibiteur calcique.</p>','i10-d-icc')
t('ALLHAT',[('A','Antihypertensive (antihypertenseur)'),('L','and Lipid-'),('L','Lowering treatment'),('H','to prevent Heart'),('A','Attack'),('T','Trial')],'Essai ALLHAT (2002)',
 '<p>Chlortalidone, amlodipine et lisinopril équivalents sur le critère coronaire ; chlortalidone supérieure sur l’insuffisance cardiaque ; bras doxazosine interrompu (excès d’insuffisance cardiaque).</p>','i10-d-thz')
t('HYVET',[('HY','HYpertension in the'),('V','Very'),('E','Elderly'),('T','Trial')],'Essai HYVET (2008)',
 '<p>Patients de 80 ans et plus : indapamide ± périndopril, cible 150/80 mmHg ; réduction de la mortalité totale et de l’insuffisance cardiaque.</p>')
t('ONTARGET',[('ON','ONgoing'),('T','Telmisartan'),('A','Alone and in combination with'),('R','Ramipril'),('G','Global'),('E','Endpoint'),('T','Trial')],'Essai ONTARGET (2008)',
 '<p>Telmisartan non inférieur au ramipril ; l’association des deux augmente les insuffisances rénales, l’hyperkaliémie et l’hypotension sans bénéfice.</p>')
t('ASTRAL',[('A','Angioplasty (angioplastie)'),('ST','and STenting'),('R','for Renal'),('A','Artery'),('L','Lesions')],'Essai ASTRAL (2009)',
 '<p>Sténose athéromateuse de l’artère rénale : pas de bénéfice de la revascularisation sur la fonction rénale ni sur les événements.</p>','i10-sar')
t('CORAL',[('C','Cardiovascular'),('O','Outcomes in'),('R','Renal'),('A','Atherosclerotic'),('L','Lesions')],'Essai CORAL (2014)',
 '<p>Stent contre traitement médical optimal dans la sténose athéromateuse de l’artère rénale : pas de réduction des événements.</p>','i10-sar')
t('CLICK',[('CL','CLorthalidone'),('I','In'),('C','Chronic'),('K','Kidney disease')],'Essai CLICK (2021)',
 '<p>Chlortalidone dans la maladie rénale chronique de stade 4 : baisse de la systolique ambulatoire d’environ 10 mmHg par rapport au placebo.</p>','i10-d-thz')
t('CHAP',[('C','Chronic'),('H','Hypertension'),('A','And'),('P','Pregnancy')],'Essai CHAP (2022)',
 '<p>Hypertension chronique légère de la grossesse : traiter jusqu’à &lt; 140/90 mmHg réduit les complications sans altérer la croissance fœtale.</p>')
t('ASPRE',[('AS','ASpirin for evidence-based'),('PRE','PREeclampsia prevention')],'Essai ASPRE (2017)',
 '<p>Acide acétylsalicylique 150 mg le soir de 11–14 à 36 semaines chez les femmes à risque : réduction de 62 % de la prééclampsie avant 37 semaines.</p>','i10-asp')
t('PROGNOSIS',[('PROGNOSIS','acronyme arrangé de « PRediction of short-term Outcome in preGNant wOmen with Suspected preeclampsIa Study », non strictement lettre à lettre')],'Étude PROGNOSIS (2016)',
 '<p>Validation du seuil 38 du rapport sFlt-1/PlGF pour exclure une prééclampsie dans la semaine suivante.</p>','i10-sflt')
t('DASH',[('D','Dietary (diététiques)'),('A','Approaches (approches)'),('S','to Stop (pour arrêter l’)'),('H','Hypertension')],'Régime et essai DASH (1997)',
 '<p>Alimentation riche en fruits, légumes et produits laitiers maigres : baisse d’environ 11 mmHg de la systolique chez les hypertendus.</p>','i10-dash')
t('DASH-Sodium',[('DASH','Dietary Approaches to Stop Hypertension'),('Sodium','avec trois niveaux d’apport sodé')],'Essai DASH-Sodium (2001)',
 '<p>Les effets du régime DASH et de la réduction du sel s’additionnent.</p>','i10-dash')
t('SSaSS',[('S','Salt (sel)'),('S','Substitute (de substitution)'),('a','and (et)'),('S','Stroke (accident vasculaire cérébral)'),('S','Study (étude)')],'Essai SSaSS (2021)',
 '<p>Villages chinois : un sel enrichi en potassium réduit les accidents vasculaires cérébraux, les événements cardiovasculaires et la mortalité.</p>')
t('TIME',[('T','Treatment (traitement)'),('I','In (le)'),('M','Morning (matin)'),('E','versus Evening (contre le soir)')],'Essai TIME (2022)',
 '<p>Prise des antihypertenseurs le matin ou le soir : aucune différence sur les événements cardiovasculaires.</p>')
t('SYMPLICITY HTN-3',[('SYMPLICITY','nom du système de dénervation rénale évalué, non acronyme'),('HTN','HyperTensioN'),('3','troisième essai')],'Essai SYMPLICITY HTN-3 (2014)',
 '<p>Premier essai de dénervation rénale contrôlé contre procédure simulée ; résultat négatif.</p>','i10-dnr')
t('SPYRAL HTN',[('SPYRAL','nom du cathéter de dénervation évalué, non acronyme'),('HTN','HyperTensioN')],'Programme d’essais SPYRAL HTN (2018–2022)',
 '<p>Dénervation par radiofréquence contre procédure simulée, chez des patients sans traitement (OFF MED) puis sous traitement (ON MED) : baisse tensionnelle modeste et durable.</p>','i10-dnr')
t('RADIANCE-HTN',[('RADIANCE','nom de programme d’essais, non acronyme'),('HTN','HyperTensioN')],'Essais RADIANCE-HTN (2018–2021)',
 '<p>Dénervation rénale par ultrasons contre procédure simulée, hypertension modérée (SOLO) ou résistante (TRIO).</p>','i10-dnr')
t('RADIANCE',[('RADIANCE','nom de programme d’essais de dénervation rénale par ultrasons, non acronyme')],'Programme d’essais RADIANCE',
 '<p>Essais RADIANCE-HTN et RADIANCE II (2023) : baisse de la pression ambulatoire diurne supérieure à la procédure simulée.</p>','i10-dnr')
t('PROGRESS',[('PROGRESS','acronyme arrangé de « Perindopril pROtection aGainst REcurrent Stroke Study », non strictement lettre à lettre')],'Essai PROGRESS (2001)',
 '<p>Après un accident vasculaire cérébral : périndopril ± indapamide réduit la récidive, y compris chez les normotendus.</p>')
t('HOPE',[('H','Heart'),('O','Outcomes'),('P','Prevention'),('E','Evaluation')],'Essai HOPE (2000)',
 '<p>Ramipril chez des patients à haut risque vasculaire : réduction des infarctus, accidents vasculaires cérébraux et décès cardiovasculaires.</p>')
t('EUROPA',[('EU','EUropean trial on'),('R','Reduction'),('O','Of cardiac events with'),('P','Perindopril in stable coronary'),('A','Artery disease')],'Essai EUROPA (2003)',
 '<p>Périndopril chez le coronarien stable : réduction des événements cardiovasculaires.</p>')
t('LIFE',[('L','Losartan'),('I','Intervention'),('F','For'),('E','Endpoint reduction in hypertension')],'Essai LIFE (2002)',
 '<p>Hypertendus avec hypertrophie ventriculaire : losartan supérieur à l’aténolol, surtout sur les accidents vasculaires cérébraux.</p>','i10-d-ara')
t('IDNT',[('I','Irbesartan'),('D','Diabetic'),('N','Nephropathy'),('T','Trial')],'Essai IDNT (2001)',
 '<p>Irbésartan dans la néphropathie diabétique de type 2 : ralentissement de la progression rénale.</p>','i10-d-ara')
t('RENAAL',[('RENAAL','acronyme arrangé de « Reduction of Endpoints in NIDDM with the Angiotensin II Antagonist Losartan », non strictement lettre à lettre')],'Essai RENAAL (2001)',
 '<p>Losartan dans la néphropathie diabétique de type 2 : ralentissement de la progression rénale.</p>','i10-d-ara')
t('Syst-Eur',[('Syst','SYSTolic hypertension (hypertension systolique)'),('Eur','in EURope (en Europe)')],'Essai Syst-Eur (1997)',
 '<p>Nitrendipine dans l’hypertension systolique isolée du sujet âgé : réduction des accidents vasculaires cérébraux.</p>','i10-d-icc')
t('ASCOT-BPLA',[('A','Anglo-'),('S','Scandinavian'),('C','Cardiac'),('O','Outcomes'),('T','Trial'),('BP','Blood Pressure'),('L','Lowering'),('A','Arm')],'Essai ASCOT-BPLA (2005)',
 '<p>Amlodipine ± périndopril supérieurs à aténolol ± thiazidique sur les accidents vasculaires cérébraux et la mortalité.</p>','i10-d-icc')
t('MOXCON',[('MOX','MOXonidine'),('CON','CONgestive heart failure')],'Essai MOXCON (2003)',
 '<p>Moxonidine dans l’insuffisance cardiaque : surmortalité, essai interrompu.</p>','i10-d-alpha')

# Institutions suisses
a('FMH',[('F','Foederatio (fédération)'),('M','Medicorum (des médecins)'),('H','Helveticorum (suisses)')],'Fédération des médecins suisses',
 '<p>Organisation faîtière du corps médical suisse ; elle héberge la plateforme « Guidelines Schweiz », qui recense les recommandations reprises en Suisse.</p>')
a('mediX',[('mediX','nom propre d’un réseau suisse de médecins de famille, non acronyme')],'Réseau de médecins de famille mediX',
 '<p>Réseau suisse qui publie des recommandations de pratique pour la médecine de premier recours ; sa recommandation « Hypertonie » (révisée en 2024, mise à jour en 2025) s’appuie sur l’ESC 2024.</p>')
