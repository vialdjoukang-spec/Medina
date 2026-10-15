# Rapport de rédaction — E59 — Carence alimentaire en sélénium (E-06-Endocrinologie et métabolisme)

Cycle Betta 42, leçon 1, agent C42-A2-ENDO (Sonnet 5.5). Rédaction du 15.10.2026 à partir de `recherche.md` et `sources.json` (27 sources). Porte de vérité (`python3 tools/betta_verite.py`) : VÉRITÉ OK avant rédaction. Aucune donnée hors dossier ; les calculs arithmétiques du rédacteur (conversions µmol/L ↔ µg/L, 255/70, 25,3 nmol × 79) sont signalés comme tels dans le texte.

## Fichiers
| Fichier | Octets |
|---|---|
| chapters/E59/E59_a.html (en-tête, onglet Pathologie, îlots 0 à 6, figure 1) | 43 168 |
| chapters/E59/E59_b.html (îlots 7 à 16, pager) | 54 901 |
| chapters/E59/E59_c.html (onglet Examens : 4 îlots dont 5 quiz ; onglet Sciences : biochimie, physiologie, histologie) | 32 299 |
| chapters/E59/E59_d.html (onglet Pharmacologie, 5 îlots) | 15 399 |
| chapters/E59/E59_pop1.html (37 fenêtres) | 64 932 |
| chapters/E59/E59_pop2.html (22 fenêtres : examens, monographies, 9 Pareto) | 26 192 |
| glossary/e59.py (15 entrées conditionnelles) | 6 422 |

Environ 14 800 mots dans les quatre onglets et 9 300 mots dans les fenêtres ; 59 fenêtres (dont 9 Pareto), 5 quiz de cas fictifs, 4 schémas SVG légendés (figures 1 à 4), 17 îlots de pathologie (0 à 16), 4 îlots d’examens, 3 îlots de sciences, 5 îlots de pharmacologie.

## Matrice de complétude et emplacement dans la leçon
Onglets : pA Pathologie, pE Examens, pS Sciences, pP Pharmacologie. Les identifiants sont ceux des `section.ilot` (ou des fenêtres `data-pop`).

| rubrique | statut | onglet et identifiant HTML | sources |
|---|---|---|---|
| 1. Question clinique et enjeu pour l’examen fédéral | ✔ | pA `e59-0` ; objectifs d’examen `e59-15` ; fenêtre `e59-cas-publie` | S13, S3, S26 |
| 2. Définition et périmètre CIM-10-GM | ✔ | pA `e59-1` ; fenêtres `e59-nosologie`, `e59-def-deplet` | S1, S3, S4 |
| 3. Classifications et stades | ✔ (gradation biochimique ESPEN ; pas de stades officiels, déclaré) | pA `e59-2` ; fenêtres `e59-gradation`, `e59-mnemo` | S3, S11 |
| 4. Épidémiologie suisse puis européenne | ✔ (incidence suisse codée : lacune) | pA `e59-3`, `e59-4` ; fenêtres `e59-statut-suisse`, `e59-vaud`, `e59-biostat`, `e59-anorexie`, `e59-keshan`, `e59-kashin` | S6, S7, S8, S9, S11, S14, S16, S20 |
| 5. Normal → pathologique | ✔ | pA `e59-5` (figure 1) ; pS `e59-s-bioc`, `e59-s-physio`, `e59-s-histo` ; fenêtres `e59-selenoproteines`, `e59-gpx`, `e59-desiodase`, `e59-selenop`, `e59-absorption`, `e59-cardiomyopathie`, `e59-virus` | S2, S3, S11, S13, S14, S15, S16, S18, S27 |
| 6. Étiologies et facteurs de risque | ✔ | pA `e59-6` ; fenêtres `e59-np`, `e59-bariatrie`, `e59-dialyse`, `e59-brulures`, `e59-vegane`, `e59-anorexie` | S2, S3, S6, S9, S11, S13, S20, S21, S22 |
| 7. Anamnèse et symptômes (fréquences) | ✔ (fréquences : lacune, déclarée) | pA `e59-7` | S6, S11, S13, S14 |
| 8. Examen clinique | ✔ (sensibilité/spécificité : lacune, déclarée) | pA `e59-8` ; fenêtres `e59-leuconychie`, `e59-qtc` | S2, S3, S11, S13 |
| 9. Drapeaux rouges et urgences | ✔ (délais chiffrés : lacune, déclarée) | pA `e59-10` (`div.alert` et tableau) ; fenêtre `e59-cas-publie` | S3, S13, S15 |
| 10. Examens complémentaires | ✔ (pré-analytique : lacune, déclarée) | pE `e59-e-1` à `e59-e-4` ; fenêtres `e59-se-plasma`, `e59-crp-albumine`, `e59-gpx3`, `e59-selenop-dosage`, `e59-matrices`, `e59-reference-suisse`, `e59-bnp`, `e59-biopsie`, `e59-conversion` | S3, S4, S9, S11, S13, S14 |
| 11. Diagnostic différentiel | ✔ | pA `e59-9` (deux tableaux) ; pE `e59-e-3` ; fenêtres `e59-selenose`, `e59-zinc`, `e59-kashin`, `e59-cretinisme` | S1, S2, S3, S11, S13, S16 |
| 12. Prise en charge suisse (FI datées) | ✔ (remboursement LS : lacune ; ESPGHAN 2018 : lacune) | pA `e59-11` ; pP `e59-p-1` à `e59-p-5` ; fenêtres `e59-d-selenase`, `e59-d-nutryelt`, `e59-d-addaven`, `e59-d-peditrace`, `e59-d-vitc`, `e59-d-surdosage`, `e59-d-espen-doses` | S2, S3, S4, S21, S23, S24, S25 |
| 13. Complications et pronostic | ✔ | pA `e59-10` (sous-titre « Complications et pronostic »), `e59-12` (« Pronostic ») ; pS `e59-s-histo` | S3, S11, S13, S14, S15, S16, S22 |
| 14. Suivi, prévention, dépistage | ✔ (dépistage : absence de recommandation, déclarée) | pA `e59-12` ; fenêtre `e59-ul-efsa` | S2, S3, S5, S6, S11, S12 |
| 15. Situations particulières | ✔ | pA `e59-13` ; fenêtres `e59-orbitopathie`, `e59-valeurs-suisses`, `e59-ul-efsa` | S2, S3, S5, S9, S10, S12, S17, S18, S20, S23, S25 |
| 16. Spécificités suisses | ✔ (LS, liste OFSP, Suva/AI, conduite de la maladie : lacunes déclarées) | pA `e59-14` ; pP `e59-p-3` ; fenêtre `e59-d-selenase` | S1, S2, S5, S6, S7, S8 |
| 17. Critères formels du diagnostic (`div.alert`) | ✔ (conjonction opérationnelle, pas de critères consensuels) | pA `e59-16` (`div.alert`) | S1, S3, S4, S13, S22 |
| 18. Paramètres clés chiffrés (`div.key`) | ✔ | pA `e59-16` (`div.key`) ; Pareto `pareto-e59-ex` | S2, S3, S5, S6, S11, S12 |
| 19. Sous-codes CIM-10-GM couverts | ✔ (E59 sans sous-code ; E64.8, M12.1, E00.1, I42.8, E61, E83 traités comme voisins) | pA `e59-1`, `e59-9` ; fenêtre `e59-nosologie` | S1 |
| 20. Points d’examen fédéral | ✔ | pA `e59-15` (SSP 16, 138, 170 ; liens 198 et 142 ; sept pièges) ; pE `e59-e-4` (5 quiz) ; fenêtre `e59-profiles` ; `pareto-e59-ex` | S26, S17, S18, S3, S2, S6 |

## Sources utilisées
S1 OFS ClaML 2024 ; S2 FI selenase® (juin 2023) ; S3 ESPEN 2022 § 11 (texte intégral) ; S4 exposé suisse ESPEN 2022 ; S5 OSAV 2022 ; S6 OSAV 2023 ; S7 et S8 études suisses (résumés) ; S9 étude vaudoise 2026 ; S10 D-A-CH 2015 (résumé) ; S11 revue nordique 2023 ; S12 EFSA 2023 ; S13 cas publié 2026 ; S14 cohorte d’insuffisance cardiaque 2020 ; S15 et S16 revues Keshan et Kashin-Beck (description seulement) ; S17 EUGOGO 2021 via article 2025 ; S18 et S19 revues thyroïde et endocrinologie (résumés) ; S20 anorexie (résumé) ; S21 bariatrie (compte rendu) ; S22 cas 1994 (résumé) ; S23, S24, S25 FI Nutryelt, Addaven, Peditrace® ; S26 PROFILES (correspondance du dépôt) ; S27 virus (résumé). S19 n’apporte aucun fait chiffré (cité en référence du paragraphe de biochimie).

## Lacunes explicites (reportées dans le chapitre)
Pas d’article du Swiss Medical Forum ni de la Revue médicale suisse ; remboursement de selenase® (Liste des spécialités) non vérifié ; ESPGHAN 2018 (nutrition parentérale pédiatrique) non lue, doses pédiatriques issues des FI suisses ; dose de sélénium EUGOGO non relue (aucune posologie proposée pour l’orbitopathie) ; fréquences des symptômes, sensibilité et spécificité des signes, délais d’urgence chiffrés non trouvés ; incidence suisse de E59 codée absente ; recommandations pré-analytiques primaires, liste OFSP des déclarations, aptitude à la conduite liée à la maladie, Suva et assurance-invalidité non lues ; classification officielle en stades inexistante dans les sources lues ; règle de codage d’une carence par perte plutôt que par apport non documentée ; absence de règle ESPEN explicite pour un sélénium entre 0,4 et 0,75 µmol/L avec CRP supérieure à 20 mg/L (déclarée dans l’îlot e59-e-3) ; posologie détaillée d’Addaven non reprise ; valeur « plage normale inférieure à 10,0 µg/dL » du cas publié écartée comme erronée.

## Auto-contrôle du cahier W
Balises équilibrées sur a+b+c+d (le gabarit `template`, l’onglet pA et le panneau pS se ferment d’un fichier à l’autre, comme dans N17, D50 et E58) ; 17+4+3+5 îlots ; identifiants uniques et tous préfixés `e59-` (hors `pA`, `pE`, `pS`, `pP`, `ch-E59`) ; 59 fenêtres, aucune clé `data-k` orpheline et aucune fenêtre non référencée ; clés préfixées `e59-` ou `pareto-e59-` ; classes limitées à la liste fermée ; chaque data-cover de Pareto renvoie à des îlots existants ; `build_medina.py E59` (copie de travail hors dépôt, glossaires complets) affiche « E59 non couvertes: 0 » et aucune erreur Pareto. `test_preview.py` : fenêtres et onglets passent, seule l’erreur de chargement de `lesson-core.js` (absent du dépôt, identique à D50 et E58) subsiste. Aucun fichier n’a été écrit hors du dossier du cycle ; ni `chapters/` racine, ni `glossary/` racine, ni `chapters.json`, ni git n’ont été touchés.

Audit différé — revue IA, distincte d’une validation médicale humaine.
