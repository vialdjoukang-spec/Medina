# Glossaire MEDINA — chapitre I21 (syndromes coronariens aigus et infarctus)
from cardio_1 import a, G

def t(k, lit, full, d, ref=None):
    a(k, lit, full, d, ref)

# --- syndromes et concepts ---
a('SCA',[('S','Syndrome'),('C','Coronarien'),('A','Aigu')],'Syndrome coronarien aigu',
 '<p>Ensemble des présentations causées par une réduction brutale du flux coronaire : STEMI, NSTEMI et angor instable. L’ESC 2023 les traite comme un spectre.</p>')
a('STEMI',[('ST','segment ST'),('E','Elevation (sus-décalage)'),('M','Myocardial (du myocarde)'),('I','Infarction (infarctus)')],'Infarctus du myocarde avec sus-décalage du segment ST',
 '<p>Sus-décalage persistant du ST (ou équivalent d’occlusion) avec symptômes ischémiques : reperfusion immédiate.</p>','i21-omi')
a('NSTEMI',[('N','Non'),('ST','segment ST'),('E','Elevation (sus-décalage)'),('M','Myocardial (du myocarde)'),('I','Infarction (infarctus)')],'Infarctus du myocarde sans sus-décalage du segment ST',
 '<p>Troponine qui monte et/ou descend au-dessus du 99e percentile dans un contexte ischémique, sans sus-décalage persistant.</p>')
a('NSTE-ACS',[('N','Non'),('ST','segment ST'),('E','Elevation (sus-décalage)'),('A','Acute (aigu)'),('C','Coronary (coronarien)'),('S','Syndrome')],'Syndrome coronarien aigu sans sus-décalage persistant du segment ST',
 '<p>Terme ESC regroupant le NSTEMI et l’angor instable ; la prise en charge repose sur la stratification du risque.</p>')
a('OMI',[('O','Occlusion'),('M','Myocardial (du myocarde)'),('I','Infarction (infarctus)')],'Infarctus occlusif du myocarde',
 '<p>Infarctus par occlusion coronaire aiguë, avec ou sans sus-décalage classique, qui justifie une reperfusion immédiate.</p>','i21-omi')
a('MINOCA',[('M','Myocardial (myocardique)'),('I','Infarction, puis Injury (lésion) depuis 2026'),('N','with Non-'),('O','Obstructive'),('C','Coronary'),('A','Arteries')],'Infarctus (lésion depuis 2026) à coronaires non obstructives',
 '<p>Critères d’infarctus sans sténose coronaire ≥ 50 % : diagnostic de travail qui impose de chercher la cause, notamment par IRM.</p>','i21-minoca')
a('SCAD',[('S','Spontaneous (spontanée)'),('C','Coronary (coronaire)'),('A','Artery (artère)'),('D','Dissection')],'Dissection coronaire spontanée',
 '<p>Hématome intramural ou déchirure intimale non athéromateuse ; femme jeune, péripartum, dysplasie fibromusculaire.</p>','i21-scad')
a('DAPT',[('D','Dual (double)'),('A','Anti'),('P','Platelet (plaquettaire)'),('T','Therapy (traitement)')],'Double antiagrégation plaquettaire',
 '<p>Association d’acide acétylsalicylique et d’un inhibiteur P2Y12 ; 12 mois par défaut après un SCA, modulée selon les risques ischémique et hémorragique.</p>','i21-dapt')
a('HNF',[('H','Héparine'),('N','Non'),('F','Fractionnée')],'Héparine non fractionnée',
 '<p>Anticoagulant parentéral de demi-vie courte, antagonisable par la protamine ; anticoagulant de référence de l’angioplastie primaire.</p>','i21-d-hep')
a('GRACE',[('G','Global'),('R','Registry of'),('A','Acute'),('C','Coronary'),('E','Events')],'Registre mondial des événements coronariens aigus (score GRACE)',
 '<p>Score pronostique à huit variables ; &gt; 140 = haut risque dans le NSTE-ACS.</p>','i21-grace')
a('ARC-HBR',[('A','Academic'),('R','Research'),('C','Consortium'),('H','High'),('B','Bleeding'),('R','Risk')],'Critères du consortium de recherche académique pour le haut risque hémorragique',
 '<p>Un critère majeur ou deux mineurs définissent un risque hémorragique élevé après angioplastie.</p>','i21-archbr')
a('TIMI',[('T','Thrombolysis'),('I','In'),('M','Myocardial'),('I','Infarction')],'Groupe d’études Thrombolysis In Myocardial Infarction',
 '<p>Groupe d’essais qui a donné son nom au grade de flux coronaire (0 à 3) et à plusieurs essais.</p>','i21-timi')
a('IVA',[('I','artère Inter'),('V','Ventriculaire'),('A','Antérieure')],'Artère interventriculaire antérieure',
 '<p>Branche du tronc commun gauche ; vascularise la paroi antérieure, les deux tiers antérieurs du septum et souvent l’apex.</p>','i21-sa-coro')
a('VPN',[('V','Valeur'),('P','Prédictive'),('N','Négative')],'Valeur prédictive négative','<p>Probabilité d’absence de la maladie lorsque le test est négatif.</p>')
a('VPP',[('V','Valeur'),('P','Prédictive'),('P','Positive')],'Valeur prédictive positive','<p>Probabilité de la maladie lorsque le test est positif.</p>')
a('mg/dL',[('mg','milligrammes'),('/dL','par décilitre')],'Milligrammes par décilitre','<p>Unité de concentration (1 dL = 100 mL) ; lipoprotéine(a) : seuil de risque 50 mg/dL.</p>')

# --- biologie, molécules, gènes ---
a('CK-MB',[('C','Créatine'),('K','Kinase'),('M','sous-unité Muscle'),('B','sous-unité Brain (cerveau)')],'Isoenzyme MB de la créatine kinase',
 '<p>Marqueur ancien de nécrose, normalisé en 48 à 72 heures ; sans indication diagnostique lorsque la troponine hypersensible est disponible.</p>')
a('ADP',[('A','Adénosine'),('D','Di-'),('P','Phosphate')],'Adénosine diphosphate',
 '<p>Médiateur libéré par les plaquettes activées ; agit sur le récepteur P2Y12, cible des thiénopyridines et du ticagrélor.</p>','i21-plaquette')
a('P2Y12',[('P2','récepteur Purinergique de type 2'),('Y','lettre conventionnelle de la sous-famille métabotropique couplée aux protéines G (sans développement)'),('12','sous-type 12')],'Récepteur plaquettaire P2Y12 de l’ADP',
 '<p>Récepteur couplé à une protéine Gi qui amplifie l’activation plaquettaire ; bloqué par le clopidogrel, le prasugrel, le ticagrélor et le cangrélor.</p>','i21-d-p2y12')
a('TXA₂',[('TX','ThromboXane'),('A₂','de type A2')],'Thromboxane A2',
 '<p>Prostanoïde plaquettaire vasoconstricteur et proagrégant, produit par la cyclo-oxygénase 1 ; sa synthèse est bloquée par l’acide acétylsalicylique.</p>','i21-d-asa')
a('GP IIb/IIIa',[('GP','GlycoProtéine'),('IIb/IIIa','intégrine αIIbβ3 (sous-unités IIb et IIIa)')],'Glycoprotéine IIb/IIIa plaquettaire',
 '<p>Récepteur du fibrinogène, voie finale de l’agrégation plaquettaire ; cible du tirofiban et de l’eptifibatide.</p>','i21-plaquette')
a('PCSK9',[('P','Proprotein (proprotéine)'),('C','Convertase'),('S','Subtilisin (subtilisine)'),('K','Kexin (kexine)'),('9','type 9')],'Proprotéine convertase subtilisine/kexine de type 9',
 '<p>Protéine hépatique qui entraîne la dégradation du récepteur des LDL ; cible des anticorps évolocumab et alirocumab et de l’inclisiran.</p>','i21-d-pcsk9')
a('CYP2C19',[('CYP','Cytochrome P450'),('2','famille 2'),('C','sous-famille C'),('19','isoenzyme 19')],'Isoenzyme 2C19 du cytochrome P450',
 '<p>Enzyme hépatique qui active le clopidogrel ; ses allèles perte de fonction réduisent l’effet antiagrégant. Inhibée par l’oméprazole et l’ésoméprazole.</p>')
a('LDL',[('L','Low (basse)'),('D','Density (densité)'),('L','Lipoprotein (lipoprotéine)')],'Lipoprotéine de basse densité',
 '<p>Principale lipoprotéine athérogène ; cible après un syndrome coronarien aigu : &lt; 1,4 mmol/L et baisse ≥ 50 %.</p>')
a('LDL-cholestérol',[('LDL','cholestérol transporté par les Lipoprotéines de basse Densité (Low Density Lipoprotein)')],'Cholestérol des lipoprotéines de basse densité',
 '<p>Cible thérapeutique principale de la prévention secondaire.</p>','i21-ldl')
a('LDLR',[('LDL','Low Density Lipoprotein (lipoprotéine de basse densité)'),('R','Receptor (récepteur)')],'Récepteur des LDL (gène et protéine)',
 '<p>Récepteur hépatique qui épure les LDL ; ses variants causent la majorité des hypercholestérolémies familiales.</p>','i21-hf')
a('APOB',[('APO','APOlipoprotéine'),('B','B')],'Gène de l’apolipoprotéine B',
 '<p>Code la protéine de structure des LDL ; certains variants réduisent sa liaison au récepteur et causent une hypercholestérolémie familiale.</p>','i21-hf')
a('LPA',[('LP','LiPoprotéine'),('A','(a)')],'Gène de l’apolipoprotéine(a)',
 '<p>Détermine à plus de 80 % le taux de lipoprotéine(a), via le nombre de répétitions du domaine kringle IV de type 2.</p>','i21-lpa')
a('HMG-CoA',[('H','3-Hydroxy-3-'),('M','Méthyl'),('G','Glutaryl'),('CoA','Coenzyme A')],'3-hydroxy-3-méthylglutaryl-coenzyme A',
 '<p>Substrat de l’HMG-CoA réductase, enzyme limitante de la synthèse du cholestérol inhibée par les statines.</p>','i21-d-statine')
a('NPC1L1',[('N','Niemann-'),('P','Pick'),('C1','type C1'),('L1','Like 1 (apparenté de type 1)')],'Transporteur intestinal Niemann-Pick C1-Like 1',
 '<p>Transporteur de l’absorption intestinale du cholestérol, bloqué par l’ézétimibe.</p>','i21-d-ezet')
a('NLRP3',[('NLR','NOD-Like Receptor (récepteur apparenté à NOD : Nucleotide-binding Oligomerization Domain)'),('P','Pyrin domain (domaine pyrine)'),('3','membre 3')],'Inflammasome NLRP3',
 '<p>Complexe intracellulaire qui active l’interleukine 1β ; son activation est réduite par la colchicine.</p>','i21-d-colch')

# --- imagerie et invasif ---
a('FFR',[('F','Fractional (fractionnelle)'),('F','Flow (du flux)'),('R','Reserve (réserve)')],'Réserve fractionnelle de flux coronaire',
 '<p>Rapport des pressions en aval et en amont d’une sténose sous hyperémie ; ≤ 0,80 = sténose hémodynamiquement significative.</p>')
a('iFR',[('i','instantaneous (instantané)'),('F','wave-Free (sans onde)'),('R','Ratio (rapport)')],'Rapport instantané sans onde',
 '<p>Rapport de pressions mesuré en diastole sans hyperémie ; ≤ 0,89 = sténose significative.</p>')
a('OCT',[('O','Optical (optique)'),('C','Coherence (de cohérence)'),('T','Tomography (tomographie)')],'Tomographie en cohérence optique endocoronaire',
 '<p>Imagerie endocoronaire par lumière infrarouge, résolution d’environ 10 µm : distingue rupture, érosion et dissection.</p>')
a('IVUS',[('I','Intra'),('V','Vascular (vasculaire)'),('U','Ultra'),('S','Sound (échographie : ultrasons)')],'Échographie endocoronaire',
 '<p>Imagerie endocoronaire par ultrasons : taille du vaisseau, charge de plaque, optimisation du stent.</p>')

# --- ECG ---
a('DI',[('D','Dérivation'),('I','bipolaire I (bras droit – bras gauche)')],'Dérivation frontale DI','<p>Dérivation latérale haute avec aVL.</p>')
a('DII',[('D','Dérivation'),('II','bipolaire II (bras droit – jambe gauche)')],'Dérivation frontale DII','<p>Dérivation inférieure avec DIII et aVF.</p>','i21-ecg-terr')
a('DIII',[('D','Dérivation'),('III','bipolaire III (bras gauche – jambe gauche)')],'Dérivation frontale DIII','<p>Dérivation inférieure ; un sus-décalage plus marqué qu’en DII oriente vers la coronaire droite.</p>','i21-ecg-terr')
a('aVL',[('a','augmentée'),('V','dérivation unipolaire (Voltage)'),('L','du bras gauche (Left)')],'Dérivation unipolaire augmentée du bras gauche','<p>Dérivation latérale haute ; son sous-décalage est le miroir précoce d’un infarctus inférieur.</p>')
a('aVR',[('a','augmentée'),('V','dérivation unipolaire (Voltage)'),('R','du bras droit (Right)')],'Dérivation unipolaire augmentée du bras droit','<p>Explore la cavité ; un sus-décalage associé à un sous-décalage diffus évoque une ischémie du tronc commun ou pluritronculaire.</p>','i21-ecg-avr')
for n, pos in [('3','entre V2 et V4, 4e–5e espace intercostal gauche'),('4','5e espace intercostal gauche, ligne médioclaviculaire'),('5','ligne axillaire antérieure, au niveau de V4'),('6','ligne axillaire moyenne, au niveau de V4'),('7','ligne axillaire postérieure, au niveau de V6'),('8','pointe de l’omoplate, au niveau de V6'),('9','bord gauche du rachis, au niveau de V6')]:
    a('V'+n,[('V','dérivation précordiale (Voltage unipolaire)'),(n,'n° '+n+' : '+pos)],'Dérivation précordiale V'+n,'<p>Position : '+pos+'.</p>','i21-ecg-terr' if int(n)<7 else 'i21-ecg-post')
a('V3R',[('V3','position de V3'),('R','reportée à droite (Right)')],'Dérivation précordiale droite V3R','<p>Symétrique de V3 à droite ; explore le ventricule droit.</p>','i21-ecg-post')
a('V4R',[('V4','position de V4'),('R','reportée à droite (Right)')],'Dérivation précordiale droite V4R','<p>Symétrique de V4 à droite ; un sus-décalage ≥ 0,5 mm signe un infarctus du ventricule droit.</p>','i21-e-vd')
for k, d, ref in [('V1–V2','précordiales V1 et V2 (septales)','i21-ecg-terr'),('V1–V3','précordiales V1 à V3 (septales et antérieures)','i21-ecg-terr'),('V1–V4','précordiales V1 à V4 (antéroseptales)','i21-ecg-terr'),('V1–V6','précordiales V1 à V6 (ensemble de la paroi antérieure et latérale)','i21-ecg-terr'),('V2–V3','précordiales V2 et V3, où le sus-décalage physiologique impose des seuils plus élevés','i21-ecg-terr'),('V4–V6','précordiales V4 à V6 (antérolatérales)','i21-ecg-terr'),('V5–V6','précordiales V5 et V6 (latérales basses)','i21-ecg-terr'),('V7–V9','précordiales postérieures V7 à V9','i21-ecg-post'),('V3R–V4R','précordiales droites V3R et V4R (ventricule droit)','i21-ecg-post')]:
    a(k,[('V','dérivations précordiales (Voltage unipolaire)'),(k[1:],'de '+k.split('–')[0]+' à '+k.split('–')[1])],'Dérivations '+d,'<p>Groupe de dérivations contiguës : '+d+'.</p>',ref)
a('QS',[('Q','onde Q'),('S','fusionnée avec l’onde S, sans onde R')],'Complexe QS','<p>QRS entièrement négatif ; en V2–V3 ou dans deux dérivations contiguës, séquelle de nécrose.</p>','i21-ecg-q')
a('S1Q3T3',[('S1','onde S en DI'),('Q3','onde Q en DIII'),('T3','onde T négative en DIII')],'Aspect S1Q3T3 (embolie pulmonaire)','<p>Aspect de surcharge droite aiguë, peu sensible et peu spécifique.</p>')

# --- institutions et classifications ---
a('OFS',[('O','Office'),('F','Fédéral'),('S','de la Statistique')],'Office fédéral de la statistique (Suisse)','<p>Publie la statistique des causes de décès et la statistique médicale des hôpitaux.</p>')
a('OMS',[('O','Organisation'),('M','Mondiale'),('S','de la Santé')],'Organisation mondiale de la santé','<p>Responsable de la Classification internationale des maladies.</p>')
a('CIM-11',[('C','Classification'),('I','Internationale'),('M','des Maladies'),('11','11e révision')],'Classification internationale des maladies, 11e révision','<p>Révision de l’OMS en vigueur depuis 2022 ; la Suisse code encore en CIM-10-GM.</p>')
a('ACC',[('A','American'),('C','College of'),('C','Cardiology')],'American College of Cardiology','<p>Société savante américaine de cardiologie, coautrice de la définition universelle de l’infarctus.</p>')
a('AHA',[('A','American'),('H','Heart'),('A','Association')],'American Heart Association','<p>Association américaine de cardiologie, coautrice de la définition universelle de l’infarctus.</p>')
a('WHF',[('W','World'),('H','Heart'),('F','Federation')],'World Heart Federation (Fédération mondiale du cœur)','<p>Coautrice de la définition universelle de l’infarctus.</p>')
a('EAS',[('E','European'),('A','Atherosclerosis'),('S','Society')],'Société européenne d’athérosclérose','<p>Coautrice avec l’ESC des recommandations sur les dyslipidémies (2019, mise à jour 2025).</p>')
a('AMIS Plus',[('A','Acute'),('M','Myocardial'),('I','Infarction in'),('S','Switzerland'),('Plus','registre élargi à l’ensemble des SCA')],'Registre national suisse des syndromes coronariens aigus',
 '<p>Registre des patients hospitalisés pour un SCA dans des hôpitaux suisses, depuis 1997.</p>')

# --- essais ---
t('INTERHEART',[('INTERHEART','nom d’étude (étude INTERnationale sur le cœur, HEART), non développé lettre à lettre')],'Étude INTERHEART (2004)','<p>Étude cas-témoins dans 52 pays : neuf facteurs modifiables expliquent plus de 90 % du risque attribuable de premier infarctus.</p>')
t('DETO2X-AMI',[('DETO2X','DETermination of the role of OXygen'),('AMI','in suspected Acute Myocardial Infarction')],'Essai DETO2X-AMI (2017)','<p>Oxygène systématique chez les patients normoxémiques suspects d’infarctus : pas de réduction de la mortalité.</p>')
t('COMPLETE',[('COMPLETE','nom d’essai (« COMPLETE revascularization versus culprit-only PCI »), non développé lettre à lettre')],'Essai COMPLETE (2019)','<p>STEMI pluritronculaire : la revascularisation complète réduit les décès cardiovasculaires et les infarctus.</p>','i21-complete')
t('FIRE',[('FIRE','nom d’essai (Functional assessment In elderly MI patients with multivessel disease), non développé lettre à lettre')],'Essai FIRE (2023)','<p>Chez les plus de 75 ans avec infarctus pluritronculaire, la revascularisation complète guidée par la physiologie réduit les événements à un an.</p>','i21-complete')
t('CULPRIT-SHOCK',[('CULPRIT','CULPRIT lesion only PCI (angioplastie de la seule lésion coupable)'),('SHOCK','in cardiogenic SHOCK')],'Essai CULPRIT-SHOCK (2017)','<p>Choc cardiogénique : l’angioplastie de la seule artère coupable réduit le décès ou l’insuffisance rénale sévère à 30 jours.</p>')
t('OAT',[('O','Occluded'),('A','Artery'),('T','Trial')],'Essai OAT (2006)','<p>Ouverture tardive (3 à 28 jours) d’une artère occluse chez un patient stable : pas de bénéfice.</p>')
t('STREAM',[('ST','STrategic'),('R','Reperfusion'),('E','Early'),('A','After'),('M','Myocardial infarction')],'Essai STREAM (2013)','<p>Stratégie pharmaco-invasive (ténectéplase préhospitalière puis coronarographie) comparable à une angioplastie primaire tardive ; demi-dose après 75 ans.</p>','i21-d-lyse')
t('IABP-SHOCK II',[('IABP','IntraAortic Balloon Pump (ballon de contre-pulsion intra-aortique)'),('SHOCK','in cardiogenic SHOCK'),('II','deuxième essai')],'Essai IABP-SHOCK II (2012)','<p>Le ballon de contre-pulsion intra-aortique ne réduit pas la mortalité dans le choc cardiogénique compliquant un infarctus.</p>','i21-choc')
t('DanGer Shock',[('Dan','DANish'),('Ger','GERman'),('Shock','cardiogenic Shock trial')],'Essai DanGer Shock (2024)','<p>STEMI avec choc cardiogénique : la pompe microaxiale réduit la mortalité à 180 jours, avec plus de complications (hémorragies, ischémie de membre).</p>','i21-choc')
t('ISAR-REACT 5',[('ISAR','Intracoronary Stenting and Antithrombotic Regimen'),('REACT','Rapid Early Action for Coronary Treatment'),('5','cinquième essai')],'Essai ISAR-REACT 5 (2019)','<p>SCA avec stratégie invasive : le prasugrel réduit le décès, l’infarctus ou l’AVC par rapport au ticagrélor.</p>','i21-d-p2y12')
t('PLATO',[('PLAT','PLATelet inhibition'),('O','and patient Outcomes')],'Essai PLATO (2009)','<p>Ticagrélor contre clopidogrel dans le SCA : moins d’événements ischémiques et de décès.</p>','i21-d-p2y12')
t('TRITON-TIMI 38',[('TRITON','TRial to assess Improvement in Therapeutic Outcomes by optimizing platelet inhibitioN with prasugrel'),('TIMI 38','Thrombolysis In Myocardial Infarction, essai n° 38')],'Essai TRITON-TIMI 38 (2007)','<p>Prasugrel contre clopidogrel dans le SCA traité par angioplastie : moins d’événements ischémiques, plus d’hémorragies.</p>','i21-d-p2y12')
t('CURE',[('C','Clopidogrel in'),('U','Unstable angina to prevent'),('R','Recurrent'),('E','Events')],'Essai CURE (2001)','<p>Clopidogrel ajouté à l’acide acétylsalicylique dans le NSTE-ACS : réduction des événements ischémiques.</p>','i21-d-p2y12')
t('TWILIGHT',[('TWILIGHT','nom d’essai (« Ticagrelor With aspirin or alone In high-risk patients after coronary intervention »), non développé lettre à lettre')],'Essai TWILIGHT (2019)','<p>Après 3 mois de double antiagrégation, ticagrélor seul : moins d’hémorragies sans excès d’événements ischémiques.</p>','i21-dapt')
t('STOPDAPT-2',[('STOP','ShorT and OPtimal duration of'),('DAPT','Dual AntiPlatelet Therapy'),('2','deuxième essai')],'Essai STOPDAPT-2 (2019)','<p>Un mois de double antiagrégation puis clopidogrel seul après angioplastie : moins d’hémorragies.</p>','i21-dapt')
t('MASTER DAPT',[('MASTER','MAnagement of high bleeding risk patients post bioresorbable polymer coated STEnt implantation with an abbReviated versus standard'),('DAPT','Dual AntiPlatelet Therapy regimen')],'Essai MASTER DAPT (2021)','<p>Patients à haut risque hémorragique : un mois de double antiagrégation, moins d’hémorragies sans excès d’événements.</p>','i21-dapt')
t('PEGASUS-TIMI 54',[('PEGASUS','nom d’essai (ticagrélor au long cours après infarctus), non développé lettre à lettre'),('TIMI 54','Thrombolysis In Myocardial Infarction, essai n° 54')],'Essai PEGASUS-TIMI 54 (2015)','<p>Ticagrélor 60 mg deux fois par jour, 1 à 3 ans après un infarctus : moins d’événements ischémiques, plus d’hémorragies.</p>','i21-dapt')
t('COMPASS',[('C','Cardiovascular'),('OM','OutcoMes for'),('P','People using'),('A','Anticoagulation'),('SS','StrategieS')],'Essai COMPASS (2017)','<p>Rivaroxaban 2,5 mg deux fois par jour avec acide acétylsalicylique dans la maladie coronaire ou artérielle stable : moins d’événements.</p>','i21-dapt')
t('TALOS-AMI',[('TALOS','TicAgrelor versus CLOpidogrel in Stabilized patients'),('AMI','with Acute Myocardial Infarction')],'Essai TALOS-AMI (2021)','<p>Désescalade non guidée vers le clopidogrel à un mois après infarctus : moins d’hémorragies.</p>','i21-desesc')
t('TROPICAL-ACS',[('TROPICAL','Testing Responsiveness to Platelet Inhibition on Chronic Antiplatelet treatment'),('ACS','for Acute Coronary Syndromes')],'Essai TROPICAL-ACS (2017)','<p>Désescalade guidée par un test de fonction plaquettaire : non inférieure au prasugrel.</p>','i21-desesc')
t('POPular Genetics',[('POPular','nom de programme néerlandais d’essais sur l’inhibition plaquettaire, non développé lettre à lettre'),('Genetics','guidé par le génotype')],'Essai POPular Genetics (2019)','<p>Choix de l’inhibiteur P2Y12 guidé par le génotype du CYP2C19 : non inférieur, moins d’hémorragies.</p>','i21-desesc')
t('POPular AGE',[('POPular','nom de programme néerlandais d’essais sur l’inhibition plaquettaire, non développé lettre à lettre'),('AGE','patients âgés de 70 ans ou plus')],'Essai POPular AGE (2020)','<p>Chez les 70 ans ou plus avec NSTE-ACS, le clopidogrel cause moins d’hémorragies que le ticagrélor ou le prasugrel.</p>')
t('AUGUSTUS',[('AUGUSTUS','nom d’essai (apixaban et acide acétylsalicylique dans la fibrillation auriculaire avec SCA ou angioplastie), non développé lettre à lettre')],'Essai AUGUSTUS (2019)','<p>Apixaban : moins d’hémorragies qu’un antivitamine K ; l’acide acétylsalicylique ajouté augmente les hémorragies.</p>','i21-triple')
t('SENIOR-RITA',[('SENIOR','patients âgés de 75 ans ou plus'),('RITA','Randomised Intervention Trial of unstable Angina (nom du programme)')],'Essai SENIOR-RITA (2024)','<p>NSTEMI après 75 ans : la stratégie invasive réduit les infarctus non mortels sans réduire la mortalité.</p>')
t('REDUCE-AMI',[('REDUCE','Randomized Evaluation of Decreased Usage of beta-bloCkErs'),('AMI','after Acute Myocardial Infarction')],'Essai REDUCE-AMI (2024)','<p>Infarctus avec FEVG ≥ 50 % : le bêtabloquant ne réduit pas le décès ou le réinfarctus.</p>','i21-d-bb')
t('REBOOT',[('REBOOT','nom d’essai arrangé à partir de « tREatment with Beta-blockers after myOcardial infarction withOut reduced ejection fracTion », non développé lettre à lettre')],'Essai REBOOT (2025)','<p>Infarctus avec FEVG &gt; 40 % : pas de bénéfice du bêtabloquant sur le critère principal.</p>','i21-d-bb')
t('BETAMI-DANBLOCK',[('BETAMI','BEta-blocker Treatment After acute Myocardial Infarction (essai norvégien)'),('DANBLOCK','DANish trial of beta-BLOCKer treatment (essai danois)')],'Essais BETAMI et DANBLOCK combinés (2025)','<p>Infarctus avec FEVG ≥ 40 % : réduction du critère composite par le bêtabloquant.</p>','i21-d-bb')
t('CAPRICORN',[('CAPRICORN','nom d’essai arrangé à partir de « CArvedilol Post-infaRct survIval COntRol in left ventricular dysfunctioN », non développé lettre à lettre')],'Essai CAPRICORN (2001)','<p>Carvédilol après infarctus avec FEVG ≤ 40 % : réduction de la mortalité.</p>','i21-d-bb')
t('EPHESUS',[('EPHESUS','Eplerenone Post-acute myocardial infarction Heart failure Efficacy and SUrvival Study, non strictement lettre à lettre')],'Essai EPHESUS (2003)','<p>Éplérénone après infarctus avec FEVG ≤ 40 % et insuffisance cardiaque ou diabète : réduction de la mortalité.</p>','i21-d-arm')
t('SAVE',[('S','Survival'),('A','And'),('V','Ventricular'),('E','Enlargement')],'Essai SAVE (1992)','<p>Captopril après infarctus avec dysfonction ventriculaire gauche : réduction de la mortalité.</p>','i21-d-iec')
t('AIRE',[('A','Acute'),('I','Infarction'),('R','Ramipril'),('E','Efficacy')],'Essai AIRE (1993)','<p>Ramipril après infarctus avec insuffisance cardiaque : réduction de la mortalité.</p>','i21-d-iec')
t('TRACE',[('TRA','TRAndolapril'),('C','Cardiac'),('E','Evaluation')],'Essai TRACE (1995)','<p>Trandolapril après infarctus avec dysfonction ventriculaire gauche : réduction de la mortalité.</p>','i21-d-iec')
t('VALIANT',[('VAL','VALsartan'),('I','In'),('A','Acute myocardial'),('N','iNfarcTion'),('T','(infarcTion)')],'Essai VALIANT (2003)','<p>Valsartan non inférieur au captopril après infarctus compliqué ; l’association n’apporte rien et augmente les effets indésirables.</p>','i21-d-iec')
t('ISIS-2',[('I','International'),('S','Study of'),('I','Infarct'),('S','Survival'),('2','deuxième étude')],'Essai ISIS-2 (1988)','<p>Acide acétylsalicylique et streptokinase dans l’infarctus : chacun réduit la mortalité, leurs effets s’additionnent.</p>','i21-d-asa')
t('OASIS-5',[('O','Organization to'),('AS','ASsess'),('IS','strategies in Ischemic Syndromes'),('5','cinquième essai')],'Essai OASIS-5 (2006)','<p>Fondaparinux contre énoxaparine dans le NSTE-ACS : efficacité comparable, moins d’hémorragies graves.</p>','i21-d-hep')
t('PROVE-IT',[('PROVE','PRavastatin Or atorVastatin Evaluation'),('IT','and Infection Therapy')],'Essai PROVE-IT (2004)','<p>Après un SCA, atorvastatine 80 mg supérieure à la pravastatine 40 mg.</p>','i21-d-statine')
t('IMPROVE-IT',[('IMPROVE','IMProved Reduction of Outcomes'),('IT',': Vytorin Efficacy International Trial')],'Essai IMPROVE-IT (2015)','<p>Ézétimibe ajouté à la simvastatine après un SCA : réduction modeste des événements.</p>','i21-d-ezet')
t('FOURIER',[('FOURIER','Further cardiOvascular OUtcomes Research with PCSK9 Inhibition in subjects with Elevated Risk, non strictement lettre à lettre')],'Essai FOURIER (2017)','<p>Évolocumab chez des patients athéroscléreux sous statine : réduction des événements cardiovasculaires.</p>','i21-d-pcsk9')
t('ODYSSEY OUTCOMES',[('ODYSSEY','nom du programme d’essais de l’alirocumab, non développé lettre à lettre'),('OUTCOMES','essai sur les événements cliniques après un SCA')],'Essai ODYSSEY OUTCOMES (2018)','<p>Alirocumab après un SCA récent : réduction des événements cardiovasculaires.</p>','i21-d-pcsk9')
t('CLEAR Outcomes',[('CLEAR','Cholesterol Lowering via bEmpedoic acid, an ACL-inhibiting Regimen'),('Outcomes','essai sur les événements cliniques')],'Essai CLEAR Outcomes (2023)','<p>Acide bempédoïque chez des patients intolérants aux statines : réduction des événements cardiovasculaires majeurs.</p>','i21-d-bempe')
t('COLCOT',[('COL','COLchicine'),('C','Cardiovascular'),('O','Outcomes'),('T','Trial')],'Essai COLCOT (2019)','<p>Colchicine 0,5 mg/jour dans les 30 jours d’un infarctus : réduction des événements ischémiques.</p>','i21-d-colch')
t('LoDoCo2',[('Lo','Low'),('Do','Dose'),('Co','Colchicine'),('2','deuxième essai')],'Essai LoDoCo2 (2020)','<p>Colchicine à faible dose dans la coronaropathie chronique : réduction des événements.</p>','i21-d-colch')
t('CLEAR SYNERGY',[('CLEAR','Colchicine and spironoLactone in patiEnts with myocArdial infarction, non strictement lettre à lettre'),('SYNERGY','registre du stent SYNERGY')],'Essai CLEAR SYNERGY (2024)','<p>Colchicine débutée à la phase aiguë de l’infarctus : pas de réduction des événements.</p>','i21-d-colch')
t('EMPACT-MI',[('EMPA','EMPAgliflozine'),('CT','effect on hospitalisation for heart failure and mortality in patients with aCuTe'),('MI','Myocardial Infarction')],'Essai EMPACT-MI (2024)','<p>Empagliflozine après infarctus : pas de réduction du critère principal (décès ou hospitalisation pour insuffisance cardiaque).</p>')
t('DAPA-MI',[('DAPA','DAPAgliflozine'),('MI','in patients with Myocardial Infarction')],'Essai DAPA-MI (2024)','<p>Dapagliflozine après infarctus sans diabète ni insuffisance cardiaque : pas de réduction des événements cardiovasculaires.</p>')
t('COGENT',[('CO','Clopidogrel and the Optimization of'),('G','Gastrointestinal'),('EN','EveNts'),('T','Trial')],'Essai COGENT (2010)','<p>Oméprazole sous double antiagrégation : moins d’hémorragies digestives, sans hausse démontrée des événements cardiovasculaires.</p>','i21-d-ipp')

a('METs',[('MET','Metabolic Equivalent of Task (équivalent métabolique)'),('s','pluriel')],'Équivalents métaboliques',
 '<p>1 MET correspond à la consommation d’oxygène au repos, environ 3,5 mL/kg/min. Une capacité &gt; 4 METs équivaut à monter deux étages sans s’arrêter.</p>','i21-conduite')
t('Lp(a)HORIZON',[('Lp(a)','Lipoprotéine(a)'),('HORIZON','nom d’essai, non développé lettre à lettre')],'Essai Lp(a)HORIZON (2026)','<p>Pelacarsen, oligonucléotide dirigé contre l’apolipoprotéine(a), chez des patients avec maladie cardiovasculaire et lipoprotéine(a) élevée : critère principal non atteint.</p>','i21-lpa')
t('PRISM-PLUS',[('PRISM','Platelet Receptor Inhibition in ischemic Syndrome Management'),('PLUS','in Patients Limited by Unstable Signs and symptoms')],'Essai PRISM-PLUS (1998)','<p>Tirofiban ajouté à l’héparine dans l’angor instable et le NSTEMI : réduction des événements ischémiques.</p>','i21-d-gp')
t('PURSUIT',[('PURSUIT','Platelet glycoprotein IIb/IIIa in Unstable angina: Receptor Suppression Using Integrilin Therapy, non strictement lettre à lettre')],'Essai PURSUIT (1998)','<p>Eptifibatide dans le SCA sans sus-décalage : réduction modeste du décès ou de l’infarctus.</p>','i21-d-gp')
t('CHAMPION PHOENIX',[('CHAMPION','Cangrelor versus standard tHerapy to Achieve optimal Management of Platelet InhibitiON, non strictement lettre à lettre'),('PHOENIX','nom du troisième essai du programme')],'Essai CHAMPION PHOENIX (2013)','<p>Cangrélor contre clopidogrel pendant l’angioplastie : moins d’événements ischémiques périprocéduraux, dont les thromboses de stent.</p>','i21-d-gp')
a('CIR',[('CIR','CIRculation : préfixe éditorial des articles de la revue Circulation dans leur identifiant numérique')],'Préfixe de la revue Circulation dans un identifiant d’article (doi)','<p>Élément d’un identifiant d’objet numérique, non une abréviation clinique.</p>')

# --- références suisses (balayage du 08.10.2026) ---
a('GSLA',[('G','Groupe'),('S','Suisse'),('L','Lipides'),('A','et Athérosclérose')],'Groupe de travail Lipides et Athérosclérose (Arbeitsgruppe Lipide und Atherosklerose, AGLA en allemand)',
 '<p>Groupe d’experts suisse qui adapte au contexte suisse les recommandations européennes sur les lipides et la prévention de l’athérosclérose ; il publie le calculateur de risque GSLA et le guide de poche « Prévention de l’athérosclérose ».</p>')
a('SCPRS',[('S','Swiss (suisse)'),('C','Cardiovascular (cardiovasculaire)'),('P','Prevention (prévention)'),('R','Rehabilitation (réadaptation)'),('S','Sports cardiology (cardiologie du sport)')],'Groupe de travail suisse pour la prévention cardiovasculaire, la réadaptation et la cardiologie du sport',
 '<p>Groupe de travail de la Société suisse de cardiologie qui fixe les critères de qualité des programmes de réadaptation cardiaque ; le respect de ces critères conditionne leur prise en charge par l’assurance obligatoire.</p>')
