# Audit médical ALPHA77 — G73, Affections musculaires et neuromusculaires au cours de maladies classées ailleurs (S08-Neurologie)

Mission `ALPHA1-CLAUDE-G73-MED` · branche `claude/alpha1/g73-med-g1` · base `103745baaa38c76f18288758cc7f689e5091ccdb` · sources figées au manifeste (`523832d9`) · audit du 16.10.2026 · modèle et effort conformes au manifeste.

## Lecture

Les sept fichiers de la leçon ont été lus en entier : `G73_a`, `G73_b`, `G73_c`, `G73_d`, `G73_pop1`, `G73_pop2` et `glossary/g73.py`. Leurs empreintes SHA-256 sont identiques à celles du manifeste. La première source lue est la liste systématique CIM-10-GM 2024 du BfArM, bloc G70–G73 (S1). Les contrôles exécutés donnent ceci : `test_v7.py --static G73` passe (13 342 mots, 32 fenêtres, 5 quiz, 9 Pareto). En revanche, `tests/audit_sciences.py` échoue avec 14 erreurs.

## Verdict

Le cours est honnête sur ses limites, et ses chiffres sont presque tous exacts : 389 grandeurs sur 417 concordent avec la source lue ou avec le recalcul. Il présente pourtant quatre défauts de fond :

- **la sémiologie est absente** ;
- **le différentiel avec la myasthénie n’est pas enseigné**, alors que c’est le piège principal ;
- **trois gestes d’urgence manquent**, alors que les sources suisses lues les donnent : l’atropine dans la crise cholinergique, la déclaration du botulisme dans les 2 heures, et la conduite face à la paralysie thyréotoxique ;
- **deux erreurs chiffrées** : les arrêts thérapeutiques de Leiden sont mal attribués (8 occurrences), et le score DELTA-P est déclaré non pondéré alors que la source le pondère.

Aucun constat n’est BLOQUANT. La leçon ne peut cependant pas être close tant que C01 et C02 restent ouverts.

| BLOQUANT | MAJEUR | MINEUR | ENRICHISSEMENT |
|---|---|---|---|
| 0 | 11 | 9 | 7 |

## Calculs (exigence du 16.10.2026)

Un script relève tous les nombres du texte visible des sept fichiers (`calculs/inventaire.py`). Un second script (`calculs/verifier.py`) rattache chaque grandeur à une règle : soit un recalcul (formule et tolérance écrites), soit une comparaison à la valeur citée par la source lue. Pour les pourcentages, il contrôle aussi le rapport n/N quand la source donne les effectifs. Les 40 chiffres nouveaux des propositions sont recalculés de la même façon.

| Relevés | Non-grandeurs exclues | Calculables | Recalculés | Corrects | Arrondis | Faux | Non vérifiables |
|---|---|---|---|---|---|---|---|
| 469 | 52 | 417 | 417 | 389 | 4 | 10 | 14 |

Le tableau se lit ainsi : chaque grandeur calculable a été recalculée, et aucune n’est restée sans règle.

- **Les 10 faux.** Huit présentent des arrêts de traitement tous motifs comme des arrêts pour effets indésirables (C03). Deux appellent « médiane » une moyenne (C12).
- **Les 4 arrondis.** Ils sont hérités des sources : la borne de l’intervalle de confiance de la Cochrane est imprimée « 3,6 » au lieu de 3,66 attendus, et 35/62 donne 56,5 % pour 57 % imprimés.
- **Les 14 non vérifiables.** Ce sont des énoncés incomplets : vignettes au DELTA-P incalculable, 38 % de 38 patients, deux n/N incohérents dans la source S7, posologie « 3 ou 4 prises ».

Les posologies sont toutes conformes aux informations professionnelles suisses : Firdapse® (janvier 2022) et Mestinon® (juin 2020). Les trois exemples d’incrément, ainsi que les scores PNS-Care 6, 9 et 5, sont exacts.

## Constats MAJEURS

1. **C01 — Sémiologie absente.** L’onglet Sciences compte 4 sous-onglets (`g73-s-physio`, `-immu`, `-elec`, `-bioch`) et aucun `g73-s-semio`. Une proposition complète existe : 9 sections, une figure de raisonnement mesurée à 390 px, 3 cas corrigés et 4 fenêtres. Les fréquences par symptôme viennent du Table 1 de la cohorte prospective (S4).
2. **C02 — Contrôle des sciences en échec.** Les encadrés « Science → examen », « Science → traitement » et « À retenir » manquent dans les 4 disciplines. L’immunologie n’a aucune figure, et l’électrophysiologie ne compte que 245 mots.
3. **C03 — Arrêts thérapeutiques mal attribués.** Les chiffres 50 %, 38 % et 32 % sont des arrêts tous motifs. Les arrêts pour effets indésirables touchent environ 40 % des patients sous azathioprine, 15 % sous prednisolone et 16 % sous pyridostigmine (S7).
4. **C04 — Antidote absent.** La crise cholinergique sous pyridostigmine est décrite sans son antidote : atropine 1 à 2 mg IV lente, répétée toutes les 5 à 30 minutes (FI Mestinon®, S17).
5. **C05 — Paralysie thyréotoxique sans conduite.** Cette urgence n’a ni ECG, ni surveillance de la kaliémie, ni mise en garde contre l’hyperkaliémie de rebond, ni mention du bêtabloquant non sélectif. La preuve repose sur des observations isolées, sans source européenne.
6. **C06 — DELTA-P déclaré non pondéré.** Le cours affirme que la pondération manque, alors que S4 la donne : un point par item, Karnofsky inférieur à 70, signes des trois premiers mois. Le score est donc recalculable, et la vignette de l’îlot 0 compte au moins 3 points.
7. **C07 — Codage de la forme non tumorale.** G73.1* exige un code de tumeur (C00–D48†). La forme sans tumeur, qui représente 77 % des patients à Leiden, relève de G70.8 selon l’index alphabétique : le glossaire est à corriger. Cette entrée vient d’une republication non officielle et reste à confirmer.
8. **C08 — Botulisme sans règle suisse.** Il manque la déclaration par téléphone dans les 2 heures au médecin cantonal et à l’OFSP, ainsi que la disponibilité de l’antitoxine à la Pharmacie de l’armée (S19).
9. **C09 — Drapeaux rouges de la myosite de l’enfant.** Le cours omet les signes d’alarme de la rhabdomyolyse : créatine kinase supérieure à 10 fois la limite supérieure, ou à 15 000 U/L, urines foncées, myoglobinurie (S12).
10. **C10 — Différentiel avec la myasthénie absent.** Les sources lues le permettent pourtant. Trois signes cliniques séparent les deux maladies : le début oculobulbaire, des réflexes normaux et l’absence de dysautonomie dans la myasthénie (S18). L’électrophysiologie s’y ajoute : un incrément d’au moins 60 % est rare dans la myasthénie, avec une spécificité de 95,7 % (S5).
11. **C16 — Consignes de la FI Firdapse® omises.** Il manque l’arrêt du traitement en cas de crise convulsive, l’interaction avec les cholinergiques (la pyridostigmine est associée chez 59 % des patients), les myorelaxants et l’évaluation du rapport bénéfice-risque dans la forme non tumorale.

## Constats MINEURS

- **C11** — Le cas de myopathie anti-SRP concerne un homme, non une patiente ; la créatine kinase est passée de 6 106 à 7 020 U/L, et le traitement est documenté.
- **C12** — Le séjour de 3,2 jours est une moyenne ; les 63 % d’influenza B incluent des co-infections.
- **C13** — Le chiffre de 38 % rapporté à 38 patients a un dénominateur inconnu ; les données sont déclarées par les patients.
- **C14** — À Leiden, le cancer touche moins d’un patient sur quatre (16 sur 70) ; la source donne « 14/34 (44 %) », alors que 14/34 = 41,2 %.
- **C15** — 15 mg en 4 prises n’est pas réalisable avec un comprimé de 10 mg sécable : la dose correspond à 3 × 5 mg.
- **C17** — La liste de prudence de Mestinon® est incomplète, et l’adaptation à l’insuffisance rénale manque.
- **C18** — Pour la trichinellose, la source donne 87 % dans son résumé et 86 % dans ses résultats ; 4 cas ont été déclarés en Suisse.
- **C19** — Le seuil d’incrément est écrit tantôt « supérieur à 60 % », tantôt « au moins 60 % ».
- **C20** — Un texte déborde de la figure de la myopathie cortisonique à 390 px.

## Enrichissements

- **C21** — Technique électrophysiologique : suspension des traitements 12 h avant, peau à au moins 32 °C, mesure après 10 à 30 s, décrément d’au moins 10 %.
- **C22** — Extrapolation à la Suisse : environ 27 patients et 3 à 4 nouveaux cas par an.
- **C23** — Firdapse® figure sur la liste des spécialités, à 1567,25 francs les 100 comprimés, soit environ 94 francs par jour à 60 mg.
- **C24** — Ajouter la grille PNS-Care.
- **C25** — Valeur de la facilitation post-effort : elle n’apparaît que chez un tiers des patients.
- **C26** — Épidémiologie et examens de la paralysie thyréotoxique.
- **C27** — Aptitude à la conduite.

## Matrice des 20 rubriques et rubrique 21

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique | couvert | g73-0 |
| 2 | Définition et périmètre CIM-10-GM | partiel | g73-1 (C07) |
| 3 | Classifications | partiel | g73-1, g73-14 (C24) |
| 4 | Épidémiologie | partiel | g73-2 (C22) |
| 5 | Normal → pathologique | couvert | g73-3, g73-s-* |
| 6 | Étiologies | couvert | g73-2, g73-5 à g73-8 |
| 7 | Anamnèse et symptômes | partiel | g73-4 (C01) |
| 8 | Examen clinique | partiel | g73-4 (C01, C25) |
| 9 | Drapeaux rouges | partiel | g73-11 (C04, C05, C08, C09) |
| 10 | Examens complémentaires | couvert | g73-e-1 à e-6 (C21) |
| 11 | Différentiel | partiel | g73-9 (C10) |
| 12 | Prise en charge suisse | partiel | g73-12, g73-p-* (C03, C15, C16, C17) |
| 13 | Pronostic | couvert | g73-13 |
| 14 | Suivi et dépistage | couvert | g73-10.3, g73-e-4 |
| 15 | Situations particulières | couvert | g73-13.2 |
| 16 | Spécificités suisses | partiel | (C08, C23, C27) |
| 17 | Critères formels (div.alert) | couvert | g73-14 |
| 18 | Paramètres clés (div.key) | couvert | g73-14 |
| 19 | Sous-codes | partiel | G73.0–G73.7 ; G70.8 absent |
| 20 | Points d’examen fédéral | partiel | (C10) |
| **21** | **Sémiologie fondamentale et analytique** | **absent** | **C01 ; grille SEM : SEM-01, -02, -03, -08 et -13 non satisfaits** |

La rubrique 21 se lit ainsi. Les critères SEM-01, SEM-02, SEM-03 et SEM-08 échouent parce que le sous-onglet n’existe pas et que le contrôle des sciences échoue. Le critère SEM-13 n’est que partiel : la priorité d’urgence de g73-11 omet l’atropine. Seuls SEM-04, SEM-19 et SEM-24 sont satisfaits.

## Figures

Le cours compte 3 figures. Toutes sont des schémas vectoriels en boîtes, sans structure anatomique : aucune figure anatomique n’a été dessinée par une IA. Une seule déborde à 390 px (C20). La figure proposée pour la sémiologie a été mesurée sans débordement, avec un texte de 11,9 px.

## Lacunes

- Il n’existe aucune recommandation suisse ni européenne propre au SMLE.
- L’index alphabétique officiel CIM-10-GM 2024 n’a pas été lu : l’entrée G70.8 vient d’une republication de 2026.
- Aucune source européenne de conduite n’a été trouvée pour la paralysie thyréotoxique.
- Seuls les résumés ont été lus pour la revue Cochrane 2011 et pour le registre néerlando-belge.
- Aucune source universitaire suisse de sémiologie neuromusculaire n’a été lue.
- Aucune capture réelle n’a été faite (SEM-22 et SEM-23).

Les calculs, eux, sont clos : les 417 grandeurs calculables ont été recalculées.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G73 — Affections musculaires et neuromusculaires au cours de maladies classées ailleurs (S08-Neurologie) |
| Fichiers lus | 7/7, empreintes conformes |
| Sources lues | 32 entrées (`sources.json`), dont 2 FI suisses et 11 textes intégraux |
| Constats | 0 BLOQUANT · 11 MAJEUR · 9 MINEUR · 7 ENRICHISSEMENT |
| Calculs | 417/417 recalculés · 10 faux · 0 non rattaché |
| Propositions | 8 fichiers HTML dans `propositions/` |
| Contrôles | test_v7 OK · audit_sciences en échec (C02) |
| Alerte | Clôture impossible avant C01 et C02 |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
