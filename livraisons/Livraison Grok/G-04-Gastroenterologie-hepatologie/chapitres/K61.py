# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K61', 'Abcès des régions anale et rectale',
    'K61 — Abcès des régions anale et rectale · CIM-10-GM 2024 · Canal anal et rectum',
    'Adulte · abcès cryptoglandulaire subanodermique, intersphinctérien, ischio-anal et supralévatorien (K61.0 à K61.4) · rédaction du 10.10.2026 · référentiels S3 Analabszess 2026 (DGAV/DGK, avec Koloproktologie Schweiz), S3 Kryptoglanduläre Analfistel 2026',
    'Antibiotiques et soins de plaie')
w = C.w
ABS = ('Fritz S. et al., S3-Leitlinie Analabszess, version 3.0, mai 2026 (AWMF 088-005, DGAV/DGK avec Koloproktologie Schweiz)', 'https://register.awmf.org/assets/guidelines/088-005l_S3_Analabszess_2026-06.pdf')
FST = ('Jaschke et al., S3-Leitlinie Kryptoglanduläre Analfistel, version 3.1, 2026 (AWMF 088-003)', 'https://register.awmf.org/assets/guidelines/088-003l_S3_Kryptoglandulaere_Analfisteln_2026-06.pdf')
PA2 = credit({'auteur': 'Dr. K.-H. Günther, Klinikum Main Spessart, Lohr am Main', 'licence': 'CC BY 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Perianalabszess_01.jpg'})
PA1 = credit({'auteur': 'Jump3now', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Perianalabscess.jpg'})
VEI = credit({'auteur': 'Finger74', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Anorectal_abscess.jpg'})
J6 = credit({'auteur': 'Finger74', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:6_Day_after_OP.JPG'})
FOU = credit({'auteur': 'M. K. Moslemi, M. A. Sadighi Gilani, A. A. Moslemi, A. Arabshahi', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Fournier_gangrene_01.jpg'})

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 42 ans, diabétique et en surpoids, consulte pour une douleur anale qui augmente depuis trois jours ; elle est devenue lancinante, l’empêche de s’asseoir et l’a réveillé cette nuit. À l’inspection, la marge anale droite est rouge, chaude et tuméfiée. <b>La question est donc la suivante : s’agit-il d’un ' + w('k61-abs', 'abcès anal') + ', et faut-il l’opérer tout de suite ou d’abord donner un antibiotique ?</b>',
 'Pour y répondre, le médecin doit d’abord comprendre d’où vient le pus : il naît le plus souvent d’une ' + w('k61-glande', 'glande anale') + ' infectée, située entre les deux sphincters. Ensuite, il doit situer l’abcès dans l’un des quatre espaces de la classification, car ce siège décide de la voie de drainage. De plus, il doit savoir que le traitement est chirurgical et urgent, et que l’antibiotique seul ne guérit pas l’abcès. Enfin, il doit prévoir la suite, car environ la moitié des patients développent ensuite une ' + w('k61-fst', 'fistule anale') + '.')
 + P('<i>Pourquoi ce cas ?</i> En effet, cet homme réunit les trois facteurs de risque établis par la S3 2026 : le sexe masculin, l’obésité et un diabète mal équilibré. Ainsi, contrairement à un manuel figé qui énumère des formes anatomiques, ce cours relie chaque espace à un signe clinique et à un geste ; chaque mot vert ouvre la définition, le critère ou l’image qui justifie la décision.')
 + key('Douleur anale croissante sur quelques jours, tuméfaction rouge et chaude : penser abcès → situer l’espace → drainer chirurgicalement sans attendre → ménager le sphincter → surveiller l’apparition d’une fistule.', 'Point de départ.'))

C.a(1, 'Définitions et épidémiologie', P(
 'Selon la S3 2026, l’abcès anal est une collection de pus de la région anale ou rectale qui naît, dans la grande majorité des cas, d’une infection des glandes du canal anal ; on parle donc d’infection ' + w('k61-crypto', 'cryptoglandulaire') + '. Par ailleurs, la S3 distingue cet abcès des abcès cutanés superficiels, qui naissent d’un follicule pileux ou d’une ' + w('k61-acne', 'acné inverse') + ' sans lien avec le canal anal ; c’est pourquoi le terme ancien d’« abcès périanal » mélange souvent deux maladies différentes.',
 'En outre, les études de population trouvent une incidence très variable, entre 9 et 60 cas pour 100 000 habitants par an ; l’âge moyen se situe entre 38 et 45 ans, et environ trois patients sur quatre ont entre 20 et 60 ans. De plus, les hommes sont atteints trois à quatre fois plus souvent que les femmes ; la S3 avance comme explication possible un nombre plus élevé de glandes anales chez l’homme et des différences hormonales, sans preuve définitive. Enfin, les facteurs de risque établis sont le sexe masculin, l’obésité et un diabète mal équilibré, alors que le lien avec le tabac et l’alcool reste moins net.')
 + P('Le code K61 se subdivise selon l’espace atteint, ce qui reprend en partie la classification anatomique décrite plus bas : abcès anal (K61.0), rectal (K61.1), ano-rectal (K61.2), ischio-rectal (K61.3) et intrasphinctérien (K61.4). Dès lors, le codage oblige déjà à se poser la question clinique essentielle, celle de l’espace infecté.')
 + key('L’abcès anal est le plus souvent cryptoglandulaire. Il touche surtout l’homme jeune, trois à quatre fois plus souvent que la femme, entre 38 et 45 ans en moyenne ; le sexe masculin, l’obésité et le diabète mal équilibré sont les facteurs de risque établis.')
 + src(ABS))

C.a(2, 'Physiopathologie : de la glande à l’espace infecté', P(
 'Les glandes anales siègent en règle dans l’espace intersphinctérien, c’est-à-dire entre le sphincter interne et le sphincter externe ; leur canal s’abouche dans une crypte de la ' + w('k61-pect', 'ligne pectinée') + '. Ainsi, lorsque ce canal s’obstrue, la sécrétion stagne et s’infecte, le plus souvent par Escherichia coli ou par des Bacteroides, c’est-à-dire par des germes de la flore digestive. De plus, les glandes sont plus nombreuses en arrière ; une étude a d’ailleurs trouvé 65 % des trajets fistuleux dans le secteur postérieur.',
 'Dès lors, l’abcès commence presque toujours dans l’espace intersphinctérien, puis le pus suit le chemin de moindre résistance. D’abord, il peut descendre vers la marge anale et former un abcès intersphinctérien superficiel. Ensuite, s’il traverse le sphincter externe, il gagne la graisse de la fosse ischio-anale et forme un ' + w('k61-ischio', 'abcès ischio-anal') + '. Enfin, s’il monte entre les sphincters au-dessus du releveur, il forme un ' + w('k61-supra', 'abcès supralévatorien') + '. C’est pourquoi la S3 retient quatre types : subanodermique, intersphinctérien, ischio-anal et supralévatorien.')
 + C.img('k61_abces_perianal2.gif', 'Photographie d’une marge anale : une tuméfaction rouge et luisante occupe le côté droit de l’anus et s’étend vers la fesse.', 'Abcès de la marge anale : tuméfaction rouge, tendue et asymétrique.', PA2)
 + P('<i>Que montre l’image ?</i> La tuméfaction est rouge, tendue et limitée à un côté ; ainsi, elle traduit une collection proche de la peau, typique d’un abcès subanodermique ou ischio-anal superficiel. Or, la peau reste fermée : le pus n’a pas d’issue, la pression monte et la douleur devient lancinante. C’est pourquoi l’ouverture chirurgicale soulage immédiatement, alors qu’un antibiotique ne peut pas pénétrer correctement une cavité close et mal vascularisée.')
 + table(['Type d’abcès', 'Fréquence selon les séries', 'Ce qui le caractérise'], [
   ['Subanodermique', '40 à 75 %', 'Il est superficiel, rouge et visible à l’inspection.'],
   ['Intersphinctérien', '13 à 55 %', 'Il est souvent invisible et ne se palpe qu’au toucher rectal.'],
   ['Ischio-anal', '5 à 42 %', 'Il a traversé le sphincter externe et occupe la graisse de la fesse.'],
   ['Supralévatorien', '2 à 8 %', 'Il siège au-dessus du releveur ; la douleur est pelvienne et diffuse, avec fièvre.']])
 + P('<i>Que montre le tableau ?</i> Les fréquences varient beaucoup d’une série à l’autre, car les auteurs n’utilisent pas tous la même classification ; cependant, les formes superficielles dominent toujours. En revanche, plus l’abcès est profond, moins il se voit ; c’est pourquoi un examen externe normal n’exclut pas un abcès intersphinctérien ou supralévatorien.')
 + key('Glande anale obstruée → infection par la flore digestive dans l’espace intersphinctérien → extension vers la marge, la fosse ischio-anale ou au-dessus du releveur. Plus l’abcès est profond, moins il se voit, et plus il expose à une fistule.')
 + src(ABS))

C.a(3, 'Diagnostic clinique', P(
 'Selon la S3 2026, le diagnostic repose sur l’anamnèse, l’inspection et la palpation. En effet, le symptôme typique est une tuméfaction douloureuse de la région anale, qui augmente en quelques jours ; dans les formes subanodermiques et ischio-anales, on trouve en règle une rougeur et une chaleur locales, et la palpation montre une induration douloureuse. Par ailleurs, l’abcès intersphinctérien ne se sent souvent qu’au toucher rectal ou bidigital ; cependant, ce toucher doit rester bref, car il est très douloureux. De plus, l’anuscopie et la rectoscopie apportent peu et font mal ; c’est pourquoi on peut le plus souvent s’en passer.',
 'En outre, l’anamnèse doit chercher des abcès antérieurs et la durée des symptômes, car une récidive oriente vers une fistule. Elle doit aussi chercher des signes de ' + w('k61-mici', 'maladie inflammatoire chronique de l’intestin') + ', puisqu’un abcès peut révéler une maladie de Crohn. Enfin, l’abcès supralévatorien trompe souvent : l’inspection est normale, la douleur est pelvienne, diffuse et progressive, et la fièvre ainsi que l’altération de l’état général sont plus fréquentes ; le toucher rectal trouve alors une induration haute, parfois fluctuante.')
 + C.img('k61_abces_veille.gif', 'Photographie de la région anale la veille d’une opération en urgence : la peau périanale est discrètement bombée et rosée d’un côté.', 'Abcès anorectal la veille du drainage : les signes externes peuvent être discrets.', VEI)
 + P('<i>Que montre l’image ?</i> Ici, la rougeur est discrète et la tuméfaction peu visible ; pourtant, le patient a été opéré en urgence. Ainsi, l’intensité de la douleur et le toucher rectal comptent davantage que l’aspect de la peau, car un abcès plus profond soulève peu la peau. C’est pourquoi une douleur anale intense sans lésion visible impose de chercher un abcès intersphinctérien ou supralévatorien.')
 + trap('Une douleur anale intense avec une marge normale n’est pas forcément une fissure : si la douleur est continue, lancinante et non liée aux selles, ou s’il y a de la fièvre, il faut chercher un abcès profond par le toucher rectal, puis par l’imagerie si le doute persiste.', 'Piège')
 + key('Le diagnostic est clinique : douleur croissante, tuméfaction rouge et chaude, induration douloureuse. L’abcès intersphinctérien ne se sent qu’au toucher rectal, et l’abcès supralévatorien se manifeste surtout par une douleur pelvienne diffuse et de la fièvre.')
 + src(ABS))

C.a(4, 'Gravité : sepsis et gangrène de Fournier', P(
 'La plupart des abcès restent localisés ; cependant, deux situations changent l’urgence. D’abord, un ' + w('k61-sepsis', 'sepsis') + ' avec fièvre élevée, hypotension ou confusion signifie que l’infection a franchi les défenses locales. Ensuite, la ' + w('k61-fournier', 'gangrène de Fournier') + ' est une infection nécrosante des tissus mous du périnée et des organes génitaux, qui s’étend rapidement le long des fascias. C’est pourquoi la S3 demande une imagerie en cas de sepsis sévère ou de suspicion de Fournier, afin de mesurer l’extension avant l’opération.',
 'Par ailleurs, la S3 cite comme terrains d’abcès récidivants ou graves l’immunosuppression, le VIH, les hémopathies et les cancers ; en effet, une défense immunitaire affaiblie limite la formation d’une paroi autour du pus. Dès lors, chez ces patients, l’antibiothérapie s’ajoute au drainage, et la surveillance doit être plus étroite.')
 + C.img('k61_fournier.gif', 'Photographie d’un patient après débridement d’une gangrène de Fournier : vaste plaie rouge du périnée, du scrotum et de la racine des cuisses.', 'Gangrène de Fournier après débridement étendu et dérivation digestive.', FOU)
 + P('<i>Que montre l’image ?</i> Le chirurgien a dû exciser une grande partie de la peau du périnée et des bourses, car les tissus étaient nécrosés ; de plus, une colostomie a été réalisée pour détourner les selles de la plaie. Ainsi, l’image montre ce que l’on cherche à éviter : une infection anale négligée peut devenir une nécrose étendue. C’est pourquoi une douleur disproportionnée, des crépitations ou une peau violacée imposent une chirurgie immédiate.')
 + alert('Fièvre élevée, hypotension, douleur disproportionnée, crépitations sous-cutanées ou peau violacée du périnée : suspecter un sepsis ou une gangrène de Fournier, faire une imagerie, débuter les antibiotiques et opérer en urgence.', 'Gravité d’abord.')
 + key('Un sepsis ou une suspicion de gangrène de Fournier imposent une imagerie, des antibiotiques et une chirurgie immédiate ; l’immunosuppression favorise les formes graves et les récidives.')
 + src(ABS))

C.a(5, 'Traitement : drainer, et non temporiser', P(
 'Selon la S3 2026, le traitement de l’abcès anal est chirurgical ; c’est l’intensité des symptômes qui fixe le moment de l’intervention, et l’abcès aigu constitue en principe une indication d’urgence. En effet, une régression spontanée est extrêmement rare, et un traitement antibiotique seul n’a pas de chance de succès ; c’est pourquoi la S3 demande de ne pas retarder l’opération. De plus, une ponction avec lavage et antibiotiques donne plus de récidives que l’opération. Enfin, même si l’abcès s’est ouvert spontanément, une intervention semi-élective reste recommandée, car l’orifice spontané est souvent trop petit pour drainer toute la cavité.',
 'Ensuite, la voie d’abord dépend du siège : on draine par voie périanale les abcès subanodermiques et ischio-anaux, et par voie transrectale certains abcès intersphinctériens hauts ou supralévatoriens. Ainsi, le but est un ' + w('k61-drain', 'drainage large') + ' du foyer infecté, sans léser les structures saines, en particulier le sphincter. Par ailleurs, l’opération doit se faire avec une anesthésie suffisante, afin de pouvoir inspecter le canal anal sans douleur ; en revanche, aucune préparation intestinale n’est nécessaire.')
 + table(['Décision', 'Ce que recommande la S3 2026', 'Pourquoi'], [
   ['Moment de l’opération', 'L’abcès aigu est une urgence ; les symptômes fixent le délai.', 'Le pus enfermé progresse vers les espaces voisins.'],
   ['Antibiotique seul', 'Il n’est pas recommandé.', 'Il pénètre mal une cavité close et ne vide pas le pus.'],
   ['Ouverture spontanée', 'On fait quand même une intervention semi-élective.', 'L’orifice spontané draine mal et favorise la récidive.'],
   ['Prélèvement bactériologique', 'On peut s’en passer dans un abcès non compliqué.', 'Le résultat ne change pas la conduite.'],
   ['Histologie', 'Elle est obligatoire si l’aspect est suspect.', 'Elle exclut un cancer et protège sur le plan médico-légal.']])
 + P('<i>Que montre le tableau ?</i> Toutes les décisions découlent d’un même principe : l’abcès est une cavité fermée, que seule l’ouverture guérit. Or, ce principe explique aussi les exceptions ; ainsi, l’histologie redevient nécessaire lorsque la cavité pourrait être autre chose qu’un abcès simple, par exemple une tumeur nécrosée.')
 + key('L’abcès se draine chirurgicalement en urgence, par voie périanale ou transrectale selon son siège, largement et sans léser le sphincter ; l’antibiotique seul et la ponction simple ne suffisent pas, et un abcès ouvert spontanément se reprend quand même.')
 + src(ABS))

C.a(6, 'L’abcès et la fistule', P(
 'L’abcès et la fistule sont deux étapes d’une même maladie : l’abcès est la phase aiguë de l’infection de la glande, alors que la fistule en est la phase chronique, c’est-à-dire le trajet qui persiste entre la crypte et la peau. Ainsi, selon la S3, environ 50 % des patients développent une fistule après l’incision d’un abcès, le plus souvent dans les 12 mois. De plus, ce risque dépend du siège : une étude prospective a trouvé une fistule chez 4 % des abcès subanodermiques, 36 % des intersphinctériens et 48 % des ischio-anaux ; c’est pourquoi les abcès ischio-anaux et supralévatoriens sont ceux qui donnent le plus de fistules.',
 'Dès lors, que faire d’une fistule découverte pendant le drainage ? D’abord, la S3 demande de la chercher avec beaucoup de prudence et de ne jamais forcer sa mise en évidence, car une sonde poussée en force crée un faux trajet et peut léser le sphincter. Ensuite, si la fistule est certainement superficielle, un opérateur expérimenté peut la mettre à plat dans le même temps. En revanche, si elle est haute ou si le trajet est incertain, la cure doit attendre une seconde intervention ; dans ce cas, on pose un ' + w('k61-seton', 'séton de drainage') + ', et le patient doit en être informé avant l’opération.')
 + P('Enfin, la S3 cite comme facteurs de risque d’une fistule secondaire le sexe féminin, l’âge plus élevé, le diabète de type 2 mal équilibré et la maladie de Crohn ; de plus, une CRP élevée, une grande cavité, un siège profond et un drainage insuffisant favorisent la récidive de l’abcès. Par conséquent, un abcès qui récidive au même endroit doit faire chercher une fistule et une maladie de Crohn.')
 + key('Environ un patient sur deux développe une fistule après un abcès, surtout après un abcès ischio-anal ou supralévatorien. On ne force jamais la recherche d’une fistule ; on met à plat une fistule superficielle évidente, mais on draine une fistule haute par séton avant une cure secondaire (cours K60).')
 + src(ABS, FST))

C.a(7, 'Après l’opération : soins de plaie et complications', P(
 'Après le drainage, la plaie doit rester ouverte ; en effet, si l’orifice externe se ferme trop tôt, le pus se reforme en dessous. Ainsi, la S3 demande de veiller à ce que l’ouverture ne se referme pas prématurément et de nettoyer régulièrement la plaie par une ' + w('k61-douche', 'douche à l’eau du robinet') + ', qui suffit si elle est de qualité potable. En revanche, les antiseptiques locaux exposent à une toxicité pour les cellules qui cicatrisent ; de plus, la S3 demande de renoncer aux méchages répétés, qui font mal sans améliorer la guérison.',
 'Par ailleurs, les complications précoces sont surtout le saignement et la ' + w('k61-retention', 'rétention urinaire') + ' ; cette dernière n’est pas propre à l’abcès, et elle est favorisée par une antalgie insuffisante et par trop de perfusions intraveineuses. En outre, une incontinence n’est pas attendue après un drainage bien fait ; elle survient plutôt lorsqu’on a coupé trop de muscle en cherchant une fistule, ou lorsque l’inflammation étendue a laissé un rectum cicatriciel moins compliant.')
 + C.img('k61_plaie_j6.gif', 'Photographie de la marge anale six jours après le drainage : petite plaie ouverte, rouge et propre, sur le côté de l’anus.', 'Plaie de drainage au 6e jour : elle cicatrise de la profondeur vers la surface.', J6)
 + P('<i>Que montre l’image ?</i> Six jours après l’opération, la plaie est encore ouverte, rouge et propre, sans pus ni rougeur autour ; ainsi, elle cicatrise de la profondeur vers la surface, ce qui empêche une nouvelle collection. C’est pourquoi le patient doit la doucher après chaque selle plutôt que de la couvrir hermétiquement.')
 + key('La plaie reste ouverte et se douche à l’eau du robinet ; on évite les méchages répétés et les antiseptiques. Les complications précoces sont le saignement et la rétention urinaire, alors que l’incontinence est rare si le sphincter a été ménagé.')
 + src(ABS))

C.a(8, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons le patient du début. La tuméfaction rouge, chaude et douloureuse de la marge droite signe un abcès superficiel ; comme il n’a ni fièvre élevée ni signe de nécrose, aucune imagerie n’est nécessaire. Ainsi, il est opéré le jour même sous anesthésie : on ouvre largement la cavité par voie périanale, sans chercher en force une fistule, et l’on adresse le tissu en histologie seulement s’il paraît suspect.',
 'Ensuite, il douche sa plaie plusieurs fois par jour, sans méchage, et il ne reçoit pas d’antibiotique, car le drainage est complet et il n’est pas immunodéprimé. Cependant, son diabète augmente le risque de fistule et de récidive ; c’est pourquoi on équilibre la glycémie et on le revoit, en lui expliquant qu’un écoulement persistant dans les mois suivants signerait une fistule.')
 + C.pareto('pareto-k61-clinique', 'Abcès anal', ['k61-1', 'k61-2', 'k61-3', 'k61-4', 'k61-5', 'k61-6', 'k61-7'],
     ['Une douleur anale croissante avec tuméfaction chaude évoque un abcès.',
      'Un examen externe normal n’exclut pas un abcès profond.',
      'Le sepsis ou la suspicion de Fournier imposent une imagerie et une chirurgie immédiate.',
      'On draine chirurgicalement, sans attendre l’effet d’un antibiotique.',
      'On ne force jamais la recherche d’une fistule.',
      'L’antibiotique n’est utile que dans des situations d’exception.',
      'Environ la moitié des patients développent une fistule dans l’année.'])
 + key('Le patient a un abcès superficiel : on le draine en urgence, on douche la plaie et l’on ne donne pas d’antibiotique. On équilibre son diabète et on surveille l’apparition d’une fistule pendant l’année qui suit.')
 + src(ABS))

C.a(9, 'Critères formels et paramètres clés', alert(
 '<p>Selon la S3 2026, l’<b>abcès anal cryptoglandulaire</b> naît d’une glande de l’espace intersphinctérien et se classe en quatre types : subanodermique, intersphinctérien, ischio-anal et supralévatorien. Une <b>imagerie</b> (échographie endoanale, IRM ou scanner) est indiquée si le tableau est incertain, en cas de sepsis sévère ou si l’on suspecte une gangrène de Fournier.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> L’incidence varie de 9 à 60 pour 100 000 habitants par an, avec un rapport hommes-femmes de 3-4 pour 1. Les abcès subanodermiques représentent 40 à 75 % des cas et les supralévatoriens 2 à 8 %. Environ 50 % des patients développent une fistule, le plus souvent dans les 12 mois ; quand l’antibiothérapie est indiquée, elle dure 5 à 7 jours.</div>'
 + src(ABS))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Dans la plupart des cas, l’examen clinique suffit, et une imagerie retarderait inutilement le drainage ; en revanche, l’imagerie devient nécessaire lorsque l’abcès est profond ou que l’on suspecte une forme grave.')
 + table(['Question', 'Examen', 'Quand ?'], [
   ['Y a-t-il un abcès superficiel ?', 'Inspection et palpation', 'Toujours'],
   ['L’abcès est-il intersphinctérien ou haut ?', 'Toucher rectal ou bidigital, bref', 'Si la marge paraît normale malgré une forte douleur'],
   ['Où est l’abcès, et jusqu’où s’étend-il ?', w('k61-eus', 'Échographie endoanale') + ', ' + w('k61-irm', 'IRM pelvienne') + ' ou scanner', 'Tableau incertain, sepsis sévère, suspicion de Fournier'],
   ['Faut-il un prélèvement ?', 'Bactériologie du pus', 'Pas dans l’abcès non compliqué ; elle est utile chez l’immunodéprimé ou dans une infection grave'],
   ['La cavité est-elle autre chose ?', 'Histologie du tissu excisé', 'Aspect suspect, par exemple pour exclure un cancer']])
 + P('<i>Que montre le tableau ?</i> Chaque examen répond à une question précise ; ainsi, on ne demande pas d’IRM pour un abcès visible, mais on la demande pour un abcès qu’on ne voit pas. De plus, la S3 rappelle que l’échographie endoanale est parfois trop douloureuse pour être faite sans anesthésie, alors que l’IRM se fait sans douleur, même en urgence.')
 + key('L’abcès typique se diagnostique cliniquement ; l’imagerie sert aux abcès profonds, au sepsis sévère et à la suspicion de Fournier, et l’histologie aux aspects suspects.')
 + C.pareto('pareto-k61-examens', 'Examens', ['k61-e-1'],
     ['L’inspection et la palpation suffisent le plus souvent.',
      'Le toucher rectal cherche un abcès intersphinctérien ou haut.',
      'L’IRM localise un abcès profond sans douleur.',
      'Le prélèvement bactériologique est inutile dans l’abcès simple.'])
 + src(ABS))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : quatre espaces autour du canal anal', P(
 'Le canal anal est entouré du sphincter interne, lisse, puis du sphincter externe, strié ; entre les deux se trouve l’espace intersphinctérien, où siègent les glandes. Ainsi, en dehors du sphincter externe s’étend la fosse ischio-anale, remplie de graisse, et, au-dessus du muscle releveur de l’anus, l’espace supralévatorien. Or, ces espaces communiquent par des chemins anatomiques ; c’est pourquoi un abcès peut faire le tour de l’anus en fer à cheval ou monter vers le pelvis.')
 + key('Le siège de la glande explique le point de départ intersphinctérien ; les espaces voisins expliquent les formes ischio-anales, supralévatoriennes et en fer à cheval.', 'Science → clinique.'))
C.s('immuno', 'Immunologie', 'Immunologie : pourquoi un abcès est une cavité fermée', P(
 'Face à une infection bactérienne, les polynucléaires neutrophiles affluent, détruisent les germes puis meurent ; le pus est donc un mélange de neutrophiles morts, de bactéries et de tissu détruit. Ainsi, une paroi inflammatoire se forme autour de lui et isole l’infection, ce qui protège l’organisme mais empêche aussi les antibiotiques circulants d’atteindre le centre de la collection. De plus, le pus est pauvre en oxygène et riche en germes, ce qui réduit encore l’efficacité des antibiotiques. C’est pourquoi l’ouverture chirurgicale reste le seul traitement curatif, et pourquoi l’immunodéprimé, qui forme mal cette paroi, fait des infections plus diffuses.')
 + key('Le pus est enfermé dans une paroi que les antibiotiques franchissent mal ; seule l’ouverture vide la cavité.', 'Science → traitement.'))
C.s('micro', 'Microbiologie', 'Microbiologie : une flore digestive mixte', P(
 'Les germes de l’abcès cryptoglandulaire viennent du contenu digestif ; il s’agit surtout d’Escherichia coli et de Bacteroides, c’est-à-dire d’une flore mixte aérobie et anaérobie. Ainsi, lorsqu’un antibiotique est indiqué, il doit couvrir ces deux groupes. Par ailleurs, une flore cutanée, par exemple staphylococcique, oriente plutôt vers un abcès d’origine cutanée sans lien avec le canal anal ; cette distinction a une conséquence pratique, car un tel abcès ne donne pas de fistule.')
 + key('Une flore digestive mixte signe une origine cryptoglandulaire, alors qu’une flore cutanée oriente vers un abcès de la peau.', 'Science → pronostic.'))

# ---------------- Pharmacologie
C.p(1, 'Antibiotiques : seulement dans des situations précises', P(
 'Selon la S3 2026, il ne faut pas donner systématiquement un antibiotique après un drainage adéquat (recommandation de grade B). En effet, les études sur la prévention de la fistule se contredisent : un essai randomisé de 2017 a trouvé moins de fistules après 7 jours de ceftriaxone et de métronidazole (14 % contre 30 %), alors qu’un essai randomisé en double aveugle de 2011 a trouvé davantage de fistules secondaires dans le groupe traité (37 % contre 22 %). Ainsi, la S3 juge le bénéfice non démontré et retient le risque de résistances et d’effets indésirables.',
 'En revanche, la S3 recommande une antibiothérapie de 5 à 7 jours dans quatre situations : une immunosuppression, une hémopathie immunosuppressive, une infection étendue des tissus mous et des signes infectieux systémiques. Dès lors, le choix de la molécule doit couvrir la flore digestive aérobie et anaérobie ; cependant, la S3 ne fixe ni molécule ni dose, et aucun référentiel suisse consacré à l’abcès anal n’a été lu pour ce cours. C’est pourquoi la molécule et la posologie doivent suivre le protocole local d’antibiothérapie de l’hôpital (TODO : source suisse à identifier).')
 + table(['Situation', 'Antibiotique ?', 'Justification'], [
   ['Abcès simple, bien drainé', 'Non', 'Le drainage suffit, et la prévention de la fistule n’est pas démontrée.'],
   ['Immunosuppression ou hémopathie', 'Oui, 5 à 7 jours', 'Les défenses ne limitent pas la diffusion de l’infection.'],
   ['Infection étendue des tissus mous', 'Oui, 5 à 7 jours', 'Le drainage n’atteint pas toute la cellulite autour de la cavité.'],
   ['Signes infectieux systémiques', 'Oui, 5 à 7 jours', 'Les germes ont gagné la circulation.']])
 + P('<i>Que montre le tableau ?</i> L’antibiotique traite ce que le bistouri n’atteint pas : la cellulite autour de la cavité, la bactériémie ou l’infection d’un patient sans défenses. À l’inverse, il n’apporte rien lorsque tout le pus a été évacué ; c’est pourquoi on ne le prescrit pas « pour être sûr ».')
 + key('Pas d’antibiotique systématique après un bon drainage ; une antibiothérapie de 5 à 7 jours, couvrant la flore digestive mixte, est réservée à l’immunosuppression, aux hémopathies, aux infections étendues et aux signes systémiques.')
 + src(ABS))

C.p(2, 'Antalgie, soins et surveillance', alert(
 'On revoit le patient si la fièvre réapparaît, si la douleur augmente de nouveau ou si la plaie se ferme alors qu’elle suinte encore, car ces signes évoquent une collection résiduelle. Par ailleurs, une rétention urinaire après l’opération doit être cherchée, surtout si l’antalgie était insuffisante.', 'Sécurité.')
 + P('L’antalgie doit être suffisante, car la douleur favorise la rétention urinaire et gêne la toilette de la plaie ; de plus, la S3 n’impose pas de molécule particulière. Ensuite, la surveillance se prolonge pendant environ un an, car c’est le délai d’apparition de la plupart des fistules ; ainsi, un écoulement persistant ou un abcès récidivant au même endroit doivent faire adresser le patient au proctologue.')
 + key('Une antalgie suffisante prévient la rétention urinaire ; la reprise de la douleur ou de la fièvre fait chercher une collection résiduelle, et un écoulement persistant pendant l’année suivante signe une fistule.')
 + C.pareto('pareto-k61-pharma', 'Antibiotiques et soins', ['k61-p-1', 'k61-p-2'],
     ['L’antibiotique ne remplace jamais le drainage.',
      'Il est réservé à l’immunosuppression, aux infections étendues et aux signes systémiques.',
      'Sa durée est de 5 à 7 jours.',
      'On douche la plaie et l’on évite les méchages répétés.'])
 + src(ABS))

# ---------------- Fenêtres
L = lab
C.pop('k61-abs', 'Abcès anal', L(('Définition', 'C’est une collection de pus de la région anale ou rectale, née le plus souvent d’une glande anale infectée.'), ('Signes', 'Le patient décrit une douleur qui augmente en quelques jours, avec une tuméfaction rouge, chaude et douloureuse.'), ('Traitement', 'On le draine chirurgicalement en urgence, car un antibiotique seul ne vide pas la cavité.')) + C.img('k61_abces_perianal.gif', 'Marge anale avec tuméfaction luisante et douloureuse à côté de l’anus.', 'Abcès douloureux de la marge anale.', PA1) + src(ABS))
C.pop('k61-glande', 'Glande anale', L(('Siège', 'Elle se trouve dans l’espace entre les deux sphincters, et son canal s’ouvre dans une crypte de la ligne pectinée.'), ('Rôle dans la maladie', 'Si son canal s’obstrue, la sécrétion s’infecte ; c’est le point de départ de presque tous les abcès et de presque toutes les fistules.')) + src(ABS))
C.pop('k61-crypto', 'Infection cryptoglandulaire', L(('Définition', 'C’est l’infection d’une glande anale, qui s’ouvre dans une crypte du canal anal.'), ('Pourquoi ce terme ?', 'Il distingue l’abcès lié au canal anal, qui peut donner une fistule, de l’abcès de la peau, qui n’en donne pas.')) + src(ABS))
C.pop('k61-acne', 'Acné inverse', L(('Nature', 'C’est une maladie inflammatoire chronique des follicules pileux des plis, qui donne des nodules et des abcès récidivants.'), ('Pourquoi la distinguer ?', 'Ses abcès ne communiquent pas avec le canal anal ; ils relèvent donc d’une autre prise en charge, dermatologique et chirurgicale.')) + src(ABS))
C.pop('k61-fst', 'Fistule anale', L(('Définition', 'C’est un trajet infecté qui relie une crypte du canal anal à la peau.'), ('Lien avec l’abcès', 'Environ la moitié des patients en développent une après un abcès, en général dans les 12 mois.'), ('Traitement', 'Il est chirurgical ; il est détaillé dans le cours K60.')) + src(ABS, FST))
C.pop('k61-pect', 'Ligne pectinée', L(('Définition', 'C’est la ligne festonnée du canal anal où s’ouvrent les cryptes et les glandes anales.'), ('Intérêt', 'Elle marque l’origine des abcès cryptoglandulaires ; de plus, sous cette ligne, la muqueuse est sensible, ce qui explique la douleur intense.')) + src(ABS))
C.pop('k61-ischio', 'Abcès ischio-anal', L(('Mécanisme', 'Le pus a traversé le sphincter externe et occupe la graisse de la fosse ischio-anale.'), ('Signes', 'La fesse est tuméfiée, rouge et chaude, parfois sur une large surface.'), ('Pronostic', 'Il donne souvent une fistule, chez près de la moitié des patients dans une étude prospective.')) + src(ABS))
C.pop('k61-supra', 'Abcès supralévatorien', L(('Siège', 'Il se trouve au-dessus du muscle releveur de l’anus.'), ('Signes', 'L’inspection est souvent normale ; le patient a une douleur pelvienne diffuse, de la fièvre et un malaise général, et le toucher rectal trouve une induration haute.'), ('Conduite', 'On le localise par imagerie, puis on choisit la voie de drainage, parfois transrectale.')) + src(ABS))
C.pop('k61-mici', 'Maladie inflammatoire chronique de l’intestin', L(('Lien', 'La maladie de Crohn peut se révéler par un abcès ou une fistule anale.'), ('Indices', 'On y pense devant des abcès récidivants, des fistules multiples, une diarrhée chronique ou un amaigrissement.'), ('Pourquoi c’est important', 'La prise en charge est alors médicale et chirurgicale à la fois ; elle est décrite dans le cours K50.')) + src(ABS))
C.pop('k61-sepsis', 'Sepsis', L(('Définition', 'C’est une défaillance d’organe causée par une réponse déréglée de l’organisme à une infection.'), ('Signes d’alerte', 'On s’inquiète devant une fièvre élevée, une hypotension, une tachycardie ou une confusion.'), ('Conséquence', 'La S3 demande alors une imagerie avant l’opération, et l’on ajoute des antibiotiques au drainage.')) + src(ABS))
C.pop('k61-fournier', 'Gangrène de Fournier', L(('Définition', 'C’est une infection nécrosante des tissus mous du périnée et des organes génitaux.'), ('Signes', 'On la suspecte devant une douleur disproportionnée, une peau violacée ou noire, des crépitations et un sepsis.'), ('Conduite', 'On fait une imagerie si elle ne retarde pas le geste, on débute les antibiotiques et l’on excise chirurgicalement tous les tissus nécrosés en urgence.')) + C.img('k61_fournier.gif', 'Périnée après débridement étendu d’une gangrène de Fournier.', 'Gangrène de Fournier après débridement.', FOU) + src(ABS))
C.pop('k61-drain', 'Drainage large', L(('Geste', 'On ouvre largement la cavité, on évacue le pus et l’on laisse la plaie ouverte.'), ('Pourquoi large ?', 'Un drainage insuffisant est la principale cause de récidive ; de plus, la S3 recommande une reprise sous anesthésie si l’abcès est étendu.'), ('Limite', 'On ne coupe pas le sphincter pour drainer, afin de préserver la continence.')) + src(ABS))
C.pop('k61-seton', 'Séton de drainage', L(('Principe', 'Un fil passé dans le trajet fistuleux maintient l’orifice ouvert, si bien que le pus s’écoule.'), ('Indication', 'On le pose lorsqu’on découvre une fistule haute pendant le drainage, en attendant une cure secondaire.'), ('Information', 'La S3 demande d’en parler au patient avant l’opération.')) + src(ABS))
C.pop('k61-douche', 'Douche de la plaie', L(('Geste', 'Le patient rince la plaie à l’eau du robinet, en particulier après chaque selle.'), ('Pourquoi ?', 'Le rinçage empêche l’accumulation de pus et la fermeture trop rapide de l’orifice ; de plus, l’eau potable suffit, alors que les antiseptiques abîment les cellules qui cicatrisent.')) + C.img('k61_plaie_j6.gif', 'Plaie de drainage propre, six jours après l’opération.', 'Plaie au 6e jour.', J6) + src(ABS))
C.pop('k61-retention', 'Rétention urinaire postopératoire', L(('Mécanisme', 'La douleur anale inhibe par réflexe le relâchement du sphincter de la vessie, et l’excès de perfusion remplit vite la vessie.'), ('Prévention', 'On assure une antalgie suffisante et l’on évite un excès de liquides intraveineux.')) + src(ABS))
C.pop('k61-eus', 'Échographie endoanale', L(('Principe', 'Une sonde placée dans le canal montre les sphincters, l’abcès et un éventuel trajet fistuleux.'), ('Limite', 'Elle peut être trop douloureuse dans l’abcès aigu et demander une sédation.')) + src(ABS, FST))
C.pop('k61-irm', 'IRM pelvienne', L(('Intérêt', 'Elle montre l’abcès, son extension et le trajet d’une fistule par rapport aux sphincters et au releveur.'), ('Avantage', 'Elle ne fait pas mal et se réalise aussi en urgence ; elle aide donc à choisir la voie de drainage d’un abcès profond.')) + src(ABS))

C.termes = [
 (r'abcès anal', 'k61-abs'), (r'glandes? anales?', 'k61-glande'), (r'cryptoglandulaire', 'k61-crypto'), (r'acné inverse', 'k61-acne'),
 (r'fistule anale', 'k61-fst'), (r'ligne pectinée', 'k61-pect'), (r'abcès ischio-anal', 'k61-ischio'), (r'abcès supralévatorien', 'k61-supra'),
 (r'maladie de Crohn', 'k61-mici'), (r'sepsis', 'k61-sepsis'), (r'gangrène de Fournier', 'k61-fournier'), (r'drainage large', 'k61-drain'),
 (r'séton', 'k61-seton'), (r'rétention urinaire', 'k61-retention'), (r'échographie endoanale', 'k61-eus'), (r'IRM', 'k61-irm'),
]

C.write()
