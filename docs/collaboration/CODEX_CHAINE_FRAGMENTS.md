# MEDINA — chaîne de production des dix fragments Codex

La demande actuelle de Vial autorise la mise en route de la file Codex : **un fragment entier à la fois, un seul chapitre courant, plusieurs missions spécialisées en parallèle dans ce chapitre**. Codex coordonne la production, remet chaque chapitre à Claude, reçoit sa contrelecture, corrige, fait contre-vérifier, puis injecte et publie. Le fragment suivant s'ouvre seulement après clôture prouvée du précédent.

La chaîne commence par **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**, avec l'inventaire des sources, livraisons et réserves existantes avant reprise. Cette consigne remplace l'attente globale d'achèvement de C-01-Cardiologie avant l'ouverture de la file Codex. La cardiologie conserve ses réserves, ses preuves et ses travaux dans le suivi partagé ; elle n'est pas déclarée achevée. Avant activation, vérifier qu'aucun autre chapitre Codex n'est déjà actif ; une réserve cardiologique conservée ne devient pas une seconde production Codex.

Lire [AGENTS.md](../../AGENTS.md), [la répartition commune](FRAGMENTS_RESTANTS.md), [le plan](../../organisation/production_plan.json), [la passation](HANDOFF_LATEST.md), [les livraisons repérées](DELIVERIES_LATEST.md), [le protocole de remise](DELIVERY_PROTOCOL.md), [le cahier Claude](CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md) et [la règle CIM-11](../COMPLETUDE_CIM11.md) à leur tête partagée actuelle. Les sources, reçus et commits contrôlés priment sur une copie ancienne. Une attribution ou une mission publiée ne prouve pas sa prise en charge.

## File des fragments entiers

Toutes les catégories et sous-catégories restent regroupées dans leur fragment de rattachement. La file attribue des fragments entiers ; elle ne distribue pas les catégories individuellement entre les agents.

| Position | ID stable | Fragment entier Codex |
| --- | --- | --- |
| 1 | T1 | I-03-Infectiologie |
| 2 | S08 | N-05-Neurologie |
| 3 | S04 | N-07-Néphrologie |
| 4 | T4 | O-09-Oncologie, génétique médicale et soins palliatifs |
| 5 | S16 | O-11-Obstétrique et néonatologie |
| 6 | S07 | I-13-Immunologie et allergologie |
| 7 | S15 | U-15-Urologie et andrologie |
| 8 | S11 | D-16-Dermatologie |
| 9 | T5 | D-20-Diagnostic clinique et examens complémentaires |
| 10 | T6 | M-21-Médecine de premier recours et santé publique |

Dans le fragment actif, prendre les priorités du registre puis l'ordre du catalogue, en reprenant d'abord le cours primaire existant lorsque sa revue reste ouverte. Chaque chapitre se termine avant le suivant. D-20-Diagnostic clinique et examens complémentaires exige un inventaire pédagogique et des identifiants canoniques avant réservation ; son inventaire actuellement vide ne démontre aucun achèvement.

Nommer toute catégorie ou tout chapitre cité **code — intitulé (libellé complet du fragment)**. Le titre du cours et l'intitulé du catalogue restent distincts quand leurs sources le sont. Les champs techniques `code`, `title` et `fragment_id` restent séparés dans le plan, les commandes et les manifestes.

Les cours communs ont un producteur unique et des renvois contrôlés. **M30 — Périartérite noueuse et affections apparentées (R-14-Rhumatologie et orthopédie)** conserve son rattachement Claude et renvoie au cours **M31 — Vascularites systémiques (I-13-Immunologie et allergologie)**, produit par Codex. La révision de ce cours doit conserver les particularités de la catégorie consommatrice et leur accès autonome ; elle ne transfère aucune catégorie au fragment Codex.

## Capacité et propriété des fichiers

Le dispositif prévoit **24 missions spécialisées, réparties en quatre vagues de six**. La capacité de cette session est de **sept agents actifs au total, coordinateur compris** : au maximum six sous-agents simultanés. Les 24 missions s'exécutent par vagues ; certaines peuvent revenir au même agent après clôture de sa mission précédente. Toute autre tâche utilisant un slot réduit la capacité disponible.

Chaque mission reste dans le chapitre actif. Les recherches et propositions peuvent être parallèles ; les vagues suivantes commencent lorsque leurs prérequis sont disponibles. Codex fixe pour chaque délégation le nom complet du chapitre, son fragment, le SHA de départ, les chemins autorisés, les chemins en lecture seule, les sources attendues, les dépendances et le format de remise.

**Un auteur par fichier à un instant donné.** Les quatre HTML principaux ont chacun un auteur désigné ; les spécialistes qui contribuent au même onglet remettent des propositions ou patchs séparés à cet auteur. Les fichiers auxiliaires sont attribués individuellement. Les modifications transversales du glossaire, de la banque de fenêtres, du manifeste ou du registre passent par le coordinateur lorsque leur propriétaire n'est pas explicitement désigné. Les agents préservent les fichiers et changements existants.

Utiliser le checkout existant : une tâche cloud est déjà isolée et ne nécessite pas de nouveau worktree. Les validations des copies proposées peuvent employer un répertoire temporaire distinct, sans écraser les sources canoniques ou les travaux d'une autre session. Seul le coordinateur effectue les opérations Git communes, fige les commits, assemble, intègre et publie ; aucun `checkout`, `reset`, fusion ou commit concurrent par les sous-agents.

## Les 24 missions dans le chapitre courant

Les chemins concrets sont fixés à la réservation. Les numéros ci-dessous désignent des responsabilités ; ils ne déclarent pas des agents démarrés ni des résultats obtenus.

### Vague 1 — périmètre, sources et plan

| Rôle | Mission | Remise et droit d'écriture |
| --- | --- | --- |
| R01 — Classification et périmètre | Contrôler catégories, sous-catégories, variantes, correspondances officielles et rattachements du chapitre ; identifier les lacunes d'inventaire. | Matrice versionnée et propositions dans ses fichiers dédiés ; registres canoniques en lecture seule. |
| R02 — Référentiels suisses | Vérifier les recommandations et informations professionnelles applicables en Suisse, leurs versions et leurs passages utiles. | Références précises, citations localisées et limites d'accès dans son dossier dédié. |
| R03 — Référentiels européens | Examiner les recommandations européennes pertinentes et les différences d'application. | Matrice de recommandations et divergences sourcées ; aucun HTML principal modifié. |
| R04 — Preuves et études | Vérifier les études, niveaux de preuve, populations, effets, limites et incertitudes derrière les affirmations retenues. | Tableau affirmation → preuve → limite, avec références exactes. |
| R05 — Actualité et arbitrages | Comparer dates, versions, seuils et recommandations contradictoires ; distinguer preuve, consensus et point non vérifié. | Liste d'arbitrages proposée au coordinateur, sans effacer une réserve. |
| R06 — Plan pédagogique | Organiser les notions nouvelles, le normal avant le pathologique et les objectifs des quatre onglets. | Plan du seul chapitre, repères stables et contrats de remise aux auteurs. |

### Vague 2 — pathologie et raisonnement clinique

| Rôle | Mission | Remise et droit d'écriture |
| --- | --- | --- |
| R07 — Anatomie et physiologie | Expliquer les fonctions normales nécessaires à la compréhension du chapitre. | Propositions sourcées pour les auteurs, fichiers intermédiaires dédiés. |
| R08 — Physiopathologie | Relier les causes aux mécanismes, signes, conséquences cliniques et limites. | Matrice causale localisée ; propositions sans écriture dans les onglets possédés par d'autres. |
| R09 — Présentation clinique | Vérifier signes, symptômes, formes, gravité et populations pertinentes. | Texte proposé avec distinctions utiles et références. |
| R10 — Diagnostic et décision | Vérifier critères formels, confirmation objective et décisions découlant des résultats. | Proposition des critères finaux et paramètres clés, avec justification de chaque étape. |
| R11 — Différentiels et urgences | Distinguer diagnostics concurrents, situations urgentes et erreurs susceptibles de changer la conduite. | Tableau commenté et précautions à garder visibles dans le texte principal. |
| R12 — Auteur Pathologie | Assembler les résultats acceptés dans l'onglet Pathologie ; préserver le contenu utile et les repères. | Auteur unique du HTML principal Pathologie, normalement `<CODE>_a.html`, avec rapport de couverture. |

### Vague 3 — examens, sciences et pharmacologie

| Rôle | Mission | Remise et droit d'écriture |
| --- | --- | --- |
| R13 — Auteur Examens et biologie | Justifier indication, principe, préparation, normal, interprétation, limites et conduite ; assembler l'onglet Examens. | Auteur unique du HTML principal Examens, normalement `<CODE>_b.html`. |
| R14 — Imagerie et explorations | Vérifier examens d'imagerie et fonctionnels, performances, risques et conséquences sur les décisions. | Propositions dédiées à R13 ; aucun accès en écriture à son HTML. |
| R15 — Auteur Sciences | Développer les mécanismes scientifiques et leurs conséquences cliniques, avec les résultats de R07 et R08. | Auteur unique du HTML principal Sciences, normalement `<CODE>_c.html`. |
| R16 — Choix thérapeutiques | Vérifier indications, alternatives, bénéfices, objectifs et mécanismes d'action des traitements. | Matrice thérapeutique sourcée proposée à R18. |
| R17 — Doses et populations | Vérifier doses, unités, voies, adaptations, contre-indications, interactions et surveillance pertinentes. | Tableau contrôlé sur les sources consultées ; valeurs non vérifiées conservées en réserve. |
| R18 — Auteur Pharmacologie | Assembler mécanismes, choix et utilisation clinique des traitements dans l'onglet Pharmacologie. | Auteur unique du HTML principal Pharmacologie, normalement `<CODE>_d.html`. |

### Vague 4 — contenus associés et validation préparatoire

| Rôle | Mission | Remise et droit d'écriture |
| --- | --- | --- |
| R19 — Fenêtres contextualisées | Expliquer les affirmations et décisions au passage concerné : réponse, mécanisme, conséquence, limites et source. | Auteur des seuls fichiers de fenêtres qui lui sont explicitement attribués ; propositions pour toute banque partagée. |
| R20 — Figures et schémas | Vérifier précision, légendes, lisibilité et concordance médicale des figures. | Fichiers graphiques dédiés ou propositions ; aucun fichier attribué à R19 modifié. |
| R21 — Tableaux et exemples | Contrôler comparaisons, unités, exemples chiffrés, introduction et commentaire des tableaux. | Propositions localisées aux auteurs des onglets, sans écrire dans leurs fichiers. |
| R22 — Quiz et Pareto | Vérifier questions, réponses, explications et synthèses ; préserver les précautions qui changent la décision. | Fichiers auxiliaires dédiés ou propositions à l'auteur du fichier concerné. |
| R23 — Français et glossaire | Vérifier phrases complètes, progression, répétitions, nomenclature et définition littérale des abréviations. | Rapport et propositions ; écriture du glossaire uniquement avec propriété explicite du fichier. |
| R24 — Contrat et navigateur | Contrôler HTML, identifiants, classes, liens, compilation et parcours global/autonome sur ordinateur et mobile. | Journaux, captures et anomalies au SHA testé ; contrôles en lecture seule des sources, sorties isolées. |

Chaque affirmation médicale reçoit une justification précise, ses limites et une source réellement consultée. Les informations décisives restent dans le texte principal. Les quatre onglets et leurs fenêtres, figures, tableaux, quiz, Pareto, glossaire et références appartiennent au périmètre du chapitre. Aucun quota de mots ni succès de compilation ne remplace ces exigences.

## Trio de sentinelles aux passages délicats

À la réception d'une remise, à la clôture d'un audit et avant injection ou publication, réserver **trois slots au trio de sentinelles**, plus le coordinateur. Il reste alors **au maximum trois auteurs actifs** ; réduire ou terminer les autres missions avant d'ouvrir cette phase. Une réserve prioritaire prime sur le lancement d'une nouvelle vague.

Les sentinelles travaillent indépendamment de l'auteur : elles n'ont pas écrit les sources qu'elles contrôlent, n'en modifient aucune et rendent trois avis séparés au même SHA figé. Elles peuvent lire les rapports déjà reçus mais vérifient leurs preuves. Leur contrôle prépare et surveille la décision ; **l'audit médical croisé Claude ↔ Codex reste obligatoire**.

| Sentinelle | Réception et audit | Intégrité, injection et déploiement |
| --- | --- | --- |
| S1 — Sources et audit médical | Vérifier identité du chapitre, périmètre réellement relu, sources accessibles, justification des arbitrages, réserves et rapport indépendant de l'autre responsable au SHA proposé. | Vérifier que les corrections médicales ont été contre-vérifiées et qu'aucune adaptation nouvelle n'échappe à cet audit ; stopper si réserve majeure. |
| S2 — Provenance et contenu | Comparer SHA de départ, SHA livré, manifestes, empreintes et diff ; relever fichiers partagés, changements concurrents, aliases de cours et pertes de contenu. | Comparer proposition acceptée et sources injectées ; préserver commits et rapports du contributeur ; vérifier reçus et correspondance entre commits audités et intégrés. |
| S3 — Technique et publication | Vérifier contrat des sources, méthode de validation des copies, commandes réellement exécutées, résultats et limites. | Contrôler reconstruction, tests adaptés, navigateur global et fragment autonome ; vérifier SHA publié, déploiement Pages, liens et contenu réellement servi. |

Un avis mentionne le SHA, les fichiers, les contrôles effectués, les réserves et sa conclusion. Une source inaccessible, une incohérence d'empreinte, une perte de contenu, une erreur médicale, une réserve majeure ou un contrôle requis en échec conserve le chapitre en `blocked`. Le coordinateur réceptionne la preuve, corrige dans le chapitre courant et refait le contrôle affecté au nouveau SHA. Les observations mineures restantes demandent une décision motivée et conservée dans le reçu ; elles ne sont pas masquées par un « validé » global.

## Chaîne de remise, audit et injection par chapitre

Les étapes ci-dessous se répètent pour chaque chapitre du fragment actif. Les états des rapports peuvent être plus détaillés que `active_chapter.stage` ; ce dernier utilise seulement `writing`, `review`, `checks`, `integration` ou `blocked` jusqu'à sa libération après clôture.

| Checkpoint | Opération et preuves obligatoires | Condition de passage |
| --- | --- | --- |
| C0 — Réservation | Inventorier branches et PR avec pagination, relire reçus et diff utiles ; fixer fragment, chapitre primaire, SHA complet de départ, chemins et rapport. Consigner un seul `agents.Codex.active_chapter` avec `fragment_id`, `code`, `title`, `stage`, `base_commit`, `report_path`. | Aucun autre chapitre Codex actif ; sources actuelles identifiées ; validation structurelle par `python3 tools/production_plan.py`. |
| C1 — Production | Exécuter les quatre vagues dans le seul chapitre ; assembler sous responsabilité Codex, conserver corrections reçues et réserves, contrôler les copies proposées avec une méthode isolée. | Sources et contenus associés complets pour le périmètre annoncé ; aucun résultat de contrôle supposé. |
| C2 — Remise à Claude | Déposer sources et rapport dans `livraisons/Livraison Codex/<libellé>/`, un chapitre par lot et PR ; préserver empreintes de base, publier le SHA livré et les preuves préparatoires. Rendre le lien et la demande d'audit accessibles à Claude. | Disponibilité distante vérifiée. L'état reste « remis à Claude » jusqu'à son accusé ; aucune lecture ni session externe présumée. |
| C3 — Réception de l'audit Claude | Relever rapport, branche, commit du rapport et SHA exact du contenu examiné. Le trio vérifie couverture et réserves. Codex accuse réception sous `docs/collaboration/receipts/`. | Contrelecture indépendante Claude reçue et périmètre explicite ; une autoévaluation Codex ne la remplace pas. |
| C4 — Correction et contre-vérification | Corriger les réserves sur les sources proposées ; figer le nouveau SHA de contenu, conserver le premier rapport et remettre les corrections à Claude. Recevoir sa contre-vérification du nouveau SHA. | Aucune réserve bloquante ; audit accepté sur le contenu exact à injecter ; trio sans blocage ouvert. |
| C5 — Injection canonique | Codex vérifie conflits et écritures concurrentes, injecte les sources acceptées ou intègre les commits appropriés, puis reconstruit. Conserver SHA livré, SHA audité, SHA corrigé et SHA d'intégration, avec adaptations expliquées. | Proposition acceptée et sources canoniques rapprochées. Si un conflit exige une adaptation médicale, la préparer dans la proposition et la faire contre-vérifier avant son écriture canonique. Un reçu automatique provisoire ne clôt rien. |
| C6 — Contrôles et publication | Réexécuter les contrôles adaptés au SHA d'intégration, global et fragment autonome, ordinateur et mobile. Publier sources et reçu ; relever SHA publié, déploiement Pages, liens et contenu servi vérifiés. | Audit clos, tests requis réussis, sources injectées, reçu définitif, disponibilité distante et déploiement vérifiés. Libérer alors `active_chapter` et réserver le chapitre suivant du même fragment. |
| C7 — Clôture du fragment entier | Vérifier tous les chapitres et enseignements attendus, sous-catégories, variantes et renvois ; rapprocher la matrice officielle CIM-11 versionnée et les reçus au contenu publié. Claude audite la couverture du fragment et ses réserves. | Aucun enseignement pertinent manquant ni réserve bloquante ; couverture et accès prouvés. Le coordinateur consigne la clôture du fragment avant d'ouvrir le suivant de sa file. |

Pour une **remise Claude**, conserver le sens réciproque : Claude produit → Codex accuse réception et audite → Claude corrige → Codex contre-vérifie → Codex injecte et contrôle → publication vérifiée. Le trio vérifie aussi ces réceptions, sans modifier la branche de Claude ni effacer ses commits. Un lot historique regroupant plusieurs cours reste recevable ; son examen et sa clôture s'effectuent chapitre par chapitre, en préservant ses preuves originales.

Le code primaire est réservé une fois, même si plusieurs catégories renvoient au cours. Les fichiers communs nécessaires au chapitre sont identifiés et justifiés. Ne publier ni simple copie de rapport ni HTML généré comme substitut des sources canoniques. Le plan ne verrouille pas les autres sessions : relire sa tête partagée avant réservation, injection et libération ; signaler toute concurrence.

La clôture du fragment dépend de la règle CIM-11. Le catalogue historique CIM-10-GM, un compteur, `covers` ou `DONE_SYS` ne la démontre pas. Tant que l'inventaire pertinent manque, enregistrer **« couverture CIM-11 non établie »** et poursuivre le travail utile dans le fragment actif ; ne pas ouvrir le suivant pour contourner ce manque. Une suspension et un changement de production nécessitent une décision explicite du propriétaire, tracée avec leurs preuves.

## Veille locale et GitHub

La veille prévue par [tools/claude_watch.py](../../tools/claude_watch.py) et [le workflow GitHub Actions](../../.github/workflows/claude_watch.yml) relève les contributions disponibles, les changements de têtes et les éléments à examiner, puis alimente une file de réception. Les états « détecté », « reçu », « audité », « injecté », « contrôlé » et « publié » restent distincts. Une exécution partielle ou un accès indisponible conserve son erreur explicite ; il ne prouve pas l'absence de livraison.

Pendant une session active, Codex reprend cette file, mobilise le trio aux passages délicats et suit les checkpoints. Après la fin de la session, GitHub Actions peut continuer sa collecte selon sa configuration et conserver les éléments pour la reprise. Cette détection est utile à la continuité : **elle ne crée pas, à elle seule, une session Claude ou Codex, un audit médical par IA, une correction ni une injection**. Une veille locale dépend aussi de la durée de vie réelle du processus et de la machine.

La prochaine session lit les preuves et les nouveaux SHAs avant de continuer le chapitre actif. Le travail reste disponible et ordonné même si une contrelecture externe ou un accès manque. Aucun chapitre nouveau, fragment nouveau, acquittement médical ou changement de propriétaire n'est ouvert automatiquement par une réussite de veille ou de CI.

Pour lancer une collecte ponctuelle depuis le checkout :

```sh
python3 tools/claude_watch.py --once --repo-root /workspace/Medina --state-dir /workspace/medina-env/claude-watch
```

Pour la boucle locale, utiliser les mêmes arguments avec `--interval 300` à la place de `--once`, dans une session persistante. Vérifier d'abord qu'aucune boucle ne cible déjà cet état. Lire `status.json` : seul un `status: ok` récent établit la réussite du dernier scan. `degraded` conserve les éléments antérieurs et expose l'erreur ; `busy` indique un autre scan actif. Lire ensuite `queue.json`, puis les sources au SHA annoncé. L'état `detected_pending_audit` du détecteur ne reprend pas automatiquement les verdicts humains consignés dans les reçus.

Le point d'entrée pour Claude est [SIGNAUX_CODEX.json](SIGNAUX_CODEX.json), qui donne le chapitre actif, le SHA demandé pour la revue initiale et les rapports de retour sur ses remises. La disponibilité distante, l'accusé de réception et la clôture d'un audit sont consignés séparément. Une nouvelle tête ne réutilise un contrôle ancien que si l'identité des fichiers concernés est effectivement vérifiée.

À chaque remise au propriétaire, citer le chapitre avec son fragment, l'étape atteinte, les SHAs réellement reçus et contrôlés, les liens publiés, les réserves et la prochaine opération du même chapitre. Ce document organise la chaîne ; il ne certifie aucune production, prise en charge Claude ou clôture médicale par sa seule présence.
