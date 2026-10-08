# MEDINA — thème clair uniquement, 8 octobre 2026

## Résultat

Les sources d'interface produisent des HTML au thème clair. Le bouton et le moteur sombre, leurs règles CSS et la lecture/enregistrement du choix sombre ont été retirés. La seule référence de production restante à `medina.dark` est une migration `localStorage.removeItem`, protégée contre les navigateurs qui refusent le stockage. `color-scheme:only light` demande aussi des composants natifs clairs et interdit l'assombrissement automatique pris en charge par cette propriété.

Le front original, ses thèmes chromatiques, les outils de lecture et les interactions de cours restent présents. Aucune source médicale, banque de fenêtres, aucun glossaire ni registre de production n'a été modifié par cette mission. Aucun commit ni écriture dans `dist/`.

Base locale observée : `61a841b3c96b3bd4f3ad58ec5870d06945e63292`.

## Fichiers modifiés

- `shell/polish.js` : retrait de `autoDark`, `autoLight`, `darkButton`, du stockage/chargement de l'état sombre et des observateurs liés ; migration de l'ancienne clé ; conservation des repositionnements, onglets et autres modules.
- `shell/polish.css` : retrait du bouton et de toutes les règles `html.mdn-dark` ; contrastes du thème clair appliqués sans condition sombre ; `color-scheme:only light`.
- `shell/fragment.css` : retrait des variables sombres propres aux fragments.
- `modules/cardiovascular_cs.css` : retrait des trois règles sombres de la scène CS injectée dans S01. Fichier supplémentaire annoncé et confirmé libre par le coordinateur.
- `tests/verify_sciences_cs.cjs` : contrôle CS clair remplaçant l'injection forcée sombre ; option facultative `MEDINA_QA_BASE_URL` pour le même contrôle via HTTP, en conservant le défaut `file://`.
- `tests/verify_light_theme.cjs` : contrôle navigateur global + 22 fragments, anciennes préférences, palettes et fenêtres.

Patch complet : `/workspace/work/theme-clair.patch`.

## Vérifications réellement exécutées

1. `node --check shell/polish.js`, `node --check tests/verify_light_theme.cjs`, `node --check tests/verify_sciences_cs.cjs` : réussis. Le dernier test complet exécute également la version finale du nouveau script.
2. `git diff --check -- shell/polish.js shell/polish.css shell/fragment.css modules/cardiovascular_cs.css tests/verify_sciences_cs.cjs tests/verify_light_theme.cjs` : réussi.
3. Recherche des marqueurs sombres dans `shell/`, `engine/`, `modules/` : aucun `mdn-dark`, `autoDark`, `mdn-dk-*`, `darkMode`, `mdn-theme`, `theme-toggle` ou `prefers-color-scheme`. La clé historique subsiste uniquement pour sa suppression.
4. Reconstructions réussies dans `/workspace/work/theme-clair-build` : `MEDINA_OUT=/workspace/work/theme-clair-build python3 build_front.py`, puis `--all-fragments`. Après découverte des trois règles CS, seul S01 a été reconstruit avec `--fragment S01`.
5. `MEDINA_OUT=/workspace/work/theme-clair-build MEDINA_QA_OUT=/workspace/work/theme-clair-qa node tests/verify_light_theme.cjs` : **314 contrôles réussis, 23 HTML, 100 palettes par HTML, zéro erreur JavaScript inattendue**. Navigateur : Chromium `151.0.7922.173`. Préférence système sombre émulée, ancienne clé `medina.dark=1`, ancien thème `night`, suppression de cette clé, absence de bouton/classes/moteur sombre, surfaces claires mesurées, choix chromatique réel, conservation du carnet, vues mobiles global et S01. Ouverture de la scène thorax CS, des quatre onglets I83 et d'une fenêtre explicative I83 : fonds clairs vérifiés. Les empreintes des HTML sont restées stables pendant le contrôle.
6. Captures global et S01 mobiles inspectées visuellement : surfaces claires, boutons de lecture et navigation présents. Fichiers dans `/workspace/work/theme-clair-qa/`.
7. Suite existante `verify_sciences_cs.cjs` exécutée réellement via HTTP : **292 assertions réussies avant échec**, zéro erreur JavaScript, puis arrêt sur `I83 — Varices des membres inférieurs : discipline 2 avec figure et liens`. Ce résultat n'est pas présenté comme une réussite de la suite.

Preuve complète : `/workspace/work/theme-clair-qa/light-theme-browser-results.json`.
Preuve du contrôle partiel : `/workspace/work/theme-clair-sciences-cs/science-cs-browser-results.json`.

## Limites constatées

- La coque globale importe dès le chargement `lesson-core.js`, lecteur historique absent du dépôt. Le navigateur rapporte `Failed to fetch dynamically imported module ... /lesson-core.js`. Le test de thème trace ce seul message précisément identifié dans `knownLimitations` et échoue sur les autres erreurs JavaScript. Le module absent n'a pas été simulé ni remplacé.
- La politique Chromium de cet environnement bloque `file://` par `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Le contrôle existant a donc été exécuté avec les mêmes HTML par un serveur `127.0.0.1`, grâce à l'option HTTP. Aucun contrôle `file://` réussi n'est revendiqué.
- Diagnostic ciblé de l'arrêt I83 : le panneau `i83-s-histo` possède le texte « Science → traitement. », mais aucun `figure svg[role="img"][aria-label]`. Les panneaux biochimie et génétique n'en possèdent pas non plus. Cette condition de contenu n'est pas modifiée dans le cadre du thème. Le contrôle dédié des onglets/fenêtres I83 passe.
- La coque originale conserve une ancienne définition `night` dont `applyTheme` est remplacé par le moteur des 100 palettes actuelles claires. Son chargement depuis un ancien état a été testé : rendu clair. La coque protégée n'a pas été modifiée.
- Ce travail vérifie le comportement technique du thème ; il ne constitue ni audit médical, ni validation d'un fragment, ni preuve de publication distante. Le coordinateur gère l'application au dernier `main`, l'intégration et la livraison.
