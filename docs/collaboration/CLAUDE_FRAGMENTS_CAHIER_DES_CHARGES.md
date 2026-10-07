# MEDINA — cahier des charges exécutable de Claude

Consigne de Vial du **8 octobre 2026**. **Codex, coordinateur de cette session, prend le relais de GPT « work »** pour l'organisation, la réception, les audits croisés, l'injection et la publication. Conserver les contributions et les commits de GPT « work » et des autres sessions ; une priorité de coordination ne permet pas de les supprimer ou de les écraser.

**La répartition porte sur des fragments entiers : 11 fragments pour Claude et 10 fragments pour Codex. Mission Claude : produire ou reprendre ses 11 fragments, avec un seul chapitre actif, puis auditer indépendamment chaque chapitre remis par Codex.** Toutes les catégories et sous-catégories restent regroupées dans leur fragment propriétaire ; aucune redistribution de catégories entre responsables n'est autorisée par cette répartition. Claude et Codex avancent en parallèle sur leurs chapitres respectifs. Chaque responsable utilise plusieurs sous-agents spécialisés **dans son chapitre actif**. La disponibilité de ce document ne prouve ni que Claude l'a lu, ni qu'une session Claude a démarré.

**Nomenclature obligatoire : chaque catégorie ou chapitre cité dans le texte, les tableaux, les rapports et les navigations apparaît sous la forme `code — intitulé (libellé complet du fragment)`.** Employer le titre canonique du chapitre lorsqu'on cite un cours, et l'intitulé officiel du catalogue lorsqu'on cite une catégorie. Les codes techniques des commandes, identifiants et chemins restent stables ; leur désignation complète figure dans le texte qui les présente.

## 1. Références et reprise obligatoire

Lire à la tête publiée actuelle, dans cet ordre :

1. [`AGENTS.md`](../../AGENTS.md), [`CLAUDE.md`](../../CLAUDE.md), le présent cahier, [`FRAGMENTS_RESTANTS.md`](FRAGMENTS_RESTANTS.md) et [`organisation/production_plan.json`](../../organisation/production_plan.json).
2. [`HANDOFF_LATEST.md`](HANDOFF_LATEST.md), [`DELIVERIES_LATEST.md`](DELIVERIES_LATEST.md), les [reçus](receipts/) et les rapports des contributions qui touchent le chapitre choisi.
3. [`PROMPT_MEDINA.md`](../../PROMPT_MEDINA.md), [`CHAPTER_SPEC.md`](../../CHAPTER_SPEC.md), [`STYLE_REDACTION.md`](../STYLE_REDACTION.md), [`DELIVERY_PROTOCOL.md`](DELIVERY_PROTOCOL.md) et [`COMPLETUDE_CIM11.md`](../COMPLETUDE_CIM11.md).
4. [`MECHANISMS_PLAN.json`](MECHANISMS_PLAN.json) et [`MECHANISMS_CLAUDE.md`](MECHANISMS_CLAUDE.md) pour rattacher les relectures existantes et conserver leurs limites explicites.

Les nouvelles consignes de répartition et de progression par chapitre remplacent les anciens cycles de deux systèmes et les objectifs historiques de longueur. Les contrats de sources, de rendu, de nomenclature et de justification demeurent applicables.

Inventorier **toutes les branches et PR, avec pagination**, pas seulement le clone local ou une branche Claude. Exécuter `python3 tools/collaboration_sync.py --out docs/collaboration`, ou fournir un inventaire équivalent au scanner avec `--snapshot` si seul le connecteur fonctionne. Une collecte partielle doit indiquer ce qui manque ; elle n'autorise pas à conclure qu'une livraison n'existe pas. Lire aussi les anciens rapports à plat et les branches sans PR.

Vérifier les têtes de `main` et de `codex/sciences-cs-fragments-20261007`. Le protocole actuel désigne cette dernière comme branche d'intégration : confirmer qu'elle reste la destination avant une remise. Les sources canoniques les plus récentes, les reçus et les commits effectivement contrôlés priment sur une copie de livraison ancienne. Noter le SHA complet de départ. Utiliser le checkout existant lorsque possible ; une tâche cloud est déjà isolée et ne nécessite pas de nouveau worktree.

**Priorité cardiologie : vérifier son état réel.** Le plan conserve la mission C-01-Cardiologie avant l'ouverture des files suivantes. Repérer les réserves, remises et audits encore ouverts ; les signaler au coordinateur avec leurs preuves. Ne déclarer cette priorité clôturée qu'à partir des reçus, contrôles et publications correspondants. Les 21 attributions ci-dessous ne certifient pas l'achèvement de la cardiologie et ne doivent pas effacer ses travaux.

## 2. Les 11 fragments dont Claude est responsable

Suivre cet ordre ; les identifiants et libellés proviennent du registre partagé. **Chaque ligne attribue l'ensemble du fragment**, avec ses catégories, ses sous-catégories, ses chapitres et ses contenus associés. Cette liste ne distribue pas les catégories individuellement entre Claude et Codex.

| File Claude | ID stable | Libellé exact du fragment entier |
| --- | --- | --- |
| 1 | S02 | P-02-Pneumologie |
| 2 | S03 | G-04-Gastroentérologie et hépatologie |
| 3 | S05 | E-06-Endocrinologie et métabolisme |
| 4 | S06 | H-08-Hématologie |
| 5 | S14 | G-10-Gynécologie et sénologie |
| 6 | T2 | M-12-Médecine des âges de la vie |
| 7 | S10 | R-14-Rhumatologie et orthopédie |
| 8 | S12 | O-17-Oto-rhino-laryngologie et médecine bucco-dentaire |
| 9 | S13 | O-18-Ophtalmologie |
| 10 | T3 | M-19-Médecine d’urgence, traumatologie et toxicologie |
| 11 | T7 | E-22-Éthique médicale, droit et communication |

Les axes transversaux exigent également un inventaire pédagogique et des chapitres nommés. Ils ne sont pas terminés par défaut. Les cours communs existants conservent **un producteur unique**, sans modifier les rattachements de leurs catégories : coordonner les renvois vers les passages spécifiques accessibles dans tous les fragments consommateurs. Ainsi, **M30 — Périartérite noueuse et affections apparentées (R-14-Rhumatologie et orthopédie)** reste une catégorie du fragment Claude et renvoie au cours primaire **M31 — Vascularites systémiques (I-13-Immunologie et allergologie)**, produit par Codex selon l'organisation commune existante. Claude ne crée pas un deuxième cours indépendant pour cette catégorie. Ce renvoi ne transfère ni la catégorie ni ses sous-catégories au fragment Codex ; vérifier leurs enseignements spécifiques dans le cours commun et leur accès depuis le fragment propriétaire Claude.

Le premier point d'entrée après vérification de la priorité cardiologie est **J45 — Asthme (P-02-Pneumologie)**, en commençant par sa revue exhaustive si elle reste ouverte. Le titre canonique est `Asthme` dans `chapters.json` et `MECHANISMS_PLAN.json` ; conserver ce titre dans les rapports et navigations. Le cours traite aussi **J46 — État de mal asthmatique (P-02-Pneumologie)** : vérifier les enseignements spécifiques, sans assimiler le regroupement à une couverture complète et sans déplacer les catégories. **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)** est le premier point d'entrée Codex et la première cible d'audit croisé lorsque Codex en publie une remise. Ces points d'entrée ne constituent pas une déclaration de démarrage.

## 3. Parallélisme autorisé et responsabilité des fichiers

Maintenir **un fragment actif et un chapitre actif par responsable**, même lorsque plusieurs sous-agents travaillent. Claude peut auditer la remise de Codex en parallèle de son propre chapitre : cet audit n'ouvre pas une seconde production. Aucun sous-agent ne commence un autre chapitre ou fragment.

Claude désigne un responsable d'assemblage et délègue, dans la limite des ressources disponibles :

| Sous-agent | Mission dans le chapitre actif | Remise attendue |
| --- | --- | --- |
| Sources et référentiels | Vérifier recommandations, indications, seuils, preuves et correspondances CIM ; hiérarchiser sources suisses, européennes puis internationales applicables en Suisse. | Matrice affirmation → référence précise, version, date de consultation, passage cité et limites d'accès. |
| Pathologie et rédaction | Réviser définition, présentation, mécanismes, démarche diagnostique et prises en charge ; assurer la compréhension des notions nouvelles. | Texte ou patch limité à l'onglet Pathologie, avec repères stables. |
| Examens | Justifier indication, principe, préparation, interprétation, limites et conséquence sur la conduite. | Texte ou patch limité à l'onglet Examens ; distinction normal/pathologique. |
| Sciences | Expliquer les mécanismes causaux et leurs conséquences cliniques, de la physiologie normale à la pathologie. | Texte ou patch limité à l'onglet Sciences, avec sources et réserves. |
| Pharmacologie | Vérifier mécanismes d'action, indications, choix, doses, unités, adaptation, contre-indications, interactions et surveillance pertinentes. | Texte ou patch limité à l'onglet Pharmacologie ; points à confirmer explicitement. |
| Fenêtres et pédagogie | Préparer fenêtres contextualisées, figures, tableaux, quiz, Pareto et glossaire ; conserver les informations décisives dans le texte principal. | Fichiers auxiliaires dédiés ou propositions identifiées, sans écriture dans les quatre onglets possédés par d'autres agents. |
| Audit technique et assemblage | Vérifier contrat HTML, liens, identifiants, abréviations, compilation et navigateur. | Journaux de contrôles et anomalies localisées ; aucune certification médicale déduite des tests. |

Avant chaque délégation, donner à chaque sous-agent : la désignation `code — intitulé (libellé complet du fragment)`, le SHA de départ, les chemins qu'il peut modifier, les chemins en lecture seule, les notions attendues, les références à vérifier et le format de remise. Certains rôles peuvent partager un agent ou s'exécuter par vagues selon le nombre de places ; cela ne change pas le périmètre actif ni le regroupement des catégories dans le fragment propriétaire.

**Un seul auteur par fichier à un instant donné.** Les recherches et relectures peuvent être parallèles ; les écritures concurrentes dans un même HTML, glossaire, manifeste, banque JSON ou fichier partagé sont interdites. L'assembleur applique les propositions transversales après réception. Les sous-agents ne font pas de `checkout`, `reset`, fusion ou commit simultané dans un checkout partagé. Réserver les opérations Git au responsable et utiliser des fichiers intermédiaires distincts si nécessaire.

Claude conserve sa branche et ses commits ; il ne pousse pas sur la branche Codex, ne la déplace pas et ne réécrit pas son historique. Codex reste responsable des écritures d'intégration et des mises à jour communes après réception. Une branche Claude existante reste recevable ; ne pas la remettre artificiellement au niveau de Codex. Aucun secret ou jeton n'est transféré.

## 4. Réserver et terminer un chapitre

Relire le dernier plan partagé avant réservation. Pour **J45 — Asthme (P-02-Pneumologie)**, déclarer au coordinateur, avec le SHA de référence et le rapport prévu, un objet unique de cette forme ; les champs techniques gardent leurs valeurs canoniques distinctes :

```json
{
  "fragment_id": "S02",
  "code": "J45",
  "title": "Asthme",
  "stage": "writing",
  "base_commit": "<SHA-complet-de-depart>",
  "report_path": "livraisons/Livraison Claude/P-02-Pneumologie/travail/<lot-J45>/rapport.md"
}
```

Le coordinateur consigne cette réservation dans `agents.Claude.active_chapter` sans écraser une modification concurrente. Remplacer les valeurs entre chevrons par le SHA réel de 40 caractères hexadécimaux et un nom de lot réel. Les champs `fragment_id`, `code`, `title`, `stage`, `base_commit`, `report_path` sont des chaînes non vides ; `report_path` est relatif au dépôt et ne sort pas de celui-ci. Réserver le code primaire d'un cours commun, avec son titre canonique et son rattachement réel au fragment. Vérifier avec `python3 tools/production_plan.py`. **Le validateur vérifie la structure et la provenance de la réservation ; il ne certifie pas les preuves d'audit, les tests, la clôture ou la publication.** Le plan est un suivi partagé, **pas un verrou distant** ; signaler une réservation déjà active ou un conflit de sources avant d'écrire. Les étapes admises sont `writing`, `review`, `checks`, `integration`, `blocked`.

Le chapitre comprend les quatre onglets **Pathologie, Examens, Sciences, Pharmacologie**, leurs fenêtres, figures, tableaux, quiz, Pareto, glossaire et références. Reprendre aussi les contenus associés déjà présents et les variantes pertinentes des catégories couvertes. Conserver les identifiants, routes et fonctions de lecture ; ne pas reconstruire une architecture différente ni réactiver la coque V7 abandonnée.

Chaque affirmation médicale ou décision doit exposer sa justification causale ou clinique précise, sa conséquence, ses limites et sa référence. Pour un examen biologique, distinguer **pourquoi le doser, comment interpréter le résultat et comment agir**. Distinguer association et causalité, preuve et consensus. Une fenêtre ciblée ne vaut pas revue exhaustive. Les mises en garde qui changent une décision restent visibles dans le texte principal. Aucun quota de mots ne remplace ces exigences.

Employer un français professionnel compréhensible, des phrases complètes, un développement logique et des exemples chiffrés exacts lorsque utiles ; expliquer le normal avant le pathologique. Introduire et commenter les tableaux. Toute abréviation possède sa définition littérale dans le glossaire. Respecter le contrat HTML, la liste de classes, les préfixes du code et les critères diagnostiques formels finaux, puis les paramètres clés.

Pour **J45 — Asthme (P-02-Pneumologie)**, vérifier explicitement la cohérence entre diagnostic et confirmation objective, diagnostics différentiels, appréciation du contrôle et du risque, traitement de fond et de secours, technique et observance des dispositifs, exacerbation aiguë, limites d'application selon la population et suivi. Justifier chaque point à partir des sources officielles effectivement consultées ; ne pas annoncer une version de recommandation ou une dose comme vérifiée sans cette consultation.

Le chapitre reste actif si une source, un audit, un accès, un contrôle ou une publication bloque. Rapporter ce blocage avec son opération précise et poursuivre les travaux utiles **dans ce chapitre**, dont la contrelecture disponible. Seule une décision explicite du propriétaire permet sa suspension et l'ouverture d'une autre production. L'attente d'injection n'autorise pas à démarrer le chapitre suivant.

## 5. Remise de Claude : un chapitre, preuves et PR

Déposer les sources et le rapport dans `livraisons/Livraison Claude/<libellé-exact>/`, avec un sous-dossier de travail ou d'archives distinct pour chaque lot. Suivre le protocole de livraison ; préserver toute copie ou correction déjà présente. `prepare-claude` opère à l'échelle d'un fragment : vérifier son périmètre et les fichiers existants avant usage, puis restreindre le lot remis au **seul chapitre actif**. Les fichiers partagés nécessaires sont nommés et justifiés individuellement.

Le manifeste conserve, pour chaque remplacement, `target_path`, `source_path` et **l'empreinte SHA-256 de la source originale** ; ne pas remplacer cette empreinte par celle de la correction. Pour les ajouts admis par l'outil, utiliser `operation: "add"`, `sha256: null` et `proposed_sha256`. L'outil accepte les HTML/JSON primaires des cours déjà intégrés ; remettre créations de cours, glossaires et corrections transversales par branche/PR avec leur rapport et leur diff.

Chaque rapport, selon [`REVIEW_TEMPLATE.md`](REVIEW_TEMPLATE.md), comporte :

- Identité du responsable, sous-agents mobilisés, désignation `code — intitulé (libellé complet du fragment)`, lot et dates ; regrouper les catégories et sous-catégories sous leur fragment propriétaire.
- Branche, SHA complet de départ, SHA effectivement relu, SHA livré et lien de PR ; compléter le SHA livré après le commit, sans inventer une référence future.
- Liste des sources canoniques et des copies modifiées, empreintes, périmètre détaillé par onglet et repère stable.
- Matrice des affirmations contrôlées et des corrections, sources primaires avec version, URL/DOI, section/page/tableau, date de consultation et statut d'accès au texte.
- Commandes exactes réellement exécutées, résultats, journaux et captures pertinentes ; conserver les échecs et les contrôles non exécutés.
- Réserves médicales, rédactionnelles, techniques et CIM-11 séparées ; sections non relues, sources inaccessibles et conditions encore bloquantes.
- Demande de contrelecture à Codex du **commit exact**, puis tableau de bord de livraison : cours, catégories réellement traitées, fragments consommateurs, taille des sorties et alertes.

Publier sur sa branche et ouvrir **une PR par chapitre** vers la branche d'intégration confirmée. L'autorisation permanente de Vial couvre les publications GitHub de MEDINA ; elle ne crée pas une connexion technique manquante. Si l'écriture est indisponible, remettre sources, rapport et patch complet ; l'absence de push ne doit pas être présentée comme une publication. Ne pas publier seulement un HTML généré ou un rapport sans les sources de sa correction.

## 6. Audit croisé indépendant avant injection

**Pour chaque chapitre Claude : Claude produit → Codex audite → Claude corrige → Codex contre-vérifie → injection.**

**Pour chaque chapitre Codex : Codex produit → Claude audite → Codex corrige → Claude contre-vérifie → injection.**

L'auditeur examine un SHA complet fixé et publie son propre rapport. Il consulte indépendamment les références et vérifie tous les onglets et contenus associés ; il ne se limite pas aux fenêtres ajoutées ou au rapport de l'auteur. Identifier chaque anomalie par fichier et repère, avec gravité, raison, source et correction attendue. Une affirmation laissée non vérifiée demeure une réserve. Toute correction qui modifie une conclusion médicale est réauditée au nouveau SHA ; conserver le rapport initial et la contre-vérification.

**Une erreur médicale, une réserve majeure non résolue, une perte de contenu utile ou un contrôle requis en échec bloque l'injection.** Le coordinateur réceptionne la remise, enregistre les observations et conserve le chapitre actif. Les observations mineures restantes nécessitent une décision explicite et motivée dans le reçu ; elles ne doivent pas être masquées par une mention globale « validé ».

Pour l'audit de **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**, vérifier notamment définitions et limites diagnostiques, recherche du foyer et diagnostics différentiels, prélèvements, traitement anti-infectieux et réévaluation, contrôle du foyer, réanimation et surveillance, populations particulières et justifications physiopathologiques. Vérifier les seuils, doses, unités et délais dans les recommandations effectivement consultées. Aucun point n'est déclaré conforme par cette liste seule.

Les autoaudits et les rapports de sous-agents de l'auteur sont utiles à la préparation, mais ne remplacent pas la contrelecture de l'autre responsable. Claude remet ses audits Codex sur sa propre branche, avec code, titre, SHA examiné et conclusion ; il ne corrige pas directement la branche Codex.

## 7. Contrôles, injection et publication coordonnés par Codex

Effectuer les contrôles préparatoires utiles sur le lot avant remise, puis les répéter sur les sources canoniques résultant de l'injection. Pour **J45 — Asthme (P-02-Pneumologie)**, premier chapitre Claude prévu, les commandes existantes sont :

```bash
python3 tools/production_plan.py
python3 tools/livraison.py check-claude "livraisons/Livraison Claude/P-02-Pneumologie"
python3 test_v7.py --static J45
MEDINA_OUT="$PWD/dist" python3 build_front.py
MEDINA_OUT="$PWD/dist" python3 build_front.py --fragment S02
MEDINA_OUT="$PWD/dist" python3 test_v7.py J45
```

`check-claude` vérifie chemins, empreintes, UTF-8 et syntaxe JSON ; il **ne valide pas la médecine**. Exécuter cette commande sur le dossier contenant réellement `livraison.json`, à adapter si le lot utilise un dossier distinct. Les copies de livraison demandent une compilation isolée de validation avant injection : les commandes de construction ordinaires lisent les sources canoniques et ne prouvent pas que les copies corrigées ont été testées. Utiliser un répertoire temporaire de validation distinct si nécessaire, sans écraser le checkout ou les travaux d'une autre session, puis consigner sa méthode et son SHA.

**Codex seul exécute l'injection après l'audit croisé accepté**, notamment `python3 tools/livraison.py apply-claude "<dossier-contenant-livraison.json>"` lorsque cette voie est applicable. Pour une PR comprenant des sources hors périmètre de cet outil, il examine le diff et intègre les commits sans perdre l'attribution de Claude. Il contrôle les conflits et adaptations, puis reconstruit MEDINA et les fragments consommateurs depuis les sources canoniques. Un reçu automatique « injecté, reconstruction/contrôles à faire » reste provisoire.

Contrôler le navigateur sur ordinateur et mobile : affichage des quatre onglets, fenêtres, quiz, Pareto, navigation, taille de police, mode livre, liens internes, erreurs JavaScript et absence de débordement. Vérifier **aussi le fragment autonome** et ses passages liés : `test_v7.py` cible le `MEDINA.html` global et ne suffit pas à prouver l'accès dans le fragment. Utiliser les tests navigateur existants adaptés ou une vérification documentée. Exécuter les contrôles des outils partagés si leur modification le requiert ; consigner les commandes et résultats réels, jamais une réussite supposée.

Codex publie ensuite les sources et un reçu dans `docs/collaboration/receipts/`, avec SHAs reçu, relu et intégré, chemins, empreintes, audit croisé, adaptations, commandes, résultats et réserves. Actualiser inventaire, passation et tableau de bord. Vérifier séparément disponibilité distante, déploiement Pages et contenu réellement servi au lien du cours ; un push sur une branche n'est pas cette preuve.

**Chapitre suivant autorisé seulement après** sources complètes, audit croisé clos, contrôles réussis, injection canonique, reconstruction, reçu et publication vérifiés. Archiver le rapport, consigner la clôture et laisser le coordinateur remettre `active_chapter` à `null` avant la réservation suivante. Ne passer au fragment suivant qu'après vérification de son périmètre attendu selon la règle CIM-11.

## 8. Complétude et accusé de prise en charge

Construire la matrice officielle CIM-11 versionnée : code, identifiant OMS, intitulé, parent, version, URL, rattachements MEDINA, passage pédagogique spécifique, lien autonome contrôlé et rapport indépendant au SHA exact. L'inventaire historique CIM-10-GM, un `covers`, une catégorie titrée ou une valeur `DONE_SYS` ne démontre pas la complétude. Tant que l'inventaire pertinent manque, indiquer **« couverture CIM-11 non établie »**, sans pourcentage inventé ni fragment déclaré achevé.

À réception de ce cahier, Claude publie un accusé de prise en charge dans sa passation ou son rapport, avec : lien et version du cahier lu, tête Git consultée, livraisons antérieures examinées, état prouvé de la priorité cardiologie, chapitre réservé, répartition des sous-agents, chemins possédés, contrôles prévus et blocages. Codex peut alors enregistrer « mission reçue ». Sans cet accusé, l'état reste **« cahier disponible ; prise en charge non confirmée »**.

Aux remises, distinguer **attribué, actif, livré, reçu, audité, injecté, contrôlé, publié** et l'état de la complétude. Chaque annonce au propriétaire repose sur des SHAs, rapports, contrôles et liens vérifiables. Aucune présence de fichier n'atteste un travail nocturne automatique ou une session externe en cours.
