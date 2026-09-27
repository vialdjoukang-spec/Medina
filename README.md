# MEDINA — code source

Atlas pédagogique de médecine par systèmes pour l’examen fédéral suisse. Voir `CLAUDE.md` (démarrage) et `PROMPT_MEDINA.md` (règles complètes et état).

- Construire : `python3 build_front.py` → `MEDINA.html` (un seul fichier autonome, cours compressés).
- Tester : `python3 test_v7.py <codes>`.
- Empaqueter / restaurer : `pack_v7.py` → `MEDINA_SOURCES.json` ; `restore.py`.
