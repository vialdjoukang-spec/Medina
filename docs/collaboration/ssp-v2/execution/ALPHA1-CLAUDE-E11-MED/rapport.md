# Audit médical Alpha, tour 1 — E11 — Diabète sucré de type 2 (S05 Endocrinologie)

**Mission** ALPHA1-CLAUDE-E11-MED · branche `claude/alpha1/e11-med-g1` · base `f664dd9e` · génération 1 · conversation `alpha1-claude-e11-med` · exécutant : sous-agent Claude Code (voir accusé issue 107) · modèle et effort conformes au manifeste · 15.10.2026.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## 1. Lecture et intégrité

J’ai lu en entier les sept fichiers de la leçon : les quatre onglets, les deux fichiers de fenêtres et le glossaire. Ma lecture couvre le texte, les tableaux, les figures, les quiz, les fenêtres, les Pareto, les critères `div.alert`, les paramètres `div.key` et le glossaire. Les empreintes SHA-256 recalculées sont **identiques aux sept empreintes du manifeste** (`lecture.empreintes_conformes = true`). Le manifeste porte un instantané source `bfc4576b`. La branche part de `f664dd9e`, et les sept fichiers y sont identiques octet pour octet.

La **première source lue** est l’information professionnelle suisse de Glucophage®, publiée par AmiKo (`https://amiko.oddb.org/fr/fi?gtin=7680260610169`). J’en ai lu les rubriques « Posologie », pour l’insuffisance rénale modérée, et « Mises en garde », pour les produits de contraste iodés. Au total, j’ai lu **25 sources** (`sources.json`) :

- 12 informations professionnelles suisses, avec leur date de mise à jour ;
- 7 textes suisses : SSED 2011, 2023 et 2025, consensus insuffisance cardiaque 2024, brochure néphrologique 2024, directive de conduite 2025, QualiCCare 2023 ;
- les données Obsan et le Plan de vaccination OFSP 2026 ;
- les recommandations ESC 2023, le consensus des crises hyperglycémiques 2024 et le consensus ADA/EASD 2026 ;
- la CIM-10-GM 2024 du BfArM.

## 2. Jugement d’ensemble

La leçon est **médicalement solide**. Je n’ai trouvé aucune erreur dangereuse. Les points les plus sensibles concordent avec les sources primaires suisses et européennes que j’ai lues :

- les doses, adaptations rénales, contre-indications et interactions sont **conformes aux informations professionnelles suisses en vigueur** ;
- les critères de l’acidocétose et le traitement des crises hyperglycémiques concordent avec le consensus 2024 ;
- les cibles concordent avec la SSED 2023 ;
- les seuils de dépistage de l’insuffisance cardiaque et les règles de conduite concordent avec les textes suisses.

La dose maximale de metformine de 1000 mg/j entre 30 et 59 mL/min/1,73 m² paraît plus stricte que la règle européenne habituelle. Elle reproduit pourtant exactement la FI suisse de Glucophage® (octobre 2025), qui prime ici. Il en va de même pour l’arrêt de la metformine 48 heures **avant** un produit de contraste iodé lorsque le DFG est inférieur à 60.

L’audit retient **1 constat majeur, 5 mineurs et 3 enrichissements**.

## 3. Constats par gravité

### BLOQUANT — aucun

### MAJEUR (1)

**E11-MED-01 — Provenance américaine du calendrier de dépistage** (`E11_a.html`, îlot 4, fenêtre `e11-depistage`, Pareto `pareto-e11-clin`)
- **Ce que dit la leçon.** Elle présente le dépistage « dès 35 ans, et à tout âge en cas de surpoids ou d’obésité avec facteur de risque » comme une proposition du consensus ADA/EASD 2026. La fenêtre l’appelle même un « calendrier européen co-signé ».
- **Ce que disent les sources.** Le consensus ne fait que *rapporter* cette règle (« Recent recommendations suggest… »). Il la tire de sa référence 23 : les *Standards of Care 2025* de l’American Diabetes Association. Une conduite de dépistage repose donc sur une recommandation américaine, ce que la loi 2 du prompt de vérité interdit.
- **Proposition.** Présenter le seuil de 35 ans comme un repère américain de comparaison. Déclarer qu’aucun calendrier suisse ou européen n’a été retrouvé, puis garder comme fondement européen la règle de l’ESC 2023 : rechercher un diabète chez tout patient cardiovasculaire. Voir `propositions/E11_a_1.html`, `E11_pop1_1.html` et `E11_pop2_1.html`.

### MINEUR (5)

| Id | Fichier | Constat | Source |
|---|---|---|---|
| E11-MED-02 | `E11_b.html` (îlot 10) | La leçon dit que les sulfonylurées « ne sont plus recommandées par la SSED ». Or la SSED 2023 recommande encore le gliclazide seul, dans des cas choisis. La fenêtre `e11-su` est juste, mais le résumé la contredit. | S13 |
| E11-MED-03 | `E11_d.html` (tableau des classes) | La même inexactitude figure dans la cellule « N’est plus recommandé par la SSED ; exceptions ». | S13 |
| E11-MED-04 | `E11_b.html` (îlot 10) | La phrase « éviter une HbA1c trop élevée » est vague. La SSED fixe un seuil précis : une HbA1c **> 8,0 % est à éviter dans tous les cas**. | S13 |
| E11-MED-05 | `E11_b.html` (îlot 10) | L’aspirine en prévention primaire fait l’objet d’un contentieux non exposé : la SSED la déconseille généralement, alors que l’ESC 2023 écrit « may be considered » (75–100 mg/j). | S13, S20 |
| E11-MED-06 | `glossary/e11.py` (NPH) | Selon le glossaire, la SSED « ne la recommande plus » : aucun texte lu ne le dit. La SSED 2025 cite au contraire Huminsulin® Basal comme « also an option ». | S18 |

Le tableau se lit ligne par ligne : chaque constat renvoie à la ligne de `rapport.json` qui porte la citation exacte et la proposition de remplacement. Les constats 02 et 03 se corrigent ensemble, car ils portent sur la même phrase de la SSED.

### ENRICHISSEMENT (3)

| Id | Rubrique | Ajout proposé | Source | Fichier |
|---|---|---|---|---|
| E11-MED-07 | 14 et 16 | Vaccinations OFSP 2026 : grippe, pneumocoques dès le diagnostic si atteinte d’organe, COVID-19 si complications ou HbA1c ≥ 8 % | S24 | `propositions/E11_b_4.html` |
| E11-MED-08 | 15 | Diabète de type 2 à début précoce (< 40 ans) : réduction pondérale, emploi précoce des iSGLT2 et des thérapies GLP-1, cible ≤ 6,5 %, conseil contraceptif | S22 | `propositions/E11_b_5.html` |
| E11-MED-09 | 2 et 19 | Fenêtre `e11-codage` en prose, sans îlot ni tableau CIM : E11.0 à E11.9, cinquième caractère, exclusions | S25 | `propositions/E11_pop2_1.html` |

Toutes les ancres (`ancre`) sont des extraits exacts. Un script a vérifié que chacune apparaît **une seule fois** dans son fichier (`ancre_occurrences = 1`).

## 4. Matrice des 20 rubriques (leçon telle qu’elle est)

| n | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique | couvert | `E11_a.html#e11-0` |
| 2 | Définition et périmètre CIM-10-GM | partiel | `#e11-1` (libellés et exclusions absents) |
| 3 | Classifications et stades | partiel | `#e11-1`, `e11-mrc`, `e11-cetones`, `e11-pied` (rétinopathie et neuropathie autonome non classées) |
| 4 | Épidémiologie | partiel | `#e11-2` (suisse vérifiée ; européenne absente) |
| 5 | Normal → pathologique | couvert | `#e11-3`, onglet Sciences |
| 6 | Étiologies, facteurs de risque | couvert | `#e11-4` |
| 7 | Anamnèse et symptômes | partiel | `#e11-5` (sans fréquences) |
| 8 | Examen clinique | couvert | `#e11-6` |
| 9 | Drapeaux rouges, urgences | couvert | `#e11-8` |
| 10 | Examens complémentaires | couvert | `#e11-e-1` à `#e11-e-3` |
| 11 | Diagnostic différentiel | couvert | `#e11-7`, `#e11-e-3` |
| 12 | Prise en charge suisse | couvert | `#e11-10`, onglet Pharmacologie |
| 13 | Complications et pronostic | partiel | `#e11-9` (traitement de la rétinopathie et neuropathie autonome absents) |
| 14 | Suivi, prévention, dépistage | partiel | `#e11-11` (vaccinations absentes ; E11-MED-01) |
| 15 | Situations particulières | partiel | `#e11-12` (début précoce et adolescent absents) |
| 16 | Spécificités suisses | partiel | `e11-conduite`, `e11-cout` (vaccinations OFSP absentes, AI non traitée) |
| 17 | Critères formels (`div.alert`) | couvert | `#e11-13` |
| 18 | Paramètres clés (`div.key`) | couvert | `#e11-13` |
| 19 | Sous-codes CIM-10-GM | absent | E11-MED-09 |
| 20 | Points d’examen fédéral | couvert | `#e11-7`, `e11-ssp-polydipsie`, `e11-ssp-hyperglycemie` |

Les rubriques partielles sont le meilleur point de départ : les enrichissements 07, 08 et 09 en comblent trois, et les autres attendent les lectures listées en section 5.

## 5. Lacunes déclarées

Certaines vérifications n’ont pas pu être faites ; je les déclare ici plutôt que de les présenter comme réalisées.

- **Critères de l’état hyperosmolaire** (bicarbonates ≥ 15, osmolalités 300/320). Ils figurent dans la figure 2b du consensus 2024, qui est une image : je ne les ai pas vérifiés mot à mot, mais aucune source lue ne les contredit.
- **SCORE2-Diabetes et cibles LDL de l’ESC.** Le tableau 7 et la figure 10 sont des images que je n’ai pas lues. Les cibles LDL suisses de la brochure néphrologique, elles, sont vérifiées.
- **Calendrier suisse ou européen de dépistage de population.** Je n’en ai trouvé aucun ; la requête tentée figure dans `rapport.json`.
- **Rétinopathie (stades, anti-VEGF, laser) et neuropathie autonome.** Je n’ai lu aucune source suisse ou européenne sur ces sujets ; l’enrichissement reste à rédiger après cette lecture.
- **Sources non relues dans cette mission.** Certaines FI (Trulicity®, Trajenta®, Ryzodeg®, NovoRapid®, Lantus®, Huminsulin®, Ezetrol®, Actos®, Onglyza®), IWGDF 2023, JBDS 2023, SSED technologies 2025, SSN 2025, plusieurs essais, Atila 2026, ainsi que les catalogues Viollier et La Source. Je n’y ai relevé aucune contradiction, mais je n’ai pas vérifié leurs chiffres moi-même.
- **Épidémiologie européenne.** Elle n’a pas été recherchée.

## 6. Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | E11 — Diabète sucré de type 2 (S05 Endocrinologie) |
| Fichiers lus / empreintes conformes | 7 / 7 |
| Sources lues | 25 (12 FI suisses, 9 suisses non FI, 3 européennes ou internationales, 1 classification) |
| BLOQUANT / MAJEUR / MINEUR / ENRICHISSEMENT | 0 / 1 / 5 / 3 |
| Propositions rédigées | 10 fichiers dans `propositions/` |
| Matrice des 20 rubriques | 11 couvertes, 8 partielles, 1 absente |
| Ancres vérifiées (occurrence unique) | 9 / 9 |
| Fichiers canoniques modifiés | aucun |
| Alertes | Dépistage fondé sur un texte américain (MAJEUR) ; critères HHS et SCORE2 lus seulement en figure |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
