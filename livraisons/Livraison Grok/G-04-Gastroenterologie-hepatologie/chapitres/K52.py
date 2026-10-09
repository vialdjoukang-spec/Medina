import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K52', 'Autres gastroentérites et colites non infectieuses : colite microscopique',
    'K52 — Autres gastroentérites et colites non infectieuses · CIM-10-GM 2024 · Côlon',
    'Adulte · colite microscopique (collagène et lymphocytaire, K52.8), colites radiques, toxiques, allergiques et indéterminées · rédaction du 09.10.2026 · référentiels UEG/EMCG colite microscopique 2021, ECCO maladie de Crohn 2024, informations professionnelles suisses',
    'Pharmacologie de la colite microscopique')
w = C.w
EMCG = ('Miehlke S. et al., European guidelines on microscopic colitis: United European Gastroenterology and European Microscopic Colitis Group statements and recommendations, United European Gastroenterol J 2021;9:13-37', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8259259/')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 66 ans, fumeuse, traitée par oméprazole et par un anti-inflammatoire pour une arthrose, a depuis trois mois six à huit selles aqueuses par jour, y compris la nuit, sans sang. Or, sa coloscopie est macroscopiquement normale. <b>La question est donc de savoir s’il s’agit d’une ' + w('k52-cm', 'colite microscopique') + ', comment la prouver et comment la traiter.</b>',
 'Pour y répondre, le médecin doit savoir : évoquer la maladie devant une diarrhée aqueuse chronique, surtout chez une femme âgée ; exiger des biopsies du côlon droit et gauche même si la muqueuse paraît normale ; reconnaître les critères histologiques de la ' + w('k52-cc', 'colite collagène') + ' et de la ' + w('k52-cl', 'colite lymphocytaire') + ' ; enfin, traiter par ' + w('k52-d-budesonide', 'budésonide') + ' et retirer les médicaments suspects.')
 + key('Diarrhée aqueuse chronique, nocturne, sans sang, avec coloscopie normale : biopsier pour chercher une colite microscopique.', 'Point de départ.'))

C.a(1, 'Définition et périmètre', P(
 'La catégorie K52 regroupe les gastroentérites et colites qui ne sont ni infectieuses ni rattachées à une maladie de Crohn ou à une rectocolite hémorragique. Ainsi, elle comprend les atteintes dues à une irradiation (K52.0), les formes toxiques (K52.1), les formes allergiques et alimentaires (K52.2), la colite indéterminée (K52.3), les autres formes précisées (K52.8) et les formes non précisées (K52.9).',
 'Parmi ces formes, la colite microscopique est la plus fréquente en pratique ; c’est pourquoi elle occupe l’essentiel de ce cours. En effet, il s’agit d’une maladie inflammatoire chronique du côlon, responsable d’une diarrhée aqueuse, dont la muqueuse paraît normale ou presque à l’endoscopie, mais dont l’histologie est anormale (EMCG 2021). Par conséquent, son diagnostic est exclusivement histologique, et elle comporte deux formes, collagène et lymphocytaire, ainsi qu’une forme incomplète.')
 + table(['Entité', 'Mécanisme'], [
   ['Gastroentérite et colite radiques', 'Lésion des tissus par la radiothérapie'],
   ['Gastroentérite et colite toxiques', 'Médicaments ou toxiques'],
   ['Formes allergiques et alimentaires', 'Réaction immunitaire à un aliment'],
   ['Colite indéterminée', 'Colite inflammatoire non classable entre Crohn et rectocolite'],
   ['Autres formes précisées, dont la colite microscopique', 'Inflammation muqueuse microscopique']])
 + P('Le tableau se lit par la colonne « Mécanisme » : en effet, chaque forme est définie par sa cause, si bien que l’interrogatoire sur les traitements et les expositions est décisif.')
 + key('K52 : colites non infectieuses hors Crohn et rectocolite. Colite microscopique : diarrhée aqueuse, muqueuse normale à l’œil, histologie anormale.')
 + src(EMCG))

C.a(2, 'Épidémiologie et facteurs de risque', P(
 'Après la définition, il faut mesurer la fréquence. Ainsi, l’incidence groupée de la colite microscopique est estimée à 11,4 cas pour 100 000 personnes-années, et sa prévalence à 119 pour 100 000 (EMCG 2021, énoncés 1.1 et 1.2). De plus, elle est retrouvée chez 12,8 % des patients qui ont une diarrhée aqueuse chronique inexpliquée (énoncé 1.3) ; elle n’est donc pas rare.',
 'Par ailleurs, le risque est plus élevé chez la femme (énoncé 1.5), et le tabagisme, ancien et surtout actuel, l’augmente (énoncé 1.4). En outre, l’usage chronique ou fréquent d’' + w('k52-ipp', 'inhibiteurs de la pompe à protons') + ', d’anti-inflammatoires non stéroïdiens ou d’' + w('k52-isrs', 'inhibiteurs sélectifs de la recapture de la sérotonine') + ' est associé à la maladie ; toutefois, cette association n’implique pas de causalité (énoncé 1.7).')
 + key('Incidence ≈ 11,4/100 000/an ; 12,8 % des diarrhées aqueuses chroniques inexpliquées ; femme, tabac ; association avec IPP, AINS, ISRS.')
 + src(EMCG))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre la diarrhée, il faut regarder la muqueuse au microscope. Selon l’EMCG, la pathogénie est complexe et multifactorielle ; ainsi, elle peut associer des facteurs luminaux, comme des médicaments ou des acides biliaires, une dysrégulation immunitaire et une prédisposition génétique (énoncé 2.1). Dans la colite collagène, une bande de collagène sous-épithéliale épaissie s’ajoute à l’inflammation ; or, cette bande gêne la réabsorption de l’eau et des électrolytes.',
 'De plus, l’infiltrat lymphocytaire intraépithélial et l’inflammation du chorion entretiennent une sécrétion d’eau. Par conséquent, la diarrhée est aqueuse et persiste la nuit, ce qui la distingue d’une diarrhée fonctionnelle. Enfin, une ' + w('k52-dab', 'diarrhée par malabsorption des acides biliaires') + ' coexiste souvent et peut expliquer une résistance au traitement.')
 + key('Facteurs luminaux, immunité, gènes → bande collagène épaissie et/ou lymphocytes intraépithéliaux → défaut de réabsorption et sécrétion → diarrhée aqueuse, nocturne.')
 + src(EMCG))

C.a(4, 'Présentation clinique', P(
 'La présentation est donc dominée par la diarrhée. En effet, le symptôme le plus fréquent est une diarrhée chronique aqueuse, non sanglante, souvent associée à des besoins impérieux, à des selles nocturnes et à une incontinence fécale (énoncé 3.1). De plus, la qualité de vie est altérée selon l’activité de la maladie et les comorbidités (énoncé 3.3).',
 'Cependant, les symptômes chevauchent ceux du syndrome de l’intestin irritable. C’est pourquoi l’EMCG demande d’exclure une colite microscopique chez le patient qui remplit les critères d’un trouble fonctionnel, surtout s’il a des facteurs de risque ou ne répond pas au traitement du syndrome de l’intestin irritable (énoncé 3.2). Par ailleurs, l’activité se mesure par les ' + w('k52-hjortswang', 'critères de Hjortswang') + ' : la rémission clinique correspond à moins de 3 selles par jour en moyenne et à moins d’une selle aqueuse par jour, sur une semaine (énoncé 3.4).')
 + quiz('Une patiente de 70 ans a une diarrhée aqueuse nocturne depuis 4 mois et remplit les critères de Rome du syndrome de l’intestin irritable. Que faire ?',
   [('Retenir le syndrome de l’intestin irritable sans autre examen', False), ('Coloscopie avec biopsies du côlon droit et gauche', True), ('Calprotectine pour exclure la colite microscopique', False)],
   'L’âge, les selles nocturnes et la diarrhée aqueuse imposent d’exclure une colite microscopique ; or, la calprotectine n’est pas utile pour l’exclure (EMCG 2021, énoncés 3.2 et 4.7).')
 + key('Diarrhée aqueuse, non sanglante, besoins impérieux, selles nocturnes, incontinence ; à exclure devant un « intestin irritable » atypique ; rémission : < 3 selles/j et < 1 selle aqueuse/j.')
 + src(EMCG))

C.a(5, 'Démarche diagnostique', P(
 'Devant ce tableau, l’examen clé est l’' + w('k52-biopsies', 'iléocoloscopie avec biopsies') + '. Ainsi, l’EMCG recommande des biopsies prélevées au moins dans le côlon droit et dans le côlon gauche (recommandation 4.5, forte) ; en effet, les lésions sont présentes des deux côtés dans 95 à 98 % des cas. Or, l’aspect endoscopique est souvent normal, ou montre des anomalies non spécifiques (énoncé 4.1) : c’est pourquoi des biopsies doivent être faites même si la muqueuse paraît saine.',
 'Par ailleurs, la ' + w('k52-calpro', 'calprotectine fécale') + ' n’est pas utile pour exclure ou suivre la maladie (énoncé 4.7). En revanche, une maladie cœliaque doit être recherchée chez tout patient atteint de colite microscopique (recommandation 4.8, forte), car elle y est plus fréquente. Enfin, la recherche d’une diarrhée par acides biliaires n’est pas systématique, mais elle peut être envisagée en cas d’échec du budésonide (recommandation 4.10).')
 + key('Biopsies du côlon droit et gauche même si l’endoscopie est normale ; calprotectine inutile ; dépister la maladie cœliaque ; acides biliaires si échec du budésonide.')
 + src(EMCG))

C.a(6, 'Critères histologiques', P(
 'Le diagnostic repose donc sur l’histologie standard, en coloration hématoxyline-éosine. Ainsi, la colite collagène associe une bande de collagène sous-épithéliale épaissie d’au moins 10 µm et un infiltrat inflammatoire accru du chorion (énoncé 4.2). En revanche, la colite lymphocytaire associe au moins 20 ' + w('k52-lie', 'lymphocytes intraépithéliaux') + ' pour 100 cellules épithéliales de surface, un infiltrat accru du chorion et une bande collagène non significativement épaissie, inférieure à 10 µm (énoncé 4.3).',
 'De plus, l’EMCG décrit une ' + w('k52-cmi', 'colite microscopique incomplète') + ' : bande collagène de plus de 5 µm mais de moins de 10 µm, ou plus de 10 mais moins de 20 lymphocytes intraépithéliaux, avec un infiltrat modéré (énoncé 4.4). Par ailleurs, une surveillance histologique n’est pas recommandée après le diagnostic (recommandation 4.6).')
 + C.img('k52_collagene.gif', 'Coupe histologique de muqueuse colique en coloration trichrome : sous l’épithélium de surface, une bande continue colorée en bleu, nettement épaissie.', 'Colite collagène, coloration trichrome : la bande de collagène sous-épithéliale, colorée en bleu, est épaissie (≥ 10 µm), sous un épithélium de surface altéré.', credit({'auteur': 'Ed Uthman', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Collagenous_Colitis,_Trichrome_Stain_(3884931660).jpg'}))
 + C.img('k52_lympho.gif', 'Coupe histologique annotée de muqueuse colique : nombreux petits noyaux sombres de lymphocytes intercalés entre les cellules épithéliales de surface.', 'Colite lymphocytaire, coloration hématoxyline-éosine annotée : excès de lymphocytes intraépithéliaux (≥ 20 pour 100 cellules épithéliales), sans épaississement de la bande collagène.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_lymphocytic_colitis,_annotated.jpg'}))
 + key('Collagène : bande ≥ 10 µm + infiltrat. Lymphocytaire : ≥ 20 LIE/100 cellules + infiltrat + bande < 10 µm. Incomplète : bande 5-10 µm ou 10-20 LIE.')
 + src(EMCG))

C.a(7, 'Traiter la colite microscopique', P(
 'Le diagnostic établi, le traitement commence par les mesures simples. Ainsi, l’EMCG suggère de retirer tout médicament dont l’introduction est chronologiquement liée au début de la diarrhée (recommandation 1.8, faible) ; de plus, l’arrêt du tabac est conseillé, bien que son effet sur l’évolution ne soit pas démontré (énoncé 1.6). Par ailleurs, le ' + w('k52-d-loperamide', 'lopéramide') + ' peut être utilisé dans une forme légère, selon l’avis des experts (recommandation 5.6).',
 'Ensuite, le traitement de référence est le ' + w('k52-d-budesonide', 'budésonide') + ' oral, recommandé pour induire la rémission dans la colite collagène (recommandation 5.1.1, forte) comme dans la colite lymphocytaire (5.1.2, forte). En effet, l’information professionnelle suisse d’Entocort CIR® prévoit 9 mg/j pendant 8 semaines, avec une réduction progressive au cours des deux dernières semaines. En revanche, la mésalazine (5.4), les probiotiques (5.10), les antibiotiques (5.9) et la prednisolone ou tout corticoïde autre que le budésonide (5.11) ne sont pas recommandés.')
 + trap('L’arrêt d’un IPP, d’un AINS ou d’un ISRS est raisonnable s’il existe un lien chronologique avec la diarrhée ; cependant, l’EMCG souligne que l’association n’est pas causale par elle-même : il faut peser l’indication de chaque médicament.', 'Nuance')
 + key('Retirer les médicaments suspects, arrêter le tabac ; lopéramide si léger ; budésonide 9 mg/j 8 semaines ; ni mésalazine, ni probiotiques, ni antibiotiques, ni prednisolone.')
 + src(EMCG, FI('Entocort CIR®')))

C.a(8, 'Rechutes, entretien et formes réfractaires', P(
 'Après l’induction, les rechutes sont fréquentes. C’est pourquoi le budésonide oral est recommandé pour maintenir la rémission dans la colite collagène (recommandation 5.2.1, forte) et suggéré dans la colite lymphocytaire (5.2.2, faible). Ainsi, 6 mg/j pendant 6 mois réduisent le risque de rechute clinique, et des doses plus faibles, par exemple 3 mg/j en alternance avec 6 mg/j, semblent aussi efficaces ; en outre, le risque d’effets indésirables graves n’est pas accru (énoncé 5.3.1).',
 'Cependant, un usage prolongé peut diminuer la densité minérale osseuse (énoncé 5.3.2). Par ailleurs, en cas de diarrhée par acides biliaires associée, un ' + w('k52-chelateur', 'chélateur des acides biliaires') + ' est suggéré (recommandation 5.7). Enfin, chez le patient sélectionné qui ne répond pas au budésonide, les thiopurines, les anti-TNF ou le védolizumab sont recommandés, alors que le méthotrexate ne l’est pas (recommandation 5.12) ; la chirurgie reste un dernier recours (5.13).')
 + trap('L’information professionnelle suisse d’Entocort CIR® n’autorise le budésonide que pour l’« initiation d’une rémission » de la colite microscopique : l’entretien recommandé par l’EMCG est donc hors indication en Suisse. À valider à l’audit.', 'Point à valider')
 + key('Entretien : budésonide à la dose minimale efficace (≈ 3-6 mg/j), hors indication en Suisse ; os à surveiller ; chélateur si acides biliaires ; réfractaire : thiopurines, anti-TNF, védolizumab.')
 + src(EMCG, FI('Entocort CIR®')))

C.a(9, 'Pronostic et autres colites non infectieuses', P(
 'Sur le plan pronostique, la colite microscopique est rassurante. En effet, elle n’augmente ni le risque de cancer colorectal ni celui d’adénome, et aucun programme de coloscopie de surveillance particulier n’est recommandé (recommandation 1.9, forte). Toutefois, l’évolution chronique et récidivante pèse sur la qualité de vie.',
 'Par ailleurs, les autres sous-catégories de K52 relèvent d’abord de la cause. Ainsi, une colite ou une rectite radique (K52.0) survient pendant ou après une irradiation pelvienne ; une colite toxique (K52.1) impose de retirer le médicament ou le toxique ; une forme allergique ou alimentaire (K52.2) fait rechercher l’aliment responsable. Enfin, la ' + w('k52-indeterminee', 'colite indéterminée') + ' (K52.3) désigne une colite inflammatoire chronique qu’on ne peut classer entre maladie de Crohn et rectocolite ; elle suit alors les principes de traitement des maladies inflammatoires de l’intestin.')
 + trap('Les recommandations spécifiques de la rectite radique et des colites allergiques n’ont pas été lues pour ce cours ; aucune dose ni stratégie n’est donc donnée. TODO : intégrer une recommandation européenne dédiée.', 'Lacune documentaire')
 + key('Colite microscopique : pas de surrisque de cancer, pas de surveillance spécifique. Autres K52 : traiter la cause (irradiation, toxique, aliment) ; colite indéterminée : raisonner comme une MICI.')
 + C.pareto('pareto-k52-clinique', 'Colite microscopique', ['k52-2', 'k52-4', 'k52-5', 'k52-6', 'k52-7', 'k52-8', 'k52-9'],
     ['Femme âgée, tabac, IPP, AINS, ISRS.',
      'Diarrhée aqueuse, nocturne, sans sang.',
      'Biopsies droite et gauche même si muqueuse normale.',
      'Collagène : bande ≥ 10 µm ; lymphocytaire : ≥ 20 LIE/100.',
      'Budésonide 9 mg/j 8 semaines.',
      'Pas de mésalazine, ni de prednisolone.',
      'Pas de surveillance du cancer.'])
 + src(EMCG))

C.a(10, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. Les biopsies du côlon droit et gauche montrent une bande collagène de 18 µm et un infiltrat du chorion : il s’agit donc d’une colite collagène. De plus, les anticorps de la maladie cœliaque sont négatifs.',
 'Dès lors, la conduite associe trois mesures. D’abord, l’anti-inflammatoire est arrêté et l’indication de l’oméprazole réévaluée, et l’arrêt du tabac est proposé. Ensuite, le budésonide 9 mg/j est prescrit pendant 8 semaines, avec une décroissance finale. Enfin, en cas de rechute, un entretien à faible dose est discuté, en informant la patiente de son statut hors indication et en surveillant l’os.')
 + key('Biopsies → colite collagène → cœliaque exclue → arrêt des médicaments suspects → budésonide → entretien à faible dose si rechute.')
 + src(EMCG))

C.a(11, 'Critères formels et paramètres clés', alert(
 '<p><b>Colite collagène.</b> Bande collagène sous-épithéliale ≥ 10 µm + infiltrat accru du chorion (HE). <b>Colite lymphocytaire.</b> ≥ 20 lymphocytes intraépithéliaux/100 cellules de surface + infiltrat accru + bande < 10 µm. <b>Forme incomplète.</b> Bande > 5 et < 10 µm, ou > 10 et < 20 LIE. <b>Rémission (Hjortswang).</b> < 3 selles/j et < 1 selle aqueuse/j en moyenne sur une semaine.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Incidence ≈ 11,4/100 000/an ; 12,8 % des diarrhées aqueuses chroniques inexpliquées ; biopsies droite et gauche (lésions bilatérales dans 95-98 %) ; budésonide 9 mg/j 8 semaines (FI) ; entretien 6 mg/j ou moins (EMCG, hors indication en Suisse).</div>'
 + src(EMCG, FI('Entocort CIR®')))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Place'], [
   ['Diarrhée infectieuse ?', 'Coprocultures, C. difficile', 'Diarrhée prolongée'],
   ['Colite microscopique ?', w('k52-biopsies', 'Iléocoloscopie avec biopsies droite et gauche'), 'Examen clé'],
   ['Maladie cœliaque associée ?', 'Sérologie (anticorps anti-transglutaminase IgA et IgA totales)', 'Systématique (recommandation 4.8)'],
   ['Exclure par un marqueur fécal ?', w('k52-calpro', 'Calprotectine'), 'Inutile (énoncé 4.7)'],
   ['Échec du budésonide ?', 'Recherche d’une diarrhée par acides biliaires', 'Recommandation 4.10']])
 + P('Le tableau se lit de haut en bas : ainsi, seules les biopsies établissent le diagnostic, et les autres examens cherchent une cause associée ou un diagnostic différentiel.')
 + key('Biopsies coliques droite et gauche ; cœliaque systématique ; calprotectine inutile ; acides biliaires si échec.')
 + src(EMCG))

C.e(2, 'Lire le compte rendu histologique', P(
 'Le pathologiste mesure la bande collagène et compte les lymphocytes intraépithéliaux, sur coupes en hématoxyline-éosine ; ainsi, le compte rendu doit fournir ces deux chiffres. Or, la bande peut varier selon le segment, d’où l’intérêt de biopsies multiples et orientées. Par ailleurs, une coloration trichrome aide à visualiser le collagène, mais les critères de l’EMCG s’appliquent aux coupes standard.')
 + C.img('k52_collagene_he.gif', 'Coupe histologique en hématoxyline-éosine : sous l’épithélium de surface, une bande rose homogène et épaisse, au-dessus d’un chorion inflammatoire.', 'Colite collagène en coloration hématoxyline-éosine : bande de collagène sous-épithéliale homogène, épaissie au-delà de 10 µm.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_collagenous_colitis.jpg'}))
 + key('Compte rendu : épaisseur de la bande (µm) et nombre de LIE/100 cellules ; critères sur coupes HE.')
 + C.pareto('pareto-k52-examens', 'Examens', ['k52-e-1', 'k52-e-2'],
     ['Biopsies droite et gauche.',
      'Bande ≥ 10 µm ou ≥ 20 LIE/100.',
      'Cœliaque à rechercher.',
      'Calprotectine inutile.'])
 + src(EMCG))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : côlon droit et côlon gauche', P(
 'Le côlon droit, du cæcum à l’angle colique droit, réabsorbe une grande part de l’eau ; ainsi, une atteinte diffuse du côlon perturbe la déshydratation des selles. Or, les lésions de la colite microscopique peuvent être inégalement réparties, parfois plus marquées à droite. Par conséquent, des biopsies limitées au rectum ou au sigmoïde peuvent les manquer.')
 + key('C’est pourquoi l’EMCG exige des biopsies des deux côtés du côlon.', 'Science → examen.'))
C.s('histo', 'Histologie', 'Histologie : la membrane basale et le chorion', P(
 'Sous l’épithélium de surface du côlon, une fine couche de collagène, de quelques microns, sépare l’épithélium du chorion ; ainsi, son épaississement au-delà de 10 µm définit la colite collagène. De plus, l’épithélium normal contient moins de cinq lymphocytes intraépithéliaux pour 100 cellules ; or, la colite lymphocytaire en compte au moins 20.')
 + key('Deux mesures simples, l’épaisseur du collagène et le compte lymphocytaire, distinguent les deux formes.', 'Science → diagnostic.'))
C.s('physio', 'Physiologie', 'Physiologie : réabsorption hydrique colique', P(
 'Le côlon réabsorbe chaque jour plus d’un litre d’eau, couplée au transport actif du sodium par l’épithélium ; ainsi, toute atteinte épithéliale réduit cette réabsorption. De plus, des acides biliaires non réabsorbés dans l’iléon stimulent la sécrétion colique. Par conséquent, la colite microscopique et la malabsorption des acides biliaires produisent toutes deux une diarrhée aqueuse.')
 + key('C’est pourquoi un chélateur des acides biliaires peut aider quand le budésonide échoue.', 'Science → traitement.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : premier passage du budésonide', P(
 'Le budésonide est un glucocorticoïde puissant, mais environ 85 à 90 % de la dose absorbée est inactivée au premier passage hépatique par le CYP3A4 ; ainsi, l’exposition systémique est faible. Toutefois, les inhibiteurs puissants du CYP3A4, comme le kétoconazole, augmentent cette exposition. Par conséquent, ils sont évités, et l’usage prolongé reste surveillé, notamment pour l’os.')
 + trap('La fraction inactivée au premier passage (85-90 %) est une donnée pharmacologique classique non vérifiée dans la FI lue pour ce cours. TODO : confirmer dans la FI Entocort CIR®.', 'À vérifier')
 + key('Premier passage élevé : action locale, peu d’effets systémiques ; attention aux inhibiteurs du CYP3A4.', 'Science → sécurité.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, le budésonide domine la stratégie, et les autres traitements sont des appoints ou des recours.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Corticoïde à fort premier passage', 'Budésonide (Entocort CIR®)', 'Induction (et entretien hors indication)', w('k52-d-budesonide', 'Monographie')],
   ['Antidiarrhéique opioïde périphérique', 'Lopéramide', 'Forme légère', w('k52-d-loperamide', 'Fiche')],
   ['Chélateur des acides biliaires', 'Colestyramine', 'Diarrhée par acides biliaires associée', w('k52-chelateur', 'Fiche')],
   ['Immunomodulateurs et biothérapies', 'Thiopurines, anti-TNF, védolizumab', 'Formes réfractaires sélectionnées', w('k52-refractaire', 'Fiche')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, les immunosuppresseurs ne sont envisagés qu’après l’échec du budésonide.')
 + key('Budésonide d’abord ; lopéramide si léger ; chélateur si acides biliaires ; immunosuppresseurs si réfractaire.')
 + src(EMCG))

C.p(2, 'Doses et statut réglementaire', P('Les éléments suivants proviennent de l’EMCG 2021 et de l’information professionnelle suisse ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Situation', 'Dose ou règle', 'Source'], [
   ['Budésonide (Entocort CIR®)', 'Induction', '9 mg/j 8 semaines, réduction progressive les 2 dernières semaines', 'FI Entocort CIR®'],
   ['Budésonide', 'Entretien', '6 mg/j 6 mois, ou 3 mg/j en alternance avec 6 mg/j', 'EMCG 2021 (hors indication en Suisse)'],
   ['Lopéramide', 'Forme légère', 'Dose : TODO (FI non lue)', 'EMCG 2021, avis d’experts'],
   ['Méthotrexate', 'Forme réfractaire', 'Non recommandé', 'EMCG 2021, 5.12']])
 + P('Par exemple, chez la patiente du début, le budésonide est prescrit à 9 mg/j le matin ; ensuite, en cas de rechute, une dose de 3 à 6 mg/j est discutée, avec une densitométrie osseuse si l’usage se prolonge.')
 + key('Budésonide 9 mg/j 8 semaines ; entretien 3-6 mg/j hors indication ; méthotrexate non recommandé.')
 + src(EMCG, FI('Entocort CIR®')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'Le budésonide n’augmente pas le risque d’effets indésirables graves dans la colite microscopique (énoncé 5.3.1) ; cependant, un usage prolongé peut réduire la densité minérale osseuse (énoncé 5.3.2). C’est pourquoi la dose d’entretien est la plus faible efficace, et l’os est surveillé chez la patiente âgée.', 'Sécurité.')
 + P('Par ailleurs, les thiopurines et les biothérapies des formes réfractaires imposent les mêmes précautions que dans les maladies inflammatoires de l’intestin : dépistage infectieux, formule sanguine et vaccinations. Enfin, le lopéramide est arrêté en cas de fièvre ou de diarrhée sanglante, qui font chercher une autre cause.')
 + key('Dose minimale efficace de budésonide ; surveillance osseuse ; précautions des immunosuppresseurs ; lopéramide arrêté si fièvre ou sang.')
 + C.pareto('pareto-k52-pharma', 'Pharmacologie', ['k52-p-1', 'k52-p-2', 'k52-p-3'],
     ['Budésonide 9 mg/j 8 semaines.',
      'Entretien 3-6 mg/j, hors indication en Suisse.',
      'Pas de mésalazine, de prednisolone, de probiotiques ni d’antibiotiques.',
      'Réfractaire : thiopurines, anti-TNF, védolizumab ; pas de méthotrexate.'])
 + src(EMCG))

# ---------------- Fenêtres
L = lab
C.pop('k52-cm', 'Colite microscopique', L(('Définition', 'Colite chronique à diarrhée aqueuse, muqueuse normale ou presque à l’endoscopie, histologie anormale.'), ('Formes', 'Collagène, lymphocytaire, incomplète.'), ('Code', 'K52.8 (autres formes précisées).')) + src(EMCG))
C.pop('k52-cc', 'Colite collagène', L(('Critères (énoncé 4.2)', 'Bande collagène sous-épithéliale ≥ 10 µm et infiltrat accru du chorion, sur coupes HE.')) + src(EMCG))
C.pop('k52-cl', 'Colite lymphocytaire', L(('Critères (énoncé 4.3)', '≥ 20 lymphocytes intraépithéliaux/100 cellules de surface, infiltrat accru, bande < 10 µm.')) + src(EMCG))
C.pop('k52-cmi', 'Colite microscopique incomplète', L(('Critères (énoncé 4.4)', 'Bande > 5 et < 10 µm, ou > 10 et < 20 LIE/100 cellules, avec infiltrat modéré.')) + src(EMCG))
C.pop('k52-lie', 'Lymphocytes intraépithéliaux', L(('Définition', 'Lymphocytes T situés entre les cellules épithéliales de surface.'), ('Seuil', '≥ 20/100 cellules : colite lymphocytaire.')) + src(EMCG))
C.pop('k52-hjortswang', 'Critères de Hjortswang', L(('Rémission clinique', 'Moins de 3 selles/j et moins d’une selle aqueuse/j en moyenne, sur une semaine de recueil.'), ('Statut', 'Critère recommandé en l’absence d’indice validé (énoncé 3.4).')) + src(EMCG))
C.pop('k52-biopsies', 'Biopsies coliques', L(('Règle (recommandation 4.5, forte)', 'Au moins côlon droit et côlon gauche, même si la muqueuse paraît normale.'), ('Rendement', 'Lésions bilatérales dans 95-98 % des cas.')) + src(EMCG))
C.pop('k52-calpro', 'Calprotectine fécale', L(('Colite microscopique', 'Non utile pour exclure ou suivre la maladie (énoncé 4.7).'), ('Ailleurs', 'Utile pour Crohn et rectocolite.')) + src(EMCG))
C.pop('k52-dab', 'Diarrhée par malabsorption des acides biliaires', L(('Mécanisme', 'Acides biliaires non réabsorbés dans l’iléon, qui stimulent la sécrétion colique.'), ('Fréquence', 'Coexiste avec la colite microscopique chez environ 14 % des patients (étude SeHCAT citée par l’EMCG).'), ('Traitement', 'Chélateur des acides biliaires (recommandation 5.7).')) + src(EMCG))
C.pop('k52-ipp', 'Inhibiteurs de la pompe à protons', L(('Lien', 'Usage chronique associé à la colite microscopique, sans preuve de causalité (énoncé 1.7).'), ('Conduite', 'Réévaluer l’indication, arrêter si lien chronologique.')) + src(EMCG))
C.pop('k52-isrs', 'Inhibiteurs sélectifs de la recapture de la sérotonine', L(('Lien', 'Usage chronique associé à la colite microscopique (énoncé 1.7).'), ('Conduite', 'Discuter l’arrêt ou le changement si lien chronologique.')) + src(EMCG))
C.pop('k52-chelateur', 'Chélateurs des acides biliaires', L(('Exemple', 'Colestyramine.'), ('Place', 'Diarrhée par acides biliaires associée (recommandation 5.7, faible).')) + src(EMCG))
C.pop('k52-refractaire', 'Colite microscopique réfractaire', L(('Options (recommandation 5.12)', 'Thiopurines, anti-TNF, védolizumab chez des patients sélectionnés.'), ('Non recommandé', 'Méthotrexate.'), ('Dernier recours', 'Chirurgie (5.13).')) + src(EMCG))
C.pop('k52-indeterminee', 'Colite indéterminée', L(('Définition', 'Colite inflammatoire chronique qui ne peut être classée entre maladie de Crohn et rectocolite.'), ('Codes', 'K52.30 pancolite, K52.31 gauche, K52.32 rectosigmoïde, K52.38 autres.')))
C.pop('k52-d-budesonide', 'Budésonide (Entocort CIR®)', L(('Indication suisse', 'Initiation d’une rémission de la colite microscopique aiguë.'), ('Dose', '9 mg/j le matin 8 semaines ; réduction progressive les 2 dernières semaines.'), ('EMCG 2021', 'Induction (fort) ; entretien (fort dans la colite collagène, faible dans la lymphocytaire).')) + src(FI('Entocort CIR®'), EMCG))
C.pop('k52-d-loperamide', 'Lopéramide', L(('Mécanisme', 'Agoniste des récepteurs opioïdes μ intestinaux : ralentit le transit.'), ('Place', 'Forme légère, selon l’avis des experts (recommandation 5.6).')) + src(EMCG))

C.termes = [
 (r'colite microscopique', 'k52-cm'), (r'colite collagène', 'k52-cc'), (r'colite lymphocytaire', 'k52-cl'), (r'lymphocytes intraépithéliaux', 'k52-lie'),
 (r'Hjortswang', 'k52-hjortswang'), (r'calprotectine', 'k52-calpro'), (r'acides biliaires', 'k52-dab'), (r'budésonide', 'k52-d-budesonide'),
 (r'lopéramide', 'k52-d-loperamide'), (r'colite indéterminée', 'k52-indeterminee'), (r'chélateur', 'k52-chelateur'), (r'oméprazole', 'k52-ipp'),
 (r'biopsies', 'k52-biopsies'), (r'ISRS', 'k52-isrs'), (r'IPP', 'k52-ipp'),
]

C.write()
