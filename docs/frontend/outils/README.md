# Outils de contrôle du frontend MEDINA

Cette page recense les automates du frontend et les outils externes recommandés. Elle concerne l’interface construite, jamais le contenu médical.

## Automates

| Nom | Rôle | Commande |
|---|---|---|
| `front_garde` | Contrôle qualité rapide du frontend construit, réutilisable à chaque PR : police, erreurs, débordement, contraste, saturation, cartes, mouvement, focus, axe-core | `python3 tools/front_garde.py --out <MEDINA_OUT> --json rapport.json` |

**Préparer le dossier.** `MEDINA_OUT=<dossier> python3 build_front.py && python3 build_front.py --all-fragments`, puis `python3 build_index.py --fragments-dir <dossier>/fragments --output <dossier>/index.html`. Copier `assets/images` vers `<dossier>/images` et `<dossier>/fragments/images`, comme `pages.yml`.

**Pages contrôlées.** L’Accueil (`index.html`), la page du fragment (`--fragment`, S08 par défaut), une Leçon (`--lecon`, sinon la première leçon rédigée) et Navigo ouvert. Chaque page est contrôlée à 390 et 1280 px, puis rechargée sous `prefers-reduced-motion: reduce`.

**Navigateur.** L’outil utilise le module Python `playwright` et un Chromium déjà présent. Il ne lance jamais `playwright install`. Si la version du module ne correspond pas au navigateur, il cherche un exécutable sous `PLAYWRIGHT_BROWSERS_PATH`, `/opt/pw-browsers` ou `~/.cache/ms-playwright`. L’option `--chromium` impose un chemin. Code retour : 0 si tout passe, 1 en cas d’échec, 2 si le contrôle ne peut pas s’exécuter.

### Seuils documentés

| Contrôle | Règle d’échec |
|---|---|
| police | Première famille calculée de `body` et du conteneur ≠ Atkinson Hyperlegible Next, police non chargée, ou moins de 90 % des glyphes rendus en Atkinson (CDP `CSS.getPlatformFontsForNode`). Les codes en chasse fixe sont une exception signalée. |
| erreurs | Erreur JavaScript, erreur de console ou réponse HTTP ≥ 400. La requête implicite du navigateur vers `/favicon.ico` est seulement informative. |
| debordement | `scrollWidth` > `clientWidth` à 390 px ; l’outil liste les coupables les plus externes. |
| contraste | Rapport WCAG 2.x < 4,5:1 sur 80 éléments de texte visibles. L’alpha et l’opacité sont composés. Sur un dégradé, le pire arrêt l’emporte. Un fond d’image est noté « indéterminé ». `--grand-texte-wcag` applique 3:1 au grand texte. |
| saturation | Fond ou arrêt de dégradé de saturation HSL ≥ 80 % et luminosité HSL entre 30 et 70 %, sur au moins 4 000 px² d’un même élément (≈ 63 × 63 px). Les petites pastilles restent permises. |
| cartes | Rapport max/min > 1,2 en hauteur ou en largeur des cartes visibles (`.specialty-card`, `.mcg-category-card`). |
| transitions | Durée + délai d’une transition > 300 ms (pseudo-éléments inclus). |
| mouvement-reduit | Sous `reduce`, une transition ou une animation > 20 ms, ou `scroll-behavior: smooth`. |
| focus | Au clavier (20 Tab), un lien ou un bouton focalisé sans contour, ombre ou changement de fond, de bordure, de couleur ou de soulignement. |
| axe | axe-core 4.13.0, règles WCAG 2.0/2.1 A et AA, à 1280 px. Résultat informatif ; `--axe-strict` fait échouer les violations `serious` ou `critical`. |

**axe-core intégré.** Le paquet npm ne télécharge aucun navigateur. `--installer-axe` exécute `npm install --no-save --ignore-scripts axe-core@4.13.0` dans `~/.cache/medina-front-garde/`. `--axe <axe.min.js>` ou `AXE_CORE_JS` désignent un fichier existant. Sans fichier, le contrôle axe est simplement omis.

## Outils recommandés

| Outil | Statut | Justification |
|---|---|---|
| [axe-core](https://www.npmjs.com/package/axe-core) | Intégré | Moteur d’accessibilité de référence, injecté dans la page par `add_script_tag` puis `axe.run()`. Il ne couvre qu’une partie des critères WCAG ; les contrôles propres de `front_garde` le complètent. |
| [@axe-core/playwright](https://www.npmjs.com/package/@axe-core/playwright) | Recommandé pour des tests Node | API chaînable (`new AxeBuilder({ page }).analyze()`), avec injection dans tous les cadres et exclusions par sélecteur. |
| [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) | Recommandé en CI | `lhci autorun` avec `staticDistDir` sert le dossier construit et audite chaque HTML. Les budgets d’accessibilité et de performance s’écrivent en assertions. Trois passages par URL, médiane retenue. |
| [Playwright `toHaveScreenshot`](https://playwright.dev/docs/api/class-snapshotassertions) | Recommandé | Régression visuelle : la première exécution crée la référence, les suivantes la comparent. Régler `maxDiffPixelRatio` (≈ 1 % pour une page) et masquer les zones changeantes. |
| [pa11y-ci](https://github.com/pa11y/pa11y-ci) | Optionnel | Parcourt une liste d’URL ou un sitemap avec les moteurs HTML_CodeSniffer et axe. Il échoue au-delà d’un seuil, mais il fait doublon avec axe-core intégré. |

Ces outils mesurent la technique et l’accessibilité. Ils ne valident ni la médecine ni la pédagogie.

## Référence « avant » — construction de `main` `d1a488ad`, 15 octobre 2026

Commande : `python3 tools/front_garde.py --out <dossier> --axe <axe.min.js>`, sur le fragment S08 et la leçon C70, avec Chromium 141, en 40 s. Résultat : **ÉCHEC, 18 contrôles en échec**, code retour 1.

| Contrôle | Résultat | Constats principaux |
|---|---|---|
| police | ok | Atkinson Hyperlegible Next calculée et rendue sur les quatre pages (≥ 99,9 % des glyphes) |
| erreurs | ok | Aucune erreur JS ni ressource manquante, hors favicon implicite |
| debordement | ok | Aucun défilement horizontal à 390 px |
| contraste | **échec** (6/8) | Accueil : texte blanc sur jaune `#ffc93c` dans `.overview .motifs li` (1,45:1). Surtitres `.eyebrow` et `.section-kicker` orange `#e0613f` sur `#e9f7ff` (3,23:1). Fragment : `.mcg-category-foot span` à 35 % d’opacité (2,08:1) ; « Neurologie » blanc sur jaune (1,54:1). Leçon : onglets `.mc-tabs button` blanc sur `#00b4c6` (2,52:1). axe confirme : 2 nœuds sur l’Accueil, 160 sur le fragment. |
| saturation | **échec** (6/8) | Accueil : bandeau `.overview` `#ffc93c` (HSL 43/100/62). Fragment : couverture `.mcg-cover` `#0869b4` (206/91/37), lien actif de la barre latérale `#00b4c6`, lien `.medina-home` jaune. Leçon : onglets `#00b4c6` (185/100/39). |
| cartes | ok | Ratio des hauteurs 1,05 (Accueil) à 1,13 (fragment à 1280 px) ; largeurs 1,00 |
| transitions | **échec** (6/8) | `.mdn-toast` : `transition: all 0.4s` (400 ms) sur le fragment, la Leçon et Navigo |
| mouvement-reduit | ok | `prefers-reduced-motion` respecté partout |
| focus | ok | 17 à 19 éléments focalisés par page, tous avec un indicateur visible |
| axe | info | Seule violation : `color-contrast` (serious) ; aucune sur la Leçon ni sur Navigo |
