# Audit linguistique G97 — Affections du système nerveux après des actes médicaux (S08)

Mission ALPHA1-CLAUDE-G97-LANG, tour 1, génération 1. Branche `claude/alpha1/g97-lang-g1`, base `103745ba` (HEAD du worktree ; le manifeste indique `523832d9`). Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est globalement soigné et sobre : aucune faute d’orthographe lexicale n’a été relevée à la lecture, et les contrôles mécaniques ne trouvent ni apostrophe droite ni mot doublé. Les défauts relevés tiennent surtout aux phrases nominales ou à l’infinitif injonctif dans les encadrés « À retenir » et les cartes, aux ellipses de verbe ou d’article, à des constructions de fourchettes (« à 24 à 48 heures »), à des parenthèses imbriquées dans les libellés de liens, à des mentions de fabrication du cours (« îlot », « dossier », « le cours ») et à quelques ambiguïtés de référence (« leur confirmation », « s’il est indispensable »).

- **105 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire, puis `build_medina.audit()` : aucune abréviation non couverte, balises et `data-evidence` inchangés.
- **27 renvois médicaux** : formulations dont la correction créerait ou retirerait une causalité, un chiffre, une portée ou un énoncé de classification. Ils ne sont pas corrigés ici.
- **Choix différés** : espaces insécables globales (aucune dans les sept fichiers), graphie du toponyme « Fribourg-en-Brisgau », harmonisation « 2 semaines » / « deux semaines ».
- **2 constats hors périmètre** transmis à l’audit MED : sous-onglet de sémiologie absent (H-01) et provenance des trois figures (H-02).

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 38 |
| registre | 16 |
| ambiguïté | 13 |
| ponctuation | 9 |
| lexique | 9 |
| grammaire | 8 |
| répétition | 5 |
| cohérence | 4 |
| lourdeur | 1 |
| terminologie | 1 |
| typographie | 1 |

## Propositions par fichier

| Fichier | Propositions | Renvois |
|---|---|---|
| chapters/G97/G97_a.html | 19 | 7 |
| chapters/G97/G97_b.html | 32 | 12 |
| chapters/G97/G97_c.html | 17 | 4 |
| chapters/G97/G97_d.html | 12 | 1 |
| chapters/G97/G97_pop1.html | 10 | 1 |
| chapters/G97/G97_pop2.html | 14 | 1 |
| glossary/g97.py | 1 | 1 |

## Propositions les plus utiles

- **P-49** (G97_b.html) : « et un second patch chez 19,8 % ; l’échec est associé à un antécédent de migraine » devient « et un second patch chez 19,8 %. Dans cette cohorte, l’échec est associé à un antécédent de migraine ». Phrase de 74 mots (consigne : une vingtaine de mots au plus, STYLE_REDACTION § 2) : coupure au point-virgule, sujet de la seconde partie précisé.
- **P-12** (G97_a.html) : « Une localisation vermienne (OR 0,34) ou hémisphérique (OR 0,23) est moins à risque que le quatrième ventricule. » devient « Une localisation vermienne (rapport de cotes, OR 0,34) ou hémisphérique (OR 0,23) expose à un risque moindre que le quatrième ventricule. ». Le sigle OR est employé avant d’être défini (la définition ne vient que quatre phrases plus loin) ; « est moins à risque » attribue le risque à la localisation (calque de l’anglais « less at risk »).
- **P-31** (G97_b.html) : « La troisième ventriculocisternostomie endoscopique secondaire lors d’un dysfonctionnement donne » devient « La ventriculocisternostomie endoscopique du troisième ventricule, pratiquée secondairement lors d’un dysfonctionnement, donne ». Terminologie : l’ordinal « troisième » se lit comme « la troisième intervention » ; il s’agit du troisième ventricule.
- **P-01** (G97_a.html) : « Pour apprendre sans se perdre, le cours organise cette hétérogénéité autour de quatre tableaux cliniques, détaillés dans le tableau ci-dessous. » devient « Pour apprendre sans se perdre, on organise cette hétérogénéité autour de quatre tableaux cliniques, résumés ci-dessous. ». Le sujet « le cours » décrit la fabrication du cours (STYLE_REDACTION § 3) ; « tableaux cliniques » et « le tableau ci-dessous » juxtaposent deux sens de « tableau » ; le tableau résume, il ne détaille pas.
- **P-27** (G97_b.html) : « Urgence neurochirurgicale : hématome rachidien compressif. Urgence d’imagerie : signe focal, trouble visuel, altération de la conscience, crise, aggravation malgré le … » devient « L’hématome rachidien compressif est une urgence neurochirurgicale. Un signe focal, un trouble visuel, une altération de la conscience, une crise ou une aggravation malgré le blood patch c… ». Phrases nominales dans l’encadré « À retenir » (STYLE_REDACTION § 2) ; mêmes éléments en phrases complètes.
- **P-26** (G97_b.html) : « sont à la fois des diagnostics qui imitent la céphalée post-ponction et ses complications. » devient « sont à la fois des diagnostics qui imitent la céphalée post-ponction et des complications de celle-ci. ». Ambiguïté : « imitent… et ses complications » peut se lire « imitent les complications » ; la coordination porte en réalité sur deux statuts.
- **P-30** (G97_b.html) : « comprennent des plaquettes d’au moins » devient « comprennent un taux de plaquettes d’au moins ». Les précautions ne « comprennent » pas des plaquettes : elles comprennent un seuil du taux de plaquettes.
- **P-85** (G97_pop1.html) : « Voir l’îlot sur la prise en charge pour les données » devient « Voir la partie sur la prise en charge pour les données ». « Îlot » désigne la fabrication du cours, non son contenu (STYLE_REDACTION § 3).
- **P-65** (G97_c.html) : « permet de les calculer sur des chiffres réels » devient « permet de les illustrer sur des chiffres réels ». Seuls la différence absolue et le nombre à traiter sont calculés dans le tableau ; l’intervalle de confiance et le rapport de cotes ne le sont pas. « Illustrer » est exact pour les quatre notions.
- **P-73** (G97_d.html) : « sans vérifier la fonction rénale, ou en cas d’alcoolisme, de dénutrition ou de traitement par la flucloxacilline. » devient « sans vérifier la fonction rénale, ou malgré un alcoolisme, une dénutrition ou un traitement par la flucloxacilline. ». Coordination bancale : « sans vérifier… ou en cas de… » ; l’erreur est d’appliquer le plafond malgré ces situations.
- **P-39** (G97_b.html) : « déconseille l’ibuprofène chez la femme qui allaite et recommande le sevrage s’il est indispensable. » devient « déconseille l’ibuprofène chez la femme qui allaite et recommande le sevrage si le traitement est indispensable. ». Le pronom « il » peut renvoyer au sevrage ou à l’ibuprofène ; le contexte (le sevrage est la conséquence d’un traitement indispensable) impose le traitement. Formulation conforme à la fenêtre g97-ibuprofene (« si… »).
- **P-67** (G97_c.html) : « tandis que l’hématome et les facteurs de pression artérielle reposent sur des preuves » devient « tandis que les données sur l’hématome et sur les facteurs de pression artérielle reposent sur des preuves ». Faute de sujet : ce ne sont pas l’hématome ni la pression qui « reposent sur des preuves » mais les données qui les concernent.
- **P-91** (G97_pop2.html) : « Dans le dossier, D accompagne » devient « Dans ce cours, D accompagne ». « Dossier » désigne la fabrication du cours, non son contenu.

La liste complète figure dans `propositions.json`.

## Renvois médicaux (hors correction linguistique)

Classés par nature du risque pour le fond. Chaque renvoi cite l’extrait exact de la leçon.

- **R-01** (cohérence interne, G97_a.html) : « la seule cohorte suisse chiffrée (Genève) ». L’encadré affirme que la seule cohorte suisse chiffrée est celle de Genève et qu’elle ne porte pas sur l’incidence. La partie 8.4 (G97_b) chiffre pourtant une cohorte de Fribourg-en-Brisgau et de Berne (séjour médian de 31 jours, arrêt de travail médian de 381 jours) et la partie 11.7 cite Genève, Berne et Lausanne. La reformulation (« la seule cohorte suisse d’efficacité » ou autre) relève de l’audit médical.
- **R-04** (cohérence interne, G97_a.html) : « Une composante posturale absente n’exclut pas le diagnostic, mais impose de chercher une autre cause ». La fenêtre g97-orthostatique (G97_pop1) dit « ne permet pas d’affirmer la céphalée post-ponction ; elle justifie d’envisager l’imagerie ». « N’exclut pas… mais impose de chercher une autre cause » et « ne permet pas d’affirmer… justifie d’envisager » ne portent pas le même niveau d’obligation. Harmoniser suppose de choisir un énoncé clinique.
- **R-12** (cohérence interne, G97_b.html) : « La rééducation cognitive et la physiothérapie sont les seules options établies. ». La phrase précédente dit « Aucun traitement efficace n’est défini » ; celle-ci parle d’« options établies ». Le lecteur ne sait pas si ces options sont efficaces. À trancher par l’audit médical (même formulation dans la fenêtre g97-mutisme-therapie : « seules options établies »).
- **R-13** (cohérence interne, G97_b.html) : « La céphalée post-ponction durale évolue favorablement ». L’énoncé s’oppose, quelques lignes plus bas, à « Le pronostic n’est pas toujours favorable » (suivi de 5 ans, forme chronique). Concilier les deux (évolution le plus souvent favorable, avec une minorité chronique) ajoute une nuance de fréquence non établie.
- **R-22** (cohérence interne, G97_c.html) : « Une céphalée qui persiste malgré le blood patch ou change de caractère sort du cadre. ». Les « drapeaux rouges » de la partie 8.2 sont « une aggravation malgré un blood patch » ; ici « persiste malgré le blood patch » suffit à sortir du cadre. Persistance et aggravation ne sont pas équivalentes (la leçon chiffre l’échec du blood patch à 25,9 % et à 28,3 %, ce qui rend la persistance fréquente).
- **R-27** (cohérence interne, G97_pop1.html) : « B. Basse pression du LCR (moins de 60 mm de LCR) et/ou fuite de LCR à l’imagerie. ». La fenêtre g97-ichd écrit « et/ou » pour le critère B de la rubrique 7.2, alors que la partie 1.1 écrit « ou » (« ou une fuite visible à l’imagerie »). Les deux énoncés ne sont pas équivalents (cumul possible ou non). Le texte d’ICHD-3 doit trancher.
- **R-02** (incohérence chiffrée, G97_a.html) : « l’incidence rapportée va de moins de 2 % à 40 % ». La borne basse est « moins de 2 % » dans la partie 2 et « 2 % » dans l’encadré qui suit (« l’étendue de 2 % à 40 % »). Un chiffre est à corriger ou à sourcer ; le rôle linguistique ne touche pas aux chiffres.
- **R-03** (statistique, G97_a.html) : « Le médulloblastome multiplie le risque par 2,85 ». Le texte écrit « multiplie le risque » pour un rapport de cotes, alors que l’encadré qui suit (« Une cote de 2,85… mesure une association… pas une probabilité absolue ») et la partie sur les preuves (« Il compare des cotes, non des risques ») disent le contraire. Remplacer « le risque » par « la cote » change l’énoncé statistique : à trancher par l’audit médical.
- **R-05** (anatomie, G97_a.html) : « circule dans l’espace entouré par la dure-mère ». Formulation imprécise (« l’espace entouré par la dure-mère » pour le compartiment du LCR) ; la partie c emploie « l’enveloppe qui contient le LCR ». Une formule anatomique plus précise (espace sous-arachnoïdien, sac dural) est une affirmation d’anatomie à valider par l’audit médical.
- **R-06** (antécédent / chiffre, G97_a.html) : « les tumeurs cérébrales sont les tumeurs solides les plus fréquentes de l’enfant, et la moitié siège dans la fosse postérieure ». Le sujet de « la moitié » est ambigu : la moitié des tumeurs cérébrales ou la moitié des tumeurs solides de l’enfant ? Le même énoncé figure en G97_c (« la moitié siège dans la fosse postérieure »). La précision modifie le chiffre rapporté.
- **R-07** (ambiguïté, G97_b.html) : « aide à retenir les deux durées ». Une seule durée (5 jours) est citée dans le paragraphe ; « les deux durées » (5 jours et 2 semaines) n’est expliqué que dans la fenêtre g97-mnemo. Expliciter les chiffres dans la phrase est un ajout d’information : à décider par l’auteur ou l’audit médical.
- **R-08** (ordre / promesse, G97_b.html) : « Diagnostic différentiel, de la menace vitale à l’explication bénigne ». L’intitulé annonce un classement de la menace vitale à l’explication bénigne ; la liste n’est pas ordonnée ainsi (hématome sous-dural et thrombose veineuse cérébrale, puis thrombose veineuse cérébrale et vasoconstriction, puis hématome épidural, hypotension spontanée, autres troubles de la parole). La thrombose veineuse cérébrale figure dans deux puces, et la cinquième puce (« pour le mutisme, la définition reste débattue ») n’énonce aucun diagnostic différentiel. Réordonner ou retirer la promesse est un choix de fond.
- **R-09** (connecteur causal, G97_b.html) : « est donc la mesure de sécurité principale ». « Donc » fait découler la surveillance de la phrase précédente (« Les sources lues ne chiffrent aucun délai »), ce qui n’est pas une conséquence logique ; le lien réel est « le pronostic dépend du délai ». Retirer ou remplacer le connecteur change le raisonnement.
- **R-10** (connecteur causal, G97_b.html) : « Les opioïdes sont donc un recours bref, pas une option de fond. ». « Donc » tire une conclusion sur les opioïdes d’une phrase qui énumère des traitements sans soutien (grade I) parmi lesquels les opioïdes ne figurent pas ; les opioïdes sont traités plus haut (courts : grade C ; long cours : grade D). La place de la phrase ou son connecteur est à revoir par l’audit médical.
- **R-11** (terminologie, G97_b.html) : « Les opioïdes courts sont réservés à l’échec (grade C) ». « Opioïdes courts » (ici et dans le tableau de G97_d, « Opioïdes courts ») peut désigner une durée de traitement ou une courte durée d’action. Le contexte (« au long cours », « recours bref », « pas d’usage prolongé ») oriente vers la durée, mais le choix « de courte durée » ou « à courte durée d’action » est un énoncé pharmacologique.
- **R-19** (terminologie, G97_a.html) : « L’influence de l’aiguille est la donnée la mieux établie. ». L’aiguille est dite « conventionnelle biseautée » dans la partie 2, « coupante » en 3.1, 4.2, 9.1 et dans l’encadré des paramètres de G97_b, « conventionnelle » dans G97_c et dans les fenêtres. Rien n’indique que ces termes recouvrent exactement la même catégorie d’aiguille. L’unification est un choix de terminologie médicale.
- **R-14** (exclusivité, G97_b.html) : « Le mutisme cérébelleux est la complication neurologique de l’enfant opéré ». « La » complication neurologique de l’enfant opéré suggère qu’il n’y en a qu’une ; la catégorie G97 en compte d’autres (surdrainage de dérivation, hématome). Remplacer par « une complication » ou « une complication typique » est un choix de portée clinique.
- **R-15** (exactitude de la citation, G97_b.html) : « A. Céphalée remplissant les critères de 7.2 et le critère C. ». Le critère A de 7.2.1 est reproduit comme « céphalée remplissant les critères de 7.2 et le critère C », alors que la fenêtre g97-ichd donne pour 7.2 « A. Toute céphalée remplissant le critère C ». Le rapport entre critères de 7.2 et de 7.2.1 est à vérifier dans le texte intégral d’ICHD-3 par l’audit médical ; le rôle linguistique ne corrige pas une citation de critères.
- **R-16** (lisibilité d’un chiffre, G97_b.html) : « Hématome épidural rachidien postopératoire : 0,52 % (0,10 à 0,69 %) ». La parenthèse (0,10 à 0,69 %) est placée après la moyenne comme un intervalle de confiance, alors qu’il s’agit de l’étendue des séries (partie 2). Le lecteur peut la prendre pour un intervalle de confiance. Préciser (« étendue des séries ») est un énoncé statistique.
- **R-17** (sources, G97_b.html) : « est cosigné par des sociétés européennes mais dirigé par des sociétés majoritairement américaines ». Le paragraphe affirme utiliser des recommandations « européennes ou internationales » alors que le consensus est dirigé par des sociétés majoritairement américaines et gradué selon l’échelle d’un organisme américain (G97_pop2). Règle de projet : jamais de recommandation américaine comme référence de conduite. L’arbitrage (maintenir, remplacer, ou ne présenter que comme éclairage) relève de l’audit médical.
- **R-18** (terminologie clinique, G97_b.html) : « un déficit focal, un trouble visuel ou une convulsion imposent une imagerie urgente ». « Convulsion » ici, « crise » partout ailleurs (parties 6, 7.2, 8.2, tableaux, quiz). Crise et convulsion ne sont pas strictement synonymes (une crise peut être non convulsive) ; unifier est un choix clinique.
- **R-20** (structure de tableau, G97_d.html) : « Intervalle de 6 heures ». Dans le tableau p-2, la colonne « Dose par prise » contient « Intervalle de 6 heures » et « Intervalle de 8 heures » pour les insuffisances rénales ; ce sont des intervalles entre prises, non des doses. Corriger l’intitulé de colonne ou déplacer ces valeurs change le sens du tableau.
- **R-21** (logique, G97_c.html) : « une pression d’ouverture supérieure à ce seuil n’est pas une valeur normale, simplement non pathologique selon ce critère ». Pour un critère de diagnostic, « non pathologique » et « normal » se confondent ; la phrase oppose deux notions sans définir la différence, et les sources lues ne donnent pas de valeur normale. Reformuler suppose une assertion clinique.
- **R-23** (portée de la preuve, G97_c.html) : « tandis que l’hématome et les facteurs de pression artérielle reposent sur des preuves de faible qualité ». La phrase range « l’hématome » tout entier dans les preuves de faible qualité, alors que la partie 4.3 ne qualifie ainsi que les facteurs tensionnels et que l’incidence provient d’une méta-analyse de 40 études. Le périmètre exact des « preuves de faible qualité » est à fixer par l’audit médical (la proposition de ce rôle ne corrige que la syntaxe).
- **R-24** (cohérence du cas, G97_c.html) : « C. Répéter un blood patch. ». Le cas 2 ne mentionne aucun blood patch préalable ; « répéter » suppose un patch déjà réalisé. Le distracteur est peut-être volontaire ; si non, le verbe est à changer (« Réaliser un blood patch »), ce qui modifie le leurre du quiz.
- **R-25** (ellipse, G97_pop2.html) : « Avec des plaquettes d’au moins 70 × 10⁹/L et une fonction normale ». « Une fonction normale » n’a pas de complément : fonction plaquettaire ? fonction de coagulation ? La source (consensus de 2023, texte non lu) doit trancher ; la précision change le sens.
- **R-26** (développement des sigles, g97.py) : « ('GRADE','nom d’un système de cotation de la certitude de la preuve') ». Le champ « lit » ne développe pas GRADE lettre à lettre (convention du glossaire : définition littérale lettre à lettre). Le développement (Grading of Recommendations Assessment, Development and Evaluation) n’a pas été vérifié dans une source lue ici ; de même pour AIPS (« développement lettre à lettre non établi »). À sourcer par l’audit médical ou l’intégrateur du glossaire.

## Choix différés

- Espaces insécables (avant ; : ! ? et » ; après « ; dans les nombres de plus de quatre chiffres ; entre un nombre et % ou une unité) : non appliquées, ni proposées. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F, et le moteur de rendu (build_medina.py) n’en insère aucun. Relevé pour l’intégrateur : 405 espaces ordinaires avant ; : ? ! , 21 guillemets « suivis d’une espace ordinaire, 109 occurrences de « nombre, espace ordinaire, % », 5 nombres de cinq chiffres ou plus (31 412, 47 920…). Une correction globale par script (et non par 500 propositions locales) est préférable.
- Toponyme « Fribourg en Brisgau » (G97_b 8.4 ; G97_pop2 g97-cppd-chronique) : la graphie correcte est « Fribourg-en-Brisgau ». Non proposé : build_medina.audit() signale le mot à trait d’union comme abréviation non couverte (deux majuscules) ; il faudrait d’abord une entrée de glossaire.
- Harmonisation « 2 semaines » / « deux semaines » (7 et 5 occurrences) et « convulsion » / « crise » : non appliquée (voir R-18 pour crise et convulsion).
- Phrases longues sans coupure sûre : G97-C0035 (53 mots), G97-C0039 (49), G97-C0062 (45), G97-C0473 (60), G97-C0475 (48), pop1 G97-C0326 (56) et G97-C0485 (67, liste de libellés CIM). Seule G97-C0474 (74 mots) a pu être coupée sans toucher au fond (P-49).

## Constats hors périmètre transmis à l’audit MED

- **H-01** (MAJEUR (à instruire par l’audit MED), chapters/G97/G97_c.html) : Le panneau « Sciences fondamentales spécialisées » compte trois sous-onglets (Anatomie, Physiologie, Preuves chiffrées : data-s = g97-s-anat, g97-s-physio, g97-s-preuves). Le sous-onglet « Sémiologie fondamentale et analytique » (6e sous-onglet exigé, AGENTS.md) est absent, de même que histologie, biochimie ou immunologie, et génétique ou microbiologie (STYLE_REDACTION § 6).
- **H-02** (réserve, chapters/G97/G97_c.html) : Trois figures SVG dessinées dans le dépôt : Figure 1 (orientation du biseau), Figure 2 (chaîne de la céphalée post-ponction), Figure 3 (barres d’incidences). Leur légende les dit schémas didactiques non calibrés ; aucune n’est une illustration anatomique réelle. Le contrôle a porté sur le texte des légendes, pas sur leur provenance ; la vérification est transmise à l’audit MED.
- **Figures** : Le contrôle a porté sur le texte des figures (légendes, étiquettes), pas sur leur provenance. La vérification de la provenance est transmise à l’audit MED.

## Observations

- Style nominal des fenêtres : la plupart des fenêtres (G97_pop1, G97_pop2) emploient, sous l’étiquette « Définition », « Fréquence », « Facteurs », des segments nominaux (« Âge avancé, coagulopathie… », « Aggravation rapide… »). STYLE_REDACTION § 2 les proscrit, mais la convention « lab + fragment » est systématique dans le moteur ; seules les phrases franchement incomplètes ont été reprises. Les puces Pareto (contraction voulue) n’ont pas été corrigées, sauf une (infinitif injonctif).
- Objectifs de la partie 0 (G97-C0016) : une suite d’infinitifs (« Reconnaître… ; savoir… ; maîtriser… ») ; STYLE_REDACTION § 2 interdit l’infinitif injonctif. Non corrigé : une reformulation (« Le lecteur sait… ») est proscrite par § 3 et le choix revient à l’auteur.
- Tableaux sans introduction : le tableau de prévention (9.1) et celui des diagnostics associés (e-3) suivent directement leur titre, sans phrase d’ouverture (STYLE_REDACTION § 4). Ils sont commentés après coup. Ajouter une phrase d’introduction est un ajout de contenu.
- Annonce de plan : « La suite détaille le raisonnement pour… » (G97-C0097) et « Le cours le signale chaque fois » (G97-C0066) décrivent la fabrication du cours (STYLE_REDACTION § 3). Non modifiés : la suppression retire une phrase entière.
- Répétition : la mention « 50 % vers le jour 16 » (amélioration du mutisme) figure six fois (G97_b ×3, G97_c ×1, G97_pop2 ×2) ; l’énoncé « les tumeurs cérébrales sont les tumeurs solides les plus fréquentes de l’enfant » figure deux fois (G97_a, G97_c).
- Métadiscours : « sources lues » (22 occurrences), « n’a pas été lu », « dossier ». C’est la convention de transparence du projet (voir PROMPT_VERITE) et non une faute ; seules les occurrences de « dossier » et d’« îlot » (qui désignent la fabrication du cours) font l’objet de propositions.
- Anglicisme admis : « drapeaux rouges » (parties 8.2 et 9.7) et « sagging » (entre guillemets, traduction absente). Non modifiés.
- Libellé « Lésions élémentaires » de la fiche 2 (c) : terme de dermatologie appliqué à des signes d’imagerie ; rubrique de gabarit, non modifiée.
- Les libellés de liens interactifs portent systématiquement une parenthèse de destination (« libellé (destination) », STYLE_REDACTION § 5) ; seules les parenthèses imbriquées ont donné lieu à des propositions (P-03, P-21, P-54).

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucune lecture des sources primaires citées (ICHD-3, consensus de 2023, méta-analyses, informations professionnelles) : les écarts avec les sources ne sont établis que par comparaison interne entre les sept fichiers de la leçon.
- Aucun contrôle de rendu navigateur des propositions : l’application a été simulée en mémoire (comptage des balises, conservation des data-evidence et des data-k, build_medina.audit() sur le résultat), aucun fichier canonique n’est modifié.
- Les espaces insécables, la graphie « Fribourg-en-Brisgau » et l’harmonisation chiffres/lettres sont différés (voir la rubrique « differes »).
- La grille de sémiologie et l’exigence de calculs relèvent de l’audit MED et n’ont pas été traitées par ce rôle.
- Le manifeste (base_sha 523832d9) et le HEAD du worktree (103745ba) diffèrent ; les empreintes des sept fichiers sont conformes au manifeste.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes | oui |
| Propositions | 105 |
| Propositions à ancien unique | 105 sur 105 |
| Renvois médicaux | 27 |
| Choix différés | 4 |
| Constats hors périmètre | 2 |
| Abréviations non couvertes avant / après application | 0 / 0 |
| Source canonique modifiée | non |

Horodatage : date_debut non relevé (null) ; date_fin 2026-10-16T10:05:35Z (date -u avant le commit).
