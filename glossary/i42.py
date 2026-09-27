# Glossaire MEDINA — chapitre I42 (cardiomyopathies, I42 et I43)
from cardio_1 import a, G

# ---- phénotypes
a('CMH',[('C','Cardio-'),('M','Myopathie'),('H','Hypertrophique')],'Cardiomyopathie hypertrophique',
 '<p>Épaisseur pariétale du ventricule gauche ≥ 15 mm dans au moins un segment (≥ 13 mm chez un apparenté du premier degré), non expliquée par les conditions de charge (ESC 2023). Le plus souvent due à un variant d’un gène du sarcomère.</p>','i42-obstruction')
a('CMD',[('C','Cardio-'),('M','Myopathie'),('D','Dilatée')],'Cardiomyopathie dilatée',
 '<p>Dilatation du ventricule gauche avec dysfonction systolique globale (FEVG &lt; 50 %), non expliquée par une maladie coronaire ou les conditions de charge (ESC 2023).</p>')
a('CMNDVG',[('C','Cardio-'),('M','Myopathie'),('N','Non'),('D','Dilatée'),('VG','du Ventricule Gauche')],'Cardiomyopathie non dilatée du ventricule gauche',
 '<p>Phénotype créé par l’ESC 2023 : cicatrice non ischémique ou remplacement graisseux du ventricule gauche, ou hypokinésie globale isolée, sans dilatation. Gènes fréquents : <i>DSP</i>, <i>FLNC</i>, <i>LMNA</i>.</p>')
a('CMAVD',[('C','Cardio-'),('M','Myopathie'),('A','Arythmogène'),('VD','du Ventricule Droit')],'Cardiomyopathie arythmogène du ventricule droit',
 '<p>Remplacement fibro-adipeux du myocarde, surtout du ventricule droit, avec arythmies ventriculaires ; le plus souvent due à un variant desmosomal (<i>PKP2</i>). Diagnostic selon les critères de la Task Force 2010 et de Padoue 2020.</p>','i42-arvc-tfc')
a('CMR',[('C','Cardio-'),('M','Myopathie'),('R','Restrictive')],'Cardiomyopathie restrictive',
 '<p>Physiologie restrictive d’un ou des deux ventricules, avec volumes normaux ou réduits et épaisseur pariétale normale (ESC 2023). À ne pas confondre avec l’abréviation anglaise de l’IRM cardiaque, non utilisée dans MEDINA.</p>','i42-restriction')
a('FEVD',[('F','Fraction'),('E','d’Éjection'),('V','du Ventricule'),('D','Droit')],'Fraction d’éjection du ventricule droit',
 '<p>Mesurée de préférence par IRM ; valeur normale supérieure à environ 45 %. Une FEVD ≤ 40 % est un critère majeur de CMAVD et un critère de défibrillateur.</p>')

# ---- scores, critères, lois
a('HCM Risk-SCD',[('HCM','Hypertrophic CardioMyopathy (cardiomyopathie hypertrophique)'),('Risk','risque'),('SCD','Sudden Cardiac Death (mort subite cardiaque)')],'Score de risque de mort subite dans la cardiomyopathie hypertrophique',
 '<p>Estimation du risque de mort subite à 5 ans à partir de sept variables, chez le patient de 16 ans ou plus (O’Mahony 2014 ; ESC 2023). ≥ 6 % : défibrillateur à envisager (IIa).</p>','i42-hcmrisk')
a('HCM Risk-Kids',[('HCM','Hypertrophic CardioMyopathy (cardiomyopathie hypertrophique)'),('Risk','risque'),('Kids','enfants')],'Score de risque de mort subite de la cardiomyopathie hypertrophique de l’enfant',
 '<p>Équivalent pédiatrique du score HCM Risk-SCD, utilisé avant 16 ans.</p>','i42-hcmrisk')
a('InterTAK',[('Inter','International'),('TAK','TAKotsubo (registre)')],'Registre international du Tako-tsubo',
 '<p>Registre international coordonné depuis Zurich. Il a publié les critères diagnostiques internationaux (2018) et un score de probabilité avant coronarographie.</p>','i42-intertak')
a('BOARD',[('B','Bromocriptine'),('O','traitements Oraux de l’insuffisance cardiaque'),('A','Anticoagulation'),('R','vasoRelaxateurs'),('D','Diurétiques')],'Aide-mémoire BOARD de la cardiomyopathie du péripartum',
 '<p>Aide pédagogique proposée par des experts de l’Association de l’insuffisance cardiaque de l’ESC ; non critère officiel.</p>','i42-ppcm')
a('LAGH',[('L','Loi fédérale sur l’'),('A','Analyse'),('G','Génétique'),('H','Humaine')],'Loi fédérale suisse sur l’analyse génétique humaine',
 '<p>Loi qui encadre les analyses génétiques en Suisse (version révisée en vigueur depuis décembre 2022) : consentement éclairé, conseil génétique, protection contre l’usage abusif des résultats par les employeurs et les assureurs.</p>','i42-conseil')
a('E/A',[('E','onde E (remplissage rapide, « Early »)'),('A','onde A (contraction Auriculaire)')],'Rapport des ondes E et A du flux mitral',
 '<p>Rapport entre le pic de vitesse du remplissage protodiastolique et celui du remplissage par la contraction auriculaire. E/A &gt; 2 avec un temps de décélération court : physiologie restrictive.</p>','i42-restriction')
a('Pi',[('P','Phosphate'),('i','inorganique')],'Phosphate inorganique','<p>Produit de l’hydrolyse de l’ATP par la myosine ; sa libération déclenche le coup de rame. Les inhibiteurs de la myosine cardiaque la ralentissent.</p>','i42-sarcomere')

# ---- essais
a('EXPLORER-HCM',[('EXPLORER','nom d’essai (non acronyme lettre à lettre) : « explorer »'),('HCM','Hypertrophic CardioMyopathy')],'Essai EXPLORER-HCM (2020)',
 '<p>Mavacamten contre placebo dans la CMH obstructive symptomatique : amélioration de la capacité d’effort, de la classe NYHA et du gradient.</p>','i42-d-mava')
a('VALOR-HCM',[('VALOR','nom d’essai (non acronyme lettre à lettre)'),('HCM','Hypertrophic CardioMyopathy')],'Essai VALOR-HCM (2022)',
 '<p>Mavacamten chez des candidats à une réduction septale : la majorité n’en avait plus besoin à 16 semaines.</p>','i42-d-mava')
a('ODYSSEY-HCM',[('ODYSSEY','nom d’essai (non acronyme lettre à lettre)'),('HCM','Hypertrophic CardioMyopathy')],'Essai ODYSSEY-HCM (2025)',
 '<p>Mavacamten dans la CMH non obstructive : critères principaux non atteints.</p>','i42-d-mava')
a('SEQUOIA-HCM',[('SEQUOIA','nom d’essai (non acronyme lettre à lettre)'),('HCM','Hypertrophic CardioMyopathy')],'Essai SEQUOIA-HCM (2024)',
 '<p>Aficamten contre placebo dans la CMH obstructive : VO₂ pic augmentée de 1,7 mL/kg/min à 24 semaines.</p>','i42-d-afi')
a('MAPLE-HCM',[('MAPLE','nom d’essai (non acronyme lettre à lettre)'),('HCM','Hypertrophic CardioMyopathy')],'Essai MAPLE-HCM (2025)',
 '<p>Aficamten contre métoprolol en monothérapie dans la CMH obstructive : supériorité de l’aficamten sur la VO₂ pic.</p>','i42-d-afi')
a('ACACIA-HCM',[('ACACIA','nom d’essai (non acronyme lettre à lettre)'),('HCM','Hypertrophic CardioMyopathy')],'Essai ACACIA-HCM (2026)',
 '<p>Aficamten contre placebo dans la CMH non obstructive symptomatique : amélioration de la qualité de vie et de la VO₂ pic (présenté en août 2026).</p>','i42-d-afi')
a('ATTR-ACT',[('ATTR','Amylose à TransThyRétine'),('ACT','fin du nom d’essai « Tafamidis in Transthyretin Cardiomyopathy Clinical Trial », non strictement lettre à lettre')],'Essai ATTR-ACT (2018)',
 '<p>Tafamidis contre placebo dans l’amylose ATTR avec cardiomyopathie : mortalité totale 29,5 % contre 42,9 % à 30 mois.</p>','i42-d-tafa')
a('ATTRibute-CM',[('ATTR','Amylose à TransThyRétine'),('ibute','terminaison du nom d’essai « ATTRibute », non abréviative'),('CM','CardioMyopathie')],'Essai ATTRibute-CM (2024)',
 '<p>Acoramidis contre placebo dans l’amylose ATTR avec cardiomyopathie : critère hiérarchique favorable, hospitalisations cardiovasculaires réduites.</p>','i42-d-acora')
a('DANISH',[('DANISH','nom d’essai signifiant « danois » : Danish Study to Assess the Efficacy of ICDs in Patients with Non-ischemic Systolic Heart Failure on Mortality, non strictement lettre à lettre')],'Essai DANISH (2016)',
 '<p>Défibrillateur en prévention primaire dans l’insuffisance cardiaque non ischémique : pas de réduction de la mortalité totale ; bénéfice possible chez le patient plus jeune.</p>','i42-dai')

# ---- gènes et variants
a('PKP2',[('PKP','PlaKoPhiline'),('2','2')],'Gène de la plakophiline 2','<p>Protéine desmosomale ; première cause génétique de CMAVD.</p>','i42-desmosome')
a('DSG2',[('DSG','DeSmoGléine'),('2','2')],'Gène de la desmogléine 2','<p>Cadhérine desmosomale ; cause de CMAVD, parfois biventriculaire.</p>','i42-desmosome')
a('DSC2',[('DSC','DeSmoColline'),('2','2')],'Gène de la desmocolline 2','<p>Cadhérine desmosomale ; cause rare de CMAVD.</p>','i42-desmosome')
a('JUP',[('JUP','Junction Plakoglobin (plakoglobine de jonction)')],'Gène de la plakoglobine','<p>Protéine desmosomale ; ses variants récessifs causent la maladie de Naxos (CMAVD, kératodermie palmoplantaire, cheveux crépus).</p>','i42-desmosome')
a('TMEM43',[('TMEM','TransMEMbrane protein (protéine transmembranaire)'),('43','numéro 43')],'Gène de la protéine transmembranaire 43','<p>Protéine de l’enveloppe nucléaire ; variant fondateur de Terre-Neuve responsable d’une CMAVD très arythmogène.</p>')
a('DES',[('DES','DESmine')],'Gène de la desmine','<p>Filament intermédiaire du muscle ; ses variants causent des myopathies et des cardiomyopathies dilatées, restrictives ou arythmogènes.</p>')
a('BAG3',[('BAG','Bcl-2-Associated athanoGene (gène associé à Bcl-2)'),('3','3')],'Gène BAG3','<p>Co-chaperon qui protège les protéines du sarcomère ; cause de CMD.</p>')
a('TNNT2',[('TNN','TropoNiNe'),('T','T'),('2','isoforme cardiaque 2')],'Gène de la troponine T cardiaque','<p>Cause de CMH, parfois avec hypertrophie modérée mais risque rythmique notable.</p>','i42-sarcomere')
a('TNNI3',[('TNN','TropoNiNe'),('I','I'),('3','isoforme cardiaque 3')],'Gène de la troponine I cardiaque','<p>Cause de CMH et de CMR sarcomériques.</p>','i42-sarcomere')
a('TPM1',[('TPM','TroPoMyosine'),('1','1 (alpha)')],'Gène de l’alpha-tropomyosine','<p>Cause rare de CMH et de CMD.</p>','i42-sarcomere')
a('MYL2',[('MYL','MYosine, chaîne Légère'),('2','2 (régulatrice)')],'Gène de la chaîne légère régulatrice de la myosine','<p>Cause rare de CMH.</p>','i42-sarcomere')
a('MYL3',[('MYL','MYosine, chaîne Légère'),('3','3 (essentielle)')],'Gène de la chaîne légère essentielle de la myosine','<p>Cause rare de CMH.</p>','i42-sarcomere')
a('ACTC1',[('ACT','ACTine'),('C','Cardiaque'),('1','1 (alpha)')],'Gène de l’alpha-actine cardiaque','<p>Cause rare de CMH et de CMD.</p>','i42-sarcomere')
a('LAMP2',[('LAMP','Lysosome-Associated Membrane Protein (protéine membranaire associée au lysosome)'),('2','2')],'Gène LAMP2','<p>Son déficit, lié à l’X, cause la maladie de Danon : hypertrophie massive, préexcitation, myopathie, évolution rapide.</p>','i42-phenocopies')
a('PRKAG2',[('PRKA','PRotéine Kinase activée par l’AMP'),('G','sous-unité Gamma'),('2','2')],'Gène PRKAG2','<p>Variants responsables d’une surcharge en glycogène : hypertrophie, préexcitation, troubles de conduction.</p>','i42-phenocopies')
a('HFE',[('HFE','High FE (fer élevé ; « Fe » = symbole du fer)')],'Gène de l’hémochromatose','<p>L’homozygotie C282Y est la cause principale de l’hémochromatose génétique en Europe.</p>','i42-hemochrom')
a('C282Y',[('C','Cystéine'),('282','en position 282'),('Y','remplacée par une tYrosine')],'Variant C282Y du gène HFE','<p>Variant fondateur de l’Europe du Nord ; l’homozygotie expose à la surcharge en fer, avec une pénétrance clinique incomplète.</p>','i42-hemochrom')
a('HER2',[('HER','Human Epidermal growth factor Receptor (récepteur humain du facteur de croissance épidermique)'),('2','type 2')],'Récepteur HER2','<p>Récepteur surexprimé dans certains cancers du sein ; cible du trastuzumab, dont la cardiotoxicité est souvent réversible.</p>','i42-anthra')
a('Gb3',[('Gb','GloBo- (globotriaosyl-)'),('3','tri- (trois oses)')],'Globotriaosylcéramide','<p>Sphingolipide accumulé dans la maladie de Fabry par déficit en alpha-galactosidase A.</p>','i42-fabry')
a('lyso-Gb3',[('lyso','forme désacylée (lyso-)'),('Gb3','GloBotriaosylcéramide')],'Globotriaosylsphingosine','<p>Dérivé plasmatique du Gb3 ; biomarqueur du diagnostic et du suivi de la maladie de Fabry.</p>','i42-fabry')
a('RASopathie',[('RAS','voie de signalisation RAS (Rat Sarcoma, oncogène du sarcome du rat)'),('opathie','maladie')],'RASopathie','<p>Syndrome génétique par activation de la voie RAS-MAPK (syndrome de Noonan et apparentés) ; cause de CMH de l’enfant.</p>','i42-phenocopies')
a('RASopathies',[('RAS','voie de signalisation RAS (Rat Sarcoma)'),('opathies','maladies')],'RASopathies','<p>Pluriel de RASopathie.</p>','i42-phenocopies')

# ---- éponymes
a('Brockenbrough-Braunwald-Morrow',[('Brockenbrough-Braunwald-Morrow','noms propres des auteurs (Edwin Brockenbrough, Eugene Braunwald, Andrew Morrow, 1961) ; ce n’est pas une abréviation')],'Signe de Brockenbrough-Braunwald-Morrow',
 '<p>Après une extrasystole ventriculaire, la pression différentielle aortique diminue alors que le gradient intraventriculaire augmente : signe d’obstruction dynamique.</p>','i42-e-pouls')
a('Emery-Dreifuss',[('Emery-Dreifuss','noms propres d’Alan Emery et Fritz Dreifuss ; ce n’est pas une abréviation')],'Dystrophie musculaire d’Emery-Dreifuss',
 '<p>Dystrophie avec contractures précoces et atteinte cardiaque (troubles de conduction, arythmies) ; forme autosomique liée à <i>LMNA</i>.</p>','i42-neuromusc')

# ---- codes CIM-10
a('D86.8',[('D86.8','code CIM-10 : D86 = sarcoïdose ; .8 = sarcoïdose d’autres localisations et de localisations associées')],'Code CIM-10 D86.8 : sarcoïdose d’autres localisations','<p>Utilisé avec I43.8 pour la cardiomyopathie sarcoïdosique et avec I41.8 pour la myocardite sarcoïdosique.</p>','i42-sarcoid')
a('E75.2',[('E75.2','code CIM-10 : E75 = troubles du métabolisme des sphingolipides ; .2 = autres sphingolipidoses (dont la maladie de Fabry)')],'Code CIM-10 E75.2 : autres sphingolipidoses','<p>Code de la maladie de Fabry.</p>','i42-fabry')
a('O90.3',[('O90.3','code CIM-10 : O90 = complications de la puerpéralité ; .3 = cardiomyopathie au cours de la puerpéralité')],'Code CIM-10 O90.3 : cardiomyopathie du péripartum','<p>Code de la cardiomyopathie du péripartum.</p>','i42-ppcm')
