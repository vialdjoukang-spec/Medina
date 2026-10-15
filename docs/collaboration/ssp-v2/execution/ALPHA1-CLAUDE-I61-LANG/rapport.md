# Audit linguistique agressif — I61 Hémorragie intracérébrale

**Mission** ALPHA1-CLAUDE-I61-LANG · **branche** `claude/alpha1/i61-lang-g1` · **génération** 1 · **base** `f664dd9e8d`

> Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## 1. Ce qui a été fait

Les sept fichiers de la leçon ont été lus en entier : les six fichiers HTML (texte, tableaux, légendes, quiz, fenêtres, encadrés de synthèse « Loi de Pareto », critères formels, paramètres clés) et le glossaire `glossary/i61.py`. Les empreintes SHA-256 des sept fichiers ont d'abord été recalculées : **7 conformes sur 7** au manifeste. Aucun fichier de la leçon n'a été modifié ; les corrections sont proposées dans `propositions.json`.

Chaque proposition est locale : un extrait exact (`ancien`), unique dans son fichier, remplacé par un `nouveau`, avec son motif. Aucun fait, chiffre, dose ou source n'est ajouté, retiré ou modifié. Quand une reformulation risquait de changer un sens médical, elle n'est pas proposée : l'élément est marqué `renvoi_medical` avec l'explication.

## 2. Tableau de bord

| Fichier | Propositions | Renvois médicaux |
|---|---:|---:|
| I61_a (Pathologie, sections 1 à 6) | 45 | 5 |
| I61_b (Pathologie, sections 7 à 12) | 56 | 2 |
| I61_c (Examens et Sciences fondamentales) | 22 | 3 |
| I61_d (Pharmacologie) | 12 | 0 |
| I61_pop1 (fenêtres, 1re partie) | 25 | 5 |
| I61_pop2 (fenêtres, 2e partie) | 26 | 3 |
| glossary/i61.py | 2 | 0 |
| **Total** | **188** | **18** |

Catégories des propositions : phrase_nominale (40), ambiguïté (27), précision_lexicale (23), grammaire (22), syntaxe (15), répétition (14), lourdeur (7), anglicisme (7), registre (6), terminologie (6), style_annonce (5), ponctuation (4), ponctuation_registre (3), typographie (2), cohérence (2), métaphore (2), intitulé (1), unités (1), orthographe (1).

Contrôles mécaniques : chacune des 206 entrées a son extrait présent **exactement une fois** dans le fichier ; aucun chevauchement entre propositions ; l'application simulée (hors dépôt) conserve toutes les balises HTML et le glossaire compile ; les nombres sont identiques avant et après pour toutes les propositions (une proposition ajoute seulement le mot « intervalle de confiance »). `build_medina.audit()` renvoie `{}` sur les six fichiers (aucune abréviation sans clé de glossaire).

## 3. Constats les plus importants

1. **Délais lus comme des heures d'horloge** (LANG-072, LANG-104, LANG-125, LANG-161, LANG-178, LANG-196) : « début avant 6 h » et « dernière prise avant 15 h » se lisent comme des heures du jour, alors que les passages internes (encadré Paramètres clés ; fenêtre Ondexxya : « moins de 6 heures après les symptômes et moins de 15 heures après la dernière prise ») en font des délais. La formule proposée est « depuis moins de 6 heures », « remontant à moins de 15 heures », dans le tableau de réversion, l'encadré de synthèse, le quiz, la fenêtre de dose d'andexanet et la fenêtre Praxbind. Ces critères conditionnent un antidote : l'ambiguïté mérite la priorité.
2. **Phrases nominales et infinitifs injonctifs** (40 propositions, dont les encadrés « À retenir » et leurs copies « Loi de Pareto ») : le guide de rédaction les proscrit partout, y compris dans les encadrés et les fenêtres. Exemples : « aucun traitement clinique validé » (LANG-041, LANG-190), « Ne jamais donner l'andexanet… » (LANG-144, LANG-203), les fragments « Ce que l'on compare » des fenêtres de calcul (LANG-152, LANG-155, LANG-158, LANG-160, LANG-162, LANG-166).
3. **Fautes de langue effectives** : « dégénérer la paroi » au lieu de « dégrader » (LANG-030) ; « complexe prothrombique » au lieu de « prothrombinique » (LANG-180) ; « le groupe » qui serait « dosé » (LANG-097) ; « la phenprocoumone reprend » (LANG-087) ; « une ellipsoïde » (LANG-156) ; « à la tête du patient » pour « au chevet » (LANG-154) ; « baisse en médiane » (LANG-074, LANG-174) ; « sans lever » (LANG-185).
4. **Liens logiques abusifs ou ambigus** : « d'où l'aspect de lumière dans la lumière » (LANG-031) ; « Cette évolution » (LANG-025) ; « Il dépasse le seuil » (LANG-079) ; « parmi elles » (LANG-043) ; « qui sont l'examen décisif » (LANG-173).
5. **Annonces qui décrivent le cours ou l'interface** (5 propositions) : « Le lecteur doit savoir… », « Les antécédents à rechercher sont cliquables », « l'îlot des diagnostics différentiels ».
6. **Typographie : aucune espace insécable** dans les six fichiers HTML (règle globale GLOB-01, section 5).

## 4. Renvois médicaux (aucune reformulation proposée)

| Id | Fichier | Point à décider |
|---|---|---|
| LANG-019 | I61_a.html | Accord ambigu : « acquis » (masculin) suit « fistule artério-veineuse » (féminin). Selon le libellé OFS, I67.1 désigne l’anévrisme cérébral sans rupture ; la formule « anévrisme ou fistule … acquis » doit être comparée au texte de la CIM-10-GM avant correction. Formulation non modifiée pour ne pas altérer le sens de codage. |
| LANG-023 | I61_a.html | Dénominateur ambigu : la phrase donne 39,1 % des 2250 patients évalués puis 33,2 % de la cohorte entière, et « 25,1 % étaient décédés » sans préciser la base. La fenêtre « Registre suisse des AVC » écrit « 25,1 % de la cohorte décédés ». Choix de la formulation laissé à l’audit médical. |
| LANG-037 | I61_a.html | Incohérence interne : la légende affirme que chaque étape ouvre une possibilité thérapeutique, alors que le paragraphe de lecture et l’encadré final indiquent que la lésion secondaire (dernière étape) n’a pas de traitement validé. Reformulation médicale à décider. |
| LANG-042 | I61_a.html | Comparatif sans second terme : « plus souvent » que quoi (que les hémorragies lobaires ? « le plus souvent » ?). Le choix change la portée de l’affirmation ; à trancher à l’audit médical. |
| LANG-047 | I61_a.html | Tension entre le texte (« les causes ne s’excluent pas ») et le tableau dont les six fréquences totalisent 100 % (46,7 + 21,4 + 10,3 + 8,6 + 8,2 + 4,8). Une répartition exclusive et une attribution non exclusive ne se concilient pas ; clarification médicale requise. De plus, « Dans le registre, l’atteinte mixte … représente 63,6 % » ne précise pas si ces pourcentages (CADMUS) viennent du registre suisse ou de la cohorte CADMUS. |
| LANG-059 | I61_b.html | Incohérence : la parenthèse suit « déclin cognitif ou hémorragie cérébrale antérieure » et vise « l’un de ces éléments », alors que la section 11.1 et la fenêtre sur les critères de Boston citent trois éléments (déclin cognitif, hémorragie cérébrale, épisodes focaux transitoires). Ajout éventuel des épisodes focaux transitoires à décider par l’audit médical. |
| LANG-092 | I61_b.html | Dans le paragraphe sur l’enfant, l’argument « les malformations vasculaires sont la première cause chez le jeune adulte » ne concerne pas l’enfant : non-séquitur à lever par l’audit médical (soit retirer, soit remplacer par une donnée pédiatrique sourcée). |
| LANG-111 | I61_c.html | Terminologie à vérifier : « niveau liquide-sang » n’est pas la désignation usuelle (on parle de niveau liquide-liquide ou de niveau sédimentation/sérum dans un hématome). Aucun remplacement proposé sans contrôle de la source. |
| LANG-115 | I61_c.html | Omission : 22,1 % correspond à l’absence simultanée de microangiopathie et d’hypertension (arbre DIAGRAM du même onglet ; 7,3 % si microangiopathie absente mais hypertension présente). Proposition : « … sans hypertension ni microangiopathie : … ». Même omission dans l’encadré de synthèse Pareto « Imagerie ». |
| LANG-119 | I61_c.html | Incohérence de datation des intervalles de référence du CHUV : « état au 16 octobre 2024 » dans le tableau, « version du 9 juin 2026 » dans les sources de la même partie et de la fenêtre INTERACT3. Vérification de la source requise. |
| LANG-159 | I61_pop1.html | Lien causal non convaincant : le « car » justifie l’ajout de vitamine K par deux délais (30 minutes ; 4 à 6 heures), sans mentionner le caractère transitoire de la correction par le concentré, qui est la vraie raison. Reformulation médicale à décider. |
| LANG-165 | I61_pop1.html | Incohérence interne : les spécificités chiffrées dans la phrase précédente sont identiques pour les deux versions (95,0 % contre 95,0 %), alors que la phrase conclut à une spécificité moindre. À clarifier (source = jugement de Berne vs chiffres de l’article). |
| LANG-167 | I61_pop1.html | Avertissement important sur la fiabilité des pourcentages de l’arbre DIAGRAM ; il contraste avec la légende de la figure de l’onglet Examens (« Les pourcentages de l’arbre sont donnés sans arrondi ») qui ne mentionne pas cette limite. À harmoniser par l’audit médical. |
| LANG-168 | I61_pop1.html | Même accord ambigu que dans l’onglet Pathologie (« acquis » masculin après « fistule » féminin) ; libellé OFS à vérifier. |
| LANG-171 | I61_pop1.html | Libellé ambigu, calque de l’allemand : interdiction, déconseil ou délai non défini ? La force de la recommandation est à préciser à partir du protocole bernois. |
| LANG-179 | I61_pop2.html | Incohérence de seuil : ici « mRS préalable inférieur à 3 », alors que le tableau de réversion de l’onglet Pathologie exclut les patients avec « mRS supérieur à 3 » (soit un mRS de 3 autorisé). Le seuil réel doit être vérifié dans le protocole bernois. |
| LANG-182 | I61_pop2.html | Rubrique « Effets indésirables » vide (« Voir la fiche. ») dans cinq fenêtres (Konakion MM, Trandate, Cleviprex, acide tranexamique, Keppra) : renvoi sans contenu, contraire au principe « le lecteur comprend, il ne devine pas » ; contenu à rédiger à partir de l’information professionnelle (non réalisé dans cette mission linguistique). |
| LANG-200 | I61_pop2.html | Même omission que dans l’onglet Examens : 22,1 % suppose l’absence d’hypertension et de microangiopathie. |

## 5. Règles globales (non appliquées, car non locales)

- **GLOB-01 — Espaces insécables absentes** (haute). Aucune espace insécable (U+00A0 ou U+202F) dans les six fichiers de leçon. Les espaces avant « ; : ? ! », à l'intérieur de « » , entre un nombre et son unité (5 mg, 38 °C, 30 %) et dans les groupes de milliers (100 000, 11 349) sont des espaces ordinaires : les coupures de ligne peuvent séparer le signe de son mot ou le nombre de son unité. *Traitement :* Opération mécanique globale, non appliquée ici (volume ≈ 1 500 occurrences, non « locale »). Les champs « nouveau » de propositions.json conservent volontairement les espaces ordinaires pour rester comparables à l'ancien. Recette proposée à l'intégrateur : appliquer sur le texte hors balises, attributs, identifiants et URL : (1) ' ;', ' :', ' ?', ' !' → U+202F + signe ; (2) '« ' et ' »' → U+00AB/U+00BB avec U+00A0 intérieure ; (3) '(\d) (mg|µg|g|kg|ml|µl|cm|mm|mmHg|mmol|UI|%|°C|h|min)' → U+00A0 ; (4) groupes de milliers '(\d) (\d{3})' → U+202F ; exclure les identifiants et les attributs. Contrôler ensuite que build_medina.audit() renvoie toujours {}.
- **GLOB-02 — Nombres en lettres et en chiffres** (moyenne). « trois mois » (8 occurrences) et « 3 mois » (20) ; « trois premières heures » (4) et « 3 premières heures » (2). Règle conseillée : chiffres devant une unité de temps (3 mois, 3 premières heures), avec « trois » réservé aux emplois non mesurés. *Traitement :* Non appliqué : 14 occurrences sont dispersées dans des phrases déjà proposées à la correction ; harmonisation à faire dans l'étape d'intégration.
- **GLOB-03 — Synonymes concurrents** (moyenne). « antiagrégant » (3) / « antiplaquettaire » (5) ; « Stroke Unit » (5) / « unité AVC » (1) ; « Stroke Center » (1) / « centre AVC » (1) ; « aPTT » (6, sigle anglais) alors que le glossaire le développe en « Temps de céphaline activée » (TCA, 0 occurrence) ; « c-statistique » (2) / « surface sous la courbe » (2). *Traitement :* Un terme par notion à choisir ; propositions ponctuelles LANG pour c-statistique et Stroke Units ; reste à trancher pour antiagrégant/antiplaquettaire et aPTT/TCA.
- **GLOB-04 — Intervalles de confiance non étiquetés** (moyenne). Huit intervalles sont écrits « (rapport de cotes x ; a à b) » ou « (x ; a à b) » sans la mention « intervalle de confiance » (onglet Pathologie, 6 ; fenêtres Tranexamic, 2). Le niveau (95 %) n'est jamais précisé dans ces passages. *Traitement :* Une seule proposition (LANG sur 9.3) pour ne pas ajouter de fait ; convention à généraliser et niveau de confiance à vérifier aux sources (renvoi médical implicite).
- **GLOB-05 — Phrases nominales dans les fenêtres de monographie** (haute). Les fenêtres « monographie suisse » (Ondexxya, Praxbind, Prothromplex, Beriplex, Konakion, Ebrantil, Trandate, Cleviprex, Catapresan, acide tranexamique, Clexane, Keppra) s'écrivent presque entièrement en rubriques nominales (« Protéinurie transitoire fréquente », « Surveillance. Hémostase, reprise du saignement… », « Posologie. 5 g… »). Le guide de rédaction (§ 2) proscrit la phrase nominale partout, fenêtres comprises. *Traitement :* Seuls les cas les plus lourds sont proposés (une douzaine de propositions) ; une réécriture complète des rubriques des douze monographies dépasse une correction « locale » et relève d'une mission de rédaction.
- **GLOB-06 — Titres de références traduits** (moyenne). La plupart des références sont données avec un titre français pour des articles publiés en anglais (par exemple « Étude genevoise de l'AVC : incidence et létalité selon la CIM-11 (Neurology 2025;104:e213353) ») alors que d'autres gardent le titre anglais (« Acute intracerebral haemorrhage: diagnosis and management »). Un titre traduit sans mention « [trad.] » peut passer pour le titre officiel ; trois références n'ont pas d'auteur (« Hémorragie intracérébrale sous anticoagulants oraux, registres suisse et norvégien »). *Traitement :* Renvoi à l'audit des sources ; non modifié.
- **GLOB-07 — Glossaire i61.py** (basse). Clé « DPA » définie mais jamais employée dans les six fichiers ; cinq définitions identiques « Nom propre, non une abréviation. » (LEO, CSL, CPS, UCB-Pharma, AstraZeneca), elliptiques ; définition de « APOE » parlant de « gène » alors que la forme développée est « Apolipoprotéine E » (protéine). build_medina.audit() exécuté en lecture seule sur les six fichiers : {} (aucune abréviation non couverte). *Traitement :* Observations ; deux propositions LANG sur les définitions GCS et HIC.
- **GLOB-08 — Observations de structure (non modifiées)** (moyenne). (1) La sous-section 2.3 « Règles de codage » et la fenêtre « Sous-codes CIM-10-GM » traitent le code CIM, ce que l'instruction de style de la section 11 déconseille (« sans îlot ni tableau consacré au code CIM »). (2) Le tableau de 3.4 (onglet Pathologie) et celui de 2.3 (onglet Examens) ne sont précédés d'aucun paragraphe d'introduction (guide § 4). (3) En 8.1, le mot cliquable « transformation et critères du scanner » est placé après « effet de masse et l'hypertension intracrânienne », loin de la notion qu'il ouvre. (4) Le titre « 1.3 Prérequis cliquables » décrit l'interface. (5) Le tableau 1.1 de l'onglet Examens annonce trois statuts (indiqué, conditionnel, non systématique) alors qu'il contient aussi « Indiqué à Berne chez tous » et « Piège ». *Traitement :* Hors du périmètre d'une correction de formulation locale ; transmis pour décision.

## 6. Lacunes de l'audit

- Aucune vérification médicale ni de source n'a été faite (périmètre linguistique). Les 18 renvois médicaux ne sont pas résolus ; aucune des affirmations chiffrées n'a été confrontée à une source.
- Les propositions n'ont pas été appliquées aux fichiers ; aucune compilation (build_front.py), aucun test navigateur (test_v7.py) et aucun rendu visuel n'ont été réalisés. Le moteur (shell/polish.js) n'a pas été examiné pour savoir s'il insère des espaces insécables au rendu.
- Le texte des figures SVG (schémas) n'a été lu que dans sa transcription textuelle ; leurs titres et descriptions internes (balises title/desc) ne sont pas audités.
- Le glossaire commun (glossary/cardio_1.py et autres modules) n'a pas été relu : seules les clés ajoutées par glossary/i61.py l'ont été. L'audit d'abréviations de build_medina repose sur l'heuristique du moteur (au moins deux majuscules) ; des sigles à une seule majuscule ou des mots composés n'ont été vérifiés que par lecture.
- L'hypothèse selon laquelle « avant 6 h » et « avant 15 h » désignent des délais (et non des heures d'horloge) s'appuie sur les passages internes de la leçon (encadré Paramètres clés ; fenêtre Ondexxya) et non sur une relecture du protocole bernois.
- Les titres de références et les intitulés de sources n'ont pas été comparés aux publications originales.

## 7. Livrables

- `rapport.json` : synthèse structurée, empreintes, contrôles, renvois, lacunes.
- `propositions.json` : 206 entrées `{id, fichier, ancien, nouveau, motif, categorie, fond_inchange}` (plus `type` et `occurrences_ancien`).
- Les champs `nouveau` conservent les espaces ordinaires du texte d'origine, afin que la conversion en espaces insécables (GLOB-01) reste une opération globale distincte.

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
