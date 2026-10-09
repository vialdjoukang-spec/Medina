# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('C18', 'Tumeur maligne du côlon : cancer du côlon localisé',
    'C18 — Tumeur maligne du côlon · CIM-10-GM 2024 · Côlon',
    'Adulte · adénocarcinome du côlon localisé (stades I à III), dépistage, bilan, chirurgie, traitement adjuvant et surveillance · rédaction du 09.10.2026 · référentiels ESMO cancer du côlon localisé 2020, UICC TNM 8e édition, OPAS art. 12e (version du 1er juillet 2026), OFS/ONEC 2018-2022, informations professionnelles suisses',
    'Pharmacologie du traitement adjuvant')
w = C.w
ESMO = ('Argilés G. et al., Localised colon cancer: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up, Ann Oncol 2020;31:1291-1305', 'https://doi.org/10.1016/j.annonc.2020.06.022')
TNM = ('UICC, TNM Classification of Malignant Tumours, 8e édition — tableau supplémentaire S1 de la recommandation ESMO 2020', 'https://www.annalsofoncology.org/cms/10.1016/j.annonc.2020.06.022/attachment/dd2a0bf3-36ed-44d3-846a-71d5e6786b04/mmc1.pdf')
OPAS = ('Ordonnance du DFI sur les prestations de l’assurance des soins (OPAS, RS 832.112.31), art. 12e, let. d, version en vigueur depuis le 1er juillet 2026', 'https://www.fedlex.admin.ch/eli/cc/1995/4964_4964_4964/fr')
OFS = ('Office fédéral de la statistique et Organe national d’enregistrement du cancer, Monitorage du cancer en Suisse, cancer colorectal, moyennes annuelles 2018-2022 (publié le 10.11.2025)', 'https://krebs-monitoring.bfs.admin.ch/fr/detail/C18-20/')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 68 ans consulte pour une fatigue ; or, sa formule sanguine montre une anémie ferriprive, et il signale depuis deux mois une modification du transit et une perte de poids de 4 kg. <b>La question est donc de savoir s’il a un ' + w('c18-ccr', 'cancer du côlon') + ', comment le confirmer, en préciser l’extension et décider du traitement.</b>',
 'Pour y répondre, le médecin doit savoir : reconnaître les signes d’appel ; exiger une ' + w('c18-colo', 'coloscopie totale') + ' avec biopsies ; demander un ' + w('c18-tdm', 'scanner thoraco-abdomino-pelvien') + ' et le dosage de l’' + w('c18-ace', 'antigène carcinoembryonnaire') + ' ; lire la classification ' + w('c18-tnm', 'TNM') + ' ; ensuite, indiquer une chimiothérapie adjuvante selon le stade et le statut ' + w('c18-mmr', 'MMR/MSI') + ' ; enfin, organiser la surveillance.')
 + key('Anémie ferriprive, troubles du transit et amaigrissement après 50 ans : coloscopie totale, puis bilan d’extension.', 'Point de départ.'))

C.a(1, 'Définition et épidémiologie', P(
 'Le cancer du côlon est une tumeur maligne née de la muqueuse colique ; en effet, il croît à la fois vers la lumière et dans la paroi, puis peut s’étendre aux organes voisins (ESMO 2020). Le plus souvent, il s’agit d’un adénocarcinome. Par ailleurs, l’OFS le regroupe avec la jonction rectosigmoïdienne et le rectum sous le terme de cancer colorectal.',
 'En Suisse, ce cancer colorectal est fréquent. Ainsi, de 2018 à 2022, on a compté en moyenne 2 528 nouveaux cas par an chez l’homme et 2 035 chez la femme, soit 41,4 et 28,9 pour 100 000 ; de plus, il a causé 894 et 712 décès par an (OFS/ONEC). À l’échelle mondiale, il cause plus de 600 000 décès par an et constitue la quatrième cause de décès par cancer (ESMO 2020).')
 + key('Suisse 2018-2022 : ≈ 4 560 nouveaux cas et ≈ 1 600 décès par an de cancer colorectal ; le côlon en représente la majeure partie avec le sigmoïde et le rectum.')
 + src(OFS, ESMO))

C.a(2, 'Facteurs de risque et formes héréditaires', P(
 'Après la fréquence, il faut repérer les personnes à risque. Ainsi, l’ESMO relie la hausse de l’incidence à l’« occidentalisation » du mode de vie : obésité, sédentarité, alcool, consommation élevée de viande rouge et tabac ; en outre, un déséquilibre du microbiote intestinal pourrait jouer un rôle.',
 'Par ailleurs, le risque augmente avec les antécédents personnels ou familiaux de cancer colorectal ou d’adénome. Enfin, 2 à 5 % des cancers colorectaux relèvent d’un syndrome héréditaire : la ' + w('c18-paf', 'polypose adénomateuse familiale') + ' et ses variantes (1 %), le ' + w('c18-lynch', 'syndrome de Lynch') + ' (2 à 4 %), ainsi que les syndromes de Turcot, de Peutz-Jeghers et la polypose associée à MUTYH (ESMO 2020). C’est pourquoi l’histoire familiale fait partie de tout bilan.')
 + key('Mode de vie occidental (obésité, sédentarité, alcool, viande rouge, tabac) ; antécédents personnels ou familiaux ; 2-5 % héréditaires, dont Lynch 2-4 % et PAF 1 %.')
 + src(ESMO))

C.a(3, 'Dépistage', P(
 'Puisque le cancer naît le plus souvent d’une lésion précancéreuse, le dépistage permet de l’empêcher ou de le trouver tôt. Ainsi, l’ESMO recommande la coloscopie totale chez l’homme et la femme à risque moyen, entre 50 et 74 ans, avec un intervalle de 10 ans après un examen négatif ; de plus, le ' + w('c18-fit', 'test immunochimique fécal') + ' paraît supérieur au test au gaïac pour détecter adénomes et cancers. En revanche, la capsule colique n’est pas recommandée pour le dépistage.',
 'En Suisse, l’assurance obligatoire prend en charge ce dépistage de 50 à 74 ans, selon l’' + w('c18-opas', 'article 12e de l’OPAS') + ' : soit une recherche de sang occulte dans les selles tous les deux ans, suivie d’une coloscopie si elle est positive, soit une coloscopie tous les dix ans. Par ailleurs, dans les programmes cantonaux énumérés par l’ordonnance, aucune franchise n’est prélevée. Enfin, un test positif impose une coloscopie au plus vite (ESMO 2020).')
 + trap('Un test de sang occulte positif n’est jamais « contrôlé » par un second test : il impose une coloscopie, au plus vite.', 'Piège')
 + key('Risque moyen 50-74 ans : sang occulte (FIT) tous les 2 ans ou coloscopie tous les 10 ans (OPAS, assurance de base) ; test positif → coloscopie.')
 + src(OPAS, ESMO))

C.a(4, 'Présentation clinique', P(
 'Lorsque le cancer donne des symptômes, la tumeur est en général volumineuse ou avancée ; de plus, ces symptômes ne sont pas spécifiques. Ainsi, les plus fréquents sont une modification du transit, des douleurs abdominales générales ou localisées, une perte de poids sans autre cause, une faiblesse, une carence martiale et une anémie ; en outre, ils dépendent de la localisation et du stade (ESMO 2020).',
 'Par ailleurs, certains cancers se révèlent par une complication : occlusion, perforation, fistule, abcès ou hémorragie massive, qui peuvent imposer une résection urgente. Enfin, le cancer peut être multiple : des lésions synchrones sont présentes dans 3,6 % des cas, et des cancers métachrones apparaissent chez jusqu’à 3 % des patients dans les 5 ans suivant la chirurgie (ESMO 2020). C’est pourquoi le côlon entier doit être exploré, avant puis après l’opération.')
 + quiz('Un homme de 70 ans a une anémie ferriprive isolée, sans symptôme digestif. Quelle attitude ?',
   [('Supplémenter en fer et contrôler dans trois mois', False), ('Explorer le tube digestif, dont le côlon par coloscopie', True), ('Doser l’ACE pour exclure un cancer', False)],
   'La carence martiale et l’anémie font partie des signes d’appel les plus fréquents ; or, l’ACE n’a pas de valeur diagnostique en l’absence de biopsie (ESMO 2020).')
 + key('Transit modifié, douleurs, amaigrissement, faiblesse, carence martiale, anémie ; complications : occlusion, perforation, hémorragie ; synchrones 3,6 %.')
 + src(ESMO))

C.a(5, 'Diagnostic et bilan d’extension', P(
 'Devant ce tableau, l’examen de référence est la coloscopie totale, qui confirme le diagnostic par biopsie et cherche des lésions synchrones [I, A] ; en effet, elle permet aussi de repérer et de marquer la tumeur et d’enlever d’autres lésions précancéreuses. Si elle n’est pas réalisable, une coloscopie gauche limitée combinée à une coloscopie virtuelle par scanner est une alternative [I, A] ; dans ce cas, une coloscopie complète doit être faite dans les 3 à 6 mois suivant l’opération [IV, B].',
 'Ensuite, le bilan d’extension recherche des métastases, présentes d’emblée chez environ 20 % des patients : surtout le foie (17 %), puis le péritoine (5 %), le poumon (5 %) et les ganglions (3 %). Ainsi, le scanner thoracique, abdominal et pelvien avec injection est la méthode préférée [II, B] ; cependant, il détecte mal les métastases péritonéales. Par ailleurs, l’IRM précise les rapports d’une tumeur localement avancée, et l’ACE est dosé avant la chirurgie [III, A] : en effet, un taux postopératoire supérieur à 5 ng/ml annonce un pronostic plus défavorable (ESMO 2020).')
 + C.img('c18_endo.gif', 'Image d’endoscopie colique : masse bourgeonnante, irrégulière et friable, qui rétrécit la lumière du côlon sigmoïde.', 'Adénocarcinome du côlon sigmoïde en coloscopie : masse bourgeonnante et irrégulière qui sténose la lumière ; la biopsie confirme le diagnostic.', credit({'auteur': 'Endospopy1 (Wikimedia Commons)', 'licence': 'GFDL / CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Colorectal_cancer_endo_2.jpg'}))
 + key('Coloscopie totale + biopsies ; sinon coloscopie complète dans les 3-6 mois postopératoires ; scanner TAP injecté ; ACE préopératoire ; métastases synchrones ≈ 20 % (foie 17 %).')
 + src(ESMO))

C.a(6, 'Classification TNM et stades', P(
 'Le pronostic et le traitement dépendent donc du stade, établi selon la classification ' + w('c18-tnm', 'TNM') + ' de l’UICC, 8e édition, que l’ESMO impose au compte rendu pathologique. Ainsi, la catégorie T décrit la profondeur d’invasion de la paroi, la catégorie N le nombre de ganglions régionaux envahis, et la catégorie M les métastases à distance.',
 'De plus, ces catégories se regroupent en stades. En effet, le stade I correspond à T1 ou T2 sans ganglion ; le stade II à T3 ou T4 sans ganglion (IIA T3, IIB T4a, IIC T4b) ; le stade III à toute atteinte ganglionnaire, ou à des ' + w('c18-depots', 'dépôts tumoraux') + ' (N1c), sans métastase ; enfin, le stade IV à toute métastase (IVA M1a, IVB M1b, IVC M1c).')
 + table(['Catégorie', 'Définition (UICC, 8e édition)'], [
   ['Tis', 'Carcinome intramuqueux : invasion du chorion, sans franchissement de la musculaire muqueuse'],
   ['T1 / T2', 'Invasion de la sous-muqueuse / de la musculeuse'],
   ['T3', 'Invasion de la sous-séreuse ou des tissus péricoliques non péritonisés'],
   ['T4a / T4b', 'Perforation du péritoine viscéral / envahissement direct d’autres organes ou structures'],
   ['N1 (a, b, c)', '1 à 3 ganglions régionaux (1 ; 2-3) ; N1c : dépôts tumoraux sans ganglion envahi'],
   ['N2 (a, b)', '4 ganglions ou plus (4-6 ; 7 ou plus)'],
   ['M1a / M1b / M1c', 'Un seul organe sans péritoine / plus d’un organe / péritoine, avec ou sans organe']])
 + P('Le tableau se lit de haut en bas, de la paroi vers la distance : ainsi, chaque ligne franchie aggrave le pronostic et change la décision thérapeutique.')
 + key('Stade I : T1-2 N0 ; II : T3-4 N0 ; III : N+ (ou N1c) M0 ; IV : M1 (M1c = péritoine).')
 + src(TNM, ESMO))

C.a(7, 'Anatomopathologie et statut MMR/MSI', P(
 'Après l’exérèse, le compte rendu pathologique fixe le stade ; c’est pourquoi l’ESMO exige au moins 12 ganglions examinés lorsque c’est possible [IV, B], afin de distinguer avec certitude un stade II d’un stade III. De plus, le compte rendu précise le type histologique, le grade, l’invasion lymphatique et veineuse, les marges et le statut MMR/MSI.',
 'En effet, le statut MMR/MSI a deux objectifs : préciser le pronostic et le bénéfice d’une chimiothérapie, et dépister une prédisposition génétique. Ainsi, en ' + w('c18-ihc', 'immunohistochimie') + ', la perte de MSH2 ou de MSH6 fait suspecter un syndrome de Lynch ; en revanche, une perte de MLH1 et PMS2 impose de chercher une mutation de BRAF ou une hyperméthylation du promoteur de MLH1, qui orientent vers une altération somatique plutôt que vers un Lynch (ESMO 2020). Par ailleurs, le statut MMR/MSI doit être déterminé dans tout stade II ; au stade III, il sert surtout à identifier le syndrome de Lynch [IV, A].')
 + C.img('c18_piece.gif', 'Pièce de colectomie ouverte : tumeur ulcérée et bourgeonnante de la muqueuse colique, accompagnée de deux petits polypes.', 'Pièce de colectomie ouverte : adénocarcinome invasif ulcéré et bourgeonnant, avec deux polypes adénomateux voisins ; le pathologiste y mesure l’invasion et compte les ganglions.', credit({'auteur': 'Emmanuelm (Wikipédia en anglais)', 'licence': 'CC BY 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Colon_cancer.jpg'}))
 + key('≥ 12 ganglions ; MMR/MSI : perte MSH2/MSH6 → suspicion de Lynch ; perte MLH1/PMS2 → BRAF ou méthylation de MLH1 ; MMR obligatoire au stade II.')
 + src(ESMO))

C.a(8, 'Chirurgie et formes compliquées', P(
 'Le cancer infiltrant ne peut pas être enlevé par coloscopie ; il relève donc de la chirurgie, qui résèque largement le segment colique atteint et son drainage lymphatique [I, A]. De plus, une exérèse en bloc des organes envahis est nécessaire en cas de pT4b [I, B], et la cavité péritonéale ainsi que les ovaires sont explorés pendant l’intervention [I, C].',
 'Cependant, deux situations s’écartent de ce schéma. D’une part, un cancer sur polype : l’exérèse endoscopique en bloc suffit pour un adénocarcinome non invasif (pTis) [IV, B] ; en revanche, un carcinome invasif pT1 avec invasion lymphatique ou veineuse, grade 3, ou ' + w('c18-budding', 'bourgeonnement tumoral') + ' significatif impose une résection chirurgicale avec curage [IV, B]. D’autre part, l’occlusion : en centre expert, une ' + w('c18-stent', 'prothèse colique') + ' peut servir de pont vers une chirurgie programmée, notamment après 70 ans ou en cas de classe ASA supérieure à II [II].')
 + trap('Un polype réséqué contenant un carcinome pT1 n’est pas « guéri » d’office : la relecture conjointe par le pathologiste et le chirurgien décide de la colectomie complémentaire selon les critères de risque.', 'Piège')
 + key('Résection large + curage ; en bloc si pT4b ; exploration péritonéale ; pTis sur polype : exérèse en bloc ; pT1 à risque : colectomie ; occlusion : prothèse en pont si centre expert.')
 + src(ESMO))

C.a(9, 'Traitement adjuvant', P(
 'Une fois le stade connu, la chimiothérapie adjuvante vise à éradiquer la maladie microscopique ; ainsi, au stade III, le standard associe une ' + w('c18-fp', 'fluoropyrimidine') + ' et l’' + w('c18-d-oxali', 'oxaliplatine') + ' [I, A]. De plus, la durée dépend du schéma, selon l’' + w('c18-idea', 'analyse IDEA') + ' : ' + w('c18-capox', 'CAPOX') + ' pendant 3 ou 6 mois, ou ' + w('c18-folfox', 'FOLFOX') + ' pendant 6 mois [I, A]. En effet, 3 mois de CAPOX n’étaient pas inférieurs à 6 mois, alors que 3 mois de FOLFOX l’étaient ; en outre, la neuropathie de grade 2 ou plus passait de 34 % à 11 %. Par ailleurs, l’ESMO propose, avec prudence, 3 mois de CAPOX pour T1-3 N1 et 6 mois pour T4 ou N2.',
 'En revanche, le patient qui ne peut pas recevoir d’oxaliplatine reçoit la ' + w('c18-d-cape', 'capécitabine') + ' ou le ' + w('c18-lv5fu2', 'LV5FU2') + ' pendant 6 mois [I, A]. Au stade II, la décision suit le risque : surveillance seule si le risque est faible [I, A] ; fluoropyrimidine pendant 6 mois si le risque est intermédiaire [I, B] ; ajout possible d’oxaliplatine si le risque est élevé, c’est-à-dire pT4, moins de 12 ganglions ou plusieurs facteurs intermédiaires [I, C]. Enfin, la chimiothérapie commence au plus tôt, idéalement avant 8 semaines [II, B], car un délai plus long est associé à un risque relatif de décès de 1,20.')
 + trap('L’information professionnelle suisse de Xeloda® prévoit l’association avec l’oxaliplatine en adjuvant « pendant 6 mois » ; or, l’ESMO 2020 admet 3 mois de CAPOX. La durée de 3 mois est donc fondée sur la recommandation, plus récente que le libellé de la FI. À valider à l’audit.', w('c18-contentieux', 'Contentieux de sources'))
 + key('Stade III : CAPOX 3 mois (T1-3 N1) ou 6 mois (T4/N2), FOLFOX 6 mois ; sans oxaliplatine : capécitabine ou LV5FU2 6 mois ; stade II selon risque et MMR ; débuter avant 8 semaines.')
 + src(ESMO, FI('Xeloda®')))

C.a(10, 'Surveillance après résection', P(
 'Après le traitement, la surveillance cherche une récidive curable et un nouveau cancer ; en effet, une surveillance intensive permet de détecter plus tôt la rechute chez les patients à risque [II, B]. Ainsi, l’examen clinique et le dosage de l’ACE sont recommandés tous les 3 à 6 mois pendant 3 ans, puis tous les 6 à 12 mois pendant les années 4 et 5 [II, B].',
 'De plus, une coloscopie est faite à un an, puis tous les 3 à 5 ans, à la recherche d’adénomes et de cancers métachrones [III, B]. Par ailleurs, un scanner thoracique et abdominal tous les 6 à 12 mois pendant 3 ans peut être envisagé chez les patients à risque élevé de récidive [II, B]. En revanche, les autres examens biologiques et radiologiques n’ont pas fait la preuve de leur intérêt (ESMO 2020).')
 + key('Clinique + ACE tous les 3-6 mois 3 ans, puis 6-12 mois ans 4-5 ; coloscopie à 1 an puis tous les 3-5 ans ; scanner 6-12 mois 3 ans si risque élevé.')
 + C.pareto('pareto-c18-clinique', 'Cancer du côlon', ['c18-3', 'c18-5', 'c18-6', 'c18-7', 'c18-9', 'c18-10'],
     ['Dépistage 50-74 ans : FIT tous les 2 ans ou coloscopie tous les 10 ans.',
      'Coloscopie totale + scanner TAP + ACE.',
      'Stade III = ganglion envahi.',
      '≥ 12 ganglions ; MMR/MSI en stade II et pour le Lynch.',
      'CAPOX 3-6 mois ou FOLFOX 6 mois, avant 8 semaines.',
      'Coloscopie à 1 an ; ACE tous les 3-6 mois.'])
 + src(ESMO))

C.a(11, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons le patient du début. La coloscopie totale montre une tumeur sténosante du côlon sigmoïde, et la biopsie confirme un adénocarcinome ; de plus, le scanner thoraco-abdomino-pelvien ne montre pas de métastase. Ensuite, la colectomie sigmoïdienne avec curage ramène 3 ganglions envahis sur 18, sur une tumeur pT3 : il s’agit donc d’un stade III, pT3 N1b M0.',
 'Dès lors, la conduite associe trois mesures. D’abord, le statut DPD est testé avant toute fluoropyrimidine. Ensuite, comme la tumeur est T1-3 N1, un CAPOX de 3 mois est proposé et commencé avant 8 semaines. Enfin, la surveillance associe l’examen clinique et l’ACE tous les 3 à 6 mois et une coloscopie à un an.')
 + key('Coloscopie + biopsie → scanner → colectomie + ≥ 12 ganglions → pT3 N1b → DPD → CAPOX 3 mois → surveillance.')
 + src(ESMO))

C.a(12, 'Critères formels et paramètres clés', alert(
 '<p><b>Stades (UICC 8).</b> I : T1-2 N0 M0 ; II : T3-4 N0 M0 ; III : tout T, N1-2 (dont N1c) M0 ; IV : M1 (a un organe, b plusieurs, c péritoine). <b>Stade II à haut risque (ESMO).</b> pT4, moins de 12 ganglions, ou plusieurs facteurs intermédiaires. <b>pT1 sur polype à risque.</b> Invasion lymphatique ou veineuse, grade 3, bourgeonnement significatif.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Suisse 2018-2022 : 2 528 + 2 035 nouveaux cas/an ; dépistage 50-74 ans (OPAS) ; métastases synchrones ≈ 20 % ; ≥ 12 ganglions ; CAPOX 3 ou 6 mois, FOLFOX 6 mois ; début avant 8 semaines ; ACE > 5 ng/ml postopératoire : pronostic défavorable.</div>'
 + src(ESMO, TNM, OPAS, OFS))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Niveau (ESMO 2020)'], [
   ['Le cancer existe-t-il ?', w('c18-colo', 'Coloscopie totale avec biopsies'), '[I, A]'],
   ['Coloscopie impossible ?', 'Coloscopie gauche + coloscopie virtuelle par scanner', '[I, A]'],
   ['Métastases ?', w('c18-tdm', 'Scanner thoraco-abdomino-pelvien injecté'), '[II, B]'],
   ['Rapports locaux d’une tumeur avancée ?', 'IRM injectée', 'Cas ambigus ou pT4b'],
   ['Pronostic et suivi ?', w('c18-ace', 'ACE préopératoire'), '[III, A]'],
   ['Toxicité des fluoropyrimidines ?', w('c18-dpd', 'Génotypage DPYD ou phénotypage DPD'), '[III, A]']])
 + P('Le tableau se lit de haut en bas : ainsi, seule la biopsie établit le diagnostic, tandis que les autres examens fixent l’extension et préparent le traitement.')
 + key('Coloscopie + biopsie ; scanner TAP ; IRM si doute local ; ACE ; DPD avant fluoropyrimidine.')
 + src(ESMO))

C.e(2, 'Lire le compte rendu histologique', P(
 'Le compte rendu doit fournir le pT, le nombre de ganglions examinés et envahis, l’envahissement d’autres organes, et le statut MMR/MSI (ESMO 2020) ; ainsi, il permet de classer la tumeur selon l’UICC. Or, si moins de 12 ganglions sont examinés, la tumeur est considérée à haut risque au stade II. Par ailleurs, l’histologie montre des glandes tumorales irrégulières qui envahissent la paroi.')
 + C.img('c18_histo.gif', 'Coupe histologique à faible grossissement : glandes tumorales irrégulières, serrées, qui infiltrent la paroi colique.', 'Adénocarcinome colique, faible grossissement : glandes tumorales irrégulières et serrées qui infiltrent la paroi ; la profondeur d’invasion définit le pT.', credit({'auteur': 'Netha Hussain', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Adenocarcinoma_of_the_colon-histology.JPG'}))
 + key('Compte rendu : pT, ganglions (≥ 12), marges, invasion vasculaire, grade, MMR/MSI.')
 + C.pareto('pareto-c18-examens', 'Examens', ['c18-e-1', 'c18-e-2'],
     ['Coloscopie totale + biopsies.',
      'Scanner TAP injecté.',
      'ACE avant chirurgie.',
      '≥ 12 ganglions et MMR/MSI.',
      'DPD avant fluoropyrimidine.'])
 + src(ESMO))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : segments et péritoine du côlon', P(
 'Le côlon comprend le cæcum, le côlon ascendant, le transverse, le descendant et le sigmoïde ; or, une partie de sa surface est recouverte de péritoine viscéral, et une autre ne l’est pas. Ainsi, la classification distingue la perforation du péritoine viscéral (T4a) de l’invasion des tissus péricoliques non péritonisés (T3). Par conséquent, la localisation exacte de la tumeur, marquée lors de la coloscopie, guide le chirurgien et le pathologiste.')
 + key('C’est pourquoi le marquage endoscopique et la description du péritoine comptent pour le stade.', 'Science → stade.'))
C.s('histo', 'Histologie', 'Histologie : les couches de la paroi et la catégorie T', P(
 'La paroi colique comprend, de dedans en dehors, la muqueuse avec son chorion et sa musculaire muqueuse, la sous-muqueuse, la musculeuse, puis la sous-séreuse et la séreuse ; ainsi, la catégorie T suit exactement cette succession. En effet, Tis reste dans le chorion, T1 atteint la sous-muqueuse, T2 la musculeuse et T3 la sous-séreuse. De plus, le franchissement de la musculaire muqueuse donne accès aux lymphatiques, d’où le risque ganglionnaire du pT1.')
 + key('Chaque couche franchie correspond à une catégorie T : la lecture de la paroi est la lecture du stade.', 'Science → TNM.'))
C.s('biomol', 'Biologie moléculaire', 'Biologie moléculaire : la réparation des mésappariements', P(
 'Les protéines MLH1, MSH2, MSH6 et PMS2 réparent les erreurs de réplication de l’ADN ; ainsi, leur perte produit une instabilité des microsatellites. Or, cette perte est soit constitutionnelle, dans le syndrome de Lynch, soit acquise, par exemple par hyperméthylation du promoteur de MLH1. C’est pourquoi l’ESMO recommande, devant une perte de MLH1, de chercher une mutation de BRAF ou cette hyperméthylation, qui orientent vers une cause somatique.')
 + key('Perte MMR → MSI ; Lynch si constitutionnelle ; BRAF ou méthylation de MLH1 → cause somatique probable.', 'Science → génétique.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : la DPD et les fluoropyrimidines', P(
 'La dihydropyrimidine déshydrogénase est l’enzyme limitante du catabolisme du 5-fluorouracile ; ainsi, un déficit expose à une toxicité grave, voire mortelle, avec stomatite, diarrhée, neutropénie et neurotoxicité, en général dès le premier cycle (FI Xeloda®). De plus, la capécitabine est une prodrogue orale transformée en 5-fluorouracile. Par conséquent, l’ESMO recommande un test DPD avant toute fluoropyrimidine, avec une réduction de dose de 50 % en cas de variant hétérozygote ; en revanche, un déficit complet contre-indique Xeloda®.')
 + key('DPD : test avant 5-FU ou capécitabine ; hétérozygote → dose réduite de 50 % ; déficit complet → contre-indication.', 'Science → sécurité.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, le traitement adjuvant repose sur deux familles, associées ou non.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Fluoropyrimidine orale', 'Capécitabine (Xeloda®)', 'CAPOX ; monothérapie si pas d’oxaliplatine', w('c18-d-cape', 'Monographie')],
   ['Fluoropyrimidine intraveineuse', '5-fluorouracile + acide folinique', 'FOLFOX, LV5FU2', w('c18-fp', 'Fiche')],
   ['Sel de platine', 'Oxaliplatine (Eloxatine®)', 'CAPOX, FOLFOX ; stade III', w('c18-d-oxali', 'Monographie')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, l’oxaliplatine s’ajoute à une fluoropyrimidine, jamais l’inverse.')
 + key('Fluoropyrimidine (capécitabine ou 5-FU) ± oxaliplatine ; oxaliplatine au stade III et dans le stade II à haut risque.')
 + src(ESMO))

C.p(2, 'Doses et statut réglementaire', P('Les doses suivantes proviennent des informations professionnelles suisses ; de plus, les écarts avec l’ESMO sont signalés.')
 + table(['Médicament', 'Situation', 'Dose', 'Source'], [
   ['Capécitabine (Xeloda®)', 'Adjuvant, monothérapie (6 mois)', '1 250 mg/m² 2 ×/j, J1-J14, toutes les 3 semaines', 'FI Xeloda®'],
   ['Capécitabine + oxaliplatine (CAPOX)', 'Adjuvant', 'Oxaliplatine 130 mg/m² en 2 h à J1, puis capécitabine 1 000 mg/m² 2 ×/j J1-J14, toutes les 3 semaines', 'FI Xeloda® (6 mois) ; ESMO : 3 ou 6 mois'],
   ['Oxaliplatine (Eloxatine®) + 5-FU/acide folinique (FOLFOX)', 'Adjuvant, stade III', '85 mg/m² toutes les 2 semaines, 12 cycles (6 mois), avant le 5-FU', 'FI Eloxatine®'],
   ['Fluoropyrimidine', 'Variant DPYD hétérozygote', 'Dose réduite de 50 %', 'ESMO 2020']])
 + P('Par exemple, chez le patient du début, CAPOX comporte 4 cycles de 3 semaines, soit 3 mois ; ensuite, la dose de capécitabine est adaptée à la tolérance et à la fonction rénale.')
 + trap('Les doses du 5-fluorouracile et de l’acide folinique du schéma FOLFOX n’ont pas été lues dans une FI pour ce cours. TODO : compléter à partir de l’information professionnelle du 5-fluorouracile.', 'Lacune documentaire')
 + key('Xeloda® 1 250 mg/m² 2 ×/j (seule) ou 1 000 mg/m² 2 ×/j (avec oxaliplatine 130 mg/m²), J1-J14/21 ; Eloxatine® 85 mg/m²/2 semaines, 12 cycles.')
 + src(FI('Xeloda®'), FI('Eloxatine®'), ESMO))

C.p(3, 'Surveillance et effets indésirables', alert(
 'Xeloda® est contre-indiqué en cas de déficit complet connu en DPD, de grossesse et d’allaitement, d’insuffisance rénale sévère (clairance de la créatinine < 30 ml/min), d’insuffisance hépatique Child-Pugh C et de traitement par la brivudine. De plus, il est interrompu si la bilirubine dépasse 3 fois la normale ou les transaminases 2,5 fois la normale (FI Xeloda®).', 'Sécurité.')
 + P('Par ailleurs, l’oxaliplatine est contre-indiqué en cas de neutrophiles < 2 000/mm³ ou de plaquettes < 50 000/mm³, de neuropathie sensitive préexistante avec gêne fonctionnelle, de clairance de la créatinine < 30 ml/min, de grossesse et d’allaitement (FI Eloxatine®). En effet, sa toxicité principale est la ' + w('c18-neuro', 'neuropathie sensitive') + ', dont la fréquence dépend de la durée ; c’est pourquoi la durée courte de CAPOX la réduit nettement.')
 + key('Xeloda® : DPD, rein, foie, brivudine, bilirubine > 3 N ; oxaliplatine : neuropathie, myélosuppression, rein ; durée courte = moins de neuropathie.')
 + C.pareto('pareto-c18-pharma', 'Pharmacologie', ['c18-p-1', 'c18-p-2', 'c18-p-3'],
     ['DPD avant fluoropyrimidine.',
      'CAPOX : oxaliplatine 130 mg/m² + capécitabine 1 000 mg/m² 2 ×/j J1-J14.',
      'FOLFOX : oxaliplatine 85 mg/m² toutes les 2 semaines.',
      'Neuropathie : raison de la durée courte.'])
 + src(FI('Xeloda®'), FI('Eloxatine®'), ESMO))

# ---------------- Fenêtres
L = lab
C.pop('c18-ccr', 'Cancer du côlon', L(('Définition', 'Tumeur maligne de la muqueuse colique, le plus souvent un adénocarcinome, qui croît vers la lumière et dans la paroi.'), ('Regroupement OFS', 'Cancer colorectal : côlon, jonction rectosigmoïdienne et rectum.')) + src(ESMO, OFS))
C.pop('c18-colo', 'Coloscopie totale', L(('Rôle', 'Confirmation par biopsie, recherche de lésions synchrones, marquage et exérèse de lésions précancéreuses [I, A].'), ('Si incomplète', 'Coloscopie gauche + coloscopie virtuelle ; coloscopie complète dans les 3-6 mois postopératoires.')) + src(ESMO))
C.pop('c18-tdm', 'Scanner thoraco-abdomino-pelvien', L(('Place', 'Méthode préférée pour les métastases à distance [II, B].'), ('Limite', 'Sensibilité faible pour les métastases péritonéales.')) + src(ESMO))
C.pop('c18-ace', 'Antigène carcinoembryonnaire (ACE)', L(('Usage', 'Dosage préopératoire et au cours du suivi [III, A] ; pas de valeur diagnostique sans biopsie.'), ('Pronostic', 'Taux postopératoire > 5 ng/ml : évolution plus défavorable.')) + src(ESMO))
C.pop('c18-tnm', 'Classification TNM (UICC, 8e édition)', L(('T', 'Tis chorion ; T1 sous-muqueuse ; T2 musculeuse ; T3 sous-séreuse ; T4a péritoine viscéral ; T4b autres organes.'), ('N', 'N1a 1 ; N1b 2-3 ; N1c dépôts ; N2a 4-6 ; N2b ≥ 7 ganglions.'), ('M', 'M1a un organe ; M1b plusieurs ; M1c péritoine.')) + src(TNM))
C.pop('c18-depots', 'Dépôts tumoraux (N1c)', L(('Définition', 'Nodules tumoraux de la sous-séreuse ou des tissus péricoliques non péritonisés, sans ganglion régional envahi.'), ('Conséquence', 'Classent la tumeur en stade III.')) + src(TNM))
C.pop('c18-mmr', 'Statut MMR/MSI', L(('Définition', 'Déficit de réparation des mésappariements (dMMR), mesuré par immunohistochimie, ou instabilité microsatellitaire (MSI), mesurée par PCR.'), ('Usage', 'Obligatoire au stade II pour la décision adjuvante ; dépistage du Lynch [IV, A].')) + src(ESMO))
C.pop('c18-ihc', 'Immunohistochimie MMR', L(('Perte MSH2 et/ou MSH6', 'Suspicion de syndrome de Lynch.'), ('Perte MLH1 et PMS2', 'Chercher une mutation BRAF ou une hyperméthylation du promoteur de MLH1 : si présente, altération somatique probable.')) + src(ESMO))
C.pop('c18-lynch', 'Syndrome de Lynch', L(('Définition', 'Prédisposition héréditaire liée à un gène de réparation des mésappariements ; anciennement « cancer colorectal héréditaire sans polypose ».'), ('Fréquence', '2-4 % des cancers colorectaux.')) + src(ESMO))
C.pop('c18-paf', 'Polypose adénomateuse familiale', L(('Fréquence', 'Environ 1 % des cancers colorectaux, avec ses variantes.'), ('Dépistage', 'Relève des recommandations ESMO des cancers digestifs héréditaires.')) + src(ESMO))
C.pop('c18-fit', 'Test immunochimique fécal (FIT)', L(('Principe', 'Détection immunologique de l’hémoglobine humaine dans les selles.'), ('Performance', 'Supérieur au test au gaïac pour le taux de détection et la valeur prédictive positive.'), ('Suisse', 'Tous les 2 ans de 50 à 74 ans ; coloscopie si positif (OPAS).')) + src(ESMO, OPAS))
C.pop('c18-opas', 'OPAS, article 12e, lettre d', L(('Tranche d’âge', '50 à 74 ans (version en vigueur depuis le 1er juillet 2026).'), ('Méthodes', 'Sang occulte tous les 2 ans, coloscopie si positif ; ou coloscopie tous les 10 ans.'), ('Franchise', 'Aucune dans les programmes cantonaux énumérés.')) + src(OPAS))
C.pop('c18-budding', 'Bourgeonnement tumoral', L(('Définition', 'Cellules isolées ou petits amas tumoraux au front d’invasion.'), ('Portée', 'Grade supérieur à 1 dans un pT1 sur polype : critère de résection chirurgicale [IV, B].')) + src(ESMO))
C.pop('c18-stent', 'Prothèse colique', L(('Place', 'Pont vers une chirurgie programmée en cas d’occlusion, en centre expert, surtout après 70 ans ou si ASA > II [II].')) + src(ESMO))
C.pop('c18-fp', 'Fluoropyrimidines', L(('Molécules', '5-fluorouracile (intraveineux, avec acide folinique) et capécitabine (orale, prodrogue).'), ('Précaution', 'Test DPD avant le début [III, A].')) + src(ESMO, FI('Xeloda®')))
C.pop('c18-idea', 'Analyse IDEA', L(('Effectif', '12 834 patients de stade III, six essais, 3 contre 6 mois.'), ('Résultat', 'CAPOX 3 mois non inférieur (HR 0,95) ; FOLFOX 3 mois inférieur (HR 1,16) ; neuropathie ≥ grade 2 : 11 % contre 34 %.')) + src(ESMO))
C.pop('c18-capox', 'CAPOX', L(('Composition', 'Capécitabine + oxaliplatine, cycles de 3 semaines.'), ('Durée (ESMO)', '3 mois si T1-3 N1, 6 mois si T4 ou N2 (avec prudence).')) + src(ESMO, FI('Xeloda®')))
C.pop('c18-folfox', 'FOLFOX', L(('Composition', 'Acide folinique, 5-fluorouracile, oxaliplatine, cycles de 2 semaines.'), ('Durée', '6 mois (12 cycles) ; 3 mois inférieurs dans IDEA.')) + src(ESMO, FI('Eloxatine®')))
C.pop('c18-lv5fu2', 'LV5FU2 (schéma de de Gramont)', L(('Composition', 'Acide folinique et 5-fluorouracile en perfusion.'), ('Place', 'Adjuvant de 6 mois sans oxaliplatine [I, A].')) + src(ESMO))
C.pop('c18-dpd', 'Test DPD', L(('Méthodes', 'Génotypage DPYD (DPYD*2A, c.1679T>G, c.2846A>T, c.1236G>A) ou phénotypage.'), ('Conduite', 'Hétérozygote : dose réduite de 50 % ; homozygote : fluoropyrimidine évitée.')) + src(ESMO))
C.pop('c18-neuro', 'Neuropathie de l’oxaliplatine', L(('Nature', 'Neuropathie périphérique sensitive, cumulative.'), ('IDEA', 'Grade ≥ 2 : 34 % après 6 mois, 11 % après 3 mois.')) + src(ESMO, FI('Eloxatine®')))
C.pop('c18-contentieux', 'Contentieux : durée de CAPOX', L(('FI Xeloda®', 'Association avec l’oxaliplatine en adjuvant : 6 mois.'), ('ESMO 2020', 'CAPOX 3 ou 6 mois [I, A] ; 3 mois pour T1-3 N1.'), ('Choix du cours', 'La recommandation européenne la plus récente ; usage hors libellé de la FI à signaler.')) + src(ESMO, FI('Xeloda®')))
C.pop('c18-d-cape', 'Capécitabine (Xeloda®)', L(('Indication suisse', 'Adjuvant du cancer du côlon de stade C de Dukes, seule ou avec l’oxaliplatine.'), ('Doses', '1 250 mg/m² 2 ×/j J1-J14 seule ; 1 000 mg/m² 2 ×/j J1-J14 avec oxaliplatine ; dans les 30 minutes suivant un repas.'), ('Contre-indications', 'Déficit complet en DPD, ClCr < 30 ml/min, Child-Pugh C, brivudine, grossesse.')) + src(FI('Xeloda®')))
C.pop('c18-d-oxali', 'Oxaliplatine (Eloxatine®)', L(('Indication suisse', 'Adjuvant du stade III avec 5-FU et acide folinique.'), ('Dose', '85 mg/m² toutes les 2 semaines, 12 cycles ; perfusion de 2 h dans du glucose 5 %.'), ('Contre-indications', 'Neutrophiles < 2 000/mm³, plaquettes < 50 000/mm³, neuropathie fonctionnelle, ClCr < 30 ml/min.')) + src(FI('Eloxatine®')))

C.termes = [
 (r'cancer du côlon', 'c18-ccr'), (r'coloscopie totale', 'c18-colo'), (r'ACE', 'c18-ace'), (r'TNM', 'c18-tnm'), (r'dépôts tumoraux', 'c18-depots'),
 (r'MMR/MSI', 'c18-mmr'), (r'syndrome de Lynch', 'c18-lynch'), (r'Lynch', 'c18-lynch'), (r'polypose adénomateuse familiale', 'c18-paf'),
 (r'FIT', 'c18-fit'), (r'OPAS', 'c18-opas'), (r'bourgeonnement', 'c18-budding'), (r'prothèse', 'c18-stent'), (r'fluoropyrimidine', 'c18-fp'),
 (r'IDEA', 'c18-idea'), (r'CAPOX', 'c18-capox'), (r'FOLFOX', 'c18-folfox'), (r'LV5FU2', 'c18-lv5fu2'), (r'DPD', 'c18-dpd'),
 (r'neuropathie', 'c18-neuro'), (r'capécitabine', 'c18-d-cape'), (r'Xeloda', 'c18-d-cape'), (r'oxaliplatine', 'c18-d-oxali'), (r'immunohistochimie', 'c18-ihc'),
 (r'scanner', 'c18-tdm'),
]

C.write()
