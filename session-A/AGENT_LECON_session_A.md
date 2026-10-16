# Agent de leçon — chaînage Alpha77 Claude (ordre de Vial, 16.10.2026)

Tu es l'unique agent d'UNE leçon `<CODE>`. Tu fais tout, dans l'ordre : audit médical, audit linguistique, intégration
(corrections, complétion, pédagogie, fenêtres), contrôles, reçu de publication, PR. Un agent neuf est lancé pour chaque
leçon (recyclage voulu pour garder la performance) : ne présume rien d'une leçon précédente.

## 0. Mission, isolement, garde (règles anti-conflit, non négociables)
- Mission : `ALPHA77-CLAUDE-<CODE>-INTEGRATE` (manifeste dans `origin/main:.medina/missions/`). Branche exacte :
  `claude/alpha77/<code>-integrate-g1`. Tu n'écris QUE dans ses chemins : `chapters/<CODE>/`, `glossary/<code>.py`,
  `assets/img/<code>/alpha/claude/`, `organisation/alpha-publications/Claude/<CODE>/`,
  `docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-<CODE>-INTEGRATE/`. Rien d'autre (ni moteur, ni fichier partagé).
- Démarrage (depuis /home/user/Medina, sans y écrire) :
  `git fetch -q origin main medina/session-registry` ; `B=$(git rev-parse origin/main)` ;
  `python3 tools/ai_session_guard.py acquire --base $B ALPHA77-CLAUDE-<CODE>-INTEGRATE` ;
  worktree partiel `W=/tmp/claude-0/-home-user-Medina/bd99f81d-6b1e-5698-bd58-22e14f9e16b4/scratchpad/lecons/<CODE>` :
  `git worktree add -q --no-checkout -B claude/alpha77/<code>-integrate-g1 $W $B`, puis dans $W
  `git sparse-checkout set --cone chapters/<CODE> glossary tools tests engine shell assets/img/<code> organisation/alpha-publications .medina docs/collaboration/betta docs/collaboration/instructions docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-<CODE>-INTEGRATE`
  (ajoute ce dont les outils ont besoin, en lecture), `git checkout -q`, puis
  `python3 tools/ai_session_guard.py start --base $B --worktree $W --actor Claude --conversation alpha77-claude-<code>-integrate ALPHA77-CLAUDE-<CODE>-INTEGRATE`.
- Jamais de force-push, jamais de push sur une autre branche, jamais `git stash` nu, jamais de modification de `main`.

## 1. Lire d'abord
`docs/collaboration/betta/PROMPT_VERITE.md`, `docs/STYLE_REDACTION.md` (git show origin/main:…),
`.../scratchpad/audits/PROTOCOLE_ALPHA1_CLAUDE.md` (A = MED, B = LANG), `EXIGENCE_CALCULS.md`, `EXIGENCE_SEMIOLOGIE.md`,
`docs/collaboration/instructions/PUBLICATION_ALPHA_RUNTIME.md`, `docs/collaboration/instructions/FIGURES_ANATOMIQUES_IA_2026-10-15.md`.
Modèle complet d'une intégration close à imiter (structure des dossiers, `revue/MED.json`, `revue/LANG.json`,
`revue/SEMIO.json`, `integration/corrections.json`, `integration/controles.json`, `livraison/`, captures, reçu
`organisation/alpha-publications/Claude/G72/0001.json`, script `integration/generer_recu.py`) :
`origin/main:docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-G72-INTEGRATE/`.
Si des rapports d'audit déjà produits existent pour ta leçon sur `origin/claude/alpha1/<code>-med-g1` ou
`origin/claude/alpha1/<code>-lang-g1` (`git ls-remote`), lis-les et repars d'eux : ne refais pas ce qui est juste,
vérifie ce qui ne l'est pas.

## 2. Audit MED puis LANG
Exhaustif, sources suisses puis européennes, FI Swissmedic datée pour toute posologie, AUCUNE recommandation
américaine comme conduite, rien de mémoire. Calculs : inventaire scripté, recalcul par `calculs/verifier.py` conservé,
« ne laisse rien passer ». Sémiologie = 6e sous-onglet de Sciences. Rapports dans `revue/`.

## 3. Intégration (objectif de Vial)
Complétion médicale rigoureuse, amélioration et pédagogie : corrige chaque BLOQUANT/MAJEUR, comble les lacunes
sourcées, ajoute une fenêtre explicative (mot interactif) partout où une notion le demande, garde le plan monographique,
le contrat HTML, le glossaire (`build_medina.audit()` → `{}`), le français de `STYLE_REDACTION.md`. Figures anatomiques
dessinées par IA : remplace par des figures réelles sourcées et licenciées (`tools/image_clo_finder.py`) ou retire-les.
Aucune validation médicale humaine prétendue.

## 4. Contrôles avant push
`python3 test_v7.py --static <CODE>` OK ; `python3 tests/audit_sciences.py --base $B --codes <CODE>` (expliquer tout échec) ;
construction du fragment (`MEDINA_OUT=<scratch> python3 build_front.py --fragment <FRAGMENT>`) ; deux captures réelles
(ouverture + fenêtre) bureau et 390 px ; reçu Alpha `organisation/alpha-publications/Claude/<CODE>/0001.json` (ou
le numéro suivant) généré comme pour G72 ; `git status` ne montre que tes chemins ;
`python3 tools/ai_session_guard.py check --base $B --head $(git rev-parse HEAD) --branch claude/alpha77/<code>-integrate-g1` → passed.
Avant le push, intègre `origin/main` (merge, pas rebase) et refais `check`.

## 5. Publication
`git push -u origin claude/alpha77/<code>-integrate-g1`. Ouvre la PR vers `main` avec l'outil MCP GitHub
(`mcp__github__create_pull_request`, chargé via ToolSearch) : titre « Alpha77 <CODE> — <intitulé> : audit et intégration »,
corps en français court (constats graves, corrections, calculs relevés/recalculés/faux, contrôles, lacunes), finissant par
🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015STHmuYWNmuSZzRgs2rHdW
Commits terminés par :
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015STHmuYWNmuSZzRgs2rHdW
N'écris aucun identifiant de modèle dans les fichiers, commits ou PR. Ne fusionne pas (Vial fusionne).
Ne libère pas la réservation : elle reste active jusqu'à la fusion.

## 6. Réponse finale (structurée)
`code`, `pr` (numéro), `sha`, `bloquants`, `majeurs`, `calculs` (relevés/recalculés/faux), `fenetres_ajoutees`,
`lacunes` (liste), `statut` = `audite_pr_ouverte` | `bloque` (avec la raison exacte).
