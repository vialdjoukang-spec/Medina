# Passation Claude — 9 octobre 2026

Branche : `claude/inspiring-maxwell-rjor0z` (au-dessus de `main`). Le blocage venait du contrôle de sécurité de la session précédente, non du dépôt ; `.claude/settings.json` (permissions) a été élargi par Vial sur `main`.

## Fait et publié
- PR #32 : travail de PR #20 injecté, Codex arrêté, scellement (désactivé depuis par Vial dans `tools/sceller.py`, ligne 78 : `if False:`).
- PR #33 : 1 766 liens vérifiés dans 15 leçons de cardiologie ; liens réparés J93, J45, J09. Publié (Pages, commit `3f43d7a`).

## Sauvegardé sur la branche, à terminer
P-02-Pneumologie, vague 1 (relecteur distinct, deux passes, aucune réserve bloquante) :
- `chapters/I27`, `glossary/i27.py` — Hypertension pulmonaire et autres maladies des vaisseaux pulmonaires (couvre I27, I28)
- `chapters/J47`, `glossary/j47.py` — Bronchiectasies (J47)
- `chapters/J80`, `glossary/j80.py` — Syndrome de détresse respiratoire aiguë de l’adulte (J80)
- Rapports : `livraisons/Livraison Claude/P-02-Pneumologie/travail/<CODE>/rapport_relecture.md`

En cours dans la session précédente (peut-être inachevé) : J81 — Œdème pulmonaire non cardiogénique ; J12 — Pneumonies virales et à autres micro-organismes (J12, J16, J17) ; J21 — Bronchiolite aiguë et infection aiguë des voies respiratoires inférieures (J21, J22). Vérifier `travail/<CODE>/rapport_relecture.md` et `chapters/<CODE>/` ; relancer la relecture si absente.

## Étapes suivantes
1. Ajouter I27, J47, J80 (puis J81, J12, J21) à `chapters.json` (`code`, `covers`, `title`, `integrated: true`) et à `organisation/course_groups.json` (`owner: "S02"`, `scope`).
2. `python3 -c "import build_medina as b; print(b.audit())"` doit renvoyer `{}` ; tests `python3 -m unittest discover -s tests -p 'test_*.py'` ; `MEDINA_OUT=$PWD/dist python3 build_front.py && python3 build_front.py --all-fragments && python3 tests/audit_fragments.py`.
3. `python3 tools/sceller.py enregistrer`, commit, PR vers `main`, fusion, vérifier Pages.
4. Vagues suivantes P-02 (restent : J60–J65+J92, J66–J67, J68–J70, J82, J95, J98–J99, R04, R05, R06), puis G-04, E-06, H-08 (`organisation/FILE_FRAGMENTS_CLAUDE.json`). Chaîne : rédacteur → relecteur distinct (deux passes, 4 dimensions, sources suisses puis européennes, FI Swissmedic, chaque source = lien vérifié par PMID/DOI/URL 200).
