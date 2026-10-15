# Rapport de rédaction : E35, Anomalies endocriniennes au cours de maladies classées ailleurs

Cycle Betta 36, leçon 1 (c36-E35), fragment E-06-Endocrinologie et métabolisme. Agent de rédaction C36-A2-ENDO (Sonnet 5.5), 15.10.2026.
**Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (sous `chapters/E35/`, `glossary/`)
| Fichier | Octets | Mots |
|---|---|---|
| E35_a.html (onglet 1, îlots 0 à 6) | 30 620 | 3 177 |
| E35_b.html (onglet 1, îlots 7 à 13, critères formels, paramètres clés, références) | 29 768 | 3 338 |
| E35_c.html (Examens e-1 à e-4 ; Sciences : anatomie, histologie, physiologie, microbiologie) | 24 145 | 2 161 |
| E35_d.html (Pharmacologie p-1 à p-4) | 10 063 | 1 050 |
| E35_pop1.html (24 fenêtres) | 24 749 | 2 153 |
| E35_pop2.html (7 monographies et fenêtres thérapeutiques, 13 Pareto) | 14 277 | 1 386 |
| glossary/e35.py | 3 839 | |

Total : environ 13 250 mots, 44 fenêtres, 13 boutons Pareto, 5 quiz de cas, 2 schémas SVG noir et blanc légendés.

## Sources utilisées
Les 26 sources du dossier (`sources.json`), rattachées dans le texte par leur nom court (OFS, BfArM, Flück 2023, ESE 2024, OFSP 2025, guide suisse de la tuberculose, informations professionnelles Solu-Cortef®, Rocephin®, Rimactan®, Florinef®, revues et cas cliniques). Les sources américaines ne servent qu'à des données descriptives (S8, S10, S14).

## Lacunes conservées (aucune donnée inventée)
L1 délimitation E35/E27/E03 présentée comme raisonnement ; L2 aucune donnée suisse sur la tuberculose surrénalienne ou thyroïdienne ; L3 codes dague des infections surrénaliennes non tuberculeuses ; L4 E35.8* sans entité ; L5 guide ESCMID 2016 inaccessible, durée adulte de la ceftriaxone et prise en charge du sepsis méningococcique non fournies ; L6 aucune dose d'ajustement de l'hydrocortisone sous rifampicine ; L7 aucune dose adulte d'hydrocortisone orale ; L8 aucune source suisse sur le syndrome de Waterhouse-Friderichsen ; L9 tuberculose thyroïdienne documentée par cas cliniques ; L10 texte intégral de Husebye 2021 non lu. Les doses antituberculeuses chiffrées, les seuils chiffrés d'hypotension orthostatique et les effets indésirables détaillés des médicaments ne figurent pas au dossier et ne sont pas donnés. Le guide ESE/ES 2024 concerne surtout l'insuffisance induite par les glucocorticoïdes : son application à la crise infectieuse est signalée comme raisonnement.

## Auto-contrôle (cahier W)
- Construction `build_medina.py` en racine temporaire (hors dépôt) : `E35 non couvertes: 0`, aucune erreur Pareto.
- Aperçu navigateur (copie de `test_preview.py`) : OK ; l'erreur d'import dynamique `lesson-core.js` de la coque est préexistante, identique pour N17.
- 54 balises `div` ouvertes et fermées, 26 `section` équilibrées, aucun identifiant dupliqué, tous préfixés `e35`.
- Toute clé `data-k` possède son `template data-pop` ; aucune fenêtre inutilisée ; aucune clé nouvelle sans préfixe `e35-` ou `pareto-e35-`.
- Glossaire : MSH, BfArM, TI-RADS, éponyme Waterhouse-Friderichsen, codes A18.7, A18.8, A39.1, E35.0, E35.1, E35.8 (entrées conditionnelles, aucune clé existante écrasée).
- Aucun fichier modifié hors du dossier de la leçon (ni `chapters/`, ni `glossary/` racine, ni `chapters.json`, ni git).
