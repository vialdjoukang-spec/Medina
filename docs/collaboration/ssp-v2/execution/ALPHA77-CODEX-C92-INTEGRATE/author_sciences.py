"""Sciences C92 : raisonnement clinique et neuf unités sémiologiques explicites."""
from common import refs,table,original,causal

def unit(marker,title,body,*sources):
 return f'<section class="ilot" id="c92-semio-{marker}" data-semiology="{marker}"><h3>{title}</h3>{body}{refs(*sources)}</section>'

SEMIO=unit('normal','Pour la leçon : quelle est la sémiologie fondamentale et analytique ?', '''
<h4>Partir des fonctions avant de nommer la maladie</h4>
<p>La moelle produit les éléments sanguins dans un environnement organisé. Les hématies transportent l’oxygène, les plaquettes participent à l’hémostase et les leucocytes assurent différentes fonctions de défense. La maturation et la production sont régulées : le nombre total de cellules ne suffit pas à décrire leur fonction. Une augmentation de cellules anormales peut donc coexister avec un défaut de défense et une réduction des lignées normales.</p>
<p>Cette organisation permet de comprendre trois groupes de manifestations : défaut d’une lignée normale, accumulation/infiltration de cellules anormales et conséquences systémiques du clone ou du traitement. Anémie, saignement et infection ne sont pas interchangeables, même s’ils peuvent survenir ensemble. Une masse extramédullaire, une splénomégalie et une coagulopathie ajoutent des mécanismes différents à l’insuffisance médullaire.</p>
<p>La sémiologie relie ainsi fonction, mécanisme, signe, examen et décision. C92 désigne une famille de codage, pas un syndrome clinique unique. Une LAM, une LPA, une LMC et un sarcome myéloïde peuvent commencer par des symptômes différents et appeler des urgences différentes. Le diagnostic précis ne doit pas être anticipé à partir du seul code.</p>
''','NORMAL','NORMAL-WBC','NORMAL-HEMO','WHO','OFS')

SEMIO+=unit('signs','2. Décrire les symptômes et les signes', '''
<p>Interroger le début et la vitesse d’évolution de la fatigue, la dyspnée, les palpitations, les infections et les saignements. Distinguer ecchymoses, pétéchies, épistaxis, gingivorragies et saignement profond ; préciser abondance, spontanéité, médicaments et antécédents. Une fièvre se décrit avec son contexte et ses signes de gravité, sans l’attribuer d’emblée à la tumeur.</p>
<p>Rechercher perte de poids involontaire, sueurs nocturnes, gêne ou satiété précoce sous les côtes gauches, douleurs osseuses et masses. Dans la LMC, une découverte fortuite à l’hémogramme est possible : l’absence de symptôme ne prouve pas l’absence de maladie. À l’inverse, fatigue et amaigrissement sont peu spécifiques et ne démontrent pas une leucémie.</p>
<p>L’examen apprécie conscience, paramètres vitaux, perfusion, état respiratoire, peau et muqueuses, adénopathies, foie, rate et anomalies focales. Une hypertrophie gingivale ou une lésion cutanée peut orienter vers une infiltration, mais exige une confirmation adaptée. Documenter ce qui est réellement observé ; ne pas ajouter un signe classique absent chez le patient pour compléter une liste.</p>
''','ONKO-AML','ELN-AML','ELN-CML','CHUV-CML','SARCOMA')

SEMIO+=unit('mechanisms','3. Relier les manifestations à leurs mécanismes', '''
<p>Dans la LAM, une prolifération avec défaut de différenciation peut réduire l’hématopoïèse efficace. Une baisse de l’hémoglobine réduit le transport d’oxygène ; une baisse ou une anomalie des plaquettes contribue au saignement ; un déficit de neutrophiles fonctionnels expose aux infections. Ces relations expliquent des tendances, sans déterminer à elles seules la gravité individuelle.</p>
<p>Dans la LPA, une coagulopathie complexe expose notamment à des hémorragies graves. Le risque n’est pas résumé par le nombre de plaquettes. Dans une hyperleucocytose, les propriétés des cellules et leurs interactions microvasculaires peuvent contribuer à une leucostase ; le nombre total ne suffit donc pas à prévoir dyspnée ou atteinte neurologique. La lyse cellulaire, spontanée ou après traitement, libère des constituants qui perturbent urate, potassium, phosphate et fonction rénale.</p>
<p>Dans la LMC, la prolifération granulocytaire conserve une part de maturation. Une grande numération peut coexister avec peu de symptômes initiaux. La rate peut augmenter de volume et devenir symptomatique. Une masse myéloïde extramédullaire produit un effet local, mais peut appartenir à une maladie systémique ; mécanisme local et nature hématologique doivent être considérés ensemble.</p>
''','ELN-AML','ONKO-APL','ELN-CML','SARCOMA')

SEMIO+=unit('examination','4. Examiner et choisir les premières mesures', '''
<p>La première question est la stabilité : détresse respiratoire, trouble neurologique, saignement actif ou état septique demandent une prise en charge urgente. L’hémogramme avec formule et le frottis décrivent ensuite les lignées et les cellules. Comparer aux résultats antérieurs et demander une lecture spécialisée des alertes morphologiques.</p>
<p>Le bilan initial recherche aussi coagulation perturbée, atteinte rénale, risque de lyse et complications. Si une LPA est suspectée, la recherche rapide de PML::RARA et la prise en charge de la coagulopathie se déroulent sans attendre la fin de tout le bilan génétique. La ponction médullaire, la biopsie, la cytométrie et la génétique répondent à des questions complémentaires, avec une répartition adaptée des prélèvements.</p>
<p>Devant une masse, la topographie et le retentissement guident l’imagerie et l’urgence. Une compression médullaire n’a pas le même délai qu’une petite lésion cutanée stable. Le prélèvement tissulaire doit permettre l’immunohistochimie et, si nécessaire, la génétique ; un résultat qualifié seulement de « petites cellules » ne suffit pas à conclure à un sarcome myéloïde.</p>
''','ELN-AML','ONKO-APL','ELN-CML','SARCOMA','CH-SARCOMA')

SEMIO+=unit('interpretation','5. Interpréter ensemble, sans raccourci', '''
<p>Une leucocytose ne prouve pas une leucémie et une numération leucocytaire normale ne l’exclut pas. Un pourcentage de blastes doit être rattaché au sang ou à la moelle, à une méthode et à la classification utilisée. La règle de 20 % conserve une place importante mais comporte des exceptions génétiques ; OMS et ICC ne formulent pas toutes ces exceptions de la même façon.</p>
<p>Un corps d’Auer soutient la différenciation myéloïde, sans identifier à lui seul PML::RARA. Une PCR ciblée négative ne remplace pas la vérification d’une discordance avec caryotype ou FISH ; des transcrits atypiques peuvent échapper à une méthode. Pour une LMC, la démonstration de BCR::ABL1 est centrale, tandis qu’un MDS/MPN avec neutrophilie exige son exclusion et d’autres critères.</p>
<p>Après traitement, rémission morphologique, récupération des numérations et maladie résiduelle mesurable décrivent trois dimensions. Une moelle à moins de 5 % de blastes ne prouve pas seule une rémission complète ; une MRD négative signifie absence de signal détecté dans les conditions de l’analyse, pas absence certaine de toute cellule leucémique.</p>
''','WHO','ELN-AML','ELN-CML','MLL','ONKO-APL')

SEMIO+=unit('differentials','6. Construire les diagnostics différentiels', '''
<p>Selon le tableau, discuter réaction infectieuse ou inflammatoire, effet médicamenteux, autres néoplasies myéloprolifératives, SMD/MDS-MPN, leucémie lymphoblastique et autres causes de cytopénies. La chronologie, la persistance, les cellules observées, les autres lignées et la génétique resserrent les hypothèses. Un traitement récent peut aussi modifier le frottis et les numérations.</p>
<p>Dans une prolifération neutrophilique, BCR::ABL1, dysgranulopoïèse, proportion de précurseurs et exclusions moléculaires aident à distinguer LMC, MDS/MPN avec neutrophilie et autres entités. Dans une masse, lymphome et autres tumeurs font partie des diagnostics concurrents : la morphologie isolée ou un marqueur peu spécifique peut tromper.</p>
<p>Une maladie connue ne protège pas d’une complication indépendante. Une dyspnée chez un patient leucémique peut notamment refléter infection, anémie, surcharge, hémorragie ou leucostase selon le contexte. Reconnaître plusieurs mécanismes évite de retarder un traitement urgent en attribuant tout au clone.</p>
''','WHO','ELN-AML','ELN-CML','MLL','SARCOMA')

SEMIO+=unit('urgency','7. Identifier ce qui ne peut pas attendre', '''
<p>Suspecter et prendre en charge sans délai une LPA avec coagulopathie, une leucostase symptomatique, une lyse tumorale, une infection grave en contexte neutropénique, une hémorragie menaçante ou une compression neurologique. L’appel spécialisé et la stabilisation se font en parallèle du diagnostic ; ils ne sont pas reportés jusqu’à obtention de toutes les analyses.</p>
<p>Le traitement lui-même crée des urgences : syndrome de différenciation, arythmie avec QT prolongé, réaction de perfusion ou toxicité neurologique. La date du traitement et des changements de dose participe à l’interprétation. Les autres causes, notamment infection, ne disparaissent pas parce qu’une toxicité est plausible.</p>
<p>Éviter deux automatismes dangereux : appliquer une leucaphérèse à toute hyperleucocytose, et transfuser les hématies sans discuter le contexte de leucostase. Dans la LPA, support hémostatique et éviction des gestes invasifs non indispensables sont prioritaires. Chaque décision doit être contextualisée plutôt que déduite d’un seuil unique.</p>
''','ELN-AML','ONKO-APL','TRISENOX','TIBSOVO','VANFLYTA','CYTOSAR')

SEMIO+=unit('limits','8. Reconnaître les limites de ce que l’on sait', '''
<p>Les photographies montrent des champs sélectionnés. Elles ne fournissent ni numération absolue, ni décompte représentatif, ni génotype. Les données de cohorte ou les survies médianes ne prédisent pas le devenir d’une personne. Un taux d’incidence européen ne devient pas une incidence suisse, et une statistique regroupant toutes les leucémies n’est pas celle de C92 seul.</p>
<p>Le risque ELN dépend de la version et du traitement : la classification de 2022 pour traitements intensifs n’est pas interchangeable avec celle de 2024 pour certains traitements moins intensifs. Les entités rares disposent souvent de données rétrospectives. Les divergences entre recommandations et FI doivent être nommées, pas masquées derrière un seul tableau.</p>
<p>L’examen clinique oriente la probabilité et la gravité, mais les sources consultées ne donnent pas ici une sensibilité/spécificité universelle de chaque signe pour C92. La leçon ne transforme pas cette absence de mesure en chiffre inventé. Les cas pédagogiques sont fictifs ; leur réponse ne remplace pas l’évaluation d’une personne réelle.</p>
''','ELN-AML','ELN-LOW','ELN-CML','EBMT','OFS-CANCER','AUER-IMAGE','APL-IMAGE','CML-IMAGE')

SEMIO+=unit('sources','9. Sources et portée des liens cliniques', '''
<p>Le codage repose sur la CIM-10-GM française publiée par l’OFS. La classification biologique s’appuie sur l’OMS 2022 et les distinctions ICC exposées par l’ELN. Les recommandations ELN 2022/2024 pour LAM et ELN 2025 pour LMC, les recommandations Onkopedia lues et les informations professionnelles suisses datées structurent les décisions décrites.</p>
<p>Le chapitre suisse CHUV de LMC sert pour manifestations et diagnostic, pas comme source thérapeutique suffisante pour 2026. Le résumé institutionnel suisse sur le sarcome ORL est identifié comme résumé, avec complément par une revue européenne. EBMT et MLL éclairent les entités rares et leurs limites. Les références sont attribuées aux passages ; aucune lecture intégrale de chaque document ni validation médicale humaine n’est revendiquée.</p>
''','OFS','WHO','ELN-AML','ELN-LOW','ELN-CML','ONKO-AML','ONKO-APL','CHUV-CML','CH-SARCOMA','SARCOMA','EBMT','MLL')

SEMIO+=causal('c92-causal-semio','Du signe à la décision',[
'Décrire symptôme, chronologie et gravité',
'Relier aux fonctions perturbées',
'Comparer les mécanismes possibles',
'Choisir examen et traitement urgent utiles',
'Réévaluer avec les résultats et la réponse'],
'Schéma de raisonnement ; aucun signe isolé ne démontre toutes les maladies de C92.')

ANAT='''<h3>Moelle, sang et tissus : trois espaces à relier</h3>
<p>Le tissu hématopoïétique médullaire occupe des espaces au sein de l’os. Son organisation permet renouvellement, maturation et passage des cellules vers la circulation. La photographie macroscopique ci-dessous localise ce compartiment entre les travées ; elle ne montre ni la hiérarchie des cellules souches, ni les marqueurs de surface, ni les anomalies génétiques. La structure visible sert de repère spatial à un fonctionnement qui nécessite d’autres méthodes pour être étudié.</p>
<p>Le sang circulant est un échantillon accessible, mais il n’est pas une copie complète de la moelle. Des cellules anormales peuvent prédominer dans la moelle sans être nombreuses dans le sang. À l’inverse, une forte circulation de cellules renseigne sur leur présence, sans décrire l’architecture médullaire. Cette différence explique pourquoi numération, frottis, aspiration et biopsie ne sont pas redondants.</p>
'''+original('marrow','c92-science-marrow')+'''
<p>L’aspiration fournit des cellules dissociées pour morphologie, cytométrie et génétique. La biopsie conserve une architecture : cellularité, répartition d’un infiltrat et environnement tissulaire. Un prélèvement hémodilué ou pauvre peut sous-représenter la population recherchée. La qualité et le site du prélèvement doivent donc accompagner l’interprétation, surtout lorsque le résultat paraît incompatible avec la clinique.</p>
<p>La rate participe à la circulation et au traitement des éléments sanguins ; elle peut augmenter de volume dans certaines néoplasies myéloïdes. Une gêne sous-costale gauche ou une satiété précoce peut conduire à son examen. La splénomégalie n’est cependant pas spécifique de LMC : infections, maladies hépatiques et autres hémopathies font partie des contextes possibles. Le mécanisme et l’étiologie ne se déduisent pas du seul volume.</p>
<p>Un sarcome myéloïde correspond à une masse de cellules myéloïdes immatures en dehors de la moelle. Le site détermine une partie des symptômes : peau, tissus mous, os, structures ORL ou autres organes ne donnent pas la même présentation. Une lésion rachidienne avec compression impose une priorité différente d’une masse sans retentissement immédiat. Pourtant, le traitement n’est pas uniquement déterminé par la topographie : la nature systémique potentielle justifie un bilan médullaire et moléculaire.</p>
<p>L’imagerie répond à des questions anatomiques : localisation, extension, compression, sites multiples et accessibilité d’une biopsie. Elle ne remplace pas l’identification du type cellulaire. Une réponse locale après traitement ne prouve pas seule la disparition du clone dans les autres compartiments. Le raisonnement doit conserver la distinction entre cible visible, maladie systémique et mesure de réponse.</p>
<p>Cette carte des compartiments guide enfin les gestes. La coagulopathie d’une LPA modifie le risque d’un prélèvement invasif ; l’urgence du diagnostic doit être conciliée avec sa sécurité. L’absence d’une image spectaculaire n’autorise pas à retarder une prise en charge si le sang, la coagulation et l’état clinique indiquent une urgence.</p>
'''+refs('NORMAL','NORMAL-IMAGE','ELN-AML','ELN-CML','SARCOMA','CH-SARCOMA','ONKO-APL')

HISTO='''<h3>De la cellule normale au clone : regarder sans surinterpréter</h3>
<p>La maturation granulocytaire transforme progressivement noyau, chromatine et cytoplasme. Dans le sang normal, les éléments matures ont des fonctions différentes de celles des précurseurs médullaires. Le frottis permet de reconnaître des catégories morphologiques, mais les limites entre certaines cellules exigent expérience, coloration adaptée et décompte représentatif.</p>
<p>Un blaste se décrit avec taille, rapport nucléocytoplasmique, chromatine, nucléoles et cytoplasme. Aucun de ces caractères isolés ne suffit à définir toute une lignée ou toute une entité. La leucémie peut modifier les aspects habituels et exprimer des marqueurs aberrants. Morphologie, cytométrie et génétique se complètent ; un désaccord doit être résolu, pas effacé.</p>
'''+original('auer','c92-science-auer')+'''
<p>Les corps d’Auer sont des inclusions cytoplasmiques associées à la différenciation myéloïde. Leur présence est un indice utile, pas une analyse moléculaire. Les deux flèches rouges de l’original ont été conservées ; elles ne transforment pas le champ en décompte de blastes. Une image sélectionnée peut illustrer un signe sans représenter la proportion de cellules porteuses dans toute la moelle.</p>
'''+original('apl','c92-science-apl')+'''
<p>La LPA hypogranulaire montre pourquoi une règle visuelle trop simple est dangereuse. Les granulations peuvent être peu évidentes et les noyaux irréguliers. La provenance de la figure précise le diagnostic et la coloration ; aucun corps d’Auer n’est affirmé dans ce champ. En situation clinique, la morphologie suspecte déclenche une recherche rapide de PML::RARA et la gestion de la coagulopathie, sans attendre une « photographie parfaite ».</p>
'''+original('cml','c92-science-cml')+'''
<p>Dans la LMC, un frottis peut montrer un continuum de maturation granulocytaire. Le champ choisi illustre cette diversité, pas la valeur absolue des leucocytes ni la preuve de BCR::ABL1. La basophilie, lorsqu’elle est documentée par un décompte, participe au bilan ; elle n’est pas assignée ici à une cellule incertaine pour fabriquer un repère.</p>
<p>La dysplasie désigne des anomalies morphologiques de maturation. Elle peut être importante dans un MDS/MPN avec neutrophilie, mais la dysplasie seule ne définit plus toutes les catégories modernes de LAM liées à la myélodysplasie. Le contexte, les anomalies cytogénétiques et les mutations déterminées par la classification choisie doivent être intégrés. Le changement de nom n’est donc pas seulement un changement d’étiquette.</p>
<p>Enfin, le décompte dépend du matériel : sang, aspiration médullaire, apposition ou tissu. Les critères de réponse utilisent des seuils et des exigences distincts du simple diagnostic morphologique. La photographie pédagogique ne peut ni démontrer une rémission, ni établir une maladie résiduelle négative. Son rôle est d’apprendre à poser la question que le laboratoire pourra mesurer.</p>
'''+refs('NORMAL-WBC','ELN-AML','ONKO-APL','ELN-CML','WHO','MLL','AUER-IMAGE','APL-IMAGE','CML-IMAGE')

PHYSIO='''<h3>Produire, différencier, défendre : les fonctions ne se résument pas au nombre</h3>
<p>L’hématopoïèse normale renouvelle en continu les cellules sanguines. Production, maturation, survie et sortie vers le sang contribuent à la numération observée. Une concentration mesurée à un instant résulte donc de plusieurs processus ; elle ne mesure pas directement la vitesse de production ni la qualité fonctionnelle de chaque cellule.</p>
<p>Dans une LAM, l’expansion d’un clone et le défaut de différenciation peuvent réduire la production normale. Les conséquences suivent les lignées : transport d’oxygène pour les hématies, défense pour les neutrophiles et hémostase pour les plaquettes. Une leucocytose faite de cellules anormales ne compense pas automatiquement un défaut de défense. Le nombre total et la formule doivent être interprétés ensemble.</p>
'''+causal('c92-causal-fonction','De la prolifération au signe clinique',[
'Clone myéloïde anormal et maturation perturbée',
'Hématopoïèse normale moins efficace',
'Défaut de transport, défense ou hémostase',
'Anémie, infection ou saignement à caractériser',
'Examens et prise en charge selon mécanisme'],
'Chaîne explicative simplifiée ; plusieurs mécanismes peuvent coexister chez une même personne.')+'''
<p>L’anémie diminue la capacité de transport d’oxygène ; le retentissement dépend aussi de la vitesse d’installation et des réserves cardiorespiratoires. Une saturation normale ne mesure pas la quantité totale d’hémoglobine disponible. La neutropénie modifie la réponse à l’infection ; l’absence de pus ou de forte réaction locale n’exclut pas une infection grave. La thrombopénie contribue au saignement, mais une coagulopathie peut ajouter un risque indépendant.</p>
<p>La LPA illustre ce dernier point. Le désordre de coagulation n’est pas expliqué uniquement par le remplacement médullaire. Il exige des mesures spécifiques, une surveillance rapprochée et un traitement rapide du mécanisme leucémique. Une amélioration d’un paramètre isolé ne suffit pas à conclure que le risque hémorragique est résolu.</p>
<p>Dans la LMC, la maturation relativement conservée rend possible une accumulation importante de granulocytes avec un début parfois peu symptomatique. L’inhibition de BCR::ABL1 réduit l’avantage du clone et permet une réponse hématologique, puis moléculaire. Ces étapes n’ont pas le même délai ni la même profondeur : normaliser la numération n’équivaut pas à atteindre une réponse moléculaire majeure.</p>
<p>Après traitement d’une LAM, l’aplasie liée au médicament peut précéder la récupération des lignées. Une cytopénie persistante peut également refléter la maladie, une infection ou d’autres causes. La moelle, la chronologie et les traitements associés aident à distinguer ces mécanismes. C’est pourquoi la conduite sous vénétoclax diffère avant et après rémission documentée.</p>
<p>La physiologie rend enfin les objectifs cohérents : stabiliser une fonction vitale aujourd’hui, contrôler le clone, puis réduire le risque de rechute. Ces objectifs se complètent mais ne se confondent pas. Une transfusion peut améliorer le transport d’oxygène sans traiter la leucémie ; une réponse moléculaire peut être profonde sans effacer toutes les toxicités ou les besoins de support.</p>
'''+refs('NORMAL','NORMAL-WBC','NORMAL-HEMO','ELN-AML','ONKO-APL','ELN-CML','VENCLYXTO')

BIO='''<h3>Signaux, mort cellulaire et métabolisme : du mécanisme à la surveillance</h3>
<p>Une cellule hématopoïétique reçoit des signaux qui règlent croissance, différenciation et survie. Une anomalie de kinase peut maintenir un signal de prolifération ; une anomalie de régulation transcriptionnelle ou épigénétique peut perturber la maturation. Plusieurs mécanismes coopèrent souvent. Une mutation isolée n’explique donc pas à elle seule toute la trajectoire d’une LAM.</p>
<p>BCR::ABL1 est une kinase de fusion centrale dans la LMC. Les TKI dirigés vers le site ATP et l’asciminib dirigé vers la poche myristoylique n’occupent pas la même zone. Cette différence aide à comprendre des profils de résistance distincts. La démonstration d’une mutation résistante appelle une interprétation liée au produit, à sa dose autorisée et au contexte ; elle ne justifie pas de choisir arbitrairement un autre inhibiteur portant la même étiquette de classe.</p>
<p>FLT3 transmet des signaux de croissance et de survie. Les altérations ITD et du domaine tyrosine kinase n’ont pas exactement les mêmes implications pour chaque traitement. La présence d’une cible n’efface pas les autres mutations, le risque de rechute ni les contraintes de tolérance. Les essais et les FI définissent les populations dans lesquelles la cible devient une indication.</p>
'''+causal('c92-causal-cible','Une cible moléculaire ne suffit pas à prescrire',[
'Anomalie démontrée par une méthode adaptée',
'Mécanisme et sensibilité au médicament',
'Population et phase de maladie étudiées',
'Indication suisse, interactions et organes',
'Prescription spécialisée et suivi de réponse'],
'La plausibilité biologique est une étape ; preuve clinique et conditions d’utilisation restent nécessaires.')+'''
<p>Dans la LPA, PML::RARA perturbe la différenciation. ATRA et ATO agissent sur cette biologie ; la différenciation peut s’accompagner d’une réaction inflammatoire systémique. Fièvre, dyspnée, prise de poids ou atteinte rénale doivent donc être interprétées dans la chronologie du traitement. Une complication peut survenir pendant un effet antileucémique attendu, et une infection concomitante reste possible.</p>
<p>BCL-2 protège certaines cellules de l’apoptose. Le vénétoclax abaisse ce seuil de survie, ce qui peut contribuer à une destruction tumorale rapide. La lyse libère potassium, phosphate et précurseurs de l’urate ; les troubles électrolytiques et l’atteinte rénale peuvent s’amplifier mutuellement. La prévention et les prises de sang après les paliers de dose découlent de cette cinétique, pas seulement d’une anomalie déjà présente avant traitement.</p>
<p>La rasburicase dégrade l’urate. Son activité peut se poursuivre dans le tube après prélèvement : le dosage risque alors de sous-estimer la concentration réelle si les conditions préanalytiques ne sont pas respectées. Ce mécanisme explique une consigne de laboratoire qui pourrait sembler administrative. Son risque d’hémolyse/méthémoglobinémie en déficit de G6PD explique aussi une contre-indication indépendante du niveau d’urate.</p>
<p>Les voies du métabolisme médicamenteux relient la biochimie à la sécurité. CYP3A, transporteurs et élimination ne contribuent pas de façon identique à chaque produit. Ajouter un inhibiteur enzymatique peut augmenter l’exposition ; cela peut imposer une réduction pour vénétoclax ou ivosidenib, mais ne permet pas de copier cette règle à l’asciminib. Le tableau d’interactions doit porter le nom du produit, le contexte et la date de la FI.</p>
<p>Le QT dépend enfin de l’électrophysiologie et de facteurs modifiables : médicaments associés, potassium, magnésium, bradycardie et maladies cardiaques. Les seuils de suspension et de reprise sont propres aux protocoles et aux FI. Un ECG « presque normal » ne neutralise pas une association à risque, et une correction électrolytique ne remplace pas toute la surveillance requise.</p>
'''+refs('WHO','ELN-AML','ELN-CML','SCEMBLIX','VENCLYXTO','TRISENOX','TIBSOVO','VANFLYTA','FASTURTEC')

GEN='''<h3>Classification, pronostic et suivi : trois usages de la génétique</h3>
<p>Une analyse génétique peut nommer la maladie, estimer un risque ou mesurer une réponse. Ces objectifs utilisent parfois la même anomalie, mais pas nécessairement la même méthode ni le même seuil. Le compte rendu doit préciser matériel, technique, cible, sensibilité et contexte. Un résultat « positif » sans ces éléments ne suffit pas à décider.</p>
<p>Dans la LMC, la démonstration de BCR::ABL1 est centrale. Le caryotype peut montrer le chromosome Philadelphie et des anomalies additionnelles ; la FISH cible le remaniement ; la RT-PCR identifie un transcrit et prépare le suivi. Une PCR courante peut manquer un transcrit atypique : la discordance avec les autres méthodes exige une discussion avec le laboratoire. Le suivi de ces formes atypiques peut nécessiter une méthode personnalisée plutôt qu’un chiffre standard mal appliqué.</p>
<p>Dans la LAM, certaines anomalies génétiques définissent une entité à des niveaux de blastes inférieurs à 20 %, mais les classifications diffèrent. L’OMS 2022 conserve notamment des exceptions exigeant 20 % pour BCR::ABL1 et CEBPA ; l’ICC exposée par l’ELN emploie souvent un seuil de 10 % pour ses entités génétiques, avec exceptions. Il faut donc écrire la classification utilisée et conserver la corrélation morphologique, au lieu de mémoriser un seuil unique pour tout.</p>
<p>La catégorie LAM liée à la myélodysplasie ne repose plus sur la seule dysplasie morphologique. L’histoire clinique, des anomalies cytogénétiques et des mutations définies participent à sa classification. Les listes ne sont pas identiques entre OMS et ICC ; RUNX1 illustre une différence. Une ancienne catégorie de codage ou un libellé historique de FI, tel AML-MRC, ne peut être remplacé automatiquement par la nouvelle catégorie sans examiner les critères.</p>
'''+causal('c92-causal-genetique','Donner un sens à un résultat génétique',[
'Méthode et matériel documentés',
'Anomalie interprétée dans une classification datée',
'Risque adapté au traitement envisagé',
'Cible éventuelle et indication vérifiées',
'Marqueur de suivi choisi avec ses limites'],
'Diagnostic, pronostic, choix thérapeutique et suivi sont des fonctions distinctes du résultat.')+'''
<p>Le pronostic dépend du traitement. L’ELN 2022 pour traitements intensifs ne conserve plus le ratio allélique FLT3-ITD comme dans l’ancienne version ; une mutation NPM1 ne doit pas faire ignorer une cytogénétique défavorable. L’ELN 2024 pour certains traitements moins intensifs utilise d’autres associations, avec un rôle majeur de TP53 et des conditions autour de NPM1, IDH1/2 et des voies de signalisation. Ce tableau ne s’étend pas automatiquement à tous les traitements, aux rechutes ni aux patients déjà exposés à un hypométhylant.</p>
<p>La maladie résiduelle mesurable utilise un marqueur suivi dans le temps avec une sensibilité connue. Certaines mutations de l’hématopoïèse clonale, notamment DNMT3A, TET2 et ASXL1, peuvent persister sans signifier à elles seules le même risque qu’un marqueur leucémique spécifique. Une négativité dépend de la qualité du prélèvement et des contrôles analytiques ; une variation doit être replacée dans une cinétique.</p>
<p>En LMC, l’échelle internationale permet de suivre BCR::ABL1 pour les transcrits usuels. Une réponse moléculaire majeure correspond à ≤ 0,1 %, MR4 à ≤ 0,01 % et MR4,5 à ≤ 0,0032 %, sous réserve de contrôles adéquats. Un résultat indétectable avec trop peu de transcrits de contrôle ne démontre pas nécessairement une réponse profonde. La profondeur et sa durée contribuent aux critères d’un éventuel arrêt surveillé du TKI.</p>
<p>Enfin, une prédisposition germinale peut modifier le conseil familial et le choix d’un donneur apparenté. Une variante mesurée dans le sang tumoral n’est pas automatiquement germinale ; un prélèvement non hématopoïétique approprié et un conseil spécialisé peuvent être nécessaires. Éviter un donneur porteur d’une prédisposition pertinente demande une démarche dédiée, pas une conclusion tirée d’un seul panel tumoral.</p>
'''+refs('WHO','ELN-AML','ELN-LOW','ELN-CML','OFS','VYXEOS')

TABS=[('semio','Sémiologie fondamentale et analytique',SEMIO),('anat','Anatomie',ANAT),('histo','Histologie',HISTO),('physio','Physiologie',PHYSIO),('bio','Biochimie et pharmacologie moléculaire',BIO),('gen','Génétique',GEN)]
LINKS={
'semio':('Chronologie et gravité orientent les mécanismes possibles.','Hémogramme, frottis, coagulation et génétique répondent à des questions différentes.','Stabiliser les urgences en parallèle du diagnostic précis.'),
'anat':('Un clone médullaire peut avoir un retentissement sanguin et extramédullaire.','Aspiration, biopsie et imagerie renseignent des compartiments différents.','Le contrôle local d’une masse ne remplace pas le traitement systémique indiqué.'),
'histo':('La maturation cellulaire et ses anomalies expliquent les aspects du frottis.','Un champ choisi ne vaut ni décompte représentatif ni génotype.','Une suspicion morphologique de LPA impose un circuit urgent.'),
'physio':('Une leucocytose peut coexister avec une défense inefficace.','Numération, fonction et réponse moléculaire ne sont pas synonymes.','Support immédiat, contrôle du clone et prévention de rechute se complètent.'),
'bio':('Signal prolifératif, différenciation et apoptose produisent des manifestations distinctes.','Électrolytes, fonction rénale et ECG accompagnent les traitements ciblés.','Interactions et adaptations sont propres au produit exact.'),
'gen':('Une même étiquette C92 recouvre plusieurs biologies.','Classification, risque et MRD exigent méthodes et versions précisées.','Une cible moléculaire ne remplace ni l’indication ni la discussion clinique.')}
def sciences():
 bar='<div class="panel" id="pS" hidden><div class="sci-bar ui" role="tablist">'
 for k,title,_ in TABS:bar+=f'<button id="c92-tab-{k}" role="tab" aria-selected="{str(k=="semio").lower()}" aria-controls="c92-s-{k}" data-s="c92-s-{k}">{title}</button>'
 bar+='</div><div class="chap-body sci-body">'
 for k,title,body in TABS:
  bridge='<div class="key">'+''.join(f'<p><b>{label}</b> {text}</p>' for label,text in zip(['Science → clinique.','Science → examen.','Science → traitement.'],LINKS[k]))+'<p><b>À retenir.</b> Relier fonction normale, mécanisme, mesure et décision sans effacer les limites.</p></div>'
  content=body if k=='semio' else f'<section class="ilot" id="c92-s-{k}-cours">{body}</section>'
  hide='' if k=='semio' else ' hidden'
  bar+=f'<div class="sci" id="c92-s-{k}" role="tabpanel" aria-labelledby="c92-tab-{k}"{hide}>{content}{bridge}<button class="pareto-btn ui" data-k="pareto-c92-{k}">▲ Loi de Pareto — {title}</button></div>'
 return bar+'</div><div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div></div>'
