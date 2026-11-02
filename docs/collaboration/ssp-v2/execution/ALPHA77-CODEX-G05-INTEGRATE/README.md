# G05 — paquet de monographie relu

[Aperçu natif autonome](G05-apercu-autonome.html), SHA256 `42d8f942ddaaba5709f87a88720e57cb5448d991785ea6a34ac4b4879b5bf8d0`. Les deux originaux anatomiques humains sont incorporés avec leurs pixels inchangés ; les annotations françaises sont dans leHTML. Navigation des autres cours héritée, non auditée ici.

47lectures ciblées réelles,14points monographiques et20rubriques relus ;6sciences,9sections sémiologiques,45fenêtres et7quiz. Ces nombres ne sont pas une mesure de qualité ni des tokens.

- [Sources](recherche_G05/sources.json) : URL, section, population, limites, paraphrase et empreinte ; documents complets horsGit.
- [14points](monograph-14.json), [20rubriques](matrix-20.json), [revue médicale](reviews/medical.json), [langue](reviews/language.json), [sémiologie](reviews/semiology.json).
- [Figures](figures.json), [inspection visuelle](visual-self-review.json), [navigateur](browser-autonomous.json), [liaison des sources](source-binding.json).

Les contrôles natifs passent sur1440 et390px, avec images après défilement/décodage, six onglets, neuf sections, livre24px, fenêtres, quiz et dernières références ; toutes requêtes externes bloquées. TransportHTTP local éphémère, aucun déploiement distant affirmé.

Toutes les revues sont attribuées à l’auteur en `self_review`, jamais qualifiées d’indépendantes ou humaines. Les limites listées dans le manifeste sont jugées non bloquantes pour le périmètre effectivement enseigné : codage2024, absence d’incidence suisse générale, lectures résumés identifiées, disponibilité étrangère non extrapolée, protocoles rares non prescrits sansFI exacte.

Le dossier `compatibilite_betta_G05` est une projection expliciteR1–R47 versS101–S147 pour le vérificateur historique ; il ne crée aucune lecture supplémentaire.

Reproduction : build natifS08 vers `preview/`, bundler commun, puis `node browser-check.cjs`, `python3 test_v7.py --static G05` et `python3 tools/betta_verite.py <compatibilite_betta_G05>`. Refaire les contrôles et le reçu si les sources changent. AucunePR ni écriture surmain.
