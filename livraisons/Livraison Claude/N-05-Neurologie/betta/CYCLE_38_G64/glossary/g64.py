"""Abréviations G64 (Cycle Betta 38). Entrées indépendantes ; la fusion avec le glossaire racine relève de l’injection."""
G = {}
def a(key, letters, full, definition, window):
    G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': 'g64-' + window}
a('SGB', [('S', 'Syndrome'), ('G', 'de Guillain-'), ('B', 'Barré')], 'Syndrome de Guillain-Barré',
  'Neuropathie aiguë dysimmune dont le nadir est atteint en quatre semaines au plus, d’après la revue allemande de 2018. Elle apparaît souvent comme une paralysie ascendante après une infection digestive ou respiratoire.', 'sgb')
a('PIDC', [('P', 'Polyradiculoneuropathie'), ('I', 'Inflammatoire'), ('D', 'Démyélinisante'), ('C', 'Chronique')], 'Polyradiculoneuropathie inflammatoire démyélinisante chronique',
  'Neuropathie dysimmune dont l’évolution dépasse huit semaines, ce qui la distingue du syndrome de Guillain-Barré. Le dossier cite 2 à 3 cas pour 100 000, sans préciser s’il s’agit d’une incidence ou d’une prévalence.', 'pidc')
a('QST', [('Q', 'Quantitative'), ('S', 'Sensory'), ('T', 'Testing (tests sensitifs quantitatifs)')], 'Tests sensitifs quantitatifs',
  'Ensemble d’épreuves psychophysiques qui mesurent les seuils de perception sensitive. Avec la densité des fibres intraépidermiques, ils soutiennent le diagnostic de neuropathie des petites fibres.', 'petites-fibres')
a('NeuPSIG', [('Neu', 'Neuropathic (douleur neuropathique)'), ('P', 'Pain'), ('SIG', 'Special Interest Group (groupe d’intérêt)')], 'Groupe d’intérêt sur la douleur neuropathique de l’association internationale pour l’étude de la douleur',
  'Ce groupe a publié en 2025, dans Lancet Neurology, une méta-analyse de 313 essais sur les traitements de la douleur neuropathique. Ses résultats valent pour toutes les causes, non pour G64 en particulier.', 'neupsig')
a('IRSN', [('I', 'Inhibiteurs de la'), ('R', 'Recapture de la'), ('S', 'Sérotonine et de la'), ('N', 'Noradrénaline')], 'Inhibiteurs de la recapture de la sérotonine et de la noradrénaline',
  'Classe d’antidépresseurs dont fait partie la duloxétine. La méta-analyse NeuPSIG 2025 la place en première ligne forte pour la douleur neuropathique.', 'neupsig')
a('ANCA', [('A', 'Anticorps'), ('N', 'Anti-'), ('C', 'Cytoplasme des'), ('A', 'neutrophiles')], 'Anticorps anti-cytoplasme des neutrophiles',
  'Auto-anticorps dosés dans le bilan d’une suspicion de vascularite. Leur présence figure parmi les critères en faveur d’une vascularite systémique selon la guideline PNS 2010. Le dossier cite les variantes p-ANCA et c-ANCA.', 'vasc-criteres')
a('ANA', [('A', 'Anticorps'), ('N', 'Anti-'), ('A', 'Noyaux')], 'Anticorps antinucléaires',
  'Auto-anticorps dosés dans la biologie élargie orientée de la revue allemande de 2018.', 'biologie')
a('VS', [('V', 'Vitesse de'), ('S', 'Sédimentation')], 'Vitesse de sédimentation',
  'Marqueur inflammatoire exprimé en mm/h. Une valeur de 100 mm/h ou plus figure parmi les critères en faveur d’une vascularite systémique selon la guideline PNS 2010.', 'vasc-criteres')
a('CRP', [('C', 'C-'), ('R', 'Reactive (réactive)'), ('P', 'Protein (protéine)')], 'Protéine C-réactive',
  'Marqueur inflammatoire inclus dans la biologie de base de la démarche diagnostique de la revue allemande de 2018.', 'biologie')
a('HbA1c', [('Hb', 'Hémoglobine'), ('A1c', 'fraction glyquée A1c')], 'Hémoglobine glyquée',
  'Paramètre de l’équilibre glycémique, inclus dans la biologie de base devant une polyneuropathie, car le diabète est la première cause en Europe.', 'biologie')
a('TSH', [('T', 'Thyréo-'), ('S', 'Stimulating (stimulante)'), ('H', 'Hormone')], 'Hormone thyréotrope',
  'Hormone dosée dans la biologie de base de la démarche diagnostique de la revue allemande de 2018.', 'biologie')
a('CDT', [('C', 'Carbohydrate-'), ('D', 'Deficient (déficiente)'), ('T', 'Transferrin (transferrine)')], 'Transferrine déficiente en glucides',
  'La revue allemande de 2018 la range dans la biologie de base. Le dossier de la leçon ne détaille pas son interprétation.', 'biologie')
a('LCR', [('L', 'Liquide'), ('C', 'Céphalo-'), ('R', 'Rachidien')], 'Liquide céphalorachidien',
  'Liquide prélevé par ponction lombaire quand une cause inflammatoire est suspectée. Dans la PIDC, la revue allemande décrit moins de 10 leucocytes par microlitre et des protéines élevées, sans que ces critères soient obligatoires.', 'lcr')
a('EMG', [('E', 'Électro-'), ('M', 'Myo-'), ('G', 'Graphie')], 'Électromyographie',
  'Examen neurophysiologique associé à la neurographie pour classer l’atteinte en axonale ou démyélinisante.', 'neurographie')
a('ENG', [('E', 'Électro-'), ('N', 'Neuro-'), ('G', 'Graphie')], 'Électroneurographie',
  'Étude de la conduction nerveuse. L’électroneurographie standard ne détecte pas une neuropathie des petites fibres.', 'neurographie')
a('IRM', [('I', 'Imagerie par'), ('R', 'Résonance'), ('M', 'Magnétique')], 'Imagerie par résonance magnétique',
  'Technique d’imagerie dont la neurographie par IRM figure à l’étape 4 de la démarche de la revue allemande de 2018.', 'imagerie')
a('TA', [('T', 'Tension'), ('A', 'Artérielle')], 'Tension artérielle',
  'Pression artérielle. La Duloxetin-Mepha® élève en moyenne la tension de 1 à 2 mmHg et des crises hypertensives sont décrites, d’où une surveillance.', 'duloxetine')
a('NNT', [('N', 'Number'), ('N', 'Needed'), ('T', 'to Treat (nombre de patients à traiter)')], 'Nombre de patients à traiter',
  'Nombre de patients à traiter pour qu’un patient de plus qu’avec le comparateur obtienne le bénéfice mesuré. Plus il est bas, plus le traitement est efficace.', 'neupsig')
a('NNH', [('N', 'Number'), ('N', 'Needed'), ('H', 'to Harm (nombre de patients à traiter pour un préjudice)')], 'Nombre de patients à traiter pour observer un effet nocif',
  'Nombre de patients à traiter pour qu’un patient de plus qu’avec le comparateur subisse l’événement indésirable mesuré. Plus il est haut, mieux le traitement est toléré. Le résumé lu de la méta-analyse ne précise pas l’événement retenu.', 'neupsig')
a('POEMS', [('P', 'Polyneuropathy (polyneuropathie)'), ('O', 'Organomegaly (organomégalie)'), ('E', 'Endocrinopathy (endocrinopathie)'), ('M', 'Monoclonal protein (protéine monoclonale)'), ('S', 'Skin changes (lésions cutanées)')], 'Syndrome POEMS',
  'Association d’une polyneuropathie, d’une paraprotéine, d’une organomégalie, d’une endocrinopathie et de lésions cutanées ou ostéosclérotiques. La revue allemande de 2018 la cite parmi les drapeaux rouges.', 'poems')
a('MAG', [('M', 'Myelin-'), ('A', 'Associated (associée à la myéline)'), ('G', 'Glycoprotein (glycoprotéine)')], 'Glycoprotéine associée à la myéline',
  'Cible des anticorps IgM de la neuropathie à IgM ; la revue allemande de 2018 cite l’anti-MAG parmi les anticorps de la biologie élargie.', 'paraproteine')
a('GM1', [('GM1', 'Ganglioside GM1, nom propre d’un lipide membranaire, non une abréviation à développer')], 'Ganglioside GM1',
  'Les anticorps IgM anti-GM1 sont présents chez environ la moitié des patients atteints de neuropathie motrice multifocale selon la revue allemande de 2018.', 'dysimmun')
a('GQ1b', [('GQ1b', 'Ganglioside GQ1b, nom propre d’un lipide membranaire, non une abréviation à développer')], 'Ganglioside GQ1b',
  'Les anticorps anti-GQ1b figurent dans la biologie élargie orientée de la revue allemande de 2018.', 'biologie')
a('IgM', [('Ig', 'Immunoglobuline'), ('M', 'classe M')], 'Immunoglobuline M',
  'Classe d’anticorps. Une paraprotéine IgM oriente vers la maladie de Waldenström ou la neuropathie anti-MAG.', 'paraproteine')
a('IgG', [('Ig', 'Immunoglobuline'), ('G', 'classe G')], 'Immunoglobuline G',
  'Classe d’anticorps. Une paraprotéine IgG avec amylose figure parmi les drapeaux rouges.', 'paraproteine')
a('VIH', [('V', 'Virus de l’'), ('I', 'Immunodéficience'), ('H', 'Humaine')], 'Virus de l’immunodéficience humaine',
  'Sérologie incluse dans la biologie élargie orientée de la revue allemande de 2018.', 'biologie')
a('B12', [('B12', 'Vitamine B12, nom de la cobalamine, non une abréviation à développer')], 'Vitamine B12',
  'Sa carence cause une neuropathie, et peut exister sans anémie macrocytaire.', 'biologie')
a('Clcr', [('Cl', 'Clairance de la'), ('cr', 'créatinine')], 'Clairance de la créatinine',
  'Mesure ou estimation de la fonction rénale exprimée en ml/min. La Lyrica® impose une adaptation de dose entre 30 et 60 ml/min et n’est pas recommandée en dessous de 30 ml/min.', 'pregabaline')
a('FI', [('F', 'Fachinformation'), ('I', 'Information, soit l’information professionnelle')], 'Information professionnelle suisse',
  'Texte de référence du médicament approuvé par Swissmedic, lu dans la base AIPS via AmiKo.', 'pregabaline')
a('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')], 'Fédération européenne des sociétés de neurologie',
  'Elle est aujourd’hui l’Académie européenne de neurologie (EAN). Elle a publié avec la PNS la guideline 2010 sur la biopsie cutanée.', 'biopsie-cutanee')
a('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')], 'Académie européenne de neurologie',
  'Successeur de l’EFNS. Le dossier n’a lu aucune guideline EAN récente sur la neuropathie non étiquetée.', 'biopsie-cutanee')
a('PNS', [('P', 'Peripheral'), ('N', 'Nerve'), ('S', 'Society')], 'Société du nerf périphérique',
  'Société internationale. Elle a publié en 2010 la guideline sur la vascularite non systémique et, avec l’EFNS, celle sur la biopsie cutanée.', 'vasc-criteres')
a('GM', [('G', 'German'), ('M', 'Modification')], 'Modification allemande de la classification',
  'Suffixe de CIM-10-GM : adaptation allemande de la classification internationale, publiée par le BfArM et reprise par l’OFS.', 'code')
a('OFS', [('O', 'Office'), ('F', 'fédéral de la'), ('S', 'statistique')], 'Office fédéral de la statistique',
  'Éditeur suisse de la CIM-10-GM.', 'code')
a('BfArM', [('BfArM', 'Bundesinstitut für Arzneimittel und Medizinprodukte, nom propre de l’institut allemand, non une abréviation à développer en français')], 'Institut fédéral allemand des médicaments et des dispositifs médicaux',
  'Éditeur allemand de la CIM-10-GM 2024.', 'code')
a('CIM', [('C', 'Classification'), ('I', 'Internationale des'), ('M', 'Maladies')], 'Classification internationale des maladies',
  'Ici la CIM-10-GM 2024, dont G64 est une catégorie.', 'code')
a('Nav', [('Na', 'Sodium (natrium)'), ('v', 'voltage-dépendant')], 'Canal sodique voltage-dépendant',
  'Les variants à gain de fonction des canaux Nav1.7, 1.8 et 1.9 sont associés à la neuropathie des petites fibres.', 'nav')
a('PMP22', [('PMP22', 'Peripheral Myelin Protein 22, nom de gène, non développé lettre à lettre')], 'Gène PMP22',
  'Un des gènes de la liste génétique de la revue allemande de 2018.', 'genetique')
a('GJB1', [('GJB1', 'Gap Junction Beta 1, nom de gène, non développé lettre à lettre')], 'Gène GJB1',
  'Un des gènes de la liste génétique de la revue allemande de 2018.', 'genetique')
a('MPZ', [('MPZ', 'Myelin Protein Zero, nom de gène, non développé lettre à lettre')], 'Gène MPZ',
  'Un des gènes de la liste génétique de la revue allemande de 2018.', 'genetique')
a('MFN2', [('MFN2', 'Mitofusin 2, nom de gène, non développé lettre à lettre')], 'Gène MFN2',
  'Un des gènes de la liste génétique de la revue allemande de 2018.', 'genetique')
a('Dtsch Arztebl', [('Dtsch Arztebl', 'Deutsches Ärzteblatt, nom propre de revue, non une abréviation')], 'Deutsches Ärzteblatt, revue médicale allemande',
  'Elle a publié en 2018 la revue narrative « Polyneuropathies », source principale de la leçon.', 'code')
a('AmiKo', [('AmiKo', 'nom propre d’une application de consultation des informations professionnelles, non une abréviation')], 'AmiKo, application de consultation des informations professionnelles suisses',
  'Elle donne accès aux informations professionnelles de Swissmedic.', 'pregabaline')
