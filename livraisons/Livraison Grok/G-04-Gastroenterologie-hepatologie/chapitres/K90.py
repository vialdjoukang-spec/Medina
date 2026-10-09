# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K90', 'Malabsorption intestinale : maladie cœliaque de l’adulte',
    'K90 — Malabsorption intestinale · CIM-10-GM 2024 · Côlon et intestin grêle',
    'Adulte · centré sur la maladie cœliaque (K90.0) : diagnostic sérologique et histologique, régime sans gluten, suivi, maladie cœliaque réfractaire ; autres malabsorptions (intolérance, stéatorrhée pancréatique, anse borgne, sprue tropicale) signalées · rédaction du 09.10.2026 · référentiels ESsCD 2025 (parties 1 et 2), information professionnelle suisse',
    'Pharmacologie et diététique')
w = C.w
E1 = ('Al-Toma A. et al., European Society for the Study of Coeliac Disease 2025 updated guidelines on the diagnosis and management of coeliac disease in adults. Part 1: diagnostic approach, United European Gastroenterol J 2025', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12704582/')
E2 = ('Al-Toma A. et al., ESsCD 2025 updated guidelines on the diagnosis and management of coeliac disease in adults. Part 2: management, follow-up, and complex disease courses, United European Gastroenterol J 2026', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC13097674/')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')
MARSH = credit({'auteur': 'Samir (Wikipédia en anglais)', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Coeliac_path.jpg'})
HIST = credit({'auteur': 'I. Dina, C. Iacobescu, C. Vrabie, S. Omer', 'licence': 'CC BY 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Histologic_examination_of_celiac_disease.png'})
ENDO = credit({'auteur': 'D. V. Balaban, A. Popp, F. Vasilescu, D. Haidautu, R. M. Purcarea, M. Jinga', 'licence': 'CC BY 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Scalloping_of_the_Kerckring_folds.jpg'})
DH = credit({'auteur': 'L. Weinstock, T. Myers, M. Steinhoff, J. Smith', 'licence': 'CC BY 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Dermatitis_herpetiformis.jpg'})

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 32 ans consulte pour une fatigue, des ballonnements après les repas et une ' + w('k90-fer', 'carence en fer') + ' qui récidive malgré les comprimés ; elle a une thyroïdite de Hashimoto. <b>La question est donc de savoir s’il faut chercher une ' + w('k90-mc', 'maladie cœliaque') + ', avec quel test, et à quelles conditions le résultat est interprétable.</b>',
 'Pour y répondre, le médecin doit savoir : reconnaître les situations où le test s’impose ; demander les ' + w('k90-tg2', 'IgA anti-transglutaminase') + ' avec les IgA totales, pendant que la patiente mange du gluten ; ensuite, confirmer par des biopsies duodénales ou, chez certains adultes, par la stratégie sans biopsie ; enfin, conduire le ' + w('k90-rsg', 'régime sans gluten') + ' à vie, le suivi, et reconnaître la maladie réfractaire.')
 + P('<i>Pourquoi ce cas ?</i> En effet, la maladie cœliaque de l’adulte se présente rarement par une diarrhée franche ; ainsi, elle se cache derrière une anémie, une fatigue ou une maladie auto-immune. Par conséquent, contrairement à un manuel figé qui liste des symptômes, ce cours relie chaque signe à son mécanisme, et chaque mot vert ouvre le seuil exact ou l’image histologique, si bien que la décision peut être refaite pas à pas.')
 + key('Carence en fer inexpliquée + ballonnements + auto-immunité : penser maladie cœliaque → IgA anti-TG2 + IgA totales sous gluten → confirmation → régime sans gluten à vie.', 'Point de départ.'))

C.a(1, 'Définitions et épidémiologie', P(
 'La ' + w('k90-malabs', 'malabsorption intestinale') + ' désigne un défaut d’absorption des nutriments par l’intestin ; or, ses causes sont multiples : atteinte de la muqueuse (maladie cœliaque), défaut de digestion (stéatorrhée pancréatique), intolérance (par exemple au lactose), prolifération bactérienne dans une anse borgne, ou sprue tropicale. Parmi elles, la maladie cœliaque est une entéropathie auto-immune déclenchée par le gluten chez des sujets génétiquement prédisposés, porteurs de ' + w('k90-hla', 'HLA-DQ2 ou HLA-DQ8') + ' (ESsCD 2025).',
 'Par ailleurs, elle est fréquente. En effet, dans les pays occidentaux, sa prévalence est d’environ 0,7 % lorsqu’elle est confirmée par l’histologie, et de 1 à 1,6 % dans les dépistages sérologiques de la population générale ; de plus, depuis 2000, elle est la plus élevée en Europe du Nord (1,60 %) et la plus basse en Europe de l’Ouest (0,60 %). Cependant, une grande partie des cas reste non diagnostiquée ; ainsi, historiquement, plus de 70 % des diagnostics étaient posés après 20 ans (ESsCD 2025).')
 + key('Malabsorption : muqueuse, digestion, intolérance, anse borgne, sprue tropicale ; maladie cœliaque = entéropathie auto-immune au gluten sur terrain HLA-DQ2/DQ8 ; ≈ 0,7 % (histologie), 1-1,6 % (sérologie) ; souvent méconnue.')
 + src(E1))

C.a(2, 'Physiopathologie : du gluten à l’atrophie villositaire', P(
 'Le gluten contient des peptides de gliadine que la digestion ne dégrade pas complètement ; ainsi, ils traversent l’épithélium et sont modifiés par la transglutaminase tissulaire de type 2 (TG2). Ensuite, ces fragments sont présentés, de façon dépendante de HLA-DQ2 ou HLA-DQ8, à des lymphocytes T spécifiques de la gliadine ; par conséquent, une réaction inflammatoire se déclenche dans le grêle et aboutit à l’' + w('k90-atrophie', 'atrophie villositaire') + ' et à la malabsorption (ESsCD 2025).',
 'De plus, cette réaction produit des anticorps contre la TG2 elle-même : c’est pourquoi les IgA anti-TG2 sont le marqueur diagnostique. Or, ils dépendent de l’exposition au gluten ; en effet, ils se normalisent habituellement sous régime sans gluten, ce qui explique qu’un test fait après l’arrêt du gluten puisse être faussement négatif. Enfin, l’atrophie réduit la surface d’absorption, surtout dans le duodénum et le jéjunum proximal ; ainsi, le fer, absorbé dans le duodénum, manque tôt, d’où l’anémie ferriprive comme mode de révélation fréquent.')
 + C.img('k90_marsh.gif', 'Coupe histologique de biopsie du grêle : villosités émoussées, cryptes allongées et infiltrat lymphocytaire.', 'Maladie cœliaque, biopsie du grêle : villosités émoussées, hyperplasie des cryptes et infiltration lymphocytaire, compatibles avec un stade Marsh III.', MARSH)
 + P('<i>Lecture de l’image.</i> Normalement, les villosités sont hautes et fines, et les cryptes courtes ; ici, à l’inverse, la surface est presque plane et les cryptes sont allongées. En effet, l’inflammation détruit les entérocytes au sommet des villosités, et les cryptes prolifèrent pour compenser ; ainsi, la muqueuse perd sa surface d’absorption, ce qui explique directement la carence en fer, la perte de poids et la diarrhée.')
 + key('Gliadine → modification par la TG2 → présentation HLA-DQ2/DQ8 → lymphocytes T → atrophie villositaire ; anti-TG2 = trace de la réaction, dépendante du gluten ; duodénum atteint → fer absorbé en premier touché.')
 + src(E1))

C.a(3, 'Qui tester ? Présentation clinique', P(
 'La présentation est très variée ; c’est pourquoi l’ESsCD liste les situations où il faut tester. Ainsi, les signes évocateurs sont la diarrhée chronique non sanglante, la stéatorrhée, la perte de poids inexpliquée, la carence martiale chronique et l’anémie inexpliquée, les ballonnements postprandiaux, la dyspepsie, les douleurs abdominales récidivantes et la constipation. De plus, des troubles associés justifient le test : le syndrome de l’intestin irritable, la colite microscopique, l’élévation inexpliquée des transaminases, le diabète de type 1, la thyroïdite de Hashimoto, l’ataxie ou la neuropathie inexpliquées, la ' + w('k90-dh', 'dermatite herpétiforme') + ', l’ostéoporose précoce et l’infertilité avec fausses couches répétées.',
 'Par ailleurs, certains sujets asymptomatiques doivent être dépistés : les apparentés au premier degré d’un malade, ainsi que les personnes atteintes d’un syndrome de Down, de Turner ou de Williams (ESsCD 2025). En effet, le test se justifie lorsque la prévalence de la maladie non diagnostiquée atteint au moins 2 à 2,5 %, seuil retenu pour des raisons de rapport coût-efficacité.')
 + C.img('k90_dh.gif', 'Coude d’une femme : petites lésions groupées, rouges, excoriées, sur la face d’extension.', 'Dermatite herpétiforme du coude chez une femme de 37 ans : lésions groupées, très prurigineuses, sur une face d’extension.', DH)
 + P('<i>Lecture de l’image.</i> Les lésions sont groupées en bouquet et souvent excoriées, car elles démangent intensément ; or, elles sont la manifestation cutanée de la même intolérance au gluten. Ainsi, une dermatite herpétiforme impose de chercher la maladie cœliaque, même sans aucun symptôme digestif.')
 + key('Tester : diarrhée, perte de poids, carence en fer, ballonnements, transaminases, auto-immunité (diabète de type 1, Hashimoto), dermatite herpétiforme, ostéoporose précoce ; dépister : apparentés au premier degré, Down, Turner, Williams.')
 + src(E1))

C.a(4, 'Sérologie : le bon test dans les bonnes conditions', P(
 'L’ESsCD recommande les IgA anti-TG2 comme test initial unique, à tout âge (recommandation forte) ; en effet, leur sensibilité est d’environ 90,7 % et leur spécificité de 87,4 % chez l’adulte, et les tests automatisés atteignent 99 % et 100 %. De plus, deux conditions sont indispensables : doser en même temps les IgA totales, pour ne pas méconnaître un déficit en IgA, et tester pendant que le patient mange du gluten. Par ailleurs, la combinaison systématique de plusieurs tests sérologiques est déconseillée (forte), et les tests dans la salive ou les selles ne doivent pas être utilisés.',
 'Cependant, le ' + w('k90-defiga', 'déficit en IgA') + ' touche 2 à 3 % des malades. Dans ce cas, la sérologie utilise des tests IgG, comme les IgG anti-TG2 ou anti-DGP ; toutefois, leur sensibilité est plus faible, si bien qu’un résultat négatif n’exclut pas la maladie. C’est pourquoi, en présence de signes de malabsorption, une gastroscopie avec biopsies duodénales est faite quel que soit le résultat IgG (ESsCD 2025).')
 + trap('Un test fait après l’arrêt du gluten peut être faussement négatif : les anticorps se normalisent sous régime. De même, un déficit en IgA rend les IgA anti-TG2 faussement négatifs : d’où le dosage systématique des IgA totales.', 'Piège')
 + quiz('La patiente a réduit le gluten depuis trois mois « pour voir ». Ses IgA anti-TG2 sont négatives, avec des IgA totales normales. Que conclure ?',
   [('La maladie cœliaque est exclue', False), ('Le test n’est pas interprétable : il doit être fait sous régime contenant du gluten', True), ('Il faut doser les IgA anti-endomysium', False)],
   'Les marqueurs se normalisent sous régime sans gluten ; l’ESsCD demande de tester pendant la consommation de gluten (ESsCD 2025, recommandation forte).')
 + key('IgA anti-TG2 seules + IgA totales, sous gluten ; pas de combinaison systématique ; pas de test salivaire ou fécal ; déficit en IgA (2-3 %) : IgG anti-TG2 ou anti-DGP, biopsies si malabsorption.')
 + src(E1))

C.a(5, 'Confirmation : biopsies duodénales ou stratégie sans biopsie', P(
 'Classiquement, le diagnostic est confirmé par l’histologie. Ainsi, l’ESsCD recommande au moins quatre biopsies du duodénum distal et deux du bulbe (recommandation forte), même si la muqueuse paraît normale, car les lésions peuvent être en mosaïque ; de plus, les biopsies doivent être bien orientées et colorées à l’hématoxyline-éosine. Ensuite, l’histologie est classée selon la ' + w('k90-marsh', 'classification de Marsh') + ', dont le stade III (atrophie villositaire) est subdivisé en 3A (partielle), 3B (subtotale) et 3C (totale).',
 'Par ailleurs, l’ESsCD 2025 introduit une ' + w('k90-sansbiopsie', 'stratégie sans biopsie') + ' chez l’adulte de moins de 45 ans dont les IgA anti-TG2 sont au moins 10 fois la limite supérieure de la normale (recommandation conditionnelle). En effet, à ce seuil, la spécificité atteint 100 % dans une méta-analyse de 12 103 participants, alors que la sensibilité n’est que de 51 %. Cependant, trois conditions s’ajoutent : le résultat doit être confirmé sur un second prélèvement, le patient doit continuer le gluten jusqu’à confirmation, et la décision revient à un centre de soins secondaires. Enfin, un stade Marsh I avec une sérologie négative rend la maladie peu probable ; il faut alors chercher une autre cause.')
 + C.img('k90_histo.gif', 'Coupe histologique colorée à l’hématoxyline-éosine : atrophie villositaire marquée et nombreux lymphocytes dans l’épithélium.', 'Maladie cœliaque : atrophie villositaire marquée et augmentation des lymphocytes intraépithéliaux (HE, × 200).', HIST)
 + P('<i>Lecture de l’image.</i> Les petits noyaux sombres glissés entre les entérocytes sont des lymphocytes intraépithéliaux ; or, leur augmentation est le premier stade de Marsh, avant même l’atrophie. Ainsi, la lecture histologique suit la cascade immunitaire : d’abord l’infiltrat, puis l’hyperplasie des cryptes, enfin l’aplatissement des villosités. C’est pourquoi un infiltrat isolé, sans anticorps, ne suffit pas au diagnostic.')
 + key('≥ 4 biopsies du duodénum distal + 2 du bulbe ; Marsh III = atrophie (3A, 3B, 3C) ; sans biopsie : < 45 ans, IgA anti-TG2 ≥ 10 × la normale, confirmées sur un second prélèvement, décision en soins secondaires ; Marsh I séronégatif : autre cause.')
 + src(E1))

C.a(6, 'Traitement : le régime sans gluten à vie', P(
 'Le traitement de la maladie cœliaque est le régime sans gluten strict et à vie (recommandation forte) ; en effet, il contrôle les symptômes, améliore la qualité de vie et réduit le risque de complications. Ainsi, le seuil généralement admis est de 10 mg de gluten par jour au maximum, car des apports plus élevés peuvent léser la muqueuse chez certains malades. De plus, seule l’avoine certifiée sans gluten est sûre ; elle peut être introduite dès le diagnostic, même si une petite minorité y réagit (ESsCD 2025).',
 'Par ailleurs, le diététicien a un rôle central (forte) : dès le diagnostic, il éduque le patient, évalue l’état nutritionnel et corrige les carences ; ensuite, il surveille l’adhésion et repère les expositions involontaires. En outre, une restriction temporaire du lactose peut aider au diagnostic, puisque le déficit secondaire en lactase guérit avec la muqueuse ; enfin, aucun traitement médicamenteux non diététique n’est disponible hors essais cliniques (ESsCD 2025).')
 + trap('Un régime « pauvre en gluten » ne suffit pas : le seuil toléré est de l’ordre de 10 mg par jour, soit des traces. C’est pourquoi l’étiquetage et le risque de contamination croisée des céréales doivent être enseignés.', 'Piège')
 + key('Régime sans gluten strict à vie (forte) ; ≤ 10 mg de gluten/j ; avoine certifiée sans gluten ; diététicien au diagnostic et au suivi ; lactose réduit temporairement si besoin ; pas de médicament hors essais.')
 + src(E2))

C.a(7, 'Bilan initial et maladies associées', P(
 'Au diagnostic, l’état nutritionnel est évalué par la clinique, l’anthropométrie, l’enquête alimentaire et des dosages ciblés (forte) ; ainsi, on recherche la dénutrition et les carences en micronutriments. De plus, la fonction thyroïdienne est contrôlée par la TSH, avec T4 libre si la TSH est anormale (forte). Par ailleurs, une densitométrie osseuse est recommandée après un an de régime chez les patients à risque : diagnostic tardif, malabsorption sévère ou amaigrissement marqué, antécédent de fracture de fragilité, autre facteur de risque d’ostéoporose ou syndrome de Down (ESsCD 2025).',
 'Ensuite, la vaccination contre le pneumocoque est recommandée en cas d’asplénie fonctionnelle, de maladie auto-immune associée, de maladie réfractaire de type II, ou après 65 ans. Enfin, les apparentés sont dépistés : chez l’adulte, la sérologie anti-TG2 est le test initial le plus rentable, et un contrôle tous les 4 à 5 ans peut être envisagé chez l’apparenté séronégatif selon son risque (conditionnelle).')
 + key('Bilan nutritionnel, TSH, densitométrie à 1 an si risque, pneumocoque si asplénie, auto-immunité, réfractaire II ou > 65 ans ; dépistage des apparentés.')
 + src(E2))

C.a(8, 'Suivi et réponse au régime', P(
 'Le suivi à long terme est recommandé ; en effet, il vérifie l’adhésion, détecte les complications et soutient le patient. Ainsi, les symptômes s’améliorent généralement entre 4 semaines et 4 à 5 mois ; de plus, les IgA anti-TG2 baissent dès 2 à 4 semaines et se normalisent le plus souvent en environ 12 mois. Enfin, la muqueuse guérit en général vers un an, mais la guérison histologique complète ne concerne que 50 à 83 % des patients après 1 à 5 ans (ESsCD 2025).',
 'Cependant, la sérologie de suivi a une valeur asymétrique. En effet, des IgA anti-TG2 positives sous régime suggèrent une mauvaise adhésion ou une contamination ; en revanche, un résultat négatif ne prouve ni l’adhésion stricte ni la guérison de la muqueuse (forte). C’est pourquoi la biopsie de contrôle n’est pas systématique, mais elle est discutée de façon personnalisée, notamment si les symptômes persistent ou s’aggravent (conditionnelle).')
 + key('Symptômes : 4 semaines à 4-5 mois ; anti-TG2 : baisse à 2-4 semaines, normalisation ≈ 12 mois ; muqueuse ≈ 1 an (guérison complète 50-83 %) ; anti-TG2 positives = gluten ; négatives ≠ guérison.')
 + src(E2))

C.a(9, 'Réponse incomplète et maladie cœliaque réfractaire', P(
 'Une réponse incomplète au régime est le plus souvent due à une exposition persistante au gluten ; toutefois, elle peut aussi traduire une maladie lente à répondre, une ' + w('k90-mcr', 'maladie cœliaque réfractaire') + ', une erreur diagnostique initiale ou une maladie associée. Ainsi, devant des symptômes persistants, il faut d’abord vérifier le diagnostic initial et l’adhésion ; ensuite, si l’adhésion est confirmée, refaire l’histologie et chercher une autre cause, comme un trouble fonctionnel, une autre maladie digestive, une forme réfractaire ou une tumeur (forte).',
 'Par ailleurs, la maladie réfractaire est définie par la persistance ou la récidive des symptômes et de l’atrophie après au moins 12 mois de régime strict, sans autre cause ; elle est de type I ou II selon la proportion de lymphocytes T aberrants. De plus, son diagnostic repose sur la sérologie, les biopsies avec cytométrie en flux des lymphocytes intraépithéliaux et étude de clonalité, l’entéroscopie et l’imagerie en coupes, de préférence dans un centre tertiaire. Enfin, aucun traitement n’est validé par des essais contrôlés ; le ' + w('k90-d-budes', 'budésonide') + ' en capsules ouvertes est considéré comme le premier choix du type I, et il peut traiter le type II léger à modéré (ESsCD 2025, conditionnelle).')
 + C.pareto('pareto-k90-clinique', 'Maladie cœliaque', ['k90-3', 'k90-4', 'k90-5', 'k90-6', 'k90-8', 'k90-9'],
     ['Tester devant une carence en fer, des ballonnements ou une auto-immunité.',
      'IgA anti-TG2 + IgA totales, sous gluten.',
      'Biopsies : ≥ 4 distales + 2 bulbaires ; sans biopsie seulement si < 45 ans et ≥ 10 × la normale.',
      'Régime sans gluten strict à vie, avec diététicien.',
      'Anti-TG2 positives sous régime = gluten.',
      'Réfractaire : ≥ 12 mois de régime strict, autre cause exclue.'])
 + key('Réponse incomplète : gluten caché d’abord ; réfractaire = symptômes et atrophie après ≥ 12 mois de régime strict ; types I et II ; centre tertiaire ; budésonide en capsules ouvertes (hors indication suisse).')
 + src(E2))

C.a(10, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. Elle a une carence en fer récidivante, des ballonnements et une thyroïdite de Hashimoto : elle doit donc être testée. Cependant, elle a réduit le gluten ; c’est pourquoi on lui demande de le réintroduire avant le dosage des IgA anti-TG2 et des IgA totales.',
 'Ensuite, ses IgA anti-TG2 reviennent à 15 fois la limite supérieure, avec des IgA totales normales. Or, elle a moins de 45 ans ; dès lors, la stratégie sans biopsie est possible, à condition de confirmer le résultat sur un second prélèvement et de décider en consultation spécialisée. Enfin, le régime sans gluten est lancé avec un diététicien, le fer est corrigé, et la sérologie est recontrôlée pour vérifier l’adhésion.')
 + key('Indication de test → réintroduction du gluten → anti-TG2 ≥ 10 × + IgA normales → < 45 ans : confirmation sur second prélèvement → régime sans gluten + diététicien → suivi sérologique.')
 + src(E1, E2))

C.a(11, 'Autres malabsorptions et paramètres clés', P(
 'Les autres sous-catégories de K90 ne sont traitées ici que brièvement. Ainsi, la stéatorrhée pancréatique relève de l’insuffisance pancréatique exocrine : l’ESsCD rappelle que, chez le malade cœliaque, un traitement enzymatique substitutif peut être indiqué lorsque cette insuffisance est confirmée (conditionnelle). De même, une intolérance au lactose secondaire à l’atrophie est habituellement transitoire. En revanche, la sprue tropicale et le syndrome de l’anse borgne n’ont pas été traités faute de recommandation lue pour ce cours (TODO).')
 + alert(
 '<p><b>Critères.</b> Test initial : IgA anti-TG2 + IgA totales sous gluten. Biopsies : ≥ 4 duodénum distal + 2 bulbe. Sans biopsie : < 45 ans, IgA anti-TG2 ≥ 10 × la normale, confirmées sur un second prélèvement, décision en soins secondaires. Réfractaire : symptômes et atrophie après ≥ 12 mois de régime strict, autre cause exclue.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Prévalence ≈ 0,7 % (histologie), 1-1,6 % (sérologie) ; anti-TG2 : sensibilité 90,7 %, spécificité 87,4 % ; ≥ 10 × : spécificité 100 %, sensibilité 51 % ; déficit en IgA 2-3 % ; ≤ 10 mg de gluten/j ; normalisation des anti-TG2 ≈ 12 mois ; guérison histologique 50-83 %.</div>'
 + src(E1, E2))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Recommandation ESsCD 2025'], [
   ['Suspicion ?', w('k90-tg2', 'IgA anti-TG2') + ' + IgA totales, sous gluten', 'Test initial unique (forte)'],
   ['Déficit en IgA ?', 'IgG anti-TG2 ou anti-DGP', 'Biopsies si malabsorption, même si négatives'],
   ['Confirmation ?', 'Gastroscopie : ≥ 4 biopsies distales + 2 bulbaires', 'Forte'],
   ['Confirmation sans biopsie ?', 'Anti-TG2 ≥ 10 × la normale, second prélèvement', 'Adulte < 45 ans (conditionnelle)'],
   ['Doute diagnostique ?', w('k90-hla', 'Typage HLA-DQ2/DQ8'), 'Pas en routine ; forte valeur prédictive négative'],
   ['Suivi ?', 'Anti-TG2 ; biopsie selon l’évolution', 'Biopsie non systématique (conditionnelle)']])
 + P('<i>Lecture du tableau.</i> La sérologie trie, l’histologie confirme, et le typage HLA sert surtout à exclure ; en effet, l’absence de HLA-DQ2 et DQ8 rend la maladie très improbable, alors que leur présence est banale dans la population. Ainsi, chaque examen est demandé pour une question, jamais en bloc.')
 + key('Anti-TG2 + IgA totales → biopsies (ou sans biopsie si < 45 ans et ≥ 10 ×) → HLA pour exclure en cas de doute → anti-TG2 pour suivre l’adhésion.')
 + src(E1, E2))

C.e(2, 'Lire l’endoscopie et la biopsie', P(
 'En endoscopie, l’atrophie peut se voir : festonnement des plis de Kerckring, perte des plis, aspect en mosaïque. Cependant, la muqueuse peut paraître normale ; c’est pourquoi les biopsies sont faites même si l’aspect est normal (ESsCD 2025). Ensuite, le pathologiste décrit les lymphocytes intraépithéliaux, les cryptes et les villosités, et donne le stade de Marsh.')
 + C.img('k90_endo.gif', 'Endoscopie en lumière blanche du duodénum descendant : plis de Kerckring à bord dentelé, en feston.', 'Maladie cœliaque en endoscopie : festonnement des plis de Kerckring dans le duodénum descendant.', ENDO)
 + P('<i>Lecture de l’image.</i> Les plis normaux ont un bord lisse ; ici, en revanche, leur bord est dentelé, parce que la muqueuse aplatie ne les recouvre plus de villosités. Ainsi, ce signe oriente la biopsie ; toutefois, son absence n’exclut rien, puisque l’atrophie peut être en mosaïque.')
 + key('Endoscopie : festonnement, perte des plis, mosaïque ; biopsies même si l’aspect est normal ; histologie : lymphocytes intraépithéliaux → cryptes → villosités (Marsh).')
 + C.pareto('pareto-k90-examens', 'Examens', ['k90-e-1', 'k90-e-2'],
     ['IgA anti-TG2 + IgA totales sous gluten.',
      '≥ 4 biopsies distales + 2 bulbaires.',
      'Sans biopsie : < 45 ans, ≥ 10 ×, deux prélèvements.',
      'HLA-DQ2/DQ8 pour exclure.'])
 + src(E1))

# ---------------- Sciences
C.s('immuno', 'Immunologie', 'Immunologie : une auto-immunité déclenchée par un aliment', P(
 'La maladie cœliaque a une particularité : son déclencheur est connu et extérieur, le gluten. Ainsi, la TG2 modifie la gliadine, qui se lie mieux à HLA-DQ2 ou DQ8 et active des lymphocytes T ; de plus, la réponse produit des anticorps dirigés contre la TG2 elle-même. Par conséquent, retirer le gluten éteint à la fois l’inflammation et les anticorps, ce qui fait du régime un traitement causal.')
 + key('Antigène connu (gliadine) + auto-antigène (TG2) → retirer le gluten = traiter la cause.', 'Science → traitement.'))
C.s('genet', 'Génétique', 'Génétique : HLA nécessaire mais non suffisant', P(
 'Presque tous les malades portent HLA-DQ2 ou HLA-DQ8 ; en effet, moins de 1 % ne portent aucun de ces hétérodimères (ESsCD 2025). Cependant, ces allèles sont fréquents dans la population générale ; ainsi, leur présence ne prouve rien, alors que leur absence rend la maladie très improbable. C’est pourquoi le typage HLA a une faible valeur prédictive positive et une forte valeur prédictive négative.')
 + key('HLA-DQ2/DQ8 absents → maladie très improbable ; présents → non spécifique.', 'Science → interprétation.'))
C.s('histo', 'Histologie', 'Histologie : la surface d’absorption', P(
 'Les villosités et les microvillosités multiplient la surface du grêle ; or, l’atrophie la réduit fortement. Ainsi, les nutriments absorbés dans le duodénum et le jéjunum proximal, comme le fer, manquent les premiers ; de plus, la perte des enzymes de la bordure en brosse, comme la lactase, explique l’intolérance secondaire au lactose, qui régresse quand la muqueuse guérit.')
 + key('Atrophie → moins de surface et moins de lactase → carence en fer, intolérance au lactose transitoire.', 'Science → clinique.'))
C.s('stat', 'Biostatistique', 'Biostatistique : pourquoi le seuil de 10 fois la normale', P(
 'À un seuil élevé, un test devient plus spécifique mais moins sensible ; ainsi, au-delà de 10 fois la normale, les IgA anti-TG2 ont une spécificité de 100 % mais une sensibilité de 51 % (ESsCD 2025). Par conséquent, un résultat très élevé permet de se passer de la biopsie, alors qu’un résultat plus bas ne permet pas de conclure sans histologie. De plus, la confirmation sur un second prélèvement protège contre une erreur de laboratoire.')
 + key('Seuil haut = spécifique → règle d’inclusion ; sous le seuil → biopsie.', 'Science → décision.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie : diététique d’abord', P(
 'Dans la maladie cœliaque, le « médicament » principal est un régime ; en effet, aucun traitement médicamenteux non diététique n’est disponible hors essais cliniques (ESsCD 2025, forte).')
 + table(['Situation', 'Mesure', 'Source', 'Fenêtre'], [
   ['Toute maladie cœliaque', 'Régime sans gluten strict à vie, ≤ 10 mg/j', 'ESsCD 2025, forte', w('k90-rsg', 'Fiche')],
   ['Carences au diagnostic', 'Correction ciblée (fer notamment) selon les dosages', 'ESsCD 2025', w('k90-fer', 'Fiche')],
   ['Insuffisance pancréatique exocrine confirmée', 'Enzymes pancréatiques substitutives', 'ESsCD 2025, conditionnelle', w('k90-malabs', 'Fiche')],
   ['Maladie réfractaire de type I', 'Budésonide en capsules ouvertes', 'ESsCD 2025, conditionnelle', w('k90-d-budes', 'Monographie')]])
 + P('<i>Lecture du tableau.</i> Seule la première ligne traite la cause ; les autres corrigent ses conséquences ou une complication. Ainsi, une carence en fer qui récidive malgré la supplémentation signale le plus souvent une exposition persistante au gluten, et non un échec du fer.')
 + key('Régime sans gluten = traitement causal ; carences corrigées ; enzymes si insuffisance pancréatique ; budésonide dans la forme réfractaire.')
 + src(E2))

C.p(2, 'Doses et statut réglementaire', P(
 'Les recommandations lues ne donnent pas de doses de fer, de vitamines ni d’enzymes pancréatiques ; c’est pourquoi aucune dose n’est proposée ici (TODO : à compléter par les informations professionnelles suisses). En revanche, le statut du budésonide est précis.')
 + table(['Médicament', 'Indication suisse (FI)', 'Usage dans la maladie cœliaque', 'Source'], [
   ['Budésonide (Entocort CIR®)', 'Maladie de Crohn iléo-cæcale légère à modérée ; induction de la rémission de la colite microscopique', 'Maladie réfractaire de type I et type II léger à modéré : hors indication', 'FI Entocort CIR®, ESsCD 2025'],
   ['Vaccin pneumococcique', 'Selon le plan de vaccination', 'Asplénie fonctionnelle, auto-immunité, réfractaire II, > 65 ans', 'ESsCD 2025']])
 + P('<i>Lecture du tableau.</i> Le budésonide est un corticoïde à fort effet de premier passage hépatique ; ainsi, ouvrir la capsule permet de libérer le principe actif plus haut dans le grêle, là où siège l’atrophie. Cependant, cet usage n’est pas une indication suisse ; de plus, l’information professionnelle le contre-indique en cas de trouble sévère de la fonction hépatique.')
 + trap('Le budésonide en capsules ouvertes dans la maladie cœliaque réfractaire est un usage hors indication en Suisse : il relève d’un centre spécialisé et ne remplace jamais la vérification préalable de l’adhésion au régime.', 'Point à valider')
 + key('Doses de fer, vitamines, enzymes : TODO ; budésonide : hors indication suisse dans la forme réfractaire, contre-indiqué si atteinte hépatique sévère.')
 + src(FI('Entocort CIR®'), E2))

C.p(3, 'Surveillance', alert(
 'Un régime sans gluten mal équilibré peut entraîner des carences en macro- et micronutriments ; de plus, les adultes sous régime ont un risque plus élevé de syndrome métabolique que les malades non traités. C’est pourquoi un suivi nutritionnel et diététique, une activité physique et la surveillance du poids, de la pression artérielle, des lipides et de la résistance à l’insuline sont recommandés (ESsCD 2025).', 'Sécurité.')
 + P('Par ailleurs, l’adhésion se mesure par l’entretien clinique, la sérologie et la revue diététique ; en outre, la recherche de peptides immunogènes du gluten dans les selles ou les urines peut être envisagée en cas de doute. Enfin, l’adhésion est moins bonne chez les jeunes, les patients de faible niveau socio-économique, ceux qui mangent souvent hors du domicile ou qui n’ont pas de symptômes.')
 + key('Équilibre du régime, syndrome métabolique, adhésion (sérologie, diététicien, peptides du gluten si doute).')
 + C.pareto('pareto-k90-pharma', 'Pharmacologie et diététique', ['k90-p-1', 'k90-p-2', 'k90-p-3'],
     ['Régime sans gluten strict, ≤ 10 mg/j.',
      'Diététicien au diagnostic et au suivi.',
      'Corriger les carences.',
      'Surveiller le syndrome métabolique.'])
 + src(E2))

# ---------------- Fenêtres
L = lab
C.pop('k90-mc', 'Maladie cœliaque', L(('Définition', 'Entéropathie auto-immune déclenchée par le gluten sur terrain HLA-DQ2/DQ8.'), ('Prévalence', '≈ 0,7 % (histologie), 1-1,6 % (sérologie) en Occident.'), ('Traitement', 'Régime sans gluten strict à vie.')) + C.img('k90_marsh.gif', 'Biopsie du grêle : atrophie villositaire.', 'Atrophie villositaire (Marsh III).', MARSH) + src(E1, E2))
C.pop('k90-malabs', 'Malabsorption intestinale', L(('Mécanismes', 'Atteinte muqueuse, défaut de digestion, intolérance, anse borgne, sprue tropicale.'), ('Pancréas', 'Enzymes substitutives si insuffisance exocrine confirmée (ESsCD, conditionnelle).')) + src(E2))
C.pop('k90-fer', 'Carence en fer', L(('Lien', 'Le fer est absorbé dans le duodénum, premier segment atteint.'), ('Valeur', 'Carence martiale chronique et anémie inexpliquée : indications de test (ESsCD 2025).'), ('Dose', 'Non précisée par les sources lues (TODO).')) + src(E1))
C.pop('k90-tg2', 'IgA anti-transglutaminase (TG2)', L(('Place', 'Test initial unique à tout âge (forte).'), ('Performance', 'Sensibilité 90,7 %, spécificité 87,4 % ; ≥ 10 × : spécificité 100 %, sensibilité 51 %.'), ('Conditions', 'Avec IgA totales ; sous gluten.')) + src(E1))
C.pop('k90-defiga', 'Déficit en IgA', L(('Fréquence', '2-3 % des malades cœliaques.'), ('Conduite', 'IgG anti-TG2 ou anti-DGP ; négatif n’exclut pas ; biopsies si malabsorption.')) + src(E1))
C.pop('k90-hla', 'HLA-DQ2 / HLA-DQ8', L(('Rôle', 'Présentent la gliadine modifiée aux lymphocytes T.'), ('Test', 'Faible valeur prédictive positive, forte valeur prédictive négative ; pas en routine ; utile en cas de doute.')) + src(E1))
C.pop('k90-atrophie', 'Atrophie villositaire', L(('Définition', 'Aplatissement des villosités du grêle (Marsh III).'), ('Conséquence', 'Perte de surface d’absorption : fer, poids, diarrhée.')) + C.img('k90_histo.gif', 'Histologie : atrophie et lymphocytes intraépithéliaux.', 'Atrophie villositaire et lymphocytose intraépithéliale.', HIST) + src(E1))
C.pop('k90-marsh', 'Classification de Marsh', L(('I', 'Augmentation des lymphocytes intraépithéliaux.'), ('III', 'Atrophie villositaire : 3A partielle, 3B subtotale, 3C totale.'), ('Limite', 'Sous-stades peu utiles en routine ; Marsh I séronégatif : autre cause.')) + C.img('k90_marsh.gif', 'Biopsie : Marsh III.', 'Stade Marsh III.', MARSH) + src(E1))
C.pop('k90-sansbiopsie', 'Stratégie sans biopsie', L(('Conditions', 'Adulte < 45 ans ; IgA anti-TG2 ≥ 10 × la normale.'), ('Obligations', 'Second prélèvement confirmant ; gluten maintenu jusqu’à confirmation ; décision en soins secondaires.'), ('Grade', 'Conditionnelle (ESsCD 2025).')) + src(E1))
C.pop('k90-dh', 'Dermatite herpétiforme', L(('Aspect', 'Lésions groupées, très prurigineuses, sur les faces d’extension.'), ('Valeur', 'Indication de test de la maladie cœliaque (ESsCD 2025).')) + C.img('k90_dh.gif', 'Coude : dermatite herpétiforme.', 'Dermatite herpétiforme.', DH) + src(E1))
C.pop('k90-rsg', 'Régime sans gluten', L(('Règle', 'Strict et à vie (forte).'), ('Seuil', '≤ 10 mg de gluten par jour.'), ('Avoine', 'Seulement certifiée sans gluten.'), ('Appui', 'Diététicien spécialisé.')) + src(E2))
C.pop('k90-mcr', 'Maladie cœliaque réfractaire', L(('Définition', 'Symptômes et atrophie après ≥ 12 mois de régime strict, autre cause exclue ; types I et II.'), ('Bilan', 'Biopsies avec cytométrie en flux et clonalité, entéroscopie, imagerie ; centre tertiaire.'), ('Traitement', 'Aucun validé par essai ; budésonide en capsules ouvertes en premier dans le type I.')) + src(E2))
C.pop('k90-d-budes', 'Budésonide', L(('Indications suisses', 'Maladie de Crohn iléo-cæcale ; colite microscopique (induction).'), ('Maladie cœliaque', 'Réfractaire : hors indication (ESsCD, conditionnelle).'), ('Contre-indication', 'Trouble sévère de la fonction hépatique.')) + src(FI('Entocort CIR®'), E2))

C.termes = [
 (r'maladie cœliaque réfractaire', 'k90-mcr'), (r'maladie cœliaque', 'k90-mc'), (r'malabsorption', 'k90-malabs'), (r'IgA anti-TG2', 'k90-tg2'),
 (r'déficit en IgA', 'k90-defiga'), (r'HLA-DQ2', 'k90-hla'), (r'atrophie villositaire', 'k90-atrophie'), (r'Marsh', 'k90-marsh'),
 (r'sans biopsie', 'k90-sansbiopsie'), (r'dermatite herpétiforme', 'k90-dh'), (r'régime sans gluten', 'k90-rsg'), (r'budésonide', 'k90-d-budes'),
 (r'carence en fer', 'k90-fer'),
]

C.write()
