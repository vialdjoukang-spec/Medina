import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K21', 'Reflux gastro-œsophagien et œsophage de Barrett',
    'K21 — Reflux gastro-œsophagien · leçon étendue à K22.7 — Œsophage de Barrett · CIM-10-GM 2024 · Tube digestif',
    'Adulte · reflux, œsophagite, complications et Barrett · rédaction du 09.10.2026 · référentiels S2k DGVS 2023, consensus de Lyon 2.0 (2024), ESGE 2023, informations professionnelles suisses',
    'Pharmacologie du reflux')
w = C.w
S2K = ('Madisch A. et al., S2k-Leitlinie Gastroösophageale Refluxkrankheit und eosinophile Ösophagitis (DGVS), Z Gastroenterol 2023;61:862-933', 'https://register.awmf.org/de/leitlinien/detail/021-013')
LYON = ('Gyawali C. P. et al., Updates to the modern diagnosis of GERD: Lyon consensus 2.0, Gut 2024;73:361-371', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10846564/')
BAR = ('Weusten B. L. A. M. et al., ESGE, diagnostic et prise en charge de l’œsophage de Barrett, Endoscopy 2023;55:1124-1146', 'https://www.esge.com/assets/downloads/pdfs/guidelines/2023_a-2176-2440.pdf')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS via AmiKo), consultée le 09.10.2026', 'https://amiko.oddb.org/fr')

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 52 ans, en surpoids, se plaint depuis des années de brûlures rétrosternales après les repas et en position couchée. Il prend « de temps en temps » un antiacide. Or, depuis deux mois, il a l’impression que les aliments solides « restent bloqués ». <b>La question n’est donc plus seulement de soulager le reflux, mais de savoir si une complication est apparue.</b>',
 'Pour répondre à cette question, le médecin doit savoir : définir le reflux pathologique ; reconnaître les symptômes typiques et les ' + w('k21-alarme', 'signes d’alarme') + ' ; décider quand un traitement d’épreuve suffit et quand l’endoscopie s’impose ; interpréter la ' + w('k21-los-angeles', 'classification de Los Angeles') + ' et les seuils de la pH-métrie ; prescrire un IPP à la bonne dose et pour la bonne durée, puis l’arrêter quand il n’est plus utile ; enfin, reconnaître et surveiller un ' + w('k21-barrett', 'œsophage de Barrett') + '.')
 + key(w('k21-rgo-def', 'reflux gastro-œsophagien pathologique (définition)') + ' ; ' + w('k21-preuve', 'preuve objective (endoscopie ou pH-métrie)') + '.', 'Point de départ.'))

C.a(1, 'Définition et classification', P(
 'Le reflux du contenu gastrique dans l’œsophage est physiologique en petite quantité, surtout après les repas. En revanche, selon la S2k 2023 (énoncé 1.1), on parle de <b>maladie de reflux gastro-œsophagien</b> lorsque ce reflux provoque des symptômes gênants ou des lésions de l’œsophage. Cette définition repose donc sur la gêne ou sur la lésion, et non sur la simple présence de reflux.',
 'À partir de cette définition, on distingue plusieurs formes. L’' + w('k21-oesophagite', 'œsophagite érosive') + ' comporte des pertes de substance visibles à l’endoscopie. À l’inverse, la ' + w('k21-nerd', 'maladie de reflux non érosive') + ' associe des symptômes typiques et un reflux pathologique, sans lésion visible. Enfin, les complications sont la sténose peptique, l’œsophage de Barrett et l’adénocarcinome.')
 + table(['Forme', 'Critère', 'Conséquence'], [
   ['Œsophagite érosive', 'Lésions endoscopiques, gradées A à D (Los Angeles)', 'Grades C et D : traitement continu'],
   ['Maladie non érosive', 'Symptômes et reflux pathologique en pH-métrie, endoscopie normale', 'Traitement guidé par les symptômes'],
   ['Hypersensibilité au reflux', 'Exposition acide normale, mais symptômes associés aux épisodes de reflux', 'Prise en charge d’un trouble fonctionnel'],
   ['Complications', 'Sténose peptique, Barrett, adénocarcinome', 'Endoscopie, biopsies, surveillance']])
 + P('Le tableau se lit par la colonne de droite : en effet, la forme décide de la durée du traitement et de la surveillance.')
 + key('Le reflux devient une maladie lorsqu’il gêne ou lèse. La forme (érosive, non érosive, hypersensibilité, complication) commande la suite.')
 + src(S2K, LYON))

C.a(2, 'Épidémiologie et facteurs de risque', P(
 'Après la définition, la fréquence situe l’enjeu. Ainsi, selon la S2k 2023, la prévalence du reflux pathologique atteint 15 à 25 % dans les pays à haut niveau de vie, contre environ 10 % dans les pays plus pauvres, et elle augmente. Les facteurs de risque établis sont l’' + w('k21-obesite', 'indice de masse corporelle élevé') + ', le tabac, une prédisposition génétique et la ' + w('k21-hernie', 'hernie hiatale') + '. À l’inverse, l’infection à Helicobacter pylori semble diminuer ce risque.',
 'Par ailleurs, l’œsophage de Barrett touche environ 2 % des personnes de 50 ans et plus qui ont des symptômes de reflux, d’après une étude de dépistage citée par l’ESGE 2023. Toutefois, son risque de progression vers une dysplasie de haut grade ou un adénocarcinome reste faible : 0,3 à 0,8 % par an.')
 + trap('Aucune donnée nationale suisse de prévalence n’a été retrouvée lors de la rédaction ; les chiffres cités sont européens et attribués.', 'Lacune documentaire')
 + key('Le reflux est fréquent (15 à 25 %), surtout en cas de surpoids et de hernie hiatale ; un Barrett touche environ 2 % des patients symptomatiques de plus de 50 ans, mais il progresse peu.')
 + src(S2K, BAR))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre ces facteurs, il faut décrire la barrière anti-reflux. Normalement, la ' + w('k21-jog', 'jonction œsogastrique') + ' est fermée par le sphincter inférieur de l’œsophage, renforcé par le diaphragme crural. Or, cette barrière s’ouvre de façon transitoire après les repas : ce sont les relaxations transitoires du sphincter, principal mécanisme du reflux. De plus, la ' + w('k21-hernie', 'hernie hiatale') + ' dissocie le sphincter et le diaphragme, si bien que la barrière s’affaiblit.',
 'Ensuite, la gravité dépend de l’agression et de la clairance. En effet, l’acide et la pepsine lèsent l’épithélium malpighien ; le surpoids augmente la pression abdominale ; enfin, une motricité œsophagienne faible ralentit l’évacuation du reflux. Par conséquent, l’exposition acide se prolonge et les lésions apparaissent.',
 'À long terme, l’agression chronique peut transformer l’épithélium. Ainsi, l’épithélium malpighien est remplacé par un ' + w('k21-metaplasie', 'épithélium cylindrique de type intestinal') + ' : c’est l’œsophage de Barrett, qui peut évoluer vers la dysplasie puis l’adénocarcinome.')
 + C.img('k21_oesophagite_histologie.gif', 'Coupe histologique d’épithélium malpighien œsophagien : hyperplasie de la couche basale et allongement des papilles.', 'Œsophagite par reflux, coloration hématoxyline-éosine. L’hyperplasie basale et l’allongement des papilles traduisent la régénération d’un épithélium agressé.', credit({'auteur': 'Nephron', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Gastroesophageal_reflux_disease_--_intermed_mag.jpg'}))
 + key('Les relaxations transitoires du sphincter, la hernie hiatale et le surpoids ouvrent la barrière, et une clairance faible prolonge l’agression.')
 + src(S2K))

C.a(4, 'Anamnèse et symptômes', P(
 'La démarche commence donc par l’interrogatoire. Les symptômes typiques sont le ' + w('k21-pyrosis', 'pyrosis') + ', une brûlure rétrosternale ascendante, et les ' + w('k21-regurgitation', 'régurgitations') + ' acides. Par ailleurs, il existe des manifestations extra-œsophagiennes : toux chronique, enrouement, asthme, érosions dentaires. Cependant, leur lien avec le reflux est plus difficile à établir.',
 'L’interrogatoire recherche ensuite les ' + w('k21-alarme', 'signes d’alarme') + ', car ils imposent une endoscopie immédiate. De plus, il précise l’ancienneté des symptômes, le poids, le tabac, l’alcool, les médicaments et les traitements déjà essayés.')
 + trap('Attribuer une douleur thoracique au reflux sans avoir exclu une origine cardiaque : la cause coronarienne est éliminée en premier.', 'Piège')
 + key('Pyrosis et régurgitations sont typiques ; dysphagie, odynophagie, saignement, anémie ferriprive, perte de poids, vomissements répétés et antécédents familiaux de cancer digestif sont des signes d’alarme.')
 + src(S2K))

C.a(5, 'Démarche diagnostique', P(
 'Au terme de l’interrogatoire, deux situations se présentent. D’une part, chez un patient aux symptômes typiques, sans signe d’alarme ni facteur de risque de complication, la S2k 2023 propose un ' + w('k21-epreuve', 'traitement d’épreuve par IPP en dose standard') + ' (recommandation 2.3). D’autre part, en présence de signes d’alarme ou en cas d’échec du traitement d’épreuve, une œsogastroduodénoscopie est indiquée (recommandation 1.5).',
 'Il faut cependant savoir que la réponse aux IPP ne prouve pas le diagnostic (énoncé 1.3). En effet, aucun examen n’est un gold standard ; la preuve est apportée par l’endoscopie ou par la ' + w('k21-phmetrie', 'pH-métrie') + '. De plus, en cas de symptômes anciens de plusieurs années, une endoscopie est conseillée pour dépister un œsophage de Barrett (recommandation 1.6).')
 + quiz('Une femme de 38 ans a un pyrosis typique depuis 3 mois, sans signe d’alarme. Quelle conduite ?',
   [('Gastroscopie d’emblée', False), ('IPP en dose standard pendant 4 à 8 semaines', True), ('pH-métrie avant tout traitement', False)],
   'En l’absence de signe d’alarme et de facteur de risque de complication, la S2k 2023 recommande un traitement d’épreuve par IPP ; l’endoscopie est réservée à l’échec ou aux signes d’alarme.')
 + key('Des symptômes typiques sans alarme justifient un traitement d’épreuve, alors qu’une alarme ou un échec imposent une endoscopie. La réponse aux IPP ne prouve rien, car l’effet placebo et les autres causes acido-sensibles répondent aussi.')
 + src(S2K))

C.a(6, 'Preuve objective : quand le reflux est-il établi ?', P(
 'Lorsque le diagnostic doit être prouvé, deux sources européennes récentes divergent sur un point. D’un côté, la S2k 2023 retient comme preuve concluante une œsophagite de grade C ou D, un Barrett de plus de 1 cm confirmé par histologie ou une sténose peptique (énoncé 1.2). De l’autre, le ' + w('k21-lyon', 'consensus de Lyon 2.0') + ', publié en 2024, considère que le grade B est lui aussi concluant, sur la base d’études récentes de pH-métrie prolongée.',
 'Par conséquent, le cours suit la source la plus récente, tout en signalant l’écart. De plus, Lyon 2.0 fixe les seuils de la pH-métrie sans IPP : un temps d’exposition acide supérieur à 6 % est diagnostique, alors qu’un temps inférieur à 4 % sur tous les jours d’enregistrement, sans association symptomatique, exclut le reflux pathologique. Enfin, l’endoscopie doit idéalement être faite 2 à 4 semaines après l’arrêt des IPP chez un patient sans reflux prouvé.')
 + C.img('k21_oesophagite_ulceree_endo.gif', 'Vue endoscopique de l’œsophage distal : muqueuse inflammatoire avec ulcérations multiples et lumière rétrécie.', 'Œsophagite par reflux sévère avec ulcères multiples et sténose, chez un homme de 72 ans. Des lésions aussi étendues correspondent aux grades élevés de Los Angeles et exigent un traitement continu.', credit({'auteur': 'melvil', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Esophageal_ulcer.jpg'}))
 + trap('Grade B de Los Angeles : non concluant pour la S2k 2023, concluant pour Lyon 2.0 (2024). Le cours retient Lyon 2.0, plus récent, et signale la divergence.', 'Point discuté')
 + key('Le reflux est prouvé par une œsophagite B, C ou D (Lyon 2.0), un Barrett histologique, une sténose peptique ou un temps d’exposition acide > 6 % sans IPP.')
 + src(LYON, S2K))

C.a(7, 'Traitement : mesures générales et traitement d’épreuve', P(
 'Une fois le diagnostic posé ou probable, le traitement associe mesures générales et médicaments. D’abord, la S2k 2023 demande d’informer tout patient de la place des ' + w('k21-mesures', 'mesures générales') + ' (recommandation 2.2). Ainsi, la perte de poids améliore les symptômes et l’efficacité des médicaments ; de même, surélever la tête du lit et éviter les repas tardifs réduisent le reflux nocturne.',
 'Ensuite, le traitement médicamenteux de référence est l’' + w('k21-d-ipp', 'IPP') + '. En cas de reflux prouvé ou probable, il est donné pendant au moins 4 à 8 semaines, à une dose adaptée au phénotype et au statut d’autorisation du produit (recommandation 2.6). Par ailleurs, chez un patient aux symptômes typiques sans alarme, d’autres produits sont possibles s’ils suffisent au patient : ' + w('k21-alginate', 'alginates') + ', antiacides ou antihistaminiques H2 (recommandation 2.4).')
 + key('Le patient perd du poids, surélève la tête du lit et évite les repas tardifs ; il reçoit un IPP 4 à 8 semaines, ou des alginates et des antiacides s’ils suffisent.')
 + src(S2K, FI('Nexium®'), FI('Gaviscon®')))

C.a(8, 'Échec du traitement et reflux réfractaire', P(
 'Si les symptômes persistent, il faut d’abord vérifier l’observance et la prise de l’IPP avant le repas. Ensuite, la S2k 2023 permet de changer d’IPP, de doubler la dose en deux prises ou d’ajouter un alginate (recommandation 2.7). Cependant, en l’absence de réponse après 8 semaines de dose double, on parle de ' + w('k21-refractaire', 'reflux réfractaire') + ' et une exploration complète s’impose (recommandation 2.8).',
 'Cette exploration comprend l’endoscopie avec biopsies, notamment pour rechercher une ' + w('k21-eoe', 'œsophagite à éosinophiles') + ', puis une ' + w('k21-impedance', 'pH-impédancemétrie') + ' qui distingue un reflux persistant acide ou non acide, une hypersensibilité et des symptômes sans lien avec le reflux (recommandation 1.11). De plus, une ' + w('k21-manometrie', 'manométrie à haute résolution') + ' recherche un trouble moteur (recommandation 1.12). En revanche, la radiographie n’a pas de place dans le diagnostic primaire (recommandation 1.14).')
 + quiz('Un patient a toujours des brûlures après 8 semaines d’ésoméprazole 40 mg matin et soir, bien pris avant les repas. L’endoscopie est normale. Quel examen ?',
   [('Transit baryté', False), ('pH-impédancemétrie sous IPP', True), ('Nouvelle gastroscopie dans 3 mois', False)],
   'Le reflux est réfractaire ; la pH-impédancemétrie sous IPP montre si un reflux persiste et s’il est associé aux symptômes (S2k 2023, recommandation 1.11 ; Lyon 2.0).')
 + key('En cas d’échec, on vérifie l’observance, puis on change ou on double l’IPP. Si le reflux reste réfractaire après 8 semaines de dose double, on fait une endoscopie avec biopsies, une pH-impédancemétrie et une manométrie.')
 + src(S2K, LYON))

C.a(9, 'Traitement au long cours et arrêt des IPP', P(
 'Après la phase initiale, la durée du traitement dépend de la forme. En effet, dans le reflux non compliqué (maladie non érosive, œsophagite A ou B), la S2k 2023 recommande un traitement guidé par les symptômes et demande d’éviter le surtraitement (recommandation 2.9). À l’inverse, l’œsophagite C ou D et la sténose peptique justifient un traitement continu (recommandation 2.10).',
 'Par conséquent, l’IPP qui n’est plus nécessaire doit être arrêté (recommandation 2.15), éventuellement de façon progressive, avec une prise à la demande en cas de récidive. Toutefois, la S2k rappelle que le risque absolu des IPP est faible et que, dans un reflux avéré, le bénéfice l’emporte (énoncé 2.16). De plus, en cas de traitement prolongé, la recherche de Helicobacter pylori suit la recommandation correspondante (recommandation 2.17).')
 + key('Le reflux non compliqué se traite à la demande, sans surtraitement. Les grades C et D et la sténose demandent un traitement continu, et un IPP inutile s’arrête.')
 + src(S2K))

C.a(10, 'Chirurgie anti-reflux', P(
 'Lorsque le traitement médical ne convient pas, la chirurgie peut être discutée. Cependant, la S2k 2023 exige au préalable une ' + w('k21-impedance', 'pH-impédancemétrie') + ' qui prouve le reflux pathologique (recommandation 3.2) et une ' + w('k21-manometrie', 'manométrie à haute résolution') + ' qui exclut un trouble moteur (recommandation 3.3). En effet, opérer un patient sans reflux prouvé ou atteint d’achalasie expose à l’échec.',
 'La ' + w('k21-fundoplicature', 'fundoplicature laparoscopique') + ' est l’intervention de première intention, efficace et peu morbide (recommandation 3.5). Par ailleurs, l’augmentation magnétique du sphincter peut être envisagée dans des indications précises (recommandation 3.6). Enfin, la hernie para-œsophagienne symptomatique et l’estomac retourné sont des indications chirurgicales propres (recommandation 3.8).')
 + key('Avant toute chirurgie, le reflux doit être prouvé par pH-impédancemétrie et la manométrie doit être normale. La fundoplicature laparoscopique est l’intervention de référence.')
 + src(S2K))

C.a(11, 'Complications : sténose peptique et œsophage de Barrett', P(
 'Si le reflux se prolonge, des complications peuvent apparaître. D’abord, la ' + w('k21-stenose', 'sténose peptique') + ' se manifeste par une dysphagie progressive aux solides ; elle impose une endoscopie avec biopsies pour exclure un cancer, puis un IPP au long cours.',
 'Ensuite, l’' + w('k21-barrett', 'œsophage de Barrett') + ' se définit, selon la S2k 2023, par la présence à l’histologie d’un épithélium cylindrique de type intestinal avec cellules caliciformes, sur une zone suspecte à l’endoscopie (énoncé 4.1). De plus, sa longueur est décrite selon la ' + w('k21-prague', 'classification de Prague') + ' (recommandation 4.3). En revanche, une métaplasie cylindrique de moins de 1 cm à la ligne Z n’est pas un Barrett et ne justifie aucune surveillance (recommandation 4.18).')
 + C.img('k21_barrett_histologie.gif', 'Coupe histologique : muqueuse œsophagienne de type glandulaire avec cellules caliciformes, caractéristique de la métaplasie intestinale de Barrett.', 'Œsophage de Barrett, coloration hématoxyline-éosine. L’épithélium malpighien est remplacé par un épithélium cylindrique avec cellules caliciformes (métaplasie intestinale).', credit({'auteur': 'Armed Forces Institute of Pathology (AFIP)', 'licence': 'Domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Barrett%27s_mucosa,_H%26E.jpg'}))
 + C.img('k21_stenose_peptique.gif', 'Vue endoscopique d’un rétrécissement de l’œsophage distal près de la jonction avec l’estomac.', 'Sténose peptique de l’œsophage distal chez un patient atteint de sclérodermie, vue endoscopique. La lumière est réduite par la fibrose cicatricielle.', credit({'auteur': 'Samir धर्म', 'licence': 'Domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Peptic_stricture.png'}))
 + key('La sténose donne une dysphagie aux solides ; on la biopsie et on donne un IPP continu. Le Barrett se définit par une métaplasie intestinale histologique décrite selon Prague, et un segment de moins de 1 cm ne se surveille pas.')
 + src(S2K, BAR))

C.a(12, 'Surveillance et traitement du Barrett', P(
 'Une fois le Barrett établi, la conduite dépend de sa longueur et de la dysplasie. Ainsi, l’ESGE 2023 propose une ' + w('k21-surveillance', 'surveillance endoscopique') + ' tous les 5 ans pour un Barrett de 1 à moins de 3 cm, tous les 3 ans de 3 à moins de 10 cm, et un suivi en centre expert au-delà de 10 cm. Lors de chaque examen, des biopsies ciblées des zones suspectes sont suivies de biopsies des quatre quadrants tous les 1 à 2 cm (S2k 2023, recommandation 4.6).',
 'En cas de dysplasie, la conduite change. En effet, une ' + w('k21-dysplasie', 'dysplasie de bas grade') + ' confirmée par un second pathologiste expérimenté justifie une ablation endoscopique (ESGE 2023), alors qu’une dysplasie de haut grade ou un cancer muqueux visible imposent une ' + w('k21-resection', 'résection endoscopique') + ', qui traite et permet le staging (S2k, recommandation 4.11). En revanche, le Barrett sans dysplasie n’est pas traité par ablation (recommandation 4.8).')
 + trap('Chimioprévention par IPP : la S2k 2023 la juge non établie (recommandation 4.5), alors que l’ESGE 2023, plus récente, propose un IPP en dose standard une fois par jour (recommandation faible). L’aspirine et les AINS ne sont pas recommandés dans ce but.', 'Point discuté')
 + key('Un Barrett de 1 à < 3 cm se surveille tous les 5 ans et de 3 à < 10 cm tous les 3 ans, alors qu’un Barrett ≥ 10 cm relève d’un centre expert. Une dysplasie de bas grade confirmée justifie une ablation, et une dysplasie de haut grade ou une lésion visible une résection.')
 + C.pareto('pareto-k21-clinique', 'Reflux et Barrett', ['k21-1', 'k21-5', 'k21-6', 'k21-8', 'k21-9', 'k21-12'],
     ['Le reflux devient pathologique quand il cause des symptômes gênants ou des lésions.',
      'Symptômes typiques sans alarme : IPP d’épreuve ; alarme ou échec : endoscopie.',
      'La preuve repose sur un grade B, C ou D de Los Angeles, un Barrett, une sténose ou une exposition acide > 6 %.',
      'Réfractaire après 8 semaines de dose double : pH-impédancemétrie et manométrie.',
      'Le reflux non compliqué se traite à la demande, alors que les grades C et D et la sténose demandent un traitement continu.',
      'Le Barrett se surveille tous les 5 ans (1 à < 3 cm) ou tous les 3 ans (3 à < 10 cm).'])
 + src(BAR, S2K))

C.a(13, 'Situations particulières', P(
 'Certaines situations modifient ces règles. Pendant la grossesse, la S2k 2023 recommande une escalade progressive : mesures générales, antiacide, alginate, sucralfate, antihistaminique H2, puis IPP (recommandation 2.14). De même, en cas de manifestations extra-œsophagiennes suspectées chez l’adulte, un IPP à double dose pendant 12 semaines est proposé (recommandation 2.11) ; en revanche, chez l’enfant, une exploration doit précéder le traitement.',
 'Pour conclure, reprenons le patient du début. Sa dysphagie récente est un signe d’alarme ; par conséquent, une gastroscopie est faite rapidement. Elle montre une œsophagite de grade C et une sténose peptique courte ; les biopsies sont bénignes. Dès lors, il reçoit un IPP continu, une perte de poids est engagée, et l’endoscopie de contrôle recherchera un Barrett après cicatrisation.')
 + key('Pendant la grossesse, on escalade progressivement jusqu’à l’IPP. Chez l’adulte avec des symptômes extra-œsophagiens, on donne un IPP à double dose pendant 12 semaines.')
 + src(S2K))

C.a(14, 'Critères formels du diagnostic et paramètres clés', alert(
 '<p>Le <b>reflux</b> est <b>pathologique</b> quand il cause des symptômes gênants ou des lésions. La <b>preuve objective</b> repose sur une œsophagite de Los Angeles B, C ou D, un Barrett histologique, une sténose peptique ou un temps d’exposition acide > 6 % sans IPP. À l’inverse, un temps d’exposition acide < 4 % sur tous les jours, sans association symptomatique, <b>exclut</b> le reflux. Le reflux est <b>réfractaire</b> après l’échec de 8 semaines d’IPP à double dose. Enfin, le <b>Barrett</b> exige une métaplasie intestinale histologique d’au moins 1 cm.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> L’IPP dure 4 à 8 semaines : l’ésoméprazole se donne à 40 mg/j pendant 4 semaines pour l’œsophagite, puis à 20 mg/j, et le pantoprazole à 20 mg/j dans le reflux léger. L’endoscopie se fait 2 à 4 semaines après l’arrêt des IPP si le reflux n’est pas prouvé. Le Barrett se surveille tous les 5 ans ou tous les 3 ans selon sa longueur.</div>'
 + src(LYON, S2K, BAR, FI('Nexium®'), FI('Pantozol®')))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Statut'], [
   ['Y a-t-il une lésion, une complication, un Barrett ?', w('k21-ogd', 'Œsogastroduodénoscopie'), 'Indiquée si alarme, échec ou symptômes anciens'],
   ['Le reflux est-il pathologique sans lésion ?', w('k21-phmetrie', 'pH-métrie sans IPP'), 'Indiquée si diagnostic non prouvé'],
   ['Reste-t-il un reflux sous IPP ?', w('k21-impedance', 'pH-impédancemétrie sous IPP'), 'Indiquée si reflux prouvé réfractaire'],
   ['Y a-t-il un trouble moteur ?', w('k21-manometrie', 'Manométrie à haute résolution'), 'Indiquée avant chirurgie ou si diagnostic incertain'],
   ['Œsophagite à éosinophiles ?', 'Biopsies étagées de l’œsophage', 'Indiquées si réfractaire ou dysphagie'],
   ['Diagnostic primaire du reflux ?', 'Radiographie barytée', 'Non indiquée']])
 + P('Le tableau se lit de haut en bas : ainsi, l’endoscopie vient en premier dès qu’il existe un signe d’alarme, alors que la pH-métrie sert à prouver un reflux sans lésion visible.')
 + key('L’endoscopie montre les lésions, la pH-métrie apporte la preuve, l’impédancemétrie sous IPP explore le reflux réfractaire, et la manométrie précède la chirurgie.')
 + src(S2K, LYON))

C.e(2, 'Interpréter la pH-métrie selon Lyon 2.0', P(
 'L’interprétation repose surtout sur le ' + w('k21-tea', 'temps d’exposition acide') + '. Ainsi, au-dessus de 6 %, le reflux est pathologique ; au-dessous de 4 %, il est normal ; entre les deux, le résultat n’est pas concluant et des critères complémentaires sont utilisés. De plus, le nombre total d’épisodes de reflux apporte un argument : moins de 40 par jour plaide contre un reflux pathologique, plus de 80 par jour pour un reflux objectif.',
 'Par ailleurs, l’' + w('k21-impedance-basale', 'impédance basale') + ' renseigne sur l’intégrité de la muqueuse : inférieure à 1500 ohms, elle soutient le diagnostic ; supérieure à 2500 ohms, elle plaide contre. Enfin, sous IPP optimisé, l’association d’un temps d’exposition acide supérieur à 4 % et de plus de 80 épisodes signe un reflux réfractaire justifiant une escalade.')
 + quiz('La pH-métrie sans IPP montre un temps d’exposition acide de 2,8 % sur tous les jours, mais chaque épisode de brûlure coïncide avec un reflux. Quel diagnostic ?',
   [('Reflux pathologique', False), ('Hypersensibilité au reflux', True), ('Résultat non concluant', False)],
   'Une exposition acide inférieure à 4 % avec une association symptomatique positive définit l’hypersensibilité au reflux (Lyon 2.0).')
 + key('Une exposition acide > 6 % est pathologique, < 4 % normale, et de 4 à 6 % non concluante. Dans ce dernier cas, plus de 80 épisodes par jour et une impédance < 1500 ohms plaident en faveur du reflux.')
 + src(LYON))

C.e(3, 'Lire un compte rendu d’endoscopie', P(
 'Le compte rendu nomme d’abord le grade de Los Angeles de l’œsophagite. Ensuite, il situe la ' + w('k21-jog', 'jonction œsogastrique') + ' au sommet des plis gastriques, sans insufflation excessive (S2k 2023, recommandation 4.4), et décrit une éventuelle hernie hiatale. Enfin, s’il existe une muqueuse cylindrique, il la mesure selon Prague et précise les biopsies réalisées.',
 'Cependant, les biopsies de l’œsophage ne servent pas à diagnostiquer une maladie non érosive (énoncé 1.9). En revanche, elles sont indispensables devant une sténose, une suspicion de Barrett ou une dysphagie sans cause évidente.')
 + quiz('L’endoscopie décrit un Barrett C2M5. Que signifient ces chiffres ?',
   [('2 cm de longueur circonférentielle, 5 cm d’extension maximale', True), ('Grade C de Los Angeles sur 5 cm', False)],
   'La classification de Prague décrit l’extension circonférentielle (C) et l’extension maximale (M) en centimètres ; avec M = 5 cm, l’ESGE propose une surveillance tous les 3 ans.')
 + key('On classe l’œsophagite selon Los Angeles et le Barrett selon Prague, et l’on situe la jonction au sommet des plis gastriques ; les biopsies sont inutiles dans la maladie non érosive.')
 + C.pareto('pareto-k21-examens', 'Examens', ['k21-e-1', 'k21-e-2', 'k21-e-3'],
     ['L’endoscopie s’impose en cas d’alarme, d’échec ou de symptômes anciens.',
      'Sans IPP, la pH-métrie est pathologique au-delà de 6 % d’exposition acide et normale en dessous de 4 %.',
      'pH-impédancemétrie sous IPP pour le reflux réfractaire.',
      'La manométrie à haute résolution précède toute chirurgie.',
      'La classification de Prague mesure C et M en centimètres.'])
 + src(S2K, LYON, BAR))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : la jonction œsogastrique', P(
 'La barrière anti-reflux associe trois éléments : le sphincter inférieur de l’œsophage, le pilier droit du diaphragme qui l’entoure, et l’angle de His entre œsophage et grosse tubérosité. Or, dans la hernie hiatale par glissement, la jonction remonte dans le thorax ; dès lors, le sphincter et le diaphragme ne s’additionnent plus. À l’inverse, dans la hernie para-œsophagienne, la jonction reste en place mais l’estomac s’engage à côté de l’œsophage, avec un risque de volvulus.')
 + key('La hernie par glissement affaiblit la barrière et cause le reflux, alors que la hernie para-œsophagienne expose à un risque mécanique et s’opère si elle est symptomatique.', 'Science → clinique.'))
C.s('histo', 'Histologie', 'Histologie : de l’œsophagite au Barrett', P(
 'L’œsophage normal est revêtu d’un épithélium malpighien non kératinisé. Sous l’effet du reflux, la couche basale s’épaissit et les papilles s’allongent ; ensuite, des polynucléaires et parfois quelques éosinophiles apparaissent. Lorsque l’agression persiste, un épithélium cylindrique avec cellules caliciformes peut remplacer l’épithélium malpighien : c’est la métaplasie intestinale du Barrett. Par la suite, une dysplasie de bas puis de haut grade peut précéder l’adénocarcinome.')
 + key('Métaplasie intestinale, puis dysplasie, puis adénocarcinome : c’est pourquoi le Barrett est surveillé et biopsié.', 'Science → examen.'))
C.s('phys', 'Physiologie', 'Physiologie : relaxations transitoires et clairance', P(
 'Après un repas, la distension gastrique déclenche par voie vagale des relaxations transitoires du sphincter, indépendantes de la déglutition. Ainsi, elles permettent l’éructation, mais elles laissent aussi passer le reflux. Ensuite, la clairance repose sur le péristaltisme, qui vide l’œsophage, et sur la salive, dont les bicarbonates neutralisent l’acide résiduel. Par conséquent, la nuit, quand la salivation et la déglutition diminuent, l’exposition acide se prolonge.')
 + key('C’est pourquoi surélever la tête du lit et éviter les repas tardifs réduisent le reflux nocturne.', 'Science → traitement.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : pourquoi l’IPP se prend avant le repas', P(
 'L’IPP est une prodrogue activée en milieu acide, dans le canalicule de la cellule pariétale ; il bloque alors de façon irréversible les pompes H⁺/K⁺-ATPase actives. Or, les pompes sont surtout activées par le repas. Par conséquent, l’IPP est pris avant le repas ; l’information professionnelle suisse du pantoprazole précise environ 1 heure avant. En revanche, l’alginate forme un radeau visqueux à la surface du contenu gastrique ; il agit donc après le repas, sans réduire la sécrétion acide.')
 + key('L’IPP se prend avant le repas et l’alginate après, car le moment de la prise découle du mécanisme.', 'Science → traitement.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir la classe. En pratique, l’IPP est le traitement de fond, alors que les alginates et les antiacides soulagent les symptômes à la demande.')
 + table(['Classe', 'Molécule disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Inhibiteur de la pompe à protons', 'Ésoméprazole, pantoprazole, oméprazole', 'Traitement de référence', w('k21-d-ipp', 'Monographie')],
   ['Alginate associé à un antiacide', 'Gaviscon®', 'Symptômes légers, ajout à l’IPP, grossesse', w('k21-alginate', 'Monographie')],
   ['Antihistaminique H2', 'Aucune spécialité orale retrouvée dans les informations professionnelles consultées ; disponibilité à vérifier', 'Alternative mentionnée par la S2k 2023', w('k21-anti-h2', 'Fiche')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, seul l’IPP cicatrise une œsophagite ; les autres classes agissent surtout sur les symptômes.')
 + key('IPP pour cicatriser et prévenir ; alginate et antiacide pour soulager.')
 + src(S2K))

C.p(2, 'Doses et durées', P('Les doses suivantes proviennent des informations professionnelles suisses ; de plus, les écarts avec les recommandations sont signalés.')
 + table(['Médicament', 'Situation', 'Dose et durée', 'Source'], [
   ['Ésoméprazole', 'Œsophagite par reflux', '40 mg 1×/j, 4 semaines, puis 4 semaines de plus si nécessaire', 'Information professionnelle Nexium®'],
   ['Ésoméprazole', 'Prévention des récidives de l’œsophagite', '20 mg 1×/j', 'Information professionnelle Nexium®'],
   ['Ésoméprazole', 'Reflux symptomatique sans œsophagite', '20 mg 1×/j ; à la demande après disparition des symptômes', 'Information professionnelle Nexium®'],
   ['Pantoprazole', 'Reflux léger', '20 mg 1×/j, 4 semaines, prolongeables de 4 semaines', 'Information professionnelle Pantozol®'],
   ['Pantoprazole', 'Œsophagite modérée', '40 mg 1×/j, 4 à 8 semaines', 'Information professionnelle Pantozol®'],
   ['IPP', 'Reflux réfractaire', 'Dose double en deux prises (1-0-1), 8 semaines', 'S2k 2023, recommandations 2.7 et 2.8'],
   ['Gaviscon®', 'Symptômes', '2 à 4 comprimés à croquer après les repas et au coucher, jusqu’à 4×/j', 'Information professionnelle Gaviscon®']])
 + P('Par exemple, le patient du début, atteint d’une œsophagite de grade C, reçoit ésoméprazole 40 mg chaque matin pendant 8 semaines, puis un traitement d’entretien continu, car les grades C et D justifient un traitement prolongé.')
 + key('L’œsophagite se traite à dose pleine 4 à 8 semaines, l’entretien à demi-dose, et le reflux réfractaire à dose double en deux prises.')
 + src(FI('Nexium®'), FI('Pantozol®'), FI('Gaviscon®'), S2K))

C.p(3, 'Interactions, surveillance et effets indésirables', alert(
 'L’association de l’ésoméprazole au clopidogrel est déconseillée par l’information professionnelle suisse. De même, chez un patient sous méthotrexate à forte dose, l’IPP est suspendu. Par ailleurs, l’IPP modifie l’absorption des médicaments dont la résorption dépend du pH gastrique ; ainsi, l’association à l’atazanavir ou au nelfinavir n’est pas recommandée.', 'Interactions importantes.')
 + P('Au long cours, les IPP exposent à une ' + w('k21-ipp-long-cours', 'hypomagnésémie') + ', à une hausse modérée du risque de fractures et à des infections digestives un peu plus fréquentes. Cependant, la S2k 2023 rappelle que ce risque absolu est faible et que, dans un reflux avéré, le bénéfice l’emporte. Par conséquent, l’enjeu principal est d’arrêter l’IPP quand l’indication disparaît, plutôt que de le refuser quand elle existe.',
 'Quant aux alginates, ils contiennent du sodium (environ 63 mg par comprimé de Gaviscon®) ; il faut donc en tenir compte chez le patient insuffisant cardiaque ou soumis à un régime pauvre en sel.')
 + key('L’IPP demande de la prudence avec le clopidogrel et le méthotrexate à forte dose ; au long cours, on surveille le magnésium et le risque de fracture et l’on réévalue l’indication. Les alginates apportent du sodium.')
 + C.pareto('pareto-k21-pharma', 'Pharmacologie', ['k21-p-1', 'k21-p-2', 'k21-p-3'],
     ['L’IPP se prend environ 1 heure avant le repas, et l’alginate après.',
      'Ésoméprazole 40 mg/j 4 à 8 semaines pour l’œsophagite, 20 mg/j en entretien.',
      'Le reflux réfractaire reçoit une dose double en deux prises pendant 8 semaines.',
      'L’association du clopidogrel à l’ésoméprazole est déconseillée.',
      'Arrêter l’IPP quand l’indication disparaît.'])
 + src(FI('Nexium®'), FI('Gaviscon®'), S2K))

# ---------------- Fenêtres
L = lab
C.pop('k21-alarme', 'Signes d’alarme du reflux', L(('Liste (S2k 2023)', 'Les signes d’alarme sont la dysphagie, l’odynophagie, les signes d’hémorragie digestive y compris l’anémie ferriprive, l’anorexie, la perte de poids involontaire, les vomissements répétés et les antécédents familiaux de tumeur digestive.'), ('Conduite', 'Ils imposent une endoscopie immédiate, sans traitement d’épreuve préalable, car un cancer ou une complication doit être exclu.')) + src(S2K))
C.pop('k21-los-angeles', 'Classification de Los Angeles', L(('Grade A', 'Une ou plusieurs lésions ≤ 5 mm, ne reliant pas le sommet de deux plis.'), ('Grade B', 'Au moins une lésion > 5 mm, ne reliant pas le sommet de deux plis.'), ('Grade C', 'Lésions reliant le sommet de deux plis ou plus, sur moins de 75 % de la circonférence.'), ('Grade D', 'Lésions sur au moins 75 % de la circonférence.'), ('Valeur', 'Selon Lyon 2.0, les grades B, C et D sont concluants, alors que la S2k 2023 ne retient que les grades C et D.')) + src(LYON, S2K))
C.pop('k21-barrett', 'Œsophage de Barrett', L(('Définition', 'L’épithélium malpighien de l’œsophage distal est remplacé sur au moins 1 cm par un épithélium cylindrique avec métaplasie intestinale.'), ('Risque', 'Il progresse vers une dysplasie de haut grade ou un adénocarcinome chez 0,3 à 0,8 % des patients par an (ESGE 2023).'), ('Conduite', 'On le biopsie selon le protocole, on le surveille selon sa longueur et on traite la dysplasie par voie endoscopique.')) + src(BAR, S2K) + C.img('k21_barrett_histologie.gif', 'Histologie : muqueuse glandulaire avec cellules caliciformes (métaplasie intestinale).', 'Les cellules caliciformes, claires et arrondies, signent la métaplasie intestinale ; or, c’est elle qui définit le Barrett et qui porte le risque d’adénocarcinome.', credit({'auteur': 'Armed Forces Institute of Pathology (AFIP)', 'licence': 'Domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Barrett%27s_mucosa,_H%26E.jpg'})))
C.pop('k21-rgo-def', 'Maladie de reflux gastro-œsophagien', L(('Définition (S2k 2023, énoncé 1.1)', 'Reflux du contenu gastrique qui provoque des symptômes gênants ou des lésions de l’œsophage.'), ('Définition « actionnable » (Lyon 2.0)', 'Le reflux est « actionnable » quand l’endoscopie ou la pH-métrie apporte une preuve objective associée à des symptômes compatibles.')) + src(S2K, LYON))
C.pop('k21-preuve', 'Preuve objective du reflux', L(('Endoscopie', 'L’endoscopie prouve le reflux quand elle montre une œsophagite de grade B, C ou D, un Barrett histologique ou une sténose peptique.'), ('pH-métrie sans IPP', 'Temps d’exposition acide > 6 %.'), ('Ce qui ne prouve pas', 'La réponse aux IPP ne prouve pas le reflux (S2k 2023, énoncé 1.3), et les biopsies ne le prouvent pas dans la maladie non érosive.')) + src(LYON, S2K))
C.pop('k21-oesophagite', 'Œsophagite érosive', L(('Définition', 'Ce sont des pertes de substance de la muqueuse œsophagienne distale, visibles à l’endoscopie.'), ('Classification', 'On la classe de A à D selon Los Angeles.'), ('Traitement', 'On donne un IPP à dose pleine pendant 4 à 8 semaines, puis un traitement continu pour les grades C et D, car ils récidivent et se compliquent.')) + src(S2K) + C.img('k21_oesophagite_ulceree_endo.gif', 'Endoscopie : œsophage distal inflammatoire avec ulcérations multiples.', 'Les ulcérations confluent sur la muqueuse distale, là où l’acide stagne le plus longtemps ; c’est pourquoi l’œsophagite sévère prédomine juste au-dessus de la jonction.', credit({'auteur': 'melvil', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Esophageal_ulcer.jpg'})))
C.pop('k21-nerd', 'Maladie de reflux non érosive', L(('Définition', 'Le patient a des symptômes typiques et un reflux pathologique en pH-métrie, sans lésion endoscopique.'), ('Piège', 'Les biopsies ne permettent pas ce diagnostic (S2k 2023, énoncé 1.9).'), ('Traitement', 'Guidé par les symptômes, souvent à la demande.')) + src(S2K))
C.pop('k21-obesite', 'Surpoids et reflux', L(('Mécanisme', 'La pression abdominale augmente et favorise la hernie hiatale.'), ('Preuve', 'Dans l’étude HUNT citée par la S2k, la perte de poids améliorait les symptômes, proportionnellement à la baisse de l’indice de masse corporelle.')) + src(S2K))
C.pop('k21-hernie', 'Hernie hiatale', L(('Par glissement', 'La jonction œsogastrique remonte dans le thorax ; la barrière anti-reflux s’affaiblit.'), ('Para-œsophagienne', 'L’estomac s’engage à côté de l’œsophage et risque un volvulus ; c’est pourquoi on opère si elle est symptomatique (S2k 2023, recommandation 3.8).')) + src(S2K))
C.pop('k21-jog', 'Jonction œsogastrique', L(('Repère endoscopique', 'La jonction se situe au sommet des plis gastriques, vue sans insufflation excessive ni péristaltisme (S2k 2023, recommandation 4.4).'), ('Ligne Z', 'La ligne Z est la limite visible entre la muqueuse malpighienne pâle et la muqueuse cylindrique rouge ; normalement, elle se situe au niveau de la jonction.')) + src(S2K))
C.pop('k21-metaplasie', 'Métaplasie intestinale', L(('Définition', 'Un épithélium est remplacé par un épithélium de type intestinal, qui contient des cellules caliciformes.'), ('Signification', 'Elle définit le Barrett et précède la dysplasie.')) + src(S2K))
C.pop('k21-pyrosis', 'Pyrosis', L(('Définition', 'Le pyrosis est une brûlure rétrosternale ascendante, qui survient souvent après les repas ou en décubitus.'), ('Valeur', 'Symptôme typique du reflux, mais insuffisant pour en prouver la nature pathologique.'), ('Piège', 'Une douleur thoracique impose d’exclure d’abord une cause cardiaque.')))
C.pop('k21-regurgitation', 'Régurgitation', L(('Définition', 'La régurgitation est une remontée sans effort de contenu gastrique dans la bouche, sans nausée.'), ('Diagnostic différentiel', 'Rumination, achalasie (régurgitation d’aliments non digérés).')))
C.pop('k21-epreuve', 'Traitement d’épreuve par IPP', L(('Indication', 'On le propose en cas de symptômes typiques, sans signe d’alarme, sans antécédent familial de cancer digestif haut et sans facteur de risque de complication (S2k 2023, recommandation 2.3).'), ('Durée', 'Il dure 4 à 8 semaines en dose standard.'), ('Échec', 'Après 8 semaines bien conduites : exploration (recommandation 2.5).')) + src(S2K))
C.pop('k21-phmetrie', 'pH-métrie œsophagienne', L(('Technique', 'Capteur de pH placé dans l’œsophage distal pendant 24 heures (sonde) ou jusqu’à 96 heures (capsule sans fil).'), ('Condition', 'Sans IPP pour prouver le reflux ; sous IPP pour explorer un reflux réfractaire prouvé.'), ('Seuils (Lyon 2.0)', 'Un temps d’exposition acide > 6 % est pathologique, alors qu’un temps < 4 % est normal.')) + src(LYON))
C.pop('k21-lyon', 'Consensus de Lyon 2.0', L(('Nature', 'Consensus international d’experts sur le diagnostic moderne du reflux, publié dans Gut en 2024.'), ('Apports', 'Lyon 2.0 rend concluant le grade B de Los Angeles, fixe les seuils de la pH-métrie et introduit la notion de reflux « actionnable ».')) + src(LYON))
C.pop('k21-mesures', 'Mesures générales', L(('Efficaces', 'La perte de poids, la tête du lit surélevée en cas de symptômes nocturnes, l’absence de repas tardif et l’arrêt du tabac chez le patient de poids normal sont efficaces.'), ('Plausibles', 'Le décubitus latéral gauche, la respiration abdominale et l’absence de vêtements serrés sont plausibles, mais moins prouvés.')) + src(S2K))
C.pop('k21-alginate', 'Alginates (Gaviscon®)', L(('Composition', 'Gaviscon® contient de l’alginate de sodium, du bicarbonate de sodium et du carbonate de calcium.'), ('Mécanisme', 'Formation d’un radeau visqueux qui flotte sur le contenu gastrique et limite le reflux.'), ('Posologie suisse', '2 à 4 comprimés à croquer après les repas et au coucher, jusqu’à 4 fois par jour.'), ('Précaution', 'Chaque comprimé apporte environ 63 mg de sodium, ce qui compte chez l’insuffisant cardiaque ou rénal.')) + src(FI('Gaviscon®')))
C.pop('k21-refractaire', 'Reflux réfractaire', L(('Définition (S2k 2023)', 'Réponse insuffisante après au moins 8 semaines d’IPP à double dose (1-0-1).'), ('Causes', 'Mauvaise observance, reflux persistant, hypersensibilité, trouble fonctionnel, œsophagite à éosinophiles, autre diagnostic.'), ('Conduite', 'On fait une endoscopie avec biopsies, une pH-impédancemétrie et une manométrie, car il faut prouver le reflux et écarter un autre diagnostic.')) + src(S2K))
C.pop('k21-eoe', 'Œsophagite à éosinophiles', L(('Définition', 'C’est une inflammation chronique de l’œsophage d’origine immuno-allergique, avec un infiltrat éosinophile.'), ('Indice', 'Une dysphagie, des impactions alimentaires ou un reflux réfractaire doivent la faire évoquer.'), ('Diagnostic', 'Biopsies étagées de plusieurs niveaux de l’œsophage (S2k 2023, recommandation 1.10).')) + src(S2K))
C.pop('k21-impedance', 'pH-impédancemétrie', L(('Principe', 'Mesure de l’impédance électrique, qui détecte le passage du bol refluant qu’il soit acide ou non, couplée au pH.'), ('Indications', 'On la demande en cas de reflux réfractaire sous IPP, avant une chirurgie anti-reflux pour prouver le reflux, et devant des éructations ou une rumination.'), ('Lecture', 'Elle compte les épisodes de reflux, mesure l’exposition acide et calcule l’association entre symptômes et reflux.')) + src(S2K, LYON))
C.pop('k21-manometrie', 'Manométrie œsophagienne à haute résolution', L(('Principe', 'Sonde à capteurs multiples qui mesure la pression du sphincter et le péristaltisme.'), ('Indications', 'On la fait avant toute chirurgie anti-reflux et quand le diagnostic est incertain, pour exclure une achalasie ou un trouble moteur (S2k 2023, recommandations 1.12 et 3.3).')) + src(S2K))
C.pop('k21-fundoplicature', 'Fundoplicature laparoscopique', L(('Principe', 'La grosse tubérosité est enroulée autour de l’œsophage distal pour reconstituer une barrière anti-reflux ; le hiatus est refermé.'), ('Place', 'Intervention de première intention si l’indication est posée (S2k 2023, recommandation 3.5).'), ('Effets indésirables', 'Dysphagie, ballonnements, difficulté à éructer.')) + src(S2K))
C.pop('k21-stenose', 'Sténose peptique', L(('Mécanisme', 'Une œsophagite chronique cicatrise par fibrose et rétrécit la lumière.'), ('Clinique', 'Le patient présente une dysphagie progressive aux solides.'), ('Conduite', 'On fait une endoscopie avec biopsies pour exclure un cancer, puis on donne un IPP continu (S2k 2023, recommandation 2.10) et on dilate si nécessaire.')) + src(S2K) + C.img('k21_stenose_peptique.gif', 'Endoscopie : rétrécissement de l’œsophage distal près de la jonction.', 'La fibrose cicatricielle rétrécit la lumière de façon régulière ; cependant, seule la biopsie exclut un cancer, qui peut prendre le même aspect.', credit({'auteur': 'Samir धर्म', 'licence': 'Domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Peptic_stricture.png'})))
C.pop('k21-prague', 'Classification de Prague', L(('C', 'C mesure en centimètres l’extension circonférentielle de la muqueuse cylindrique au-dessus de la jonction.'), ('M', 'M mesure en centimètres l’extension maximale, languettes comprises.'), ('Usage', 'La valeur M guide l’intervalle de surveillance de l’ESGE 2023.')) + src(S2K, BAR))
C.pop('k21-surveillance', 'Surveillance du Barrett sans dysplasie', L(('ESGE 2023', 'Un Barrett de M ≥ 1 et < 3 cm se surveille tous les 5 ans, et de M ≥ 3 et < 10 cm tous les 3 ans ; à partir de 10 cm, il relève d’un centre expert. Une ligne Z irrégulière < 1 cm ne justifie ni biopsies ni surveillance.'), ('S2k 2023', 'La S2k propose un contrôle à 1 an, puis tous les 3 à 5 ans selon les facteurs de risque.'), ('Biopsies', 'Biopsies ciblées, puis quatre quadrants tous les 1 à 2 cm.')) + src(BAR, S2K))
C.pop('k21-dysplasie', 'Dysplasie de bas grade dans le Barrett', L(('Confirmation', 'Un second pathologiste expérimenté confirme le diagnostic, puis une endoscopie à 2 à 3 mois exclut une lésion visible (S2k 2023, recommandation 4.9).'), ('Traitement', 'Si elle est confirmée sur deux endoscopies, on fait une ablation endoscopique (ESGE 2023, recommandation forte) ; sinon, on surveille à 6 mois, puis chaque année.')) + src(BAR, S2K))
C.pop('k21-resection', 'Résection endoscopique', L(('Indication', 'Toute lésion visible avec dysplasie ou cancer muqueux se résèque, car la pièce permet le staging.'), ('Critères de guérison', 'Cancer pT1 sm1 (< 500 µm), sans invasion lymphatique ni veineuse, bien ou moyennement différencié, résection complète (S2k 2023, recommandation 4.16).'), ('Suite', 'Ablation du Barrett résiduel, puis endoscopies à 3, 6 et 12 mois, puis annuelles.')) + src(S2K, BAR))
C.pop('k21-ogd', 'Œsogastroduodénoscopie dans le reflux', L(('Indications', 'On la fait en cas de signes d’alarme, d’échec du traitement d’épreuve ou de symptômes anciens de plusieurs années, pour dépister un Barrett.'), ('Moment', 'Idéalement, on la fait 2 à 4 semaines après l’arrêt des IPP si le reflux n’est pas prouvé, car les IPP cicatrisent l’œsophagite (Lyon 2.0).')) + src(S2K, LYON))
C.pop('k21-tea', 'Temps d’exposition acide', L(('Définition', 'Pourcentage du temps d’enregistrement pendant lequel le pH œsophagien est inférieur à 4.'), ('Seuils', 'Un temps > 6 % est pathologique, un temps < 4 % est normal, et un temps de 4 à 6 % n’est pas concluant (Lyon 2.0).')) + src(LYON))
C.pop('k21-impedance-basale', 'Impédance basale', L(('Définition', 'C’est l’impédance de la muqueuse entre les épisodes de reflux ; elle baisse quand la muqueuse est lésée, car les espaces intercellulaires s’élargissent.'), ('Seuils (Lyon 2.0)', '< 1500 ohms : argument en faveur du reflux ; > 2500 ohms : argument contre.')) + src(LYON))
C.pop('k21-d-ipp', 'IPP dans le reflux', L(('Mécanisme', 'Prodrogue activée en milieu acide, inhibition irréversible des pompes H⁺/K⁺-ATPase actives.'), ('Prise', 'On prend l’IPP environ 1 heure avant un repas (information professionnelle Pantozol®), car il n’inhibe que les pompes activées par le repas.'), ('Posologies suisses', 'L’ésoméprazole se donne à 40 mg/j pendant 4 à 8 semaines pour l’œsophagite, puis à 20 mg/j en entretien ; le pantoprazole se donne à 20 mg/j dans le reflux léger et à 40 mg/j dans l’œsophagite modérée.')) + src(FI('Nexium®'), FI('Pantozol®')))
C.pop('k21-anti-h2', 'Antihistaminiques H2', L(('Mécanisme', 'Ils bloquent les récepteurs H2 de la cellule pariétale ; leur effet est moins puissant et plus bref que celui de l’IPP.'), ('Place', 'On les réserve aux symptômes légers, et ils sont une option pendant la grossesse avant l’IPP (S2k 2023, recommandations 2.4 et 2.14).')) + src(S2K))
C.pop('k21-ipp-long-cours', 'IPP au long cours', L(('Hypomagnésémie', 'Elle apparaît après au moins 3 mois, surtout après un an.'), ('Fractures', 'Risque modérément accru après plus d’un an à dose élevée.'), ('Règle', 'Réévaluer et arrêter si l’indication disparaît (S2k 2023, recommandation 2.15).')) + src(FI('Nexium®'), S2K))

C.termes = [
 (r'sphincter inférieur de l’œsophage', 'k21-jog'), (r'IPP', 'k21-d-ipp'), (r'ésoméprazole', 'k21-d-ipp'), (r'pantoprazole', 'k21-d-ipp'),
 (r'sténose peptique', 'k21-stenose'), (r'hernie para-œsophagienne', 'k21-hernie'), (r'classification de Prague|Prague', 'k21-prague'),
 (r'temps d’exposition acide', 'k21-tea'), (r'hypersensibilité au reflux|hypersensibilité', 'k21-hypersensibilite'),
 (r'Los Angeles', 'k21-los-angeles'), (r'Barrett', 'k21-barrett'), (r'dysplasie de haut grade', 'k21-resection'), (r'adénocarcinome', 'k21-adk'),
 (r'alginates?', 'k21-alginate'), (r'antihistaminiques? H2', 'k21-anti-h2'), (r'achalasie', 'k21-achalasie'), (r'ligne Z', 'k21-jog'),
 (r'Gaviscon®', 'k21-alginate'), (r'clopidogrel', 'k21-clopidogrel'), (r'méthotrexate', 'k21-clopidogrel'),
]
C.pop('k21-hypersensibilite', 'Hypersensibilité au reflux', L(('Définition (Lyon 2.0)', 'L’exposition acide est normale (< 4 %), mais les symptômes sont associés aux épisodes de reflux.'), ('Conséquence', 'Trouble de l’interaction intestin-cerveau ; l’escalade des IPP est peu utile.')) + src(LYON))
C.pop('k21-adk', 'Adénocarcinome de l’œsophage', L(('Origine', 'Il naît le plus souvent sur un œsophage de Barrett, par la séquence métaplasie, dysplasie puis cancer.'), ('Précoce', 'Une lésion visible avec dysplasie ou cancer muqueux se traite par résection endoscopique.'), ('Renvoi', 'Le cours C15 — Tumeur maligne de l’œsophage traite le cancer invasif.')) + src(BAR))
C.pop('k21-achalasie', 'Achalasie', L(('Définition', 'Défaut de relaxation du sphincter inférieur et absence de péristaltisme.'), ('Pertinence', 'Elle peut imiter un reflux réfractaire ; une fundoplicature l’aggraverait. C’est pourquoi la manométrie précède toute chirurgie anti-reflux.')) + src(S2K))
C.pop('k21-clopidogrel', 'IPP et clopidogrel, méthotrexate', L(('Clopidogrel', 'Association à l’ésoméprazole déconseillée en raison d’une interaction pharmacocinétique et pharmacodynamique documentée ; l’ésoméprazole inhibe le CYP2C19 (information professionnelle suisse).'), ('Méthotrexate', 'Taux accrus de méthotrexate ; suspendre l’IPP en cas de méthotrexate à forte dose.')) + src(FI('Nexium®')))

C.write()
