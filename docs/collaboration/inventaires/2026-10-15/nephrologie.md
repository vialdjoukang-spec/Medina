# Inventaire N-07-Néphrologie — 15 octobre 2026

État des sources figé sur `bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373`. Les **79 branches distantes** ont été lues sur leurs SHA respectifs. Le relevé couvre les **33 catégories attribuées à S04**, les dossiers canoniques et toutes les livraisons correspondantes, y compris les anciennes versions et Betta. Les SHA de branches, les empreintes des sources et les variantes sont dans [nephrologie.json](nephrologie.json).

## Cours réellement présents

| Cours | Origine | HTML | Fenêtres | Images | État au relevé |
| --- | --- | ---: | ---: | ---: | --- |
| N04 — Syndrome néphrotique | Cycle 3, Claude | 6 | 53 | 5 | Injecté dans main ; absent de la page publique contrôlée |
| N12 — Néphrite tubulo-interstitielle, non précisée comme aiguë ou chronique | Betta 31, Claude | 6 | 40 | 0 | Injecté dans main ; route publique fonctionnelle |
| N17 — Insuffisance rénale aiguë | Cycle 1, Codex puis corrections Claude | 6 | 81 | 4 | Injecté dans main ; route publique fonctionnelle |
| N18 — Maladie rénale chronique | Cycle 2, Codex puis corrections Claude | 6 | 111 | 8 | Injecté dans main ; route publique fonctionnelle |
| N27 — Petit rein de cause inconnue | Betta 31, Claude | 6 | 35 | 0 | Injecté dans main ; route publique fonctionnelle |
| N29 — Autres affections du rein et de l’uretère au cours de maladies classées ailleurs | Betta 32, Claude | 6 | 61 | 0 | Injecté dans main ; route publique fonctionnelle |

Total : **6 cours, 36 HTML, 6 glossaires, 381 fenêtres et 17 images**. Les 27 autres catégories n'ont aucun cours rédigé repéré dans les branches ; leur liste exacte figure dans le JSON. Les plans de cycles ne sont pas comptés comme cours.

## Branches et versions conservées

Aucune branche ne fournit un septième cours néphrologique ni une leçon supplémentaire à injecter. N04, N12, N27 et N29 n'ont qu'une version de contenu chacun. N17 possède quatre versions historiques et N18 deux. Les sources canoniques actuelles comprennent les corrections Claude ; remplacer leurs fichiers par une livraison plus ancienne les ferait régresser. Aucune substitution, fusion médicale, suppression ni réécriture n'a été réalisée.

La branche documentaire `codex/cim10gm-nephrologie` contient la classification ; elle n'ajoute aucun cours HTML. Les variantes historiques, y compris les copies dans `preuves/` et `provenance/`, restent préservées ; elles ne constituent pas de nouvelles leçons à publier.

## Vérification technique

La construction du fragment S04 et `python3 test_v7.py --static N04 N12 N17 N18 N27 N29` réussissent. Chaque cours possède ses six HTML et son glossaire ; aucune fenêtre, ancre interne ou image locale ne manque, aucun identifiant ni nom de fenêtre n'est dupliqué. Le contrôle navigateur ouvre les six cours en 1300 × 900 et 390 × 844, parcourt les 48 onglets et ouvre une fenêtre disponible par onglet. Aucune fiche absente, erreur JavaScript ou largeur débordante n'est constatée. Les figures différées de N18 sont recontrôlées après défilement réel ; leurs sources sont intactes.

Aucune correction technique de contenu n'est nécessaire dans ce périmètre. Les fichiers livrés par cette mission sont exclusivement cet inventaire et ses résultats de contrôle.

## Publication observée

[Fragment public S04](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S04_renal-voies-urinaires.html) : réponse HTTP 200, copie publique initiale de 2 388 560 octets, en-tête `Last-Modified: Thu, 15 Oct 2026 14:22:05 GMT`. Les routes N12, N17, N18, N27 et N29 affichent leur cours réel. N04 est encore absent de cette copie publique : sa publication relève de l'intégration centralisée. Ce relevé est ponctuel ; un déploiement ultérieur peut le remplacer.

Aucun audit médical nouveau ni validation médicale humaine n'est affirmé. Les réserves et les audits différés des sources existantes restent tels qu'ils sont. Aucun push, fusion ou déploiement n'a été effectué par cette mission.
