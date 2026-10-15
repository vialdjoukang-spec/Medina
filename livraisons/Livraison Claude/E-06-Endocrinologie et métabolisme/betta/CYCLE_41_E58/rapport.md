# Rapport de rédaction — E58 — Carence alimentaire en calcium (E-06-Endocrinologie et métabolisme)

Cycle Betta 41, leçon 2, agent C41-A2-ENDO (Sonnet 5.5). Rédaction du 15.10.2026 à partir de `recherche.md` et `sources.json` (17 sources, 16 citées). Aucune donnée hors dossier.

## Fichiers (dossier `chapters/E58/` et `glossary/`)
| Fichier | Octets |
|---|---|
| E58_a.html (en-tête, onglet Pathologie, îlots 0 à 6) | 28 633 |
| E58_b.html (îlots 7 à 14, pager) | 28 464 |
| E58_c.html (onglet Examens 4 îlots ; onglet Sciences : physiologie, biochimie, histologie osseuse) | 25 260 |
| E58_d.html (onglet Pharmacologie, 5 îlots) | 11 244 |
| E58_pop1.html (27 fenêtres) | 28 052 |
| E58_pop2.html (20 fenêtres : monographies, 8 Pareto, sources) | 15 568 |
| glossary/e58.py (11 entrées conditionnelles) | — |

Environ 14 700 mots, 47 fenêtres, 6 quiz de cas (3 dans l'onglet Examens), 4 schémas SVG légendés, 8 boutons Pareto.

## Sources utilisées
S1 OFS CIM-10-GM 2024 ; S3 et S4 OSAV 2022 ; S5 SSN/OSAV 2024 ; S6 consensus mondial 2016 ; S7 Thandrayen et Pettifor 2018 ; S8 Society for Endocrinology 2016 ; S9 Rizzoli et Chevalley 2024 ; S10, S11 véganes ; S13 FI Calcimagon-D3 ; S14 FI carbonate de calcium Salmon Pharma ; S15 EAPC 2025 ; S16 menuCH ; S17 EFSA phosphore 2015. S2 (libellé anglais) et S12 non utilisés dans le texte.

## Lacunes explicites (reportées dans le chapitre)
Pas de source SSED ni Swiss Medical Forum ; avis EFSA calcium inaccessible ; aucune FI suisse de calcium intraveineux ni pédiatrique (posologie IV issue du texte britannique, adulte) ; pas de prévalence suisse ; pas de seuil ni critère diagnostique adulte ; notes d'inclusion/exclusion CIM non lues ; intervalles de référence de laboratoire non fournis (le compte rendu du laboratoire prévaut) ; formule du calcium corrigé non fournie ; ACNAP non développé (seule l'EAPC est citée).

## Auto-contrôle du cahier W
HTML bien formé (aucune balise déséquilibrée), identifiants uniques et préfixés `e58-`, toutes les clés `data-k` ont leur fenêtre (47/47, aucune orpheline), clés préfixées `e58-` ou `pareto-e58-`, ids de Pareto existants, `build_medina.audit()` renvoie `{}`, `build_medina.py E58` affiche « non couvertes: 0 » (build sur copie de travail, hors dépôt). `test_preview.py` n'a pas pu aboutir : `lesson-core.js` est absent du dépôt et le même échec se produit sur le chapitre D50 de référence.

Audit différé — revue IA, distincte d'une validation médicale humaine.
