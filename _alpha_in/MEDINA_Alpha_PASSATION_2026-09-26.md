# MEDINA_Alpha — passation opérationnelle

**État arrêté le 26 septembre 2026, après le cycle 1.** Ce document sert à reprendre le travail avec une autre IA ou dans un nouvel environnement. Il accompagne le HTML utilisable et l’archive de sources. Avant de modifier quoi que ce soit, vérifier si une version plus récente a été enregistrée dans le dossier Drive ci-dessous : elle prime sur les chiffres de cette photographie.

**Dossier de livraison :** [Medina Alpha, Google Drive](https://drive.google.com/drive/folders/1QipZHuYkfXRNGIAmr5EZjuLqUTYiCgiV). Il est distinct de `Medina_claude` et de `Medina.html` (79 Mo).

## 1. Mission et périmètre

MEDINA_Alpha est l’atlas de médecine destiné à la préparation de l’examen fédéral suisse. La production est organisée **par système de l’organisme**, puis par pathologie. Elle ne suit pas le plan SSP symptôme par symptôme. Les situations cliniques et les symptômes peuvent nourrir les cas d’application, sans devenir l’unité de rédaction.

`MEDINA_0` est le fichier Drive historique d’environ 79 Mo contenant les SSP. Il reste séparé et intact. Son adjonction éventuelle aura lieu à la fin du projet, après vérification des deux architectures et d’une méthode de fusion. Ne pas écraser `Medina.html`, `MEDINA_Claude.html` ni le dossier `Medina_claude` avec MEDINA_Alpha.

**Nouvelle instruction explicite du propriétaire :** après chaque livraison de MEDINA_Alpha, synchroniser dans le dossier **Medina Alpha** le HTML utilisable, les sources restaurables, le paquet transportable et la passation. Mettre à jour les fichiers de ce dossier sans créer une pile de copies ambiguës ; conserver l’identité et l’historique des fichiers lorsque le connecteur le permet. Vérifier les métadonnées et les tailles après l’écriture. Si la synchronisation échoue, l’indiquer clairement.

## 2. Fichiers de reprise

| Nom dans le dossier | Rôle |
|---|---|
| `MEDINA_Alpha_26-09-2026.html` | Produit autonome à ouvrir dans un navigateur moderne ; 22 cours intégrés au cycle 1. |
| `MEDINA_Alpha_SOURCES.json.gz` | Dictionnaire compressé des fichiers éditables ; ne pas le confondre avec le HTML de lecture. |
| `MEDINA_Alpha_TRANSPORT_26-09-2026.zip` | HTML, sources compressées, PDF du cycle, notice, restaurateur et manifeste SHA-256. Taille au cycle 1 : environ 5,2 Mo, donc inférieure à 30 Mo. |
| `MEDINA_Alpha_05_Cycle_1_26-09-2026.pdf` | État formel de la vague 1 après le premier cycle à deux systèmes. |
| `MEDINA_Alpha_PASSATION_2026-09-26.md` | Présent guide. Une copie figure aussi dans les sources compressées. |

**Règle de priorité :** l’état actuel se lit d’abord dans `chapters.json`, `shell/data.py` et les audits de la dernière archive de sources. Les anciens tableaux narratifs de `PROMPT_MEDINA.md`, `IDENTITE_MEDINA_Alpha.md` et du prompt dans `Medina_claude` peuvent décrire une étape antérieure. Les instructions de fond de `PROMPT_MEDINA.md` et `CHAPTER_SPEC.md` restent applicables, sous réserve des décisions expresses et plus récentes du propriétaire.

## 3. État réellement vérifié

La vague 1 comporte **six systèmes** et **574 catégories** dans le référentiel de suivi. **69/574 catégories (12,0 %) disposent d’un cours intégré** ; cette mesure est une couverture rédactionnelle, pas un pourcentage de validation clinique.

| Ordre de production | Système | Catégories avec cours / total | État |
|---|---|---:|---|
| 1 | Cœur et hémodynamique | 56/56 | Couverture éditoriale historique ; 17 cours inscrits dans `DONE_COURSES`. |
| 2 | Poumon, plèvre et ventilation | 12/64 | J45, J44, J18 et I26 intégrés ; révisions et contrôles ouverts. |
| 3 | Microorganismes et infections | 1/155 | A41 intégré ; le reste du système est à produire. |
| 4 | Tube digestif, foie et pancréas | 0/102 | À produire. |
| 5 | Système nerveux | 0/120 | À produire. |
| 6 | Métabolisme et endocrines | 0/77 | À produire. |

Le **cycle 1** a produit en parallèle I26 (embolie pulmonaire) et A41 (sepsis de l’adulte), avec quatre onglets chacun, respectivement 37 et 30 fenêtres, quatre quiz chacun, ainsi que des contre-audits ciblés. Ils sont présents dans le même HTML. Ni ces deux chapitres ni leurs systèmes ne sont déclarés à 100 % : les contrôles visuels en navigateur et la revue clinique exhaustive demeurent ouverts. `DONE_SYS={1}` ; l’insigne « 100 % rédigé » des chapitres relève uniquement de `DONE_COURSES`, à modifier après les portes d’audit.

**Prochaine paire de la vague 1 :** digestif + système nerveux. Commencer par le chapitre le plus fréquent et grave dans chaque système (hémorragie digestive et AVC/AIT dans le plan actuel), après vérification des codes CIM-10-GM et de `chapters.json`. Terminer le cycle en signalant les deux chapitres réellement intégrés, sans annoncer deux systèmes achevés. La rotation suivante doit continuer à couvrir les six systèmes selon la priorité de l’examen. Les fréquences sont une estimation de rendement pédagogique : le blueprint officiel ne fournit pas une pondération publique par système.

## 4. Restaurer, construire et contrôler

1. Extraire le ZIP dans un dossier vide. Vérifier les empreintes mentionnées dans `SHA256.txt`.
2. Exécuter `python3 RESTAURER_MEDINA_Alpha.py MEDINA_Alpha_SOURCES.json.gz DOSSIER_VIDE` ; ce programme refuse d’écraser un dossier non vide et vérifie les chemins.
3. Se placer dans le dossier restauré. Lancer `python3 build_front.py` pour obtenir `dist/MEDINA.html`, puis `python3 chantier.py` pour l’état des lieux et `python3 pack_v7.py` pour le dictionnaire source.
4. Pour chaque chapitre, vérifier `build_medina.transform`, les clés `data-k`/`data-pop`, les ancres, les ratios Pareto et `build_medina.audit` (aucune abréviation candidate non couverte). Contrôler la syntaxe JavaScript, le nombre de panneaux et la reconstruction globale.
5. Si Playwright **et Chromium** sont disponibles, exécuter `python3 test_v7.py <CODE>` et inspecter PC, mobile, onglets, mode livre, Navigo, Police Taille, fenêtres, quiz et absence d’erreurs JavaScript. Au cycle 1, l’environnement ne disposait pas d’un navigateur local utilisable : aucun succès de test visuel ne doit être inventé.
6. Après intégration, comparer les nombres de catégories effectivement couvertes aux `covers` déclarés. Déclarer `integrated: true` seulement après assemblage ; ajouter à `DONE_COURSES` et `DONE_SYS` uniquement lorsque leurs contrôles propres sont satisfaits.

`build_front.py` est la voie officielle. `shell/medina_front.html` est la coque conservée ; `build_v7.py` et `shell/shell.html` sont un ancien chemin de construction refusé. Les fichiers `chapters/<CODE>/` et `glossary/<code>.py` sont les unités de rédaction ; `chapters/I50/` est un exemple **de forme**, sans clonage du texte. `PROMPT_MEDINA.md` précise le périmètre complet, et `CHAPTER_SPEC.md` décrit les classes et la structure HTML. Leurs chemins `/home/claude/...` sont des exemples historiques : utiliser les chemins du dossier effectivement restauré.

## 5. Contrat éditorial et clinique

- Quatre onglets : **Pathologie et prise en charge**, **Examens complémentaires**, **Sciences fondamentales spécialisées**, **Pharmacologie de la pathologie**. Rédiger le système en profondeur, avec cas et QCM corrigés, et non comme une liste de slogans.
- Dans la pathologie : définition et classification, épidémiologie datée, mécanismes expliqués, étiologies, anamnèse, signes fonctionnels et physiques distincts, démarche diagnostique, gravité, traitement justifié, surveillance et situations particulières. Présenter les longues énumérations de signes en deux colonnes lorsque cela clarifie la lecture. Chaque antécédent ou notion annoncée comme interactive doit ouvrir une fiche réelle.
- Dans les examens : question clinique, indication, performance et interprétation, seuils sourcés, limites, diagnostics différentiels, exemples. Dans la pharmacologie : mécanisme, choix selon le phénotype, posologies et ajustements vérifiés sur les informations professionnelles suisses, interactions, contre-indications et surveillance.
- Prioriser les sources primaires suisses, puis européennes et internationales. Vérifier les recommandations à la date de rédaction ; attribuer explicitement leur année et leur société. Ne jamais inventer de seuil, d’effectif, de posologie ou de grade. La guideline ESC/ERS de l’embolie pulmonaire reste celle de 2019 dans l’audit I26 ; l’AHA/ACC a publié une autre recommandation en 2026. La *Surviving Sepsis Campaign* adultes a publié une mise à jour en mars 2026. Ne pas confondre ces référentiels.
- Ajouter un glossaire littéral, des fenêtres vertes réellement reliées, des figures utiles et des synthèses Pareto fidèles. Le titre des parties est souligné d’une **seule couleur ocre** ; les numéros sont **rouges et soulignés** ; prose justifiée et famille de police cohérente, aussi sur mobile.
- « Navigo » est fixé à droite et reconstruit le plan des parties/sous-parties de l’onglet actif ; il permet une recherche et les sauts en lecture verticale ou en mode livre. « Police Taille » règle de 14 à 24 px et mémorise le choix par cours. Préserver ces fonctions lors de chaque reconstruction.

**Audit minimal avant « 100 % » :** exactitude et actualité des données, profondeur, compréhension, fenêtres, sciences, examens, pharmacologie, cas et quiz, navigation, lisibilité mobile, contre-audit indépendant et essai navigateur. Un contrôle de syntaxe ou de quelques doses ne vaut pas validation clinique intégrale. Les réserves particulières sont dans `audits/J18.md`, `audits/J44.md`, `audits/I26.md`, `audits/A41.md` et `audits/NAVIGO_2026-09-26.md`.

## 6. Production à deux systèmes et synchronisation

Un cycle traite **deux systèmes distincts en parallèle** ; les rédacteurs ou agents travaillent dans des dossiers de chapitres séparés. Un seul intégrateur met à jour `chapters.json`, la coque, le registre, le HTML et les fichiers livrés. Chaque agent peut demander une contre-lecture indépendante, en indiquant précisément son périmètre. Aucun agent ne modifie simultanément le maître commun.

Après chaque cycle, annoncer « vague N, cycle M, systèmes X + Y » avec les chapitres ajoutés, les contrôles passés, les réserves et la progression recalculée. L’utilisateur peut demander de commencer immédiatement le cycle suivant. Sinon, la tâche existante suit une **cadence horaire** ; l’attente d’une minute après l’annonce sert à recevoir une éventuelle instruction, elle ne constitue pas une garantie de déclenchement automatique à 60 secondes.

À **chaque livraison** : (1) rechercher la version la plus récente dans la bibliothèque de travail et le dossier Drive ; (2) reconstruire le HTML, empaqueter les sources et vérifier le manifeste et une restauration à blanc ; (3) déposer ou remplacer dans **Medina Alpha** le HTML, les sources compressées, le ZIP, le PDF de progression actualisé et cette passation ; (4) lire les métadonnées du dossier pour confirmer noms, tailles et liens ; (5) informer l’utilisateur du résultat exact. Ne jamais présenter une version locale plus ancienne comme « la plus récente » lorsqu’un autre cycle vient de publier.

Si la compression dépasse un jour **30 Mo**, fractionner l’archive binaire avec ordre, empreintes et script de réassemblage. On peut reconstruire bit pour bit le HTML à partir de ses fragments ; deux moitiés HTML ne sont pas présumées fonctionnelles séparément. Ne jamais tronquer un cours pour réduire la taille.

## 7. Point de vigilance sur les autres branches

Le dossier `Medina_claude` comporte `MEDINA_Claude.html` et `MEDINA_Prompt_passation.md`, relatifs à une branche différente et à une répartition de travail historique. Le prompt y évoque notamment D84, M06 et M32 qui ne figurent **pas** dans `chapters.json` de la présente édition Alpha. Ne pas ajouter ces cours à la progression Alpha sans récupérer leurs sources, contrôler leur version, résoudre les conflits et les intégrer réellement. Le fichier `Medina.html` de 79 Mo reste MEDINA_0.

**Fin de passation.** Reprendre par les fichiers vérifiés du dossier [Medina Alpha](https://drive.google.com/drive/folders/1QipZHuYkfXRNGIAmr5EZjuLqUTYiCgiV), puis par `PROMPT_MEDINA.md`, `CHAPTER_SPEC.md` et les audits dans l’archive source.
