# Audit linguistique G71 — Affections musculaires primitives (S08)

Mission ALPHA1-CLAUDE-G71-LANG, tour 1, génération 1. Branche `claude/alpha1/g71-lang-g1`, base `32416a20`. Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est globalement correct et sobre. Les défauts relevés tiennent à des constructions fautives de fourchettes (« à 10 à 14 ans », « supérieur à 10 à 12 »), à des accords (« la suxaméthonium », « la troisième percentile », « chaque 6 mois »), à des anglicismes et personnifications, à des parenthèses imbriquées dans les libellés de liens et à des mentions de fabrication du cours (« îlot », « dépôt »).

- **59 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte.

- **31 renvois médicaux** : formulations où une correction créerait ou retirerait une causalité, une fréquence ou une chronologie que la source ne porte pas. Ils ne sont pas corrigés ici.

- **Choix différés, non appliqués** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers) ; choix « fibrillation atriale » ou « auriculaire ».

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 18 |
| registre | 14 |
| grammaire | 10 |
| typographie | 4 |
| conjugaison | 3 |
| ambiguité | 3 |
| orthographe | 3 |
| ponctuation | 1 |
| terminologie | 1 |
| cohérence | 1 |
| répétition | 1 |

## Renvois médicaux (hors correction linguistique)

Classés par type de risque pour le fond. Chaque renvoi cite l'extrait exact de la leçon.

- **R-03** (causalité, G71_a.html) : « C’est pourquoi le consensus déconseille l’exercice excentrique ». Le connecteur « C’est pourquoi » fait du mécanisme (ischémie d’effort) la justification du consensus. La fenêtre associée juxtapose « Pourquoi » et « Conduite » sans que la source établisse ce lien. À confirmer ou à retirer par l’audit médical.
- **R-05** (causalité, G71_a.html) : « Ce choix de classement oriente le diagnostic différentiel ». Affirmation de conséquence clinique (« une myosite se traite autrement qu’une dystrophie ») sans source indiquée dans la phrase ; un classement CIM n’« oriente » pas le diagnostic. À sourcer ou retirer.
- **R-06** (causalité, G71_a.html) : « la diminution de la capacité vitale rend la paroi thoracique rigide et restrictive ». Sens de la causalité douteux : une paroi thoracique rigide ou restrictive réduit la capacité vitale, la phrase l’énonce à l’envers. La fenêtre G71_pop1 ne contient pas cette relation. Même énoncé dans G71_c (anatomie), voir R-24. Reformulation = changement de fond.
- **R-12** (causalité, G71_b.html) : « ce qui conduit les recommandations européennes à redéfinir ». Le texte fait de la fréquence des CK élevées chez les sujets sains la raison de la redéfinition ; la fenêtre (G71_pop1) ne le dit pas et la source est un abstract (EFNS 2010). Lien causal à confirmer ou à retirer.
- **R-13** (causalité, G71_b.html) : « évite le retard diagnostique ». Résultat affirmé (« évite ») pour une orientation précoce ; une source donnant cet effet n’est pas citée. « Réduit le risque de » serait un autre énoncé ; à décider par l’audit médical.
- **R-17** (causalité, G71_b.html) : « l’hypoxémie est un signe d’hypoventilation, pas la cause à traiter isolément ». Contradiction avec 8.3 (« l’hypoxémie traduit hypoventilation, atélectasie ou pneumonie ») : ici seule l’hypoventilation est citée. Le mécanisme « la SpO2 se corrige tandis que le CO2 s’accumule » n’est pas dans les fenêtres associées.
- **R-24** (causalité, G71_c.html) : « la paroi thoracique devient rigide et restrictive quand la capacité vitale diminue ». Même énoncé que R-06, avec la causalité inversée possible ; reformulation = changement de fond.
- **R-25** (causalité, G71_c.html) : « L’exercice aérobie sous-maximal est donc préféré ». « Donc » fait découler la recommandation du mécanisme (voir R-03) ; lien non établi par la source.
- **R-26** (causalité, G71_c.html) : « la myotonie explique la difficulté à lâcher un objet, et que la mexilétine ». Trois défauts : (1) coordination fautive (« explique la difficulté… et que la mexilétine… ») ; (2) lien causal « la myotonie explique l’absence d’amélioration de la qualité de vie sous mexilétine », absent de la revue Cochrane lue ; (3) « la ventilation nocturne précède la détresse » est une chronologie non sourcée. La phrase doit être réécrite sur le fond, pas seulement sur la forme.
- **R-27** (causalité, G71_c.html) : « un défaut énergétique diffus explique l’association de myopathie et d’atteinte du système nerveux central ». Contradit 3.4 (« le dossier lu ne détaille pas la sélectivité tissulaire », association seulement « cohérente avec » la fréquence de 69 %). « Explique » transforme une association descriptive en mécanisme.
- **R-30** (causalité, G71_d.html) : « La surveillance d’un médicament suit son mécanisme ». Généralisation causale : l’effet digestif du givinostat n’est pas relié à son mécanisme (inhibiteur des histone-désacétylases) par une source lue ; l’« à retenir » présente une règle générale comme un fait.
- **R-01** (causalité/fonction, G71_a.html) : « relie le cytosquelette de la fibre musculaire ». La dystrophine est présentée comme « reliant le cytosquelette », formule absente de la fenêtre associée (G71_pop1 : « protéine du cytosquelette ; assure la solidité, la stabilité et la fonction ») et tautologique pour une protéine du cytosquelette. Toute reformulation modifie l’énoncé fonctionnel : à trancher par l’audit médical (liaison sarcolemme-cytosquelette ou simple retrait de « relie »).
- **R-07** (causalité/chronologie, G71_a.html) : « touche d’abord les tissus gourmands ». « Touche d’abord les tissus gourmands » affirme une sélectivité tissulaire et une antériorité, alors que 3.4 précise que « le dossier lu ne détaille pas la sélectivité tissulaire ». « Gourmands » est de plus une métaphore. Toute correction suppose de retirer l’assertion : à trancher par l’audit médical.
- **R-02** (chronologie, G71_a.html) : « Chaque famille suit la même logique ». Chaîne causale unique « anomalie génomique, puis fibre, puis organe » posée comme commune à toutes les familles ; la figure 1 précise elle-même que les étapes intermédiaires diffèrent. La généralisation et le « puis » ne sont pas établis par les sources par famille. Reformulation = changement de fond.
- **R-08** (chronologie, G71_a.html) : « retarder le diagnostic de plusieurs années ». Durée du retard diagnostique (« plusieurs années ») absente des fenêtres associées. À sourcer ou à nuancer.
- **R-18** (chronologie, G71_b.html) : « annoncent un handicap plus rapide à anticiper ». Les seuils prédisent « un déclin plus rapide dans les 12 mois » (G71_pop2, Birnkrant 2018) ; « handicap plus rapide » est un résultat différent et la tournure « handicap plus rapide à anticiper » est inintelligible. Reformulation = choix de fond.
- **R-22** (chronologie, G71_b.html) : « l’intérêt renouvelé pour les thérapies précoces relance la question ». Chronologie et causalité (« programmes interrompus », « intérêt renouvelé… relance ») absentes des fenêtres lues ; source à indiquer ou énoncé à retirer.
- **R-14** (chronologie/ordre, G71_b.html) : « Diagnostic différentiel, de la cause la plus grave à la plus fréquente ». L’intitulé annonce un classement de la cause la plus grave à la plus fréquente ; la liste qui suit (myosites, troubles métaboliques, hépatopathie, hyperCKémie isolée) n’est justifiée ni par la gravité ni par la fréquence. Retirer la promesse ou classer la liste = changement de fond.
- **R-10** (fréquence, G71_a.html) : « Ces chiffres rappellent que l’atteinte musculaire est souvent la partie visible ». « Souvent » interprète les chiffres de la cohorte : atteinte musculaire isolée dans 27 %, du système nerveux central dans 69 %, cardiaque dans 21 % ; la source américaine est descriptive. Généralisation à valider.
- **R-11** (fréquence, G71_a.html) : « un variant de l’ADN mitochondrial pour la plupart des syndromes MELAS ». « La plupart » : le consensus lu dit « en particulier m.3243A>G » (G71_pop1, abstract seul) ; aucune proportion n’est donnée.
- **R-19** (fréquence, G71_b.html) : « car les complications majeures sont muettes avant d’être graves ». Généralisation à toutes les complications ; les sources lues décrivent le silence clinique de l’atteinte respiratoire et cardiaque, pas de toutes les complications (la crise surrénalienne, l’embolie graisseuse ne sont pas muettes).
- **R-28** (fréquence, G71_c.html) : « Une mère conductrice transmet l’anomalie, et les garçons sont atteints ». Formulation générale : tous les garçons ne sont pas atteints (transmission récessive liée à l’X) ; la source lue ne donne pas la proportion. Reformulation = ajout d’un fait.
- **R-29** (fréquence, G71_c.html) : « Un patient ne se limite jamais à son premier muscle atteint. ». « Jamais » absolu non établi par les sources lues (dystrophies des ceintures, myotonies non dystrophiques à atteinte prédominante musculaire).
- **R-09** (fréquence/comparaison, G71_a.html) : « orientent plus vite que n’importe quel examen ». Comparaison absolue (« plus vite que n’importe quel examen ») non établie par une source lue ; hyperbole à nuancer (« orientent d’emblée ») par l’audit médical.
- **R-04** (classification, G71_a.html) : « relèvent d’autres rubriques, et non de G71 ». Incohérence interne : cette phrase (et la phrase de 7.1 du fichier G71_b) exclut la dermatomyosite-polymyosite et l’infarctus musculaire ischémique de G71, alors que la fenêtre G71_pop1 les place en exclusion de G72 (catégorie voisine). La formule « myopathies inflammatoires, c’est-à-dire la dermatomyosite-polymyosite » assimile en outre un groupe à l’un de ses membres. Correction = fait de classification.
- **R-15** (omission, G71_b.html) : « un cas isolé montre une ophtalmoplégie externe progressive chronique mitochondriale ». La phrase omet le fait central du cas rapporté (faux positif des anticorps anti-récepteur de l’acétylcholine chez un patient atteint d’OEPC unilatérale, G71_pop1). Le lecteur ne comprend pas pourquoi le cas est cité. Ajout d’un fait = changement de fond.
- **R-21** (omission, G71_d.html) : « La contre-indication concerne l’hypersensibilité et l’insuffisance hépatique sévère ». La liste omet les vaccins vivants, pourtant contre-indiqués selon la même fiche (p-3 et p-5) ; le lecteur peut croire qu’il n’y a que deux contre-indications. Ajouter un élément = changement de fond.
- **R-20** (portée, G71_b.html) : « du test des apparentées ». « Apparentées » (féminin) limite le test aux parentes ; le conseil génétique de la conductrice peut viser tous les apparentés. Le même libellé figure dans G71_pop1 (« test des apparentées »). Le choix entre féminin et masculin générique change le périmètre : à trancher par l’audit médical.
- **R-16** (portée des sources, G71_b.html) : « (recommandations ESC 2022, section lue) ». Incohérence : ici « section lue », alors que G71_pop1 écrit « le tableau ESC 2022 sur les maladies neuromusculaires n’a pas été extrait » et le range parmi les sources non lues. La portée de lecture de la citation est à clarifier.
- **R-23** (cohérence du cas, G71_b.html) : « sa capacité vitale forcée est à 55 % ». Le cas récapitulatif décide d’« organiser la toux assistée » alors que la CVF (55 %) n’atteint pas le seuil lu (< 50 %, tableau de 9.1), et d’« éviter les agents déclenchants à l’anesthésie » alors que l’enfant « vient d’être opéré ». Cohérence clinique à rétablir par l’audit médical.
- **R-31** (exactitude du développement, g71.py) : « ('E','European'),('N','Neuromuscular'),('M','Muscle'),('C','Centre') ». Le développement lettre à lettre est faux : E-N-M-C se lit European NeuroMuscular Centre, la lettre M ne correspond pas à « Muscle » en plus de « Neuromuscular » ; le développement français retenu (« Centre européen du muscle et des maladies neuromusculaires ») n’est pas la dénomination courante. Correction = fait nominal sourçable ; non appliquée par ce rôle.

## Propositions les plus utiles

- **P-01** (G71_a.html) : « perd la marche en moyenne à 10 à 14 ans » devient « perd la marche en moyenne entre 10 et 14 ans ». Construction fautive « à 10 à 14 ans » : la fourchette s’exprime par « entre … et … ».
- **P-02** (G71_a.html) : « ou à la troisième percentile » devient « ou au troisième percentile ». Percentile est masculin.
- **P-14** (G71_b.html) : « le dépistage des apparentées » devient « le dépistage des apparentés ». Accord au masculin générique ; cohérent avec « le dépistage des apparentés » en 4. La portée féminine n’est pas établie dans la source.
- **P-15** (G71_b.html) : « les anesthésiques inhalés et la suxaméthonium exposent » devient « les anesthésiques inhalés et le suxaméthonium exposent ». Suxaméthonium est masculin.
- **P-16** (G71_b.html) : « Éviter les anesthésiques inhalés et la suxaméthonium, et demander » devient « Éviter les anesthésiques inhalés et le suxaméthonium, et demander ». Suxaméthonium est masculin.
- **P-17** (G71_b.html) : « les anesthésiques inhalés et la suxaméthonium peuvent provoquer » devient « les anesthésiques inhalés et le suxaméthonium peuvent provoquer ». Suxaméthonium est masculin.
- **P-31** (G71_b.html) : « réévaluer chaque 6 mois » devient « réévaluer tous les 6 mois ». « Chaque » ne se construit pas avec un pluriel de fréquence.
- **P-33** (G71_b.html) : « conductrices de dystrophine</button> » devient « conductrices de dystrophinopathie</button> ». Cohérence terminologique avec « conductrices de dystrophinopathie » employé en 4 ; la dystrophine est une protéine, la maladie est une dystrophinopathie.
- **P-39** (G71_c.html) : « quatre marches de plus de 8 secondes, dix mètres de plus de 10 à 12 secondes » devient « quatre marches en plus de 8 secondes, dix mètres en plus de 10 à 12 secondes ». Une durée s’exprime par « en plus de ».
- **P-46** (G71_d.html) : « une case vide signifie que la dose n’est pas rapportée » devient « la mention Non précisée signifie que la dose n’est pas rapportée ». Le tableau ne contient aucune case vide ; il emploie la mention « Non précisée » (cohérence interne).
- **P-47** (G71_d.html) : « l’anesthésie sans agents déclenchants évite le dantrolène prophylactique » devient « l’anesthésie sans agents déclenchants ne justifie pas de dantrolène prophylactique ». « Évite » est ambigu (l’anesthésie ne peut éviter un médicament) ; reprend la formule « n’est pas indiqué » de la leçon.

La liste complète figure dans `propositions.json`.

## Constats transmis à l'audit MED

- **H-01** (hors périmètre linguistique, MAJEUR, transmis à l'audit MED) : G71_c.html compte 5 `data-s` (Anatomie, Histologie, Physiologie, Biochimie, Génétique) ; le sous-onglet « Sémiologie fondamentale et analytique » est absent.
- **Figures** : la Figure 2 (topographies de faiblesse, SVG anatomique dessiné) est classée ORIGINE_INCONNUE, en réserve. Les Figures 1, 3, 4, 5 et 6 sont des schémas non anatomiques d'après leur légende, non évalués. Le contrôle a porté sur le texte des figures, pas sur leur provenance ; la vérification de provenance est transmise à l'audit MED.
- Aucune proposition n'affaiblit une obligation clinique.

## Observations

- Terminologie : « succinylcholine » (G71_a, 3.4 et 4 ; G71_pop1 hyperthermie maligne) et « suxaméthonium » (G71_b, G71_d, G71_pop1, G71_pop2) désignent la même substance ; harmonisation à décider (dénomination suisse à confirmer par l’audit médical).
- Libellés de liens interactifs : plusieurs libellés incorporent une parenthèse explicative (ex. « hyperCKémie (seuil, cause et conduite) ») qui alourdit la phrase ; seules les parenthèses imbriquées ont fait l’objet de propositions (P-10, P-11, P-12, P-32, P-44).
- Nombres : « 100 000 » est écrit avec espace, « 1000 » et « 3000 » sans ; relève du choix différé sur les espaces insécables et les nombres.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire, aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Le manifeste et la consigne donnent deux base_sha différents (d1a488ad contre 32416a20) ; les empreintes des sept fichiers sont conformes.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes | oui |
| Propositions | 59 |
| Propositions à ancien unique | 59 sur 59 |
| Renvois médicaux | 31 |
| Choix différés | 2 |
| Abréviations non couvertes après application | 0 |
| Source canonique modifiée | non |
