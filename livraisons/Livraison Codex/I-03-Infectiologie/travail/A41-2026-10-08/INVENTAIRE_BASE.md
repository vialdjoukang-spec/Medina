# A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie) — inventaire de base

Relevé du **8 octobre 2026**, réalisé en lecture seule par un sous-agent Codex chargé de l'inventaire et de la revue documentaire de base. Les opérations effectivement réalisées sont : lecture des sources et des suivis existants, analyse statique HTML avec la bibliothèque standard Python, inspection JSON et AST du glossaire, calcul SHA-256, comparaison aux blobs Git et lecture du diff entre les deux commits ci-dessous. Aucune source canonique n'a été modifiée ; aucune correction médicale, consultation primaire nouvelle, compilation ou vérification navigateur n'est annoncée par ce relevé.

**Base initialement inventoriée : `b6e5d18c2c2383893819c4c0834d6402bbe30e67`. Base proposée pour la contrelecture de Claude : `39b7ff0cc585c59ffbb99fb448940daa1950b34d`.** Le second commit a été signalé par le coordinateur comme nouvelle tête d'intégration ; ses objets ont été comparés localement en lecture seule. Les différences sont décrites en fin de document. Le relevé initial n'est pas présenté comme une revue médicale de cette nouvelle tête.

`chapters.json` déclare le cours intégré, titre canonique `Sepsis et choc septique de l’adulte`, et un seul code dans `covers` : `A41`. Cette déclaration de disponibilité n'établit pas la couverture du fragment entier ni sa complétude CIM-11. Le suivi partagé maintient le cours en `pending_exhaustive_review`.

## Sources et répartition réelle des quatre onglets

Les quatre fichiers principaux sont des segments de la source concaténée : **leur nom ne correspond pas à un onglet indépendant**. Il faut attribuer les fichiers réels avant toute écriture, en particulier le segment qui contient deux onglets.

| Onglet affiché | Segment canonique et panneau | Repères et contenu existant |
| --- | --- | --- |
| Pathologie et prise en charge | [`A41_a.html`](../../../../../chapters/A41/A41_a.html), ouverture du panneau `pA`, puis [`A41_b.html`](../../../../../chapters/A41/A41_b.html), sa continuation et sa fermeture | `a41-0` à `a41-12`, soit 13 sections : cas de Mme R., définitions, épidémiologie, mécanismes, foyers et terrains, anamnèse, examen clinique, diagnostic, urgences, traitement, suivi, terrains particuliers et critères formels finaux. |
| Examens | [`A41_c.html`](../../../../../chapters/A41/A41_c.html), panneau `pE` | `a41-e-1` à `a41-e-5` : choix des examens, microbiologie, lactate/gaz/rein/coagulation, imagerie et geste anatomique, puis trois cas sous forme de quiz. |
| Sciences | Le même `A41_c.html`, panneau `pS` | Quatre disciplines `a41-s-anat`, `a41-s-histo`, `a41-s-physio`, `a41-s-immun`, contenant `a41-s-1` à `a41-s-4` : barrières et foyer, endothélium et microcirculation, perfusion/lactate, réponse de l'hôte. |
| Pharmacologie | [`A41_d.html`](../../../../../chapters/A41/A41_d.html), panneau `pP` | `a41-p-1` à `a41-p-4` : choix thérapeutiques, tableau des doses, interactions et surveillance, traitements à éviter et désescalade. |

Le relevé statique identifie **7 SVG avec leurs légendes, 8 blocs de quiz et 18 tableaux HTML** : 15 tableaux dans les quatre segments principaux et trois dans les fenêtres. Aucune image externe `<img>` n'a été identifiée dans ces huit HTML. Ces comptes décrivent les sources ; ils ne prouvent ni l'affichage ni la validité des contenus.

La fin de la Pathologie, `a41-12`, comprend les critères Sepsis-3, les limites de qSOFA et les paramètres décisionnels. L'auteur doit préserver la distinction entre critères de classification, reconnaissance clinique et décision de prise en charge dans tous les supports associés.

## Fenêtres natives et justifications ajoutées à la construction

Les quatre fichiers de fenêtres contiennent **63 définitions natives `data-pop`**, sans clé native dupliquée. Les **63 clés `data-k` distinctes** repérées dans les HTML principaux et les fenêtres disposent chacune d'une définition native ; aucune clé native sans usage n'a été relevée. Il s'agit d'une résolution statique des noms, pas d'un test d'ouverture ou de focus dans le navigateur.

| Source | Définitions natives | Repères pour la relecture |
| --- | ---: | --- |
| [`A41_pop1.html`](../../../../../chapters/A41/A41_pop1.html) | 19 | `a41-perfusion`, `a41-lactate`, `a41-sofa`, `a41-sepsis3`, `a41-ssc`, `a41-swiss-report`, `a41-endo`, `a41-atcd-immune`, `a41-atcd-device`, `a41-atcd-organ`, `a41-sympt-conf`, `a41-sympt-dysp`, `a41-sign-perfusion`, `a41-sign-rr`, `a41-sign-focal`, `a41-qsofa`, `a41-cultures`, `a41-source`, `a41-pkpd`. |
| [`A41_pop2.html`](../../../../../chapters/A41/A41_pop2.html) | 11 | Quatre monographies : `a41-norad`, `a41-vaso`, `a41-hydro`, `a41-piptazo` ; sept Pareto détaillés ci-dessous. |
| [`A41_pop_pa.html`](../../../../../chapters/A41/A41_pop_pa.html) | 32 | Scores et syndrome : `a41-sirs`, `a41-news2`, `a41-bacteriemie`, `a41-postsepsis`, `a41-pam` ; mécanismes et terrains : `a41-cardiomyo`, `a41-civd`, `a41-bmr`, `a41-cortico`, `a41-asplenie`, `a41-allergie`, `a41-directives` ; examen : `a41-frissons`, `a41-fievre`, `a41-oligurie`, `a41-glasgow`, `a41-spo2` ; gravité : `a41-fasciite`, `a41-chocs`, `a41-refractaire`, `a41-sdra`, `a41-ira` ; décisions : `a41-delai-atb`, `a41-remplissage`, `a41-lpj`, `a41-oxygene`, `a41-mesures`, `a41-desescalade`, `a41-sortie`, `a41-vaccins`, `a41-phoenix`, `a41-grossesse`. |
| [`A41_pop_sciences_revision.html`](../../../../../chapters/A41/A41_pop_sciences_revision.html) | 1 | `a41-science-reading` : réévaluer perfusion, pression et lactate sans traiter automatiquement un chiffre. |

La banque [`A41_justifications.json`](../../../../../chapters/A41/A41_justifications.json) comporte **10 entrées et 10 cibles déclarées**. Ces fenêtres sont ajoutées par la construction ; elles sont distinctes des 63 définitions natives. Leur présence ne certifie pas que toutes les affirmations du cours possèdent une justification exhaustive.

| Entrée de banque | Segment et ancrage déclaré | Passage ciblé |
| --- | --- | --- |
| `a41-j-cholestase` | `A41_a.html`, `a41-3` | « Cholestase inflammatoire, hypoperfusion ». |
| `a41-j-selection` | `A41_a.html`, `a41-4` | « Sélection de germes résistants ». |
| `a41-j-glycemie` | `A41_b.html`, `a41-9` | « Le stress et l’hydrocortisone élèvent la glycémie ». |
| `a41-j-muqueuse-gastrique` | `A41_b.html`, `a41-9` | « Le choc réduit la perfusion de la muqueuse gastrique ». |
| `a41-j-rendement-culture` | `A41_c.html`, `a41-e-2` | Rendement des prélèvements selon antibiotique antérieur et volume. |
| `a41-j-gazometrie` | `A41_c.html`, `a41-e-3` | « pression artérielle en oxygène et pH ». |
| `a41-j-glycocalyx` | `A41_c.html`, `a41-s-2` | Jonctions endothéliales et glycocalyx. |
| `a41-j-starling` | `A41_c.html`, `a41-s-2` | Réponse cardiaque à l'augmentation du remplissage. |
| `a41-j-rythme` | `A41_d.html`, `a41-p-3` | « rythme cardiaque ». |
| `a41-j-renal-antibiotique` | `A41_d.html`, `a41-p-3` | « Sous antibiotique, suivre fonction rénale ». |

## Figures, quiz et Pareto à contrôler ensemble

| Support existant | Repère canonique | Contrôle demandé |
| --- | --- | --- |
| Figure 1, réponse normale puis dérèglement systémique | `A41_a.html`, `a41-3` | Chaque flèche, causalité, limites et concordance avec le tableau organe → mécanisme → signe. |
| Figure 2, algorithme Sepsis-3 | `A41_b.html`, `a41-7` | Critères, branches, portée de qSOFA et distinction diagnostic/urgence clinique. |
| Figure 3, chronologie de la prise en charge | `A41_b.html`, `a41-9` | Catégories de probabilité, délai de l'antibiotique, prélèvements et contrôle du foyer, d'après les recommandations effectivement consultées. |
| Quatre figures Sciences | `A41_c.html`, `a41-s-1` à `a41-s-4` | Barrières, endothélium, lactate et réponse immunitaire ; éviter d'attribuer une décision thérapeutique à une simple plausibilité mécanistique. Les légendes brutes portent « Figure — … » sans numéro. |
| Quatre quiz Pathologie | `a41-1`, `a41-6`, `a41-7`, `a41-9` | Sepsis versus choc, perfusion malgré pression à la cible, absence de fièvre, corticothérapie antérieure et dose de stress. |
| Trois quiz Examens | `a41-e-5` | Infection seulement possible sans choc, vasopresseur avec lactate inférieur au seuil de classification, drainage du foyer. |
| Un quiz Sciences | `a41-s-4` | Lactate élevé et décision de bolus supplémentaire. |

Les sept destinations Pareto sont définies dans `A41_pop2.html`. Les sources principales contiennent dix boutons Pareto, car le même Pareto Sciences est appelé depuis plusieurs disciplines. Le relevé ne recalcule pas leurs fractions.

| Destination | Sections désignées par `data-cover` |
| --- | --- |
| `pareto-a41-def` | `a41-0`, `a41-1`, `a41-2`. |
| `pareto-a41-physio` | `a41-3`, `a41-4`. |
| `pareto-a41-diag` | `a41-5`, `a41-6`, `a41-7`, `a41-8`. |
| `pareto-a41-trait` | `a41-9`, `a41-10`, `a41-11`, `a41-12`. |
| `pareto-a41-examens` | `a41-e-1` à `a41-e-5`. |
| `pareto-a41-sciences` | `a41-s-1` à `a41-s-4`. |
| `pareto-a41-pharma` | `a41-p-1` à `a41-p-4`. |

Une contrelecture doit vérifier que les quiz et Pareto ne simplifient pas une recommandation conditionnelle en règle universelle et conservent les mises en garde des passages développés.

## Glossaire et références déjà présents

[`glossary/a41.py`](../../../../../glossary/a41.py) contient **23 appels locaux à `a(...)`**, recensés sans exécuter le module. Les définitions locales comprennent notamment SOFA, SIRS, Sepsis-3, V1a, les essais VASST, ADRENAL, APROCCHSS, SEPSISPAM, MERINO, BLING, CLOVERS, SOAP, BALANCE, ANDROMEDA-SHOCK et ANDROMEDA-SHOCK-2, FiO₂, Solu-Cortef et Ait-Oufella, ainsi que des clés techniques de classification. Le module importe `a` et `G` depuis `cardio_1` ; le relevé des définitions locales ne vérifie pas à lui seul la résolution globale ni les collisions d'abréviations.

Les HTML incorporent **59 URL HTTP(S) distinctes**, et la banque en cite **12 autres**, soit **71 URL distinctes au total**. Ce comptage conserve les URL littérales ; il ne vérifie ni leur disponibilité ni l'équivalence des versions avec/sans `www`.

| Ensemble cité dans les sources | Repères existants et statut de cette mission |
| --- | --- |
| Sepsis-3, Singer et collaborateurs, 2016 | Lien PMC dans la bibliographie Pathologie ; critères et tableau SOFA dans `a41-1`, `a41-7`, `a41-12`, `a41-sofa`. Source repérée, non rouverte ici. |
| Surviving Sepsis Campaign 2026 | Page officielle SCCM, DOI `10.1007/s00134-026-08361-1`, guide rapide PDF ; version générale SCCM également citée dans la banque. Les énoncés, niveaux de certitude et pratiques du panel demandent une vérification distincte. |
| Surviving Sepsis Campaign 2021 | DOI `10.1007/s00134-021-06506-y` ; passages d'hydrocortisone et de vasopressine explicitement attribués à 2021, à confronter aux énoncés de 2026. |
| Épidémiologie et suivi | Swiss Sepsis Report 2025, Rudd, SOAP, Sakr, Prescott/Angus ; références dans la bibliographie Pathologie. Distinguer cohortes, années, définitions et populations. |
| Scores, perfusion et terrains | NEWS2, Glasgow, SOFA-2, critères Phoenix, KDIGO, techniques de recoloration et de lever passif des jambes, recommandations endocriniennes et sepsis maternel ; références déjà nommées dans la bibliographie Pathologie. |
| Monographies suisses et américaines | Swissmedicinfo pour huit informations professionnelles ; références Refdata, liste Swissmedic, DailyMed et registre ClinicalTrials.gov. `a41-p-2` contient doses, unités, présentations, adaptations et réserves de transposition. |
| Essais thérapeutiques | VASST, SEPSISPAM, essai 65, ADRENAL, APROCCHSS, MERINO, BLING III, CLOVERS, BALANCE, ANDROMEDA-SHOCK et ANDROMEDA-SHOCK-2 ; liens bibliographiques et descriptions dans les fenêtres/glossaire. Résumé, registre, source secondaire et texte intégral restent à distinguer. |
| Valeurs usuelles et prévention | CHUV pour le lactate, HUG pour les plaquettes, plan suisse de vaccination 2026 ; références datées dans `a41-e-3` et la bibliographie Pathologie. |
| Mécanismes de la banque | Travaux expérimentaux, données de diagnostic, recommandations d'experts sur l'acidose, informations DailyMed, résistance aux antimicrobiens OMS et recommandations SCCM. Vérifier l'extrapolation du modèle à la décision clinique. |

Le coordinateur signale un **HTTP 403 actuel pour les accès SCCM/OMS**. Cette mission n'a pas retesté ces accès ni lu les textes primaires par une autre voie. Les dates de consultation inscrites dans les sources et anciens audits sont des déclarations historiques, pas des consultations effectuées dans cette mission. Aucune formulation clinique nouvelle n'est justifiée par ces seuls liens.

## Revues ouvertes et demandes précises à Claude

Le [suivi MECHANISMS_PLAN](../../../../../docs/collaboration/MECHANISMS_PLAN.json) conserve `pending_exhaustive_review` pour le cours et chacun des huit HTML. Les dix justifications ciblées ne clôturent pas cette revue.

L'[audit historique](../../../../../audits/A41.md), daté du 26 septembre, contient plusieurs passes et états intermédiaires : ne pas confondre un ancien « PASS provisoire » ou une réserve annoncée levée avec une validation indépendante au nouveau SHA. La [réception du lot linguistique global](../../../../../docs/collaboration/receipts/CLAUDE_GLOBAL_LOT1_2026-10-07.json) indique une relecture partielle et une adaptation du passage sur le lactate ; elle ne certifie pas le cours entier.

| Priorité de revue indépendante | Repères concrets | Question à documenter avec source, version et passage précis |
| --- | --- | --- |
| Critères et scores | `a41-1`, `a41-7`, `a41-12`, `a41-sofa`, `a41-qsofa`, Figure 2 et quiz associés | Les critères et seuils du score d'origine sont-ils exacts, cohérents et correctement distingués de SOFA-2 et du dépistage ? Vérifier aussi l'application chiffrée au cas de Mme R. et les limites d'un lactate isolé. |
| Délais infectieux et contrôle du foyer | `a41-9`, `a41-delai-atb`, `a41-cultures`, `a41-source`, Figure 3, `a41-e-5` et Pareto traitement | Les catégories possible/probable/certain, le choc, les prélèvements, les délais et les niveaux de preuve sont-ils fidèles au texte primaire applicable ? Le passage préhospitalier est-il correctement limité ? |
| Fluides, perfusion et pression | `a41-remplissage`, `a41-lpj`, `a41-sign-perfusion`, `a41-lactate`, `a41-9`, `a41-12`, `a41-s-2`, `a41-s-3` | Vérifier quantité initiale, poids utilisé, réévaluation, réponse dynamique, arrêt pour intolérance, interprétation de CLOVERS et des essais de perfusion, et cible de pression selon l'âge. Les associations ne doivent pas être présentées comme causalité prouvée. |
| Vasopresseurs et concentrations | `a41-p-1`, tableau `a41-p-2`, `a41-norad`, `a41-vaso`, `a41-p-3` et Pareto pharmacologie | Vérifier présentation suisse, conversion des unités, préparation prête/dilution, voie, titration, adaptations, risques et place de chaque agent ; distinguer information professionnelle, recommandation et pratique déclarée du panel. |
| Corticostéroïdes | `a41-cortico`, `a41-hydro`, `a41-9`, `a41-p-1`, `a41-p-2` et quiz de `a41-9` | Séparer dose de stress liée au traitement antérieur, indication dans le choc, seuils et délais attribués à 2021, données de 2026 et réserves de la monographie suisse. Vérifier populations et durées d'ADRENAL/APROCCHSS. |
| Antibiotiques et durée | `a41-piptazo`, `a41-pkpd`, `a41-desescalade`, `a41-p-2`, `a41-e-2` | Vérifier limites de l'exemple posologique, adaptations rénales, perfusion, foyer, résistances, MERINO/BLING III et exclusions de BALANCE ; ne pas transformer l'exemple en protocole universel. |
| Valeurs et mécanismes | `a41-e-3`, `a41-s-1` à `a41-s-4`, banque entière | Vérifier valeurs du laboratoire, prélèvement, gazométrie, transport d'oxygène, production/clairance du lactate, glycocalyx, réponse de l'hôte et limites des modèles expérimentaux. |
| Traitements associés et terrains | `a41-mesures`, `a41-oxygene`, `a41-p-4`, `a41-11`, `a41-grossesse`, `a41-phoenix` | Recontrôler chaque indication ou suggestion négative, la population adulte du cours et les limites des renvois pédiatriques/maternels, sans extrapoler les doses. |
| Références primaires inaccessibles historiquement | `a41-norad`, `a41-vaso`, bibliographie de `a41-p-2`, audit historique « Réserves subsistantes » | VASST et SEPSISPAM : recontrôler les résultats attribués aux sources secondaires nommées lorsque le texte intégral primaire devient accessible. Conserver l'origine secondaire explicite tant que ce contrôle manque. |
| Rédaction, figures et contenus associés | Ensemble du chapitre ; huit quiz ; sept Pareto ; quatre figures Sciences | Vérifier français, définition des sigles, nomenclature, précautions visibles, adéquation des explications aux réponses et cohérence des légendes. L'ancien audit cite un fichier `A41_c2.html` absent de cette base : revoir l'état actuel au lieu de recopier son ancienne demande de renumérotation. |

Les techniques de recoloration capillaire et de lever des jambes sont historiquement attribuées à des méthodes d'essais, faute de norme suisse publiée dans l'ancien audit. Leur technique, leur reproductibilité et leurs limites restent à apprécier. La mention de SOFA-2 ne démontre pas sa validation comme substitut du score utilisé par Sepsis-3.

Claude doit examiner les sources au SHA fixé, vérifier indépendamment les références accessibles et rendre un rapport avec fichiers, ancrages, gravité, source et correction proposée pour chaque anomalie. Les points non vérifiés restent des réserves explicites. Toute correction médicale doit être sourcée et contre-vérifiée sur son nouveau SHA avant injection ; le présent inventaire ne constitue pas cet audit.

## Empreintes initiales et delta de la nouvelle tête d'intégration

Les neuf fichiers sous `chapters/A41` et `glossary/a41.py` lus dans le checkout étaient identiques à leurs blobs du commit initial. Les empreintes ci-dessous sont calculées sur les octets des objets Git correspondants ; **elles ne sont pas interchangeables entre versions**.

| Fichier | SHA-256 initial au commit `b6e5d18…` | SHA-256 à auditer au commit `39b7ff0…` |
| --- | --- | --- |
| `A41_a.html` | `66cc0619488eb4e03a90e4f089856eae7b88a1232735f657cec164da684fef54` | `20bee14603813855228d2cc28159f5ff2768c856c5b1470a60761878a52af008` |
| `A41_b.html` | `f0f5a2c90e03475238dedb7dd83b8e1c3c8a8ddd45f47b036189a34c0308d999` | `e8934903adb6be13d606bb06928342489e97b34d5214899ee8a5da397060d16f` |
| `A41_c.html` | `f506369fedac6bf9b2901481f34c5d3ec17f72660a02f49bf778a62b7ef9d397` | `7b0767d8485e7b17c9d4d963621d722b640812cee6664554a147223105db3180` |
| `A41_d.html` | `508f1452d42ef543ba1fd7519150b98d3c71d2e11ef84cc91907376010aab204` | Identique. |
| `A41_justifications.json` | `c6dd7b6f9653cb6286315d8ba709d4d3e10e5711f2b80b3ee2303c534a5d3704` | Identique. |
| `A41_pop1.html` | `e1f4fcff21096f61e1d4b255c1076f98975b7afb25f855eba257066150802d59` | Identique. |
| `A41_pop2.html` | `107ab25cb44237f62721bb5bfa85bb593f363bfa216c81438626647b067a14bd` | Identique. |
| `A41_pop_pa.html` | `06d04dd469584b9e5d94233c01da7d40524d668c438626d81c95d3c2df3aac35` | Identique. |
| `A41_pop_sciences_revision.html` | `46d45aca44d3adb8ed104f7506221126c6cf4f8a355bdea035eb901b6b97832b` | Identique. |
| `glossary/a41.py` | `6ecaeda10acdab0f2825c1248b33c55859bf724338b473d49f7717a7e1c6fb38` | Identique. |

Le diff ciblé entre `b6e5d18c2c2383893819c4c0834d6402bbe30e67` et `39b7ff0cc585c59ffbb99fb448940daa1950b34d` contient **trois fichiers modifiés, 33 lignes ajoutées et 33 supprimées** selon `git diff --stat` ; les longues lignes HTML ne représentent pas des quantités d'enseignements.

| Segment modifié | Nature des changements examinés |
| --- | --- |
| `A41_a.html`, 76 723 → 76 130 octets | Remplacement d'« îlot » par « section » dans les renvois, suppression d'annonces décrivant la fabrication du cours et reformulations pédagogiques, notamment périmètre clinique/codage, suivi après sortie et lien entre mécanisme et signe. |
| `A41_b.html`, 88 095 → 87 707 octets | Même suppression d'annonces de sections futures, renvois reformulés et libellés du pager harmonisés ; reformulation de l'annonce de surveillance des défaillances. |
| `A41_c.html`, 32 768 → 32 828 octets | Deux annonces Sciences remplacées par des formulations sur les fonctions et l'interprétation des constantes, puis sur les limites d'une valeur isolée. |

Pour chacun des trois segments, les suites d'identifiants `id`, clés `data-k`, définitions `data-pop` éventuelles et URL `href` sont **inchangées** entre les deux objets. Les quatre fichiers de fenêtres, la banque et le glossaire sont identiques. Ce contrôle de conservation des attributs n'est pas une preuve de concordance médicale des reformulations.

**La nouvelle contrelecture demandée à Claude doit porter sur `39b7ff0cc585c59ffbb99fb448940daa1950b34d` exact**, y compris ce delta, avec les empreintes nouvelles. Les réserves initiales, anciens rapports et empreintes de base demeurent conservés. Si une tête ultérieure change à nouveau une source du chapitre, signaler son delta et fixer un nouveau SHA d'audit au lieu de transférer silencieusement un verdict précédent.

Résultat de cette mission : inventaire et repères disponibles, revue médicale exhaustive ouverte. Aucune validation médicale, disponibilité primaire actuelle, réussite technique au nouveau SHA, prise en charge de Claude ou complétude CIM-11 n'est certifiée par ce document.
