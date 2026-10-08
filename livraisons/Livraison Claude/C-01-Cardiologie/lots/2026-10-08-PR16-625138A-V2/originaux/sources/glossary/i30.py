# Glossaire MEDINA — chapitre I30 Péricardites, épanchement péricardique, tamponnade et constriction
from cardio_1 import a, G

def t(k, lit, full, d, ref=None):
    a(k, lit, full, d, ref)

# ---- notions et examens
a('IMPS',[('I','Inflammatory (inflammatoire)'),('M','Myo- (myocardique)'),('P','Pericardial (péricardique)'),('S','Syndrome')],'Inflammatory myopericardial syndrome (syndrome inflammatoire myopéricardique)',
 '<p>Terme parapluie introduit par l’ESC 2025 pour réunir péricardite, myopéricardite et myocardite, qui partagent leurs causes et se chevauchent souvent.</p>','i30-imps')
a('FASTE',[('F','Fièvre > 38 °C'),('A','Absence de réponse après une semaine d’anti-inflammatoire'),('S','installation Subaiguë'),('T','Tamponnade'),('E','Épanchement abondant > 20 mm')],'Aide-mémoire des critères majeurs de haut risque de la péricardite',
 '<p>Moyen mnémotechnique pédagogique, non critère officiel ; les critères eux-mêmes sont ceux de l’ESC 2015, repris par l’ESC 2025.</p>','i30-mnemo-faste')
a('TP',[('T','fin de l’onde T'),('P','début de l’onde P suivante')],'Segment TP de l’électrocardiogramme',
 '<p>Intervalle électrique de repos entre la fin de la repolarisation ventriculaire et la dépolarisation auriculaire suivante ; sert de ligne de base. Sa pente descendante (signe de Spodick) évoque une péricardite.</p>','i30-spodick')
a('ADN',[('A','Acide'),('D','Désoxyribo-'),('N','Nucléique')],'Acide désoxyribonucléique',
 '<p>Support de l’information génétique. Les anticorps anti-ADN natif sont très spécifiques du lupus érythémateux disséminé.</p>')
a('SARS-CoV-2',[('S','Severe (sévère)'),('A','Acute (aigu)'),('R','Respiratory (respiratoire)'),('S','Syndrome'),('Co','Corona-'),('V','Virus'),('2','de type 2')],'Coronavirus du syndrome respiratoire aigu sévère de type 2',
 '<p>Virus responsable du COVID-19 ; cause possible de péricardite et de myocardite, comme, plus rarement, les vaccins à ARN messager dirigés contre lui.</p>')
a('Epstein-Barr',[('Epstein-Barr','noms propres des découvreurs, Anthony Epstein et Yvonne Barr (1964) ; ce n’est pas une abréviation')],'Virus d’Epstein-Barr',
 '<p>Herpèsvirus humain de type 4, agent de la mononucléose infectieuse ; cause virale possible de péricardite.</p>')
a('JACC',[('J','Journal of the'),('A','American'),('C','College of'),('C','Cardiology')],'Journal of the American College of Cardiology',
 '<p>Revue de l’ACC ; elle a publié en 2025 le consensus américain sur le diagnostic et le traitement de la péricardite.</p>')
a('JAMA',[('J','Journal of the'),('A','American'),('M','Medical'),('A','Association')],'Journal of the American Medical Association',
 '<p>Revue médicale généraliste américaine ; elle a publié l’essai AIRTRIP (2016).</p>')
# ---- gènes
a('MEFV',[('ME','MEditerranean (méditerranéenne)'),('FV','FeVer (fièvre)')],'Gène de la fièvre méditerranéenne familiale',
 '<p>Code la pyrine, un régulateur de l’inflammasome. Ses variants causent la fièvre méditerranéenne familiale, de transmission autosomique récessive, qui peut se manifester par des péricardites récidivantes.</p>','i30-autoinfl')
a('TNFRSF1A',[('TNF','Tumor Necrosis Factor (facteur de nécrose tumorale)'),('R','Receptor (récepteur)'),('SF','SuperFamily (superfamille)'),('1A','membre 1A')],'Gène du récepteur de type 1 du facteur de nécrose tumorale',
 '<p>Ses variants causent un syndrome auto-inflammatoire de transmission autosomique dominante ; des variants de faible pénétrance sont retrouvés dans certaines péricardites récidivantes résistantes à la colchicine.</p>','i30-autoinfl')
a('BMC',[('B','BioMed'),('C','Central')],'BioMed Central','<p>Éditeur scientifique en libre accès ; sa revue <i>BMC Medicine</i> a publié en 2014 l’étude de Pandie sur le diagnostic de la péricardite tuberculeuse.</p>')
# ---- essais
t('COPE',[('CO','COlchicine for acute'),('PE','PEricarditis')],'Essai COPE (2005)',
 '<p>Colchicine for acute Pericarditis : colchicine ajoutée à l’aspirine dans un premier épisode de péricardite, réduction des récidives. Essai ouvert, italien.</p>','i30-d-colch')
t('ICAP',[('I','Investigation on'),('C','Colchicine for'),('A','Acute'),('P','Pericarditis')],'Essai ICAP (2013)',
 '<p>Essai randomisé en double aveugle (<i>New England Journal of Medicine</i>) : colchicine dans le premier épisode de péricardite ; péricardite incessante ou récidivante réduite de 37,5 % à 16,7 %.</p>','i30-d-colch')
t('CORE',[('CO','COlchicine for'),('RE','REcurrent pericarditis')],'Essai CORE (2005)',
 '<p>Colchicine dans la première récidive de péricardite, essai ouvert : réduction des nouvelles récidives.</p>','i30-d-colch')
t('CORP',[('CO','COlchicine for'),('R','Recurrent'),('P','Pericarditis')],'Essai CORP (2011)',
 '<p>Essai randomisé en double aveugle : colchicine dans la première récidive de péricardite, récidives réduites d’environ moitié.</p>','i30-d-colch')
t('CORP-2',[('CO','COlchicine for'),('R','Recurrent'),('P','Pericarditis'),('2','deuxième essai')],'Essai CORP-2 (2014)',
 '<p>Colchicine chez les patients ayant eu plusieurs récidives : récidives réduites de 42,5 % à 21,6 %.</p>','i30-d-colch')
t('COPPS',[('CO','COlchicine for the'),('P','Prevention of the'),('P','Post-pericardiotomy'),('S','Syndrome')],'Essai COPPS (2010)',
 '<p>Colchicine débutée après chirurgie cardiaque : réduction du syndrome post-péricardiotomie.</p>','i30-pcis')
t('COPPS-2',[('CO','COlchicine for the'),('P','Prevention of the'),('P','Post-pericardiotomy'),('S','Syndrome'),('2','deuxième essai (administration périopératoire)')],'Essai COPPS-2 (2014)',
 '<p>Colchicine périopératoire : réduction du syndrome post-péricardiotomie, au prix de davantage de troubles digestifs ; pas de réduction de la fibrillation auriculaire postopératoire.</p>','i30-pcis')
t('AIRTRIP',[('AIRTRIP','nom d’essai arrangé à partir de « Anakinra – Treatment of Recurrent Idiopathic Pericarditis », non strictement lettre à lettre')],'Essai AIRTRIP (2016)',
 '<p>Anakinra chez 21 patients avec péricardite récidivante corticodépendante et résistante à la colchicine : après retrait randomisé, récidive chez 18 % sous anakinra contre 90 % sous placebo (<i>JAMA</i>).</p>','i30-d-antiil1')
t('RHAPSODY',[('RHAPSODY','nom d’essai arrangé à partir de « Rilonacept inHibition of interleukin-1 Alpha and beta for recurrent Pericarditis: a pivotal Symptomatology and Outcomes stuDY », non strictement lettre à lettre')],'Essai RHAPSODY (2021)',
 '<p>Essai de phase 3 (<i>New England Journal of Medicine</i>) : rilonacept dans la péricardite récidivante active à protéine C réactive élevée ; après retrait randomisé, récidives fortement réduites (rapport de risque 0,04).</p>','i30-d-antiil1')
t('IMPI',[('IMPI','nom d’essai arrangé à partir de « Investigation of the Management of Pericarditis », non strictement lettre à lettre')],'Essai IMPI (2014)',
 '<p>Péricardite tuberculeuse en Afrique : la prednisolone a réduit la constriction et les hospitalisations sans réduire le critère principal, et a augmenté les cancers liés au VIH ; l’immunothérapie par <i>Mycobacterium indicus pranii</i> n’a pas eu d’effet.</p>','i30-tb')
