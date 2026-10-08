# Nouvelles têtes Claude — comparaison en lecture seule, 8 octobre 2026

Les seules branches changées depuis le snapshot complet précédent sont `claude/affectionate-fermi-xpf9yz` (`18e4150` → `6be5e247e98f3104cb58f6184e409dab3eb1e624`) et la nouvelle branche `claude/vigilant-mayer-cevhwj` (`b272295dd318044ab748a760f7a5fbfbec7a957c`). Aucun de leurs changements ne touche une source A41, B24 ou la livraison interne d’Infectiologie. Aucune contribution distante n’a été fusionnée, publiée, injectée ou appliquée.

## Base, dates et méthode

- Dépôt lu : `/workspace/work/medina-resume`, HEAD local observé `79d8ece8ed8742da6c753e02080caa7904486d02`, daté du 8 octobre à 17:57:23 UTC.
- Base demandée et branche d’intégration distante : `2f4a7dbffba7c43ec791fb6dcea4be7d553ff5a9`, datée de 16:08:58 UTC ; `main` distant est encore identique lors de ce fetch.
- Fetch effectué avec `git fetch --no-write-fetch-head --no-tags origin '+refs/heads/*:refs/remotes/origin/*'`. Il actualise les références distantes locales et les objets Git, sans modifier la branche de travail ou ses fichiers. Les analyses écrivent exclusivement dans ce dossier scratch.
- Dernière tête Fermi : 17:20:08 UTC ; tête Vigilant : 18:07:48 UTC. La date de commit établit la chronologie du dépôt, pas la provenance d’une nouvelle demande directe du propriétaire.
- Le scan du coordinateur à 18:15:08 UTC contient 22 têtes et vise la bonne branche `codex/protocole-fragments-20261008`, au SHA `2f4a7db`. Il conserve `scan_complete: false` à cause de limites de comparaison historiques. Les preuves complémentaires ci-dessous lèvent précisément les quatre troncatures sans modifier cet index.

`comparaison-exacte.json` contient les périmètres exacts des nouvelles branches. Les fichiers `*-base2f.diff` sont les diffs complets des arbres aux deux SHA, sans renommages. Fermi diverge avant la base : son merge-base avec `2f4a7db` est `baa69c5a96cc7189319b720ad318e62fcdc8a7ee`. Une comparaison des arbres Fermi/base contient 85 chemins ; elle ne signifie pas 85 nouveaux fichiers à importer. La contribution depuis son merge-base contient 47 chemins et le delta depuis la précédente tête Claude seulement 14. Vigilant a pour parent exact `2f4a7db` : les trois périmètres coïncident, 14 fichiers.

## Quatre têtes historiques : identité démontrée

| Tête exacte | Fichiers du diff complet | Résultat contre l’ancien snapshot |
| --- | ---: | --- |
| `39b7ff0cc585c59ffbb99fb448940daa1950b34d` | 571 | Tous les chemins et statuts identiques |
| `4d8efb864bf7e95357d589c7ac865c641d54f751` | 2 689 | Tous les chemins et statuts identiques |
| `83bff147e0aba6b31e7a080e098770b0a6b4250d` | 591 | Tous les chemins et statuts identiques |
| `fdad6c8adac0c9e623d469211674bdab666d6c47` | 615 | Tous les chemins et statuts identiques |

Les quatre têtes distantes restent aux mêmes SHA. Les listes ont été recalculées par `git diff --no-renames --name-status -z <merge-base> <head>`, avec merge-base exact `20915d9a36f0ebc65a79ec6428357727dd5afe6c`, puis rapprochées de `files-exact-<SHA>.json` du précédent snapshot. La détection de renommages doit rester désactivée : avec elle, la liste de `4d8efb8` n’a que 2 599 entrées, certaines suppressions/ajouts étant regroupées. Ce changement de compte ne représente pas une modification de la tête.

Preuve reproductible : `historique-identite-preuve.json`, avec date UTC, empreintes SHA-256 des anciens fichiers de preuve, références distantes correspondantes et noms des quatre nouvelles listes exactes. Ces têtes conservent les divergences et audits historiques déjà décrits dans `../RAPPORT_REPRISE_SYNC.md` ; aucune nouvelle réserve médicale ou technique n’est déduite de leur simple redécouverte.

## Fermi : quatorze fichiers depuis `18e4150`

```text
M CHAPTER_SPEC.md
M chapters/J09/J09_a.html
M chapters/J09/J09_b.html
M chapters/J09/J09_c.html
M chapters/J09/J09_d.html
M chapters/J09/J09_pop1.html
M chapters/J09/J09_pop2.html
M chapters/J09/J09_pop_pa.html
M chapters/J09/J09_pop_sciences.html
M engine/medina_course.css
M modules/cardiovascular_cs.css
M modules/cardiovascular_cs.html
M organisation/libelles_clairs.json
A tools/compendium_fi.cjs
```

Le contenu médical nouveau est J09/Pneumologie et la sémiologie cardiovasculaire. Les repères « Piège », « Instant réflexe », « Il faut y penser », « Instant examen fédéral » reçoivent une spécification et un style `data-flag`. L’outil Compendium lit des sections françaises par Chromium ; sa sortie constitue une extraction à contrôler, pas la preuve qu’une FI intégrale a été obtenue. La présente mission n’a pas exécuté cet outil contre des produits ni fait une relecture clinique de J09 ou du module cardiovasculaire.

La comparaison globale à `2f4a7db` montre aussi des divergences moteur antérieures à `18e4150`, déjà repérées lors de la synchronisation précédente :

- `fragment_surface.py` ajoute `tools/libelles.py` et `organisation/libelles_clairs.json`, pour reformuler les titres affichés en conservant les codes. Ces dépendances doivent accompagner une éventuelle intégration. L’isolation et la propriété des cours restent contrôlées dans le helper.
- `engine/atlas_v2.css` impose Atkinson dans les cours et fenêtres malgré le sélecteur de police conservé, réduit la largeur des cartes, impose cinq colonnes à partir de 1 500 px et utilise un gris-bleu de page différent. `engine/atlas_v2.js` reporte la couleur de catégorie dans le cours et supprime `data-theme`. `engine/portal_v2.css` masque l’illustration d’accueil et modifie les colonnes. Ce sont des choix fonctionnels et visuels à comparer aux instructions directes, pas une nouvelle correction médicale T1.
- `engine/category_organisation.js` retire l’override de la page méthode propre à la spécialité. `tests/verify_fragment_frontends.cjs` retire les contrôles du contraste 4,5:1, de la police réellement rendue, du choix de police appliqué à Navigo et aux fenêtres, de la page méthode et de certaines propriétés du portail. Ces suppressions ne prouvent pas que les garanties antérieures sont devenues inutiles.
- `tests/verify_light_theme.cjs` rétablit un clic direct sur une carte de thème historiquement masquée par Atlas ; le repli utilisé dans la cible actuelle disparaît. Risque de test navigateur bloqué sur un élément caché lors d’une intégration globale.
- `tools/build_work_preview.py` retire `display:flex` de l’override de barre supérieure de l’aperçu. Aucun changement de périmètre médical n’apparaît dans ce hunk.
- Les différences d’arbres contiennent des suppressions de captures et preuves Codex présentes dans la cible mais absentes de la branche divergente. Elles ne doivent pas être prises pour des suppressions de preuves demandées par Claude.

**Réserve reproduite :** le contrôle des libellés de Fermi échoue pour I99. Sa table renvoie `Troubles circulatoires sans précision diagnostique`, alors que son propre test interdit `sans précision`. Le résultat a été reproduit en chargeant les blobs Git de `tools/libelles.py`, de sa table et du catalogue en mémoire, sans import ou écriture dans le dépôt. Aucune correction n’a été appliquée.

## Vigilant : quatorze fichiers depuis la base `2f4a7db`

```text
M AGENTS.md
M CLAUDE.md
M COORDINATION.md
A docs/collaboration/instructions/CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE.md
A docs/collaboration/instructions/CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE.pdf
A docs/collaboration/receipts/2026-10-08_CLAUDE_CONSIGNES_CHAINE_CONTINUE.md
A engine/federal_exam.css
A engine/federal_exam.js
M fragment_surface.py
A organisation/PILE_FRAGMENTS.html
A organisation/federal_exam.json
A organisation/pile_fragments.json
A tools/consignes_pdf.py
A tools/pile_fragments.py
```

Le nouveau document dit maintenir la remise de fragment entier, l’auto-revue, l’audit croisé unique et l’immutabilité INJECTÉ. Il ajoute une progression continue, une couverture de toutes les catégories CIM sans lacune, le parallélisme par catégorie, une priorité des corrections et une pile visible. Il attribue à Claude l’achèvement de la cardiologie historique avant Pneumologie ; Codex reste T1 puis Neurologie. Il distingue explicitement son inventaire CIM-10-GM de la certification CIM-11. Aucun registre médical ou de statut n’est modifié par ces quatorze fichiers.

Le PDF est généré à partir du Markdown par `tools/consignes_pdf.py`, avec métadonnées d’auteur attribuant les consignes au propriétaire et la mise en forme à Claude. Le reçu est émis par Claude. **Il s’agit d’une livraison documentaire Claude, distincte du PDF joint par l’utilisateur et de ses demandes directes.** Les déclarations d’autorité et de priorité qu’elle contient ne sont pas appliquées automatiquement par cette analyse.

Le frontend injecte le registre et les deux assets du filtre à chaque `finish_surface`. Le filtre ne retire aucune catégorie : il marque en doré les leçons correspondant à un code ou un `covers` sélectionné, mémorise l’état par fragment et respecte la préférence de réduction des animations. Ce branchement est indépendant de l’import J09 ; l’import isolé du hunk Python sans les assets/registre ferait échouer la compilation.

Le registre T1 est expressément provisoire et reprend dix codes prioritaires : A41, B24, B18, A54, A53, B50, A04, A69, A15 et A16. Le document le présente comme une sélection éditoriale, sans pondération officielle fédérale. Le contrôle clinique et documentaire de cette sélection reste à faire dans son périmètre.

La pile s’appuie sur `frontend_catalog`, sur les catégories du propriétaire et sur le registre des cours. Elle affiche T1 à **1/184 catégories couvertes**, puis S08 à **0/92**, et ne lit pas les sources de l’aperçu interne A41/B24. Le compteur mesure un rattachement au registre, pas une couverture médicale établie, une auto-revue ou une complétude du fragment. La pile ne peut pas servir de preuve que le paquet interne aurait disparu ni de certification d’un fragment achevé. Sa page annonce Atkinson mais n’embarque pas ses WOFF2 : le rendu peut dépendre des fontes installées.

Aucun test automatisé pour ces deux nouvelles fonctions n’est fourni dans la livraison. Le reçu Claude annonce un essai Chromium sur S01, choix mémorisé, viewport 390 px et absence d’erreur JavaScript ; ce constat déclaré ne couvre pas les 22 fragments et n’a pas été reproduit dans cette mission de comparaison.

## Portée pour la publication B24

Les blobs canoniques `chapters/A41/*`, `glossary/a41.py` et l’arbre `livraisons/Livraison Codex/I-03-Infectiologie/` sont identiques à `2f4a7db` dans les deux nouvelles têtes Claude. Les anciennes réserves A41 ne sont donc pas une nouvelle modification distante à appliquer au paquet gelé. Ni Fermi ni Vigilant n’est ancêtre de HEAD local lors du contrôle.

La publication autorisée du seul paquet B24 peut conserver son périmètre et ses dix-neuf sources gelées. L’import des nouvelles fonctions et consignes Claude constitue une décision distincte, à faire avec leurs dépendances, leurs réserves et leurs preuves. Cette analyse n’a pas modifié le paquet, un statut ou un fichier partagé ; elle ne constitue pas un nouvel audit croisé médical.
