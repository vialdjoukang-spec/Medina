# Carte des fragments

Les identifiants de systèmes reprennent à l’identique le champ `system` de la source MEDINA. Les codes de chapitre reprennent le champ `code` de `chapters.json`. Un chapitre n’apparaît que dans un fragment.

## Rattachement des chapitres existants

| Fragment | Chapitres |
|---|---|
| S01 — Cardiovasculaire | I50, I21, I25, I48, I10, I30, I33, I35, I34, I00, I40, I42, I44, I47, I49, I46, Q21, I71, I80, I70 |
| S02 — Respiratoire | J45, J44, J18, I26 |
| S03 — Digestif et hépatobiliaire | — |
| S04 — Rénal et voies urinaires | — |
| S05 — Endocrinien et métabolique | — |
| S06 — Hématopoïétique et lymphatique | — |
| S07 — Immunitaire | D84, M32, T78, M31 |
| S08 — Nerveux | — |
| S10 — Locomoteur | M06 |
| S11 — Tégumentaire | — |
| S12 — ORL et cervico-facial | — |
| S13 — Visuel | — |
| S14 — Reproducteur féminin et sein | — |
| S15 — Reproducteur masculin | — |
| S16 — Grossesse et périnatal | — |
| T1 — Agents et thérapeutique | A41 |
| T2 — Âges de la vie | — |
| T3 — Soins aigus | — |
| T4 — Oncologie, génétique et palliatif | — |
| T5 — Diagnostic | — |
| T6 — Premier recours et société | — |
| T7 — Éthique, droit et communication | — |

## Chapitres non rattachés

Aucun chapitre actuellement déclaré dans `chapters.json` n’est laissé sans fragment.

Le psychisme est volontairement exclu de la carte des fragments conformément au périmètre demandé. Tout futur chapitre relevant du psychisme devra donc rester non rattaché, avec cette exclusion comme raison.

## Étanchéité et navigation

S01 active la surface `courses-v1` : une seule spécialité (`cardiologie`, affichée « Cardiovasculaire »), un accueil des 20 cours écrits répartis en huit catégories cliniques et un Navigo rectangulaire fixe. Le panneau reste ouvert à partir de 1 100 px ; en dessous, un bouton fixe ouvre le plan. Les liens de cours, la recherche, les renvois CIM et le carnet sont limités aux cours de S01. Le carnet utilise une clé distincte de celui de l’atlas complet. L’Atlas ECG et les contenus des cours sont conservés. Les catalogues de spécialités et d’examen fédéral de l’atlas complet ne sont pas embarqués dans cette surface.

Cette surface est activée uniquement dans le manifeste de S01. Le build complet et les autres fragments gardent leur comportement actuel ; leur adaptation sera faite fragment par fragment. Le contrôle de cette première adaptation se trouve dans `audits/S01_2026-10-05/README.md`.

Un build de fragment ne conserve que les entrées CIM explicitement rattachées ou appartenant à un système rattaché. Les spécialités sont ensuite déduites de ces entrées (et leurs listes d’entrées sont recoupées) ; profils, focus, SSP reliés, plans, recherche, compteurs et modules de progression utilisent ce même sous-ensemble. Cette règle ne s’applique jamais au build MEDINA complet.

Le bandeau classe les entrées dans l’ordre croissant des codes CIM et utilise leur `block` et leur `blockTitle` comme catégorie. Un cours présent dans `chapters.json` est cliquable ; les autres entrées du bloc sont des plans grisés « à venir ». Pour un fragment transversal `T`, le champ `system` forme d’abord un axe, puis les blocs CIM forment ses catégories. Si aucun cours n’est rédigé, le bandeau est remplacé par « Aucun chapitre rédigé pour l'instant ».

Les modules transversaux suivent leur contenu : le Directeur des systèmes et les nouveaux cours sont reconstruits avec les seuls chapitres du fragment. L’Atlas ECG est réservé à S01, seul fragment actuellement concerné par ses tracés et ses cours ; il est absent des autres fragments.
