import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K50', 'Maladie de Crohn',
    'K50 — Maladie de Crohn [enteritis regionalis] · CIM-10-GM 2024 · Intestin grêle et côlon',
    'Adulte · diagnostic, classification de Montréal, traitement d’induction et d’entretien, stratégie « treat-to-target » · rédaction du 09.10.2026 · référentiels ECCO traitement médical 2024, classification de Montréal 2005, informations professionnelles suisses',
    'Pharmacologie de la maladie de Crohn')
w = C.w
ECCO = ('Gordon H. et al., ECCO Guidelines on Therapeutics in Crohn’s Disease: Medical Treatment, J Crohns Colitis 2024;18:1531-1555', 'https://doi.org/10.1093/ecco-jcc/jjae091')
MTL = ('Satsangi J. et al., The Montreal classification of inflammatory bowel disease, Gut 2006;55:749-753', 'https://doi.org/10.1136/gut.2005.082909')
DIAG = ('Maaser C. et al., ECCO-ESGAR Guideline for Diagnostic Assessment in IBD Part 1, J Crohns Colitis 2019;13:144-164', 'https://doi.org/10.1093/ecco-jcc/jjy113')
STR = ('Turner D. et al., STRIDE-II, Gastroenterology 2021;160:1570-1583', 'https://doi.org/10.1053/j.gastro.2020.12.031')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 24 ans, fumeur, souffre depuis quatre mois de diarrhée sans sang, de douleurs de la fosse iliaque droite et d’un amaigrissement de 6 kg. Or, sa CRP est à 38 mg/l et sa ' + w('k50-calpro', 'calprotectine fécale') + ' très élevée. <b>La question est donc de savoir s’il a une maladie de Crohn, quelle en est l’étendue et le phénotype, et quel traitement proposer d’emblée.</b>',
 'Pour y répondre, le médecin doit savoir : confirmer le diagnostic par l’' + w('k50-ileocolo', 'iléocoloscopie avec biopsies') + ' et l’imagerie du grêle ; classer la maladie selon la ' + w('k50-montreal', 'classification de Montréal') + ' ; choisir entre ' + w('k50-d-budesonide', 'budésonide') + ', corticoïdes systémiques et traitements avancés ; enfin, suivre une stratégie ' + w('k50-t2t', '« treat-to-target »') + ' fondée sur des marqueurs objectifs.')
 + key('Diarrhée chronique, douleur de la fosse iliaque droite, amaigrissement et calprotectine élevée chez un jeune : penser maladie de Crohn.', 'Point de départ.'))

C.a(1, 'Définition', P(
 'La maladie de Crohn est une maladie inflammatoire chronique de l’intestin, qui évolue par poussées et rémissions. Ainsi, elle peut toucher tout le tube digestif, de la bouche à l’anus, avec une prédilection pour l’iléon terminal et le côlon. De plus, l’inflammation est ' + w('k50-transmurale', 'transmurale') + ' et segmentaire, avec des intervalles de muqueuse saine ; c’est pourquoi elle se complique de sténoses, de fistules et d’abcès.',
 'Par opposition, la rectocolite hémorragique (K51) est limitée à la muqueuse du côlon et s’étend de façon continue depuis le rectum. Par conséquent, la CIM-10-GM classe la maladie de Crohn selon la localisation : intestin grêle (K50.0), gros intestin (K50.1), atteinte combinée (K50.8) et forme non précisée (K50.9).')
 + table(['Caractère', 'Maladie de Crohn', 'Rectocolite hémorragique'], [
   ['Localisation', 'Tout le tube digestif, surtout iléon terminal', 'Rectum et côlon'],
   ['Distribution', 'Segmentaire, discontinue', 'Continue depuis le rectum'],
   ['Profondeur', 'Transmurale', 'Muqueuse'],
   ['Granulomes', 'Possibles (non nécrosants)', 'Absents'],
   ['Atteinte périanale', 'Fréquente (fistules, abcès)', 'Rare']])
 + P('Le tableau se lit ligne par ligne : en effet, chaque critère oriente, mais aucun ne suffit seul, si bien que le diagnostic repose sur leur ensemble.')
 + key('Inflammation chronique, transmurale, segmentaire, de la bouche à l’anus ; sténoses, fistules, abcès ; granulomes non nécrosants possibles.')
 + src(DIAG, MTL))

C.a(2, 'Épidémiologie et facteurs de risque', P(
 'Après la définition, il faut situer le patient. Ainsi, la maladie débute le plus souvent chez l’adolescent et l’adulte jeune, mais elle peut apparaître à tout âge, y compris après 60 ans. De plus, elle résulte de l’interaction entre une susceptibilité génétique, un microbiote intestinal altéré et des facteurs d’environnement. Parmi ces derniers, le tabagisme est un facteur de risque reconnu, qui aggrave aussi l’évolution ; c’est pourquoi l’arrêt du tabac fait partie du traitement.',
 'Par ailleurs, une maladie de Crohn colique étendue et ancienne augmente le risque de cancer colorectal, et une atteinte du grêle expose au cancer du grêle. En outre, la maladie s’accompagne volontiers de ' + w('k50-mei', 'manifestations extra-intestinales') + ', articulaires, cutanées, oculaires ou hépatobiliaires.')
 + trap('Aucune donnée suisse d’incidence vérifiée n’a été retrouvée dans les sources lues ; aucun chiffre n’est donc avancé.', 'Lacune documentaire')
 + key('La maladie touche surtout l’adulte jeune et naît de l’interaction des gènes, du microbiote et de l’environnement. Le tabac augmente le risque et aggrave l’évolution, et les manifestations extra-intestinales sont fréquentes.')
 + src(ECCO))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre les traitements, il faut suivre la cascade immunitaire. D’abord, une barrière épithéliale défaillante laisse passer des antigènes bactériens ; or, chez le sujet prédisposé, l’immunité innée, par exemple par les variants du gène ' + w('k50-nod2', 'NOD2') + ', répond de façon inadaptée. Ensuite, les lymphocytes T auxiliaires de type 1 et 17 s’activent sous l’effet des interleukines 12 et 23, et produisent du ' + w('k50-tnf', 'TNF-α') + ' et d’autres cytokines.',
 'Par conséquent, chaque cible thérapeutique correspond à un maillon de cette cascade. Ainsi, les anti-TNF neutralisent le TNF-α ; l’' + w('k50-d-ustekinumab', 'ustékinumab') + ' bloque la sous-unité p40 commune aux interleukines 12 et 23, et le ' + w('k50-d-risankizumab', 'risankizumab') + ' la sous-unité p19 de l’interleukine 23 ; le ' + w('k50-d-vedolizumab', 'védolizumab') + ' empêche l’intégrine α4β7 de guider les lymphocytes vers l’intestin ; enfin, l’' + w('k50-d-upadacitinib', 'upadacitinib') + ' inhibe la signalisation intracellulaire par JAK-1.')
 + key('Une barrière défaillante et une immunité innée inadaptée (NOD2) activent les lymphocytes Th1/Th17, l’IL-12/23 et le TNF-α, ce qui crée l’inflammation transmurale ; chaque biothérapie cible un maillon de cette chaîne.')
 + src(ECCO))

C.a(4, 'Présentation clinique', P(
 'La présentation dépend donc de la localisation et du phénotype. Ainsi, l’atteinte iléale typique associe une diarrhée chronique, des douleurs de la fosse iliaque droite, parfois une masse, un amaigrissement et une fièvre ; à l’inverse, l’atteinte colique peut donner une diarrhée sanglante qui imite la rectocolite. De plus, la ' + w('k50-perianal', 'maladie périanale') + ' se manifeste par des fissures, des fistules ou des abcès, parfois révélateurs.',
 'Par ailleurs, l’évolution transmurale explique les complications. En effet, une sténose provoque des douleurs postprandiales et un syndrome occlusif, alors qu’une fistule peut relier l’intestin à la peau, à la vessie ou à un autre segment digestif. Enfin, l’examen recherche une dénutrition, une anémie et des manifestations extra-intestinales.')
 + C.img('k50_ulcere.gif', 'Photographie endoscopique d’une muqueuse colique inflammatoire avec un ulcère profond, allongé et sinueux.', 'Ulcère serpigineux du côlon dans une maladie de Crohn, vue d’iléocoloscopie. Les ulcères profonds et discontinus, séparés par une muqueuse d’aspect normal, sont typiques.', credit({'auteur': 'Samir (The Scope)', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:CD_serpiginous_ulcer.jpg'}))
 + key('L’atteinte iléale donne une diarrhée, une douleur de la fosse iliaque droite et un amaigrissement, et l’atteinte colique une diarrhée parfois sanglante. L’atteinte périanale se manifeste par des fistules et des abcès, et une sténose par un syndrome occlusif.')
 + src(DIAG))

C.a(5, 'Démarche diagnostique', P(
 'Devant ce tableau, le diagnostic repose sur un faisceau d’arguments cliniques, biologiques, endoscopiques, histologiques et radiologiques. D’abord, la biologie mesure l’inflammation (CRP) et les carences, et la ' + w('k50-calpro', 'calprotectine fécale') + ' distingue une inflammation intestinale d’un trouble fonctionnel. De plus, une infection doit être exclue par des coprocultures et la recherche de Clostridioides difficile.',
 'Ensuite, l’' + w('k50-ileocolo', 'iléocoloscopie') + ' est l’examen central : en effet, elle visualise l’iléon terminal et le côlon et permet des biopsies étagées, au moins deux par segment, dans l’iléon et dans cinq sites coliques dont le rectum (ECCO-ESGAR 2019). Par ailleurs, l’atteinte du grêle et les complications pénétrantes sont évaluées par l’' + w('k50-ire', 'entéro-IRM') + ' ou par l’échographie intestinale, qui évitent l’irradiation. Enfin, une gastroscopie est discutée en cas de symptômes digestifs hauts.')
 + C.img('k50_irm.gif', 'Coupe coronale d’entéro-IRM : les anses grêles sont distendues par le produit de contraste, et un long segment d’iléon terminal a une paroi épaissie qui se rehausse.', 'Entéro-IRM (technique de Sellink) en séquence T1 avec saturation de graisse après injection : atteinte longue de l’iléon terminal, à paroi épaissie et rehaussée, dans une maladie de Crohn.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Morbus_Crohn_MR-Sellink_T1FSKM_cor.jpg'}))
 + quiz('Quel examen est indispensable pour poser le diagnostic de maladie de Crohn iléale ?',
   [('Scanner abdominal seul', False), ('Iléocoloscopie avec biopsies de l’iléon terminal et du côlon', True), ('Calprotectine fécale seule', False)],
   'La calprotectine oriente, l’imagerie précise l’étendue, mais l’iléocoloscopie avec biopsies étagées est l’examen diagnostique de référence (ECCO-ESGAR 2019).')
 + key('On dose la CRP et la calprotectine et l’on recherche une infection par coprocultures et C. difficile. Ensuite, on fait une iléocoloscopie avec biopsies étagées, puis une entéro-IRM ou une échographie pour le grêle et les complications.')
 + src(DIAG))

C.a(6, 'Classer la maladie : Montréal', P(
 'Le diagnostic posé, la maladie est classée, car le phénotype guide le pronostic et le traitement. Ainsi, la ' + w('k50-montreal', 'classification de Montréal') + ' décrit l’âge au diagnostic (A), la localisation (L) et le comportement (B), avec le suffixe « p » pour une atteinte périanale. Or, le comportement évolue avec le temps : une maladie initialement inflammatoire peut devenir sténosante ou pénétrante.')
 + table(['Axe', 'Catégories'], [
   ['Âge (A)', 'A1 : ≤ 16 ans ; A2 : 17-40 ans ; A3 : > 40 ans'],
   ['Localisation (L)', 'L1 : iléale ; L2 : colique ; L3 : iléocolique ; L4 : tractus digestif haut (ajouté à L1-L3)'],
   ['Comportement (B)', 'B1 : ni sténosant ni pénétrant ; B2 : sténosant ; B3 : pénétrant ; p : atteinte périanale']])
 + P('Par exemple, le patient du début, âgé de 24 ans, avec une atteinte de l’iléon terminal sans sténose, est classé A2 L1 B1 ; en revanche, l’apparition d’une fistule le ferait passer en B3.')
 + key('La classification de Montréal décrit l’âge (A1-A3), la localisation (L1-L4), le comportement (B1-B3) et le suffixe p ; or, le comportement évolue avec le temps vers la sténose ou la pénétration.')
 + src(MTL))

C.a(7, 'Principes de traitement', P(
 'Une fois la maladie classée, le traitement suit des principes généraux. D’abord, l’ECCO recommande une ' + w('k50-mdt', 'équipe multidisciplinaire') + ' et une décision partagée avec le patient (consensus de 97 %). Ensuite, la stratégie ' + w('k50-t2t', '« treat-to-target »') + ', avec contrôle étroit, vise des cibles objectives, comme la normalisation de la calprotectine ou de la CRP, plutôt que les seuls symptômes. De plus, le choix du médicament tient compte de son efficacité, de sa sécurité, des manifestations extra-intestinales, de la maladie périanale, des comorbidités et d’un projet de grossesse.',
 'Par ailleurs, l’ECCO 2024 ne hiérarchise plus les traitements « du conventionnel à l’avancé » ; en effet, chaque médicament est jugé sur ses mérites. Cependant, la distinction entre induction et entretien reste essentielle : certains traitements induisent la rémission sans pouvoir l’entretenir, comme les corticoïdes, et d’autres l’entretiennent sans l’induire, comme les thiopurines.')
 + key('Une équipe multidisciplinaire décide avec le patient et vise des cibles objectives, la calprotectine et la CRP ; l’induction et l’entretien se raisonnent séparément.')
 + src(ECCO, STR))

C.a(8, 'Induire la rémission', P(
 'Dans une poussée légère à modérée limitée à l’iléon ou au côlon ascendant, le ' + w('k50-d-budesonide', 'budésonide') + ' est recommandé pour induire la rémission (recommandation forte) ; ainsi, l’information professionnelle suisse d’Entocort CIR® prévoit 9 mg/j pendant 8 semaines. En revanche, l’ECCO recommande de ne pas utiliser le ' + w('k50-5asa', '5-ASA') + ' dans la maladie de Crohn, ni pour l’induction ni pour l’entretien. De plus, la ' + w('k50-nee', 'nutrition entérale exclusive') + ' peut induire la rémission chez un patient motivé qui veut éviter les corticoïdes (recommandation faible).',
 'Dans une poussée modérée à sévère, les ' + w('k50-cs', 'corticoïdes systémiques') + ' peuvent être utilisés pour l’induction (recommandation faible), mais jamais pour l’entretien. Par conséquent, un traitement d’entretien doit être prévu dès l’induction. Ainsi, l’ECCO recommande fortement, en induction comme en entretien, l’' + w('k50-d-infliximab', 'infliximab') + ', l’adalimumab, l’' + w('k50-d-ustekinumab', 'ustékinumab') + ', le ' + w('k50-d-risankizumab', 'risankizumab') + ', le ' + w('k50-d-vedolizumab', 'védolizumab') + ' et l’' + w('k50-d-upadacitinib', 'upadacitinib') + ' ; de plus, le méthotrexate parentéral et le certolizumab sont des options plus faibles.')
 + alert('Avant tout immunosuppresseur ou biothérapie : dépister la tuberculose latente et les hépatites virales, vérifier les vaccinations, et rechercher un abcès, qui doit être drainé avant l’immunosuppression. L’infliximab est contre-indiqué en cas de tuberculose active, d’infection sévère ou d’insuffisance cardiaque NYHA III-IV.', 'Sécurité d’abord.')
 + quiz('Poussée légère de maladie de Crohn iléale. Quel traitement d’induction ?',
   [('Mésalazine orale', False), ('Budésonide 9 mg/j', True), ('Azathioprine seule', False)],
   'Le budésonide est recommandé pour l’atteinte iléale ou du côlon ascendant légère à modérée ; le 5-ASA n’est pas recommandé, et les thiopurines ne doivent pas servir à l’induction (ECCO 2024).')
 + key('La forme légère iléo-cæcale reçoit du budésonide 9 mg/j, mais pas de 5-ASA. La forme modérée à sévère reçoit des corticoïdes systémiques, pour l’induction seulement, ou un traitement avancé : anti-TNF, ustékinumab, risankizumab, védolizumab ou upadacitinib.')
 + src(ECCO, FI('Entocort CIR®'), FI('Remicade®')))

C.a(9, 'Entretenir la rémission', P(
 'Une fois la rémission obtenue, il faut la maintenir. Ainsi, les ' + w('k50-thiopurines', 'thiopurines') + ' peuvent être utilisées en monothérapie d’entretien (recommandation faible), mais pas en induction (recommandation forte contre). De plus, quand l’infliximab est débuté, l’ECCO recommande fortement de l’associer à une thiopurine, et de maintenir cette association au moins 6 à 12 mois ; en revanche, l’adalimumab est plutôt utilisé en monothérapie chez le patient naïf de biothérapie.',
 'Par ailleurs, tout traitement avancé qui a induit la rémission est en général poursuivi en entretien. En outre, chez le patient naïf de biothérapie, l’adalimumab et l’ustékinumab semblent d’efficacité équivalente en induction comme en entretien (recommandation faible). Enfin, la réponse est contrôlée par la calprotectine, la CRP et, selon le cas, l’endoscopie ou l’imagerie, conformément à la stratégie « treat-to-target ».')
 + key('Les thiopurines servent à l’entretien, mais pas à l’induction. L’infliximab s’associe à une thiopurine pendant ≥ 6-12 mois, alors que l’adalimumab se donne seul. En entretien, on poursuit le traitement qui a induit la rémission.')
 + src(ECCO))

C.a(10, 'Complications et chirurgie', P(
 'Malgré le traitement médical, les complications transmurales peuvent imposer un geste. Ainsi, un abcès est drainé, de préférence par voie percutanée, avant toute immunosuppression ; de plus, une sténose fibreuse symptomatique relève d’une dilatation endoscopique ou d’une résection. Par ailleurs, l’' + w('k50-resection', 'iléocæcectomie') + ' est une option à discuter tôt dans une maladie iléale limitée, en concertation multidisciplinaire.',
 'En outre, la maladie périanale fistulisante associe drainage chirurgical, souvent par séton, et traitement médical, notamment par anti-TNF ; en effet, l’infliximab est autorisé en Suisse dans la maladie de Crohn fistulisante sévère. Enfin, la surveillance endoscopique du cancer colorectal s’impose dans les formes coliques étendues et anciennes.')
 + key('On draine l’abcès avant d’immunosupprimer, sinon le sepsis s’aggrave. La sténose fibreuse se dilate ou se résèque, et la fistule périanale reçoit un séton et un anti-TNF. Une colite étendue impose la surveillance du cancer colorectal.')
 + C.pareto('pareto-k50-clinique', 'Maladie de Crohn', ['k50-1', 'k50-5', 'k50-6', 'k50-7', 'k50-8', 'k50-9', 'k50-10'],
     ['Transmurale, segmentaire, de la bouche à l’anus.',
      'Iléocoloscopie avec biopsies étagées ; entéro-IRM.',
      'Montréal : A, L, B, p.',
      'La stratégie « treat-to-target » vise la normalisation de la calprotectine et de la CRP.',
      'La forme légère iléale reçoit du budésonide, mais pas de 5-ASA.',
      'La forme modérée à sévère reçoit une biothérapie ou de l’upadacitinib, et les corticoïdes ne servent qu’à l’induction.',
      'Abcès drainé avant immunosuppression.'])
 + src(ECCO))

C.a(11, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons le patient du début. L’iléocoloscopie montre des ulcères de l’iléon terminal sur 15 cm, avec un côlon normal ; de plus, les biopsies révèlent une inflammation chronique avec un granulome non nécrosant, et l’entéro-IRM ne montre ni sténose ni fistule. Il s’agit donc d’une maladie de Crohn A2 L1 B1.',
 'Dès lors, la conduite associe trois mesures. D’abord, l’arrêt du tabac est fortement conseillé. Ensuite, la poussée étant modérée, le budésonide 9 mg/j est débuté, et un traitement d’entretien est discuté en équipe, car l’amaigrissement et la CRP élevée font craindre une évolution défavorable. Enfin, la calprotectine est contrôlée pour vérifier que la cible est atteinte.')
 + key('Diagnostic (endoscopie, histologie, IRM) → Montréal → induction adaptée à la gravité → entretien → contrôle objectif ; arrêt du tabac.')
 + src(ECCO, MTL))

C.a(12, 'Critères formels et paramètres clés', alert(
 '<p>Le <b>diagnostic</b> repose sur un faisceau d’arguments cliniques, biologiques, endoscopiques, histologiques et radiologiques, car aucun critère isolé ne suffit. La classification de <b>Montréal</b> distingue l’âge (A1 ≤ 16 ans, A2 17-40, A3 > 40), la localisation (L1 iléale, L2 colique, L3 iléocolique, L4 haute) et le comportement (B1, B2 sténosant, B3 pénétrant, p périanal). Dans les essais, la <b>rémission clinique</b> correspond à un CDAI < 150.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Le budésonide se donne à 9 mg/j pendant 8 semaines, puis à 6 mg/j (FI). L’infliximab se perfuse à 5 mg/kg aux semaines 0, 2 et 6, puis toutes les 8 semaines. L’adalimumab se donne à 160 mg, puis 80 mg à 2 semaines, puis 40 mg toutes les 2 semaines. L’ustékinumab se donne à environ 6 mg/kg IV, puis 90 mg SC toutes les 8 semaines. Le védolizumab se perfuse à 300 mg IV aux semaines 0, 2 et 6, le risankizumab à 600 mg IV aux semaines 0, 4 et 8, et l’upadacitinib se prend à 45 mg/j pendant 12 semaines.</div>'
 + src(ECCO, MTL, FI('Entocort CIR®')))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Place'], [
   ['Inflammation intestinale ?', w('k50-calpro', 'Calprotectine fécale') + ', CRP', 'Premier recours'],
   ['Infection ?', 'Coprocultures, C. difficile', 'Toute diarrhée'],
   ['Diagnostic et étendue colique ?', w('k50-ileocolo', 'Iléocoloscopie') + ' et biopsies étagées', 'Examen central'],
   ['Grêle, sténose, fistule, abcès ?', w('k50-ire', 'Entéro-IRM') + ' ou échographie intestinale', 'Bilan initial et suivi'],
   ['Atteinte haute ?', 'Gastroscopie', 'Symptômes hauts'],
   ['Avant biothérapie ?', 'Tuberculose latente, hépatites B et C, VIH', 'Systématique']])
 + P('Le tableau se lit de haut en bas : ainsi, la calprotectine trie les patients, puis l’endoscopie et l’imagerie établissent le diagnostic et la carte des lésions.')
 + key('On dose la calprotectine et la CRP, on fait des coprocultures, une iléocoloscopie avec biopsies et une entéro-IRM ou une échographie ; avant une biothérapie, on fait un bilan infectieux.')
 + src(DIAG))

C.e(2, 'Lire les biopsies', P(
 'L’histologie apporte des arguments, mais rarement une preuve absolue. Ainsi, une inflammation chronique focale, des distorsions architecturales et un ' + w('k50-granulome', 'granulome épithélioïde non nécrosant') + ' sont évocateurs ; or, le granulome manque dans une grande partie des biopsies. Par conséquent, son absence n’exclut pas la maladie, et sa présence impose d’éliminer d’autres granulomatoses, notamment la tuberculose intestinale.')
 + C.img('k50_granulome.gif', 'Coupe histologique de muqueuse colique : au centre, un amas arrondi de grandes cellules à cytoplasme rose pâle, sans nécrose centrale.', 'Granulome non nécrosant de la muqueuse colique dans une maladie de Crohn, coloration hématoxyline-éosine : amas d’histiocytes épithélioïdes à cytoplasme éosinophile abondant.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_granuloma_of_colonic_mucosa.jpg'}))
 + key('Inflammation chronique focale + granulome non nécrosant : évocateur ; absence de granulome : n’exclut pas ; penser à la tuberculose intestinale.')
 + C.pareto('pareto-k50-examens', 'Examens', ['k50-e-1', 'k50-e-2'],
     ['La calprotectine distingue une inflammation d’un trouble fonctionnel.',
      'L’iléocoloscopie prélève ≥ 2 biopsies par segment, dans l’iléon et dans 5 sites coliques.',
      'Entéro-IRM : grêle, sténoses, fistules.',
      'Granulome non nécrosant : évocateur, inconstant.'])
 + src(DIAG))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : l’iléon terminal et la paroi intestinale', P(
 'L’iléon terminal, riche en tissu lymphoïde (plaques de Peyer), est le site le plus fréquent de la maladie ; ainsi, la douleur se projette dans la fosse iliaque droite. Or, la paroi intestinale comporte muqueuse, sous-muqueuse, musculeuse et séreuse. Par conséquent, une inflammation transmurale peut traverser toute la paroi et créer une fistule vers un organe voisin ou la peau.')
 + key('C’est pourquoi l’imagerie en coupe, qui voit toute la paroi et le mésentère, complète l’endoscopie, qui ne voit que la muqueuse.', 'Science → examen.'))
C.s('histo', 'Histologie', 'Histologie : granulome et inflammation transmurale', P(
 'Le granulome épithélioïde est un amas d’histiocytes activés, parfois avec des cellules géantes, sans nécrose caséeuse ; ainsi, il traduit une réponse immunitaire cellulaire. De plus, l’inflammation de la maladie de Crohn s’étend en profondeur sous forme d’agrégats lymphoïdes transmuraux. À l’inverse, la rectocolite reste muqueuse, avec des abcès cryptiques et une distorsion diffuse.')
 + key('Granulome non nécrosant et agrégats transmuraux : Crohn ; inflammation muqueuse continue : rectocolite.', 'Science → diagnostic.'))
C.s('immuno', 'Immunologie', 'Immunologie : de l’IL-23 au TNF-α', P(
 'Les cellules dendritiques activées sécrètent de l’interleukine 12, qui oriente vers les lymphocytes Th1, et de l’interleukine 23, qui entretient les Th17 ; ensuite, ces lymphocytes produisent de l’interféron γ, de l’interleukine 17 et du TNF-α. Par ailleurs, l’intégrine α4β7 des lymphocytes se lie à la molécule MAdCAM-1 des vaisseaux intestinaux, ce qui les fait migrer dans la muqueuse.')
 + key('C’est pourquoi anti-TNF, anti-IL-12/23 (p40), anti-IL-23 (p19) et anti-α4β7 sont efficaces : ils coupent la cascade à des niveaux différents.', 'Science → traitement.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : thiopurines et TPMT', P(
 'L’azathioprine est transformée en 6-mercaptopurine, puis en nucléotides thioguanine actifs ; or, la ' + w('k50-tpmt', 'thiopurine méthyltransférase') + ' détourne une partie de ce métabolisme. Ainsi, un déficit en TPMT, ou un variant du gène NUDT15, accumule les métabolites actifs et expose à une aplasie médullaire rapide, selon l’information professionnelle d’Imurek®. Par conséquent, la mesure de l’activité TPMT ou le génotypage avant traitement, puis la surveillance de la formule sanguine, sont nécessaires.')
 + key('Déficit TPMT ou variant NUDT15 : toxicité médullaire ; tester avant, surveiller la formule sanguine pendant.', 'Science → sécurité.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, leur place dépend de la gravité et du moment, induction ou entretien.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Corticoïde à action locale', 'Budésonide (Entocort CIR®)', 'Induction, forme iléo-cæcale légère à modérée', w('k50-d-budesonide', 'Monographie')],
   ['Corticoïdes systémiques', 'Prednisone, prednisolone', 'Induction seule, forme modérée à sévère', w('k50-cs', 'Fiche')],
   ['Thiopurines', 'Azathioprine (Imurek®)', 'Entretien ; association à l’infliximab', w('k50-thiopurines', 'Fiche')],
   ['Anti-TNF', 'Infliximab, adalimumab', 'Induction et entretien', w('k50-d-infliximab', 'Monographie')],
   ['Anti-interleukines', 'Ustékinumab, risankizumab', 'Induction et entretien', w('k50-d-ustekinumab', 'Fiche')],
   ['Anti-intégrine', 'Védolizumab', 'Induction et entretien', w('k50-d-vedolizumab', 'Fiche')],
   ['Inhibiteur de JAK', 'Upadacitinib', 'Induction et entretien', w('k50-d-upadacitinib', 'Fiche')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, un médicament d’induction seule doit toujours être relayé par un traitement d’entretien.')
 + key('Le budésonide et les corticoïdes servent à l’induction, les thiopurines à l’entretien, et les biothérapies et l’upadacitinib aux deux ; on ne donne pas de 5-ASA.')
 + src(ECCO))

C.p(2, 'Doses et statut réglementaire', P('Les éléments suivants proviennent de l’ECCO 2024 et des informations professionnelles suisses ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Schéma', 'Source'], [
   ['Budésonide (Entocort CIR®)', '9 mg/j 8 semaines ; entretien 6 mg/j ; décroissance progressive à l’arrêt', 'FI Entocort CIR®'],
   ['Infliximab (Remicade®)', '5 mg/kg IV semaines 0, 2, 6, puis toutes les 8 semaines', 'ECCO 2024 ; FI Remicade®'],
   ['Adalimumab', '160 mg SC, 80 mg à 2 semaines, puis 40 mg toutes les 2 semaines', 'ECCO 2024'],
   ['Ustékinumab', '≈ 6 mg/kg IV, puis 90 mg SC à 8 semaines et toutes les 8 semaines', 'ECCO 2024'],
   ['Védolizumab', '300 mg IV semaines 0, 2, 6 (dose supplémentaire à 10 semaines si besoin), puis toutes les 8 semaines', 'ECCO 2024'],
   ['Risankizumab', '600 mg IV semaines 0, 4, 8 ; entretien SC (dose : TODO, FI Skyrizi® non lue)', 'ECCO 2024'],
   ['Upadacitinib', '45 mg/j 12 semaines ; entretien (dose : TODO, FI Rinvoq® non lue)', 'ECCO 2024']])
 + trap('L’information professionnelle suisse d’Imurek® (azathioprine) ne mentionne pas les maladies inflammatoires de l’intestin parmi ses indications : son usage dans la maladie de Crohn, recommandé par l’ECCO en entretien, est donc hors indication en Suisse. À valider à l’audit.', 'Point à valider')
 + P('Par exemple, chez le patient du début, si un anti-TNF est choisi, l’infliximab serait associé à l’azathioprine pendant au moins 6 à 12 mois, après information sur ce statut hors indication et dépistage de la tuberculose.')
 + key('Le budésonide se donne à 9 mg/j ; l’infliximab à 5 mg/kg (semaines 0, 2 et 6, puis toutes les 8 semaines) avec une thiopurine ; l’adalimumab à 160, 80, puis 40 mg. L’azathioprine est hors indication en Suisse.')
 + src(ECCO, FI('Entocort CIR®'), FI('Remicade®'), FI('Imurek®')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'Les biothérapies et les immunosuppresseurs exposent aux infections, dont la réactivation tuberculeuse et l’hépatite B ; c’est pourquoi le dépistage précède le traitement. De plus, l’infliximab peut provoquer des réactions à la perfusion, et il est contre-indiqué en cas d’insuffisance cardiaque modérée ou sévère (NYHA III-IV).', 'Sécurité.')
 + P('Par ailleurs, les thiopurines exigent une formule sanguine régulière, en raison du risque de myélotoxicité, notamment en cas de déficit en TPMT ou de variant NUDT15 ; en outre, elles augmentent le risque de cancers cutanés non mélaniques et de lymphome. Enfin, le budésonide, malgré son fort premier passage hépatique, garde des effets corticoïdes, d’où une durée limitée et une décroissance progressive.')
 + key('On dépiste les infections avant le traitement et l’on surveille les réactions à la perfusion. Une insuffisance cardiaque NYHA III-IV contre-indique l’infliximab. Sous thiopurines, on contrôle la formule sanguine et l’on conseille une protection solaire, car elles augmentent le risque de cancer cutané.')
 + C.pareto('pareto-k50-pharma', 'Pharmacologie', ['k50-p-1', 'k50-p-2', 'k50-p-3'],
     ['On ne donne pas de 5-ASA dans la maladie de Crohn.',
      'Les corticoïdes servent à l’induction, jamais à l’entretien.',
      'Infliximab + thiopurine ≥ 6-12 mois.',
      'On dépiste la tuberculose et l’hépatite B avant une biothérapie.',
      'On teste la TPMT et NUDT15 avant l’azathioprine.'])
 + src(ECCO, FI('Remicade®'), FI('Imurek®')))

# ---------------- Fenêtres
L = lab
C.pop('k50-calpro', 'Calprotectine fécale', L(('Nature', 'Protéine des polynucléaires neutrophiles, dosée dans les selles.'), ('Usage', 'Distinguer inflammation intestinale et trouble fonctionnel ; suivre la réponse (« treat-to-target »).'), ('Limite', 'Elle s’élève aussi dans les infections, sous AINS et dans les néoplasies ; elle n’est donc pas spécifique.')) + src(DIAG, ECCO))
C.pop('k50-ileocolo', 'Iléocoloscopie avec biopsies', L(('Technique', 'Exploration du côlon et de l’iléon terminal.'), ('Biopsies (ECCO-ESGAR 2019)', 'On prélève au moins 2 biopsies par segment, dans l’iléon et dans 5 sites coliques dont le rectum.'), ('Signes', 'Elle montre des ulcères aphtoïdes ou profonds et discontinus, un aspect pavimenteux et des sténoses.')) + src(DIAG) + C.img('k50_ulcere.gif', 'Endoscopie : ulcère colique profond, allongé et sinueux.', 'L’ulcère est profond et entouré de muqueuse moins atteinte, car l’inflammation est discontinue et transmurale ; c’est l’aspect typique de la maladie de Crohn.', credit({'auteur': 'Samir (The Scope)', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:CD_serpiginous_ulcer.jpg'})))
C.pop('k50-ire', 'Entéro-IRM', L(('Usage', 'Elle précise l’étendue de l’atteinte du grêle et recherche les sténoses, les fistules et les abcès.'), ('Avantage', 'Pas d’irradiation chez des patients jeunes, souvent réexaminés.'), ('Alternative', 'L’échographie intestinale peut la remplacer.')) + src(DIAG) + C.img('k50_irm.gif', 'Entéro-IRM coronale : long segment d’iléon terminal épaissi et rehaussé.', 'La paroi iléale épaissie se rehausse, car elle est inflammatoire et hypervascularisée ; l’IRM mesure ainsi la longueur atteinte sans irradier.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Morbus_Crohn_MR-Sellink_T1FSKM_cor.jpg'})))
C.pop('k50-montreal', 'Classification de Montréal', L(('Âge', 'A1 ≤ 16 ans ; A2 17-40 ans ; A3 > 40 ans.'), ('Localisation', 'L1 désigne l’atteinte iléale, L2 colique, L3 iléocolique et L4 haute.'), ('Comportement', 'B1 désigne la forme inflammatoire, B2 sténosante et B3 pénétrante ; le suffixe p signale une atteinte périanale.')) + src(MTL))
C.pop('k50-transmurale', 'Inflammation transmurale', L(('Définition', 'L’inflammation touche toute l’épaisseur de la paroi, de la muqueuse à la séreuse.'), ('Conséquences', 'C’est pourquoi elle provoque des sténoses, des fistules et des abcès.')) + src(DIAG))
C.pop('k50-mei', 'Manifestations extra-intestinales', L(('Exemples', 'Les arthrites périphériques et axiales, l’érythème noueux, le pyoderma gangrenosum, l’uvéite, l’épisclérite et la cholangite sclérosante primitive en sont des exemples.'), ('Portée', 'Elles influencent le choix du traitement (ECCO 2024).')) + src(ECCO))
C.pop('k50-perianal', 'Maladie périanale', L(('Lésions', 'Elle comprend des fissures, des fistules, des abcès et une sténose anale.'), ('Classification', 'Le suffixe « p » de Montréal la signale.'), ('Traitement', 'On draine par un séton et l’on donne un anti-TNF, car le drainage seul ne ferme pas la fistule.')) + src(MTL, ECCO))
C.pop('k50-nod2', 'Gène NOD2', L(('Rôle', 'Ce récepteur intracellulaire reconnaît des fragments bactériens et participe à l’immunité innée.'), ('Lien', 'Variants associés à la maladie de Crohn iléale.')))
C.pop('k50-tnf', 'TNF-α', L(('Nature', 'Cytokine pro-inflammatoire majeure.'), ('Cible', 'Infliximab, adalimumab, certolizumab.')) + src(ECCO))
C.pop('k50-t2t', 'Stratégie « treat-to-target »', L(('Principe', 'Fixer une cible objective, la mesurer régulièrement et ajuster le traitement si elle n’est pas atteinte.'), ('Cibles', 'On vise la normalisation de la calprotectine ou de la CRP et la cicatrisation endoscopique (STRIDE-II).'), ('Niveau', 'Recommandée par l’ECCO 2024 (consensus 97 %).')) + src(ECCO, STR))
C.pop('k50-mdt', 'Équipe multidisciplinaire', L(('Membres', 'Gastroentérologue, chirurgien, radiologue, pathologiste, infirmière spécialisée, diététicien, psychologue.'), ('Niveau', 'Recommandée par l’ECCO 2024 (consensus 97 %).')) + src(ECCO))
C.pop('k50-5asa', '5-ASA (mésalazine)', L(('ECCO 2024', 'Non recommandé pour l’induction (recommandation forte) ni pour l’entretien (recommandation forte).'), ('Remarque', 'La mésalazine est efficace dans la rectocolite hémorragique, mais pas dans la maladie de Crohn.')) + src(ECCO))
C.pop('k50-nee', 'Nutrition entérale exclusive', L(('Place', 'Induction chez le patient motivé, avec soutien diététique, qui veut éviter les corticoïdes (recommandation faible).')) + src(ECCO))
C.pop('k50-cs', 'Corticoïdes systémiques', L(('Place', 'Ils induisent la rémission de la forme modérée à sévère (recommandation faible).'), ('Jamais', 'En entretien.'), ('Risques', 'Infections, ostéoporose, diabète, dépendance aux corticoïdes.')) + src(ECCO))
C.pop('k50-thiopurines', 'Thiopurines', L(('Molécules', 'Ce sont l’azathioprine et la 6-mercaptopurine.'), ('Place', 'Elles servent à l’entretien (recommandation faible), mais pas à l’induction (recommandation forte contre), car elles agissent en plusieurs mois ; associées à l’infliximab, elles se donnent pendant ≥ 6-12 mois.'), ('Avant', 'On teste la TPMT ou NUDT15 avant de les prescrire.')) + src(ECCO, FI('Imurek®')))
C.pop('k50-tpmt', 'Thiopurine méthyltransférase (TPMT)', L(('Rôle', 'Enzyme qui inactive une partie des thiopurines.'), ('Déficit', 'Un déficit expose à une aplasie médullaire rapide sous azathioprine (FI Imurek®).'), ('Conduite', 'On mesure l’activité ou le génotype avant le traitement, ainsi que NUDT15.')) + src(FI('Imurek®')))
C.pop('k50-granulome', 'Granulome épithélioïde non nécrosant', L(('Aspect', 'C’est un amas d’histiocytes épithélioïdes sans nécrose caséeuse.'), ('Valeur', 'Évocateur, inconstant ; éliminer tuberculose et autres granulomatoses.')) + src(DIAG) + C.img('k50_granulome.gif', 'Histologie : amas arrondi d’histiocytes épithélioïdes sans nécrose centrale.', 'L’absence de nécrose caséeuse distingue ce granulome de celui de la tuberculose ; cependant, il manque dans une grande partie des biopsies.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Histopathology_of_granuloma_of_colonic_mucosa.jpg'})))
C.pop('k50-resection', 'Iléocæcectomie', L(('Indication', 'On la propose dans une maladie iléale limitée, une sténose fibreuse ou un échec médical, et on la discute tôt en équipe.'), ('Suite', 'On prévient ensuite la récidive postopératoire et on la contrôle par endoscopie.')) + src(ECCO))
C.pop('k50-d-budesonide', 'Budésonide (Entocort CIR®)', L(('Indication suisse', 'Induction et maintien de la rémission des poussées légères à modérées avec atteinte de l’iléon terminal et du côlon proximal.'), ('Dose', 'On donne 9 mg/j pendant 8 semaines, puis 6 mg/j en entretien, avec une réduction progressive.'), ('ECCO 2024', 'L’ECCO le recommande fortement pour induire la rémission d’une atteinte iléale ou du côlon ascendant, car il agit localement à cet endroit.')) + src(FI('Entocort CIR®'), ECCO))
C.pop('k50-d-infliximab', 'Infliximab (Remicade®)', L(('Indication suisse', 'Il est autorisé dans la maladie de Crohn active modérée à sévère après échec du traitement conventionnel et dans la forme fistulisante sévère.'), ('Schéma', 'On perfuse 5 mg/kg IV aux semaines 0, 2 et 6, puis toutes les 8 semaines.'), ('Contre-indications', 'Tuberculose ou infection sévère, insuffisance cardiaque NYHA III-IV.')) + src(FI('Remicade®'), ECCO))
C.pop('k50-d-ustekinumab', 'Ustékinumab', L(('Cible', 'Sous-unité p40 des interleukines 12 et 23.'), ('Schéma (ECCO 2024)', '≈ 6 mg/kg IV, puis 90 mg SC toutes les 8 semaines.'), ('Place', 'Il sert à l’induction et à l’entretien (recommandation forte).')) + src(ECCO))
C.pop('k50-d-risankizumab', 'Risankizumab', L(('Cible', 'Il cible la sous-unité p19 de l’interleukine 23.'), ('Induction (ECCO 2024)', '600 mg IV semaines 0, 4, 8.'), ('Place', 'Il sert à l’induction et à l’entretien (recommandation forte).')) + src(ECCO))
C.pop('k50-d-vedolizumab', 'Védolizumab', L(('Cible', 'Il cible l’intégrine α4β7 et bloque ainsi la migration intestinale des lymphocytes.'), ('Schéma', 'On perfuse 300 mg IV aux semaines 0, 2 et 6, puis toutes les 8 semaines (ou 108 mg SC toutes les 2 semaines).'), ('Place', 'Il sert à l’induction et à l’entretien (recommandation forte).')) + src(ECCO))
C.pop('k50-d-upadacitinib', 'Upadacitinib', L(('Cible', 'Janus kinase 1 (inhibiteur oral).'), ('Induction (ECCO 2024)', 'On donne 45 mg/j pendant 12 semaines.'), ('Place', 'Il sert à l’induction et à l’entretien (recommandation forte).')) + src(ECCO))

C.termes = [
 (r'calprotectine', 'k50-calpro'), (r'iléocoloscopie', 'k50-ileocolo'), (r'entéro-IRM', 'k50-ire'), (r'Montréal', 'k50-montreal'),
 (r'transmurale', 'k50-transmurale'), (r'manifestations extra-intestinales', 'k50-mei'), (r'maladie périanale', 'k50-perianal'),
 (r'NOD2', 'k50-nod2'), (r'TNF-α', 'k50-tnf'), (r'« treat-to-target »', 'k50-t2t'), (r'5-ASA', 'k50-5asa'), (r'nutrition entérale exclusive', 'k50-nee'),
 (r'corticoïdes systémiques', 'k50-cs'), (r'thiopurines?', 'k50-thiopurines'), (r'azathioprine', 'k50-thiopurines'), (r'TPMT', 'k50-tpmt'),
 (r'granulome', 'k50-granulome'), (r'iléocæcectomie', 'k50-resection'), (r'budésonide', 'k50-d-budesonide'), (r'infliximab', 'k50-d-infliximab'),
 (r'ustékinumab', 'k50-d-ustekinumab'), (r'risankizumab', 'k50-d-risankizumab'), (r'védolizumab', 'k50-d-vedolizumab'), (r'upadacitinib', 'k50-d-upadacitinib'),
]

C.write()
