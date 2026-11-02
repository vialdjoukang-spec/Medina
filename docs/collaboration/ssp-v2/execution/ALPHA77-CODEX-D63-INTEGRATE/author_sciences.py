"""Six sciences locales et neuf unités de sémiologie au contrat natif."""
from common import refs,table,original,causal

def unit(marker,title,body,*sources):
 return f'<section class="ilot" id="d63-semio-{marker}" data-semiology="{marker}"><h3>{title}</h3>{body}{refs(*sources)}</section>'

SEMIO=unit('normal','Pour la leçon : quelle est la sémiologie fondamentale et analytique ?', '''
<h4>1. Partir de la fonction normale</h4>
<p>Les hématies assurent une grande partie du transport d’oxygène grâce à leur hémoglobine. La moelle les renouvelle, le fer recyclé par les macrophages contribue à la synthèse d’hème et la production rénale d’érythropoïétine participe à l’adaptation de l’érythropoïèse. Un stock de fer, un transport plasmatique et une utilisation médullaire sont trois compartiments fonctionnels différents.</p>
<p>La saturation mesurée par oxymétrie décrit la proportion d’hémoglobine oxygénée, sans donner la quantité totale d’hémoglobine. Une saturation à 98 % peut donc coexister avec une capacité de transport abaissée par l’anémie. Le retentissement dépend aussi du débit circulatoire, des besoins et des réserves cardiorespiratoires. La vitesse d’installation explique qu’un même taux d’Hb puisse être toléré différemment.</p>
<p>Cette chaîne normale donne le fil du raisonnement : fonction perturbée, manifestation ressentie ou observée, examen qui répond à une question, interprétation puis décision. D63 est un code de manifestation dans une maladie classée ailleurs ; il ne dispense pas de démontrer le mécanisme de l’anémie chez la personne.</p>
''','NORMAL','NORMAL-RBC','WEISS','OFS-CIM')
SEMIO+=original('blood','d63-semio-frottis')
SEMIO+=unit('signs','2. Symptômes et signes : décrire avant d’attribuer', '''
<p>La fatigue se décrit par son début, sa progression, son effet sur les activités, le sommeil et les efforts. Préciser dyspnée d’effort ou de repos, palpitations, vertiges, douleur thoracique, malaise et limitation fonctionnelle. Une plainte apparue en quelques heures n’a pas la même signification qu’une diminution progressive des capacités sur plusieurs mois.</p>
<p>La pâleur est un constat compatible avec l’anémie ; elle ne mesure pas l’Hb et sa perception dépend des conditions d’examen. Tachycardie et polypnée peuvent traduire une compensation mais aussi fièvre, douleur, infection ou hypovolémie. Rechercher signes de pertes sanguines, manifestations de la maladie inflammatoire, amaigrissement, fièvre et effets des traitements.</p>
<p>Ne pas réduire la personne à une anomalie biologique : une anémie modérée peut contribuer à une gêne importante chez un patient cardiorespiratoire fragile, tandis que des symptômes sévères peuvent venir d’une autre cause concomitante. Les sources étudiées ne fournissent pas ici une sensibilité ou une spécificité validée permettant de convertir une pâleur en taux d’Hb.</p>
''','MEDIX','WEISS','KDIGO','PROFILES17')
SEMIO+=unit('mechanisms','3. Mécanismes : relier disponibilité du fer et réponse médullaire', '''
<p>L’inflammation stimule notamment l’axe interleukine 6–STAT3 et l’hepcidine hépatique. L’hepcidine réduit la sortie du fer par la ferroportine, dans les entérocytes et les macrophages. Le fer peut rester présent dans des réserves tout en devenant moins disponible pour l’érythropoïèse. Le profil peut associer fer circulant et TSAT bas, ferritine conservée ou élevée et production réticulocytaire insuffisante.</p>
<p>D’autres mécanismes s’ajoutent : réponse à l’érythropoïétine diminuée, production hormonale insuffisante en MRC, inhibition des précurseurs et survie érythrocytaire raccourcie. Une perte sanguine, une malabsorption ou un déficit vitaminique peuvent coexister. Une explication par l’hepcidine seule ne suffit donc pas à tous les tableaux.</p>
<p>La chronologie teste la cohérence du mécanisme. Une baisse importante d’Hb en quelques heures ne doit pas être attribuée à la seule réduction de fabrication de nouvelles hématies. Chercher saignement, hémolyse, dilution ou autre événement aigu selon le contexte. Le mécanisme explique une tendance, il ne justifie pas toute variation.</p>
''','WEISS','KDIGO','MEDIX')
SEMIO+=unit('examination','4. Examen clinique et choix des mesures', '''
<p>Évaluer d’abord les paramètres vitaux, la conscience, la perfusion et la présence d’un saignement. Examiner peau et muqueuses, rechercher ictère, signes cardiorespiratoires, maladie inflammatoire active et anomalies suggérant une autre affection. L’examen doit être guidé par l’histoire et répété si l’état évolue.</p>
<p>La numération confirme la concentration d’Hb et décrit VGM et autres lignées. Les réticulocytes évaluent une réponse de production ; ferritine, TSAT et contexte inflammatoire explorent disponibilité et réserves. Créatinine et filtration estimée renseignent sur une contribution rénale. Le frottis ou les examens d’hémolyse répondent à des questions supplémentaires, sans être un substitut à l’histoire.</p>
<p>Préciser les unités et la méthode. Pour l’Hb, 100 g/L correspondent à 10 g/dL. La ferritine en µg/L ne se compare pas numériquement à une concentration de fer sérique. CHr et mesures apparentées dépendent de l’analyseur : un seuil provenant d’une population n’est pas automatiquement transférable à une autre.</p>
''','WHO','KDIGO','MEDIX','ECCO','ESMO')
SEMIO+=unit('interpretation','5. Interprétation : combiner les résultats', '''
<p>Une ferritine très basse soutient une carence absolue. Une ferritine élevée n’exclut pas une restriction du fer disponible, ni une carence associée dans une maladie inflammatoire. Une TSAT basse aide à reconnaître la disponibilité réduite mais ne sépare pas à elle seule stock épuisé et séquestration.</p>
<p>Les recommandations utilisent des seuils liés à leur population et à leur objectif. Dans la MICI active, ECCO décrit une zone de ferritine 30–100 µg/L compatible avec une association carence/inflammation. KDIGO donne des critères de début de fer distincts en hémodialyse et hors hémodialyse. Ces seuils thérapeutiques ne doivent pas être transformés en une définition universelle de l’anémie inflammatoire.</p>
<p>Un VGM normal représente une moyenne ; il ne prouve pas que toutes les hématies sont normales ni que le fer et la vitamine B12 sont suffisants. Une anémie rénale peut aussi être carentielle ou hémorragique. La bonne interprétation conserve les hypothèses concurrentes et indique le résultat qui les renforcera ou les affaiblira.</p>
''','WEISS','ECCO','KDIGO','MEDIX')
SEMIO+=unit('differentials','6. Diagnostics différentiels et mécanismes associés', '''
<p>Discuter carence martiale isolée, mécanisme mixte, MRC, pertes chroniques ou aiguës, hémolyse, déficit vitaminique, toxicité médicamenteuse et maladie médullaire selon les données. Une hémoglobinopathie peut faire partie des causes de microcytose ; elle ne se diagnostique pas à partir d’un seul VGM.</p>
<p>Des cytopénies multiples, un frottis inhabituel, une aggravation inexpliquée ou une discordance durable avec l’activité inflammatoire justifient une évaluation élargie. Une maladie cancéreuse n’implique pas que l’anémie provient uniquement des cytokines : saignement, traitement, infiltration ou insuffisance rénale peuvent contribuer.</p>
<p>Une amélioration après fer soutient une composante répondant au fer ; elle ne prouve pas que la cause de la perte a disparu. De même, une hausse d’Hb sous ESA ne démontre pas que le diagnostic initial était complet. Réponse thérapeutique et diagnostic étiologique se complètent.</p>
''','MEDIX','WEISS','KDIGO','ESMO')
SEMIO+=unit('urgency','7. Urgence : la tolérance prime sur l’étiquette chronique', '''
<p>Douleur thoracique, dyspnée de repos marquée, syncope, altération de conscience, instabilité circulatoire ou saignement actif imposent une évaluation urgente. Une maladie connue depuis longtemps ne protège pas d’un événement aigu. La correction de la maladie inflammatoire ou l’effet d’un ESA ne répondent pas à un besoin immédiat de transport d’oxygène.</p>
<p>La recommandation suisse smarter medicine donne des repères restrictifs de 70 g/L chez l’adulte stable sans maladie cardiovasculaire et de 80 g/L avec maladie cardiovasculaire préexistante stable. Ces repères ne sont pas un algorithme pour hémorragie majeure ou syndrome coronarien aigu. NICE distingue ces situations et recommande une unité suivie d’une réévaluation chez les adultes sans saignement actif quand une transfusion est indiquée.</p>
<p>Le risque de surcharge circulatoire, les antécédents transfusionnels et un projet de greffe rénale participent à la décision. Ils ne doivent pas conduire à retarder une transfusion nécessaire dans une situation menaçante. La décision se documente avec le contexte, le bénéfice attendu et la réponse observée.</p>
''','SMARTER','NICE','KDIGO','ESMO')
SEMIO+=unit('limits','8. Limites, pièges et niveau de preuve', '''
<p>La pâleur n’est pas un dosage, la saturation n’est pas une mesure de masse d’Hb, la ferritine n’est pas exclusivement un indicateur de stock et une valeur normale de VGM n’est pas une preuve d’absence de carence. Chaque raccourci peut conduire à omettre une maladie associée ou à traiter un chiffre sans bénéfice démontré.</p>
<p>Les données de prévalence de carence associée à l’inflammation sont hétérogènes ; elles ne donnent pas une probabilité individuelle suisse. Une association entre Hb basse et mortalité en MRC ne prouve pas que normaliser l’Hb par ESA améliore la survie. Les essais ayant testé des objectifs élevés justifient au contraire la prudence des cibles recommandées.</p>
<p>Les désaccords de seuils ou de formulations sont conservés : CHr 29 pg dans ECCO contre 28 dans ESMO ; TSAT 16 % dans un énoncé ECCO contre 20 % dans son texte ; objectif Eprex 10–12 g/dL contre cible KDIGO inférieure à 11,5. Une valeur sans date, population et objectif perd une partie de sa signification.</p>
''','WEISS','KDIGO','ECCO','ESMO','EPREX')
SEMIO+=unit('sources','9. Sources lues et portée des liens cliniques', '''
<p>Les recommandations suisses medix et smarter medicine structurent la pratique générale et transfusionnelle ; KDIGO 2026 précise le contexte rénal. ECCO 2024 et ESMO 2018 concernent respectivement la MICI et l’oncologie. La revue européenne de Weiss et collaborateurs de 2019 explicite les mécanismes ; elle ne remplace pas les indications et contre-indications des produits suisses.</p>
<p>Les passages consultés portent sur les mécanismes, les profils biologiques, les décisions thérapeutiques et leurs limites. Les informations professionnelles précisent les produits Ferinject, Eprex et ferro sanol. Les figures originales montrent une anatomie ou un frottis normaux ; elles ne constituent pas une preuve diagnostique d’anémie inflammatoire. Cette auto-relecture pédagogique reste distincte d’une validation médicale humaine indépendante.</p>
''','MEDIX','SMARTER','KDIGO','ECCO','ESMO','WEISS','FERINJECT','EPREX','FERROSANOL')

ANAT='''<h3>Moelle, foie, intestin, rein : une organisation fonctionnelle</h3>
<p>La production des hématies se déroule dans le tissu hématopoïétique médullaire. Les cellules en maturation dépendent d’un environnement qui apporte nutriments et signaux. La photographie originale ci-dessous situe ce tissu dans l’os spongieux ; une coupe macroscopique ne permet pas de voir les stades de maturation ni de quantifier le stock de fer.</p>
'''+original('marrow','d63-science-moelle')+'''
<h4>Le circuit du fer relie plusieurs organes</h4>
<p>L’intestin constitue une porte d’entrée du fer alimentaire. Le fer transféré au plasma est transporté par la transferrine. Une part majeure du fer requis chaque jour pour l’érythropoïèse provient cependant du recyclage des hématies âgées par les macrophages, notamment dans les organes du système réticulo-endothélial. Le foie participe au stockage et produit l’hepcidine, signal qui réduit la sortie de fer vers le plasma.</p>
<p>Le rein contribue à l’adaptation hormonale par l’érythropoïétine. Une MRC peut donc associer défaut relatif de stimulation et inflammation, sans que le fer soit nécessairement absent de tous les compartiments. Les sites anatomiques expliquent pourquoi une même Hb basse peut avoir plusieurs mécanismes ; ils ne donnent pas à eux seuls un diagnostic.</p>
<h4>Relier le site à l’examen</h4>
<p>La numération examine le sang circulant ; les réticulocytes renseignent sur la production récente. Une aspiration ou une biopsie médullaire explore un autre compartiment et se discute lorsqu’une question médullaire persiste. La ferritine plasmatique n’est pas une photographie directe des réserves de tous les organes. Des examens invasifs ne se justifient pas simplement parce que l’anémie est associée à une maladie chronique.</p>
<p>Le lien thérapeutique suit ces fonctions : traiter une maladie intestinale peut améliorer absorption et pertes ; réduire l’inflammation peut améliorer la sortie du fer ; un ESA agit sur la production ; une transfusion apporte des hématies déjà formées. Ces actions ont des délais et des risques différents. Elles ne doivent pas être présentées comme quatre moyens interchangeables d’augmenter instantanément l’Hb.</p>
'''+refs('NORMAL','NORMAL-RBC','WEISS','KDIGO','ECCO')

HISTO='''<h3>Hématies et réticulocytes : ce que l’on observe réellement</h3>
<p>L’hématie mature humaine ne possède pas de noyau. Sa forme et sa richesse en hémoglobine contribuent à son rôle de transport. La maturation érythroïde se déroule avant son passage dans le sang ; les réticulocytes sont des cellules récemment libérées, identifiées par des méthodes adaptées aux constituants résiduels. Un frottis standard à faible grossissement ne permet pas de les compter de façon fiable.</p>
'''+original('blood','d63-science-frottis')+'''
<h4>De la morphologie à la mesure</h4>
<p>La taille moyenne donnée par le VGM résume une distribution. Deux populations de tailles différentes peuvent produire une moyenne normale. Le centre plus clair d’une hématie sur une image ne fournit pas une concentration d’Hb mesurée ; préparation, coloration, étalement et grossissement influencent l’apparence. La morphologie complète les indices, elle ne les remplace pas.</p>
<p>L’anémie inflammatoire est souvent normocytaire, mais une microcytose peut apparaître et une carence associée peut modifier le profil. Il n’existe pas sur cette image normale un « signe de D63 » qui établirait la maladie. La recherche d’anomalies orientant vers hémolyse ou maladie médullaire nécessite un examen adapté et une interprétation de laboratoire.</p>
<h4>Réticulocytes et disponibilité récente du fer</h4>
<p>Le nombre de réticulocytes renseigne sur une réponse de production. Leur contenu en Hb reflète une disponibilité récente du fer pour les cellules nouvellement produites. Ces deux informations ne sont pas identiques : une population peut être peu nombreuse et peu chargée en Hb, ou répondre après correction d’un déficit. Le degré d’anémie et la chronologie doivent accompagner les résultats.</p>
<p>Les seuils de CHr cités par ECCO et ESMO ne sont pas strictement identiques. On ne doit pas remplacer le nom d’un paramètre par celui d’un autre analyseur sans vérifier la comparabilité. Une mesure de contenu en Hb peut soutenir une restriction martiale, mais elle ne localise pas les réserves ni ne prouve le mécanisme inflammatoire à elle seule.</p>
'''+refs('NORMAL','NORMAL-RBC','WEISS','ECCO','ESMO','BLOOD-IMAGE')

PHYSIO='''<h3>Renouvellement, oxygène et adaptation</h3>
<p>La masse érythrocytaire résulte d’un équilibre entre production, durée de vie et pertes. La réponse hormonale à une baisse d’apport d’oxygène stimule l’érythropoïèse, à condition que les précurseurs disposent du fer et des autres substrats nécessaires. Une production stimulée ne fournit pas immédiatement des hématies matures ; le temps biologique de réponse est une donnée clinique.</p>
<p>En anémie, des compensations circulatoires peuvent maintenir une partie de l’apport tissulaire. Leur efficacité dépend de la réserve cardiovasculaire et du rythme d’installation. Une personne souffrant d’insuffisance cardiaque ou de maladie coronarienne peut être moins tolérante. Une dyspnée garde néanmoins plusieurs causes possibles ; ni l’anémie ni la saturation ne suffisent à décrire tout le transport d’oxygène.</p>
'''+causal('d63-physio-causal','Pourquoi une saturation normale ne rassure pas à elle seule',[
'Moins d’hémoglobine dans le sang',
'Proportion oxygénée parfois normale',
'Quantité transportée potentiellement réduite',
'Compensation dépendante des réserves',
'Tolérance clinique à évaluer'],
'La saturation renseigne sur une proportion ; l’Hb et l’état circulatoire apportent des informations complémentaires.')+'''
<h4>La réponse devient insuffisante</h4>
<p>L’inflammation peut réduire la réponse médullaire à l’érythropoïétine et modifier la survie des hématies. La MRC ajoute un défaut relatif de production hormonale. Une réticulocytose insuffisante pour le degré d’anémie devient alors cohérente, mais reste non spécifique : une carence ou une maladie médullaire peut produire un résultat comparable.</p>
<p>Le traitement vise une amélioration utile, pas la normalisation d’un chiffre à tout prix. Dans la MRC, KDIGO recommande une cible d’Hb inférieure à 11,5 g/dL sous ESA chez l’adulte. Une Hb basse associée à un pronostic défavorable dans une cohorte ne prouve pas qu’un objectif pharmacologique élevé corrige ce pronostic. Les risques thrombotiques et cardiovasculaires font partie du raisonnement physiologique appliqué.</p>
<p>Une transfusion augmente rapidement la quantité d’hématies circulantes, mais ne corrige pas la cause de l’anémie et ajoute ses propres risques. Le fer corrige une disponibilité insuffisante lorsque l’indication est établie ; l’ESA stimule la production dans des situations définies. Le choix dépend du délai acceptable, de la tolérance et du mécanisme.</p>
'''+refs('NORMAL-RBC','WEISS','KDIGO','EPREX','SMARTER')

BIO='''<h3>Fer de réserve, fer transporté et fer utilisable</h3>
<p>La ferritine stocke le fer dans les cellules ; sa concentration circulante sert d’indicateur indirect des réserves, tout en participant au profil de phase aiguë. La transferrine transporte le fer dans le plasma. La saturation de la transferrine est une proportion de sites occupés ; ce n’est ni la quantité totale de fer de l’organisme ni un comptage des hématies.</p>
<p>La ferroportine permet la sortie du fer de certains compartiments cellulaires. L’hepcidine se lie à cette voie d’export et en réduit l’activité, notamment par internalisation/dégradation et inhibition de transport. En inflammation, la sortie du fer des macrophages et des entérocytes diminue. Le fer peut donc être conservé dans les tissus tandis que le plasma et les précurseurs érythroïdes en disposent moins.</p>
'''+causal('d63-bio-causal','De l’inflammation à la restriction martiale',[
'Signal inflammatoire, notamment IL-6',
'Voie STAT3 et hepcidine augmentées',
'Export par ferroportine diminué',
'Fer moins disponible pour l’érythropoïèse',
'Profil biologique à interpréter en contexte'],
'Cette chaîne n’exclut ni une carence absolue associée ni les autres mécanismes d’anémie.')+'''
<h4>Le recyclage explique le paradoxe apparent</h4>
<p>La revue de Weiss décrit une contribution supérieure à 90 % du recyclage au fer quotidien nécessaire à l’érythropoïèse. Bloquer la disponibilité de ce flux peut donc avoir un effet important même lorsque l’absorption alimentaire n’est pas nulle. Ce pourcentage concerne un flux physiologique, pas la probabilité de carence d’un patient ni une indication de supplémentation.</p>
<p>Une ferritine élevée et une TSAT basse ne sont pas contradictoires : elles peuvent décrire des compartiments différents sous l’effet de l’inflammation. L’interprétation doit aussi tenir compte des transfusions, du fer administré récemment et des maladies hépatiques. La ferritine mesurée trop tôt après fer IV peut surestimer la reconstitution durable des réserves.</p>
<h4>Biologie et calculs thérapeutiques</h4>
<p>La formule de Ganzoni utilise une différence d’Hb en g/dL, multipliée par 2,4, puis ajoute les réserves en mg. Entrer des g/L sans conversion crée un facteur dix d’erreur dans la composante de déficit. De même, 50 mg/mL est une concentration de Ferinject, non la dose par kg. Le calcul total, la limite pondérale et la limite hebdomadaire doivent être contrôlés séparément.</p>
'''+refs('WEISS','MEDIX','DELPHI','FERINJECT')

GEN='''<h3>Régulation des gènes et maladie acquise : ne pas les confondre</h3>
<p>L’hepcidine est un peptide dont la production dépend d’une régulation de l’expression génique. La voie inflammatoire IL-6–STAT3 augmente cette production ; d’autres signaux reflètent le fer disponible et les besoins de l’érythropoïèse. Une modification d’expression provoquée par l’inflammation ne signifie pas qu’une mutation constitutionnelle a été acquise.</p>
<p>La revue de Weiss discute la régulation de l’hepcidine, le rôle de facteurs comme TMPRSS6 et les variations qui peuvent influencer le métabolisme du fer. Cela éclaire la diversité des réponses biologiques. Cela ne fonde pas un dépistage génétique systématique de toute anémie associée à une maladie chronique.</p>
<h4>Trois questions distinctes</h4>
<p>Une anémie acquise dans une maladie inflammatoire répond à une question de mécanisme actuel. Une histoire familiale, une anomalie ancienne ou un profil inhabituel peuvent conduire à rechercher une cause constitutionnelle. Une anomalie clonale médullaire relève encore d’une autre démarche. Les confondre peut conduire à demander un test inadapté ou à attribuer à tort une anomalie à l’inflammation.</p>
<p>Une microcytose persistante n’est pas un synonyme de carence martiale. L’histoire, les réserves, l’inflammation et, lorsque cela est indiqué, l’exploration d’une hémoglobinopathie aident à organiser le différentiel. Le résultat d’un test doit être expliqué selon sa portée : ce qui a été recherché, ce qui n’a pas été couvert et les conséquences pour la personne et sa famille.</p>
<h4>Du mécanisme moléculaire au médicament</h4>
<p>Les voies de réponse à l’hypoxie participent à la régulation de l’érythropoïétine. Des médicaments ciblant les prolyl-hydroxylases de HIF peuvent agir sur cette réponse, mais une plausibilité biologique n’est pas une autorisation suisse pour toute anémie. KDIGO 2026 préfère un ESA aux HIF-PHI en première intention lorsqu’une stimulation est décidée et décrit des précautions ; le statut exact du produit et de l’indication doit être vérifié séparément.</p>
<p>Les traitements dirigés contre la maladie inflammatoire peuvent modifier plusieurs signaux et améliorer l’anémie. On ne peut pas attribuer toute amélioration à un seul gène ou conclure qu’un marqueur moléculaire remplace le suivi d’Hb, des réserves et de la tolérance. Le niveau moléculaire explique une partie du mécanisme ; la décision clinique intègre aussi la personne et les preuves thérapeutiques.</p>
'''+causal('d63-gen-causal','Expression régulée, diagnostic à construire',[
'Inflammation : modification des signaux',
'Expression de l’hepcidine modulée',
'Disponibilité du fer modifiée',
'Ce mécanisme ne prouve pas une mutation',
'Clinique et bilan guident la décision'],
'La régulation acquise décrite ne justifie pas un panel génétique systématique.')+refs('WEISS','KDIGO','MEDIX')

TABS=[('semio','Sémiologie fondamentale et analytique',SEMIO),('anat','Anatomie',ANAT),('histo','Histologie',HISTO),('physio','Physiologie',PHYSIO),('bio','Biochimie et inflammation',BIO),('gen','Génétique et régulation',GEN)]
LINKS={
'semio':('La tolérance et la chronologie rendent les signes interprétables.','Hb, réticulocytes et bilan martial répondent à des questions distinctes.','Stabiliser si nécessaire, puis traiter le mécanisme documenté.'),
'anat':('Moelle, intestin, rein et foie peuvent contribuer au même tableau.','Le sang circulant ne révèle pas directement tous les compartiments.','La voie et le délai d’action du traitement dépendent de sa cible.'),
'histo':('Une moyenne normale peut masquer des populations différentes.','Frottis, réticulocytes et CHr ne mesurent pas la même chose.','Une réponse morphologique ou biologique se confronte à la clinique.'),
'physio':('Une saturation normale ne garantit pas un transport suffisant.','Mesurer l’Hb et examiner les réserves cardiorespiratoires.','Une cible d’ESA élevée n’est pas un objectif physiologique anodin.'),
'bio':('Un fer séquestré peut manquer à la moelle malgré des réserves.','Confronter ferritine, TSAT, inflammation et traitement récent.','Calculer dose totale, dose par séance et limites du produit séparément.'),
'gen':('Régulation inflammatoire acquise et maladie génétique diffèrent.','Un test spécialisé exige une question et une portée explicites.','Un mécanisme moléculaire plausible ne remplace pas l’autorisation ni les preuves.')}
def sciences():
 bar='<div class="panel" id="pS" hidden><div class="sci-bar ui" role="tablist">'
 for k,title,_ in TABS:bar+=f'<button id="d63-tab-{k}" role="tab" aria-selected="{str(k=="semio").lower()}" aria-controls="d63-s-{k}" data-s="d63-s-{k}">{title}</button>'
 bar+='</div><div class="chap-body sci-body">'
 for k,title,body in TABS:
  bridge='<div class="key">'+''.join(f'<p><b>{label}</b> {text}</p>' for label,text in zip(['Science → clinique.','Science → examen.','Science → traitement.'],LINKS[k]))+'<p><b>À retenir.</b> Relier la fonction normale au mécanisme, puis à une mesure et à une décision dont les limites restent explicites.</p></div>'
  # Le premier ilot de sémiologie porte lui-même le h3 exact et les neuf marqueurs restent indépendants.
  content=body if k=='semio' else f'<section class="ilot" id="d63-s-{k}-cours">{body}</section>'
  hide='' if k=='semio' else ' hidden'
  bar+=f'<div class="sci" id="d63-s-{k}" role="tabpanel" aria-labelledby="d63-tab-{k}"{hide}>{content}{bridge}<button class="pareto-btn ui" data-k="pareto-d63-{k}">▲ Loi de Pareto — {title}</button></div>'
 return bar+'</div><div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div></div>'
