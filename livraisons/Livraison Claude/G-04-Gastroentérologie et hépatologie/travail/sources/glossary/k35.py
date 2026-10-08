# Glossaire MEDINA — K35 Appendicite (G-04-Gastroentérologie et hépatologie), rédaction Claude du 08.10.2026
from cardio_1 import a, G
# Dépendances : WSES et G-04-Gastroentérologie sont définies dans glossary/k25.py (même zone de travail) et ne sont pas redéfinies ici.
# Collision possible : APPAC, CODA ou McBurney pourraient être définies par K65 ou R10 ; garder une seule définition à l’intégration.

a('CODA',[('C','Comparison of'),('O','Outcomes of antibiotic'),('D','Drugs and'),('A','Appendectomy')],'Essai CODA (Comparison of Outcomes of antibiotic Drugs and Appendectomy, 2020)',
 '<p>Essai randomisé pragmatique de 1552 adultes dans 25 centres américains : antibiotiques non inférieurs à l’appendicectomie pour la qualité de vie à 30 jours ; 29 % d’appendicectomies à 90 jours dans le groupe antibiotique.</p>','k35-coda')
a('APPAC',[('APP','APPendicitis'),('AC','ACuta')],'Essais finlandais APPAC (Appendicitis Acuta)',
 '<p>Série d’essais randomisés finlandais sur l’appendicite simple confirmée par tomodensitométrie : APPAC (antibiotiques contre appendicectomie), APPAC II (antibiotique oral contre intraveineux), APPAC III (antibiotique contre placebo), APPAC IV (en cours).</p>','k35-appac')
a('PSOGI',[('P','Peritoneal'),('S','Surface'),('O','Oncology'),('G','Group'),('I','International')],'Peritoneal Surface Oncology Group International (groupe international d’oncologie des surfaces péritonéales)',
 '<p>Groupe qui a publié en 2016 le consensus de classification des néoplasies mucineuses de l’appendice et du pseudomyxome péritonéal.</p>','k35-lamn')
a('ENETS',[('E','European'),('NE','NeuroEndocrine'),('T','Tumor'),('S','Society')],'European Neuroendocrine Tumor Society (Société européenne des tumeurs neuroendocrines)',
 '<p>Société savante européenne ; son guide de 2023 encadre la prise en charge des tumeurs neuroendocrines de l’appendice.</p>','k35-tne')
a('LAMN',[('L','Low-grade (de bas grade)'),('A','Appendiceal (appendiculaire)'),('M','Mucinous (mucineuse)'),('N','Neoplasm (néoplasie)')],'Néoplasie mucineuse appendiculaire de bas grade',
 '<p>Tumeur mucineuse de l’appendice à atypies de bas grade, sans invasion infiltrante ; sa rupture peut provoquer un pseudomyxome péritonéal (consensus PSOGI 2016).</p>','k35-lamn')
a('HAMN',[('H','High-grade (de haut grade)'),('A','Appendiceal (appendiculaire)'),('M','Mucinous (mucineuse)'),('N','Neoplasm (néoplasie)')],'Néoplasie mucineuse appendiculaire de haut grade',
 '<p>Tumeur mucineuse à atypies de haut grade sans invasion infiltrante, catégorie créée par le consensus PSOGI 2016.</p>','k35-lamn')
a('KRAS',[('K','Kirsten'),('RAS','RAt Sarcoma (sarcome de rat, famille des petites protéines G)')],'Gène KRAS (oncogène viral du sarcome de rat de Kirsten)',
 '<p>Gène d’une petite protéine G de la voie de prolifération ; muté dans 40 % des néoplasies mucineuses appendiculaires disséminées d’une série de 2014.</p>','k35-lamn')
a('GNAS',[('GNAS','Guanine Nucleotide binding protein, Alpha Stimulating (sous-unité alpha stimulatrice de la protéine G liant les nucléotides guanyliques) ; sigle de gène, non strictement lettre à lettre')],'Gène GNAS (sous-unité alpha de la protéine Gs)',
 '<p>Ses mutations du codon 201 bloquent l’extinction de la protéine Gs et maintiennent l’AMPc élevé ; mutées dans 31 % des néoplasies mucineuses appendiculaires disséminées d’une série de 2014.</p>','k35-lamn')
a('MANTRELS',[('M','Migration'),('A','Anorexia'),('N','Nausea'),('T','Tenderness'),('R','Rebound'),('E','Elevated temperature'),('L','Leukocytosis'),('S','Shift to the left')],'Moyen mnémotechnique anglais du score d’Alvarado',
 '<p>Aide pédagogique, non critère officiel : migration, anorexie, nausées, douleur provoquée, décompression, fièvre, leucocytose, déviation à gauche.</p>','k35-alvarado')
a('McBurney',[('McBurney','nom propre du chirurgien américain Charles McBurney (1845–1913), non abréviation')],'Point de McBurney',
 '<p>Point situé à la jonction du tiers latéral et des deux tiers médiaux de la ligne qui joint l’épine iliaque antéro-supérieure droite à l’ombilic.</p>','k35-mcburney')

# Codes CIM-10-GM 2024 à décimale (bloc K35–K38, BfArM)
a('K35.2',[('K35.2','code CIM-10-GM 2024')],'Appendicite aiguë avec péritonite généralisée','<p>Appendicite avec péritonite généralisée (diffuse) après perforation ou rupture.</p>')
a('K35.30',[('K35.30','code CIM-10-GM 2024')],'Appendicite aiguë avec péritonite localisée, sans perforation ni rupture','<p>Sous-code de K35.3- (péritonite localisée).</p>')
a('K35.31',[('K35.31','code CIM-10-GM 2024')],'Appendicite aiguë avec péritonite localisée, avec perforation ou rupture','<p>Sous-code de K35.3- (péritonite localisée).</p>')
a('K35.32',[('K35.32','code CIM-10-GM 2024')],'Appendicite aiguë avec abcès péritonéal','<p>Sous-code de K35.3- ; correspond aux abcès péri-appendiculaires.</p>')
a('K35.8',[('K35.8','code CIM-10-GM 2024')],'Appendicite aiguë, sans précision','<p>Appendicite aiguë sans mention de péritonite localisée ou généralisée.</p>')
a('K38.0',[('K38.0','code CIM-10-GM 2024')],'Hyperplasie de l’appendice','<p>Catégorie K38, autres maladies de l’appendice.</p>')
a('K38.1',[('K38.1','code CIM-10-GM 2024')],'Concrétions appendiculaires','<p>Fécalome, stercolithe de l’appendice.</p>')
a('K38.2',[('K38.2','code CIM-10-GM 2024')],'Diverticule de l’appendice','<p>Catégorie K38, autres maladies de l’appendice.</p>')
a('K38.3',[('K38.3','code CIM-10-GM 2024')],'Fistule de l’appendice','<p>Catégorie K38, autres maladies de l’appendice.</p>')
a('K38.8',[('K38.8','code CIM-10-GM 2024')],'Autres maladies précisées de l’appendice','<p>Comprend l’invagination de l’appendice.</p>')
a('K38.9',[('K38.9','code CIM-10-GM 2024')],'Maladie de l’appendice, sans précision','<p>Code de dernier recours de la catégorie K38.</p>')
