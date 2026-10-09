import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K85', 'Pancréatite aiguë',
    'K85 — Pancréatite aiguë · CIM-10-GM 2024 · Pancréas exocrine',
    'Adulte · diagnostic, gravité, réanimation initiale, étiologie biliaire, nécrose infectée · rédaction du 09.10.2026 · référentiels WSES 2019, ESGE 2018, classification d’Atlanta révisée (2012), informations professionnelles suisses',
    'Pharmacologie de la pancréatite aiguë')
w = C.w
WSES = ('Leppäniemi A. et al., 2019 WSES guidelines for the management of severe acute pancreatitis, World J Emerg Surg 2019;14:27', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6567462/')
ESGE = ('Arvanitakis M. et al., ESGE, prise en charge endoscopique de la pancréatite aiguë nécrosante, Endoscopy 2018;50:524-546', 'https://www.esge.com/assets/downloads/pdfs/guidelines/2018_a_0588_5365.pdf')
ATL = ('Banks P. A. et al., Classification of acute pancreatitis 2012: revision of the Atlanta classification, Gut 2013;62:102-111 (définitions reprises par la WSES 2019 et l’ESGE 2018)', 'https://doi.org/10.1136/gutjnl-2012-302779')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS via AmiKo), consultée le 09.10.2026', 'https://amiko.oddb.org/fr')

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 58 ans arrive aux urgences pour une douleur épigastrique intense, apparue brutalement après un repas et irradiant dans le dos ; elle vomit. Or, la lipase dépasse dix fois la limite supérieure de la normale, et une échographie montre une vésicule lithiasique. <b>La question n’est donc pas seulement de poser le diagnostic de pancréatite aiguë, mais de prévoir sa gravité et d’en traiter la cause.</b>',
 'Pour répondre à cette question, le médecin doit savoir : poser le diagnostic selon les ' + w('k85-criteres', 'critères d’Atlanta révisés') + ' ; classer la gravité selon la ' + w('k85-atlanta', 'classification d’Atlanta révisée') + ' ; reconnaître la ' + w('k85-defaillance', 'défaillance d’organe') + ' et sa persistance au-delà de 48 heures ; conduire la réanimation liquidienne et l’analgésie ; décider d’une ' + w('k85-cpre', 'CPRE') + ' en urgence ; enfin, prendre en charge une ' + w('k85-necrose-infectee', 'nécrose infectée') + ' selon une stratégie progressive.')
 + key(w('k85-criteres', 'deux critères sur trois') + ' pour le diagnostic ; ' + w('k85-defaillance', 'défaillance d’organe persistante') + ' pour la gravité.', 'Point de départ.'))

C.a(1, 'Définition et classification', P(
 'La pancréatite aiguë est une inflammation aiguë du pancréas, caractérisée à l’histologie par une destruction des cellules acineuses (WSES 2019). Ainsi, la classification d’Atlanta révisée en 2012 distingue deux formes morphologiques : la ' + w('k85-interstitielle', 'pancréatite interstitielle œdémateuse') + ', de loin la plus fréquente, et la ' + w('k85-necrosante', 'pancréatite nécrosante') + '. De plus, elle décrit deux phases : une phase précoce, dominée par la réponse inflammatoire systémique et la défaillance d’organe, puis une phase tardive, marquée par les complications locales.',
 'À partir de ces formes, la gravité se classe en trois degrés. La forme légère ne comporte ni défaillance d’organe ni complication ; en revanche, la forme modérément sévère comporte une défaillance d’organe transitoire, de moins de 48 heures, ou une complication locale ou systémique. Enfin, la forme sévère se définit par une défaillance d’organe persistante, de plus de 48 heures, unique ou multiple.')
 + table(['Degré (Atlanta 2012)', 'Défaillance d’organe', 'Complications locales ou systémiques'], [
   ['Légère', 'Aucune', 'Aucune'],
   ['Modérément sévère', 'Transitoire (< 48 h)', 'Possibles, sans défaillance persistante'],
   ['Sévère', 'Persistante (> 48 h), unique ou multiple', 'Habituelles']])
 + P('Le tableau se lit par la colonne du milieu : en effet, c’est la durée de la défaillance d’organe, et non l’aspect de la nécrose, qui sépare la forme sévère des autres. Par ailleurs, la ' + w('k85-dbc', 'classification fondée sur les déterminants') + ' ajoute un degré « critique » (défaillance persistante et nécrose infectée) ; toutefois, la WSES 2019 juge les deux classifications équivalentes.')
 + key('Deux formes (interstitielle, nécrosante), deux phases (précoce, tardive), trois degrés : la défaillance d’organe persistante au-delà de 48 heures définit la forme sévère.')
 + src(ATL, WSES, ESGE))

C.a(2, 'Épidémiologie et étiologies', P(
 'Après la définition, la fréquence et les causes situent l’enjeu. Ainsi, selon la WSES 2019, la plupart des patients ont une forme légère ; cependant, 20 à 30 % développent une forme sévère, dont la mortalité hospitalière atteint environ 15 %. De plus, la nécrose s’infecte chez 20 à 40 % des patients atteints d’une forme sévère, ce qui aggrave les défaillances d’organe.',
 'Les deux causes principales sont la ' + w('k85-biliaire', 'lithiase biliaire') + ' et la consommation excessive d’alcool. En outre, en l’absence de lithiase et d’alcool, il faut doser les triglycérides et le calcium : une ' + w('k85-tg', 'hypertriglycéridémie') + ' supérieure à 11,3 mmol/l (1000 mg/dl) suffit à expliquer la pancréatite (WSES 2019). Enfin, on parle de pancréatite ' + w('k85-idiopathique', 'idiopathique') + ' lorsque le bilan initial ne trouve aucune cause.')
 + trap('Aucune donnée nationale suisse d’incidence n’a été retrouvée lors de la rédaction ; les chiffres cités sont ceux de la WSES 2019, attribués.', 'Lacune documentaire')
 + key('Lithiase biliaire et alcool en tête ; triglycérides > 11,3 mmol/l et calcium à rechercher sinon. Forme sévère : 20 à 30 %, mortalité d’environ 15 %.')
 + src(WSES))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre la gravité, il faut suivre l’agression de la cellule acineuse. Normalement, les enzymes pancréatiques sont sécrétées sous forme inactive et activées dans le duodénum. Or, au cours de la pancréatite, elles s’activent dans le pancréas lui-même ; dès lors, la glande et la graisse qui l’entoure sont digérées. C’est ainsi qu’apparaît la ' + w('k85-cytosteatonecrose', 'cytostéatonécrose') + ', nécrose de la graisse par la lipase.',
 'Ensuite, la lésion locale déclenche une réponse inflammatoire systémique. En effet, la perméabilité capillaire augmente, le liquide fuit vers le troisième secteur et l’hémoconcentration s’installe ; par conséquent, la microcirculation pancréatique se dégrade, ce qui favorise la nécrose. De plus, la barrière intestinale s’altère, si bien que des bactéries d’origine digestive peuvent coloniser la nécrose (WSES 2019).')
 + C.img('k85_cytosteatonecrose_he.gif', 'Coupe histologique de tissu adipeux péripancréatique : adipocytes nécrosés à contours fantomatiques, bordés d’un infiltrat inflammatoire.', 'Cytostéatonécrose tryptique dans une pancréatite sévère, coloration hématoxyline-éosine. Les adipocytes détruits par les enzymes pancréatiques perdent leur noyau et sont cernés par une réaction inflammatoire.', credit({'auteur': 'Patho', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Tryptic_fat_tissue_necrosis_in_severe_pancreatitis,_HE_1.JPG'}))
 + key('Activation enzymatique intrapancréatique, cytostéatonécrose, fuite capillaire et hémoconcentration ; la translocation bactérienne explique l’infection tardive de la nécrose.')
 + src(WSES))

C.a(4, 'Présentation clinique', P(
 'La démarche commence donc par la clinique. Le symptôme cardinal est une douleur épigastrique aiguë, intense, souvent transfixiante vers le dos, associée à des nausées et des vomissements. Par ailleurs, l’examen recherche les signes de gravité : tachycardie, hypotension, polypnée, oligurie et confusion, car ils traduisent une défaillance d’organe débutante.',
 'Plus rarement, une ecchymose péri-ombilicale (' + w('k85-cullen', 'signe de Cullen') + ') ou des flancs (signe de Grey-Turner) témoigne d’une diffusion hémorragique rétropéritonéale. Cependant, ces signes sont tardifs et inconstants ; ils ne doivent donc pas retarder l’évaluation de la gravité.')
 + C.img('k85_cullen.gif', 'Photographie de l’abdomen d’un homme : ecchymose violacée autour de l’ombilic.', 'Signe de Cullen chez un homme de 36 ans, quatre jours après le début d’une douleur épigastrique sévère survenue après une forte consommation d’alcool ; la lipase était élevée et le scanner montrait une inflammation pancréatique et péripancréatique marquée.', credit({'auteur': 'Herbert L. Fred, MD et Hendrik A. van Dijk', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Cullen%27s_sign.jpg'}))
 + trap('Une douleur épigastrique avec lipase élevée n’exclut pas une perforation d’ulcère ou une ischémie mésentérique : si le diagnostic reste douteux, le scanner tranche (WSES 2019).', 'Piège')
 + key('Douleur épigastrique transfixiante et vomissements ; tachycardie, hypotension, polypnée, oligurie et confusion signalent la défaillance d’organe.')
 + src(WSES))

C.a(5, 'Diagnostic', P(
 'Au terme de l’examen, le diagnostic repose sur ' + w('k85-criteres', 'deux des trois critères') + ' suivants : une douleur abdominale compatible ; une ' + w('k85-lipase', 'lipase') + ' ou une amylase sériques supérieures à trois fois la limite supérieure de la normale ; enfin, des signes caractéristiques à l’imagerie. Ainsi, lorsque la douleur est typique et la lipase élevée, aucune imagerie n’est nécessaire au diagnostic.',
 'De plus, la lipase est préférée à l’amylase, car elle est plus spécifique et reste élevée plus longtemps (WSES 2019). En revanche, son niveau ne reflète pas la gravité. Enfin, une ' + w('k85-echo', 'échographie abdominale') + ' est faite dès l’admission, non pour confirmer la pancréatite, mais pour rechercher une lithiase biliaire.')
 + quiz('Un homme de 45 ans a une douleur épigastrique typique depuis 6 heures ; la lipase vaut 5 fois la normale. Faut-il un scanner pour poser le diagnostic ?',
   [('Oui, le scanner est indispensable', False), ('Non, deux critères sur trois sont réunis', True), ('Oui, mais seulement après 72 heures', False)],
   'Douleur compatible et lipase supérieure à trois fois la normale suffisent ; le scanner est réservé au doute diagnostique ou, plus tard, au bilan des complications (WSES 2019).')
 + key('Deux critères sur trois : douleur, lipase ou amylase > 3 fois la normale, imagerie. Échographie dès l’admission pour la cause biliaire.')
 + src(WSES, ATL))

C.a(6, 'Évaluation de la gravité', P(
 'Une fois le diagnostic posé, la question devient celle de la gravité. Or, aucun score n’est un gold standard ; toutefois, la WSES 2019 et l’ESGE 2018 retiennent le ' + w('k85-bisap', 'score BISAP') + ' dans les 24 premières heures, simple et aussi performant que l’APACHE II. De plus, plusieurs marqueurs simples complètent ce score : un ' + w('k85-hematocrite', 'hématocrite supérieur à 44 %') + ' est un facteur de risque indépendant de nécrose, et une urée élevée, ou qui augmente, prédit la mortalité.',
 'Ensuite, la ' + w('k85-crp', 'CRP') + ' supérieure ou égale à 150 mg/l au troisième jour est un facteur pronostique de forme sévère (WSES 2019). Cependant, le critère décisif reste la ' + w('k85-defaillance', 'défaillance d’organe') + ' : par conséquent, tout patient qui présente une défaillance d’organe doit être admis en soins intensifs dès que possible (WSES 2019).')
 + quiz('Un patient a un BISAP à 3 à l’admission et une hypoxémie qui persiste à 60 heures malgré l’oxygène. Quel degré selon Atlanta 2012 ?',
   [('Légère', False), ('Modérément sévère', False), ('Sévère', True)],
   'Une défaillance d’organe qui persiste plus de 48 heures définit la forme sévère, quel que soit le score initial (Atlanta 2012, WSES 2019).')
 + key('BISAP dans les 24 heures ; hématocrite > 44 %, urée qui monte, CRP ≥ 150 mg/l au 3e jour ; défaillance d’organe : soins intensifs.')
 + src(WSES, ESGE))

C.a(7, 'Prise en charge initiale : liquides, analgésie, nutrition', P(
 'La gravité étant estimée, le traitement initial vise à préserver la microcirculation. Ainsi, la WSES 2019 recommande une ' + w('k85-remplissage', 'réanimation liquidienne précoce') + ' par cristalloïdes isotoniques, sans attendre l’aggravation hémodynamique ; l’ESGE 2018 propose du Ringer lactate, par exemple 5 à 10 ml/kg/h au début. Cependant, la surcharge liquidienne est délétère ; c’est pourquoi le débit est réévalué fréquemment, selon l’hémodynamique, la diurèse, l’hématocrite, l’urée, la créatinine et le lactate.',
 'Par ailleurs, la douleur doit être soulagée dans les 24 premières heures, selon une ' + w('k85-analgesie', 'analgésie multimodale') + ' ; en revanche, les AINS sont évités en cas d’insuffisance rénale aiguë. De plus, l’alimentation orale précoce est la règle dans la forme légère (WSES 2019). Enfin, dans la forme sévère qui ne tolère pas l’alimentation orale après 72 heures, l’ESGE 2018 recommande une ' + w('k85-nutrition', 'nutrition entérale') + ', d’abord par sonde nasogastrique ; la nutrition parentérale totale est évitée.')
 + alert('Aucun traitement pharmacologique spécifique n’a fait la preuve de son efficacité : seuls le support des organes et la nutrition sont indiqués (WSES 2019, grade 1B). De même, l’antibioprophylaxie systématique n’est pas recommandée (WSES 2019, grade 1A ; ESGE 2018, recommandation forte).', 'Ce qu’il ne faut pas faire.')
 + key('Cristalloïdes précoces, réévalués souvent ; analgésie dans les 24 heures ; alimentation orale précoce ; entérale si intolérance à 72 heures ; pas d’antibioprophylaxie.')
 + src(WSES, ESGE))

C.a(8, 'Pancréatite biliaire : CPRE et cholécystectomie', P(
 'Si la cause est biliaire, deux décisions s’ajoutent. D’abord, l’ESGE 2018 recommande une ' + w('k85-cpre', 'CPRE') + ' urgente, dans les 24 heures, avec drainage biliaire en cas d’' + w('k85-angiocholite', 'angiocholite') + ' associée (recommandation forte). De plus, en cas d’obstruction biliaire persistante, la CPRE est faite dans les 72 heures. En revanche, sans angiocholite ni obstruction, elle n’est pas indiquée, même si la pancréatite est prédite sévère (ESGE 2018 ; WSES 2019).',
 'Ensuite, la récidive doit être prévenue. Ainsi, dans la forme légère, la ' + w('k85-cholecystectomie', 'cholécystectomie laparoscopique') + ' est recommandée pendant la même hospitalisation (WSES 2019, grade 1A), même après une sphinctérotomie. À l’inverse, en présence de collections péripancréatiques, elle est différée jusqu’à leur résolution ou leur stabilisation.')
 + quiz('Une patiente a une pancréatite biliaire légère, sans angiocholite ; la bilirubine se normalise en 48 heures. Que faire ?',
   [('CPRE en urgence', False), ('Cholécystectomie laparoscopique pendant la même hospitalisation', True), ('Cholécystectomie à distance, après 3 mois', False)],
   'Sans angiocholite ni obstruction persistante, la CPRE n’est pas indiquée ; la cholécystectomie pendant la même hospitalisation prévient la récidive (WSES 2019, grade 1A).')
 + key('Angiocholite : CPRE dans les 24 heures ; obstruction persistante : dans les 72 heures ; sinon pas de CPRE. Forme légère : cholécystectomie pendant la même hospitalisation.')
 + src(ESGE, WSES))

C.a(9, 'Complications locales', P(
 'Au-delà de la première semaine, l’évolution est dominée par les complications locales, que la classification d’Atlanta révisée définit selon le délai et le contenu. Ainsi, avant 4 semaines, on distingue la ' + w('k85-apfc', 'collection liquidienne péripancréatique aiguë') + ', qui se résorbe habituellement seule, et la ' + w('k85-anc', 'collection nécrotique aiguë') + ', qui contient du liquide et de la nécrose. Après 4 semaines, ces collections s’entourent d’une paroi : elles deviennent respectivement un ' + w('k85-pseudokyste', 'pseudokyste') + ' et une ' + w('k85-won', 'nécrose organisée') + ' (« walled-off necrosis »).',
 'Par ailleurs, d’autres complications locales existent : syndrome du compartiment abdominal, obstruction de la vidange gastrique ou de la voie biliaire, thrombose des veines splénique et porte, nécrose colique, hémorragie majeure, ascite et épanchements pleuraux (ESGE 2018). De plus, une rupture du canal pancréatique principal peut isoler une partie de la glande : c’est le ' + w('k85-dpds', 'syndrome du canal déconnecté') + '.')
 + C.img('k85_pseudokyste_ct.gif', 'Scanner abdominal injecté en coupes axiale et coronale : volumineuse collection hypodense à paroi fine, au contact de la face postérieure de l’estomac.', 'Pseudokyste pancréatique au contact étroit de l’estomac, chez un homme de 50 ans ; cette relation anatomique a permis un drainage transgastrique.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Pankreaspseudozyste_mit_enger_Beziehung_zum_Magen_50M_-_CT_-_001.jpg'}))
 + key('Avant 4 semaines : collection liquidienne aiguë ou collection nécrotique aiguë ; après 4 semaines : pseudokyste ou nécrose organisée.')
 + src(ESGE, WSES, ATL))

C.a(10, 'Nécrose infectée : diagnostic et antibiotiques', P(
 'Parmi ces complications, la nécrose infectée est la plus redoutable. En effet, la mortalité atteint 35,2 % lorsque la nécrose infectée s’associe à une défaillance d’organe, contre 19,8 % pour une nécrose stérile avec défaillance (méta-analyse citée par la WSES 2019). Or, le diagnostic est difficile, car l’infection se distingue mal de l’inflammation propre à la pancréatite.',
 'C’est pourquoi on la suspecte devant une aggravation clinique, une fièvre ou une hausse des marqueurs inflammatoires après la première semaine, ou devant du gaz dans la collection au scanner. De plus, une ' + w('k85-pct', 'procalcitonine') + ' basse plaide fortement contre l’infection (WSES 2019). En revanche, la ponction à l’aiguille fine n’est plus systématique (ESGE 2018) ; elle est réservée aux cas où la clinique et l’imagerie restent ambiguës.',
 'Dès que l’infection est suspectée ou prouvée, des ' + w('k85-atb', 'antibiotiques') + ' qui pénètrent dans le pancréas sont indiqués : ainsi, carbapénèmes, quinolones et métronidazole ont une bonne pénétration, alors que les aminosides pénètrent mal (WSES 2019). Cependant, les carbapénèmes sont réservés aux patients très graves, en raison de la diffusion de Klebsiella pneumoniae résistante.')
 + key('Infection suspectée : aggravation après la 1re semaine, gaz dans la collection ; procalcitonine basse rassurante ; antibiotiques à bonne pénétration pancréatique ; ponction non systématique.')
 + src(WSES, ESGE))

C.a(11, 'Nécrose infectée : stratégie progressive', P(
 'Lorsque les antibiotiques ne suffisent pas, une intervention s’impose ; toutefois, son moment et sa forme ont changé. D’abord, l’ESGE 2018 propose de retarder la première intervention de 4 semaines si l’état du patient le permet, afin que la nécrose s’organise. En effet, la chirurgie différée au-delà de 4 semaines réduit la mortalité (WSES 2019, grade 2B).',
 'Ensuite, l’intervention suit une ' + w('k85-step-up', 'stratégie progressive') + ' (« step-up ») : un drainage endoscopique transmural ou percutané est fait en premier (ESGE 2018, recommandation forte), et il suffit à guérir l’infection chez 25 à 60 % des patients (WSES 2019). Par conséquent, la ' + w('k85-necrosectomie', 'nécrosectomie') + ' endoscopique ou mini-invasive n’est envisagée qu’en l’absence d’amélioration ; la chirurgie ouverte est la dernière option.')
 + C.img('k85_ct_exsudative.gif', 'Scanner abdominal injecté en coupe axiale : pancréas tuméfié entouré d’une large infiltration liquidienne péripancréatique.', 'Pancréatite aiguë exsudative au scanner, avec un épanchement liquidien étendu autour du pancréas ; c’est le scanner injecté, fait après 72 heures, qui évalue la nécrose et les collections.', credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Akute_exsudative_Pankreatitis_-_CT_axial.jpg'}))
 + key('Retarder l’intervention à 4 semaines si possible ; drainage endoscopique ou percutané d’abord ; nécrosectomie mini-invasive ensuite ; chirurgie ouverte en dernier.')
 + C.pareto('pareto-k85-clinique', 'Pancréatite aiguë', ['k85-1', 'k85-5', 'k85-6', 'k85-7', 'k85-8', 'k85-11'],
     ['Diagnostic : deux critères sur trois (douleur, lipase > 3 fois la normale, imagerie).',
      'Forme sévère : défaillance d’organe > 48 heures.',
      'Cristalloïdes précoces, réévalués souvent ; pas d’antibioprophylaxie.',
      'Angiocholite : CPRE dans les 24 heures ; sinon pas de CPRE de routine.',
      'Forme biliaire légère : cholécystectomie pendant l’hospitalisation.',
      'Nécrose infectée : différer, drainer, puis nécrosectomie mini-invasive.'])
 + src(ESGE, WSES))

C.a(12, 'Indications chirurgicales et suivi', P(
 'Au-delà de la stratégie progressive, la WSES 2019 retient des indications chirurgicales propres : le ' + w('k85-sca', 'syndrome du compartiment abdominal') + ' résistant au traitement conservateur, une hémorragie aiguë après échec de l’embolisation, une ischémie intestinale ou une cholécystite nécrosante, et une fistule digestive dans une collection. De plus, après 4 semaines, une défaillance d’organe persistante sans signe d’infection, une obstruction digestive ou biliaire par la nécrose, un syndrome du canal déconnecté ou un pseudokyste symptomatique justifient aussi une intervention ; après 8 semaines, une douleur persistante peut en être l’indication.',
 'Pour conclure, reprenons la patiente du début. Sa pancréatite est biliaire ; or, elle n’a ni angiocholite ni défaillance d’organe, et le BISAP vaut 1. Par conséquent, elle reçoit des cristalloïdes réévalués, une analgésie multimodale et une alimentation orale précoce ; dès lors, la cholécystectomie laparoscopique est faite avant sa sortie, ce qui prévient la récidive.')
 + key('Chirurgie : compartiment abdominal réfractaire, hémorragie après échec endovasculaire, ischémie, fistule. Après 4 semaines : défaillance persistante, obstruction, canal déconnecté, pseudokyste symptomatique.')
 + src(WSES))

C.a(13, 'Critères formels du diagnostic et paramètres clés', alert(
 '<p><b>Diagnostic.</b> Deux critères sur trois : douleur compatible ; lipase ou amylase > 3 fois la limite supérieure ; imagerie caractéristique. <b>Gravité (Atlanta 2012).</b> Légère : ni défaillance ni complication ; modérément sévère : défaillance < 48 h ou complication ; sévère : défaillance > 48 h. <b>Collections.</b> Avant 4 semaines : collection liquidienne ou nécrotique aiguë ; après : pseudokyste ou nécrose organisée.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> BISAP dans les 24 heures ; hématocrite > 44 % ; CRP ≥ 150 mg/l au 3e jour ; triglycérides > 11,3 mmol/l ; Ringer lactate 5 à 10 ml/kg/h au début, réévalué ; CPRE ≤ 24 h si angiocholite ; scanner injecté à 72-96 heures dans la forme sévère ; intervention différée à 4 semaines.</div>'
 + src(WSES, ESGE, ATL))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur moment importe autant que leur choix.')
 + table(['Question', 'Examen', 'Moment'], [
   ['Est-ce une pancréatite ?', w('k85-lipase', 'Lipase sérique'), 'Admission'],
   ['La cause est-elle biliaire ?', w('k85-echo', 'Échographie abdominale') + ', bilan hépatique', 'Admission ou 48 premières heures'],
   ['Quelle gravité prévoir ?', w('k85-bisap', 'BISAP') + ', hématocrite, urée, CRP', '24 heures, puis 48 à 72 heures'],
   ['Y a-t-il une nécrose ou une complication ?', w('k85-scanner', 'Scanner injecté'), '72 à 96 heures dans la forme sévère'],
   ['Calcul caché de la voie biliaire ?', w('k85-bilirm', 'Bili-IRM ou écho-endoscopie'), 'Si la cause reste inconnue'],
   ['La nécrose est-elle infectée ?', w('k85-pct', 'Procalcitonine') + ', scanner', 'Après la 1re semaine si aggravation']])
 + P('Le tableau se lit de haut en bas : ainsi, la lipase et l’échographie suffisent le premier jour, alors que le scanner n’apporte rien avant 72 heures, puisque la nécrose n’est pas encore visible.')
 + key('Lipase et échographie à l’admission ; scores à 24-48 heures ; scanner injecté à 72-96 heures si forme sévère ; bili-IRM ou écho-endoscopie si cause inconnue.')
 + src(WSES, ESGE))

C.e(2, 'Lire le scanner : index de sévérité', P(
 'Le scanner injecté est l’examen de référence pour le bilan morphologique ; toutefois, fait trop tôt, il ne montre pas la nécrose et ne modifie pas la conduite de la première semaine (WSES 2019). En revanche, après 4 jours, sa sensibilité pour la nécrose approche 100 %. Ainsi, l’' + w('k85-ctsi', 'index de sévérité scanographique') + ' de Balthazar additionne un grade de l’inflammation (0 à 4) et un score de nécrose (0 à 6).',
 'Par ailleurs, l’IRM est préférée en cas d’allergie au produit de contraste iodé, d’insuffisance rénale, de grossesse ou chez le sujet jeune ; de plus, elle caractérise mieux le contenu solide des collections, ce qui guide le drainage après 4 semaines (ESGE 2018). Cependant, elle détecte moins bien le gaz dans les collections.')
 + quiz('Le scanner à J4 montre un pancréas inflammatoire avec deux collections (grade E) et une nécrose de 40 % de la glande. Quel index de Balthazar ?',
   [('6', False), ('8', True), ('10', False)],
   'Grade E = 4 points ; nécrose de 30 à 50 % = 4 points ; l’index vaut donc 8, dans la tranche 7-10, associée à une morbidité de 92 % et une mortalité de 17 % (WSES 2019, tableau 3).')
 + key('Scanner injecté à 72-96 heures ; index de Balthazar = grade (0-4) + nécrose (0-6) ; IRM si contre-indication, grossesse, ou pour caractériser une collection.')
 + src(WSES, ESGE))

C.e(3, 'Biologie : diagnostic, gravité, étiologie', P(
 'La biologie répond à trois questions distinctes ; c’est pourquoi on ne l’interprète pas d’un seul bloc. D’abord, la lipase établit le diagnostic, mais son niveau ne dit rien de la gravité. Ensuite, l’hématocrite, l’urée, la créatinine et la CRP renseignent sur la gravité ; ainsi, l’ESGE 2018 retient une urée supérieure ou égale à 8,2 mmol/l à 48 heures comme prédicteur de défaillance d’organe persistante.',
 'Enfin, la biologie oriente l’étiologie : une cytolyse et une cholestase évoquent la cause biliaire ; de même, les triglycérides et la calcémie sont dosés en l’absence de lithiase et d’alcool. En revanche, après une pancréatite idiopathique, au moins deux échographies sont nécessaires, puis une écho-endoscopie à distance de l’épisode (WSES 2019).')
 + key('Lipase pour le diagnostic ; hématocrite, urée, CRP pour la gravité ; bilan hépatique, triglycérides et calcium pour la cause.')
 + C.pareto('pareto-k85-examens', 'Examens', ['k85-e-1', 'k85-e-2', 'k85-e-3'],
     ['Lipase > 3 fois la normale : diagnostic, pas gravité.',
      'Échographie à l’admission pour la lithiase.',
      'Scanner injecté à 72-96 heures, pas avant, dans la forme sévère.',
      'Index de Balthazar = inflammation (0-4) + nécrose (0-6).',
      'Cause inconnue : bili-IRM ou écho-endoscopie.'])
 + src(WSES, ESGE))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : pancréas et voies biliaires', P(
 'Le pancréas est rétropéritonéal, couché devant l’aorte et la veine cave, derrière l’estomac. Ainsi, une collection pancréatique refoule souvent la paroi postérieure de l’estomac, ce qui rend possible un drainage endoscopique transgastrique. De plus, le canal pancréatique principal et le canal cholédoque s’abouchent ensemble à la papille majeure ; par conséquent, un calcul enclavé dans l’ampoule peut obstruer les deux voies et déclencher la pancréatite biliaire. Enfin, la veine splénique longe la face postérieure du corps et de la queue, ce qui explique sa thrombose au cours des pancréatites sévères.')
 + key('Contact gastrique : drainage transgastrique ; papille commune : pancréatite biliaire ; veine splénique au contact : thrombose.', 'Science → clinique.'))
C.s('histo', 'Histologie', 'Histologie : acinus et nécrose', P(
 'Le pancréas exocrine est formé d’acini, dont les cellules stockent les enzymes sous forme de zymogènes inactifs. Or, dans la pancréatite, l’activation précoce de la trypsine dans l’acinus déclenche l’autodigestion. Dès lors, deux lésions s’observent : la nécrose du parenchyme et la cytostéatonécrose, où la lipase libère des acides gras qui se combinent au calcium. C’est pourquoi une hypocalcémie peut accompagner les formes étendues.')
 + key('Autodigestion de l’acinus et cytostéatonécrose : la nécrose visible au scanner a cette double origine.', 'Science → examen.'))
C.s('phys', 'Physiologie', 'Physiologie : fuite capillaire et défaillance d’organe', P(
 'La réponse inflammatoire systémique augmente la perméabilité capillaire ; ainsi, le plasma fuit vers le rétropéritoine, l’intestin et les plèvres. Par conséquent, la volémie efficace baisse et l’hématocrite monte par hémoconcentration. Ensuite, l’hypoperfusion touche le rein, le poumon et le pancréas lui-même, ce qui favorise la nécrose. En revanche, un remplissage excessif aggrave l’œdème, la pression intra-abdominale et l’hypoxémie.')
 + key('C’est pourquoi le remplissage doit être précoce mais réévalué : trop peu favorise la nécrose, trop favorise le compartiment abdominal.', 'Science → traitement.'))
C.s('micro', 'Microbiologie', 'Microbiologie : d’où vient l’infection de la nécrose ?', P(
 'Les germes de la nécrose infectée sont surtout des bacilles à Gram négatif d’origine digestive : Escherichia coli, Proteus, Klebsiella pneumoniae (WSES 2019). Ils atteignent la nécrose par translocation à travers une muqueuse intestinale lésée, mais aussi par voie hématogène, biliaire ou canalaire. De plus, des cocci à Gram positif, des anaérobies et parfois des Candida sont retrouvés ; cependant, la prophylaxie antifongique systématique n’est pas recommandée.')
 + key('Origine digestive des germes : c’est pourquoi la nutrition entérale, qui protège la barrière intestinale, est préférée à la voie parentérale.', 'Science → traitement.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, aucun ne traite la pancréatite elle-même. En pratique, le traitement associe donc des liquides, des antalgiques et, seulement en cas d’infection, des antibiotiques.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Cristalloïde isotonique', 'Ringer lactate', 'Réanimation initiale', w('k85-remplissage', 'Fiche')],
   ['Antalgique non opioïde', 'Métamizole (Novalgin®)', 'Analgésie multimodale', w('k85-d-metamizole', 'Monographie')],
   ['Opioïde', 'Hydromorphone (Palladon® Inject)', 'Douleur intense, analgésie contrôlée par le patient', w('k85-d-hydromorphone', 'Monographie')],
   ['Carbapénème', 'Méropénème (Meronem®)', 'Nécrose infectée grave seulement', w('k85-d-meropeneme', 'Monographie')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, l’antibiotique n’intervient qu’en cas d’infection prouvée ou suspectée, jamais en prophylaxie.')
 + key('Liquides et antalgiques pour tous ; antibiotiques pour la seule nécrose infectée ; aucun traitement spécifique.')
 + src(WSES, ESGE))

C.p(2, 'Doses et durées', P('Les doses suivantes proviennent des informations professionnelles suisses ; de plus, les recommandations de la WSES et de l’ESGE sont signalées.')
 + table(['Médicament', 'Situation', 'Dose', 'Source'], [
   ['Ringer lactate', 'Réanimation initiale', 'Par exemple 5 à 10 ml/kg/h au début, adapté et réévalué souvent', 'ESGE 2018'],
   ['Métamizole i.v.', 'Douleur aiguë sévère', '0,5 à 1 g lentement (max. 1 ml/min), toutes les 6 à 8 h ; max. 5 g/j', 'Information professionnelle Novalgin®'],
   ['Hydromorphone i.v.', 'Patient naïf d’opioïdes, ≥ 50 kg', '1 à 1,5 mg toutes les 3 à 4 h, injecté en 2 à 3 minutes ; perfusion 0,15 à 0,45 mg/h', 'Information professionnelle Palladon® Inject'],
   ['Hydromorphone, analgésie contrôlée par le patient i.v.', 'Douleur intense', 'Bolus de 0,2 mg, intervalle de sécurité de 5 à 10 minutes', 'Information professionnelle Palladon® Inject'],
   ['Méropénème i.v.', 'Infection intra-abdominale grave', '500 mg à 1 g toutes les 8 h ; adaptation à la fonction rénale', 'Information professionnelle Meronem®']])
 + P('Par exemple, chez un patient de 70 kg en forme sévère, le Ringer lactate peut débuter à environ 350 à 700 ml/h, puis le débit est réduit dès que la diurèse et l’hémodynamique se normalisent, car la surcharge aggrave le pronostic.')
 + trap('La WSES 2019 préfère l’hydromorphone à la morphine ou au fentanyl chez le patient non intubé ; aucune source suisse spécifique de l’analgésie de la pancréatite n’a été retrouvée. Le débit initial de Ringer lactate de l’ESGE 2018 est un exemple, et non une dose fixe.', 'Point à valider')
 + key('Ringer lactate réévalué ; métamizole 0,5 à 1 g toutes les 6 à 8 h ; hydromorphone titrée ou en analgésie contrôlée ; méropénème seulement si infection grave.')
 + src(FI('Novalgin® solution injectable'), FI('Palladon® Inject'), FI('Meronem® i.v.'), ESGE, WSES))

C.p(3, 'Interactions, surveillance et effets indésirables', alert(
 'Le métamizole peut provoquer une agranulocytose potentiellement mortelle, même après une utilisation antérieure sans problème ; de plus, son injection rapide expose à une chute tensionnelle ou à un choc, c’est pourquoi il est injecté lentement chez le patient allongé. Par ailleurs, l’hydromorphone expose à la dépression respiratoire ; l’antidote est la naloxone, 0,4 à 2 mg i.v.', 'Sécurité.')
 + P('Au cours du traitement, la surveillance porte d’abord sur la tolérance du remplissage : ainsi, la diurèse, la fréquence respiratoire, la saturation et la pression intra-abdominale sont suivies. Ensuite, les AINS sont évités en cas d’insuffisance rénale aiguë (WSES 2019). Enfin, les carbapénèmes sont réservés aux patients les plus graves ; en effet, leur usage large favorise les entérobactéries résistantes.')
 + key('Métamizole : agranulocytose et hypotension ; hydromorphone : dépression respiratoire, naloxone ; AINS évités si insuffisance rénale ; carbapénèmes épargnés.')
 + C.pareto('pareto-k85-pharma', 'Pharmacologie', ['k85-p-1', 'k85-p-2', 'k85-p-3'],
     ['Aucun traitement spécifique ; pas d’antibioprophylaxie.',
      'Cristalloïdes précoces, réévalués souvent.',
      'Analgésie multimodale dans les 24 heures.',
      'Méropénème 1 g toutes les 8 h si nécrose infectée grave.',
      'Métamizole : agranulocytose ; injection lente.'])
 + src(FI('Novalgin® solution injectable'), FI('Palladon® Inject'), FI('Meronem® i.v.'), WSES))

# ---------------- Fenêtres
L = lab
C.pop('k85-criteres', 'Critères diagnostiques (Atlanta 2012)', L(('Deux critères sur trois', '1. Douleur abdominale compatible ; 2. lipase ou amylase sériques > 3 fois la limite supérieure de la normale ; 3. signes caractéristiques à l’imagerie.'), ('Conséquence', 'Si 1 et 2 sont présents, l’imagerie n’est pas nécessaire au diagnostic.')) + src(WSES, ATL))
C.pop('k85-atlanta', 'Classification d’Atlanta révisée (2012)', L(('Légère', 'Ni défaillance d’organe ni complication locale ou systémique ; résolution habituelle en une semaine.'), ('Modérément sévère', 'Défaillance d’organe transitoire (< 48 h), complication locale ou systémique, ou décompensation d’une comorbidité.'), ('Sévère', 'Défaillance d’organe persistante (> 48 h), unique ou multiple.'), ('Phases', 'Précoce (1re semaine) puis tardive.')) + src(ATL, WSES))
C.pop('k85-defaillance', 'Défaillance d’organe', L(('Organes', 'Cardiovasculaire, respiratoire et rénal.'), ('Transitoire', 'Moins de 48 heures : forme au plus modérément sévère.'), ('Persistante', 'Plus de 48 heures : forme sévère ; risque de décès élevé, surtout si une nécrose infectée s’y associe.'), ('Conduite', 'Admission en soins intensifs dès que possible (WSES 2019, grade 1C).')) + src(WSES, ATL))
C.pop('k85-cpre', 'CPRE dans la pancréatite biliaire', L(('Urgente (≤ 24 h)', 'Angiocholite associée (ESGE 2018, recommandation forte).'), ('Dans les 72 h', 'Obstruction biliaire persistante.'), ('Non indiquée', 'Ni angiocholite ni obstruction, même si la pancréatite est prédite sévère (ESGE 2018 ; WSES 2019, grade 2B).')) + src(ESGE, WSES))
C.pop('k85-necrose-infectee', 'Nécrose infectée', L(('Fréquence', '20 à 40 % des formes sévères (WSES 2019).'), ('Pronostic', 'Mortalité 35,2 % si défaillance d’organe associée.'), ('Conduite', 'Antibiotiques, puis intervention différée et progressive.')) + src(WSES))
C.pop('k85-interstitielle', 'Pancréatite interstitielle œdémateuse', L(('Définition', 'Inflammation avec œdème diffus de la glande, rehaussement homogène au scanner, sans nécrose.'), ('Évolution', 'Habituellement favorable en une semaine ; une collection tardive devient un pseudokyste.')) + src(ATL, ESGE))
C.pop('k85-necrosante', 'Pancréatite nécrosante', L(('Définition', 'Nécrose du parenchyme pancréatique et/ou du tissu péripancréatique.'), ('Imagerie', 'Zones non rehaussées au scanner injecté, visibles de façon fiable après 72 heures.'), ('Évolution', 'Collection nécrotique aiguë, puis nécrose organisée après 4 semaines ; infection possible.')) + src(ESGE, WSES))
C.pop('k85-dbc', 'Classification fondée sur les déterminants', L(('Degrés', 'Légère ; modérée (nécrose stérile et/ou défaillance transitoire) ; sévère (nécrose infectée ou défaillance persistante) ; critique (les deux).'), ('Limite', 'Elle exige de connaître le statut de la nécrose, donc s’applique mal à la première semaine (ESGE 2018).')) + src(ESGE, WSES))
C.pop('k85-biliaire', 'Pancréatite biliaire', L(('Mécanisme', 'Calcul ou sludge qui migre et obstrue transitoirement l’ampoule de Vater.'), ('Indices', 'Lithiase vésiculaire à l’échographie, cytolyse et cholestase.'), ('Prévention', 'Cholécystectomie pendant la même hospitalisation si la forme est légère.')) + src(WSES))
C.pop('k85-tg', 'Hypertriglycéridémie', L(('Seuil', 'Triglycérides > 11,3 mmol/l (1000 mg/dl) : cause retenue (WSES 2019, grade 2C).'), ('Quand doser', 'En l’absence de lithiase et de consommation importante d’alcool, avec la calcémie.')) + src(WSES))
C.pop('k85-idiopathique', 'Pancréatite idiopathique', L(('Définition', 'Aucune cause après le bilan biologique et d’imagerie initial.'), ('Bilan', 'Au moins deux échographies ; puis scanner et écho-endoscopie à distance (microlithiase, tumeur, pancréatite chronique) ; IRM si l’écho-endoscopie est normale.')) + src(WSES))
C.pop('k85-cytosteatonecrose', 'Cytostéatonécrose', L(('Définition', 'Nécrose du tissu adipeux par la lipase pancréatique ; les acides gras libérés se combinent au calcium (saponification).'), ('Conséquence', 'Plages blanchâtres « en taches de bougie » à la chirurgie ; hypocalcémie possible.')))
C.pop('k85-cullen', 'Signes de Cullen et de Grey-Turner', L(('Cullen', 'Ecchymose péri-ombilicale.'), ('Grey-Turner', 'Ecchymose des flancs.'), ('Signification', 'Diffusion d’un épanchement hémorragique rétropéritonéal ; signes tardifs et inconstants.')))
C.pop('k85-lipase', 'Lipase sérique', L(('Seuil', '> 3 fois la limite supérieure de la normale.'), ('Avantages', 'Plus spécifique que l’amylase ; élévation plus prolongée (WSES 2019).'), ('Limites', 'Son niveau ne reflète pas la gravité ; élévations non pancréatiques possibles (insuffisance rénale, appendicite, cholécystite).')) + src(WSES))
C.pop('k85-echo', 'Échographie abdominale', L(('Moment', 'À l’admission ou dans les 48 premières heures.'), ('But', 'Rechercher une lithiase vésiculaire, un sludge, une dilatation des voies biliaires.'), ('Limite', 'Le pancréas est souvent mal vu à cause des gaz digestifs.')) + src(WSES))
C.pop('k85-bisap', 'Score BISAP', L(('Un point par critère', 'Urée > 8,9 mmol/l ; troubles de la conscience ; syndrome de réponse inflammatoire systémique ; âge > 60 ans ; épanchement pleural à la radiographie.'), ('Usage', 'Dans les 24 premières heures ; prédit gravité, défaillance d’organe et décès (WSES 2019 ; ESGE 2018, recommandation faible).')) + src(WSES, ESGE))
C.pop('k85-hematocrite', 'Hématocrite', L(('Seuil', '> 44 % : facteur de risque indépendant de nécrose (WSES 2019, grade 1B).'), ('Mécanisme', 'Hémoconcentration par fuite capillaire.'), ('Suivi', 'Sa baisse sous remplissage est un objectif de perfusion.')) + src(WSES))
C.pop('k85-crp', 'CRP', L(('Seuil', '≥ 150 mg/l au 3e jour : facteur pronostique de forme sévère (WSES 2019, grade 2A).'), ('Limite', 'Retard d’ascension : peu utile à l’admission.')) + src(WSES))
C.pop('k85-remplissage', 'Réanimation liquidienne', L(('Principe', 'Précoce, sans attendre l’aggravation hémodynamique, par cristalloïdes isotoniques (WSES 2019, grade 1B).'), ('Débit', 'Par exemple Ringer lactate 5 à 10 ml/kg/h au début (ESGE 2018), adapté au patient.'), ('Surveillance', 'Hémodynamique, diurèse, hématocrite, urée, créatinine, lactate ; éviter la surcharge.')) + src(WSES, ESGE))
C.pop('k85-analgesie', 'Analgésie multimodale', L(('Règle', 'Toute pancréatite reçoit une analgésie dans les 24 premières heures (WSES 2019).'), ('Moyens', 'Antalgiques non opioïdes, opioïdes, analgésie péridurale ou contrôlée par le patient.'), ('Prudence', 'AINS évités en cas d’insuffisance rénale aiguë.')) + src(WSES))
C.pop('k85-nutrition', 'Nutrition dans la pancréatite aiguë', L(('Forme légère', 'Alimentation orale précoce.'), ('Forme sévère', 'Nutrition entérale polymérique si l’alimentation orale n’est pas tolérée après 72 heures (ESGE 2018, recommandation forte).'), ('Voie', 'Sonde nasogastrique d’abord, nasojéjunale en cas d’intolérance ; parentérale si échec ou objectif calorique non atteint.')) + src(ESGE, WSES))
C.pop('k85-angiocholite', 'Angiocholite', L(('Définition', 'Infection de la voie biliaire obstruée.'), ('Clinique', 'Douleur, fièvre, ictère.'), ('Conduite', 'Antibiotiques et drainage biliaire par CPRE dans les 24 heures.')) + src(ESGE))
C.pop('k85-cholecystectomie', 'Cholécystectomie après pancréatite biliaire', L(('Forme légère', 'Pendant la même hospitalisation (WSES 2019, grade 1A), même après sphinctérotomie (grade 1B).'), ('Collections', 'Différée jusqu’à leur résolution ou stabilisation (grade 2C).')) + src(WSES))
C.pop('k85-apfc', 'Collection liquidienne péripancréatique aiguë', L(('Délai', 'Moins de 4 semaines, dans une pancréatite interstitielle.'), ('Aspect', 'Liquide sans paroi définie.'), ('Évolution', 'Résorption spontanée habituelle ; pas de drainage.')) + src(ESGE, ATL))
C.pop('k85-anc', 'Collection nécrotique aiguë', L(('Délai', 'Moins de 4 semaines, dans une pancréatite nécrosante.'), ('Contenu', 'Liquide et nécrose en proportions variables.'), ('Évolution', 'Nécrose organisée après 4 semaines.')) + src(ESGE, WSES))
C.pop('k85-pseudokyste', 'Pseudokyste pancréatique', L(('Définition', 'Collection liquidienne entourée d’une paroi bien définie, sans matériel solide, après au moins 4 semaines d’une pancréatite interstitielle.'), ('Traitement', 'Drainage seulement s’il est symptomatique ou s’il grossit (WSES 2019).')) + src(ESGE, WSES))
C.pop('k85-won', 'Nécrose organisée (walled-off necrosis)', L(('Définition', 'Collection encapsulée de nécrose partiellement liquéfiée, après au moins 4 semaines.'), ('Traitement', 'Drainage si infection ou symptômes ; endoscopique ou percutané en premier.')) + src(ESGE, WSES))
C.pop('k85-dpds', 'Syndrome du canal déconnecté', L(('Définition', 'Rupture du canal pancréatique principal qui isole un segment de glande encore sécrétant.'), ('Conséquence', 'Collection récidivante ; indication d’intervention s’il est symptomatique (WSES 2019).')) + src(WSES, ESGE))
C.pop('k85-pct', 'Procalcitonine', L(('Usage', 'Test biologique le plus sensible pour détecter l’infection de la nécrose ; une valeur basse est un fort argument contre (WSES 2019, grade 2A).'), ('Limite', 'Ne remplace pas la clinique et l’imagerie.')) + src(WSES))
C.pop('k85-atb', 'Antibiotiques dans la nécrose infectée', L(('Indication', 'Infection suspectée ou prouvée ; jamais en prophylaxie.'), ('Pénétration pancréatique', 'Bonne : carbapénèmes, quinolones, métronidazole ; intermédiaire : pipéracilline-tazobactam, céphalosporines de 3e génération ; mauvaise : aminosides.'), ('Épargne', 'Quinolones si allergie aux bêtalactamines ; carbapénèmes chez les patients très graves.')) + src(WSES))
C.pop('k85-step-up', 'Stratégie progressive (step-up)', L(('Étape 1', 'Antibiotiques et support des organes ; attendre l’organisation de la nécrose (environ 4 semaines).'), ('Étape 2', 'Drainage endoscopique transmural ou percutané.'), ('Étape 3', 'Nécrosectomie endoscopique ou chirurgie mini-invasive si absence d’amélioration.'), ('Résultat', 'Le drainage seul guérit 25 à 60 % des patients (WSES 2019, grade 1A).')) + src(ESGE, WSES))
C.pop('k85-necrosectomie', 'Nécrosectomie', L(('Endoscopique', 'Ablation de la nécrose à travers une prothèse transgastrique.'), ('Chirurgicale mini-invasive', 'Débridement rétropéritonéal vidéo-assisté.'), ('Comparaison', 'Moins de défaillances d’organe nouvelles que la chirurgie ouverte, mais plus de gestes (WSES 2019, grade 1B).')) + src(WSES, ESGE))
C.pop('k85-sca', 'Syndrome du compartiment abdominal', L(('Définition', 'Hyperpression intra-abdominale soutenue avec défaillance d’organe nouvelle.'), ('Traitement', 'Mesures conservatrices d’abord ; laparotomie de décompression si elles échouent (WSES 2019).')) + src(WSES))
C.pop('k85-scanner', 'Scanner injecté', L(('Moment', '72 à 96 heures après le début dans la forme sévère (WSES 2019, grade 1C) ; plus tôt seulement si le diagnostic est douteux.'), ('Apport', 'Nécrose, collections, complications vasculaires.'), ('Limite', 'Scanners répétés : irradiation, peu d’effet sur la décision.')) + src(WSES, ESGE))
C.pop('k85-bilirm', 'Bili-IRM et écho-endoscopie', L(('Indication', 'Rechercher un calcul caché de la voie biliaire principale si l’échographie est négative et la cause inconnue.'), ('Avantage', 'Évitent une CPRE diagnostique, invasive (WSES 2019).')) + src(WSES))
C.pop('k85-ctsi', 'Index de sévérité scanographique (Balthazar)', L(('Grade', 'A pancréas normal 0 ; B augmentation de volume 1 ; C inflammation et/ou graisse péripancréatique 2 ; D une collection 3 ; E ≥ 2 collections et/ou air rétropéritonéal 4.'), ('Nécrose', 'Aucune 0 ; < 30 % 2 ; 30 à 50 % 4 ; > 50 % 6.'), ('Pronostic', 'Index 7-10 : morbidité 92 %, mortalité 17 %.')) + src(WSES))
C.pop('k85-d-metamizole', 'Métamizole (Novalgin®)', L(('Dose i.v. adulte', '0,5 à 1 g lentement (max. 1 ml/min), répétable toutes les 6 à 8 h ; max. 5 g/j.'), ('Risques', 'Agranulocytose potentiellement mortelle ; hypotension, choc en injection rapide.'), ('Contre-indication', 'Antécédent d’agranulocytose aux pyrazolones.')) + src(FI('Novalgin® solution injectable')))
C.pop('k85-d-hydromorphone', 'Hydromorphone (Palladon® Inject)', L(('Dose i.v.', 'Adulte naïf d’opioïdes ≥ 50 kg : 1 à 1,5 mg toutes les 3 à 4 h en 2 à 3 minutes ; perfusion 0,15 à 0,45 mg/h.'), ('Analgésie contrôlée', 'Bolus de 0,2 mg, intervalle de 5 à 10 minutes.'), ('Surdosage', 'Naloxone 0,4 à 2 mg i.v.')) + src(FI('Palladon® Inject'), WSES))
C.pop('k85-d-meropeneme', 'Méropénème (Meronem®)', L(('Indication suisse', 'Infections sévères, dont intra-abdominales et sepsis.'), ('Dose', '500 mg à 1 g i.v. toutes les 8 h (1,5 à 6 g/j) ; adaptation rénale.'), ('Place', 'Nécrose infectée chez le patient très grave ; épargne des carbapénèmes (WSES 2019).')) + src(FI('Meronem® i.v.'), WSES))
C.pop('k85-sirs', 'Syndrome de réponse inflammatoire systémique', L(('Critères', 'Au moins deux parmi : température anormale, tachycardie, polypnée ou hypocapnie, leucocytose ou leucopénie.'), ('Valeur', 'Critère du score BISAP ; sa persistance annonce la défaillance d’organe.')) + src(WSES))
C.pop('k85-ringer', 'Ringer lactate', L(('Nature', 'Cristalloïde isotonique balancé.'), ('Place', 'Proposé par l’ESGE 2018 ; supériorité sur le sérum physiologique faiblement démontrée (WSES 2019).')) + src(ESGE, WSES))

C.termes = [
 (r'Ringer lactate', 'k85-ringer'), (r'réponse inflammatoire systémique', 'k85-sirs'), (r'BISAP', 'k85-bisap'), (r'CPRE', 'k85-cpre'),
 (r'lipase', 'k85-lipase'), (r'procalcitonine', 'k85-pct'), (r'pseudokyste', 'k85-pseudokyste'), (r'nécrose organisée', 'k85-won'),
 (r'collection nécrotique aiguë', 'k85-anc'), (r'angiocholite', 'k85-angiocholite'), (r'cholécystectomie', 'k85-cholecystectomie'),
 (r'défaillance d’organe persistante', 'k85-defaillance'), (r'nécrose infectée', 'k85-necrose-infectee'), (r'cytostéatonécrose', 'k85-cytosteatonecrose'),
 (r'hypertriglycéridémie', 'k85-tg'), (r'métamizole', 'k85-d-metamizole'), (r'hydromorphone', 'k85-d-hydromorphone'), (r'méropénème', 'k85-d-meropeneme'),
 (r'carbapénèmes', 'k85-atb'), (r'écho-endoscopie', 'k85-bilirm'), (r'Bili-IRM|bili-IRM', 'k85-bilirm'), (r'scanner injecté', 'k85-scanner'),
 (r'syndrome du compartiment abdominal|compartiment abdominal', 'k85-sca'), (r'canal déconnecté', 'k85-dpds'), (r'nécrosectomie', 'k85-necrosectomie'),
 (r'Balthazar', 'k85-ctsi'), (r'Atlanta', 'k85-atlanta'), (r'nutrition entérale', 'k85-nutrition'), (r'hématocrite', 'k85-hematocrite'), (r'CRP', 'k85-crp'),
]

C.write()
