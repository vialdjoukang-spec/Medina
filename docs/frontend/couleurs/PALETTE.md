# MEDINA — système de couleurs premium (16 octobre 2026)

**Périmètre.** Portail (`index.html`), accueils des 23 fragments, pages de catégorie, Leçons (quatre onglets), îlots, fenêtres explicatives, Navigo, mode Livre. Aucun contenu médical, glossaire, nosologie ni chapitre n’est modifié. Thème clair uniquement ; aucun sélecteur de thème n’est ajouté (vingt thèmes optionnels viendront d’un autre chantier, voir « Thèmes futurs »).

| Fichier | Rôle |
|---|---|
| `engine/couleurs_premium.css` | Dernière couche de la cascade (portail et fragments). Blocs générés `<tokens>`, `<specialites>`, `<categories>` ; règles qui ne lisent que des custom properties. |
| `docs/frontend/couleurs/palette.py` | Source unique : valeurs OKLCH, conversion sRGB, contrastes WCAG, contrôles photopiques (TCP, Duv, luminosité par rôle, plafond de chroma), appel de `validate_palette.js`, réécriture des blocs générés (`--ecrire`) et des tableaux de ce document (`--doc`). |
| `docs/frontend/couleurs/recuit.py` | Recuit simulé des 23 emplacements (bande de luminosité, contraintes du validateur, écart toutes paires, cibles sémantiques) ; `--emettre` produit les constantes à reporter dans `palette.py`. Non exécuté au build. |
| `docs/frontend/couleurs/sonde.py` | Sonde du rendu réel (Chromium) : part de surface en gris bleuâtre, bordures et ombres bleuâtres, texte bleu saturé de l’interface. |
| `docs/frontend/couleurs/validation.txt` | Sortie brute du validateur (`palette.py --valider --rapport …`). |
| `build_front.py` | Une ligne : injection de `medina-couleurs-premium` après `medina-finition-premium` (préfixe de spécificité premium). |
| `build_index.py` | Couche injectée en dernier sur le portail ; cartes de spécialité branchées sur `--sp-<id>`. |
| `engine/category_organisation.css` | Couche « survol » : valeurs littérales remplacées par les tokens ; contour de focus des leçons sans transition (indicateur immédiat). |

Commandes :

```bash
python3 docs/frontend/couleurs/palette.py --ecrire --doc --valider --rapport docs/frontend/couleurs/validation.txt
python3 docs/frontend/couleurs/sonde.py --site <dossier construit> --fragment S08 --lesson G45
```

## Vision photopique diurne — exigence de Vial (16 octobre 2026)

> « Des couleurs qui se rapprochent de la façon dont l’œil humain normal voit durant la journée. »

De jour, la vision est **photopique** : les cônes L, M et S travaillent, les bâtonnets sont saturés. Quatre conséquences ont été traduites en règles mesurables ; `palette.py` les vérifie à chaque génération (section « Vision photopique diurne » de sa sortie).

### 1. Luminosité perçue, et non valeur RVB

- Les couleurs sont posées en **OKLCH / OKLab**, espace construit pour que la luminosité `L` suive la clarté perçue ; la luminance de WCAG est la **luminance photopique CIE Y** (pondération V(λ), maximum vers 555 nm, le vert-jaune). C’est pourquoi un jaune et un bleu de même RVB « saturé » n’ont rien de commun : à 555 nm l’œil voit le plus clair, dans le bleu le plus sombre.
- **À rôle égal, luminosité égale** (écart ≤ 0,06, soit ± 0,03 en `L`) :

| Rôle | `L` OKLCH | Écart mesuré |
|---|---|---|
| Repères des 23 emplacements (`--cat-NN`, `--sp-<id>`) : filets, pastilles, icônes | 0,522 à 0,578 | 0,058 (avant : 0,151) |
| Encres de teinte (`--cat-NN-ink`) : texte en couleur | 0,430 | 0,002 |
| Fonds teintés (`--cat-NN-tint`) | 0,975 ± 0,003 (suivi à 1/10 du repère) | 0,008 |
| Sélections (`--cat-NN-sel`) | 0,945 ± 0,003 | 0,007 |
| Statuts (`--status-ok`, `-prep`, `-prov`) | 0,47 à 0,49 | 0,02 |

  L’ancienne palette étageait les repères sur trois paliers (0,46 / 0,535 / 0,61) : à l’Accueil, le bleu de Prusse de l’urologie pesait visiblement plus lourd que le corail de la cardiologie. Les repères sont désormais dans une bande de ± 0,03 : aucune spécialité ne « crie » plus qu’une autre.
- **Pas de bleu saturé pour le texte ni pour un détail fin.** Les cônes S sont rares (environ 5 %) et absents de la fovéola : un texte bleu saturé paraît flou et vibre. Le texte courant de l’interface (`--ink-1/2/3`) et le statut « En préparation » sont achromatiques (C ≤ 0,006, contre 0,018 à 0,024 en bleu ardoise auparavant). Les encres des teintes bleues à violettes (215° à 300°) sont plafonnées à C 0,080 : leur lisibilité repose sur le contraste de luminance (voies L + M), toujours ≥ 4,5:1.

### 2. Blanc de référence D65, papier très légèrement chaud

- sRGB est défini sous **D65**, la lumière du jour moyenne (6 504 K, Duv +0,0032). La surface des cartes reste le blanc D65 (`#ffffff`).
- Les autres neutres suivent un seul axe, teinte OKLCH **80°**, chroma ≤ 0,006 : un papier **neutre à très légèrement chaud**, sur le locus des lumières du jour. Mesures (température de couleur proximale, CIE 1960, Duv > 0 vers le vert) :

| Neutre | Avant | TCP · Duv avant | Après | TCP · Duv après |
|---|---|---|---|---|
| Papier `--n-paper` | `#f5f8f6` (h 160) | 6 530 K · +0,0046 (dérive verte) | `#f8f7f4` (h 80) | 6 355 K · +0,0036 |
| Encart `--n-sunken` | `#eff2f0` (h 160) | 6 530 K · +0,0047 | `#f2f0ed` | 6 315 K · +0,0033 |
| Filet `--n-line` | `#ced2d7` (h 250) | 6 925 K · +0,0036 (bleuté) | `#d3d1ce` | 6 290 K · +0,0032 |
| Contour `--n-line-strong` | `#7a8188` (h 250) | 7 600 K · +0,0048 (bleuté) | `#817e7b` | 6 110 K · +0,0027 |
| Texte `--ink-2` | `#353e4a` (h 255) | 11 015 K · +0,0055 (bleu ardoise) | `#3e3d3a` | 6 015 K · +0,0044 |
| Encre `--ink-1` | `#141a22` (h 255) | 13 425 K · +0,0064 (bleu nuit) | `#1a1917` | 5 825 K · +0,0040 |

  Bornes contrôlées : surfaces C ≤ 0,012 et 5 500 K ≤ TCP ≤ 6 600 K avec 0 ≤ Duv ≤ +0,005 (ni bleuté froid au-dessus de 6 600 K, ni crème jaunie au-dessous de 5 500 K, ni vert ni magenta) ; tous les neutres C ≤ 0,012 et TCP ≤ 6 600 K.
- Verdict sur les neutres repris : le papier et l’encart (teinte 160) n’étaient pas froids mais **légèrement verdâtres** (Duv +0,0047 au lieu de +0,0032) ; les filets, contours et encres (teintes 250-255) étaient **franchement bleutés** (6 800 à 13 400 K). Les deux sont corrigés.

### 3. Chroma modérée, relief sous une lumière venant d’en haut

- Plafond global C ≤ 0,15 (aucune couleur « néon ») ; repères C 0,10 à 0,12 ; seul l’or de l’étoile atteint 0,145 (L 0,76, métal et non fluorescence). Les rôles des cours conservés (`--lesson-*`) sont hors plafond : valeurs fixées par Vial, non appliquées par cette couche.
- **Ombres** : couleur `--n-shadow` = papier assombri (oklch 0,240 0,008 80), jamais un gris bleuâtre (avant : `rgb(16 24 36)`, teinte 255). La lumière vient d’en haut : liseré clair en haut des cartes (`inset 0 1px 0`), ombre portée décalée vers le bas, ombre de contact courte. Toutes les ombres littérales des couches antérieures (barre supérieure, accueil de fragment, bouton principal, Navigo, mode Livre, jauges-filtres) sont remplacées par les rôles `--shadow-0`, `--shadow-1`, `--shadow-2`, `--shadow-bar`, `--shadow-float`, `--shadow-pop`. Le voile des fenêtres (`--n-veil`) suit la même teinte.

### 4. Identité conservée, tout redéfinissable

- L’ancre `#1f3428` (`--brand-700`) et sa rampe (teinte 158,4°) sont inchangées : sur un papier neutre, le vert de Medina est la seule couleur d’identité de l’Accueil.
- Aucun sélecteur de thème n’est ajouté ; tout reste redéfinissable sur `:root` (voir « Thèmes futurs »).

### Compromis assumé

Égaliser la luminosité de 23 teintes réduit l’écart entre couleurs : on ne peut plus jouer sur trois paliers de clarté (0,46 / 0,535 / 0,61). Le recuit (`recuit.py`) a des objectifs hiérarchisés, tous atteints :

| Mesure | Avant (trois paliers) | Après (bande ± 0,03) | Seuil |
|---|---|---|---|
| Voisins contractuels, vision normale (ΔE OKLab ×100) | ≥ 15,3 | ≥ 15,6 | 15 (bloquant) |
| Voisins contractuels, protanopie/deutéranopie | ≥ 8,1 (PASS) | ≥ 6,8 (WARN, bande 6–8) | 6 (bloquant), 8 (cible) |
| Accueil en 3 colonnes, voisins verticaux (informatif) | ≥ 9,0 | ≥ 8,1 | — |
| Écart minimal toutes paires des 23 repères | 6,1 | 3,75 | 3,5 (contrôle `palette.py`) |
| Écart de luminosité entre repères | 0,151 | 0,058 | 0,06 |

Le passage de la séparation daltonienne dans la bande 6–8 est **légal uniquement avec un encodage secondaire** : c’est le cas partout (numéro et intitulé de chaque catégorie, nom de chaque spécialité, gouttières entre cartes). Deux teintes de même angle (rose et prune, 349°) ne diffèrent que par leur luminosité ; elles ne sont jamais voisines (rangs 5 et 19), et leurs fonds restent distincts parce que fonds et sélections suivent la luminosité du repère au dixième.

Spécialités, avant et après (l’identité sémantique est conservée pour la cardiologie, l’hématologie, la neurologie, la pneumologie, la psychiatrie et l’infectiologie) :

| Spécialité (ordre de l’Accueil) | Avant : repère, L C h | Après : repère, L C h | Après : encre | Après : fond |
|---|---|---|---|---|
| O-11-Obstétrique et néonatologie | `#874304` rouille (0.460 0.113 54) | `#a06504` cuivre (0.558 0.120 70) | `#704500` | `#fef6ed` |
| N-05-Neurologie | `#7e77c7` pervenche (0.610 0.119 286) | `#716bba` pervenche (0.569 0.120 285) | `#4c497a` | `#f6f6ff` |
| R-14-Rhumatologie et orthopédie | `#a07e12` moutarde (0.609 0.120 89) | `#786a02` moutarde (0.522 0.108 100) | `#5b5000` | `#f8f6eb` |
| D-16-Dermatologie | `#7c5aa6` amethyste (0.536 0.120 303) | `#b55868` vieux-rose (0.578 0.121 11) | `#842d40` | `#fff4f5` |
| O-17-Oto-rhino-laryngologie et médecine bucco-dentaire | `#099885` jade (0.610 0.109 180) | `#017799` petrole (0.531 0.102 227) | `#085872` | `#ecf8fe` |
| M-19-Médecine d’urgence, traumatologie et toxicologie | `#a74c52` garance (0.534 0.120 18) | `#9c5410` rouille (0.522 0.120 57) | `#793e00` | `#fef4ec` |
| G-04-Gastroentérologie et hépatologie | `#7c8d2e` anis (0.611 0.121 119) | `#058d7f` jade (0.578 0.102 183) | `#005d54` | `#edfbf9` |
| P-23-Psychiatrie et psychothérapie | `#6a438c` violet (0.461 0.120 307) | `#8b66b2` violet (0.579 0.119 305) | `#603b84` | `#faf5ff` |
| E-06-Endocrinologie et métabolisme | `#b86e32` cuivre (0.609 0.120 57) | `#997301` ocre (0.578 0.118 85) | `#654b00` | `#fcf7ed` |
| O-18-Ophtalmologie | `#5766b2` saphir (0.534 0.120 273) | `#457bbf` saphir (0.577 0.120 255) | `#30517b` | `#f1f8ff` |
| G-10-Gynécologie et sénologie | `#b8638d` rose (0.610 0.120 350) | `#9b4974` prune (0.522 0.121 349) | `#7d2e59` | `#fef2f7` |
| I-03-Infectiologie | `#2e6720` sapin (0.459 0.120 140) | `#418d4f` sapin (0.579 0.120 148) | `#0b6125` | `#f1fbf2` |
| U-15-Urologie et andrologie | `#035e8a` prusse (0.459 0.102 239) | `#7158a6` amethyste (0.521 0.121 297) | `#544676` | `#f7f4ff` |
| M-21-Médecine de premier recours et santé publique | `#4a9759` vert (0.611 0.120 148) | `#027c5d` malachite (0.521 0.105 168) | `#005f46` | `#edf9f4` |
| H-08-Hématologie | `#8e3648` grenat (0.461 0.120 11) | `#ad5a85` rose (0.579 0.120 349) | `#7d2f5a` | `#fff4f9` |
| P-02-Pneumologie | `#4887c9` bleuet (0.611 0.120 251) | `#2e72b1` bleuet (0.540 0.120 250) | `#2a527a` | `#eff8ff` |
| C-01-Cardiologie | `#c1645f` corail (0.611 0.120 24) | `#a34b3c` brique (0.522 0.120 31) | `#853023` | `#fff2f0` |
| N-07-Néphrologie | `#06779f` petrole (0.534 0.106 231) | `#0288a0` lagon (0.578 0.102 216) | `#005a6a` | `#edfbfe` |
| O-09-Oncologie, génétique médicale et soins palliatifs | `#9a5d04` ambre (0.535 0.117 66) | `#8e5f01` ambre (0.523 0.110 75) | `#6c4700` | `#fcf5eb` |
| D-20-Diagnostic clinique et examens complémentaires | `#0c93ab` azur (0.611 0.106 215) | `#019069` emeraude (0.579 0.120 166) | `#005f44` | `#effbf5` |
| I-13-Immunologie et allergologie | `#45509a` indigo (0.460 0.120 274) | `#5562ae` indigo (0.522 0.120 274) | `#434c7b` | `#f3f5ff` |
| M-12-Médecine des âges de la vie | `#707304` olive (0.535 0.117 112) | `#837e0e` olive (0.579 0.120 107) | `#565300` | `#f9f9ed` |
| E-22-Éthique médicale, droit et communication | `#a06bb2` orchidee (0.610 0.119 317) | `#8f4d8a` orchidee (0.521 0.120 330) | `#73336e` | `#fcf2fb` |

## Méthode

1. **Audit rendu** (`getComputedStyle` sur Accueil, fragment, catégorie, quatre onglets, fenêtre, Navigo, Livre ; S08 / G45 — Accidents ischémiques cérébraux transitoires et syndromes apparentés (N-05-Neurologie)) et sonde `sonde.py` avant/après.
2. **Tokens** posés en OKLCH : pas de luminosité réguliers, chroma plafonnée, teinte constante par rampe ; conversion sRGB et contrôle de gamut dans `palette.py`.
3. **Teintes catégorielles** : 23 emplacements choisis par recuit simulé dans la bande de luminosité 0,52–0,58 (maximiser l’écart minimal entre voisins sous protanopie et deutéranopie, simulation Machado 2009 ; plancher 15 en vision normale ; voisins verticaux de grille à 3 et 4 colonnes ; puis écart minimal toutes paires), puis **figés dans un ordre fixe**. Chroma 0,10 à 0,12 : assez pour porter une identité (plancher 0,10), assez bas pour rester sobre.
4. **Spécialités** : chaque spécialité reçoit un des 23 emplacements (identité fixe, Accueil et fragment), avec des cibles sémantiques pondérées (cardiologie rouge, hématologie grenat, neurologie pervenche, pneumologie bleu, psychiatrie violet, infectiologie vert sapin) sous la contrainte que l’ordre d’affichage de l’Accueil passe le validateur.
5. **Validation** : `validate_palette.js` (compétence dataviz) en mode clair sur la surface réelle `--n-paper`, contrôles photopiques de `palette.py`, puis `tools/front_garde.py`, `sonde.py` et `tools/front_capture.py`.

## Règles d’emploi

- **Encre / repère / fond.** Chaque teinte existe en quatre pas : repère (`--cat-NN`, filets, pastilles, icônes ; ≥ 3:1), encre (`-ink`, L 0,43, texte ≥ 4,5:1), fond teinté (`-tint`, L 0,975, C 0,015) et sélection (`-sel`, L 0,945, C 0,028). Aucune grande surface saturée.
- **Accent du contexte.** `--accent`, `--accent-ink`, `--accent-tint`, `--accent-sel` valent la marque sur l’Accueil et la teinte de la spécialité dans un fragment (`html[data-medina-fragment="S08"]{--accent:var(--sp-s08)…}`). Les variables historiques (`--atlas-accent`, `--mp-*`, `--mz-*`, `--p-*`, `--bg`, `--ink`…) sont ramenées sur ces tokens.
- **Catégories.** `engine/atlas_v2.js` pose `--cat` en style en ligne (20 couleurs vives par rang). La couche les remappe par sélecteur d’attribut (`[style*="--cat: #C2185B" i]` → `--cat-01`) avec `!important` : le rang *n* prend l’emplacement *n*. Au-delà du 23ᵉ rang (S08 : 29 catégories, S10 : 30, T1 : 25, T3 : 26), les rangs 24 à 32 reçoivent des tokens de débordement `--cat-24` … `--cat-32` : la teinte d’angle d’or posée par atlas_v2.js, ramenée en OKLCH dans la même bande de luminosité ; ces rangs, les moins prioritaires pour l’Examen fédéral, ne sont pas couverts par le validateur (aucune palette de plus de 23 teintes ne peut l’être) et restent portés par leur numéro et leur intitulé.
- **Statuts** (`--status-ok`, `--status-prep`, `--status-prov`) : toujours avec leur libellé et une forme (disque plein « Lire le cours », cercle vide « En préparation », demi-disque sur la mention de publication provisoire) ; jamais la couleur seule.
- **Jauges** : rampe séquentielle à une teinte (marque, 158,4°), piste `--gauge-track` cernée de `--gauge-edge` (≥ 3:1), remplissage dégradé `--gauge-fill-top` → `--gauge-fill` (5,7:1 sur la piste).
- **Étoile d’or** : facettes conservées, contour `--star-edge` (5,7:1) ; bandeau PROFILES et bouton Pareto en aplat `--gold-100`, texte `--gold-800` (8,5:1).
- **Leçon** : les rôles sémantiques fixés par Vial sont conservés à l’identique (`--lesson-*` : bleu marine du cycle, titres rouges soulignés, termes orange foncé, mot vert, abréviations). Point signalé à Vial : le corps des cours du cycle (`#0f2c66`, bleu marine, C ≈ 0,11) est un bleu assez saturé ; son contraste de luminance (13,4:1) garantit la lisibilité, mais un marine désaturé (C ≈ 0,06) serait plus fidèle à la règle photopique. Non modifié ici : c’est une règle de Vial portée par `engine/tetrade_cycle.css`, hors périmètre de ce chantier.
- **Contours interactifs** : boutons, champs, onglets d’outils, options de quiz, pagination du Livre, Navigo → `--n-line-strong` (≥ 3:1 sur surface, papier et encart).
- **Ombres** : uniquement par les rôles `--shadow-*` ; jamais une couleur d’ombre littérale.
- **Thèmes futurs** : tout est redéfinissable sur `:root` ; un thème peut remplacer les primitives (`--n-*` dont `--n-shadow` et `--n-veil`, `--ink-*`, `--brand-*`, `--cat-NN*`, `--gold-*`, `--gauge-*`, `--status-*`) ou les rôles (`--accent*`, `--focus-ring`, `--shadow-*`, `--gauge-*`, `--star-*`). Dans un fragment, l’accent est fixé par la règle `html[data-medina-fragment="…"]` : un thème qui veut le changer redéfinit `--sp-<id>` (ou `--cat-NN`). Pour qu’un thème garde la règle photopique, il suffit de modifier les constantes de `palette.py` (`NEUTRE_H`, `NEUTRES`, `OMBRE`, `BANDE_REPERES`, `EMPLACEMENTS`) et de relancer les contrôles.

## Tokens (valeurs du thème par défaut)

<!-- <tokens-doc> — généré par palette.py --doc ; ne pas éditer à la main. -->

### Neutres, marque, statuts, jauges, or, leçon

L / C / h : valeurs OKLCH mesurées sur l’hexadécimal arrondi. TCP : température de couleur proximale (CIE 1960, locus de Planck), Duv > 0 vers le vert.

| Token | Valeur | L / C / h (OKLCH) | TCP · Duv | Rôle |
|---|---|---|---|---|
| `--n-surface` | `#ffffff` | 1.000 / 0.000 / — | 6505 K · +0.0033 | Cartes, îlots, fenêtres, Navigo (blanc D65) |
| `--n-paper` | `#f8f7f4` | 0.976 / 0.004 / 91.4 | 6355 K · +0.0036 | Fond de page (surface de validation) |
| `--n-sunken` | `#f2f0ed` | 0.956 / 0.005 / 78.3 | 6315 K · +0.0033 | Encarts, puits, jauges informatives, survol neutre |
| `--n-line-soft` | `#e3e2df` | 0.913 / 0.004 / 91.4 | 6345 K · +0.0036 | Séparations décoratives (non interactives) |
| `--n-line` | `#d3d1ce` | 0.861 / 0.005 / 78.3 | 6290 K · +0.0032 | Bordures de cartes, de tableaux et d’îlots |
| `--n-line-strong` | `#817e7b` | 0.595 / 0.006 / 67.7 | 6110 K · +0.0027 | Contours interactifs (≥ 3:1 sur surface, papier et encart) |
| `--ink-3` | `#5f5d5a` | 0.479 / 0.005 / 78.3 | 6075 K · +0.0032 | Texte atténué (≥ 4,5:1 sur encart) |
| `--ink-2` | `#3e3d3a` | 0.360 / 0.005 / 91.5 | 6015 K · +0.0044 | Texte courant de l’interface |
| `--ink-1` | `#1a1917` | 0.214 / 0.004 / 84.6 | 5825 K · +0.0040 | Encre primaire, titres de l’interface |
| `--n-shadow` | `#211f1b` | 0.240 / 0.008 / 84.6 | 5420 K · +0.0046 | Couleur des ombres (papier assombri) |
| `--n-veil` | `rgb(29 26 22 / 0.55)` | oklch(0.220 0.008 80 / 0.55) |  | Voile des fenêtres (papier assombri, 55 %) |
| `--brand-50` | `#f1f9f4` | 0.975 / 0.011 / 158.8 |  | Rampe de la marque |
| `--brand-100` | `#e2f3e8` | 0.949 / 0.023 / 157.6 |  | Rampe de la marque |
| `--brand-200` | `#c8e5d3` | 0.896 / 0.039 / 158.3 |  | Rampe de la marque |
| `--brand-300` | `#a2cdb3` | 0.810 / 0.058 / 158.3 |  | Rampe de la marque |
| `--brand-400` | `#71aa89` | 0.689 / 0.077 / 158.2 |  | Rampe de la marque |
| `--brand-500` | `#488a67` | 0.579 / 0.087 / 158.8 |  | Rampe de la marque |
| `--brand-600` | `#2d684a` | 0.469 / 0.079 / 158.9 |  | Rampe de la marque |
| `--brand-700` | `#1f3428` | 0.303 / 0.035 / 158.4 |  | Rampe de la marque |
| `--brand-800` | `#122219` | 0.234 / 0.028 / 158.7 |  | Rampe de la marque |
| `--status-ok` | `#296a3b` | 0.470 / 0.100 / 149.9 |  | Statut « Disponible » (disque plein) |
| `--status-ok-bg` | `#e7f8e9` | 0.962 / 0.027 / 148.8 |  | Fond du statut |
| `--status-prep` | `#5f5d5a` | 0.479 / 0.005 / 78.3 |  | Statut « En préparation » (cercle vide) |
| `--status-prep-bg` | `#f2f0ed` | 0.956 / 0.005 / 78.3 |  | Fond du statut |
| `--status-prov` | `#8a5111` | 0.491 / 0.105 / 62.3 |  | Statut « Provisoire » (demi-disque) |
| `--status-prov-bg` | `#fef1db` | 0.963 / 0.032 / 81.0 |  | Fond du statut |
| `--gauge-400` | `#71aa89` | 0.689 / 0.077 / 158.2 |  | Rampe séquentielle des jauges |
| `--gauge-500` | `#488a67` | 0.579 / 0.087 / 158.8 |  | Rampe séquentielle des jauges |
| `--gauge-600` | `#2d684a` | 0.469 / 0.079 / 158.9 |  | Rampe séquentielle des jauges |
| `--gauge-700` | `#234c36` | 0.380 / 0.060 / 158.2 |  | Rampe séquentielle des jauges |
| `--gold-100` | `#fff3ce` | 0.964 / 0.050 / 92.2 |  | Étoile d’or, Pareto |
| `--gold-300` | `#f8d376` | 0.879 / 0.120 / 88.2 |  | Étoile d’or, Pareto |
| `--gold-500` | `#e1a52c` | 0.760 / 0.145 / 79.7 |  | Étoile d’or, Pareto |
| `--gold-600` | `#bc7d19` | 0.640 / 0.130 / 71.9 |  | Étoile d’or, Pareto |
| `--gold-700` | `#925a1a` | 0.520 / 0.105 / 64.3 |  | Étoile d’or, Pareto |
| `--gold-800` | `#643d17` | 0.399 / 0.075 / 61.7 |  | Étoile d’or, Pareto |
| `--lesson-ink` | `#0f2c66` | 0.310 / 0.108 / 262.2 |  | Corps des cours du cycle (bleu marine renforcé) |
| `--lesson-title` | `#b3261e` | 0.501 / 0.178 / 28.7 |  | Titres et numéros rouges soulignés |
| `--lesson-term` | `#9b3900` | 0.477 / 0.142 / 42.6 |  | Termes interactifs des cours du cycle |
| `--lesson-word` | `#187349` | 0.493 / 0.107 / 157.7 |  | Mot vert : fenêtre explicative ou contentieux |
| `--lesson-abbr` | `#205d55` | 0.437 / 0.064 / 183.2 |  | Abréviation à clé du glossaire |

### Rôles (alias)

| Token | Valeur | Rôle |
|---|---|---|
| `--accent` | `var(--brand-600)` | Accent du contexte : marque sur l’Accueil, teinte de spécialité dans un fragment (filets, pastilles, soulignés) |
| `--accent-ink` | `var(--brand-700)` | Texte et icônes en accent (≥ 4,5:1) |
| `--accent-tint` | `var(--brand-50)` | Fond teinté de l’accent (sélection légère, survol) |
| `--accent-sel` | `var(--brand-100)` | Fond de l’élément sélectionné ou courant |
| `--focus-ring` | `var(--accent-ink)` | Anneau de focus clavier (2 px, ≥ 3:1) |
| `--on-accent` | `var(--n-surface)` | Texte sur un aplat d’encre d’accent |
| `--shadow-color` | `var(--n-shadow)` | Couleur des ombres : surface assombrie, même teinte que le papier |
| `--shadow-0` | `0 1px 2px color-mix(in srgb,var(--shadow-color) 10%,transparent)` | Ombre de contact (boutons pleins, barres) |
| `--shadow-1` | `inset 0 1px 0 var(--n-surface),0 1px 2px color-mix(in srgb,var(--shadow-color) 5%,transparent),0 8px 22px -16px color-mix(in srgb,var(--shadow-color) 26%,transparent)` | Relief de repos des cartes (lumière d’en haut : liseré clair, ombre portée vers le bas) |
| `--shadow-2` | `inset 0 1px 0 var(--n-surface),0 2px 5px color-mix(in srgb,var(--shadow-color) 7%,transparent),0 14px 30px -18px color-mix(in srgb,var(--shadow-color) 32%,transparent)` | Relief au survol |
| `--shadow-bar` | `0 6px 16px -14px color-mix(in srgb,var(--shadow-color) 28%,transparent)` | Barre supérieure collante |
| `--shadow-float` | `0 2px 6px color-mix(in srgb,var(--shadow-color) 8%,transparent),0 10px 26px -18px color-mix(in srgb,var(--shadow-color) 40%,transparent)` | Boutons flottants (Navigo, pagination du Livre) |
| `--shadow-pop` | `0 2px 6px color-mix(in srgb,var(--shadow-color) 6%,transparent),0 22px 44px -26px color-mix(in srgb,var(--shadow-color) 40%,transparent)` | Fenêtres, Navigo, panneaux flottants |
| `--backdrop` | `var(--n-veil)` | Voile derrière une fenêtre explicative |
| `--gauge-track` | `var(--brand-50)` | Piste des jauges |
| `--gauge-edge` | `var(--n-line-strong)` | Contour de la piste (≥ 3:1) |
| `--gauge-fill` | `var(--gauge-600)` | Remplissage des jauges |
| `--gauge-fill-top` | `var(--gauge-500)` | Haut du dégradé de remplissage (relief) |
| `--star-edge` | `var(--gold-700)` | Contour de l’étoile d’or (≥ 3:1) |
| `--star-fill` | `var(--gold-500)` | Corps de l’étoile d’or |
| `--star-light` | `var(--gold-300)` | Facette éclairée de l’étoile |
| `--star-shade` | `var(--gold-600)` | Facette ombrée de l’étoile |

### Emplacements catégoriels (ordre fixe) et spécialités

Chaque emplacement `--cat-NN` a ses variantes `--cat-NN-ink` (texte), `--cat-NN-tint` (fond) et `--cat-NN-sel` (sélection). Chaque spécialité a `--sp-<id>`, `--sp-<id>-ink`, `--sp-<id>-tint`, `--sp-<id>-sel` (alias de son emplacement). Repères : L 0.522–0.578 ; encres : L 0.43 ; fonds : L 0.975 ; sélections : L 0.945.

| N° | Nom | Repère | L / C / h | Encre | L / C / h encre | Fond | Repère / papier | Encre / fond | Spécialité |
|---|---|---|---|---|---|---|---|---|---|
| 1 | moutarde | `#786a02` | 0.522 / 0.108 / 100.1 | `#5b5000` | 0.429 / 0.089 / 100.2 | `#f8f6eb` | 5.08:1 | 7.47:1 | `--sp-s10` R-14-Rhumatologie et orthopédie |
| 2 | petrole | `#017799` | 0.531 / 0.102 / 226.5 | `#085872` | 0.430 / 0.080 / 227.3 | `#ecf8fe` | 4.78:1 | 7.33:1 | `--sp-s12` O-17-Oto-rhino-laryngologie et médecine bucco-dentaire |
| 3 | vieux-rose | `#b55868` | 0.578 / 0.121 / 10.8 | `#842d40` | 0.430 / 0.120 / 10.5 | `#fff4f5` | 4.30:1 | 8.03:1 | `--sp-s11` D-16-Dermatologie |
| 4 | lagon | `#0288a0` | 0.578 / 0.102 / 216.0 | `#005a6a` | 0.430 / 0.076 / 215.2 | `#edfbfe` | 3.90:1 | 7.43:1 | `--sp-s04` N-07-Néphrologie |
| 5 | prune | `#9b4974` | 0.522 / 0.121 / 349.4 | `#7d2e59` | 0.429 / 0.120 / 349.6 | `#fef2f7` | 5.45:1 | 8.00:1 | `--sp-s14` G-10-Gynécologie et sénologie |
| 6 | olive | `#837e0e` | 0.579 / 0.120 / 106.7 | `#565300` | 0.431 / 0.093 / 107.3 | `#f9f9ed` | 3.96:1 | 7.52:1 | `--sp-t2` M-12-Médecine des âges de la vie |
| 7 | amethyste | `#7158a6` | 0.521 / 0.121 / 296.8 | `#544676` | 0.430 / 0.079 / 296.3 | `#f7f4ff` | 5.37:1 | 7.69:1 | `--sp-s15` U-15-Urologie et andrologie |
| 8 | ambre | `#8e5f01` | 0.523 / 0.110 / 75.2 | `#6c4700` | 0.429 / 0.091 / 75.1 | `#fcf5eb` | 5.18:1 | 7.64:1 | `--sp-t4` O-09-Oncologie, génétique médicale et soins palliatifs |
| 9 | bleuet | `#2e72b1` | 0.540 / 0.120 / 249.6 | `#2a527a` | 0.429 / 0.081 / 250.2 | `#eff8ff` | 4.71:1 | 7.56:1 | `--sp-s02` P-02-Pneumologie |
| 10 | brique | `#a34b3c` | 0.522 / 0.120 / 31.4 | `#853023` | 0.430 / 0.120 / 31.1 | `#fff2f0` | 5.40:1 | 7.86:1 | `--sp-s01` C-01-Cardiologie |
| 11 | jade | `#058d7f` | 0.578 / 0.102 / 182.7 | `#005d54` | 0.430 / 0.076 / 183.5 | `#edfbf9` | 3.83:1 | 7.34:1 | `--sp-s03` G-04-Gastroentérologie et hépatologie |
| 12 | orchidee | `#8f4d8a` | 0.521 / 0.120 / 330.0 | `#73336e` | 0.430 / 0.120 / 330.5 | `#fcf2fb` | 5.45:1 | 7.92:1 | `--sp-t7` E-22-Éthique médicale, droit et communication |
| 13 | emeraude | `#019069` | 0.579 / 0.120 / 165.7 | `#005f44` | 0.430 / 0.090 / 165.7 | `#effbf5` | 3.77:1 | 7.27:1 | `--sp-t5` D-20-Diagnostic clinique et examens complémentaires |
| 14 | pervenche | `#716bba` | 0.569 / 0.120 / 285.4 | `#4c497a` | 0.431 / 0.080 / 285.3 | `#f6f6ff` | 4.34:1 | 7.69:1 | `--sp-s08` N-05-Neurologie |
| 15 | ocre | `#997301` | 0.578 / 0.118 / 85.4 | `#654b00` | 0.429 / 0.088 / 85.7 | `#fcf7ed` | 4.08:1 | 7.68:1 | `--sp-s05` E-06-Endocrinologie et métabolisme |
| 16 | saphir | `#457bbf` | 0.577 / 0.120 / 255.1 | `#30517b` | 0.430 / 0.080 / 255.1 | `#f1f8ff` | 4.05:1 | 7.58:1 | `--sp-s13` O-18-Ophtalmologie |
| 17 | rouille | `#9c5410` | 0.522 / 0.120 / 56.6 | `#793e00` | 0.430 / 0.104 / 57.1 | `#fef4ec` | 5.31:1 | 7.74:1 | `--sp-t3` M-19-Médecine d’urgence, traumatologie et toxicologie |
| 18 | malachite | `#027c5d` | 0.521 / 0.105 / 167.7 | `#005f46` | 0.431 / 0.088 / 167.3 | `#edf9f4` | 4.85:1 | 7.14:1 | `--sp-t6` M-21-Médecine de premier recours et santé publique |
| 19 | rose | `#ad5a85` | 0.579 / 0.120 / 349.1 | `#7d2f5a` | 0.430 / 0.119 / 349.1 | `#fff4f9` | 4.28:1 | 8.06:1 | `--sp-s06` H-08-Hématologie |
| 20 | sapin | `#418d4f` | 0.579 / 0.120 / 147.8 | `#0b6125` | 0.431 / 0.120 / 147.7 | `#f1fbf2` | 3.81:1 | 7.21:1 | `--sp-t1` I-03-Infectiologie |
| 21 | violet | `#8b66b2` | 0.579 / 0.119 / 305.4 | `#603b84` | 0.431 / 0.121 / 305.3 | `#faf5ff` | 4.22:1 | 7.97:1 | `--sp-s09` P-23-Psychiatrie et psychothérapie |
| 22 | cuivre | `#a06504` | 0.558 / 0.120 / 69.7 | `#704500` | 0.430 / 0.093 / 69.7 | `#fef6ed` | 4.50:1 | 7.72:1 | `--sp-s16` O-11-Obstétrique et néonatologie |
| 23 | indigo | `#5562ae` | 0.522 / 0.120 / 274.2 | `#434c7b` | 0.431 / 0.079 / 274.4 | `#f3f5ff` | 5.23:1 | 7.55:1 | `--sp-s07` I-13-Immunologie et allergologie |
| 24 | debord-24 | `#9165a7` | 0.578 / 0.110 / 313.8 | `#653b7a` | 0.431 / 0.110 / 313.4 | `#fdf6ff` | 4.24:1 | 8.05:1 | débordement |
| 25 | debord-25 | `#6e6e0b` | 0.521 / 0.110 / 109.7 | `#545300` | 0.429 / 0.093 / 109.0 | `#f8f8ed` | 5.03:1 | 7.51:1 | débordement |
| 26 | debord-26 | `#067ca6` | 0.550 / 0.110 / 231.3 | `#115774` | 0.430 / 0.080 / 231.6 | `#effaff` | 4.41:1 | 7.50:1 | débordement |
| 27 | debord-27 | `#ae5c75` | 0.578 / 0.110 / 1.7 | `#7e314c` | 0.429 / 0.110 / 1.0 | `#fff5f8` | 4.27:1 | 8.09:1 | débordement |
| 28 | debord-28 | `#42793b` | 0.522 / 0.110 / 141.5 | `#275e20` | 0.430 / 0.110 / 141.5 | `#f2faf1` | 4.86:1 | 7.28:1 | débordement |
| 29 | debord-29 | `#6469b1` | 0.549 / 0.111 / 279.0 | `#474a7b` | 0.429 / 0.081 / 279.8 | `#f6f7ff` | 4.67:1 | 7.76:1 | débordement |
| 30 | debord-30 | `#aa6730` | 0.578 / 0.111 / 57.3 | `#783e00` | 0.429 / 0.103 / 57.6 | `#fff7ef` | 4.18:1 | 7.96:1 | débordement |
| 31 | debord-31 | `#007c62` | 0.522 / 0.102 / 171.4 | `#005e4a` | 0.429 / 0.083 / 171.7 | `#eefbf6` | 4.83:1 | 7.32:1 | débordement |
| 32 | debord-32 | `#95588f` | 0.549 / 0.110 / 330.6 | `#71366c` | 0.431 / 0.111 / 330.6 | `#fef5fd` | 4.82:1 | 8.05:1 | débordement |

<!-- </tokens-doc> -->

## Résultats (16 octobre 2026)

**Référence « avant »** : `main` 2b9da0d (couches antérieures, sans ce système de couleurs). **« Après »** : cette branche, 23 fragments construits, Accueil, S08 / G45 — Accidents ischémiques cérébraux transitoires et syndromes apparentés (N-05-Neurologie).

- `palette.py --valider` : 0 échec de contraste, 0 teinte hors gamut, tous les contrôles photopiques réussis ; validateur dataviz : **ALL CHECKS PASS** sur les 9 séquences contractuelles (rang 1 à 23, Accueil, colonnes de 3 et 4) et sur la rampe des jauges (`--ordinal`). CVD dans la bande 6–8 (WARN légal, encodage secondaire présent) ; vision normale ≥ 15,6. Sortie brute : `validation.txt`.
- `tools/front_garde.py` (390 et 1280 px) : avant 0 échec, après **0 échec** (police, erreurs, débordement, contraste, saturation, cartes, transitions, mouvement réduit, focus).
- `node tests/verify_categories.cjs` : OK (1 107 contrôles, 23 fragments) ; `node tests/verify_fragment_frontends.cjs` : passed (1 089 contrôles) ; `python -m unittest discover -s tests` : 777 tests OK.
- Sonde du rendu (`sonde.py`, 1 280 px) :

| Page | Fond de page (L / C / h) | Surface en gris bleuâtre | Bordures gris bleuâtre | Ombres gris bleuâtre | Texte gris bleuté (interface) | Texte bleu saturé (interface) |
|---|---|---|---|---|---|---|
| Accueil, avant | 0,975 / 0,003 / 128 | 0 % | 138 | 38 | 144 | 0 |
| Accueil, après | 0,976 / 0,004 / 91 | 0 % | 8 ¹ | 0 | 0 | 0 |
| Fragment S08, avant | 0,975 / 0,003 / 128 | 5,3 % | 87 | 37 | 231 | 31 |
| Fragment S08, après | 0,976 / 0,004 / 91 | 0 % | 0 | 0 | 0 | 0 |
| Leçon G45, avant | 0,975 / 0,003 / 128 | 3,1 % | 35 | 14 | 142 | 23 |
| Leçon G45, après | 0,976 / 0,004 / 91 | 0 % | 0 | 0 | 0 | 2 ² |

¹ Contours des pictogrammes de spécialité bleues (`--sp-<id>-sel`, C 0,028) : teinte d’identité voulue, non un neutre.
² Code et statut de l’en-tête de Leçon en `--lesson-ink` (`#0f2c66`), rôle conservé de Vial (voir « Leçon »).

