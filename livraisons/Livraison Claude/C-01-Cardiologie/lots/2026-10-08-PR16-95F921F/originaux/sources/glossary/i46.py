# Glossaire MEDINA — chapitre I46 Arrêt cardiaque
from cardio_1 import a, G

# ---- entités et issues
a('RCP',[('R','Réanimation'),('C','Cardio-'),('P','Pulmonaire')],'Réanimation cardiopulmonaire',
 '<p>Ensemble des compressions thoraciques et des ventilations destinées à maintenir une perfusion minimale du cerveau et du cœur pendant un arrêt cardiaque, en attendant la défibrillation ou la correction de la cause.</p>','i46-rcpqual')
a('ACEH',[('A','Arrêt'),('C','Cardiaque'),('E','Extra-'),('H','Hospitalier')],'Arrêt cardiaque extrahospitalier',
 '<p>Arrêt cardiaque survenant hors de l’hôpital, le plus souvent au domicile ; son pronostic dépend surtout de la reconnaissance, de la RCP et de la défibrillation par les témoins.</p>','i46-chaine')
a('ACIH',[('A','Arrêt'),('C','Cardiaque'),('I','Intra-'),('H','Hospitalier')],'Arrêt cardiaque intrahospitalier',
 '<p>Arrêt cardiaque d’un patient hospitalisé ; souvent précédé de signes de détérioration, avec un rythme initial le plus souvent non choquable.</p>','i46-acih')
a('RACS',[('R','Retour'),('A','à une'),('C','Circulation'),('S','Spontanée')],'Retour à une circulation spontanée',
 '<p>Reprise d’un pouls palpable ou d’une pression artérielle mesurable après un arrêt cardiaque. Équivalent anglais : ROSC. Il ne préjuge pas de l’issue neurologique.</p>','i46-spac')
a('AESP',[('A','Activité'),('E','Électrique'),('S','Sans'),('P','Pouls')],'Activité électrique sans pouls',
 '<p>Rythme organisé au moniteur sans pouls palpable ; rythme non choquable dont le traitement repose sur les compressions, l’adrénaline et la correction de la cause.</p>','i46-aesp')
a('CPC',[('C','Cerebral'),('P','Performance'),('C','Category')],'Catégorie de performance cérébrale (Cerebral Performance Category)',
 '<p>Échelle d’issue neurologique après arrêt cardiaque, de 1 (bonne récupération) à 5 (décès) ; les catégories 1 et 2 définissent une issue favorable.</p>')
a('ALS',[('A','Advanced'),('L','Life'),('S','Support')],'Advanced Life Support (réanimation avancée)',
 '<p>Réanimation avancée : défibrillateur manuel, médicaments, voies aériennes avancées, recherche instrumentale des causes, selon l’algorithme de l’ERC.</p>')
a('BLS',[('B','Basic'),('L','Life'),('S','Support')],'Basic Life Support (réanimation de base)',
 '<p>Réanimation de base : reconnaissance, appel, compressions thoraciques, ventilations et utilisation d’un DAE, accessibles à tout témoin formé.</p>')

# ---- organismes
a('SRC',[('S','Swiss'),('R','Resuscitation'),('C','Council')],'Swiss Resuscitation Council (Conseil suisse de réanimation)',
 '<p>Organisation faîtière suisse de la réanimation ; elle adapte les recommandations de l’ERC et fixe les directives des cours reconnus en Suisse (directives de cours 2025, transition jusqu’au 31.12.2026).</p>')
a('ASSM',[('A','Académie'),('S','Suisse des'),('S','Sciences'),('M','Médicales')],'Académie suisse des sciences médicales',
 '<p>Institution qui publie les directives médico-éthiques suisses, notamment « Décisions de réanimation » (2021) et « Diagnostic de la mort en vue de la transplantation d’organes » (2017).</p>','i46-assm')
a('ILCOR',[('I','International'),('L','Liaison'),('C','Committee'),('O','On'),('R','Resuscitation')],'International Liaison Committee on Resuscitation',
 '<p>Comité international qui réunit les conseils de réanimation (dont l’ERC et l’American Heart Association) et publie les synthèses de preuves (CoSTR) sur lesquelles reposent les recommandations.</p>')
a('ESICM',[('E','European'),('S','Society of'),('I','Intensive'),('C','Care'),('M','Medicine')],'European Society of Intensive Care Medicine (Société européenne de médecine intensive)',
 '<p>Société savante européenne de médecine intensive ; coauteur, avec l’ERC, des recommandations 2025 sur les soins post-réanimation.</p>')
a('IAS',[('I','Inter-'),('A','Association de'),('S','Sauvetage')],'Interassociation de sauvetage',
 '<p>Organisation faîtière suisse du sauvetage ; elle gère notamment le registre Swissreca des arrêts cardiaques extrahospitaliers.</p>')
a('EuReCa',[('Eu','European'),('Re','Registry of'),('Ca','Cardiac arrest')],'European Registry of Cardiac Arrest',
 '<p>Études européennes de registre des arrêts extrahospitaliers menées selon le style d’Utstein (2014, 2017, 2022).</p>','i46-eureca')

# ---- mesures physiologiques
a('CO₂',[('C','Carbone'),('O₂','dioxyde (deux atomes d’Oxygène)')],'Dioxyde de carbone',
 '<p>Gaz produit par le métabolisme oxydatif et éliminé par les poumons ; sa présence dans l’air expiré pendant la réanimation reflète le débit pulmonaire.</p>','i46-capno')
a('EtCO₂',[('Et','End-tidal (en fin d’expiration)'),('CO₂','dioxyde de carbone')],'Dioxyde de carbone en fin d’expiration',
 '<p>Valeur du CO₂ mesurée à la fin de chaque expiration par capnographie ; normale 35–45 mmHg. Pendant la réanimation, elle confirme l’intubation, reflète la qualité des compressions et signale le RACS.</p>','i46-capno')
a('PaCO₂',[('P','Pression'),('a','artérielle'),('CO₂','en dioxyde de carbone')],'Pression artérielle partielle en dioxyde de carbone',
 '<p>Mesurée par gazométrie artérielle ; normale 35–45 mmHg. Elle règle le débit sanguin cérébral : cible de normocapnie après un arrêt cardiaque.</p>','i46-gds')
a('PaO₂',[('P','Pression'),('a','artérielle'),('O₂','en oxygène')],'Pression artérielle partielle en oxygène',
 '<p>Mesurée par gazométrie artérielle ; cible 75–100 mmHg après un arrêt cardiaque, en évitant l’hypoxie et l’hyperoxie.</p>','i46-gds')
a('PAM',[('P','Pression'),('A','Artérielle'),('M','Moyenne')],'Pression artérielle moyenne',
 '<p>Pression de perfusion moyenne des organes, environ diastolique + un tiers de la différentielle ; cible &gt; 60–65 mmHg après un arrêt cardiaque (ERC-ESICM 2025).</p>')
a('H⁺',[('H⁺','ion Hydrogène (proton)')],'Ion hydrogène',
 '<p>Proton libre ; sa concentration définit le pH. Il s’accumule pendant l’ischémie (lactate, CO₂).</p>')
a('HCO₃⁻',[('H','Hydrogène'),('C','Carbone'),('O₃','trois atomes d’Oxygène'),('⁻','charge négative')],'Ion bicarbonate',
 '<p>Principal tampon extracellulaire ; normal 22–26 mmol/L. Administré sous forme de bicarbonate de sodium dans l’hyperkaliémie et certaines intoxications.</p>','i46-d-bicar')
a('H₂CO₃',[('H₂','deux atomes d’Hydrogène'),('C','Carbone'),('O₃','trois atomes d’Oxygène')],'Acide carbonique',
 '<p>Intermédiaire instable entre le bicarbonate et le CO₂ : H⁺ + HCO₃⁻ ⇄ H₂CO₃ ⇄ CO₂ + H₂O.</p>')
a('H₂O',[('H₂','deux atomes d’Hydrogène'),('O','un atome d’Oxygène')],'Eau',
 '<p>Formule chimique de l’eau.</p>')
a('CA1',[('CA','Cornu Ammonis (corne d’Ammon)'),('1','secteur 1')],'Secteur CA1 de l’hippocampe (corne d’Ammon)',
 '<p>Région de l’hippocampe dont les neurones pyramidaux sont parmi les plus vulnérables à l’anoxie ; son atteinte explique les troubles mnésiques des survivants.</p>','i46-ischcereb')
a('NSE',[('N','Neuron-'),('S','Specific'),('E','Enolase')],'Énolase neuronale spécifique (neuron-specific enolase)',
 '<p>Enzyme glycolytique des neurones libérée lors de leur destruction ; &gt; 60 µg/L à 48 et/ou 72 heures est un critère défavorable après arrêt cardiaque (ERC-ESICM 2025). Faussement élevée en cas d’hémolyse.</p>','i46-nse')
a('PESS',[('P','Potentiels'),('E','Évoqués'),('SS','SomeSthésiques (les deux S du mot)')],'Potentiels évoqués somesthésiques',
 '<p>Réponses corticales à la stimulation du nerf médian ; l’absence bilatérale de l’onde N20 à 24 heures ou plus est un critère défavorable très spécifique.</p>','i46-pess')
a('N20',[('N','onde Négative'),('20','culminant vers 20 millisecondes')],'Onde N20 des potentiels évoqués somesthésiques',
 '<p>Réponse du cortex somesthésique primaire à la stimulation du nerf médian ; son absence bilatérale signe une lésion corticale étendue.</p>','i46-pess')
a('N9',[('N','onde Négative'),('9','vers 9 millisecondes')],'Onde N9 (plexus brachial)',
 '<p>Réponse périphérique enregistrée au point d’Erb ; sa présence prouve que la stimulation a été efficace.</p>','i46-pess')
a('N13',[('N','onde Négative'),('13','vers 13 millisecondes')],'Onde N13 (moelle cervicale)',
 '<p>Réponse de la moelle cervicale ; sa présence avec une N20 absente localise la lésion au-dessus du tronc cérébral.</p>','i46-pess')
a('EEG',[('E','Électro-'),('E','Encéphalo-'),('G','Gramme')],'Électroencéphalogramme',
 '<p>Enregistrement de l’activité électrique cérébrale ; après un arrêt cardiaque, un tracé hautement malin est un critère défavorable, un tracé continu et réactif un signe favorable.</p>','i46-eeg')
a('HOPE',[('H','Hypothermia'),('O','Outcome'),('P','Prediction after'),('E','ECLS (extracorporeal life support)')],'Score HOPE (prédiction de survie de l’hypothermie après réchauffement extracorporel)',
 '<p>Score qui estime la probabilité de survie d’un arrêt cardiaque hypothermique réchauffé par ECMO, à partir de l’âge, du sexe, du mécanisme (asphyxie ou non), de la durée de réanimation, de la kaliémie et de la température ; recommandé par l’ERC 2025 pour décider du réchauffement extracorporel.</p>','i46-hypoth')

# ---- essais cliniques
a('TTM',[('T','Targeted'),('T','Temperature'),('M','Management')],'Essai TTM (Targeted Temperature Management, 2013)',
 '<p>Essai randomisé comparant 33 °C et 36 °C après arrêt extrahospitalier : pas de différence de mortalité ni d’issue neurologique.</p>','i46-temp')
a('TTM2',[('TTM','Targeted Temperature Management'),('2','deuxième essai')],'Essai TTM2 (2021)',
 '<p>Hypothermie à 33 °C contre normothermie (cible ≤ 37,5 °C, dispositif de refroidissement si la température atteint 37,8 °C) : mortalité à 6 mois de 50 % contre 48 %, sans différence.</p>','i46-temp')
a('HACA',[('H','Hypothermia'),('A','After'),('C','Cardiac'),('A','Arrest')],'Essai HACA (Hypothermia After Cardiac Arrest, 2002)',
 '<p>Essai européen montrant une meilleure issue neurologique avec une hypothermie à 32–34 °C après arrêt par FV ; fondateur de la gestion de la température.</p>','i46-temp')
a('HYPERION',[('HYPERION','nom d’essai, non développable lettre à lettre')],'Essai HYPERION (2019)',
 '<p>Arrêts à rythme non choquable : meilleur devenir neurologique à 90 jours avec 33 °C qu’avec 37 °C (10,2 % contre 5,7 %).</p>','i46-temp')
a('COACT',[('COACT','COronary Angiography after Cardiac arrest Trial (acronyme non développable exactement lettre à lettre)')],'Essai COACT (2019)',
 '<p>Arrêt extrahospitalier sans sus-décalage du ST : la coronarographie immédiate n’améliore pas la survie à 90 jours par rapport à une coronarographie différée.</p>','i46-coro')
a('TOMAHAWK',[('TOMAHAWK','nom d’essai, non développable lettre à lettre')],'Essai TOMAHAWK (2021)',
 '<p>Arrêt extrahospitalier sans sus-décalage du ST : pas de bénéfice de la coronarographie immédiate, tendance défavorable sur la mortalité à 30 jours.</p>','i46-coro')
a('PARAMEDIC2',[('P','Prehospital'),('A','Assessment of the'),('R','Role of'),('A','Adrenaline:'),('M','Measuring the'),('E','Effectiveness of'),('D','Drug administration'),('I','In'),('C','Cardiac arrest'),('2','deuxième essai')],'Essai PARAMEDIC2 (2018)',
 '<p>Adrénaline contre placebo dans l’arrêt extrahospitalier : survie à 30 jours de 3,2 % contre 2,4 %, sans différence significative de survie avec bonne fonction neurologique.</p>','i46-d-adre')
a('PARAMEDIC-3',[('PARAMEDIC','nom de série repris de PARAMEDIC (voir cette entrée)'),('3','troisième essai de la série')],'Essai PARAMEDIC-3 (NEJM, en ligne 2024, imprimé 2025)',
 '<p>Voie intraosseuse contre voie intraveineuse en première intention dans l’arrêt extrahospitalier : pas de différence de survie à 30 jours.</p>','i46-acces')
a('PARAMEDIC',[('PA','Pre-hospitAl'),('RA','RAndomised assessment of a'),('ME','MEchanical compression'),('D','Device'),('I','In'),('C','Cardiac arrest')],'Essai PARAMEDIC (2015)',
 '<p>Compressions mécaniques contre manuelles dans l’arrêt extrahospitalier : pas de bénéfice sur la survie à 30 jours.</p>','i46-mecha')
a('IVIO',[('IV','IntraVeineuse'),('IO','IntraOsseuse')],'Essai IVIO (2024)',
 '<p>Essai danois : voie intraosseuse contre intraveineuse dans l’arrêt extrahospitalier ; pas de différence de RACS soutenu.</p>','i46-acces')
a('ALPS',[('A','Amiodarone,'),('L','Lidocaine, or'),('P','Placebo'),('S','Study')],'Essai ALPS (2016)',
 '<p>FV réfractaire : ni l’amiodarone ni la lidocaïne n’améliorent significativement la survie à la sortie par rapport au placebo ; bénéfice possible dans les arrêts devant témoin.</p>','i46-d-lido')
a('DOSE-VF',[('DO','DOuble'),('S','Sequential'),('E','External defibrillation'),('VF','for refractory Ventricular Fibrillation')],'Essai DOSE-VF (2022)',
 '<p>FV réfractaire : survie à la sortie de 30,4 % avec défibrillation séquentielle double, 21,7 % avec changement de vecteur, 13,3 % avec la défibrillation standard.</p>','i46-refract')
a('ARREST',[('ARREST','Advanced R2Eperfusion STrategies for Refractory Cardiac Arrest (acronyme non développable lettre à lettre)')],'Essai ARREST (2020)',
 '<p>FV réfractaire extrahospitalière, un centre de Minneapolis : survie à la sortie de 43 % avec RCP extracorporelle contre 7 % ; arrêt précoce pour efficacité.</p>','i46-ecpr')
a('OHCA',[('O','Out-of-'),('H','Hospital'),('C','Cardiac'),('A','Arrest')],'Out-of-hospital cardiac arrest (arrêt cardiaque extrahospitalier)',
 '<p>Terme anglais de l’ACEH ; utilisé ici dans le nom de l’essai Prague OHCA (2022) sur la RCP extracorporelle.</p>','i46-ecpr')
a('INCEPTION',[('INCEPTION','nom d’essai, non développable lettre à lettre')],'Essai INCEPTION (2023)',
 '<p>Essai multicentrique néerlandais et belge : RCP extracorporelle sans différence significative de survie avec bonne fonction neurologique à 30 jours.</p>','i46-ecpr')
a('AIRWAYS-2',[('AIRWAYS','nom d’essai'),('2','deuxième essai')],'Essai AIRWAYS-2 (2018)',
 '<p>Dispositif supraglottique contre intubation trachéale par des ambulanciers britanniques : pas de différence d’issue fonctionnelle à 30 jours.</p>','i46-ventil')
a('PART',[('P','Pragmatic'),('A','Airway'),('R','Resuscitation'),('T','Trial')],'Essai PART (2018)',
 '<p>Tube laryngé contre intubation trachéale par des ambulanciers américains : survie à 72 heures meilleure avec le tube laryngé.</p>','i46-ventil')
a('BOX',[('B','Blood pressure'),('OX','and OXygenation targets')],'Essai BOX (2022)',
 '<p>Après arrêt extrahospitalier : pas de différence entre une PAM cible de 63 et de 77 mmHg, ni entre une cible d’oxygénation basse et haute.</p>','i46-d-vaso')
a('TELSTAR',[('T','Treatment of'),('EL','ELectroencephalographic'),('ST','STatus epilepticus'),('A','After cardiopulmonary'),('R','Resuscitation')],'Essai TELSTAR (2022)',
 '<p>Traitement agressif des décharges EEG rythmiques et périodiques après arrêt cardiaque : pas d’amélioration de l’issue neurologique.</p>','i46-eeg')
a('COCA',[('C','Calcium for'),('O','Out-of-hospital'),('C','Cardiac'),('A','Arrest')],'Essai COCA (2021)',
 '<p>Calcium contre placebo dans l’arrêt extrahospitalier : pas de bénéfice, tendance défavorable ; arrêt prématuré.</p>')
a('LINC',[('L','LUCAS (dispositif de compression)'),('IN','IN'),('C','Cardiac arrest')],'Essai LINC (2014)',
 '<p>Compressions mécaniques associées à la défibrillation pendant les compressions contre RCP manuelle : pas de différence de survie à 4 heures.</p>','i46-mecha')
a('LUCAS',[('LUCAS','Lund University Cardiopulmonary Assist System')],'Dispositif de compressions mécaniques LUCAS',
 '<p>Dispositif à piston de compressions thoraciques mécaniques, évalué dans les essais LINC et PARAMEDIC.</p>','i46-mecha')
a('CIRC',[('C','Circulation'),('I','Improving'),('R','Resuscitation'),('C','Care')],'Essai CIRC (2014)',
 '<p>Compressions mécaniques par bande de répartition de charge contre RCP manuelle de haute qualité : équivalence de survie à la sortie.</p>','i46-mecha')
a('TROICA',[('TRO','ThROmbolysis'),('I','In'),('CA','Cardiac Arrest')],'Essai TROICA (2008)',
 '<p>Ténectéplase contre placebo dans l’arrêt extrahospitalier non sélectionné : pas de bénéfice. Justifie de réserver la fibrinolyse à l’embolie pulmonaire suspectée.</p>','i46-d-lyse')

a('pH',[('p','potentiel'),('H','Hydrogène')],'Potentiel hydrogène',
 '<p>Cologarithme de la concentration en ions H⁺ ; normal 7,35–7,45 dans le sang artériel. Pendant l’arrêt, l’acidose est mixte (lactique et respiratoire).</p>','i46-gds')
a('Lance-Adams',[('Lance-Adams','éponyme : James Lance et Raymond Adams, neurologues')],'Syndrome de Lance-Adams',
 '<p>Myoclonies d’action chroniques survenant après une anoxie cérébrale chez un patient qui a repris conscience ; compatible avec une bonne récupération, à distinguer de l’état de mal myoclonique précoce.</p>','i46-d-antiep')

a('ROSC',[('R','Return'),('O','Of'),('S','Spontaneous'),('C','Circulation')],'Return of spontaneous circulation (retour à une circulation spontanée)',
 '<p>Terme anglais du RACS, utilisé dans la littérature internationale.</p>','i46-spac')
a('CoSTR',[('Co','Consensus on'),('S','Science with'),('T','Treatment'),('R','Recommendations')],'Consensus on Science with Treatment Recommendations',
 '<p>Synthèses de preuves publiées par l’ILCOR, sur lesquelles l’ERC et l’American Heart Association fondent leurs recommandations.</p>')
a('ECLS',[('E','Extra-'),('C','Corporeal'),('L','Life'),('S','Support')],'Extracorporeal life support (assistance vitale extracorporelle)',
 '<p>Terme générique des assistances circulatoires extracorporelles, dont l’ECMO veino-artérielle.</p>','i46-ecpr')
a('Rega',[('Re','REttungsflugwacht (allemand)'),('ga','GArde aérienne (français)')],'Rega, Garde aérienne suisse de sauvetage',
 '<p>Fondation suisse de sauvetage héliporté, engagée notamment par la centrale 144.</p>')
