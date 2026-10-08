# Reprise interne d’I-03-Infectiologie — 8 octobre 2026

L’état vérifiable au commit `2f4a7dbffba7c43ec791fb6dcea4be7d553ff5a9` est le suivant : **184 catégories du catalogue frontend actuel, un seul cours propre déclaré intégré et une couverture CIM-11 non établie**. Le chapitre actif reste **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**. Le prochain chapitre proposé est **B24 — Infection par le VIH et maladie à VIH de l’adulte (I-03-Infectiologie)**, après clôture documentée de la revue interne d’A41. Cette proposition ne réserve ni ne commence un second chapitre.

Ce dossier est un inventaire de travail. Il ne modifie aucune source canonique, aucun statut, aucun commit et aucun audit final. La mission a utilisé uniquement les sources locales ; elle n’a pas réinterrogé l’OMS ni recherché de nouvelles recommandations médicales.

## Périmètre constaté

| Objet | État au commit examiné | Portée de la preuve |
|---|---:|---|
| Catalogue anatomique historique T1 | 155 catégories | Ancien classement local CIM-10-GM 2024 |
| Catalogue frontend actuel T1 | 184 catégories, 24 blocs | Résultat de `fragment_surface.frontend_catalog()` |
| Sous-codes locaux dans ces catégories | 539 | Inventaire local ; aucun dénominateur CIM-11 |
| Catégories ajoutées par spécialité | 29 | Aucun retrait des 155 catégories historiques |
| Cours canoniques propres déclarés | 1 | A41, avec `covers=[A41]` |
| Catégories sans déclaration de cours propre intégré | 183 | Absence de déclaration ; aucune conclusion sur des enseignements dans une autre surface |
| Statut du fragment | `EN_PRODUCTION`, `complete=false` | Registre partagé |
| Inventaire pédagogique CIM-11 validé | Non établi | `inventory_path=null`, `coverage.status=non_etablie` |
| Revue interne finale, audit croisé final, injection finale | Aucun | Registre du fragment ; les preuves historiques d’A41 restent distinctes |

La source des propriétaires frontend est `fragment_surface.py`. Les 155 catégories encore mentionnées dans certains documents et outils d’organisation décrivent le classement historique ; ce chiffre ne correspond plus au catalogue frontend actuel. Le fichier `catalogue_frontend_t1.csv` conserve les 184 catégories, leurs intitulés, blocs, anciens propriétaires et déclarations de cours. `etat_t1.json` conserve aussi leurs sous-codes et les 29 transferts constatés.

Ces transferts comprennent les infections intestinales et les hépatites auparavant rattachées à S03, plusieurs infections neurologiques auparavant rattachées à S08, **A43 — Nocardiose (I-03-Infectiologie)** auparavant rattachée à S01 et trois catégories auparavant rattachées à S11. **B18 — Hépatite virale chronique (I-03-Infectiologie)** et **A04 — Autres infections intestinales bactériennes (I-03-Infectiologie)** sont donc bien dans la file actuelle de Codex. Le tableau détaillé des changements évite de reconstruire une répartition indépendante.

## A41 : préserver la base et terminer la revue interne

La version canonique d’**A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)** conserve l’injection historique `a5563238887df2a72da7a9f663bdae9ab01f4bc8`, après l’audit Claude `ba6a80fbbe901b52085f3b8f992e2e49fe592e4d`. Cette injection de chapitre sous l’ancien protocole ne signifie pas que le fragment est injecté.

Le dossier `livraisons/Livraison Codex/I-03-Infectiologie/travail/FRAGMENT_COMPLET_2026-10-08/` contient une copie interne de dix fichiers. Les dix empreintes correspondent au manifeste ; les dix fichiers canoniques correspondent toujours à la base historique préservée. Six fichiers internes ont changé ; quatre sont identiques. Le manifeste décrit expressément des propositions à contre-vérifier, un fragment incomplet et aucune injection canonique.

Les contrôles navigateur enregistrés comportent 4 446 assertions, zéro échec et zéro erreur de page, sur ordinateur et mobile, achevés à `2026-10-08T14:46:50.858Z`. Ils n’ont pas été réexécutés dans cette mission. Ils prouvent un contrôle technique de cette version, sans clôturer une relecture clinique exhaustive.

Les prochains travaux utiles sur le chapitre actif sont :

1. Faire contre-vérifier indépendamment les ajouts ESP-03 et ESP-07, avec le texte source, sa date, son domaine d’application et chaque fenêtre consommatrice. Pour les bicarbonates, conserver la distinction entre bicarbonate actuel artériel, bicarbonate standard et dosage plasmatique ; les documents locaux de 2023/2024 ne prouvent pas que les intervalles sont inchangés en 2026.
2. Fermer ou documenter les réserves cliniques encore citées : grades SSC 2026, lecture primaire d’ANDROMEDA-SHOCK-2 et Leone, codage R65, plage de prednisone, chiffre de mortalité à 29,9 %, informations suisses de gentamicine et dobutamine. Aucune correction clinique n’est décidée par cet inventaire.
3. Vérifier la cohérence entre texte, fenêtres, justifications, calculs, quiz, Pareto et glossaire, notamment les acronymes SMART, PLUS et SAFE. Chaque affirmation chiffrée doit retrouver sa source effectivement consultée et sa population.
4. Consigner la clôture interne sur une version et des empreintes exactes, avec les réserves résolues et les limites conservées. Refaire les contrôles techniques uniquement si de nouvelles modifications le justifient.

Le dossier examiné ne contient pas la preuve de cette clôture. Il est donc prématuré de remplacer le chapitre actif ou de demander un audit croisé final.

## CIM-11 : source officielle candidate, rattachement à construire

L’export officiel conservé est la **CIM-11 MMS 2026-01, français**, depuis `https://icdcdn.who.int/static/releasefiles/2026-01/SimpleTabulation-ICD-11-MMS-fr.zip`. Son empreinte SHA-256 recomputée correspond à la provenance :

`c5c7c4a07ad007892a642afd1599314f303eac5dcee89c1d1e315fcf64fa2f0f`

Le candidat du chapitre 01 contient 1 069 lignes : un chapitre, 43 blocs et 1 025 catégories ou sous-catégories. Parmi celles-ci, 323 catégories résiduelles sont conservées. Les codes et URI MMS restent présents ; les Foundation URI absentes des résiduels ne sont pas inventées. Le parent manquant de **1C1G — Borréliose de Lyme** dans la source officielle reste manquant. Les URI originales parfois non versionnées sont accompagnées de la version de l’export ; les liens français dérivés vers 2026-01 ne constituent pas une preuve de consultation individuelle.

Ce chapitre OMS ne définit pas à lui seul le périmètre pédagogique de T1. Des infections sont classées ailleurs, par exemple les infections liées aux dispositifs et implants (`NE83.1`), celles du fœtus ou nouveau-né (`KA60–KA6Z`), les maladies à prions (`8E00–8E0Z`) et les pneumonies (`CA40`). Le chapitre OMS contient aussi des entités dont la spécialité frontend relève de Claude. Un rattachement clinique explicite doit donc examiner le périmètre entier de la spécialité sans importer automatiquement des cours étrangers dans son HTML.

`matrice_cim11_candidat_a_renseigner.csv` conserve les 1 069 lignes et tous les parents fournis. Ses colonnes de rattachement pédagogique, justification, fichier, onglet, ancre et contrôle de source restent vides. Chaque ligne est marquée `RATTACHEMENT_PEDAGOGIQUE_A_ETABLIR` : ce n’est ni une liste de manques prouvés ni un dénominateur final. Pour progresser, il faut décider le périmètre pédagogique, puis documenter chaque enseignement spécifique et sa source accessible, y compris les résiduels et les variantes.

Deux entités OMS fournissent un point de départ pour la revue du sepsis : **1G40 — Sepsis sans choc septique** et **1G41 — Sepsis avec choc septique**. Leur présence dans la classification ne prouve pas leur couverture par un passage d’A41. Le bloc OMS VIH contient 27 entités codées à examiner, avec ses distinctions et résiduels ; aucune équivalence complète avec un futur chapitre n’est appliquée.

La table officielle locale de conversion 2026-01 comporte des lignes pour `A41 → 1G40`, `A41.9 → 1G40` et, de façon nécessitant une vérification manuelle, `B24 → 1C62.1` (« HIV disease clinical stage 2 without mention of tuberculosis or malaria »). Cette dernière ligne ne doit pas servir à traduire automatiquement la catégorie locale « VIH, sans précision » ni le futur chapitre VIH entier. La table est une conversion CIM-10 de l’OMS, pas une validation automatique de CIM-10-GM 2024 ni une matrice d’enseignements. Les trois lignes exactes, leurs URI et leur provenance sont conservées dans `concordance_oms_candidat.json`, avec `mapping_application=null`.

## Prochain chapitre proposé, après la clôture interne d’A41

La première priorité suivante du registre est **B24 — Immunodéficience humaine virale [VIH], sans précision (I-03-Infectiologie)**. Le titre éditorial proposé est **B24 — Infection par le VIH et maladie à VIH de l’adulte (I-03-Infectiologie)** ; il ne requalifie pas le libellé du catalogue et reste à confirmer lors de la réservation.

La préparation de ce chapitre doit commencer par un plan traçable : examiner les catégories locales B20–B24, les 27 entités codées du bloc OMS VIH et les situations relevant de la population adulte ; déterminer ce qui est enseigné dans les quatre onglets, fenêtres, quiz, Pareto et glossaire. Une déclaration `covers` ne suffira pas à certifier ce périmètre.

Les sources à sélectionner ensuite sont les recommandations et monographies primaires réellement en vigueur et applicables à la Suisse, complétées par les recommandations européennes et OMS nécessaires. Il faut conserver le texte, la version, la date de consultation et les limites de population avant de rédiger traitements, doses, interactions ou données chiffrées. Cet inventaire ne prétend pas avoir vérifié leur version courante.

Le livrable interne attendu est un chapitre complet, ses sources datées, sa matrice d’enseignements spécifiques et une revue interne sur version exacte. Il reste dans le dossier du fragment ; il n’est pas transmis comme un fragment complet.

## Progression dans le même fragment

Après ce chapitre, la file prioritaire constatée est :

| Rang suivant | Catégorie — intitulé (fragment) |
|---:|---|
| 3 | B18 — Hépatite virale chronique (I-03-Infectiologie) |
| 4 | A54 — Infection gonococcique (I-03-Infectiologie) |
| 5 | A53 — Syphilis, autres et sans précision (I-03-Infectiologie) |
| 6 | B50 — Paludisme à Plasmodium falciparum (I-03-Infectiologie) |
| 7 | A04 — Autres infections intestinales bactériennes (I-03-Infectiologie) |
| 8 | A69 — Autres infections à spirochètes (I-03-Infectiologie) |
| 9 | A15 — Tuberculose de l’appareil respiratoire, avec confirmation bactériologique, par biologie moléculaire ou histologique (I-03-Infectiologie) |
| 10 | A16 — Tuberculose de l’appareil respiratoire, sans confirmation bactériologique, par biologie moléculaire ou histologique (I-03-Infectiologie) |

Il faudra ensuite traiter les autres familles du catalogue et les entités CIM-11 pertinentes au périmètre retenu. Un regroupement pédagogique cohérent est possible si ses variantes sont réellement enseignées et reliées à des preuves ; le nombre de chapitres ou de catégories déclarées couvertes ne démontre pas la complétude.

Le travail reste dans **I-03-Infectiologie**. Le fragment Codex suivant, S08, ne commence qu’après la progression prévue pour le fragment entier. La file Codex est `T1 → S08 → S04 → T4 → S16 → S07 → S15 → S11 → T5 → T6` ; les fragments `S02, S03, S05, S06, S14, T2, S10, S12, S13, T3, T7` appartiennent à Claude. Le changement de propriétaire frontend de certaines infections n’autorise pas une réécriture des cours Claude.

Préserver les contributions historiques de Claude à A41. Les productions nouvelles de T1 ne doivent pas modifier les sources Claude de pneumologie ou d’autres spécialités, ni rouvrir la cardiologie. Les relations transversales se documentent dans la matrice avec la justification de leur périmètre ; elles ne deviennent pas des copies de contenu médical étranger dans le frontend isolé d’infectiologie.

Quand le périmètre CIM-11 est établi et tout le fragment rédigé, conduire l’auto-revue complète, corriger, contrôler l’accès aux sources et les HTML clair sur ordinateur et mobile, puis préparer une remise du fragment entier sur commit et empreintes exacts. **Claude réalise alors l’unique audit croisé final, corrige et injecte**. Les anciens audits ciblés d’A41 ne consomment pas ce tour. Le statut `INJECTE` terminal sera attribué uniquement avec les preuves du fragment entier ; aucune transmission finale n’est proposée ici.

## Pièces et limites de cette mission

- `etat_t1.json` : état, 184 catégories et sous-codes, 29 changements de propriétaire, priorités, intégrité d’A41 et proposition du prochain chapitre.
- `catalogue_frontend_t1.csv` : catalogue lisible sans recalcul de propriétaires.
- `concordance_oms_candidat.json` : entités candidates sepsis/VIH, trois lignes officielles de conversion non appliquées et limites de périmètre.
- `matrice_cim11_candidat_a_renseigner.csv` : amorce complète du chapitre 01 OMS, sans déclaration de couverture.
- `preuves_sources.json` : 20 sources du dépôt avec commit, SHA-256 et blob Git ; dix contrôles d’intégrité A41 ; provenance de la table de conversion locale.
- `constituer_inventaire.py` : reproduction locale en lecture seule, sorties limitées à ce dossier scratch.

Les preuves documentaires principales sont `AGENTS.md`, `COORDINATION.md`, `docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md`, `organisation/production_plan.json`, `organisation/fragment_status.json`, `fragment_surface.py`, `chapters.json`, `docs/COMPLETUDE_CIM11.md`, le rapport et manifeste internes d’A41, le contrôle navigateur enregistré et l’export OMS versionné. Leurs empreintes permettent de repérer tout changement postérieur au commit examiné ; il faudra actualiser l’état avant une future réservation ou remise. L’accès distant aux branches, les sources médicales nouvelles et une validation médicale humaine ne font pas partie des preuves obtenues par cet inventaire local.
