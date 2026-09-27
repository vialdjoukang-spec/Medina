from cardio_1 import a, G
for x in [
('HEp-2',[('H','Human'),('Ep','Epithelioma'),('2','lignée 2')],'Cellules HEp-2','<p>Lignée cellulaire humaine utilisée pour le dépistage des anticorps antinucléaires en immunofluorescence.</p>'),
('Sm',[('Sm','Smith (nom de la patiente)')],'Antigène Sm','<p>Protéines du complexe ribonucléoprotéique nucléaire ; anticorps anti-Sm très spécifiques du lupus.</p>'),
('SSA',[('S','Sjögren'),('S','Syndrome'),('A','antigène A (Ro)')],'Antigène SSA (Ro)','<p>Anticorps anti-SSA : Sjögren, lupus subaigu, lupus néonatal, bloc cardiaque congénital.</p>'),
('SSB',[('S','Sjögren'),('S','Syndrome'),('B','antigène B (La)')],'Antigène SSB (La)','<p>Anticorps souvent associés aux anti-SSA.</p>'),
('RNP',[('R','RiboNucléo'),('N','(nucléaire)'),('P','Protéine')],'Ribonucléoprotéine U1','<p>Anticorps anti-RNP : connectivite mixte.</p>'),
('SLEDAI-2K',[('S','Systemic'),('L','Lupus'),('E','Erythematosus'),('D','Disease'),('A','Activity'),('I','Index'),('2K','version 2000')],'Indice d’activité du lupus','<p>Score pondéré de 24 items sur 30 jours.</p>','m32-sledai'),
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
a('Euro-Lupus',[('Euro-Lupus','nom d’essai européen (cyclophosphamide à faible dose)')],'Schéma Euro-Lupus','<p>Cyclophosphamide 500 mg toutes les 2 semaines, 6 perfusions ; aussi efficace que les fortes doses avec moins de toxicité.</p>')
