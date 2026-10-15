# PROMPT DE TRANSITION — Claude MEDINA, Audit Alpha / ALPHA77 (15.10.2026, ~22 h Europe/Zurich)

Tu reprends le travail de la session `session_012rLPEdW6E6hLqqjusnCoMF`. Lis ce fichier en entier, puis `AGENTS.md` et `CLAUDE.md` de `main` à jour. Ce dossier (`docs/collaboration/claude-transition-2026-10-15/` sur la branche `claude/vigilant-faraday-x8bwa8`) conserve les outils et protocoles qui vivaient hors dépôt.

## 1. Ordres de Vial en vigueur (dans l'ordre)
1. Audit Alpha : lots de 7 leçons, **2 agents par leçon** ; audit médical agressif (Opus, effort élevé) et linguistique local sans changement de fond (Sonnet, effort élevé). Pas d'audit croisé.
2. **Figures anatomiques dessinées par IA : non recevables** (MAJEUR si l'origine IA est démontrée ; `ORIGINE_INCONNUE` = réserve). Remplacement par des originaux réels sourcés. Règle : `docs/collaboration/instructions/FIGURES_ANATOMIQUES_IA_2026-10-15.md`.
3. Moteurs propres à Claude : **Image_Clo_finder** (dans main : `tools/image_clo_finder.py`, couche sur `tools/image_codex_finder.py`, cache et budget partagés) et **7_Starter_Claude** (lot suivant seulement après clôture réelle du précédent ; arrêt à **77 leçons, premier lot inclus** ; à l'arrêt, couper les exécuteurs d'images, garder images et preuves).
4. **Sémiologie obligatoire** : dans chaque leçon, **1er sous-onglet de Sciences** « Sémiologie fondamentale et analytique », ouvert par défaut. Titre exact : « Pour la leçon : quelle est la sémiologie fondamentale et analytique ? ». S'y ajoute un bloc clinique `data-semiology-clinical` dans pA. Vial a choisi cette option A sur maquettes (pas de 5ᵉ onglet). Contrat : `docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml` ; grille SEM-01…SEM-24 : `EXIGENCE_SEMIOLOGIE.md` ici.
5. **Autonomie et droit de publication** (relayés par Codex, issue 107) : ne rien attendre ; avancer dans les missions préapprouvées ; laisser à chaque étape une trace visible par Codex (commentaire `[CLAUDE-ÉTAT]` sur l'issue 107 + fichiers sur les branches).
6. **Jauge verte permanente** dans chaque réponse à Vial (🟩/⬜) : jauge 7_Starter (leçons closes sur 77) et jauge d'intégration.

## 2. Gouvernance (ne jamais contourner)
Mission approuvée dans `main` (`.medina/missions/`), puis `python3 tools/ai_session_guard.py acquire <ID> --base <SHA main>`, puis `git worktree add -b <branche exacte> <dossier> <SHA>`, puis `start … --actor Claude --conversation <manifeste> --worktree <dossier>`. Aucune auto-approbation. Ne jamais forcer `main`. Une leçon n'est **close** que par son reçu Alpha dans main (`organisation/alpha-publications/Claude/<CODE>/`, phase `completed`, `audits.SEMIO`). Des rapports seuls ne clôturent rien.

## 3. État exact au moment de la transition
- Lot 1 (I61, G45, E11, E12, N18, D50, C77) : 14 audits ALPHA1 fusionnés (PR #124–#137), réservations libérées. Outil PR #141 fusionné.
- Missions **ALPHA77-CLAUDE-<CODE>-INTEGRATE** acquises et démarrées (base `abd681e5175db8c89e87dd7b83f96d0249d81cd7`), branches `claude/alpha77/<code>-integrate-g1`.
- Étapes par leçon : prép P → corrections W → sémiologie intégrée → revue P (`revue/MED|LANG|SEMIO.json`) → reçu Alpha → PR → fusion → libération.

| Leçon | État au moment de la transition | Action restante |
|---|---|---|
| **E11** | reçu Alpha `completed` VALIDE (c73f307f) ; **PR #147 ouverte** | vérifier la CI, fusionner, libérer la réservation `ALPHA77-CLAUDE-E11-INTEGRATE` → 1ʳᵉ leçon close |
| E12 | corrections de309165 ; revue mise à jour 6e287b46 (close) ; droits dans `droits/` | reçu bloqué par le défaut de l'outil (§ 4 bis) ; générateur `integration/generer_recu.py` |
| D50 | droits conservés (1b236155) ; note `integration/phase3_blocage.json` | reçu bloqué par le défaut de l'outil (§ 4 bis) ; générateur à refaire (l'ancien est dans le scratchpad perdu) |
| C77 | corrections 64257cb8 ; revue mise à jour 6ef663d6 (close) | régénérer le reçu avec les nouvelles empreintes de revue/ ; reçu bloqué (§ 4 bis) |
| I61 | revue close e0365fcc | W phase 3 en cours : ajout « ou taux > 100 ng/ml » dans _c et _pop1, puis mise à jour de revue/ par P, puis reçu (aucune figure nouvelle : pas concerné par § 4 bis) |
| G45 | revue close 97ba87d2 (sans bloquant) ; W applique 5 mineurs (ticagrélor hors indication FI Brilique, aspirine + dipyridamole sans FI, clopidogrel faible métaboliseur, OAC annexe 1, dates des sources) | ensuite P met à jour revue/, puis reçu (bloqué par § 4 bis : figures attribuées) |
| N18 | revue close 5bf53a9c (sans bloquant ; aucune figure Alpha nouvelle) | W phase 3 lancée : reçu sans modifier la leçon ; si valide → PR, fusion, libération. Retouche différée : « 5 mg oral » → « par voie orale » (pop1, fenêtre Eliquis) |

Vérifier l'état réel avant tout : `git fetch origin` puis lire chaque branche ; ne pas supposer que les agents de l'ancienne session ont fini.

## 4. Décisions du coordinateur (à maintenir)
- `tests/audit_sciences.py` exige un SVG dans chaque figure des Sciences ; il rejette donc à tort les images réelles. Ce n'est ni dans la CI ni dans `alpha_publication`. **Faux positif connu** consigné dans `integration/controles.json` ; **interdiction absolue** d'ajouter un SVG (factice ou de données) dans une figure d'image pour passer le test. Mission partagée de correction demandée à Codex (issue 107, `ALPHA77-CLAUDE-OUTIL-AUDITSCIENCES`). SEM-03 est précisé dans ce sens.
- Fichiers admis par `alpha_publication` : `<CODE>_a,_b,_c,_d,_pop1,_pop2` + `glossary/<code>.py`. **Aucun `_pop3`** : les fenêtres de sémiologie vont dans pop1/pop2. Pas de Pareto sur une section `data-semiology`.
- Choix différés (ne pas appliquer sans Vial) : espaces insécables globales (*Guide du typographe* romand, par script, mission partagée), « fibrillation atriale/auriculaire », groupe `LIENS` d'E11.
- N18 : 15 sigles gardent leur clé commune (ne pas redéfinir dans `n18.py`).
- Dans un worktree partagé par P et W : jamais `git stash`, `reset`, `checkout -- .`, `clean`. User-Agent neutre seulement : `MEDINA-ImageCloFinder/0.1 (+https://github.com/vialdjoukang-spec/Medina)`. Trois requêtes antérieures ont porté « vial.djoukang » ; Vial est informé.
- Le catalogue d'audit Claude compte 52 leçons (lots 7,7,7,7,7,7,10). Le plafond de 77 se complète, comme côté Codex, par 25 productions nouvelles prises dans la file de production Claude ; les missions du lot 2 (C72, G23, G58, G63, G64, G71, G72) ont été demandées à Codex et ne sont pas encore dans main.

## 4 bis. BLOQUANT OUTIL — `tools/alpha_publication.py` (fichier Codex, partagé)
Le contrôle « attribution invisible dans le cours » échoue toujours. Le cours est dans `<template id="ch-<CODE>">` (de `_a` à `_d`), les Sciences sont `hidden`, et l'ordre de concaténation vient d'un `set` (aléatoire). Tout reçu d'une leçon contenant une figure attribuée est donc refusé. Signalé à Codex (issue 107) avec une proposition de correction. Ne jamais contourner. C77 : reçu `0001.json` prêt mais NON poussé (commit local `ec1e645e`, qui sera perdu avec l'ancien conteneur : régénérer depuis `64257cb8`), corrections poussées en `64257cb8`, empreintes de revue/ à mettre à jour par P.

## 5. Réserves à rapporter honnêtement
- Revue SEMIO non indépendante : P relit la sémiologie qu'il a rédigée. Proposition : un relecteur tiers par leçon avant la clôture.
- D50 : frottis normal choisi par une IA ; un choix humain par Vial est demandé.
- Commons répond souvent 429 : aucune image non vérifiée insérée (I61 sans photo).
- Aucune revue IA ne vaut validation médicale humaine.

## 6. Reprise immédiate
1. `git fetch`, puis lire `main` (nouvelles missions, messages de Codex sur l'issue 107).
2. Restaurer les outils : copier `seven_starter.py`, `jauge/` et les protocoles de ce dossier dans le scratchpad de la nouvelle session, et y corriger les chemins codés en dur. Relancer 7_Starter et la jauge d'intégration, puis réinstaller le hook Stop et la ligne d'état dans `~/.claude/settings.json` (voir `jauge/`).
3. Pour chaque leçon : finir la phase 3 (corrections, mise à jour des empreintes de revue, reçu valide par `python3 tools/alpha_publication.py --before abd681e5… --after HEAD`), ouvrir la PR, la fusionner une fois les contrôles verts, libérer la réservation avec son motif, puis publier `[CLAUDE-ÉTAT]` sur l'issue 107.
4. Une fois les 7 reçus fusionnés : 7_Starter passe au lot 2, dès que les missions sont dans main.
