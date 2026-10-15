# Audit Alpha tour 1 — G45 — Accidents ischémiques cérébraux transitoires et syndromes apparentés (N-05-Neurologie, S08)

**Mission** ALPHA1-CLAUDE-G45-MED · audit médical agressif avec enrichissement · génération 1 · branche `claude/alpha1/g45-med-g1` · base `f664dd9e` (instantané des sources `bfc4576b`).
**Exécutant** : sous-agent Claude Code (voir accusé issue 107) ; modèle et effort conformes au manifeste. **Période** : 15.10.2026, 18:22–18:36 UTC.

## Lecture
Les sept fichiers ont été lus en entier : `G45_a`, `G45_b`, `G45_c`, `G45_d`, `G45_pop1`, `G45_pop2` et `glossary/g45.py`. Leurs empreintes SHA-256 sont **conformes au manifeste**. Toutes les ancres citées ont été vérifiées par script : chacune apparaît une seule fois dans son fichier.

La **première source lue** est le référentiel bernois *Stroke Guidelines* (PDF du 10.08.2026), page PDF 10 : définitions de l'AIT, parcours de 0 à 48 heures, score ABCD2 et différentiel avec l'aura.

## Verdict d'ensemble
La leçon est **remarquablement exacte**. Elle est fidèle au référentiel bernois, à l'ESO 2021, à la recommandation germano-austro-suisse sur l'amnésie globale transitoire et aux quatre informations professionnelles suisses. Vingt-quatre groupes de faits ont été confrontés à la source et sont conformes (liste dans `rapport.json`, clé `verifications_conformes`), dont les doses, les seuils, les essais et les calculs.

L'audit ne relève **aucune erreur bloquante**. Le défaut principal est une **omission décisionnelle** : la monothérapie antiplaquettaire immédiate de l'AIT à bas risque n'est jamais énoncée. Viennent ensuite des imprécisions de force de recommandation ou de libellé, puis des enrichissements surtout suisses et européens.

## Constats par gravité

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 1 |
| MINEUR | 7 |
| ENRICHISSEMENT | 12 |

### MAJEUR
- **C01 — `G45_b`, partie 10.2.** Les options antithrombotiques ne décrivent que la bithérapie à haut risque et la fibrillation atriale. Le parcours bernois prévoit pourtant « Start ASS » dès l'évaluation, ainsi qu'une monothérapie par aspirine, clopidogrel ou aspirine-dipyridamole [S1 p. 10 et 18]. L'ESO suggère aussi une monothérapie « de novo » [S3, PICO 7.1]. La proposition figure dans `propositions/G45_b_1.html`.

### MINEUR
- **C02** — Eren 2021 est une revue du *Deutsches Ärzteblatt*, non une « revue européenne » (`G45_a`, partie 5.4).
- **C03, C04** — L'ESO **suggère** de confirmer une sténose par angiographie (recommandation faible, preuve de très faible certitude) ; la leçon écrit « demande » ou « recommande » (fenêtres carotide et imagerie vasculaire).
- **C05** — Le tableau différentiel décrit l'amnésie globale comme « antérograde isolée ». La source et la partie 6.1 décrivent une amnésie antérograde **et** rétrograde, d'une durée moyenne de 6 à 8 heures.
- **C06** — Pour l'AIT lié à une athérosclérose intracrânienne, le tableau de conduite écrit « Déconseillée » alors que le référentiel bernois indique « No ».
- **C07** — La ligne Plavix omet deux mentions de la FI : l'association aux anticoagulants oraux n'est pas recommandée, et la triple thérapie avec le dipyridamole non plus (`propositions/G45_d_2.html`).
- **C08** — L'encadré « Examen fédéral » omet les situations 99 (troubles de la parole ou du langage) et 102 (troubles de la mémoire), rattachées à G45 dans le graphe SSP de MEDINA.

### ENRICHISSEMENTS (propositions prêtes à intégrer)

| Id | Fichier | Apport | Proposition |
|---|---|---|---|
| C09 | G45_b | Paramètres clés **chiffrés** dans le dernier `div.key` (rubrique 18) | G45_b_4.html |
| C10 | G45_b | Base légale suisse de la conduite : annexe 1, 1er et 2e groupes ; art. 15d LCR | G45_b_2.html |
| C11 | G45_b | Stratégie antihypertensive bernoise par paliers | G45_b_3.html |
| C12 | G45_a | Jusqu'à 60 % d'imitateurs ; définition ESO du haut risque (> 5 min, récidives, grosse artère) | G45_a_1.html |
| C13 | G45_a | Amnésie globale : durée moyenne, âge, rareté avant 50 ans, déclencheurs, migraine, absence de séquelle | G45_a_2.html |
| C14 | G45_a | CIM-10-GM : infarctus corrélé exclu vers I63 ; inclusions de G45.9 | G45_a_3.html |
| C15 | G45_a | Filière bernoise de l'occlusion artérielle rétinienne et de l'artérite | G45_a_4.html |
| C16 | G45_c | Bilan biologique standard, antiphospholipides avant 50 ans, polygraphie, fréquence des causes | G45_c_1.html |
| C17 | G45_c | Indications de l'ETO ; règle de fermeture du foramen ovale (RoPE, PASCAL) | G45_c_2.html |
| C18 | G45_pop1 | Strates ABCD2 à deux jours : 1 %, 4 %, 8 % | G45_pop1_1.html |
| C19 | G45_pop1 | ESO carotide 2021 : 70–99 % / 50–69 %, < 2 semaines, stent < 70 ans | G45_pop1_2.html |
| C20 | G45_d | Alternatives : clopidogrel, aspirine-dipyridamole, ticagrélor, rivaroxaban à faible dose | G45_d_1.html |

## Matrice des 20 rubriques (leçon actuelle)

| # | Rubrique | Statut | Où |
|---|---|---|---|
| 1 | Question clinique | couvert | g45-a01 |
| 2 | Définition, périmètre CIM | partiel | g45-a02 (C14) |
| 3 | Classifications | couvert | g45-a02-partie-5, g45-a04, g45-score |
| 4 | Épidémiologie | partiel | g45-a03 (lacune suisse), C12 |
| 5 | Normal → pathologique | couvert | g45-s01 à s03 |
| 6 | Étiologies, facteurs de risque | partiel | g45-a07 (C16) |
| 7 | Anamnèse (fréquences) | partiel | g45-a08 ; sans fréquences |
| 8 | Examen clinique | couvert | g45-a08, g45-examen |
| 9 | Drapeaux rouges | couvert | g45-a09 (div.alert) |
| 10 | Examens complémentaires | couvert | g45-e01 à e03 |
| 11 | Diagnostic différentiel | couvert | tableau g45-a07 |
| 12 | Prise en charge suisse | partiel | g45-a10, p01, p02 (C01, C11, C20) |
| 13 | Complications, pronostic | partiel | g45-a03, a06 (C18) |
| 14 | Suivi, prévention | couvert | g45-a11, a10-partie-4 |
| 15 | Situations particulières | couvert | g45-a11, p02-partie-5 |
| 16 | Spécificités suisses | partiel | 144, parcours, conduite (C10) |
| 17 | Critères formels (div.alert) | couvert | g45-a12 |
| 18 | Paramètres clés chiffrés | partiel | g45-a12 sans chiffre (C09) |
| 19 | Sous-codes CIM-10-GM | partiel | G45.0–G45.9 traités par îlot, non nommés |
| 20 | Points d'examen fédéral | partiel | key de g45-a07 (C08) |

## Lacunes de l'audit
- L'incidence suisse ou européenne représentative de l'AIT n'a pas été trouvée. Les requêtes PubMed et web sont consignées dans `rapport.json`.
- Le texte de l'ESO 2021 sur l'AIT a été lu partiellement par extraction outillée ; son tableau 1 mérite une relecture humaine directe. L'ESO 2021 sur la carotide n'a été lue qu'en résumé, et Eren 2021 par passages.
- Les FI de Brilique, de Xarelto, de l'association aspirine-dipyridamole et de l'aspirine intraveineuse n'ont pas été lues. Aucune dose n'est donc affirmée pour ces produits.
- Aucune recommandation suisse spécifique sur la conduite après AIT n'a été trouvée ; seule la base légale fédérale a été lue. PROFILES n'a pas été relu directement.
- Le référentiel bernois a été lu aux pages PDF 10 à 14, 18 à 21, 26 et 27. Les figures, leurs licences et les fenêtres de physiologie (Maier 2026, Kho 2025) n'ont pas été contrôlées.
- Avant d'intégrer C17, il faut ajouter une clé de glossaire RoPE.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G45 — Accidents ischémiques cérébraux transitoires et syndromes apparentés (N-05-Neurologie) |
| Fichiers lus / empreintes | 7 / conformes |
| Sources lues | 15 (S1–S15), dont 4 FI suisses en texte intégral |
| Constats | 0 BLOQUANT · 1 MAJEUR · 7 MINEUR · 12 ENRICHISSEMENT |
| Propositions rédigées | 14 fichiers sous `propositions/` |
| Matrice | 10 couvert · 10 partiel · 0 absent |
| Fichiers canoniques modifiés | aucun |

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
