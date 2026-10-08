# Méthode — fragments et jauges du catalogue historique

Instantané **local**, 2026-10-08T10:01:41.144288+00:00, tête Git `72ccab4ea2197f8890d090270d212bb54184e0d0`, branche `codex/decision-i83-20261008`. **32 cours primaires intégrés localement** ; l’intégration I83 — Varices des membres inférieurs (C-01-Cardiologie) est incluse. La disponibilité distante et le déploiement sont en cours de vérification par root, pas certifiés ici. Aucun Git fetch, checkout, source modifiée ou message externe.

## Lecture et unités

`FRAGMENTS.json` conserve les 22 fragments, leurs libellés publics, propriétaire, rang de file et catégories sous leur fragment. Le registre et le plan fixent 11 fragments Claude, 10 Codex et C-01-Cardiologie partagé hors de cette répartition. Les rattachements explicites de `fragments.json` priment sur son rattachement par système du catalogue. La méthode reproduit en lecture seule la sélection de `tools/build_organisation.py` et `build_front.py`, sans exécuter ces scripts. Les SHA256 de toutes les sources sont conservés ; leur stabilité a été contrôlée avant écriture.

Le catalogue est extrait du bloc JSON `medora-data` de `shell/medina_front.html` : **1 636 catégories CIM-10-GM 2024**, toutes à trois caractères. Les blocs organisateurs et les sous-codes sont présents séparément dans le JSON ; ils ne gonflent aucun dénominateur de catégorie. Les sous-codes disponibles ne sont pas un inventaire exhaustif validé. Le relevé historique du 7 octobre n’est pas réutilisé comme instantané actuel.

## Numérateurs et dénominateurs

- **Cours primaires intégrés** : entrées `integrated:true` de `chapters.json`, rattachées par leur code primaire. Les quatre sources principales sont présentes pour les 32 cours. Cela établit la présence locale, pas l’exactitude médicale.
- **Couverture locale** : nombre de catégories du fragment dans l’union des `covers` de ses propres cours primaires, divisé par le nombre total de catégories historiques rattachées au fragment. Total : **82/1 636 (5,01 %)**.
- **Couverture avec renvois déclarés** : même dénominateur, avec les catégories disposant d’un cours intégré déclaré dans un autre fragment. Total : **83/1 636 (5,07 %)**. Une seule différence : M30 — Périartérite noueuse et affections apparentées (R-14-Rhumatologie et orthopédie), renvoyant à M31 — Vascularites systémiques (I-13-Immunologie et allergologie). La catégorie reste dans R-14-Rhumatologie et orthopédie ; son cours cible reste dans I-13-Immunologie et allergologie.
- **Sans dénominateur** : `0/0`, `measurable:false`, pourcentage `null`, pour M-12-Médecine des âges de la vie, D-20-Diagnostic clinique et examens complémentaires et E-22-Éthique médicale, droit et communication. Afficher « inventaire à constituer », jamais 0 % ou 100 % d’achèvement.

Les 83 catégories représentent **32 codes primaires, 50 regroupements locaux et 1 renvoi interfragment**. `covers` est une déclaration à l’échelle d’une catégorie, pas une vérification du passage spécifique ni de toutes ses sous-catégories. Le détail pliable indique `primary_integrated`, `grouped_with_local_course`, `cross_fragment_reference` ou `planned`, avec le cours cible et son propre fragment. Les rubriques de menu pédagogiques sont séparées des catégories CIM dans `pedagogical_menu_groups`.

## Tableau des 22 fragments

| Fragment | Responsable | Rang de file | Cours primaires locaux | Catégories par cours locaux | Catégories avec renvois |
| --- | --- | ---: | ---: | ---: | ---: |
| C-01-Cardiologie | Claude/Codex partagé | — | 21 | 58/77 | 58/77 |
| P-02-Pneumologie | Claude | 1 | 5 | 13/64 | 13/64 |
| I-03-Infectiologie | Codex | 1 | 1 | 1/155 | 1/155 |
| G-04-Gastroentérologie et hépatologie | Claude | 2 | 0 | 0/102 | 0/102 |
| N-05-Neurologie | Codex | 2 | 0 | 0/120 | 0/120 |
| E-06-Endocrinologie et métabolisme | Claude | 3 | 0 | 0/77 | 0/77 |
| N-07-Néphrologie | Codex | 3 | 0 | 0/27 | 0/27 |
| H-08-Hématologie | Claude | 4 | 0 | 0/44 | 0/44 |
| O-09-Oncologie, génétique médicale et soins palliatifs | Codex | 4 | 0 | 0/54 | 0/54 |
| G-10-Gynécologie et sénologie | Claude | 5 | 0 | 0/50 | 0/50 |
| O-11-Obstétrique et néonatologie | Codex | 5 | 0 | 0/134 | 0/134 |
| M-12-Médecine des âges de la vie | Claude | 6 | 0 | 0/0 | 0/0 |
| I-13-Immunologie et allergologie | Codex | 6 | 4 | 8/13 | 8/13 |
| R-14-Rhumatologie et orthopédie | Claude | 7 | 1 | 2/155 | 3/155 |
| U-15-Urologie et andrologie | Codex | 7 | 0 | 0/52 | 0/52 |
| D-16-Dermatologie | Codex | 8 | 0 | 0/89 | 0/89 |
| O-17-Oto-rhino-laryngologie et médecine bucco-dentaire | Claude | 8 | 0 | 0/80 | 0/80 |
| O-18-Ophtalmologie | Claude | 9 | 0 | 0/56 | 0/56 |
| M-19-Médecine d’urgence, traumatologie et toxicologie | Claude | 10 | 0 | 0/152 | 0/152 |
| D-20-Diagnostic clinique et examens complémentaires | Codex | 9 | 0 | 0/0 | 0/0 |
| M-21-Médecine de premier recours et santé publique | Codex | 10 | 0 | 0/135 | 0/135 |
| E-22-Éthique médicale, droit et communication | Claude | 11 | 0 | 0/0 | 0/0 |

## Jauges par IA

| Périmètre attribué | Fragments attribués | Cours primaires présents dans ce périmètre | Couverture locale | Avec renvois |
| --- | ---: | ---: | ---: | ---: |
| Claude | 11/11 | 6 | 15/780 (1,92 %) | 16/780 (2,05 %) |
| Codex | 10/10 | 5 | 9/779 (1,16 %) | 9/779 (1,16 %) |
| Cardiologie partagée, hors file | 1 | 21 | 58/77 (75,32 %) | 58/77 (75,32 %) |

**Ces jauges suivent le périmètre des responsabilités actuelles, pas l’auteur historique des cours ni leur production pendant cette nuit.** Un fragment attribué n’est pas un fragment achevé. La cardiologie conserve son activité et ses réserves distinctes de la file 11/10.

## Tâches majeures et limites de mesure

Le plan enregistré conserve A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie) en étape `review` pour Codex ; `active_chapter` Claude est `null`, donc J45 — Asthme (P-02-Pneumologie) demeure une prochaine entrée proposée, pas un chapitre dont le démarrage est prouvé. L’intervention réelle sur I83 — Varices des membres inférieurs (C-01-Cardiologie) et sa publication sont un contexte opérationnel séparé du plan. Le plan n’est pas une télémétrie en direct. Conserver les états production, audit croisé, intégration locale, publication et déploiement séparés dans le tableau des tâches.

Pour **chacun des 22 fragments**, la couverture CIM-11 est **non établie**, avec numérateur, dénominateur et pourcentage `null`. Les données canoniques examinées n’offrent pas la matrice d’entités attendues nécessaire à une jauge CIM-11. La règle `docs/COMPLETUDE_CIM11.md` demande l’inventaire OMS MMS 2026-01 français versionné (code, identifiant, parent et rattachements), un passage spécifique par entité et sous-entité, les relectures indépendantes et les contrôles d’accès. Des mentions ponctuelles ou une correspondance présumée CIM-10/CIM-11 ne remplacent pas cette matrice.

Le JSON est prêt pour un tableau pliable par fragment puis bloc et catégorie ; toutes les catégories gardent leur libellé complet de fragment. Aucune attribution ou catégorie n’a été déplacée.
