# G03 — Méningite due à des causes autres et non précisées

[Aperçu autonome](G03-apercu-autonome.html), SHA256 `6886570ceb0d1ec6e92ae31223f89f5f4ef5fea1bd4043e46df233902c9cb272`.

18 lectures ciblées réelles, dont un résumé primaire explicitement borné. Sources suisses : SSI 2017, RMS 2016 et revue chronique RMS 2021, FI exactes 2025/2024 ; compléments OMS 2025 et DGN. Textes complets conservés hors Git, paraphrases seulement. [Lectures](recherche_G03/sources.json).

14 points et 20 rubriques confrontés aux sources ; six sciences, sémiologie en tête avec neuf sections, 35 fenêtres et quatre quiz. Deux originaux humains, pixels inchangés, quatre annotations adjacentes chacun ; six schémas conceptuels non anatomiques sourcés. [Monographie](monograph-14.json), [matrice](matrix-20.json), [figures](figures.json).

**Incident de procédure conservé :** la première projection Betta a été contrôlée après première rédaction et a échoué sur son format. Aucune conformité initiale rétroactive. Après VÉRITÉ OK, reprise clinique réelle des 40 sections et 35 fenêtres, quatre corrections : suivi auditif secondaire, limite de l’essai suppressif, bandes spécifiques du LCR, attribution SSI resserrée. La correction structurelle h3/lien direct des sources a ensuite été contrôlée sur les sept conditions statiques de starter_codex.py ; puis reconstruction, nouveaux tests et nouvelles auto-revues. [Journal et heures](post-gate-clinical-reprise.json), [échec initial](betta-initial-format-check.log).

Contrôles natifs réels à 1440/390 : six sciences, neuf sections, 35 fenêtres, quatre quiz, livre 24 px, Entrée/Espace, deux images décodées, dernières annotations et références accessibles. HTTP local éphémère, toutes autres requêtes bloquées, aucun déploiement public affirmé. [Parcours](browser-autonomous.json), [fenêtres](browser-all-windows.json), [annotations](browser-figure-rows.json), [inspection ciblée](visual-self-review.json).

[Revue médicale](reviews/medical.json), [langue](reviews/language.json), [sémiologie](reviews/semiology.json), [ordinateur](reviews/visual_desktop.json), [mobile](reviews/visual_mobile.json) : toutes `self_review` de Sol. Aucun audit indépendant ni validation médicale humaine. Les dénombrements ne mesurent pas la qualité clinique ; tokens et coût non exposés. [Binding final](source-binding.json).

Limites : incidence suisse non établie ; sources datées et populations conservées ; définitions de recherche non universelles ; traitement causal spécialisé, aucune prescription universelle G03 ; codage GM 2024 sans certification de facturation suisse 2026. Un contrôle fixe peut recouvrir temporairement du texte mobile, accessible au défilement. Autres cours et jauges hérités hors audit médical. [Limites détaillées](documented-limits.json).

Reproduction : `MEDINA_OUT=<dossier unique> python3 build_front.py --fragment S08`, bundle natif du harness, scripts `browser-*.cjs`, `python3 test_v7.py --static G03`, `tests/audit_sciences.py` avec base SHA40, et `tools/betta_verite.py` sur la projection locale. Sources/glossaire partagés hors G03 conservés.

Branche réservée pour revue, aucune PR ni main. Achèvement de projet distinct d’une certification clinique.
