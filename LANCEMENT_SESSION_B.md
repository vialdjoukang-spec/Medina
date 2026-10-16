# Session B — chaînage Alpha77 Claude en sens inverse (ordre de Vial, 16.10.2026)

Tu es la session B. La session A traite les 38 leçons existantes dans l'ordre G73 → D74 ; tu les traites en sens
INVERSE, deux leçons par cycle, un agent neuf (sous-agent, effort élevé) par leçon, les deux agents d'un cycle en
parallèle, cycle suivant dès que les deux ont fini. Pas d'attente de la fusion : chaque leçon a ses propres chemins.

File B : D74 D73 · D71 C96 · C94 C93 · N27 N12 · E59 E58 · E56 E54 · E52 E51 · E50 E46 · E45 E41 · E34 R27 ·
R26 I67 · I65 I62 · G99 G98 · G97 G96 · G94 G93 · G92 G91 · G90 G83 · G82 G81 · G80 G73.

## Démarrage
1. Lis CLAUDE.md, AGENTS.md, REPRISE_SESSION.md (règles permanentes : notification push chaque fois que Vial doit
   agir ; vérifier le déploiement Pages après chaque fusion).
2. `git fetch origin main medina/alpha77-chainage medina/session-registry`.
3. Lis : `git show origin/medina/alpha77-chainage:AGENT_LECON.md` (protocole complet d'un agent de leçon), puis
   `…:PROTOCOLE_ALPHA1_CLAUDE.md`, `…:EXIGENCE_CALCULS.md`, `…:EXIGENCE_SEMIOLOGIE.md`. Copie ces quatre fichiers dans
   ton répertoire temporaire et donne leur chemin à chaque agent.
4. Vérifie que `origin/main:.medina/missions/ALPHA77-CLAUDE-<CODE>-INTEGRATE.json` existe (PR 255 fusionnée).

## Anti-collision (la garde centrale fait foi)
- Chaque agent commence par `python3 tools/ai_session_guard.py acquire --base $(git rev-parse origin/main)
  ALPHA77-CLAUDE-<CODE>-INTEGRATE`. Si la mission est déjà active (prise par la session A), l'agent s'arrête aussitôt
  sans rien écrire et tu passes à la leçon suivante de ta file.
- Deux refus consécutifs = les deux files se sont rejointes : termine le cycle en cours et arrête-toi.
- Jamais de force-push, jamais `git stash` nu, aucun fichier partagé (moteur, `.github`, `tools`, `.medina`), jamais
  de fusion : Vial fusionne avec « Create a merge commit ».
- Les branches de leçon sont `claude/alpha77/<code>-integrate-g1` ; ne pousse sur aucune autre.

## Publication et jauge
- Chaque agent ouvre sa PR (outil MCP GitHub). Envoie à Vial une notification push par PR prête.
- La jauge de Vial est tenue par la session A à partir des PR et des branches sur GitHub : tu n'as rien à y écrire.
- Fin de chaque leçon : réponds en une ligne (code, PR, bloquants, majeurs, calculs faux).
