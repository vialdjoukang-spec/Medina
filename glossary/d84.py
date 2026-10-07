from cardio_1 import a, G
a('IUIS',[('I','International'),('U','Union of'),('I','Immunological'),('S','Societies')],'Union internationale des sociétés d’immunologie','<p>Publie la classification des erreurs innées de l’immunité (mise à jour 2024).</p>','d84-iei')
a('ESID',[('E','European'),('S','Society for'),('I','Immuno'),('D','Deficiencies')],'Société européenne des déficits immunitaires','<p>Définitions de travail du registre (2019), dont les critères du déficit immunitaire commun variable.</p>')
a('TREC',[('T','T-cell receptor'),('R','(Récepteur)'),('E','Excision'),('C','Circles')],'Cercles d’excision du récepteur des lymphocytes T','<p>Marqueur de production thymique ; dépistage néonatal du déficit combiné sévère.</p>','d84-trec')
a('BTK',[('B','Bruton’s'),('T','Tyrosine'),('K','Kinase')],'Tyrosine kinase de Bruton','<p>Gène de l’agammaglobulinémie liée à l’X ; indispensable à la maturation des lymphocytes B.</p>')
a('WAO',[('W','World'),('A','Allergy'),('O','Organization')],'Organisation mondiale de l’allergie','<p>Coauteur de la recommandation internationale sur l’angio-œdème héréditaire.</p>')
a('EAACI',[('E','European'),('A','Academy of'),('A','Allergy and'),('C','Clinical'),('I','Immunology')],'Académie européenne d’allergologie et d’immunologie clinique','<p>Coauteur de la recommandation internationale sur l’angio-œdème héréditaire.</p>')
a('AH50',[('A','Alternative (voie alterne)'),('H','Hémolytique'),('50','50 % d’hémolyse')],'Activité hémolytique de la voie alterne','<p>Explore la voie alterne et la voie terminale du complément.</p>','d84-ch50')
a('CD40LG',[('CD40','CD40'),('L','Ligand'),('G','Gène')],'Gène du ligand de CD40','<p>Lié à l’X ; son déficit cause le syndrome hyper-IgM.</p>')
a('CD27',[('CD','Cluster of Differentiation'),('27','27')],'Marqueur CD27','<p>Marqueur des lymphocytes B mémoire.</p>')
a('IgD',[('Ig','Immunoglobuline'),('D','D')],'Immunoglobuline D','<p>Présente à la surface des lymphocytes B naïfs ; perdue après commutation.</p>')
a('IPEX',[('I','Immune dysregulation'),('P','Polyendocrinopathy'),('E','Enteropathy'),('X','X-linked')],'Syndrome IPEX','<p>Dysrégulation immunitaire liée à l’X par déficit du facteur FOXP3 des lymphocytes T régulateurs.</p>')
a('FOXP3',[('FOX','FOrkhead boX'),('P3','protéine P3')],'Facteur de transcription FOXP3','<p>Indispensable aux lymphocytes T régulateurs.</p>')
a('CTLA-4',[('C','Cytotoxic'),('T','T-'),('L','Lymphocyte'),('A','Antigen'),('4','4')],'Antigène 4 des lymphocytes T cytotoxiques','<p>Récepteur inhibiteur ; son haplo-insuffisance cause une dysrégulation traitée par abatacept.</p>')
a('JAK',[('J','JAnus'),('A','(kinase)'),('K','Kinase')],'Kinases Janus','<p>Kinases de signalisation des cytokines ; cible des inhibiteurs de JAK.</p>')
a('STAT',[('S','Signal'),('T','Transducer and'),('A','Activator of'),('T','Transcription')],'Facteurs STAT','<p>Transmettent le signal des cytokines au noyau.</p>')
for k,d in [('STAT1','Gain de fonction : candidose cutanéomuqueuse chronique, auto-immunité.'),('STAT3','Perte de fonction dominante : syndrome hyper-IgE ; gain de fonction : auto-immunité.')]:
    a(k,[('STAT','Signal Transducer and Activator of Transcription'),(k[-1],k[-1])],'Facteur '+k,'<p>'+d+'</p>')
for k,d in [('WAS','Gène de la protéine du syndrome de Wiskott-Aldrich (lié à l’X).'),('CYBB','Gène de la sous-unité gp91phox de la NADPH oxydase ; forme liée à l’X de la granulomatose septique chronique.'),('IL2RG','Gène de la chaîne gamma commune des récepteurs de cytokines ; déficit combiné sévère lié à l’X.'),('RAG1','Gène activant la recombinaison des récepteurs lymphocytaires.'),('RAG2','Gène activant la recombinaison des récepteurs lymphocytaires.'),('ADA','Adénosine désaminase ; son déficit cause un déficit combiné sévère traitable par thérapie génique.'),('SERPING1','Gène de l’inhibiteur de la C1 estérase ; angio-œdème héréditaire.')]:
    lit={'WAS':[('W','Wiskott'),('A','Aldrich'),('S','Syndrome')],'CYBB':[('CYB','CYtochrome B'),('B','béta (chaîne)')],'IL2RG':[('IL2R','Interleukin-2 Receptor'),('G','Gamma')],'RAG1':[('R','Recombination'),('A','Activating'),('G','Gene'),('1','1')],'RAG2':[('R','Recombination'),('A','Activating'),('G','Gene'),('2','2')],'ADA':[('A','Adénosine'),('D','Désaminase'),('A','(enzyme)')],'SERPING1':[('SERPIN','SERine Protease INhibitor'),('G1','clade G, membre 1')]}[k]
    a(k,lit,'Gène '+k,'<p>'+d+'</p>')
for c,t in [('D80.0','Hypogammaglobulinémie héréditaire'),('D80.2','Déficit sélectif en immunoglobuline A'),('D81.9','Déficit immunitaire combiné, sans précision'),('D82.0','Syndrome de Wiskott-Aldrich'),('D82.1','Syndrome de DiGeorge'),('D84.1','Anomalies du système du complément')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],t,'<p>Code CIM-10-GM.</p>')
a('IgA',[('Ig','Immunoglobuline'),('A','de classe A')],'Immunoglobuline A','<p>Anticorps des muqueuses (forme sécrétoire dimérique) ; son déficit sélectif est le déficit immunitaire primaire le plus fréquent.</p>')
a('BCG',[('B','Bacille de'),('C','Calmette et'),('G','Guérin')],'Bacille de Calmette et Guérin','<p>Vaccin vivant atténué contre la tuberculose ; contre-indiqué dans les déficits combinés (infection disséminée).</p>')
a('NK',[('N','Natural'),('K','Killer')],'Lymphocytes tueurs naturels','<p>Lymphocytes de l’immunité innée cytotoxiques pour les cellules infectées ou tumorales.</p>')
a('CH50',[('C','Complément'),('H','Hémolytique'),('50','50 % d’hémolyse')],'Activité hémolytique totale de la voie classique','<p>Explore la voie classique et terminale du complément.</p>','d84-ch50')
a('NADPH',[('N','Nicotinamide'),('A','Adénine'),('D','Dinucléotide'),('P','Phosphate'),('H','forme réduite (Hydrogène)')],'Nicotinamide adénine dinucléotide phosphate réduit','<p>Cofacteur ; la NADPH oxydase des phagocytes produit l’anion superoxyde.</p>')
a('ACWY',[('A','sérogroupe A'),('C','sérogroupe C'),('W','sérogroupe W'),('Y','sérogroupe Y')],'Sérogroupes A, C, W et Y du méningocoque','<p>Vaccin conjugué quadrivalent.</p>')
a('AB',[('A','antigène A'),('B','antigène B')],'Groupe sanguin AB','<p>Porte les antigènes A et B : pas d’isohémagglutinines anti-A ni anti-B.</p>')
a('IL-12',[('IL','InterLeukine'),('12','12')],'Interleukine 12','<p>Cytokine des macrophages qui induit l’interféron gamma ; axe indispensable contre les mycobactéries.</p>')
for k,t in [('CD19','marqueur pan-B'),('CD16','récepteur Fc gamma III des NK'),('CD56','marqueur des NK'),('CD40','récepteur des lymphocytes B interagissant avec le CD40 ligand')]:
    a(k,[('CD','Cluster of Differentiation (classe de différenciation)'),(k[2:],k[2:])],'Marqueur '+k,'<p>'+t+'.</p>')
for k,t in [('C1','Premier composant de la voie classique (C1q, C1r, C1s).'),('C1q','Sous-unité de reconnaissance de C1 ; son déficit expose au lupus.'),('C2','Composant de la voie classique ; son déficit expose au lupus.'),('C5','Premier composant de la voie terminale.'),('C5b','Fragment qui initie le complexe d’attaque membranaire.'),('C9','Dernier composant du complexe d’attaque membranaire.')]:
    a(k,[('C','Complément'),(k[1:],'composant '+k[1:])],'Composant '+k+' du complément','<p>'+t+'</p>')
for k,t in [('Wiskott-Aldrich','Alfred Wiskott et Robert Aldrich'),('Howell-Jolly','William Howell et Justin Jolly'),('Chédiak-Higashi','Moisés Chédiak et Ototaka Higashi')]:
    a(k,[(k,'nom propre : '+t)],k,'<p>Éponyme ('+t+').</p>')

# Désignations rencontrées dans les fenêtres de justification.
a('anti-CD20',[('anti','Anticorps dirigé contre'),('CD','Cluster of Differentiation (classe de différenciation)'),('20','20')],'Anticorps dirigés contre l’antigène de différenciation CD20','<p>Le rituximab reconnaît cette protéine de surface de nombreux lymphocytes B. La déplétion B peut réduire la réponse à de nouveaux antigènes et entraîner une hypogammaglobulinémie ; les plasmocytes matures ne sont pas tous directement ciblés.</p>')
for k,t in [('C6','S’associe au fragment C5b au début de l’assemblage terminal.'),('C7','Participe à l’insertion du complexe terminal dans la membrane cible.'),('C8','Participe à la formation du pore terminal.')]:
    a(k,[('C','Complément'),(k[1:],'composant '+k[1:])],'Composant '+k+' du complément','<p>'+t+'</p>')
