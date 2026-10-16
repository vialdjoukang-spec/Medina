# Frontend premium — note de conception (15 octobre 2026)

**Périmètre.** Accueil (portail `index.html`), accueils des 23 fragments, pages de catégorie, Leçons (quatre onglets), Navigo. Aucun cours, glossaire, nosologie ni donnée médicale n’est modifié ; l’architecture (un HTML et une navigation par fragment) est conservée.

## Logique des catégories (et des spécialités de l’Accueil)

**Ordre retenu : priorité Examen fédéral, puis CIM-10-GM.** Les catégories qui réunissent le plus de pathologies de l’Examen fédéral (correspondances PROFILES 2017 / SSP, déjà portées par les étoiles d’or) viennent d’abord ; à égalité, l’ordre de la CIM-10-GM garde ensemble les familles voisines. C’est un ordre d’affichage seulement (`fragment_surface.order_blocks`) : la numérotation 1., 2., … le suit partout (grille, barre latérale, page de catégorie), l’ordre CIM d’origine reste disponible dans `cim_order`, et la règle est rappelée en petite police sous « Les catégories ». Chaque carte indique sous son titre le nombre de pathologies de l’Examen fédéral qu’elle contient. L’Accueil applique la même règle aux 23 spécialités (poids Examen fédéral, puis rang du registre), avec un rang discret au-dessus du titre ; il ne s’ouvre donc plus sur la cardiologie par simple ordre de registre.

## Couches ajoutées

| Fichier | Rôle |
|---|---|
| `engine/finition_premium.css` | Dernière couche des fragments, injectée par `build_front.py` avec un préfixe de spécificité supérieur aux couches historiques. Palette claire et neutre, accent de spécialité atténué, séparations de 1 px (opacité 0,25 à 0,38), cartes de taille identique (`grid-auto-rows:1fr`), focus visible, transitions de 220 ms en ease-out au survol et au focus seulement. |
| `engine/finition_premium.js` | Navigo : parties dépliables (survol, focus clavier, premier toucher, flèches ← →), ligne de descente et chevron, partie et titre courants mis en évidence pendant la lecture, barre « Position de lecture » qui avance en douceur. Les boutons du plan ne sont ni déplacés ni renommés. |
| `engine/portal_premium.css` | Dernière couche du portail : bandeau de synthèse et fonds dégradés remplacés par des surfaces claires, cartes de spécialité uniformes à filet de couleur. |

`prefers-reduced-motion: reduce` ramène toutes les durées à 0 et supprime les mises à l’échelle. Dans `shell/polish.css`, l’apparition des cartes au défilement (cartes à 35 % d’opacité hors champ) et les animations infinies (halo, anneau, rotation) sont retirées ; l’entrée de page devient un fondu de 220 ms.

## Bug de l’accueil « qui ouvre sur la cardiologie »

`index.html` est bien le portail multi-spécialités (`build_index.py`). Le lien « L’atlas » du portail mène à `organisation.html`, dont le script (`organisation/dashboard_template.html`) présélectionnait `fragments[0]`, c’est-à-dire **C-01-Cardiologie**, en l’absence d’ancre (titre de page « MEDINA · C-01-Cardiologie »). Sans ancre, la page ouvre désormais une vue d’ensemble des 23 spécialités ; les liens profonds `#fragment=…` sont inchangés. Le workflow Pages n’est pas en cause et n’a pas été modifié.

## Automates

- `tools/front_capture.py` : construit un fragment (ou tous) et l’Accueil, puis capture Accueil, accueil du fragment, catégories, une catégorie, Leçon, Sciences, Navigo (survol d’une partie) à 390 et 1280 px, plus police 24 px et mode Livre à 1280 px ; rapport JSON des erreurs JavaScript.
  `python3 tools/front_capture.py --build fragment --fragment S04 --lesson N18 --site /tmp/front --out docs/frontend/premium/captures --prefix apres`
- `tools/front_garde.py` (contrôles automatiques : police, couleurs saturées, uniformité, contraste, mouvement réduit, erreurs JS, débordement) et la recherche d’outils reconnus (axe-core, Lighthouse CI, régression visuelle Playwright) sont confiés à un second agent (branche `claude/frontend-garde-g1`).

## Captures

`captures/avant-*.png` (état publié) et `captures/apres-*.png` (cette branche), N18 — Maladie rénale chronique (N-07-Néphrologie). Le moteur de lecture garde ses quatre onglets, ses fenêtres, la taille de police et le mode Livre.

## Vérifications

`python3 test_v7.py --static N18 E12` OK ; `python -m unittest discover -s tests` : 737 tests OK ; `verify_fragment_bootstrap`, `verify_fragment_filters`, `verify_category_progress` (23 fragments) OK ; `verify_organisation --targeted` OK ; `tools/front_garde.py` (branche du second agent) : 0 échec sur S04/N18 et S08/G45, axe non exécuté (paquet absent hors ligne).

## Corrections des défauts hérités de main

- Mode Livre : la mise en page horizontale fonctionnait mais restait invisible en haut de Leçon ; les pages prennent un aspect de feuille (colonne de 72 caractères, ombre douce) et la pagination « Partie précédente · n / N · Partie suivante » reste collée en bas d’écran (vérifiée : le bouton suivant avance d’une page).
- Barre latérale des fragments : le filtre passe avant la liste des catégories, qui n’est plus tronquée à mi-ligne (la barre défile d’un seul tenant) ; au-delà de 720 px, le doublon « Filtre » du contenu est masqué (il reste sur mobile, où la barre est un tiroir).
- Onglets collants : alignés sur `--mdn-top`, sans bande où le texte défile.
- Accueil : jauges sur un seul niveau, séparées par des filets.

## Réserve

- `tests/verify_fragment_frontends.cjs` attend 23 liens `fragments/` sur l’Accueil ; main en publie déjà 92 (jauges cliquables) : échec antérieur à cette branche, hors du workflow Pages.

## Recommandations

1. Retirer progressivement les couches historiques superposées (`atlas_v2` à `harmonie_v5`, `portal_v2`/`v3`) au profit de jetons uniques ; les sélecteurs à attributs répétés et `!important` rendent chaque finition plus coûteuse.
2. Ajouter la garde frontend au workflow Pages (chemin partagé `.github/workflows`, mission d’intégration requise).
3. Servir Atkinson en WOFF2 externe préchargé (`font-display: swap`) plutôt qu’en base64 : exige de copier `shell/fonts` dans `_site` depuis le workflow Pages (chemin partagé). Anthropic Serif n’est déjà plus incorporée dans l’Accueil (elle reste une option du lecteur de cours).

`MEDINA.html` (atlas global) importait `./lesson-core.js`, absent de la publication : le module embarqué est désormais importé depuis un blob, sans erreur JavaScript.
