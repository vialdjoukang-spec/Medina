from cardio_1 import a, G
from cardio_2 import t
for k,lit,full,d in [
('VHB',[('V','Virus de l’'),('H','Hépatite'),('B','B')],'Virus de l’hépatite B','<p>Risque de réactivation sous immunosuppresseurs.</p>'),
('VHC',[('V','Virus de l’'),('H','Hépatite'),('C','C')],'Virus de l’hépatite C','<p>Cause d’arthralgies et de facteur rhumatoïde positif (cryoglobulinémie).</p>'),
('DAS28',[('D','Disease'),('A','Activity'),('S','Score'),('28','sur 28 articulations')],'Score d’activité de la maladie sur 28 articulations','<p>Score composite : 28 articulations douloureuses et gonflées, CRP ou vitesse de sédimentation, évaluation globale du patient. Ses seuils n’ont pas été relus dans une source primaire lors de la révision du 08.10.2026 ; le cours définit la rémission par le CDAI, le SDAI ou la définition booléenne 2022.</p>'),
('CDAI',[('C','Clinical'),('D','Disease'),('A','Activity'),('I','Index')],'Indice clinique d’activité','<p>Score sans biologie ; rémission ≤ 2,8.</p>'),
('SDAI',[('S','Simplified'),('D','Disease'),('A','Activity'),('I','Index')],'Indice simplifié d’activité','<p>Inclut la CRP ; rémission ≤ 3,3.</p>'),
('SCQM',[('S','Swiss'),('C','Clinical'),('Q','Quality'),('M','Management in rheumatic diseases')],'Registre suisse des maladies rhumatismales','<p>Registre national de qualité et de pharmacovigilance.</p>'),
('HLA-DRB1',[('HLA','Human Leukocyte Antigen'),('DRB1','locus DR, chaîne bêta 1')],'Gène HLA-DRB1','<p>Porte l’épitope partagé, facteur génétique de la polyarthrite rhumatoïde séropositive.</p>'),
('HLA-DR',[('HLA','Human Leukocyte Antigen'),('DR','locus DR')],'Molécules HLA de classe II de type DR','<p>Présentent les peptides aux lymphocytes T CD4.</p>'),
('PTPN22',[('PTP','Protein Tyrosine Phosphatase'),('N22','non-récepteur de type 22')],'Gène PTPN22','<p>Phosphatase du signal lymphocytaire ; locus de susceptibilité.</p>'),
('RANKL',[('R','Receptor Activator of'),('A','(activateur)'),('N','Nuclear factor'),('K','Kappa-B'),('L','Ligand')],'Ligand du récepteur activateur de NF-κB','<p>Active les ostéoclastes ; responsable des érosions.</p>'),
('IL-6',[('IL','InterLeukine'),('6','6')],'Interleukine 6','<p>Cytokine de l’inflammation systémique (CRP, fièvre, anémie) ; cible du tocilizumab et du sarilumab.</p>'),
('IL-1',[('IL','InterLeukine'),('1','1')],'Interleukine 1','<p>Cytokine pro-inflammatoire.</p>'),
('CD80',[('CD','Cluster of Differentiation'),('80','80')],'Molécule de costimulation CD80','<p>Portée par les cellules présentatrices ; cible indirecte de l’abatacept.</p>'),
('CD86',[('CD','Cluster of Differentiation'),('86','86')],'Molécule de costimulation CD86','<p>Portée par les cellules présentatrices.</p>'),
('CD28',[('CD','Cluster of Differentiation'),('28','28')],'Récepteur de costimulation CD28','<p>Sur les lymphocytes T.</p>'),
('HBs',[('H','Hépatite'),('B','B'),('s','antigène de surface')],'Antigène de surface du virus de l’hépatite B','<p>Marqueur d’infection active.</p>'),
('HBc',[('H','Hépatite'),('B','B'),('c','antigène de capside (core)')],'Antigène de capside du virus de l’hépatite B','<p>Les anticorps anti-HBc signalent une infection passée ou présente.</p>'),
('EIRA',[('E','Epidemiological'),('I','Investigation of'),('R','Rheumatoid'),('A','Arthritis')],'Étude suédoise EIRA','<p>Étude cas-témoins sur les facteurs de risque de la polyarthrite.</p>'),
('ORAL',[('ORAL','nom d’essai (programme du tofacitinib), non strictement lettre à lettre')],'Programme d’essais ORAL','<p>ORAL Surveillance (2022) : tofacitinib versus anti-TNF chez des patients à risque cardiovasculaire.</p>'),
('AA',[('A','Amylose'),('A','de type A (protéine amyloïde A sérique)')],'Amylose AA','<p>Amylose secondaire des inflammations chroniques.</p>')]:
    a(k,lit,full,d)
for c,tt in [('M06.0','Polyarthrite rhumatoïde séronégative')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],tt,'<p>Code CIM-10-GM.</p>')
a('TNF',[('T','Tumor'),('N','Necrosis'),('F','Factor')],'Facteur de nécrose tumorale','<p>Cytokine pro-inflammatoire centrale de la synovite ; « anti-TNF » désigne les biothérapies qui la bloquent.</p>')
a('Gougerot-Sjögren',[('Gougerot-Sjögren','nom propre : Henri Gougerot et Henrik Sjögren')],'Syndrome de Gougerot-Sjögren','<p>Maladie auto-immune des glandes exocrines (sécheresse oculaire et buccale).</p>')
a('DR4',[('DR','locus HLA-DR'),('4','spécificité 4')],'Antigène HLA-DR4','<p>Porte souvent l’épitope partagé.</p>')
a('DR1',[('DR','locus HLA-DR'),('1','spécificité 1')],'Antigène HLA-DR1','<p>Porte l’épitope partagé.</p>')
