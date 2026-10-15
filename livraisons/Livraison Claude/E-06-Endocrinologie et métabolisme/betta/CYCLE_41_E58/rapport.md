# Rapport de rédaction — E58 — Carence alimentaire en calcium (E-06-Endocrinologie et métabolisme)

Cycle Betta 41, leçon 2, agent C41-A2-ENDO (Sonnet 5.5). Rédaction du 15.10.2026 à partir de `recherche.md` et `sources.json` (20 sources). Porte de vérité (`tools/betta_verite.py`) : VÉRITÉ OK avant rédaction. Aucune donnée hors dossier.

## Fichiers
| Fichier | Octets |
|---|---|
| chapters/E58/E58_a.html (en-tête, onglet Pathologie, îlots 0 à 6) | 28 633 |
| chapters/E58/E58_b.html (îlots 7 à 14, pager) | 31 888 |
| chapters/E58/E58_c.html (onglet Examens 4 îlots ; onglet Sciences : physiologie, biochimie, histologie osseuse) | 25 260 |
| chapters/E58/E58_d.html (onglet Pharmacologie, 5 îlots) | 11 510 |
| chapters/E58/E58_pop1.html (32 fenêtres) | 28 052 |
| chapters/E58/E58_pop2.html (18 fenêtres : monographies dont Calcium D3 Sandoz, SVGO, PROFILES, 8 Pareto, sources) | 18 931 |
| glossary/e58.py (14 entrées conditionnelles) | 6 141 |

Environ 15 100 mots, 50 fenêtres, 8 boutons Pareto, 4 schémas SVG légendés, quiz de cas fictifs dans l'onglet Examens.

## Matrice de complétude et emplacement dans la leçon
Onglets : pA Pathologie, pE Examens, pS Sciences, pP Pharmacologie. Les identifiants sont ceux des `section.ilot` (ou des fenêtres `data-pop`).

| rubrique | statut | onglet et identifiant HTML | sources |
|---|---|---|---|
| 1. Question clinique, enjeu examen fédéral | ✔ | pA `e58-0` ; objectifs d'examen `e58-13` | S6, S19 |
| 2. Définition, périmètre CIM-10-GM | ✔ partiel (notes d'inclusion/exclusion non lues) | pA `e58-1` ; fenêtre `e58-nosologie` | S1, S2 |
| 3. Classifications et stades | ✔ | pA `e58-1` ; fenêtres `e58-apport-seuils`, `e58-vitd-statut` | S6 |
| 4. Épidémiologie suisse puis européenne | ✔ partiel (pas de prévalence suisse) | pA `e58-3` ; fenêtre `e58-menuch` | S6, S7, S10, S11, S16 |
| 5. Normal → pathologique | ✔ | pA `e58-2`, `e58-4` ; pS `e58-s-physio`, `e58-s-bioc`, `e58-s-histo` | S3, S5, S7, S9, S13, S17 |
| 6. Étiologies, facteurs de risque | ✔ | pA `e58-5` ; fenêtres `e58-phytates-oxalates`, `e58-medicaments`, `e58-vegane` | S6, S7, S9, S13 |
| 7. Anamnèse et symptômes | ✔ (fréquences non chiffrées dans les sources) | pA `e58-6` | S5, S6, S8, S13 |
| 8. Examen clinique | ✔ | pA `e58-7` ; fenêtres `e58-signes-squelette`, `e58-chvostek-trousseau` | S6, S8 |
| 9. Drapeaux rouges et urgences | ✔ | pA `e58-9` ; fenêtres `e58-urgence-bolus`, `e58-hypomagnesemie` ; pP `e58-d-gluconate` | S8 |
| 10. Examens complémentaires | ✔ | pE `e58-e-1` à `e58-e-4` ; fenêtres `e58-radio`, `e58-ca-corrige`, `e58-pal`, `e58-phosphate`, `e58-calciurie` | S6, S7, S8 |
| 11. Diagnostic différentiel | ✔ | pA `e58-8` ; pE `e58-e-3` | S1, S7, S8 |
| 12. Prise en charge suisse (FI datées) | ✔ (calcium IV sans FI suisse) | pA `e58-10` (enfant), `e58-11` (adulte, SVGO, Sandoz) ; pP `e58-p-1` à `e58-p-5` ; fenêtres `e58-d-calcimagon`, `e58-d-sandoz`, `e58-svgo` | S3, S5, S6, S7, S8, S9, S13, S14, S15, S18, S20 |
| 13. Complications et pronostic | ✔ | pA `e58-9`, `e58-12` | S6, S7, S9 |
| 14. Suivi, prévention, dépistage | ✔ | pA `e58-12` | S6, S8, S13, S18 |
| 15. Situations particulières | ✔ | pA `e58-13` ; fenêtre `e58-nourrisson` | S3, S6, S8, S9, S10, S11, S13 |
| 16. Spécificités suisses | ✔ partiel (déclaration, Suva, conduite, assurance-invalidité, liste des spécialités non sourcées, signalé dans le texte) | pA `e58-2`, `e58-11`, `e58-13` | S3, S5, S13, S18, S20 |
| 17. Critères formels du diagnostic (`div.alert`) | ✔ (aucun critère adulte) | pA `e58-14` | S6, S8 |
| 18. Paramètres clés chiffrés (`div.key`) | ✔ | pA `e58-14` ; Pareto `pareto-e58-trait` | S3, S5, S6, S8, S9, S13 |
| 19. Sous-codes CIM-10-GM couverts | ✔ (E58 seul, aucun sous-code) | pA `e58-1` ; fenêtre `e58-nosologie` | S1 |
| 20. Points d'examen fédéral (PROFILES/SSP, pièges) | ✔ | pA `e58-13` (SSP 16, 138, 170 ; six pièges) ; fenêtre `e58-profiles` ; `pareto-e58-ex` | S5, S6, S7, S13, S19 |

## Sources utilisées
S1 OFS CIM-10-GM 2024 ; S3, S4 OSAV 2022 ; S5 SSN/OSAV 2024 ; S6 consensus mondial 2016 ; S7 Thandrayen et Pettifor 2018 ; S8 Society for Endocrinology 2016 ; S9 Rizzoli et Chevalley 2024 ; S10, S11 véganes ; S13 FI Calcimagon-D3 ; S14 FI carbonate de calcium Salmon Pharma ; S15 EAPC 2025 ; S16 menuCH ; S17 EFSA phosphore 2015 ; S18 SVGO 2020 ; S19 PROFILES ; S20 FI Calcium D3 Sandoz (seule la section indication et posologie est lue). S2 (libellé anglais) et S12 non utilisés dans le texte.

## Lacunes explicites (reportées dans le chapitre)
Pas de source SSED ni Swiss Medical Forum ; avis EFSA calcium inaccessible (HTTP 403) ; aucune FI suisse de calcium intraveineux ni pédiatrique (posologie IV issue du texte britannique, adulte) ; pas de prévalence suisse ; pas de seuil ni critère diagnostique adulte ; notes d'inclusion/exclusion CIM non lues ; administration suisse (déclaration, Suva/LAA, conduite, assurance-invalidité, remboursement) non sourcée, signalée sans être affirmée ; intervalles de référence de laboratoire non fournis (le compte rendu du laboratoire prévaut) ; formule du calcium corrigé non fournie ; ACNAP non développé.

## Auto-contrôle du cahier W
Balises équilibrées sur l'ensemble a+b+c+d (les îlots, onglets et le gabarit se ferment d'un fichier à l'autre, comme dans N17/D50) ; identifiants uniques et préfixés `e58-` ; 50 fenêtres, aucune clé `data-k` orpheline ; clés de fenêtres préfixées `e58-` ou `pareto-e58-` ; `build_medina.py E58` (copie de travail hors dépôt) affiche « non couvertes: 0 ». `test_preview.py` n'a pas été exécuté (`lesson-core.js` absent du dépôt, échec identique sur D50).

Audit différé — revue IA, distincte d'une validation médicale humaine.
