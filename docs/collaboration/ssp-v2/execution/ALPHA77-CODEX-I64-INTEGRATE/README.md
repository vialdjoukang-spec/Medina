# I64 — monographie relue et aperçu natif autonome

[Aperçu autonome](I64-apercu-autonome.html), SHA256 `3bd2f292131c8a1f9a94b5e76c97e37ca61e50d810af7a3e2eeef1b7c3b656a9`.

34 lectures ciblées réelles, 14 points monographiques et 20 rubriques couverts en auto-relecture ; 15 346 mots, 39 fenêtres, 5 quiz, 6 sciences et 9 sections sémiologiques. Ces nombres ne constituent ni certification clinique ni mesure de qualité. Tokens et coût non exposés.

Les deux originaux anatomiques humains sont incorporés, pixels inchangés et quatre annotations françaises adjacentes par figure. Les trois occurrences se décodent après défilement. Les autres cours du fragment natif sont hérités et non audités ici.

- [Sources et limites de lecture](recherche_I64/sources.json) : URL, section, population, paraphrase et empreinte ; textes complets hors Git.
- [14 points](monograph-14.json), [20 rubriques](matrix-20.json), [revue médicale](reviews/medical.json), [langue](reviews/language.json), [sémiologie](reviews/semiology.json).
- [Figures](figures.json), [inspection de dix captures finales](visual-self-review.json), [navigateur](browser-autonomous.json), [liaison des sources](source-binding.json).
- [Contrôles statique et Betta réellement exécutés](checks-executed.json). La projection Betta R1–R34 vers S101–S134 n’ajoute aucune lecture.

Contrôles natifs réussis à 1440 et 390 px : six sous-onglets, neuf sections, images après défilement et décodage, livre 24 px, fenêtres, cinq quiz et dernières références. Toutes requêtes externes bloquées ; transport HTTP local éphémère, aucun déploiement distant affirmé. Pour les quiz, clic sur le fond de la réponse : cliquer une abréviation imbriquée ouvre normalement son glossaire.

Les limites jugées non bloquantes sont détaillées dans le manifeste : codage allemand 2024 sans certification de facturation suisse, épidémiologie suisse 2017 sans incidence I64 actuelle, résumés identifiés, différences FI/protocoles explicites, stratégies de recours sans doses non vérifiées, anatomie normale historique. Le bouton flottant Plan peut masquer temporairement quelques mots sur mobile ; ils deviennent lisibles au défilement. Aucun moteur partagé modifié.

Toutes les revues sont `self_review` de l’auteur ; aucune revue indépendante ni certification humaine. Les correspondances PROFILES 2017/MEBEKO 2026 sont pédagogiques ; PROFILES 2, base de l’examen 2028, est distingué.

Reproduction : build natif S08 dans `preview/`, bundler commun, `node browser-check.cjs`, `python3 test_v7.py --static I64`, puis `python3 tools/betta_verite.py <compatibilite_betta_I64>`. Toute modification des sources impose régénération, contrôles et nouveau reçu. Ni PR ni écriture sur main.
