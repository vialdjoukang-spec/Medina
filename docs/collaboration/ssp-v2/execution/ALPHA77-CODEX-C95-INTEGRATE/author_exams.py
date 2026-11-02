"""Examens complémentaires et cinq applications natives corrigées."""
from common import sec,table,w,original

sec('e-1','Prescrire selon la question clinique',f'''
<p>Le bilan initial doit fournir une réponse assez rapide pour les urgences et assez complète pour la classification. Une collection de tests sans question peut retarder l’interprétation ; une analyse trop étroite peut manquer une catégorie déterminante. Le centre coordonne la disponibilité des cellules et les priorités du laboratoire.</p>
{table(['Question','Examen','Ce que le résultat ne dit pas seul'],[
['Existe-t-il une cytopénie ou une population circulante anormale ?','Numération, différentiel, frottis.','Une numération normale ou sans blaste ne démontre pas une moelle normale.'],
['Quelle population médullaire est présente ?','Aspiration, morphologie ; biopsie selon contexte/qualité.','Le pourcentage de blastes ne suffit pas à attribuer la lignée.'],
['Quelles lignées sont définies ?','Cytométrie avec panel, contrôles et marqueurs intracellulaires adaptés.','CD13, CD33, CD7 ou CD34 isolés ne font pas une LAPM.'],
['Une catégorie génétique change-t-elle le diagnostic ?','Caryotype, FISH et analyses moléculaires hiérarchisées.','Un test ciblé négatif n’exclut pas toute anomalie génétique.'],
['Y a-t-il coagulopathie ou risque de lyse ?','Plaquettes/coagulation ; urate, ions, créatinine, LDH, diurèse.','Un urate normal ne suffit pas à exclure toutes les composantes de lyse.'],
['Existe-t-il une atteinte extramédullaire ou neurologique ?','Examen et imagerie/prélèvements ciblés ; bilan du système nerveux selon protocole.','Une TDM ne remplace pas la caractérisation cellulaire ; ponction lombaire non automatique si risque procédural.'],
['Comment suivre la réponse ?','Moelle et MRD à temps définis, avec cible et sensibilité documentées.','Une MRD négative n’équivaut pas à absence absolue de maladie.']])}
<p>Les prélèvements de référence sont particulièrement utiles avant le traitement lorsque cela est réalisable sans retarder les soins indispensables. Ils permettent de conserver le phénotype initial, une cible moléculaire et les éléments de comparaison à la rechute. Un traitement déjà administré doit être signalé au laboratoire.</p>
<p>Le bilan préthérapeutique explore aussi les fonctions d’organe et les risques infectieux selon le protocole. Le typage et la recherche de donneur se discutent si une allogreffe est envisagée ; ils ne transforment pas à eux seuls la greffe en décision déjà acquise. La pertinence du test dépend de la stratégie qu’il peut modifier.</p>
''','AML','ALL','WHO','FLOW','ALAL','FASTURTEC')

sec('e-2','Lire un chiffre avec son unité et sa finalité',f'''
<p>Les repères HUG2019 lus pour l’adulte sont Hb140–180g/L chez l’homme et120–160g/L chez la femme, leucocytes4–11G/L, plaquettes150–350G/L. Ils servent à comprendre le bilan et restent datés ; les intervalles du laboratoire du patient prévalent. Ils ne sont ni des normes pédiatriques ni des seuils transfusionnels.</p>
{table(['Nombre','Objet mesuré','Erreur à éviter'],[
['≥20 %','Total de blastes néoplasiques pour LALA dans les cadres étudiés.','Le transférer à toute LMA génétiquement définie ou en faire un préalable à l’urgence LAP.'],
['>50 % de l’intensité normale','Repère OMS de certains marqueurs, dont MPO/CD3/CD19 selon contrôles appropriés.','Le lire comme50 % des cellules positives.'],
['5 %','Seuil ICC de composante mineure dans le contexte bilinéaire décrit.','L’imposer à l’OMS ou compter des précurseurs normaux comme leucémiques.'],
['<5 % de blastes médullaires','Un des éléments de RC morphologique/hématologique, selon protocole.','En déduire MRD négative ou guérison.'],
['10⁻⁴ =0,01 %','Sensibilité moléculaire minimale de MRD soulignée par Onkopedia LLA.','La confondre avec0,1 % =10⁻³ de certaines indications thérapeutiques.'],
['100G/L de leucocytes','Repère souvent associé à l’hyperleucocytose.','Exclure une leucostase symptomatique sous ce chiffre.'],
['0,20mg/kg/j','Dose pondérale de rasburicase dans la fiche suisse.','Confondre mg/kg, mg/m² et mg/mL.']])}
<p><b>Exemple fictif :</b> dans un prélèvement de200cellules évaluables,60blastes représentent30 %. Ce calcul suppose que le dénominateur et les cellules aient été correctement définis. Il ne donne ni l’intensité de MPO ni la proportion d’une lignée sur un diagramme différent.</p>
<p>Autre exemple : une MRD de0,02 % dépasse0,01 % et vaut2×10<sup>−4</sup>. La décision dépend pourtant du temps du protocole, de la méthode et du seuil clinique retenu ; le calcul ne suffit pas à choisir le traitement. Une incertitude préanalytique ou un échantillon pauvre doit rester visible dans le compte rendu.</p>
''','HUG','WHO','FLOW','ALL','AML','FASTURTEC')

sec('e-3','Interpréter le panel et les méthodes génétiques',f'''
<h3>Un panel construit pour éviter les faux raccourcis</h3>
<p>La comparaison aux cellules normales aide à distinguer expression faible, forte et maturation coordonnée. Le compte rendu doit identifier la population analysée et ne pas additionner des positivités provenant de cellules différentes comme si elles appartenaient toutes au même blaste.</p>
{table(['Profil','Lecture intégrée','Étape complémentaire'],[
['CD19 fort + CD22 fort + MPO définissante','Profil B/myéloïde possible sur une même population.','Vérifier autres critères, génétique et exclusions.'],
['CD19 fort + marqueurs B + CD13 isolé','Lignée B avec marqueur associé myéloïde possible.','Ne pas appeler LAPM sans critère myéloïde définissant.'],
['CD7 + CD34, sans CD3 définissant','Immaturité et marqueur associé, pas preuve T suffisante.','Panel étendu et diagnostics différentiels.'],
['MPO absente, deux marqueurs monocytaires concordants','Différenciation monocytaire possible dans le cadre approprié.','Intégrer morphologie, autres populations et classification.'],
['Aucun marqueur de lignée après panel complet','LAI possible si exclusions satisfaites.','Rechercher catégories génétiques et différenciations rares.']])}
<p>Le caryotype montre des anomalies à l’échelle chromosomique ; FISH teste des régions choisies ; PCR et séquençage ont leurs cibles et limites. Le laboratoire choisit des méthodes complémentaires selon l’urgence et le spectre recherché. Une fusion peut être importante pour la classification, le choix d’un médicament et le suivi, sans répondre de façon identique à ces trois usages.</p>
<p>Si BCR::ABL1 est détecté, rechercher le contexte de LMC avant de conclure à une LAPM de novo. Si une mutation liée à la myélodysplasie est détectée, préciser OMS ou ICC et intégrer l’histoire. Si le phénotype change à la rechute, comparer au clone initial et élargir les analyses pertinentes.</p>
<p>Les images originales des onglets clinique et scientifique montrent des exemples publiés, pas une bibliothèque exhaustive de tous les profils possibles. Elles aident à apprendre la lecture des axes, contrôles et populations ; elles ne remplacent pas l’interprétation spécialisée d’un cas réel.</p>
''','WHO','FLOW','ALAL')

sec('e-4','Préanalytique, réponse et discordances',f'''
<p>Un résultat fiable commence avant la machine. Identité, heure, type de prélèvement, traitement reçu, quantité cellulaire et transport conditionnent l’analyse. Une moelle diluée par du sang ou un échantillon pauvre peut réduire la capacité à détecter une maladie résiduelle. Le rapport doit rendre cette limite visible.</p>
<p>La mesure d’urate sous rasburicase illustre un piège particulier : l’enzyme continue de dégrader l’urate après le prélèvement. La fiche Fasturtec impose tube hépariné prérefroidi, glace, centrifugation à4°C et dosage dans les4heures. Une valeur très basse dans un tube resté à température ambiante ne constitue donc pas une preuve suffisante de contrôle métabolique.</p>
<p>Pour la MRD, conserver cible initiale, méthode, sensibilité et calendrier. Le marqueur peut être immunophénotypique ou moléculaire ; il doit rester informatif dans le contexte du traitement. Après un traitement ciblant CD19, une analyse trop centrée sur cet antigène peut manquer une évolution de lignée.</p>
<p>Une discordance se résout par la confrontation des données : qualité des échantillons, cellules réellement mesurées, méthode, cible et évolution clinique. Il n’est pas logique de choisir automatiquement le résultat le plus rassurant ou de moyenner deux tests qui ne mesurent pas la même chose.</p>
<div class="key"><b>À retenir.</b> Le compte rendu utile relie résultat, limite et conséquence. Il indique ce qui a été démontré, ce qui reste probable et l’examen supplémentaire qui peut changer la décision. La surveillance doit rester proportionnée au risque et au protocole.</div>
''','ALL','ALAL','FASTURTEC','FLOW')

def quiz(title,question,answers,explain):
 return '<div class="quiz ui"><p><b>'+title+'</b> '+question+'</p>'+''.join(f"<button data-ok=\"{int(i==0)}\">{txt.replace('MPO','myéloperoxydase').replace('BCR::ABL1','la fusion observée')}</button>" for i,txt in enumerate(answers))+'<p class="fb" hidden>'+explain+'</p></div>'
sec('e-5','Cinq cas pour vérifier le raisonnement',
'''<p>Vignettes fictives. Choisir une réponse puis lire le raisonnement, y compris lorsqu’elle paraît évidente. Les cas vérifient une décision et ses limites, sans simuler une prescription personnalisée.</p>'''+
quiz('Cas1 — marqueurs','Des lymphoblastes B expriment CD19/CD22 et une faible MPO uniforme, sous le repère de lignée, sans profil monocytaire. Quelle conclusion est correcte ?',[
'A. Ne pas conclure à une LAPM sur la seule faible MPO ; intégrer le panel et les contrôles.',
'B. Toute MPO détectable impose une LAPM B/myéloïde.',
'C. La moitié des blastes doivent obligatoirement exprimer MPO pour toute classification.'],
'Réponse A. Intensité, configuration et contexte comptent. Le50 % OMS est une intensité relative au contrôle normal, pas un pourcentage universel de blastes positifs. La figure6 originale illustre une LLA-B à MPO faible aberrante.')+
quiz('Cas2 — génétique','Une leucémie blastique de phénotype mixte porte BCR::ABL1. Que faut-il encore examiner ?',[
'A. Le contexte d’une LMC en phase blastique, avec histoire et bilan intégré.',
'B. Rien : BCR::ABL1 prouve toujours une LAPM de novo.',
'C. Uniquement le code de facturation.'],
'Réponse A. La même fusion existe dans plusieurs contextes. Elle peut être une cible thérapeutique sans suffire à définir l’entité. Le diagnostic intégré précède l’application d’une stratégie propre à la maladie.')+
quiz('Cas3 — urgence','Un patient avec48G/L de leucocytes blastiques présente dyspnée hypoxémique et confusion. Quelle conduite de raisonnement est correcte ?',[
'A. Évaluation urgente de leucostase et des autres causes, sans attendre100G/L.',
'B. Exclure la leucostase car les leucocytes sont sous100G/L.',
'C. Attendre la fin du séquençage avant toute prise en charge.'],
'Réponse A. La leucostase est clinique et peut survenir sans hyperleucocytose extrême. Infection, hémorragie et cause métabolique restent à rechercher. Soins urgents et caractérisation se conduisent en parallèle.')+
quiz('Cas4 — réponse','Une moelle contient3 % de blastes et une MRD est détectée à0,02 % par une méthode appropriée. Quelle affirmation est correcte ?',[
'A. Morphologie et MRD décrivent des niveaux différents ; vérifier aussi les autres critères de réponse.',
'B. Moins de5 % prouve automatiquement la guérison.',
'C.0,02 % équivaut à2 % et impose le même traitement dans tout protocole.'],
'Réponse A.0,02 %=2×10⁻⁴. La décision dépend du moment, de la méthode et du protocole ; les numérations et sites extramédullaires comptent aussi dans la définition de réponse. Une MRD positive ne se code pas automatiquement comme réfractarité morphologique.')+
quiz('Cas5 — rasburicase','Sous rasburicase, un tube d’urate est resté à température ambiante avant analyse et le résultat est très bas. Quelle lecture est correcte ?',[
'A. Suspecter une baisse ex vivo et refaire selon la préanalytique de la fiche, avec surveillance des autres paramètres.',
'B. Arrêter toute surveillance de lyse puisque l’urate est bas.',
'C. Conclure que potassium et phosphate sont nécessairement normaux.'],
'Réponse A. La rasburicase reste active dans le tube. Tube hépariné prérefroidi, glace, centrifugation à4°C et dosage dans les4heures limitent cet artefact. Le traitement de l’urate ne corrige pas directement toutes les perturbations de lyse.'),
'WHO','FLOW','ALAL','AML','ALL','FASTURTEC')
