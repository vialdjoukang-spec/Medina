from cardio_1 import a, G
from cardio_2 import t
L=[
('GA²LEN',[('G','Global'),('A²','Allergy and Asthma'),('L','(European)'),('E','Excellence'),('N','Network')],'Global Allergy and Asthma Excellence Network','<p>Réseau européen d’excellence ; consensus 2024 sur la définition de l’anaphylaxie.</p>'),
('ABCDE',[('A','Airway (voies aériennes)'),('B','Breathing (respiration)'),('C','Circulation'),('D','Disability (état neurologique)'),('E','Exposure (exposition, peau)')],'Approche ABCDE','<p>Évaluation hiérarchisée des menaces vitales.</p>'),
('PAF',[('P','Platelet'),('A','Activating'),('F','Factor')],'Facteur d’activation plaquettaire','<p>Médiateur lipidique mastocytaire ; son taux est corrélé à la sévérité de l’anaphylaxie.</p>'),
('MRGPRX2',[('MRGPR','Mas-Related G Protein-coupled Receptor'),('X2','membre X2')],'Récepteur MRGPRX2','<p>Récepteur mastocytaire des réactions non allergiques aux opiacés, à la vancomycine, aux fluoroquinolones et à certains curares.</p>','t78-mrg'),
('KIT',[('KIT','proto-oncogène KIT (récepteur du facteur de cellule souche)')],'Récepteur KIT (CD117)','<p>Récepteur tyrosine kinase indispensable aux mastocytes ; mutation D816V dans la mastocytose systémique.</p>'),
('D816V',[('D','acide aspartique (D)'),('816','en position 816'),('V','remplacé par une valine (V)')],'Mutation KIT D816V','<p>Mutation activatrice somatique de la mastocytose systémique.</p>'),
('LTP',[('L','Lipid'),('T','Transfer'),('P','Protein')],'Protéines de transfert lipidique','<p>Allergènes végétaux stables à la chaleur et à la digestion (Pru p 3) ; réactions systémiques.</p>','t78-crd'),
('PR-10',[('PR','Pathogenesis-Related protein'),('10','famille 10')],'Protéines PR-10','<p>Homologues de Bet v 1, thermolabiles ; syndrome pollen-aliment.</p>','t78-crd'),
('PEN-FAST',[('PEN','PENicilline (allergie rapportée)'),('F','Five years (≤ 5 ans)'),('A','Anaphylaxie ou angio-œdème'),('S','Severe cutaneous reaction (réaction cutanée sévère)'),('T','Treatment required (traitement nécessaire)')],'Score PEN-FAST','<p>Score de risque d’allergie vraie à la pénicilline.</p>','t78-penfast'),
('LEAP',[('L','Learning'),('E','Early'),('A','About'),('P','Peanut allergy')],'Essai LEAP (2015)','<p>Introduction précoce de l’arachide : allergie réduite de plus de 80 %.</p>'),
('DRESS',[('D','Drug'),('R','Reaction with'),('E','Eosinophilia and'),('S','Systemic'),('S','Symptoms')],'Syndrome DRESS','<p>Toxidermie grave retardée avec éosinophilie et atteintes viscérales ; réintroduction interdite.</p>'),
('HLA-B*15:02',[('HLA','Human Leukocyte Antigen'),('B*15:02','allèle B*15:02')],'Allèle HLA-B*15:02','<p>Risque de nécrolyse à la carbamazépine chez les patients d’Asie du Sud-Est.</p>','t78-hla'),
('HLA-A*31:01',[('HLA','Human Leukocyte Antigen'),('A*31:01','allèle A*31:01')],'Allèle HLA-A*31:01','<p>Toxidermies à la carbamazépine, y compris chez les Européens.</p>','t78-hla'),
('HLA-B*57:01',[('HLA','Human Leukocyte Antigen'),('B*57:01','allèle B*57:01')],'Allèle HLA-B*57:01','<p>Hypersensibilité à l’abacavir ; dépistage obligatoire.</p>','t78-hla'),
('HLA-B*58:01',[('HLA','Human Leukocyte Antigen'),('B*58:01','allèle B*58:01')],'Allèle HLA-B*58:01','<p>Toxidermies graves à l’allopurinol.</p>','t78-hla'),
('TPSAB1',[('TPS','TryPtaSe'),('AB','alpha/bêta'),('1','gène 1')],'Gène TPSAB1','<p>Code l’alpha- ou la bêta-tryptase ; copies supplémentaires dans l’alpha-tryptasémie héréditaire.</p>'),
('CD117',[('CD','Cluster of Differentiation'),('117','117 (KIT)')],'Marqueur CD117','<p>Récepteur KIT ; marqueur des mastocytes.</p>'),
('CD63',[('CD','Cluster of Differentiation'),('63','63')],'Marqueur CD63','<p>Exprimé à la surface du basophile activé ; base du test d’activation des basophiles.</p>'),
('CD25',[('CD','Cluster of Differentiation'),('25','25')],'Marqueur CD25','<p>Expression aberrante sur les mastocytes de la mastocytose.</p>'),
('CD30',[('CD','Cluster of Differentiation'),('30','30')],'Marqueur CD30','<p>Expression aberrante possible sur les mastocytes néoplasiques.</p>'),
('CD2',[('CD','Cluster of Differentiation'),('2','2')],'Marqueur CD2','<p>Expression aberrante sur les mastocytes de la mastocytose.</p>'),
('IgG4',[('Ig','Immunoglobuline'),('G4','sous-classe G4')],'Immunoglobuline G4','<p>Anticorps « bloquants » induits par l’immunothérapie allergénique.</p>'),
('IL-10',[('IL','InterLeukine'),('10','10')],'Interleukine 10','<p>Cytokine régulatrice de la tolérance.</p>'),
('kUA',[('k','kilo'),('U','Unités'),('A','Allergène-spécifiques')],'Kilo-unités d’anticorps spécifiques par litre','<p>Unité des IgE spécifiques (kUA/L).</p>'),
('SSAI',[('S','Société'),('S','Suisse d’'),('A','Allergologie et d’'),('I','Immunologie')],'Société suisse d’allergologie et d’immunologie','<p>Société savante suisse de référence ; coautrice de la recommandation S2k 2021 sur l’anaphylaxie.</p>'),
('S2k',[('S2','niveau de développement 2'),('k','consensus (Konsens)')],'Niveau de recommandation S2k','<p>Recommandation allemande fondée sur un consensus formel d’experts (système de l’AWMF).</p>'),
('AWMF',[('A','Arbeitsgemeinschaft der'),('W','Wissenschaftlichen'),('M','Medizinischen'),('F','Fachgesellschaften')],'Association des sociétés médicales scientifiques d’Allemagne','<p>Publie les recommandations germanophones.</p>'),
('JAMA',[('J','Journal of the'),('A','American'),('M','Medical'),('A','Association')],'Revue JAMA','<p>Revue médicale générale.</p>'),
('CD',[('CD','Cluster of Differentiation (classe de différenciation)')],'Classe de différenciation','<p>Nomenclature des marqueurs de surface des cellules.</p>'),
]
for x in L: a(*x)
for c,tt in [('T78.0','Choc anaphylactique dû à une intolérance alimentaire'),('T78.1','Autres réactions d’intolérance alimentaire'),('T78.2','Choc anaphylactique, sans précision'),('T78.3','Œdème angioneurotique'),('T78.4','Allergie, sans précision'),('T80.5','Choc anaphylactique dû à un sérum'),('T88.6','Choc anaphylactique dû à un médicament correctement administré')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],tt,'<p>Code CIM-10-GM.</p>')
for k,t2 in [('Stevens-Johnson','Albert Stevens et Frank Johnson'),('Bezold-Jarisch','Albert von Bezold et Adolf Jarisch')]:
    a(k,[(k,'nom propre : '+t2)],k,'<p>Éponyme ('+t2+').</p>')
a('États-Unis',[('États-Unis','nom de pays')],'États-Unis d’Amérique','<p>Pays ; autorités du médicament : Food and Drug Administration.</p>')
a('Sud-Est',[('Sud-Est','point cardinal composé')],'Asie du Sud-Est','<p>Région géographique (Chine du Sud, Thaïlande, Malaisie, Indonésie, Philippines, Vietnam…).</p>')
a('H1',[('H','Histamine'),('1','récepteur de type 1')],'Récepteur H1 de l’histamine','<p>Médie prurit, vasodilatation, perméabilité capillaire ; cible des antihistaminiques.</p>','t78-d-antih')
