import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K51', 'Rectocolite hémorragique',
    'K51 — Colite ulcéreuse (rectocolite hémorragique) · CIM-10-GM 2024 · Côlon et rectum',
    'Adulte · étendue de Montréal, gravité, induction et entretien, colite aiguë grave · rédaction du 09.10.2026 · référentiels ECCO traitement médical 2022 et chirurgical 2022, classification de Montréal 2005, informations professionnelles suisses',
    'Pharmacologie de la rectocolite hémorragique')
w = C.w
MED = ('Raine T. et al., ECCO Guidelines on Therapeutics in Ulcerative Colitis: Medical Treatment, J Crohns Colitis 2022;16:2-17', 'https://doi.org/10.1093/ecco-jcc/jjab178')
CHIR = ('Spinelli A. et al., ECCO Guidelines on Therapeutics in Ulcerative Colitis: Surgical Treatment, J Crohns Colitis 2022;16:179-189', 'https://doi.org/10.1093/ecco-jcc/jjab177')
MTL = ('Satsangi J. et al., The Montreal classification of inflammatory bowel disease, Gut 2006;55:749-753', 'https://doi.org/10.1136/gut.2005.082909')
TW = ('Truelove S. C., Witts L. J., Cortisone in ulcerative colitis: final report on a therapeutic trial, Br Med J 1955;2:1041-1048', 'https://doi.org/10.1136/bmj.2.4947.1041')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 32 ans, non fumeuse, a depuis six semaines des selles glaireuses et sanglantes, cinq fois par jour, avec des ' + w('k51-tenesme', 'épreintes et un ténesme') + '. Or, les coprocultures sont négatives et la calprotectine fécale est très élevée. <b>La question est donc de savoir s’il s’agit d’une rectocolite hémorragique, quelle en est l’étendue et la gravité, et quel traitement débuter.</b>',
 'Pour y répondre, le médecin doit savoir : confirmer le diagnostic par l’endoscopie et l’histologie ; définir l’étendue selon la ' + w('k51-montreal', 'classification de Montréal') + ' ; mesurer la gravité et reconnaître la ' + w('k51-cagg', 'colite aiguë grave') + ' par les ' + w('k51-tw', 'critères de Truelove et Witts') + ' ; choisir la voie et la molécule, d’abord la ' + w('k51-d-mesalazine', 'mésalazine') + ' ; enfin, organiser l’entretien et la surveillance.')
 + key('Diarrhée sanglante, glaires, ténesme, calprotectine élevée et coprocultures négatives : penser rectocolite hémorragique.', 'Point de départ.'))

C.a(1, 'Définition', P(
 'La rectocolite hémorragique est une maladie inflammatoire chronique de l’intestin, caractérisée par une inflammation du côlon qui s’étend de façon continue depuis le rectum, sur une longueur variable (ECCO 2022). Ainsi, à la différence de la maladie de Crohn, elle épargne l’intestin grêle et reste limitée à la muqueuse ; de plus, elle évolue par poussées et rémissions.',
 'Par conséquent, l’étendue de l’atteinte structure toute la prise en charge. En effet, une proctite relève souvent d’un traitement local, alors qu’une colite étendue exige un traitement oral. C’est pourquoi la CIM-10-GM distingue notamment la pancolite (K51.0), la proctite (K51.2), la rectosigmoïdite (K51.3) et la colite gauche (K51.5).')
 + table(['Étendue (Montréal)', 'Limite', 'Traitement de première ligne d’une poussée légère à modérée'], [
   ['E1 : proctite', 'Rectum seul', 'Mésalazine rectale (suppositoire)'],
   ['E2 : colite gauche', 'En aval de l’angle colique gauche', 'Mésalazine rectale + orale'],
   ['E3 : colite étendue', 'Au-delà de l’angle colique gauche', 'Mésalazine orale (+ rectale)']])
 + P('Le tableau se lit de haut en bas : en effet, plus l’atteinte remonte, plus le traitement oral devient indispensable, car le traitement rectal n’atteint pas le côlon proximal.')
 + key('Inflammation muqueuse continue depuis le rectum ; étendue E1, E2, E3 ; l’étendue décide de la voie d’administration.')
 + src(MED, MTL))

C.a(2, 'Épidémiologie et facteurs de risque', P(
 'Après la définition, il faut situer la patiente. Ainsi, la maladie débute surtout chez l’adulte jeune, avec un second pic possible plus tard dans la vie. De plus, elle résulte, comme la maladie de Crohn, d’une interaction entre gènes, microbiote et environnement. Cependant, le tabac a ici un effet inverse : en effet, l’arrêt du tabac est souvent suivi de l’apparition ou de l’aggravation de la maladie, ce qui ne justifie évidemment pas de fumer.',
 'Par ailleurs, la rectocolite s’associe à la ' + w('k51-csp', 'cholangite sclérosante primitive') + ', qui en aggrave le risque de cancer colorectal. En outre, l’ancienneté, l’étendue et l’intensité de l’inflammation augmentent ce risque ; c’est pourquoi une surveillance endoscopique est organisée.')
 + trap('Aucune donnée suisse d’incidence vérifiée n’a été retrouvée dans les sources lues ; aucun chiffre n’est donc avancé.', 'Lacune documentaire')
 + key('Adulte jeune ; tabac « protecteur » paradoxal ; association à la cholangite sclérosante primitive ; risque de cancer colorectal selon durée, étendue, inflammation.')
 + src(MED))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre la clinique, il faut partir de la muqueuse. D’abord, la barrière épithéliale colique et sa couche de mucus sont altérées ; ainsi, le microbiote stimule de façon excessive l’immunité muqueuse. Ensuite, des lymphocytes T et des polynucléaires infiltrent la muqueuse, envahissent les cryptes et forment des ' + w('k51-abces', 'abcès cryptiques') + ', puis des ulcérations.',
 'Par conséquent, la muqueuse saigne et sécrète du mucus, et le rectum enflammé provoque le ténesme et les besoins impérieux. Toutefois, comme l’inflammation reste superficielle, les fistules sont rares ; en revanche, une poussée grave peut paralyser la musculeuse et dilater le côlon, ce qui définit le ' + w('k51-megacolon', 'mégacôlon toxique') + '.')
 + key('Barrière muqueuse altérée → inflammation muqueuse continue → abcès cryptiques, ulcérations → saignement, glaires, ténesme ; forme grave : mégacôlon toxique.')
 + src(MED, CHIR))

C.a(4, 'Présentation clinique', P(
 'La présentation reflète donc l’étendue et la gravité. Ainsi, la proctite donne des rectorragies, des glaires, des épreintes et un ténesme, parfois avec une constipation paradoxale ; à l’inverse, la colite étendue provoque une diarrhée sanglante fréquente, des douleurs abdominales et, dans les formes graves, de la fièvre, une tachycardie et une anémie.',
 'De plus, l’examen recherche des ' + w('k51-mei', 'manifestations extra-intestinales') + ' articulaires, cutanées, oculaires ou hépatobiliaires. Par ailleurs, devant toute poussée, il faut éliminer une infection, en particulier par Clostridioides difficile, et, dans une forme grave ou réfractaire, une infection à ' + w('k51-cmv', 'cytomégalovirus') + '.')
 + C.img('k51_endoscopie.gif', 'Photographie endoscopique d’une muqueuse colique rouge, granitée, friable, sans relief vasculaire, couverte par endroits de fibrine.', 'Rectocolite hémorragique, vue endoscopique : muqueuse érythémateuse et granitée, disparition de la trame vasculaire, friabilité et ulcérations superficielles, de façon continue.', credit({'auteur': 'Sebb (Wikipédia en anglais), auteur présumé', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Ulcerative_colitis.jpg'}))
 + key('Proctite : rectorragies, glaires, ténesme. Colite étendue : diarrhée sanglante. Forme grave : fièvre, tachycardie, anémie. Toujours exclure C. difficile ; CMV si grave ou réfractaire.')
 + src(MED))

C.a(5, 'Démarche diagnostique', P(
 'Devant ce tableau, le diagnostic associe arguments cliniques, biologiques, endoscopiques et histologiques. D’abord, la biologie évalue l’inflammation (CRP), l’anémie et l’albumine, et la ' + w('k51-calpro', 'calprotectine fécale') + ' confirme l’inflammation colique. De plus, les coprocultures et la recherche de Clostridioides difficile écartent une colite infectieuse.',
 'Ensuite, la ' + w('k51-colo', 'coloscopie') + ' avec iléoscopie montre une atteinte continue depuis le rectum et en fixe l’étendue ; en outre, des biopsies étagées documentent une inflammation chronique, avec distorsion architecturale des cryptes. Cependant, en cas de colite grave, une rectosigmoïdoscopie prudente, sans préparation complète, suffit, car la coloscopie totale expose à la perforation.')
 + C.img('k51_histo.gif', 'Coupe histologique de muqueuse colique ulcérée : les cryptes normales ont disparu, remplacées par un tissu de granulation riche en cellules inflammatoires.', 'Rectocolite hémorragique sévère, coloration hématoxyline-éosine : ulcération avec perte de l’architecture cryptique, tissu de granulation et infiltrat inflammatoire dense riche en polynucléaires.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_severe_ulcerative_colitis.jpg'}))
 + quiz('Poussée grave de colite chez une patiente fébrile. Quel examen endoscopique en premier ?',
   [('Coloscopie totale après préparation complète', False), ('Rectosigmoïdoscopie prudente avec biopsies', True), ('Capsule endoscopique', False)],
   'Dans une colite grave, une rectosigmoïdoscopie avec peu d’insufflation suffit au diagnostic, aux biopsies (dont la recherche de CMV) et limite le risque de perforation.')
 + key('CRP, hémoglobine, albumine, calprotectine ; coprocultures et C. difficile ; coloscopie avec biopsies étagées ; si colite grave : rectosigmoïdoscopie prudente.')
 + src(MED))

C.a(6, 'Évaluer la gravité', P(
 'Le diagnostic posé, la gravité oriente le traitement et le lieu de soins. Ainsi, l’ECCO distingue les poussées légères à modérées et les poussées modérées à sévères, en reconnaissant que ces catégories forment un continuum. Par ailleurs, le ' + w('k51-mayo', 'score de Mayo') + ' associe fréquence des selles, rectorragies, aspect endoscopique et appréciation globale ; il sert surtout dans les essais et le suivi.',
 'En pratique, il faut surtout reconnaître la ' + w('k51-cagg', 'colite aiguë grave') + ', qui impose une hospitalisation. En effet, selon les ' + w('k51-tw', 'critères de Truelove et Witts') + ', au moins six selles sanglantes par jour associées à au moins un signe systémique (fréquence cardiaque > 90/min, température > 37,8 °C, hémoglobine < 10,5 g/dl ou vitesse de sédimentation > 30 mm/h) définissent une poussée grave.')
 + quiz('Huit selles sanglantes par jour, pouls à 104/min, hémoglobine 11,8 g/dl. Gravité ?',
   [('Poussée modérée : traitement ambulatoire', False), ('Colite aiguë grave : hospitalisation et corticoïdes IV', True), ('Proctite', False)],
   'Six selles sanglantes ou plus et au moins un critère systémique (ici la tachycardie > 90/min) définissent la colite aiguë grave selon Truelove et Witts.')
 + key('Truelove et Witts : ≥ 6 selles sanglantes/j + ≥ 1 critère (FC > 90, T > 37,8 °C, Hb < 10,5 g/dl, VS > 30 mm/h) = colite aiguë grave → hospitalisation.')
 + src(TW, MED, CHIR))

C.a(7, 'Traiter une poussée légère à modérée', P(
 'Dans une poussée légère à modérée, la ' + w('k51-d-mesalazine', 'mésalazine') + ' est le traitement de base. Ainsi, l’ECCO recommande le 5-ASA oral à au moins 2 g/j pour induire la rémission (recommandation forte) ; de même, dans une colite distale, la mésalazine rectale à au moins 1 g/j est recommandée (recommandation forte). De plus, pour une atteinte au moins rectosigmoïdienne, l’association orale et rectale est préférée à la voie orale seule (recommandation faible).',
 'Par ailleurs, les corticoïdes rectaux sont efficaces dans la colite distale, mais la mésalazine rectale leur est préférée (recommandation faible). En cas de réponse insuffisante au 5-ASA, un ' + w('k51-d-budmmx', 'corticoïde à libération colique') + ', comme le budésonide MMX, peut induire la rémission (recommandation faible) ; en revanche, les thiopurines ne doivent pas servir à l’induction (recommandation faible contre).')
 + trap('Une proctite « résistante » à la mésalazine orale est souvent une proctite mal traitée : le traitement rectal est indispensable, car la mésalazine orale atteint mal le rectum.', 'Piège')
 + key('5-ASA oral ≥ 2 g/j ; rectal ≥ 1 g/j si distale ; association orale + rectale si ≥ rectosigmoïde ; budésonide MMX si échec du 5-ASA ; pas de thiopurine en induction.')
 + src(MED, FI('Pentasa®'), FI('Cortiment® MMX®')))

C.a(8, 'Traiter une poussée modérée à sévère', P(
 'Dans une poussée modérée à sévère sans critère de gravité aiguë, la ' + w('k51-cs', 'prednisolone orale') + ' est recommandée chez le patient non hospitalisé (recommandation forte). Cependant, les corticoïdes n’entretiennent pas la rémission ; c’est pourquoi un traitement d’entretien est discuté dès ce moment. Ainsi, l’ECCO recommande, en induction comme en entretien, les ' + w('k51-antitnf', 'anti-TNF') + ' (infliximab, adalimumab, golimumab), le ' + w('k51-d-vedolizumab', 'védolizumab') + ', l’ustékinumab et le ' + w('k51-d-tofacitinib', 'tofacitinib') + ' (recommandations fortes).',
 'De plus, le védolizumab est suggéré plutôt que l’adalimumab (recommandation faible), sur la base d’un essai comparatif direct. Par ailleurs, en entretien, les ' + w('k51-thiopurines', 'thiopurines') + ' sont recommandées en monothérapie chez le patient corticodépendant ou intolérant au 5-ASA (recommandation forte). Enfin, le choix tient compte des comorbidités, de la voie d’administration et des risques propres à chaque molécule, notamment thromboemboliques pour le tofacitinib.')
 + alert('Avant tout immunosuppresseur ou biothérapie : dépister tuberculose latente et hépatites virales, vérifier les vaccinations. Le tofacitinib augmente les embolies pulmonaires et les thromboses veineuses et artérielles par rapport aux anti-TNF (FI Xeljanz®) : il est évité chez le patient à risque thromboembolique.', 'Sécurité d’abord.')
 + key('Prednisolone orale en induction ; anti-TNF, védolizumab, ustékinumab, tofacitinib en induction et entretien ; thiopurines en entretien si corticodépendance.')
 + src(MED, FI('Xeljanz®')))

C.a(9, 'Colite aiguë grave', P(
 'Quand les critères de Truelove et Witts sont réunis, la situation devient urgente. Ainsi, le patient est hospitalisé et reçoit des corticoïdes intraveineux en première ligne, qui induisent la rémission et réduisent la mortalité (ECCO 2022, énoncé 1.1). De plus, il faut éliminer C. difficile et le cytomégalovirus, corriger les troubles hydroélectrolytiques et l’anémie, prévenir la maladie thromboembolique et faire suivre le patient conjointement par le gastroentérologue et le chirurgien.',
 'Cependant, jusqu’à 30 % des patients ne répondent pas et nécessitent une colectomie. C’est pourquoi la réponse est réévaluée après quelques jours de corticoïdes ; en cas d’échec, l’' + w('k51-d-infliximab', 'infliximab') + ' ou la ' + w('k51-d-ciclosporine', 'ciclosporine') + ' sont utilisés en traitement de sauvetage, selon l’expérience du centre et le traitement d’entretien envisagé (énoncé 1.2). En revanche, un sauvetage de troisième ligne par anticalcineurine retarde la colectomie au prix d’effets indésirables fréquents, et reste réservé aux centres spécialisés (énoncé 1.4).')
 + C.img('k51_megacolon.gif', 'Radiographie abdominale de face : côlon transverse très dilaté, rempli de gaz, avec perte des haustrations.', 'Mégacôlon toxique compliquant une rectocolite hémorragique : dilatation majeure du côlon transverse sur la radiographie d’abdomen. La patiente a été colectomisée.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Toxic_Megacolon_in_Ulcerative_Colitis.jpg'}))
 + trap('La dose de corticoïdes intraveineux et le jour exact de l’évaluation de la réponse ne figurent pas dans les extraits lus de l’ECCO 2022 ; ils ne sont donc pas chiffrés ici. TODO : compléter à partir du texte intégral de l’ECCO chirurgical 2022.', 'Lacune documentaire')
 + key('Colite aiguë grave : hospitalisation, corticoïdes IV, exclure C. difficile et CMV, thromboprophylaxie, équipe médico-chirurgicale ; échec : infliximab ou ciclosporine ; sinon colectomie.')
 + src(CHIR))

C.a(10, 'Entretien, surveillance et chirurgie', P(
 'Une fois la rémission obtenue, il faut la maintenir. Ainsi, la mésalazine orale à au moins 2 g/j est recommandée en entretien (recommandation forte), et la mésalazine rectale est suggérée dans les formes distales (recommandation faible). De plus, un traitement avancé qui a induit la rémission est poursuivi en entretien : anti-TNF, védolizumab, ustékinumab ou tofacitinib.',
 'Par ailleurs, la rectocolite expose au cancer colorectal ; c’est pourquoi une ' + w('k51-surveillance', 'coloscopie de surveillance') + ' est organisée après plusieurs années d’évolution, plus tôt et plus souvent en cas de cholangite sclérosante primitive. Enfin, la ' + w('k51-colectomie', 'coloproctectomie') + ' est indiquée en cas de colite grave réfractaire, de dysplasie non résécable ou de cancer ; en effet, elle guérit la maladie colique, au prix d’une anastomose iléo-anale avec réservoir ou d’une iléostomie.')
 + trap('Le délai de début et le rythme exacts de la coloscopie de surveillance ne figurent pas dans les recommandations lues ; TODO : recommandation ECCO de surveillance à intégrer.', 'Lacune documentaire')
 + key('Entretien : 5-ASA ≥ 2 g/j, ou traitement avancé qui a induit la rémission ; surveillance du cancer colorectal ; colectomie si réfractaire, dysplasie ou cancer.')
 + C.pareto('pareto-k51-clinique', 'Rectocolite hémorragique', ['k51-1', 'k51-5', 'k51-6', 'k51-7', 'k51-8', 'k51-9', 'k51-10'],
     ['Inflammation muqueuse continue depuis le rectum.',
      'Exclure C. difficile ; coloscopie et biopsies.',
      'Truelove et Witts : ≥ 6 selles sanglantes + 1 critère systémique.',
      'Légère à modérée : mésalazine orale ≥ 2 g/j ± rectale ≥ 1 g/j.',
      'Modérée à sévère : prednisolone, puis biothérapie ou tofacitinib.',
      'Colite aiguë grave : corticoïdes IV ; sauvetage infliximab ou ciclosporine.',
      'Entretien : 5-ASA ≥ 2 g/j ; surveillance du cancer.'])
 + src(MED, CHIR))

C.a(11, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. La coloscopie montre une atteinte continue du rectum jusqu’au côlon sigmoïde, et les biopsies confirment une inflammation chronique ; de plus, il n’y a ni fièvre, ni tachycardie, ni anémie. Il s’agit donc d’une rectocolite hémorragique E2, en poussée modérée sans gravité aiguë.',
 'Dès lors, le traitement associe la mésalazine orale et la mésalazine rectale. Ensuite, la réponse est jugée sur les symptômes puis sur la calprotectine. Enfin, en cas d’échec, un budésonide MMX ou une prednisolone orale seraient discutés, puis un traitement avancé si la maladie devient corticodépendante.')
 + key('Étendue (E2) et gravité (pas de critère de Truelove) → mésalazine orale + rectale → contrôle de la réponse → escalade si échec.')
 + src(MED))

C.a(12, 'Critères formels et paramètres clés', alert(
 '<p><b>Étendue (Montréal).</b> E1 proctite ; E2 colite gauche, en aval de l’angle colique gauche ; E3 colite étendue. <b>Colite aiguë grave (Truelove et Witts).</b> ≥ 6 selles sanglantes par jour et au moins un critère : fréquence cardiaque > 90/min, température > 37,8 °C, hémoglobine < 10,5 g/dl, vitesse de sédimentation > 30 mm/h.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Mésalazine orale ≥ 2 g/j (maximum 4 g/j, FI Pentasa®) ; rectale ≥ 1 g/j ; budésonide MMX 9 mg/j jusqu’à 8 semaines ; tofacitinib 10 mg 2×/j au moins 8 semaines puis 5 mg 2×/j, arrêt si pas de réponse à 16 semaines ; colectomie après échec médical dans jusqu’à 30 % des colites aiguës graves.</div>'
 + src(MED, CHIR, TW, FI('Pentasa®'), FI('Cortiment® MMX®'), FI('Xeljanz®')))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Place'], [
   ['Inflammation colique ?', w('k51-calpro', 'Calprotectine fécale') + ', CRP', 'Premier recours, suivi'],
   ['Infection ?', 'Coprocultures, C. difficile ; ' + w('k51-cmv', 'CMV') + ' sur biopsies si grave', 'Toute poussée'],
   ['Diagnostic, étendue ?', w('k51-colo', 'Coloscopie') + ' avec biopsies étagées', 'Bilan initial'],
   ['Colite grave ?', 'Rectosigmoïdoscopie prudente ; radiographie d’abdomen', 'Hospitalisation'],
   ['Avant biothérapie ?', 'Tuberculose latente, hépatites B et C', 'Systématique'],
   ['Cholangite associée ?', 'Phosphatases alcalines, cholangio-IRM si anomalie', 'Bilan et suivi']])
 + P('Le tableau se lit de haut en bas : ainsi, l’infection est écartée avant d’attribuer une poussée à la maladie elle-même.')
 + key('Calprotectine, C. difficile, coloscopie avec biopsies ; si grave : rectosigmoïdoscopie, CMV, radiographie ; bilan infectieux avant biothérapie.')
 + src(MED, CHIR))

C.e(2, 'Lire l’endoscopie et les biopsies', P(
 'À l’endoscopie, l’atteinte est continue, sans intervalle sain, et commence au rectum ; ainsi, on observe un érythème, une disparition de la trame vasculaire, une friabilité, puis des ulcérations. De plus, le sous-score endoscopique de Mayo gradue l’atteinte de 0 (normale) à 3 (saignement spontané, ulcérations). En histologie, la distorsion architecturale des cryptes, la plasmocytose basale et les abcès cryptiques signent la chronicité ; en revanche, l’absence de granulome aide à distinguer la rectocolite de la maladie de Crohn.')
 + key('Atteinte continue depuis le rectum ; Mayo endoscopique 0-3 ; distorsion des cryptes, plasmocytose basale, abcès cryptiques ; pas de granulome.')
 + C.pareto('pareto-k51-examens', 'Examens', ['k51-e-1', 'k51-e-2'],
     ['Calprotectine : inflammation et suivi.',
      'C. difficile à chaque poussée ; CMV si grave.',
      'Coloscopie : continuité depuis le rectum.',
      'Colite grave : rectosigmoïdoscopie, pas de coloscopie totale.'])
 + src(MED))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : rectum, sigmoïde et angle colique gauche', P(
 'Le côlon gauche, en aval de l’angle colique gauche, comprend le côlon descendant, le sigmoïde et le rectum ; ainsi, l’angle colique gauche sert de limite entre les étendues E2 et E3. Or, un lavement atteint en général le côlon gauche, alors qu’un suppositoire n’agit que sur le rectum. Par conséquent, la forme galénique de la mésalazine se choisit selon l’étendue.')
 + key('Suppositoire : rectum ; lavement : côlon gauche ; voie orale : tout le côlon.', 'Science → traitement.'))
C.s('histo', 'Histologie', 'Histologie : la muqueuse colique chronique', P(
 'La muqueuse colique normale est faite de cryptes droites et parallèles, riches en cellules caliciformes ; or, l’inflammation chronique les raccourcit, les ramifie et les raréfie. De plus, des plasmocytes s’accumulent à la base des cryptes et des polynucléaires y forment des abcès. Par conséquent, ces signes de chronicité distinguent la rectocolite d’une colite infectieuse aiguë, qui conserve l’architecture.')
 + key('Distorsion architecturale = chronicité ; architecture conservée = colite aiguë, souvent infectieuse.', 'Science → diagnostic.'))
C.s('immuno', 'Immunologie', 'Immunologie : cibles des traitements avancés', P(
 'Les anti-TNF neutralisent le TNF-α ; ainsi, ils réduisent l’inflammation systémique et muqueuse. Par ailleurs, le védolizumab bloque l’intégrine α4β7 et empêche les lymphocytes de migrer vers l’intestin, ce qui explique sa sélectivité intestinale. Enfin, le tofacitinib inhibe les Janus kinases, en particulier JAK-1 et JAK-3, et coupe la signalisation de nombreuses cytokines.')
 + key('Anti-TNF : action systémique ; védolizumab : sélectivité intestinale ; tofacitinib : inhibition de JAK par voie orale.', 'Science → traitement.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : galénique de la mésalazine', P(
 'La mésalazine agit localement sur la muqueuse colique ; or, absorbée trop tôt dans le grêle, elle n’atteindrait pas le côlon. C’est pourquoi les formes orales sont à libération retardée ou prolongée, et les formes rectales délivrent la molécule directement sur la muqueuse inflammatoire. De même, le budésonide MMX est libéré dans le côlon puis inactivé en grande partie au premier passage hépatique, ce qui limite ses effets systémiques.')
 + key('Libération colique et action topique : efficacité locale, moins d’effets systémiques.', 'Science → traitement.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, leur choix dépend de l’étendue, de la gravité et du moment, induction ou entretien.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['5-ASA', 'Mésalazine (Pentasa®, Asacol®)', 'Induction et entretien des formes légères à modérées', w('k51-d-mesalazine', 'Monographie')],
   ['Corticoïde à libération colique', 'Budésonide MMX (Cortiment® MMX®)', 'Induction si 5-ASA insuffisant', w('k51-d-budmmx', 'Fiche')],
   ['Corticoïdes systémiques', 'Prednisolone ; IV si colite grave', 'Induction seule', w('k51-cs', 'Fiche')],
   ['Thiopurines', 'Azathioprine', 'Entretien si corticodépendance', w('k51-thiopurines', 'Fiche')],
   ['Anti-TNF', 'Infliximab, adalimumab, golimumab', 'Induction et entretien ; sauvetage (infliximab)', w('k51-antitnf', 'Fiche')],
   ['Anti-intégrine', 'Védolizumab', 'Induction et entretien', w('k51-d-vedolizumab', 'Fiche')],
   ['Inhibiteur de JAK', 'Tofacitinib (Xeljanz®)', 'Induction et entretien', w('k51-d-tofacitinib', 'Monographie')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, à la différence de la maladie de Crohn, le 5-ASA est ici le traitement de fond de première ligne.')
 + key('5-ASA d’abord ; corticoïdes en induction seulement ; traitements avancés pour les formes modérées à sévères.')
 + src(MED))

C.p(2, 'Doses et statut réglementaire', P('Les éléments suivants proviennent de l’ECCO 2022 et des informations professionnelles suisses ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Schéma', 'Source'], [
   ['Mésalazine orale (Pentasa®)', 'Poussée : jusqu’à 4 g/j en 2 à 4 prises ; 4 g/j supérieur à 2 g/j ; ECCO : ≥ 2 g/j', 'FI Pentasa® ; ECCO 2022'],
   ['Mésalazine rectale (Pentasa®)', 'Lavement 1 g le soir 2 à 4 semaines ; suppositoire si proctite', 'FI Pentasa®'],
   ['Budésonide MMX (Cortiment® MMX®)', '9 mg le matin, jusqu’à 8 semaines, si 5-ASA insuffisant', 'FI Cortiment® MMX®'],
   ['Tofacitinib (Xeljanz®)', '10 mg 2×/j ≥ 8 semaines, puis 5 mg 2×/j ; arrêt si pas de réponse à 16 semaines', 'FI Xeljanz®'],
   ['Corticoïdes IV (colite grave)', 'TODO : dose non retrouvée dans les extraits lus', 'ECCO 2022 chirurgical']])
 + trap('La FI Pentasa® contre-indique la mésalazine en cas de trouble sévère de la fonction hépatique ou rénale, d’ulcère gastroduodénal et de tendance hémorragique marquée ; ces restrictions dépassent celles discutées par l’ECCO et doivent être vérifiées avant prescription.', 'Point à valider')
 + P('Par exemple, chez la patiente du début, la mésalazine est prescrite à 4 g/j par voie orale avec un lavement de 1 g le soir ; ensuite, après la rémission, la dose orale d’entretien est maintenue à au moins 2 g/j.')
 + key('Mésalazine ≤ 4 g/j orale + 1 g rectal ; budésonide MMX 9 mg/j ≤ 8 sem ; tofacitinib 10 mg 2×/j puis 5 mg 2×/j.')
 + src(MED, FI('Pentasa®'), FI('Cortiment® MMX®'), FI('Xeljanz®')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'La mésalazine peut, rarement, provoquer une néphrite interstitielle et des réactions cutanées graves ; c’est pourquoi la fonction rénale est surveillée. De plus, le tofacitinib expose aux thromboses veineuses et artérielles, aux infections dont le zona, et doit être utilisé à la dose efficace la plus faible.', 'Sécurité.')
 + P('Par ailleurs, les corticoïdes au long cours exposent à l’ostéoporose, au diabète et aux infections ; c’est pourquoi ils ne sont jamais un traitement d’entretien. En outre, les thiopurines exigent une formule sanguine régulière et une protection solaire. Enfin, la ciclosporine de sauvetage impose une surveillance de la pression artérielle, de la fonction rénale et des taux sanguins.')
 + key('Fonction rénale sous mésalazine ; thromboses et zona sous tofacitinib ; pas de corticoïdes au long cours ; formule sanguine sous thiopurines ; taux et rein sous ciclosporine.')
 + C.pareto('pareto-k51-pharma', 'Pharmacologie', ['k51-p-1', 'k51-p-2', 'k51-p-3'],
     ['5-ASA : traitement de fond de première ligne.',
      'Distale : traitement rectal indispensable.',
      'Corticoïdes : induction seule.',
      'Tofacitinib : 10 mg 2×/j puis 5 mg 2×/j ; risque thromboembolique.',
      'Mésalazine : surveiller la fonction rénale.'])
 + src(MED, FI('Pentasa®'), FI('Xeljanz®')))

# ---------------- Fenêtres
L = lab
C.pop('k51-tenesme', 'Épreintes et ténesme', L(('Épreintes', 'Douleurs coliques précédant l’évacuation.'), ('Ténesme', 'Sensation de tension rectale et besoin d’évacuer sans résultat.'), ('Valeur', 'Signes d’atteinte rectale.')))
C.pop('k51-montreal', 'Classification de Montréal (rectocolite)', L(('E1', 'Proctite : rectum seul.'), ('E2', 'Colite gauche : en aval de l’angle colique gauche.'), ('E3', 'Colite étendue : au-delà de l’angle colique gauche.')) + src(MTL, MED))
C.pop('k51-cagg', 'Colite aiguë grave', L(('Définition', 'Critères de Truelove et Witts réunis.'), ('Conduite', 'Hospitalisation, corticoïdes IV, équipe médico-chirurgicale.'), ('Pronostic', 'Jusqu’à 30 % de colectomies après échec du traitement conservateur.')) + src(CHIR, TW))
C.pop('k51-tw', 'Critères de Truelove et Witts', L(('Critère majeur', '≥ 6 selles sanglantes par jour.'), ('Et au moins un', 'Fréquence cardiaque > 90/min ; température > 37,8 °C ; hémoglobine < 10,5 g/dl ; vitesse de sédimentation > 30 mm/h.')) + src(TW))
C.pop('k51-mayo', 'Score de Mayo', L(('Items (0-3 chacun)', 'Fréquence des selles, rectorragies, aspect endoscopique, appréciation globale du médecin.'), ('Total', '0 à 12.'), ('Usage', 'Essais cliniques, suivi ; sous-score endoscopique 0-3.')))
C.pop('k51-csp', 'Cholangite sclérosante primitive', L(('Définition', 'Inflammation et fibrose des voies biliaires intra- et extrahépatiques.'), ('Lien', 'Associée surtout à la rectocolite ; augmente le risque de cancer colorectal et de cholangiocarcinome.')))
C.pop('k51-abces', 'Abcès cryptiques', L(('Aspect', 'Polynucléaires dans la lumière des cryptes.'), ('Valeur', 'Signe d’activité ; non spécifique isolément.')))
C.pop('k51-megacolon', 'Mégacôlon toxique', L(('Définition', 'Dilatation colique aiguë avec toxicité systémique au cours d’une colite grave.'), ('Risque', 'Perforation.'), ('Conduite', 'Urgence médico-chirurgicale ; colectomie si absence d’amélioration rapide.')) + src(CHIR))
C.pop('k51-mei', 'Manifestations extra-intestinales', L(('Exemples', 'Arthrites, érythème noueux, pyoderma gangrenosum, uvéite, épisclérite, cholangite sclérosante primitive.')) + src(MED))
C.pop('k51-cmv', 'Cytomégalovirus', L(('Contexte', 'Réactivation dans les colites graves ou réfractaires aux corticoïdes.'), ('Diagnostic', 'Biopsies coliques (histologie, immunohistochimie, PCR).')))
C.pop('k51-calpro', 'Calprotectine fécale', L(('Usage', 'Confirmer l’inflammation colique ; suivre la réponse.'), ('Limite', 'Élevée aussi dans les infections et sous AINS.')) + src(MED))
C.pop('k51-colo', 'Coloscopie avec biopsies', L(('Objectifs', 'Diagnostic, étendue, gravité endoscopique (Mayo 0-3), biopsies étagées.'), ('Colite grave', 'Rectosigmoïdoscopie prudente plutôt que coloscopie totale.')) + src(MED))
C.pop('k51-surveillance', 'Coloscopie de surveillance', L(('But', 'Dépister la dysplasie et le cancer colorectal.'), ('Facteurs', 'Durée, étendue, inflammation, cholangite sclérosante primitive.'), ('Délai et rythme', 'TODO : recommandation ECCO de surveillance non lue.')))
C.pop('k51-colectomie', 'Coloproctectomie', L(('Indications', 'Colite grave réfractaire, maladie réfractaire, dysplasie non résécable, cancer.'), ('Reconstruction', 'Anastomose iléo-anale avec réservoir ou iléostomie.')) + src(CHIR))
C.pop('k51-cs', 'Corticoïdes systémiques', L(('Ambulatoire', 'Prednisolone orale : induction des formes modérées à sévères (recommandation forte).'), ('Colite grave', 'Voie intraveineuse en première ligne.'), ('Jamais', 'En entretien.')) + src(MED, CHIR))
C.pop('k51-thiopurines', 'Thiopurines', L(('Place', 'Entretien chez le patient corticodépendant ou intolérant au 5-ASA (recommandation forte) ; pas d’induction.'), ('Surveillance', 'Formule sanguine ; TPMT ou NUDT15 avant.')) + src(MED))
C.pop('k51-antitnf', 'Anti-TNF', L(('Molécules', 'Infliximab, adalimumab, golimumab.'), ('Place', 'Induction et entretien (recommandations fortes) ; infliximab en sauvetage de la colite grave.')) + src(MED, CHIR))
C.pop('k51-d-mesalazine', 'Mésalazine (5-ASA)', L(('Indication suisse (Pentasa®)', 'Poussées et prévention des récidives de rectocolite, proctosigmoïdite, proctite.'), ('Doses', 'Orale jusqu’à 4 g/j ; lavement 1 g le soir 2-4 semaines ; ECCO : ≥ 2 g/j oral, ≥ 1 g/j rectal.'), ('Contre-indications', 'Insuffisance hépatique ou rénale sévère, ulcère gastroduodénal, tendance hémorragique.')) + src(FI('Pentasa®'), MED))
C.pop('k51-d-budmmx', 'Budésonide MMX (Cortiment® MMX®)', L(('Indication suisse', 'Induction de la rémission d’une colite légère à modérée si le 5-ASA est insuffisant.'), ('Dose', '9 mg le matin, jusqu’à 8 semaines ; réduction progressive à l’arrêt.')) + src(FI('Cortiment® MMX®'), MED))
C.pop('k51-d-vedolizumab', 'Védolizumab', L(('Cible', 'Intégrine α4β7.'), ('Place', 'Induction et entretien (recommandations fortes) ; suggéré plutôt que l’adalimumab.')) + src(MED))
C.pop('k51-d-tofacitinib', 'Tofacitinib (Xeljanz®)', L(('Indication suisse', 'Colite ulcéreuse active modérée à sévère après échec des corticoïdes, de l’azathioprine, de la 6-mercaptopurine ou d’un anti-TNF.'), ('Dose', '10 mg 2×/j ≥ 8 semaines, puis 5 mg 2×/j ; arrêt si pas de réponse à 16 semaines.'), ('Risque', 'Embolies pulmonaires et thromboses accrues par rapport aux anti-TNF.')) + src(FI('Xeljanz®'), MED))
C.pop('k51-d-infliximab', 'Infliximab de sauvetage', L(('Indication', 'Colite aiguë grave réfractaire aux corticoïdes IV (ECCO 2022, énoncé 1.2).'), ('Schéma', 'Régime optimal non établi (énoncé 1.3).')) + src(CHIR))
C.pop('k51-d-ciclosporine', 'Ciclosporine de sauvetage', L(('Indication', 'Alternative à l’infliximab dans la colite aiguë grave réfractaire aux corticoïdes.'), ('Condition', 'Prévoir un traitement d’entretien ; expérience du centre.'), ('Surveillance', 'Pression artérielle, fonction rénale, taux sanguins.')) + src(CHIR))

C.termes = [
 (r'mésalazine', 'k51-d-mesalazine'), (r'5-ASA', 'k51-d-mesalazine'), (r'budésonide MMX', 'k51-d-budmmx'), (r'tofacitinib', 'k51-d-tofacitinib'),
 (r'védolizumab', 'k51-d-vedolizumab'), (r'anti-TNF', 'k51-antitnf'), (r'thiopurines?', 'k51-thiopurines'), (r'prednisolone', 'k51-cs'),
 (r'ciclosporine', 'k51-d-ciclosporine'), (r'infliximab', 'k51-d-infliximab'), (r'Truelove et Witts', 'k51-tw'), (r'colite aiguë grave', 'k51-cagg'),
 (r'Montréal', 'k51-montreal'), (r'score de Mayo|Mayo', 'k51-mayo'), (r'cholangite sclérosante primitive', 'k51-csp'), (r'abcès cryptiques', 'k51-abces'),
 (r'mégacôlon toxique', 'k51-megacolon'), (r'cytomégalovirus|CMV', 'k51-cmv'), (r'calprotectine', 'k51-calpro'), (r'coloscopie', 'k51-colo'),
 (r'coloproctectomie|colectomie', 'k51-colectomie'), (r'ténesme', 'k51-tenesme'), (r'manifestations extra-intestinales', 'k51-mei'),
]

C.write()
