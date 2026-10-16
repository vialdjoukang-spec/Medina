# front_poids — poids et vitesse de l’Atlas construit

Ce relevé porte sur l’état « avant » de `main` (`d1a488ad`, 15–16 octobre 2026). Le site a été construit par `build_front.py` et `build_front.py --all-fragments`, puis assemblé comme le fait `pages.yml` (copie des images, `build_index.py`). Le profil mobile émulé par CDP impose un CPU ralenti ×4, 150 ms de RTT et 1,44 Mbit/s de débit descendant. L’outil ne modifie aucun contenu médical.

```bash
MEDINA_OUT=/tmp/site python3 build_front.py && MEDINA_OUT=/tmp/site python3 build_front.py --all-fragments
python3 tools/front_poids.py --out /tmp/site --json /tmp/front_poids.json \
  --scenarios file-brut,file-mobile,http-brut,http-mobile [--budget budget.json] [--proposer-budget b.json]
```

Le code retour vaut 1 si un budget est dépassé. L’option `--sans-navigateur` limite la mesure aux poids. Chromium est pris dans `/opt/pw-browsers` ; `playwright install` n’est jamais appelé. La compression brotli est mesurée si le module `brotli` est installé.

## Résultats

| Page | Brut | gzip | Contenu dominant |
|---|---|---|---|
| Site entier (521 fichiers) | 304 Mo | 211 Mo | 51,8 Mo de copies identiques |
| `MEDINA.html` (atlas) | 67,5 Mo | 46,8 Mo | gabarits `mdn-pack` en base64 : 59,3 Mo |
| `fragments/…S03` (le plus lourd) | 23,0 Mo | 15,6 Mo | données 21,8 Mo |
| `fragments/…S08` (leçon mesurée) | 7,5 Mo | 3,4 Mo | pack 3,3 Mo, organisation 2,2 Mo |
| `index.html` (Accueil) | 691 ko | 465 ko | polices incorporées : 588 ko (85 %) |

| Temps (ms) | file brut | file mobile | HTTP mobile |
|---|---|---|---|
| Accueil : FCP / TTI | 140 / 140 | 456 / 456 | 3 636 / 3 864 |
| Leçon I63 (S08) : FCP / prête | 84 / 936 | 288 / 4 419 | 5 180 / 41 590 |
| Atlas `MEDINA.html` : FCP / prête | 140 / 6 742 | 384 / 28 211 | 7 632 / 368 843 |

Sur l’atlas, la plus longue tâche mobile dure 12,6 s et le tas JavaScript atteint 230 Mo. Sur la leçon, la couverture Chromium montre 79 % de CSS inutilisé (265 ko sur 336 ko, hors `@font-face`) et 64 % de JS inutilisé (171 ko sur 267 ko). Sur l’Accueil, le CSS inutilisé représente 38 % (13 ko). Les polices sont déclarées en `font-display: swap` et ne sont jamais préchargées, puisqu’elles sont incorporées. Sur six faces, trois seulement se chargent : Anthropic Serif romain et italique (342 ko binaires) ne servent ni sur l’Accueil ni sur la leçon. Un défaut a aussi été relevé : `MEDINA.html` importe `lesson-core.js`, absent de la sortie, et l’erreur « Failed to fetch dynamically imported module » apparaît à chaque ouverture.

## Budget proposé

Le budget de non-régression ajoute 10 % aux poids et 25 % aux temps mesurés. `--proposer-budget` en produit la version complète, avec toutes les pages. Extrait à garder dans la CI de construction :

```json
{"max": {
  "site.total.brut": 335000000,
  "pages.[MEDINA.html].total.brut": 74300000,
  "pages.[fragments/MEDINA_S08_nerveux.html].total.gzip": 3800000,
  "pages.[index.html].total.gzip": 600000,
  "couverture.lecon.css.inutilise": 300000,
  "couverture.lecon.js.inutilise": 190000,
  "temps.accueil.http-mobile.fcp_ms": 4600,
  "temps.lecon.file-mobile.pret_ms": 5600,
  "temps.atlas.file-mobile.pret_ms": 35300
}}
```

Cible après les recommandations ci-dessous : Accueil sous 150 ko gzip et FCP mobile HTTP sous 1,5 s ; leçon prête en moins de 2 s sur mobile file:// ; atlas prêt en moins de 5 s sur mobile file://.

## Cinq recommandations, par gain décroissant

1. **Charger les gabarits de cours à la demande.** Aujourd’hui, `MEDINA.html` décode d’un bloc 59,3 Mo de base64 (`atob` puis `Uint8Array.from` caractère par caractère), décompresse le tout et injecte environ 86 Mo de HTML dans un `div` caché. Un paquet gzip par cours, décompressé à l’ouverture de la route, ramène l’atlas à environ 8 Mo. On attend alors un état « prêt » de quelques secondes au lieu de 28 s sur mobile file://, de 369 s en HTTP mobile, et environ 200 Mo de tas en moins. Servir ces paquets en binaire `.gz` plutôt qu’en base64 retire en plus le surcoût de 33 %, soit environ 15 Mo.
2. **Sortir les polices des pages et retirer les faces inutilisées.** Les 588 ko de `@font-face` incorporés sont répétés dans les 25 pages : 10,6 Mo sont redondants sur le site, et ce bloc pèse 85 % de l’Accueil. La solution comprend trois actions : supprimer Anthropic Serif du chargement par défaut (option du lecteur, chargée sur demande : −456 ko par page), servir Atkinson en fichiers WOFF2 mis en cache, et précharger la face romaine. Sur l’Accueil, cela fait −3,1 s de FCP en HTTP mobile (588 ko à 188 ko/s).
3. **Dédoublonner les données d’organisation.** Les blocs `medina-category-organisation-data` totalisent 38,9 Mo bruts dans les fragments (11,1 Mo pour S10, qui pèse 13,1 Mo en tout). La moitié environ (19,3 Mo) répète `blocks` dans `nosology.lessons`. Une seule copie, chargée après le premier rendu, réduit le travail d’analyse JSON au démarrage de chaque fragment.
4. **Images : ne plus copier, et passer au WebP.** `pages.yml` copie `assets/img` et `images` une seconde fois sous `fragments/`, ce qui fait 51,8 Mo de doublons. Un chemin relatif `../assets/img` suffit. La conversion WebP (qualité 82) des 76 PNG/JPG fait passer leurs 31,6 Mo à 9,1 Mo (−71 %). Le seul `e10-09-immunology.png` pèse 5,6 Mo.
5. **Découper le CSS et le JS par route sur la leçon.** Sur la leçon, 265 ko de CSS et 171 ko de JS ne servent pas. Un exemple : le principal script en ligne (146 ko) est inutilisé à 90 %. Il faut charger les styles et scripts de l’examen fédéral, de l’atlas des systèmes et de l’organisation seulement sur leurs routes. On attend environ −400 ko analysés et une tâche longue mobile ramenée sous 500 ms (937 ms aujourd’hui). Il faut aussi corriger ou retirer l’import de `lesson-core.js`.

*Mesures locales (4 cœurs, Chromium 1194). Les temps varient d’une machine à l’autre, d’où la marge de 25 %. `http.server` n’applique pas gzip : les durées HTTP mobile sont donc des bornes hautes.*
