"""Six sciences, avec neuf étapes de sémiologie analytique."""
from common import refs,table,original,causal

def part(marker,title,body,*sources):
 return f'<section class="ilot" id="c95-semio-{marker}" data-semiology="{marker}"><h3>{title}</h3>{body}{refs(*sources)}</section>'

SEMIO='''<h2>Comment une lignée ambiguë produit-elle des signes observables ?</h2><p>La sémiologie analytique relie une fonction normale, sa perturbation, un signe et une décision. Elle évite deux raccourcis : déduire une lignée d’un symptôme et déduire l’absence de danger d’un chiffre isolé. Les neuf étapes suivantes complètent l’examen clinique de la monographie.</p>'''
SEMIO+=part('normal','1. Fonctions normales et réserves', '''
<p>La moelle renouvelle des cellules aux fonctions différentes. Les érythrocytes transportent l’oxygène grâce à l’hémoglobine ; les neutrophiles répondent rapidement à des agressions infectieuses ; les plaquettes issues des mégacaryocytes participent à l’obturation initiale d’une brèche vasculaire. La coagulation stabilise ensuite le clou plaquettaire par un réseau de fibrine.</p>
<p>Le nombre, la maturation et la fonction ne sont pas identiques. Une numération leucocytaire élevée peut être composée de cellules immatures malignes, tandis que le contingent utile de neutrophiles est insuffisant. De même, une saturation normale indique la proportion d’hémoglobine oxygénée, sans donner la quantité totale d’hémoglobine disponible.</p>
<p>La réponse à un défaut de production dépend de la réserve et de la vitesse d’installation. Une baisse rapide d’hémoglobine peut être mal tolérée avant qu’une adaptation ne se produise. Les maladies cardiorespiratoires modifient la tolérance ; le même résultat biologique n’impose donc pas la même lecture clinique chez tous les patients.</p>
''','NORMAL','NORMAL-RBC','NORMAL-WBC','NORMAL-HEMO','AML')
SEMIO+=original('marrow','c95-figure-semio-moelle')
SEMIO+=part('mecanisme','2. Perturbation : production insuffisante et infiltration', '''
<p>L’accumulation de cellules leucémiques perturbe l’hématopoïèse normale. Les cytopénies peuvent toucher une ou plusieurs lignées et coexister avec une hyperleucocytose blastique. L’infiltration d’organes, les interactions microvasculaires, l’infection et les perturbations métaboliques ajoutent d’autres mécanismes.</p>
<p>Une douleur osseuse peut accompagner une atteinte médullaire ; une organomégalie évoque une infiltration sans la prouver ; une fièvre peut être infectieuse ou liée à d’autres mécanismes. Le raisonnement ne consiste pas à attribuer tous les signes à une seule cause dès que le mot leucémie apparaît.</p>
<p>La LALA ajoute une difficulté de classification, mais ne crée pas un syndrome clinique spécifique permettant d’identifier B/myéloïde ou T/myéloïde au lit du malade. Le laboratoire caractérise les cellules ; l’examen clinique mesure le retentissement et la priorité des soins. Ces deux analyses se complètent.</p>
''','AML','ALL','ALAL')
SEMIO+=part('symptomes','3. Symptômes : décrire la plainte et sa chronologie', '''
<p>Pour la fatigue, préciser début, progression, effort déclenchant, dyspnée, douleur thoracique, vertiges et perte d’autonomie. Pour la fièvre, rechercher frissons, prises médicamenteuses, douleur buccale, toux, symptômes urinaires et date d’un éventuel traitement cytotoxique. L’absence d’un foyer évident ne rassure pas en neutropénie.</p>
<p>Un saignement se décrit par site, abondance, caractère spontané, répétition et tolérance. Épistaxis, gingivorragies, pétéchies et règles abondantes orientent vers une anomalie de l’hémostase primaire, sans exclure une coagulopathie associée. Céphalée nouvelle ou déficit focal imposent une évaluation urgente.</p>
<p>Rechercher les traitements antérieurs, l’exposition à un médicament ciblant CD19, l’histoire d’hémopathie et les résultats initiaux. Ces informations peuvent modifier la classification d’une rechute. Les préférences, l’entourage et l’accès au centre participent ensuite au plan de soins, sans remplacer la stabilisation immédiate.</p>
''','AML','ALL','RMS-NF','ALAL')
SEMIO+=part('signes','4. Signes physiques : constater sans surinterpréter', '''
<p>Pâleur, tachycardie et dyspnée sont compatibles avec une anémie, mais la tachycardie peut aussi être liée à fièvre, douleur, déshydratation ou autre cause. Le purpura suggère une extravasation sanguine ; sa présence ne donne pas le nombre de plaquettes et n’établit pas seule une CIVD.</p>
<p>Palper ganglions, foie et rate, examiner peau et muqueuses, rechercher foyer infectieux et signe neurologique. Une masse médiastinale exige une exploration adaptée si la clinique l’évoque. L’absence d’adénopathie ou d’organomégalie n’exclut pas une leucémie aiguë.</p>
<p>Noter état de conscience, fréquence respiratoire, saturation, pression, pouls, température et perfusion. Une réévaluation répétée peut montrer une aggravation avant le retour des analyses spécialisées. Les sources étudiées ne donnent pas de sensibilité/spécificité validée de ces signes pour reconnaître spécifiquement une LAPM.</p>
''','AML','ALL','RMS-NF')
SEMIO+=part('syndromes','5. Regrouper les syndromes sans les confondre', '''
<p>Le syndrome d’insuffisance médullaire regroupe les conséquences des cytopénies. Un syndrome tumoral décrit les infiltrations ou masses. Une leucostase est un syndrome de retentissement microvasculaire ; une lyse tumorale est un ensemble de perturbations métaboliques. Ils peuvent coexister et demander des réponses différentes.</p>
<p>Une personne présentant leucocytes48G/L, hypoxémie et confusion peut avoir une leucostase, une infection, une hémorragie ou une cause métabolique. Le chiffre inférieur à100G/L n’exclut pas la première hypothèse. Inversement, une hyperleucocytose sans manifestation ne démontre pas à elle seule la leucostase.</p>
<p>La suspicion de LAP avec coagulopathie constitue une filière particulière : traiter l’urgence et rechercher PML::RARA en parallèle. Le fait que la lignée finale ne soit pas encore connue ne justifie ni attente passive ni traitement identique pour toutes les leucémies.</p>
''','AML','APL','FASTURTEC')
SEMIO+=part('examens','6. Transformer une hypothèse en examen utile', '''
<p>Une numération avec différentiel quantifie les lignées circulantes ; le frottis décrit les cellules ; la moelle permet une analyse plus complète du compartiment de production. La cytométrie attribue des profils, et la génétique précise les catégories et cibles. Chaque examen répond à une question différente.</p>
<p>Devant un saignement, compléter la numération par la coagulation selon le contexte. Devant une menace métabolique, suivre urate, potassium, phosphate, calcium, créatinine et diurèse. Sous rasburicase, respecter la préanalytique du dosage d’urate ; un prélèvement non refroidi peut produire un résultat faussement bas.</p>
<p>Le laboratoire doit connaître la suspicion et l’urgence pour organiser les tests rapides. Le panel étendu n’est pas une raison de retarder l’antibiothérapie ou le traitement d’une LAP suspectée. Une ponction lombaire se programme en tenant compte du risque hémorragique et de la situation clinique.</p>
''','AML','ALL','FASTURTEC','RMS-NF')
SEMIO+=part('interpretation','7. Interpréter : unité, méthode et dénominateur', '''
<p>Le pourcentage de blastes porte sur un ensemble de cellules défini. L’intensité de MPO est un signal relatif comparé à des neutrophiles normaux. Le seuil OMS «50 %» de cette intensité ne signifie donc pas que50 % des blastes doivent être positifs. Confondre ces deux mesures peut créer une fausse lignée.</p>
<p>La MRD à0,01 % correspond à10<sup>−4</sup>. Un résultat négatif n’est interprétable que si la sensibilité et la qualité de l’échantillon sont suffisantes. Une RC morphologique sous5 % de blastes n’exclut pas une population résiduelle détectable à une échelle bien plus fine.</p>
<p>Enfin, les intervalles d’un laboratoire, les critères diagnostiques et les seuils d’intervention sont trois objets différents. Les repères adultes HUG2019 servent à comprendre les unités ; ils ne constituent ni normes nationales2026 ni seuils transfusionnels universels.</p>
''','WHO','FLOW','ALL','HUG')
SEMIO+=part('gravite','8. Gravité : la priorité peut précéder le nom final', '''
<p>Instabilité hémodynamique, détresse respiratoire, déficit neurologique, hémorragie importante ou perturbation métabolique grave justifient une prise en charge immédiate. L’équipe peut commencer soins de support et investigations en parallèle. Le diagnostic intégré affine ensuite la stratégie antileucémique.</p>
<p>Une fièvre après chimiothérapie avec neutropénie possible demande une évaluation urgente ; les signes locaux peuvent manquer. La revue suisse insiste sur une antibiothérapie rapide, avec choix actuel adapté aux résistances et au protocole local. La source2016 ne sert pas ici à figer une molécule en2026.</p>
<p>Le traitement lui-même crée des risques : syndrome de différenciation sous ATRA, occlusion sous ponatinib, hémolyse sous rasburicase chez une personne prédisposée, ou lyse après une thérapie efficace. Les consignes de surveillance doivent donc évoluer avec le traitement reçu.</p>
''','RMS-NF','APL','ICLUSIG','FASTURTEC','VENCLYXTO')
SEMIO+=part('synthese','9. Synthèse analytique et transmission', '''
<p>Une transmission utile commence par l’état du patient, les syndromes menaçants, les résultats discriminants et ce qui reste attendu. Par exemple : « suspicion de leucémie aiguë, saignement et thrombopénie, stabilité actuelle documentée, coagulation et caractérisation en cours, centre prévenu ». Elle ne remplace pas une incertitude par un diagnostic trop précis.</p>
<p>Après le bilan, préciser le type de LALA, les critères de lignée, la génétique et la stratégie de réponse/MRD. Le parcours prévoit les étapes de consolidation, les soins de support et les contacts d’urgence. À chaque réévaluation, relier un changement de résultat à une décision réelle.</p>
<p>La qualité du raisonnement se voit dans les limites conservées : absence de signes n’exclut pas la maladie, nombre élevé ne garantit pas la fonction, marqueur positif ne définit pas seul une lignée, et résultat négatif ne signifie pas absence absolue. Ces distinctions rendent l’information utile au patient et à l’équipe.</p>
''','ALAL','WHO','PROFILES17','ALL')

ANAT='''<h2>Moelle, sang et sites d’infiltration</h2>
<h3>Le compartiment normal</h3>
<p>La moelle rouge se situe dans les espaces du tissu osseux spongieux et contient les cellules hématopoïétiques avec leur environnement de soutien. Chez l’adulte, la répartition de la moelle active diffère de celle du jeune enfant ; le sang circulant n’en est qu’une sortie, pas une reproduction complète du contenu médullaire. Une anomalie de production peut donc être importante sans nombreux blastes dans le sang.</p>
<p>Les cellules souches et progéniteurs se différencient dans ce compartiment. Les lymphocytes T poursuivent une maturation thymique, tandis que les cellules B se développent initialement dans la moelle puis participent aux réponses dans les tissus lymphoïdes. Les cellules circulantes peuvent gagner d’autres territoires ; sang, moelle, ganglion et liquide cérébrospinal répondent ainsi à des questions anatomiques distinctes.</p>
'''+original('marrow','c95-figure-moelle-science')+'''
<h3>De la localisation au prélèvement</h3>
<p>Une aspiration médullaire fournit des cellules dispersées, utiles pour morphologie, cytométrie et génétique. La biopsie conserve une organisation tissulaire et peut aider lorsque l’aspiration est pauvre ou discordante. Ces techniques ne sont pas deux noms du même prélèvement ; le choix et leur complémentarité dépendent de la question.</p>
<p>Une infiltration ganglionnaire, splénique, cutanée ou du système nerveux peut accompagner une leucémie aiguë. Le site ne détermine pas automatiquement la lignée et une masse ne constitue pas un stade TNM de LALA. L’exploration neurologique se décide avec le protocole et la sécurité procédurale ; une ponction lombaire ne doit pas être banalisée chez une personne à risque hémorragique.</p>
<h3>Ce que l’image permet de comprendre</h3>
<p>La photographie montre de la moelle dans un support osseux. Elle permet de situer le tissu, sans identifier une cellule leucémique, mesurer une infiltration ni déduire un nombre de blastes. La barre de l’original est conservée sans conversion métrique, faute de valeur d’échelle fournie sur ce fichier. Cette limite distingue une illustration anatomique d’un examen diagnostique.</p>
'''+refs('NORMAL','NORMAL-WBC','NORMAL-IMAGE','AML','ALL')

HISTO='''<h2>Morphologie et cytométrie : deux langages complémentaires</h2>
<h3>Reconnaître maturation et population</h3>
<p>Le frottis permet d’apprécier taille, rapport nucléocytoplasmique, chromatine, nucléoles, granulations et éventuelles inclusions. Ces indices suggèrent une immaturité ou une différenciation, mais une morphologie semblable peut recouvrir des maladies différentes. Le diagnostic LALA exige une confrontation avec immunophénotype et génétique.</p>
<p>La cytométrie mesure des signaux sur des cellules sélectionnées. Les marqueurs de surface et intracellulaires demandent des méthodes adaptées ; les contrôles normaux servent à comparer les intensités. CD34 ou TdT renseignent l’immaturité, tandis que les combinaisons CD19/CD10/CD22/CD79a, CD3 spécifique et MPO/différenciation monocytaire contribuent à attribuer une lignée dans le cadre OMS.</p>
'''+original('mpal','c95-figure-mpal-science')+'''
<h3>Pourquoi un signal positif peut être insuffisant</h3>
<p>Une MPO faible uniforme sur une LLA-B ne démontre pas une seconde lignée. Le profil de maturation, les intensités et la présence d’autres marqueurs cohérents comptent. La figure6 de la revue illustre précisément un cas classé LLA-B malgré un faible signal MPO. À l’inverse, la figure3 montre une population remplissant les critères B/myéloïdes.</p>
<p>Dans une forme bilinéale, il faut démontrer que chaque population est aberrante. Une composante de lignée myéloïde distincte peut être classée selon les critères LMA appropriés même si elle n’exprime pas MPO ; il serait faux d’imposer le même raisonnement simplifié à toute population biphénotypique et à toute population séparée. Les divergences de taille minimale OMS/ICC doivent rester explicites.</p>
<h3>La LAI est un résultat d’exclusion documentée</h3>
<p>Absence de MPO n’équivaut pas à absence de toute lignée. Le panel doit examiner les alternatives lymphoïdes, monocytaires, mégacaryocytaires, érythroïdes et dendritiques pertinentes. La figure14 publiée montre des blastes CD34/CD117 sans profil définissant après ce bilan ; TdT n’y est pas fortement positive. Aucune image unique ne remplace les résultats complets du cas.</p>
'''+original('aul','c95-figure-lai-science')+refs('WHO','FLOW','ALAL')

PHYSIO='''<h2>Production, fonction et insuffisance médullaire</h2>
<h3>Régulation et maturation normales</h3>
<p>L’hématopoïèse associe renouvellement, engagement de lignée, maturation et élimination des cellules vieillies. Les besoins de l’organisme modulent la production par des signaux, dont l’érythropoïétine pour la lignée rouge. La réponse dépend cependant d’une moelle capable de produire et de ressources suffisantes ; un signal hormonal ne garantit pas une compensation efficace dans une moelle malade.</p>
<p>Le réticulocyte est une cellule rouge récemment libérée, encore porteuse de matériel résiduel. Sa mesure contribue à distinguer une production insuffisante d’une réponse régénérative dans le contexte d’une anémie. Elle ne diagnostique pas une leucémie à elle seule. L’hémoglobine porte l’oxygène ; la saturation mesure la fraction de sites occupés, et non le stock total de transport.</p>
<h3>Défense et hémostase</h3>
<p>Les neutrophiles migrent vers des signaux inflammatoires et participent à la phagocytose et à la destruction microbienne. Les lymphocytes B et T ont des fonctions immunitaires distinctes. Les blastes peuvent exprimer certains marqueurs de ces lignées sans avoir la fonction d’une cellule mature. Une hyperleucocytose blastique peut donc coexister avec une défense insuffisante.</p>
<p>Les plaquettes sont des fragments de mégacaryocytes. Leur adhésion et leur activation construisent un clou initial, renforcé par la fibrine. Une thrombopénie compromet cette première réponse, tandis qu’une coagulopathie peut altérer la stabilisation. Les mécanismes se superposent parfois, ce qui explique pourquoi numération plaquettaire et bilan de coagulation répondent à des questions complémentaires.</p>
'''+causal('c95-physio-causal','Une même moelle, plusieurs fonctions en défaut',[
'Production normale perturbée par la maladie',
'Érythrocytes, neutrophiles ou plaquettes insuffisants',
'Transport O₂, défense ou hémostase compromis',
'Tolérance clinique + bilan de chaque lignée',
'Soins de support et traitement causal adaptés'],
'Les trois fonctions ne chutent pas toujours avec la même intensité ; la numération leucocytaire totale ne mesure pas la défense immunitaire.')+'''
<h3>Le lien thérapeutique</h3>
<p>Traiter la maladie vise à restaurer une hématopoïèse utile, mais l’induction peut temporairement aggraver les cytopénies. Le soutien transfusionnel, la prévention infectieuse et la surveillance s’inscrivent donc dans le même parcours. Une récupération des numérations ne prouve pas seule l’absence de MRD ; la réponse doit être mesurée à plusieurs niveaux.</p>
'''+refs('NORMAL','NORMAL-RBC','NORMAL-WBC','NORMAL-HEMO','AML','ALL')

BIO='''<h2>Signal enzymatique, lyse et oxydation</h2>
<h3>MPO : fonction et lecture analytique</h3>
<p>La myéloperoxydase appartient au programme enzymatique de certaines cellules myéloïdes. En diagnostic, sa détection est un marqueur de différenciation ; l’intensité mesurée dépend de la méthode et des contrôles. Le seuil OMS relatif ne mesure ni l’activité antimicrobienne effective du blaste ni la proportion de cellules capables de défendre l’organisme.</p>
<p>Une expression faible peut être aberrante dans une LLA-B. La lecture doit conserver le profil global et les autres marqueurs, au lieu de traiter chaque signal comme une valeur binaire. Le laboratoire décide si le critère de lignée est rempli dans la classification annoncée.</p>
<h3>Catabolisme des acides nucléiques et urate</h3>
<p>Une destruction cellulaire importante libère des composants intracellulaires. Le catabolisme des purines contribue à la charge en acide urique, tandis que potassium et phosphate ont leurs propres conséquences. La fonction rénale conditionne l’élimination et peut être aggravée par ces perturbations ; la prévention exige une vision métabolique globale.</p>
<p>La rasburicase catalyse la conversion de l’urate en allantoïne plus soluble. Cette réaction produit aussi du peroxyde d’hydrogène, ce qui explique le risque oxydatif en déficit en G6PD. La méthémoglobine ne transporte pas l’oxygène de la même manière que l’hémoglobine fonctionnelle ; une complication oxydative impose une évaluation urgente et l’arrêt selon la fiche.</p>
'''+causal('c95-bio-causal','Une enzyme agit aussi après le prélèvement',[
'Rasburicase présente dans le sang prélevé',
'Dégradation de l’urate poursuivie dans le tube',
'Sans préanalytique adaptée : urate faussement bas',
'Tube prérefroidi, glace, centrifugation à 4 °C',
'Dosage dans les 4 heures selon fiche suisse'],
'Le refroidissement concerne la qualité de la mesure ; il ne remplace pas la surveillance des autres paramètres de lyse.')+'''
<h3>Unités et décision</h3>
<p>Une dose enmg/kg ne se confond pas avec une concentration enmg/mL ni une dose enmg/m². Le calcul doit préciser masse corporelle ou surface, puis préparation et durée de perfusion. De même,0,01 % et10<sup>−4</sup> décrivent la même proportion, tandis que0,1 % est dix fois plus élevé. Une erreur d’unité peut faire franchir artificiellement un seuil diagnostique ou thérapeutique.</p>
<p>La LDH peut augmenter avec renouvellement cellulaire ou lésion tissulaire ; elle n’est ni une preuve de LAPM ni une mesure directe de MRD. Son interprétation complète le bilan plutôt qu’elle ne remplace une analyse cellulaire. Le mécanisme biologique explique une mesure, mais ne suffit pas à lui donner une spécificité qu’elle n’a pas.</p>
'''+refs('WHO','FLOW','AML','FASTURTEC','ALL')

GEN='''<h2>Génome, programme de lignée et évolution clonale</h2>
<h3>Trois niveaux à distinguer</h3>
<p>Une anomalie constitutionnelle concerne la personne au-delà du clone tumoral ; une anomalie somatique est acquise dans une population cellulaire ; une anomalie clonale est partagée par des cellules apparentées. Un panel tumoral ne suffit pas à prouver une prédisposition familiale. Une question germinale demande une démarche spécifique et un prélèvement approprié.</p>
<p>Le caryotype explore des anomalies chromosomiques visibles à son niveau de résolution. Une FISH répond à une cible définie. Les analyses moléculaires recherchent des séquences, variants ou fusions selon leur conception. Un résultat négatif n’exclut pas une anomalie que le test ne couvre pas, et un caryotype normal n’est pas un génome sans altération.</p>
<h3>Les anomalies qui organisent le raisonnement LALA</h3>
<p>BCR::ABL1 produit une kinase de fusion et peut constituer une cible d’ITK ; il impose aussi le diagnostic différentiel de LMC blastique. KMT2A et ZNF384 réarrangés sont associés à des groupes biologiques particuliers. BCL11B peut être activé par une réorganisation régulatrice ; cela illustre l’importance des programmes d’expression, au-delà du simple changement de séquence codante.</p>
<p>Les mutations liées à la myélodysplasie et les antécédents peuvent conduire vers une LMA, mais les frontières et listes diffèrent entre OMS et ICC. RUNX1 est un exemple de divergence. Une anomalie cytogénétique quelconque ne signifie pas caryotype complexe ; la fréquence élevée d’anomalies dans une série n’autorise pas cette substitution.</p>
'''+causal('c95-gen-causal','Un clone peut présenter plusieurs programmes',[
'Anomalies fondatrices dans un progéniteur',
'Programmes de différenciation variables',
'Populations phénotypiques parfois différentes',
'Sélection et évolution possibles sous traitement',
'Rechute : recontrôler phénotype et parenté clonale'],
'Modèle explicatif issu des revues ; il ne prouve pas le mécanisme de chaque cas ni un risque chiffré universel.')+'''
<h3>Pourquoi la génétique aide au suivi</h3>
<p>Une cible moléculaire informative peut suivre le clone même si certains marqueurs de surface changent. Elle doit néanmoins rester liée à la maladie réellement mesurée, à la qualité du prélèvement et à la sensibilité. La discordance entre morphologie, cytométrie et génétique impose une interprétation intégrée.</p>
<p>Une cible ne donne pas automatiquement une indication de traitement : mutation sensible, contexte clinique, données d’efficacité, autorisation suisse et interactions comptent aussi. La génétique permet de poser une meilleure question thérapeutique ; elle ne dispense pas d’en vérifier la réponse clinique.</p>
'''+refs('WHO','ALAL','KARASEK','FLOW','GLIVEC','ICLUSIG')

LINKS={
'semio':('Relier fatigue, infection et saignement aux fonctions atteintes, puis rechercher les urgences.','Chaque examen répond à une question ; une intensité n’est pas un pourcentage de cellules.','Soins urgents et caractérisation avancent en parallèle, avec réévaluation.','Un signe oriente et mesure la gravité ; il ne définit pas une lignée.'),
'anat':('Moelle, sang et organes infiltrés peuvent donner des manifestations différentes.','Aspiration, biopsie et liquide cérébrospinal ne répondent pas à la même question.','Le site et le risque procédural modifient le parcours, pas le code seul.','Une photographie de moelle situe le tissu ; elle ne compte pas les blastes.'),
'histo':('Des symptômes semblables peuvent recouvrir LLA, LMA ou LALA.','Morphologie, intensité, panel, populations et génétique s’intègrent.','Une attribution erronée de seconde lignée peut orienter vers une stratégie inadaptée.','Marqueur associé, marqueur d’immaturité et marqueur définissant sont différents.'),
'physio':('Hyperleucocytose blastique et défense anti-infectieuse insuffisante peuvent coexister.','Différentiel, réticulocytes, plaquettes et coagulation examinent des fonctions distinctes.','Soutenir les fonctions pendant le traitement et mesurer leur récupération.','Nombre, maturation et fonction ne sont pas synonymes.'),
'bio':('Lyse et toxicité oxydative peuvent altérer rapidement les organes.','Préanalytique de l’urate, unités et autres électrolytes conditionnent l’interprétation.','Rasburicase traite l’urate, avec contre-indications ; elle ne corrige pas tous les composants de lyse.','Une mesure techniquement fausse peut masquer une urgence.'),
'gen':('Plasticité et évolution clonale expliquent certaines rechutes au phénotype différent.','Confronter couverture du test, contexte, cible et classification.','Une kinase de fusion peut être ciblée après vérification clinique et réglementaire.','Somatique, constitutionnel et clonal répondent à trois questions différentes.')}
def bridges(name):
 return '<div class="key">'+''.join('<p><b>'+label+'</b> '+text+'</p>' for label,text in zip(['Science → clinique.','Science → examen.','Science → traitement.','À retenir.'],LINKS[name]))+'</div>'
TABS=[('semio','Sémiologie fondamentale et analytique',SEMIO),('anat','Anatomie',ANAT),('histo','Histologie et cytométrie',HISTO),('physio','Physiologie',PHYSIO),('bio','Biochimie',BIO),('gen','Génétique',GEN)]
def sciences():
 bar='<div class="panel" id="pS" hidden><div class="sci-bar ui" role="tablist">'
 for key,title,_ in TABS:
  bar+=f'<button id="c95-tab-{key}" role="tab" aria-selected="{str(key=="semio").lower()}" aria-controls="c95-s-{key}" data-s="c95-s-{key}">{title}</button>'
 bar+='</div><div class="chap-body sci-body">'
 for key,title,body in TABS:
  hide='' if key=='semio' else ' hidden'
  bar+=f'<div class="sci" id="c95-s-{key}" role="tabpanel" aria-labelledby="c95-tab-{key}"{hide}><section class="ilot" id="c95-s-{key}-cours">{body}{bridges(key)}<button class="pareto-btn ui" data-k="pareto-c95-{key}">▲ Loi de Pareto — {title}</button></section></div>'
 return bar+'</div><div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div></div>'
