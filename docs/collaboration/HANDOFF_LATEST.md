# MEDINA — dernière passation

Mise à jour : 7 octobre 2026. Lire [l’inventaire des livraisons](DELIVERIES_LATEST.md) avant de reprendre un travail. Il recense les branches et PR ; les [reçus](receipts/) conservent les preuves de réception et d’intégration.

## Livraisons de Claude retrouvées et intégrées

| Livraison | Sources et destination | État |
| --- | --- | --- |
| Alpha du 26 septembre — PR #1 | 435 fichiers ; cours, réécritures, glossaire, interface et audits historiques. | Déjà fusionnée le 27 septembre ; présence confirmée dans la branche actuelle. |
| I48 et CS — PR #8 | Quatre fichiers de cours I48 et les deux sources CS cardiovasculaires ; fragment S01. | Rapports ouverts, sources intégrées et contrôlées au commit `f5c83957a239a27b836b838063e97835cd80f4d9`. |

La PR #8 est fusionnée. Les deux rapports originaux restent dans `reviews/`, à leur emplacement initial. Trois passages I48 ont été adaptés après contre-lecture des sources et une formulation jugulaire a été nuancée. Voir [l’arbitrage d’intégration](reviews/2026-10-07/I48_CS/INTEGRATION_CODEX.md) et [le reçu détaillé](receipts/CLAUDE_I48_CS_2026-10-07.json).

La branche de Claude conserve ses commits. Claude peut déposer le prochain lot sur cette branche ou une nouvelle branche. La réception examine tous les chemins publiés, y compris les rapports historiques et les branches sans PR.

## Lot global toujours à relire

Base de la mission initiale : `bb134857e12245f46b4f329c1334ebd57251fcff`. Les enrichissements comprennent 30 cours dans cinq fragments et la Sémiologie CS cardiovasculaire. Les corrections I48/CS ci-dessus doivent être prises en compte pour éviter de réintroduire une ancienne formulation.

| Fragment | Cours |
| --- | --- |
| S01 — Cardiovasculaire | I00, I10, I21, I25, I30, I33, I34, I35, I40, I42, I44, I46, I47, I48, I49, I50, I70, I71, I80, Q21 |
| S02 — Respiratoire | J45, J44, J18, I26 |
| S07 — Immunitaire | D84, M32, M31, T78 |
| S10 — Locomoteur | M06 |
| T1 — Agents et thérapeutique | A41 |

[Mission globale](CLAUDE_AUDIT_GLOBAL_2026-10-07.md), [manifeste de la base](CLAUDE_REVIEW_SCOPE_2026-10-07.json), [sources communes](SOURCES_CANONIQUES.md) et [procédure de remise](reviews/README.md). La mission porte sur les quatre onglets, toutes les fenêtres, les figures, les quiz, les glossaires et les textes CS. Français professionnel, précis et fluide ; conserver les notions utiles.

## Contrôles exécutés sur l’intégration I48/CS

- Reconstruction des 22 fragments et de MEDINA global ; audit des fragments réussi, JavaScript valide et build reproductible.
- Audit statique I48/I70/I71/I80 et audit sciences des 30 cours réussis.
- 569 contrôles navigateur sciences/CS et quatre vérifications ciblées des textes I48 dans S01 : réussis, aucune erreur JavaScript.

Les [preuves de contrôle](../../audits/CLAUDE_INTEGRATION_2026-10-07/) se rapportent à cette intégration. Elles ne constituent pas un audit médical intégral.

## Travail restant

| Travail | État réel |
| --- | --- |
| Relecture intégrale des 30 cours et CS | À poursuivre ; seuls les lots ciblés reçus sont crédités. |
| R08 — fenêtre des épisodes auriculaires rapides | Réserve ouverte. |
| R11 — classe de l’évaluation du rythme dès 65 ans | Source primaire relue ; classe I C confirmée pendant la contre-lecture. |
| C10 — complément vasculaire de CS | Réserve ouverte. |
| Complétude CIM-11 des cinq fragments | Non établie ; catalogue local historique CIM-10-GM 2024. |
| PR #6 — accueil et QCM | Travail Codex distinct, encore en attente d’intégration. |

Lire [la règle CIM-11](../COMPLETUDE_CIM11.md) et [le relevé de couverture](../../audits/COMPLETUDE_2026-10-07/README.md). Aucun fragment n’est déclaré complet.

Après chaque lot : publier les sources et les contrôles, enregistrer réception, intégration et réserves dans un reçu, actualiser l’inventaire et cette passation, puis vérifier les liens GitHub. Le déploiement du site depuis `main` est contrôlé séparément.
