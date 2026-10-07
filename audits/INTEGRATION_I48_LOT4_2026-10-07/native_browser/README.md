# Contrôle navigateur natif — I48 — Fibrillation et flutter auriculaires

**Résultat final : conforme.** 4,245 contrôles, aucune erreur de contrôle, JavaScript ou console. Navigateur Chromium 153.0.8010.0.

- 221 occurrences natives : 206 mots verts et 15 synthèses Pareto.
- 100 fenêtres I48 et le renvoi externe `e-crepitants`.
- 36 renvois entre fenêtres, avec retour au contenu précédent.
- 38 parents contenant des abréviations : clic direct sur la notation, Enter et Espace ouvrent la fenêtre mécanistique ; les abréviations autonomes gardent leur définition.
- 499 activations par pointeur ; 76 par clavier ; aucune activation de contournement.
- Quatre onglets et cinq disciplines scientifiques ; largeur mobile 390 px, texte 17 et 24 px ; fenêtres sans débordement horizontal.
- Fermeture par bouton et Échap ; restitution du focus après l’événement natif `close`.
- Sept captures visuelles.

`results.json` est le rapport final faisant foi. `results_initial_probe.json` et `results_focus_race_probe.json` sont des passages diagnostiques antérieurs : le premier a révélé l’interception des clics par les abréviations imbriquées, tout en comptant à tort les traits d’union conditionnels du moteur comme des différences textuelles ; le second a vérifié la correction produit mais contrôlait le focus avant l’événement `close`. Ces deux défauts de comparaison et de synchronisation du test sont corrigés dans le script final.

Le comparateur retire uniquement U+00AD et normalise les espaces. Il compare les titres et le texte intégral des fenêtres aux templates construits.

Les huit sources I48, le glossaire et le moteur sont inchangés durant le passage final. Le fragment isolé `dist/verified-lot4/fragments/MEDINA_S01_cardiovasculaire.html` porte exactement la même empreinte que le fragment contrôlé.

SHA-256 du fragment : `08279a521cb0fa93de132809a526c02c80852e5d7bcc436d1c3b9e011970341a`.

Script reproductible : `tests/verify_i48_native.cjs`. Le fichier et le dossier de sortie peuvent être définis par `MEDINA_I48_NATIVE_FILE` et `MEDINA_QA_OUT`. Le script utilise la découverte Playwright et Chromium commune du dépôt ; `MEDINA_CHROMIUM_PATH` permet de sélectionner un navigateur installé.
