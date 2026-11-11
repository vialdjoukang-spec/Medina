# Audit médical ALPHA77 — G80 Infirmité motrice cérébrale (paralysie cérébrale), fragment S08 Neurologie

Mission ALPHA1-CLAUDE-G80-MED · branche `claude/alpha1/g80-med-g1` · base `103745ba` (sources figées du manifeste, snapshot `523832d9`) · 16 octobre 2026
Exécutant : sous-agent Claude Code (voir accusé issue 107) · modèle et effort conformes au manifeste.

> Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## 1. Synthèse

La leçon G80 est honnête sur ses limites et exacte sur la grande majorité de ses chiffres : 432 des 470 valeurs recalculées ou comparées sont exactes, 21 sont des arrondis corrects. Elle comporte pourtant quatre erreurs chiffrées qui touchent des décisions, et elle manque la sémiologie exigée par Vial.

Les erreurs les plus graves sont les suivantes :

1. **Sulfate de magnésium (C04).** La leçon enseigne une indication « avant 34 SA ». Ce seuil est le critère d’inclusion des essais Cochrane. La recommandation suisse de la SSGO (avis d’experts n° 66, 16.12.2019) limite l’indication à **24+0–32+0 SA**, en bolus unique de 4 g sur 15 minutes.
2. **Baclofène oral (C05, C06, C08).** Le Liorésal® est présenté comme « autorisé dès 12 mois ». La FI suisse ne l’indique que dans la sclérose en plaques et la spasticité médullaire : dans la PC, il est employé hors indication. La leçon omet aussi l’abaissement du seuil convulsif, chez des enfants épileptiques dans 15 à 60 % des cas, et la toxicité rénale dès plus de 5 mg/j. Elle annonce enfin des « interactions dangereuses » sans en citer aucune.
3. **DAYC (C03).** Un **indice C de 83 %** est présenté six fois comme une **sensibilité**.
4. **Baclofène intrathécal (C09).** Le palier d’escalade de 5–20 % est donné sans distinction. La FI limite la titration d’origine cérébrale à **5–15 %** et réserve 5–20 % à l’entretien.

Le sous-onglet de sémiologie fondamentale et analytique est absent (C01). Il est proposé en entier, avec les seuils HINE, les signes d’alerte à 9 mois, les spécificités chiffrées et trois cas corrigés. La Figure 2 de la hanche est un dessin anatomique d’origine IA démontrée (C07).

## 2. Tableau de bord

| Indicateur | Valeur |
|---|---|
| Empreintes SHA-256 des 7 fichiers | conformes au manifeste |
| Constats | **0 BLOQUANT · 9 MAJEUR · 11 MINEUR · 5 ENRICHISSEMENT** |
| Valeurs relevées par script | 666 (`calculs/inventaire.json`) |
| Calculables / recalculées | 471 / 470 |
| Correctes / arrondis / fausses | 432 / 21 / **17** (4 erreurs distinctes) |
| Non vérifiables | 1 (37 SA, glossaire, C21) — audit des calculs **non clos** sur ce point |
| `test_v7.py --static G80` | OK (11 076 mots, 47 fenêtres, 6 quiz, 14 Pareto) |
| `tests/audit_sciences.py` | **échec**, 14 erreurs (C02) |
| Figures | 5 (1 ANATOMIQUE_IA, 4 non anatomiques), textes rendus de 7,3 à 8,9 px à 390 px |
| Propositions | 10 fichiers ; 45 blocs « ancien » vérifiés uniques par script |
| Sources lues | 26 (8 en texte intégral, 3 par section, 15 résumés) |

## 3. Constats MAJEURS

| Id | Fichier, ancre | Constat | Preuve | Proposition |
|---|---|---|---|---|
| C01 | `_c`, `data-s="g80-s-anat"` | Le sous-onglet de sémiologie est absent. La leçon compte 4 disciplines et aucune `g80-s-semio`. Les signes d’alerte, la technique des gestes, les seuils et le regroupement syndromique manquent. | S5 tableaux 1–2 | `G80_c_semio.html`, `G80_pop3_semio.html` |
| C02 | `_c`, `g80-s-physio` | `audit_sciences` échoue : physiologie 223 mots, génétique 188, biochimie 219 ; les libellés « Science → … » manquent. | test | Compléter les disciplines |
| C03 | `_b`, `DAYC (indice C) 83 %` | Un indice C est présenté comme une sensibilité (6 occurrences). | S5 résumé | `G80_c_1.html` |
| C04 | `_b`, g80-10 | Le sulfate de magnésium est indiqué « avant 34 SA » ; le seuil suisse est 24+0–32+0 SA, en bolus de 4 g (6 occurrences). | S27, S15 | `G80_b_1.html` |
| C05 | `_b`, « est autorisé dès 12 mois » | Le baclofène oral est employé hors indication dans la PC en Suisse. | S14 Indications | `G80_d_1.html` 1, 2, 4, 13 |
| C06 | `_b`, g80-11 | L’épilepsie (seuil convulsif) est omise ; la conduite en insuffisance rénale est inexacte (« non ajustée »). | S14 Mises en garde | `G80_d_1.html` 3, 7 |
| C07 | `_c`, Figure 2 | Le schéma de hanche est un dessin anatomique d’origine IA démontrée (commit 71fdb467). | git | `G80_c_figures.html` 1 |
| C08 | `_d`, p-3 | L’alerte « Interactions » est vide : dépresseurs du SNC (dont diazépam), tricycliques, antihypertenseurs, néphrotoxiques ; aminoglycosides avec la toxine. | S14, S13 | `G80_d_1.html` 7 |
| C09 | `_d`, p-2 | La titration intrathécale d’origine cérébrale est limitée à 5–15 %, l’entretien à 5–20 %. La colonne « Maximum » contient des moyennes ; la règle de la dose initiale manque. | S18 Posologie | `G80_d_1.html` 5, 11 |

## 4. Constats MINEURS

| Id | Constat | Source |
|---|---|---|
| C10 | « Effet maximal vers 2 semaines » vient des rubriques blépharospasme et hyperhidrose. Chez l’enfant, la FI fixe la réinjection à au moins 12 semaines (membre inférieur) ou 16 semaines (membre supérieur). | S13 |
| C11 | Dans le cas Dysport® de 20 kg, la limite effective par jambe est 300 U (15 U/kg) et non 500 U. | S13 |
| C12 | La dose de 0,3 mg/kg/j n’est pas réalisable avec les comprimés suisses (5 mg au minimum). Le plafond de 40 mg/j l’emporte sur 2 mg/kg/j dès 20 kg. | S14 |
| C13 | La SCPE recommande de classer selon la MRICS les IRM faites après 2 ans. | S4 |
| C14 | L’enquête sur les cannabinoïdes a interrogé 70 médecins d’Europe, d’Amérique du Nord et d’Australie, et non des médecins du registre suisse. | S21 |
| C15 | Le taux de 3,4 % de baclofène intrathécal vaut pour six pays en 2011, non pour « l’Europe ». | S19 |
| C16 | Le chiffre de mort subite en épilepsie concerne les enfants épileptiques en général (Suède : 1,11/1000 avant 16 ans). | S4, S25 |
| C17 | G80.1 inclut la PC spastique sans autre précision. | S1 |
| C18 | Dans la Figure 3, le type spastique est placé dans la zone « mouvement augmenté », sans source. Les textes des cinq figures mesurent 7,3 à 8,9 px à 390 px. | S4 |
| C19 | Le mécanisme du sevrage du baclofène est énoncé sans source. | S14 |
| C21 | La définition de la prématurité (37 SA) n’est pas sourcée. C’est la seule valeur non vérifiable. | — |

## 5. Enrichissements

| Id | Apport | Source |
|---|---|---|
| E01 | **Assurance-invalidité.** La PC relève du chiffre 390 de l’OIC-DFI (paralysies cérébrales infantiles congénitales). Le chiffre 395 couvre les symptômes neuromoteurs précoces avant 2 ans. | S22, S23 |
| E02 | Intervalles de radiographie des hanches du programme suédois : au diagnostic puis au moins une fois par an jusqu’à 8 ans dans les formes bilatérales ; à 4 ans dans l’hémiplégie et l’ataxie pure. | S9 |
| E03 | Seuils HINE : inférieur à 73, haut risque ; inférieur à 40, PC presque certaine ; 50–73, forme unilatérale ; inférieur à 50, forme bilatérale. | S5 |
| E04 | Spécificités : fidgety absents, Se 95 % et Sp 97 % (RV+ ≈ 32) ; HINE à 3 mois, Se 88 % et Sp 62 % ; imagerie, Se 79 % et Sp 99 % (série cas-témoins). | S26 |
| E05 | Sevrage intrathécal : délai, causes liées au cathéter et au réservoir, diagnostic différentiel. | S18 |

## 6. Calculs (EXIGENCE_CALCULS)

L’inventaire est exhaustif. `calculs/extraire.py` relève 666 nombres dans les 7 fichiers : texte visible, attributs `data-title` et `aria-label`, textes SVG et glossaire. `calculs/verifier.py` classe ces nombres en trois groupes : 85 occurrences rattachées à 20 calculs dérivés recalculés par formule, 385 valeurs comparées à leur source et 195 valeurs non calculables ; une seule valeur reste sans source. Les valeurs non calculables sont des dates, des numéros, des codes et des données de vignette.

| Contrôle | Formule | Attendu | Leçon | Verdict |
|---|---|---|---|---|
| K01 Risque avant 28 SA rapporté au terme | 146 / 1,13 | 129,2 | « près de 130 » | ARRONDI |
| K02 « un enfant sur sept » | 1000 / 146 | 6,85 | 7 | ARRONDI |
| K04 Cohorte suisse | 14 / 235 | 5,96 % | 6 % | ARRONDI |
| K05 GMFCS du registre suisse | 59 + 12 + 29 | 100 % | 100 % | CORRECT |
| K06 Hanches | 38 / 212 | 17,9 % | 18 % | ARRONDI |
| K07 Baclofène intrathécal | 114 / 3398 | 3,35 % | 3,4 % | ARRONDI |
| K08 Forme unilatérale chez les moins de 1500 g | 336 / 1426 | 23,6 % | 24 % | ARRONDI |
| K10 NNT du sulfate de magnésium | 1 / (RCT × 0,29) | RCT implicite 5,75 % | 60 | CORRECT |
| K11 Dysport®, 20 kg, deux jambes | min(30 × 20 ; 1000) | 600 U | 600 U | CORRECT |
| K12 Limite par jambe | min(15 × 20 ; 500) | 300 U | 500 U cité | CORRECT, incomplet (C11) |
| K13 Plafond de 40 mg/j | 40 / 2 mg/kg | 20 kg | non dit | CORRECT (C12) |
| K14 Baclofène pour 12 kg | 0,3 × 12 / 4 | 0,9 mg par prise | — | non réalisable (C12) |
| K16 Palier intrathécal | FI | titration 5–15 % | 5–20 % | **FAUX** (C09) |
| K17 DAYC | S5 | indice C | « sensibilité » | **FAUX** (C03) |
| K18 Chirurgie de hanche | 66,8 − 8,1 | 58,7 points | — | CORRECT |
| K19 Imagerie de la PC ataxique | 29 + 28,5 + 23,5 + 19 | 100 % | — | CORRECT |
| K20 Lecture des sensibilités | 100 × Se | 98 ; 90 ; 86–89 | idem | CORRECT |

Les valeurs fausses comparées à leur source sont les suivantes : « 34 SA » (6 occurrences, C04), « 83 % » (6, C03), « 2 semaines » (3, C10) et « 5–20 % » (2, C09). L’audit des calculs n’est **pas clos** : 470 valeurs ont été recalculées sur 471 calculables. La valeur restante, 37 SA dans le glossaire, n’a pas de source (C21).

## 7. Rubrique 21 — Sémiologie fondamentale et analytique

**Statut : absente (MAJEUR, C01).** La leçon contient des éléments épars dans l’onglet 1. L’îlot g80-5 donne les comorbidités chiffrées. L’îlot g80-6 cite les outils GMA et HINE avec leur sensibilité, et précise que « les sources lues ne détaillent pas la technique ». La leçon ne donne aucun signe d’alerte daté, aucun seuil, aucune spécificité, aucun syndrome par type ni aucun cas sémiologique.

| Critère | Leçon actuelle | Proposition |
|---|---|---|
| SEM-01 bouton `g80-s-semio` en tête | non | oui |
| SEM-02 titre exact | non | oui |
| SEM-03 audit_sciences | non | oui (2533 mots, figure, quatre libellés) |
| SEM-04 test_v7 --static | oui | à vérifier après injection |
| SEM-05 tableau des symptômes | non | oui |
| SEM-06 technique | non | partielle (appui plantaire) |
| SEM-07 mécanisme | non | partiel (déclaré) |
| SEM-08 valeurs sourcées | partiel | oui |
| SEM-09 normal d’abord | non | oui |
| SEM-10 pièges | partiel | oui |
| SEM-11 syndromes | non | oui |
| SEM-12 raisonnement en cinq étapes | non | oui |
| SEM-13 priorité clinique | non | oui (seuil de 9 mois, intervention précoce, régression) |
| SEM-14 discriminants | non | oui |
| SEM-15 examen systématique | non | oui (10 étapes) |
| SEM-16 synthèse présentée | non | oui |
| SEM-17 trois cas | non | oui |
| SEM-18 fenêtres au navigateur | non évaluable | non vérifié |
| SEM-19 sources | non évaluable | oui |
| SEM-20 cohérence | non évaluable | oui |
| SEM-21 pas de redite | non évaluable | oui |
| SEM-22 lisibilité à 390 px | non | non vérifié |
| SEM-23 captures | non | non réalisé |
| SEM-24 statut IA | oui | oui |

## 8. Matrice des 20 rubriques

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique | couvert | g80-0 |
| 2 | Définition, CIM-10-GM | couvert | g80-1 (C17) |
| 3 | Classifications | partiel | g80-2 (MACS non lu ; C13) |
| 4 | Épidémiologie | partiel | g80-3 (pas de prévalence suisse) |
| 5 | Normal → pathologique | partiel | g80-4, sciences (C02) |
| 6 | Étiologies | couvert | g80-4.2–4.3 |
| 7 | Anamnèse | partiel | g80-5 (C01) |
| 8 | Examen clinique | partiel | g80-6 (C01, E03, E04) |
| 9 | Drapeaux rouges | partiel | g80-8 (E05) |
| 10 | Examens complémentaires | partiel | e-1 à e-3 (C03, E02) |
| 11 | Diagnostic différentiel | partiel | g80-7.3 |
| 12 | Prise en charge suisse | partiel | g80-9, p-* (C05, C08, C09) |
| 13 | Complications, pronostic | partiel | g80-8, g80-10.3 |
| 14 | Suivi, prévention | partiel | g80-10 (C04) |
| 15 | Situations particulières | partiel | g80-11 (C06) |
| 16 | Spécificités suisses | partiel | registre ; AI absente (E01) |
| 17 | Critères formels | couvert | g80-12 alert |
| 18 | Paramètres clés | partiel | g80-12 key (C04) |
| 19 | Sous-codes | couvert | g80-1 |
| 20 | Points d’examen fédéral | partiel | quiz e-4, p-3 |
| 21 | Sémiologie | absent | C01 |

## 9. Lacunes de l’audit

- Aucune recommandation suisse de société savante sur la PC n’a été trouvée. Aucune source universitaire de sémiologie neuropédiatrique n’a été lue.
- La valeur des signes parentaux n’est pas chiffrée dans les sources lues.
- Les spécificités chiffrées proviennent d’une seule série cas-témoins, qui surestime la précision.
- La définition méthodologique de l’indice C n’est pas sourcée.
- Fedlex n’a pas pu être affiché : l’OIC-DFI a été lue sur une republication, et la circulaire OFAS de 2004 la corrobore.
- La page BfArM a été lue par une extraction résumée. Les intitulés français de l’OFS n’ont pas été vérifiés.
- Image_Clo_finder n’a donné qu’un candidat, non contrôlé visuellement, avant un refus HTTP 429. Aucune nouvelle tentative n’a été faite.
- Les captures n’ont pas été réalisées. La lisibilité des figures a été calculée géométriquement.
- Calculs : l’attribution des valeurs aux sources repose sur des motifs de contexte. Elle a été contrôlée sur un échantillon de 45 occurrences ; une erreur résiduelle reste possible.
- Les FI du diazépam, de la tizanidine, du glycopyrronium et des antiépileptiques n’ont pas été lues.

## 10. Propositions

`propositions/G80_c_semio.html` (discipline complète), `G80_pop3_semio.html`, `G80_b_1.html` (sulfate de magnésium), `G80_d_1.html` (pharmacologie, 14 blocs), `G80_c_1.html` (DAYC, HINE), `G80_b_2.html` (hanches, MRICS, populations), `G80_a_1.html` (AI, CIM), `G80_c_figures.html`, `G80_mineurs.html`, `glossary_g80_ajouts.py`. Chaque bloc « ancien » est présent une seule fois dans son fichier (`calculs/verifier_ancres.py`).
