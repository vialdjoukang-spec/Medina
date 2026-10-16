# Reprise — ALPHA77-CLAUDE-D73-INTEGRATE (16.10.2026)

Sauvegarde demandée par le coordinateur (limite d'usage atteinte). Aucune source canonique modifiée.

## Étape atteinte
- Réservation acquise (`ai_session_guard.py acquire`, registre 9afa2d7c) et mission démarrée (`start` réussi) sur la base `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`.
- Worktree partiel créé, branche `claude/alpha77/d73-integrate-g1`.
- Lectures faites : PROMPT_VERITE, STYLE_REDACTION, PROTOCOLE_ALPHA1_CLAUDE, EXIGENCE_CALCULS, EXIGENCE_SEMIOLOGIE, PUBLICATION_ALPHA_RUNTIME, FIGURES_ANATOMIQUES_IA, modèle G72 (generer_recu.py, controles.json, inventaire_images.json, structure sémiologie de G72_c.html, validateur `tools/starter_codex.py` § semiology).
- Aucun audit Alpha 1 antérieur pour D73 (`git ls-remote` vide).
- Lecture de la leçon commencée : `D73_a.html` lu (îlots d73-0 à d73-6) ; `_b`, `_c`, `_d`, `_pop1`, `_pop2`, `glossary/d73.py` non encore lus.

## Suite exacte
1. Finir la lecture des sept fichiers ; empreintes SHA-256 de départ.
2. Audit MED (sources suisses puis européennes, FI Swissmedic datée), inventaire et recalcul des calculs (`calculs/inventaire.json`, `calculs/verifier.py`, `calculs/resultats.json`) ; audit LANG ; grille SEM-01 à SEM-24 ; rapports dans `revue/` (MED.json, LANG.json, SEMIO.json).
3. Intégration : corrections, sémiologie en premier sous-onglet de `#pS` (`d73-tab-semio`, `d73-s-semio`, sections `data-semiology` normal/signs/mechanisms/examination/interpretation/differentials/urgency/limits/sources, bloc `data-semiology-clinical="D73"` dans pA), fenêtres, glossaire ; figure 1 de `_a` = schéma non anatomique (recevable si sourcé).
4. Contrôles (test_v7 --static, audit_sciences, build fragment, captures bureau et 390 px), `integration/generer_recu.py` (modèle G72), reçu `organisation/alpha-publications/Claude/D73/0001.json`, merge origin/main, `check`, push, PR.
