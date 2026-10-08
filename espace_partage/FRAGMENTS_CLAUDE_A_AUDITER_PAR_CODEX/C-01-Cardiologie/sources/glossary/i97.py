# Glossaire MEDINA — chapitre I97 Troubles de l’appareil circulatoire après des actes médicaux (I97, I98, I99)
from cardio_1 import a, G

# ---- définitions et codes
a('MINS',[('M','Myocardial (myocardique)'),('I','Injury (lésion)'),('N','after Noncardiac (après chirurgie non cardiaque)'),('S','Surgery (chirurgie)')],'Lésion myocardique après chirurgie non cardiaque',
 '<p>Terme de la cohorte VISION : hausse postopératoire de la troponine attribuée à une ischémie coronaire, en l’absence d’autre cause cardiaque ou extracardiaque. Sous-ensemble de la lésion myocardique périopératoire définie par l’ESC 2022.</p>','i97-pmi')
a('T81.1',[('T81','catégorie CIM-10-GM des complications des actes à visée diagnostique et thérapeutique'),('.1','sous-catégorie du choc pendant ou après un acte')],'Choc pendant ou résultant d’un acte à visée diagnostique et thérapeutique (CIM-10-GM 2024)',
 '<p>Code du choc postopératoire, exclu de I97 par la CIM-10-GM.</p>')
a('A52.0',[('A52','catégorie CIM-10-GM de la syphilis tardive'),('.0','sous-catégorie de la syphilis cardiovasculaire')],'Syphilis cardiovasculaire (CIM-10-GM 2024)',
 '<p>Code d’étiologie (croix) associé à I98.0* pour une aortite syphilitique.</p>','i97-dague')
a('RCRI',[('R','Revised (révisé)'),('C','Cardiac (cardiaque)'),('R','Risk (de risque)'),('I','Index (indice)')],'Indice de risque cardiaque révisé (Lee, 1999)',
 '<p>Six critères d’un point : cardiopathie ischémique, maladie cérébrovasculaire, insuffisance cardiaque, diabète sous insuline, créatinine &gt; 177 µmol/L, chirurgie à haut risque.</p>','i97-rcri')
a('DASI',[('D','Duke (université Duke)'),('A','Activity (activité)'),('S','Status (état)'),('I','Index (indice)')],'Indice d’activité de Duke',
 '<p>Questionnaire de douze activités quotidiennes, score de 0 à 58,2 ; un score inférieur à 34 s’associe à davantage de décès ou d’infarctus à 30 jours après chirurgie non cardiaque.</p>','i97-dasi')
a('ESAIC',[('E','European (européenne)'),('S','Society of (société d’)'),('A','Anaesthesiology (anesthésiologie)'),('I','and Intensive (et de soins intensifs)'),('C','Care')],'Société européenne d’anesthésiologie et de soins intensifs',
 '<p>Société qui a approuvé les recommandations ESC 2022 sur la chirurgie non cardiaque.</p>')
a('ELSO',[('E','Extracorporeal (extracorporelle)'),('L','Life (vie)'),('S','Support (assistance)'),('O','Organization (organisation)')],'Organisation pour l’assistance vitale extracorporelle',
 '<p>Société savante internationale et registre de l’assistance par ECMO, coautrice du consensus 2020 sur l’assistance postcardiotomie.</p>')
a('AATS',[('A','American (américaine)'),('A','Association for (association de)'),('T','Thoracic (chirurgie thoracique)'),('S','Surgery')],'American Association for Thoracic Surgery (Association américaine de chirurgie thoracique)',
 '<p>Coautrice du consensus 2020 sur l’assistance circulatoire postcardiotomie.</p>')

# ---- essais et cohortes (noms non strictement lettre à lettre lorsque précisé)
a('VISION',[('V','Vascular events (événements vasculaires)'),('I','In noncardiac (en chirurgie non cardiaque)'),('S','Surgery'),('I','patIents (patients)'),('O','cOhort (cohorte)'),('N','evaluatioN (évaluation)')],'Cohorte VISION (nom d’étude, non strictement lettre à lettre)',
 '<p>Cohorte internationale prospective de patients de 45 ans ou plus opérés d’une chirurgie non cardiaque, avec dosage systématique de la troponine ; elle a défini la MINS (8,0 % des 15 065 patients de 2014).</p>','i97-pmi')
a('BASEL-PMI',[('BASEL','ville de Bâle (nom de lieu, non une abréviation)'),('P','Perioperative (périopératoire)'),('M','Myocardial (myocardique)'),('I','Injury (lésion)')],'Étude bâloise sur la lésion myocardique périopératoire',
 '<p>Étude prospective de Bâle (2014–2015) : lésion après 16 % des interventions, mortalité à 30 jours 8,9 % contre 1,5 %.</p>','i97-basel')
a('MANAGE',[('MANAGE','nom d’essai (Management of myocardial injury After NoncArdiac surGEry), non strictement lettre à lettre')],'Essai MANAGE (2018)',
 '<p>Dabigatran 110 mg deux fois par jour contre placebo après une lésion myocardique ischémique postopératoire : complications vasculaires majeures 11 % contre 15 %.</p>','i97-manage')
a('POISE',[('P','Peri- (péri-)'),('O','Operative (opératoire)'),('IS','ISchemic (ischémique)'),('E','Evaluation (évaluation)')],'Programme d’essais POISE (nom non strictement lettre à lettre)',
 '<p>Série d’essais randomisés en chirurgie non cardiaque : métoprolol (POISE-1), aspirine et clonidine (POISE-2), acide tranexamique et stratégies tensionnelles (POISE-3).</p>','i97-poise')
a('POISE-1',[('POISE','PeriOperative ISchemic Evaluation (évaluation ischémique périopératoire)'),('1','premier essai')],'Essai POISE-1 (2008)',
 '<p>Métoprolol à libération prolongée 200 mg débuté 2 à 4 heures avant l’intervention : moins d’infarctus, mais plus de décès et d’AVC.</p>','i97-poise')
a('POISE-2',[('POISE','PeriOperative ISchemic Evaluation (évaluation ischémique périopératoire)'),('2','deuxième essai')],'Essai POISE-2 (2014)',
 '<p>Aspirine périopératoire : aucun effet sur les décès ni les infarctus, davantage de saignements majeurs.</p>','i97-poise')
a('POISE-3',[('POISE','PeriOperative ISchemic Evaluation (évaluation ischémique périopératoire)'),('3','troisième essai')],'Essai POISE-3 (2022–2023)',
 '<p>Stratégie d’évitement de l’hypotension contre stratégie d’évitement de l’hypertension : 13,9 % contre 14,0 % de complications vasculaires majeures.</p>','i97-poise3')
a('CARP',[('C','Coronary (coronaire)'),('A','Artery (artère)'),('R','Revascularization (revascularisation)'),('P','Prophylaxis (prophylactique)')],'Essai CARP (2004)',
 '<p>Revascularisation coronaire prophylactique avant chirurgie vasculaire : aucun bénéfice sur l’infarctus à 30 jours ni sur la mortalité à long terme.</p>','i97-carp')
a('MOST',[('MO','MOde (mode)'),('S','Selection (choix)'),('T','Trial (essai)')],'Essai MOST (choix du mode de stimulation)',
 '<p>Essai de stimulation chez des patients atteints de maladie du sinus ; 18,3 % des patients stimulés en mode VVIR ont présenté un syndrome du stimulateur.</p>','i97-pm-syndrome')
a('POPE',[('P','Post-'),('O','Operative (opératoire)'),('P','Pericardial (péricardique)'),('E','Effusion (épanchement)')],'Essai POPE (diclofénac et épanchement péricardique postopératoire)',
 '<p>Le diclofénac n’a pas réduit les épanchements péricardiques postopératoires asymptomatiques et a exposé à des effets indésirables.</p>')
a('LOAD',[('LOAD','nom d’essai (« charge » en anglais : Lowering the risk of Operative complications using Atorvastatin loading Dose), non strictement lettre à lettre')],'Essai LOAD (dose de charge d’atorvastatine avant chirurgie non cardiaque)',
 '<p>La dose de charge d’atorvastatine n’a pas réduit les événements cardiovasculaires majeurs postopératoires.</p>')

# ---- noms propres composés
a('Schulz-Menger',[('Schulz-Menger','nom de l’autrice (Jeanette Schulz-Menger), non une abréviation')],'Jeanette Schulz-Menger, coprésidente des recommandations ESC 2025 sur les myocardites et les péricardites','')
