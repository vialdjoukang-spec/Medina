# MEDINA — code source

Atlas pédagogique de médecine par systèmes pour l’examen fédéral suisse. Voir `CLAUDE.md` (démarrage) et `PROMPT_MEDINA.md` (règles complètes et état).

- Construire : `python3 build_front.py` → `MEDINA.html` (un seul fichier autonome, cours compressés).
- Contrôle courant des chapitres : `python3 test_v7.py <codes>`.
- `test_preview.py` est l’outil d’aperçu du 28 septembre 2026. `pack.py` l’empaquette encore ; ce fichier et `pack.py` restent en place. Ce n’est pas le contrôle des chapitres.
- Empaqueter / restaurer : `pack_v7.py` → `MEDINA_SOURCES.json` ; `restore.py`.
- Versions prouvées des instructions, avec la délégation non fusionnée : [docs/collaboration/REFERENCES_NAVIGATION.md](docs/collaboration/REFERENCES_NAVIGATION.md).
