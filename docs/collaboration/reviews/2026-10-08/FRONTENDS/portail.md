# Portail d’accueil MEDINA — 8 octobre 2026

Modification source : `build_index.py` uniquement, dans `/workspace/work/medina-resume`.

L’accueil présente 22 espaces de spécialité, leurs titres lisibles sans identifiants en grand, une icône distincte, leur accent hérité du frontend construit, une courte description et leur nombre propre de cours intégrés. La page adopte le papier ivoire `#faf9f6`, l’encre `#292821`, les tons secondaires `#73726b`, des cartes légèrement en relief et un accueil spacieux. Aucun cours médical global n’est affiché et aucun lien vers le regroupement `MEDINA.html` n’est proposé.

Les routes de fragments `fragments/MEDINA_<id>_<slug>.html` sont conservées. Les noms canoniques complets restent dans le titre des liens. La liste et son ordre viennent du registre des 22 fragments ; les champs de présentation et les comptes proviennent du JSON `medina-category-organisation-data` de chaque HTML construit, y compris après décodage de `mdn-pack` si nécessaire. Aucun calcul de propriétaire n’est recopié et aucune taille de fichier n’est montrée. Le total de cette construction est de 32 cours intégrés. Ce nombre ne constitue pas une validation médicale ni une déclaration de complétude.

L’authentique Anthropic Serif, romain et italique, fournie par `shell/typography.css` et les deux fichiers WOFF2 locaux, est embarquée en `data:font/woff2;base64` dans le portail : la page n’exige aucune requête externe. Le thème reste clair lorsque le navigateur préfère le sombre. La recherche ignore les accents et la casse, annonce son résultat via une région `aria-live`, propose un état vide et des commandes de réinitialisation, conserve l’accès au clavier et répond à Échap. Les liens ont un focus visible ; les mouvements sont neutralisés avec `prefers-reduced-motion`.

## Vérifications réellement exécutées

- Compilation Python et génération de l’accueil à partir des 22 HTML de `/workspace/work/theme-clair-build/fragments`.
- 20 contrôles navigateur réussis : 22 cartes et 22 routes distinctes, total de 32 cours cohérent avec les données intégrées, absence de lien global médical, vraie Anthropic Serif chargée, zéro requête externe et erreur JavaScript, clair sous préférence sombre, recherche française sans accents, résultat vide, réinitialisation et Échap, parcours clavier et focus visible, absence de débordement à 1440, 390 et 320 pixels.
- Inspection visuelle des captures desktop et mobile ; titre compact sur mobile pour laisser apparaître la première spécialité rapidement.

Résultats : `browser-report.json`. Captures : `captures/accueil-desktop.png`, `captures/accueil-mobile.png`, `captures/recherche-mobile.png`. HTML compilé : `index.html`.

La preuve a utilisé une construction des fragments antérieure aux nouveaux champs de présentation de l’agent responsable de `fragment_surface.py` ; les accents/descriptions de cette construction ont donc des valeurs de repli. Une construction récente apporte automatiquement les nouveaux accents et descriptions, sans modification du portail. Le propriétaire frontend reste celui décidé par le helper central du fragment construit.

Aucune source médicale, `engine/category*`, `fragment_surface.py`, `build_front.py`, branche ou publication modifiée par cette mission.
