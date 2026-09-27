# Glossaire MEDINA — chapitre I33 (endocardite infectieuse, I33, I38, I39)
from cardio_1 import a, G

# ---- maladie, formes, terrains
a('EI',[('E','Endocardite'),('I','Infectieuse')],'Endocardite infectieuse',
 '<p>Infection de la surface endocardique du cœur, le plus souvent valvulaire, native ou prothétique, ou d’un matériel intracardiaque. Lésion caractéristique : la végétation. Diagnostic selon les critères de Duke modifiés (ESC 2023).</p>','i33-duke')
a('UDIV',[('U','Usager'),('D','de Drogues'),('I','par voie Intra'),('V','Veineuse')],'Usager de drogues par voie intraveineuse',
 '<p>Personne qui s’injecte des drogues. Terrain d’EI du cœur droit à <i>Staphylococcus aureus</i>, avec embolies pulmonaires septiques et récidives fréquentes si l’addiction n’est pas traitée.</p>','i33-udiv')
a('DECI',[('D','Dispositif'),('E','Électronique'),('C','Cardiaque'),('I','Implantable')],'Dispositif électronique cardiaque implantable',
 '<p>Stimulateur cardiaque, défibrillateur implantable ou dispositif de resynchronisation. Son infection (loge ou sondes) impose l’extraction complète du système en cas d’endocardite.</p>','i33-deci')
a('HACEK',[('H','<i>Haemophilus</i> (sauf <i>H. influenzae</i>)'),('A','<i>Aggregatibacter</i>'),('C','<i>Cardiobacterium</i>'),('E','<i>Eikenella</i>'),('K','<i>Kingella</i>')],'Groupe HACEK',
 '<p>Bacilles à Gram négatif de la flore oropharyngée, à croissance lente, germes typiques de l’endocardite (critère majeur de Duke). Traitement : ceftriaxone.</p>','i33-hacek')
a('CMI',[('C','Concentration'),('M','Minimale'),('I','Inhibitrice')],'Concentration minimale inhibitrice',
 '<p>Plus faible concentration d’antibiotique empêchant la croissance visible d’une souche in vitro (mg/L). La CMI de la pénicilline guide le traitement des endocardites à streptocoque.</p>','i33-cmi')
a('CRP',[('C','C (polysaccharide C du pneumocoque, qu’elle précipite)'),('R','Reactive (réactive)'),('P','Protein (protéine)')],'Protéine C-réactive',
 '<p>Protéine de la phase aiguë de l’inflammation, synthétisée par le foie sous l’effet de l’interleukine 6. Valeur usuelle &lt; 5 mg/L. Dans l’endocardite, sa décroissance suit la réponse au traitement et entre dans les critères du relais oral.</p>')
a('PCR',[('P','Polymerase'),('C','Chain'),('R','Reaction')],'Polymerase chain reaction (amplification en chaîne par polymérase)',
 '<p>Technique d’amplification de l’ADN. La PCR universelle du gène de l’ARN ribosomique 16S sur une valve opérée identifie la bactérie même après antibiothérapie.</p>','i33-hcneg')
if 'ADN' not in G: a('ADN',[('A','Acide'),('D','Désoxyribo-'),('N','Nucléique')],'Acide désoxyribonucléique','<p>Support de l’information génétique. L’ADN extracellulaire participe à la matrice des biofilms bactériens.</p>')
a('IgG',[('Ig','Immunoglobuline'),('G','de classe G')],'Immunoglobuline G',
 '<p>Anticorps de la réponse secondaire, durable. Dans l’endocardite : IgG de phase I anti-<i>Coxiella burnetii</i> &gt; 1:800 (critère majeur, ESC 2023) ; IgG anti-<i>Bartonella</i> ≥ 1:800 (critère majeur, Duke-ISCVID 2023).</p>','i33-coxiella')
a('IgM',[('Ig','Immunoglobuline'),('M','de classe M')],'Immunoglobuline M',
 '<p>Anticorps pentamérique de la réponse précoce. Le facteur rhumatoïde est le plus souvent une IgM dirigée contre le fragment constant des IgG.</p>')
a('ANCA',[('A','Anti- (dirigés contre le)'),('N','Neutrophil (polynucléaire neutrophile)'),('C','Cytoplasmic (cytoplasme)'),('A','Antibodies (anticorps)')],'Anticorps anti-cytoplasme des polynucléaires neutrophiles',
 '<p>Autoanticorps des vascularites à ANCA. Des ANCA anti-protéinase 3 peuvent apparaître au cours d’une endocardite subaiguë : ils ne doivent pas faire conclure à une vascularite ni prescrire un immunosuppresseur avant d’avoir exclu l’infection.</p>')
a('PR3',[('PR','Protéinase'),('3','trois')],'Protéinase 3','<p>Enzyme des granules des polynucléaires neutrophiles, cible antigénique des ANCA de spécificité cytoplasmique.</p>')
a('C3',[('C','Complément, fraction'),('3','trois')],'Fraction C3 du complément','<p>Protéine centrale de la cascade du complément. Abaissée par la consommation dans les glomérulonéphrites à complexes immuns, notamment au cours de l’endocardite.</p>')
a('C4',[('C','Complément, fraction'),('4','quatre')],'Fraction C4 du complément','<p>Protéine de la voie classique du complément, activée par les complexes immuns ; abaissée dans la glomérulonéphrite de l’endocardite.</p>')

# ---- imagerie
if 'TEP' not in G: a('TEP',[('T','Tomographie'),('E','par Émission de'),('P','Positons')],'Tomographie par émission de positons',
 '<p>Imagerie fonctionnelle qui détecte la distribution d’un traceur radioactif émetteur de positons, le plus souvent le FDG.</p>','i33-tep')
a('TDM',[('T','Tomo-'),('D','Densito-'),('M','Métrie')],'Tomodensitométrie (scanner)',
 '<p>Imagerie en coupes par rayons X. Le scanner cardiaque synchronisé à l’ECG détecte abcès, pseudoanévrismes et fistules et visualise les coronaires.</p>','i33-tdm')
a('TEP-TDM',[('TEP','Tomographie par Émission de Positons'),('TDM','couplée à la TomoDensitoMétrie')],'Tomographie par émission de positons couplée au scanner',
 '<p>Associe l’image métabolique de la TEP et l’anatomie du scanner. Au FDG, elle détecte l’inflammation autour d’une prothèse, d’un tube aortique ou d’une sonde : critère majeur de Duke (ESC 2023).</p>','i33-tep')
a('FDG',[('F','[18F]-Fluoro-'),('D','Désoxy-'),('G','Glucose')],'[18F]-fluorodésoxyglucose',
 '<p>Analogue du glucose marqué au fluor 18, capté par les cellules à métabolisme glucidique élevé (inflammation, tumeurs). Une préparation pauvre en glucides supprime la captation myocardique physiologique.</p>','i33-tep')

# ---- microbiologie
a('MSCRAMM',[('M','Microbial (microbiens)'),('S','Surface'),('C','Components (composants de)'),('R','Recognizing (reconnaissant les)'),('A','Adhesive'),('M','Matrix (de la matrice)'),('M','Molecules (molécules adhésives)')],'Composants de surface microbiens reconnaissant les molécules adhésives de la matrice',
 '<p>Famille d’adhésines de <i>Staphylococcus aureus</i> (protéines de liaison au fibrinogène et à la fibronectine) qui permettent sa fixation sur le thrombus et l’endothélium.</p>','i33-adhesines')
a('PLP',[('P','Protéines de'),('L','Liaison à la'),('P','Pénicilline')],'Protéines de liaison à la pénicilline',
 '<p>Enzymes de la synthèse de la paroi bactérienne (transpeptidases), cibles des bêtalactamines. Leur modification explique plusieurs résistances.</p>')
a('PLP2a',[('P','Protéine de'),('L','Liaison à la'),('P','Pénicilline'),('2a','de type 2a')],'Protéine de liaison à la pénicilline 2a',
 '<p>PLP de faible affinité pour les bêtalactamines, codée par le gène <i>mecA</i> : elle rend <i>Staphylococcus aureus</i> résistant à la méticilline et aux bêtalactamines usuelles.</p>')
a('mecA',[('mec','méticilline (résistance à la)'),('A','gène A')],'Gène mecA','<p>Gène porté par un élément mobile du chromosome staphylococcique ; il code la PLP2a et confère la résistance à la méticilline.</p>')
a('rpoB',[('rpo','RNA polymerase (ARN polymérase)'),('B','sous-unité bêta')],'Gène rpoB','<p>Gène de la sous-unité bêta de l’ARN polymérase bactérienne, cible de la rifampicine. Une seule mutation suffit à conférer la résistance : la rifampicine ne s’utilise jamais seule.</p>','i33-d-rif')

# ---- critères, essais, sociétés
a('ISCVID',[('I','International'),('S','Society for'),('C','Cardio-'),('V','Vascular'),('I','Infectious'),('D','Diseases')],'Société internationale d’infectiologie cardiovasculaire',
 '<p>Société savante auteure des critères Duke-ISCVID 2023, mise à jour des critères de Duke modifiés.</p>','i33-iscvid')
a('POET',[('POET','nom d’essai arrangé à partir de « Partial Oral Treatment of Endocarditis » (traitement oral partiel de l’endocardite), non strictement lettre à lettre')],'Essai POET (Partial Oral Treatment of Endocarditis, 2019)',
 '<p>Essai randomisé danois : chez 400 patients stables atteints d’endocardite gauche, le relais par deux antibiotiques oraux après au moins 10 jours de traitement intraveineux n’a pas été inférieur au traitement intraveineux complet.</p>','i33-poet')
a('SSI',[('S','Société'),('S','Suisse d’'),('I','Infectiologie')],'Société suisse d’infectiologie',
 '<p>Société savante suisse des maladies infectieuses ; avec la Société suisse de cardiologie et les sociétés pédiatriques, auteure des recommandations suisses d’antibioprophylaxie de l’endocardite (2021).</p>','i33-prophy')
a('FROM JANE',[('F','Fièvre'),('R','Roth (taches de)'),('O','Osler (nodosités d’)'),('M','Murmur (souffle)'),('J','Janeway (lésions de)'),('A','Anémie'),('N','Nail (hémorragies sous-unguéales)'),('E','Embolies')],'Aide-mémoire des signes cliniques de l’endocardite',
 '<p>Aide pédagogique, non critère officiel.</p>','i33-mnemo-fromjane')
a('qSOFA',[('q','quick (rapide)'),('S','Sequential'),('O','Organ'),('F','Failure'),('A','Assessment')],'Score qSOFA (évaluation rapide des défaillances d’organes)',
 '<p>Outil de repérage du sepsis au lit du patient : fréquence respiratoire ≥ 22/min, pression artérielle systolique ≤ 100 mmHg, altération de la conscience ; un point par critère. Un score ≥ 2 signale un risque élevé. Outil de repérage, non critère diagnostique.</p>','i33-v-sepsis')
a('B37.6',[('B37.6','code CIM-10 : B = maladies infectieuses et parasitaires ; B37 = candidose ; .6 = endocardite à <i>Candida</i>')],'Code CIM-10 B37.6 : endocardite à Candida',
 '<p>Code « dague » de l’endocardite à <i>Candida</i>, associé au code « étoile » I39.8* dans le système dague-étoile.</p>')
a('Libman-Sacks',[('Libman-Sacks','noms propres : Emanuel Libman et Benjamin Sacks, médecins new-yorkais, 1924')],'Endocardite de Libman-Sacks',
 '<p>Endocardite verruqueuse non infectieuse du lupus érythémateux systémique et du syndrome des antiphospholipides : dépôts stériles de fibrine et de complexes immuns sur les deux faces des valves, emboligènes, avec des hémocultures négatives. Diagnostic différentiel de l’endocardite infectieuse.</p>','i33-etnb')
if 'IDSA' not in G: a('IDSA',[('I','Infectious'),('D','Diseases'),('S','Society of'),('A','America')],'Infectious Diseases Society of America (Société américaine d’infectiologie)',
 '<p>Société savante américaine des maladies infectieuses ; auteure notamment des recommandations sur les candidoses (2016), qui fixent les doses antifongiques de l’endocardite à <i>Candida</i>.</p>')
