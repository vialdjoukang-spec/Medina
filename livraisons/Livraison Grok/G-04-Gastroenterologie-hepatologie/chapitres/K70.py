import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K70', 'Maladie alcoolique du foie',
    'K70 — Maladie alcoolique du foie · CIM-10-GM 2024 · Foie',
    'Adulte · stéatose, hépatite alcoolique, fibrose et cirrhose alcooliques, trouble de l’usage d’alcool · rédaction du 09.10.2026 · référentiels EASL maladie alcoolique du foie 2018, Baveno VII (2022), informations professionnelles suisses',
    'Pharmacologie de la maladie alcoolique du foie')
w = C.w
ALD = ('EASL Clinical Practice Guidelines: Management of alcohol-related liver disease, J Hepatol 2018;69:154-181', 'https://easl.eu/wp-content/uploads/2018/10/EASL-CPG-Mgmt-ALD.pdf')
BAV = ('de Franchis R. et al., Baveno VII — Renewing consensus in portal hypertension, J Hepatol 2022;76:959-974', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11090185/')
STOP = ('Thursz M. R. et al., Prednisolone or pentoxifylline for alcoholic hepatitis (STOPAH), N Engl J Med 2015;372:1619-1628', 'https://doi.org/10.1056/NEJMoa1412278')
MDF = ('Carithers R. L. et al., Methylprednisolone therapy in patients with severe alcoholic hepatitis, Ann Intern Med 1989;110:685-690 (fonction discriminante modifiée)', 'https://doi.org/10.7326/0003-4819-110-9-685')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 48 ans, qui boit environ une bouteille de vin par jour depuis quinze ans, consulte pour un ictère apparu en trois semaines, avec fièvre modérée et amaigrissement. Or, elle n’a ni douleur biliaire ni prise de paracétamol. <b>La question est donc de savoir s’il s’agit d’une ' + w('k70-ha', 'hépatite alcoolique') + ', si elle est sévère, et s’il faut la traiter par corticoïdes.</b>',
 'Pour y répondre, le médecin doit savoir : quantifier la consommation et dépister le ' + w('k70-tua', 'trouble de l’usage d’alcool') + ' ; distinguer stéatose, hépatite alcoolique et cirrhose ; mesurer la gravité par la ' + w('k70-mdf', 'fonction discriminante de Maddrey') + ' ou le ' + w('k70-meld', 'score MELD') + ' ; décider d’une corticothérapie et juger la réponse au septième jour par le ' + w('k70-lille', 'score de Lille') + ' ; enfin, organiser l’abstinence, qui détermine le pronostic à long terme.')
 + key('Ictère récent chez un buveur excessif : penser hépatite alcoolique, mesurer la gravité, rechercher l’infection, puis décider.', 'Point de départ.'))

C.a(1, 'Définition et spectre lésionnel', P(
 'La maladie alcoolique du foie regroupe les lésions hépatiques causées par une consommation excessive et prolongée d’alcool. Ainsi, l’EASL 2018 décrit un spectre qui va de la ' + w('k70-steatose', 'stéatose') + ' pure à la ' + w('k70-sha', 'stéatohépatite alcoolique') + ', puis à la fibrose progressive, à la cirrhose et au carcinome hépatocellulaire. En outre, ces lésions coexistent souvent chez un même patient, si bien que le diagnostic clinique ne suffit pas toujours à les séparer.',
 'Parmi ces formes, l’' + w('k70-ha', 'hépatite alcoolique') + ' occupe une place à part. En effet, c’est un syndrome clinique d’ictère d’apparition récente, sous-tendu par une stéatohépatite, qui peut survenir sur un foie déjà cirrhotique. Par conséquent, la CIM-10-GM distingue la stéatose (K70.0), l’hépatite alcoolique (K70.1), la fibrose (K70.2), la cirrhose (K70.3), l’insuffisance hépatique alcoolique (K70.4) et la forme non précisée (K70.9).')
 + table(['Forme', 'Lésion dominante', 'Réversibilité'], [
   ['Stéatose (K70.0)', 'Vacuoles lipidiques dans les hépatocytes', 'Réversible en quelques semaines d’abstinence'],
   ['Hépatite alcoolique (K70.1)', 'Ballonnisation, corps de Mallory-Denk, polynucléaires', 'Partielle ; mortalité précoce si forme sévère'],
   ['Fibrose (K70.2) et cirrhose (K70.3)', 'Fibrose périveinulaire puis septa et nodules', 'Fibrose partiellement réversible ; cirrhose au mieux stabilisée']])
 + P('Le tableau se lit de haut en bas : en effet, chaque forme ajoute une lésion à la précédente, et la réversibilité diminue en conséquence.')
 + key('Stéatose → stéatohépatite → fibrose → cirrhose → carcinome hépatocellulaire ; l’hépatite alcoolique est un syndrome aigu possible à chaque stade.')
 + src(ALD))

C.a(2, 'Seuils de consommation et facteurs de risque', P(
 'Après la définition, il faut quantifier l’exposition. Ainsi, selon l’EASL 2018, le risque de maladie alcoolique du foie augmente au-delà de 30 g d’alcool par jour, ou au-delà de 7 unités par semaine chez la femme et de 14 unités chez l’homme ; de plus, à 100 g par jour, le risque relatif atteint 26. Par ailleurs, le diagnostic est évoqué dès une consommation régulière de plus de 20 g par jour chez la femme et de plus de 30 g par jour chez l’homme, associée à des anomalies cliniques ou biologiques hépatiques.',
 'Cependant, tous les buveurs excessifs ne développent pas une maladie grave. En effet, environ 90 % d’entre eux ont une stéatose, mais une minorité seulement évolue vers la cirrhose. C’est pourquoi l’EASL insiste sur les cofacteurs : sexe féminin, obésité et insulinorésistance, tabagisme, surcharge en fer, hépatites virales et variants du gène ' + w('k70-pnpla3', 'PNPLA3') + '. En outre, l’hépatite alcoolique survient en général après des décennies de consommation lourde, supérieure à 80 g par jour.')
 + trap('Une unité standard ne contient pas la même quantité d’alcool selon les pays ; la source EASL ne précise pas la valeur retenue. Le calcul en grammes (volume en ml × degré × 0,8 / 100) évite cette ambiguïté.', 'Piège des unités')
 + key('Le risque apparaît au-delà de 30 g/j, et l’on évoque le diagnostic au-delà de 20 g/j chez la femme ou de 30 g/j chez l’homme en présence d’anomalies hépatiques. Le sexe féminin, l’obésité, le tabac, le fer, les virus et PNPLA3 aggravent le risque.')
 + src(ALD))

C.a(3, 'Physiopathologie', P(
 'Pour comprendre ces seuils, il faut suivre le métabolisme de l’éthanol. D’abord, l’alcool déshydrogénase puis l’aldéhyde déshydrogénase oxydent l’éthanol en acétaldéhyde, puis en acétate ; or, cette oxydation consomme du NAD⁺ et favorise la synthèse d’acides gras, d’où la stéatose. Ensuite, l’induction du cytochrome CYP2E1 produit des espèces réactives de l’oxygène ; de plus, l’éthanol épuise les antioxydants, notamment le glutathion.',
 'Par conséquent, le stress oxydatif et l’acétaldéhyde lèsent l’hépatocyte. En outre, l’alcool augmente la perméabilité intestinale, et les endotoxines bactériennes activent les cellules de Kupffer, qui libèrent des cytokines et attirent les polynucléaires neutrophiles. Enfin, les cellules étoilées activées produisent du collagène autour des veinules centrolobulaires : c’est pourquoi la fibrose alcoolique débute typiquement dans la région périveinulaire.')
 + key('L’éthanol devient de l’acétaldéhyde, produit un excès de NADH et un stress oxydatif par le CYP2E1, et laisse passer des endotoxines ; il en résulte une stéatose, une inflammation neutrophile et une fibrose périveinulaire.')
 + src(ALD))

C.a(4, 'Présentation clinique', P(
 'La présentation dépend donc du stade. Ainsi, la stéatose est le plus souvent asymptomatique et découverte devant des enzymes hépatiques anormales ; de même, une fibrose avancée peut exister avec des tests hépatiques normaux. En revanche, l’hépatite alcoolique se manifeste par un ' + w('k70-ictere', 'ictère') + ' progressif, souvent associé à de la fièvre, même sans infection, à un malaise, à un amaigrissement et à une dénutrition (EASL 2018).',
 'De plus, l’examen recherche les signes de cirrhose et d’hypertension portale, ainsi que les atteintes extrahépatiques de l’alcool. En effet, l’alcool touche aussi le cœur, le pancréas, le rein et le système nerveux. Par conséquent, un trouble de la conscience chez ce patient évoque une encéphalopathie hépatique, mais aussi une ' + w('k70-wernicke', 'encéphalopathie de Wernicke') + ' ou un ' + w('k70-sevrage', 'syndrome de sevrage') + ', qui doivent être écartés.')
 + C.img('k70_ictere.gif', 'Photographie rapprochée d’un œil dont la sclère est franchement jaune.', 'Ictère conjonctival. Dans l’hépatite alcoolique, c’est le signe cardinal : un ictère d’apparition récente chez un buveur excessif doit faire évoquer le diagnostic (EASL 2018).', credit({'auteur': 'CDC / Dr Thomas F. Sellers, Emory University ; travail dérivé : த.உழவன்', 'licence': 'domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Jaundice_eye_new.jpg'}))
 + key('La stéatose et la fibrose restent souvent muettes. L’hépatite alcoolique donne un ictère récent, une fièvre et une dénutrition. Un trouble de conscience évoque une encéphalopathie hépatique, une encéphalopathie de Wernicke ou un sevrage.')
 + src(ALD))

C.a(5, 'Dépister le trouble de l’usage d’alcool', P(
 'Avant toute décision hépatologique, il faut nommer et évaluer la consommation. Ainsi, l’EASL recommande le terme de ' + w('k70-tua', 'trouble de l’usage d’alcool') + ', défini par le DSM-5, plutôt que les termes stigmatisants d’« alcoolique » ou d’« abus ». De plus, le questionnaire ' + w('k70-audit', 'AUDIT') + ' ou sa version courte AUDIT-C doit servir au dépistage (grade A1), et le patient doit être examiné à la recherche de troubles psychiatriques et d’autres addictions.',
 'Par ailleurs, les marqueurs biologiques complètent l’entretien. En effet, la GGT, le volume globulaire moyen et la ' + w('k70-cdt', 'transferrine carboxy-déficiente') + ' sont des marqueurs indirects ; en revanche, l’' + w('k70-etg', 'éthylglucuronide') + ' urinaire ou capillaire est un marqueur direct qui permet de vérifier l’abstinence (grade A2). Enfin, le patient dépisté reçoit une intervention brève et est adressé à une équipe multidisciplinaire (grade A1).')
 + quiz('Quel marqueur permet de documenter une abstinence sur plusieurs mois ?',
   [('GGT sérique', False), ('Éthylglucuronide dans les cheveux', True), ('ALAT sérique', False)],
   'L’éthylglucuronide capillaire reflète la consommation sur une fenêtre allant jusqu’à environ six mois ; l’urinaire, sur environ 80 heures (EASL 2018, tableau 5).')
 + key('Le terme correct est trouble de l’usage d’alcool (DSM-5). On le dépiste par l’AUDIT ou l’AUDIT-C, et l’on vérifie l’abstinence par l’éthylglucuronide urinaire ou capillaire. Il se traite par une intervention brève et une équipe multidisciplinaire.')
 + src(ALD))

C.a(6, 'Démarche diagnostique de l’atteinte hépatique', P(
 'Une fois la consommation établie, il reste à mesurer l’atteinte hépatique. Ainsi, le bilan comporte la GGT, l’ALAT et l’ASAT, mais aussi un test de fibrose, par exemple l’' + w('k70-elasto', 'élastographie impulsionnelle') + ', car une fibrose avancée peut coexister avec des tests normaux (grade A1). De plus, toute anomalie conduit à une échographie, et d’autres causes sont recherchées : sérologies des hépatites B et C, ferritine et saturation de la transferrine notamment.',
 'Cependant, l’alcool ne s’affirme pas par l’imagerie, qui ne sert qu’à décrire la stéatose, la cirrhose et ses complications. C’est pourquoi la ' + w('k70-biopsie', 'biopsie hépatique') + ' est requise en cas d’incertitude diagnostique, pour un stadage précis ou dans les essais (grade A1). En outre, si une cirrhose est présente, la recherche de varices suit les critères de Baveno, et une surveillance clinique, biologique et échographique est instaurée.')
 + C.img('k70_steatose.gif', 'Coupe histologique de foie colorée : nombreux hépatocytes remplis de grandes vacuoles claires et amas éosinophiles irréguliers dans certains hépatocytes.', 'Biopsie hépatique dans une maladie alcoolique : stéatose macrovacuolaire (vacuoles claires) et hyalin de Mallory (inclusions éosinophiles), sur un foie cirrhotique.', credit({'auteur': 'Ed Uthman', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Mallorys_Hyalin_in_Alcoholic_Liver_Disease_(2632109950).jpg'}))
 + key('Tout buveur excessif reçoit des tests hépatiques et un test de fibrose ; une anomalie conduit à une échographie et à la recherche de causes associées, et la biopsie sert en cas de doute ou de stadage nécessaire.')
 + src(ALD, BAV))

C.a(7, 'Reconnaître l’hépatite alcoolique', P(
 'Parmi les atteintes, l’hépatite alcoolique est la plus urgente. Ainsi, un ictère récent chez un buveur excessif doit la faire suspecter (grade A1). De plus, la biologie typique associe une polynucléose neutrophile, une bilirubine supérieure à 50 µmol/l et une ASAT supérieure à deux fois la normale, rarement au-delà de 300 UI/l, avec un rapport ASAT/ALAT habituellement supérieur à 1,5-2 (EASL 2018).',
 'Cependant, ce tableau peut aussi résulter d’un sepsis, d’une atteinte médicamenteuse ou d’une migration lithiasique. C’est pourquoi, en cas de doute, une ' + w('k70-biopsie', 'biopsie hépatique') + ' par voie transjugulaire confirme le diagnostic ; en effet, elle découvre un autre diagnostic dans 10 à 20 % des cas. Par conséquent, des transaminases très élevées, au-delà de 300 UI/l, doivent faire chercher une autre cause, notamment une hépatite virale, ischémique ou médicamenteuse.')
 + C.img('k70_hepatite.gif', 'Coupe histologique de foie en coloration hématoxyline-éosine : hépatocytes ballonnisés, vacuoles graisseuses et inclusions éosinophiles entourées de polynucléaires.', 'Hépatite alcoolique, coloration hématoxyline-éosine : stéatose, nécrose hépatocytaire et corps de Mallory-Denk, inclusions éosinophiles des hépatocytes ballonnisés.', credit({'auteur': 'Countincr (Wikipédia en anglais), image PEIR, université d’Alabama à Birmingham', 'licence': 'CC BY-SA 2.5', 'url': 'https://commons.wikimedia.org/wiki/File:Alcoholic_hepatitis.jpg'}))
 + quiz('Une patiente buveuse a un ictère, une bilirubine à 180 µmol/l et une ASAT à 1 450 UI/l. Que penser ?',
   [('Hépatite alcoolique typique', False), ('Valeur inhabituelle : chercher une autre cause (virale, ischémique, médicamenteuse)', True), ('Stéatose simple', False)],
   'Dans l’hépatite alcoolique, l’ASAT dépasse rarement 300 UI/l (EASL 2018) ; une cytolyse massive oriente vers une autre cause, comme une intoxication au paracétamol ou une hépatite virale.')
 + key('Un buveur excessif a un ictère récent, une bilirubine > 50 µmol/l et des ASAT > 2 × la normale, mais rarement > 300 UI/l, avec un rapport ASAT/ALAT > 1,5-2. En cas de doute, on fait une biopsie transjugulaire, car elle reste possible malgré les troubles de la coagulation.')
 + src(ALD))

C.a(8, 'Évaluer la gravité de l’hépatite alcoolique', P(
 'Le diagnostic posé, la décision dépend de la gravité. Ainsi, les scores pronostiques doivent être utilisés pour identifier les formes sévères (grade A1). En effet, une ' + w('k70-mdf', 'fonction discriminante de Maddrey') + ' d’au moins 32 définit l’hépatite alcoolique sévère et sert habituellement de seuil de traitement ; à l’inverse, une forme non sévère (inférieure à 32) a une mortalité à un mois inférieure à 10 %.',
 'De plus, d’autres scores sont validés : le ' + w('k70-meld', 'score MELD') + ', le ' + w('k70-gahs', 'score de Glasgow') + ' et le score ' + w('k70-abic', 'ABIC') + '. Par exemple, une fonction de Maddrey d’au moins 32 associée à un score de Glasgow d’au moins 9 désigne un mauvais pronostic et un bénéfice des corticoïdes à 84 jours. Toutefois, ces scores reposent largement sur les mêmes variables et prédisent la survie à court terme avec une efficacité comparable (EASL 2018).')
 + key('La forme est sévère si le Maddrey est ≥ 32 (ou selon le MELD, le Glasgow ou l’ABIC). Sous 32, la mortalité à un mois est < 10 %. Un Glasgow ≥ 9 avec un Maddrey ≥ 32 désigne les patients qui bénéficient des corticoïdes.')
 + src(ALD, MDF))

C.a(9, 'Traiter l’hépatite alcoolique sévère', P(
 'En cas de forme sévère, la corticothérapie se discute. Ainsi, en l’absence d’infection active, la ' + w('k70-d-prednisolone', 'prednisolone') + ' 40 mg/j ou la méthylprednisolone 32 mg/j doivent être envisagées pour réduire la mortalité à court terme (grade A1), pendant 28 jours. Cependant, l’essai ' + w('k70-stopah', 'STOPAH') + ' n’a montré qu’une réduction limite de la mortalité à 28 jours, et aucun bénéfice au-delà d’un mois ; c’est pourquoi l’EASL précise que les corticoïdes n’influencent pas la survie à moyen et long terme.',
 'De plus, la ' + w('k70-d-nac', 'N-acétylcystéine') + ' intraveineuse pendant cinq jours peut être associée aux corticoïdes (grade B2). Par ailleurs, l’infection doit être recherchée systématiquement avant le traitement, pendant la corticothérapie et au cours du suivi (grade A1), car les corticoïdes exposent au sepsis et à l’hémorragie digestive. Enfin, une ' + w('k70-nutrition', 'évaluation nutritionnelle') + ' vise un apport d’au moins 35 à 40 kcal/kg et de 1,2 à 1,5 g/kg de protéines par jour, par voie orale en première intention (grade A2).')
 + alert('Avant toute corticothérapie : hémocultures, examen d’urine, radiographie thoracique et ponction d’ascite si présente. Une infection active contre-indique le traitement tant qu’elle n’est pas contrôlée.', 'Infection d’abord.')
 + key('Dans la forme sévère sans infection active, on donne de la prednisolone 40 mg/j (ou de la méthylprednisolone 32 mg/j) pendant 28 jours, éventuellement avec de la N-acétylcystéine IV pendant 5 jours. Le patient reçoit 35-40 kcal/kg/j et 1,2-1,5 g/kg/j de protéines, et l’on dépiste les infections de façon répétée.')
 + src(ALD, STOP))

C.a(10, 'Juger la réponse au septième jour', P(
 'Une fois les corticoïdes débutés, la réponse doit être mesurée tôt. Ainsi, le ' + w('k70-lille', 'score de Lille') + ', calculé au septième jour à partir des données initiales et de l’évolution de la bilirubine, varie de 0 à 1 ; un score d’au moins 0,45 indique une absence de réponse. De plus, trois profils ont été décrits : répondeurs complets (au plus 0,16), répondeurs partiels (0,16 à 0,56) et non-répondeurs nuls (au moins 0,56).',
 'Par conséquent, des règles strictes d’arrêt doivent être appliquées dès le septième jour (grade A1), et les corticoïdes sont interrompus en particulier chez le non-répondeur nul. En revanche, chez le répondeur, la prednisolone est poursuivie jusqu’au 28e jour, puis arrêtée d’un coup ou diminuée sur trois semaines. Enfin, chez le non-répondeur très sélectionné, une ' + w('k70-tx', 'transplantation hépatique précoce') + ' doit être discutée (grade A1).')
 + quiz('Au septième jour de prednisolone, le score de Lille vaut 0,62. Que faire ?',
   [('Poursuivre jusqu’au 28e jour', False), ('Arrêter les corticoïdes et discuter une transplantation précoce chez un patient sélectionné', True), ('Doubler la dose', False)],
   'Un score de Lille ≥ 0,56 définit le non-répondeur nul : les corticoïdes sont arrêtés, et une transplantation précoce peut être proposée à une minorité de patients sélectionnés (EASL 2018).')
 + key('À J7, un Lille ≥ 0,45 signale une non-réponse, et un Lille ≥ 0,56 un non-répondeur nul, ce qui impose l’arrêt. Le répondeur poursuit 28 jours, puis arrête ou décroît sur 3 semaines.')
 + src(ALD))

C.a(11, 'Cirrhose alcoolique et transplantation', P(
 'Au-delà de l’épisode aigu, la cirrhose alcoolique impose une prise en charge au long cours. Ainsi, l’abstinence complète doit être conseillée et encouragée pour réduire les complications et la mortalité (grade A1) ; de plus, les cofacteurs, comme l’obésité, l’insulinorésistance, la dénutrition, le tabac, la surcharge en fer et les hépatites virales, sont recherchés et traités. En outre, les règles générales de la cirrhose s’appliquent : prévention de la décompensation selon Baveno VII, dépistage des varices et surveillance du carcinome hépatocellulaire, dont l’incidence annuelle est d’environ 2,6 % chez les patients Child-Pugh A et B.',
 'Par ailleurs, la ' + w('k70-tx', 'transplantation hépatique') + ' doit être envisagée chez le patient Child-Pugh C ou avec un MELD d’au moins 15, car elle confère un bénéfice de survie (grade A1). Cependant, la sélection ne doit pas reposer sur le seul critère des six mois d’abstinence (grade A2) ; en effet, la durée d’abstinence exigée dépend de la gravité hépatique et du profil addictologique, et l’évaluation est multidisciplinaire avant et après la greffe.')
 + key('Le patient vise l’abstinence complète, traite ses cofacteurs et suit les règles générales de la cirrhose (Baveno VII, carcinome hépatocellulaire). On discute la transplantation en Child-Pugh C ou si le MELD est ≥ 15, sans s’en tenir à la règle des six mois.')
 + C.pareto('pareto-k70-clinique', 'Maladie alcoolique du foie', ['k70-2', 'k70-5', 'k70-7', 'k70-8', 'k70-9', 'k70-10', 'k70-11'],
     ['Risque au-delà de 30 g/j d’alcool.',
      'L’AUDIT-C dépiste, et l’éthylglucuronide vérifie l’abstinence.',
      'Hépatite alcoolique : ictère récent, ASAT rarement > 300 UI/l.',
      'Sévère : Maddrey ≥ 32.',
      'La prednisolone se donne à 40 mg/j pendant 28 jours, en l’absence d’infection active.',
      'Un Lille à J7 ≥ 0,45 signale une non-réponse et fait arrêter les corticoïdes.',
      'Transplantation si Child-Pugh C ou MELD ≥ 15.'])
 + src(ALD, BAV))

C.a(12, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. Sa bilirubine vaut 210 µmol/l et son ASAT 160 UI/l ; de plus, le taux de prothrombine est allongé et la fonction de Maddrey atteint 48. Il s’agit donc d’une hépatite alcoolique sévère. Or, l’examen d’urine montre une infection urinaire : c’est pourquoi celle-ci est traitée d’abord, puis la prednisolone 40 mg/j est débutée.',
 'Ensuite, au septième jour, la bilirubine a baissé et le score de Lille vaut 0,21 : la patiente est donc une répondeuse partielle, et le traitement est poursuivi jusqu’au 28e jour. Parallèlement, la nutrition, les vitamines du groupe B et le sevrage encadré sont mis en place. Enfin, l’abstinence est préparée avec l’équipe d’addictologie, car c’est elle qui déterminera la survie à long terme.')
 + key('Si le Maddrey est ≥ 32, on traite d’abord l’infection, puis on donne la prednisolone et on calcule le Lille à J7 pour poursuivre ou arrêter. À long terme, la nutrition, la thiamine et l’abstinence restent indispensables.')
 + src(ALD))

C.a(13, 'Critères formels et paramètres clés', alert(
 '<p>On parle d’<b>hépatite alcoolique</b> quand un buveur excessif a un ictère récent, une bilirubine > 50 µmol/l et des ASAT > 2 × la normale, rarement > 300 UI/l, avec un rapport ASAT/ALAT > 1,5-2. La <b>gravité</b> se définit par un Maddrey ≥ 32. Pour la <b>réponse</b>, un Lille à J7 ≥ 0,45 signale une non-réponse, et ≥ 0,56 un non-répondeur nul.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Le risque apparaît au-delà de 30 g/j. La prednisolone se donne à 40 mg/j, ou la méthylprednisolone à 32 mg/j, pendant 28 jours, et la N-acétylcystéine IV pendant 5 jours (grade B2). Le patient reçoit 35-40 kcal/kg/j et 1,2-1,5 g/kg/j de protéines. Les benzodiazépines du sevrage ne dépassent pas 10-14 jours, et la transplantation se discute en Child-Pugh C ou si le MELD est ≥ 15.</div>'
 + src(ALD))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Place'], [
   ['Consommation à risque ?', w('k70-audit', 'AUDIT-C') + ', entretien', 'Premier recours, urgences'],
   ['Abstinence réelle ?', w('k70-etg', 'Éthylglucuronide') + ' urinaire ou capillaire', 'Suivi, liste de greffe'],
   ['Atteinte hépatique ?', 'GGT, ALAT, ASAT, ' + w('k70-elasto', 'élastographie'), 'Tout buveur excessif'],
   ['Stéatose, cirrhose, complication ?', 'Échographie', 'Si anomalie'],
   ['Hépatite alcoolique sévère ?', w('k70-mdf', 'Maddrey') + ', ' + w('k70-meld', 'MELD'), 'Ictère récent'],
   ['Diagnostic incertain ?', w('k70-biopsie', 'Biopsie transjugulaire'), 'Doute diagnostique']])
 + P('Le tableau se lit de haut en bas : ainsi, la biopsie n’intervient qu’après l’échec des examens simples à trancher.')
 + key('On fait l’AUDIT-C, puis les tests hépatiques et l’élastographie, puis l’échographie ; un ictère impose les scores de gravité, et un doute la biopsie.')
 + src(ALD))

C.e(2, 'Interpréter les marqueurs de l’alcool', P(
 'Les marqueurs indirects, comme la GGT, l’ASAT, l’ALAT, le volume globulaire moyen et la transferrine carboxy-déficiente, reflètent une consommation chronique excessive ; cependant, leur sensibilité et leur spécificité sont modestes, et la maladie hépatique elle-même les modifie. En revanche, les marqueurs directs mesurent l’éthanol ou ses métabolites : l’alcool expiré ou sérique pendant 4 à 12 heures, l’éthylglucuronide urinaire jusqu’à environ 80 heures et l’éthylglucuronide capillaire jusqu’à six mois (EASL 2018, tableau 5).',
 'Par conséquent, le choix dépend de la question. Ainsi, pour une consommation récente, l’éthylglucuronide urinaire suffit ; à l’inverse, pour documenter une abstinence prolongée avant une greffe, l’éthylglucuronide capillaire est préféré.')
 + key('Les marqueurs indirects (GGT, VGM, CDT) reflètent une consommation chronique, mais sont peu spécifiques. Les marqueurs directs couvrent des fenêtres différentes : l’éthanol 4-12 h, l’éthylglucuronide urinaire environ 80 h et l’éthylglucuronide capillaire jusqu’à 6 mois.')
 + C.pareto('pareto-k70-examens', 'Examens', ['k70-e-1', 'k70-e-2'],
     ['AUDIT-C pour dépister.',
      'Élastographie : une fibrose avancée peut avoir des tests normaux.',
      'Un Maddrey ≥ 32 définit l’hépatite sévère.',
      'Éthylglucuronide capillaire : abstinence sur ≤ 6 mois.'])
 + src(ALD))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : le lobule et la zone 3', P(
 'Le lobule hépatique est organisé autour de la veine centrolobulaire ; ainsi, le sang circule des espaces portes vers le centre du lobule. Or, les hépatocytes de la zone 3, périveinulaire, reçoivent le sang le moins oxygéné et expriment le plus de CYP2E1. Par conséquent, c’est dans cette zone que prédominent la stéatose, la ballonnisation et la fibrose alcooliques.')
 + key('C’est pourquoi la fibrose alcoolique est d’abord périveinulaire, à la différence de la fibrose portale des hépatites virales.', 'Science → histologie.'))
C.s('histo', 'Histologie', 'Histologie : les quatre lésions élémentaires', P(
 'L’EASL décrit quatre groupes de lésions, prédominant dans la région centrolobulaire avant la cirrhose : la stéatose macrovacuolaire, la souffrance hépatocytaire avec ballonnisation, l’inflammation lobulaire à polynucléaires et la fibrose. De plus, les hépatocytes ballonnisés contiennent souvent des ' + w('k70-mallory', 'corps de Mallory-Denk') + ', formés surtout de kératines 8 et 18. Toutefois, la stéatose peut être minime, voire absente, dans une stéatohépatite sévère ou après une période d’abstinence.')
 + key('Stéatose, ballonnisation, corps de Mallory-Denk, polynucléaires, fibrose périveinulaire : signature de la stéatohépatite alcoolique.', 'Science → diagnostic.'))
C.s('bioch', 'Biochimie', 'Biochimie : le métabolisme de l’éthanol', P(
 'L’éthanol est oxydé en acétaldéhyde par l’alcool déshydrogénase et, en cas de consommation chronique, par le CYP2E1 induit ; ensuite, l’aldéhyde déshydrogénase transforme l’acétaldéhyde en acétate. Or, ces réactions produisent du NADH, ce qui bloque la β-oxydation des acides gras et favorise leur synthèse. Par conséquent, les triglycérides s’accumulent dans l’hépatocyte, ce qui explique la stéatose.')
 + key('C’est pourquoi la stéatose régresse en quelques semaines d’abstinence : sa cause métabolique disparaît avec l’éthanol.', 'Science → clinique.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : corticoïdes et foie malade', P(
 'Les glucocorticoïdes inhibent la transcription des cytokines pro-inflammatoires ; ainsi, ils freinent l’inflammation neutrophile de l’hépatite alcoolique. Cependant, ils favorisent les infections, dont les aspergilloses invasives et les pneumocystoses décrites dans cette indication. De plus, l’information professionnelle suisse de la prednisolone signale qu’une hypoalbuminémie augmente la fraction libre active et qu’une cirrhose peut justifier une réduction de dose.')
 + key('Anti-inflammatoire efficace à court terme, mais risque infectieux élevé : d’où la recherche systématique d’infection et l’arrêt précoce chez le non-répondeur.', 'Science → traitement.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, ils visent deux cibles distinctes : l’inflammation hépatique aiguë et le trouble de l’usage d’alcool.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Glucocorticoïde', 'Prednisolone', 'Hépatite alcoolique sévère sans infection active', w('k70-d-prednisolone', 'Monographie')],
   ['Antioxydant', 'N-acétylcystéine IV', 'Associée aux corticoïdes (grade B2)', w('k70-d-nac', 'Fiche')],
   ['Maintien de l’abstinence', 'Acamprosate', 'Après sevrage, avec prise en charge psychosociale', w('k70-d-acamprosate', 'Monographie')],
   ['Sevrage', 'Benzodiazépines', 'Syndrome de sevrage, ≤ 10-14 jours', w('k70-sevrage', 'Fiche')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, aucun médicament ne remplace la prise en charge psychosociale de l’addiction, que l’EASL juge l’élément le plus important.')
 + key('La prednisolone traite l’hépatite sévère, l’acamprosate soutient l’abstinence, des benzodiazépines brèves traitent le sevrage, et les vitamines B préviennent l’encéphalopathie de Wernicke.')
 + src(ALD))

C.p(2, 'Doses et statut réglementaire', P('Les éléments suivants proviennent de l’EASL 2018 et des informations professionnelles suisses ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Situation', 'Dose ou règle', 'Source'], [
   ['Prednisolone', 'Hépatite alcoolique sévère', '40 mg/j, 28 jours ; arrêt brutal ou décroissance sur 3 semaines', 'EASL 2018'],
   ['Méthylprednisolone', 'Alternative', '32 mg/j, 28 jours', 'EASL 2018'],
   ['N-acétylcystéine', 'Avec corticoïdes', 'Intraveineuse, 5 jours (schéma : TODO, non détaillé dans la source lue)', 'EASL 2018 (grade B2)'],
   ['Acamprosate (Campral®)', 'Maintien de l’abstinence', '2 comprimés 3 fois par jour, 6 à 12 mois ; contre-indiqué si créatinine > 120 µmol/l', 'FI Campral®'],
   ['Disulfirame (Antabus®)', 'Soutien de l’abstinence', 'Contre-indiqué en cas d’affection hépatique avancée', 'FI Antabus®']])
 + trap('L’information professionnelle suisse de la prednisolone ne cite pas l’hépatite alcoolique parmi ses indications hépatiques et gastro-intestinales ; son usage y est donc hors indication, quoique recommandé par l’EASL. De plus, le baclofène n’a pas d’autorisation suisse dans le trouble de l’usage d’alcool ; la limite de 80 mg/j citée par l’EASL est une recommandation temporaire française. À arbitrer à l’audit.', 'Point à valider')
 + P('Par exemple, chez la patiente du début, la prednisolone est prescrite à 40 mg/j après information sur son statut hors indication ; ensuite, l’acamprosate est débuté après le sevrage, la fonction rénale étant normale.')
 + key('Prednisolone 40 mg/j 28 jours (hors indication en Suisse) ; acamprosate 2 cp 3×/j, contre-indiqué si créatinine > 120 µmol/l ; disulfirame contre-indiqué si hépatopathie avancée.')
 + src(ALD, FI('Prednisolone Streuli®'), FI('Campral®'), FI('Antabus®')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'Sous corticoïdes, l’infection est le principal risque : bactérienne, mais aussi aspergillose invasive et pneumocystose, de pronostic très sombre. C’est pourquoi l’infection est recherchée avant, pendant et après le traitement (grade A1), et le score de Lille est calculé au septième jour.', 'Sécurité.')
 + P('Par ailleurs, les benzodiazépines du sevrage ne doivent pas dépasser 10 à 14 jours, en raison du risque d’abus et d’encéphalopathie (grade A1). De plus, une supplémentation en vitamines du groupe B prévient l’encéphalopathie de Wernicke. Enfin, le paracétamol à dose thérapeutique peut léser le foie du buveur chronique dénutri : sa dose est donc surveillée.')
 + key('Sous corticoïdes, on surveille les infections et l’on calcule le Lille à J7. Les benzodiazépines ne dépassent pas 10-14 jours, on donne des vitamines B, et l’on reste prudent avec le paracétamol.')
 + C.pareto('pareto-k70-pharma', 'Pharmacologie', ['k70-p-1', 'k70-p-2', 'k70-p-3'],
     ['Prednisolone 40 mg/j 28 jours si sévère et sans infection.',
      'On arrête si le Lille est ≥ 0,56 (non-répondeur nul).',
      'Acamprosate : contre-indiqué si créatinine > 120 µmol/l.',
      'Disulfirame : contre-indiqué si hépatopathie avancée.',
      'Benzodiazépines ≤ 10-14 jours ; vitamines B.'])
 + src(ALD, FI('Campral®'), FI('Antabus®')))

# ---------------- Fenêtres
L = lab
C.pop('k70-ha', 'Hépatite alcoolique', L(('Définition', 'Syndrome d’ictère d’apparition récente chez un buveur excessif, sous-tendu par une stéatohépatite.'), ('Biologie (EASL 2018)', 'Bilirubine > 50 µmol/l ; ASAT > 2 × normale, rarement > 300 UI/l ; ASAT/ALAT > 1,5-2 ; polynucléose.'), ('Code', 'K70.1.')) + src(ALD))
C.pop('k70-tua', 'Trouble de l’usage d’alcool', L(('Définition', 'Terme du DSM-5, qui remplace « abus » et « dépendance ».'), ('Dépistage', 'AUDIT ou AUDIT-C (grade A1).'), ('Prise en charge', 'On associe une intervention brève, une équipe multidisciplinaire, une psychothérapie et des médicaments, car l’abstinence est le premier facteur pronostique.')) + src(ALD))
C.pop('k70-mdf', 'Fonction discriminante de Maddrey (modifiée)', L(('Formule', '4,6 × (temps de prothrombine du patient − témoin, en secondes) + bilirubine (mg/dl).'), ('Seuil', 'Un score ≥ 32 définit l’hépatite alcoolique sévère et constitue le seuil habituel de traitement.'), ('Pronostic', '< 32 : mortalité à un mois < 10 %.')) + src(MDF, ALD))
C.pop('k70-meld', 'Score MELD', L(('Variables', 'Il combine la bilirubine, l’INR et la créatinine.'), ('Usage', 'Il prédit la mortalité à court terme de l’hépatite alcoolique et priorise la greffe ; dans la cirrhose alcoolique, un MELD ≥ 15 fait discuter la transplantation.')) + src(ALD))
C.pop('k70-gahs', 'Score de Glasgow de l’hépatite alcoolique', L(('Variables', 'Âge, bilirubine, urée, temps de prothrombine, leucocytes.'), ('Échelle', '5 à 12.'), ('Seuil', '≥ 9 avec Maddrey ≥ 32 : mauvais pronostic, bénéfice des corticoïdes à 84 jours.')) + src(ALD))
C.pop('k70-abic', 'Score ABIC', L(('Variables', 'Il combine l’âge, la bilirubine, l’INR et la créatinine.'), ('Usage', 'Il classe le risque de décès à 90 jours en faible, intermédiaire ou élevé.')) + src(ALD))
C.pop('k70-lille', 'Score de Lille', L(('Variables', 'Il combine les données initiales et l’évolution de la bilirubine entre J0 et J7 de corticoïdes.'), ('Seuils', 'Un score ≤ 0,16 signale un répondeur complet, de 0,16 à 0,56 un répondeur partiel et ≥ 0,56 un non-répondeur nul ; à partir de 0,45, on parle de non-réponse.'), ('Conduite', 'On arrête les corticoïdes en cas de non-réponse, car ils n’apportent alors que le risque infectieux.')) + src(ALD))
C.pop('k70-steatose', 'Stéatose alcoolique', L(('Lésion', 'Les hépatocytes contiennent des vacuoles lipidiques, surtout macrovacuolaires.'), ('Fréquence', 'Elle touche environ 90 % des buveurs excessifs.'), ('Évolution', 'Peut régresser complètement en quelques semaines d’abstinence.')) + src(ALD) + C.img('k70_steatose.gif', 'Histologie : hépatocytes remplis de grandes vacuoles lipidiques.', 'Les grandes vacuoles repoussent le noyau en périphérie ; elles traduisent l’accumulation de triglycérides due à l’excès de NADH.', credit({'auteur': 'Ed Uthman', 'licence': 'CC BY 2.0', 'url': 'https://commons.wikimedia.org/wiki/File:Mallorys_Hyalin_in_Alcoholic_Liver_Disease_(2632109950).jpg'})))
C.pop('k70-sha', 'Stéatohépatite alcoolique', L(('Lésions', 'Elle associe une stéatose, une ballonnisation, une nécrose et une inflammation lobulaire à polynucléaires.'), ('Portée', 'Lésion progressive, qui augmente le risque de cirrhose et de carcinome hépatocellulaire.')) + src(ALD) + C.img('k70_hepatite.gif', 'Histologie : hépatocytes ballonnisés, inclusions éosinophiles et polynucléaires.', 'Les hépatocytes ballonnisés, les corps de Mallory-Denk et les polynucléaires signent la stéatohépatite ; c’est cette inflammation que les corticoïdes freinent.', credit({'auteur': 'Countincr (Wikipédia en anglais), image PEIR, université d’Alabama à Birmingham', 'licence': 'CC BY-SA 2.5', 'url': 'https://commons.wikimedia.org/wiki/File:Alcoholic_hepatitis.jpg'})))
C.pop('k70-mallory', 'Corps de Mallory-Denk', L(('Nature', 'Inclusions éosinophiles des hépatocytes ballonnisés, faites surtout de kératines 8 et 18.'), ('Valeur', 'Ils évoquent une stéatohépatite, mais ne sont pas spécifiques.')) + src(ALD))
C.pop('k70-pnpla3', 'Gène PNPLA3', L(('Rôle', 'Variants associés à un risque accru de lésions hépatiques alcooliques chez les sujets caucasiens.'), ('Usage', 'C’est un facteur de risque, mais on ne recommande pas de le tester en routine.')) + src(ALD))
C.pop('k70-ictere', 'Ictère', L(('Signe', 'La bilirubine colore en jaune la peau et les sclères.'), ('Valeur ici', 'Signe cardinal de l’hépatite alcoolique quand il est récent.')) + src(ALD) + C.img('k70_ictere.gif', 'Œil à sclère franchement jaune.', 'La sclère jaunit tôt, car son élastine fixe la bilirubine ; on la voit le mieux à la lumière du jour.', credit({'auteur': 'CDC / Dr Thomas F. Sellers, Emory University ; travail dérivé : த.உழவன்', 'licence': 'domaine public', 'url': 'https://commons.wikimedia.org/wiki/File:Jaundice_eye_new.jpg'})))
C.pop('k70-wernicke', 'Encéphalopathie de Wernicke', L(('Cause', 'Elle est due à une carence en thiamine (vitamine B1).'), ('Prévention', 'Vitamines du groupe B chez le patient alcoolique, notamment dans l’hépatite alcoolique.'), ('Diagnostic différentiel', 'Il faut la distinguer de l’encéphalopathie hépatique et du sevrage.')) + src(ALD))
C.pop('k70-sevrage', 'Syndrome de sevrage alcoolique', L(('Traitement', 'Benzodiazépines (ou clométhiazole), à limiter à 10-14 jours (grade A1).'), ('Risque', 'Si on prolonge les benzodiazépines, elles exposent à l’abus et à l’encéphalopathie.')) + src(ALD))
C.pop('k70-audit', 'Questionnaire AUDIT', L(('Contenu', 'Il comporte dix questions de l’OMS sur la consommation, la dépendance et les conséquences ; l’AUDIT-C reprend les trois premières, qui portent sur la consommation.'), ('Usage', 'Dépistage du trouble de l’usage d’alcool (grade A1).')) + src(ALD))
C.pop('k70-cdt', 'Transferrine carboxy-déficiente', L(('Type', 'C’est un marqueur sérique indirect de consommation chronique excessive.'), ('Limite', 'Sa sensibilité et sa spécificité sont modestes, et des facteurs de confusion existent.')) + src(ALD))
C.pop('k70-etg', 'Éthylglucuronide', L(('Type', 'C’est un métabolite direct de l’éthanol.'), ('Fenêtre', 'Il reste détectable jusqu’à environ 80 h dans l’urine et jusqu’à 6 mois dans les cheveux.'), ('Usage', 'Il sert à vérifier l’abstinence (grade A2).')) + src(ALD))
C.pop('k70-elasto', 'Élastographie impulsionnelle', L(('Usage', 'Mesure de la fibrose chez tout buveur excessif dépisté (grade A1).'), ('Piège', 'L’inflammation d’une hépatite alcoolique surestime les valeurs.')) + src(ALD))
C.pop('k70-biopsie', 'Biopsie hépatique', L(('Indications (grade A1)', 'On la fait en cas d’incertitude diagnostique, de besoin d’un stadage précis ou d’essai clinique.'), ('Voie', 'Transjugulaire dans l’hépatite alcoolique (troubles de la coagulation).'), ('Rendement', 'Elle trouve un autre diagnostic dans 10 à 20 % des cas.')) + src(ALD))
C.pop('k70-stopah', 'Essai STOPAH', L(('Plan', 'Cet essai britannique de 2011-2014 a testé la prednisolone et la pentoxifylline dans l’hépatite alcoolique sévère.'), ('Résultat', 'La prednisolone a réduit de façon limite la mortalité à 28 jours, sans aucun bénéfice au-delà d’un mois.')) + src(STOP, ALD))
C.pop('k70-nutrition', 'Nutrition de l’hépatite alcoolique', L(('Objectifs (grade A2)', 'On vise ≥ 35-40 kcal/kg/j et 1,2-1,5 g/kg/j de protéines, d’abord par voie orale, car la dénutrition aggrave le pronostic.'), ('Risque', 'Apport < 21,5 kcal/kg/j : mortalité et infections accrues.'), ('Si échec', 'On passe à une nutrition entérale par sonde.')) + src(ALD))
C.pop('k70-tx', 'Transplantation hépatique', L(('Cirrhose alcoolique (grade A1)', 'Child-Pugh C et/ou MELD ≥ 15.'), ('Abstinence', 'La règle des six mois ne suffit pas à elle seule ; une évaluation multidisciplinaire décide.'), ('Hépatite sévère', 'Greffe précoce chez une minorité de non-répondeurs sélectionnés.')) + src(ALD))
C.pop('k70-d-prednisolone', 'Prednisolone', L(('Dose (EASL 2018)', 'On donne 40 mg/j pendant 28 jours, puis on arrête brutalement ou l’on décroît sur 3 semaines.'), ('Contre-indication pratique', 'Infection active non contrôlée.'), ('Statut suisse', 'L’hépatite alcoolique ne figure pas dans les indications de la FI, et la dose peut être réduite en cas de cirrhose.')) + src(ALD, FI('Prednisolone Streuli®')))
C.pop('k70-d-nac', 'N-acétylcystéine', L(('Principe', 'Elle restaure le glutathion et limite ainsi le stress oxydatif.'), ('Place', 'On la donne par voie intraveineuse pendant 5 jours avec les corticoïdes (grade B2) ; seule, elle n’améliore pas la survie.')) + src(ALD))
C.pop('k70-d-acamprosate', 'Acamprosate (Campral®)', L(('Indication suisse', 'Il est autorisé pour maintenir l’abstinence après le sevrage, avec des mesures psychosociales.'), ('Dose', '2 comprimés 3 fois par jour, débuté vers le 5e jour d’abstinence, 6 à 12 mois.'), ('Contre-indications', 'Il est contre-indiqué si la créatinine dépasse 120 µmol/l et pendant l’allaitement, et il demande de la prudence en Child-Pugh C.')) + src(FI('Campral®'), ALD))

C.termes = [
 (r'hépatite alcoolique', 'k70-ha'), (r'trouble de l’usage d’alcool', 'k70-tua'), (r'Maddrey', 'k70-mdf'), (r'MELD', 'k70-meld'),
 (r'score de Glasgow', 'k70-gahs'), (r'ABIC', 'k70-abic'), (r'(score de )?Lille', 'k70-lille'), (r'stéatose', 'k70-steatose'),
 (r'stéatohépatite', 'k70-sha'), (r'Mallory-Denk', 'k70-mallory'), (r'AUDIT(-C)?', 'k70-audit'), (r'éthylglucuronide', 'k70-etg'),
 (r'transferrine carboxy-déficiente', 'k70-cdt'), (r'élastographie', 'k70-elasto'), (r'biopsie', 'k70-biopsie'), (r'STOPAH', 'k70-stopah'),
 (r'prednisolone', 'k70-d-prednisolone'), (r'N-acétylcystéine', 'k70-d-nac'), (r'acamprosate', 'k70-d-acamprosate'), (r'Wernicke', 'k70-wernicke'),
 (r'sevrage', 'k70-sevrage'), (r'transplantation', 'k70-tx'), (r'ictère', 'k70-ictere'), (r'PNPLA3', 'k70-pnpla3'),
]

C.write()
