# C85 — Lymphomes non hodgkiniens de types autres et non précisés

[Ouvrir la leçon autonome et ses images annotées](C85-apercu-autonome.html).

Cette reprise conserve le cours existant et enrichit les sciences de 999 à 4 338 mots, avec six disciplines, neuf sections de sémiologie et six figures dans les sciences. Le compteur global du dépôt indique 20 667 mots, 49 fenêtres et cinq quiz ; ces volumes ne mesurent pas la qualité médicale.

Deux originaux humains CC BY 4.0 sont intégrés : scanner médiastinal et histologie. Leurs pixels sont inchangés ; les annotations françaises renvoient aux flèches et panneaux d’origine. La figure OpenStax actuelle sous licence NC-SA a été écartée. Les quatre autres figures sont des schémas causaux non anatomiques conservés et relus dans leur contexte.

Les corrections médicales sont détaillées dans [l’auto-relecture](review-package/self-review.json) : codage C85.7, diagnostic intégré, EHA 2025, indications suisses de Keytruda et Polivy, portée des 48 heures de prophylaxie dans MabThera, taux de signalement Yescarta et populations des résultats de survie. Le [registre de recherche](recherche_C85/sources.json) distingue 18 sources actuellement lues des 23 références héritées, conservées avec leur provenance. Les résumés sont identifiés comme tels ; aucune nouvelle posologie n’en est tirée.

Les [14 points monographiques](monograph-14.json) sont cartographiés et les [20 rubriques](recherche_C85/recherche.md) montrent les limites. **Sept réserves restent ouvertes** : classification, décisions de compression/anesthésie, composants cytotoxiques, situations particulières, administration suisse, chiffres hérités restants et objectifs fédéraux. Voir [les actions précises](reserves.json). Le cours est présentable pour revue, sans déclaration d’achèvement.

Le [script de vérification](verify_c85.py) a réellement exécuté six étapes : statique natif, sciences, vérité, construction, incorporation des images et navigateur. Il n’appelle aucun modèle, ne modifie aucune source médicale et ne pousse rien. Sur 1440 et 390 px, les quatre occurrences originales se décodent après défilement ; les six sciences, neuf sections, fenêtres et Livre à 24 px fonctionnent sans erreur JS ni débordement. Les [captures](captures) viennent de cette exécution. Le [reçu final](verification.json) et la [liaison aux sources](source-binding.json) donnent les empreintes exactes. Il s’agit d’une origine HTTP interceptée, sans revendication de déploiement public.

Les auto-relectures sont explicitement attribuées à l’auteur. Aucun score 20/20, audit indépendant complet, certification médicale humaine, PR ou modification de main n’est revendiqué. Les scripts de migration enrich_c85.py, complete_sciences.py, clinical_corrections.py et classification_and_context.py documentent les transformations de cette reprise ; ne pas les rejouer sur des sources ultérieurement modifiées. Pour contrôler le paquet courant, employer verify_c85.py.
