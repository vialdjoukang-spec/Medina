## Travail en conversations parallèles — 15 octobre 2026

Pour S08/S05/S04/S06, lire [le protocole par conversation](docs/collaboration/instructions/CONVERSATIONS_PARALLELES_2026-10-15.txt) et [son PDF](docs/collaboration/Medina-protocole-collaboration.pdf). Une tâche, un cours, un rôle, un worktree et des chemins propres ; intégration séquentielle des fichiers partagés. Plusieurs conversations d’une même IA sont possibles sur des chemins distincts. La politique commune de parité et de publication reste applicable.

# REPRISE DE SESSION — règle absolue (Vial, 15.10.2026, actualisée le 15.10.2026 après-midi)

Toute nouvelle session Claude lit **ce fichier seul** et reprend sans relire l'historique.
L'état réel se lit dans `organisation/CYCLES_CLAUDE.json` (ne jamais se fier à une jauge recopiée ici).

## Règles permanentes
- Réponses au propriétaire : ultra-concises ; « captures + FIN PUBLIÉ + lien » et jauge en leçons publiées / 120 et cycles Novo / 9.
- **Projet Novo_12** (`organisation/novo_12/PLAN_NOVO_12.json`) : 12 leçons par cycle (3 par système), préparées ensemble ;
  publication par la garde existante, quatre leçons à la fois, dans l'ordre du plan tétrade.
- Distributeur d'agents : skill `.claude/skills/agent-distributor/SKILL.md`, veille `tools/distributor_veille.py`.
- Veille Codex : `tools/clov2_veille.py --boucle 600` ; lire les messages de Codex (issue 97) et les pondérer.
- **Tout refus ou blocage est transmis aussitôt à Codex** (commentaire dans l'issue 97) : il est là pour assainir le chemin (Vial, 15.10.2026).
- Délégation de Vial : `docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md`.
- Revues auteur **datées après le démarrage du cycle** de la leçon (la garde refuse toute preuve antérieure) : une leçon
  préparée en avance reçoit une vraie revue auteur dans son cycle, jamais une date réécrite.
- Matrice suisse : la matrice auteur reste « pending_independent_review » ; un agent contrôleur distinct produit
  `preuves/contexte_suisse_controle.json` en vérifiant chaque décision.
- Chaque injection met à jour l'empreinte de `chapters.json` dans `nosology/integrity.json` et lance `tools/refresh_gauges.py`.
- Une étape par poussée sur main (contrôles, injection, publication séparés).

## Historique accompli (NE PAS REJOUER)
- `tools/claude_chaine_main.sh` : exécuté une fois le 15.10.2026 ; **ne plus jamais le relancer** (il reconstruit d'anciens arbres).
- Cycles 1 et 2 publiés et clôturés ; Cycle 3 ouvert le 15.10.2026.

## Prochaines actions
1. Terminer le Cycle 3 : publier E05 (après un déploiement contenant ses sources), injecter et publier N04 puis D69, clôturer
   (`tools/cycle_claude_stage.py close 3`), ouvrir le 4 (`start 4 --direct`).
2. Novo N1 (cycles 4–6) : dossiers et rédactions dans `livraisons/Livraison Claude/*/travail/CYCLE_0[4-6]_*` ;
   à l'ouverture de chaque cycle : revue auteur datée, matrice de contrôle, contrôle à 4 captures, injection, publication.
3. Novo N2 à N9 selon le plan.

Branche de travail : `claude/vibrant-johnson-7k5okg`. Permissions : `.claude/settings.json` (JSON valide, un seul objet).
