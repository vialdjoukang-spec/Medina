# Zones Compendium pré-marquées — convention commune

Une **zone Compendium** est un passage d'un cours dont le contenu suisse (posologie, contre-indication, interaction, autorisation, grossesse) doit être tiré de l'information professionnelle suisse en vigueur.

## Marquage
- Chaque cours peut porter `chapters/<CODE>/<CODE>_compendium.json` (format décrit dans `tools/compendium_zones.py`).
- Une zone désigne un passage par son **texte exact** (même principe que `<CODE>_justifications.json`), le produit et les sections à lire. Le HTML du cours ne change pas.
- Statut `a_lire` à la rédaction ; `lu` après lecture, avec la date et l'URL `…/mpro`.

## Lecture
- `node tools/compendium_fi.cjs "<produit>" <section…>` (rendu Chromium de compendium.ch) ; ou consultation directe de la page `https://compendium.ch/fr/product/<id>-<nom>/mpro`.
- Le texte du cours reprend ce que dit l'information suisse et le cite : « Information professionnelle suisse, compendium.ch, <produit>, consultée le <date> ».
- Si la recommandation internationale la plus récente diverge, elle reste dans le texte principal et l'information suisse est exposée derrière un mot vert (règle de contentieux du 8 octobre 2026), ou l'inverse quand la règle suisse est contraignante pour la prescription.

## Contrôle
- `python3 tools/compendium_zones.py verifier <CODE>` doit sortir sans erreur avant toute remise ou injection.
- `python3 tools/compendium_zones.py a_lire <CODE>` liste les zones restantes et la commande de lecture correspondante.
