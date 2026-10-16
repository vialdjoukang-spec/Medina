# MEDINA — thèmes de lecture (16 octobre 2026)

**Périmètre.** Portail (`index.html`) et fragments (accueil, catégories, Leçons, Navigo, mode Livre). Aucun contenu médical, glossaire, nosologie ni chapitre n’est modifié. Le thème « Par défaut » est celui de `engine/couleurs_premium.css`, inchangé : sans choix enregistré, aucun attribut n’est posé et la page est identique à la version sans thèmes.

| Fichier | Rôle |
|---|---|
| `engine/themes_medina.css` | Styles du sélecteur ; bloc `<themes>` (tokens de chaque thème, valeurs sRGB issues d’OKLCH) ; règles de famille qui ne lisent que des custom properties. |
| `engine/themes_medina.js` | Pose `html[data-medina-theme]` avant le premier rendu, construit le bouton « Thème » et son panneau, mémorise le choix, relie les cartes voisines (`--mth-next`). Bloc `<catalogue>` : liste des thèmes. |
| `build_front.py` | Une ligne : `medina-themes` (CSS) et `medina-themes-runtime` (JS) injectés dans `<head>` juste après `medina-couleurs-premium`. |
| `build_index.py` | Même injection sur le portail, après `medina-couleurs-premium`. |

## Fonctionnement

- **Aucun flash.** Le script est dans `<head>`, après la feuille : il lit `localStorage["medina.theme"]` (dans un `try/catch`) et pose `data-medina-theme` sur `<html>` avant que le `<body>` soit analysé. Un identifiant inconnu ou un stockage indisponible donne « Par défaut ».
- **Partage portail / fragments.** Le portail et les fragments sont servis par la même origine (GitHub Pages ou dossier local) : la clé est commune. Un changement dans un autre onglet est appliqué à la volée (événement `storage`). « Par défaut » efface la clé.
- **Bouton.** Fragments : enfant direct de `.topbar`, avant `.top-actions` (sous 700 px, `.top-actions` est masqué ; une quatrième colonne de 44 px est réservée au bouton). Portail : dernier élément de la navigation de l’en-tête. Libellé « Thème » visible au-dessus de 1023 px dans les fragments (700 px sur le portail), icône seule de 44 px au-dessous, pour laisser sa place à la recherche (le libellé reste lu par les lecteurs d’écran). Les anciens `#theme-btn` / `.theme-btn` des coques restent masqués ; le nouveau bouton n’en reprend ni l’identifiant ni la classe.
- **Panneau.** `role="dialog"` non modal, relié par `aria-controls` / `aria-expanded` / `aria-haspopup`. Trois groupes (thème actuel, Géométrique pâle, Multicolore iconique) ; chaque pastille est un bouton `aria-pressed` qui montre un aperçu (fond, motif ou voile, barre, deux cartes) et le nom du thème. Clavier : Entrée ou Espace ouvre ; le focus va sur le thème actif ; flèches, Début et Fin déplacent le focus ; Échap ferme et rend le focus au bouton ; sortir du panneau par Tab ou cliquer ailleurs le ferme. Annonce polie « Thème « … » appliqué ». Ouverture en 160 ms (opacité, 4 px), supprimée sous `prefers-reduced-motion: reduce`.
- **API.** `window.MEDINA_THEMES.list()`, `.get()`, `.set(id)` (outils de capture et de contrôle).
- **Spécificité.** Tokens : `:root[data-medina-theme="…"]` (0,2,0), au-dessus de `:root` et de `html[data-medina-fragment="…"]` (0,1,1) de `couleurs_premium.css`. Règles de surface : préfixe `html[data-medina-theme]:not(#mth-z) body`, une colonne d’identifiant au-dessus des préfixes des couches antérieures, sans nouvelle surenchère d’attributs.

## Règles communes aux thèmes

- **Contenu des cours sur fond blanc immaculé (règle de Vial, 16.10.2026).** Sous tout thème, la Leçon (`.mc` : outils, en-tête, onglets, îlots, tableaux, Sciences, mode Livre) et les fenêtres explicatives (`dialog.mc-dlg`, `#mc-dialog`) sont sur `#ffffff`, sans teinte ni motif : `.mc` devient une feuille blanche et, à l’intérieur, les fonds teintés du thème (`--n-paper`, `--n-sunken`, `--accent-tint`, `--accent-sel`) redeviennent blancs. Contrôle par comparaison au thème par défaut (G45, 761 éléments mesurés) : les seules différences sont la feuille blanche de `.mc` et l’onglet actif, blanc au lieu d’être teinté. Motifs et couleurs régionales ne portent que sur le fond de page, les barres, la couverture, les cartes du portail et des accueils et les jauges. L’encre des cours, les termes interactifs et Navigo (`.mc-navigo*`) ne sont jamais redéfinis par cette couche.
- Le texte reste achromatique : `--ink-1/2/3` (`#1a1917`, `#3e3d3a`, `#5f5d5a`) ne sont jamais redéfinis ; les rôles des cours (`--lesson-*` : bleu marine du cycle, titres rouges, termes orange, mot vert) et les statuts ne sont pas touchés.
- Les teintes de catégorie (`--cat-NN`) et de spécialité (`--sp-<id>`) gardent leur identité validée dans `PALETTE.md`.
- Le motif ou le voile est peint sur un **calque fixe** (`body::after`, `position:fixed`, `z-index:-1`) derrière toute la page ; `.main` devient transparente. Les cartes, îlots, fenêtres, barre supérieure et barre latérale gardent leur surface claire : le motif n’est jamais derrière le texte d’une carte. Le calque fixe est composité une fois : le défilement reste fluide.
- Contrastes contrôlés pour chaque thème : texte principal (`--ink-1`) ≥ 12:1 sur tous les fonds du thème, pire pixel du motif compris (minimum mesuré 12,5:1, Bleu · grille fine) ; texte secondaire ≥ 4,5:1 sur papier, encart, fonds d’accent et **pire pixel du motif** ; encre d’accent ≥ 4,5:1 ; texte blanc sur bouton ≥ 4,5:1 ; repère d’accent, contour interactif (`--n-line-strong`) et anneau de focus ≥ 3:1 ; remplissage de jauge ≥ 3:1 sur sa piste.

## Famille « Géométrique pâle »

Un thème par couleur primaire et secondaire (rouge, jaune, bleu ; orange, vert, violet), plus magenta et cyan. Recette OKLCH, teinte *h* propre au thème :

| Token | L | C | Rôle |
|---|---|---|---|
| `--n-paper` | 0,979 | 0,016 (réduite au gamut) | Fond de page (exigence : L ≥ 0,975, C ≤ 0,02) |
| `--n-sunken` / `--n-line-soft` / `--n-line` | 0,957 / 0,912 / 0,862 | 0,018 / 0,016 / 0,020 | Encarts, séparations, bordures |
| `--n-line-strong` | 0,575 | 0,045 | Contours interactifs (≥ 3:1) |
| `--accent` / `--accent-ink` | 0,535 / 0,430 | 0,125 / 0,105 | Repère / encre et boutons |
| `--accent-tint` / `--accent-sel` | 0,972 / 0,935 | 0,022 / 0,042 | Survol / sélection |
| `--brand-50` … `--brand-800`, `--gauge-400` … `-700`, `--gauge-track` | rampe 0,975 → 0,32 | ≤ 0,125 | Marque et jauges à une teinte |
| `--n-shadow`, `--n-veil` | 0,245 / 0,22 | 0,025 | Ombres et voile teintés du thème |
| Motif | trait 1 px de `oklch(0.50 0.13 h)` | opacité 0,14 à 0,20 | SVG data-URI (0,2 à 0,6 ko) |

| Thème | Identifiant | Fond (L / C / h) | Accent · encre | Motif | Marge la plus faible |
|---|---|---|---|---|---|
| Rouge · losanges | `geo-rouge` | `#fff6f5` (0.980 / 0.010 / 25) | `#aa4c47` · `#803531` | losanges (treillis à 45°, maille 32 px), opacité 0.17 | texte secondaire sur pire pixel du motif : 4,80 (≥ 4,5) |
| Orange · cercles concentriques | `geo-orange` | `#fff6f1` (0.979 / 0.012 / 51) | `#a35612` · `#7a3d02` | cercles concentriques (trois anneaux, maille 96 px), opacité 0.15 | 4,93 |
| Jaune · hexagones | `geo-jaune` | `#fcf8ec` (0.979 / 0.016 / 92) | `#846a00` · `#614e00` | hexagones en nid d’abeille (côté 14 px), opacité 0.20 | 4,69 |
| Vert · triangles | `geo-vert` | `#f1fbf3` (0.978 / 0.015 / 152) | `#298144` · `#175f2f` | triangles équilatéraux (réseau isométrique, côté 32 px), opacité 0.14 | 5,12 |
| Cyan · ondes | `geo-cyan` | `#ecfcfd` (0.980 / 0.017 / 201) | `#007c86` · `#005b63` | ondes douces (période 64 px), opacité 0.18 | 4,82 |
| Bleu · grille fine | `geo-bleu` | `#f4f9ff` (0.980 / 0.010 / 253) | `#356eb4` · `#235088` | grille millimétrée (pas 24 px, trait fort tous les 96 px), opacité 0.20 | 4,66 |
| Violet · chevrons | `geo-violet` | `#f9f6ff` (0.978 / 0.012 / 301) | `#795aaa` · `#594080` | chevrons (zigzag, rangées de 24 px), opacité 0.17 | 4,85 |
| Magenta · points | `geo-magenta` | `#fff5fa` (0.979 / 0.013 / 346) | `#9e4c7e` · `#77355d` | points en quinconce (pas 11 px), opacité 0.19 | 4,67 |

Le fond reste sous L 0,98 : la couleur se devine, elle ne gêne jamais la lecture. Les thèmes se distinguent d’abord par leur motif (huit géométries différentes) puis par leur teinte ; dans un fragment, l’accent du thème remplace l’accent de spécialité, les teintes des catégories restent les leurs.

## Famille « Multicolore iconique »

Cinq teintes par thème, distribuées par **régions** :

| Région | Teinte | Où |
|---|---|---|
| a → b | accent, puis fin de barre | Barre supérieure des fragments et en-tête du portail (voile pâle et liseré inférieur de 3 px), barre de lecture `#mdn-progress` |
| c → d | barre latérale | Voile vertical et liseré droit de 3 px (bordure `border-image`) ; élément de navigation actif en teinte c |
| d → e | couverture | Couverture du fragment et bloc de progression de l’Accueil (liseré supérieur) ; surtitre de couverture en encre d |
| c → e | jauges | Remplissage des jauges (`.gauge-fluid`, `<progress>` ; Navigo exclu) |
| propre → suivante | cartes | Chaque carte de catégorie et de spécialité garde sa teinte (filet gauche, numéro, fond teinté) ; son liseré supérieur de 4 px part de sa teinte et s’éteint là où naît celle de la carte suivante |
| a ↘ b | page | Voile très pâle (L 0,962, C 0,030) en diagonale, angle propre au thème |

**Surfaces claires.** Les liserés sont portés par un pseudo-élément `::after` (3 à 4 px de dégradé, rayon hérité de la carte) ou par une bordure : la surface des régions et des cartes ne reçoit que des voiles très pâles (L ≈ 0,97), jamais une couleur saturée derrière du texte.

**Évanouissement et renaissance.** Toutes les frontières utilisent deux calques superposés, sans mélange des couleurs : `linear-gradient(θ, A 0%, transparent x%)` puis `linear-gradient(θ, transparent x%, B 100%)` (x = 50 % pour les liserés et jauges, 55 % pour le voile de page). Au point x, les deux couleurs sont nulles ; A n’existe qu’avant, B qu’après. La bordure de la barre latérale n’accepte qu’une image : elle emploie `linear-gradient(180deg, A 0%, transparent 50%, B 100%)`, rendu identique aux deux calques. `transparent` est interpolé en alpha prémultiplié : A s’atténue sans virer au gris. `--mth-next` est lu par `themes_medina.js` sur la carte suivante (`--mp-cat` ou `--card-accent`) ; la dernière carte reprend la première.

Pour chaque teinte : repère (L 0,50 à 0,62, C 0,11 à 0,17, ≥ 3:1), encre (L 0,43, C ≤ 0,10, ≥ 4,5:1), fond (L 0,972, C 0,022) et voile (L 0,962, C 0,030). Neutres : papier L 0,979, C 0,006, teinte de a.

| Thème | Identifiant | Teintes a · b · c · d · e | Angle | Marge la plus faible |
|---|---|---|---|---|
| Vitrail | `multi-vitrail` | rubis `#9c4343` · saphir `#436cb9` · émeraude `#009772` · ambre `#8f5300` · améthyste `#8656a6` | 115° | jauge sur piste : 3,36 (≥ 3) |
| Bauhaus | `multi-bauhaus` | bleu `#2b58b1` · jaune `#a97f00` · rouge `#a9231e` · bleu · jaune | 90° | jauge sur piste : 3,35 |
| Minéral | `multi-mineral` | glacier `#009a9a` · argile `#9f4f25` · ardoise `#3e8cc9` · lichen `#71943f` · quartz rose `#9d486c` | 135° | accent sur papier : 3,25 |
| Aurore boréale | `multi-aurore` | vert `#2e9052` · violet `#6959ae` · cyan `#009b8f` · magenta `#9b467a` · bleu `#3265af` | 160° | jauge sur piste : 3,16 |
| Agrumes et lagon | `multi-agrumes` | orange `#c16e2d` · menthe `#0f9b89` · corail `#9f4d47` · lagon `#0081a1` · citron vert `#7c9135` | 100° | jauge sur piste : 3,21 |

L’ordre a → e de chaque thème a été cherché pour que les teintes qui se touchent (a/b, b/c, c/d, d/e et c/e) restent séparées sous protanopie et deutéranopie (ΔE OKLab ≥ 8,9, simulation Machado 2009) et en vision normale (ΔE ≥ 17), et pour que les cinq thèmes restent distincts entre eux (signature a/b ou encre d’accent).

## Validation (16.10.2026)

| Contrôle | Résultat |
|---|---|
| Contrastes (générateur : toutes les paires texte, encre, repère, contour, focus, statut et jauge, dont le pire pixel du motif) | 13 thèmes, 0 échec |
| `theme_check.py` (règles WCAG, signatures) | Géométriques 8/8 OK ; Multicolores 5/5 OK ; `--distinct` (famille multicolore) : 0 paire trop proche |
| `validate_palette.js` (compétence dataviz) | 5 palettes de région : PASS sans avertissement (bande de luminosité, chroma ≥ 0,10, CVD, ΔE normal ≥ 15, contraste ≥ 3:1) ; 8 rampes de jauge géométriques `--ordinal` : PASS |
| `tools/front_garde.py --lecon G45`, sous chaque thème et « Par défaut » (390 et 1280 px, mouvement normal et réduit) | 14/14 SUCCÈS : police, erreurs JS, débordement, contraste, saturation, cartes, transitions, mouvement réduit, focus |
| Erreurs JavaScript (Accueil, Neurologie, G45, panneau ouvert) | 0 |
| Contenu des cours (G45 sous les 13 thèmes, comparé au défaut) | fond de `.mc` `#ffffff` ; aucune teinte ni motif dans les éléments du cours |

Note : un contrôle catégoriel des huit accents géométriques ensemble n’a pas de sens (deux thèmes ne coexistent jamais à l’écran) ; ils sont séparés par leur motif dans le panneau.

## Ajouter ou modifier un thème

1. Choisir une teinte OKLCH (Géométrique pâle) ou cinq teintes et leur ordre de régions (Multicolore), puis calculer les tokens selon les recettes ci-dessus ; un motif est un SVG de 1 px de trait, tuile ≤ 96 px, encodé en data-URI dans `--mth-motif` (avec `--mth-motif-size`).
2. Ajouter le bloc `:root[data-medina-theme="<id>"],.mth-swatch[data-mth-swatch="<id>"]{…}` dans `<themes>` et l’entrée `{"id","famille","nom"}` dans `<catalogue>` de `themes_medina.js`. Préfixe `geo-` ou `multi-` : les règles de famille s’appliquent seules.
3. Vérifier les seuils du paragraphe « Règles communes », lancer `validate_palette.js` sur les teintes, reconstruire (`MEDINA_OUT=<d> python3 build_front.py --fragment S08`, puis `python3 build_index.py --fragments-dir <d>/fragments --output <d>/index.html`) et passer `tools/front_garde.py` avec le thème enregistré.
4. Si `couleurs_premium.css` change ses neutres ou sa marque, « Par défaut » suit automatiquement ; l’aperçu « Par défaut » du panneau lit les valeurs calculées sans attribut de thème.
