# REPRISE DE SESSION — règle absolue (Vial, 15.10.2026)

Toute nouvelle session Claude lit **ce fichier seul** et reprend sans relire l'historique.

## Règles permanentes
- Réponses au propriétaire : ultra-concises ; seulement « captures + FIN PUBLIÉ + lien » et la jauge `n/30`.
- Modèles : recherche Opus (effort moyen→élevé), rédaction Sonnet 5.5 moyen, mécanique Sonnet moyen. Interdit de rédiger faux.
- Cycles 3→30 : recherche + rédaction + contrôle coordinateur (4 captures) + publication directe ; **aucun audit avant le Cycle 30**.
- Un seul cycle actif. Chaîne : skill `.claude/skills/cycle-medina/SKILL.md`. Garde : `tools/cycle_claude.py` (ne jamais l'affaiblir).

## État au 15.10.2026
- Cycle 1 : publié et audité (main). Jauge **1/30**.
- Cycle 2 (G45, E10, N18, D64) : 4 leçons contrôlées, `PRET_A_INJECTER` dans `organisation/CYCLES_CLAUDE.json`.
- Cycle 3 (I61, E05, N04, D69) : rédigé dans `livraisons/Livraison Claude/*/travail/CYCLE_03_*` ; reste contrôle + publication.
- Branche de travail : `claude/great-cerf-uizsml`.

## Prochaines actions, dans l'ordre
1. `bash tools/claude_chaine_main.sh` puis pousser C1, C2, C3 vers `main` (avances rapides ; la garde exige des étapes séparées).
2. Injection Cycle 2 une leçon à la fois G45→E10→N18→D64 : copie canonique (chapters/, glossary/, assets/img/cycle2/), ajout `chapters.json`,
   `python3 tools/sceller.py enregistrer`, reçu d'injection, `tools/cycle_claude_stage.py stage CODE INJECTE`, garde, push main,
   attente Pages, relecture publique, `stage CODE PUBLIE_VERIFIE`. Puis `close 2`.
3. Cycle 3 : `start 3 --direct`, contrôle de chaque leçon (`/tmp`-libre : script type dans `tools/cycle_claude_control.py`), injection, publication.
4. Cycles 4→30 : `/cycle-medina n`.

## Permission requise
`git push` vers main : règle `Bash(git push:*)` dans `.claude/settings.json` (déjà sur main) ou approbation manuelle.
