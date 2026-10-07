# Reprise du lot 4 — justification systématique de I48 (cours pilote)

État au 7 octobre 2026. Le workflow a été interrompu par un redémarrage du conteneur.

## Ce qui est fait

| Étape | Résultat | Fichier |
| --- | --- | --- |
| Inventaire des affirmations sans mécanisme | 505 affirmations, dont 98 de priorité haute ; 503 ancres `old` retrouvées exactement | `items_I48_*.json` |
| Plan par fichier | 362 compléments à intégrer au texte, 86 thèmes de fenêtres | `resultats_partiels.json` → `plans` |
| Fusion des thèmes | 53 fenêtres : 12 à créer, 41 existantes à compléter | `resultats_partiels.json` → `fusion` |
| Rédaction des fenêtres | 27 sorties produites, **non vérifiées** : premières rédactions et révisions confondues | `resultats_partiels.json` → `fenetres_redigees_non_verifiees` |

Les sources de base sont les copies corrigées par le lot 2, dans `../../sources/chapters/I48/`. `I48_d.html` n'y figure pas : il reste inchangé dans `chapters/I48/`.

## Ce qui reste

1. Rédiger les fenêtres manquantes, puis vérifier toutes les fenêtres par un vérificateur médical sceptique, avec révision au besoin. Le script complet est `workflow_justification.js` ; ses étapes de rédaction et de vérification peuvent repartir de `fusion`.
2. Vérifier les 362 compléments intégrés au texte : exactitude, sens, phrases complètes, sigles.
3. Appliquer centralement aux copies de `sources/chapters/I48/`. Pour chaque ancre, transformer `label` en `<button class="w" data-k="CLE">label</button>`. Ajouter les nouvelles fenêtres au fichier `_pop` cible et les rubriques complémentaires aux fenêtres existantes. Remplacer `old` par `new` pour les compléments intégrés au texte.
4. Contrôles : `test_v7.py --static I48` (aucune fenêtre manquante, aucun sigle non couvert), build, `audit_fragments`, `audit_sciences`, `verify_sciences_cs.cjs`, `verify_s01_browser.cjs`, puis `check-claude`.
5. Rédiger le rapport et le journal, mettre à jour le manifeste et la passation, puis ouvrir une PR.
6. Montrer au propriétaire quelques fenêtres types d'I48 pour validation, puis étendre la méthode aux 14 autres cours de Claude (`docs/collaboration/MISSION_JUSTIFICATION_2026-10-07.md`).

## Source primaire utile

L'ESC 2024 sur la FA en texte intégral s'obtient en téléchargeant `https://forening.sls.se/media/kfyncecr/2024-esc-guidelines.pdf`, puis en lançant `pdftotext -layout`. On y cherche ensuite les passages voulus avec grep.
