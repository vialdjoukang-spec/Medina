# FUSION_ALPHA — intégration de la branche Alpha (ChatGPT) dans la branche Claude

**Date** : 26 septembre 2026. **Exécutant** : Claude Code, intégrateur unique (REPRISE_CLAUDE_CODE.md, phase 1).
**Sources** : `_alpha_in/MEDINA_Alpha_TRANSPORT_26-09-2026.zip` (6 empreintes SHA-256 conformes), restauré par `RESTAURER_MEDINA_Alpha.py` dans `../_alpha` (252 fichiers) ; `_alpha_in/MEDINA_Alpha_PASSATION_2026-09-26.md`.

## 1. Authenticité et version retenue

| Pièce | Constat | Décision |
|---|---|---|
| `MEDINA_Alpha_SOURCES.json.gz` | Reconstruit par `build_front.py` en un HTML **identique octet pour octet** au HTML du zip (11 953 435 o, 1 743 gabarits) | Source de vérité de la branche Alpha |
| `MEDINA_Alpha_26-09-2026.html` téléversé seul (11 788 946 o) | État **antérieur strict** : 20 cours, sans A41 ni I26, sans Navigo ni Police Taille ; aucun gabarit absent du zip, aucun gabarit différent | Conservé dans `_alpha_in/` pour mémoire ; non utilisé |
| Passation envoyée en cours de session | Identique (SHA-256) à celle de `_alpha_in/` | Aucune action |

## 2. Inventaire différentiel (`diff -rq`, avant fusion)

- **Identiques dans les deux branches** : les 17 chapitres cardiologiques, **J45**, 31 fichiers de glossaire communs sauf `j44.py`, `modules/ecg.py`, `modules/ecg.json`, `CHAPTER_SPEC.md`, `build_v7.py`, `restore.py`, `test_preview.py`, `test_medina.py`, `pack.py`.
- **Seulement Alpha** : chapitres **J18, I26, A41** (+ `j18.py`, `i26.py`, `a41.py`), `J44_pop3.html`, `audits/` (8 rapports), `IDENTITE_MEDINA_Alpha.md`, `create_cycle_pdf.py`, `create_status_pdf.py`, `recover_polish.py`.
- **Seulement Claude** : chapitres D84, I70, I71, I80, M06, M31, M32, T78 (+ glossaires), `modules/p2.html`, `p3.html`, `prev.html`, `CLAUDE.md`, `REPRISE_CLAUDE_CODE.md`, `.claude/commands/`.
- **Divergents** : `chapters.json`, J44 (6 fichiers) et `j44.py`, `engine/medina_course.js` et `.css`, `shell/polish.css` et `.js`, `shell/data.py`, `shell/medina_front.html` (seulement le nom « MEDINA_Alpha » dans `<title>` et `application-name`), `build_front.py`, `build_medina.py`, `chantier.py`, `pack_v7.py`, `test_v7.py`, `PROMPT_MEDINA.md`.

Après fusion, tout fichier Alpha est présent dans le dépôt ou remplacé à dessein (tableau § 4).

## 3. Chapitres

| Chapitre | Décision | Détail |
|---|---|---|
| J18 Pneumonies de l’adulte | **Repris** (vague 2, vérifiée dans `medora-data`) | `covers` restreint à **J13, J14, J15, J18** : le cours traite la pneumonie communautaire bactérienne de l’adulte ; J12 (virales → futur J09), J16, J17 non traités (contrôle de contrat, § 6) |
| I26 Embolie pulmonaire aiguë | **Repris** (vague 2) | `covers` = I26 |
| A41 Sepsis et choc septique de l’adulte | **Repris** (vague 7) | `covers` = A41 ; A40 et R57.2 non développés (signalés dans le cours) |
| J44 BPCO | **Fusionné** section par section | Base Alpha (évolution stricte de Claude : aucune section propre à Claude) ; restaurations Claude vérifiées ; journal détaillé : `audits/FUSION_J44.md` ; 10 256 mots, 50 fenêtres, 4 quiz, 7 Pareto |
| J45 et 17 cours cardiologiques | Identiques | Aucune action |
| D84, I70, I71, I80, M06, M31, M32, T78 | Conservés (propres à Claude) | M31 : sigle « PRES » corrigé en « PReS » (collision de sens, § 5) |

## 4. Code et interface

| Élément | Origine | Décision |
|---|---|---|
| **Navigo** (plan flottant, onglets, recherche, sauts en lecture verticale et en mode livre) | Alpha | Porté (`engine/medina_course.js`, `shell/polish.css`) ; libellés corrigés (espace entre numéro et titre) |
| **Police Taille** (14–24 px, curseur, A−/A+, réinitialisation, mémorisation par cours, transmise aux fenêtres) | Alpha | Porté |
| **Mode livre** : pas de page calculé sur la largeur réelle et l’espacement ; sciences masquées respectées ; flèches du clavier inactives dans les champs | Alpha | Porté |
| Numéros de sous-parties `mc-subn` | Alpha | Porté (`build_medina.transform`) |
| `DONE_COURSES` : insigne « 100 % rédigé » réservé aux chapitres audités, distinct de l’intégration | Alpha | **Adopté** : 17 cours cardiologiques ; `MEDINA_COMPLETE` injecté par `build_front.py` |
| Directeur des systèmes intégré à l’accueil (cartes, jauges, pastilles de cours) | Alpha | Porté ; ajouté **à côté** du bouton directeur Claude, relié à sa fenêtre (« Plan de rédaction ») |
| Accueil : phrase périmée « Aucun cours n’est déclaré complet » | Alpha | Remplacée à la construction |
| Style des cours (en-tête, onglets, îlots, encadrés, quiz, tableaux, fenêtres) | Alpha | Porté, **adapté à la typographie retenue** : titres et numéros rouges soulignés (l’ocre `#ad8242` n’est pas retenu) ; en-tête de cours et en-tête des fenêtres en version claire pour garder le contraste du titre rouge |
| `pack_v7.py` : empaquette `shell/*.css`, `shell/*.js`, `audits/*.md` | Alpha | Adopté (les couches `polish` n’étaient pas empaquetées dans la branche Claude) ; ajout de `docs/`, `.claude/commands/`, `modules/*.html` |
| `test_v7.py` : code de sortie non nul en cas d’échec | Alpha | Adopté |
| `create_cycle_pdf.py`, `create_status_pdf.py`, `recover_polish.py` | Alpha | Copiés à la racine (outils) |
| `IDENTITE_MEDINA_Alpha.md`, `PROMPT_MEDINA.md` d’Alpha (version 3.0 antérieure) | Alpha | Archivés dans `docs/alpha/` (le prompt Claude est un sur-ensemble) |
| Nom « MEDINA_Alpha » dans `medina_front.html` | Alpha | Non repris : le produit s’appelle Medina |
| Compression des cours, bouton directeur, atlas ECG, notification, insignes, typographie Georgia | Claude | **Conservés** |
| Notification « Nouveaux cours livrés » | Claude | Conservée ; chaque cours non achevé y porte « en révision » |

### Défauts découverts et corrigés pendant la fusion

1. **Cours inaccessibles** : la coque d’origine redirige `#/entry/I30`, `K35`, `A41`, `I63` vers d’anciens modules pilotes `#/pathology/…` introuvables dans le fichier autonome (« Chargement impossible »). Le cours **I30** (Péricardites) était donc inaccessible dans les deux branches, et **A41** l’aurait été. Correctif de construction (`build_medina.build`, remplacements assertés) : la redirection n’a lieu que si aucun cours MEDINA n’existe, et `#/pathology/<code>` renvoie vers le cours quand il existe ; `MEDINA_ALIAS` est désormais injecté dans `<head>`, avant les scripts de la coque.
2. **Doublons de fonctions** apparus au portage (`toast`, `ecgButton`) : supprimés.
3. `test_v7.py` : Chromium local (`MEDINA_CHROMIUM` ou `/opt/pw-browsers/chromium`) ; mode `--static` ; contrôles ajoutés pour Navigo (ouverture, contenu, saut), Police Taille (réglage, réinitialisation) et mode livre ; I50, chapitre modèle antérieur à la règle des préfixes, est exempté de ce seul contrôle.

## 5. Glossaire

À compléter par l’arbitrage : `audits/FUSION_GLOSSAIRE.md`.

## 6. Contrôle de conformité des chapitres Alpha et corrections

Contrôle indépendant du contrat (PROMPT_MEDINA.md § 4, 10, 13, 14, 15) : voir ci-dessous et les sections « Corrections de fusion Claude — 26.09.2026 » de `audits/J18.md`, `audits/I26.md`, `audits/A41.md`.

## 7. Réserves reportées

À compléter.
