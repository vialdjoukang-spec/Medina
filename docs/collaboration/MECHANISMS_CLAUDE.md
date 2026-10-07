# Mission Claude — justifier chaque affirmation

Le lot 5 final `2947ba8` est reçu et injecté dans le contenu `1fe38461d8502fb7984d66b0fe223afecd759889`, avec les corrections ciblées de main préservées et les remises rafraîchies. Ne pas repartir des anciennes copies. Les travaux nouveaux suivent le cahier des charges du 8 octobre : un seul chapitre actif à la fois, sous-agents spécialisés dans ce chapitre et audit croisé avant injection. I83 — Varices des membres inférieurs (C-01-Cardiologie) précède I89 ; la relecture exhaustive des cours déjà enrichis demeure ouverte. Aucun quota de mots ni multiplicateur de volume.


## Tes dix cours actifs — C-01-Cardiologie

- I48 — Fibrillation et flutter auriculaires
- I30 — Péricardites, épanchement péricardique, tamponnade et constriction
- I33 — Endocardite infectieuse
- I35 — Valvulopathies aortiques
- I34 — Valvulopathies mitrales, tricuspides et pulmonaires
- I40 — Myocardites
- I42 — Cardiomyopathies
- I44 — Troubles de la conduction et bradycardies
- I00 — Rhumatisme articulaire aigu
- Q21 — Cardiopathies congénitales de l’adulte

La [priorité actuelle](FRAGMENT_01_PRIORITE.md) remplace le partage historique 15/15. Codex prend les dix autres cours présents du Fragment 01, notamment I47, I49, I46, I71 et I80 qui lui sont transférés. I00 reste à Claude car sa production est déjà en cours. I48 et les dix cours supplémentaires reçus à `67c01cb4` sont injectés et contrôlés techniquement. Q21 est reçu dans le lot 5 final à `2947ba86`. Poursuivre I83 et I89, ainsi que la fermeture documentée des réserves des cours attribués. I46 et I49, rédigés avant la nouvelle répartition, sont reçus aussi et gardés ; Codex poursuit leur revue. Les productions prioritaires I83 — Varices des membres inférieurs et I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques sont aussi confiées à Claude ; Codex prend I73 et I95. Le périmètre des autres entrées et la CIM-11 restent à établir. Achever le Fragment 01 avant de passer au Fragment 02.

Les fenêtres répondent directement à la question locale avant de développer mécanisme, conséquence clinique, limites et sources. Aucun objectif de longueur ni multiplication de volume n’est imposé. Le lot I48 est intégré et contrôlé ; son volume n’est pas un gabarit obligatoire pour les autres cours. Conserver les notions utiles, supprimer les répétitions. Comparer les nouveautés ESC 2026 entre parenthèses ou dans une fenêtre dédiée. Anthropic Serif est une préférence à appliquer lorsqu’un fichier de police utilisable est disponible ; elle est absente de cette session.

## Ce que doit expliquer chaque passage

Relire intégralement Pathologie, Examens, Sciences, Pharmacologie, fenêtres, tableaux, figures et leurs flèches, quiz, rétroactions, Pareto et glossaires. Pour toute relation causale ou clinique, exposer la chaîne pertinente : déclencheur, cible cellulaire ou organique, effet fonctionnel, signe ou conséquence observée. Pour un bilan, justifier chaque dosage, son interprétation et les limites. Pour un traitement, distinguer mécanisme, bénéfice clinique démontré, indications et risques. Ne pas inventer une causalité lorsqu’on ne dispose que d’une association ; l’indiquer et citer la source.

Exemple : « anémie : facteur aggravant » doit expliquer la baisse du transport d’oxygène, les compensations circulatoires et la réserve limitée du cœur dans ce contexte. « Sodium » doit distinguer concentration et quantité de sodium corporel, mécanismes de dilution ou de pertes, et intérêt du dosage. « Potassium » doit relier gradients transmembranaires, excitabilité/conduction, risque rythmique, fonction rénale et médicaments, sans fixer une conduite à partir d’un chiffre isolé.

Choisir le mot ou groupe de mots natif qui ouvre une fenêtre contextualisée. Une justification doit être claire, précise, professionnelle et agréable à lire. Éviter remplissage, métaphores et annonces sur « cet îlot ». Le texte principal reste fluide ; une fenêtre ne doit pas cacher une réserve nécessaire à la lecture principale.

## Format et remise

Les sources canoniques sont `chapters/<CODE>/`. Une banque `chapters/<CODE>/<CODE>_justifications.json` peut réutiliser le compilateur strict `tools/insert_justifications.py` : version 1 ; course `{code,title}` ; entries avec id `<code-minuscule>-j-<nom>`, title, match `[{file,anchor,text,occurrence?}]`, explanation, mechanism, implication, limits, sources `[{title,url}]`. Les cibles doivent être du texte natif non interactif sous une ancre existante. Une occurrence explicite est obligatoire si le texte est répété ; ne pas choisir silencieusement la première. Tous les champs de prose sont échappés ; les sources HTTPS restent des liens bibliographiques.

Reprendre depuis la branche d’intégration `codex/sciences-cs-fragments-20261007` et lire [la passation](HANDOFF_LATEST.md) ainsi que les reçus avant de retoucher I48. Préserver les originaux et les corrections d’intégration nouvelles. Déposer les sources corrigées sous `livraisons/Livraison Claude/<libellé>/sources/`, rapport et manifeste selon [le protocole](DELIVERY_PROTOCOL.md), puis publier sa branche et sa PR. Une banque nouvelle doit figurer dans le manifeste au même titre que le HTML ; vérifier les empreintes de départ. Les anciens dossiers et rapports sont examinés aussi.

Pour chaque section, fournir les affirmations revues, les justifications ajoutées, les sources vérifiées et les points encore ouverts. Ne marquer un cours relu intégralement qu’après cette revue de tous ses contenus. La compilation et le nombre de fenêtres ne certifient pas l’exhaustivité médicale.

## Navigation et complétude

Toujours nommer une leçon par code CIM + nom complet ; fragments selon `organisation/fragments.json`. Préserver les catégories numérotées des plateformes originales, les chapitres ordonnés et les codes discrets en haut à droite. Un seul J40 — Bronchite couvre J20/J40/J41/J42. Le catalogue historique est CIM-10-GM 2024 ; ne pas déclarer complet en CIM-11 sans inventaire validé de toutes ses catégories et sous-catégories.
