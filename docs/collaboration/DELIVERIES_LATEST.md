# MEDINA — livraisons repérées

Branche d'intégration : `codex/sciences-cs-fragments-20261007`.
Commit cible : `7fa06329b3369f54ef0831ae9f6cdf90fce5f605`.

Scan : complet selon les données fournies.
Une livraison repérée ou reçue n'est pas présumée intégrée. Une intégration ne prouve pas une vérification.

| Branche / PR | Tête | Reçu | Intégré dans la cible | Vérifié | Routage |
| --- | --- | --- | --- | --- | --- |
| codex/accueil-qcm-20260929 · #6 | `871bb223564d` | Non confirmé | Non démontré | Non démontré | GLOBAL |
| claude/medina-alpha-integration-7dul4i · #1 | `303f95a66dd2` | Oui | Oui, preuve enregistrée | Non démontré | À préciser |
| claude/review-i48-esc2024-20261007 | `c3770739b58c` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| claude/review-medina-global-20261007 · #9 | `394dc0857f83` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | GLOBAL, S01, S02, S07, S10, T1 |
| claude/review-medina-global-20261007 · #8 | `f6e400df9e5d` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | À préciser |
| codex/ajouter-options-de-generation-de-fragments · #3 | `1539f4e77171` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| codex/configurer-publication-github-pages-automatique · #4 | `8d0de9bcd572` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| codex/creer-fragments.json-et-corrige-des-chemins · #2 | `0f38d9aab4ef` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| codex/etancheite-complete-des-fragments · #5 | `7071e557cfc2` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| codex/fragment-s01-accueil-navigo-20261005 · #7 | `c50a28a23d7e` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| main | `d4309b0d3de9` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |

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

## claude/medina-alpha-integration-7dul4i

- PR #1 vise main ; comparaison à la cible MEDINA requise.

## claude/review-i48-esc2024-20261007


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


## codex/ajouter-options-de-generation-de-fragments

- PR #3 vise main ; comparaison à la cible MEDINA requise.

## codex/configurer-publication-github-pages-automatique

- PR #4 vise main ; comparaison à la cible MEDINA requise.

## codex/creer-fragments.json-et-corrige-des-chemins

- PR #2 vise main ; comparaison à la cible MEDINA requise.

## codex/etancheite-complete-des-fragments

- PR #5 vise main ; comparaison à la cible MEDINA requise.

## codex/fragment-s01-accueil-navigo-20261005

- PR #7 vise main ; comparaison à la cible MEDINA requise.

## main


## Limites

- Reçus lus dans les fichiers locaux : SHA cible indisponible ; fournir receipts dans le snapshot pour les figer.
- Catalogue lu dans les fichiers locaux : le SHA cible n'est pas disponible localement. Vérifier leurs empreintes ou fournir catalog dans le snapshot.
- Les rapports et les tests déclarés ne constituent pas une vérification médicale indépendante.
- Le routage est contrôlé contre les sources locales de la cible, avant les changements proposés.
- Aucune branche n'est fusionnée, aucun reçu créé et aucun commit publié par ce scanner.
