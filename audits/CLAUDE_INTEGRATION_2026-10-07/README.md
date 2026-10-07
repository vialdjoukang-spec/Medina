# Contrôles de l'intégration Claude I48 et CS

Contenu intégré : `f5c83957a239a27b836b838063e97835cd80f4d9`, arbre `8b39acdf91589b4e9c778da7b81c3824ef6e0409`. Le même arbre de contenu a été contrôlé localement avant sa publication.

| Contrôle | Résultat |
| --- | --- |
| `python3 build_front.py --all-fragments` | 22 fragments reconstruits. |
| `python3 tests/audit_fragments.py` | JavaScript valide, build reproductible. |
| `python3 test_v7.py --static I48 I70 I71 I80` | OK. |
| `python3 tests/audit_sciences.py` | 30 cours ; aucune erreur. |
| `node tests/verify_sciences_cs.cjs` | 569 contrôles réussis, aucune erreur JavaScript ; Chromium 153.0.8010.0. |
| Vérification navigateur ciblée I48 | Texte ECG visible dans le cours, la fenêtre de dépistage et le Pareto ; aucune erreur JavaScript. |
| `python3 build_front.py` | MEDINA global reconstruit. |
| Scanner de collaboration | Pagination, reçus au commit cible, routage, sorties dérivées et distinctions d'état contrôlés par ses tests. |

[Résultats sciences/CS](science-cs-browser-results.json) et [résultats ciblés I48](i48-browser-results.json). Les empreintes des six sources sont conservées dans [le reçu](../../docs/collaboration/receipts/CLAUDE_I48_CS_2026-10-07.json).

Les trois adaptations I48 et la nuance jugulaire figurent dans [l'arbitrage](../../docs/collaboration/reviews/2026-10-07/I48_CS/INTEGRATION_CODEX.md). Les rapports de Claude sont conservés sans réécriture. R08 et C10 restent ouverts ; l'audit intégral des 30 cours et la complétude CIM-11 ne sont pas certifiés par ces contrôles.
