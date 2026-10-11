# Rapport d’auteur — E11 — Diabète sucré de type 2 (E-06-Endocrinologie et métabolisme)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant E11. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/E11/E11_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (figure 1 physiopathologique, Pareto clinique).
- `chapters/E11/E11_b.html` — îlots 7 à 13 (Pareto diagnostic et urgences, Pareto complications et traitement, Pareto suivi et critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/E11/E11_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Biologie cellulaire, Physiologie, Biochimie, Physiologie rénale ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/E11/E11_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/E11/E11_pop1.html` — 35 fenêtres cliniques, diagnostiques et d’urgence.
- `chapters/E11/E11_pop2.html` — 17 fenêtres de traitement et situations particulières, 8 monographies, 6 Pareto.
- `glossary/e11.py` — 42 clés nouvelles : SSED, SGED, EASD, ADA/EASD, DPP-4, SGLT1, MASLD, MODY, LADA, GAD, IA2, ZnT8, HGPO, NPH, AMPK, GLUT2, GLUT4, IRS-1, IRS-2, PI3K, AKT, FOXO1, DCCT, UKPDS, ACCORD, DiRECT, FLOW, SOUL, SURPASS, SURPASS-CVOT, ARMSS-T2D, ORIGIN, DEVOTE, QualiCCare, G1, G2, G3a, G3b, G4, G5, Galicia-Garcia, E-06-Endocrinologie et métabolisme. Aucune n’existe dans `glossary/*.py` ni dans les glossaires des dossiers `livraisons/Livraison Claude/*/travail/*/glossary/` au 09.10.2026 (vérification par chargement des modules et par recherche des clés, refaite en fin de rédaction).

## Plan

Pathologie : 0 question clinique (chauffeur-livreur de 58 ans, obèse, albuminurique) ; 1 définition et classification (type 2, type 1/LADA, MODY, secondaire, gestationnel ; sous-groupes) ; 2 épidémiologie suisse (MonAM 2022) et pronostic (rein, cœur, foie) ; 3 physiopathologie (insulinorésistance, glucolipotoxicité, effet incrétine, rémission, mémoire métabolique ; figure) ; 4 facteurs de risque et dépistage (mediX, ESC, ADA/EASD) ; 5 anamnèse (formes typique et trompeuses) ; 6 examen (pieds, signes d’insuffisance cardiaque) ; 7 diagnostic et type (critères SSED 2011/ESC 2023, pièges de l’HbA1c, peptide C, différentiels par gravité) ; 8 urgences métaboliques (`div.alert` : hypoglycémie, état hyperosmolaire, acidocétose sous inhibiteur du SGLT2, acidose lactique) ; 9 complications chroniques, concises avec renvois ; 10 objectifs et traitement (cibles, mode de vie, multifactoriel, algorithme, tableau situation → classe, insuline, chirurgie métabolique) ; 11 suivi et prévention (critères SSED, autosurveillance, règles des jours de maladie) ; 12 situations particulières (sujet âgé, insuffisance rénale, grossesse et contraception, conduite, périopératoire, corticothérapie, cas récapitulatif) ; 13 critères formels et paramètres clés.

Choix de périmètre : le diabète de type 1 (E10), l’obésité (E66) et les dyslipidémies (E78) sont renvoyés à leurs cours ; rétinopathie, néphropathie, neuropathie et pied diabétique restent concis, avec fenêtres. Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Gastaldi et al., recommandations SSED/SGED pour le traitement du diabète de type 2, Swiss Med Wkly 2023;153:40060 (PMID 37011604) | Texte intégral HTML (galée brute smw.ch), lu en entier |
| SSED, page « SGED-Empfehlungen Diabetologie » (recensement des documents en vigueur) | HTML ; aucune mise à jour de l’algorithme du type 2 postérieure à 2023 n’y figure |
| SSED et SGRM, Richtlinien Fahreignung und Fahrfähigkeit bei Diabetes mellitus, édition 1, août 2025 (PDF) | Texte intégral (pdftotext) |
| SSED, Withdrawal of several insulins and alternative options, état août 2025 (fichier 2026) | Texte intégral PDF |
| SSED et Société suisse de néphrologie, Diabetische Nierenkrankheit bei Typ-2-Diabetes, version courte mai 2024 | Texte intégral PDF |
| Paul et al., SSED et groupe insuffisance cardiaque de la SSC, Swiss Med Wkly 2024 (doi 10.57187/s.4000) ; carte de poche 2024 | Carte de poche lue en texte intégral ; article : résumé PubMed et carte |
| SSED, prise de position HbA1c pour le diagnostic, 2011 ; critères de bonne prise en charge 2017 | Texte intégral PDF |
| QualiCCare, guide pratique du pied diabétique, 2023 (diffusé par la SSED) | Texte intégral PDF |
| mediX, guideline Diabetes mellitus, révisée 03/2024, mise à jour 05/2026 | Texte intégral HTML (rendu navigateur) |
| OFSP et Obsan, indicateur MonAM Diabète (âge 15+), mise à jour 17.03.2025 | Texte intégral HTML |
| Davies et al., consensus ADA/EASD « Management of type 2 diabetes, 2026 », Diabetologia, 02.10.2026 (PMID 42825923) | Texte intégral HTML en accès libre (Springer, rendu navigateur) ; sections thérapeutiques, cardio-rénales, âge, poids, MASLD lues |
| Marx et al., ESC 2023 maladies cardiovasculaires et diabète (PMID 37622663) | Texte intégral de la traduction officielle italienne (G Ital Cardiol 2024;25 suppl. 1:e1-e103, PDF) ; original OUP inaccessible (contrôle anti-robot) |
| Umpierrez et al., crises hyperglycémiques, consensus ADA/EASD/JBDS/AACE/DTS, Diabetologia 2024 (PMC11343900) | Texte intégral (BioC PMC) ; critères de l’état hyperosmolaire en figure, non lisibles en texte |
| Mustafa et al., JBDS, état hyperosmolaire, Diabet Med 2023 (PMC10107355) | Texte intégral |
| International Hypoglycaemia Study Group, Diabetologia 2017 (PMC6518070) | Texte intégral |
| Galicia-Garcia et al., Int J Mol Sci 2020 (PMC7503727) | Texte intégral |
| Nauck et Meier 2018 (PMID 29364588) ; Taylor et al., Cell Metab 2018 (PMID 30078554) ; Ahlqvist et al. 2018 (PMID 29503172) | Résumés PubMed |
| UKPDS 33 et 34 (PMID 9742976, 9742977), UKPDS 80 (18784090), UKPDS 91 (38772405), ACCORD (18539917), Steno-2 (18256393), DiRECT (29221645), LEADER (27295427), FLOW (38785209), SOUL (40162642), FIDELIO-DKD (33264825), EMPA-REG OUTCOME (26378978) | Résumés PubMed ; chiffres d’EMPA-REG OUTCOME, SUSTAIN-6, FLOW et DAPA-CKD repris des informations professionnelles suisses |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Glucophage (10.2025), Jardiance (07.2025), Forxiga (08.2026), Ozempic (07.2026), Rybelsus N (08.2026), Trulicity (07.2026), Mounjaro (07.2026), Januvia (04.2024), Trajenta (11.2023), Diamicron MR (02.2025), Tresiba (12.2024), Toujeo (07.2021), Lantus (09.2022), Ryzodeg (11.2020), Kerendia (11.2025), Baqsimi (03.2026) | Texte intégral ; indications, posologie, contre-indications, mises en garde, interactions, grossesse, mécanisme et efficacité clinique lus pour les molécules citées |

Tous les liens du cours (31 URL externes) ont été testés : HTTP 200 (203 pour PubMed via le mandataire, page servie). Les 16 PMID cités ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite : le consensus ADA/EASD est retenu au titre de l’EASD, co-signataire, avec cette nuance explicite ; les essais publiés sont cités comme données. Le sigle « ADA » n’est jamais employé seul, car la clé `ADA` du glossaire désigne l’adénosine désaminase ; la clé composée `ADA/EASD` le neutralise.

## Arbitrages et contentieux présentés dans des fenêtres

1. **Place de la metformine** (`e11-contentieux-algo`) : SSED 2023 (combinaison initiale) contre mediX 05/2026 (monothérapie possible sous 8,5 %) contre ADA/EASD 2026 (classes protectrices de première ligne avec ou sans metformine). Source la plus récente : ADA/EASD 2026 ; texte suisse en vigueur : SSED 2023 ; conduite pratique identique chez le patient à haut risque.
2. **Sulfonylurées** (`e11-su`) : SSED (plus recommandées, mortalité observationnelle) contre ADA/EASD 2026 (pas de surmortalité dans les revues) ; texte suisse retenu.
3. **Dépistage de l’insuffisance cardiaque par NT-proBNP** (`e11-ic-depistage`) : SSED/SSC 2024 (annuel dès 60 ans) contre mediX 2026 (sans bénéfice démontré, non remboursé).
4. **Cibles d’HbA1c et de pression artérielle** (`e11-cibles`, `e11-ta`) : tableaux comparatifs SSED, ESC, ADA/EASD, mediX.
5. **Arrêt de l’inhibiteur du SGLT2 avant chirurgie** (`e11-perop`) : SSED 2 jours contre information professionnelle de l’empagliflozine 3 jours ; l’information professionnelle fait foi.
6. **Seuils du prédiabète** (`e11-prediabete`) et **HGPO** (`e11-hgpo`) : OMS contre American Diabetes Association, ESC contre mediX.
7. **Metformine entre 30 et 59 mL/min/1,73 m²** : la SSED 2023 limite à 1000 mg par jour entre 30 et 45 ; l’information professionnelle suisse limite à 1000 mg par jour entre 30 et 59 ; le cours applique l’information professionnelle.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Version de travail revue par IA.
2. **Recommandation SSED 2023 non actualisée** : le site de la SSED ne présente pas de version plus récente de l’algorithme du type 2 au 09.10.2026 ; les modifications suisses postérieures (remboursement du tirzépatide depuis 02/2026, suppression de la garantie de prise en charge pour l’association inhibiteur du SGLT2 et agoniste du GLP-1 depuis 01/2026) proviennent de mediX et n’ont pas été vérifiées dans la liste des spécialités de l’OFSP.
3. **ESC 2023** lue dans sa traduction officielle italienne, non dans l’original anglais (OUP inaccessible).
4. **Critères numériques de l’état hyperosmolaire** : ceux du consensus 2024 figurent dans une figure non lisible en texte ; le cours retient les critères britanniques JBDS 2023 (glycémie habituellement ≥ 30 mmol/L, osmolalité ≥ 320, cétonémie ≤ 3,0). La mortalité citée (15 à 20 %) est celle des séries britanniques ; le consensus 2024 rapporte une mortalité hospitalière américaine bien plus basse (0,77 % en 2018) ; non exposé dans le cours.
5. **Traitement de l’hypoglycémie chez le patient conscient** : aucune source suisse ou européenne lue ne chiffre la quantité de glucides hors contexte de conduite (la fenêtre mediX « Hypoglykämie » est réservée aux membres) ; le cours écrit « glucides rapides » sans dose, sauf pour la conduite (10 à 20 g, SSED 2025). Le glucose intraveineux n’est pas mentionné faute de source lue.
6. **Tirzépatide** : l’information professionnelle suisse (07.2026) ne mentionne pas d’indication cardiovasculaire ; les données SURPASS-CVOT viennent du consensus ADA/EASD 2026.
7. **Agonistes du GLP-1 et cancer médullaire de la thyroïde** : le consensus ADA/EASD 2026 parle de contre-indication, l’information professionnelle suisse d’absence de données et de prudence ; le cours ne développe pas ce point (lacune assumée, à arbitrer par le relecteur).
8. **Épidémiologie** : enquête par déclaration (MonAM 2022), sans distinction des types ni estimation des diabètes ignorés (lacune nommée dans l’îlot 2).
9. **Résumés seulement** pour plusieurs essais (voir tableau) ; les chiffres repris figurent dans ces résumés ou dans les informations professionnelles.
10. **Volume** : environ 16 400 mots de texte (hors SVG), au-dessus de la cible indicative de 11 000 à 15 000 ; l’excédent est dans les fenêtres (≈ 7 000 mots), conformément à la règle « détail dans les fenêtres ». Le relecteur peut condenser les fenêtres de monographie.
11. **Glossaire** : la clé `E-06-Endocrinologie et métabolisme` est ajoutée ici sur le modèle de `fragments_medina.py` ; si un autre rédacteur du fragment l’ajoute aussi, le relecteur la déplacera dans `fragments_medina.py`. Les clés G1 à G5 sont génériques (catégories KDIGO) et pourront servir aux autres cours.
12. `tests/audit_sciences.py` exigera d’ajouter E11 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/E11` + `glossary/e11.py` + entrée E11 temporaire dans une copie de `chapters.json`)

- `python3 build_medina.py E11` : **`E11 non couvertes: 0`**, six Pareto calculés (7 à 14 % du texte couvert).
- Clés : 66 `data-k` (60 fenêtres et 6 Pareto), toutes avec leur `template data-pop`, toutes préfixées `e11-` ou `pareto-e11-` ; aucun identifiant dupliqué ; aucune fenêtre orpheline ; tous les `data-cover` existent.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : navigation complète ; 4 disciplines de 388 à 435 mots, une figure légendée et accessible chacune, les quatre liens présents.
- `test_preview.py E11` (Chromium 1194 de `/opt/pw-browsers`) : seul échec, l’erreur d’environnement `preview/lesson-core.js` absent de la copie, identique à celle signalée pour J84 et J12. Contrôle Playwright complémentaire : 71 mots verts cliqués dans les quatre onglets et les quatre disciplines, aucune « Fiche absente », 6 Pareto ouverts, un quiz cliqué, **aucune erreur JavaScript propre au cours** ; mobile 390 px : `scrollWidth` = 390 dans les quatre onglets. Rendu des cinq figures vérifié visuellement et corrigé (débordements de texte supprimés). Captures de travail dans le scratchpad, non livrées.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : E11), injection et scellement.
