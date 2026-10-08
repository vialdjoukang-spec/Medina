# Réception Claude — I89-3 — PR #12 @ 04cb957

Date : 2026-10-08  
Dépôt : `vialdjoukang-spec/Medina`  
PR : [#12](https://github.com/vialdjoukang-spec/Medina/pull/12)  
Branche : `claude/loving-shannon-spwrhc`  
Tête de livraison : `04cb95729d44648cc65339f28cf6631574babbb2`  
Baseline déclarée et vérifiée : `f204b06ac174d41632b742ec6b82097b1532b2c8`  
Lot : `2026-10-08-I89-3` — remplace I89-2.

## Décision

État : **repéré et reçu ; corrections médicales ciblées acceptées ; non intégré ; non contrôlé techniquement de bout en bout ; publication documentaire seulement**.

Le lot est bien une livraison Claude : la branche, `SIGNAUX_CLAUDE.json`, le manifeste `livraison.json` et `CORRECTIONS_AUDIT_CODEX_2.md` convergent. Il s'agit d'un contenu nouveau, pas d'une simple réémission : quatre propositions changent depuis I89-2 (`I89_c.html`, `I89_d.html`, `I89_pop2.html`, `I89_pop4.html`).

Aucune source canonique n'est injectée dans cette itération. I83 demeure le chapitre actif de Claude tant que son intégration et sa publication ne sont pas closes ; cette réception ne modifie aucune attribution ni chapitre actif. Le workspace de réception ne fournit pas le dépôt/runtime local requis pour `tools/livraison.py`, la reconstruction et les vérifications navigateur indépendantes.

## Archive immuable

Racine : `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_04CB957_I89_3/`

- 18 originaux réutilisent directement leurs blobs Git source.
- Arbre des originaux : `6d9f53ff5aadda19ae07d3820f94f2704ce14b5d`.
- Arbre archive avec provenance : `e84be709bb593dcd6e90ed43d13669f68d4416c9`.
- `PROVENANCE.json` consigne chaque chemin, SHA-1 Git et taille.

## Réconciliation de baseline et empreintes

- Baseline du lot = tête de `main` au moment de la remise : exacte.
- 11/11 SHA-256 des propositions : exacts.
- 2/2 SHA-256 des cibles remplacées : exacts (`chapters.json`, `tests/verify_s01_browser.cjs`).
- Les neuf cibles ajoutées I89 sont absentes de la baseline canonique.
- I89-2 n'est pas réappliqué : seuls les contenus réellement nouveaux de I89-3 sont considérés.

## Contre-relecture médicale ciblée

Les deux réserves bloquantes de I89-2 sont levées dans ce delta :

1. L'extrapolation du minoxidil à partir de l'hydralazine a été supprimée. Le texte distingue maintenant les mécanismes documentés par les notices officielles américaines : rénine/rétention hydro-sodée avec le minoxidil, activation rénine–angiotensine–aldostérone avec l'hydralazine.
2. Les mécanismes corrigés sont rattachés à des sources primaires ou réglementaires identifiées : notices DailyMed courantes pour minoxidil, hydralazine, ibuprofène, prednisone et pénicilline V ; étude primaire Lund et coll. (1986) pour le myxœdème, explicitement présentée comme petite étude et hypothèse des auteurs.

Cette conclusion est une **contre-relecture du delta I89-2→I89-3**, pas une certification exhaustive d'I89, des 30 cours ni du catalogue.

Réserves persistantes non bloquantes pour cette réception :

- les notices citées sont américaines, pas les informations professionnelles suisses ;
- le statut et la disponibilité suisses de Verdye en 2026 ne sont pas vérifiés ici ;
- l'étude Lund porte sur dix patients et l'archive ne fournit que l'abstract ;
- les passages non touchés sur glitazones/ENaC et docétaxel n'ont pas été contre-relus à nouveau ;
- I88 n'est pas couvert et aucune complétude CIM-11 n'est établie.

## Contrôles

### Exécutés indépendamment

- inventaire distant paginé des branches et PR ;
- comparaison de contenu I89-2→I89-3 ;
- recalcul des 11 SHA-256 de propositions ;
- recalcul des deux SHA-256 de baseline ;
- contrôle d'absence des neuf cibles ajoutées sur `main` ;
- audit statique ciblé des huit HTML : 44 gabarits/identifiants, 111 déclencheurs, aucun doublon, aucune référence manquante, aucun script embarqué.

### Archivés mais non reproduits

Le producteur annonce 118 tests unitaires, 2 595 contrôles natifs et 73 contrôles S01. Le résultat natif archivé couvre ordinateur `1360×900` et mobile `390×844` et référence les empreintes I89-3 ; ces résultats ne valent pas reproduction indépendante.

### Non exécutés

- `tools/livraison.py` ;
- injection canonique ;
- reconstruction de S01 ;
- tests unitaires locaux ;
- navigateur interactif ordinateur/mobile ;
- déploiement du site.

## Suite requise avant intégration

Conserver I83 comme chapitre actif. Après clôture I83, réconcilier à nouveau `main`, injecter les sources canoniques via `tools/livraison.py`, reconstruire S01 et reproduire les contrôles navigateur ordinateur/mobile avant toute publication du cours.
