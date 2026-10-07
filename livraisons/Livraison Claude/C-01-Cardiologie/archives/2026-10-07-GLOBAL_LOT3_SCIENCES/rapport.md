# Rapport de relecture MEDINA — audit global, lot 3 : gabarits clonés de l'onglet Sciences

- Responsable : Claude Code, au moyen d'un workflow de 80 agents. Chaque cours passe par une rédaction, une vérification de fidélité médicale, une vérification de style et de non-duplication, puis un arbitrage. Les sorties sont ensuite validées et appliquées centralement.
- Mission : `docs/collaboration/CLAUDE_AUDIT_GLOBAL_2026-10-07.md`, critères 5 et 6 (répétitions, figures introduites par une information spécifique) ; ce lot fait suite au constat transversal du lot 2.
- Branche et commit de départ, SHA complet : `claude/review-medina-global-20261007`, depuis `3636759adb8b74402f98ee8d48c6e8dd49f08a13`.
- Commit relu : `3636759adb8b74402f98ee8d48c6e8dd49f08a13`.
- Date : 7 octobre 2026.
- Cours, 20 en tout :
  - **C-01-Cardiologie**, 16 cours : I00, I10, I21, I25, I30, I33, I34, I35, I40, I42, I44, I46, I47, I49, I50 et Q21.
  - **P-02-Pneumologie**, 4 cours : I26, J18, J44 et J45.
  - I48 a été traité au lot 2.
- Fichiers modifiés : le seul fichier `_c.html` de chaque cours.
- Remise : copies sous `livraisons/Livraison Claude/C-01-Cardiologie/sources/` et `livraisons/Livraison Claude/P-02-Pneumologie/sources/`, manifestes `livraison.json` complétés (empreintes originales et proposées). Le journal détaillé se trouve à côté de ce rapport.
- État : proposition à injecter ; `check-claude` conforme pour les deux fragments.

## Constat

L'enrichissement des Sciences du 7 octobre a produit un même gabarit dans tous les cours :

| Défaut | Occurrences traitées |
| --- | --- |
| Introduction de figure « La figure relie « X » à « Y ». Elle montre les étapes utiles pour comprendre … », parfois agrammaticale | 28 dans les blocs « Interprétation guidée », et 15 introductions génériques ou en métadiscours devant les figures hors bloc |
| Légende générique « Les flèches relient les mécanismes décrits dans le texte » ou « Les branches distinguent deux contributions » | 43 |
| Paragraphe après la figure qui recopie mot pour mot les encadrés « Science → clinique » et « Science → examen », ou qui commence par « Le lecteur… » | 43 examinés : 31 supprimés, 12 réécrits sans répétition |
| « À retenir » identique à une phrase du développement | 88 réécrits en synthèse pratique |
| Phrases défectueuses du bloc : métadiscours « Le lecteur distingue… », constructions fautives, tautologies | 48 corrigées |

Au total, 103 sites dans 20 cours, et 265 éditions.

## Règles appliquées

- Chaque nouvelle introduction de figure nomme les cases du schéma, lues dans le SVG, et leur relation : chaîne causale, branches convergentes, ordre temporel.
- Chaque légende conserve son préfixe « Figure — titre. » et y ajoute une phrase propre à la figure : sens de lecture, relation clé ou limite.
- Chaque « À retenir » dit ce que le clinicien doit retenir, sans recopier le bloc.
- **Aucun fait médical nouveau** n'a été ajouté, qu'il s'agisse d'un chiffre, d'un seuil, d'un médicament, d'un examen ou d'une recommandation. Les erreurs ou imprécisions médicales repérées ont été consignées en réserve, sans être corrigées.

Contrôles mécaniques avant application :
- chaque cible a exactement une édition, avec la bonne enveloppe HTML ;
- le préfixe des légendes est conservé ;
- aucune formule interdite (« Elle montre les étapes », « Le lecteur », « Cette partie », légendes clonées) ;
- aucune phrase recopiée d'un bloc ;
- aucun sigle absent du fichier ;
- aucune phrase répétée d'une unité à l'autre, ce qui interdit de recréer un clone ;
- chaque ancien texte est trouvé une seule fois.

Résultat : **0 anomalie**.

## Exemples

| Cours | Avant | Après |
| --- | --- | --- |
| I50, figure « Relier cavité, valve et congestion » | « La figure relie « Géométrie ventriculaire » à « Symptômes congestifs ». Elle montre les étapes utiles pour comprendre relier cavité, valve et congestion. » | « Les quatre cases forment une chaîne causale : une « Géométrie ventriculaire » modifiée peut altérer la « Coaptation valvulaire » ; la fuite fonctionnelle qui en résulte augmente la charge volumique et contribue à élever les « Pressions de remplissage », qui produisent les « Symptômes congestifs ». » |
| I50, même bloc, « À retenir » | « L'anatomie éclaire la cause ; la physiologie explique les symptômes. » (copie de la dernière phrase) | « Devant une dyspnée, la cavité, la valve et les pressions de remplissage s'évaluent ensemble. Une fraction d'éjection conservée n'écarte pas une congestion. » |
| I00, chorée de Sydenham | « Le lecteur distingue un syndrome clinique progressif d'une étiquette posée sur tout mouvement anormal. » | « La chorée de Sydenham est un syndrome clinique progressif ; elle ne doit pas servir d'étiquette à tout mouvement anormal. » |

## Réserves médicales relevées, non corrigées

Les agents ont relevé 81 réserves distinctes ; le journal les donne toutes. Les principales sont les suivantes.

- **J44**
  - Trois schémas suggèrent une causalité inexacte.
  - Le premier enchaîne « Débit expiratoire limité → Temps expiratoire raccourci » ; or le temps expiratoire raccourcit parce que la fréquence respiratoire augmente à l'effort.
  - Le deuxième enchaîne « Protéases actives → Protection insuffisante » ; il s'agit en réalité d'un déséquilibre entre les deux.
  - Le troisième enchaîne « Distribution à l'imagerie → Mécanisme fonctionnel ».
- **J18**
  - La figure du bloc « Bronches et régions déclives » décrit l'extension pleurale, alors que le texte traite de l'aspiration.
  - Le terme « shunt » est appliqué à une unité « très diminuée » au lieu d'une unité non ventilée.
- **I46**
  - La phrase « Un rythme non choquable exige une autre lecture du protocole, avec recherche des causes réversibles » laisse croire que cette recherche ne concerne pas les rythmes choquables.
  - Le bloc ne cite aucune donnée ERC/SRC.
- **I10** : le bloc rénine-aldostérone réserve la question hormonale à l'hypokaliémie, alors que l'onglet Pathologie rappelle que l'hypokaliémie manque le plus souvent.
- **I26** : plusieurs formulations restent ambiguës : « fibrine, globules rouges et cellules », variant de la prothrombine, objet de « génération ».
- **I34**
  - L'intitulé « pharmacologie de la sérotonine » n'est pas traité.
  - L'exposition d'une valve rhumatismale à l'endocardite n'est pas rappelée.
- **I30, I33, I40, I50** : de nombreux blocs restent très généraux. Aucun germe, gène, médicament ni seuil n'y est nommé. La mission de justification systématique (`MISSION_JUSTIFICATION_2026-10-07.md`) devra combler ces manques par des mécanismes précis et sourcés.

## Contrôles réellement exécutés

Les contrôles ont tourné après copie temporaire des 20 fichiers corrigés, et de ceux du lot 2, dans `chapters/`. Les sources canoniques ont ensuite été restaurées par `git checkout -- chapters`.

| Commande | Résultat |
| --- | --- |
| `python3 test_v7.py --static I00 I10 I21 I25 I26 I30 I33 I34 I35 I40 I42 I44 I46 I47 I49 I50 J18 J44 J45 Q21` | OK ; aucune abréviation non couverte, aucune fenêtre manquante |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi (22 fragments) |
| `python3 tests/audit_fragments.py` | Réussi |
| `python3 tests/audit_sciences.py --out /tmp/medina-science-content.json` | `errors: []` |
| `node tests/verify_sciences_cs.cjs` | 583 contrôles, 0 erreur |
| `node tests/verify_s01_browser.cjs` | 71 contrôles, 0 erreur |
| `python3 tools/livraison.py check-claude …/C-01-Cardiologie` et `…/P-02-Pneumologie` | Conformes : 23 et 4 fichiers |

## Limites

Ce lot ne relit que les unités listées ; il ne vaut pas relecture intégrale des 20 cours. Les textes ont été produits par des agents puis vérifiés par d'autres agents et par les contrôles mécaniques ci-dessus ; un échantillon a été relu par Claude Code. Aucun statut `DONE_*` n'est modifié, et aucune complétude CIM-11 n'est revendiquée.
