# Glossaire MEDINA — R00 Palpitations, anomalies du rythme et souffles cardiaques (C-01-Cardiologie)
from cardio_1 import a, G

# ---- codes CIM-10-GM 2024 du cours
a('R00.0',[('R00','catégorie Anomalies du rythme cardiaque'),('.0','sous-code Tachycardie, sans précision')],'Tachycardie, sans précision (CIM-10-GM 2024)',
 '<p>Code d’un symptôme : tachycardie sinusale ou rythme rapide sans diagnostic précis. Il est remplacé par un code I47 ou I48 dès qu’une arythmie est documentée.</p>')
a('R00.1',[('R00','catégorie Anomalies du rythme cardiaque'),('.1','sous-code Bradycardie, sans précision')],'Bradycardie, sans précision (CIM-10-GM 2024)',
 '<p>Code d’un symptôme : bradycardie sinusale, sinoatriale ou vagale sans diagnostic précis ; un code de cause externe peut identifier un médicament responsable.</p>')
a('R00.2',[('R00','catégorie Anomalies du rythme cardiaque'),('.2','sous-code Palpitations')],'Palpitations (CIM-10-GM 2024)',
 '<p>Perception des battements cardiaques, codée tant qu’aucune arythmie ni cause précise n’est établie.</p>')
a('R00.3',[('R00','catégorie Anomalies du rythme cardiaque'),('.3','sous-code Activité électrique sans pouls')],'Activité électrique sans pouls, non classée ailleurs (CIM-10-GM 2024)',
 '<p>Activité électrique organisée sans pouls palpable ; l’arrêt cardiaque proprement dit est codé en I46.</p>')
a('R00.8',[('R00','catégorie Anomalies du rythme cardiaque'),('.8','sous-code Autres anomalies, non précisées')],'Anomalies du rythme cardiaque, autres et non précisées (CIM-10-GM 2024)',
 '<p>Code résiduel d’une irrégularité du rythme non caractérisée.</p>')
a('R01.0',[('R01','catégorie Souffles et autres bruits cardiaques'),('.0','sous-code Souffles bénins et anodins')],'Souffles cardiaques bénins et anodins (CIM-10-GM 2024)',
 '<p>Souffle fonctionnel ou innocent ; le code suppose que les critères du souffle innocent ont été vérifiés.</p>')
a('R01.1',[('R01','catégorie Souffles et autres bruits cardiaques'),('.1','sous-code Souffle, sans précision')],'Souffle cardiaque, sans précision (CIM-10-GM 2024)',
 '<p>Souffle, le plus souvent systolique, dont la cause n’est pas encore établie.</p>')
a('R01.2',[('R01','catégorie Souffles et autres bruits cardiaques'),('.2','sous-code Autres bruits cardiaques')],'Autres bruits cardiaques (CIM-10-GM 2024)',
 '<p>Bruits du cœur assourdis, augmentés ou diminués ; frottement précordial.</p>')

# ---- sociétés savantes
a('DGPK',[('D','Deutsche (allemande)'),('G','Gesellschaft (société)'),('P','für Pädiatrische (de pédiatrique)'),('K','Kardiologie (cardiologie)')],'Deutsche Gesellschaft für Pädiatrische Kardiologie (Société allemande de cardiologie pédiatrique et des cardiopathies congénitales)',
 '<p>Société savante allemande de cardiologie pédiatrique. Sa recommandation « Abklärung eines Herzgeräuschs » (adoptée le 29.11.2017, actualisation annoncée en 2025) sert de référence de langue allemande pour l’évaluation d’un souffle chez l’enfant.</p>')
