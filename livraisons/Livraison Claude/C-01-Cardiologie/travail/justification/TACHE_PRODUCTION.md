# Production — justification d'une partie d'un cours

Entrées : le code du cours `<CODE>`, la liste de fichiers qui te sont confiés et ton suffixe `Pn` (P1 ou P2). Les sources sont dans `chapters/<CODE>/`. Le dossier de résultats est `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/<CODE>/`. Lis d'abord `CONSIGNES.md`.

## 1. Inventaire
Lis intégralement chaque fichier confié. Relève chaque affirmation médicale qui ne porte pas son pourquoi : phrase, cellule de tableau, item de liste, encadré, légende de figure, Pareto, réponse ou rétroaction de quiz, rubrique de fenêtre. Ignore une affirmation déjà expliquée sur place ou dans la fenêtre qu'ouvre un mot vert voisin. Ne relève pas de faux positifs.

## 2. Choix de la forme
- **Complément dans le texte**, si une à trois phrases suffisent : réécris le passage avec son mécanisme.
- **Fenêtre**, si l'explication est longue ou sert à plusieurs endroits. Réutilise d'abord une fenêtre existante qui couvre le sujet (`grep -o 'data-pop="[^"]*" data-title="[^"]*"' chapters/<CODE>/*.html`) : action `completer`. Sinon, crée-en une : action `creer`, clé nouvelle `<code-minuscule>-<nom>`, absente du cours. Regroupe dans une même fenêtre les affirmations qui relèvent du même mécanisme.

## 3. Sorties (dans le dossier de résultats du cours)
**Le dossier est partagé avec l'autre producteur : ne jamais vider ni supprimer un dossier ou un fichier qui ne porte pas ton suffixe ou ne correspond pas à tes fichiers confiés.**
- `edits/<FICHIER>.json` (par exemple `edits/I30_a.json`) : liste `[{"id":"<FICHIER>-<n>", "old":…, "new":…, "source":…}]`.
  - `old` est un passage **exact** du fichier, présent **une seule fois**. Il est court : une phrase, une cellule ou un item ; il ne contient aucun bouton et ne chevauche aucun autre `old`.
  - `new` reprend `old` avec l'explication intégrée. Il garde toutes les balises de `old` et ne contient aucun bouton.
- `jobs/<cle>__<Pn>.json` : `{"cle":…, "titre":…, "action":"creer"|"completer", "fichier_cible":"<FICHIER>", "ancres":[{"file":"<FICHIER>", "id":"<FICHIER>-a<n>", "old":…, "label":…}]}`.
  - `label` est une sous-chaîne exacte de 2 à 7 mots de `old`, hors balise et hors bouton existant ; elle deviendra le mot vert.
  - Une ancre ne doit pas se trouver dans la fenêtre qu'elle ouvre.
  - Le `old` d'une ancre ne doit pas recouvrir le `old` d'un complément.
  - Pour `creer`, `fichier_cible` est un fichier pop du cours que tu traites, choisi par cohérence de thème.
- `out/<cle>__<Pn>.html` :
  - pour `creer`, le template complet `<template data-pop="CLE" data-title="TITRE">…</template>`, avec ses rubriques Physiologie normale, Mécanisme, Conséquence clinique, Ce qui change la décision et Source (intitulés adaptables) ;
  - pour `completer`, seulement les rubriques nouvelles, sans redire l'existant, terminées par « Source complémentaire ».
- `out/<cle>__<Pn>.json` : `{"sources":[références complètes vérifiées], "reserves":[…], "ancres_retirees":[], "label_modifies":[]}`.
- `bilan_<Pn>.json` : nombre d'affirmations relevées, de compléments, de fenêtres créées ou complétées, erreurs du cours trouvées et réserves.

## 4. Vérification avant de rendre
Relis tout comme un examinateur sceptique : chaque chiffre est contrôlé dans la source, `old` est unique, le HTML est valide et `verifier_sigles.py` affiche `{}` sur chaque fichier `out/*.html` et sur le texte de tes `new`. Ta réponse finale tient en quelques lignes : les chiffres du bilan et les erreurs du cours trouvées.
