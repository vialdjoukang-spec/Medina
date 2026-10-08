# Glossaire MEDINA — chapitre I51 Complications des cardiopathies et atteintes cardiaques au cours d'autres maladies
from cardio_1 import a, G
from cardio_2 import t

# ---- essais cités
a('GUSTO-I',[('G','Global (mondiale)'),('U','Utilization (utilisation)'),('S','of Streptokinase (de la streptokinase)'),('T','and Tissue plasminogen activator (et de l’activateur tissulaire du plasminogène)'),('O','for Occluded coronary arteries (pour les artères coronaires occluses)'),('I','premier essai de la série')],'Global Utilization of Streptokinase and Tissue plasminogen activator for Occluded coronary arteries, premier essai',
 '<p>Essai de thrombolyse de l’infarctus. L’analyse secondaire de Crenshaw et collaborateurs (<i>Circulation</i> 2000;101:27–32) compare la mortalité des communications interventriculaires sans randomiser leur traitement médical ou chirurgical.</p>','i51-damluji')

# ---- repères ajoutés lors de la contrelecture ciblée
a('GEIST',[('GEIST','German Italian Spanish Takotsubo, registre allemand, italien et espagnol')],'German Italian Spanish Takotsubo registry',
 '<p>Registre observationnel du Tako-tsubo. La prescription de bêtabloquants à la sortie est associée à une moindre mortalité dans son analyse de 2025 ; l’absence de randomisation interdit d’attribuer cette différence au seul médicament.</p>','i51-consensus-ii')
a('HR',[('H','Hazard (risque instantané)'),('R','Ratio (rapport)')],'Hazard ratio, rapport des risques instantanés',
 '<p>Compare les vitesses instantanées de survenue d’un événement entre deux groupes. Ce rapport n’est ni un risque absolu ni une preuve de causalité ; son intervalle de confiance précise l’incertitude.</p>','i51-consensus-ii')
a('TVP',[('T','Thrombose'),('V','Veineuse'),('P','Profonde')],'Thrombose veineuse profonde',
 '<p>Un thrombus se forme dans une veine profonde. Les repères posologiques de son traitement par énoxaparine ne constituent pas une autorisation propre au thrombus ventriculaire gauche.</p>','i51-hbpm')
a('EP',[('E','Embolie'),('P','Pulmonaire')],'Embolie pulmonaire',
 '<p>Un embol veineux obstrue une artère pulmonaire. Son traitement curatif fournit un repère pour l’énoxaparine, à distinguer de l’extrapolation au thrombus ventriculaire.</p>','i51-hbpm')
a('TIH',[('T','Thrombopénie'),('I','Induite par'),('H','l’Héparine')],'Thrombopénie induite par l’héparine',
 '<p>Dans la forme immunologique, des anticorps activent les plaquettes et exposent à des thromboses malgré leur diminution. Une suspicion impose l’arrêt de toute héparine et une évaluation urgente d’un anticoagulant non héparinique.</p>','i51-tih')

# ---- classifications et codes
a('CIM-10-CM',[('C','Classification'),('I','Internationale des'),('M','Maladies'),('10','10e révision'),('CM','Clinical Modification (modification clinique américaine)')],'Classification internationale des maladies, 10e révision, modification clinique des États-Unis',
 '<p>Version américaine de la CIM-10, plus détaillée que la version de l’OMS. Elle réserve le code I51.81 au syndrome de Tako-tsubo ; elle ne s’applique pas en Suisse, qui utilise la CIM-10-GM.</p>','i51-codage-tts')
a('M32.1',[('M32.1','code CIM-10 : M32 = lupus érythémateux systémique ; .1 = lupus avec atteinte d’organes ou de systèmes')],'Code CIM-10 M32.1 : lupus érythémateux systémique avec atteinte viscérale',
 '<p>Employé avec un code astérisque I32.8 (péricardite) ou I39 (endocardite de Libman-Sacks) pour coder l’atteinte cardiaque du lupus.</p>','i51-libman')

# ---- études et essais
t('RIVAWAR',[('RIVA','RIVAroxaban'),('WAR','WARfarine')],'Essai RIVAWAR (2025)',
 '<p>Nom d’essai formé des premières syllabes des deux molécules comparées, non un sigle lettre à lettre. Essai randomisé ouvert de 261 patients : rivaroxaban contre warfarine pour un thrombus ventriculaire gauche après un infarctus ; résorption équivalente à 12 semaines.</p>','i51-meta-aod')
t('RED VELVT',[('RED VELVT','nom propre de l’étude ; son développement lettre à lettre n’a pas pu être vérifié lors de la rédaction')],'Étude RED VELVT (2020)',
 '<p>Étude observationnelle rétrospective qui associait les AOD à davantage d’embolies que l’antivitamine K dans le thrombus ventriculaire gauche ; résultat non confirmé par les essais randomisés.</p>','i51-redvelvt')
t('APEX-AMI',[('APEX','Assessment of PEXelizumab'),('AMI','in Acute Myocardial Infarction')],'Essai APEX-AMI (2007)',
 '<p>Essai du pexélizumab dans l’infarctus aigu traité par angioplastie primaire ; ses données ont servi à décrire le pronostic des ruptures de pilier opérées ou non.</p>','i51-pilier')
