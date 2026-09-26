# REPRISE — Mission de Claude Code (à exécuter dans l’ordre)

> Écrit le 26.09.2026 à la demande du propriétaire. Priorité sur toute répartition antérieure. Lire aussi `CLAUDE.md`, `PROMPT_MEDINA.md` (règles de fond) et `CHAPTER_SPEC.md`.

## Contexte : deux branches du même projet
- **Branche Claude** (ce dossier, `medina/`) : 27 cours intégrés — système Cœur complet (17), J45, J44, D84, M06, M32, T78, M31, I71, I80, I70 ; cours compressés dans le HTML (DecompressionStream) ; bouton directeur de l’accueil ; typographie Georgia, titres et numéros rouges soulignés, texte justifié ; atlas ECG.
- **Branche Alpha** (ChatGPT, dossier Drive **« Medina Alpha »**) : même architecture (build_front.py, chapters.json, glossary, engine), **22 cours** au cycle 1, dont **J18 Pneumonies, I26 Embolie pulmonaire, A41 Sepsis de l’adulte** (absents de la branche Claude), versions possiblement révisées de J45 et J44, audits (`audits/J18.md`, `J44.md`, `I26.md`, `A41.md`, `NAVIGO_2026-09-26.md`), et des fonctions d’interface : **Navigo** (plan flottant à droite, reconstruit par onglet, recherche, sauts), **Police Taille** (14 à 24 px, mémorisée par cours), **mode livre**, notion `DONE_COURSES` dans `shell/data.py`.
- Fichiers Alpha à placer par le propriétaire dans `medina/_alpha_in/` : `MEDINA_Alpha_TRANSPORT_26-09-2026.zip` (contient HTML, `MEDINA_Alpha_SOURCES.json.gz`, `RESTAURER_MEDINA_Alpha.py`, `SHA256.txt`, PDF), `MEDINA_Alpha_PASSATION_2026-09-26.md`. Si le dossier Drive est synchronisé localement, les prendre directement dans « Medina Alpha » (sans jamais y écrire, sauf demande).
- `Medina.html` (79 Mo, dit MEDINA_0, avec les SSP) reste **intact** ; ne pas l’écraser.

## PHASE 1 — Intégrer TOUTE l’avancée Alpha dans la branche Claude
1. Extraire le zip Alpha dans `_alpha_in/`, vérifier `SHA256.txt`, restaurer : `python3 RESTAURER_MEDINA_Alpha.py MEDINA_Alpha_SOURCES.json.gz ../_alpha` (dossier vide).
2. **Inventaire différentiel** écrit dans `audits/FUSION_ALPHA.md` : `diff -rq medina _alpha` ; liste des chapitres (comparer les deux `chapters.json`), des fichiers de glossaire, de `engine/`, `shell/` (polish, data.py, medina_front.html), `build_*.py`, `test_v7.py`, `audits/`.
3. **Chapitres** :
   - Présents seulement dans Alpha (J18, I26, A41, et tout autre) : **copier** `chapters/<CODE>/` et leurs clés de glossaire, déclarer dans `chapters.json` avec la bonne vague (champ `system` de `medora-data`).
   - Présents dans les deux (J45, J44, cardiologie…) : comparer section par section ; **garder la version la plus complète et la plus exacte**, en fusionnant les ajouts utiles de l’autre (figures, fenêtres, quiz, corrections d’audit). Consigner chaque décision dans `FUSION_ALPHA.md`.
   - Présents seulement dans Claude (D84, M06, M32, T78, M31, I71, I80, I70) : conserver.
4. **Glossaire** : union des clés ; en cas de conflit de définition, garder la plus littérale et exacte.
5. **Interface** : porter dans la branche Claude **toutes** les fonctions Alpha (Navigo, Police Taille, mode livre, et toute autre amélioration trouvée), en conservant les fonctions Claude (compression des cours, bouton directeur, atlas ECG, notification, insignes, typographie). Adopter `DONE_COURSES` si elle clarifie l’insigne « 100 % rédigé » (chapitre audité) distinct de `chapters.json` (chapitre intégré).
6. **Typographie retenue** (décision du propriétaire à Claude) : numéros **rouges soulignés** (les deux branches concordent) ; titres **rouges soulignés** ; texte justifié ; une seule police partout, y compris sur mobile. L’ocre des titres de la branche Alpha n’est pas retenu.
7. **Audits** : copier `audits/` d’Alpha ; reporter leurs réserves.
8. Construire, tester (`test_v7.py` sur tous les chapitres fusionnés, PC et mobile), aucune erreur JavaScript, `audit()` = `{}` partout.
9. **Livrable de phase 1** : `MEDINA_Claude.html` (version fusionnée) + `MEDINA_SOURCES.json` + mise à jour de `PROMPT_MEDINA.md` § 19.

## PHASE 2 — Moderniser et styliser le front-end partout
- Objectif : interface moderne, élégante, cohérente sur **toutes** les pages (accueil, atlas des spécialités, listes de systèmes, entrées CIM, cours, fenêtres, quiz, Pareto, Examen fédéral, Carnet, recherche, atlas ECG, bouton directeur), PC et mobile.
- **Garder l’identité et l’architecture de Medina** (navigation, routes, barre latérale verte, logique des pages) : le propriétaire a refusé par le passé une refonte qui changeait la structure (coque V7). Moderniser = typographie soignée, espacements, hiérarchie visuelle, cartes, ombres douces, micro-animations sobres (respect de `prefers-reduced-motion`), mode sombre facultatif, accessibilité (contraste, focus clavier), performance.
- Implémenter dans la couche `shell/polish.css` / `polish.js` et, si nécessaire, dans `engine/medina_course.css` ; ne supprimer aucune fonction.
- Captures avant/après (Playwright, 1360 px et 390 px) dans `audits/FRONT_captures/`.

## PHASE 3 — Livrer `MEDINA_final.html`
- Construire, tester, puis livrer **`MEDINA_final.html`** (et `MEDINA_final_SOURCES.json`) dans `MEDINA_OUT` ; copie dans le dossier Drive `Medina_claude` s’il est synchronisé (`MEDINA_DRIVE`). Terminer par le tableau de bord.

## PHASE 4 — Production par cycles de DEUX systèmes, qualité extrême
- Un cycle = **deux systèmes en parallèle** (sous-agents : un rédacteur par système, dossiers séparés ; un auditeur indépendant par chapitre ; un seul intégrateur pour `chapters.json`, la coque et le HTML).
- **Ordre des cycles** (vérifier chaque code dans `medora-data` et `chapters.json` avant d’écrire) :
  1. **Poumon, plèvre et ventilation** (après J45, J44, J18, I26 : J09, J96, J90, J93, A15, C34, J84, D86, G47.3, I27, J47, J20, J60, puis tout le reste du système) **+ Vaisseaux et microcirculation / Immunité** (I73, I83, I89, I95, D90, B24 ; D86 commun avec Poumon).
  2. **Microorganismes et infections** (après A41) + **Tube digestif, foie, pancréas**.
  3. **Système nerveux** + **Métabolisme, diabète, endocrinologie**.
  4. **Rein, eau et électrolytes** + **Sang, moelle, hémostase, oncologie**.
  5. **Grossesse et gynécologie** + **Nouveau-né, pédiatrie, génétique**.
  6. Puis les autres systèmes du catalogue (locomoteur, peau, œil, ORL, urologie, traumatologie, toxicologie…), toujours par paires.
- **Qualité extrême** : niveau au moins égal à J45 ou T78 (10 000 à 15 000 mots par chapitre majeur) ; sources suisses d’abord, recommandations datées ; figures ; ≥ 3 quiz ; fenêtres réelles ; critères formels en dernier îlot ; audit indépendant /20 (cible 20/20) avant l’insigne « 100 % rédigé ». Ne jamais condenser.
- Réécrire au niveau exigé : J44 (si la fusion ne l’a pas déjà porté à ce niveau), D84, M06, M32.
- Après chaque cycle : annonce « cycle N, systèmes X + Y », chapitres ajoutés, contrôles, réserves, progression recalculée, tableau de bord ; livraison de `MEDINA_final.html` mis à jour.
