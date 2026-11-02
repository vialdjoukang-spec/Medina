# C95 — Leucémie à cellules non précisées : plan de révision

Auteur exclusif : Codex Hématologie. Base approuvée `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`, réservation distante et démarrage joints. Le harness testé et la veille sont actifs avant toute modification médicale. Les cours C85 et C86 sont clos ; leurs fichiers restent en lecture seule.

Le socle comprend 13 472 mots de texte réellement extrait, 43 fenêtres, quatre quiz et quatre sciences. Les six sources HTML ont été lues. Ce socle fixe le minimum de profondeur ; aucun simple changement de nombre d’onglets ne vaut enrichissement.

## Travail ordonné

1. Lire les passages suisses applicables et les recommandations Onkopedia avec participation SSH/SGMO, puis les classifications primaires et études européennes. Conserver les textes complets hors Git ; publier seulement références, empreintes et paraphrases.
2. Consigner les lectures dans `recherche_C95/sources.json`, la matrice obligatoire de vingt rubriques et les lacunes ; faire réussir `betta_verite.py` avant rédaction.
3. Reprendre les quatorze composantes monographiques : ouverture clinique ; définition/classifications ; épidémiologie ; normal/mécanismes ; étiologies ; anamnèse ; examen ; diagnostic/différentiels ; urgences ; traitement ; complications ; suivi/prévention ; situations particulières ; synthèse/examen fédéral.
4. Corriger les erreurs déjà repérées dans toutes les surfaces, résumés et quiz compris : seuil de 20 % non universel ; critères OMS/ICC distincts ; deux populations phénotypiques ne prouvent pas deux clones indépendants ; MPO faible et marqueurs associés ne suffisent pas ; leucostase possible sans hyperleucocytose majeure ; seuils et doses Onkopedia contextualisés ; allogreffe adulte à discuter, non automatique ; MRD et calendrier non transposés sans contexte ; populations et dénominateurs explicites.
5. Compléter les six sciences avec la sémiologie fondamentale et analytique, ses neuf composantes et leur correspondance clinique. Ajouter des figures originales licenciées, inspectées, avec explications françaises et limites. Aucun dessin anatomique généré par IA.
6. Relire quatre informations professionnelles suisses de produits exacts, dates et adaptations comprises ; distinguer indication autorisée, usage hors indication et remboursement. Compléter les autres FI seulement si des affirmations pharmacologiques nouvelles le nécessitent.
7. Construire le chapitre natif et sa prévisualisation isolée, vérifier liens/fenêtres/quiz, six sciences, images, responsive et captures. Le navigateur réel bloque `file://` : documenter cette limite ; ne pas assimiler une interception HTTP de test à une navigation réelle autorisée.
8. Lier les quatre relectures IA aux empreintes finales, vérifier 14/14 et 20/20, contrôle de périmètre sur SHA exact, publication sur branche de revue, vérification distante, puis clôture harness et libération explicite de réservation.

## Prévention des conflits et coûts

Un auteur écrit uniquement dans les chemins C95 réservés. Aucun changement de catalogue commun, aucune PR et aucune mutation de `main`. Chaque opération de réservation passe par `harness/registry_guard.py` avec référence Git unique, sans `FETCH_HEAD` partagé. Réutilisation attribuée des sources déjà collectées, lecture ciblée après empreinte, scripts de reconstruction et vérification réutilisables. Les tokens et coûts non exposés restent `null` ; aucune économie chiffrée n’est déduite des octets évités.

## Rapport et limites

Le suivi vit dans le dashboard à quatre spécialités ; le rapport du 2 novembre 2026 à 08 h 00 Europe/Zurich est figé à partir de 07 h 00 UTC. Une clôture de branche représente une production relue par IA et testée, distincte d’une validation médicale humaine et de l’intégration finale après examen des leçons et images par Vial.
