from cardio_1 import a, G
for x in [
('HEp-2',[('H','Human'),('Ep','Epithelioma'),('2','lignée 2')],'Cellules HEp-2','<p>Lignée cellulaire humaine utilisée pour le dépistage des anticorps antinucléaires en immunofluorescence.</p>'),
('Sm',[('Sm','Smith (nom de la patiente)')],'Antigène Sm','<p>Protéines du complexe ribonucléoprotéique nucléaire ; anticorps anti-Sm très spécifiques du lupus.</p>'),
('SSA',[('S','Sjögren'),('S','Syndrome'),('A','antigène A (Ro)')],'Antigène SSA (Ro)','<p>Anticorps anti-SSA : Sjögren, lupus subaigu, lupus néonatal, bloc cardiaque congénital.</p>'),
('SSB',[('S','Sjögren'),('S','Syndrome'),('B','antigène B (La)')],'Antigène SSB (La)','<p>Anticorps souvent associés aux anti-SSA.</p>'),
('RNP',[('R','RiboNucléo'),('N','(nucléaire)'),('P','Protéine')],'Ribonucléoprotéine U1','<p>Anticorps anti-RNP : connectivite mixte.</p>'),
('SLEDAI-2K',[('S','Systemic'),('L','Lupus'),('E','Erythematosus'),('D','Disease'),('A','Activity'),('I','Index'),('2K','version 2000')],'Indice d’activité du lupus','<p>Indice pondéré d’activité du lupus, cité par l’EULAR 2023 parmi les instruments validés.</p>','m32-sledai'),
('SLICC',[('S','Systemic'),('L','Lupus'),('I','International'),('C','Collaborating'),('C','Clinics')],'Groupe SLICC','<p>Auteur de l’indice de dommage et de critères de classification (2012).</p>','m32-sledai'),
('ISN',[('I','International'),('S','Society of'),('N','Nephrology')],'Société internationale de néphrologie','<p>Coauteur de la classification ISN/RPS de la néphrite lupique.</p>'),
('RPS',[('R','Renal'),('P','Pathology'),('S','Society')],'Société de pathologie rénale','<p>Coauteur de la classification ISN/RPS.</p>'),
('BLyS',[('B','B-'),('Ly','Lymphocyte'),('S','Stimulator')],'Facteur de stimulation des lymphocytes B','<p>Facteur de survie des lymphocytes B ; cible du bélimumab.</p>','m32-d-bio'),
('TPMT',[('T','Thiopurine'),('P','(S-)'),('M','Méthyl'),('T','Transférase')],'Thiopurine méthyltransférase','<p>Enzyme d’inactivation de l’azathioprine ; déficit = toxicité médullaire.</p>'),
('LDH',[('L','Lactate'),('D','DésHydrogénase'),('H','(enzyme)')],'Lactate déshydrogénase','<p>Élevée dans l’hémolyse et les lésions cellulaires.</p>'),
('IRF5',[('I','Interferon'),('R','Regulatory'),('F','Factor'),('5','5')],'Facteur régulateur de l’interféron 5','<p>Gène de susceptibilité au lupus.</p>'),
('STAT4',[('STAT','Signal Transducer and Activator of Transcription'),('4','4')],'Facteur STAT4','<p>Gène de susceptibilité au lupus.</p>'),
('TREX1',[('TREX','Three prime Repair EXonuclease'),('1','1')],'Exonucléase TREX1','<p>Ses mutations causent des formes monogéniques de lupus.</p>'),
('TLR7',[('T','Toll-'),('L','Like'),('R','Receptor'),('7','7')],'Récepteur Toll 7','<p>Capteur d’ARN endosomal ; gène sur le chromosome X.</p>'),
('DR2',[('DR','locus HLA-DR'),('2','spécificité 2')],'Antigène HLA-DR2','<p>Allèle de susceptibilité au lupus.</p>'),
('DR3',[('DR','locus HLA-DR'),('3','spécificité 3')],'Antigène HLA-DR3','<p>Allèle de susceptibilité au lupus.</p>'),
('BLISS-LN',[('BLISS','nom d’essai (bélimumab dans le lupus)'),('LN','Lupus Nephritis')],'Essai BLISS-LN (2020)','<p>Bélimumab ajouté au traitement standard de la néphrite : meilleure réponse rénale.</p>'),
('TULIP',[('TULIP','Treatment of Uncontrolled Lupus via the Interferon Pathway')],'Essais TULIP','<p>Anifrolumab dans le lupus actif.</p>')]:
    a(*x)
a('ENA',[('E','Extractable'),('N','Nuclear'),('A','Antigens')],'Antigènes nucléaires solubles','<p>Groupe d’antigènes (Sm, RNP, SSA, SSB, Scl-70, Jo-1…) recherchés après des anticorps antinucléaires positifs.</p>')
a('Euro-Lupus',[('Euro-Lupus','nom d’essai européen (cyclophosphamide à faible dose)')],'Schéma Euro-Lupus','<p>Cyclophosphamide 500 mg toutes les 2 semaines, 6 perfusions (3 g cumulés), suivi d’azathioprine ; résultats comparables au schéma à forte dose dans l’essai européen de 2002.</p>')

a('NUDT15',[('NUDT','Nudix hydrolase'),('15','15')],'Nudix hydrolase 15','<p>Enzyme qui participe à l’inactivation de métabolites thiopuriniques. Des variants réduisant sa fonction augmentent la susceptibilité à une toxicité hématologique ; la surveillance sanguine reste nécessaire.</p>')
a('EDTA',[('E','European'),('D','Dialysis and'),('T','Transplant'),('A','Association')],'European Dialysis and Transplant Association (Association européenne de dialyse et de transplantation)','<p>Ancien nom de l’association européenne de néphrologie ; coautrice, avec l’EULAR, des recommandations EULAR/ERA-EDTA 2019 sur la néphrite lupique.</p>')
a('BILAG',[('B','British'),('I','Isles'),('L','Lupus'),('A','Assessment'),('G','Group')],'Indice BILAG','<p>Instrument d’activité du lupus par organe, élaboré par le groupe britannique d’évaluation du lupus ; cité par l’EULAR 2023 parmi les instruments validés.</p>','m32-sledai')
a('CellCept',[('CellCept','nom commercial du mycophénolate mofétil (nom propre, non abréviatif)')],'CellCept®','<p>Nom commercial suisse du mycophénolate mofétil, autorisé dans la prévention du rejet de greffe.</p>')
a('SSCS',[('S','Swiss'),('S','Systemic lupus erythematosus'),('C','Cohort'),('S','Study')],'Cohorte suisse du lupus érythémateux systémique','<p>Cohorte nationale multicentrique, ouverte en 2007, qui suit les patients lupiques en immunologie clinique, médecine interne, néphrologie et rhumatologie.</p>')
