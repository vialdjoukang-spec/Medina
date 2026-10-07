# Accusés de réception et intégrations

Un reçu est écrit par l'agent qui ouvre et intègre une livraison. Il identifie son auteur, sa branche, sa tête exacte (`head_sha`), la date de réception, les sources, les fragments et les réserves. Après intégration, il donne `integration_commit` ; les contrôles réellement exécutés sont associés à `verification_commit` et `checks`.

Le scanner vérifie que ces commits appartiennent à la branche d'intégration. Une déclaration sans cette preuve ne transforme pas « reçu » en « intégré ». Une fusion ne certifie pas le fond médical ni la complétude CIM-11.

- `CLAUDE_ALPHA_2026-09-26.json` : livraison historique déjà fusionnée ; pas de validation médicale supplémentaire.
- `CLAUDE_I48_CS_2026-10-07.json` : réception, intégration, adaptations, empreintes et contrôles du lot I48/CS.

Conserver les reçus existants. Un nouveau lot, même sur la même branche, reçoit un nouveau reçu lié à sa propre tête. Les rapports originaux restent conservés ; les adaptations sont exposées dans un rapport d'intégration séparé.
