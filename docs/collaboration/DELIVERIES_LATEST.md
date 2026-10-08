## Alignement visuel avec Claude — 8 octobre 2026

Sur instruction directe de Vial, Atkinson Hyperlegible Next de Claude (`f928674`) est la police par défaut. Ses deux commits frontend sont repris avec son attribution. Les 22 spécialités, le thème clair, les contrastes et les préférences de lecture sont vérifiés ; les sources médicales et statuts d’injection sont inchangés. [Réalisation](FRONTENDS_2026-10-08.md) · [Reçu d’alignement](receipts/CODEX_ALIGNEMENT_ATKINSON_2026-10-08.json). Les mentions Anthropic et publication à vérifier ci-dessous correspondent aux étapes antérieures ; le reçu d’alignement donne l’état actuel.

## Frontends distincts — 8 octobre 2026

La demande directe de Vial ajoute un accueil moderne clair, Anthropic Serif embarquée et un frontend strictement limité à chaque spécialité. Les 22 frontends sont reconstruits et contrôlés ; le portail donne accès aux 32 cours intégrés. L’aperçu A41 interne est consultable sous `apercus/infectiologie.html#/entry/A41`, avec statut de travail et sans certification finale. Sources médicales canoniques et statuts d’injection inchangés. Voir [la réalisation](FRONTENDS_2026-10-08.md) et [le reçu](receipts/CODEX_FRONTENDS_2026-10-08.json). La publication servie reste à vérifier dans le reçu. La remise distante J09 de 9fa4651 est conservée comme travail de chapitre ; elle ne vaut pas fragment entier prêt à l’audit unique.

## Reprise par fragments — 8 octobre 2026

[Nouveau protocole](PROTOCOLE_FRAGMENTS_2026-10-08.md) et [rapport de reprise](reviews/2026-10-08/REPRISE_FRAGMENTS/REPRISE.md). Les listes complètes de branches/PR et leurs pages suivantes sont vérifiées ; [têtes relevées](reviews/2026-10-08/REPRISE_FRAGMENTS/REMOTE_HEADS.json). A41 a été injecté comme chapitre à `a556323`, après audit Claude `ba6a80f` sous les règles précédentes. Le fragment T1 reste incomplet ; la nouvelle copie A41 demeure interne. L’index détaillé ci-dessous conserve son ancienne cible et son état historique.

# MEDINA — livraisons repérées

Branche d'intégration : `codex/sciences-cs-fragments-20261007`.
Commit cible : `83bff147e0aba6b31e7a080e098770b0a6b4250d`.

Scan : partiel ; réserves ci-dessous.
Une livraison repérée ou reçue n'est pas présumée intégrée. Une intégration ne prouve pas une vérification.

| Branche / PR | Tête | Reçu | Intégré dans la cible | Vérifié | Routage |
| --- | --- | --- | --- | --- | --- |
| claude/loving-shannon-spwrhc · #12 | `9aa65044972f` | Non confirmé | Non démontré | Non démontré | GLOBAL, S01, S02 |
| codex/a41-corrections-20261008 · #15 | `5f04f5d950f7` | Non confirmé | Non démontré | Non démontré | CS, GLOBAL, S01, T1 |
| codex/accueil-qcm-20260929 · #6 | `871bb223564d` | Non confirmé | Non démontré | Non démontré | GLOBAL |
| codex/decision-i83-20261008 | `db06b1fae3c2` | Non confirmé | Non démontré | Non démontré | CS, GLOBAL, S01, T1 |
| codex/transition-cardio-20261008 | `fdad6c8adac0` | Non confirmé | Non démontré | Non démontré | GLOBAL |
| main | `61a841b3c96b` | Non confirmé | Non démontré | Non démontré | CS, GLOBAL, S01, T1 |
| claude/medina-alpha-integration-7dul4i · #1 | `303f95a66dd2` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL, S01, S02, S07, S10, SYSTEM, T1 |
| claude/mission-justification-20261007 · #11 | `45d34a9bd303` | Oui | Oui, preuve enregistrée | Non démontré | GLOBAL |
| claude/review-i48-esc2024-20261007 | `c3770739b58c` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| claude/review-medina-global-20261007 · #10 | `7651825416cc` | Oui | Oui, preuve enregistrée | Non démontré | GLOBAL, S01, S02 |
| claude/review-medina-global-20261007 · #9 | `394dc0857f83` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | GLOBAL, S01, S02, S07, S10, T1 |
| claude/review-medina-global-20261007 · #8 | `f6e400df9e5d` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | CS, GLOBAL, S01 |
| codex/ajouter-options-de-generation-de-fragments · #3 | `1539f4e77171` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/configurer-publication-github-pages-automatique · #4 | `8d0de9bcd572` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/creer-fragments.json-et-corrige-des-chemins · #2 | `0f38d9aab4ef` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/etancheite-complete-des-fragments · #5 | `7071e557cfc2` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/fragment-s01-accueil-navigo-20261005 · #7 | `c50a28a23d7e` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL, S01 |
| codex/mechanismes-20261007 | `39b7ff0cc585` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| codex/repartition-fragments-20261008 | `20915d9a36f0` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| codex/sciences-cs-fragments-20261007 · #13 | `83bff147e0ab` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL, S01, S02, S07, S10, T1 |

## claude/loving-shannon-spwrhc

- Chemin sans route de build connue ; examen manuel requis.
- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- Cours absent de chapters.json de la cible ; déclaration à intégrer.
- S01 : le cours doit figurer exactement une fois dans categories[].chapters.
- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction.
- Diff de branche potentiellement tronqué ; consulter tous les fichiers de la PR ou un diff Git local.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.gitignore` | unknown |  | integration_target |
| `CLAUDE.md` | documentation | GLOBAL | integration_target |
| `chapters.json` | registration_source | GLOBAL | integration_target |
| `chapters/I83/I83_a.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_b.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_c.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_d.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop1.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop2.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop3.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop4.html` | course_source | S01 | integration_target |
| `docs/collaboration/REGLES_VIAL_2026-10-08.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/SIGNAUX_CLAUDE.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/VEILLE.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ZONES_COMPENDIUM.md` | documentation | GLOBAL | integration_target |
| `glossary/fragments_medina.py` | glossary_source | GLOBAL | integration_target |
| `glossary/i83.py` | glossary_source | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/ACCUSE_PRISE_EN_CHARGE_2026-10-08.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/README.md` | delivery_source | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I00/I00_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I10/I10_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I21/I21_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I25/I25_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I30/I30_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I33/I33_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I34/I34_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I35/I35_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I40/I40_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I42/I42_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I44/I44_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I46/I46_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I47/I47_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I48/I48_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I48/I48_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I48/I48_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I48/I48_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I49/I49_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I50/I50_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I71/I71_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I71/I71_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I71/I71_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I71/I71_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I71/I71_pop.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I71/I71_pop_sciences.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I80/I80_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I80/I80_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I80/I80_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I80/I80_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I80/I80_pop.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/I80/I80_pop_sciences.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/sources/chapters/Q21/Q21_pop7.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08-ESC2026_COMPARAISONS/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I30/controles/i30_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I30/controles/i30_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I30/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I30/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I30/sources/chapters/I30/I30_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I30/sources/chapters/I30/I30_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/controles/i33_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/controles/i33_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/sources/chapters/I33/I33_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I33/sources/chapters/I33/I33_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I34/controles/i34_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I34/controles/i34_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I34/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I34/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I34/sources/chapters/I34/I34_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I34/sources/chapters/I34/I34_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/controles/i35_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/controles/i35_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/sources/chapters/I35/I35_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/sources/chapters/I35/I35_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I35/sources/chapters/I35/I35_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I40/controles/i40_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I40/controles/i40_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I40/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I40/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I40/sources/chapters/I40/I40_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I40/sources/chapters/I40/I40_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/controles/i42_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/controles/i42_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I42/sources/chapters/I42/I42_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/controles/i44_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/controles/i44_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/sources/chapters/I44/I44_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/sources/chapters/I44/I44_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/sources/chapters/I44/I44_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-I44/sources/chapters/I44/I44_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/controles/q21_native_main.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/controles/q21_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/sources/chapters/Q21/Q21_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/sources/chapters/Q21/Q21_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026-Q21/sources/chapters/Q21/Q21_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I30/I30_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I30/I30_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I33/I33_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I33/I33_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I34/I34_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I34/I34_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I35/I35_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I35/I35_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I40/I40_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I40/I40_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I42/I42_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I44/I44_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I44/I44_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I44/I44_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/I44/I44_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/Q21/Q21_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/Q21/Q21_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-ESC2026_HUIT_COURS_AUDITE/sources/chapters/Q21/Q21_pop_esc_comparison.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/complements/glossary/i83.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/controles/diff_main.diff` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/controles/i83_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/controles/s01_browser_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-2/sources/chapters/I83/I83_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/complements/glossary/i83.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/controles/diff_main.diff` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/controles/i83_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/controles/s01_browser_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-3/sources/chapters/I83/I83_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/complements/glossary/i83.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/controles/diff_main.diff` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/controles/i83_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/controles/s01_browser_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-4/sources/chapters/I83/I83_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/complements/glossary/i83.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/controles/diff_main.diff` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/controles/i83_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/controles/s01_browser_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/rapport.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/sources/chapters/I83/I83_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/complements/glossary/i83.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/controles/diff_main.diff` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/controles/i83_native_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/controles/s01_browser_results.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-6/sources/chapters/I83/I83_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/complements/glossary/i83.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/controles/diff_main_8d6deee.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/controles/i83_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/controles/s01_browser_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION/sources/chapters/I83/I83_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/CORRECTIONS_AUDIT_CODEX.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/LIMITES_FERMEES.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/PREUVES_SOURCES_SUISSES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/PREUVE_AETHOXYSKLEROL_COMPRESSION.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_main_31b086a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_main_625fddb.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_main_e5bde2b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_main_ea105ac.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_main_v4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_results_v2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/i83_native_results_v3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/s01_attestation_v5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/s01_browser_branche.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/s01_browser_main_31b086a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/s01_browser_main_625fddb.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/s01_browser_main_v4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/s01_browser_main_v5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/simulation_main_31b086a_JOURNAL.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/simulation_main_e434eac_JOURNAL.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/simulation_main_e5bde2b_JOURNAL.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/simulation_main_e5bde2b_v2_JOURNAL.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/controles/simulation_main_ea105ac_JOURNAL.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/preuves/injection_intra_arterielle_extraits.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/preuves/ofsp_liste_specialites_20261001_veinotropes.ndjson` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/preuves/rapidocain_extraits.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/CORRECTIONS_AUDIT_CODEX.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/controles/diff_main.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/controles/i89_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/controles/s01_browser_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters.json` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/chapters/I89/I89_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/glossary/i89.py` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-2/sources/tests/verify_s01_browser.cjs` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/CORRECTIONS_AUDIT_CODEX_2.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/controles/diff_main.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/controles/i89_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/controles/s01_browser_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters.json` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/chapters/I89/I89_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/glossary/i89.py` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3/sources/tests/verify_s01_browser.cjs` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/controles/diff_main.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/controles/i89_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/controles/s01_browser_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters.json` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/chapters/I89/I89_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/glossary/i89.py` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/sources/tests/verify_s01_browser.cjs` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/PLAN.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/reserves_a.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/reserves_b.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/reserves_c.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/reserves_d.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/verification_ab.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89/verification/verification_cd.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I00/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/edits/I30_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/jobs/i30-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/out/i30-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/out/i30-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/out/i30-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/verdicts/I30_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I33/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I33/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I33/jobs/i33-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I33/out/i33-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I33/out/i33-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I33/out/i33-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I34/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I34/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I34/jobs/i34-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I34/out/i34-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I34/out/i34-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I34/out/i34-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/edits/I35_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/jobs/i35-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/out/i35-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/out/i35-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/out/i35-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/verdicts/I35_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/jobs/i40-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/out/i40-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/out/i40-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/out/i40-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/edits/I42_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/edits/I42_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/edits/I42_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/edits/I42_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/jobs/i42-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/out/i42-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/out/i42-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/out/i42-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/verdicts/I42_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/verdicts/I42_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/verdicts/I42_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42/verdicts/I42_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42_variante_main/LISEZMOI.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42_variante_main/jobs/i42-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42_variante_main/out/i42-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42_variante_main/out/i42-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I42_variante_main/out/i42-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/edits/I44_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/edits/I44_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/jobs/i44-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/out/i44-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/out/i44-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/out/i44-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/verdicts/I44_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/verdicts/I44_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/LEVEE_RESERVES.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/PROVENANCE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/Q21/PREUVES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/Q21/bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/Q21/jobs/q21-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/Q21/out/q21-esc-2026-comparaison__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/Q21/out/q21-esc-2026-comparaison__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/Q21/out/q21-esc-2026-comparaison__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/RECOMMANDATIONS_2026.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/TACHE_ESC2026.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/AVANCEMENT.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/CONSIGNES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-bpg-vagal__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-carditeinfra__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-crp-vs__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-d-bpg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-e-choree__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-e-souffle-ia__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-e-souffle-im__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-histoire__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-jones__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-mcisaac__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-mnemo-duree__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-pr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-strepto__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-v-fc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-v-fc__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-whf__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-bpg-vagal__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-bpg-vagal__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-bpg-vagal__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-carditeinfra__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-carditeinfra__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-carditeinfra__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-crp-vs__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-crp-vs__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-crp-vs__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-d-bpg__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-d-bpg__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-d-bpg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-choree__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-choree__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-choree__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-ia__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-ia__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-ia__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-im__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-im__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-im__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-histoire__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-histoire__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-histoire__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-jones__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-jones__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-jones__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mcisaac__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mcisaac__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mcisaac__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mnemo-duree__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mnemo-duree__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mnemo-duree__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-pr__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-pr__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-pr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-strepto__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-strepto__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-strepto__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-whf__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-whf__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-whf__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-bilan__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-cortdep__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-crit__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-crp__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-ains__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-antiil1__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-colch__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-cortico__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-ecg-stades__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-echo-tamp__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-grossesse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-mnemo-faste__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-neo__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-pcis__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-pericardectomie__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-ponction__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-purul__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-tb__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-bilan__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-bilan__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-bilan__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-cortdep__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-cortdep__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-cortdep__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crit__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crit__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crit__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crp__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crp__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crp__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-ains__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-ains__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-ains__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-antiil1__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-antiil1__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-antiil1__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-colch__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-colch__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-colch__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-cortico__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-cortico__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-cortico__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ecg-stades__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ecg-stades__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ecg-stades__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-echo-tamp__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-echo-tamp__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-echo-tamp__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-grossesse__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-grossesse__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-grossesse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-mnemo-faste__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-mnemo-faste__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-mnemo-faste__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-neo__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-neo__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-neo__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pcis__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pcis__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pcis__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pericardectomie__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pericardectomie__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pericardectomie__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ponction__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ponction__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ponction__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-purul__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-purul__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-purul__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-tb__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-tb__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-tb__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-atcd-valve__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-chir__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-coxiella__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-cefaz__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-ceftri__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-dapto__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-flucl__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-genta__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-lzd__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-pen__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-rif__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-vanco__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-deci__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-duke__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-eto__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-fongique__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-gallo__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-hacek__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-ic-aigue__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-iscvid__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-neuro-cat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-poet__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-prothese__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-risque-emb__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-roth__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-saureus__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-tep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-atcd-valve__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-atcd-valve__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-atcd-valve__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-chir__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-chir__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-chir__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-coxiella__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-coxiella__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-coxiella__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-cefaz__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-cefaz__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-cefaz__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-ceftri__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-ceftri__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-ceftri__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-dapto__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-dapto__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-dapto__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-flucl__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-flucl__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-flucl__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-genta__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-genta__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-genta__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-lzd__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-lzd__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-lzd__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-pen__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-pen__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-pen__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-rif__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-rif__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-rif__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-vanco__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-vanco__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-vanco__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-deci__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-deci__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-deci__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-duke__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-duke__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-duke__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-eto__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-eto__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-eto__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-fongique__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-fongique__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-fongique__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-gallo__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-gallo__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-gallo__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-hacek__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-hacek__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-hacek__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-ic-aigue__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-ic-aigue__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-ic-aigue__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-iscvid__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-iscvid__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-iscvid__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-neuro-cat__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-neuro-cat__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-neuro-cat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-poet__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-poet__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-poet__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-prothese__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-prothese__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-prothese__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-risque-emb__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-risque-emb__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-risque-emb__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-roth__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-roth__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-roth__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-saureus__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-saureus__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-saureus__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-tep__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-tep__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-tep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/src/dl.bin` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-anticoag-valve__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-avk-interact__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-congestion-renale__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-invictus__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-marqueurs-imp__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-marqueurs-imp__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-anticoag-valve__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-anticoag-valve__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-anticoag-valve__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-avk-interact__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-avk-interact__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-avk-interact__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-congestion-renale__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-congestion-renale__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-congestion-renale__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-invictus__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-invictus__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-invictus__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/src/esc2025.pdf` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-bernoulli__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-calcif__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-chirnc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-choix-tech__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-aod-meca__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-asa__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-benza__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-hep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-inotrope__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-nitroprus__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-discord__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-dissection__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-dse__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-effort__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-grossesse__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-inr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-lflg-parad__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-manoeuvres__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-pacemaker__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-prothese__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-ra-asympto__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-seuils-aorte__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-suivi__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-bernoulli__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-bernoulli__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-bernoulli__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-calcif__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-calcif__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-calcif__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-chirnc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-chirnc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-chirnc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-choix-tech__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-choix-tech__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-choix-tech__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-aod-meca__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-aod-meca__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-aod-meca__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-asa__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-asa__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-asa__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-benza__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-benza__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-benza__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-hep__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-hep__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-hep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-inotrope__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-inotrope__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-inotrope__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-nitroprus__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-nitroprus__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-nitroprus__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-discord__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-discord__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-discord__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dissection__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dissection__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dissection__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dse__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dse__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dse__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-effort__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-effort__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-effort__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-grossesse__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-grossesse__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-grossesse__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-inr__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-inr__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-inr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-lflg-parad__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-lflg-parad__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-lflg-parad__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-manoeuvres__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-manoeuvres__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-manoeuvres__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-pacemaker__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-pacemaker__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-pacemaker__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-prothese__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-prothese__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-prothese__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-ra-asympto__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-ra-asympto__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-ra-asympto__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-seuils-aorte__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-seuils-aorte__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-seuils-aorte__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-suivi__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-suivi__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-suivi__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/src/esc2025_vhd.pdf` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-arythmies__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-b19__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-chagas-stades__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-clozapine__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-covid__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-2l__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-aza__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-bnz__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-cni__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-cortico__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-dallas__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-ecg__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-ecmo__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-eos__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-fulm-prono__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-gcm__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-genet__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-hstn__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-irm-signal__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-is-virus__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-lyme__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-mnemo-bach__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-risque__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-s-muscle__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-sport__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-strongy__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-triplem__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-wcd__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-arythmies__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-arythmies__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-arythmies__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-b19__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-b19__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-b19__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-chagas-stades__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-chagas-stades__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-chagas-stades__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-clozapine__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-clozapine__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-clozapine__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-covid__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-covid__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-covid__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-2l__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-2l__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-2l__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-aza__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-aza__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-aza__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-bnz__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-bnz__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-bnz__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cni__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cni__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cni__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cortico__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cortico__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cortico__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-dallas__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-dallas__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-dallas__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecg__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecg__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecg__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecmo__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecmo__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecmo__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-eos__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-eos__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-eos__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-fulm-prono__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-fulm-prono__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-fulm-prono__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-gcm__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-gcm__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-gcm__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-genet__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-genet__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-genet__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-hstn__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-hstn__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-hstn__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-irm-signal__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-irm-signal__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-irm-signal__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-is-virus__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-is-virus__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-is-virus__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-lyme__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-lyme__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-lyme__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-mnemo-bach__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-mnemo-bach__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-mnemo-bach__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-risque__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-risque__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-risque__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-s-muscle__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-s-muscle__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-s-muscle__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-sport__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-sport__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-sport__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-strongy__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-strongy__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-strongy__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-triplem__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-triplem__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-triplem__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-wcd__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-wcd__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-wcd__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-anticoag-fa__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-attr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-biomarq__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-cicatrice__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-fa__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-pk-myosine__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-redflags__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-stades__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-takotsubo__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-anticoag-fa__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-anticoag-fa__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-anticoag-fa__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-attr__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-attr__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-attr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-biomarq__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-biomarq__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-biomarq__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-cicatrice__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-cicatrice__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-cicatrice__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-fa__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-fa__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-fa__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-pk-myosine__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-pk-myosine__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-pk-myosine__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-redflags__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-redflags__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-redflags__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-stades__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-stades__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-stades__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-takotsubo__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-takotsubo__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-takotsubo__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-athlete__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-atropine-test__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-automat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-bbd__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-bilan-bio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-d-fab__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-d-insuline__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-d-theo__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-digitox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-echap__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-eep__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-fa-infra__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-hautdeg__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-hemodyn__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-hypothyr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-imag__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-irm__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-mob1__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-neuromusc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-rvpace__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-sync-strat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-tox__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-athlete__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-athlete__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-athlete__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-atropine-test__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-atropine-test__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-atropine-test__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-automat__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-automat__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-automat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bbd__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bbd__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bbd__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bilan-bio__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bilan-bio__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bilan-bio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-fab__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-fab__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-fab__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-insuline__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-insuline__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-insuline__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-theo__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-theo__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-theo__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-digitox__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-digitox__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-digitox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-echap__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-echap__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-echap__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-eep__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-eep__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-eep__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-fa-infra__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-fa-infra__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-fa-infra__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hautdeg__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hautdeg__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hautdeg__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hemodyn__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hemodyn__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hemodyn__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hypothyr__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hypothyr__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hypothyr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-imag__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-imag__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-imag__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-irm__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-irm__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-irm__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-mob1__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-mob1__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-mob1__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-neuromusc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-neuromusc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-neuromusc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-rvpace__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-rvpace__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-rvpace__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-sync-strat__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-sync-strat__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-sync-strat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-tox__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-tox__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-tox__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-anaph__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-atcd-medic__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-coro__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-adre__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-antiep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-bicar__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-lipid__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-lyse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-nalox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-vaso__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-enfant__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-ep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-grossesse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-hyperk__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-hypoth__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-inexpl__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-intox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-neuro__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-pnothx__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-ppc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-pronostic__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-s-temoin__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-temp__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-anaph__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-anaph__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-anaph__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-atcd-medic__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-atcd-medic__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-atcd-medic__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-coro__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-coro__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-coro__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-adre__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-adre__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-adre__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-antiep__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-antiep__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-antiep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-bicar__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-bicar__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-bicar__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lipid__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lipid__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lipid__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lyse__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lyse__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lyse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-nalox__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-nalox__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-nalox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-vaso__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-vaso__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-vaso__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-enfant__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-enfant__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-enfant__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ep__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ep__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-grossesse__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-grossesse__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-grossesse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hyperk__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hyperk__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hyperk__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hypoth__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hypoth__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hypoth__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-inexpl__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-inexpl__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-inexpl__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-intox__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-intox__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-intox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-neuro__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-neuro__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-neuro__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pnothx__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pnothx__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pnothx__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ppc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ppc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ppc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pronostic__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pronostic__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pronostic__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-s-temoin__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-s-temoin__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-s-temoin__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-temp__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-temp__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-temp__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verdicts/I46_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-abl-tsv__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-adeno__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-ajmaline__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-atcd-medic__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-automat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-bilan-tv__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-brugada__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-cicatrice__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-credible__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-cv__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-amio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-bb__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-bbns__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-cci__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-ic__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-mg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-sotalol__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-dai__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-declench__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-digox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-dualite__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-ecg-brug__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-ecg-qt__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-eep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-effort__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-genet__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-grossesse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-holter__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-irm__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-k__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-mg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-msj__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-orage__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-pa__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-qtl__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-reentree__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-repol__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-reppre__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-schwartz__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-sport__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-standing__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-tamsi__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-tdp-tt__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-tolerance__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-trav__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-wpw-asympt__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-abl-tsv__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-abl-tsv__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-abl-tsv__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-adeno__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-adeno__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-adeno__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ajmaline__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ajmaline__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ajmaline__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-atcd-medic__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-atcd-medic__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-atcd-medic__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-automat__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-automat__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-automat__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-bilan-tv__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-bilan-tv__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-bilan-tv__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-brugada__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-brugada__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-brugada__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cicatrice__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cicatrice__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cicatrice__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-credible__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-credible__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-credible__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cv__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cv__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cv__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-amio__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-amio__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-amio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bb__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bb__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bb__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bbns__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bbns__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bbns__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-cci__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-cci__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-cci__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-ic__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-ic__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-ic__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-mg__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-mg__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-mg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-sotalol__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-sotalol__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-sotalol__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dai__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dai__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dai__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-declench__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-declench__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-declench__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-digox__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-digox__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-digox__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dualite__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dualite__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dualite__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-brug__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-brug__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-brug__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-qt__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-qt__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-qt__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-eep__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-eep__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-eep__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-effort__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-effort__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-effort__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-genet__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-genet__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-genet__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-grossesse__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-grossesse__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-grossesse__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-holter__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-holter__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-holter__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-irm__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-irm__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-irm__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-k__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-k__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-k__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-mg__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-mg__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-mg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-msj__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-msj__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-msj__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-orage__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-orage__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-orage__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-pa__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-pa__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-pa__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-qtl__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-qtl__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-qtl__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reentree__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reentree__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reentree__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-repol__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-repol__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-repol__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reppre__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reppre__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reppre__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-schwartz__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-schwartz__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-schwartz__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-sport__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-sport__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-sport__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-standing__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-standing__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-standing__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tamsi__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tamsi__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tamsi__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tdp-tt__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tdp-tt__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tdp-tt__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tolerance__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tolerance__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tolerance__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-trav__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-trav__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-trav__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-wpw-asympt__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-wpw-asympt__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-wpw-asympt__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verdicts/I47_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-ablation__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-atcd-psy__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-atcd-subst__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-bilan-bio__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-bilan-bio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-cmie-crit__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-cmie-meca__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-commotio__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-couplage__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-crt__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-declench__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-e-auscult__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-ecg-base__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-effort__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-epi__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-erc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-erc__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-essa__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-pots-phys__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-pots-tt__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-prono__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-pvm__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-riva__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-rja__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-rosc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-standing__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-termino__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ablation__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ablation__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ablation__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-psy__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-psy__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-psy__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-subst__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-subst__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-subst__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-crit__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-crit__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-crit__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-meca__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-meca__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-meca__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-commotio__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-commotio__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-commotio__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-couplage__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-couplage__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-couplage__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-crt__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-crt__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-crt__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-declench__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-declench__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-declench__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-e-auscult__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-e-auscult__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-e-auscult__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ecg-base__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ecg-base__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ecg-base__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-effort__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-effort__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-effort__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-epi__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-epi__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-epi__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-essa__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-essa__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-essa__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-phys__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-phys__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-phys__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-tt__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-tt__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-tt__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-prono__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-prono__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-prono__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pvm__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pvm__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pvm__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-riva__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-riva__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-riva__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rja__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rja__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rja__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rosc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rosc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rosc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-standing__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-standing__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-standing__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-termino__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-termino__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-termino__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verdicts/I49_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_pop.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-addrs__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-anti-impulsion__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-antithrombotiques__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-aortopathie-traitement__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-depistage__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-diam__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-endofuites__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-gen__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-genetique-interpretation__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-paroi__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-seuils-thorax__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-addrs__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-addrs__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-addrs__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-anti-impulsion__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-anti-impulsion__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-anti-impulsion__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-antithrombotiques__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-antithrombotiques__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-antithrombotiques__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-aortopathie-traitement__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-aortopathie-traitement__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-aortopathie-traitement__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-depistage__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-depistage__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-depistage__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-diam__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-diam__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-diam__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-endofuites__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-endofuites__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-endofuites__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-gen__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-gen__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-gen__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-genetique-interpretation__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-genetique-interpretation__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-genetique-interpretation__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-paroi__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-paroi__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-paroi__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-seuils-thorax__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-seuils-thorax__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-seuils-thorax__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/verdicts/I71_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/verdicts/I71_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/verdicts/I71_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/verdicts/I71_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/verdicts/I71_pop.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_pop.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-antidotes__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-ddimeres__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-doses__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-duree__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-ep__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-fibrinolyse__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-phlegmatia__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-pompe__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-signes__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-test-thrombophilie__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-tih__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-virchow__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-wells__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-antidotes__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-antidotes__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-antidotes__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ddimeres__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ddimeres__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ddimeres__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-doses__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-doses__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-doses__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-duree__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-duree__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-duree__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ep__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ep__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ep__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-fibrinolyse__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-fibrinolyse__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-fibrinolyse__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-phlegmatia__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-phlegmatia__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-phlegmatia__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-pompe__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-pompe__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-pompe__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-signes__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-signes__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-signes__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-test-thrombophilie__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-test-thrombophilie__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-test-thrombophilie__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-tih__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-tih__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-tih__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-virchow__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-virchow__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-virchow__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-wells__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-wells__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-wells__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/verdicts/I80_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/verdicts/I80_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/verdicts/I80_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/verdicts/I80_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/verdicts/I80_pop.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/bilan_P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/bilan_P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop7.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-arythmie__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-chirnc__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-cyan-sys__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-d-amio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-d-anticoag__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-ecg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-endoc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-heath__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-mwho__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-rope__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-rx__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-sport__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-switch-atr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-transition__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-arythmie__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-arythmie__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-arythmie__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-chirnc__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-chirnc__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-chirnc__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-cyan-sys__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-cyan-sys__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-cyan-sys__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-amio__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-amio__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-amio__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-anticoag__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-anticoag__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-anticoag__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-ecg__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-ecg__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-ecg__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-endoc__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-endoc__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-endoc__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-heath__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-heath__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-heath__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-mwho__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-mwho__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-mwho__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rope__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rope__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rope__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rx__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rx__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rx__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-sport__P2.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-sport__P2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-sport__P2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-switch-atr__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-switch-atr__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-switch-atr__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-transition__P1.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-transition__P1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-transition__P1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop5.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop6.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verdicts/Q21_pop7.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/verification.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/TACHE_PRODUCTION.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/appliquer_justifications.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/finaliser.sh` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/manifeste.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/verifier_sigles.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/CONSIGNES_8_OCTOBRE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/PLAN.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_a.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_b.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_c.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_d.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_pop1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_pop2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_pop3.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/I83_pop4.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/brouillon/SOURCES_D.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/glossary_i83.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/glossary_i83_a.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/glossary_i83_c.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/glossary_i83_d.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/verification_ab.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83/verification_cd.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/PLAN.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_a.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_b.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_c.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_d.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_pop1.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_pop2.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_pop3.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/I89_pop4.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/reserves_a.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/reserves_b.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/reserves_c.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/brouillon/reserves_d.txt` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_a.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_b.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_c.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_d.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_final.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_verif_ab.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/glossary_i89_verif_cd.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/verification_ab.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89/verification_cd.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/TACHE_NOUVEAU_COURS.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/I-03-Infectiologie/audits/A41-39b7ff0/CONSIGNE_AUDIT.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/I-03-Infectiologie/audits/A41-39b7ff0/RAPPORT.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/I-03-Infectiologie/audits/A41-39b7ff0/audit_examens_sciences_pharmacologie.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/I-03-Infectiologie/audits/A41-39b7ff0/audit_pathologie_1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/I-03-Infectiologie/audits/A41-39b7ff0/audit_pathologie_2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/controles/diff_main.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/controles/j45_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_d.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_pop1.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_pop2.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_pop3.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/sources/chapters/J45/J45_pop4.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/verification/corrections_codex_1.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-2/verification/corrections_codex_1b.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/controles/diff_main.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/controles/j45_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_d.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_pop1.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_pop2.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_pop3.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/sources/chapters/J45/J45_pop4.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45-3/verification/corrections_codex_2.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/controles/diff_main.diff` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/controles/j45_native_results.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_d.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_pop1.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_pop2.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_pop3.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/sources/chapters/J45/J45_pop4.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/assemblage.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/examens.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/pathologie.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/pathologie_propositions.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/pharmacologie.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/sciences.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/lots/2026-10-08-J45/verification/verification.md` | delivery_report | GLOBAL | pull_request_base |
| `tests/verify_s01_browser.cjs` | integration_source | GLOBAL | pull_request_base |
| `tools/compendium_fi.cjs` | integration_source | GLOBAL | pull_request_base |
| `tools/compendium_zones.py` | integration_source | GLOBAL | pull_request_base |
| `tools/veille_collaboration.py` | integration_source | GLOBAL | pull_request_base |

## codex/a41-corrections-20261008

- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- Cours absent de chapters.json de la cible ; déclaration à intégrer.
- S01 : le cours doit figurer exactement une fois dans categories[].chapters.
- Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction.
- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Diff de branche potentiellement tronqué ; consulter tous les fichiers de la PR ou un diff Git local.
- PR #15 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/claude_watch.yml` | integration_source | GLOBAL | integration_target |
| `AGENTS.md` | documentation | GLOBAL | integration_target |
| `CLAUDE.md` | documentation | GLOBAL | integration_target |
| `audits/CHAINE_FRAGMENTS_2026-10-08/VALIDATION.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-07/README.md` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/BUILD_STATIC_UNIT.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/CONVERGENCE_MAIN_E027.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/QA_APRES_8CE.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/SCIENCES.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/categories/categories_results.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/i48_native/i48_justifications_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I46/i46_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I47/i47_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I49/i49_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I71/i71_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I80/i80_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/Q21/q21_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/sciences_cs/science-cs-browser-results.json` | review_report | S01, CS | integration_target |
| `chapters.json` | registration_source | GLOBAL | integration_target |
| `chapters/I46/I46_a.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_b.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_c.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_d.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop1.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop2.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop3.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop4.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop5.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_a.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_b.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_c.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_d.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop1.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop2.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop3.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop4.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop5.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop6.html` | course_source | S01 | integration_target |
| `chapters/I48/I48_pop3.html` | course_source | S01 | integration_target |
| `chapters/I48/I48_pop4.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_a.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_b.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_c.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_d.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop1.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop2.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop3.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop4.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop5.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_a.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_b.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_c.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_d.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_pop.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_pop_sciences.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_a.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_b.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_c.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_d.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_pop.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_pop_sciences.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_a.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_b.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_c.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_d.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop1.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop2.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop3.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop4.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_a.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_b.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_c.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_d.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop1.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop2.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop3.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop4.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop5.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop6.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop7.html` | course_source | S01 | integration_target |
| `docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/DELIVERIES_LATEST.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/DELIVERY_PROTOCOL.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.html` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/FILE_AUDIT_CODEX.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/FRAGMENTS_RESTANTS.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/README.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/REGLES_INJECTION_CLAUDE.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/SIGNAUX_CODEX.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_20261008_RECEPTION.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_3F90204_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_A0B0204_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC_4C8C534_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC_7C6FC65_CORRECTIONS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I35_2145A2A_RENAL_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_0974D85_RAPIDOCAIN_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_205D2CB_HARMONISATION_3_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_20BEE19_CONSERVATEURS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_20C67C0_PH02_INTRAARTERIELLE_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6B76E12_LIMITES_V4_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6D5797C_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6D5797C_RAPIDOCAIN_PRESENTATIONS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_8A6DC7F_HARMONISATION_6_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_8A6DC7F_HARMONISATION_6_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_A41_5BEE2A4_RECEPTION_2026-10-07.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_B526D9D_HARMONISATION_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_B983CB6_ATTESTATION_SOURCES_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_CDD2B72_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D2A460F_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D5B46AA_HARMONISATION_5_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D5B46AA_HARMONISATION_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D6178B5_HARMONISATION_2_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D94B11F_MAIN31B_PROOFS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_DECEF42_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E17107A_HARMONISATION_4_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E2C023C_COMPLEMENT_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E2C023C_INTRAARTERIELLE_STATUT_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_ESC_BE58AD9_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I89_04CB957_I89_3_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I89_7775E6E_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I89_DE67651_I89_2_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_J45_9AA6504_J45_3_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_J45_C3DD8CD_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_J45_F30B891_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_PACKET_S01_20261007T225829714502Z.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_PR12_8CE3E99_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CODEX_A41_E330776_REMIS_CLAUDE_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/A41_HASH_VERIFICATION.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/AUDIT_MEDICAL_I83.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/AUDIT_TECHNIQUE_I83.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_AUDIT_A41.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_DISTANT.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_DISTANT.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_TECHNIQUE_I83.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/ORIGINAUX_PROVENANCE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/RECEPTION.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/ACCUSE_RECEPTION_PR12.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/APPLICATION_CONSIGNES_DENSITE_SOURCES.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/APPLICATION_CONSIGNES_DENSITE_SOURCES.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/BASE_DISTANTE_ACTUALISEE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/BASE_ET_OBSERVATIONS.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/COMPLEMENT_NORMES_ARTERIELLES.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/COMPLEMENT_NORMES_ARTERIELLES.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/COMPLEMENT_PCT.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/COMPLEMENT_PCT.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_EXAMENS_SCIENCES.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_EXAMENS_SCIENCES.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_GLOSSAIRE_BANQUE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_GLOSSAIRE_BANQUE.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_PATHOLOGIE1.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_PATHOLOGIE1.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_PATHOLOGIE2.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_PATHOLOGIE2.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_PHARMACOLOGIE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTRELECTURE_PHARMACOLOGIE.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTROLES_COPIES.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTROLE_TECHNIQUE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/CONTROLE_TECHNIQUE.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/ETAT_FILE_AUDIT_POST_INJECTION.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/ETAT_FILE_AUDIT_POST_INJECTION.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/EXAMENS_SCIENCES.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/EXAMENS_SCIENCES.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/GEL_SOURCES_FINAL.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/GLOSSAIRE_BANQUE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/GLOSSAIRE_BANQUE.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/NORMES_GAZOMETRIE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/NORMES_GAZOMETRIE.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/NOTIFICATION_REGLES_I83.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/PATHOLOGIE1.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/PATHOLOGIE1.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/PATHOLOGIE2.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/PATHOLOGIE2.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/PHARMACOLOGIE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/PHARMACOLOGIE.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/RECEPTION.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/RECEPTION.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/REPARTITION_CATEGORIES_ET_SUJETS.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/SOURCES_TRANSVERSALES.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/SOURCES_TRANSVERSALES.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/SYNTHESE_75_OBSERVATIONS.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/SYNTHESE_75_OBSERVATIONS.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/bank-a41-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/bank-a41.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/bank-a41.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/bank-a41.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/baseline-comparison.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/global-browser-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/global-browser.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/global-network.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/native-a41-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/native-a41.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/native-a41/failed_a41_native_results.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/run-one.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/t1-browser-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/t1-browser.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/browser-attempt1-long-temp-path/t1-browser.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/build-global-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/build-global.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/build-t1-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/build-t1.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/compiled-sigles-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/compiled-sigles.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/compiled-sigles.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/compiled-sigles.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/global-browser-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/global-browser.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/global-http.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/global-network.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/gloss-sigles-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/gloss-sigles.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/gloss-sigles.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/gloss-sigles.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/helper-attempt1/compiled-sigles-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/helper-attempt1/compiled-sigles.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/helper-attempt1/compiled-sigles.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/http-preload.cjs` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/native-a41-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/native-a41.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/native-a41/a41_native_results.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/native-a41/failed_a41_native_results.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/native-a41/transport.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/run-one.py` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/source-inspection.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/static-a41-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/static-a41.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/t1-browser-command.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/t1-browser.cjs` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/t1-browser.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/t1-browser.log` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/controles_final/t1-browser/transport.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/CORRECTIONS_I46_I47_I49.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/CORRECTIONS_I71_I80_Q21.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/FUSION_I48.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/HARMONISATION_REFERENCES_PROSE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/INJECTION_MANIFEST.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/INJECTION_RECONCILIATION.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I46_I47_I49.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I48.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I71_I80_Q21.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/STRUCTURE_I71_I80_Q21.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/original/glossary_q21.py` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/AUDIT_JAUGES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_DASHBOARD.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C_ROUTES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DELTA_E2C023C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT_E2.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT_E2.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/FRAGMENTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/FRAGMENTS_METHODE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/TACHES_MAJEURES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/TACHES_METHODE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_CATEGORIES_S01.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_INVENTAIRE_S01.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_S01_HISTORIQUE.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_DIFFERENCES_COPIES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_DELTA_20BEE19.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_PERIMETRE_MAIN.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_ARTEFACTS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_COMMANDES_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_LOGS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_NATIFS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_RESEAU_CANONIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_ROUTES_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/DEMANDE_LECTURE_CROISEE_CLAUDE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_a.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_b.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_c.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_d.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_justifications.json` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_pop1.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_pop2.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_pop_pa.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/chapters/A41/A41_pop_sciences_revision.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/glossary/a41.py` | delivery_source | GLOBAL | pull_request_base |

## codex/accueil-qcm-20260929

- PR #6 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/pages.yml` | integration_source | GLOBAL | integration_target |
| `CLAUDE.md` | documentation | GLOBAL | integration_target |
| `build_index.py` | integration_source | GLOBAL | integration_target |
| `docs/QCM_MEDINA.md` | documentation | GLOBAL | integration_target |
| `site/index_template.html` | consultation_source | GLOBAL | integration_target |
| `site/qcm.html` | consultation_source | GLOBAL | integration_target |

## codex/decision-i83-20261008

- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- Cours absent de chapters.json de la cible ; déclaration à intégrer.
- S01 : le cours doit figurer exactement une fois dans categories[].chapters.
- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction.
- Diff de branche potentiellement tronqué ; consulter tous les fichiers de la PR ou un diff Git local.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/claude_watch.yml` | integration_source | GLOBAL | integration_target |
| `AGENTS.md` | documentation | GLOBAL | integration_target |
| `CLAUDE.md` | documentation | GLOBAL | integration_target |
| `audits/CHAINE_FRAGMENTS_2026-10-08/VALIDATION.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-07/README.md` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/BUILD_STATIC_UNIT.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/CONVERGENCE_MAIN_E027.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/QA_APRES_8CE.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/SCIENCES.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/categories/categories_results.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/i48_native/i48_justifications_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I46/i46_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I47/i47_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I49/i49_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I71/i71_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I80/i80_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/Q21/q21_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/sciences_cs/science-cs-browser-results.json` | review_report | S01, CS | integration_target |
| `chapters.json` | registration_source | GLOBAL | integration_target |
| `chapters/I46/I46_a.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_b.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_c.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_d.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop1.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop2.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop3.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop4.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop5.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_a.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_b.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_c.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_d.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop1.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop2.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop3.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop4.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop5.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop6.html` | course_source | S01 | integration_target |
| `chapters/I48/I48_pop3.html` | course_source | S01 | integration_target |
| `chapters/I48/I48_pop4.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_a.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_b.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_c.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_d.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop1.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop2.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop3.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop4.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop5.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_a.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_b.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_c.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_d.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_pop.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_pop_sciences.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_a.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_b.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_c.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_d.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_pop.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_pop_sciences.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_a.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_b.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_c.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_d.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop1.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop2.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop3.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop4.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_a.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_b.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_c.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_d.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop1.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop2.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop3.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop4.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop5.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop6.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop7.html` | course_source | S01 | integration_target |
| `docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/DELIVERIES_LATEST.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.html` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/FRAGMENTS_RESTANTS.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/README.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/SIGNAUX_CODEX.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_20261008_RECEPTION.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_3F90204_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_A0B0204_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC_4C8C534_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC_7C6FC65_CORRECTIONS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I35_2145A2A_RENAL_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_0974D85_RAPIDOCAIN_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_20BEE19_CONSERVATEURS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_20C67C0_PH02_INTRAARTERIELLE_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6B76E12_LIMITES_V4_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6D5797C_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6D5797C_RAPIDOCAIN_PRESENTATIONS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_A41_5BEE2A4_RECEPTION_2026-10-07.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_B983CB6_ATTESTATION_SOURCES_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_CDD2B72_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D2A460F_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D94B11F_MAIN31B_PROOFS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_DECEF42_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E2C023C_COMPLEMENT_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E2C023C_INTRAARTERIELLE_STATUT_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_ESC_BE58AD9_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_PACKET_S01_20261007T225829714502Z.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_PR12_8CE3E99_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/A41_HASH_VERIFICATION.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/AUDIT_MEDICAL_I83.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/AUDIT_TECHNIQUE_I83.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_AUDIT_A41.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_DISTANT.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_DISTANT.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_TECHNIQUE_I83.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/ORIGINAUX_PROVENANCE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/RECEPTION.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/CORRECTIONS_I46_I47_I49.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/CORRECTIONS_I71_I80_Q21.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/FUSION_I48.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/HARMONISATION_REFERENCES_PROSE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/INJECTION_MANIFEST.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/INJECTION_RECONCILIATION.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I46_I47_I49.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I48.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I71_I80_Q21.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/STRUCTURE_I71_I80_Q21.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/original/glossary_q21.py` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/AUDIT_JAUGES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_DASHBOARD.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C_ROUTES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DELTA_E2C023C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT_E2.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT_E2.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/FRAGMENTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/FRAGMENTS_METHODE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/TACHES_MAJEURES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/TACHES_METHODE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_CATEGORIES_S01.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_INVENTAIRE_S01.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_S01_HISTORIQUE.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_DIFFERENCES_COPIES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_DELTA_20BEE19.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_PERIMETRE_MAIN.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_ARTEFACTS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_COMMANDES_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_LOGS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_NATIFS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_RESEAU_CANONIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_ROUTES_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_S01_CANONIQUE.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_PATHOLOGIE_EXAMENS.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_PHARMACOLOGIE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_SCIENCES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_TECHNIQUE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_20BEE19.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_20C67C0.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_CANONIQUES_6D5797C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_INDEPENDANTS.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_UNITAIRES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DECISION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_20BEE19_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_20C67C0_PHARMACOLOGIE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_20C67C0_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_6D5797C_PHARMACOLOGIE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_6D5797C_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/ENVIRONNEMENT_SOURCES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/INJECTION_LOCALE_6D5797C.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/INVENTAIRE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/INVENTAIRE_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/PREUVE_AETHOXYSKLEROL_COMPRESSION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/injection_intra_arterielle_extraits.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/rapidocain_extraits.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/rapport.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PROTOCOLE_CONTROLES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/VEILLE_RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_0974D85_I83_RAPIDOCAIN/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_20BEE19_I83_CONSERVATEURS_CONTROLES/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_20C67C0_I83_PH02_INTRAARTERIELLE/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_2145A2A_I35_RENAL/RECEPTION.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_4C8C534_ESC_RAPPORTS_CONTROLES/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_6B76E12_I83_LIMITES_V4/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_6D5797C_I83_RAPIDOCAIN_PRESENTATIONS/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_7C6FC65_ESC_CORRECTIONS/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_B983CB6_I83_ATTESTATION_SOURCES/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_BE58AD9_I83_ESC_CONTROLS/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_CDD2B72_I83_COMPRESSION/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_D2A460F_I83_SIMULATION_MAIN/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_D94B11F_I83_MAIN31B_PROOFS/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_DECEF42_I83_PREUVE_CONTROLE/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_E2C023C_I83_INTRAARTERIELLE_STATUT/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_ESC2026_A0B0204/INVENTAIRE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/PR12_ESC2026_A0B0204/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/AUDIT_MEDICAL.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/AUDIT_TECHNIQUE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/RECEPTION_ACTUALISEE.md` | review_report | GLOBAL | integration_target |
| `glossary/fragments_medina.py` | glossary_source | GLOBAL | integration_target |
| `glossary/i83.py` | glossary_source | GLOBAL | integration_target |
| `glossary/q21.py` | glossary_source | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/RECEPTION.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/RECEPTION.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I00/I00_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I30/I30_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I33/I33_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I34/I34_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I35/I35_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I40/I40_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I42/I42_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_8CE3E99_RECEPTION/sources/chapters/I42/I42_b.html` | delivery_source | S01 | integration_target |

## codex/transition-cardio-20261008


| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `docs/collaboration/TRANSITION_CODEX_2026-10-08.md` | documentation | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/PRODUCTION_CARDIO_2026-10-08/I73.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/PRODUCTION_CARDIO_2026-10-08/I73_CONTRELECTURE.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/PRODUCTION_CARDIO_2026-10-08/I95.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/PRODUCTION_CARDIO_2026-10-08/I95_CONTRELECTURE.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/REPRISE_FINALE_2026-10-08/ADAPTATIONS_INTEGRATEUR.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/REPRISE_FINALE_2026-10-08/CONTRELECTURE_RYTHME.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/audits/REPRISE_FINALE_2026-10-08/CONTRELECTURE_VASCULAIRE_CONGENITAL.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I73/I73_a.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I73/I73_b.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I73/I73_c.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I73/I73_d.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I73/I73_pop1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I95/I95_a.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I95/I95_b.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I95/I95_c.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I95/I95_d.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/chapters/I95/I95_pop.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/docs/collaboration/NEW_COURSE_DELIVERY.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/docs/collaboration/PRODUCTION_CARDIO_CLAUDE_2026-10-08.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/glossary/i73.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/glossary/i95.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/tests/test_new_course_delivery.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/tools/new_course_delivery.py` | delivery_report | GLOBAL | integration_target |

## main

- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- Cours absent de chapters.json de la cible ; déclaration à intégrer.
- S01 : le cours doit figurer exactement une fois dans categories[].chapters.
- Diff de branche potentiellement tronqué ; consulter tous les fichiers de la PR ou un diff Git local.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/claude_watch.yml` | integration_source | GLOBAL | integration_target |
| `AGENTS.md` | documentation | GLOBAL | integration_target |
| `CLAUDE.md` | documentation | GLOBAL | integration_target |
| `audits/CHAINE_FRAGMENTS_2026-10-08/VALIDATION.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-07/README.md` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/BUILD_STATIC_UNIT.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/CONVERGENCE_MAIN_E027.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/QA_APRES_8CE.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/SCIENCES.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/categories/categories_results.json` | review_report | GLOBAL | integration_target |
| `audits/MECANISMES_2026-10-08/i48_native/i48_justifications_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I46/i46_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I47/i47_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I49/i49_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I71/i71_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/I80/i80_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/native/Q21/q21_native_results.json` | review_report | S01 | integration_target |
| `audits/MECANISMES_2026-10-08/sciences_cs/science-cs-browser-results.json` | review_report | S01, CS | integration_target |
| `chapters.json` | registration_source | GLOBAL | integration_target |
| `chapters/I46/I46_a.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_b.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_c.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_d.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop1.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop2.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop3.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop4.html` | course_source | S01 | integration_target |
| `chapters/I46/I46_pop5.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_a.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_b.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_c.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_d.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop1.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop2.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop3.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop4.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop5.html` | course_source | S01 | integration_target |
| `chapters/I47/I47_pop6.html` | course_source | S01 | integration_target |
| `chapters/I48/I48_pop3.html` | course_source | S01 | integration_target |
| `chapters/I48/I48_pop4.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_a.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_b.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_c.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_d.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop1.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop2.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop3.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop4.html` | course_source | S01 | integration_target |
| `chapters/I49/I49_pop5.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_a.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_b.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_c.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_d.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_pop.html` | course_source | S01 | integration_target |
| `chapters/I71/I71_pop_sciences.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_a.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_b.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_c.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_d.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_pop.html` | course_source | S01 | integration_target |
| `chapters/I80/I80_pop_sciences.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_a.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_b.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_c.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_d.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop1.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop2.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop3.html` | course_source | S01 | integration_target |
| `chapters/I83/I83_pop4.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_a.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_b.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_c.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_d.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop1.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop2.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop3.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop4.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop5.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop6.html` | course_source | S01 | integration_target |
| `chapters/Q21/Q21_pop7.html` | course_source | S01 | integration_target |
| `docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/DELIVERIES_LATEST.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/DELIVERY_PROTOCOL.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.html` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/ETAT_DES_LIEUX_2026-10-08.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/FILE_AUDIT_CODEX.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/FRAGMENTS_RESTANTS.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/README.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/REGLES_INJECTION_CLAUDE.md` | documentation | GLOBAL | integration_target |
| `docs/collaboration/SIGNAUX_CODEX.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_20261008_RECEPTION.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_3F90204_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC2026_A0B0204_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC_4C8C534_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_ESC_7C6FC65_CORRECTIONS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I35_2145A2A_RENAL_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_0974D85_RAPIDOCAIN_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_205D2CB_HARMONISATION_3_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_20BEE19_CONSERVATEURS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_20C67C0_PH02_INTRAARTERIELLE_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6B76E12_LIMITES_V4_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6D5797C_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_6D5797C_RAPIDOCAIN_PRESENTATIONS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_8A6DC7F_HARMONISATION_6_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_8A6DC7F_HARMONISATION_6_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_A41_5BEE2A4_RECEPTION_2026-10-07.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_B526D9D_HARMONISATION_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_B983CB6_ATTESTATION_SOURCES_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_CDD2B72_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D2A460F_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D5B46AA_HARMONISATION_5_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D5B46AA_HARMONISATION_INTEGRATION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D6178B5_HARMONISATION_2_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_D94B11F_MAIN31B_PROOFS_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_DECEF42_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E17107A_HARMONISATION_4_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E2C023C_COMPLEMENT_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_E2C023C_INTRAARTERIELLE_STATUT_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I83_ESC_BE58AD9_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I89_04CB957_I89_3_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I89_7775E6E_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_I89_DE67651_I89_2_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_J45_9AA6504_J45_3_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_J45_C3DD8CD_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_J45_F30B891_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_PACKET_S01_20261007T225829714502Z.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CLAUDE_PR12_8CE3E99_RECEPTION_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/receipts/CODEX_A41_E330776_REMIS_CLAUDE_2026-10-08.json` | documentation | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/A41_HASH_VERIFICATION.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/AUDIT_MEDICAL_I83.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/AUDIT_TECHNIQUE_I83.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_AUDIT_A41.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_DISTANT.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_DISTANT.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/INVENTAIRE_TECHNIQUE_I83.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/ORIGINAUX_PROVENANCE.json` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-07/PR12_I83_A41_5BEE2A4/RECEPTION.md` | review_report | T1 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/CORRECTIONS_I46_I47_I49.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/CORRECTIONS_I71_I80_Q21.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/FUSION_I48.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/HARMONISATION_REFERENCES_PROSE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/INJECTION_MANIFEST.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/INJECTION_RECONCILIATION.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I46_I47_I49.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I48.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/REVUE_I71_I80_Q21.md` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/STRUCTURE_I71_I80_Q21.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/CLAUDE_8CE3E99/original/glossary_q21.py` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/AUDIT_JAUGES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_DASHBOARD.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/CONTROLES_E2C023C_ROUTES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DELTA_E2C023C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT_E2.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/DEPLOIEMENT_E2.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/FRAGMENTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/FRAGMENTS_METHODE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/TACHES_MAJEURES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/ETAT_DES_LIEUX/TACHES_METHODE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_CATEGORIES_S01.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_INVENTAIRE_S01.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/0974D85_S01_HISTORIQUE.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_DIFFERENCES_COPIES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20BEE19_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_ARTEFACTS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_COMMANDES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_DELTA_20BEE19.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_HELPERS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_INTEGRITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_LOGS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_MANIFESTE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_PERIMETRE_MAIN.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_RESEAU_GLOBAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_RESULTATS_NATIFS.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/20C67C0_ROUTES_I83_I87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_ARTEFACTS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_COMMANDES_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_LOGS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_NATIFS_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_RESEAU_CANONIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_ROUTES_CANONIQUES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/6D5797C_S01_CANONIQUE.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_PATHOLOGIE_EXAMENS.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_PHARMACOLOGIE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_SCIENCES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/AUDIT_TECHNIQUE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_20BEE19.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_20C67C0.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_CANONIQUES_6D5797C.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_INDEPENDANTS.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/CONTROLES_UNITAIRES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DECISION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_20BEE19_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_20C67C0_PHARMACOLOGIE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_20C67C0_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_6D5797C_PHARMACOLOGIE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DELTA_6D5797C_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/ENVIRONNEMENT_SOURCES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/INJECTION_LOCALE_6D5797C.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/INVENTAIRE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/INVENTAIRE_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/PREUVE_AETHOXYSKLEROL_COMPRESSION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/injection_intra_arterielle_extraits.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/rapidocain_extraits.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PREUVES_6D5797C/rapport.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/PROTOCOLE_CONTROLES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/VEILLE_RECEPTION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/AUDIT_MEDICAL.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/AUDIT_MEDICAL.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/COMMENTAIRE_CONTRE_AUDIT.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/CONTROLE_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/CONTROLE_TECHNIQUE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/DECISION.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/DECISION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/build-global-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/build-global.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/build-s01-command.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/build-s01.log` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/global-browser-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/global-browser.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/global-http.py` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/global-network.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/gloss-sigles-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/gloss-sigles.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/gloss-sigles.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/gloss-sigles.py` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/http-preload.cjs` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/livraison.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/native-i83-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/native-i83.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/native-i83/i83_native_results.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/native-i83/transport.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/rebuild-global.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/rebuild-global.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/routes-i83-i87-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/routes-i83-i87.cjs` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/routes-i83-i87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/routes-i83-i87.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/routes-i83-i87/transport.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/run-one.py` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/s01-browser-command.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/s01-browser.log` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/s01-browser/browser-results.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/s01-browser/transport.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/source-inspection.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/static-i83-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/static-i83.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/unit.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V5/controles/unit.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/CONTROLE_TECHNIQUE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/CONTROLE_TECHNIQUE.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/DECISION.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/DECISION.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/DELTA_AUDITE.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/PUBLICATION_PAGES.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/PUBLICATION_PAGES.md` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/build-global-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/build-global.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/build-s01-command.json` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/build-s01.log` | review_report | S01 | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/global-browser-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/global-browser.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/global-http.py` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/global-network.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/gloss-sigles-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/gloss-sigles.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/gloss-sigles.log` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/gloss-sigles.py` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/http-preload.cjs` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/livraison.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/routes-i83-i87-command.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/routes-i83-i87.cjs` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/routes-i83-i87.json` | review_report | GLOBAL | integration_target |
| `docs/collaboration/reviews/2026-10-08/I83_HARMONISATION_V6/controles/routes-i83-i87.log` | review_report | GLOBAL | integration_target |

## claude/medina-alpha-integration-7dul4i

- Chemin sans route de build connue ; examen manuel requis.
- Sortie dérivée ; intégrer les sources puis reconstruire.
- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Tracés générés : vérifier modules/ecg.py et régénérer.
- Coque historique et ressources embarquées : contrôler SYSTEM et les fragments séparément.
- PR #1 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.claude/commands/audit.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/chapitre.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/cycle.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/fusion-alpha.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/livrer.md` | documentation | GLOBAL | pull_request_base |
| `.gitignore` | unknown |  | pull_request_base |
| `CHAPTER_SPEC.md` | documentation | GLOBAL | pull_request_base |
| `CLAUDE.md` | documentation | GLOBAL | pull_request_base |
| `MEDINA_ClaudeCode.zip` | derived |  | pull_request_base |
| `PASSATION_REECRITURE_2026-09-26.md` | documentation | GLOBAL | pull_request_base |
| `PROMPT_MEDINA.md` | documentation | GLOBAL | pull_request_base |
| `PROMPT_REPRISE_IA.md` | documentation | GLOBAL | pull_request_base |
| `README.md` | documentation | GLOBAL | pull_request_base |
| `REPRISE_CLAUDE_CODE.md` | documentation | GLOBAL | pull_request_base |
| `_alpha_in/LISEZMOI.txt` | unknown |  | pull_request_base |
| `_alpha_in/MEDINA_Alpha_26-09-2026.html` | unknown |  | pull_request_base |
| `_alpha_in/MEDINA_Alpha_PASSATION_2026-09-26.md` | documentation | GLOBAL | pull_request_base |
| `_alpha_in/MEDINA_Alpha_TRANSPORT_26-09-2026.zip` | unknown |  | pull_request_base |
| `audits/A41.md` | review_report | T1 | pull_request_base |
| `audits/DESIGN_2026-09-26.md` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_MODERNISATION.md` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/01_accueil_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/01_accueil_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/01_accueil_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/02_accueil_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/02_accueil_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/03_bouton_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/03_bouton_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/04_notification_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/04_notification_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/05_specialite_cardiologie_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/05_specialite_cardiologie_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/05_specialite_cardiologie_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/06_systeme_cardiologie_mobile.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/apres/06_systeme_cardiologie_pc.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/apres/07_entree_cim_plan_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/07_entree_cim_plan_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/08_cours_entete_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/08_cours_entete_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/08_cours_entete_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/09_cours_ilot_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/09_cours_ilot_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/09_cours_ilot_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/10_cours_fenetre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/10_cours_fenetre_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/10_cours_fenetre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/11_cours_quiz_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/11_cours_quiz_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/11_cours_quiz_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/12_cours_pareto_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/12_cours_pareto_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/13_cours_navigo_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/13_cours_navigo_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/13_cours_navigo_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/14_cours_police_taille_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/14_cours_police_taille_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/15_cours_mode_livre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/15_cours_mode_livre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/16_cours_sciences_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/16_cours_sciences_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/17_examen_federal_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/17_examen_federal_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/17_examen_federal_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/18_carnet_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/18_carnet_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/19_recherche_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/19_recherche_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/19_recherche_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/20_methode_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/20_methode_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/21_atlas_ecg_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/21_atlas_ecg_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/21_atlas_ecg_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/01_accueil_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/01_accueil_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/02_accueil_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/02_accueil_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/03_bouton_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/03_bouton_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/04_notification_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/04_notification_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/05_specialite_cardiologie_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/05_specialite_cardiologie_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/06_systeme_cardiologie_mobile.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/avant/06_systeme_cardiologie_pc.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/avant/07_entree_cim_plan_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/07_entree_cim_plan_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/08_cours_entete_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/08_cours_entete_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/09_cours_ilot_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/09_cours_ilot_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/10_cours_fenetre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/10_cours_fenetre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/11_cours_quiz_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/11_cours_quiz_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/12_cours_pareto_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/12_cours_pareto_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/13_cours_navigo_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/13_cours_navigo_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/14_cours_police_taille_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/14_cours_police_taille_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/15_cours_mode_livre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/15_cours_mode_livre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/16_cours_sciences_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/16_cours_sciences_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/17_examen_federal_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/17_examen_federal_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/18_carnet_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/18_carnet_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/19_recherche_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/19_recherche_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/20_methode_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/20_methode_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/21_atlas_ecg_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/21_atlas_ecg_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FUSION_ALPHA.md` | review_report | GLOBAL | pull_request_base |
| `audits/FUSION_GLOSSAIRE.md` | review_report | GLOBAL | pull_request_base |
| `audits/FUSION_J44.md` | review_report | S02 | pull_request_base |
| `audits/HOME_DIRECTEUR_2026-09-26.md` | review_report | GLOBAL | pull_request_base |
| `audits/I26.md` | review_report | S02 | pull_request_base |
| `audits/J18.md` | review_report | S02 | pull_request_base |
| `audits/J18_sources.md` | review_report | S02 | pull_request_base |
| `audits/J44.md` | review_report | S02 | pull_request_base |
| `audits/NAVIGO_2026-09-26.md` | review_report | GLOBAL | pull_request_base |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |
| `build_medina.py` | integration_source | GLOBAL | pull_request_base |
| `build_v7.py` | unknown |  | pull_request_base |
| `captures_front.py` | unknown |  | pull_request_base |
| `chantier.py` | unknown |  | pull_request_base |
| `chapters.json` | registration_source | GLOBAL | pull_request_base |
| `chapters/A41/A41_a.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_b.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_c.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_d.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop1.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop2.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop_pa.html` | course_source | T1 | pull_request_base |
| `chapters/D84/D84_a.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_b.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_c.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_d.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_pop1.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_pop2.html` | course_source | S07 | pull_request_base |
| `chapters/I00/I00_a.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_b.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_c.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_d.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_a.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_b.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_c.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_d.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_a.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_b.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_c.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_d.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_a.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_b.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_c.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_d.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I26/I26_a.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_b.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_c.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_d.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_pop2.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_pop_pa.html` | course_source | S02 | pull_request_base |
| `chapters/I30/I30_a.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_b.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_c.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_d.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_a.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_b.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_c.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_d.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_a.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_b.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_c.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_d.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_a.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_b.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_c.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_d.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_a.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_b.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_c.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_d.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_a.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_b.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_c.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_d.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_a.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_b.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_c.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_d.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_a.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_b.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_c.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_d.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_a.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_b.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_c.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_d.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_a.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_b.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_c.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_d.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_a.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_b.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_c.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_d.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_a.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_b.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_c.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_d.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_a.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_b.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_c.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_d.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_pop.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_a.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_b.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_c.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_d.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_pop.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_a.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_b.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_c.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_d.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_pop.html` | course_source | S01 | pull_request_base |
| `chapters/J18/J18_a.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_b.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_c.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_d.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_pop_pa.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_a.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_b.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_c.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_d.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop2.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop3.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop_pa.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_a.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_b.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_c.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_d.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop2.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop3.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop4.html` | course_source | S02 | pull_request_base |
| `chapters/M06/M06_a.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_b.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_c.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_d.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_pop.html` | course_source | S10 | pull_request_base |
| `chapters/M31/M31_a.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_b.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_c.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_d.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_pop.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_a.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_b.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_c.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_d.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_pop.html` | course_source | S07 | pull_request_base |
| `chapters/Q21/Q21_a.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_b.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_c.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_d.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop7.html` | course_source | S01 | pull_request_base |
| `chapters/T78/T78_a.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_b.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_c.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_d.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_pop1.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_pop2.html` | course_source | S07 | pull_request_base |
| `create_cycle_pdf.py` | unknown |  | pull_request_base |
| `create_status_pdf.py` | unknown |  | pull_request_base |
| `dist/MEDINA_Claude.html` | derived |  | pull_request_base |
| `dist/MEDINA_Etat_des_lieux.html` | derived |  | pull_request_base |
| `dist/MEDINA_SOURCES.json` | derived |  | pull_request_base |
| `dist/MEDINA_final.html` | derived |  | pull_request_base |
| `dist/MEDINA_final_SOURCES.json` | derived |  | pull_request_base |
| `docs/STYLE_REDACTION.md` | documentation | GLOBAL | pull_request_base |
| `docs/alpha/IDENTITE_MEDINA_Alpha.md` | documentation | GLOBAL | pull_request_base |
| `docs/alpha/PROMPT_MEDINA_Alpha.md` | documentation | GLOBAL | pull_request_base |
| `docs/passation/consignes_gen.py` | documentation | GLOBAL | pull_request_base |
| `docs/passation/mesure_texte.py` | documentation | GLOBAL | pull_request_base |
| `docs/passation/wf_contre_lecture.js` | documentation | GLOBAL | pull_request_base |
| `docs/passation/wf_reecriture_sequentielle.js` | documentation | GLOBAL | pull_request_base |
| `engine/medina_course.css` | integration_source | GLOBAL | pull_request_base |
| `engine/medina_course.js` | integration_source | GLOBAL | pull_request_base |
| `glossary/a41.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/cardio_1.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/cardio_2.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/cardio_3.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/d84.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i00.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i10.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i21.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i25.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i26.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i30.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i33.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i34.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i35.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i40.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i42.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i44.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i46.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i47.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i48.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i49.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i70.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i71.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i80.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/j18.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/j44.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/j45.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/m06.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/m31.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/m32.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/q21.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/t78.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/zz_fusion.py` | glossary_source | GLOBAL | pull_request_base |
| `modules/ecg.json` | derived | S01 | pull_request_base |
| `modules/ecg.py` | unknown |  | pull_request_base |
| `modules/p2.html` | unknown |  | pull_request_base |
| `modules/p3.html` | unknown |  | pull_request_base |
| `modules/prev.html` | unknown |  | pull_request_base |
| `pack.py` | unknown |  | pull_request_base |
| `pack_v7.py` | integration_source | GLOBAL | pull_request_base |
| `recover_polish.py` | unknown |  | pull_request_base |
| `restore.py` | unknown |  | pull_request_base |
| `shell/data.py` | registration_source | GLOBAL | pull_request_base |
| `shell/medina_front.html` | integration_source | GLOBAL | pull_request_base |
| `shell/polish.css` | integration_source | GLOBAL | pull_request_base |
| `shell/polish.js` | integration_source | GLOBAL | pull_request_base |
| `shell/shell.html` | integration_source | GLOBAL | pull_request_base |
| `test_medina.py` | unknown |  | pull_request_base |
| `test_preview.py` | unknown |  | pull_request_base |
| `test_v7.py` | unknown |  | pull_request_base |

## claude/mission-justification-20261007


| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `docs/collaboration/MISSION_JUSTIFICATION_2026-10-07.md` | documentation | GLOBAL | pull_request_base |

## claude/review-i48-esc2024-20261007


## claude/review-medina-global-20261007

- Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT2_I48/journal.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT2_I48/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT3_SCIENCES/journal.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT3_SCIENCES/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I10/I10_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I21/I21_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I25/I25_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I46/I46_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I47/I47_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I49/I49_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I50/I50_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/Q21/Q21_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/REPRISE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/fenetres_existantes.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats_partiels.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/workflow_justification.js` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/sources/chapters/I26/I26_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/sources/chapters/J18/J18_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/sources/chapters/J44/J44_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Claude/P-02-Pneumologie/sources/chapters/J45/J45_c.html` | delivery_source | S02 | pull_request_base |

## claude/review-medina-global-20261007


| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `chapters/A41/A41_a.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_b.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_c.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop_sciences_revision.html` | course_source | T1 | pull_request_base |
| `chapters/D84/D84_c.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_pop_sciences_revision.html` | course_source | S07 | pull_request_base |
| `chapters/I40/I40_c.html` | course_source | S01 | pull_request_base |
| `chapters/J44/J44_a.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_b.html` | course_source | S02 | pull_request_base |
| `chapters/M06/M06_c.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_pop_sciences_revision.html` | course_source | S10 | pull_request_base |
| `chapters/M31/M31_c.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_pop_sciences_revision.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_c.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_pop_sciences_revision.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_c.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_pop_sciences_revision.html` | course_source | S07 | pull_request_base |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/2026-10-07/GLOBAL_LOT1/journal.json` | review_report | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/2026-10-07/GLOBAL_LOT1/rapport.md` | review_report | GLOBAL | pull_request_base |

## claude/review-medina-global-20261007


| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `chapters/I48/I48_a.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_c.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop4.html` | course_source | S01 | pull_request_base |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/CLAUDE_CS_CARDIO_RAPPORT_2026-10-07.md` | review_report | S01, CS | pull_request_base |
| `docs/collaboration/reviews/CLAUDE_I48_ESC2024_RAPPORT.md` | review_report | S01 | pull_request_base |
| `modules/cardiovascular_cs.html` | clinical_skills_source | S01, CS | pull_request_base |
| `modules/cardiovascular_cs.js` | clinical_skills_source | S01, CS | pull_request_base |

## codex/ajouter-options-de-generation-de-fragments

- PR #3 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |

## codex/configurer-publication-github-pages-automatique

- Chemin sans route de build connue ; examen manuel requis.
- PR #4 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/pages.yml` | integration_source | GLOBAL | pull_request_base |
| `.gitignore` | unknown |  | pull_request_base |
| `build_index.py` | integration_source | GLOBAL | pull_request_base |
| `tests/audit_fragments.py` | integration_source | GLOBAL | pull_request_base |

## codex/creer-fragments.json-et-corrige-des-chemins

- Chemin sans route de build connue ; examen manuel requis.
- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- PR #2 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.gitignore` | unknown |  | pull_request_base |
| `FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `build_medina.py` | integration_source | GLOBAL | pull_request_base |
| `fragments.json` | registration_source | GLOBAL | pull_request_base |
| `test_preview.py` | unknown |  | pull_request_base |

## codex/etancheite-complete-des-fragments

- PR #5 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |
| `tests/audit_fragments.py` | integration_source | GLOBAL | pull_request_base |

## codex/fragment-s01-accueil-navigo-20261005

- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- PR #7 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `audits/S01_2026-10-05/README.md` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/browser-results.json` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/accueil_mobile.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/accueil_pc.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/cours_mobile.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/cours_pc.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/navigo_mobile.jpg` | review_report | S01 | pull_request_base |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |
| `fragment_surface.py` | integration_source | GLOBAL | pull_request_base |
| `fragments.json` | registration_source | GLOBAL | pull_request_base |
| `shell/fragment.css` | integration_source | GLOBAL | pull_request_base |
| `shell/fragment.js` | integration_source | GLOBAL | pull_request_base |
| `tests/audit_fragments.py` | integration_source | GLOBAL | pull_request_base |
| `tests/verify_s01_browser.cjs` | integration_source | GLOBAL | pull_request_base |

## codex/mechanismes-20261007


## codex/repartition-fragments-20261008


## codex/sciences-cs-fragments-20261007

- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction.
- Tableau reconstruit depuis le registre et tools/build_organisation.py.
- PR #13 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/claude_watch.yml` | integration_source | GLOBAL | pull_request_base |
| `AGENTS.md` | documentation | GLOBAL | pull_request_base |
| `CLAUDE.md` | documentation | GLOBAL | pull_request_base |
| `audits/CHAINE_FRAGMENTS_2026-10-08/VALIDATION.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/ARBITRAGES.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/LATE_BRANCH_CHECK.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/RAPPORT.md` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/REMOTE_PROOF.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/VALIDATION_SUMMARY.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/browser-final.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/fragments-final.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/justifications-final.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/static.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/unit-verbose.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_LOT4_2026-10-07/verify_i48.cjs` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/ADAPTATIONS_CODEX.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/CATEGORIES.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/CONVERGENCE_MAIN.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/I33_CONFIRMATION.json` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/INVENTORY.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/LOT5_ADAPTATIONS_CODEX.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/LOT5_SCIENCES.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/PUBLICATION.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/RAPPORT.md` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/RESERVES_CLAUDE.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/SCIENCES.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/VALIDATION_SUMMARY.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/browser.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/build.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/convergence_main/BUILD_S01.log` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/convergence_main/EXPORT_PROOF.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/convergence_main/FRAGMENTS.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/convergence_main/SCIENCES.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/convergence_main/UNIT_TESTS.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/convergence_main/VALIDATION_SUMMARY.json` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/final_s01_build.log` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/fragments.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/i48_bibliography/browser.log` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/i48_bibliography/static.log` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/initial-browser-attempt.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/lot5_build.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/lot5_four/browser.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/lot5_four/static.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/s01.log` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/s01/browser-results.json` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/static.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/unittest.log` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/verify_i48_bibliography.cjs` | review_report | S01 | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/verify_lot5_four.cjs` | review_report | GLOBAL | pull_request_base |
| `audits/CLAUDE_TEN_2026-10-07/verify_ten.cjs` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/CLAUDE_DELTA.md` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/CLAUDE_DELTA_PROOF.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/I50.md` | review_report | S01 | pull_request_base |
| `audits/REPRISE_2026-10-07/I50_CHANGES.json` | review_report | S01 | pull_request_base |
| `audits/REPRISE_2026-10-07/I50_COUNTER_REVIEW.md` | review_report | S01 | pull_request_base |
| `audits/REPRISE_2026-10-07/I50_READONLY.md` | review_report | S01 | pull_request_base |
| `audits/REPRISE_2026-10-07/J18.json` | review_report | S02 | pull_request_base |
| `audits/REPRISE_2026-10-07/J18.md` | review_report | S02 | pull_request_base |
| `audits/REPRISE_2026-10-07/J44.json` | review_report | S02 | pull_request_base |
| `audits/REPRISE_2026-10-07/J44.md` | review_report | S02 | pull_request_base |
| `audits/REPRISE_2026-10-07/README.md` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/SCIENCES.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/UNITAIRES.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/browser-final/targeted_justifications_results.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/browser/failed_justifications_results.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/browser/targeted_justifications_results.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/figures/figure-browser-results.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/figures/visual-review.json` | review_report | GLOBAL | pull_request_base |
| `audits/REPRISE_2026-10-07/verify_figures.cjs` | review_report | GLOBAL | pull_request_base |
| `chapters/I42/I42_a.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_b.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop_esc_comparison.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_a.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_b.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_c.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_d.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_a.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_b.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_c.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_d.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_a.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_b.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_d.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop_esc_comparison.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_a.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_b.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_c.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_d.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_a.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_b.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_c.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_justifications.json` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop_esc_comparison.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_a.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_b.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_c.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_d.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_pop.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_pop_sciences.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_a.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_b.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_c.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_d.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_pop.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_pop_sciences.html` | course_source | S01 | pull_request_base |
| `chapters/J18/J18_a.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_c.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_justifications.json` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_pop_sciences_revision.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_c.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_justifications.json` | course_source | S02 | pull_request_base |
| `chapters/Q21/Q21_a.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_b.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_c.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_d.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop7.html` | course_source | S01 | pull_request_base |
| `docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/DELIVERIES_LATEST.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/DELIVERIES_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/FRAGMENTS_RESTANTS.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/FRAGMENT_01_PRIORITE.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/MECHANISMS_CLAUDE.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/MECHANISMS_PLAN.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/README.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/SIGNAUX_CODEX.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_ESC2026_20261008_RECEPTION.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_LOT4_CHECKPOINT_20261007.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_LOT4_FINAL_20261007.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_LOT5_CONVERGENCE_20261008.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_LOT5_FINAL_20261007.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_PACKET_S01_20261007T214720372776Z.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/receipts/CLAUDE_PACKET_S01_20261007T221127276821Z.json` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/2026-10-07/SNAPSHOT_DEPLOYED_I48.json` | review_report | S01 | pull_request_base |
| `docs/collaboration/reviews/2026-10-07/SNAPSHOT_DEPLOYED_I48.md` | review_report | S01 | pull_request_base |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/AUDIT_MEDICAL.md` | review_report | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/AUDIT_TECHNIQUE.md` | review_report | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/RECEPTION.md` | review_report | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/2026-10-08/VEILLE_CLAUDE/RECEPTION_ACTUALISEE.md` | review_report | GLOBAL | pull_request_base |
| `glossary/q21.py` | glossary_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-I48_BIBLIOGRAPHY/MERGE_PROOF.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-I48_BIBLIOGRAPHY/sources/chapters/I48/I48_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-I48_BIBLIOGRAPHY/sources/chapters/I48/I48_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-I48_BIBLIOGRAPHY/sources/chapters/I48/I48_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-I48_BIBLIOGRAPHY/sources/chapters/I48/I48_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/AVANCEMENT.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/REMOTE_PROOF.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/livraison.original.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/q21.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I47/I47_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I71/I71_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I71/I71_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I71/I71_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I71/I71_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I71/I71_pop.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I71/I71_pop_sciences.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I80/I80_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I80/I80_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I80/I80_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I80/I80_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I80/I80_pop.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/I80/I80_pop_sciences.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/sources/chapters/Q21/Q21_pop7.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/verification/I47.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/verification/I71.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/verification/I80.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-LOT5_FINAL/verification/Q21.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/INITIAL_FETCH_DIFFERENCES.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/REMOTE_PROOF.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/livraison.original.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I00/I00_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I30/I30_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I33/I33_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I34/I34_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I35/I35_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I40/I40_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I42/I42_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I44/I44_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I46/I46_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/sources/chapters/I49/I49_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I00.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I30.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I33.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I34.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I35.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I40.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I42.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I44.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I46.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-TEN_READY/verification/I49.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I00/I00_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I10/I10_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I21/I21_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I25/I25_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I30/I30_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I33/I33_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I34/I34_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I35/I35_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I40/I40_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I42/I42_pop_esc_comparison.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I44/I44_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I46/I46_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I47/I47_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I48/I48_pop_esc_comparison.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I49/I49_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_justifications.json` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I50/I50_pop_esc_comparison.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I70/I70_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I71/I71_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I71/I71_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I71/I71_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I71/I71_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I71/I71_pop.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I71/I71_pop_sciences.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I80/I80_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I80/I80_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I80/I80_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I80/I80_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I80/I80_pop.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I80/I80_pop_sciences.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop1.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop2.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop3.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop4.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop5.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop6.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/Q21/Q21_pop7.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Codex/D-16-Dermatologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/D-16-Dermatologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/D-16-Dermatologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/D-20-Diagnostic clinique et examens complémentaires/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/D-20-Diagnostic clinique et examens complémentaires/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/D-20-Diagnostic clinique et examens complémentaires/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/E-22-Éthique médicale, droit et communication/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/E-22-Éthique médicale, droit et communication/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/E-22-Éthique médicale, droit et communication/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/G-04-Gastroentérologie et hépatologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/G-04-Gastroentérologie et hépatologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/G-04-Gastroentérologie et hépatologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/G-10-Gynécologie et sénologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/G-10-Gynécologie et sénologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/G-10-Gynécologie et sénologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/H-08-Hématologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/H-08-Hématologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/H-08-Hématologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/sources/chapters/A41/A41_a.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/sources/chapters/A41/A41_b.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/sources/chapters/A41/A41_c.html` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/sources/chapters/A41/A41_justifications.json` | delivery_source | T1 | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/travail/A41-2026-10-08/DEMANDE_LECTURE_CROISEE_CLAUDE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/travail/A41-2026-10-08/INVENTAIRE_BASE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-03-Infectiologie/travail/A41-2026-10-08/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/D84/D84_c.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/D84/D84_justifications.json` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M31/M31_a.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M31/M31_b.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M31/M31_c.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M31/M31_d.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M31/M31_justifications.json` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M31/M31_pop.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M32/M32_c.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/M32/M32_justifications.json` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/T78/T78_b.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/T78/T78_c.html` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/I-13-Immunologie et allergologie/sources/chapters/T78/T78_justifications.json` | delivery_source | S07 | pull_request_base |
| `livraisons/Livraison Codex/M-12-Médecine des âges de la vie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-12-Médecine des âges de la vie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-12-Médecine des âges de la vie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-19-Médecine d’urgence, traumatologie et toxicologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-19-Médecine d’urgence, traumatologie et toxicologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-19-Médecine d’urgence, traumatologie et toxicologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-21-Médecine de premier recours et santé publique/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-21-Médecine de premier recours et santé publique/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/M-21-Médecine de premier recours et santé publique/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/N-05-Neurologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/N-05-Neurologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/N-05-Neurologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/N-07-Néphrologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/N-07-Néphrologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/N-07-Néphrologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-09-Oncologie, génétique médicale et soins palliatifs/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-09-Oncologie, génétique médicale et soins palliatifs/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-09-Oncologie, génétique médicale et soins palliatifs/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-11-Obstétrique et néonatologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-11-Obstétrique et néonatologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-11-Obstétrique et néonatologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-17-Oto-rhino-laryngologie et médecine bucco-dentaire/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-17-Oto-rhino-laryngologie et médecine bucco-dentaire/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-17-Oto-rhino-laryngologie et médecine bucco-dentaire/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-18-Ophtalmologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-18-Ophtalmologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/O-18-Ophtalmologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/I26/I26_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/I26/I26_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/I26/I26_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/I26/I26_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J18/J18_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J18/J18_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J18/J18_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J18/J18_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J18/J18_pop1.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J18/J18_pop_sciences_revision.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J40/J40_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J40/J40_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J40/J40_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J40/J40_d.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J40/J40_pop.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J44/J44_a.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J44/J44_b.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J44/J44_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J44/J44_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J45/J45_c.html` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/P-02-Pneumologie/sources/chapters/J45/J45_justifications.json` | delivery_source | S02 | pull_request_base |
| `livraisons/Livraison Codex/R-14-Rhumatologie et orthopédie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/R-14-Rhumatologie et orthopédie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/R-14-Rhumatologie et orthopédie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/R-14-Rhumatologie et orthopédie/sources/chapters/M06/M06_c.html` | delivery_source | S10 | pull_request_base |
| `livraisons/Livraison Codex/R-14-Rhumatologie et orthopédie/sources/chapters/M06/M06_justifications.json` | delivery_source | S10 | pull_request_base |
| `livraisons/Livraison Codex/U-15-Urologie et andrologie/README.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/U-15-Urologie et andrologie/livraison.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Codex/U-15-Urologie et andrologie/sources/README.md` | delivery_source | GLOBAL | pull_request_base |
| `organisation/MEDINA_Organisation.html` | derived | GLOBAL | pull_request_base |
| `organisation/production_plan.json` | consultation_source | GLOBAL | pull_request_base |
| `tests/test_claude_watch.py` | integration_source | GLOBAL | pull_request_base |
| `tests/test_production_plan.py` | integration_source | GLOBAL | pull_request_base |
| `tests/verify_justifications_recovery.cjs` | integration_source | GLOBAL | pull_request_base |
| `tools/claude_watch.py` | integration_source | GLOBAL | pull_request_base |

## Limites

- Diff de branche potentiellement limité à 300 fichiers : 5f04f5d950f742ec8848795bc048822d566640c5.
- Diff de branche potentiellement limité à 300 fichiers : 61a841b3c96b3bd4f3ad58ec5870d06945e63292.
- Diff de branche potentiellement limité à 300 fichiers : 9aa65044972f8bdd5e922a3567a78adb2565f8fb.
- Diff de branche potentiellement limité à 300 fichiers : db06b1fae3c27e93050850df44c3eb23fcd60164.
- Reçu non lisible docs/collaboration/receipts/CLAUDE_ALPHA_2026-09-26.json : GitHub HTTP 503 sur /contents/docs/collaboration/receipts/CLAUDE_ALPHA_2026-09-26.json
- Les rapports et les tests déclarés ne constituent pas une vérification médicale indépendante.
- Le routage est contrôlé contre les sources locales de la cible, avant les changements proposés.
- Aucune branche n'est fusionnée, aucun reçu créé et aucun commit publié par ce scanner.
