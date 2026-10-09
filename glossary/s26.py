# Glossaire MEDINA — chapitre S26 Lésion traumatique du cœur (C-01-Cardiologie)
from cardio_1 import a, G

a('FAST',[('F','Focused (ciblée)'),('A','Assessment (évaluation)'),('S','with Sonography (par échographie)'),('T','in Trauma (en traumatologie)')],'Focused Assessment with Sonography in Trauma (échographie ciblée en traumatologie)',
 '<p>Échographie rapide faite au lit pendant l’examen primaire, qui recherche du liquide dans le péricarde, autour du foie et de la rate, et dans le pelvis.</p>','s26-fast')
a('EAST',[('E','Eastern'),('A','Association for the'),('S','Surgery of'),('T','Trauma')],'Eastern Association for the Surgery of Trauma (Association de chirurgie traumatologique de l’Est des États-Unis)',
 '<p>Société savante nord-américaine qui publie des recommandations de pratique en traumatologie ; ce cours cite celles de 2012 sur la contusion cardiaque et de 2015 sur la thoracotomie de réanimation.</p>','s26-east2012')
a('ATLS',[('A','Advanced'),('T','Trauma'),('L','Life'),('S','Support')],'Advanced Trauma Life Support (programme de prise en charge initiale du traumatisé de l’American College of Surgeons)',
 '<p>Programme de formation qui structure la prise en charge initiale du traumatisé en examen primaire et secondaire ; dixième édition publiée en 2018.</p>')
a('CRASH-2',[('CRASH','Clinical Randomisation of an Antifibrinolytic in Significant Haemorrhage'),('2','deuxième essai')],'Essai CRASH-2 (2010)',
 '<p>Essai randomisé de 20 211 blessés qui a montré que l’acide tranexamique réduisait la mortalité toutes causes (14,5 % contre 16,0 %) et la mortalité par hémorragie.</p>','s26-d-atx')

# ---- codes de la classification
for code,lib,txt in [
 ('S26.0','Hémopéricarde traumatique (CIM-10-GM 2024)','Accumulation traumatique de sang dans le péricarde, avec ou sans tamponnade.'),
 ('S26.81','Contusion du cœur (CIM-10-GM 2024)','Lésion du myocarde par traumatisme fermé, sans plaie de la paroi.'),
 ('S26.82','Plaie du cœur sans ouverture d’une cavité (CIM-10-GM 2024)','Plaie qui atteint le myocarde sans perforer une oreillette ni un ventricule.'),
 ('S26.83','Plaie du cœur avec ouverture d’une cavité (CIM-10-GM 2024)','Plaie qui perfore une oreillette ou un ventricule.'),
 ('S26.88','Autres lésions du cœur (CIM-10-GM 2024)','Lésions traumatiques du cœur non classées dans les sous-catégories précédentes, par exemple une rupture valvulaire.'),
 ('S26.9','Lésion du cœur, sans précision (CIM-10-GM 2024)','Code d’attente, remplacé dès que la nature de la lésion est connue.'),
 ('S21.83','Plaie ouverte du thorax avec lésion intrathoracique (CIM-10-GM 2024)','Code supplémentaire, marqué d’un point d’exclamation, ajouté à S26 lorsque la plaie thoracique communique avec la lésion du cœur.')]:
    a(code,[(code,'code de la classification internationale des maladies, '+lib.split(' (')[0][0].lower()+lib.split(' (')[0][1:])],lib,'<p>'+txt+'</p>','s26-codage')
