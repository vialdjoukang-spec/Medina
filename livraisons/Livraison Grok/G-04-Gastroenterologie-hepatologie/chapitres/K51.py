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
 + key('La maladie touche l’adulte jeune, et le tabac y est paradoxalement « protecteur ». Elle s’associe à la cholangite sclérosante primitive, et son risque de cancer colorectal dépend de la durée, de l’étendue et de l’inflammation.')
 + src(MED))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre la clinique, il faut partir de la muqueuse. D’abord, la barrière épithéliale colique et sa couche de mucus sont altérées ; ainsi, le microbiote stimule de façon excessive l’immunité muqueuse. Ensuite, des lymphocytes T et des polynucléaires infiltrent la muqueuse, envahissent les cryptes et forment des ' + w('k51-abces', 'abcès cryptiques') + ', puis des ulcérations.',
 'Par conséquent, la muqueuse saigne et sécrète du mucus, et le rectum enflammé provoque le ténesme et les besoins impérieux. Toutefois, comme l’inflammation reste superficielle, les fistules sont rares ; en revanche, une poussée grave peut paralyser la musculeuse et dilater le côlon, ce qui définit le ' + w('k51-megacolon', 'mégacôlon toxique') + '.')
 + key('La barrière muqueuse altérée laisse s’installer une inflammation muqueuse continue, qui forme des abcès cryptiques et des ulcérations ; il en résulte un saignement, des glaires et un ténesme, et la forme grave peut aboutir au mégacôlon toxique.')
 + src(MED, CHIR))

C.a(4, 'Présentation clinique', P(
 'La présentation reflète donc l’étendue et la gravité. Ainsi, la proctite donne des rectorragies, des glaires, des épreintes et un ténesme, parfois avec une constipation paradoxale ; à l’inverse, la colite étendue provoque une diarrhée sanglante fréquente, des douleurs abdominales et, dans les formes graves, de la fièvre, une tachycardie et une anémie.',
 'De plus, l’examen recherche des ' + w('k51-mei', 'manifestations extra-intestinales') + ' articulaires, cutanées, oculaires ou hépatobiliaires. Par ailleurs, devant toute poussée, il faut éliminer une infection, en particulier par Clostridioides difficile, et, dans une forme grave ou réfractaire, une infection à ' + w('k51-cmv', 'cytomégalovirus') + '.')
 + C.img('k51_endoscopie.gif', 'Photographie endoscopique d’une muqueuse colique rouge, granitée, friable, sans relief vasculaire, couverte par endroits de fibrine.', 'Rectocolite hémorragique, vue endoscopique : muqueuse érythémateuse et granitée, disparition de la trame vasculaire, friabilité et ulcérations superficielles, de façon continue.', credit({'auteur': 'Sebb (Wikipédia en anglais), auteur présumé', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Ulcerative_colitis.jpg'}))
 + key('La proctite donne des rectorragies, des glaires et un ténesme, et la colite étendue une diarrhée sanglante. La forme grave ajoute une fièvre, une tachycardie et une anémie. On exclut toujours C. difficile, et l’on recherche le CMV si la forme est grave ou réfractaire.')
 + src(MED))

C.a(5, 'Démarche diagnostique', P(
 'Devant ce tableau, le diagnostic associe arguments cliniques, biologiques, endoscopiques et histologiques. D’abord, la biologie évalue l’inflammation (CRP), l’anémie et l’albumine, et la ' + w('k51-calpro', 'calprotectine fécale') + ' confirme l’inflammation colique. De plus, les coprocultures et la recherche de Clostridioides difficile écartent une colite infectieuse.',
 'Ensuite, la ' + w('k51-colo', 'coloscopie') + ' avec iléoscopie montre une atteinte continue depuis le rectum et en fixe l’étendue ; en outre, des biopsies étagées documentent une inflammation chronique, avec distorsion architecturale des cryptes. Cependant, en cas de colite grave, une rectosigmoïdoscopie prudente, sans préparation complète, suffit, car la coloscopie totale expose à la perforation.')
 + C.img('k51_histo.gif', 'Coupe histologique de muqueuse colique ulcérée : les cryptes normales ont disparu, remplacées par un tissu de granulation riche en cellules inflammatoires.', 'Rectocolite hémorragique sévère, coloration hématoxyline-éosine : ulcération avec perte de l’architecture cryptique, tissu de granulation et infiltrat inflammatoire dense riche en polynucléaires.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_severe_ulcerative_colitis.jpg'}))
 + quiz('Poussée grave de colite chez une patiente fébrile. Quel examen endoscopique en premier ?',
   [('Coloscopie totale après préparation complète', False), ('Rectosigmoïdoscopie prudente avec biopsies', True), ('Capsule endoscopique', False)],
   'Dans une colite grave, une rectosigmoïdoscopie avec peu d’insufflation suffit au diagnostic, aux biopsies (dont la recherche de CMV) et limite le risque de perforation.')
 + key('On dose la CRP, l’hémoglobine, l’albumine et la calprotectine, on fait des coprocultures et une recherche de C. difficile, puis une coloscopie avec biopsies étagées. Dans la colite grave, on se limite à une rectosigmoïdoscopie prudente, car la coloscopie totale risque la perforation.')
 + src(MED))

C.a(6, 'Évaluer la gravité', P(
 'Le diagnostic posé, la gravité oriente le traitement et le lieu de soins. Ainsi, l’ECCO distingue les poussées légères à modérées et les poussées modérées à sévères, en reconnaissant que ces catégories forment un continuum. Par ailleurs, le ' + w('k51-mayo', 'score de Mayo') + ' associe fréquence des selles, rectorragies, aspect endoscopique et appréciation globale ; il sert surtout dans les essais et le suivi.',
 'En pratique, il faut surtout reconnaître la ' + w('k51-cagg', 'colite aiguë grave') + ', qui impose une hospitalisation. En effet, selon les ' + w('k51-tw', 'critères de Truelove et Witts') + ', au moins six selles sanglantes par jour associées à au moins un signe systémique (fréquence cardiaque > 90/min, température > 37,8 °C, hémoglobine < 10,5 g/dl ou vitesse de sédimentation > 30 mm/h) définissent une poussée grave.')
 + quiz('Huit selles sanglantes par jour, pouls à 104/min, hémoglobine 11,8 g/dl. Gravité ?',
   [('Poussée modérée : traitement ambulatoire', False), ('Colite aiguë grave : hospitalisation et corticoïdes IV', True), ('Proctite', False)],
   'Six selles sanglantes ou plus et au moins un critère systémique (ici la tachycardie > 90/min) définissent la colite aiguë grave selon Truelove et Witts.')
 + key('Selon Truelove et Witts, ≥ 6 selles sanglantes par jour avec ≥ 1 critère (FC > 90, T > 37,8 °C, Hb < 10,5 g/dl, VS > 30 mm/h) définissent la colite aiguë grave, qui impose l’hospitalisation.')
 + src(TW, MED, CHIR))

C.a(7, 'Traiter une poussée légère à modérée', P(
 'Dans une poussée légère à modérée, la ' + w('k51-d-mesalazine', 'mésalazine') + ' est le traitement de base. Ainsi, l’ECCO recommande le 5-ASA oral à au moins 2 g/j pour induire la rémission (recommandation forte) ; de même, dans une colite distale, la mésalazine rectale à au moins 1 g/j est recommandée (recommandation forte). De plus, pour une atteinte au moins rectosigmoïdienne, l’association orale et rectale est préférée à la voie orale seule (recommandation faible).',
 'Par ailleurs, les corticoïdes rectaux sont efficaces dans la colite distale, mais la mésalazine rectale leur est préférée (recommandation faible). En cas de réponse insuffisante au 5-ASA, un ' + w('k51-d-budmmx', 'corticoïde à libération colique') + ', comme le budésonide MMX, peut induire la rémission (recommandation faible) ; en revanche, les thiopurines ne doivent pas servir à l’induction (recommandation faible contre).')
 + trap('Une proctite « résistante » à la mésalazine orale est souvent une proctite mal traitée : le traitement rectal est indispensable, car la mésalazine orale atteint mal le rectum.', 'Piège')
 + key('On donne le 5-ASA oral à ≥ 2 g/j, et par voie rectale à ≥ 1 g/j si la colite est distale ; on associe les deux voies si l’atteinte atteint au moins le rectosigmoïde. En cas d’échec du 5-ASA, on ajoute du budésonide MMX, et l’on ne donne pas de thiopurine en induction.')
 + src(MED, FI('Pentasa®'), FI('Cortiment® MMX®')))

C.a(8, 'Traiter une poussée modérée à sévère', P(
 'Dans une poussée modérée à sévère sans critère de gravité aiguë, la ' + w('k51-cs', 'prednisolone orale') + ' est recommandée chez le patient non hospitalisé (recommandation forte). Cependant, les corticoïdes n’entretiennent pas la rémission ; c’est pourquoi un traitement d’entretien est discuté dès ce moment. Ainsi, l’ECCO recommande, en induction comme en entretien, les ' + w('k51-antitnf', 'anti-TNF') + ' (infliximab, adalimumab, golimumab), le ' + w('k51-d-vedolizumab', 'védolizumab') + ', l’ustékinumab et le ' + w('k51-d-tofacitinib', 'tofacitinib') + ' (recommandations fortes).',
 'De plus, le védolizumab est suggéré plutôt que l’adalimumab (recommandation faible), sur la base d’un essai comparatif direct. Par ailleurs, en entretien, les ' + w('k51-thiopurines', 'thiopurines') + ' sont recommandées en monothérapie chez le patient corticodépendant ou intolérant au 5-ASA (recommandation forte). Enfin, le choix tient compte des comorbidités, de la voie d’administration et des risques propres à chaque molécule, notamment thromboemboliques pour le tofacitinib.')
 + alert('Avant tout immunosuppresseur ou biothérapie, on dépiste la tuberculose latente et les hépatites virales et l’on vérifie les vaccinations. Le tofacitinib augmente les embolies pulmonaires et les thromboses veineuses et artérielles par rapport aux anti-TNF (FI Xeljanz®) ; c’est pourquoi on l’évite chez le patient à risque thromboembolique.', 'Sécurité d’abord.')
 + key('La prednisolone orale sert à l’induction ; les anti-TNF, le védolizumab, l’ustékinumab et le tofacitinib servent à l’induction et à l’entretien, et les thiopurines à l’entretien en cas de corticodépendance.')
 + src(MED, FI('Xeljanz®')))

C.a(9, 'Colite aiguë grave', P(
 'Quand les critères de Truelove et Witts sont réunis, la situation devient urgente. Ainsi, le patient est hospitalisé et reçoit des corticoïdes intraveineux en première ligne, qui induisent la rémission et réduisent la mortalité (ECCO 2022, énoncé 1.1). De plus, il faut éliminer C. difficile et le cytomégalovirus, corriger les troubles hydroélectrolytiques et l’anémie, prévenir la maladie thromboembolique et faire suivre le patient conjointement par le gastroentérologue et le chirurgien.',
 'Cependant, jusqu’à 30 % des patients ne répondent pas et nécessitent une colectomie. C’est pourquoi la réponse est réévaluée après quelques jours de corticoïdes ; en cas d’échec, l’' + w('k51-d-infliximab', 'infliximab') + ' ou la ' + w('k51-d-ciclosporine', 'ciclosporine') + ' sont utilisés en traitement de sauvetage, selon l’expérience du centre et le traitement d’entretien envisagé (énoncé 1.2). En revanche, un sauvetage de troisième ligne par anticalcineurine retarde la colectomie au prix d’effets indésirables fréquents, et reste réservé aux centres spécialisés (énoncé 1.4).')
 + C.img('k51_megacolon.gif', 'Radiographie abdominale de face : côlon transverse très dilaté, rempli de gaz, avec perte des haustrations.', 'Mégacôlon toxique compliquant une rectocolite hémorragique : dilatation majeure du côlon transverse sur la radiographie d’abdomen. La patiente a été colectomisée.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Toxic_Megacolon_in_Ulcerative_Colitis.jpg'}))
 + trap('La dose de corticoïdes intraveineux et le jour exact de l’évaluation de la réponse ne figurent pas dans les extraits lus de l’ECCO 2022 ; ils ne sont donc pas chiffrés ici. TODO : compléter à partir du texte intégral de l’ECCO chirurgical 2022.', 'Lacune documentaire')
 + key('La colite aiguë grave impose l’hospitalisation, des corticoïdes IV, l’exclusion de C. difficile et du CMV, une thromboprophylaxie et une équipe médico-chirurgicale. En cas d’échec, on donne de l’infliximab ou de la ciclosporine, et sinon on fait une colectomie.')
 + src(CHIR))

C.a(10, 'Entretien, surveillance et chirurgie', P(
 'Une fois la rémission obtenue, il faut la maintenir. Ainsi, la mésalazine orale à au moins 2 g/j est recommandée en entretien (recommandation forte), et la mésalazine rectale est suggérée dans les formes distales (recommandation faible). De plus, un traitement avancé qui a induit la rémission est poursuivi en entretien : anti-TNF, védolizumab, ustékinumab ou tofacitinib.',
 'Par ailleurs, la rectocolite expose au cancer colorectal ; c’est pourquoi une ' + w('k51-surveillance', 'coloscopie de surveillance') + ' est organisée après plusieurs années d’évolution, plus tôt et plus souvent en cas de cholangite sclérosante primitive. Enfin, la ' + w('k51-colectomie', 'coloproctectomie') + ' est indiquée en cas de colite grave réfractaire, de dysplasie non résécable ou de cancer ; en effet, elle guérit la maladie colique, au prix d’une anastomose iléo-anale avec réservoir ou d’une iléostomie.')
 + trap('Le délai de début et le rythme exacts de la coloscopie de surveillance ne figurent pas dans les recommandations lues ; TODO : recommandation ECCO de surveillance à intégrer.', 'Lacune documentaire')
 + key('L’entretien repose sur le 5-ASA ≥ 2 g/j ou sur le traitement avancé qui a induit la rémission, avec une surveillance du cancer colorectal. On fait une colectomie si la maladie est réfractaire ou en cas de dysplasie ou de cancer.')
 + C.pareto('pareto-k51-clinique', 'Rectocolite hémorragique', ['k51-1', 'k51-5', 'k51-6', 'k51-7', 'k51-8', 'k51-9', 'k51-10'],
     ['Inflammation muqueuse continue depuis le rectum.',
      'On exclut C. difficile, puis on fait une coloscopie avec biopsies.',
      'Truelove et Witts : ≥ 6 selles sanglantes + 1 critère systémique.',
      'La forme légère à modérée reçoit de la mésalazine orale ≥ 2 g/j, éventuellement avec la voie rectale ≥ 1 g/j.',
      'La forme modérée à sévère reçoit de la prednisolone, puis une biothérapie ou du tofacitinib.',
      'La colite aiguë grave reçoit des corticoïdes IV, puis de l’infliximab ou de la ciclosporine en sauvetage.',
      'Entretien : 5-ASA ≥ 2 g/j ; surveillance du cancer.'])
 + src(MED, CHIR))

C.a(11, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. La coloscopie montre une atteinte continue du rectum jusqu’au côlon sigmoïde, et les biopsies confirment une inflammation chronique ; de plus, il n’y a ni fièvre, ni tachycardie, ni anémie. Il s’agit donc d’une rectocolite hémorragique E2, en poussée modérée sans gravité aiguë.',
 'Dès lors, le traitement associe la mésalazine orale et la mésalazine rectale. Ensuite, la réponse est jugée sur les symptômes puis sur la calprotectine. Enfin, en cas d’échec, un budésonide MMX ou une prednisolone orale seraient discutés, puis un traitement avancé si la maladie devient corticodépendante.')
 + key('L’étendue (E2) et la gravité (aucun critère de Truelove) conduisent à la mésalazine orale et rectale ; ensuite, on contrôle la réponse et l’on escalade en cas d’échec.')
 + src(MED))

C.a(12, 'Critères formels et paramètres clés', alert(
 '<p><b>Étendue (Montréal).</b> E1 proctite ; E2 colite gauche, en aval de l’angle colique gauche ; E3 colite étendue. <b>Colite aiguë grave (Truelove et Witts).</b> ≥ 6 selles sanglantes par jour et au moins un critère : fréquence cardiaque > 90/min, température > 37,8 °C, hémoglobine < 10,5 g/dl, vitesse de sédimentation > 30 mm/h.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> La mésalazine orale se donne à ≥ 2 g/j (au plus 4 g/j, FI Pentasa®) et la rectale à ≥ 1 g/j. Le budésonide MMX se donne à 9 mg/j jusqu’à 8 semaines. Le tofacitinib se donne à 10 mg 2×/j pendant au moins 8 semaines, puis à 5 mg 2×/j, et s’arrête sans réponse à 16 semaines. Jusqu’à 30 % des colites aiguës graves finissent par une colectomie après l’échec médical.</div>'
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
 + key('On dose la calprotectine, on recherche C. difficile et l’on fait une coloscopie avec biopsies. Si la forme est grave, on fait une rectosigmoïdoscopie, une recherche de CMV et une radiographie, et avant une biothérapie un bilan infectieux.')
 + src(MED, CHIR))

C.e(2, 'Lire l’endoscopie et les biopsies', P(
 'À l’endoscopie, l’atteinte est continue, sans intervalle sain, et commence au rectum ; ainsi, on observe un érythème, une disparition de la trame vasculaire, une friabilité, puis des ulcérations. De plus, le sous-score endoscopique de Mayo gradue l’atteinte de 0 (normale) à 3 (saignement spontané, ulcérations). En histologie, la distorsion architecturale des cryptes, la plasmocytose basale et les abcès cryptiques signent la chronicité ; en revanche, l’absence de granulome aide à distinguer la rectocolite de la maladie de Crohn.')
 + key('L’atteinte est continue depuis le rectum et se gradue de 0 à 3 selon le Mayo endoscopique. L’histologie montre une distorsion des cryptes, une plasmocytose basale et des abcès cryptiques, mais pas de granulome.')
 + C.pareto('pareto-k51-examens', 'Examens', ['k51-e-1', 'k51-e-2'],
     ['Calprotectine : inflammation et suivi.',
      'On recherche C. difficile à chaque poussée et le CMV si la forme est grave.',
      'La coloscopie montre une atteinte continue depuis le rectum.',
      'Dans la colite grave, on fait une rectosigmoïdoscopie, mais pas de coloscopie totale.'])
 + src(MED))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : rectum, sigmoïde et angle colique gauche', P(
 'Le côlon gauche, en aval de l’angle colique gauche, comprend le côlon descendant, le sigmoïde et le rectum ; ainsi, l’angle colique gauche sert de limite entre les étendues E2 et E3. Or, un lavement atteint en général le côlon gauche, alors qu’un suppositoire n’agit que sur le rectum. Par conséquent, la forme galénique de la mésalazine se choisit selon l’étendue.')
 + key('Le suppositoire atteint le rectum, le lavement le côlon gauche, et la voie orale tout le côlon ; c’est pourquoi la forme galénique suit l’étendue.', 'Science → traitement.'))
C.s('histo', 'Histologie', 'Histologie : la muqueuse colique chronique', P(
 'La muqueuse colique normale est faite de cryptes droites et parallèles, riches en cellules caliciformes ; or, l’inflammation chronique les raccourcit, les ramifie et les raréfie. De plus, des plasmocytes s’accumulent à la base des cryptes et des polynucléaires y forment des abcès. Par conséquent, ces signes de chronicité distinguent la rectocolite d’une colite infectieuse aiguë, qui conserve l’architecture.')
 + key('Distorsion architecturale = chronicité ; architecture conservée = colite aiguë, souvent infectieuse.', 'Science → diagnostic.'))
C.s('immuno', 'Immunologie', 'Immunologie : cibles des traitements avancés', P(
 'Les anti-TNF neutralisent le TNF-α ; ainsi, ils réduisent l’inflammation systémique et muqueuse. Par ailleurs, le védolizumab bloque l’intégrine α4β7 et empêche les lymphocytes de migrer vers l’intestin, ce qui explique sa sélectivité intestinale. Enfin, le tofacitinib inhibe les Janus kinases, en particulier JAK-1 et JAK-3, et coupe la signalisation de nombreuses cytokines.')
 + key('Les anti-TNF agissent de façon systémique, le védolizumab de façon sélective sur l’intestin, et le tofacitinib inhibe les JAK par voie orale.', 'Science → traitement.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : galénique de la mésalazine', P(
 'La mésalazine agit localement sur la muqueuse colique ; or, absorbée trop tôt dans le grêle, elle n’atteindrait pas le côlon. C’est pourquoi les formes orales sont à libération retardée ou prolongée, et les formes rectales délivrent la molécule directement sur la muqueuse inflammatoire. De même, le budésonide MMX est libéré dans le côlon puis inactivé en grande partie au premier passage hépatique, ce qui limite ses effets systémiques.')
 + key('La libération colique et l’action topique donnent une efficacité locale avec moins d’effets systémiques.', 'Science → traitement.'))

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
 + key('Le 5-ASA vient d’abord, les corticoïdes ne servent qu’à l’induction, et les traitements avancés traitent les formes modérées à sévères.')
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
 + key('La mésalazine se donne jusqu’à 4 g/j par voie orale avec 1 g par voie rectale ; le budésonide MMX à 9 mg/j pendant 8 semaines au plus ; le tofacitinib à 10 mg 2×/j, puis 5 mg 2×/j.')
 + src(MED, FI('Pentasa®'), FI('Cortiment® MMX®'), FI('Xeljanz®')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'La mésalazine peut, rarement, provoquer une néphrite interstitielle et des réactions cutanées graves ; c’est pourquoi la fonction rénale est surveillée. De plus, le tofacitinib expose aux thromboses veineuses et artérielles, aux infections dont le zona, et doit être utilisé à la dose efficace la plus faible.', 'Sécurité.')
 + P('Par ailleurs, les corticoïdes au long cours exposent à l’ostéoporose, au diabète et aux infections ; c’est pourquoi ils ne sont jamais un traitement d’entretien. En outre, les thiopurines exigent une formule sanguine régulière et une protection solaire. Enfin, la ciclosporine de sauvetage impose une surveillance de la pression artérielle, de la fonction rénale et des taux sanguins.')
 + key('Sous mésalazine, on surveille la fonction rénale, et sous tofacitinib les thromboses et le zona. On ne donne pas de corticoïdes au long cours. Sous thiopurines, on contrôle la formule sanguine, et sous ciclosporine les taux et le rein.')
 + C.pareto('pareto-k51-pharma', 'Pharmacologie', ['k51-p-1', 'k51-p-2', 'k51-p-3'],
     ['5-ASA : traitement de fond de première ligne.',
      'La forme distale exige un traitement rectal.',
      'Les corticoïdes ne servent qu’à l’induction.',
      'Le tofacitinib se donne à 10 mg 2×/j, puis à 5 mg 2×/j, et expose au risque thromboembolique.',
      'Mésalazine : surveiller la fonction rénale.'])
 + src(MED, FI('Pentasa®'), FI('Xeljanz®')))

# ---------------- Fenêtres
L = lab
C.pop('k51-tenesme', 'Épreintes et ténesme', L(('Épreintes', 'Douleurs coliques précédant l’évacuation.'), ('Ténesme', 'Sensation de tension rectale et besoin d’évacuer sans résultat.'), ('Valeur', 'Ils signent une atteinte rectale, car le rectum inflammatoire déclenche de faux besoins.')))
C.pop('k51-montreal', 'Classification de Montréal (rectocolite)', L(('E1', 'E1 désigne la proctite, limitée au rectum.'), ('E2', 'Colite gauche : en aval de l’angle colique gauche.'), ('E3', 'Colite étendue : au-delà de l’angle colique gauche.')) + src(MTL, MED))
C.pop('k51-cagg', 'Colite aiguë grave', L(('Définition', 'Elle se définit par les critères de Truelove et Witts réunis.'), ('Conduite', 'On hospitalise le patient, on donne des corticoïdes IV et l’on réunit une équipe médico-chirurgicale, car une colectomie peut devenir urgente.'), ('Pronostic', 'Jusqu’à 30 % des patients sont colectomisés après l’échec du traitement conservateur.')) + src(CHIR, TW))
C.pop('k51-tw', 'Critères de Truelove et Witts', L(('Critère majeur', '≥ 6 selles sanglantes par jour.'), ('Et au moins un', 'Il faut en plus au moins un critère systémique : fréquence cardiaque > 90/min, température > 37,8 °C, hémoglobine < 10,5 g/dl ou vitesse de sédimentation > 30 mm/h.')) + src(TW))
C.pop('k51-mayo', 'Score de Mayo', L(('Items (0-3 chacun)', 'Le score note de 0 à 3 la fréquence des selles, les rectorragies, l’aspect endoscopique et l’appréciation globale du médecin.'), ('Total', '0 à 12.'), ('Usage', 'Il sert aux essais cliniques et au suivi, et son sous-score endoscopique va de 0 à 3.')) + C.img('k51_endoscopie.gif', 'Endoscopie : muqueuse colique rouge, granitée, friable, sans trame vasculaire.', 'La trame vasculaire disparaît et la muqueuse saigne au contact, car l’inflammation est continue et superficielle ; cet aspect correspond à un sous-score de Mayo élevé.', credit({'auteur': 'Sebb (Wikipédia en anglais), auteur présumé', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Ulcerative_colitis.jpg'})))
C.pop('k51-csp', 'Cholangite sclérosante primitive', L(('Définition', 'C’est une inflammation fibrosante des voies biliaires intra- et extrahépatiques.'), ('Lien', 'Associée surtout à la rectocolite ; augmente le risque de cancer colorectal et de cholangiocarcinome.')))
C.pop('k51-abces', 'Abcès cryptiques', L(('Aspect', 'Des polynucléaires remplissent la lumière des cryptes.'), ('Valeur', 'Ils signent l’activité, mais ne sont pas spécifiques isolément.')) + C.img('k51_histo.gif', 'Histologie : muqueuse colique ulcérée avec disparition des cryptes et tissu de granulation.', 'Les cryptes ont disparu sous l’ulcération, et l’infiltrat inflammatoire remplit la muqueuse ; ces lésions restent limitées à la muqueuse, à la différence de la maladie de Crohn.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_severe_ulcerative_colitis.jpg'})))
C.pop('k51-megacolon', 'Mégacôlon toxique', L(('Définition', 'C’est une dilatation colique aiguë avec toxicité systémique au cours d’une colite grave.'), ('Risque', 'Perforation.'), ('Conduite', 'C’est une urgence médico-chirurgicale, et l’on fait une colectomie si l’état ne s’améliore pas rapidement, car la perforation menace.')) + src(CHIR) + C.img('k51_megacolon.gif', 'Radiographie abdominale : côlon transverse très dilaté sans haustrations.', 'Le transverse, situé le plus haut chez le patient couché, se remplit de gaz et perd ses haustrations ; un diamètre aussi grand annonce le risque de perforation.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Toxic_Megacolon_in_Ulcerative_Colitis.jpg'})))
C.pop('k51-mei', 'Manifestations extra-intestinales', L(('Exemples', 'Les arthrites, l’érythème noueux, le pyoderma gangrenosum, l’uvéite, l’épisclérite et la cholangite sclérosante primitive en sont des exemples.')) + src(MED))
C.pop('k51-cmv', 'Cytomégalovirus', L(('Contexte', 'Il se réactive dans les colites graves ou réfractaires aux corticoïdes, car l’inflammation et l’immunosuppression favorisent sa réplication.'), ('Diagnostic', 'Biopsies coliques (histologie, immunohistochimie, PCR).')))
C.pop('k51-calpro', 'Calprotectine fécale', L(('Usage', 'Confirmer l’inflammation colique ; suivre la réponse.'), ('Limite', 'Elle s’élève aussi dans les infections et sous AINS.')) + src(MED))
C.pop('k51-colo', 'Coloscopie avec biopsies', L(('Objectifs', 'Diagnostic, étendue, gravité endoscopique (Mayo 0-3), biopsies étagées.'), ('Colite grave', 'Rectosigmoïdoscopie prudente plutôt que coloscopie totale.')) + src(MED))
C.pop('k51-surveillance', 'Coloscopie de surveillance', L(('But', 'Dépister la dysplasie et le cancer colorectal.'), ('Facteurs', 'Durée, étendue, inflammation, cholangite sclérosante primitive.'), ('Délai et rythme', 'TODO : recommandation ECCO de surveillance non lue.')))
C.pop('k51-colectomie', 'Coloproctectomie', L(('Indications', 'Colite grave réfractaire, maladie réfractaire, dysplasie non résécable, cancer.'), ('Reconstruction', 'Anastomose iléo-anale avec réservoir ou iléostomie.')) + src(CHIR))
C.pop('k51-cs', 'Corticoïdes systémiques', L(('Ambulatoire', 'La prednisolone orale induit la rémission des formes modérées à sévères (recommandation forte).'), ('Colite grave', 'La voie intraveineuse est la première ligne.'), ('Jamais', 'En entretien.')) + src(MED, CHIR))
C.pop('k51-thiopurines', 'Thiopurines', L(('Place', 'Elles servent à l’entretien chez le patient corticodépendant ou intolérant au 5-ASA (recommandation forte), mais pas à l’induction, car elles agissent lentement.'), ('Surveillance', 'On contrôle la formule sanguine et l’on teste la TPMT ou NUDT15 avant de les prescrire.')) + src(MED))
C.pop('k51-antitnf', 'Anti-TNF', L(('Molécules', 'Infliximab, adalimumab, golimumab.'), ('Place', 'Ils servent à l’induction et à l’entretien (recommandations fortes), et l’infliximab sert de sauvetage dans la colite grave.')) + src(MED, CHIR))
C.pop('k51-d-mesalazine', 'Mésalazine (5-ASA)', L(('Indication suisse (Pentasa®)', 'Pentasa® est autorisé pour les poussées et la prévention des récidives de rectocolite, de proctosigmoïdite et de proctite.'), ('Doses', 'La voie orale va jusqu’à 4 g/j, et le lavement se donne à 1 g le soir pendant 2 à 4 semaines ; l’ECCO recommande ≥ 2 g/j par voie orale et ≥ 1 g/j par voie rectale.'), ('Contre-indications', 'Elle est contre-indiquée en cas d’insuffisance hépatique ou rénale sévère, d’ulcère gastroduodénal et de tendance hémorragique.')) + src(FI('Pentasa®'), MED))
C.pop('k51-d-budmmx', 'Budésonide MMX (Cortiment® MMX®)', L(('Indication suisse', 'Induction de la rémission d’une colite légère à modérée si le 5-ASA est insuffisant.'), ('Dose', 'On donne 9 mg le matin jusqu’à 8 semaines, puis l’on réduit progressivement à l’arrêt.')) + src(FI('Cortiment® MMX®'), MED))
C.pop('k51-d-vedolizumab', 'Védolizumab', L(('Cible', 'Intégrine α4β7.'), ('Place', 'Il sert à l’induction et à l’entretien (recommandations fortes), et l’ECCO le suggère plutôt que l’adalimumab.')) + src(MED))
C.pop('k51-d-tofacitinib', 'Tofacitinib (Xeljanz®)', L(('Indication suisse', 'Colite ulcéreuse active modérée à sévère après échec des corticoïdes, de l’azathioprine, de la 6-mercaptopurine ou d’un anti-TNF.'), ('Dose', 'On donne 10 mg 2×/j pendant ≥ 8 semaines, puis 5 mg 2×/j, et l’on arrête en l’absence de réponse à 16 semaines.'), ('Risque', 'Il augmente les embolies pulmonaires et les thromboses par rapport aux anti-TNF.')) + src(FI('Xeljanz®'), MED))
C.pop('k51-d-infliximab', 'Infliximab de sauvetage', L(('Indication', 'Colite aiguë grave réfractaire aux corticoïdes IV (ECCO 2022, énoncé 1.2).'), ('Schéma', 'Régime optimal non établi (énoncé 1.3).')) + src(CHIR))
C.pop('k51-d-ciclosporine', 'Ciclosporine de sauvetage', L(('Indication', 'Elle remplace l’infliximab dans la colite aiguë grave réfractaire aux corticoïdes.'), ('Condition', 'Il faut prévoir un traitement d’entretien et disposer de l’expérience du centre.'), ('Surveillance', 'On surveille la pression artérielle, la fonction rénale et les taux sanguins, car elle est néphrotoxique et hypertensive.')) + src(CHIR))

C.termes = [
 (r'mésalazine', 'k51-d-mesalazine'), (r'5-ASA', 'k51-d-mesalazine'), (r'budésonide MMX', 'k51-d-budmmx'), (r'tofacitinib', 'k51-d-tofacitinib'),
 (r'védolizumab', 'k51-d-vedolizumab'), (r'anti-TNF', 'k51-antitnf'), (r'thiopurines?', 'k51-thiopurines'), (r'prednisolone', 'k51-cs'),
 (r'ciclosporine', 'k51-d-ciclosporine'), (r'infliximab', 'k51-d-infliximab'), (r'Truelove et Witts', 'k51-tw'), (r'colite aiguë grave', 'k51-cagg'),
 (r'Montréal', 'k51-montreal'), (r'score de Mayo|Mayo', 'k51-mayo'), (r'cholangite sclérosante primitive', 'k51-csp'), (r'abcès cryptiques', 'k51-abces'),
 (r'mégacôlon toxique', 'k51-megacolon'), (r'cytomégalovirus|CMV', 'k51-cmv'), (r'calprotectine', 'k51-calpro'), (r'coloscopie', 'k51-colo'),
 (r'coloproctectomie|colectomie', 'k51-colectomie'), (r'ténesme', 'k51-tenesme'), (r'manifestations extra-intestinales', 'k51-mei'),
]

C.write()
