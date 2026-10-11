# Audits croisés après la mise à jour du Prompt

Ce dossier de reprise conserve les constats antérieurs. Les nouvelles passes portent sur la version du Prompt intégrant `CLARTE_BASES_CALCULS_VIAL_2026-10-11.md`. Ce document organise le travail ; il n'atteste aucun verdict et ne change aucune autorisation.

Le coordinateur déclenche les quatre missions seulement après réception et vérification de cohérence des quatre remises auteur. Le registre donne les sept fichiers et leurs empreintes. Une nouvelle lecture effective des instructions précède la porte d'entrée datée ; aucun succès n'est antidaté.

| Chapitre examiné | Auditeur croisé | Dossier exclusif des nouveaux rapports |
|---|---|---|
| I63 — Infarctus cérébral | C01-R-HEM | CROISE_REPRISE_CLARTE_I63 |
| E11 — Diabète sucré de type 2 | C01-R-NEPH | CROISE_REPRISE_CLARTE_E11 |
| N17 — Insuffisance rénale aiguë | C01-R-ENDO | CROISE_REPRISE_CLARTE_N17 |
| D50 — Anémie par carence en fer | C01-R-NEUR | CROISE_REPRISE_CLARTE_D50 |

Chaque mission comporte deux nouvelles passes distinctes : lecture complète et constat, puis corrections par l'auteur unique et relecture complète des fichiers corrigés. Les passes historiques restent historiques. Le deuxième verdict favorable exige 20/20, sans réserve bloquante ; une note n'est jamais ajustée pour franchir une garde. Si le chapitre est insuffisant, le rapport le dit et la correction continue.

L'auditeur examine les quatre dimensions — rédaction, médecine, sources, frontend — dans les sept sources et le rendu effectivement reconstruit. Il lit les passages primaires, vérifie la couverture des recommandations suisses pertinentes, les exceptions, la population, les limites et la version. Le registre auteur constitue un index de lecture, pas une preuve de l'exactitude de son propre contenu. Chaque passe comporte au moins dix vérifications numériques distinctes documentées ; ce minimum formel ne remplace pas l'examen complet du chapitre.

La relecture couvre la clarté de chaque phrase et fenêtre, les bases anatomiques, physiologiques et biochimiques, les paramètres avec normalité suisse contextualisée, les calculs et conversions cliquables expliqués depuis les bases, les gradations en tableaux, les figures et leurs légendes, quiz et Pareto. Elle distingue valeur normale, seuil diagnostique, cible thérapeutique et classement du risque. Les divergences entre sources sont attribuées et arbitrées, sans consensus inventé. Pour N17, l'instruction ciblée sur le produit B. Braun importé est lue en entrée et en sortie ; l'autorisation documentaire ne résout pas à elle seule une divergence clinique.

Le parcours navigateur couvre tous les onglets, tous les sous-onglets scientifiques, toutes les fenêtres du chapitre et les définitions du glossaire partagé effectivement ouvertes, puis leurs liens récursifs. Les sigles automatiquement enrichis par le moteur doivent être examinés dans le contexte clinique réel. Le rendu ordinateur et mobile vérifie le texte lisible des SVG à l'échelle affichée, le clavier, les liens, quiz, polices, navigation et absence de débordement. La palette du Cycle 1 doit être activée par `production_cycle: 1` dans le catalogue de l'aperçu isolé. Le simple succès de `test_v7` ne suffit pas à ce parcours.

L'auditeur écrit ses rapports et preuves dans son dossier exclusif et son scratch sous `work/`. Il ne modifie pas le chapitre de son partenaire, le registre, les sources canoniques ou Git. Il adresse ses demandes factuelles au coordinateur et à l'auteur ; l'auteur corrige son propre dossier et renouvelle les preuves liées aux empreintes modifiées. Les captures finales sont réservées au contrôle du coordinateur : aucune nouvelle série de captures pendant ces audits.

Les rapports structurés suivent `tools/tetrade_cycle.py` : identité et runtime réels, portes d'entrée/sortie liées aux cinq fichiers du Prompt et à des preuves stables, deux rapports de passes avec dates effectives, quatre observations de dimensions, vérifications numériques primaires, empreintes finales, réserves et verdict honnête. `medical_human_validation` reste `false`.

Les quatre contre-auditeurs ne démarrent qu'après clôture documentée des quatre audits croisés. Ils utilisent des contextes neufs, sans raisonnement privé ni notes des audits précédents. Le contrôle final du coordinateur suit les quatre contre-audits. Les quatre chapitres doivent être prêts avant la première injection ; l'ordre demeure I63, E11, N17, D50, avec publication vérifiée entre deux injections. Le Cycle 2 reste fermé.
