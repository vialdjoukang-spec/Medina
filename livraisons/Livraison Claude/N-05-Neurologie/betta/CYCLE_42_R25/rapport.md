# Rapport de rédaction — R25 Mouvements involontaires anormaux (N-05-Neurologie)
Cycle Betta 42, leçon 1 — agent C42-A1-NEUR (rédaction, Sonnet 5.5), 15.10.2026.
**Audit différé — revue IA, distincte d'une validation médicale humaine.**

Porte de vérité avant rédaction : `python3 tools/betta_verite.py` a affiché `VÉRITÉ OK · CYCLE_42_R25`.

## Fichiers livrés (chapters/R25/ et glossary/)
| Fichier | Octets | Contenu |
|---|---|---|
| R25_a.html | 38 513 | En-tête, quatre onglets, plan ; îlots r25-0 à r25-6 de la Pathologie |
| R25_b.html | 37 669 | Îlots r25-7 à r25-13 (le dernier : critères formels `alert` puis paramètres `key`), références, fermeture du panneau pA |
| R25_c.html | 36 791 | Examens (r25-e-1 à r25-e-6, 4 quiz) et Sciences (anatomie, physiologie, biochimie, génétique et immunologie, 4 figures SVG) |
| R25_d.html | 12 635 | Pharmacologie (r25-p-1 à r25-p-3, 3 quiz), fermeture du gabarit |
| R25_pop1.html, R25_pop2.html | 19 580 ; 25 987 | 42 fenêtres : 33 explicatives (dont la divergence sur le magnésium et les limites de la leçon) et 9 Pareto |
| glossary/r25.py | — | 30 entrées conditionnelles (codes CIM-10-GM, sigles, protéines et gènes) |

Total : environ 11 700 mots dans les quatre fichiers principaux et 3 900 mots dans les fenêtres ; 7 quiz, 4 figures SVG noir et blanc légendées, 18 tableaux, 9 Pareto (bases, clinique, prise en charge, examens, 4 sciences, pharmacologie).

## Matrice de complétude : onglet et identifiant HTML de chaque rubrique
Les onglets sont pA (Pathologie), pE (Examens), pS (Sciences), pP (Pharmacologie). Les identifiants sont ceux des `section.ilot` ou des clés de fenêtres `data-pop`.

| Rubrique | Statut du dossier | Onglet | Identifiant HTML où elle est traitée |
|---|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | pA | r25-0 ; r25-12 ; fenêtre r25-ssp |
| 2. Définition et périmètre CIM-10-GM | ✔ | pA | r25-1 ; fenêtre r25-codage |
| 3. Classifications et stades | ✔ | pA | r25-1 (sous-parties 1.1 et 1.2) ; fenêtre r25-mds |
| 4. Épidémiologie suisse puis européenne | ✔ (Suisse : lacune L1) | pA | r25-2 ; fenêtre r25-lacunes |
| 5. Normal → pathologique | ✔ | pA, pS | r25-3 ; r25-s-anat-cours, r25-s-physio-cours ; fenêtres r25-physio-tremblement, r25-crampe-meca, r25-etirement, r25-fascic, r25-caspr2, r25-myoclonie |
| 6. Étiologies et facteurs de risque | ✔ | pA | r25-4 ; fenêtres r25-med-tremblement, r25-med-crampes, r25-cerebelleux, r25-choree |
| 7. Anamnèse et symptômes | ✔ (fréquences partielles, L2) | pA | r25-5 ; fenêtres r25-orthostatique, r25-sjsr |
| 8. Examen clinique | ✔ (sensibilité et spécificité : L3) | pA | r25-6 ; fenêtres r25-fonctionnel, r25-mnemo |
| 9. Drapeaux rouges et urgences | ✔ (délais : L4) | pA | r25-8 ; fenêtres r25-sla-fascic, r25-dystonie-tetanie |
| 10. Examens complémentaires | ✔ (valeurs normales : L5) | pE | r25-e-1 à r25-e-6 ; fenêtres r25-bio-crampes, r25-myopathie, r25-goldcoast |
| 11. Diagnostic différentiel | ✔ | pA | r25-7 ; fenêtres r25-tic-stereo, r25-akathisie, r25-sjsr |
| 12. Prise en charge suisse | ✔ (quinine : L6 ; bipéridène : L7 ; remboursement : L8) | pA, pP | r25-9 ; r25-p-1 à r25-p-3 ; fenêtres r25-d-propranolol, r25-d-magnesium, r25-div-magnesium, r25-d-quinine, r25-d-sla, r25-d-biperidene |
| 13. Complications et pronostic | ✔ | pA | r25-8 (complications) ; r25-10 ; fenêtre r25-benin |
| 14. Suivi, prévention, dépistage | ✔ | pA | r25-10 |
| 15. Situations particulières | ✔ (enfant : L9) | pA | r25-11 |
| 16. Spécificités suisses | ✔ (OFSP, conduite, assurance-invalidité, Suva : L10) | pA | r25-12 |
| 17. Critères formels du diagnostic | ✔ | pA | r25-13 (`div.alert`) |
| 18. Paramètres clés chiffrés | ✔ | pA | r25-13 (`div.key`) |
| 19. Sous-codes CIM-10-GM couverts | ✔ | pA | r25-1 ; fenêtre r25-codage (table des cinq sous-codes R25.0, R25.1, R25.2, R25.3, R25.8 et de leur traitement) |
| 20. Points d'examen fédéral | ✔ | pA | r25-12 (pièges et erreurs fréquentes) ; r25-0 ; fenêtre r25-ssp |

Conformément à la règle du projet (plan monographique sans îlot ni tableau consacré au code CIM), la liste des sous-codes se trouve dans une fenêtre liée à un mot vert et non dans un îlot.

## Sources utilisées (sources.json)
S1 à S20, toutes citées dans les paragraphes `src` : classifications (S1, S2), consensus MDS 2018 sur le tremblement (S3), lignes directrices allemande, autrichienne et suisse sur le tremblement (S4) et les crampes (S5), revue suisse Ghika 2018 (S6), revues sur la sclérose latérale amyotrophique et les fasciculations (S7 à S10), informations professionnelles suisses Magnesiocard® et Inderal® (S11, S12), myoclonies (S13), tics (S14), jambes sans repos (S15), hyperexcitabilité auto-immune (S16, S17, S20), PROFILES (S18), recherche AmiKo de la quinine (S19). Aucune donnée extérieure au dossier n'a été introduite ; les mises en relation sont des liens entre faits du dossier.

## Contentieux présenté en mot vert
Magnesiocard® (information suisse, avril 2025) mentionne les crampes du mollet parmi ses indications, alors que la ligne directrice DGN 2023, coapprouvée par la Société suisse de neurologie, juge l'efficacité du magnésium non démontrée. La fenêtre `r25-div-magnesium` applique la règle de la source primaire la plus récente pour l'efficacité et précise que l'autorisation fonde la possibilité de prescrire ; les deux textes sont en vigueur, aucun ancien texte n'est en jeu. Le contentieux est appelé depuis r25-9, r25-p-1 et r25-p-3.

## Lacunes conservées (non comblées)
L1 épidémiologie suisse ; L2 fréquence relative des types de mouvements en soins primaires ; L3 sensibilité et spécificité des signes ; L4 délais chiffrés des drapeaux rouges ; L5 valeurs normales des électrolytes ; L6 statut suisse de la quinine (aucune spécialité trouvée dans AmiKo) ; L7 information suisse du bipéridène non relue ; L8 remboursement par la liste des spécialités ; L9 données pédiatriques ; L10 déclaration OFSP du tétanos, aptitude à la conduite, assurance-invalidité, Suva ; L11 article de la Revue Médicale Suisse sur les tremblements médicamenteux. Les lacunes figurent dans la leçon (r25-2, r25-5, r25-6, r25-8, r25-9, r25-12, r25-13, fenêtre r25-lacunes). Les effets indésirables, interactions et adaptations rénales ou hépatiques de l'Inderal® n'ayant pas été lus, la fenêtre `r25-d-propranolol` le déclare.

## Auto-contrôle du cahier W
- HTML bien formé (équilibre des balises vérifié sur a+b+c+d et sur les fenêtres : aucune erreur).
- Identifiants uniques et préfixés `r25-` ; clés de fenêtres `r25-…` et `pareto-r25-…` ; aucune clé appelée sans fenêtre (0 manquante), aucune fenêtre orpheline (0) ; ids de couverture Pareto tous existants.
- Classes limitées à la liste fermée du contrat (alert, card, chap, chap-body, chap-head, code, fb, ilot, key, lab, n, pager, panel, pareto-btn, quiz, ratio, sci, sci-bar, sci-body, src, status, t, tabs, toc, trap, two, ui, w, k, prev, next) ; quatre onglets pA, pE, pS, pP ; Pareto en fin de chaque grande partie ; dernier îlot de la Pathologie : critères formels (`alert`) puis paramètres clés (`key`).
- Audit des abréviations de `build_medina.audit()` avec le glossaire racine et `r25.py` : résultat `{}`.
- Aucune recommandation américaine utilisée ; aucune formule du type « à vérifier » : les points non vérifiables sont attribués à leur source et déclarés en lacune.
- Non effectué (hors périmètre) : construction du front, injection dans `chapters/`, `chapters.json`, git. Aucun test navigateur (`test_preview.py`) n'a été lancé, car il suppose l'injection préalable.
