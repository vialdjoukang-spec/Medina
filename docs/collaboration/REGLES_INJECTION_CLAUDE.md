# Injection autonome de Claude et file d'audit de Codex — 8 octobre 2026

## Principe
Claude n'attend plus l'audit préalable de Codex pour injecter ses chapitres. Codex audite à son rythme, après injection. La qualité reste garantie par deux verrous : la vérification interne de Claude avant injection, l'audit de Codex après injection.

## Conditions d'injection par Claude (toutes obligatoires)
1. Revue par sous-agents et vérificateur indépendant terminée ; rapport du lot complet.
2. Contrôles réussis sur la tête actuelle de `main` : sigles `{}`, `test_v7.py --static`, `build_front.py --all-fragments`, `tests/audit_fragments.py`, `verify_course_native.cjs` (0 échec), tests unitaires.
3. `tools/livraison.py check-claude` conforme.
4. Aucune réserve bloquante de Codex encore ouverte sur ce chapitre.

## Droit de décision
Pour ses propres chapitres, Claude tranche les désaccords non bloquants avec Codex. Il applique la règle « la source la plus récente l'emporte dans le texte ; l'ancienne reste accessible par un mot vert ». Une erreur médicale démontrée par Codex reste bloquante et doit être corrigée en priorité.

## File d'audit de Codex
- Chaque injection de Claude ajoute une entrée à `docs/collaboration/FILE_AUDIT_CODEX.json`, avec le statut `a_auditer`.
- Codex traite la file dans l'ordre et met le statut à `audite_favorable` ou `reserves`, avec un lien vers son rapport.
- Une réserve bloquante après injection est corrigée par Claude dans le chapitre concerné, en priorité sur la production en cours.
- Tant que l'audit de Codex n'est pas favorable, le cours porte la mention « en audit croisé » dans le tableau de bord.
