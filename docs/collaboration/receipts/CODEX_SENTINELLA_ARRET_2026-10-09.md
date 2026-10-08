# Arrêt de Codex_Sentinella — 9 octobre 2026

Instruction directe de Vial : « plus besoin de sentinelle ».

- Le workflow GitHub `Codex_Sentinella — livraisons Claude` (ID `378914963`) a été désactivé via GitHub Actions ; état vérifié `disabled_manually`.
- L'exécution encore active `37858488036` a reçu une demande d'annulation, puis son état `completed/cancelled` a été vérifié.
- Les 13 issues ouvertes portant le label `codex-sentinella` ont été closes ; leur historique reste consultable dans GitHub.
- Le fichier `.github/workflows/codex_sentinella.yml` est retiré de la branche Codex pour supprimer les déclencheurs sur push, pull request et calendrier après intégration.

Le script historique `tools/codex_sentinella.py` et ses anciennes preuves restent dans le dépôt comme archives inactives. Aucun processus local Sentinella n'était actif lors du contrôle. Cette décision n'interrompt pas la rédaction des cours du fragment I-03.
