# Alignement Atkinson Hyperlegible Next — 8 octobre 2026

Mission terminée en lecture seule dans le dépôt. Les quatre fichiers Claude de `f92867451d3e46cb160a53379f7196248e4f41a6`, repris par le coordinateur avec attribution, sont réellement **Atkinson Hyperlegible Next**, version 2.001. Les copies intégrées correspondent exactement aux quatre SHA d’origine.

| Fichier | Poids | Octets | SHA256 |
| --- | --- | --- | --- |
| `ahn-400.woff2` | 400 | 23428 | `60c177b18e401ab3d2dda0d82fa9e3dbf7617be9d93a2033176952570762300b` |
| `ahn-400i.woff2` | 400 italique | 25760 | `1ad06f7d63f2494886c9e9c0f22b6e725b0e162e5c6fe4282cd7931f5d699b91` |
| `ahn-600.woff2` | 600 | 24620 | `564fca06cd5a822a269ee8f255a545ae21b209b75ecc7673b12eb6e2f448684b` |
| `ahn-700.woff2` | 700 | 24688 | `c13348157dbcdb21060bb98e386f6471fa165e20d1d71528e72c67ca3d02a46b` |

Total : **98 496 octets**. Faces statiques 400, 400 italique, 600 et 700 ; aucun axe variable. Les accents français testés et μ, ≥, ≤, ±, ° sont présents. α, β et → nécessitent une famille de secours.

## Provenance et droits

Métadonnées : © 2020, 2024 Braille Institute of America, Inc. ; fabricants Applied Design Works et Letters from Sweden. Famille confirmée sur le site officiel https://www.brailleinstitute.org/freefont/.

Licence interne exacte, identique dans les quatre binaires :

> Braille Institute of America, Inc. provides Atkinson Hyperlegible for use, without derivatives or alteration, to the public free of charge for all non-commercial and commercial work. No attribution required.

Google Fonts publie aujourd’hui la famille Next sous OFL : `METADATA.pb` et `OFL.txt` officiels ont été récupérés séparément en scratch. Les quatre WOFF2 Google actuels v7 diffèrent des quatre binaires Claude ; leur origine CDN exacte et l’application de cette OFL à ces copies ne sont pas affirmées sur cette seule comparaison. Les assets Claude sont conservés sans altération.

## Contrôles réellement exécutés après intégration

Chromium `151.0.7922.173` : **40 assertions réussies**, 3 pages réelles du build servi sur `127.0.0.1:8767`, zéro erreur JavaScript. Les quatre WOFF2 embarqués dans le portail, T1/A41 et l’aperçu Infectiologie/A41 correspondent exactement aux SHA Claude ; les poids CSS déclarés sont maintenant les quatre valeurs statiques exactes.

CDP `CSS.getPlatformFontsForNode` confirme les quatre vraies faces Atkinson, leurs noms PostScript et `isCustomFont: true`. Le portail, le texte des cours et les fenêtres A41 rendent réellement Atkinson au défaut. Le cours démarre à 17 px avec un interligne proche de 1.6 ; passage à 18 px vérifié.

Après sélection **Georgia**, le cours, les paragraphes, Navigo, son titre, sa recherche, ses boutons et les fenêtres suivent `--mc-font`, tandis que le front reste Atkinson. Police et taille persistent après recharge. Dans cet environnement Linux, la famille CSS Georgia peut être rendue par sa fonte système de secours ; le contrôle distingue cette demande CSS de l’identité réelle donnée par CDP.

Contrôle supplémentaire des titres `.mcg-cover h1` : **Infectiologie (T1) et Cardiologie (S01), chacun en 1 360 et 390 px**, rendent exclusivement `AtkinsonHyperlegibleNext-Bold`, `isCustomFont: true`, poids 700. Aucun fallback ni fonte serif dans ces quatre titres. Tailles : 52 px sur desktop et 34 px sur mobile. Le doute visuel du titre Infectiologie est levé par la fonte réellement rendue.

## Règle de cascade vérifiée

Les exclusions `.mc,.mc *,.mc-dlg,.mc-dlg *,.mc-navigo,.mc-navigo *` de la famille globale préservent le lecteur. Navigo était aussi recapturé par le raccourci `font: ... Tahoma` de `shell/fragment.css` et par `var(--atlas-font)` sur ses titres. La correction du coordinateur effectivement observée gagne dans CDP :

```css
html[data-medina-fragment][data-medina-fragment] body
:is(.mc-navigo,.mc-navigo *):not(svg,svg *){
  font-family:var(--mc-font,var(--x-font))!important;
}
```

Aucun `--mc-font` forcé ne remplace le choix de lecture. Aucun fichier du dépôt n’a été modifié par cet agent. Cette famille constitue le choix commun de MEDINA ; le contrôle ne démontre pas un standard universel de lisibilité, ni une validation médicale.

Preuves scratch : `font-metadata.json`, `provenance-check.json`, `google-fonts-comparison.json`, `OFL.txt`, `browser-results.json`, `home-title-cdp.json`, `navigo-winning-styles.json`.
