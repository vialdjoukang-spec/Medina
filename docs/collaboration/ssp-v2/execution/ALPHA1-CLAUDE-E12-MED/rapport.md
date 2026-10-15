# Audit médical Alpha, tour 1 — E12 Diabète sucré de malnutrition (S05 Endocrinologie)

**Mission** ALPHA1-CLAUDE-E12-MED · branche `claude/alpha1/e12-med-g1` · base `f664dd9e` · génération 1 · instantané des sources `bfc4576b`.
**Exécutant** : sous-agent Claude Code (voir accusé issue 107), modèle et effort conformes au manifeste.
**Date** : 15 octobre 2026.

## 1. Lecture

Les sept fichiers de la leçon ont été lus en entier : les quatre onglets, les deux fichiers de fenêtres et le glossaire. La lecture a porté sur toutes les surfaces : texte, tableaux, figures SVG et légendes, quiz, fenêtres, Pareto, `div.alert`, `div.key` et glossaire. Les sept empreintes SHA-256 recalculées sont **conformes** au manifeste.

La première source lue est l’information professionnelle suisse de Glucophage (mise à jour d’octobre 2025), consultée par `tools/swissmedic_fi.py texte 7680260610169`, rubriques Posologie et Contre-indications.

## 2. Verdict

La leçon est prudente, honnête sur ses limites et bien sourcée pour l’essentiel. Les doses de Glucophage, de Creon et de Lantus sont conformes aux informations professionnelles suisses. Le consensus de 2025 et l’étude de Vellore sont rapportés fidèlement, de même que la plupart des énoncés HaPanEU.

L’audit ne relève **aucune erreur bloquante**. Il relève toutefois **huit points majeurs** :
- quatre conduites contredites par une source suisse ou européenne de rang supérieur ;
- un contresens diagnostique ;
- un raisonnement circulaire sur le C-peptide ;
- deux figures anatomiques générées, non recevables.

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 8 |
| MINEUR | 6 |
| ENRICHISSEMENT | 11 |

Les propositions de remplacement sont rédigées et prêtes à intégrer dans `propositions/`. Aucune source canonique n’a été modifiée.

## 3. Constats majeurs

1. **C01 — Régime pauvre en graisses dans la FCPD** (`E12_b`, `E12_pop2`). La leçon suit Endotext, une revue indienne. La recommandation européenne HaPanEU demande au contraire d’éviter la restriction des graisses (énoncé 6-3.2, GRADE 1C). Elle traite la stéatorrhée par la dose d’enzymes, puis par un inhibiteur de la pompe à protons. Chez un patient dénutri, retirer la source d’énergie la plus dense aggrave la dénutrition. → `E12_b_1.html`
2. **C02 — CPRE proposée comme examen diagnostique** (`E12_c`, `E12_pop2`). Pour HaPanEU, la CPRE n’est plus un test diagnostique de la pancréatite chronique. L’échoendoscopie est la technique la plus sensible (1B) et le CT montre le mieux les calcifications (2C). L’échographie n’est utile qu’aux stades avancés (1A). → `E12_c_1.html`
3. **C03 — Sulfonylurées présentées comme option privilégiée du « type 5 »**, sans information professionnelle lue. Celle de Diamicron MR (février 2025) range les patients dénutris parmi les sujets à risque d’hypoglycémie et impose alors 30 mg par jour. Elle réserve le gliclazide aux apports alimentaires réguliers. Elle le contre-indique dans le diabète de type 1 et le diabète juvénile, pendant la grossesse et l’allaitement, et en cas d’insuffisance hépatique ou rénale sévère. → `E12_d_1.html`
4. **C04 — Syndrome de renutrition absent.** La leçon prescrit une réhabilitation nutritionnelle à des patients dont l’IMC peut descendre à 16,8 kg/m², sans dépistage du risque, sans thiamine et sans surveillance du phosphate, du potassium et du magnésium. Les sources sont suisses : Friedli et coll. (Aarau, 2018) et Krutkyte et coll. (Berne, 2022). Le rôle aggravant de l’insuline exogène est présenté comme une déduction physiopathologique, non comme un fait publié. → `E12_b_2.html`
5. **C05 — Règle de la glycémie aléatoire inversée.** Selon HaPanEU (énoncé 7-3, 1A), une glycémie aléatoire ≥ 11,1 mmol/L définit l’hyperglycémie non équivoque. La confirmation est requise *en son absence* ou en cas de doute. La leçon fait l’inverse, en trois endroits. → `E12_b_3.html`
6. **C06 — Seuil de C-peptide de 0,5 ng/mL présenté comme repère de typage.** Dans l’étude de Vellore, ce seuil était un **critère d’inclusion** des groupes, non un résultat : le raisonnement est circulaire. → `E12_b_4.html`
7. **C23 — Figure 2 « Pancréas normal et pancréas de FCPD » : figure anatomique générée, non recevable.** Elle doit être remplacée par une image réelle sourcée. → `figures_E12_c.html`
8. **C24 — Figure 3 « Îlot normal et îlot fibrosé » : figure histologique générée, non recevable.** Elle doit être remplacée de la même façon. → `figures_E12_c.html`

## 4. Constats mineurs

- **C07** : la leçon affirme qu’aucun facteur de conversion n’existe pour le C-peptide. Or 1 nmol/L = 3 ng/mL (Jones et Hattersley 2013). La médiane du « type 5 », 1,2 ng/mL, vaut donc environ 400 pmol/L : elle se situe au cœur de la zone de carence insulinique SGED (200 à 600 pmol/L).
- **C08** : les exclusions de E12 omettent l’hypo-insulinémie post-opératoire (E89.1).
- **C17** : la destruction des cellules alpha est affirmée sans nuance, alors qu’Endotext la juge discutée.
- **C18** : la figure 1 omet que les flux de glucose ont été mesurés au palier « insuline basse » du clamp.
- **C22** : le glossaire déclare inconnu le développement de HaPanEU. Il s’agit de *Harmonizing diagnosis and treatment of chronic Pancreatitis across Europe*.
- **C25** : les valeurs de la figure 1 sont exactes, mais les barres ne leur sont pas proportionnelles.

## 5. Enrichissements proposés

- **C09** : code O24.2 pour le diabète de malnutrition préexistant pendant la grossesse ; gliclazide contre-indiqué pendant la grossesse.
- **C10** : la FI de Glucophage cite le jeûne et la dénutrition comme facteurs de risque d’acidose lactique. Elle impose aussi d’arrêter la metformine 48 heures avant un produit de contraste iodé si le DFGe est inférieur à 60 mL/min/1,73 m², ce qui concerne le CT pancréatique demandé pour typer le diabète.
- **C11** : la SGED recommande une insuline co-formulée au repas principal, plutôt qu’une basale seule, dans le profil « C-peptide 200 à 600 pmol/L, anticorps négatifs ».
- **C12** : la grille suisse d’aptitude à la conduite (SGED/SGRM 2025) classe la glargine U100 en risque moyen : glycémie avant chaque trajet et aucune conduite sous 4,0 mmol/L.
- **C13** : l’information professionnelle de Januvia (sitagliptine) indique la dose, l’adaptation rénale et la mise en garde de pancréatite aiguë.
- **C14** : HaPanEU fixe une dose minimale de 40 000 à 50 000 U de lipase par repas principal (1A) ; Creon figure sur la liste des spécialités (LS).
- **C15** : élastase fécale — seuil usuel de 200 µg/g, sensibilité de 54 à 75 % dans les formes légères à modérées, faux positifs en cas de diarrhée.
- **C16** : risque de diabète dans la pancréatite chronique — 50 % à 10 ans, 83 % à 25 ans.
- **C19** : sous insuline, une HbA1c basse doit faire rechercher des hypoglycémies inaperçues ; l’effet de la carence martiale sur l’HbA1c reste non tranché.
- **C20** : le phénotype de la FCPD s’est élargi à des patients non maigres ; une hypertriglycéridémie supérieure à 500 mg/dl expose à la pancréatite.
- **C21** : la revue critique souligne le chevauchement du « type 5 » avec les formes auto-immunes.

## 6. Figures

Les sept fichiers contiennent six figures `<figure>` en SVG et cinq icônes décoratives. Ils ne contiennent ni `<img>` ni canvas.

| Figure | Fichier | Classe | Constat |
|---|---|---|---|
| 1 — Flux de glucose (Vellore) | E12_a | SCHEMA_NON_ANATOMIQUE | C25 (proportions) |
| 2 — Pancréas normal / FCPD | E12_c | **ANATOMIQUE_IA** | **C23 MAJEUR** |
| 3 — Îlot normal / fibrosé | E12_c | **ANATOMIQUE_IA** | **C24 MAJEUR** |
| 4 — Chaînes physiologiques | E12_c | SCHEMA_NON_ANATOMIQUE | conforme (0,50 ; 10,1) |
| 5 — Hypothèse antioxydante | E12_c | SCHEMA_NON_ANATOMIQUE | conforme, étiquetée « hypothèse » |
| 6 — Modèle à deux coups | E12_c | SCHEMA_NON_ANATOMIQUE | conforme à Endotext |
| Icônes de la barre de sciences | E12_c | décoratives | — |

Les candidats de remplacement sont des pages Wikimedia Commons, toutes à licence **non vérifiée** :
- pour la figure 2 : *Chronische Pankreatitis mit Verkalkungen – CT axial* et *CalcifiedPanDucStoneandSomefluid* ;
- pour la figure 3 : *Islet of Langerhans 1 – Smart-Servier* et *Langerhanssche Insel*.

Ces candidats proviennent d’une seule recherche faite avant la consigne d’utiliser le moteur commun. Ensuite, le moteur Image_Clo_finder a signalé Commons comme suspendu par son disjoncteur, et la recherche Europe PMC a été refusée par le contrôle de permissions de la session. Aucun auteur, aucune licence et aucune URL de fichier n’ont donc pu être confirmés. Une validation humaine reste obligatoire. Aucune image n’a été générée ni redessinée.

## 7. Matrice des 20 rubriques (leçon telle qu’elle est)

| # | Rubrique | Statut | Où |
|---|---|---|---|
| 1 | Question clinique | couvert | #e12-0 |
| 2 | Définition, périmètre CIM | partiel | #e12-1 (E89.1) |
| 3 | Classifications | couvert | #e12-1 |
| 4 | Épidémiologie suisse/européenne | partiel | #e12-2 (aucune donnée suisse) |
| 5 | Normal → pathologique | couvert | #e12-3, sciences |
| 6 | Étiologies, facteurs de risque | couvert | #e12-4 |
| 7 | Anamnèse (fréquences) | partiel | #e12-5 |
| 8 | Examen clinique | partiel | #e12-6 |
| 9 | Drapeaux rouges, urgences | partiel | #e12-8 (renutrition absente) |
| 10 | Examens complémentaires | partiel | pE (CPRE, élastase, seuil 0,5) |
| 11 | Diagnostic différentiel | couvert | #e12-7, #e12-e-5 |
| 12 | Prise en charge suisse | partiel | #e12-9, pP |
| 13 | Complications, pronostic | couvert | #e12-10 |
| 14 | Suivi, prévention | couvert | #e12-10 |
| 15 | Situations particulières | partiel | #e12-11 |
| 16 | Spécificités suisses | partiel | conduite, LS, AI |
| 17 | Critères formels (`div.alert`) | couvert | #e12-12 (C05) |
| 18 | Paramètres clés (`div.key`) | couvert | #e12-12 |
| 19 | Sous-codes CIM-10-GM | partiel | 31 codes non énumérés |
| 20 | Points d’examen fédéral | partiel | aucun rattachement PROFILES |

## 8. Lacunes de l’audit

- **Revue médicale suisse 2022 non relue** : l’article est payant et le dépôt UNIGE ne donne pas de lien PDF exploitable. Les affirmations qui en dépendent n’ont pas été revérifiées : 1 à 9 % des diabètes, répartition des étiologies, critères d’Ewald et Bretzel.
- **Rapport OMS 2011 sur l’HbA1c inaccessible** (vérification reCAPTCHA).
- **Codes non vérifiés** : le code CIM-11 et le libellé CIM-10-GM de O24.2.
- **Informations professionnelles non lues** : répaglinide, agonistes du GLP-1, inhibiteurs du SGLT2.
- **Friedli 2018 lu au résumé seulement.**
- **Sujets sans source lue** : la conduite de l’hypoglycémie sévère et le différentiel infectieux du migrant amaigri.
- **Figures** : licences des candidats non confirmées.

## 9. Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | E12 — Diabète sucré de malnutrition (S05) |
| Fichiers lus / empreintes conformes | 7 / 7 |
| Sources lues | 19 (5 en texte intégral, 11 par section, 3 au résumé) |
| Informations professionnelles suisses | Glucophage, Creon, Lantus, Diamicron MR, Januvia |
| Constats | 25 (0 B, 8 M, 6 m, 11 E) |
| Propositions HTML | 23 fichiers dans `propositions/` |
| Ancres vérifiées mécaniquement | toutes présentes, ≤ 200 caractères |
| Figures inventoriées | 6 (+ 5 icônes) ; 2 ANATOMIQUE_IA |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
