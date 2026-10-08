# Police Anthropic Serif — contrôle du 8 octobre 2026

Police authentique récupérée depuis les ressources publiques référencées par https://www.anthropic.com/ : le CSS officiel https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/css/ant-brand.shared.775d58967.min.css déclare `font-family: Anthropic Serif` pour le romain et l'italique.

Écrits dans `/workspace/work/medina-resume` :

- `assets/fonts/AnthropicSerif-Roman-Web.woff2` : 175356 octets.
- `assets/fonts/AnthropicSerif-Italic-Web.woff2` : 166724 octets.
- `assets/fonts/PROVENANCE.json` : URL directes, empreintes SHA256, métadonnées et couverture.
- `shell/typography.css` : deux faces variables, `--medina-serif`, corps/interfaces/cours/fenêtres, axe optique automatique ; code monospace conservé.

Les fichiers originaux portent « Anthropic Serif Web », version `26.043.1`, fabricant BSPK LLC, designers BSPK × Geist × Anthropic, et `Copyright 2025-2026 Anthropic PBC`. Les axes vérifiés sont `wght` 300–800 et `opsz` 16–48. Tous les caractères français testés sont présents. `μ`, `α`, `β` sont absents ; les familles serif de secours fournissent ces glyphes sans changer l'identité du texte courant.

Contrôle Chromium `151.0.7922.173` réussi : romain/italique chargés, fontes réellement rendues identifiées par CDP (`isCustomFont: true`, noms PostScript Anthropic), accents français, poids 650, secours grec Liberation Serif, aucune erreur JavaScript ni requête HTTP externe. Capture inspectée : `/workspace/work/anthropic-font-research/preview.png`. Preuve : `/workspace/work/anthropic-font-research/browser-results.json`.

Pour des HTML autonomes, le constructeur lit la CSS puis remplace les deux chemins `../assets/fonts/AnthropicSerif-{Roman,Italic}-Web.woff2` par `data:font/woff2;base64,` suivi du contenu encodé des fichiers correspondants. Injecter ce style partagé en dernier dans `<head>`, après les CSS de surface. CSS embarquée : 457377 octets. Le coordinateur et l'auteur du portail ont reçu cette intégration exacte ; `build_front.py` et `build_index.py` n'ont pas été modifiés par cet agent.

Disponibilité publique HTTP vérifiée sur les ressources officielles. Aucun champ de licence ni permission de redistribution n'est annoncé dans le CSS ou les fichiers ; cette disponibilité ne constitue pas une licence libre. La provenance conserve cette limite et le copyright. Aucune police de substitution n'a été renommée « Anthropic ».
