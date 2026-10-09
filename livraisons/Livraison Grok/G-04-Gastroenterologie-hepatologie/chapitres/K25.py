import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K25', 'Ulcère gastroduodénal',
    'K25 — Ulcère de l’estomac · leçon étendue à K26 — Ulcère du duodénum et K27 — Ulcère digestif, de siège non précisé · CIM-10-GM 2024 · Tube digestif',
    'Adulte · ulcère non compliqué, compliqué et prévention · rédaction du 09.10.2026 · référentiels SSI Helicobacter pylori 2026, S2k DGVS 2023, ESGE 2021, WSES 2020, informations professionnelles suisses',
    'Pharmacologie de l’ulcère')
w = C.w
SSI = ('Société suisse d’infectiologie, directives Helicobacter pylori, version longue, mise à jour du 29.06.2026', 'https://ssi.guidelines.ch/guideline/3025')
S2K = ('Fischbach W. et al., S2k-Leitlinie Helicobacter pylori und gastroduodenale Ulkuskrankheit (DGVS), Z Gastroenterol 2023;61:544-606', 'https://register.awmf.org/de/leitlinien/detail/021-001')
ESGE21 = ('Gralnek I. M. et al., ESGE, hémorragie digestive haute non variqueuse, mise à jour 2021, Endoscopy 2021;53:300-332', 'https://www.esge.com/assets/downloads/pdfs/guidelines/2021_a_1369_5274.pdf')
WSES = ('Tarasconi A. et al., WSES, ulcère peptique perforé et hémorragique, World J Emerg Surg 2020;15:3', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6947898/')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS via AmiKo), consultée le 09.10.2026', 'https://amiko.oddb.org/fr')

# ---------------- Onglet 1
C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 63 ans prend de l’ibuprofène depuis trois mois pour une gonarthrose. Elle décrit une douleur épigastrique qui la réveille la nuit. Un homme de 45 ans, fumeur, arrive aux urgences pour une douleur abdominale brutale « en coup de poignard » et un ventre de bois. <b>Les deux souffrent probablement d’un ulcère ; la première question est de savoir s’il est compliqué.</b> La cause vient ensuite, car elle commande la guérison et la prévention de la récidive.',
 'Le médecin doit savoir : définir l’ulcère et le distinguer de l’érosion ; reconnaître ses deux causes principales, Helicobacter pylori et les anti-inflammatoires ; reconnaître une complication (hémorragie, perforation, sténose) ; poser l’indication de l’endoscopie et des biopsies ; prescrire un traitement d’éradication adapté à la résistance ; prévenir l’ulcère chez le patient à risque qui prend des AINS ou des antithrombotiques.')
 + key(w('k25-ulcere-def', 'Ulcère ou érosion (la profondeur décide)') + ' ; ' + w('k25-deux-causes', 'deux causes dominantes (Helicobacter pylori et AINS)') + '.', 'Point de départ.'))

C.a(1, 'Définition et classification', P(
 'L’<b>ulcère gastroduodénal</b> est une perte de substance de la paroi de l’estomac ou du duodénum qui franchit la <b>musculaire muqueuse</b>. L’<b>érosion</b> reste limitée à la muqueuse ; elle cicatrise sans trace et saigne peu. La CIM-10-GM classe l’ulcère selon son siège (estomac K25, duodénum K26, siège non précisé K27), son caractère aigu ou chronique et la présence d’une hémorragie ou d’une perforation.')
 + C.img('k25_pneumoperitoneum_rx.gif', 'À gauche, radiographie thoracique en décubitus montrant de l’air libre sous la coupole diaphragmatique gauche ; à droite, coupe tomodensitométrique abdominale montrant un pneumopéritoine étendu en avant du foie et de l’estomac.', 'Pneumopéritoine, signe d’une perforation digestive. La radiographie peut le montrer ; cependant, la tomodensitométrie est plus sensible et localise mieux la perforation (WSES 2020).', credit({'auteur': 'Cerevisae', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Chest_X-ray_showing_presence_of_free_air_under_left_diaphragm.png'}))
 + table(['Classification', 'Catégories', 'Conséquence pratique'], [
   ['Siège', 'Gastrique (K25) ; duodénal (K26)', 'Ulcère gastrique : biopsies et contrôle endoscopique ; ulcère duodénal : contrôle endoscopique en règle non nécessaire'],
   ['Cause', 'Helicobacter pylori ; AINS ou aspirine ; causes rares ; idiopathique', 'Le traitement de la cause prévient la récidive'],
   ['Évolution', 'Non compliqué ; hémorragie ; perforation ; sténose', 'Une complication impose une prise en charge urgente']])
 + P('Le tableau se lit par la colonne de droite : le siège décide du contrôle endoscopique, la cause décide du traitement de fond, la complication décide de l’urgence.')
 + key('Un ulcère franchit la musculaire muqueuse ; une érosion ne la franchit pas. Le siège, la cause et la complication structurent toute la prise en charge.')
 + src(S2K, SSI))

C.a(2, 'Épidémiologie', P(
 'La prévalence de l’ulcère sur la vie entière est de 5 à 10 % dans la population générale, avec une incidence de 0,1 à 0,3 % par an ; 10 à 20 % des patients présentent une complication (WSES 2020). L’hémorragie est la complication la plus fréquente ; la perforation est environ six fois plus rare mais plus grave, avec une mortalité moyenne à 30 jours de 23,5 % contre 8,6 % pour l’hémorragie dans la revue citée par la WSES.',
 'L’épidémiologie change. La part des ulcères liés à Helicobacter pylori diminue et celle des AINS et de l’aspirine augmente ; dans une étude américaine de 2009 à 2018 citée par la SSI, seul un quart des ulcères duodénaux était encore associé à Helicobacter pylori. En Suisse, les données préliminaires citées par la SSI en 2026 montrent une résistance élevée de la bactérie à la clarithromycine (plus de 16 % chez les patients jamais traités).')
 + trap('Aucune série nationale suisse de l’incidence de l’ulcère n’a été retrouvée lors de la rédaction ; les données suisses disponibles portent sur la résistance de Helicobacter pylori.', 'Lacune documentaire')
 + key('L’ulcère est fréquent et se complique dans 10 à 20 % des cas ; la perforation tue plus que l’hémorragie.')
 + src(WSES, SSI))

C.a(3, 'Physiopathologie : agression et défense', P(
 'La muqueuse résiste à l’acide et à la pepsine grâce au mucus, aux bicarbonates, au renouvellement épithélial et à un flux sanguin abondant ; les ' + w('k25-prostaglandines', 'prostaglandines (gardiennes de la barrière)') + ' entretiennent ces défenses. L’ulcère apparaît quand l’agression l’emporte.',
 '<b>Helicobacter pylori</b> provoque toujours une gastrite chronique, de gravité variable. Selon la SSI, la gastrite à prédominance antrale, avec gastrine et sécrétion acide élevées, correspond au ' + w('k25-phenotype-duodenal', 'phénotype « ulcère duodénal » (10 à 15 % des infectés)') + ' ; la gastrite à prédominance fundique, avec sécrétion acide basse, expose à l’atrophie, à la métaplasie intestinale et au cancer gastrique (1 à 3 %). Plus de 80 % des infections restent asymptomatiques.',
 'Les <b>AINS et l’aspirine</b> inhibent la cyclo-oxygénase et réduisent les prostaglandines muqueuses ; l’aspirine inhibe aussi l’agrégation plaquettaire, ce qui transforme une petite lésion en hémorragie. Les corticoïdes ne sont pas ulcérogènes par eux-mêmes ; ils augmentent le risque de complication surtout lorsqu’ils sont associés à un AINS (S2k 2023, énoncé 7.4).')
 + C.img('k25_ulcere_histologie.gif', 'Coupe histologique colorée à l’hématoxyline-éosine : bord d’un ulcère gastrique avec épithélium glandulaire à gauche et fond d’ulcère inflammatoire à droite.', 'Bord d’un ulcère gastrique, coloration hématoxyline-éosine, grossissement intermédiaire. L’épithélium glandulaire s’interrompt ; le fond est fait de tissu de granulation inflammatoire.', credit({'auteur': 'Librepath', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Stomach_ulcer_--_intermed_mag.jpg'}))
 + key('Helicobacter pylori et AINS sont les deux grands agresseurs ; les corticoïdes seuls ne sont pas ulcérogènes.')
 + src(SSI, S2K))

C.a(4, 'Étiologies et facteurs de risque', P(
 'Le médecin cherche toujours la cause, car elle commande la prévention de la récidive. Selon la S2k 2023 (énoncé 7.1), les causes fréquentes d’un ulcère non lié à Helicobacter pylori sont les AINS non sélectifs et l’aspirine. En l’absence de ces deux causes, des ' + w('k25-causes-rares', 'causes rares') + ' sont recherchées ; si aucune n’est trouvée, l’ulcère est dit ' + w('k25-idiopathique', 'idiopathique') + ' (recommandation 7.2).')
 + table(['Facteur', 'Rôle', 'Source'], [
   ['Helicobacter pylori', 'Cause ; sans éradication, la récidive est de 64 % (duodénum) et 52 % (estomac)', 'SSI 2026'],
   ['AINS non sélectifs, aspirine, y compris à faible dose', 'Cause fréquente', 'S2k 2023, énoncé 7.1'],
   ['Âge supérieur à 60 ans, antécédent d’ulcère', 'Risque d’ulcère et de complication', 'S2k 2023, énoncés 7.3 et 7.4'],
   ['Aspirine, inhibiteur de P2Y12, anticoagulant', 'Risque de complication hémorragique', 'S2k 2023, énoncé 7.4'],
   ['Corticoïde associé à un AINS', 'Risque de complication', 'S2k 2023, énoncé 7.4'],
   ['ISRS associé à un AINS ou à un antiagrégant', 'Risque hémorragique', 'S2k 2023, recommandation 7.13']])
 + P('Le tableau se lit en deux temps : les deux premières lignes sont des <b>causes</b>, à traiter ; les suivantes sont des <b>facteurs de risque</b>, qui justifient une prophylaxie. Exemple : la patiente de 63 ans sous ibuprofène a un seul facteur, l’âge ; si elle prenait aussi de l’aspirine, une prophylaxie par IPP serait indiquée.')
 + key('Helicobacter pylori, AINS, aspirine : chercher, traiter, prévenir. Sans ces causes, chercher une cause rare avant de parler d’ulcère idiopathique.')
 + src(SSI, S2K))

C.a(5, 'Anamnèse', P(
 'La douleur typique est épigastrique, à type de crampe ou de brûlure, rythmée par les repas. Mais l’anamnèse <b>ne permet pas</b> de distinguer un ulcère d’une ' + w('k25-dyspepsie', 'dyspepsie fonctionnelle') + ' : selon la SSI, environ un tiers des ulcères sont asymptomatiques et 40 à 80 % des ulcères hémorragiques n’ont pas été précédés de symptômes dyspeptiques.',
 'L’anamnèse recherche donc surtout : la prise d’AINS, d’aspirine, d’antiagrégants, d’anticoagulants, de corticoïdes et d’ISRS ; un antécédent d’ulcère ou d’infection à Helicobacter pylori ; le tabac ; les ' + w('k25-alarme', 'signes d’alarme') + ' qui imposent une endoscopie ; une douleur brutale qui fait craindre une perforation ; des vomissements alimentaires tardifs qui font craindre une sténose.')
 + trap('Conclure à l’absence d’ulcère parce que le patient n’a pas mal : l’ulcère sous AINS est souvent silencieux jusqu’à la complication.')
 + key('L’anamnèse sert à trouver la cause et les signes d’alarme, pas à poser le diagnostic d’ulcère.')
 + src(SSI))

C.a(6, 'Examen clinique', P(
 'L’ulcère non compliqué donne peu de signes : sensibilité épigastrique, parfois rien. L’examen cherche surtout une complication. La ' + w('k25-perforation-clinique', 'perforation') + ' donne une douleur brutale, une défense puis une contracture abdominale ; la péritonite n’est cependant présente que chez environ deux tiers des patients, surtout si la perforation est couverte (WSES 2020). L’hémorragie se juge sur les signes vitaux et le toucher rectal (cours K92). La sténose se traduit par des vomissements et un clapotage à jeun.')
 + cards(('Complication suspectée', '<p>Le médecin mesure la fréquence cardiaque, la pression artérielle et la température, qui jugent le retentissement. Il recherche ensuite une défense, une contracture et une disparition de la matité préhépatique, qui signent une perforation, puis il fait un toucher rectal à la recherche d’un méléna.</p>'),
         ('Terrain', '<p>Âge, comorbidités, signes d’hépatopathie, signes de cancer (masse, ganglion de Troisier, amaigrissement).</p>'))
 + trap('Un sujet âgé, sous corticoïdes ou immunodéprimé peut avoir une perforation avec un abdomen peu défendu : l’imagerie tranche.')
 + key('L’examen d’un ulcère suspecté est d’abord la recherche d’une perforation, d’une hémorragie ou d’une sténose.')
 + src(WSES))

C.a(7, 'Urgences : perforation et hémorragie', alert(
 'Quand un patient sous AINS ou porteur d’un ulcère a une douleur abdominale brutale, la WSES recommande une tomodensitométrie, ou à défaut une radiographie thoracique et abdominale debout pour rechercher un ' + w('k25-pneumoperitoine', 'pneumopéritoine') + '. En cas d’instabilité, la réanimation est immédiate (pression artérielle moyenne ≥ 65 mmHg, diurèse ≥ 0,5 mL/kg/h, normalisation du lactate), avec avis chirurgical, hémocultures et antibiothérapie à large spectre.', 'Perforation suspectée.')
 + P('Avec un pneumopéritoine important, une extravasation de contraste ou une péritonite, la WSES recommande la ' + w('k25-chirurgie-perforation', 'chirurgie le plus tôt possible') + ' : suture simple pour un ulcère de moins de 2 cm, par laparoscopie chez le patient stable si l’équipe en a l’expérience, par laparotomie chez le patient instable. Le traitement non opératoire n’est envisagé que dans des cas très sélectionnés, quand l’étude au produit hydrosoluble montre que la perforation est colmatée. Les scores de Boey, PULP et ASA aident à estimer le risque ; l’hypoalbuminémie est le meilleur facteur prédictif isolé de décès.',
 'L’ulcère hémorragique suit la conduite du cours ' + w('k25-hemorragie', 'K92 — Hémorragies digestives') + ' : le patient est réanimé, le score de Glasgow-Blatchford est calculé, l’endoscopie a lieu dans les 24 heures, la classification de Forrest guide l’hémostase endoscopique, puis un IPP à forte dose est donné.')
 + quiz('Un homme de 45 ans a une douleur épigastrique brutale depuis 3 heures et un abdomen de bois. Sa pression est de 128/80 mmHg. La radiographie debout ne montre pas d’air libre. Quelle est l’étape suivante ?',
   [('Gastroscopie en urgence', False), ('Tomodensitométrie abdominale', True), ('IPP oral et réévaluation le lendemain', False)],
   'La radiographie ne voit le pneumopéritoine que dans 30 à 85 % des perforations ; la WSES recommande la tomodensitométrie, éventuellement avec contraste hydrosoluble. L’endoscopie est évitée devant une perforation suspectée.')
 + key('La perforation impose une tomodensitométrie, une réanimation, des antibiotiques et une chirurgie précoce. L’hémorragie suit la conduite du cours K92.')
 + C.pareto('pareto-k25-clinique', 'Reconnaître l’ulcère et ses complications', ['k25-1', 'k25-3', 'k25-4', 'k25-5', 'k25-7'],
     ['Ulcère : franchit la musculaire muqueuse ; érosion : reste muqueuse.',
      'Deux causes dominantes : Helicobacter pylori et AINS ou aspirine.',
      'Les symptômes sont peu fiables, et l’ulcère hémorragique reste souvent silencieux.',
      'Perforation : tomodensitométrie, réanimation, antibiotiques, chirurgie précoce.',
      'Hémorragie : Glasgow-Blatchford, endoscopie ≤ 24 h, Forrest, IPP forte dose.'])
 + src(WSES, ESGE21))

C.a(8, 'Démarche diagnostique', P(
 'L’' + w('k25-ogd', 'œsogastroduodénoscopie') + ' est l’examen de référence : elle voit l’ulcère, le situe, recherche une complication et permet les biopsies. Elle est indiquée en présence de signes d’alarme, d’un risque élevé de cancer gastrique ou après l’échec d’un traitement par IPP (SSI 2026). Devant un ulcère gastrique, des biopsies du bord et du fond sont prises pour exclure un cancer.',
 'L’infection à Helicobacter pylori est recherchée chez tout patient ulcéreux. Pendant l’endoscopie, les biopsies servent à l’histologie et, selon les centres, à la culture ou à la PCR de résistance. Hors endoscopie, le test non invasif standard en Suisse est l’' + w('k25-antigene-selles', 'antigène fécal') + ', complété si possible par une ' + w('k25-pcr-resistance', 'PCR de résistance sur selles') + '. La sérologie n’est pas recommandée, car elle ne distingue pas une infection active d’une infection ancienne.')
 + trap('Tester sous IPP ou après des antibiotiques : la SSI demande d’arrêter les IPP au moins 2 semaines et les antibiotiques au moins 4 semaines avant le test, sous peine de faux négatifs. En cas d’hémorragie aiguë, 25 à 55 % des tests sont faussement négatifs et doivent être répétés.', 'Faux négatif')
 + key('Endoscopie pour voir et biopsier ; Helicobacter pylori recherché chez tout ulcéreux, hors IPP et hors antibiotiques.')
 + src(SSI, S2K))

C.a(9, 'Traitement de l’ulcère non compliqué', P(
 'Le traitement repose sur trois gestes : <b>supprimer la cause</b>, <b>faire cicatriser</b> par un IPP et <b>contrôler</b> la guérison quand c’est nécessaire.',
 'Si Helicobacter pylori est présent, l’' + w('k25-eradication', 'éradication') + ' est indispensable : sans elle, la récidive annuelle est de 52 à 64 % ; après éradication réussie, elle tombe à 0 à 1,6 % par an (SSI 2026). Si un AINS est en cause, il est arrêté jusqu’à cicatrisation ; s’il doit être repris, il l’est sous IPP au long cours (S2k 2023, recommandation 7.7). L’ulcère gastrique induit par un AINS est traité, selon l’information professionnelle suisse de l’ésoméprazole, par 40 mg une fois par jour pendant 4 à 8 semaines.',
 'Un ulcère <b>gastrique</b> fait l’objet d’un ' + w('k25-controle-endoscopique', 'contrôle endoscopique avec biopsies après 4 à 8 semaines') + ' (S2k 2023, recommandation 3.3), car un ulcère d’allure bénigne peut être malin dans 5 % des cas (SSI 2026). Un ulcère duodénal ne demande pas de contrôle endoscopique de routine. La guérison de l’infection est vérifiée par un antigène fécal au moins 4 semaines après la fin du traitement, sans IPP.')
 + C.img('k25_ulcere_gastrique_benin.gif', 'Pièce de gastrectomie : petit ulcère antral arrondi à bords nets, plis muqueux convergeant régulièrement vers le cratère.', 'Ulcère gastrique antral bénin de 1 cm sur une pièce opératoire. Bords nets, fond propre et plis convergents réguliers sont les signes macroscopiques de bénignité ; seule la biopsie les confirme.', credit({'auteur': 'Ed Uthman, MD', 'licence': 'Domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Benign_gastric_ulcer_1.jpg'}))
 + key('On éradique Helicobacter pylori, on arrête l’AINS et on donne un IPP 4 à 8 semaines ; l’ulcère gastrique est contrôlé par endoscopie avec biopsies, car il peut cacher un cancer.')
 + src(SSI, S2K, FI('Nexium®')))

C.a(10, 'Éradication de Helicobacter pylori : choisir le schéma', P(
 'La SSI recommande en 2026 une approche <b>guidée par la résistance</b>, car l’efficacité des traitements empiriques n’atteint souvent que 70 à 90 %. La recherche de résistance à la clarithromycine et à la lévofloxacine, par PCR sur selles ou sur biopsies, permet de traiter environ 70 % des patients par une ' + w('k25-trithérapie', 'trithérapie ciblée') + ' : IPP à double dose, amoxicilline et l’antibiotique auquel la souche est sensible, pendant 14 jours.',
 'Sans test de résistance, le traitement empirique recommandé est la ' + w('k25-bqt', 'quadrithérapie bismuthée') + ' : IPP associé à Pylera®, qui contient bismuth, tétracycline et métronidazole. La clarithromycine n’est jamais donnée à l’aveugle, car la résistance dépasse 15 %.')
 + table(['Situation', 'Schéma (SSI 2026)', 'Durée'], [
   ['Souche sensible à la clarithromycine', 'Oméprazole ou ésoméprazole 40 mg 2×/j + clarithromycine 500 mg 2×/j + amoxicilline 1 g 2×/j', '14 jours'],
   ['Souche sensible à la lévofloxacine', 'Oméprazole ou ésoméprazole 40 mg 2×/j + lévofloxacine 500 mg/j + amoxicilline 1 g 2×/j', '14 jours'],
   ['Résistance inconnue', 'Oméprazole ou ésoméprazole 40 mg 2×/j + Pylera® 3 gélules 4×/j', '10 jours si métronidazole sensible ; 14 jours sinon ou après échec'],
   ['Allergie à la pénicilline', 'Quadrithérapie bismuthée', 'Comme ci-dessus']])
 + P('Le tableau se lit de haut en bas : le résultat du test de résistance choisit la ligne. Les IPP de deuxième génération sont donnés à forte dose deux fois par jour ; la SSI juge le pantoprazole insuffisant pour l’éradication.')
 + trap('L’information professionnelle suisse de l’ésoméprazole décrit encore une trithérapie de 7 jours à 20 mg deux fois par jour, et celle de Pylera® une durée de 10 jours avec oméprazole 20 mg deux fois par jour. La SSI 2026 recommande des IPP à 40 mg deux fois par jour et 14 jours dans la plupart des cas : le texte officiel et la recommandation divergent ; le cours suit la recommandation et signale l’écart.', 'Point discuté')
 + quiz('Une patiente ulcéreuse a un antigène fécal positif. La PCR sur selles montre une résistance à la clarithromycine et une sensibilité à la lévofloxacine. Elle n’est pas allergique à la pénicilline. Quel schéma ?',
   [('Ésoméprazole, clarithromycine, amoxicilline 7 jours', False), ('Ésoméprazole 40 mg 2×/j, lévofloxacine, amoxicilline 14 jours', True), ('Pantoprazole 40 mg 1×/j et métronidazole 7 jours', False)],
   'La trithérapie est choisie selon la sensibilité de la souche ; la SSI recommande 14 jours et un IPP de deuxième génération à forte dose. Les mises en garde de Swissmedic sur les fluoroquinolones restent à respecter.')
 + key('On teste la résistance, puis on traite 14 jours avec un IPP fort deux fois par jour ; sans test, on donne la quadrithérapie bismuthée. Ensuite, on contrôle toujours la guérison.')
 + src(SSI, FI('Pylera®'), FI('Nexium®')))

C.a(11, 'Prévenir l’ulcère chez le patient à risque', P(
 'La S2k 2023 propose une règle simple : un IPP de prophylaxie est indiqué quand un médicament à risque est associé à <b>au moins un facteur de risque supplémentaire</b>. L’âge supérieur à 60 ans, seul, ne suffit pas.')
 + table(['Traitement', 'Prophylaxie par IPP', 'Recommandation S2k 2023'], [
   ['AINS non sélectif', 'Si un autre facteur de risque (antécédent d’ulcère, antithrombotique, corticoïde, comorbidité grave)', '7.5'],
   ['Coxib', 'Si un autre facteur de risque ; toujours si aspirine, inhibiteur de P2Y12, anticoagulant ou ISRS associé', '7.6'],
   ['Aspirine, inhibiteur de P2Y12 ou anticoagulant seul', 'Si au moins un autre facteur de risque', '7.9'],
   ['Deux médicaments antithrombotiques associés', 'Toujours', '7.15'],
   ['Après une complication ulcéreuse, si l’AINS est poursuivi', 'Toujours, même après éradication de Helicobacter pylori', '7.8']])
 + P('Exemple : un homme de 70 ans sous aspirine et clopidogrel après un stent coronaire reçoit un IPP, car il associe deux antithrombotiques. Un homme de 65 ans sans autre facteur, qui prend de l’ibuprofène quelques jours, n’en a pas besoin. Le patient qui a saigné sous aspirine ne doit pas être passé au clopidogrel seul : la S2k recommande de garder l’aspirine sous IPP au long cours (recommandation 7.14).')
 + trap('Prescrire un IPP « par habitude » à tout patient âgé : la S2k précise qu’une prophylaxie n’est pas nécessaire quand l’âge supérieur à 60 ans est le seul facteur de risque (recommandations 7.5 et 7.9).', 'Prescription inutile')
 + key('Médicament à risque + un facteur de risque = IPP ; double antithrombotique = IPP toujours ; âge seul = pas d’IPP.')
 + src(S2K))

C.a(12, 'Ulcère idiopathique, causes rares et sténose', P(
 'Quand Helicobacter pylori est absent, contrôlé par une méthode fiable, et qu’aucun AINS ni aspirine n’est pris, la S2k recommande de chercher une cause rare : maladie de Crohn, gastroduodénite à éosinophiles, mastocytose systémique, vascularite, ischémie, ' + w('k25-gastrinome', 'gastrinome (syndrome de Zollinger-Ellison)') + ', infiltration tumorale, infection à cytomégalovirus ou à herpès simplex, médicaments comme les bisphosphonates ou le potassium. Il faut aussi vérifier une prise cachée d’AINS en automédication.',
 'L’ulcère idiopathique est traité par un IPP à forte dose ; après complication ou en cas de persistance, un IPP en dose standard au long cours est recommandé (S2k 2023, recommandation 7.17). La <b>sténose</b> pyloroduodénale est devenue rare avec les IPP ; elle se traduit par des vomissements alimentaires et une dilatation gastrique.')
 + C.img('k25_ulcere_pylorique_macro.gif', 'Pièce opératoire : estomac très dilaté avec un épaississement de la région pylorique, en rapport avec un ulcère pylorique chronique sténosant.', 'Sténose pylorique par ulcère chronique : l’estomac, en amont de l’obstacle, est très dilaté.', credit({'auteur': 'Narraburra', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Gross_stomach_enlargement,_pyloric_obstruction,_chronic_pyloric_ulcer.jpg'}))
 + key('Sans Helicobacter pylori ni AINS, on cherche une cause rare, puis on donne un IPP à forte dose ; après une complication, l’IPP se poursuit au long cours.')
 + src(S2K))

C.a(13, 'Situations particulières', P(
 '<b>Pendant la grossesse</b>, Pylera® est contre-indiqué pendant la grossesse et l’allaitement selon son information professionnelle suisse ; l’éradication est en règle reportée. <b>En cas d’insuffisance rénale ou hépatique</b>, Pylera® est également contre-indiqué. <b>Sous anticoagulant oral</b>, le métronidazole potentialise les antivitamines K : le temps de prothrombine est contrôlé pendant l’éradication. <b>Aux soins intensifs</b>, une prophylaxie des ulcères de stress par IPP est recommandée chez les patients à haut risque, par exemple en cas de troubles de la coagulation ou de ventilation mécanique de plus de 48 heures (S2k 2023, recommandation 7.18).',
 '<b>Reprenons le cas.</b> La patiente de 63 ans sous ibuprofène a un ulcère antral de 1 cm. Les biopsies sont bénignes et montrent Helicobacter pylori, sensible à la lévofloxacine. L’ibuprofène est arrêté ; elle reçoit une trithérapie ciblée de 14 jours, puis un IPP jusqu’à 8 semaines. La gastroscopie de contrôle à 8 semaines montre une cicatrisation ; l’antigène fécal, fait 4 semaines après l’arrêt de l’IPP, est négatif.')
 + key('Pylera® ne se donne pas pendant la grossesse ni en cas d’insuffisance rénale ou hépatique ; sous antivitamine K, on contrôle le temps de prothrombine.')
 + src(FI('Pylera®'), S2K))

C.a(14, 'Critères formels du diagnostic et paramètres clés', alert(
 '<p>Un <b>ulcère</b> est une perte de substance qui franchit la musculaire muqueuse, vue à l’endoscopie ou sur pièce opératoire. Un ulcère est <b>lié à Helicobacter pylori</b> quand l’infection est démontrée par histologie, culture, PCR ou antigène fécal, en dehors des IPP et des antibiotiques. Il est <b>lié aux AINS</b> quand le patient prend un AINS ou de l’aspirine, sans autre cause. Il est <b>idiopathique</b> quand aucune cause n’est trouvée après une recherche complète. Enfin, on parle de <b>guérison de l’infection</b> quand l’antigène fécal est négatif au moins 4 semaines après la fin du traitement, sans IPP.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> L’ulcère récidive dans 52 à 64 % des cas sans éradication, mais seulement dans 0 à 1,6 % par an après éradication. On arrête l’IPP 2 semaines et les antibiotiques 4 semaines avant le test. La trithérapie ciblée ou la quadrithérapie bismuthée dure en règle 14 jours. L’ulcère gastrique est contrôlé par endoscopie à 4 à 8 semaines. La perforation impose une tomodensitométrie et une chirurgie précoce, avec une suture si elle mesure moins de 2 cm.</div>'
 + C.pareto('pareto-k25-traitement', 'Diagnostic, traitement et prévention', ['k25-8', 'k25-9', 'k25-10', 'k25-11', 'k25-12'],
     ['On fait une endoscopie avec biopsies et on recherche Helicobacter pylori hors IPP et antibiotiques.',
      'Éradication : test de résistance, trithérapie ciblée 14 jours, IPP fort deux fois par jour.',
      'Sans test : quadrithérapie bismuthée ; jamais de clarithromycine à l’aveugle.',
      'Ulcère gastrique : contrôle endoscopique à 4 à 8 semaines.',
      'On prescrit un IPP quand un médicament à risque s’ajoute à un facteur de risque, et toujours sous double antithrombotique.'])
 + src(SSI, S2K, WSES))

# ---------------- Onglet Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question : y a-t-il un ulcère, est-il compliqué, quelle est sa cause, l’infection est-elle guérie ?')
 + table(['Question', 'Examen', 'Statut'], [
   ['Y a-t-il un ulcère ? est-il malin ?', w('k25-ogd', 'Œsogastroduodénoscopie avec biopsies (gold standard)'), 'Indiquée si signes d’alarme, risque de cancer ou échec des IPP'],
   ['Perforation ?', 'Tomodensitométrie ; radiographie debout si indisponible', 'Indiquée en urgence'],
   ['Helicobacter pylori sans endoscopie ?', w('k25-antigene-selles', 'Antigène fécal') + ', avec ' + w('k25-pcr-resistance', 'PCR de résistance'), 'Indiqué'],
   ['Helicobacter pylori pendant l’endoscopie ?', 'Histologie, culture ou PCR sur biopsies', 'Indiqué'],
   ['Infection guérie ?', 'Antigène fécal ≥ 4 semaines après traitement, sans IPP', 'Indiqué après tout traitement'],
   ['Infection ancienne ou active ?', 'Sérologie', 'Non recommandée']])
 + P('Le tableau se lit de haut en bas. Le test respiratoire à l’urée marquée reste fiable, mais la SSI ne le recommande plus comme test de routine en Suisse, car il exige un personnel formé et un laboratoire équipé, sans donner d’information sur la résistance.')
 + key('Endoscopie pour voir et biopsier, tomodensitométrie pour la perforation, antigène fécal et PCR de résistance pour Helicobacter pylori.')
 + src(SSI, WSES))

C.e(2, 'Interpréter les tests de Helicobacter pylori', P(
 'Les performances rapportées par la SSI sont proches. L’antigène fécal a une sensibilité de 93 à 95 % et une spécificité de 96 à 98 %, la PCR de résistance sur selles dépasse 95 %, et le test respiratoire atteint 90 à 95 %. La sérologie atteint 80 à 95 %, mais elle ne distingue pas une infection active d’une infection ancienne. La culture sur biopsies reste la référence de l’antibiogramme, avec une sensibilité de 75 à 91 % selon l’expérience du laboratoire.',
 'La cause principale d’erreur est le <b>faux négatif</b> : IPP, antibiotiques, bismuth et hémorragie aiguë réduisent la charge bactérienne. Un résultat négatif dans ces circonstances ne prouve pas l’absence d’infection.')
 + quiz('Un patient a saigné d’un ulcère duodénal il y a 3 jours. Les biopsies prises sous IPP intraveineux sont négatives pour Helicobacter pylori. Que faire ?',
   [('Conclure à un ulcère idiopathique', False), ('Répéter le test après arrêt de l’IPP pendant 2 semaines', True), ('Faire une sérologie', False)],
   'Pendant l’hémorragie et sous IPP, 25 à 55 % des tests sont faussement négatifs ; l’ESGE et la SSI demandent de répéter le test.')
 + key('Un test négatif sous IPP, sous antibiotique ou pendant une hémorragie doit être répété.')
 + src(SSI, ESGE21))

C.e(3, 'Endoscopie et imagerie : ce qu’il faut lire', P(
 'Le compte rendu d’endoscopie nomme le siège, la taille, l’aspect des bords et du fond, le stigmate de Forrest en cas d’hémorragie et le nombre de biopsies. Un ulcère gastrique à bords irréguliers, surélevés, avec des plis interrompus ou en massue, fait suspecter un cancer ; les biopsies multiples et le contrôle à 4 à 8 semaines restent nécessaires même si l’aspect est bénin.',
 'Pour la perforation, la tomodensitométrie montre de l’air libre, un épanchement, un épaississement pariétal ou une extravasation de contraste ; jusqu’à 12 % des perforations ont une tomodensitométrie normale, ce qui justifie le contraste hydrosoluble en cas de doute (WSES 2020). La radiographie debout ne montre l’air libre que dans 30 à 85 % des cas.')
 + quiz('Un ulcère gastrique de 15 mm à bords réguliers a été biopsié : aucune cellule maligne. Faut-il un contrôle endoscopique ?',
   [('Non, les biopsies sont rassurantes', False), ('Oui, après 4 à 8 semaines, avec de nouvelles biopsies si la cicatrisation est incomplète', True)],
   'La S2k recommande ce contrôle pour tout ulcère gastrique ; selon la SSI, 5 % des ulcères d’allure bénigne sont malins.')
 + key('On biopsie l’ulcère gastrique et on le revoit. Devant une perforation, on fait une tomodensitométrie, avec un contraste hydrosoluble en cas de doute.')
 + C.pareto('pareto-k25-examens', 'Examens', ['k25-e-1', 'k25-e-2', 'k25-e-3'],
     ['L’œsogastroduodénoscopie avec biopsies est l’examen de référence.',
      'L’antigène fécal et la PCR de résistance sont les tests non invasifs de référence en Suisse.',
      'Les IPP, les antibiotiques, le bismuth et l’hémorragie donnent des faux négatifs, car ils réduisent la charge bactérienne.',
      'Contrôle de l’éradication ≥ 4 semaines après traitement, sans IPP.',
      'La perforation se recherche par tomodensitométrie ; la radiographie ne sert que si elle est indisponible.'])
 + src(SSI, S2K, WSES))

# ---------------- Onglet Sciences
C.s('anat', 'Anatomie', 'Anatomie : sièges de l’ulcère et artères à risque', P(
 'L’ulcère gastrique siège surtout sur la petite courbure et l’antre ; l’ulcère duodénal siège surtout dans le bulbe. La face postérieure du bulbe est en rapport avec l’artère gastroduodénale, d’où des hémorragies massives ; la face antérieure regarde la cavité péritonéale libre, d’où les perforations avec pneumopéritoine. Un ulcère postérieur peut aussi pénétrer dans le pancréas.')
 + key('L’ulcère bulbaire antérieur perfore, car la paroi antérieure donne sur la cavité péritonéale ; l’ulcère bulbaire postérieur saigne ou pénètre le pancréas, car il érode l’artère gastroduodénale située en arrière.', 'Science → clinique.'))
C.s('histo', 'Histologie', 'Histologie : muqueuse fundique, antrale et gastrite', P(
 'La muqueuse fundique contient les cellules pariétales, qui sécrètent l’acide et le facteur intrinsèque, et les cellules principales, qui sécrètent le pepsinogène. La muqueuse antrale contient les cellules G, qui sécrètent la gastrine, et les cellules D, qui sécrètent la somatostatine. Helicobacter pylori vit dans le mucus, au contact de l’épithélium, et provoque un infiltrat lymphoplasmocytaire avec polynucléaires : la gastrite chronique active.',
 'Le fond d’un ulcère comporte, de la surface vers la profondeur, un enduit fibrinoleucocytaire, une nécrose fibrinoïde, un tissu de granulation puis une fibrose ; la fibrose explique la sténose des ulcères chroniques.')
 + key('La gastrite antrale augmente la gastrine et l’acide, ce qui mène à l’ulcère duodénal ; à l’inverse, la gastrite fundique diminue l’acide et mène à l’atrophie et au cancer.', 'Science → clinique.'))
C.s('phys', 'Physiologie', 'Physiologie : la sécrétion acide', P(
 'La cellule pariétale sécrète des ions H⁺ par la pompe H⁺/K⁺-ATPase. Trois stimulants agissent sur elle : l’histamine (récepteurs H2), la gastrine et l’acétylcholine. La somatostatine freine la sécrétion. Les IPP bloquent l’étape finale, la pompe elle-même, ce qui explique leur efficacité supérieure aux antihistaminiques H2.',
 'Le pH intragastrique conditionne l’éradication : Helicobacter pylori ne se multiplie pas entre pH 4 et 6 ; l’amoxicilline et la clarithromycine n’agissent que sur des bactéries en division. Élever le pH par un IPP fort fait entrer la bactérie en division et la rend sensible (SSI 2026).')
 + key('Un IPP fort deux fois par jour est une condition d’efficacité des antibiotiques contre Helicobacter pylori.', 'Science → traitement.'))
C.s('micro', 'Microbiologie', 'Microbiologie : Helicobacter pylori et sa résistance', P(
 'Helicobacter pylori est un bacille à Gram négatif, spiralé, microaérophile. Son uréase transforme l’urée en ammoniac, qui tamponne l’acide autour de la bactérie ; c’est la base du test respiratoire. La résistance à la clarithromycine est liée à des mutations ponctuelles de l’ARN ribosomique 23S, détectables par PCR ; la résistance à la lévofloxacine est liée à des mutations de la gyrase.',
 'En Suisse, les données ANRESIS citées par la SSI, issues surtout de patients déjà traités, montrent une résistance de 28 % à la clarithromycine, 18 % à la lévofloxacine et 44 % au métronidazole, contre 3 % à l’amoxicilline et 4 % à la tétracycline.')
 + key('Les résistances à la clarithromycine et à la lévofloxacine sont fréquentes et doivent être testées, alors que celles à l’amoxicilline et à la tétracycline sont rares.', 'Science → traitement.'))

# ---------------- Onglet Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'La pharmacologie de l’ulcère poursuit trois buts : réduire l’acide pour cicatriser, éradiquer Helicobacter pylori, prévenir la récidive chez le patient qui doit garder un médicament à risque.')
 + table(['Classe', 'Molécule disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Inhibiteur de la pompe à protons', 'Ésoméprazole, oméprazole, pantoprazole', 'Cicatrisation, prophylaxie, éradication (ésoméprazole ou oméprazole)', w('k25-d-ipp', 'Monographie')],
   ['Association bismuth, tétracycline, métronidazole', 'Pylera®', 'Quadrithérapie bismuthée', w('k25-d-pylera', 'Monographie')],
   ['Pénicilline', 'Amoxicilline', 'Trithérapie ciblée', w('k25-d-amox', 'Monographie')],
   ['Macrolide', 'Clarithromycine', 'Trithérapie si souche sensible', w('k25-d-clari', 'Monographie')],
   ['Fluoroquinolone', 'Lévofloxacine', 'Trithérapie si souche sensible', w('k25-d-levo', 'Monographie')]])
 + P('Le tableau se lit par la colonne « Place » : les antibiotiques ne sont jamais donnés sans IPP, et le choix entre clarithromycine et lévofloxacine dépend du test de résistance.')
 + key('IPP pour cicatriser et prévenir ; antibiotiques choisis selon la résistance pour éradiquer.')
 + src(SSI, S2K))

C.p(2, 'Doses et durées', P('Les doses proviennent de la SSI 2026 et des informations professionnelles suisses ; les écarts sont signalés.')
 + table(['Médicament', 'Dose', 'Durée', 'Source'], [
   ['Ésoméprazole, ulcère gastrique sous AINS', '40 mg 1×/j', '4 à 8 semaines', 'Information professionnelle suisse Nexium®'],
   ['Ésoméprazole, prévention sous AINS', '20 mg 1×/j', 'Durée du traitement à risque', 'Information professionnelle suisse Nexium®'],
   ['Ésoméprazole ou oméprazole, éradication', '40 mg 2×/j', '14 jours (10 jours avec Pylera® si métronidazole sensible)', 'SSI 2026 ; les informations professionnelles prévoient 20 mg 2×/j'],
   ['Pylera®', '3 gélules 4×/j, après les repas et au coucher', '10 jours (information professionnelle) ; 10 ou 14 jours (SSI)', 'Information professionnelle suisse Pylera® ; SSI 2026'],
   ['Amoxicilline', '1 g 2×/j', '14 jours', 'SSI 2026'],
   ['Clarithromycine', '500 mg 2×/j', '14 jours, seulement si souche sensible', 'SSI 2026'],
   ['Lévofloxacine', '500 mg 1×/j ou 250 mg 2×/j', '14 jours, seulement si souche sensible', 'SSI 2026']])
 + P('Exemple : la patiente traitée par trithérapie à la lévofloxacine prend chaque jour ésoméprazole 40 mg matin et soir, amoxicilline 1 g matin et soir et lévofloxacine 500 mg, pendant 14 jours, puis l’IPP seul jusqu’à cicatrisation.')
 + key('Pour l’éradication, la SSI recommande un IPP à 40 mg deux fois par jour pendant 14 jours ; Pylera® se prend à 3 gélules quatre fois par jour.')
 + src(SSI, FI('Nexium®'), FI('Pylera®')))

C.p(3, 'Interactions, surveillance et effets indésirables', alert(
 'Métronidazole : effet antabuse, pas d’alcool pendant le traitement et 24 heures après ; potentialisation des antivitamines K. Clarithromycine : puissant inhibiteur du CYP3A4, à confronter aux statines, aux anticoagulants et aux médicaments qui allongent le QT. Ésoméprazole : association au clopidogrel déconseillée par l’information professionnelle suisse ; méthotrexate à forte dose : suspendre l’IPP.', 'Interactions dangereuses.')
 + P('Les patients sont prévenus des effets attendus : selles noires sous bismuth, goût métallique sous métronidazole, photosensibilité sous tétracycline. La SSI rappelle que 40 à 70 % des patients ont des effets indésirables sous quadrithérapie et que l’abandon non expliqué est une cause majeure d’échec. Les gélules de Pylera® sont prises assis, avec un grand verre d’eau, pour éviter une ulcération œsophagienne par la tétracycline.',
 'Au long cours, les IPP exposent à l’hypomagnésémie (après au moins 3 mois), à un risque modérément accru de fractures et d’infections digestives (information professionnelle suisse). Leur indication est réévaluée régulièrement.')
 + key('Métronidazole : pas d’alcool, attention aux antivitamines K ; clarithromycine : CYP3A4 ; IPP au long cours : magnésium et réévaluation.')
 + C.pareto('pareto-k25-pharma', 'Pharmacologie', ['k25-p-1', 'k25-p-2', 'k25-p-3'],
     ['L’IPP se donne à 40 mg 1×/j pendant 4 à 8 semaines pour cicatriser, et à 20 mg 1×/j en prévention.',
      'L’éradication associe un IPP à 40 mg 2×/j pendant 14 jours et des antibiotiques choisis selon la résistance.',
      'Pylera® 3 gélules 4×/j ; selles noires attendues.',
      'Le métronidazole interagit avec l’alcool et les antivitamines K, et la clarithromycine avec les substrats du CYP3A4.',
      'IPP au long cours : magnésium, fractures, réévaluation.'])
 + src(FI('Pylera®'), FI('Nexium®'), SSI))

# ---------------- Fenêtres
L = lab
C.pop('k25-ulcere-def', 'Ulcère ou érosion', L(('Définition', 'L’ulcère franchit la musculaire muqueuse ; l’érosion reste dans la muqueuse.'), ('Conséquence', 'L’ulcère peut atteindre une artère sous-muqueuse et saigner abondamment, ou traverser la paroi et perforer ; il cicatrise par fibrose.'), ('Piège', 'Le terme « ulcère » est souvent employé à tort pour des érosions vues à l’endoscopie ; le compte rendu doit être précis.')) + src(S2K) + C.img('k25_ulcere_histologie.gif', 'Coupe histologique du bord d’un ulcère gastrique.', 'Au bord de l’ulcère, l’épithélium s’interrompt et le fond inflammatoire descend sous la musculaire muqueuse ; c’est ce franchissement qui distingue l’ulcère de l’érosion.', credit({'auteur': 'Librepath', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Stomach_ulcer_--_intermed_mag.jpg'})))
C.pop('k25-deux-causes', 'Helicobacter pylori et AINS', L(('Helicobacter pylori', 'Helicobacter pylori provoque toujours une gastrite chronique et cause surtout l’ulcère duodénal ; sans éradication, la récidive est très fréquente.'), ('AINS et aspirine', 'Les AINS et l’aspirine diminuent les prostaglandines et inhibent l’agrégation plaquettaire ; c’est pourquoi leurs ulcères restent souvent silencieux jusqu’à une complication.'), ('Synergie', 'Les deux causes s’additionnent ; leur association justifie la recherche de l’infection chez le patient ulcéreux sous AINS.')) + src(SSI, S2K))
C.pop('k25-prostaglandines', 'Prostaglandines et barrière muqueuse', L(('Rôle', 'Elles stimulent la sécrétion de mucus et de bicarbonates et maintiennent le flux sanguin muqueux.'), ('Conséquence', 'Les AINS, en inhibant la cyclo-oxygénase, affaiblissent la barrière ; les coxibs, plus sélectifs de la COX-2, l’affaiblissent moins.')) + src(S2K))
C.pop('k25-phenotype-duodenal', 'Phénotypes de la gastrite à Helicobacter pylori', L(('Gastrite modérée', 'Plus de 80 % des infectés ont une gastrite modérée, avec une sécrétion acide normale et sans complication.'), ('Phénotype « ulcère duodénal »', 'Chez 10 à 15 % des infectés, la gastrite prédomine dans l’antre ; la gastrine et l’acide augmentent, ce qui favorise l’ulcère duodénal.'), ('Phénotype « cancer gastrique »', 'Chez 1 à 3 % des infectés, la gastrite prédomine dans le fundus ; l’acide baisse, et l’atrophie, la métaplasie intestinale puis le cancer peuvent survenir.')) + src(SSI))
C.pop('k25-causes-rares', 'Causes rares d’ulcère (S2k 2023, tableau 11)', L(('Inflammatoires', 'Les causes inflammatoires sont la gastroentérite à éosinophiles, la maladie de Crohn, la maladie de Behçet, la sarcoïdose et les vascularites.'), ('Infectieuses', 'Les causes infectieuses sont le cytomégalovirus, l’herpès simplex et, plus rarement, Candida, le virus d’Epstein-Barr, les mycobactéries et le tréponème.'), ('Médicamenteuses', 'Les médicaments en cause sont les ISRS, les bisphosphonates, le potassium, le sirolimus, le mycophénolate, les chimiothérapies et la spironolactone.'), ('Ischémiques et toxiques', 'Une chimioembolisation ou une radioembolisation récente, la cocaïne et les amphétamines provoquent des ulcères par ischémie ou toxicité.'), ('Tumorales et sécrétoires', 'Le gastrinome (y compris dans la NEM 1), la mastocytose systémique et l’infiltration tumorale en sont les causes tumorales et sécrétoires.'), ('Stress', 'Le choc, le sepsis, le polytraumatisme, les brûlures et la ventilation mécanique prolongée provoquent des ulcères de stress.')) + src(S2K))
C.pop('k25-idiopathique', 'Ulcère idiopathique', L(('Définition', 'Un ulcère est idiopathique quand Helicobacter pylori est absent sur un test fiable, sans AINS ni aspirine et sans cause rare.'), ('Pronostic', 'Il récidive et resaigne plus souvent que l’ulcère lié à Helicobacter pylori, car sa cause persiste.'), ('Traitement', 'On le traite par un IPP à forte dose ; après une complication ou en cas de persistance, l’IPP se poursuit au long cours en dose standard (S2k, recommandation 7.17).')) + src(S2K))
C.pop('k25-dyspepsie', 'Dyspepsie et ulcère', L(('Fait', 'Les symptômes ne distinguent pas l’ulcère de la dyspepsie fonctionnelle.'), ('Chiffre', 'Environ 5 % des dyspepsies sont dues à Helicobacter pylori ; seul un tiers des patients traités est soulagé.'), ('Conséquence', 'La dyspepsie seule, sans facteur de risque, n’est pas une indication à tester et traiter selon la SSI.')) + src(SSI))
C.pop('k25-alarme', 'Signes d’alarme', L(('Liste', 'Les signes d’alarme sont un amaigrissement involontaire, des vomissements persistants, une dysphagie, une hématémèse ou un méléna et une anémie, car ils font craindre un cancer ou une complication.'), ('Conduite', 'Ils imposent une endoscopie, et l’information professionnelle de l’ésoméprazole demande d’exclure un cancer avant de traiter un ulcère gastrique suspecté.')) + src(SSI, FI('Nexium®')))
C.pop('k25-perforation-clinique', 'Clinique de la perforation', L(('Tableau', 'La douleur épigastrique est brutale, puis devient diffuse ; une défense, puis une contracture apparaissent, et un choc septique survient parfois.'), ('Limite', 'La péritonite manque dans environ un tiers des cas, surtout si la perforation est couverte.'), ('Biologie', 'L’hyperleucocytose, l’acidose métabolique et une amylase parfois élevée ne sont pas spécifiques ; la WSES recommande cependant des gaz du sang, car le lactate et l’acidose mesurent la gravité.')) + src(WSES))
C.pop('k25-pneumoperitoine', 'Pneumopéritoine', L(('Définition', 'Le pneumopéritoine est la présence d’air libre dans la cavité péritonéale.'), ('Détection', 'La tomodensitométrie le détecte le mieux, alors que la radiographie debout ou en décubitus latéral gauche ne le montre que dans 30 à 85 % des perforations.'), ('Piège', 'Son absence n’exclut pas la perforation ; en cas de doute, un contraste hydrosoluble aide à la montrer.')) + src(WSES) + C.img('k25_pneumoperitoneum_rx.gif', 'Radiographie thoracique : croissant d’air libre sous la coupole diaphragmatique gauche.', 'L’air libre dessine un croissant clair sous la coupole, car il monte au point le plus haut de la cavité péritonéale ; or, son absence n’exclut pas une perforation.', credit({'auteur': 'Cerevisae', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Chest_X-ray_showing_presence_of_free_air_under_left_diaphragm.png'})))
C.pop('k25-chirurgie-perforation', 'Chirurgie de l’ulcère perforé', L(('Délai', 'On opère le plus tôt possible, surtout après 70 ans et en cas de présentation tardive, car la péritonite aggrave le pronostic d’heure en heure.'), ('Technique', 'Un ulcère < 2 cm se ferme par une suture primaire, alors qu’un ulcère > 2 cm demande une approche adaptée au siège ; une résection avec examen extemporané s’impose si un cancer gastrique est suspecté.'), ('Voie', 'Le patient stable est opéré par laparoscopie et le patient instable par laparotomie ; en cas de choc septique, on applique une stratégie de contrôle des dégâts.')) + src(WSES))
C.pop('k25-hemorragie', 'Ulcère hémorragique', L(('Renvoi', 'La prise en charge complète est détaillée dans le cours K92 — Hémorragies digestives.'), ('Spécificité ulcéreuse', 'Dès la première endoscopie, on prélève des biopsies à la recherche de Helicobacter pylori ; si elles sont négatives, on refait un test, car le saignement donne des faux négatifs. Ensuite, on éradique puis on contrôle.')) + src(ESGE21))
C.pop('k25-ogd', 'Œsogastroduodénoscopie', L(('Rôle', 'L’œsogastroduodénoscopie est l’examen de référence : elle visualise l’ulcère, le situe, le mesure, le classe et permet les biopsies.'), ('Indications', 'On la demande en cas de signes d’alarme, de risque élevé de cancer gastrique, d’échec des IPP ou d’hémorragie, ainsi que pour contrôler un ulcère gastrique.'), ('Contre-indication relative', 'Si une perforation est suspectée, l’imagerie passe d’abord, car l’insufflation aggraverait la fuite.')) + src(SSI, S2K))
C.pop('k25-antigene-selles', 'Antigène fécal de Helicobacter pylori', L(('Principe', 'Ce test détecte par immunologie des antigènes bactériens dans les selles.'), ('Performance', 'Sa sensibilité est de 93 à 95 % et sa spécificité de 96 à 98 % (SSI).'), ('Conditions', 'Il faut arrêter les IPP 2 semaines et les antibiotiques 4 semaines avant, car ils réduisent la charge bactérienne ; il convient au contrôle de l’éradication.')) + src(SSI))
C.pop('k25-pcr-resistance', 'PCR de résistance', L(('Principe', 'La PCR amplifie l’ADN bactérien et recherche les mutations de résistance à la clarithromycine et à la lévofloxacine.'), ('Usage', 'La SSI propose de l’enchaîner automatiquement à un antigène fécal positif quand un traitement est prévu.'), ('Limite', 'Elle ne teste pas le métronidazole, et sa disponibilité reste limitée.')) + src(SSI))
C.pop('k25-eradication', 'Éradication de Helicobacter pylori', L(('Bénéfice', 'Il suffit de traiter 2 patients pour éviter une récidive d’ulcère duodénal et 3 pour l’ulcère gastrique ; de plus, l’éradication baisse le risque de cancer gastrique de 46 à 53 % dans les méta-analyses.'), ('Règle', 'Le traitement est guidé par la résistance, et la guérison est toujours contrôlée.')) + src(SSI))
C.pop('k25-controle-endoscopique', 'Contrôle endoscopique de l’ulcère gastrique', L(('Délai', 'Le contrôle se fait 4 à 8 semaines après le début du traitement.'), ('But', 'Il confirme la cicatrisation et permet de rebiopsier si elle est incomplète, afin d’exclure un cancer.'), ('Ulcère duodénal', 'L’ulcère duodénal n’est pas contrôlé en routine, car les cancers duodénaux sont exceptionnels.')) + src(S2K, SSI))
C.pop('k25-trithérapie', 'Trithérapie ciblée', L(('Composition', 'La trithérapie associe un IPP à forte dose, l’amoxicilline et, selon la sensibilité, la clarithromycine, la lévofloxacine ou le métronidazole.'), ('Avantages', 'Elle comporte six comprimés par jour en deux prises et donne moins d’effets indésirables que la quadrithérapie.'), ('Condition', 'Elle exige un test de résistance préalable et l’absence d’allergie à la pénicilline.')) + src(SSI))
C.pop('k25-bqt', 'Quadrithérapie bismuthée', L(('Composition', 'Elle associe un IPP et Pylera®, qui contient le bismuth, la tétracycline et le métronidazole dans la même gélule.'), ('Efficacité', 'Elle guérit 80 à 90 % des patients dans les essais, mais souvent moins en pratique, car le schéma est complexe.'), ('Contraintes', 'Elle impose 14 comprimés par jour en quatre prises, provoque des effets indésirables chez 40 à 70 % des patients et a déjà connu des ruptures de stock.')) + src(SSI, FI('Pylera®')))
C.pop('k25-gastrinome', 'Syndrome de Zollinger-Ellison', L(('Mécanisme', 'Une tumeur neuroendocrine sécrète de la gastrine ; l’hypersécrétion acide provoque des ulcères multiples, distaux, récidivants, souvent avec diarrhée.'), ('Indice', 'Des ulcères multiples, distaux ou réfractaires sans Helicobacter pylori ni AINS doivent faire évoquer ce syndrome.'), ('Traitement acide', 'On débute l’ésoméprazole à 40 mg deux fois par jour, puis on adapte la dose (information professionnelle suisse).')) + src(S2K, FI('Nexium®')))
C.pop('k25-d-ipp', 'Inhibiteurs de la pompe à protons', L(('Mécanisme', 'Les IPP inhibent de façon irréversible la pompe H⁺/K⁺-ATPase ; leur effet est maximal s’ils sont pris avant le repas, car la pompe est alors activée.'), ('Indications suisses (ésoméprazole)', 'L’ésoméprazole est autorisé pour l’éradication de Helicobacter pylori, l’ulcère gastrique sous AINS, la prévention sous AINS, le syndrome de Zollinger-Ellison et la prévention de la récidive hémorragique.'), ('Précautions', 'Ils interagissent avec le clopidogrel et le méthotrexate à forte dose ; au long cours, ils exposent à l’hypomagnésémie, aux fractures et aux infections digestives.')) + src(FI('Nexium®')))
C.pop('k25-d-pylera', 'Pylera®', L(('Composition', 'Pylera® contient du sous-citrate de bismuth potassique, du métronidazole et du chlorhydrate de tétracycline.'), ('Posologie suisse', 'L’information professionnelle prévoit 3 gélules 4 fois par jour pendant 10 jours, avec oméprazole 20 mg 2 fois par jour ; la SSI recommande cependant un IPP à 40 mg et jusqu’à 14 jours.'), ('Contre-indications', 'Il est contre-indiqué pendant la grossesse et l’allaitement, chez l’enfant de moins de 12 ans, en cas d’insuffisance rénale ou hépatique et dans le syndrome de Cockayne.')) + src(FI('Pylera®'), SSI))
C.pop('k25-d-amox', 'Amoxicilline', L(('Place', 'L’amoxicilline est le pilier de la trithérapie, car la résistance reste rare (3 % dans les données suisses citées par la SSI).'), ('Dose', 'Elle se donne à 1 g deux fois par jour pendant 14 jours.'), ('Contre-indication', 'En cas d’allergie aux pénicillines, on choisit la quadrithérapie bismuthée.')) + src(SSI))
C.pop('k25-d-clari', 'Clarithromycine', L(('Place', 'On ne la donne que si la souche est sensible, car la résistance dépasse 15 %.'), ('Dose', 'Elle se donne à 500 mg deux fois par jour pendant 14 jours.'), ('Interactions', 'Elle inhibe puissamment le CYP3A4 et allonge le QT.')) + src(SSI, FI('Nexium®')))
C.pop('k25-d-levo', 'Lévofloxacine', L(('Place', 'On ne la donne que si la souche est sensible, car la résistance dépasse 15 %.'), ('Dose', 'Elle se donne à 500 mg une fois par jour ou 250 mg deux fois par jour pendant 14 jours.'), ('Sécurité', 'Swissmedic et l’EMA mettent en garde contre les tendinopathies, l’anévrisme aortique et la neuropathie des fluoroquinolones ; on les réserve donc aux indications justifiées.')) + src(SSI))

from K25_liaisons import L as _LZ
from K25_termes import ajouter as _termes
_termes(C, SSI, S2K, ESGE21, WSES, FI)
C.liaisons = _LZ
C.write()
