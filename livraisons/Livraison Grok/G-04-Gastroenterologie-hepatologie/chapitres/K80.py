import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K80', 'Lithiase biliaire : colique, cholécystite aiguë, calculs de la voie biliaire principale et angiocholite',
    'K80 — Cholélithiase · CIM-10-GM 2024 · Voies biliaires',
    'Adulte · lithiase vésiculaire et cholédocienne, cholécystite aiguë lithiasique, angiocholite · rédaction du 09.10.2026 · référentiels EASL 2016, ESGE 2019, WSES 2020, directive suisse KSSG Cholécystite/Angiocholite (validée le 02.02.2026), informations professionnelles suisses',
    'Pharmacologie de la lithiase biliaire')
w = C.w
EASL = ('EASL Clinical Practice Guidelines on the prevention, diagnosis and treatment of gallstones, J Hepatol 2016;65:146-181', 'https://easl.eu/wp-content/uploads/2016/10/EASL-CPG-Gallstones.pdf')
ESGE = ('Manes G. et al., ESGE, prise en charge endoscopique des calculs de la voie biliaire principale, Endoscopy 2019;51:472-491', 'https://www.esge.com/assets/downloads/pdfs/guidelines/2019_a_0862_0346.pdf')
WSES = ('Pisano M. et al., 2020 WSES updated guidelines for the diagnosis and treatment of acute calculus cholecystitis, World J Emerg Surg 2020;15:61', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7643471/')
KSSG = ('Babouee Flury B., Flury D., Schlegel M. (validation Boggian K.), Cholezystitis/Cholangitis, directive d’infectiologie KSSG / HOCH Health Ostschweiz, guidelines.ch, validée le 02.02.2026', 'https://kssg.guidelines.ch/guideline/58/de')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS via AmiKo), consultée le 09.10.2026', 'https://amiko.oddb.org/fr')

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 47 ans, en surpoids, consulte pour une douleur de l’hypocondre droit qui dure depuis 10 heures, avec fièvre à 38,4 °C. Or, elle décrit depuis un an des crises brèves de même siège après les repas, qui cédaient en une heure. <b>La question n’est donc plus seulement de reconnaître une colique hépatique, mais de savoir si une complication est en cours et laquelle.</b>',
 'Pour répondre à cette question, le médecin doit savoir : distinguer la ' + w('k80-colique', 'colique biliaire') + ' simple de la ' + w('k80-cholecystite', 'cholécystite aiguë') + ' ; confirmer les calculs par l’' + w('k80-echo', 'échographie') + ' ; estimer le ' + w('k80-risque-vbp', 'risque de calcul de la voie biliaire principale') + ' ; reconnaître et classer une ' + w('k80-angiocholite', 'angiocholite') + ' selon Tokyo 2018 ; enfin, fixer le moment de la ' + w('k80-cholecystectomie', 'cholécystectomie laparoscopique') + ' et de la ' + w('k80-cpre', 'CPRE') + '.')
 + key(w('k80-colique', 'Colique') + ' : douleur brève ; ' + w('k80-cholecystite', 'cholécystite') + ' : douleur prolongée, fièvre, signe de Murphy ; ' + w('k80-angiocholite', 'angiocholite') + ' : fièvre, frissons, ictère.', 'Point de départ.'))

C.a(1, 'Définition et formes', P(
 'La lithiase biliaire est la présence de calculs dans la vésicule ou dans les voies biliaires. Ainsi, l’EASL 2016 distingue trois types : les ' + w('k80-cholesterol', 'calculs de cholestérol') + ', qui représentent 90 à 95 % des calculs dans les populations occidentales ; les calculs pigmentaires noirs, surtout en cas d’hémolyse chronique ou de cirrhose ; enfin, les calculs pigmentaires bruns, qui se forment surtout dans la voie biliaire principale. De plus, les calculs de cholestérol et les pigmentaires noirs naissent presque toujours dans la vésicule.',
 'À partir de ces types, la clinique se décline en plusieurs formes. D’une part, la lithiase peut rester asymptomatique ; d’autre part, elle peut provoquer une colique biliaire, puis des complications : cholécystite aiguë, calcul de la voie biliaire principale, angiocholite et ' + w('k80-pancreatite', 'pancréatite biliaire') + '.')
 + table(['Forme', 'Mécanisme', 'Conséquence'], [
   ['Lithiase asymptomatique', 'Calculs sans symptôme', 'Pas de traitement systématique'],
   ['Colique biliaire', 'Obstruction transitoire du collet ou du canal cystique', 'Cholécystectomie, le plus tôt possible'],
   ['Cholécystite aiguë', 'Obstruction prolongée et inflammation de la paroi', 'Cholécystectomie précoce'],
   ['Calcul de la voie biliaire principale', 'Migration ou formation dans le cholédoque', 'Extraction'],
   ['Angiocholite', 'Obstruction et infection de la voie biliaire', 'Antibiotiques et drainage urgent']])
 + P('Le tableau se lit de haut en bas : en effet, chaque forme ajoute un degré d’obstruction ou d’infection, si bien que l’urgence augmente.')
 + C.img('k80_calculs_macro.gif', 'Photographie d’une vésicule biliaire ouverte remplie de nombreux calculs facettés sombres.', 'Vésicule biliaire ouverte contenant de nombreux calculs facettés. Les facettes naissent du frottement des calculs entre eux dans la vésicule.', credit({'auteur': 'Emmanuelm', 'licence': 'CC BY 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Gallstones.jpg'}))
 + key('Cholestérol 90 à 95 % ; pigmentaires noirs dans la vésicule (hémolyse, cirrhose), bruns dans la voie biliaire. Colique, cholécystite, calcul cholédocien, angiocholite, pancréatite.')
 + src(EASL))

C.a(2, 'Épidémiologie et histoire naturelle', P(
 'Après la définition, la fréquence situe l’enjeu. Ainsi, selon l’EASL 2016, la lithiase biliaire touche jusqu’à 20 % de la population en Europe ; c’est la maladie digestive qui motive le plus d’hospitalisations dans les pays européens. De plus, sa fréquence augmente avec l’âge et elle est plus élevée chez la femme.',
 'Cependant, environ 80 % des porteurs restent asymptomatiques. En effet, les symptômes apparaissent chez 1 à 4 % des porteurs par an, et 20 % deviennent symptomatiques en 20 ans. Par conséquent, le risque de complication est faible sans symptôme (0,1 à 0,3 % par an), alors qu’il atteint 1 à 3 % par an après une première colique (EASL 2016).')
 + trap('Aucune donnée nationale suisse de prévalence n’a été retrouvée lors de la rédaction ; les chiffres cités sont européens et attribués à l’EASL 2016.', 'Lacune documentaire')
 + key('Jusqu’à 20 % de la population ; 80 % asymptomatiques ; complications 0,1 à 0,3 %/an sans symptôme, 1 à 3 %/an après une colique.')
 + src(EASL))

C.a(3, 'Facteurs de risque et prévention', P(
 'Pour comprendre la prévention, il faut connaître les facteurs de risque. Ainsi, les calculs de cholestérol sont liés au ' + w('k80-metabolique', 'syndrome métabolique') + ' : obésité, diabète et insulinorésistance. De plus, certaines situations favorisent la lithiase : la ' + w('k80-perte-poids', 'perte de poids rapide') + ' (régime très hypocalorique, chirurgie bariatrique), les analogues de la somatostatine, la nutrition parentérale totale et le traitement hormonal substitutif. Enfin, les calculs pigmentaires noirs s’associent à l’hémolyse chronique, par exemple la sphérocytose héréditaire ou la drépanocytose.',
 'Par conséquent, l’EASL 2016 propose un mode de vie sain, une activité physique régulière et le maintien d’un poids idéal (recommandation faible). En revanche, la prévention médicamenteuse n’est pas conseillée dans la population générale. Toutefois, lors d’une perte de poids rapide, l’' + w('k80-d-audc', 'acide ursodésoxycholique') + ' à au moins 500 mg par jour jusqu’à la stabilisation du poids peut être recommandé.')
 + key('Syndrome métabolique, perte de poids rapide, somatostatine, nutrition parentérale, hormones ; hémolyse pour les pigmentaires. Perte de poids rapide : acide ursodésoxycholique ≥ 500 mg/j.')
 + src(EASL))

C.a(4, 'Physiopathologie', P(
 'La formation d’un calcul de cholestérol exige trois conditions. D’abord, la bile est sursaturée en cholestérol ; ensuite, ce cholestérol cristallise ; enfin, une vésicule hypomobile retient les cristaux, qui grossissent. De plus, le ' + w('k80-sludge', 'sludge biliaire') + ' apparaît avec la stase et la réduction du cycle entéro-hépatique ; cependant, selon l’EASL 2016, il n’est pas en lui-même la cause des calculs.',
 'Ensuite, les symptômes naissent de l’obstruction. En effet, un calcul enclavé au collet ou dans le canal cystique distend la vésicule : c’est la colique, qui cède quand le calcul se dégage. Or, si l’obstruction persiste, la paroi s’œdématie, s’inflamme puis se surinfecte par des germes digestifs ; c’est ainsi que survient la cholécystite. Enfin, un calcul qui migre dans le cholédoque peut obstruer la voie biliaire et l’ampoule, ce qui expose à l’angiocholite et à la pancréatite.')
 + key('Sursaturation, cristallisation, hypomobilité vésiculaire ; obstruction transitoire = colique, persistante = cholécystite, cholédocienne = angiocholite ou pancréatite.')
 + src(EASL))

C.a(5, 'Clinique : colique biliaire et cholécystite', P(
 'La démarche commence donc par la clinique. Selon l’EASL 2016, la colique biliaire est une douleur intense de l’hypocondre droit ou de l’épigastre, durant au moins 15 à 30 minutes, irradiant vers le dos ou l’épaule droite et soulagée par les antalgiques. En effet, seuls trois symptômes sont associés de façon significative aux calculs : la colique, la douleur irradiée et le recours aux antalgiques.',
 'À l’inverse, la cholécystite aiguë est suspectée devant une fièvre, une douleur intense de l’hypocondre droit qui dure plusieurs heures et une douleur à la palpation de l’hypocondre droit, le ' + w('k80-murphy', 'signe de Murphy') + ' (EASL 2016, recommandation forte). Cependant, aucun signe isolé ne suffit à poser ou à exclure le diagnostic ; c’est pourquoi la WSES 2020 demande d’associer l’anamnèse, l’examen, la biologie (CRP, leucocytes) et l’imagerie.')
 + quiz('Une patiente a une douleur de l’hypocondre droit depuis 40 minutes, cédant sous antalgique, sans fièvre ; l’échographie montre des calculs sans épaississement pariétal. Quel diagnostic ?',
   [('Cholécystite aiguë', False), ('Colique biliaire', True), ('Angiocholite', False)],
   'Douleur brève, sans fièvre ni signe pariétal : c’est une colique biliaire ; elle justifie une cholécystectomie le plus tôt possible (EASL 2016).')
 + key('Colique : 15 à 30 minutes ou plus, irradiée, soulagée. Cholécystite : douleur de plusieurs heures, fièvre, Murphy, CRP et leucocytes élevés.')
 + src(EASL, WSES))

C.a(6, 'Diagnostic : échographie et recherche des calculs cholédociens', P(
 'Au terme de l’examen, l’' + w('k80-echo', 'échographie abdominale') + ' est l’examen de première intention, en raison de son coût, de sa disponibilité et de sa bonne précision (WSES 2020, recommandation forte). Ainsi, elle montre les calculs, mobiles et suivis d’un cône d’ombre, et les signes de cholécystite : paroi épaissie, liquide péri-vésiculaire, Murphy échographique. En revanche, la précision diagnostique du scanner est faible pour la cholécystite.',
 'Ensuite, il faut rechercher un calcul de la voie biliaire principale. Or, le bilan hépatique seul ne suffit pas (WSES 2020). Par conséquent, on combine le bilan hépatique et l’échographie pour estimer la probabilité (ESGE 2019) ; de plus, en cas de suspicion persistante sans preuve échographique, l’' + w('k80-eus', 'écho-endoscopie') + ' ou la ' + w('k80-bilirm', 'bili-IRM') + ' sont recommandées (ESGE 2019, recommandation forte).')
 + C.img('k80_echo_lithiase.gif', 'Échographie annotée de la vésicule : sludge déclive, calculs hyperéchogènes et cône d’ombre acoustique postérieur ; paroi fine, graisse péri-vésiculaire normale.', 'Échographie chez un homme de 83 ans, deux semaines après une colique : sludge et calculs avec cône d’ombre, paroi à 3 mm sans œdème péri-vésiculaire. Il s’agit donc d’une lithiase sans cholécystite en cours (légendes en anglais : Bile = bile, Sludge = sludge, Gallstones = calculs, Acoustic shadowing = cône d’ombre).', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Ultrasonography_of_sludge_and_gallstones,_annotated.jpg'}))
 + key('Échographie d’abord ; scanner peu précis pour la cholécystite. Calcul cholédocien : bilan hépatique + échographie, puis écho-endoscopie ou bili-IRM si doute.')
 + src(WSES, ESGE, EASL))

C.a(7, 'Stratifier le risque de calcul cholédocien', P(
 'Une fois les calculs vésiculaires prouvés, le risque cholédocien oriente l’examen suivant. Ainsi, la WSES 2020 classe les ' + w('k80-risque-vbp', 'prédicteurs') + ' en trois niveaux : très forts (calcul visible dans le cholédoque à l’échographie, angiocholite), forts (cholédoque de plus de 6 mm vésicule en place, bilirubine totale supérieure à 1,8 mg/dl) et modérés (autre anomalie du bilan hépatique, âge supérieur à 55 ans, pancréatite biliaire).',
 'Par conséquent, le patient à haut risque, qui présente un prédicteur très fort, bénéficie d’une CPRE préopératoire, d’une cholangiographie peropératoire ou d’une échographie laparoscopique. À l’inverse, le patient à risque intermédiaire bénéficie d’abord d’une bili-IRM, d’une écho-endoscopie ou d’une exploration peropératoire (WSES 2020, recommandations fortes). Enfin, le calcul cholédocien doit être extrait chez tout patient qui peut supporter le geste, qu’il soit symptomatique ou non (ESGE 2019).')
 + trap('La grille de la WSES 2020 est adaptée d’une classification de sociétés américaines (ASGE, SAGES) ; la WSES la rend plus restrictive, en réservant le haut risque aux prédicteurs très forts, pour limiter les CPRE inutiles.', 'Origine de la grille')
 + quiz('Une patiente a des calculs vésiculaires, un cholédoque à 8 mm et une bilirubine à 2,5 mg/dl, sans calcul visible ni angiocholite. Quel niveau de risque ?',
   [('Haut : CPRE d’emblée', False), ('Intermédiaire : bili-IRM ou écho-endoscopie', True), ('Faible : cholécystectomie seule', False)],
   'Deux prédicteurs forts mais aucun très fort : risque intermédiaire selon la WSES 2020 ; la bili-IRM ou l’écho-endoscopie évitent une CPRE inutile.')
 + key('Très fort (calcul visible, angiocholite) : haut risque, CPRE. Fort ou modéré seulement : intermédiaire, bili-IRM ou écho-endoscopie. Tout calcul cholédocien est extrait.')
 + src(WSES, ESGE))

C.a(8, 'Traitement de la colique et de la lithiase vésiculaire', P(
 'Le diagnostic posé, le traitement dépend des symptômes. D’abord, la colique biliaire est traitée par un ' + w('k80-d-ains', 'AINS') + ', par exemple le diclofénac (EASL 2016). Ensuite, la ' + w('k80-cholecystectomie', 'cholécystectomie') + ' est le traitement préféré de la lithiase symptomatique (recommandation forte) ; elle doit être faite le plus tôt possible après une colique non compliquée. De plus, la voie laparoscopique est la méthode de référence, y compris dans la cirrhose Child-Pugh A ou B.',
 'En revanche, la lithiase asymptomatique n’est pas traitée de façon systématique. Toutefois, une ' + w('k80-porcelaine', 'vésicule porcelaine') + ' peut justifier une cholécystectomie, de même qu’une sphérocytose héréditaire ou une drépanocytose lors d’une splénectomie. Enfin, la dissolution des calculs par acides biliaires, seule ou avec lithotritie extracorporelle, n’est pas recommandée (EASL 2016, recommandation forte).')
 + trap('L’information professionnelle suisse d’Ursofalk® mentionne la dissolution des calculs de cholestérol (environ 10 mg/kg/j, 6 à 24 mois), alors que l’EASL 2016 ne recommande pas cette litholyse. Le cours suit l’EASL et signale l’écart.', 'Point discuté')
 + key('Colique : AINS. Lithiase symptomatique : cholécystectomie laparoscopique, tôt. Asymptomatique : abstention, sauf vésicule porcelaine ou hémolyse lors d’une splénectomie.')
 + src(EASL, FI('Ursofalk® 500 mg')))

C.a(9, 'Cholécystite aiguë : chirurgie précoce', P(
 'Si une cholécystite est présente, le moment de la chirurgie devient décisif. Ainsi, la WSES 2020 recommande la cholécystectomie laparoscopique comme traitement de première intention (recommandation forte), le plus tôt possible : dans les 7 jours suivant l’admission et dans les 10 jours suivant le début des symptômes. De même, l’EASL 2016 recommande une cholécystectomie précoce, de préférence dans les 72 heures suivant l’admission. En effet, la chirurgie précoce fait mieux que la chirurgie intermédiaire ou différée.',
 'De plus, la chirurgie est proposée au patient âgé, y compris au-delà de 80 ans, à la femme enceinte et au patient cirrhotique Child A ou B (WSES 2020, recommandation faible). Cependant, en cas d’anatomie difficile, une ' + w('k80-subtotale', 'cholécystectomie subtotale') + ' ou une conversion protègent la voie biliaire. En revanche, le choc septique et les contre-indications anesthésiques absolues font renoncer à la chirurgie immédiate.')
 + C.img('k80_cholecystite_echo.gif', 'Échographie annotée de la vésicule en coupe axiale : paroi épaissie et calcul hyperéchogène avec cône d’ombre postérieur.', 'Cholécystite aiguë lithiasique à l’échographie : paroi vésiculaire épaissie (« gall bladder wall thickness ») et calcul avec cône d’ombre postérieur (« stone with posterior shadowing »).', credit({'auteur': 'Cerevisae', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Acute_cholecystitis_as_seen_on_ultrasound_axial_view.jpg'}))
 + key('Cholécystectomie laparoscopique dans les 7 jours suivant l’admission et 10 jours suivant le début (WSES 2020), idéalement ≤ 72 heures (EASL 2016). Sinon : après 6 semaines.')
 + src(WSES, EASL))

C.a(10, 'Cholécystite aiguë : patient non opérable et antibiotiques', P(
 'Lorsque la chirurgie précoce est impossible, deux options existent. D’une part, la WSES 2020 suggère une cholécystectomie différée au-delà de 6 semaines. D’autre part, chez le patient qui ne peut pas être opéré, un ' + w('k80-drainage', 'drainage de la vésicule') + ' est recommandé, car il transforme un patient septique en patient non septique (recommandation forte). Cependant, chez le patient à haut risque mais opérable, la cholécystectomie laparoscopique immédiate reste supérieure au drainage percutané (WSES 2020, recommandation forte).',
 'Quant aux ' + w('k80-atb', 'antibiotiques') + ', ils dépendent de la gravité. Ainsi, dans la cholécystite non compliquée, les antibiotiques postopératoires ne sont pas recommandés quand la cholécystectomie contrôle le foyer (WSES 2020, recommandation forte) ; de même, la directive suisse KSSG permet de les arrêter 24 heures après la cholécystectomie, en l’absence de bactériémie, d’abcès, de perforation, de forme emphysémateuse ou de nécrose. En revanche, dans la forme compliquée, le schéma tient compte des germes présumés et du risque de résistance.')
 + key('Non opérable : drainage vésiculaire, puis chirurgie différée. Haut risque opérable : chirurgie plutôt que drainage. Non compliquée : arrêt des antibiotiques 24 heures après l’exérèse.')
 + src(WSES, KSSG))

C.a(11, 'Angiocholite aiguë', P(
 'Si le calcul obstrue la voie biliaire et s’infecte, l’angiocholite menace la vie. Ainsi, devant une fièvre avec frissons, une douleur abdominale et/ou un ictère, l’EASL 2016 recommande de doser les leucocytes, la CRP et le bilan hépatique et de faire une échographie (recommandation forte). Ensuite, la gravité est classée selon les ' + w('k80-tokyo', 'critères de Tokyo 2018') + ', comme le recommande l’ESGE 2019.',
 'Par conséquent, le traitement associe des antibiotiques à large spectre immédiats et une ' + w('k80-drainage-biliaire', 'décompression biliaire') + ' (EASL 2016, recommandation forte), de préférence endoscopique. De plus, le délai dépend de la gravité : dès que possible dans la forme sévère, et dans les 12 heures en cas de choc septique ; dans les 48 à 72 heures dans la forme modérée ; de façon élective dans la forme légère (ESGE 2019).')
 + C.img('k80_cpre_calcul.gif', 'Image de radioscopie pendant une CPRE : endoscope dans le duodénum, opacification des voies biliaires et lacune arrondie dans le cholédoque distal.', 'Calcul enclavé dans le cholédoque distal, vu en radioscopie au cours d’une CPRE. L’opacification dessine les voies biliaires dilatées en amont de l’obstacle.', credit({'auteur': 'Samir धर्म', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:ERCP_stone.jpg'}))
 + alert('Angiocholite sévère avec choc septique : drainage biliaire dans les 12 heures (ESGE 2019) ; au-delà, la mortalité hospitalière augmente (rapport de cotes 3,4 dans l’étude citée).', 'Gravité d’abord.')
 + key('Fièvre, frissons, douleur, ictère : leucocytes, CRP, bilan hépatique, échographie. Antibiotiques immédiats ; drainage ≤ 12 h si choc, 48-72 h si modérée, électif si légère.')
 + src(EASL, ESGE))

C.a(12, 'Calculs de la voie biliaire principale : traitement', P(
 'Après l’urgence, il reste à libérer la voie biliaire et à prévenir la récidive. Ainsi, la ' + w('k80-sphincterotomie', 'sphinctérotomie endoscopique') + ' avec extraction est un traitement recommandé des calculs cholédociens (EASL 2016). De plus, en cas de découverte peropératoire, l’exploration chirurgicale, l’extraction transcystique ou l’extraction endoscopique sont des alternatives. Par ailleurs, une prothèse biliaire temporaire est posée quand l’extraction est incomplète (ESGE 2019), et les calculs difficiles relèvent de la lithotritie mécanique ou guidée par cholangioscopie.',
 'Ensuite, la vésicule doit être retirée. En effet, l’EASL 2016 recommande, en cas de calculs vésiculaires et cholédociens simultanés, une cholécystectomie laparoscopique précoce dans les 72 heures après la CPRE ; de son côté, l’ESGE 2019 fixe un délai maximal de 2 semaines après la CPRE. Enfin, dans la pancréatite biliaire avec angiocholite, la CPRE est faite de préférence dans les 24 heures, puis la cholécystectomie pendant la même hospitalisation si la pancréatite est légère (EASL 2016).')
 + trap('Délai de la cholécystectomie après CPRE : ≤ 72 heures selon l’EASL 2016, ≤ 2 semaines selon l’ESGE 2019. Les deux sources vont dans le même sens (opérer pendant la même prise en charge) ; le délai exact est à arbitrer à l’audit.', 'Point discuté')
 + key('Sphinctérotomie et extraction ; prothèse si extraction incomplète. Puis cholécystectomie : ≤ 72 h (EASL) ou ≤ 2 semaines (ESGE) après la CPRE.')
 + C.pareto('pareto-k80-clinique', 'Lithiase biliaire', ['k80-5', 'k80-6', 'k80-7', 'k80-9', 'k80-11', 'k80-12'],
     ['Échographie d’abord ; scanner peu précis pour la cholécystite.',
      'Lithiase symptomatique : cholécystectomie laparoscopique ; asymptomatique : abstention.',
      'Cholécystite : chirurgie ≤ 7 jours après l’admission et ≤ 10 jours après le début.',
      'Risque cholédocien intermédiaire : bili-IRM ou écho-endoscopie ; haut : CPRE.',
      'Angiocholite : antibiotiques et drainage, ≤ 12 h si choc septique.',
      'Après CPRE : cholécystectomie pendant la même prise en charge.'])
 + src(EASL, ESGE))

C.a(13, 'Situations particulières et synthèse', P(
 'Certaines situations modifient ces règles. Pendant la grossesse, la cholécystectomie laparoscopique peut être faite à tout trimestre si l’indication est urgente, et les calculs cholédociens symptomatiques sont traités par sphinctérotomie par un endoscopiste expérimenté (EASL 2016). De même, après une cholécystectomie, des symptômes biliaires conduisent à une écho-endoscopie ou à une bili-IRM.',
 'Pour conclure, reprenons la patiente du début. Sa douleur dure depuis 10 heures, avec fièvre : il s’agit donc d’une cholécystite et non d’une colique. Or, l’échographie montre une paroi épaissie et des calculs, sans dilatation du cholédoque, et la bilirubine est normale ; le risque cholédocien est donc faible. Par conséquent, elle reçoit de l’amoxicilline-acide clavulanique, puis une cholécystectomie laparoscopique dès le lendemain ; dès lors, l’antibiotique est arrêté 24 heures après l’intervention, en l’absence de complication.')
 + key('Grossesse : chirurgie possible à tout trimestre si urgente ; CPRE par un expert. Symptômes après cholécystectomie : écho-endoscopie ou bili-IRM.')
 + src(EASL, KSSG, WSES))

C.a(14, 'Critères formels et paramètres clés', alert(
 '<p><b>Colique.</b> Douleur de l’hypocondre droit ou épigastrique ≥ 15-30 min, irradiée, soulagée par les antalgiques. <b>Cholécystite.</b> Fièvre, douleur de plusieurs heures, Murphy, inflammation biologique, signes échographiques. <b>Angiocholite (Tokyo 2018).</b> Sévère : dysfonction d’organe ; modérée : leucocytes > 12 000 ou < 4000/mm³, fièvre ≥ 39 °C, âge ≥ 75 ans, bilirubine ≥ 5 mg/dl ou hypoalbuminémie ; légère : aucun de ces critères.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Cholédoque > 6 mm et bilirubine > 1,8 mg/dl : prédicteurs forts ; cholécystectomie ≤ 7 jours après l’admission (WSES) ; drainage biliaire ≤ 12 h si choc septique ; antibiotiques 4 à 7 jours dans la forme non compliquée sans exérèse, arrêt 24 h après cholécystectomie (KSSG).</div>'
 + src(EASL, ESGE, WSES, KSSG))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Statut'], [
   ['Y a-t-il des calculs, une cholécystite ?', w('k80-echo', 'Échographie abdominale'), 'Première intention'],
   ['Quelle inflammation, quelle cholestase ?', 'Leucocytes, CRP, bilan hépatique, lipase', 'Systématiques'],
   ['Calcul cholédocien en cas de doute ?', w('k80-bilirm', 'Bili-IRM') + ' ou ' + w('k80-eus', 'écho-endoscopie'), 'Risque intermédiaire'],
   ['Extraire un calcul cholédocien ?', w('k80-cpre', 'CPRE'), 'Haut risque ou calcul prouvé'],
   ['Cholécystite douteuse ?', w('k80-hida', 'Scintigraphie HIDA') + ' ou IRM', 'Patients sélectionnés'],
   ['Diagnostic de cholécystite ?', 'Scanner', 'Précision faible']])
 + P('Le tableau se lit de haut en bas : ainsi, l’échographie répond à la plupart des questions, alors que la CPRE est réservée au traitement, et non au diagnostic.')
 + key('Échographie d’abord ; bili-IRM ou écho-endoscopie pour le doute cholédocien ; CPRE pour traiter ; HIDA en cas de doute sur la cholécystite.')
 + src(WSES, ESGE))

C.e(2, 'Lire une échographie biliaire', P(
 'Le compte rendu décrit d’abord les calculs : images hyperéchogènes, mobiles avec la position et suivies d’un cône d’ombre acoustique. Ensuite, il décrit la paroi ; ainsi, un épaississement pariétal, un liquide péri-vésiculaire et un Murphy échographique orientent vers une cholécystite. Enfin, il mesure le cholédoque et recherche un calcul dans sa lumière.',
 'Cependant, l’échographie voit mal le cholédoque distal, masqué par les gaz duodénaux. Par conséquent, un cholédoque dilaté sans calcul visible ne rassure pas : en effet, la dilatation est un prédicteur fort qui conduit à la bili-IRM ou à l’écho-endoscopie (WSES 2020). En revanche, le sludge isolé, sans symptôme, n’impose aucun geste.')
 + quiz('L’échographie montre des calculs avec cône d’ombre, une paroi à 3 mm, aucun liquide péri-vésiculaire et un cholédoque de 4 mm. Le patient a eu une colique il y a 15 jours. Quelle conclusion ?',
   [('Cholécystite aiguë', False), ('Lithiase vésiculaire symptomatique sans complication', True), ('Calcul cholédocien probable', False)],
   'Paroi fine, pas de liquide, cholédoque normal : il n’y a ni cholécystite ni argument cholédocien ; la cholécystectomie est indiquée le plus tôt possible (EASL 2016).')
 + key('Calcul : hyperéchogène, mobile, cône d’ombre. Cholécystite : paroi épaisse, liquide, Murphy échographique. Cholédoque > 6 mm : prédicteur fort.')
 + C.pareto('pareto-k80-examens', 'Examens', ['k80-e-1', 'k80-e-2'],
     ['Échographie en première intention.',
      'Bilan hépatique seul insuffisant pour le calcul cholédocien.',
      'Risque intermédiaire : bili-IRM ou écho-endoscopie.',
      'CPRE pour traiter, pas pour diagnostiquer.',
      'Scanner peu précis pour la cholécystite.'])
 + src(WSES, ESGE, EASL))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : vésicule, triangle de Calot et voie biliaire', P(
 'La vésicule se draine par le canal cystique dans la voie biliaire principale. Or, l’artère cystique et le canal cystique traversent le ' + w('k80-calot', 'triangle de Calot') + ', limité par le canal cystique, le canal hépatique commun et le bord inférieur du foie. Par conséquent, l’identification de ces éléments avant toute section protège la voie biliaire principale ; c’est pourquoi, quand l’inflammation rend l’anatomie illisible, la WSES 2020 recommande une cholécystectomie subtotale ou une conversion. De plus, le cholédoque rejoint le canal pancréatique à l’ampoule de Vater, ce qui explique la pancréatite biliaire.')
 + key('Triangle de Calot identifié avant toute section : sinon, subtotale ou conversion.', 'Science → clinique.'))
C.s('phys', 'Physiologie', 'Physiologie : la bile et sa saturation', P(
 'Le cholestérol est insoluble dans l’eau ; ainsi, il n’est maintenu en solution dans la bile que par les sels biliaires et les phospholipides, qui forment des micelles. Or, quand le cholestérol est en excès par rapport à ces solubilisants, la bile se sursature et des cristaux apparaissent. De plus, la vésicule se vide sous l’effet de la cholécystokinine après un repas gras ; par conséquent, le jeûne prolongé, la nutrition parentérale et les analogues de la somatostatine, qui réduisent la vidange, favorisent la stase et les calculs.')
 + key('C’est pourquoi l’acide ursodésoxycholique, qui réduit la saturation en cholestérol, prévient les calculs lors d’une perte de poids rapide.', 'Science → traitement.'))
C.s('micro', 'Microbiologie', 'Microbiologie : les germes des infections biliaires', P(
 'Dans les infections biliaires, les bacilles à Gram négatif dominent : Escherichia coli jusqu’à 45 %, Klebsiella jusqu’à 20 %, Enterobacter jusqu’à 10 %, selon la directive KSSG. Par ailleurs, les entérocoques, les streptocoques et les anaérobes, jusqu’à 20 %, sont aussi retrouvés. En outre, Pseudomonas apparaît selon les traitements antérieurs et la colonisation connue. Par conséquent, l’antibiothérapie empirique couvre les entérobactéries et les anaérobes, puis elle est adaptée aux cultures.')
 + key('Entérobactéries et anaérobes d’abord : amoxicilline-acide clavulanique, ou ceftriaxone avec ou sans métronidazole, dans la forme communautaire légère à modérée.', 'Science → traitement.'))
C.s('histo', 'Histologie', 'Histologie : de la colique à la cholécystite', P(
 'La paroi vésiculaire comporte une muqueuse à épithélium cylindrique, une musculeuse et une séreuse. Ainsi, dans la cholécystite aiguë, l’obstruction prolongée provoque un œdème pariétal, une congestion puis un infiltrat de polynucléaires ; ensuite, une ischémie peut aboutir à la nécrose et à la perforation. À l’inverse, la cholécystite chronique associe une fibrose de la paroi et des sinus de Rokitansky-Aschoff. Par conséquent, l’épaississement pariétal vu à l’échographie traduit l’œdème de la forme aiguë ou la fibrose de la forme chronique.')
 + key('Œdème, polynucléaires, puis nécrose : c’est le substrat de l’épaississement pariétal et du risque de perforation.', 'Science → examen.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, la plupart des lithiases relèvent d’un geste, chirurgical ou endoscopique. En pratique, les médicaments servent donc à soulager, à traiter l’infection et, rarement, à prévenir.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['AINS', 'Diclofénac (Voltarène®)', 'Colique biliaire', w('k80-d-ains', 'Monographie')],
   ['Pénicilline avec inhibiteur de bêtalactamase', 'Amoxicilline-acide clavulanique (Co-Amoxi-Mepha® i.v.)', 'Cholécystite ou angiocholite communautaire légère à modérée', w('k80-d-coamoxi', 'Monographie')],
   ['Céphalosporine de 3e génération ± nitro-imidazolé', 'Ceftriaxone ± métronidazole', 'Alternative communautaire', w('k80-atb', 'Fiche')],
   ['Acide biliaire', 'Acide ursodésoxycholique (Ursofalk®)', 'Prévention lors d’une perte de poids rapide', w('k80-d-audc', 'Monographie')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, l’antibiotique ne remplace jamais le contrôle du foyer, qu’il s’agisse de la cholécystectomie ou du drainage biliaire.')
 + key('AINS pour la colique ; antibiotiques pour l’infection, avec contrôle du foyer ; acide ursodésoxycholique pour la prévention ciblée.')
 + src(EASL, KSSG))

C.p(2, 'Doses et durées', P('Les doses suivantes proviennent de la directive suisse KSSG et des informations professionnelles suisses ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Situation', 'Dose et durée', 'Source'], [
   ['Diclofénac', 'Colique biliaire sévère', '75 mg i.m. profonde, exceptionnellement 2 × 75 mg/j ; perfusion 75 mg en 30 min à 2 h ; max. 150 mg/24 h ; jamais en bolus i.v.', 'Information professionnelle Voltarène® solution injectable'],
   ['Amoxicilline-acide clavulanique', 'Communautaire, légère à modérée', '2,2 g i.v. toutes les 8 h ; relais 1 g p.o. toutes les 8 h si ambulatoire', 'KSSG ; FI Co-Amoxi-Mepha® i.v.'],
   ['Ceftriaxone ± métronidazole', 'Communautaire, légère à modérée', '2 g i.v. toutes les 24 h ± 500 mg toutes les 8 h', 'KSSG'],
   ['Pipéracilline-tazobactam', 'Forme sévère, ou patient déjà opéré ou récemment hospitalisé', '4,5 g toutes les 8 h', 'KSSG'],
   ['Imipénem', 'Forme sévère, instabilité hémodynamique', '500 mg i.v. toutes les 6 h', 'KSSG'],
   ['Durée', 'Forme non compliquée', '4 à 7 jours ; arrêt 24 h après cholécystectomie sans complication', 'KSSG ; WSES 2020'],
   ['Acide ursodésoxycholique', 'Perte de poids rapide', 'Au moins 500 mg/j jusqu’à stabilisation du poids', 'EASL 2016']])
 + P('Par exemple, la patiente du début reçoit amoxicilline-acide clavulanique 2,2 g toutes les 8 heures ; dès lors, après la cholécystectomie du lendemain, sans perforation ni abcès, l’antibiotique est arrêté à 24 heures.')
 + trap('Le schéma communautaire de la directive KSSG s’adresse aux formes légères à modérées ; chez le patient instable, la directive commence toujours par l’imipénem. Les schémas doivent être adaptés à l’épidémiologie locale.', 'À retenir')
 + key('Communautaire : amoxicilline-acide clavulanique 2,2 g/8 h ou ceftriaxone 2 g/24 h ± métronidazole ; sévère : pipéracilline-tazobactam ou imipénem ; 4 à 7 jours, ou 24 h après exérèse.')
 + src(KSSG, FI('Voltarène® solution injectable'), FI('Co-Amoxi-Mepha® i.v.'), EASL, WSES))

C.p(3, 'Interactions, surveillance et effets indésirables', alert(
 'Le diclofénac injectable ne doit jamais être injecté en bolus intraveineux ; de plus, l’injection intramusculaire doit être intraglutéale profonde, pour éviter les lésions nerveuses et le syndrome de Nicolau. Par ailleurs, les AINS sont évités en cas d’insuffisance rénale, d’ulcère ou d’anticoagulation, et la dose minimale efficace est donnée sur la durée la plus courte.', 'Sécurité.')
 + P('Au cours de l’antibiothérapie, la surveillance porte sur l’évolution clinique et sur les cultures ; ainsi, le traitement est adapté aux résultats microbiologiques, surtout en cas de risque de résistance (WSES 2020). En outre, la directive KSSG rappelle que les hémocultures sont souvent peu contributives au diagnostic, et qu’il faut envoyer en microbiologie tout liquide de ponction ou de drainage. Enfin, l’acide ursodésoxycholique doit être interrompu si les calculs se calcifient, selon l’information professionnelle suisse.')
 + key('Diclofénac : jamais en bolus i.v., i.m. profonde ; antibiotiques adaptés aux cultures ; contrôle du foyer prioritaire.')
 + C.pareto('pareto-k80-pharma', 'Pharmacologie', ['k80-p-1', 'k80-p-2', 'k80-p-3'],
     ['Colique : AINS (diclofénac).',
      'Communautaire : amoxicilline-acide clavulanique 2,2 g/8 h.',
      'Sévère ou instable : pipéracilline-tazobactam ou imipénem.',
      'Arrêt 24 h après une cholécystectomie sans complication.',
      'Pas de litholyse médicamenteuse (EASL 2016).'])
 + src(FI('Voltarène® solution injectable'), FI('Ursofalk® 500 mg'), KSSG, WSES))

# ---------------- Fenêtres
L = lab
C.pop('k80-colique', 'Colique biliaire', L(('Définition (EASL 2016)', 'Crise de douleur intense de l’hypocondre droit ou de l’épigastre, d’au moins 15 à 30 minutes, irradiant vers le dos ou l’épaule droite, soulagée par les antalgiques.'), ('Mécanisme', 'Obstruction transitoire du collet ou du canal cystique.'), ('Conduite', 'AINS ; cholécystectomie le plus tôt possible.')) + src(EASL))
C.pop('k80-cholecystite', 'Cholécystite aiguë lithiasique', L(('Clinique', 'Fièvre, douleur de l’hypocondre droit de plusieurs heures, signe de Murphy.'), ('Diagnostic', 'Association anamnèse, examen, CRP et leucocytes, échographie (WSES 2020).'), ('Traitement', 'Cholécystectomie laparoscopique ≤ 7 jours après l’admission et ≤ 10 jours après le début.')) + src(EASL, WSES))
C.pop('k80-echo', 'Échographie biliaire', L(('Place', 'Première intention, recommandation forte (WSES 2020).'), ('Calcul', 'Image hyperéchogène, mobile, cône d’ombre postérieur.'), ('Cholécystite', 'Paroi épaissie, liquide péri-vésiculaire, Murphy échographique.'), ('Limite', 'Cholédoque distal mal vu.')) + src(WSES, EASL))
C.pop('k80-risque-vbp', 'Risque de calcul de la voie biliaire principale (WSES 2020)', L(('Très forts', 'Calcul cholédocien visible à l’échographie ; angiocholite.'), ('Forts', 'Cholédoque > 6 mm (vésicule en place) ; bilirubine totale > 1,8 mg/dl.'), ('Modérés', 'Autre anomalie du bilan hépatique ; âge > 55 ans ; pancréatite biliaire.'), ('Classes', 'Haut : un prédicteur très fort ; faible : aucun ; intermédiaire : tous les autres.')) + src(WSES))
C.pop('k80-angiocholite', 'Angiocholite aiguë', L(('Définition', 'Infection d’une voie biliaire obstruée, le plus souvent par un calcul.'), ('Clinique', 'Fièvre et frissons, douleur abdominale et/ou ictère (EASL 2016) ; l’association fièvre, douleur et ictère est la triade de Charcot.'), ('Traitement', 'Antibiotiques immédiats et décompression biliaire selon la gravité de Tokyo 2018.')) + src(EASL, ESGE))
C.pop('k80-cholecystectomie', 'Cholécystectomie laparoscopique', L(('Indication', 'Lithiase symptomatique (EASL 2016, recommandation forte), cholécystite aiguë (WSES 2020).'), ('Technique', 'Quatre trocarts : deux d’au moins 10 mm et deux d’au moins 5 mm (EASL 2016).'), ('Risques', 'Mortalité 0,1 à 1 % ; plaie de la voie biliaire 0,2 à 1,5 % dans la cholécystite (WSES 2020).'), ('Ambulatoire', 'Possible sans maladie systémique.')) + src(EASL, WSES))
C.pop('k80-cpre', 'CPRE dans la lithiase', L(('Indications', 'Calcul cholédocien prouvé ou haut risque ; angiocholite ; pancréatite biliaire avec angiocholite.'), ('Geste', 'Sphinctérotomie et extraction ; prothèse temporaire si extraction incomplète.'), ('Antibioprophylaxie', 'Non systématique avant CPRE pour calcul (ESGE 2019).')) + src(ESGE, EASL))
C.pop('k80-cholesterol', 'Calculs de cholestérol', L(('Fréquence', '90 à 95 % des calculs en Occident (EASL 2016).'), ('Siège', 'Vésicule.'), ('Facteurs', 'Syndrome métabolique, perte de poids rapide, âge, sexe féminin.')) + src(EASL))
C.pop('k80-pancreatite', 'Pancréatite biliaire', L(('Mécanisme', 'Calcul migré obstruant l’ampoule de Vater.'), ('Conduite', 'CPRE ≤ 24 h si angiocholite ; cholécystectomie pendant la même hospitalisation si forme légère.'), ('Renvoi', 'Traitée en détail dans le cours K85 — Pancréatite aiguë.')) + src(EASL))
C.pop('k80-metabolique', 'Syndrome métabolique et calculs', L(('Composantes', 'Obésité, diabète, insulinorésistance.'), ('Prévention', 'Mode de vie sain, activité physique, poids idéal (EASL 2016, recommandation faible).')) + src(EASL))
C.pop('k80-perte-poids', 'Perte de poids rapide', L(('Situations', 'Régime très hypocalorique, chirurgie bariatrique.'), ('Prévention', 'Acide ursodésoxycholique ≥ 500 mg/j jusqu’à stabilisation du poids (EASL 2016).'), ('Chirurgie bariatrique', 'Pas de cholécystectomie prophylactique systématique.')) + src(EASL))
C.pop('k80-sludge', 'Sludge biliaire', L(('Définition', 'Bile épaissie contenant des cristaux et du mucus, échogène, sans cône d’ombre.'), ('Signification', 'Il traduit la stase ; il n’est pas en lui-même la cause des calculs (EASL 2016).')) + src(EASL))
C.pop('k80-murphy', 'Signe de Murphy', L(('Technique', 'Palpation profonde de l’hypocondre droit pendant l’inspiration.'), ('Positif', 'Arrêt de l’inspiration par la douleur.'), ('Valeur', 'Rapport de vraisemblance positif 2,8, intervalle de confiance incluant 1 : il ne suffit pas seul (WSES 2020).')) + src(WSES, EASL))
C.pop('k80-eus', 'Écho-endoscopie', L(('Principe', 'Sonde d’échographie au bout d’un endoscope, au contact du duodénum.'), ('Indication', 'Suspicion persistante de calcul cholédocien sans preuve échographique (ESGE 2019, recommandation forte).'), ('Avantage', 'Très sensible pour les petits calculs ; évite une CPRE diagnostique.')) + src(ESGE))
C.pop('k80-bilirm', 'Bili-IRM', L(('Principe', 'IRM pondérée en T2 qui visualise la bile sans produit de contraste.'), ('Indication', 'Risque intermédiaire de calcul cholédocien ; symptômes après cholécystectomie.')) + src(ESGE, WSES, EASL))
C.pop('k80-d-ains', 'Diclofénac (Voltarène® solution injectable)', L(('Dose', '75 mg i.m. intraglutéale profonde ; exceptionnellement 2 × 75 mg/j dans les coliques ; perfusion 75 mg en 30 min à 2 h ; max. 150 mg/24 h.'), ('Interdit', 'Bolus intraveineux.'), ('Place', 'Traitement de la colique biliaire (EASL 2016).')) + src(FI('Voltarène® solution injectable'), EASL))
C.pop('k80-porcelaine', 'Vésicule porcelaine', L(('Définition', 'Calcification de la paroi vésiculaire.'), ('Conduite', 'Cholécystectomie possible même sans symptôme (EASL 2016, recommandation faible).')) + src(EASL))
C.pop('k80-subtotale', 'Cholécystectomie subtotale', L(('Principe', 'Exérèse partielle de la vésicule, sans disséquer le triangle de Calot.'), ('Indication', 'Anatomie difficile, risque élevé de plaie biliaire (WSES 2020, recommandation forte).')) + src(WSES))
C.pop('k80-drainage', 'Drainage de la vésicule', L(('Indication', 'Cholécystite chez un patient non opérable (WSES 2020, recommandation forte).'), ('Techniques', 'Percutané transhépatique ; endoscopique transpapillaire ; transmural écho-guidé par prothèse métallique, à retirer dans les 4 semaines.'), ('Ensuite', 'Cholécystectomie différée après réduction du risque.')) + src(WSES))
C.pop('k80-atb', 'Antibiotiques des infections biliaires', L(('Communautaire légère à modérée', 'Ceftriaxone 2 g/24 h ± métronidazole 500 mg/8 h, ou amoxicilline-acide clavulanique 2,2 g/8 h.'), ('Associée aux soins', 'Pipéracilline-tazobactam 4,5 g/8 h, ou céfépime 2 g/8 h + métronidazole.'), ('Sévère', 'Pipéracilline-tazobactam ou imipénem 500 mg/6 h ; imipénem d’emblée si instabilité.'), ('Durée', '4 à 7 jours ; 24 h après cholécystectomie sans complication.')) + src(KSSG, WSES))
C.pop('k80-tokyo', 'Gravité de l’angiocholite (Tokyo 2018)', L(('Sévère (grade III)', 'Dysfonction d’au moins un système : cardiovasculaire, neurologique, respiratoire, rénal, hépatique ou hématologique.'), ('Modérée (grade II)', 'Un critère : leucocytes > 12 000 ou < 4000/mm³, fièvre ≥ 39 °C, âge ≥ 75 ans, bilirubine totale ≥ 5 mg/dl, hypoalbuminémie.'), ('Légère (grade I)', 'Aucun critère de forme modérée ou sévère.')) + src(ESGE))
C.pop('k80-drainage-biliaire', 'Drainage biliaire de l’angiocholite', L(('Délai (ESGE 2019)', 'Sévère : dès que possible, ≤ 12 h si choc septique ; modérée : 48 à 72 h ; légère : électif.'), ('Voie', 'Endoscopique de préférence ; percutanée ou chirurgicale si échec ou impossibilité.')) + src(ESGE))
C.pop('k80-sphincterotomie', 'Sphinctérotomie endoscopique', L(('Principe', 'Section du sphincter d’Oddi au cours de la CPRE pour extraire les calculs.'), ('Calculs difficiles', 'Sphinctérotomie limitée avec dilatation au ballonnet ; lithotritie mécanique ou par cholangioscopie (ESGE 2019).')) + src(ESGE, EASL))
C.pop('k80-hida', 'Scintigraphie HIDA', L(('Principe', 'Traceur excrété dans la bile ; la non-visualisation de la vésicule signe l’obstruction du cystique.'), ('Valeur', 'Sensibilité et spécificité les plus élevées pour la cholécystite, selon l’expertise locale (WSES 2020).')) + src(WSES))
C.pop('k80-calot', 'Triangle de Calot', L(('Limites', 'Canal cystique, canal hépatique commun, bord inférieur du foie.'), ('Contenu', 'Artère cystique.'), ('Enjeu', 'Identification avant toute section pour éviter la plaie de la voie biliaire principale.')) + src(WSES))
C.pop('k80-d-coamoxi', 'Amoxicilline-acide clavulanique i.v. (Co-Amoxi-Mepha®)', L(('Dose (FI suisse)', 'Infection modérée : 1,2 g 3 à 4 fois par jour ; grave : 2,2 g 3 à 4 fois par jour en perfusion d’au moins 30 minutes.'), ('Directive KSSG', '2,2 g i.v. toutes les 8 h ; relais 1 g p.o. toutes les 8 h.')) + src(FI('Co-Amoxi-Mepha® i.v.'), KSSG))
C.pop('k80-d-audc', 'Acide ursodésoxycholique (Ursofalk®)', L(('Prévention', '≥ 500 mg/j lors d’une perte de poids rapide (EASL 2016).'), ('Dissolution (FI suisse)', 'Environ 10 mg/kg/j le soir, 6 à 24 mois ; arrêt si pas de réduction à 12 mois ou calcification ; litholyse non recommandée par l’EASL 2016.')) + src(FI('Ursofalk® 500 mg'), EASL))

C.termes = [
 (r'CPRE', 'k80-cpre'), (r'écho-endoscopie', 'k80-eus'), (r'bili-IRM|Bili-IRM', 'k80-bilirm'), (r'signe de Murphy|Murphy', 'k80-murphy'),
 (r'sludge', 'k80-sludge'), (r'angiocholite', 'k80-angiocholite'), (r'cholécystite aiguë', 'k80-cholecystite'), (r'colique biliaire', 'k80-colique'),
 (r'Tokyo 2018', 'k80-tokyo'), (r'sphinctérotomie', 'k80-sphincterotomie'), (r'acide ursodésoxycholique', 'k80-d-audc'), (r'diclofénac', 'k80-d-ains'),
 (r'amoxicilline-acide clavulanique', 'k80-d-coamoxi'), (r'pipéracilline-tazobactam|imipénem|ceftriaxone', 'k80-atb'), (r'vésicule porcelaine', 'k80-porcelaine'),
 (r'cholécystectomie subtotale', 'k80-subtotale'), (r'triangle de Calot', 'k80-calot'), (r'pancréatite biliaire', 'k80-pancreatite'),
 (r'drainage percutané|drainage de la vésicule|drainage vésiculaire', 'k80-drainage'), (r'syndrome métabolique', 'k80-metabolique'), (r'cholédoque', 'k80-risque-vbp'),
]

C.write()
