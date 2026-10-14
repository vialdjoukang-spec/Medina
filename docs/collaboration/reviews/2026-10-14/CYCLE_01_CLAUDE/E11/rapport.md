# E11 — Diabète sucré de type 2 : audit Claude du 14 octobre 2026

Sous-agent d'audit E11, Cycle 1, branche `claude/great-cerf-uizsml`. Il s'agit d'une revue par intelligence artificielle, sans validation médicale humaine. Aucun commit ni push n'a été fait.

## Méthode

J'ai calculé les empreintes des sept fichiers avant toute modification (`sources/sha256_avant.txt`). J'ai ensuite lu en entier les quatre onglets, les deux fichiers de fenêtres et le glossaire. Plus de 40 chiffres clés ont été confrontés aux sources primaires lues le 14.10.2026 :

- les informations professionnelles suisses AIPS de Glucophage, Jardiance, Forxiga, Ozempic, Mounjaro, Kerendia, Tresiba, Toujeo, Januvia, Diamicron et Baqsimi ;
- les recommandations SSED 2011, 2023 et 2024 ;
- la brochure SSED–néphrologie 2024 ;
- la figure 2 du consensus 2024 sur les crises hyperglycémiques ;
- le tableau 6 de l'ESC 2023, lu dans la traduction italienne officielle ;
- l'indicateur OFSP/Obsan.

Le dossier `sources/` archive les textes extraits.

## Passe 1 — 17/20

| Critère | Note | Constat |
|---|---|---|
| Exactitude et actualité | 3,5/4 | Aucune posologie fausse. La cible stricte de 6,5 % omettait la population « complications microvasculaires » (SSED 2023). L'en-tête du tableau attribuait le prédiabète 5,6–6,9 mmol/L à l'ESC 2023, qui se contente de comparer les critères de l'OMS et de l'ADA. |
| Complétude | 2/3 | La situation PROFILES 3 (soif excessive) n'était pas traitée. Le différentiel de la situation 158 (glycémie anormale) tenait en une seule phrase. |
| Pédagogie | 2,5/3 | Le différentiel était présenté de façon linéaire, sans tableau ni examen décisif. |
| Corrélations vertes | 2/2 | — |
| Sciences et schémas | 1,5/2 | Aucune image réelle. Les schémas étaient étiquetés « pédagogiques ». |
| Examens | 2/2 | — |
| Pharmacologie | 1/1 | — |
| Pareto | 1/1 | — |
| Langue | 0,75/1 | Une phrase était répétée dans l'îlot 7, et des références contenaient des mots et des chiffres accolés. |
| Interface | 0,75/1 | Aucune image réelle. La lisibilité mobile des figures SVG avait déjà été relevée le 11.10. |

## Corrections

**Médicales (2)**
1. Cible de 6,5 % : elle s'applique au sujet jeune au diabète récent **ou** porteur de complications microvasculaires, sans hypoglycémie significative et répétée. La correction porte sur les îlots 10 et 13 et sur la fenêtre `e11-cibles`.
2. Attribution du prédiabète : l'en-tête du tableau indique désormais SSED 2011 seule, et une phrase précise le rôle comparatif de l'ESC.

**Linguistiques et de forme (4)**
1. Suppression de la répétition dans l'îlot 7.
2. « Schéma pédagogique » remplacé par « schéma didactique, et non image clinique » sur les figures 1 à 6.
3. Typographie des références dans `e11-score2-methode` et `e11-unite-mgdl`.
4. Deux formulations non sourcées que j'avais introduites, corrigées lors de la passe 2.

## Enrichissements

- **Situation PROFILES 3 (soif excessive)**
  - Un paragraphe dans l'îlot 5.
  - La fenêtre `e11-ssp-polydipsie`, sur le diagnostic d'une polyurie avec polydipsie, d'après les publications de l'Hôpital universitaire de Bâle de 2025-2026. Elle contient :
    - les définitions chiffrées (40 mL/kg/24 h, 800 mOsm/kg, 3 L/j) et un calcul ;
    - huit hypothèses classées par gravité puis par fréquence ;
    - les seuils de copeptine (21,4 et 4,9 pmol/L, natrémie ≥ 147 mmol/L) ;
    - le danger d'une restriction hydrique non surveillée ;
    - les nouveaux noms de 2022.
- **Situation PROFILES 158 (glycémie anormale)**
  - Dans l'îlot 7, un tableau de raisonnement à huit rangs : hypothèse, élément discriminant, examen décisif. Il est suivi d'une lecture commentée et d'un exemple.
  - La fenêtre `e11-ssp-hyperglycemie`, qui déroule le raisonnement en cinq étapes et traite aussi le versant hypoglycémique.
- **Quiz 5 :** polyurie sous lithium.
- **Pareto Diagnostic :** une puce sur le raisonnement à partir des situations de départ.
- **Fenêtre `e11-acanthosis`**, consacrée au signe cutané de l'insulinorésistance.
- **Glossaire :** trois noms propres ajoutés (Christ-Crain, Kimmelstiel-Wilson, KGH), en ajout conditionnel.

## Images réelles (4), vérifiées visuellement avec Read

| Figure | Emplacement | Fichier | Licence |
|---|---|---|---|
| 7 — Acanthosis nigricans axillaire | îlot 6 | acanthosis_nigricans.jpg | CC BY-SA 4.0 (Brady, Rawla) |
| 8 — Fond d'œil, rétinopathie diabétique | îlot 9 | fundus_diabetic_retinopathy.jpg | CC BY 4.0 (Hao et al., PLoS One 2022) |
| 9 — Glomérulosclérose nodulaire, coloration à l'acide périodique de Schiff | fenêtre e11-mrc | diabetic_glomerulosclerosis_4_pas.jpg | CC BY-SA 3.0 (KGH) |
| 10 — Ulcère neuropathique plantaire | fenêtre e11-pied | neuropathic_heel_ulcer_diabetic.jpg | CC BY 3.0 (J. Moore) |

Les attributions, empreintes et vérifications sont consignées dans `assets/img/cycle1/e11/ATTRIBUTIONS.json`. Chaque image est suivie d'un commentaire explicatif.

## Passe 2 — 19,5/20

J'ai relu les zones modifiées et l'ensemble des fichiers corrigés, puis corrigé quatre points :

- une hiérarchie de fréquence non sourcée (îlot 5) ;
- deux interprétations de la photographie de l'ulcère ;
- un exemple d'exposition non sourcé dans l'alerte de la fenêtre polydipsie ;
- la latéralité de l'œil retirée du texte alternatif.

| Critère | Note |
|---|---|
| Exactitude et actualité | 4/4 |
| Complétude | 2,75/3 |
| Pédagogie | 3/3 |
| Corrélations vertes | 2/2 |
| Sciences et schémas | 2/2 |
| Examens | 2/2 |
| Pharmacologie | 1/1 |
| Pareto | 1/1 |
| Langue | 1/1 |
| Interface | 0,75/1 |

Les deux demi-points restants s'expliquent ainsi :

- Complétude : l'hypoglycémie hors traitement est seulement renvoyée à une exploration spécialisée.
- Interface : le rendu mobile n'a pas été recontrôlé au navigateur.

## Contrôle technique

`python3 test_v7.py --static E11` : `E11 mots 36548 fenêtres 128 quiz 5 pareto 7` puis **OK**.

## Réserves ouvertes

1. Aucune validation médicale humaine.
2. Les sources Tervaert 2010, Radu 2022, Popa 2018, Atila 2024 et Arima 2022 ont été lues au niveau du résumé PubMed.
3. Il n'existe pas de recommandation suisse de société savante sur la polyurie-polydipsie. Cette lacune est tracée ; les sources retenues sont des revues bâloises.
4. Le registre des sources et la matrice de contexte suisse du 11.10 n'ont pas été mis à jour.
5. Les espaces insécables avant « ; : ? ! » ne sont pas posés : le projet utilise partout des espaces ordinaires, et cette conversion relève d'un traitement central.
6. La numérotation des figures n'est pas séquentielle dans l'ordre de lecture. Je l'ai héritée et conservée.
7. Le rendu navigateur n'a pas été recontrôlé, en particulier la lisibilité mobile des schémas SVG.
