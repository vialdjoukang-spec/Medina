# D50 — Anémie par carence en fer : audit médical Alpha, tour 1

Mission ALPHA1-CLAUDE-D50-MED, génération 1, branche `claude/alpha1/d50-med-g1`, base `f664dd9e`. Audit médical réalisé par un sous-agent Claude Code le 15 octobre 2026. Ce rapport ne propose que des modifications ; aucune source canonique n’a été modifiée.

## Lecture et intégrité

Les sept fichiers de la leçon ont été lus en entier : `D50_a` à `D50_d`, `D50_pop1`, `D50_pop2` et `glossary/d50.py`. Leurs empreintes SHA-256 sont identiques à celles du manifeste. Les 89 clés de fenêtres renvoient toutes à une fenêtre ou à une entrée du glossaire.

La répartition des fichiers diffère du contrat habituel. Les îlots 0 à 6 se trouvent dans `_a` et les îlots 7 à 14 dans `_b`. L’onglet Examens et les Sciences sont dans `_c`, la Pharmacologie dans `_d`.

## Sources lues

Vingt et une sources figurent dans `sources.json`. La première lue est le texte intégral de la BSG 2021, obtenu par Europe PMC. Les autres textes intégraux lus sont Onkopedia (avril 2025), l’avis n° 77 de gynécologie suisse (2022) et la revue de Novacek sur le syndrome de Plummer et Vinson.

Plusieurs sources ont été lues par sections :

- OMS 2024, tableaux 2 à 5 ;
- Delphi suisse 2019 ;
- Clénin 2017 ;
- mediX 08/2025 ;
- ESC 2026, support officiel ;
- KDIGO 2026 ;
- CIM-10-GM 2024 ;
- huit informations professionnelles suisses, dont la date de mise à jour a été vérifiée.

## Verdict

Le cours est exact. Aucune erreur médicale démontrée, aucune dose fausse et aucune contre-indication fausse n’ont été trouvées.

De nombreux contrôles sont conformes :

- les seuils, la gravité et les corrections d’altitude et de tabac de l’OMS ;
- les chiffres de la BSG ;
- la conduite pendant la grossesse et après l’accouchement ;
- les seuils de KDIGO ;
- la méta-analyse sur l’hypophosphatémie ;
- les restrictions pédiatriques et le premier trimestre selon les informations professionnelles suisses.

Les constats portent sur des points de décision incomplets, sur la présentation de certaines divergences et sur des rubriques de la matrice.

| Gravité | Nombre |
|---|---|
| Bloquant | 0 |
| Majeur | 4 |
| Mineur | 5 |
| Enrichissement | 5 |

## Constats majeurs

**MED-M1 — Éradiquer Helicobacter pylori : la divergence n’est pas exposée** (`D50_pop1`, fenêtre `d50-gastrite`). Le cours ne présente que la position de la BSG 2021 : selon elle, l’éradication n’améliore pas la réponse au fer. Le guide Onkopedia 2025, auquel participe la Société suisse d’hématologie, range au contraire l’éradication parmi les traitements de la cause lorsque la gastrite est démontrée.

La proposition `propositions/D50_pop1_1.html` concilie les deux textes. Le médecin ne pratique pas de biopsies systématiques, mais il traite une infection documentée en plus du fer.

**MED-M2 — Insuffisance cardiaque : le dépistage ESC 2026 est absent** (fenêtres `d50-ic` et `d50-divergences-suisses`). Le guide européen du 28 août 2026 recommande de mesurer la saturation de la transferrine et la ferritine chez tout patient suspect d’insuffisance cardiaque (classe I, niveau C, page 39). Les classes I B et IIa B du fer intraveineux manquent également.

La position de mediX, opposée à un dépistage général, n’est pas confrontée à ce texte postérieur. La correction figure dans `propositions/D50_pop1_2.html`.

**MED-M3 — Le seuil de ferritine de 45 µg/L de la BSG manque** (fenêtre `d50-ferritine`). Selon la BSG, ce seuil offre le meilleur compromis, avec une spécificité de 0,92. Sous 45 µg/L, l’exploration digestive peut être envisagée, surtout chez un patient anémique atteint d’inflammation chronique.

Sans ce repère, un patient dont la ferritine se situe entre 30 et 45 µg/L, sous inflammation, risque de ne pas être exploré. Le complément figure dans `propositions/D50_pop1_3.html`.

**MED-M4 — Figure 3 : frottis dessiné, non recevable** (`D50_c`, Sciences, hématologie cellulaire). Ce SVG dessine des hématies normales puis ferriprives, sans source iconographique. Selon la règle de Vial du 15 octobre 2026, une figure anatomique ou cytologique générée n’est pas recevable.

La proposition consiste à supprimer ce dessin. La Micrographie 1, frottis ferriprive réel d’Ed Uthman sous licence CC BY 2.0, illustre déjà la microcytose et l’hypochromie. Il faut la faire précéder d’une micrographie réelle de frottis normal, sous licence ouverte vérifiée, à choisir par un humain.

## Constats mineurs

- **MED-m1** (îlot 8). L’encadré des signes d’urgence contient l’indication obstétricale « hémoglobine < 90 g/L : fer intraveineux ». Cette indication relève du traitement programmé, non de l’urgence, et doit être déplacée.
- **MED-m2** (îlot 8). La toxicité du fer est incomplète. L’information professionnelle Tardyferon® de juillet 2025 ajoute que le risque augmente fortement dès 60 mg/kg. Elle précise aussi que 400 mg de fer ferreux peuvent mettre en danger la vie d’un jeune enfant.
- **MED-m3** (fenêtre `d50-transfusion`). La phrase « le fer intraveineux relève l’hémoglobine en une semaine » exagère. La BSG décrit une hausse cliniquement significative en une semaine, non une correction.
- **MED-m4** (îlot 13). Le cas récapitulatif ne situe pas la coloscopie par rapport au début du fer oral. Il contredit donc implicitement la règle des deux semaines enseignée à l’îlot 9.
- **MED-m5** (îlot 2). Les prévalences de 2 à 5 % et de 5 à 12 % sont rattachées à Clénin, alors qu’elles proviennent de la BSG 2021.

## Enrichissements proposés

| Identifiant | Proposition | Rubrique |
|---|---|---|
| MED-E1 | `propositions/D50_a_1.html` | 2 et 19 : périmètre de la CIM-10-GM (E61.1, D62, D50.0, D50.1, D50.8 et D50.9), en une phrase et sans îlot dédié |
| MED-E2 | `propositions/D50_pop1_4.html` | 19 et 20 : syndrome de Plummer et Vinson (D50.1), avec membrane, dilatation et risque de carcinome épidermoïde |
| MED-E3 | `propositions/D50_pop1_5.html` | 7 : hyperménorrhée chiffrée (règles normales de 50 mL, soit environ 25 mg de fer ; hyperménorrhée au-delà de 80 mL, chez environ 15 % des femmes) |
| MED-E4 | `propositions/D50_a_2.html` | 6 : un don de 500 mL retire environ 250 mg de fer |
| MED-E5 | `propositions/D50_b_1.html` | 4 et 15 : épidémiologie européenne, nourrisson de 6 à 24 mois, lait de vache, seuils de l’OMS chez l’enfant |

## Figures

Les sept fichiers contiennent huit figures. Une seule n’est pas recevable.

| Figure | Fichier | Classe | Résultat |
|---|---|---|---|
| Photographie 1, koilonychie | `D50_a` | image sourcée | CHeitz, CC BY 2.0 ; licence vérifiée sur Commons, attribution conforme |
| Figure 5, algorithme | `D50_b` | schéma non anatomique | étapes et flèches conformes à la BSG 2021 et à sa clarification 2025 |
| Figure 1, circuit du fer | `D50_c` | schéma non anatomique | blocs de texte, sans organe dessiné ; flèches conformes à Onkopedia et à la BSG |
| Figure 2, marqueurs biochimiques | `D50_c` | schéma non anatomique | conforme à Onkopedia § 3.5 |
| Figure 3, frottis dessiné | `D50_c` | **figure anatomique générée** | **non recevable : MED-M4** |
| Micrographie 1, frottis ferriprive | `D50_c` | image sourcée | Ed Uthman, CC BY 2.0 ; licence vérifiée, attribution conforme |
| Figure 4, régulation par TMPRSS6 | `D50_c` | schéma non anatomique | enchaînement conforme au cours ; Hoving 2025 non relu |
| Photographie 2, chéilite angulaire | `pop1` | image sourcée | Matthew Ferguson 57, CC BY-SA 3.0 ; licence vérifiée, attribution conforme |

La Micrographie 1 est le seul candidat vérifié pour remplacer la figure 3. La recherche d’un frottis normal n’a pas abouti, car l’API Commons a renvoyé des erreurs 429. L’exécution du moteur commun Image_Clo_finder a ensuite été refusée par le contrôle de permissions de la session. Ce point est déclaré en lacune.

## Matrice des 20 rubriques

| Rubrique | Statut |
|---|---|
| 1 Question clinique | couvert |
| 2 Définition et périmètre CIM-10-GM | partiel |
| 3 Classifications et stades | couvert |
| 4 Épidémiologie | partiel |
| 5 Normal → pathologique | couvert |
| 6 Étiologies | couvert |
| 7 Anamnèse et symptômes | partiel |
| 8 Examen clinique | couvert |
| 9 Drapeaux rouges | couvert |
| 10 Examens complémentaires | couvert |
| 11 Diagnostic différentiel | couvert |
| 12 Prise en charge suisse | couvert |
| 13 Complications et pronostic | couvert |
| 14 Suivi, prévention, dépistage | couvert |
| 15 Situations particulières | partiel |
| 16 Spécificités suisses | partiel |
| 17 Critères formels | couvert |
| 18 Paramètres clés | couvert |
| 19 Sous-codes CIM-10-GM | absent |
| 20 Points d’examen fédéral | couvert |

Les localisations précises figurent dans `rapport.json`.

## Lacunes

- **Maastricht VI/Florence 2022.** Le texte intégral a été refusé (erreur HTTP 403). La position européenne sur Helicobacter pylori n’a donc pas été lue ni citée.
- **Candidats d’images.** Aucune micrographie réelle de frottis normal n’a pu être vérifiée : l’API Commons a renvoyé des erreurs 429, puis l’exécution du moteur commun a été refusée.
- **Donneurs de sang.** Les règles suisses de Transfusion CRS Suisse n’ont pas été trouvées.
- **Remboursement.** Les limitations de la liste des spécialités pour le fer intraveineux n’ont pas été consultées.
- **Pédiatrie.** Aucun référentiel pédiatrique suisse n’a été recherché.
- **Sources non relues.** Les sources suivantes n’ont pas été relues dans cette passe : OFSP 2020, Hoving 2025, Viollier, Hôpital cantonal de Lucerne, consensus de médecine du sport, Karczewski, Simic, Pereira Portela et OMS 2020. Leurs chiffres restent ceux des audits antérieurs.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | D50 — Anémie par carence en fer (S06, Hématologie) |
| Fichiers lus | 7 sur 7, empreintes conformes |
| Sources consignées | 21, dont 4 lues en texte intégral et 8 informations professionnelles suisses |
| Constats | 0 bloquant, 4 majeurs, 5 mineurs, 5 enrichissements |
| Figures | 8 inventoriées : 3 images sourcées, 4 schémas non anatomiques, 1 figure anatomique générée non recevable |
| Propositions rédigées | 8 fichiers HTML et 5 remplacements en ligne dans `rapport.json` |
| Ancres | 14 constats et 8 figures vérifiés par script, chaque ancre unique dans son fichier |
| Matrice des 20 rubriques | 14 couvertes, 5 partielles, 1 absente |
| Fichiers canoniques modifiés | aucun |

Audit IA : cette revue est distincte d’une validation médicale humaine, et aucune source canonique n’a été modifiée.
