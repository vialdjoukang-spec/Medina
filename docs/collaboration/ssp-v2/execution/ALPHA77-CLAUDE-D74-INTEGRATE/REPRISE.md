# Reprise — ALPHA77-CLAUDE-D74-INTEGRATE (D74 — Méthémoglobinémie, fragment S06)

Sauvegarde demandée par le coordinateur (limite d'usage atteinte), 16.10.2026.

## Étape atteinte
- Garde : `acquire` réussi, puis `start` réussi (base `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`, worktree partiel, conversation `alpha77-claude-d74-integrate`). Réservation conservée, non libérée.
- Lectures faites : protocole agent de leçon, PROTOCOLE_ALPHA1_CLAUDE, EXIGENCE_CALCULS, EXIGENCE_SEMIOLOGIE ; modèle G72 (structure `revue/`, `integration/`, `livraison/`, `generer_recu.py`, reçu 0001) ; fichiers `D74_a`, `D74_b`, `D74_c` lus en entier.
- Aucun audit rédigé, aucune modification des sources canoniques (`chapters/D74/`, `glossary/d74.py` intacts).
- Aucun rapport Alpha 1 antérieur (`claude/alpha1/d74-*` absent du dépôt distant).

## Constats préliminaires (non encore vérifiés sur source)
- `D74_c` : onglet Sciences à 4 disciplines (Physiologie, Biochimie, Hématologie cellulaire, Génétique) ; **aucun sous-onglet Sémiologie** (exigence SEM-01 non remplie → MAJEUR).
- Figures : 3 SVG non anatomiques (courbe de dissociation qualitative, voies de réduction, familles génétiques) ; aucune figure anatomique IA repérée à ce stade.
- Calculs à recalculer : 1,5 g/dl sur 15 g/dl = 10 % ; sur 8 g/dl ≈ 19 % ; cas HFR 13 ml, 30,3 → 12,3 % ; posologies Proveblue (1–2 mg/kg = 0,2–0,4 ml/kg à 5 mg/ml ; 7 mg/kg, 4 mg/kg aniline/dapsone ; insuffisance rénale) ; perfusion 0,10–0,25 mg/kg/h ; 81,6 % ; 1/163 et 16/163.

## Suite exacte
1. Lire `D74_d`, `D74_pop1`, `D74_pop2`, `glossary/d74.py` ; empreintes SHA-256 des 7 fichiers.
2. Lire `PROMPT_VERITE.md`, `STYLE_REDACTION.md`, `PUBLICATION_ALPHA_RUNTIME.md`, `FIGURES_ANATOMIQUES_IA_2026-10-15.md`.
3. Audit MED (FI Proveblue®, Emla®, Fasturtec® datées ; EHA/EuroBloodNet 2021 ; Swissmedic 2011 ; HFR 2025), `calculs/inventaire.json`, `calculs/verifier.py`, `calculs/resultats.json` ; audit LANG.
4. Intégration : sous-onglet « Sémiologie fondamentale et analytique » en tête de `#pS` (`d74-s-semio`, îlots `d74-sm-*`, bloc clinique `data-semiology-clinical` dans pA comme G72), fenêtres, glossaire.
5. Contrôles (`test_v7.py --static D74`, `tests/audit_sciences.py`, build `--fragment S06`, captures bureau et 390 px), `revue/MED|LANG|SEMIO.json`, `integration/generer_recu.py preparer` puis `recu`, merge `origin/main`, `check`, push, PR.
