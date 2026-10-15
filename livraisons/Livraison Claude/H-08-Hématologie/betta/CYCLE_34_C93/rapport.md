# Rapport — C93 Leucémie monocytaire (cycle Betta 34, leçon 2, agent C34-A3-HEM, rédaction Sonnet 5.5)

Date : 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (dossier `livraisons/Livraison Claude/H-08-Hématologie/betta/CYCLE_34_C93/`)
C93_a.html 28 920 o ; C93_b.html 24 888 o ; C93_c.html 26 249 o ; C93_d.html 10 795 o ; C93_pop1.html 17 990 o ; C93_pop2.html 12 818 o (sous chapters/C93/) ; glossary/c93.py 12 282 o ; rapport.md. Environ 12 000 mots, 4 quiz.

## Contenu
- Onglet 1 : 15 îlots (question clinique, nosologie CIM-10-GM 2024, épidémiologie, mécanismes, causes, anamnèse, examen, diagnostic, urgences, LMMC, LAM monocytaire, forme juvénile, suivi, situations particulières, critères formels `div.alert` puis paramètres clés `div.key`), 4 Pareto.
- Onglet 2 : 5 îlots dont 4 quiz de cas cliniques, hiérarchie question-examen-statut, fiches d'interprétation, tableau des configurations.
- Onglet 3 : 4 sciences (hématologie cellulaire, génétique, immunophénotype, biochimie de la signalisation), 4 schémas SVG noir et blanc légendés, corrélations cliniques `div.key`.
- Onglet 4 : 5 îlots (classes, doses, interactions, surveillance, ce qu'il faut éviter).
- Fenêtres : 50 (dont 10 Pareto et 1 aide mnémotechnique). Glossaire : `glossary/c93.py`, entrées conditionnelles.

## Sources utilisées
Treize sources du dossier `sources.json` (BfArM, OFS, Onkopedia LMMC 2023 et LAM 2025, OMS 2022, LeukemiaNet 2022 (résumé), revue LMMJ 2021, étude 2025 sur le phénotype monocytaire, cinq informations professionnelles Swissmedic). Aucune donnée hors dossier.

## Lacunes (reprises du dossier, non comblées)
Seuils M5a/M5b ; épidémiologie suisse et part des M5 ; ponction lombaire de l'adulte ; ESMO 2020 inaccessible, LeukemiaNet 2022 au niveau du résumé ; statut Swissmedic du révuménib et de l'azacitidine pédiatrique ; mécanisme des α-défensines (hypothèse) ; C93.7 et C93.9 sans entité propre ; mécanismes d'action des médicaments et effets indésirables détaillés non décrits dans les sources lues (renvoi aux informations professionnelles).

## Auto-contrôle (cahier W)
- HTML bien formé (analyseur de balises : aucune erreur), identifiants uniques et préfixés `c93-`.
- Toutes les clés `data-k` ont leur `template data-pop` ; aucune fenêtre inutilisée ; clés préfixées `c93-` / `pareto-c93-`.
- Couverture Pareto : tous les îlots cités existent.
- `build_medina.py` (copie de travail hors dépôt, glossaire du dépôt + `c93.py`) : « C93 non couvertes: 0 », aucune erreur Pareto.
- `test_preview.py` non concluant : la coque charge dynamiquement `preview/lesson-core.js`, absent du dépôt (indépendant du chapitre).
