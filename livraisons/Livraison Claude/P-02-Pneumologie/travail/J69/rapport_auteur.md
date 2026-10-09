# Rapport d’auteur — J69 — Pneumopathies d’inhalation et atteintes respiratoires toxiques (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant J68, J69 et J70 (CIM-10-GM 2024). **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/J69/J69_a.html` — en-tête, onglets, Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/J69/J69_b.html` — îlots 7 à 14 (figure 2 algorithme, quiz, Pareto diagnostic, Pareto urgences et traitements, Pareto critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key` ; bloc `div.src` final.
- `chapters/J69/J69_c.html` — Examens (4 îlots, figure 3 débits de pointe sériés, 3 quiz, Pareto) et Sciences (Anatomie, Physiologie, Toxicologie, Histologie et radiobiologie ; figures 4 à 7 `role="img"` légendées ; quatre liens Science → clinique / examen / traitement / À retenir par discipline ; Pareto).
- `chapters/J69/J69_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J69/J69_pop1.html` — 46 fenêtres cliniques, diagnostiques et préventives.
- `chapters/J69/J69_pop2.html` — 13 monographies, 2 fenêtres d’arbitrage (contentieux), 7 Pareto.
- `glossary/j69.py` — 8 clés : RADS, CTCAE, ESMO, ECHM, Arroyo-Hernández, Perez-Lauterbach, Co-Amoxicilline, STOP.
- Fenêtres réutilisées sans modification : `j80-oedeme-lesionnel`, `j80-definition-globale`, `j96-cooxymetrie`, `j84-lba`, `j84-dlco`, `j45-metha`.

## Plan

Pathologie : 0 question clinique (Mme R., 81 ans, pneumonie d’aspiration après AVC, fil rouge) ; 1 définitions et classification par agent (aspiration, inhalation, rayonnements, médicaments ; Mendelson renvoyé à J95) ; 2 épidémiologie (BTS, ESO, Tox Info Suisse 2025, Suva, Conte, informations professionnelles) ; 3 physiopathologie (déglutition-toux, microaspiration, lésion chimique, solubilité des gaz, asphyxiants, médicaments, radiations ; figure) ; 4 causes et facteurs de risque ; 5 anamnèse (cartes typiques/trompeuses) ; 6 examen ; 7 diagnostic (critères BTS, différentiel, co-oxymétrie et lactate, exclusion médicamenteuse, chronologie radique ; figure-algorithme ; quiz) ; 8 urgences (alert) ; 9 traitement de la pneumonie d’aspiration et de la pneumopathie chimique ; 10 inhalation (oxygène, hyperbarie ECHM, hydroxocobalamine, irritants, RADS) ; 11 atteintes médicamenteuses et radiques (grades CTCAE, informations professionnelles) ; 12 suivi et prévention ; 13 situations particulières et cas récapitulatif ; 14 critères formels et paramètres clés. Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| CIM-10-GM 2024, bloc J60–J70 (BfArM, klassifikationen.bfarm.de) | Texte intégral HTML (périmètre ; Mendelson exclu vers J95.4) |
| SSI, Pneumonie acquise en communauté, version 41043 validée le 09.09.2026 (ssi.guidelines.ch/guideline/3007/fr) | Texte intégral via l’API JSON `api/reader/query/guideline` (section « Pneumonie d’aspiration », durée, PCT, imagerie, microbiologie) |
| Simpson et al., BTS Clinical Statement on aspiration pneumonia, Thorax 2023 (PMID 36863772) | Texte intégral PDF du site de la BTS (pdftotext), toutes sections |
| Meisel et al., ESO guideline on stroke-associated pneumonia, Eur Stroke J 2026 (PMID 42095755, PMC13151663) | Texte intégral (Europe PMC XML), PICO 6, 13, 14 et introduction |
| Dziewas et al., ESO-ESSD post-stroke dysphagia 2021 (PMID 34746431) | Résumé |
| Suva, Asthme professionnel et RADS, 3601-37.f, 1re édition septembre 2026 | Texte intégral PDF (français), toutes sections |
| Tox Info Suisse : fiche « Vergiftungen durch Cyanide » (janvier 2026) ; rapport annuel 2025 et annexe ; page 145 | Textes intégraux PDF et HTML |
| Mathieu et al., 10e conférence européenne ECHM, Diving Hyperb Med 2017 (PMID 28357821) | Texte intégral PDF (site EUBS) |
| Vandenplas et al., EAACI position paper irritant-induced asthma 2014 (PMID 24854136) | Résumé |
| Conte et al., ESMO Open 2022 (PMID 35219244, PMC8881716) | Texte intégral |
| Spagnolo et al., ERS 2022 (PMID 35332071) | Résumé (texte ERS inaccessible, HTTP 403) |
| Arroyo-Hernández et al., BMC Pulm Med 2021 (PMID 33407290, PMC7788688) | Texte intégral |
| Voruganti Maddali et al., Delphi radiation pneumonitis 2024 (PMID 38788551) ; Cravereau et al., AFSOS-SFRO 2025 (PMID 40796462) | Résumés seulement |
| Akgün et Nemery, Balkan Med J 2026 (PMID 42787701) | Résumé (texte du site non chargeable) |
| Bai et al., Chest 2024 (PMC11251078) | Texte intégral |
| Dragan 2018 ; Hampson 2018 ; Papin 2023 ; Anseeuw 2013 ; Mintegi 2013 ; Gigengack 2020 ; Zuhra et Szabo 2022 ; Singla 2026 ; Thalhammer 2005 ; Amaza 2020 ; Vaish 2013 ; Perez-Lauterbach 2019 ; Yildiran 2026 | Résumés PubMed |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Co-Amoxi-Mepha i.v. (08.2026), Co-Amoxicilline Spirig cpr (03.2026), Rocephin (06.2025), Dalacin C (07.2026), Flagyl (09.2025), Tavanic (08.2026), Piperacillin/Tazobactam Fresenius (03.2026), Cyanokit (09.2018), Cordarone cpr (04.2024) et i.v. (03.2025), Furadantine retard (07.2025), Metoject (02.2025), Bléomycine Baxter (02.2024), Keytruda (08.2026), Enhertu (06.2026), Prednisone Streuli (06.2026), Solu-Medrol (08.2025) | Texte intégral ; indications, posologie, contre-indications, mises en garde, effets indésirables, mécanisme |

Les 24 PMID cités ont été vérifiés par `esummary` (premier auteur, année, revue concordants). URL externes principales testées : HTTP 200 (BTS, SSI, Suva, Tox Info, EUBS, PMC, doi, swissmedicinfo, pneumotox). Aucune recommandation américaine ne fonde une conduite ; les études nord-américaines (Bai, Dragan, Hampson, Perez-Lauterbach, Amaza, Singla) et indienne (Vaish) sont citées comme données ; l’échelle CTCAE (NCI) seulement comme outil de cotation.

## Arbitrages

1. **Couverture anaérobie et durée** (fenêtre `j69-contentieux-anaerobies`) : SSI 2026 (source suisse la plus récente) retenue — amoxicilline-acide clavulanique, 5 jours ; critères BTS pour ajouter un antianaérobie à la ceftriaxone ; 7–8 jours de l’ESO limités à la pneumonie post-AVC traitée comme nosocomiale.
2. **Corticoïdes des pneumopathies iatrogènes** (fenêtre `j69-contentieux-corticoides`) : l’information professionnelle suisse prime pour pembrolizumab et trastuzumab déruxtécan ; ailleurs, schémas publiés présentés comme hors indication, sans recommandation suisse.
3. **Pneumopathie chimique** : pas d’antibiotique d’emblée, réévaluation à 24–48 h (BTS, ESO 2026), étayé par Dragan 2018.

## Réserves honnêtes

1. **Aucune validation médicale humaine.**
2. **Hors indication suisse** : corticoïdes dans les pneumopathies médicamenteuses (hors molécules dont l’IP le prévoit) et radiques (IP prednisone : alvéolite allergique, sarcoïdose seulement).
3. **Résumés seulement** pour Spagnolo (ERS 2022), EAACI 2014, ESO 2021, Delphi 2024, AFSOS-SFRO 2025, Akgün et Nemery 2026 et plusieurs séries de cas ; seuls les éléments présents dans les résumés sont repris. Le PDF du BTS est la version publiée (Thorax), lue en entier.
4. **Délais de surveillance des gaz peu solubles** (phosgène ≥ 24 h, dioxyde d’azote 3–30 h) : fondés sur des séries de cas non européennes, signalés comme tels ; aucune recommandation suisse ou européenne trouvée.
5. **Lacunes nommées** : incidence suisse de la pneumonie d’aspiration ; durée du traitement de l’abcès pulmonaire ; seuil de la prophylaxie de la pneumocystose sous corticoïdes. Aucun texte Suva spécifique sur la maladie des ensileurs n’a pu être lu (page Suva « locaux exigus » en erreur 503, non citée).
6. **Volume** : environ 19 300 mots (texte, fenêtres et références), au-dessus de la cible indicative de 11 000 à 15 000 ; trois familles nosologiques (J68–J70) dans un seul cours. Le relecteur peut condenser les fenêtres qui reprennent le corps du texte (`j69-radiographie`, `j69-segments`, `j69-ctcae`, `j69-d-coamox`).
7. **Clés de glossaire partagées avec des cours en rédaction parallèle** : `ESMO` (R06) et `STOP` (J67) sont définies de façon compatible dans leurs glossaires ; le relecteur conservera une seule définition à l’injection. `CTCAE` et `RADS` sont nouvelles.
8. **Mobile** : figures lisibles mais petites à 390 px (comportement commun des cours) ; aucun débordement de page (scrollWidth = 390 dans les quatre onglets).
9. `tests/audit_sciences.py` exigera d’ajouter J69 à la liste des nouvelles productions sans base Git.

## Contrôles effectués (copie scratchpad : dépôt + `chapters/J69` + `glossary/j69.py` + entrée J69 temporaire dans une copie de `chapters.json`, `covers` : J68, J69, J70)

- `python3 build_medina.py J69` : **`J69 non couvertes: 0`** ; sept Pareto calculés (5 à 9 % du texte couvert).
- Clés : 79 `data-k` distincts, tous avec `template data-pop` (6 réutilisés d’autres cours) ; toutes les clés nouvelles préfixées `j69-` ou `pareto-j69-` ; aucune fenêtre orpheline, aucun identifiant dupliqué ; classes toutes dans la liste fermée.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : navigation complète ; 4 disciplines de 419 à 500 mots, une figure accessible et légendée chacune, quatre liens présents.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, `executable_path` explicite, car `test_preview.py` attend le build 1243 absent) : 79 mots verts cliqués dans les quatre onglets et les quatre disciplines, **aucune « Fiche absente »**, 7 Pareto ouverts avec fraction calculée ; seule erreur JavaScript : `preview/lesson-core.js` (environnement, identique aux autres cours) ; mobile 390 px sans défilement horizontal. Sept figures contrôlées visuellement en bureau et mobile (deux débordements de texte corrigés).
- Volume : ~19 300 mots, 68 fenêtres (dont 7 Pareto), 4 quiz, 7 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json`, injection et scellement.
