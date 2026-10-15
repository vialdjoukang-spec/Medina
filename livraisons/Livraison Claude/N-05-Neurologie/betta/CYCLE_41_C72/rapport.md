# Rapport de rédaction — C72 Tumeur maligne de la moelle épinière, des nerfs crâniens et d'autres parties du système nerveux central (cycle Betta 41, leçon 2)

Agent C41-A4-NEUR (Sonnet 5.5), 15.10.2026. Fragment N-05-Neurologie. Porte de vérité franchie avant rédaction (`python3 tools/betta_verite.py` : VÉRITÉ OK). Le texte n'utilise que `recherche.md` et `sources.json` (S1 à S25). Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (`chapters/C72/` et `glossary/`)
| Fichier | Contenu | Taille (octets) |
|---|---|---|
| `C72_a.html` | en-tête, onglets, plan, îlots 0 à 6 (question clinique à examen clinique) | 21 184 |
| `C72_b.html` | îlots 7 à 13 (îlot 12 Spécificités suisses et points d'examen fédéral ; îlot 13 critères formels `div.alert` puis paramètres clés `div.key`), section `src` | 36 235 |
| `C72_c.html` | onglet Examens (pE, 5 îlots, 4 quiz) et onglet Sciences (pS : anatomie, neuropathologie, génétique, radiobiologie ; 3 schémas SVG) | 19 925 |
| `C72_d.html` | onglet Pharmacologie (pP, 4 îlots) | 9 172 |
| `C72_pop1.html` | 24 fenêtres cliniques et 4 Pareto | 29 701 |
| `C72_pop2.html` | 32 fenêtres (examens, prise en charge, suivi, monographies Temodal®, dexaméthasone, Koselugo®, spécificités suisses) et 12 Pareto | 36 484 |
| `glossary/c72.py` | environ 50 entrées (sigles, gènes, codes CIM), ajouts conditionnels | 13 522 |

Volume : environ 15 500 mots, 72 fenêtres, 6 quiz, 16 boutons Pareto, 5 schémas SVG noir et blanc.

## Matrice de complétude, avec onglet et identifiant HTML
Onglets : pA = Pathologie, pE = Examens, pS = Sciences, pP = Pharmacologie. Les identifiants sont ceux des `section.ilot`.

| Rubrique | Statut | Onglet · identifiant HTML | Sources |
|---|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | pA · c72-0 (vignette) ; objectifs PROFILES : pA · c72-12 | S6, S7, S10, S23 |
| 2. Définition et périmètre CIM-10-GM | ✔ ; note 5 du BfArM non lue (**LACUNE**) | pA · c72-1, c72-12 (fenêtre c72-codes) | S1 |
| 3. Classifications et stades | ✔ OMS 2021, groupes de méthylation ; stades au sens des grades par type | pA · c72-1 ; pS · c72-s-histo-cours | S2, S3, S4, S6, S7, S11 |
| 4. Épidémiologie suisse puis européenne | ✔ ; **LACUNE** incidence suisse propre à C72 | pA · c72-2 (fenêtre c72-epidemio-suisse) | S15, S16, S6, S7, S9, S10, S11 |
| 5. Normal → pathologique | ✔ | pA · c72-3 ; pS · c72-s-anat-cours, c72-s-histo-cours, c72-s-gen-cours, c72-s-radio-cours | S3, S4, S6, S7, S11, S14 |
| 6. Étiologies et facteurs de risque | ✔ contextes génétiques ; aucun facteur environnemental dans les sources | pA · c72-4 | S2, S4, S6, S12, S13 |
| 7. Anamnèse et symptômes | ✔ ; **LACUNE** fréquences chiffrées des symptômes | pA · c72-5 | S4, S6, S7, S12, S14, S20 |
| 8. Examen clinique | ✔ ; **LACUNE** sensibilité et spécificité des signes | pA · c72-6 | S7, S12, S14 |
| 9. Drapeaux rouges et urgences | ✔ ; **LACUNE** délai horaire d'imagerie | pA · c72-8 (`div.alert`) | S4, S12, S14, S18, S20, S21 |
| 10. Examens complémentaires | ✔ ; aucune valeur normale chiffrée pour l'IRM (dit dans le cours) | pE · c72-e-1 à c72-e-5 ; pA · c72-7 | S3, S4, S6, S7, S12, S14 |
| 11. Diagnostic différentiel | ✔ | pA · c72-7 (tableau 7.3) ; pE · c72-e-2 | S6, S7, S10, S11, S14 |
| 12. Prise en charge suisse | ✔ européenne ; **LACUNE** recommandation suisse dédiée ; FI datées (Temodal® décembre 2021, dexaméthasone juin 2022, Koselugo® juin 2026) | pA · c72-9 ; pP · c72-p-1 à c72-p-4 | S3, S4, S5, S6, S7, S8, S17, S18, S19, S20 |
| 13. Complications et pronostic | ✔ | pA · c72-8, c72-10 (tableau pronostique) | S3, S6, S7, S8, S9, S11, S16 |
| 14. Suivi, prévention, dépistage | ✔ ; aucun dépistage de population | pA · c72-10 | S3, S4, S6, S7, S12 |
| 15. Situations particulières | ✔ ; **LACUNE** insuffisance rénale ou hépatique (contre-indications du témozolomide seules) | pA · c72-11 ; pP · c72-p-3 | S7, S8, S17 |
| 16. Spécificités suisses | ✔ déclaration au registre, médicaments, réadaptation ; **LACUNE** aptitude à la conduite, AI, Suva/LAA, remboursement LS | pA · c72-12 (fenêtres c72-nkrs, c72-onc201, c72-synthese-suisse) | S22, S17, S25, S24, S20, S21 |
| 17. Critères formels du diagnostic | ✔ | pA · c72-13 (`div.alert`) | S2, S4, S14 |
| 18. Paramètres clés chiffrés | ✔ | pA · c72-13 (`div.key`) | S3, S4, S6, S7, S8, S9, S11, S12, S15 |
| 19. Sous-codes CIM-10-GM (C72.0 à C72.5, C72.8, C72.9) | ✔ ; nerfs crâniens : couverture partielle | pA · c72-12 (tableau 12.1) | S1 |
| 20. Points d'examen fédéral | ✔ SSP 159 et 227 (rattachement non officiel), SSP voisines (inférence) et neuf pièges | pA · c72-12 (12.3, quiz) | S23, S1, S2, S3, S4, S6, S7, S12, S14, S17 |

## Lacunes reprises dans le cours
- Aucune recommandation suisse de prise en charge ; les trois textes de la Praxis (S20, S21, S24) ne sont lus qu'en résumé et servent de repères, non de fondement de conduite (fenêtres c72-synthese-suisse, c72-lacunes).
- Nerfs crâniens : gliome malin du nerf optique de l'adulte, esthésioneuroblastome (C72.2 ou C30.0 non vérifié), MPNST des nerfs crâniens et tumeur maligne du nerf VIII non documentés ; ces sous-codes ne sont couverts que par la classification et la neurofibromatose de type 1.
- Incidence suisse propre à C72, délai d'imagerie en urgence, dose de corticoïde pour l'œdème médullaire, fréquences des symptômes, sensibilité et spécificité des signes : non sourcés.
- Aptitude à la conduite, assurance-invalidité, Suva et loi sur l'assurance-accidents, remboursement (Liste des spécialités) : aucune règle formulée.
- Dordaviprone (ONC201) : aucune information professionnelle trouvée dans la base AIPS au 15.10.2026 (statut à vérifier sur swissmedic.ch). Interactions du témozolomide, de la dexaméthasone et du sélumétinib : non lues, signalées dans le cours.
- Code CIM-O exact de chaque entité (déclaration au registre) non vérifié.
- Textes longs lus sur les 100 000 premiers caractères (S2, S3, S4, S12) ; S8 et S9 citent des données américaines non retenues comme fondement.
- Contentieux présenté dans une fenêtre liée à un mot vert (c72-contentieux-rt) : radiothérapie d'un épendymome de grade 2 après exérèse incomplète, EANO 2018 (II, B) contre revue de 2024 ; les deux textes sont exposés avec le choix retenu.

## Sources utilisées
Uniquement `recherche.md` et `sources.json` (S1 à S25), dont les compléments suisses S20 à S25.

## Auto-contrôle
- Abréviations non couvertes : 0 (`build_medina.audit` avec `glossary/c72.py` ajouté, copie hors dépôt).
- `build_medina.py C72` : aucune erreur Pareto, C72 non couvertes : 0. HTML bien formé sur a+b+c+d et sur les deux fichiers de fenêtres.
- Les 72 clés `data-k` ont chacune leur `template data-pop`, aucune fenêtre orpheline ; identifiants uniques, préfixés `c72` ; couvertures Pareto valides ; ancres du plan valides.
- `test_preview.py C72` : cours affiché, fenêtres, quatre onglets et mode livre sans anomalie ; la seule erreur signalée est l'absence du module `preview/lesson-core.js` dans cet environnement, identique pour N17.
- Aucune modification de `chapters/` racine, `glossary/` racine, `chapters.json` ni git.

Audit différé — revue IA, distincte d'une validation médicale humaine.
