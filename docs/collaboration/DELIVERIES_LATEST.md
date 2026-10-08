## 2026-10-08 — PR #12, tête b983cb6 : attestation S01 et preuves suisses I83

État : **reçu et archivé ; non injecté**. Quatre objets. Le S01 v5 reprend exactement les assertions et le résultat du v4, mais une attestation horodatée lie désormais le résultat aux empreintes de construction. Les sources suisses restent non contre-vérifiées indépendamment et la simulation se fonde sur un ancien main. [Rapport](reviews/2026-10-08/PR12_B983CB6_I83_ATTESTATION_SOURCES/RECEPTION.md).

## 2026-10-08 — PR #12, tête 2145a2a : correction rénale I35

État : **reçu et archivé ; non injecté**. La limite de dose initiale plus élevée en maladie rénale chronique est ajoutée conformément à l’ESC 2026 ; six objets archivés et 3 269 contrôles producteurs sans erreur déclarée. [Rapport](reviews/2026-10-08/PR12_2145A2A_I35_RENAL/RECEPTION.md).

## 2026-10-08 — PR #12, tête 6b76e12 : I83 limites v4

État : **reçu et archivé ; non injecté**. Neuf objets, dont cinq sources I83. Le contrôle natif v4 est nouveau ; le journal S01 v4 est un duplicata exact du précédent. Les affirmations Swissmedic/OFSP et le cours complet restent à contre-vérifier. [Rapport](reviews/2026-10-08/PR12_6B76E12_I83_LIMITES_V4/RECEPTION.md).

## 2026-10-08 — PR #12, tête 7c6fc65 : corrections ESC ciblées

État : **reçu et archivé ; non injecté**. Treize objets ; rapports MED lisibles, I35 corrigé et contrôlé côté producteur, faux écart I40 écarté. L’injection attend toujours la clôture d’I83 et la contrelecture indépendante par chapitre. [Rapport](reviews/2026-10-08/PR12_7C6FC65_ESC_CORRECTIONS/RECEPTION.md).

## 2026-10-08 — PR #12, tête 4c8c534 : rapports et contrôles ESC 2026

État : **reçu et archivé ; non injecté**. Vingt-quatre objets pour I30, I33, I34, I35, I40, I42, I44 et Q21 ; 26 668 contrôles producteurs déclarés sans échec sur `main` `960586e`, non reproduits indépendamment. I83 reste actif et les réserves de traçabilité/médicales empêchent l’application. [Rapport](reviews/2026-10-08/PR12_4C8C534_ESC_RAPPORTS_CONTROLES/RECEPTION.md).

## 2026-10-08 — PR #12, tête d2a460f : simulation I83 sur main

État : **reçu et archivé ; non injecté**. Simulation producteur sur `main` `625fddb`, 1 923 contrôles I83 et 72 contrôles S01 déclarés sans erreur ; ancien faux contrôle S01 rectifié. Contre-vérification indépendante et réserves médicales restantes empêchent encore l’injection. [Rapport](reviews/2026-10-08/PR12_D2A460F_I83_SIMULATION_MAIN/RECEPTION.md).

## 2026-10-08 — PR #12, tête decef42 : preuve et contrôle I83 v3

État : **reçu et archivé ; non injecté**. Preuve Aethoxysklerol avec extraits, empreinte et liens publics ; contrôle v3 sur la bonne empreinte, 1 923 contrôles déclarés sans échec. Reconstruction et navigateur indépendants de la version intégrée restent requis. [Rapport](reviews/2026-10-08/PR12_DECEF42_I83_PREUVE_CONTROLE/RECEPTION.md).

## 2026-10-08 — PR #12, tête cdd2b72 : précision I83 Aethoxysklerol

État : **reçu et archivé ; non injecté**. La version suisse est mieux identifiée, mais la source primaire citée n’est pas livrée et le contrôle natif v2 ne correspond plus à l’empreinte courante de `I83_pop4.html`. [Rapport](reviews/2026-10-08/PR12_CDD2B72_I83_COMPRESSION/RECEPTION.md).

## 2026-10-08 — PR #12, tête be58ad9 : corrections I83 et réconciliation ESC

État : **reçu et archivé ; non injecté**. I83-MED-01/02 sont corrigées ; la durée de compression Aethoxysklerol reste à réconcilier. Les lots ESC correspondent désormais à main (26 propositions, 18 remplacements, 8 ajouts), mais les tests sont annoncés en cours, les huit rapports manquent et les contrôles n’ont pas été réexécutés. [Rapport](reviews/2026-10-08/PR12_BE58AD9_I83_ESC_CONTROLS/RECEPTION.md).

## 2026-10-08 — PR #12, tête a0b0204 : ESC 2026 par chapitre

État : **reçu et archivé ; non injecté**. Huit lots, 26 HTML ; 15 doublons de contenu, 10 modifications, 1 ajout au paquet. Manifestes vides et rapports absents ; cinq conflits de baseline I42/Q21 ; audit médical complet et contrôles techniques de plateforme requis. [Rapport](reviews/2026-10-08/PR12_ESC2026_A0B0204/RECEPTION.md).

# MEDINA — livraisons repérées

## Réception I83 et audit A41 — 7 octobre 2026

La remise **I83 — Varices des membres inférieurs (C-01-Cardiologie)** et la relecture **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)** sont reçues depuis `5bee2a48ef1804a0e3452d64a1041e0bd1b50691`, objets identiques à la tête observée `9bf195a843813ea6a1a24a1bad9642ed4e24f778`. Les originaux et empreintes sont archivés. I83 conserve deux erreurs médicales bloquantes (polidocanol et EHIT III) et des réserves à vérifier. Le rapport A41 comporte dix réserves majeures, 46 mineures et 19 rédactionnelles ; six empreintes sources sont conformes et les dix objets A41/glossaire concordent avec main. Aucune nouvelle injection ni reconstruction ou publication de cours n’a été effectuée. Les contrôles techniques de cette réception sont partiels ; les résultats navigateur de Claude ne sont pas revendiqués par Codex.

[Rapport de réception](reviews/2026-10-07/PR12_I83_A41_5BEE2A4/RECEPTION.md) · [Reçu et empreintes](receipts/CLAUDE_I83_A41_5BEE2A4_RECEPTION_2026-10-07.json). I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie) n’est pas remis. Le lot ESC2026_HUIT_COURS est retiré ; MED-01/02/03 restent ouvertes. Les remises historiques sont préservées, aucune attribution ou chapitre actif n’est modifié. A41 reste actif pour Codex.


Branche d'intégration : `codex/sciences-cs-fragments-20261007`.
Commit cible : `e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6`.

Scan : complet selon les données fournies.
Une livraison repérée ou reçue n'est pas présumée intégrée. Une intégration ne prouve pas une vérification.

| Branche / PR | Tête | Reçu | Intégré dans la cible | Vérifié | Routage |
| --- | --- | --- | --- | --- | --- |
| claude/loving-shannon-spwrhc · #12 | `b6db50cb2911` | Oui | Non démontré | Non démontré | GLOBAL, S01 |
| codex/accueil-qcm-20260929 · #6 | `871bb223564d` | Non confirmé | Non démontré | Non démontré | GLOBAL |
| claude/medina-alpha-integration-7dul4i · #1 | `303f95a66dd2` | Oui | Oui, preuve enregistrée | Non démontré | GLOBAL, S01, S02, S07, S10, SYSTEM, T1 |
| claude/mission-justification-20261007 · #11 | `45d34a9bd303` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| claude/review-i48-esc2024-20261007 | `c3770739b58c` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| claude/review-medina-global-20261007 · #10 | `7651825416cc` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL, S01, S02 |
| claude/review-medina-global-20261007 · #9 | `394dc0857f83` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | GLOBAL, S01, S02, S07, S10, T1 |
| claude/review-medina-global-20261007 · #8 | `f6e400df9e5d` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | CS, GLOBAL, S01 |
| codex/ajouter-options-de-generation-de-fragments · #3 | `1539f4e77171` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/configurer-publication-github-pages-automatique · #4 | `8d0de9bcd572` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/creer-fragments.json-et-corrige-des-chemins · #2 | `0f38d9aab4ef` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/etancheite-complete-des-fragments · #5 | `7071e557cfc2` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/fragment-s01-accueil-navigo-20261005 · #7 | `c50a28a23d7e` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL, S01 |
| codex/mechanismes-20261007 | `a6f18a150b1a` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| main | `e856ed16893b` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |

## claude/loving-shannon-spwrhc

- Chemin sans route de build connue ; examen manuel requis.
- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.gitignore` | unknown |  | integration_target |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `glossary/i48.py` | glossary_source | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/fenetres_types.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/journal.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/rapport.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/livraison.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I00/I00_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I30/I30_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I33/I33_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I34/I34_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I35/I35_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I40/I40_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I42/I42_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_a.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_b.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_d.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_pop5.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I44/I44_pop6.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I46/I46_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I47/I47_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_a.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_b.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_c.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_d.html` | delivery_source | S01 | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop1.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop2.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop3.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_pop4.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I49/I49_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/Q21/Q21_c.html` | delivery_source | S01 | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/AVANCEMENT.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/CONSIGNES.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/edits/I00_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-bpg-vagal__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-carditeinfra__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-crp-vs__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-d-bpg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-e-choree__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-e-souffle-ia__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-e-souffle-im__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-histoire__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-jones__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-mcisaac__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-mnemo-duree__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-pr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-strepto__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-v-fc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-v-fc__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/jobs/i00-whf__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-bpg-vagal__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-bpg-vagal__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-bpg-vagal__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-carditeinfra__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-carditeinfra__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-carditeinfra__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-crp-vs__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-crp-vs__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-crp-vs__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-d-bpg__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-d-bpg__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-d-bpg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-choree__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-choree__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-choree__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-ia__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-ia__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-ia__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-im__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-im__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-e-souffle-im__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-histoire__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-histoire__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-histoire__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-jones__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-jones__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-jones__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mcisaac__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mcisaac__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mcisaac__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mnemo-duree__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mnemo-duree__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-mnemo-duree__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-pr__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-pr__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-pr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-strepto__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-strepto__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-strepto__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-v-fc__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-whf__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-whf__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/out/i00-whf__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verdicts/I00_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I00/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/edits/I30_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-bilan__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-cortdep__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-crit__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-crp__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-ains__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-antiil1__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-colch__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-d-cortico__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-ecg-stades__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-echo-tamp__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-grossesse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-mnemo-faste__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-neo__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-pcis__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-pericardectomie__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-ponction__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-purul__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/jobs/i30-tb__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-bilan__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-bilan__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-bilan__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-cortdep__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-cortdep__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-cortdep__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crit__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crit__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crit__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crp__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crp__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-crp__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-ains__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-ains__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-ains__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-antiil1__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-antiil1__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-antiil1__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-colch__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-colch__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-colch__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-cortico__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-cortico__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-d-cortico__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ecg-stades__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ecg-stades__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ecg-stades__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-echo-tamp__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-echo-tamp__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-echo-tamp__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-grossesse__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-grossesse__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-grossesse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-mnemo-faste__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-mnemo-faste__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-mnemo-faste__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-neo__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-neo__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-neo__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pcis__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pcis__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pcis__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pericardectomie__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pericardectomie__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-pericardectomie__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ponction__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ponction__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-ponction__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-purul__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-purul__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-purul__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-tb__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-tb__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/out/i30-tb__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verdicts/I30_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I30/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/edits/I33_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-atcd-valve__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-chir__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-coxiella__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-cefaz__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-ceftri__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-dapto__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-flucl__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-genta__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-lzd__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-pen__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-rif__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-d-vanco__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-deci__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-duke__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-eto__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-fongique__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-gallo__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-hacek__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-ic-aigue__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-iscvid__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-neuro-cat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-poet__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-prothese__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-risque-emb__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-roth__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-saureus__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/jobs/i33-tep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-atcd-valve__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-atcd-valve__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-atcd-valve__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-chir__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-chir__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-chir__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-coxiella__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-coxiella__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-coxiella__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-cefaz__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-cefaz__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-cefaz__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-ceftri__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-ceftri__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-ceftri__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-dapto__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-dapto__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-dapto__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-flucl__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-flucl__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-flucl__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-genta__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-genta__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-genta__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-lzd__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-lzd__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-lzd__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-pen__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-pen__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-pen__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-rif__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-rif__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-rif__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-vanco__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-vanco__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-d-vanco__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-deci__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-deci__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-deci__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-duke__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-duke__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-duke__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-eto__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-eto__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-eto__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-fongique__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-fongique__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-fongique__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-gallo__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-gallo__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-gallo__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-hacek__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-hacek__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-hacek__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-ic-aigue__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-ic-aigue__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-ic-aigue__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-iscvid__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-iscvid__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-iscvid__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-neuro-cat__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-neuro-cat__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-neuro-cat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-poet__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-poet__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-poet__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-prothese__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-prothese__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-prothese__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-risque-emb__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-risque-emb__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-risque-emb__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-roth__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-roth__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-roth__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-saureus__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-saureus__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-saureus__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-tep__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-tep__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/out/i33-tep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verdicts/I33_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I33/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/edits/I34_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-anticoag-valve__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-avk-interact__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-congestion-renale__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-invictus__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-marqueurs-imp__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/jobs/i34-marqueurs-imp__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-anticoag-valve__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-anticoag-valve__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-anticoag-valve__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-avk-interact__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-avk-interact__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-avk-interact__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-congestion-renale__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-congestion-renale__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-congestion-renale__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-invictus__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-invictus__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-invictus__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/out/i34-marqueurs-imp__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verdicts/I34_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I34/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/edits/I35_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-bernoulli__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-calcif__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-chirnc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-choix-tech__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-aod-meca__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-asa__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-benza__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-hep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-inotrope__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-d-nitroprus__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-discord__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-dissection__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-dse__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-effort__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-grossesse__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-inr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-lflg-parad__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-manoeuvres__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-pacemaker__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-prothese__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-ra-asympto__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-seuils-aorte__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/jobs/i35-suivi__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-bernoulli__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-bernoulli__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-bernoulli__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-calcif__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-calcif__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-calcif__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-chirnc__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-chirnc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-chirnc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-choix-tech__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-choix-tech__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-choix-tech__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-aod-meca__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-aod-meca__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-aod-meca__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-asa__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-asa__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-asa__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-benza__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-benza__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-benza__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-hep__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-hep__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-hep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-inotrope__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-inotrope__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-inotrope__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-nitroprus__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-nitroprus__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-d-nitroprus__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-discord__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-discord__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-discord__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dissection__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dissection__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dissection__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dse__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dse__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-dse__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-effort__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-effort__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-effort__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-grossesse__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-grossesse__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-grossesse__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-inr__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-inr__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-inr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-lflg-parad__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-lflg-parad__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-lflg-parad__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-manoeuvres__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-manoeuvres__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-manoeuvres__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-pacemaker__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-pacemaker__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-pacemaker__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-prothese__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-prothese__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-prothese__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-ra-asympto__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-ra-asympto__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-ra-asympto__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-seuils-aorte__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-seuils-aorte__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-seuils-aorte__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-suivi__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-suivi__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/out/i35-suivi__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verdicts/I35_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I35/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/edits/I40_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-arythmies__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-b19__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-chagas-stades__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-clozapine__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-covid__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-2l__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-aza__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-bnz__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-cni__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-d-cortico__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-dallas__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-ecg__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-ecmo__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-eos__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-fulm-prono__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-gcm__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-genet__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-hstn__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-irm-signal__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-is-virus__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-lyme__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-mnemo-bach__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-risque__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-s-muscle__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-sport__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-strongy__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-triplem__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/jobs/i40-wcd__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-arythmies__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-arythmies__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-arythmies__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-b19__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-b19__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-b19__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-chagas-stades__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-chagas-stades__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-chagas-stades__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-clozapine__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-clozapine__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-clozapine__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-covid__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-covid__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-covid__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-2l__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-2l__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-2l__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-aza__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-aza__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-aza__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-bnz__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-bnz__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-bnz__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cni__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cni__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cni__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cortico__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cortico__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-d-cortico__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-dallas__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-dallas__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-dallas__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecg__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecg__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecg__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecmo__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecmo__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-ecmo__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-eos__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-eos__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-eos__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-fulm-prono__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-fulm-prono__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-fulm-prono__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-gcm__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-gcm__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-gcm__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-genet__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-genet__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-genet__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-hstn__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-hstn__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-hstn__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-irm-signal__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-irm-signal__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-irm-signal__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-is-virus__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-is-virus__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-is-virus__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-lyme__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-lyme__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-lyme__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-mnemo-bach__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-mnemo-bach__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-mnemo-bach__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-risque__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-risque__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-risque__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-s-muscle__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-s-muscle__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-s-muscle__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-sport__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-sport__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-sport__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-strongy__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-strongy__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-strongy__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-triplem__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-triplem__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-triplem__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-wcd__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-wcd__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/out/i40-wcd__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verdicts/I40_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I40/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/edits/I42_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-anticoag-fa__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-attr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-biomarq__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-cicatrice__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-fa__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-pk-myosine__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-redflags__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-stades__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/jobs/i42-takotsubo__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-anticoag-fa__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-anticoag-fa__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-anticoag-fa__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-attr__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-attr__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-attr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-biomarq__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-biomarq__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-biomarq__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-cicatrice__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-cicatrice__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-cicatrice__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-fa__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-fa__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-fa__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-pk-myosine__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-pk-myosine__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-pk-myosine__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-redflags__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-redflags__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-redflags__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-stades__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-stades__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-stades__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-takotsubo__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-takotsubo__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/out/i42-takotsubo__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verdicts/I42_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I42/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/edits/I44_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-athlete__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-atropine-test__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-automat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-bbd__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-bilan-bio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-d-fab__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-d-insuline__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-d-theo__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-digitox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-echap__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-eep__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-fa-infra__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-hautdeg__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-hemodyn__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-hypothyr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-imag__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-irm__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-mob1__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-neuromusc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-rvpace__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-sync-strat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/jobs/i44-tox__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-athlete__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-athlete__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-athlete__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-atropine-test__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-atropine-test__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-atropine-test__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-automat__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-automat__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-automat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bbd__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bbd__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bbd__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bilan-bio__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bilan-bio__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-bilan-bio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-fab__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-fab__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-fab__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-insuline__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-insuline__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-insuline__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-theo__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-theo__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-d-theo__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-digitox__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-digitox__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-digitox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-echap__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-echap__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-echap__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-eep__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-eep__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-eep__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-fa-infra__P2.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-fa-infra__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-fa-infra__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hautdeg__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hautdeg__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hautdeg__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hemodyn__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hemodyn__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hemodyn__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hypothyr__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hypothyr__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-hypothyr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-imag__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-imag__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-imag__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-irm__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-irm__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-irm__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-mob1__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-mob1__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-mob1__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-neuromusc__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-neuromusc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-neuromusc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-rvpace__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-rvpace__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-rvpace__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-sync-strat__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-sync-strat__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-sync-strat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-tox__P1.contreverif.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-tox__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/out/i44-tox__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verdicts/I44_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I44/verification.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/edits/I46_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-anaph__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-atcd-medic__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-coro__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-adre__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-antiep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-bicar__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-lipid__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-lyse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-nalox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-d-vaso__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-enfant__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-ep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-grossesse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-hyperk__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-hypoth__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-inexpl__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-intox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-neuro__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-pnothx__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-ppc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-pronostic__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-s-temoin__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/jobs/i46-temp__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-anaph__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-anaph__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-atcd-medic__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-atcd-medic__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-coro__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-coro__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-adre__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-adre__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-antiep__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-antiep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-bicar__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-bicar__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lipid__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lipid__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lyse__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-lyse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-nalox__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-nalox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-vaso__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-d-vaso__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-enfant__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-enfant__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ep__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-grossesse__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-grossesse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hyperk__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hyperk__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hypoth__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-hypoth__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-inexpl__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-inexpl__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-intox__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-intox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-neuro__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-neuro__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pnothx__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pnothx__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ppc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-ppc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pronostic__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-pronostic__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-s-temoin__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-s-temoin__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-temp__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I46/out/i46-temp__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/edits/I47_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-abl-tsv__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-adeno__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-ajmaline__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-atcd-medic__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-automat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-bilan-tv__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-brugada__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-cicatrice__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-credible__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-cv__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-amio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-bb__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-bbns__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-cci__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-ic__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-mg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-d-sotalol__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-dai__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-declench__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-digox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-dualite__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-ecg-brug__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-ecg-qt__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-eep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-effort__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-genet__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-grossesse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-holter__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-irm__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-k__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-mg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-msj__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-orage__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-pa__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-qtl__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-reentree__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-repol__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-reppre__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-schwartz__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-sport__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-standing__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-tamsi__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-tdp-tt__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-tolerance__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-trav__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/jobs/i47-wpw-asympt__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-abl-tsv__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-abl-tsv__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-adeno__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-adeno__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ajmaline__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ajmaline__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-atcd-medic__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-atcd-medic__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-automat__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-automat__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-bilan-tv__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-bilan-tv__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-brugada__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-brugada__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cicatrice__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cicatrice__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-credible__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-credible__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cv__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-cv__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-amio__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-amio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bb__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bb__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bbns__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-bbns__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-cci__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-cci__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-ic__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-ic__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-mg__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-mg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-sotalol__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-d-sotalol__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dai__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dai__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-declench__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-declench__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-digox__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-digox__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dualite__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-dualite__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-brug__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-brug__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-qt__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-ecg-qt__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-eep__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-eep__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-effort__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-effort__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-genet__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-genet__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-grossesse__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-grossesse__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-holter__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-holter__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-irm__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-irm__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-k__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-k__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-mg__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-mg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-msj__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-msj__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-orage__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-orage__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-pa__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-pa__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-qtl__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-qtl__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reentree__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reentree__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-repol__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-repol__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reppre__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-reppre__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-schwartz__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-schwartz__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-sport__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-sport__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-standing__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-standing__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tamsi__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tamsi__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tdp-tt__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tdp-tt__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tolerance__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-tolerance__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-trav__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-trav__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-wpw-asympt__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I47/out/i47-wpw-asympt__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/edits/I49_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-ablation__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-atcd-psy__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-atcd-subst__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-bilan-bio__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-bilan-bio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-cmie-crit__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-cmie-meca__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-commotio__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-couplage__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-crt__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-declench__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-e-auscult__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-ecg-base__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-effort__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-epi__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-erc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-erc__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-essa__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-pots-phys__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-pots-tt__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-prono__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-pvm__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-riva__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-rja__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-rosc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-standing__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/jobs/i49-termino__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ablation__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ablation__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-psy__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-psy__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-subst__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-atcd-subst__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-bilan-bio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-crit__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-crit__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-meca__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-cmie-meca__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-commotio__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-commotio__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-couplage__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-couplage__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-crt__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-crt__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-declench__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-declench__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-e-auscult__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-e-auscult__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ecg-base__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-ecg-base__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-effort__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-effort__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-epi__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-epi__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-erc__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-essa__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-essa__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-phys__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-phys__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-tt__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pots-tt__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-prono__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-prono__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pvm__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-pvm__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-riva__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-riva__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rja__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rja__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rosc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-rosc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-standing__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-standing__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-termino__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I49/out/i49-termino__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/edits/I71_pop.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-addrs__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-anti-impulsion__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-antithrombotiques__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-aortopathie-traitement__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-depistage__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-diam__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-endofuites__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-gen__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-genetique-interpretation__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-paroi__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/jobs/i71-seuils-thorax__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-addrs__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-addrs__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-anti-impulsion__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-anti-impulsion__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-antithrombotiques__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-antithrombotiques__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-aortopathie-traitement__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-aortopathie-traitement__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-depistage__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-depistage__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-diam__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-diam__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-endofuites__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-endofuites__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-gen__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-gen__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-genetique-interpretation__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-genetique-interpretation__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-paroi__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-paroi__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-seuils-thorax__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I71/out/i71-seuils-thorax__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/edits/I80_pop.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-antidotes__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-ddimeres__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-doses__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-duree__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-ep__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-fibrinolyse__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-phlegmatia__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-pompe__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-signes__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-test-thrombophilie__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-tih__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-virchow__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/jobs/i80-wells__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-antidotes__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-antidotes__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ddimeres__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ddimeres__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-doses__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-doses__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-duree__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-duree__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ep__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-ep__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-fibrinolyse__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-fibrinolyse__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-phlegmatia__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-phlegmatia__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-pompe__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-pompe__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-signes__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-signes__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-test-thrombophilie__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-test-thrombophilie__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-tih__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-tih__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-virchow__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-virchow__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-wells__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/I80/out/i80-wells__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/bilan_P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/bilan_P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_a.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_b.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_c.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_d.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop3.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop4.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop5.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop6.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/edits/Q21_pop7.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-arythmie__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-chirnc__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-cyan-sys__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-d-amio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-d-anticoag__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-ecg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-endoc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-heath__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-mwho__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-rope__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-rx__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-sport__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-switch-atr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/jobs/q21-transition__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-arythmie__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-arythmie__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-chirnc__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-chirnc__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-cyan-sys__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-cyan-sys__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-amio__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-amio__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-anticoag__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-d-anticoag__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-ecg__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-ecg__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-endoc__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-endoc__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-heath__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-heath__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-mwho__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-mwho__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rope__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rope__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rx__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-rx__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-sport__P2.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-sport__P2.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-switch-atr__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-switch-atr__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-transition__P1.html` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/Q21/out/q21-transition__P1.json` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/TACHE_PRODUCTION.md` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/TACHE_VERIFICATION.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/appliquer_justifications.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/finaliser.sh` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/manifeste.py` | delivery_report | GLOBAL | integration_target |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/verifier_sigles.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/REPRISE.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/appliquer_lot4.py` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/fenetres_existantes.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/items_I48_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/CONSIGNES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/TACHE_CONTREVERIF.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/TACHE_FENETRES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/TACHE_TEXTES.md` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline/I48_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_a.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_b.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_c.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_d.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_pop1.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_pop2.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_pop3.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/inline_out/I48_pop4.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-24h.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-adeno.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-antidote.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-aod.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-avk.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-brady-tachy.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-cardiopathies.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-causes-aigues.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-cg.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-cha.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-cognition.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-cv.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-cycle-variable.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-amio.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-dig.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-drone.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-flec.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-frein.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-sotalol.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-d-vernak.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-depist.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-e-bas-debit.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-e-ta.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-e-thyr.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-ecg-flutter.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-hasbled.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-ic-flutter.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-infraclin.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-inr.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-interactions.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-k-torsades.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-kick.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-laao.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-mitral.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-mnemo-abc.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-noeudav.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-periop.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-pip.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-preexc.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-reentree.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-remod-inverse.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-remod.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-rs-embolie.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-s-palp.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-saos.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-substrat.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-tachycm.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-thyr.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-troponine.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-virchow.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/i48-vp.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/jobs/pareto-i48-exam.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-24h.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-24h.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-adeno.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-adeno.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-adeno.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-antidote.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-antidote.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-antidote.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-aod.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-aod.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-aod.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-avk.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-avk.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-avk.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-bilan.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-bilan.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-bilan.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-brady-tachy.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-brady-tachy.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-brady-tachy.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cardiopathies.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cardiopathies.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-causes-aigues.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-causes-aigues.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cg.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cg.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cg.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cha.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cha.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cognition.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cognition.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cv.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cv.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cv.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cycle-variable.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-cycle-variable.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-amio.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-amio.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-amio.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-dig.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-dig.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-dig.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-drone.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-drone.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-drone.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-flec.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-flec.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-flec.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-frein.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-frein.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-sotalol.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-sotalol.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-sotalol.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-vernak.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-vernak.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-d-vernak.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-depist.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-depist.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-e-bas-debit.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-e-bas-debit.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-e-ta.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-e-ta.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-e-thyr.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-e-thyr.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-ecg-flutter.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-ecg-flutter.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-ecg-flutter.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-hasbled.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-hasbled.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-ic-flutter.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-ic-flutter.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-ic-flutter.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-infraclin.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-infraclin.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-inr.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-inr.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-inr.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-interactions.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-interactions.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-k-torsades.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-k-torsades.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-k-torsades.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-kick.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-kick.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-laao.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-laao.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-laao.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-mitral.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-mitral.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-mnemo-abc.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-mnemo-abc.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-mnemo-abc.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-noeudav.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-noeudav.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-periop.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-periop.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-periop.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-pip.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-pip.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-pip.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-preexc.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-preexc.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-reentree.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-reentree.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-remod-inverse.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-remod-inverse.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-remod.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-remod.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-rs-embolie.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-rs-embolie.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-s-palp.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-s-palp.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-saos.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-saos.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-saos.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-substrat.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-substrat.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-tachycm.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-tachycm.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-tachycm.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-thyr.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-thyr.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-troponine.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-troponine.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-troponine.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-virchow.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-virchow.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-vp.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/i48-vp.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/pareto-i48-exam.contreverif.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/pareto-i48-exam.html` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats/out/pareto-i48-exam.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/resultats_partiels.json` | delivery_report | GLOBAL | pull_request_base |
| `livraisons/Livraison Claude/C-01-Cardiologie/travail/lot4_I48_justification/workflow_justification.js` | delivery_report | GLOBAL | pull_request_base |

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


## main


## Limites

- 13 branches et 12 PR: pages REST 1 puis 2 vides; toutes les métadonnées PR et toutes les listes paginées de fichiers relues via le plugin GitHub.
- Inventaire figé à la tête PR12 b6db50cb2911fcbe0b09e64b79df03aab294e3df; le travail Claude ultérieur n'est pas reçu automatiquement.
- La source I48 publiée e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6 remplace l'ancienne cible a6f18a1 pour les comparaisons.
- 85 fichiers dans le manifeste Claude b6db50c : I48 + huit cours supplémentaires déclarés appliqués/contrôlés dans AVANCEMENT ; métadonnées lot4 I48 et résultats globaux anciens. Candidature détectée, non reçue et non injectée.
- Toutes les comparaisons ont été recalées par Git local exact sur e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6, aucun résultat de liste de fichiers tronqué par une limite API compare.
- I48 original b1f19c3 injecté et publié au commit e856ed1, arbre identique au commit local testé201c9c1. Pages run37688889857 réussi ; contenu servi vérifié et54contrôlespublics réussis. Le commit local201 n’est pas ancêtre du commit API e856 ; l’équivalence est prouvée par l’arbre Git81f5a8c.
- La livraison structurée Claude b6db50cb contient77fichiers de huitcours supplémentaires à contrôler, ainsi que quatre nouvelles propositions de fenêtresI48. Reçu de candidatures enregistré ; aucune injection de ces propositions et aucun succès technique annoncé par Claude repris comme contrôleCodex.
- Les rapports et les tests déclarés ne constituent pas une vérification médicale indépendante.
- Le routage est contrôlé contre les sources locales de la cible, avant les changements proposés.
- Aucune branche n'est fusionnée, aucun reçu créé et aucun commit publié par ce scanner.
