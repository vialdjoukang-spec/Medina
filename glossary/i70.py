from cardio_1 import a, G
L=[
('CLTI',[('C','Chronic'),('L','Limb-'),('T','Threatening'),('I','Ischaemia')],'Ischémie chronique menaçant le membre','<p>Douleur de repos, plaie ou gangrène &gt; 2 semaines avec preuve hémodynamique.</p>'),
('WIfI',[('W','Wound (plaie)'),('I','Ischemia (ischémie)'),('fI','foot Infection (infection du pied)')],'Classification WIfI','<p>Stratification du risque d’amputation.</p>','i70-wifi'),
('LDL',[('L','Low'),('D','Density'),('L','Lipoprotein')],'Lipoprotéines de basse densité','<p>Principal lipide athérogène ; cible thérapeutique.</p>'),
('PCSK9',[('P','Proprotein'),('C','Convertase'),('S','Subtilisin/'),('K','Kexin type'),('9','9')],'Proprotéine convertase subtilisine/kexine de type 9','<p>Dégrade le récepteur des LDL ; cible de l’évolocumab, de l’alirocumab et de l’inclisiran.</p>'),
('SGLT2',[('S','Sodium-'),('GL','GLucose'),('T','co-Transporter'),('2','2')],'Cotransporteur sodium-glucose de type 2','<p>Cible des gliflozines, à bénéfice cardiovasculaire et rénal.</p>'),
('GLP-1',[('G','Glucagon-'),('L','Like'),('P','Peptide'),('1','1')],'Peptide semblable au glucagon 1','<p>Hormone incrétine ; ses agonistes réduisent le poids et les événements cardiovasculaires.</p>'),
('CAPRIE',[('CAPRIE','Clopidogrel versus Aspirin in Patients at Risk of Ischaemic Events')],'Essai CAPRIE (1996)','<p>Clopidogrel légèrement supérieur à l’aspirine, surtout dans l’artériopathie.</p>'),
('COMPASS',[('COMPASS','Cardiovascular OutcoMes for People using Anticoagulation StrategieS')],'Essai COMPASS (2018)','<p>Rivaroxaban 2,5 mg × 2 + aspirine : moins d’événements cardiovasculaires et des membres.</p>'),
('VOYAGER-PAD',[('VOYAGER','nom d’essai'),('PAD','Peripheral Artery Disease')],'Essai VOYAGER-PAD (2020)','<p>Même stratégie après revascularisation des membres inférieurs.</p>'),
('FOURIER',[('FOURIER','Further cardiovascular OUtcomes Research with PCSK9 Inhibition in subjects with Elevated Risk')],'Essai FOURIER (2017)','<p>Évolocumab : moins d’événements, dont ceux des membres.</p>'),
('ODYSSEY',[('ODYSSEY','nom du programme d’essais de l’alirocumab')],'Essai ODYSSEY OUTCOMES (2018)','<p>Alirocumab après syndrome coronarien aigu.</p>'),
('OUTCOMES',[('OUTCOMES','mot anglais (résultats cliniques), partie du nom d’essai')],'OUTCOMES','<p>Partie du nom de l’essai ODYSSEY OUTCOMES.</p>'),
('STRIDE',[('STRIDE','nom d’essai (sémaglutide dans l’artériopathie), non strictement lettre à lettre')],'Essai STRIDE (2025)','<p>Sémaglutide : amélioration de la distance de marche chez le diabétique artériopathe.</p>'),
('ASTRAL',[('ASTRAL','Angioplasty and STenting for Renal Artery Lesions')],'Essai ASTRAL (2009)','<p>Pas de bénéfice de l’angioplastie rénale systématique.</p>'),
('CORAL',[('CORAL','Cardiovascular Outcomes in Renal Atherosclerotic Lesions')],'Essai CORAL (2014)','<p>Résultat concordant avec ASTRAL.</p>'),
('VCAM-1',[('V','Vascular'),('C','Cell'),('A','Adhesion'),('M','Molecule'),('1','1')],'Molécule d’adhésion vasculaire 1','<p>Recrute les monocytes dans la plaque.</p>'),
]
for x in L: a(*x)
for c,tt in [('I70.0','Athérosclérose de l’aorte'),('I70.1','Athérosclérose de l’artère rénale'),('I70.2','Athérosclérose des artères distales (membres)'),('I74.0','Embolie et thrombose de l’aorte abdominale'),('I74.1','Embolie et thrombose de parties de l’aorte'),('I74.3','Embolie et thrombose des artères des membres inférieurs')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],tt,'<p>Code CIM-10-GM.</p>')
a('Écho-Doppler',[('Écho','échographie'),('Doppler','effet Doppler (Christian Doppler)')],'Échographie Doppler','<p>Imagerie des vaisseaux et mesure des vitesses de flux.</p>')
