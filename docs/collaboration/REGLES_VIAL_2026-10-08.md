# Règles du propriétaire — 8 octobre 2026 (Claude et Codex)

Ces règles ont été données par Vial le 8 octobre 2026 aux deux IA. Elles priment sur les consignes antérieures contraires.

## 1. Progression et parallélisme
- **Parallélisme multi-agent = plusieurs sous-agents au sein d'un même chapitre**, chacun propriétaire de ses fichiers (catégories, onglets ou sections du chapitre).
- **Le chapitre suivant s'enchaîne une fois le chapitre courant produit et remis à l'autre IA pour audit.** Les corrections des chapitres remis restent prioritaires sur la production en cours.

## 2. Densité et tableaux
- Employer un tableau **seulement lorsqu'il est pertinent** : classifications, énumérations, comparaisons.
- Cellules au contenu clair, bref et cohérent ; en-têtes explicites ; tableau intuitivement lisible. Un bon tableau remplace le bavardage.

## 3. Contentieux de sources
- Le référentiel **le plus récent l'emporte** dans le texte principal.
- La version antérieure, lorsqu'elle reste utile (encore en vigueur ailleurs, différente), reste accessible par un **mot vert interactif** qui ouvre une fenêtre datée.
- Une précision ou une nuance de source se place de préférence dans une **fenêtre derrière un mot vert**. Exemple décidé : ESC 2026, tableau 18 (« C » = insuffisance cardiaque chronique, stades B à D) est cité dans I42 — Cardiomyopathies (C-01-Cardiologie) dans une fenêtre accessible depuis un mot vert.

## 4. Sources suisses
- L'information professionnelle suisse se lit sur compendium.ch (page produit `…/product/<id>-<nom>/mpro`). L'outil `tools/compendium_fi.cjs` en extrait les sections par rendu Chromium :
  `NODE_PATH=$(npm root -g):$PWD/node_modules node tools/compendium_fi.cjs "<produit>" [section…]`
- Citer : « Information professionnelle suisse, compendium.ch, <produit>, consultée le <date> ».
