from cardio_1 import a, G
L=[
('PR3',[('P','Protéinase'),('R','(sérine protéase)'),('3','3')],'Protéinase 3','<p>Enzyme des granules des neutrophiles ; cible des ANCA de la granulomatose avec polyangéite.</p>','m31-anca'),
('MPO',[('M','Myélo'),('P','Per'),('O','Oxydase')],'Myéloperoxydase','<p>Enzyme des granules des neutrophiles ; cible des ANCA de la polyangéite microscopique.</p>','m31-anca'),
('BVAS',[('B','Birmingham'),('V','Vasculitis'),('A','Activity'),('S','Score')],'Score d’activité de Birmingham','<p>Score d’activité des vascularites ; 0 = rémission.</p>','m31-bvas'),
('FDG',[('F','Fluoro'),('D','Désoxy'),('G','Glucose')],'Fluorodésoxyglucose (¹⁸F)','<p>Traceur de la tomographie par émission de positons ; se concentre dans les tissus inflammatoires.</p>'),
('PRINTO',[('PR','Paediatric Rheumatology'),('IN','INternational'),('T','Trials'),('O','Organisation')],'Organisation internationale d’essais en rhumatologie pédiatrique','<p>Coautrice des critères EULAR/PRINTO/PReS 2010.</p>'),
# Sigle officiel « PReS » (e minuscule) : distinct de la clé « PRES » (syndrome d’encéphalopathie postérieure réversible, chapitre I10).
('PReS',[('P','Paediatric'),('R','Rheumatology'),('e','European'),('S','Society')],'Paediatric Rheumatology European Society (Société européenne de rhumatologie pédiatrique)','<p>Société savante européenne de rhumatologie pédiatrique ; coautrice, avec l’EULAR et la PRINTO, des critères de classification des vascularites de l’enfant (conférence de consensus d’Ankara 2008, publiés en 2010) : vascularite à IgA, périartérite noueuse, granulomatose avec polyangéite et artérite de Takayasu de l’enfant.</p>'),
('GiACTA',[('GiACTA','Giant-cell Arteritis Actemra (nom d’essai, non strictement lettre à lettre)')],'Essai GiACTA (2017)','<p>Tocilizumab dans l’artérite à cellules géantes.</p>','m31-d-toci'),
('RAVE',[('R','Rituximab in'),('A','ANCA-Associated'),('V','Vasculitis'),('E','(essai)')],'Essai RAVE (2010)','<p>Rituximab non inférieur au cyclophosphamide pour l’induction.</p>','m31-d-ritux'),
('PEXIVAS',[('PEXIVAS','Plasma EXchange and glucocorticoids in severe ANCA-associated VASculitis')],'Essai PEXIVAS (2020)','<p>Échanges plasmatiques sans bénéfice global sur la mort ou la dialyse terminale ; schéma réduit de corticostéroïdes aussi efficace et moins infectieux.</p>'),
('ADVOCATE',[('ADVOCATE','nom d’essai (avacopan dans les vascularites à ANCA)')],'Essai ADVOCATE (2021)','<p>Avacopan versus prednisone.</p>','m31-d-avaco'),
('MAINRITSAN',[('MAINRITSAN','MAINtenance of remission using RITuximab in Systemic ANCA-associated vasculitis')],'Essai MAINRITSAN (2014)','<p>Rituximab supérieur à l’azathioprine en entretien.</p>','m31-d-ritux'),
('MIRRA',[('MIRRA','Mepolizumab In Relapsing or Refractory EGPA (non strictement lettre à lettre)')],'Essai MIRRA (2017)','<p>Mépolizumab dans la granulomatose éosinophilique récidivante ou réfractaire.</p>'),
('MANDARA',[('MANDARA','nom d’essai (benralizumab versus mépolizumab dans la granulomatose éosinophilique)')],'Essai MANDARA (2024)','<p>Benralizumab non inférieur au mépolizumab.</p>'),
('HLA-B51',[('HLA','Human Leukocyte Antigen'),('B51','antigène B51')],'Antigène HLA-B51','<p>Associé à la maladie de Behçet.</p>'),
('HLA-DP',[('HLA','Human Leukocyte Antigen'),('DP','locus DP')],'Molécules HLA-DP','<p>Associées aux vascularites à anti-PR3.</p>'),
('HLA-DQ',[('HLA','Human Leukocyte Antigen'),('DQ','locus DQ')],'Molécules HLA-DQ','<p>Associées aux vascularites à anti-MPO.</p>'),
('HLA-DRB1*04',[('HLA','Human Leukocyte Antigen'),('DRB1*04','allèle DRB1*04')],'Allèle HLA-DRB1*04','<p>Associé à l’artérite à cellules géantes.</p>'),
('PRTN3',[('PRTN','PRoTéiNase'),('3','3 (gène)')],'Gène de la protéinase 3','<p>Locus associé aux vascularites à anti-PR3.</p>'),
('ADA2',[('A','Adénosine'),('D','Désaminase'),('A2','de type 2')],'Adénosine désaminase 2','<p>Son déficit génétique mime une périartérite noueuse précoce ; traitement par anti-TNF.</p>'),
('DADA2',[('D','Déficit en'),('ADA2','adénosine désaminase 2')],'Déficit en adénosine désaminase 2','<p>Vasculopathie autosomique récessive.</p>'),
('PD-L1',[('P','Programmed'),('D','Death'),('L1','Ligand 1')],'Ligand 1 de la mort programmée','<p>Point de contrôle inhibiteur de l’immunité.</p>'),
('VEGF',[('V','Vascular'),('E','Endothelial'),('G','Growth'),('F','Factor')],'Facteur de croissance de l’endothélium vasculaire','<p>Stimule l’angiogenèse.</p>'),
('PDGF',[('P','Platelet-'),('D','Derived'),('G','Growth'),('F','Factor')],'Facteur de croissance dérivé des plaquettes','<p>Stimule la prolifération des cellules musculaires lisses.</p>'),
('NET',[('N','Neutrophil'),('E','Extracellular'),('T','Traps')],'Pièges extracellulaires des neutrophiles','<p>Filets d’ADN et de protéines granulaires libérés par les neutrophiles activés.</p>'),
('C5aR1',[('C5a','fragment C5a du complément'),('R1','Récepteur de type 1')],'Récepteur 1 du C5a','<p>Cible de l’avacopan.</p>','m31-d-avaco'),
('C5a',[('C','Complément'),('5a','fragment a du composant 5')],'Fragment C5a du complément','<p>Anaphylatoxine chimiotactique pour les neutrophiles.</p>'),
('SARS-CoV-2',[('S','Severe'),('A','Acute'),('R','Respiratory'),('S','Syndrome'),('CoV','CoronaVirus'),('2','2')],'Coronavirus du syndrome respiratoire aigu sévère 2','<p>Virus de la COVID-19.</p>'),
]
for x in L: a(*x)
for k,tt in [('Ehlers-Danlos','Edvard Ehlers et Henri-Alexandre Danlos')]:
    a(k,[(k,'nom propre : '+tt)],'Syndrome d’'+k,'<p>Maladies héréditaires du tissu conjonctif ; la forme vasculaire expose aux ruptures artérielles.</p>')
for c,tt in [('M30.0','Périartérite noueuse'),('M30.1','Polyartérite avec atteinte pulmonaire (granulomatose éosinophilique avec polyangéite)'),('M30.3','Syndrome lympho-cutanéo-muqueux (maladie de Kawasaki)'),('M31.0','Angéite d’hypersensibilité'),('M31.1','Microangiopathie thrombotique'),('M31.3','Granulomatose avec polyangéite'),('M31.4','Syndrome de la crosse aortique (Takayasu)'),('M31.5','Artérite à cellules géantes avec pseudo-polyarthrite rhizomélique'),('M31.6','Autres artérites à cellules géantes'),('M31.7','Polyangéite microscopique'),('D69.0','Purpura allergique (vascularite à IgA)'),('M35.2','Maladie de Behçet'),('M35.3','Pseudo-polyarthrite rhizomélique')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],tt,'<p>Code CIM-10-GM.</p>')
a('IL-17',[('IL','InterLeukine'),('17','17')],'Interleukine 17','<p>Cytokine des lymphocytes Th17, inflammation neutrophilique et granulomateuse.</p>')
