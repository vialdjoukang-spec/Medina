# A69 — QA structurelle et visuelle du preview I-03

Contrôle du 8 octobre 2026, après complément des Sciences. Cible : sources A69 assemblées dans `/workspace/work/medina-resume/livraisons/Livraison Codex/I-03-Infectiologie/travail/PRODUCTION_FRAGMENT_2026-10-08/sources/chapters/A69/` et aperçu de travail généré par `tools/build_fragment_work_preview.py`. Cette QA ne porte pas sur la justesse médicale.

## Structure et intégration

- Fragments `a+b+c+d` équilibrés : quatre panneaux `pA`, `pE`, `pS`, `pP` ; plan monographique de 14 îlots en pathologie, 5 en examens, 6 en sciences et 5 en pharmacologie.
- Les 24 ancres de navigation ont une cible unique. Les six sous-onglets scientifiques ont chacun un `data-s` relié au panneau correspondant.
- 39 appels `data-k`, 35 fenêtres `data-pop` ; tous les appels sont résolus et aucune clé A69 n’est dupliquée. Classes HTML conformes au contrat ; aucune marque de placeholder `⟦…⟧`.
- Cinq quiz, dont trois dans les examens. Le manifeste inclut les sept HTML requis et `glossary/a69.py` avec leurs empreintes vérifiées par le constructeur.
- Construction du preview réussie : `/workspace/work/a69-preview-scroll-qa/infectiologie-A69.html`, huit cours I-03 et 552 fenêtres dans le pack. Le preview porte le statut de travail et ne déclare ni validation externe ni injection canonique.

## Essai navigateur

Chromium headless, route directe `#/entry/A69`, largeurs **390, 768 et 1440 px** (hauteur 900 px). Les quatre onglets, les six sous-onglets scientifiques, l’ouverture et la fermeture d’une fenêtre et le retour d’un quiz fonctionnent aux trois largeurs. Aucune erreur JavaScript ni débordement horizontal du document ou d’un panneau visible. Captures et mesures : `/workspace/work/a69-qa-captures-scrollfix/`.

### Fil d’Ariane et correction du builder

Avant correction, le cours direct s’ouvrait avec un défilement initial de 50 à 188 px selon la largeur et le moment de la mesure. L’en-tête sticky recouvrait alors les liens « Infectiologie » et « Autres maladies à spirochètes » : `elementFromPoint` confirmait que le clic atteignait l’en-tête. Capture avant : `/workspace/work/a69-qa-before-768.png`.

Le seul fichier du dépôt modifié par cette QA est `tools/build_fragment_work_preview.py`. Il ajoute un script au **preview** qui attend le montage du nouveau cours `#/entry/CODE`, puis remet le défilement à zéro. Le script ne se déclenche pas lorsqu’on change seulement d’onglet ou d’îlot dans le même cours ; il se réarme après une sortie vers l’accueil. L’override qui rendait l’en-tête non sticky uniquement sur tablette a été supprimé car ce défaut existe aux trois largeurs et que la correction de route le résout en conservant l’en-tête sticky.

Après correction, le défilement initial est à 0 px et les deux liens du fil d’Ariane sont réellement cliquables à **390, 768 et 1440 px**. Un clic sur un îlot des examens conserve le défilement voulu (4563, 3963 et 2784 px respectivement dans l’essai), sans retour intempestif en haut. Un aller accueil → A69 revient bien à 0 px. Capture après à 768 px : `/workspace/work/a69-qa-after-scrollfix-768.png` ; captures après à 390 et 1440 px dans le même dossier `/workspace/work/`.

Vérifications de changement : compilation Python sans erreur, `git diff --check` sans défaut, reconstruction du preview réussie. Le diff de `tools/build_fragment_work_preview.py` ajoute 26 lignes pour le comportement de route et retire l’override CSS tablette. Aucun contenu clinique ni source de chapitre n’a été modifié par cette QA.
