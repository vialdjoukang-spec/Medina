from common import *

pop('classification','C92, OMS et ICC : trois plans à ne pas confondre','''
<p>C92 est une famille de codage CIM-10-GM, comprenant plusieurs maladies myéloïdes. L’OMS et l’ICC sont des classifications biologiques utilisant morphologie, clinique et génétique. Un même intitulé historique de code peut donc recouvrir une entité dont le nom moderne a changé.</p>
<p>Dans la LAM, le seuil de blastes dépend de l’entité et de la classification. Ne pas transformer « 20 % » en règle sans exception, ni conclure que toute mutation suffit à abaisser ce seuil. Documenter classification, matériel et anomalie. C92.5 désigne une leucémie aiguë myélomonocytaire ; la leucémie myélomonocytaire chronique relève de C93.1.</p>
''','OFS','WHO','ELN-AML')
pop('clonalite','Clonalité : une origine commune ne donne pas toute la réponse','''
<p>Un clone regroupe des cellules issues d’une cellule ancestrale portant des caractéristiques communes. Une anomalie clonale peut aider à reconnaître une néoplasie, mais toute hématopoïèse clonale n’est pas une leucémie aiguë. Les mutations doivent être interprétées avec cytopénies, morphologie, proportion de blastes et critères de l’entité.</p>
<p>Après traitement, certaines mutations associées à l’hématopoïèse clonale peuvent persister sans avoir le même sens qu’un marqueur leucémique spécifique. La question « existe-t-il un clone ? » diffère de « quelle maladie ? » et de « quelle maladie résiduelle ? ».</p>
''','WHO','ELN-AML')
pop('differenciation','Différenciation : une maturation utile peut s’accompagner d’une urgence','''
<p>La différenciation transforme un précurseur en cellule plus mature. Dans la LPA, PML::RARA perturbe ce processus ; ATRA et ATO agissent sur cette biologie. Une réponse par différenciation n’est pas synonyme d’absence de risque immédiat.</p>
<p>Fièvre, dyspnée, prise de poids, œdèmes, hypotension ou atteinte rénale peuvent évoquer un syndrome de différenciation. Le traitement urgent et la gestion des médicaments suivent le produit/protocole ; infection et surcharge restent des diagnostics possibles ou associés. Les critères de suspension ne sont pas identiques pour ATO, ivosidenib et giltéritinib.</p>
''','ONKO-APL','TRISENOX','TIBSOVO','XOSPATA')
pop('epidemiologie','Épidémiologie : conserver la population du chiffre','''
<p>Une incidence de LAM dans une population européenne ne devient pas une incidence suisse de toutes les maladies C92. Les statistiques suisses regroupant les leucémies C91–C95 ne fournissent pas directement la fréquence de chaque sous-type de C92.</p>
<p>De même, un âge médian observé dans un registre ne fixe ni l’âge du diagnostic individuel ni l’éligibilité à un traitement. Pour les entités rares, les séries sélectionnées et les changements de classification limitent les comparaisons. Cette leçon indique les données disponibles et leur périmètre plutôt que fabriquer un taux national spécifique.</p>
''','ONKO-AML','OFS-CANCER','MLL')
pop('germinal','Prédisposition germinale et choix du donneur','''
<p>Une variante germinale est présente au-delà du clone tumoral. Une analyse du sang atteint ne permet pas toujours de distinguer prédisposition constitutionnelle et mutation acquise. L’histoire familiale, les caractéristiques cliniques et un test dans un tissu approprié peuvent orienter une évaluation spécialisée.</p>
<p>L’enjeu dépasse le diagnostic : conseil familial, suivi et choix d’un donneur apparenté peuvent changer. Un donneur portant une prédisposition pertinente doit être identifié par la démarche adaptée ; un panel tumoral isolé ne remplace pas cette évaluation.</p>
''','ELN-AML','WHO')
pop('grossesse','Grossesse, fertilité et projet parental','''
<p>Le projet parental doit être discuté tôt avec hématologie et équipes concernées. Urgence de la maladie, terme, traitement, profondeur de réponse et parent exposé modifient la décision. Les recommandations européennes et les FI suisses doivent être confrontées au cas concret.</p>
<p>Un arrêt spontané du TKI n’est pas une stratégie sûre. Les délais de contraception diffèrent selon produit et sexe ; ils ne se déduisent pas d’une durée unique pour toute la classe. La fertilité, les possibilités de préservation et l’allaitement nécessitent une discussion séparée, sans retarder indûment une urgence vitale.</p>
''','ELN-CML','ELN-AML','VESANOID','SCEMBLIX','RYDAPT','XOSPATA')
pop('interactions','Interactions : vérifier le produit, la phase et la dose','''
<p>Les inhibiteurs du CYP3A peuvent augmenter l’exposition de certains traitements. La réponse réglementaire varie : réduction de dose pour vénétoclax ou ivosidenib dans les situations décrites, adaptations spécifiques pour quizartinib, prudence sans réduction initiale automatique pour tous les cas d’asciminib.</p>
<p>Vérifier aussi les substrats concernés, les médicaments allongeant le QT, les électrolytes, les compléments et le millepertuis. Un tableau de réduction pour toxicité ne se substitue pas au tableau d’interaction. Refaire cette vérification à chaque changement de prescription.</p>
''','VENCLYXTO','TIBSOVO','VANFLYTA','SCEMBLIX')
pop('lyse','Lyse tumorale : la cinétique explique la surveillance','''
<p>La destruction de nombreuses cellules libère potassium, phosphate et précurseurs de l’urate. L’atteinte rénale peut aggraver les désordres ; des complications cardiaques ou neurologiques peuvent apparaître. Le risque dépend du clone, de la charge tumorale, du rein et du traitement.</p>
<p>Prévention de l’hyperuricémie, hydratation adaptée et contrôles biologiques après les doses sont organisés avant exposition. Sous vénétoclax, la FI prévoit des prélèvements rapprochés lors de l’escalade. Sous rasburicase, la préanalyse de l’urate est essentielle car l’enzyme peut continuer à agir dans le tube.</p>
''','ELN-AML','VENCLYXTO','FASTURTEC')
pop('myelopoiese','Myélopoïèse : production et fonction sont distinctes','''
<p>La moelle organise production et maturation des lignées myéloïdes. Une prolifération clonale peut augmenter le nombre de certaines cellules tout en réduisant la production normale. Une leucocytose peut donc coexister avec anémie, thrombopénie et défense inefficace.</p>
<p>La formule sanguine, la morphologie et la moelle renseignent des dimensions différentes. Dans la LMC, la maturation est relativement conservée ; dans de nombreuses LAM, le défaut de différenciation est plus marqué. Ces repères expliquent des tableaux, sans remplacer les critères biologiques de classification.</p>
''','NORMAL','NORMAL-WBC','WHO','ELN-AML','ELN-CML')
pop('neutropenie','Neutropénie fébrile : reconnaître l’urgence','''
<p>Une fièvre chez une personne neutropénique exige une évaluation urgente. L’immunodépression peut atténuer certains signes locaux ; l’absence de pus ou de réaction inflammatoire spectaculaire ne rassure pas à elle seule.</p>
<p>Stabilité, foyer, prélèvements, antibiotiques antérieurs, colonisations, allergies et fonction rénale guident le protocole empirique local. Ne pas retarder l’antibiothérapie nécessaire pour attendre toute l’identification microbiologique. La stratégie infectieuse doit aussi être conciliée avec les interactions des traitements antileucémiques.</p>
''','RMS-NF','ELN-AML','VENCLYXTO')
pop('observance','Observance : une variable clinique à explorer sans jugement','''
<p>Une hausse de BCR::ABL1 peut refléter une résistance, mais aussi des prises manquées, un effet indésirable, une interaction ou une difficulté d’accès au traitement. Interroger les horaires, repas, effets ressentis et contraintes quotidiennes aide à comprendre le résultat.</p>
<p>Une valeur isolée ne suffit pas toujours à changer de TKI. Confirmer la cinétique et la qualité de l’analyse, puis discuter mutation de résistance et adaptation selon le contexte. L’objectif est une prise réellement possible et efficace, pas seulement une ordonnance théoriquement correcte.</p>
''','ELN-CML','GLIVEC','SCEMBLIX')
pop('profiles','PROFILES et examen fédéral : raisonner à partir des situations','''
<p>PROFILES organise des compétences et situations de départ, pas une promesse de question d’examen sur chaque code CIM. Fatigue, fièvre, saignement, anomalies sanguines ou masse conduisent à un raisonnement clinique : gravité, hypothèses, examens pertinents et communication.</p>
<p>La documentation MEBEKO consultée pour 2026 renvoie au référentiel officiel. Les correspondances pédagogiques de cette leçon ne sont pas présentées comme une validation officielle de chaque numéro ou comme un programme exhaustif de l’examen. Le lien utile est la capacité à expliquer une décision, ses risques et ses limites.</p>
''','PROFILES','MEBEKO','PROFILES-TRANS')
pop('sarcome','Sarcome myéloïde : masse locale, bilan systémique','''
<p>Un sarcome myéloïde est une masse extramédullaire de cellules myéloïdes immatures. Il peut accompagner une leucémie ou sembler isolé. L’imagerie décrit extension et retentissement ; la biopsie avec immunohistochimie et génétique établit la nature de la lésion.</p>
<p>Un bilan médullaire recherche une atteinte concomitante. Les traitements systémiques proches de ceux de LAM sont discutés même dans certaines formes isolées ; chirurgie ou radiothérapie répondent à des indications locales sélectionnées. Les données sont surtout observationnelles, sans supériorité universelle d’un protocole spécifique démontrée ici.</p>
''','SARCOMA','CH-SARCOMA','WHO')
pop('semiologie','Sémiologie : cinq questions avant l’étiquette','''
<ol><li>Quelle fonction est perturbée : transport, défense, hémostase, infiltration ?</li><li>Depuis quand et à quelle vitesse ?</li><li>Existe-t-il une menace respiratoire, neurologique, infectieuse ou hémorragique ?</li><li>Quel examen départage les mécanismes possibles ?</li><li>Quelle décision doit précéder les résultats complets ?</li></ol>
<p>Les réponses organisent le bilan sans imposer prématurément un sous-type. Les neuf unités du sous-onglet de sémiologie détaillent normalité, signes, mécanismes, examen, interprétation, différentiels, urgence, limites et sources.</p>
''','ELN-AML','ELN-CML','ONKO-APL')
pop('urgences','Urgences : ne pas attendre la fin du classement','''
<p>LPA suspectée avec coagulopathie, leucostase symptomatique, lyse tumorale, infection grave, hémorragie ou compression neurologique imposent un circuit urgent. Stabilisation, appel spécialisé et prélèvements utiles avancent en parallèle.</p>
<p>La numération seule ne décide pas de la leucostase, et une LPA ne se traite pas comme toute autre hyperleucocytose. Après exposition, syndrome de différenciation et toxicité rythmique ajoutent des urgences propres aux médicaments. Un diagnostic plausible n’exclut pas une seconde complication.</p>
''','ELN-AML','ONKO-APL','TRISENOX','VANFLYTA')

pop('bcr-abl','BCR::ABL1 : définir la LMC et préparer son suivi','''
<p>La fusion BCR::ABL1 code une tyrosine kinase dérégulée. Caryotype, FISH et RT-PCR apportent des informations complémentaires : chromosome et anomalies additionnelles, remaniement ciblé, identité du transcrit.</p>
<p>Les transcrits atypiques peuvent échapper à une PCR courante. Une discordance mérite vérification avec le laboratoire ; une PCR négative ne doit pas faire ignorer les autres preuves. Identifier le transcrit au diagnostic permet de choisir un suivi fiable. Le terme « Philadelphie positif » ne remplace pas toute la caractérisation.</p>
''','ELN-CML','WHO')
pop('differentiels','Différentiels : tester une hypothèse concurrente','''
<p>Le diagnostic différentiel dépend du point de départ : leucocytose réactionnelle, autres néoplasies myéloprolifératives, MDS/MPN, leucémie lymphoblastique ou autre cause de cytopénie. Dans une masse, lymphome et autres tumeurs nécessitent un panel adapté.</p>
<p>La persistance, les lignées associées, le frottis, la moelle et la génétique modifient les probabilités. Une dysplasie ou un marqueur isolé ne suffit pas toujours. Une fois la leucémie connue, une infection ou une toxicité peut encore expliquer de nouveaux symptômes ; le diagnostic initial ne ferme pas le raisonnement.</p>
''','WHO','ELN-AML','MLL','SARCOMA')
pop('fi','Information professionnelle suisse : ce qu’elle établit','''
<p>La FI décrit notamment indication, dose, contre-indications, adaptations, interactions et surveillance du produit exact. Elle doit être datée. Une recommandation européenne peut discuter un usage plus large que son libellé suisse ; cet écart doit être signalé.</p>
<p>La FI ne prouve pas à elle seule le remboursement de chaque situation, ni la supériorité de son produit dans toute comparaison. Les schémas adultes ne se transposent pas automatiquement à l’enfant, à la grossesse ou à une formulation différente. Le cours conserve les limites des passages réellement lus.</p>
''','OFSP','OAMAL','TRISENOX','VANFLYTA','SCEMBLIX')
pop('genetique','Génétique : préciser l’usage du résultat','''
<p>Une anomalie peut définir une entité, contribuer au pronostic, ouvrir une option ciblée ou servir au suivi. Ces usages ont des exigences distinctes. La classification OMS ne se substitue pas au tableau pronostique ELN, et l’un ou l’autre ne remplace pas une indication Swissmedic.</p>
<p>Noter méthode, matériel, sensibilité et version de classification. Un test tumoral ne prouve pas une prédisposition germinale. Une mutation persistante d’hématopoïèse clonale n’a pas automatiquement le même sens qu’un marqueur de maladie résiduelle spécifique.</p>
''','WHO','ELN-AML','ELN-LOW','ELN-CML')
pop('greffe','Allogreffe : bénéfice antileucémique et risque propre','''
<p>L’allogreffe associe traitement préparatoire et effet immunologique contre le clone. Le bénéfice attendu dépend du risque de rechute, de la réponse/MRD, de la maladie, de l’état fonctionnel, du donneur et des risques de toxicité, infection et réaction du greffon contre l’hôte.</p>
<p>Une greffe n’est ni systématique pour toute LAM ni décidée par l’âge seul. Dans le MDS/MPN avec neutrophilie, elle constitue la stratégie à potentiel curatif établi chez des patients sélectionnés, avec données limitées sur le meilleur traitement préalable. Une prédisposition germinale peut modifier le choix du donneur.</p>
''','ELN-AML','EBMT','ELN-CML')
pop('hemogramme','Hémogramme : lire les nombres et leurs limites','''
<p>L’hémogramme donne des concentrations et des indices ; le frottis apporte la morphologie. Le nombre total de leucocytes ne dit pas combien sont des neutrophiles fonctionnels ou des blastes. Comparer aux résultats antérieurs et regarder toutes les lignées.</p>
<p>Une leucémie aiguë peut avoir une numération leucocytaire élevée, normale ou basse. Les normes d’hémoglobine et d’autres paramètres dépendent du laboratoire et de la population. Une alerte automate ou une discordance clinique demande une vérification adaptée, sans diagnostic génétique déduit d’un chiffre.</p>
''','ELN-AML','ONKO-AML','ELN-CML')
pop('immunophenotype','Immunophénotype : un panel plutôt qu’un marqueur magique','''
<p>La cytométrie décrit l’expression de marqueurs sur les populations cellulaires. Elle contribue à l’attribution de lignée et à la caractérisation du clone. Des expressions aberrantes ou des marqueurs absents peuvent compliquer une interprétation isolée.</p>
<p>Le panel doit être confronté à morphologie et génétique. Dans un tissu, l’immunohistochimie du sarcome myéloïde utilise plusieurs marqueurs, dont l’expression peut varier. Un profil diagnostic peut aussi contribuer au suivi, avec des exigences analytiques spécifiques ; il n’est pas automatiquement un test MRD validé.</p>
''','ELN-AML','SARCOMA')
pop('moelle','Aspiration et biopsie : des informations complémentaires','''
<p>L’aspiration fournit des cellules pour cytologie, cytométrie et analyses génétiques. La biopsie conserve l’architecture et aide notamment quand l’aspiration est pauvre ou impossible. Une ponction blanche ne signifie pas une moelle indemne.</p>
<p>Prévenir le laboratoire, répartir le matériel et évaluer l’hémodilution améliorent l’interprétation. Pour MRD, la qualité du prélèvement influence la sensibilité réelle. Un résultat négatif dans un échantillon inadéquat ne porte pas la même conclusion qu’un prélèvement de qualité documentée.</p>
''','ELN-AML','ELN-CML','SARCOMA')
pop('mrd','MRD : mesurable ne signifie pas omniscient','''
<p>La maladie résiduelle mesurable recherche un signal sous le seuil de la morphologie habituelle. Méthode, marqueur, matériel, sensibilité et date de traitement conditionnent sa signification. Une négativité ne prouve pas l’éradication de toute cellule leucémique.</p>
<p>Les mutations DNMT3A, TET2 et ASXL1 peuvent refléter une hématopoïèse clonale persistante ; elles ne doivent pas être assimilées sans nuance à tous les marqueurs leucémiques. La cinétique d’un marqueur approprié peut guider consolidation ou surveillance, dans le cadre de la maladie et du traitement concernés.</p>
''','ELN-AML','ONKO-AML','ELN-CML')
pop('reponse','Réponse : trois dimensions à nommer','''
<p>Dans la LAM, la morphologie, la récupération hématologique et la MRD décrivent des dimensions distinctes. La CR associe notamment moins de 5 % de blastes médullaires, absence de maladie extramédullaire/blastes circulants, neutrophiles ≥ 1 G/L et plaquettes ≥ 100 G/L.</p>
<p>CRh décrit une récupération partielle définie ; CRi une récupération incomplète selon les critères ELN. La catégorie employée doit être explicite pour éviter de compter deux fois la même réponse. En LMC, réponse hématologique et réponse moléculaire ont également des profondeurs différentes.</p>
''','ELN-AML','ELN-CML')
pop('sources','Sources : dates, lecture et désaccords conservés','''
<p>La priorité documentaire est suisse lorsque la question concerne codage, produit ou cadre national, complétée par les recommandations européennes et les sources biologiques pertinentes. Chaque référence conserve son niveau de lecture : section ciblée, résumé ou réutilisation attribuée d’une lecture antérieure.</p>
<p>Les changements de classification, les divergences FI/recommandations et les unités douteuses ne sont pas effacés. La FI française de Vyxeos présente par exemple une unité de bilirubine incohérente dans l’extraction consultée : aucun seuil numérique n’est repris de mémoire. Une entrée bibliographique n’est pas une preuve de lecture intégrale.</p>
''','OFS','WHO','ELN-AML','ELN-LOW','ELN-CML','VYXEOS')
pop('strategie','Stratégie : maladie, personne et objectif','''
<p>La décision combine entité, risque, mutations, état fonctionnel, organes, souhaits et possibilités de suivi. Une induction intensive, une association moins intensive, un TKI ou une stratégie de support répondent à des situations différentes.</p>
<p>Préciser l’objectif : urgence vitale, rémission, prévention de rechute, contrôle durable ou confort. Une cible moléculaire ouvre une discussion mais ne suffit pas à choisir la dose ou l’association. Les classifications de risque doivent correspondre au traitement envisagé.</p>
''','ELN-AML','ELN-LOW','ELN-CML','ONKO-APL')
pop('suivi','Suivi : quoi mesurer, quand et pour agir comment','''
<p>La surveillance dépend de l’entité, du traitement, de la profondeur de réponse et du marqueur disponible. Numération, toxicités, qualité de vie et mesure moléculaire ne sont pas interchangeables. Le calendrier doit annoncer quelle anomalie déclenchera une nouvelle évaluation.</p>
<p>Une PCR PML::RARA après consolidation ne signifie pas qu’un suivi moléculaire identique est nécessaire indéfiniment pour tous les schémas de LPA. En LMC, même après arrêt surveillé du TKI, le suivi moléculaire reste durable. Les recommandations et populations exactes accompagnent chaque rythme.</p>
''','ONKO-AML','ONKO-APL','ELN-CML')
pop('tfr','Arrêt surveillé du TKI : une décision sélectionnée','''
<p>Selon l’ELN 2025, l’arrêt se discute notamment en première phase chronique, avec patient motivé, accès rapide à une PCR de qualité, traitement suffisamment long et réponse moléculaire profonde durable. Les critères minimaux incluent généralement plus de cinq ans de TKI, ou plus de quatre ans avec certains TKI de deuxième génération, et MR4 depuis plus de deux ans ; d’autres conditions restent nécessaires.</p>
<p>Après arrêt : PCR toutes les 6–8 semaines les six premiers mois, tous les deux mois jusqu’à un an, puis tous les 3–6 mois. La perte de MMR conduit à reprendre le traitement, sans attendre une seconde confirmation qui retarderait la reprise. L’arrêt n’est ni une guérison prouvée ni une option autonome.</p>
''','ELN-CML')
pop('jalons','Jalons LMC : un seuil se lit dans une trajectoire','''
<p>L’ELN 2025 utilise notamment BCR::ABL1 IS ≤ 10 % à trois mois, ≤ 1 % à six mois et ≤ 0,1 % à douze mois comme jalons favorables. Une valeur au-dessus d’un seuil exige contexte, confirmation et analyse de la cinétique selon le moment.</p>
<p>À trois mois, un résultat > 10 % doit être confirmé dans les 1–3 mois avant certaines conclusions. Observance, interactions, tolérance, contrôles analytiques et mutations éventuelles participent à la décision. Changer de TKI sur un chiffre isolé sans cette analyse peut être inapproprié.</p>
''','ELN-CML')
pop('cml-is','Échelle internationale : lire la profondeur de réponse','''
<p>BCR::ABL1 IS exprime le résultat sur une échelle internationale pour les transcrits usuels. MMR correspond à ≤ 0,1 %, MR4 à ≤ 0,01 % et MR4,5 à ≤ 0,0032 %. Ces seuils exigent une qualité et une quantité suffisantes de transcrits de contrôle.</p>
<p>« Indétectable » avec un contrôle insuffisant ne prouve pas une réponse très profonde. Certains transcrits atypiques nécessitent une stratégie personnalisée. La durée d’une réponse compte aussi : une mesure profonde unique ne suffit pas à autoriser un arrêt surveillé du traitement.</p>
''','ELN-CML')
pop('flt3','FLT3 : mutation et indication sont liées au contexte','''
<p>ITD et mutations du domaine tyrosine kinase sont des catégories d’altérations FLT3. Midostaurine, quizartinib et giltéritinib ont des indications et schémas différents : première ligne FLT3 mutée, première ligne FLT3-ITD ou rechute/réfractaire selon le produit.</p>
<p>Le statut à la rechute peut devoir être réévalué. Le QT, les interactions et les phases d’induction, consolidation ou entretien modifient la prescription. La FI suisse de quizartinib ne l’indique pas en entretien après allogreffe ; une recommandation européenne plus large doit être signalée comme telle.</p>
''','RYDAPT','VANFLYTA','XOSPATA','ELN-AML')
pop('formulation','Formulation : une partie de l’identité du traitement','''
<p>Vyxeos combine daunorubicine et cytarabine dans une formulation liposomale à rapport fixe. Ses doses et jours d’administration ne sont pas interchangeables avec les deux molécules libres. Les deux quantités doivent être explicites pour éviter une erreur de préparation.</p>
<p>De même, azacitidine injectable et orale ne sont pas des substitutions automatiques. Nom, formulation, voie, dose, unité et calendrier doivent être vérifiés ensemble. Une conversion arithmétique correcte peut rester pharmacologiquement incorrecte si la formulation change.</p>
''','VYXEOS','DAUNOBLASTIN','CYTOSAR','VIDAZA')

PARETO={
'cours':('C92 en cinq décisions',['Nommer l’entité moderne sans confondre code, OMS et ICC.','Reconnaître les urgences, notamment LPA et leucostase symptomatique.','Combiner morphologie, immunophénotype et génétique.','Adapter stratégie et risque à la personne et au traitement.','Suivre réponse, toxicités et qualité de vie avec des méthodes explicites.'],['OFS','WHO','ELN-AML','ELN-CML','ONKO-APL']),
'examens':('Examens qui changent la décision',['Numération et frottis décrivent quantité et morphologie.','Moelle et tissu répondent à des questions complémentaires.','Génétique : classification, cible et risque sont distincts.','Coagulation, rein et électrolytes identifient des urgences.','MRD et réponse exigent un prélèvement et une méthode de qualité.'],['ELN-AML','ELN-CML','SARCOMA']),
'pharma':('Prescrire dans le bon contexte',['Indication suisse datée et protocole spécialisé.','Formulation, dose, voie et jours vérifiés ensemble.','Interactions revues à chaque changement.','QT, lyse, aplasie et différenciation surveillés selon produit.','Autorisation et remboursement ne sont pas synonymes.'],['VENCLYXTO','TRISENOX','VANFLYTA','SCEMBLIX','OFSP','OAMAL']),
'semio':('Partir de la fonction et de la gravité',['Transport, défense et hémostase peuvent être déficients ensemble.','Chronologie et paramètres vitaux précèdent l’étiquette.','Une numération totale ne décrit pas la fonction.','Plusieurs mécanismes peuvent coexister.','Une urgence se traite en parallèle du bilan.'],['ELN-AML','ELN-CML','ONKO-APL']),
'anat':('Trois compartiments',['Moelle : production et architecture.','Sang : cellules circulantes et nombres absolus.','Tissu : infiltration ou masse extramédullaire.','Biopsie et aspiration ne sont pas redondantes.','Contrôle local et systémique se discutent séparément.'],['NORMAL','SARCOMA','ELN-AML']),
'histo':('Regarder sans inventer',['Décrire noyau, cytoplasme et maturation.','Auer oriente la lignée sans prouver PML::RARA.','Une LPA peut être hypogranulaire.','Un champ ne vaut pas un décompte représentatif.','Morphologie, immunophénotype et génétique se confrontent.'],['ELN-AML','ONKO-APL','ELN-CML']),
'physio':('Nombre et fonction',['Le clone peut augmenter une population et réduire les lignées normales.','Leucocytose ne signifie pas défense efficace.','LPA : coagulopathie au-delà de la thrombopénie.','Réponse hématologique et moléculaire ont des profondeurs différentes.','Support et traitement du clone ont des objectifs complémentaires.'],['NORMAL-WBC','ELN-AML','ONKO-APL','ELN-CML']),
'bio':('Mécanisme et sécurité',['Kinase, différenciation et apoptose sont des cibles distinctes.','Lyse rapide impose prévention et contrôles après dose.','Différenciation peut s’accompagner d’une urgence.','Interactions et seuils QT sont propres au produit.','Plausibilité biologique ne suffit pas à créer une indication.'],['VENCLYXTO','TRISENOX','VANFLYTA','SCEMBLIX']),
'gen':('Donner un sens au résultat',['Préciser méthode, matériel et sensibilité.','Nommer la classification et sa version.','Adapter le risque au traitement.','Distinguer clone tumoral, hématopoïèse clonale et germinal.','MRD négative ne prouve pas une éradication certaine.'],['WHO','ELN-AML','ELN-LOW','ELN-CML'])}
for k,(title,items,sources) in PARETO.items():
 pop('pareto-c92-'+k,title,'<ol>'+''.join('<li>'+x+'</li>' for x in items)+'</ol><p>Cette synthèse aide au rappel ; les conditions, exceptions et sources restent dans la leçon.</p>',*sources)
