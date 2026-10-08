# Passation Claude — STOP demandé par Vial (8 octobre 2026, changement de chat)

**À lire en premier** : `docs/collaboration/instructions/CUMUL_INSTRUCTIONS_CLAUDE_CODEX.pdf` (245 règles obligatoires ; R-19.10 : captures systématiques levées) et `organisation/ETAT_DES_LIEUX_CLAUDE_2026-10-08.html`.

- **Branche** : `claude/vigilant-mayer-cevhwj` ; PR vialdjoukang-spec/Medina#16 (contrôles au vert, aucun fil ouvert). Le producteur n’écrit jamais dans `chapters/`, `glossary/`, `chapters.json` (garde `tools/espace.py garde`).
- **Remis à Codex** : C-01-Cardiologie v2 (76/76) et P-02-Pneumologie (53/53) dans `espace_partage/FRAGMENTS_CLAUDE_A_AUDITER_PAR_CODEX/`. Codex a réceptionné C-01 sans injection (7e5a648) ; P-02 non réceptionné. Aucun fragment INJECTÉ.
- **En production** : G-04 — 12/67 (K25, K57, K80, K35 contrôlés). Brouillons interrompus et plan : `livraisons/Livraison Claude/G-04-Gastroentérologie et hépatologie/travail/` (PLAN_COURS.md, BROUILLONS_INTERROMPUS_2026-10-08.md).
- **Outils** : `tools/pile_fragments.py`, `tools/consignes_pdf.py`, `tools/captures_chapitre.py` (optionnel désormais). Intégration : copie hors canonique, `chapters_additions.json`, contrôle sur une copie de `main` (`test_v7.py --static`, `build_front.py --fragment <ID>`).
- **Reprise** : vérifier les brouillons G-04, poursuivre le plan, puis E-06, H-08, G-10, M-12, R-14, O-17, O-18, M-19, E-22. Points d’arbitrage pour Vial : annexe B du cumul.
