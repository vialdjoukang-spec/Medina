# Audit Alpha tour 1 — N18 Maladie rénale chronique (S04 Néphrologie)

**Mission** ALPHA1-CLAUDE-N18-MED · audit médical agressif avec enrichissement · branche `claude/alpha1/n18-med-g1` · base `f664dd9e` · génération 1 · modèle et effort conformes au manifeste.

## Verdict

La leçon N18 est solide. Aucune erreur médicale dangereuse n’a été démontrée. Les points à risque (posologies, seuils, interactions, calculs) ont été confrontés aux informations professionnelles suisses en vigueur et aux textes KDIGO, SSN et SSED/SSN. Ils sont conformes. Les seize calculs chiffrés de la leçon ont été refaits : tous sont exacts.

Deux points décisionnels restent incomplets (MAJEUR). Trois imprécisions mineures concernent une attribution et deux figures (MINEUR). Cinq rubriques méritent un enrichissement.

Les sept fichiers ont été lus en entier : onglets, tableaux, figures, quiz, 111 fenêtres, Pareto, `div.alert`, `div.key` et glossaire. Leurs empreintes SHA-256 sont **conformes au manifeste** (7/7).

## Constats MAJEURS

**MED-01 — Bloqueur du système rénine–angiotensine : indication et dose (N18_d.html, N18-C0283).**
Le cours prend Ramipril Zentiva comme bloqueur de référence et donne 5 mg par jour comme dose maximale. Or l’indication rénale de la FI suisse se limite à la « néphropathie glomérulaire avec protéinurie supérieure à 3 g/jour » ; M. L. n’en relève pas. Le cours n’énonce pas non plus la règle de la « dose maximale tolérée et autorisée » (SSN 2025 ; KDIGO, point de pratique 3.6.1). Il ne mentionne pas Aprovel (irbésartan), dont la FI suisse couvre la néphropathie du diabétique de type 2 hypertendu, à 300 mg et sans adaptation rénale.
→ Proposition : `propositions/N18_d_1.html`.

**MED-02 — Inhibiteur SGLT2 entre 20 et 24 mL/min/1,73 m² (N18_b.html, N18-C0113, N18-C0120 et Pareto).**
Le cours oppose le seuil de classe (20) à la seule FI de Forxiga (25). Il ne signale pas que la FI suisse de Jardiance autorise l’instauration jusqu’à 20 ; le tableau SSED/SSN fait d’ailleurs cette distinction. Entre 20 et 24, le lecteur reste donc sans option conforme.
→ Proposition : `propositions/N18_b_1.html`.

## Constat MINEUR

**MED-03 — Fer et anémie (N18-C0126).** La fiche SSN 2025 présente ferritine 300–500, saturation de la transferrine > 30 % et hémoglobine 10–11,5 g/dL comme des « objectifs ». Le cours les appelle « repères ». La résolution par KDIGO 2026 reste juste, mais la source suisse doit être citée telle qu’elle est rédigée.
→ Proposition : `propositions/N18_b_6.html`.

**MED-09 — Figure 1, fréquence de contrôle (N18-C0080).** La matrice publiée (Farrell et Vassalotti 2024) indique 2 contrôles par an pour G1–G2 A3. La figure 13 de KDIGO 2024 et la fenêtre N18-C1048 en indiquent 3. Il faut signaler l’écart dans la légende.

**MED-10 — Figure 2, légende inexacte (N18-C0104, N18-C0106).** L’image est « Tips for improving the detection and management of CKD in primary care » (Robson et al. 2024). C’est une liste de conseils et de ressources australiennes, sans étape de confirmation ni de retour au suivi. Il faut la décrire exactement ou la retirer au profit de la figure 4 de la fiche SSN 2025.

## Enrichissements proposés (prêts à intégrer et sourcés)

| ID | Rubrique | Contenu | Fichier |
|---|---|---|---|
| MED-04 | 12, 15 | Metformine selon le DFGe : maximum 1 000 mg/j entre 30 et 59, contre-indication < 30, arrêt 48 h autour d’un produit de contraste iodé (FI Glucophage) ; prudence SSED/SSN entre 30 et 45 | `N18_b_2.html` |
| MED-05 | 14, 16 | Vaccinations selon le plan suisse 2026 : grippe ; COVID-19 si DFG < 60 ; pneumocoques dès le stade 4 ou en cas de syndrome néphrotique ; hépatite B à 40 µg chez le dialysé | `N18_b_3.html` |
| MED-06 | 13 | Hyperuricémie et goutte (KDIGO 3.14) | `N18_b_4.html` |
| MED-07 | 12 | Poursuite de l’IEC ou du sartan sous 30 (point de pratique 3.6.7) et motifs limités de réduction | `N18_b_5.html` |
| MED-08 | 12, 13 | KDIGO 2026 : seuil d’instauration d’un agent stimulant (85–100 g/L), vitesse de hausse, carence martiale profonde sans anémie | `N18_pop1_1.html` |

## Vérifications conformes (échantillon décisionnel)

- **Posologies et contre-indications des FI suisses** : Eliquis (réduction selon au moins 2 critères sur 3), Kerendia (10 mg avec un inhibiteur modéré du CYP3A4 ; seuils de potassium 4,8, 5,0 et 5,5), Forxiga (seuil de 25 ; essai DAPA-CKD), Aspirine Cardio (contre-indication si clairance < 30), Venofer, Aranesp, Crestor, Néphrotrans, Ozempic, Veltassa, Aldactone et Lasix.
- **KDIGO 2024** : catégories G et A, variations de 20 % et de 30 %, seuils de risque KFRE (3–5 %, 10 %, 40 %), figure 48, apport protéique, bicarbonate, finérénone, début de la dialyse.
- **Textes suisses et européens** : KDIGO 2026 pour l’anémie ; SSN 2025 ; SSED/SSN 2024 (drapeaux rouges, seuils d’âge, potassium, bicarbonate) ; valeurs de référence HUG.
- **Calculs refaits** : CKD-EPI 2021, KFRE, ACR, Cockcroft–Gault, clairance, Ganzoni et désindexation.

## Figures (règle Vial du 15.10.2026)

Les 7 fichiers ont été inventoriés. Ils contiennent **8 `<figure>`/`<img>`**, aucun `<svg>`, aucun `canvas` et aucun dessin CSS. Chaque image a été ouverte et relue.

| Ancre | Image | Classe | Source et licence | Résultat |
|---|---|---|---|---|
| N18-C0080 | n18_01 matrice G/A | SCHEMA_NON_ANATOMIQUE | Farrell et Vassalotti 2024, CC BY 4.0 (vérifiée sur PMC) | MED-09 : G1–G2 A3 = 2/an contre 3 selon KDIGO 2024 |
| N18-C0106 | n18_02 rôle du médecin généraliste (Australie) | SCHEMA_NON_ANATOMIQUE | Robson et al. 2024, CC BY 4.0 (vérifiée sur PMC) | MED-10 : légende inexacte |
| N18-C0211 | n18_03 deux échographies réelles | IMAGE_SOURCEE | Hansen et al. 2016, CC BY 4.0 (vérifiée sur PubMed/PMC) | Conforme |
| N18-C0229 | n18_04 néphron et capillaires (OpenStax) | IMAGE_SOURCEE | Commons, CC BY 3.0 déclarée | Conforme ; licence non revérifiée par l’API |
| N18-C0233 | n18_05 histologie PAS réelle (Nephron) | IMAGE_SOURCEE | Commons, CC BY-SA 3.0 déclarée | Conforme ; partage identique respecté dans la légende |
| N18-C0244 | n18_06 réabsorption et sécrétion (OpenStax) | IMAGE_SOURCEE | Commons, CC BY 3.0 déclarée | Flèches conformes à N18-C0242 |
| N18-C0258 | n18_07 homéostasie calcique (OpenStax) | SCHEMA_NON_ANATOMIQUE | Commons, CC BY 3.0 déclarée | Flèches conformes ; ambiguïté « ±10 mg/dL » expliquée par le cours |
| N18-C0270 | n18_08 système rénine–angiotensine–aldostérone (OpenStax) | IMAGE_SOURCEE | Commons, CC BY 3.0 déclarée | Conforme |

**Aucune figure anatomique générée par IA (ANATOMIQUE_IA = 0).** Aucune recherche de remplacement n’était donc requise. Pour les quatre fichiers OpenStax et l’image du contributeur Nephron, la licence Commons n’a pas pu être revérifiée : l’API a renvoyé une erreur 429, puis le moteur commun Image_Clo_finder a suspendu l’hôte. Cette vérification est déclarée en lacune. Le détail se trouve dans `rapport.json`, aux clés `figures` et `figures_inventaire`.

## Matrice des 20 rubriques

**Couvertes (10)** : 1, 3, 5, 6, 9, 10, 11, 17, 18, 19.
**Partielles (10)** : 2, 4, 7, 8, 12, 13, 14, 15, 16, 20.
**Absentes** : aucune.
Le détail figure dans `rapport.json`, champ `matrice_20`.

## Lacunes déclarées

- Les libellés CIM-10-GM 2024 n’ont pas été revérifiés contre le catalogue de l’OFS.
- Plusieurs spécificités suisses n’ont pas été recherchées : AI, aptitude à la conduite, Swisstransplant, registre de dialyse.
- L’épidémiologie européenne n’a pas été recherchée.
- Les FI de Norvasc, Ezetrol et Repatha n’ont pas été relues ligne à ligne.
- Le traitement d’urgence de l’hyperkaliémie est absent du cours. Son renvoi vers un autre chapitre n’a pas été vérifié.
- Les objectifs PROFILES/SSP n’ont pas été consultés.
- Les licences Commons des figures 4 à 8 n’ont pas été revérifiées par l’API (erreur 429, puis disjoncteur du moteur commun).

## Tableau de bord

| Élément | Valeur |
|---|---|
| Fichiers lus / empreintes conformes | 7 / 7 |
| Sources lues | 27 (dont 16 FI suisses datées) |
| BLOQUANT / MAJEUR / MINEUR / ENRICHISSEMENT | 0 / 2 / 3 / 5 |
| Figures inventoriées / ANATOMIQUE_IA | 8 / 0 |
| Propositions HTML | 8 |
| Ancres vérifiées mécaniquement | 10 constats + 8 figures, toutes présentes |
| Fichiers canoniques modifiés | 0 |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
