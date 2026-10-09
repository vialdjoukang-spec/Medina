# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
# Règles du propriétaire (09.10.2026, 23 h 52) : chaque terme, choix diagnostique et décision thérapeutique est justifié ; aucune phrase nominale ; concision sans omission.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K58', 'Syndrome de l’intestin irritable',
    'K58 — Syndrome de l’intestin irritable · CIM-10-GM 2024 · Côlon et intestin grêle',
    'Adulte · formes à diarrhée, à constipation et mixte · rédaction du 09.10.2026 · référentiels S3 DGVS/DGNM 2021 (mise à jour, Z Gastroenterol 2021;59:1323-1415), informations professionnelles suisses',
    'Pharmacologie du côlon irritable')
w = C.w
S3 = ('Layer P. et al., Update S3-Leitlinie Reizdarmsyndrom : Definition, Pathophysiologie, Diagnostik und Therapie (DGVS, DGNM), Z Gastroenterol 2021;59:1323-1415', 'https://register.awmf.org/assets/guidelines/021-016l_S3_Definition-Pathophysiologie-Diagnostik-Therapie-Reizdarmsyndroms_2022-02-abgelaufen.pdf')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')
BR = credit({'auteur': 'Cabot Health, Bristol Stool Chart', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:BristolStoolChart.png'})
CO = credit({'auteur': 'melvil', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Colonoscopy_splenic_flexure.jpg'})
PS = credit({'auteur': 'Bastique (Cary Bass)', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Psyllium_seed_husks.JPG'})

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 34 ans souffre depuis deux ans de douleurs abdominales liées aux selles, avec des selles tantôt dures, tantôt molles et des ballonnements ; elle n’a ni perte de poids, ni sang dans les selles, ni anémie. <b>La question est donc de savoir si l’on peut poser un diagnostic positif de ' + w('k58-sii', 'syndrome de l’intestin irritable') + ' sans multiplier les examens, et comment la traiter.</b>',
 'Pour y répondre, le médecin doit savoir appliquer les ' + w('k58-rome', 'critères de Rome IV') + ', rechercher les ' + w('k58-alarme', 'signes d’alarme') + ' qui interdisent ce diagnostic de travail, et exclure de façon ciblée les maladies qui imitent le syndrome. Ensuite, il doit expliquer au patient un modèle plausible de ses symptômes, puis choisir un traitement selon le symptôme dominant, car la recommandation S3 de 2021 fonde la thérapeutique sur les symptômes et non sur un mécanisme unique.')
 + P('<i>Pourquoi ce cas ?</i> En effet, le côlon irritable est un diagnostic fréquent, mais un diagnostic d’exclusion mal conduit expose à deux erreurs opposées : manquer une maladie grave ou répéter inutilement les examens. Ainsi, contrairement à un manuel figé, ce cours relie chaque décision à sa justification, et chaque mot vert ouvre le critère, la dose ou la recommandation qui la fonde.')
 + key('Le diagnostic repose sur deux piliers : des symptômes compatibles et l’exclusion ciblée des maladies qui les imitent. Le traitement vise ensuite le symptôme dominant.', 'Point de départ.'))

C.a(1, 'Définition, sous-types et épidémiologie', P(
 'Selon les critères de Rome IV cités par la S3, le syndrome de l’intestin irritable associe des douleurs abdominales récidivantes, au moins un jour par semaine en moyenne au cours des trois derniers mois, à au moins deux des trois critères suivants : un lien avec la défécation, une modification de la fréquence des selles et une modification de leur consistance. De plus, les symptômes doivent avoir commencé plus de six mois avant le diagnostic. Cette exigence de durée se justifie, car une plainte récente oriente davantage vers une maladie organique évolutive.',
 'Par ailleurs, on distingue la forme à diarrhée (K58.1), la forme à constipation (K58.2), la forme mixte (K58.3) et les formes autres ou non précisées (K58.8) dans la CIM-10-GM. En effet, Rome IV classe le patient selon les jours d’un journal de deux semaines où au moins une selle est anormale, c’est-à-dire de type 1-2 ou 6-7 sur l’' + w('k58-bristol', 'échelle de Bristol') + '. Enfin, le syndrome est plus fréquent chez la femme (odds ratio poolé de 1,46), il altère nettement la qualité de vie, parfois davantage que d’autres maladies chroniques, et il s’associe souvent à des troubles anxieux, dépressifs ou somatoformes (S3 2021).')
 + C.img('k58_bristol.gif', 'Tableau illustré de l’échelle de Bristol : sept types de selles, des billes dures séparées (type 1) aux selles entièrement liquides (type 7).', 'Échelle de Bristol : les types 1-2 traduisent un transit lent et les types 6-7 un transit rapide.', BR)
 + P('<i>Lecture de l’image.</i> La forme des selles reflète le temps qu’elles passent dans le côlon : plus elles y restent, plus le côlon réabsorbe d’eau et plus elles deviennent dures et fragmentées. C’est pourquoi l’échelle de Bristol sert de mesure simple du transit, et pourquoi Rome IV l’utilise pour classer le sous-type, qui oriente ensuite le traitement.')
 + key('Le diagnostic exige des douleurs au moins un jour par semaine depuis trois mois, liées aux selles ou à leur fréquence ou à leur forme, et un début remontant à plus de six mois. Le sous-type se détermine avec l’échelle de Bristol.')
 + src(S3))

C.a(2, 'Physiopathologie : l’axe intestin-cerveau', P(
 'La S3 décrit le syndrome comme associé à des modifications possibles à tous les niveaux de l’axe intestin-cerveau. Ainsi, elle cite des troubles de la motricité et des réflexes intestinaux, un métabolisme anormal des acides biliaires, une altération de la barrière et de la sécrétion muqueuses, une ' + w('k58-hypersens', 'hypersensibilité viscérale') + ', ainsi que des modifications du microbiote. De plus, un syndrome peut apparaître après une inflammation intestinale, infectieuse ou non, ou après une antibiothérapie (S3 2021).',
 'Par ailleurs, le cerveau module la perception. En effet, les patients peuvent percevoir plus intensément des stimuli viscéraux normaux et les interpréter comme menaçants ; or, le stress, l’anxiété et la dépression peuvent participer à l’apparition et à l’entretien des symptômes, même si le stress seul ne cause pas le syndrome. C’est pourquoi la S3 retient un modèle biopsychosocial, qui justifie à la fois les traitements intestinaux, comme les antispasmodiques, et les traitements centraux, comme les antidépresseurs ou la psychothérapie.')
 + C.img('k58_colo.gif', 'Coloscopie : muqueuse colique rose, lisse et brillante au niveau de l’angle gauche, avec une zone sombre correspondant à la rate vue par transparence.', 'Coloscopie normale (angle colique gauche) : dans le côlon irritable, la muqueuse est macroscopiquement normale.', CO)
 + P('<i>Lecture de l’image.</i> La muqueuse est normale, avec des vaisseaux fins visibles et sans ulcération. Or, c’est précisément ce que montre la coloscopie d’un patient atteint de côlon irritable : la maladie touche la fonction, la sensibilité et la régulation nerveuse, non la structure visible. Ainsi, une coloscopie normale ne prouve pas le diagnostic, mais elle aide à exclure une maladie organique quand une diarrhée ou un signe d’alarme l’impose.')
 + key('Le syndrome résulte d’un dérèglement de l’axe intestin-cerveau : motricité, acides biliaires, barrière muqueuse, hypersensibilité viscérale, microbiote et facteurs psychiques. La muqueuse reste macroscopiquement normale.')
 + src(S3))

C.a(3, 'Diagnostic positif et signes d’alarme', P(
 'La S3 exige deux composantes pour un diagnostic positif (grade A) : l’anamnèse et le profil des symptômes doivent être compatibles, et les maladies qui donnent les mêmes symptômes doivent être exclues de façon ciblée selon les symptômes. En outre, elle recommande d’exclure en priorité les maladies graves potentiellement menaçantes (grade A), puis d’envisager les causes traitables (grade B). Ce choix se justifie, car l’objectif est d’éviter à la fois l’erreur grave et la recherche aveugle.',
 'Cependant, certains signes excluent d’emblée le diagnostic de travail : la fièvre ou d’autres signes inflammatoires, une anémie ou d’autres anomalies biologiques, une perte de poids, du sang visible ou occulte dans les selles, des symptômes progressifs, et une anamnèse de moins de trois mois. En effet, chacun de ces signes témoigne d’une lésion ou d’une inflammation que le côlon irritable ne produit pas. De plus, la S3 rappelle deux pièges : plus de 85 % des patientes atteintes d’un cancer de l’ovaire ont d’abord des symptômes de type côlon irritable, et environ un tiers des patients ayant une maladie inflammatoire chronique de l’intestin en rémission en présentent le tableau complet.')
 + alert('Une fièvre, une anémie, une perte de poids, du sang dans les selles, des symptômes progressifs ou une histoire de moins de trois mois interdisent de retenir le côlon irritable avant un bilan complet. Une femme qui présente de nouveaux symptômes de type côlon irritable doit faire évoquer un cancer de l’ovaire.', 'Gravité d’abord.')
 + quiz('Un homme de 58 ans a des troubles du transit depuis deux mois et une anémie ferriprive. Peut-on retenir un côlon irritable ?',
   [('Oui, si les critères de Rome IV sont remplis', False), ('Non : l’histoire courte et l’anémie sont des signes d’alarme qui imposent un bilan, notamment endoscopique', True), ('Oui, après un essai d’antispasmodique', False)],
   'Selon la S3, une anamnèse de moins de trois mois et une anémie excluent le diagnostic de travail ; une lésion organique doit d’abord être recherchée.')
 + key('Le diagnostic positif repose sur des symptômes compatibles et une exclusion ciblée (grade A). Les signes d’alarme interdisent ce diagnostic jusqu’à un bilan complet.')
 + src(S3))

C.a(4, 'Examens : cibler et ne pas répéter', P(
 'Le bilan dépend du symptôme dominant. Ainsi, lorsque la diarrhée domine, la S3 impose un bilan complet, avec une recherche de germes dans les selles et une endoscopie (grade A) ; en effet, la plupart des diarrhées chroniques ont une cause identifiable et traitable, comme une maladie inflammatoire, une colite microscopique ou une maladie cœliaque. En revanche, en l’absence de diarrhée, un traitement symptomatique d’essai de deux mois au plus est possible après un bilan de base négatif, même sans diagnostic positif établi (grade 0).',
 'Par ailleurs, plusieurs examens sont déconseillés. En effet, aucun biomarqueur ne permet un diagnostic positif (grade 0), l’analyse du microbiote commensal ne doit pas être faite (grade B), et le dosage des IgG spécifiques d’aliments ne doit pas être demandé (grade B), car ces tests ne distinguent pas les malades des sujets sains. De plus, en cas d’intolérance alimentaire suspectée, la S3 propose un journal des symptômes suivi d’une éviction ciblée et limitée dans le temps (grade B). Enfin, une fois le diagnostic posé, il faut éviter de répéter le bilan si aucun élément nouveau n’apparaît (grade A), car la répétition entretient l’inquiétude sans bénéfice.')
 + trap('Une diarrhée chronique ne doit pas être étiquetée côlon irritable sans recherche de germes et sans endoscopie, car la majorité des diarrhées chroniques ont une autre cause. À l’inverse, refaire une coloscopie normale sans élément nouveau n’apporte rien.', 'Piège')
 + key('Une diarrhée dominante impose les selles et l’endoscopie. Les biomarqueurs, l’analyse du microbiote et les IgG alimentaires sont inutiles. Le bilan ne se répète pas sans élément nouveau.')
 + src(S3))

C.a(5, 'Traitement : principes généraux', P(
 'Le traitement commence par l’explication. En effet, la S3 recommande de donner au patient un modèle individuel plausible de ses symptômes, des objectifs réalistes et une explication du lien entre stress, émotions et fonctions intestinales (grade B) ; ainsi, le patient comprend pourquoi ses symptômes sont réels sans être dangereux. Ensuite, les déclencheurs individuels, comme certains aliments, des médicaments, le travail de nuit ou le stress, doivent être identifiés, si possible avec un journal (grade B), et l’activité physique doit être recommandée (grade B).',
 'Par ailleurs, le traitement médicamenteux est orienté sur le symptôme, et son succès se juge sur l’amélioration et la tolérance (grade B). De plus, en cas d’échec, plusieurs médicaments peuvent être essayés successivement ou associés, y compris avec des traitements non médicamenteux (grade B). Enfin, un traitement efficace peut être poursuivi, pris à la demande ou interrompu pour un essai d’arrêt (grade 0), car l’évolution du syndrome est bénigne et fluctuante.')
 + key('On explique d’abord le mécanisme, on identifie les déclencheurs et on recommande l’activité physique. On traite ensuite le symptôme dominant et on juge l’effet sur la tolérance et l’amélioration.')
 + src(S3))

C.a(6, 'Alimentation et fibres', P(
 'Il n’existe pas de régime unique valable pour tous (grade 0) ; c’est pourquoi la S3 réserve les régimes d’éviction prolongés aux intolérances prouvées, sous contrôle diététique (grade B). En effet, ces régimes exposent à la dénutrition, que la S3 demande d’éviter ou de traiter (grade A). En revanche, le ' + w('k58-fodmap', 'régime pauvre en FODMAP') + ' devrait être recommandé lorsque la douleur, les ballonnements ou la diarrhée dominent (grade B), et il peut l’être lorsque la constipation domine (grade 0), avec l’aide d’une diététicienne (grade B). Ce choix se justifie, car ces sucres courts, mal absorbés dans le grêle, attirent l’eau dans la lumière puis fermentent dans le côlon, ce qui distend un intestin hypersensible.',
 'De plus, les ' + w('k58-fibres', 'fibres solubles') + ' doivent être utilisées chez l’adulte dont la constipation domine (grade B), et elles peuvent l’être dans la forme à diarrhée (grade 0). Ce choix se justifie, car les fibres solubles retiennent l’eau et forment un gel : elles ramollissent les selles dures et donnent de la consistance aux selles liquides, alors que les fibres insolubles fermentent davantage et peuvent aggraver les ballonnements.')
 + C.img('k58_psyllium.gif', 'Photographie macroscopique de téguments de graines de psyllium, fins et blanchâtres.', 'Téguments de psyllium (Plantago ovata) : source classique de fibres solubles.', PS)
 + P('<i>Lecture de l’image.</i> Ces téguments gonflent au contact de l’eau et forment un mucilage ; ainsi, ils augmentent le volume et l’hydratation des selles. C’est pourquoi la S3 demande de les prendre avec suffisamment de liquide : sans eau, le gel ne se forme pas correctement et la constipation peut s’aggraver.')
 + key('Aucun régime ne convient à tous. Le régime pauvre en FODMAP se propose surtout quand la douleur, les ballonnements ou la diarrhée dominent. Les fibres solubles, comme le psyllium, se prescrivent dans la forme constipée et peuvent servir dans la forme diarrhéique, avec un apport hydrique suffisant.')
 + src(S3))

C.a(7, 'Traitement selon le symptôme dominant', P(
 'Contre la douleur, les ' + w('k58-spasmo', 'antispasmodiques') + ' doivent être recommandés (grade A) ; en effet, une méta-analyse Cochrane citée par la S3 montre un effet sur la douleur (58 % contre 46 % sous placebo, nombre de sujets à traiter de 5). De même, l’' + w('k58-d-menthe', 'huile de menthe poivrée') + ' doit être envisagée contre la douleur et les ballonnements (grade A). En outre, l’' + w('k58-d-ami', 'amitriptyline') + ' à faible dose devrait être utilisée contre la douleur et les symptômes globaux, sauf en cas de constipation (grade B), car son effet anticholinergique ralentit le transit. En revanche, les antalgiques périphériques ne devraient pas être utilisés (grade B) et les agonistes des récepteurs μ-opioïdes ne doivent pas l’être (grade A), en raison de leurs effets digestifs et du risque de dépendance.',
 'Contre la diarrhée, le ' + w('k58-d-lop', 'lopéramide') + ' devrait être utilisé (grade B) ; de plus, la rifaximine devrait être envisagée dans les formes réfractaires sans constipation (grade B). Contre la constipation, les laxatifs osmotiques ou stimulants devraient être proposés selon la tolérance (grade B) ; ensuite, en cas de constipation réfractaire aux laxatifs, surtout avec douleur et ballonnements, le ' + w('k58-d-lina', 'linaclotide') + ' devrait être recommandé (grade B). Par ailleurs, des probiotiques sélectionnés devraient être utilisés (grade B), car des essais randomisés ont montré un effet de certaines souches sur les symptômes ou la qualité de vie ; c’est pourquoi on choisit une souche étudiée selon le symptôme visé. Enfin, la psychothérapie doit être proposée lorsqu’elle est indiquée (grade A), alors que la mésalazine ne devrait pas être utilisée (grade B).')
 + table(['Symptôme dominant', 'Premier choix', 'Si échec', 'Grade S3'], [
   ['Douleur', 'Antispasmodique, huile de menthe poivrée', 'Amitriptyline à faible dose (sauf constipation)', 'A ; A ; B'],
   ['Diarrhée', 'Fibres solubles, lopéramide', 'Rifaximine (hors indication suisse)', '0 ; B ; B'],
   ['Constipation', 'Fibres solubles, laxatif osmotique ou stimulant', 'Linaclotide', 'B ; B ; B'],
   ['Composante psychique', 'Explication, gestion du stress', 'Psychothérapie, antidépresseur', 'B ; A']])
 + P('<i>Lecture du tableau.</i> Chaque ligne cible un mécanisme : l’antispasmodique relâche le muscle lisse, le lopéramide freine la propulsion, le laxatif osmotique retient l’eau dans le côlon, et le linaclotide fait sécréter du chlore et de l’eau dans la lumière. Ainsi, le choix suit le symptôme dominant, et l’on passe à la colonne suivante seulement si le premier choix échoue.')
 + C.pareto('pareto-k58-clinique', 'Côlon irritable', ['k58-1', 'k58-3', 'k58-4', 'k58-5', 'k58-7'],
     ['Appliquez les critères de Rome IV et classez le sous-type avec l’échelle de Bristol.',
      'Recherchez les signes d’alarme avant de retenir le diagnostic.',
      'Faites une recherche de germes et une endoscopie si la diarrhée domine.',
      'Expliquez le mécanisme et identifiez les déclencheurs.',
      'Traitez le symptôme dominant : antispasmodique, lopéramide ou fibres et laxatifs.',
      'N’utilisez pas d’opioïdes contre la douleur.'])
 + key('La douleur se traite par antispasmodique ou huile de menthe poivrée, puis amitriptyline. La diarrhée se traite par lopéramide, et la constipation par fibres et laxatifs, puis linaclotide. Les opioïdes sont proscrits.')
 + src(S3))

C.a(8, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. Ses douleurs sont liées aux selles depuis deux ans, avec des selles alternativement de types 1-2 et 6-7 : elle remplit donc les critères de Rome IV d’une forme mixte. De plus, elle n’a aucun signe d’alarme, et la diarrhée ne domine pas ; par conséquent, un bilan de base suffit et une coloscopie n’est pas nécessaire d’emblée.',
 'Dès lors, le médecin lui explique l’axe intestin-cerveau, lui propose un journal des symptômes et de l’activité physique, puis des fibres solubles et de l’huile de menthe poivrée pour la douleur et les ballonnements. Enfin, il réévalue l’effet et la tolérance ; si les douleurs persistent, il peut proposer une amitriptyline à faible dose, en l’informant qu’il s’agit d’un usage hors indication en Suisse.')
 + key('La patiente remplit les critères de Rome IV, n’a pas de signe d’alarme et reçoit une explication, des fibres solubles et de l’huile de menthe poivrée, puis éventuellement de l’amitriptyline.')
 + src(S3))

C.a(9, 'Critères formels et paramètres clés', alert(
 '<p><b>Rome IV.</b> Les douleurs abdominales surviennent au moins un jour par semaine en moyenne depuis trois mois, avec au moins deux critères parmi le lien avec la défécation, la modification de la fréquence et la modification de la forme des selles ; le début remonte à plus de six mois. <b>Signes d’alarme (S3).</b> La fièvre, l’anémie, la perte de poids, le sang dans les selles, la progression et une histoire de moins de trois mois excluent le diagnostic de travail.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Le syndrome touche plus souvent les femmes (odds ratio 1,46). Les antispasmodiques soulagent la douleur chez 58 % des patients contre 46 % sous placebo (nombre de sujets à traiter de 5). Un essai symptomatique sans diagnostic positif ne dépasse pas deux mois.</div>'
 + src(S3))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi on ne le demande que si cette question se pose.')
 + table(['Question', 'Examen', 'Recommandation S3 2021'], [
   ['Les symptômes sont-ils compatibles ?', 'Anamnèse, ' + w('k58-rome', 'critères de Rome IV') + ', journal de Bristol', 'Diagnostic positif (grade A)'],
   ['Y a-t-il une maladie grave ?', 'Recherche des ' + w('k58-alarme', 'signes d’alarme') + ', examen clinique, bilan de base', 'Exclusion prioritaire (grade A)'],
   ['La diarrhée domine-t-elle ?', 'Recherche de germes dans les selles et endoscopie', 'Obligatoire (grade A)'],
   ['Une intolérance est-elle suspectée ?', 'Journal alimentaire, éviction ciblée et limitée', 'Grade B'],
   ['Faut-il des tests du microbiote ou des IgG alimentaires ?', 'Aucun', 'À ne pas faire (grade B)']])
 + P('<i>Lecture du tableau.</i> La dernière ligne compte autant que les autres : un examen inutile retarde l’explication et entretient l’idée d’une maladie cachée. Ainsi, la S3 transforme le diagnostic d’exclusion en un diagnostic positif encadré, qui protège le patient à la fois de l’erreur et de la surenchère.')
 + key('On confirme des symptômes compatibles, on exclut les maladies graves, on explore la diarrhée et on renonce aux tests sans valeur.')
 + src(S3))

C.e(2, 'Lire l’échelle de Bristol et la coloscopie', P(
 'Le journal de Bristol sur deux semaines permet de compter les jours avec au moins une selle de type 1-2 ou 6-7 ; ainsi, il classe la forme à constipation, à diarrhée ou mixte selon Rome IV. De plus, la coloscopie, lorsqu’elle est indiquée, doit montrer une muqueuse normale ; en revanche, des ulcérations, une inflammation ou une tumeur imposent un autre diagnostic.')
 + C.img('k58_bristol.gif', 'Échelle de Bristol : sept types de selles.', 'Échelle de Bristol utilisée pour le journal des selles.', BR)
 + P('<i>Lecture de l’image.</i> Les types 3 et 4 sont les selles normales ; à l’inverse, les extrêmes traduisent un transit accéléré ou ralenti. C’est pourquoi un journal objectif vaut mieux que le souvenir du patient pour classer le sous-type et choisir le traitement.')
 + key('Le journal de Bristol classe le sous-type, et une coloscopie, si elle est indiquée, doit être normale.')
 + C.pareto('pareto-k58-examens', 'Examens', ['k58-e-1', 'k58-e-2'],
     ['Appliquez les critères de Rome IV.',
      'Cherchez les signes d’alarme.',
      'Explorez toute diarrhée chronique par les selles et l’endoscopie.',
      'Ne demandez ni test du microbiote ni IgG alimentaires.'])
 + src(S3))

# ---------------- Sciences
C.s('neuro', 'Neurophysiologie', 'Neurophysiologie : l’hypersensibilité viscérale', P(
 'Les fibres sensitives de l’intestin transmettent la distension et la contraction vers la moelle et le cerveau, qui filtrent normalement ces signaux. Or, chez le patient, ce filtrage est modifié : des distensions normales sont perçues comme douloureuses. C’est pourquoi les traitements centraux, comme l’amitriptyline à faible dose ou la psychothérapie, peuvent réduire la douleur sans modifier le transit.')
 + key('Une perception amplifiée de stimuli normaux explique la douleur et justifie les traitements centraux.', 'Science → clinique.'))
C.s('physio', 'Physiologie', 'Physiologie : eau, transit et forme des selles', P(
 'Le côlon réabsorbe la plus grande partie de l’eau qui lui arrive ; ainsi, plus le transit est lent, plus les selles sont dures. Par conséquent, un laxatif osmotique, qui retient l’eau dans la lumière, ramollit les selles, alors que le lopéramide, qui ralentit la propulsion, laisse au côlon le temps de les déshydrater. De plus, le linaclotide active la guanylate cyclase C de l’épithélium et augmente la sécrétion de chlore et d’eau.')
 + key('Le temps de transit règle l’hydratation des selles, et chaque médicament agit sur ce temps ou sur l’eau intraluminale.', 'Science → pharmacologie.'))
C.s('micro', 'Microbiologie', 'Microbiologie : après une infection ou des antibiotiques', P(
 'La S3 admet qu’un syndrome peut suivre une infection intestinale ou une antibiothérapie, et qu’il peut s’accompagner d’un microbiote modifié. Cependant, l’analyse du microbiote commensal ne doit pas être demandée, car elle ne permet pas de poser le diagnostic. Ainsi, la rifaximine, antibiotique peu absorbé, n’est envisagée que dans les formes réfractaires sans constipation.')
 + key('Le microbiote participe au mécanisme, mais son analyse n’aide pas au diagnostic.', 'Science → décision.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les médicaments se choisissent selon le symptôme dominant ; en effet, aucun ne traite l’ensemble du syndrome.')
 + table(['Symptôme', 'Médicament', 'Mécanisme', 'Fenêtre'], [
   ['Douleur, spasmes', 'Mébévérine, butylscopolamine', 'Relâchement du muscle lisse', w('k58-spasmo', 'Fiche')],
   ['Douleur, ballonnements', 'Huile de menthe poivrée', 'Relâchement du muscle lisse par blocage calcique', w('k58-d-menthe', 'Monographie')],
   ['Diarrhée', 'Lopéramide', 'Agoniste μ périphérique qui ralentit le transit', w('k58-d-lop', 'Monographie')],
   ['Constipation réfractaire', 'Linaclotide', 'Agoniste de la guanylate cyclase C', w('k58-d-lina', 'Monographie')],
   ['Douleur globale sans constipation', 'Amitriptyline à faible dose', 'Modulation centrale de la douleur', w('k58-d-ami', 'Monographie')]])
 + P('<i>Lecture du tableau.</i> Le lopéramide est un agoniste μ, comme les opioïdes que la S3 proscrit contre la douleur ; cependant, il agit surtout dans l’intestin et y freine la propulsion, ce qui explique qu’il soit utile contre la diarrhée et non contre la douleur.')
 + key('Le choix suit le symptôme : antispasmodique ou menthe pour la douleur, lopéramide pour la diarrhée, linaclotide pour la constipation réfractaire, amitriptyline pour la douleur globale.')
 + src(S3))

C.p(2, 'Doses et statut réglementaire', P(
 'Les doses ci-dessous proviennent des informations professionnelles suisses lorsqu’elles existent ; sinon, elles proviennent du tableau posologique de la S3, et l’écart réglementaire est signalé.')
 + table(['Médicament', 'Dose', 'Statut suisse', 'Source'], [
   ['Huile de menthe poivrée (Colpermin®)', '1 capsule 3 ×/j, 2 capsules 3 ×/j si symptômes sévères ; 3 mois au plus', 'Indiqué dans le côlon irritable avec spasmes et ballonnements', 'FI Colpermin®'],
   ['Mébévérine (Duspatalin® Retard 200 mg)', '1 gélule matin et soir', 'Indiqué dans les douleurs des troubles fonctionnels digestifs', 'FI Duspatalin® Retard'],
   ['Lopéramide (Imodium®)', 'Diarrhée chronique : 4 mg au début, puis 2-12 mg/j selon les selles ; 16 mg/j au plus', 'Indiqué dans la diarrhée chronique', 'FI Imodium®'],
   ['Linaclotide (Constella®)', '290 µg 1 ×/j, au moins 30 min avant un repas ; réévaluer après 4 semaines', 'Indiqué dans le côlon irritable modéré à sévère avec constipation', 'FI Constella®'],
   ['Amitriptyline (Saroten®)', '12,5 ou 25 mg le soir, augmentés chaque semaine jusqu’à 50 mg, 75 mg au plus (S3)', 'Hors indication : la FI ne cite pas le côlon irritable', 'S3 2021, FI Saroten®'],
   ['Psyllium', '1 mesure ou 1 sachet 2-6 ×/j, avec 150 ml d’eau à chaque prise (S3)', 'Dose tirée de la S3', 'S3 2021']])
 + P('<i>Lecture du tableau.</i> Les doses d’amitriptyline sont nettement plus faibles que celles de la dépression, car l’objectif est de moduler la douleur viscérale et non l’humeur ; de plus, les effets indésirables, comme la somnolence ou la bouche sèche, apparaissent souvent avant le bénéfice, ce que le patient doit savoir pour ne pas arrêter trop tôt.')
 + trap('L’amitriptyline est hors indication en Suisse dans le côlon irritable, et la rifaximine l’est aussi selon la S3 (550 mg 3 ×/j pendant 2 semaines, hors indication). Le patient doit en être informé. À valider à l’audit.', 'Point à valider')
 + key('La menthe poivrée, la mébévérine, le lopéramide et le linaclotide ont une indication suisse adaptée. L’amitriptyline et la rifaximine sont utilisées hors indication.')
 + src(FI('Colpermin®'), FI('Duspatalin® Retard'), FI('Imodium®'), FI('Constella®'), FI('Saroten®'), S3))

C.p(3, 'Contre-indications et surveillance', alert(
 'Le linaclotide est contre-indiqué en cas d’obstruction mécanique connue ou suspectée, et il ne doit être prescrit qu’après exclusion d’une maladie organique ; de plus, il peut provoquer une diarrhée (FI Constella®). La mébévérine est contre-indiquée en cas d’iléus paralytique (FI Duspatalin®). Le lopéramide ne doit pas être donné en première intention en cas de dysenterie aiguë ou de colite ulcéreuse aiguë, ni en cas d’insuffisance hépatique sévère (FI Imodium®). L’huile de menthe poivrée est contre-indiquée en cas d’obstruction biliaire, de cholécystite, d’atteinte hépatique et d’allergie à l’arachide ou au soja (FI Colpermin®). Enfin, l’amitriptyline est contre-indiquée après un infarctus récent et en cas de trouble de la conduction ou du rythme cardiaque (FI Saroten®).', 'Sécurité.')
 + P('Par ailleurs, chaque traitement se réévalue sur l’amélioration du symptôme ciblé et sur la tolérance ; ainsi, l’absence d’effet après quatre semaines de linaclotide impose de réexaminer le patient, comme le demande l’information professionnelle.')
 + key('Vérifiez l’absence d’obstruction avant le linaclotide, l’absence de colite aiguë avant le lopéramide et l’absence de trouble du rythme avant l’amitriptyline.')
 + C.pareto('pareto-k58-pharma', 'Pharmacologie', ['k58-p-1', 'k58-p-2', 'k58-p-3'],
     ['Choisissez le médicament selon le symptôme dominant.',
      'Prescrivez l’huile de menthe poivrée 3 fois par jour, 3 mois au plus.',
      'Réservez le linaclotide aux constipations réfractaires aux laxatifs.',
      'Informez le patient que l’amitriptyline est hors indication.'])
 + src(FI('Constella®'), FI('Duspatalin® Retard'), FI('Imodium®'), FI('Colpermin®'), FI('Saroten®')))

# ---------------- Fenêtres (phrases complètes)
L = lab
C.pop('k58-sii', 'Syndrome de l’intestin irritable', L(('Définition', 'Il s’agit d’un trouble de l’axe intestin-cerveau qui associe des douleurs abdominales récidivantes à des troubles du transit, sans lésion organique qui les explique.'), ('Pourquoi ce nom ?', 'Le terme « irritable » traduit l’hyperréactivité de l’intestin, à la fois motrice et sensitive.'), ('Diagnostic', 'Il repose sur les critères de Rome IV et sur l’exclusion ciblée des maladies qui l’imitent.')) + src(S3))
C.pop('k58-rome', 'Critères de Rome IV', L(('Douleur', 'Les douleurs surviennent au moins un jour par semaine en moyenne au cours des trois derniers mois.'), ('Critères associés', 'Au moins deux critères sont présents : un lien avec la défécation, une modification de la fréquence et une modification de la forme des selles.'), ('Durée', 'Les symptômes ont commencé plus de six mois avant le diagnostic.'), ('Pourquoi ?', 'Ces exigences sélectionnent un trouble chronique et stable, alors qu’une plainte récente ou progressive évoque une maladie organique.')) + src(S3))
C.pop('k58-alarme', 'Signes d’alarme', L(('Liste', 'La fièvre ou d’autres signes inflammatoires, l’anémie ou d’autres anomalies biologiques, la perte de poids, le sang dans les selles, la progression et une histoire de moins de trois mois sont des signes d’alarme.'), ('Pourquoi ?', 'Chacun traduit une lésion ou une inflammation que le côlon irritable ne produit pas.'), ('Conséquence', 'Le diagnostic de travail est exclu jusqu’à un bilan complet.')) + src(S3))
C.pop('k58-bristol', 'Échelle de Bristol', L(('Principe', 'Elle classe les selles en sept types, des billes dures (type 1) aux selles liquides (type 7).'), ('Usage', 'Rome IV compte sur deux semaines les jours avec une selle de type 1-2 ou 6-7 pour définir le sous-type.'), ('Pourquoi ?', 'La forme des selles reflète le temps de transit colique.')) + C.img('k58_bristol.gif', 'Échelle de Bristol.', 'Échelle de Bristol.', BR) + src(S3))
C.pop('k58-hypersens', 'Hypersensibilité viscérale', L(('Définition', 'Le patient perçoit plus intensément des stimuli viscéraux normaux et les juge menaçants.'), ('Conséquence', 'Cette perception explique la douleur sans lésion et justifie les traitements centraux.')) + src(S3))
C.pop('k58-fodmap', 'Régime pauvre en FODMAP', L(('Définition', 'Les FODMAP sont des oligo-, di- et monosaccharides fermentescibles et des polyols, c’est-à-dire des sucres courts mal absorbés dans l’intestin grêle.'), ('Pourquoi ?', 'Ils deviennent osmotiquement actifs et fermentent rapidement dans le côlon, ce qui provoque douleurs, ballonnements et selles molles.'), ('Déroulement', 'Le patient évite les aliments riches en FODMAP pendant 6 à 8 semaines, puis il les réintroduit progressivement pour trouver sa tolérance, et il adopte enfin une alimentation durable.'), ('Indication', 'La S3 le recommande quand la douleur, les ballonnements ou la diarrhée dominent (grade B), avec une diététicienne (grade B), afin d’éviter une restriction excessive et une dénutrition.')) + src(S3))
C.pop('k58-fibres', 'Fibres solubles', L(('Indication', 'Elles doivent être utilisées dans la forme constipée (grade B) et peuvent l’être dans la forme diarrhéique (grade 0).'), ('Pourquoi ?', 'Elles forment un gel qui normalise l’hydratation des selles.'), ('Dose (S3)', 'On donne 1 mesure ou 1 sachet de psyllium 2 à 6 fois par jour, avec 150 ml d’eau à chaque prise.')) + C.img('k58_psyllium.gif', 'Téguments de psyllium.', 'Psyllium.', PS) + src(S3))
C.pop('k58-spasmo', 'Antispasmodiques', L(('Indication', 'Ils doivent être recommandés contre la douleur (grade A).'), ('Preuve', 'Ils soulagent la douleur chez 58 % des patients contre 46 % sous placebo, avec un nombre de sujets à traiter de 5.'), ('Exemples suisses', 'La mébévérine (Duspatalin® Retard) se prend à raison d’une gélule de 200 mg matin et soir ; la butylscopolamine est un antispasmodique anticholinergique.')) + src(S3, FI('Duspatalin® Retard')))
C.pop('k58-d-menthe', 'Huile de menthe poivrée (Colpermin®)', L(('Indication', 'La FI suisse l’indique dans le côlon irritable avec spasmes et ballonnements ; la S3 demande de l’envisager (grade A).'), ('Dose', 'L’adulte prend 1 capsule 3 fois par jour, ou 2 capsules 3 fois par jour si les symptômes sont sévères, pendant 3 mois au plus.'), ('Contre-indications', 'Elle est contre-indiquée en cas d’obstruction biliaire, de cholécystite, d’atteinte hépatique, d’achlorhydrie et d’allergie à l’arachide ou au soja.')) + src(FI('Colpermin®'), S3))
C.pop('k58-d-lop', 'Lopéramide (Imodium®)', L(('Indication', 'La S3 recommande de l’utiliser contre la diarrhée (grade B), et la FI suisse l’indique dans la diarrhée chronique.'), ('Dose', 'L’adulte commence par 4 mg, puis prend 2 à 12 mg par jour selon les selles, sans dépasser 16 mg par jour.'), ('Prudence', 'On ne le donne pas en première intention en cas de dysenterie aiguë ou de colite ulcéreuse aiguë, car il retiendrait les germes et l’inflammation.')) + src(FI('Imodium®'), S3))
C.pop('k58-d-lina', 'Linaclotide (Constella®)', L(('Indication', 'La FI suisse l’indique dans le côlon irritable modéré à sévère avec constipation chez l’adulte ; la S3 le réserve aux constipations réfractaires aux laxatifs.'), ('Dose', 'On prend 290 µg une fois par jour, au moins 30 minutes avant un repas, et l’on réévalue après 4 semaines.'), ('Contre-indication', 'Il est contre-indiqué en cas d’obstruction mécanique connue ou suspectée.')) + src(FI('Constella®'), S3))
C.pop('k58-d-ami', 'Amitriptyline (Saroten®)', L(('Indication', 'La S3 recommande de l’utiliser contre la douleur et les symptômes globaux, sauf en cas de constipation (grade B).'), ('Dose (S3)', 'On commence par 12,5 ou 25 mg le soir, puis on augmente chaque semaine jusqu’à 50 mg, sans dépasser 75 mg.'), ('Statut', 'Cet usage est hors indication en Suisse.'), ('Contre-indications', 'Elle est contre-indiquée après un infarctus récent et en cas de trouble de la conduction ou du rythme cardiaque.')) + src(S3, FI('Saroten®')))

C.termes = [
 (r'syndrome de l’intestin irritable', 'k58-sii'), (r'critères de Rome IV', 'k58-rome'), (r'signes? d’alarme', 'k58-alarme'), (r'échelle de Bristol', 'k58-bristol'),
 (r'hypersensibilité viscérale', 'k58-hypersens'), (r'fibres solubles', 'k58-fibres'), (r'régime pauvre en FODMAP', 'k58-fodmap'), (r'antispasmodiques?', 'k58-spasmo'), (r'huile de menthe poivrée', 'k58-d-menthe'),
 (r'lopéramide', 'k58-d-lop'), (r'linaclotide', 'k58-d-lina'), (r'amitriptyline', 'k58-d-ami'),
]

C.write()
