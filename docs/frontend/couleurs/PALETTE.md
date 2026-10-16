# MEDINA — système de couleurs premium (16 octobre 2026)

**Périmètre.** Portail (`index.html`), accueils des 23 fragments, pages de catégorie, Leçons (quatre onglets), îlots, fenêtres explicatives, Navigo, mode Livre. Aucun contenu médical, glossaire, nosologie ni chapitre n’est modifié. Thème clair uniquement ; aucun sélecteur de thème n’est ajouté.

| Fichier | Rôle |
|---|---|
| `engine/couleurs_premium.css` | Dernière couche de la cascade (portail et fragments). Blocs générés `<tokens>`, `<specialites>`, `<categories>` ; règles qui ne lisent que des custom properties. |
| `docs/frontend/couleurs/palette.py` | Source unique : valeurs OKLCH, conversion sRGB, contrastes WCAG, appel de `validate_palette.js`, réécriture des blocs générés (`--ecrire`). |
| `docs/frontend/couleurs/validation.txt` | Sortie brute du validateur (`palette.py --valider --rapport …`). |
| `build_front.py` | Une ligne : injection de `medina-couleurs-premium` après `medina-finition-premium` (préfixe de spécificité premium). |
| `build_index.py` | Couche injectée en dernier sur le portail ; cartes de spécialité branchées sur `--sp-<id>`. |
| `engine/category_organisation.css` | Couche « survol » : valeurs littérales remplacées par les tokens ; contour de focus des leçons sans transition (indicateur immédiat). |

## Méthode

1. **Audit rendu** (`getComputedStyle` sur Accueil, fragment, catégorie, quatre onglets, fenêtre, Navigo, Livre ; S08 / G45 — Accidents ischémiques cérébraux transitoires et syndromes apparentés (N-05-Neurologie)). Chiffres avant/après ci-dessous.
2. **Tokens** posés en OKLCH : pas de luminosité réguliers, chroma plafonnée, teinte constante par rampe ; conversion sRGB et contrôle de gamut dans `palette.py`.
3. **Teintes catégorielles** : 23 emplacements choisis par recuit simulé (maximiser l’écart minimal entre voisins sous protanopie et deutéranopie, simulation Machado 2009 ; plancher 15 en vision normale ; voisins verticaux de grille à 3 et 4 colonnes), puis **figés dans un ordre fixe**. Trois paliers de luminosité (0,46 / 0,535 / 0,61), chroma 0,102 à 0,120 : assez pour porter une identité (plancher 0,10), assez bas pour rester sobre.
4. **Spécialités** : chaque spécialité reçoit un des 23 emplacements (identité fixe, Accueil et fragment), avec une cible sémantique pondérée (cardiologie rouge, hématologie grenat, neurologie pervenche, pneumologie bleu, psychiatrie violet, infectiologie vert sapin…) sous la contrainte que l’ordre d’affichage de l’Accueil passe le validateur.
5. **Validation** : `validate_palette.js` (compétence dataviz) en mode clair sur la surface réelle `#f5f8f6`, puis `tools/front_garde.py` et `tools/front_capture.py`.

## Règles d’emploi

- **Encre / repère / fond.** Chaque teinte existe en quatre pas : repère (`--cat-NN`, filets, pastilles, icônes ; ≥ 3:1), encre (`-ink`, L 0,43, texte ≥ 4,5:1), fond teinté (`-tint`, L 0,971 / 0,975 / 0,979 selon le palier, C 0,015) et sélection (`-sel`, L 0,945, C 0,028). Aucune grande surface saturée.
- **Accent du contexte.** `--accent`, `--accent-ink`, `--accent-tint`, `--accent-sel` valent la marque sur l’Accueil et la teinte de la spécialité dans un fragment (`html[data-medina-fragment="S08"]{--accent:var(--sp-s08)…}`). Les variables historiques (`--atlas-accent`, `--mp-*`, `--mz-*`, `--p-*`, `--bg`, `--ink`…) sont ramenées sur ces tokens.
- **Catégories.** `engine/atlas_v2.js` pose `--cat` en style en ligne (20 couleurs vives par rang). La couche les remappe par sélecteur d’attribut (`[style*="--cat: #C2185B" i]` → `--cat-01`) avec `!important` : le rang *n* prend l’emplacement *n*. Au-delà du 23ᵉ rang (S08 : 29 catégories, S10 : 30, T1 : 25, T3 : 26), les rangs 24 à 32 reçoivent des tokens de débordement `--cat-24` … `--cat-32` : la teinte d’angle d’or posée par atlas_v2.js, ramenée en OKLCH sur les mêmes paliers (palier décalé), si bien que chaque catégorie garde un fond distinct ; ces rangs, les moins prioritaires pour l’Examen fédéral, ne sont pas couverts par le validateur (aucune palette de plus de 23 teintes ne peut l’être) et restent portés par leur numéro et leur intitulé.
- **Statuts** (`--status-ok`, `--status-prep`, `--status-prov`) : toujours avec leur libellé et une forme (disque plein « Lire le cours », cercle vide « En préparation », demi-disque sur la mention de publication provisoire) ; jamais la couleur seule.
- **Jauges** : rampe séquentielle à une teinte (marque, 158,4°), piste `--gauge-track` cernée de `--gauge-edge` (≥ 3:1), remplissage dégradé `--gauge-fill-top` → `--gauge-fill` (5,7:1 sur la piste).
- **Étoile d’or** : facettes conservées, contour `--star-edge` (5,7:1) ; bandeau PROFILES et bouton Pareto en aplat `--gold-100`, texte `--gold-800` (8,5:1).
- **Leçon** : les rôles sémantiques fixés par Vial sont conservés à l’identique (`--lesson-*` : bleu marine du cycle, titres rouges soulignés, termes orange foncé, mot vert, abréviations).
- **Contours interactifs** : boutons, champs, onglets d’outils, options de quiz, pagination du Livre, Navigo → `--n-line-strong` (3,95:1 sur surface, 3,69:1 sur papier, 3,50:1 sur encart).
- **Thèmes futurs** : tout est redéfinissable sur `:root` ; un thème peut remplacer les primitives (`--n-*`, `--ink-*`, `--brand-*`, `--cat-NN*`, `--gold-*`, `--gauge-*`, `--status-*`) ou les rôles (`--accent*`, `--focus-ring`, `--shadow-*`, `--gauge-*`, `--star-*`). Dans un fragment, l’accent est fixé par la règle `html[data-medina-fragment="…"]` : un thème qui veut le changer redéfinit `--sp-<id>` (ou `--cat-NN`).

## Tokens (valeurs du thème par défaut)

### Neutres, marque, statuts, jauges, or, leçon

| Token | Valeur | OKLCH / origine | Rôle |
|---|---|---|---|
| `--n-surface` | `#ffffff` | oklch(1.000 0.000 160) | Cartes, îlots, fenêtres, Navigo |
| `--n-paper` | `#f5f8f6` | oklch(0.976 0.003 160) | Fond de page (surface de validation) |
| `--n-sunken` | `#eff2f0` | oklch(0.957 0.004 160) | Encarts, puits, jauges informatives, survol neutre |
| `--n-line-soft` | `#dfe2e6` | oklch(0.912 0.006 250) | Séparations décoratives (non interactives) |
| `--n-line` | `#ced2d7` | oklch(0.862 0.008 250) | Bordures de cartes, de tableaux et d’îlots |
| `--n-line-strong` | `#7a8188` | oklch(0.600 0.014 250) | Contours interactifs (≥ 3:1 sur surface, papier et encart) |
| `--ink-3` | `#565e69` | oklch(0.480 0.020 255) | Texte atténué (≥ 4,5:1 sur encart) |
| `--ink-2` | `#353e4a` | oklch(0.360 0.024 255) | Texte courant de l’interface |
| `--ink-1` | `#141a22` | oklch(0.215 0.018 255) | Encre primaire, titres de l’interface |
| `--brand-50` | `#f1f9f4` | oklch(0.975 0.010 158.4) | Rampe de la marque |
| `--brand-100` | `#e2f3e8` | oklch(0.948 0.022 158.4) | Rampe de la marque |
| `--brand-200` | `#c8e5d3` | oklch(0.895 0.038 158.4) | Rampe de la marque |
| `--brand-300` | `#a2cdb3` | oklch(0.810 0.058 158.4) | Rampe de la marque |
| `--brand-400` | `#71aa89` | oklch(0.690 0.078 158.4) | Rampe de la marque |
| `--brand-500` | `#488a67` | oklch(0.580 0.088 158.4) | Rampe de la marque |
| `--brand-600` | `#2d684a` | oklch(0.470 0.080 158.4) | Rampe de la marque |
| `--brand-700` | `#1f3428` | ancre #1f3428 | Rampe de la marque |
| `--brand-800` | `#122219` | oklch(0.235 0.028 158.4) | Rampe de la marque |
| `--status-ok` | `#296a3b` | oklch(0.470 0.100 150) | Statut « Disponible » (disque plein) |
| `--status-ok-bg` | `#e7f8e9` | oklch(0.962 0.026 150) | Fond du statut |
| `--status-prep` | `#565e69` | oklch(0.480 0.020 255) | Statut « En préparation » (cercle vide) |
| `--status-prep-bg` | `#eff2f0` | oklch(0.957 0.004 160) | Fond du statut |
| `--status-prov` | `#8a5111` | oklch(0.490 0.105 62) | Statut « Provisoire » (demi-disque) |
| `--status-prov-bg` | `#fef1db` | oklch(0.962 0.032 80) | Fond du statut |
| `--gauge-400` | `#71aa89` | oklch(0.690 0.078 158.4) | Rampe séquentielle des jauges |
| `--gauge-500` | `#488a67` | oklch(0.580 0.088 158.4) | Rampe séquentielle des jauges |
| `--gauge-600` | `#2d684a` | oklch(0.470 0.080 158.4) | Rampe séquentielle des jauges |
| `--gauge-700` | `#234c36` | oklch(0.380 0.060 158.4) | Rampe séquentielle des jauges |
| `--gold-100` | `#fff3ce` | oklch(0.965 0.050 92) | Étoile d’or, Pareto |
| `--gold-300` | `#f8d376` | oklch(0.880 0.120 88) | Étoile d’or, Pareto |
| `--gold-500` | `#e1a52c` | oklch(0.760 0.145 80) | Étoile d’or, Pareto |
| `--gold-600` | `#bc7d19` | oklch(0.640 0.130 72) | Étoile d’or, Pareto |
| `--gold-700` | `#925a1a` | oklch(0.520 0.105 65) | Étoile d’or, Pareto |
| `--gold-800` | `#643d17` | oklch(0.400 0.075 62) | Étoile d’or, Pareto |
| `--lesson-ink` | `#0f2c66` | valeur conservée | Corps des cours du cycle (bleu marine renforcé) |
| `--lesson-title` | `#b3261e` | valeur conservée | Titres et numéros rouges soulignés |
| `--lesson-term` | `#9b3900` | valeur conservée | Termes interactifs des cours du cycle |
| `--lesson-word` | `#187349` | valeur conservée | Mot vert : fenêtre explicative ou contentieux |
| `--lesson-abbr` | `#205d55` | valeur conservée | Abréviation à clé du glossaire |

### Rôles (alias)

| Token | Valeur | Rôle |
|---|---|---|
| `--accent` | `var(--brand-600)` | Accent du contexte : marque sur l’Accueil, teinte de spécialité dans un fragment (filets, pastilles, soulignés) |
| `--accent-ink` | `var(--brand-700)` | Texte et icônes en accent (≥ 4,5:1) |
| `--accent-tint` | `var(--brand-50)` | Fond teinté de l’accent (sélection légère, survol) |
| `--accent-sel` | `var(--brand-100)` | Fond de l’élément sélectionné ou courant |
| `--focus-ring` | `var(--accent-ink)` | Anneau de focus clavier (2 px, ≥ 3:1) |
| `--on-accent` | `var(--n-surface)` | Texte sur un aplat d’encre d’accent |
| `--shadow-color` | `rgb(16 24 36)` | Couleur des ombres (relief discret) |
| `--shadow-1` | `inset 0 1px 0 var(--n-surface),0 1px 2px color-mix(in srgb,var(--shadow-color) 5%,transparent),0 8px 22px -16px color-mix(in srgb,var(--shadow-color) 26%,transparent)` | Relief de repos des cartes |
| `--shadow-2` | `inset 0 1px 0 var(--n-surface),0 2px 5px color-mix(in srgb,var(--shadow-color) 7%,transparent),0 14px 30px -18px color-mix(in srgb,var(--shadow-color) 32%,transparent)` | Relief au survol |
| `--shadow-pop` | `0 2px 6px color-mix(in srgb,var(--shadow-color) 6%,transparent),0 22px 44px -26px color-mix(in srgb,var(--shadow-color) 40%,transparent)` | Fenêtres, Navigo, panneaux flottants |
| `--backdrop` | `rgb(20 24 34 / .55)` | Voile derrière une fenêtre explicative |
| `--gauge-track` | `var(--brand-50)` | Piste des jauges |
| `--gauge-edge` | `var(--n-line-strong)` | Contour de la piste (≥ 3:1) |
| `--gauge-fill` | `var(--gauge-600)` | Remplissage des jauges |
| `--gauge-fill-top` | `var(--gauge-500)` | Haut du dégradé de remplissage (relief) |
| `--star-edge` | `var(--gold-700)` | Contour de l’étoile d’or (≥ 3:1) |
| `--star-fill` | `var(--gold-500)` | Corps de l’étoile d’or |
| `--star-light` | `var(--gold-300)` | Facette éclairée de l’étoile |
| `--star-shade` | `var(--gold-600)` | Facette ombrée de l’étoile |

### 23 emplacements catégoriels (ordre fixe) et spécialités

Chaque emplacement `--cat-NN` a ses variantes `--cat-NN-ink` (texte), `--cat-NN-tint` (fond) et `--cat-NN-sel` (sélection). Chaque spécialité a `--sp-<id>`, `--sp-<id>-ink`, `--sp-<id>-tint`, `--sp-<id>-sel` (alias de son emplacement).

| N° | Nom | Repère | OKLCH | Encre | Fond | Contraste repère / papier | Contraste encre / fond | Spécialité |
|---|---|---|---|---|---|---|---|---|
| 1 | pervenche | `#7e77c7` | 0.610 0.120 286.3 | `#4c428d` | `#f7f7ff` | 3.67:1 | 7.97:1 | `--sp-s08` N-05-Neurologie |
| 2 | garance | `#a74c52` | 0.535 0.120 18.0 | `#852d36` | `#fff3f3` | 5.17:1 | 7.98:1 | `--sp-t3` M-19-Médecine d’urgence, traumatologie et toxicologie |
| 3 | violet | `#6a438c` | 0.460 0.120 306.9 | `#613a82` | `#f8f3fe` | 7.03:1 | 7.90:1 | `--sp-s09` P-23-Psychiatrie et psychothérapie |
| 4 | corail | `#c1645f` | 0.610 0.120 24.0 | `#852e2e` | `#fff4f3` | 3.74:1 | 8.03:1 | `--sp-s01` C-01-Cardiologie |
| 5 | prusse | `#035e8a` | 0.460 0.102 238.8 | `#00567e` | `#edf7ff` | 6.61:1 | 7.35:1 | `--sp-s15` U-15-Urologie et andrologie |
| 6 | anis | `#7c8d2e` | 0.610 0.120 118.5 | `#4b5700` | `#f7faef` | 3.44:1 | 7.47:1 | `--sp-s03` G-04-Gastroentérologie et hépatologie |
| 7 | bleuet | `#4887c9` | 0.610 0.120 251.4 | `#0b518f` | `#f1f9ff` | 3.52:1 | 7.63:1 | `--sp-s02` P-02-Pneumologie |
| 8 | olive | `#707304` | 0.535 0.117 111.9 | `#525400` | `#f7f8ed` | 4.74:1 | 7.46:1 | `--sp-t2` M-12-Médecine des âges de la vie |
| 9 | orchidee | `#a06bb2` | 0.610 0.120 317.2 | `#6a377a` | `#fcf5ff` | 3.75:1 | 8.05:1 | `--sp-t7` E-22-Éthique médicale, droit et communication |
| 10 | grenat | `#8e3648` | 0.460 0.120 10.7 | `#842d40` | `#fff2f3` | 7.09:1 | 7.92:1 | `--sp-s06` H-08-Hématologie |
| 11 | rose | `#b8638d` | 0.610 0.120 350.1 | `#7e2e59` | `#fff4f9` | 3.77:1 | 8.08:1 | `--sp-s14` G-10-Gynécologie et sénologie |
| 12 | indigo | `#45509a` | 0.460 0.120 274.6 | `#3e4790` | `#f2f5ff` | 6.85:1 | 7.68:1 | `--sp-s07` I-13-Immunologie et allergologie |
| 13 | moutarde | `#a07e12` | 0.610 0.120 89.0 | `#634c00` | `#fcf8ed` | 3.58:1 | 7.72:1 | `--sp-s10` R-14-Rhumatologie et orthopédie |
| 14 | saphir | `#5766b2` | 0.535 0.120 272.9 | `#3b4891` | `#f3f6ff` | 4.97:1 | 7.71:1 | `--sp-s13` O-18-Ophtalmologie |
| 15 | rouille | `#874304` | 0.460 0.113 54.2 | `#7b3c00` | `#fef3ec` | 6.93:1 | 7.73:1 | `--sp-s16` O-11-Obstétrique et néonatologie |
| 16 | azur | `#0c93ab` | 0.610 0.106 215.4 | `#005a6a` | `#edfbff` | 3.40:1 | 7.43:1 | `--sp-t5` D-20-Diagnostic clinique et examens complémentaires |
| 17 | sapin | `#2e6720` | 0.460 0.120 140.1 | `#255f17` | `#f0f8ef` | 6.38:1 | 7.10:1 | `--sp-t1` I-03-Infectiologie |
| 18 | vert | `#4a9759` | 0.610 0.120 148.1 | `#086126` | `#f2fbf3` | 3.35:1 | 7.23:1 | `--sp-t6` M-21-Médecine de premier recours et santé publique |
| 19 | amethyste | `#7c5aa6` | 0.535 0.120 303.6 | `#5e3c85` | `#f9f5ff` | 5.07:1 | 7.94:1 | `--sp-s11` D-16-Dermatologie |
| 20 | cuivre | `#b86e32` | 0.610 0.120 57.0 | `#793e00` | `#fff6ef` | 3.70:1 | 7.87:1 | `--sp-s05` E-06-Endocrinologie et métabolisme |
| 21 | petrole | `#06779f` | 0.535 0.106 230.6 | `#005876` | `#edf9ff` | 4.74:1 | 7.37:1 | `--sp-s04` N-07-Néphrologie |
| 22 | ambre | `#9a5d04` | 0.535 0.118 65.8 | `#734300` | `#fef5ec` | 4.98:1 | 7.70:1 | `--sp-t4` O-09-Oncologie, génétique médicale et soins palliatifs |
| 23 | jade | `#099885` | 0.610 0.110 179.1 | `#005e51` | `#eefcf8` | 3.36:1 | 7.32:1 | `--sp-s12` O-17-Oto-rhino-laryngologie et médecine bucco-dentaire |
| 24 | debord-24 | `#6e4383` | 0.460 0.110 313.7 | `#653b7a` | `#faf3fd` | 7.03:1 | 7.85:1 |  |
| 25 | debord-25 | `#727212` | 0.535 0.110 109.6 | `#545300` | `#f8f9ed` | 4.75:1 | 7.56:1 |  |
| 26 | debord-26 | `#298eb9` | 0.610 0.110 231.3 | `#005777` | `#effbff` | 3.47:1 | 7.57:1 |  |
| 27 | debord-27 | `#883a54` | 0.460 0.110 1.3 | `#7e314c` | `#fff2f5` | 7.06:1 | 7.93:1 |  |
| 28 | debord-28 | `#467d3e` | 0.535 0.110 141.5 | `#275e20` | `#f2faf1` | 4.61:1 | 7.28:1 |  |
| 29 | debord-29 | `#757bc4` | 0.610 0.110 279.0 | `#44478a` | `#f6f8ff` | 3.65:1 | 7.87:1 |  |
| 30 | debord-30 | `#844501` | 0.460 0.110 57.8 | `#783e00` | `#fef4ed` | 6.93:1 | 7.79:1 |  |
| 31 | debord-31 | `#038065` | 0.535 0.104 171.2 | `#005e4a` | `#eefbf6` | 4.59:1 | 7.32:1 |  |
| 32 | debord-32 | `#a86aa2` | 0.610 0.110 330.5 | `#71366c` | `#fff5fe` | 3.74:1 | 8.07:1 |  |

Rangs de catégorie au-delà du 23ᵉ : `--cat-fold` (`--ink-3`), `--cat-fold-ink`, `--cat-fold-tint`, `--cat-fold-sel`.

<!-- RESULTATS -->
