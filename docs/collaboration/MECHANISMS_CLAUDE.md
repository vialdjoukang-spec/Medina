# Mission Claude — justifier chaque affirmation

Consigne de Vial du 7 octobre 2026, [transmise dans PR #10](https://github.com/vialdjoukang-spec/Medina/pull/10#issuecomment-6041361558). Autorisation GitHub permanente selon CLAUDE.md et AGENTS.md ; utiliser la connexion effective, sans déposer de secrets. Le dépôt entier et les sources de tous les fragments sont accessibles.

## Tes quinze cours

- I48 — Fibrillation et flutter auriculaires
- I30 — Péricardites, épanchement péricardique, tamponnade et constriction
- I33 — Endocardite infectieuse
- I35 — Valvulopathies aortiques
- I34 — Valvulopathies mitrales, tricuspides et pulmonaires
- I00 — Rhumatisme articulaire aigu
- I40 — Myocardites
- I42 — Cardiomyopathies
- I44 — Troubles de la conduction et bradycardies
- I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires
- I49 — Extrasystoles et autres arythmies
- I46 — Arrêt cardiaque
- Q21 — Cardiopathies congénitales de l’adulte
- I71 — Anévrismes et dissections artérielles
- I80 — Thrombose veineuse profonde et thromboses veineuses

Les quinze autres cours existants sont attribués à Codex dans [le suivi](MECHANISMS_PLAN.json). J40 — Bronchite est une production additionnelle. La répartition fixe un responsable ; les corrections de prose antérieures restent recevables même lorsqu’elles portent sur un cours confié à l’autre.

## Ce que doit expliquer chaque passage

Relire intégralement Pathologie, Examens, Sciences, Pharmacologie, fenêtres, tableaux, figures et leurs flèches, quiz, rétroactions, Pareto et glossaires. Pour toute relation causale ou clinique, exposer la chaîne pertinente : déclencheur, cible cellulaire ou organique, effet fonctionnel, signe ou conséquence observée. Pour un bilan, justifier chaque dosage, son interprétation et les limites. Pour un traitement, distinguer mécanisme, bénéfice clinique démontré, indications et risques. Ne pas inventer une causalité lorsqu’on ne dispose que d’une association ; l’indiquer et citer la source.

Exemple : « anémie : facteur aggravant » doit expliquer la baisse du transport d’oxygène, les compensations circulatoires et la réserve limitée du cœur dans ce contexte. « Sodium » doit distinguer concentration et quantité de sodium corporel, mécanismes de dilution ou de pertes, et intérêt du dosage. « Potassium » doit relier gradients transmembranaires, excitabilité/conduction, risque rythmique, fonction rénale et médicaments, sans fixer une conduite à partir d’un chiffre isolé.

Choisir le mot ou groupe de mots natif qui ouvre une fenêtre contextualisée. Une justification doit être claire, précise, professionnelle et agréable à lire. Éviter remplissage, métaphores et annonces sur « cet îlot ». Le texte principal reste fluide ; une fenêtre ne doit pas cacher une réserve nécessaire à la lecture principale.

## Format et remise

Les sources canoniques sont `chapters/<CODE>/`. Une banque `chapters/<CODE>/<CODE>_justifications.json` peut réutiliser le compilateur strict `tools/insert_justifications.py` : version 1 ; course `{code,title}` ; entries avec id `<code-minuscule>-j-<nom>`, title, match `[{file,anchor,text,occurrence?}]`, explanation, mechanism, implication, limits, sources `[{title,url}]`. Les cibles doivent être du texte natif non interactif sous une ancre existante. Une occurrence explicite est obligatoire si le texte est répété ; ne pas choisir silencieusement la première. Tous les champs de prose sont échappés ; les sources HTTPS restent des liens bibliographiques.

Reprendre depuis le `main` publié et lire [la passation](HANDOFF_LATEST.md) ainsi que les reçus avant de retoucher I48. Préserver les originaux et les corrections d’intégration nouvelles. Déposer les sources corrigées sous `livraisons/Livraison Claude/<libellé>/sources/`, rapport et manifeste selon [le protocole](DELIVERY_PROTOCOL.md), puis publier sa branche et sa PR. Une banque nouvelle doit figurer dans le manifeste au même titre que le HTML ; vérifier les empreintes de départ. Les anciens dossiers et rapports sont examinés aussi.

Pour chaque section, fournir les affirmations revues, les justifications ajoutées, les sources vérifiées et les points encore ouverts. Ne marquer un cours relu intégralement qu’après cette revue de tous ses contenus. La compilation et le nombre de fenêtres ne certifient pas l’exhaustivité médicale.

## Navigation et complétude

Toujours nommer une leçon par code CIM + nom complet ; fragments selon `organisation/fragments.json`. Préserver les catégories numérotées des plateformes originales, les chapitres ordonnés et les codes discrets en haut à droite. Un seul J40 — Bronchite couvre J20/J40/J41/J42. Le catalogue historique est CIM-10-GM 2024 ; ne pas déclarer complet en CIM-11 sans inventaire validé de toutes ses catégories et sous-catégories.
