# Exigences cumulées de Vial — 8 octobre 2026 (Claude et Codex)

Ce fichier rassemble toutes les exigences en vigueur. Il complète [COORDINATION.md](../../COORDINATION.md) et le [protocole par fragment](PROTOCOLE_FRAGMENTS_2026-10-08.md). En cas de conflit, la consigne la plus récente de Vial l'emporte.

## 1. Organisation et espaces
- **Fragments cibles.** Claude : P-02-Pneumologie, G-04, E-06, H-08, G-10, M-12, R-14, O-17, O-18, M-19, E-22. Codex : I-03-Infectiologie, N-05, N-07, O-09, O-11, I-13, U-15, D-16, D-20, M-21. C-01-Cardiologie garde son partage historique.
- **Espaces propres.** Claude dépose dans `espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX/`, Codex dans `espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE/`. Chaque IA écrit seulement sur sa branche, ses fichiers et ses fragments. Toute opération passe par `tools/espace.py`.
- **Unité de remise : le fragment entier**, achevé et auto-revu. Un seul audit croisé : l'autre IA relit, corrige sur place, puis injecte. Un fragment INJECTÉ est immuable. Arrêt total après les 22 fragments, avec un rapport de complétion.
- **Parallélisme** : plusieurs sous-agents dans un chapitre, un seul auteur par fichier.

## 2. Modèle et niveau de rédaction
- Rédaction et revue en **Opus** uniquement, au niveau premium. Sonnet est écarté. Chaque chapitre est revu par Opus à sa fin, avant la remise.
- Les chapitres rédigés depuis le début de la session du 8 octobre sont **réécrits à ce niveau** (pour Claude : J09 — Grippe (P-02-Pneumologie)).

## 3. Style
- Français direct, précis, concis et professionnel, en phrases complètes ; lecture agréable.
- Aucune phrase lourde, aucune évidence ni banalité, aucun remplissage. Chaque phrase apporte une information.
- Densité informative maximale à nombre de mots minimal : économie de mots, pas de pauvreté.
- Fenêtres cliquables (mots verts) pour les mécanismes, les preuves, les contentieux et les précisions. Le texte principal garde les décisions.
- Chaque affirmation est justifiée (mécanisme, conséquence, limite) et sourcée par la source primaire applicable la plus récente. L'ancienne version reste accessible, datée, dans une fenêtre.
- Posologies et autorisations suisses : information professionnelle de compendium.ch, lue et datée.
- Tableaux seulement pour classer, énumérer ou comparer, avec des cellules brèves.
- Pas de métaphores, de jeux de mots ni de mentions de la fabrication du cours (« îlot », « cet îlot »).
- Abréviations : clé de glossaire obligatoire ; `build_medina.audit()` renvoie `{}`.

## 4. Interface (portail et 22 fragments)
- **Un fragment = un frontend distinct**, qui ne contient que sa spécialité.
- **Police** : Atkinson Hyperlegible Next (Braille Institute, conçue pour distinguer chaque glyphe), embarquée dans le fichier ; police de cours par défaut.
- **Contraste élevé** partout : texte principal quasi noir sur fond clair ; aucun texte gris pâle ; texte blanc sur couleur vive avec un contraste d'au moins 4,5:1.
- **Couleurs vives et distinctes** : une par spécialité au portail, une par catégorie dans chaque fragment. Elles doivent attirer l'œil d'un lecteur au regard dispersé.
- **Catégories** : rectangles compacts au nom sobre, avec le code discret en haut à droite. Un clic ouvre une page titrée par la catégorie, dont les chapitres sont rangés sur **deux colonnes** avec un contraste suffisant sur fond coloré.
- Accueil clair et agréable. **Thème clair uniquement**, jamais de mode sombre.
- Montrer les changements par **captures d'écran** pendant le travail.

## 5. Contrôles avant toute remise
`build_medina.py <CODE>` (0 abréviation non couverte), `test_v7.py --static <CODE>` et `test_v7.py <CODE>`, `build_front.py --all-fragments`, `tests/audit_fragments.py`, `node tests/verify_fragment_frontends.cjs`, puis les tests unitaires. Une revue par IA ne vaut pas validation par un médecin.
