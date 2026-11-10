# Audit linguistique G99 — Autres affections du système nerveux au cours de maladies classées ailleurs (S08)

Mission ALPHA1-CLAUDE-G99-LANG, tour 1, génération 1. Branche `claude/alpha1/g99-lang-g1`, base de la mission `523832d9` (worktree démarré sur `103745ba`, fusion de la PR #203 ; les sept sources figées sont identiques, empreintes conformes). Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est sobre et globalement correct. Les défauts relevés tiennent surtout à des phrases nominales ou à l’infinitif injonctif (proscrites par le guide de rédaction, y compris dans les fenêtres), à la mention de la fabrication du cours (« le dossier », « ce cours étudie », « la description ci-dessous »), à des ambiguïtés de référent, à des calques de l’anglais (« manquée », « confondants », « étiologie »), à des intitulés répétés (« Corrélation clinique. Corrélation clinique : ») et à un plan de la partie Pathologie qui omet la partie 12.

- **119 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte, glossaire syntaxiquement valide.
- **28 renvois médicaux** : formulations où une correction créerait ou retirerait une causalité, un chiffre, une attribution de source ou une définition. Ils ne sont pas corrigés ici.
- **9 observations hors périmètre** (sémiologie, figures, accessibilité, typographie globale) transmises au coordinateur.
- **Choix différés, non appliqués** : espaces insécables (aucun U+00A0 ni U+202F dans les sept fichiers) ; alternance chiffres et lettres ; alternance colonne et rachis.

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 56 |
| registre | 20 |
| ambiguïté | 14 |
| répétition | 8 |
| grammaire | 7 |
| ponctuation | 4 |
| cohérence | 4 |
| intitulé | 2 |
| terminologie | 2 |
| typographie | 1 |
| orthographe | 1 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| `chapters/G99/G99_a.html` | 23 |
| `chapters/G99/G99_b.html` | 29 |
| `chapters/G99/G99_c.html` | 19 |
| `chapters/G99/G99_d.html` | 5 |
| `chapters/G99/G99_pop1.html` | 30 |
| `chapters/G99/G99_pop2.html` | 9 |
| `glossary/g99.py` | 4 |

## Les trois constats les plus graves

1. **Plan du cours erroné (P-001).** Le sommaire de l’onglet Pathologie s’arrête à la partie 12 et fait pointer « Critères formels et paramètres clés » vers `#g99-12`, qui est la partie « Spécificités suisses » ; la partie 13 n’a aucune entrée. Une proposition locale rétablit les deux entrées.
2. **Statistique de 43 % à trois sens (R-06, R-07, R-08).** La partie 5 dit que 43 % des patients consultent pour la main, « souvent étiquetés » canal carpien ; le piège de la même partie, le tableau 7.5 et le tableau de la partie 12 en font la part du diagnostic erroné. Le numérateur change d’un passage à l’autre ; c’est un énoncé de fond à trancher par l’audit médical.
3. **Définition de la MCD et fourchette « jusqu’à 5 à 10 % » (R-03, R-05).** La myélopathie cervicale dégénérative est définie comme « la compression cervicale » (la fenêtre dit « dysfonction médullaire due à une compression ») ; la compression médullaire métastatique « touche jusqu’à 5 à 10 % » des patients, expression fautive dont les deux lectures (borne haute ou fourchette) diffèrent.

## Renvois médicaux (hors correction linguistique)

Classés par type. Chaque renvoi cite l’extrait exact de la leçon.

### Comptage

- **R-01** (`G99_a.html`) : « Elle réunit ici trois grands ensembles ». La partie 1 annonce « trois grands ensembles » (neuropathie autonome, myélopathie, atteinte urémique) alors qu’elle développe cinq sous-parties (dont la gastroparésie et l’amylose) et que l’épilogue dit « Quatre entités ». Le nombre est un énoncé de fond : à trancher par l’audit médical.
- **R-02** (`G99_a.html`) : « La description ci-dessous sépare les trois grandes chaînes. ». La partie 3 annonce « trois grandes chaînes » et en développe cinq (3.1 à 3.5) ; la phrase décrit en outre le plan (« ci-dessous ») au lieu d’énoncer le problème médical. Toute reformulation suppose de décider quelles chaînes sont regroupées.

### Définition

- **R-03** (`G99_a.html`) : « est la compression cervicale due à une hernie discale ». La MCD est définie comme « la compression cervicale » alors que la fenêtre g99-mcd la définit comme une « dysfonction médullaire due à une compression cervicale » (la myélopathie est la conséquence, non la compression). Même confusion dans le Pareto : « La MCD est une compression cervicale dégénérative ». Correction = définition médicale.
- **R-12** (`G99_a.html`) : « Le panel y ajoute une fonction motrice gastrique sévèrement perturbée (accord de 85 %). ». On ne sait pas si cette fonction motrice perturbée est un critère de la définition, une précision ou une option du panel ; « y ajoute » est ambigu. Lever l’ambiguïté exige de relire le consensus UEG/ESNM 2021.

### Classification

- **R-04** (`G99_a.html`) : « Ces stades correspondent à l’échelle PND de I à IV. ». Trois stades de locomotion sont mis en correspondance avec une échelle à quatre niveaux (I à IV) sans table de correspondance ; la source lue ne la donne pas (glossaire : « développement non fourni »). À sourcer ou à nuancer.

### Fréquence

- **R-05** (`G99_a.html`) : « touche jusqu’à 5 à 10 % des patients porteurs de métastases ». « Jusqu’à 5 à 10 % » est syntaxiquement fautif (borne haute ou fourchette ?). La partie 13 écrit « 5-10 % » sans « jusqu’à ». Choisir entre « jusqu’à 10 % » et « de 5 à 10 % » change le sens statistique : à trancher d’après la source (Revue médicale suisse 2016, non rouverte ici).

### Statistique

- **R-06** (`G99_a.html`) : « 43 % des présentations initiales de MCD sont de ce type ». Dans la partie 5, 43 % des patients consultent pour un engourdissement ou une douleur de la main, « souvent étiquetés » canal carpien ; ici, 43 % des présentations sont « de ce type » (main attribuée d’emblée à un canal carpien). Les deux énoncés n’ont pas le même numérateur (présentation par la main versus erreur diagnostique).
- **R-07** (`G99_b.html`) : « Syndrome du canal carpien (43 % des présentations de MCD) ». Le tableau 7.5 présente 43 % comme la part des « présentations de MCD » correspondant au diagnostic erroné de canal carpien ; la partie 5 dit seulement que 43 % consultent pour la main. Même écart que R-06.
- **R-08** (`G99_b.html`) : « Ce diagnostic erroné représente 43 % des présentations ». Le tableau de la partie 12 fait du canal carpien un diagnostic erroné représentant 43 % des présentations ; cf. R-06 et R-07. Formulation à aligner sur la source (BMJ 2018) par l’audit médical.
- **R-13** (`G99_a.html`) : « ne coexistent que dans 50 % des cas ». Le dénominateur de ces 50 % (patients avec neuropathie autonome, avec polyneuropathie, ou ensemble de la cohorte) n’est pas précisé ; la déduction « l’absence de polyneuropathie ne rassure donc pas » en dépend.
- **R-14** (`G99_a.html`) : « sont les nausées et les vomissements (95 %) ; la plénitude postprandiale ». Le même pourcentage (95 %) qualifie deux énoncés de nature différente (symptômes cardinaux ; symptômes fréquents) et revient pour d’autres items (test de vidange, test respiratoire). Possible report erroné d’une valeur de consensus, à vérifier dans la source.
- **R-15** (`G99_a.html`) : « impuissance (73 % des hommes) ». La valeur 73 % est donnée pour la dysautonomie globale (partie 2.4) et pour l’impuissance chez les hommes (partie 5) : une confusion entre deux données est possible. À vérifier dans le consensus européen 2021.

### Causalité

- **R-09** (`G99_a.html`) : « Parmi les facteurs de risque de la neuropathie autonome du diabète figure la rétinopathie ». Une association (rapport de cotes 2,26, cohorte transversale) est présentée comme « facteur de risque » ; la leçon rappelle ailleurs qu’une association pronostique ne prouve pas la causalité. Le chiffre est en outre répété (partie 2.1). Changer le terme modifie l’énoncé de fond.
- **R-24** (`G99_c.html`) : « fait de l’hyperkaliémie chronique le mécanisme principal proposé ». Une corrélation forte est présentée comme ce qui « fait » du mécanisme le principal ; l’inférence corrélation vers mécanisme contredit la prudence affichée ailleurs (partie 2.5).

### Source

- **R-10** (`G99_a.html`) : « Le consensus ESC distingue ainsi ». Le document ESC cité ailleurs est la Task Force 2018 sur la syncope (lignes directrices) ; la partie 4 parle de « consensus ESC » et le tableau de « l’ESC ». La désignation de la source (consensus, lignes directrices, Task Force) est un fait de référence, non un choix de style.
- **R-16** (`G99_a.html`) : « (Balgrist, Zurich) ». Le Balgrist est cité comme source (partie 2.3), sans entrée dans la liste de références de la partie 13 ; même remarque pour R-17 et R-26.
- **R-17** (`G99_b.html`) : « Le Balgrist (2026) recommande une décompression soutenue ». « Décompression soutenue » est inintelligible (maintenue ? précoce ? recommandée ?) et la source Balgrist (2026) ne figure pas dans la liste de références. Reformulation = choix de fond.
- **R-26** (`G99_pop1.html`) : « sa recommandation est corroborée par la source suisse du Balgrist ». La source du Balgrist ne figure pas dans les références de la fenêtre ; cf. R-16.

### Cohérence médicale

- **R-11** (`G99_a.html`) : « Deux situations ne tolèrent aucun retard ». Le premier épilogue place la « myélopathie progressive » parmi les situations qui ne tolèrent aucun retard ; la partie 8 la classe « urgence relative ». Le niveau d’urgence est un énoncé clinique.
- **R-18** (`G99_b.html`) : « Le diagnostic s’appuie sur trois éléments ». Les trois éléments sont : séquençage, biopsie, scintigraphie osseuse ; la partie e-5 annonce « trois preuves » : variante, biopsie, typage (la scintigraphie y est une phrase à part). Le typage est ici hors décompte. La liste des preuves est un énoncé de fond.
- **R-28** (`G99_d.html`) : « Médicaments à éviter ou à manier avec prudence. ». Le paragraphe range sous « à éviter » des médicaments seulement « non retenus par le consensus » (érythromycine, inhibiteurs de la pompe à protons, antiémétiques) : non retenu n’est pas à éviter. Choix de fond.

### Généralisation

- **R-19** (`G99_b.html`) : « Chaque ligne découle d’un mécanisme déjà étudié ». Seules trois des sept lignes du tableau (myélopathie/canal carpien, manipulation, compression métastatique) relèvent d’un mécanisme étudié ; les durées de prescription, le code à astérisque et la fludrocortisone n’en relèvent pas. « Peut siéger à plusieurs étages » est de plus un fait nouveau.
- **R-22** (`G99_c.html`) : « alors qu’un canal carpien ne touche qu’une main ». Le canal carpien bilatéral est cité comme signe d’alerte dans les parties 0 et 5 ; l’énoncé « ne touche qu’une main » les contredit. À reformuler par l’audit médical.

### Attribution

- **R-20** (`G99_b.html`) : « ≥ 30 mmHg en cas d’hypertension de décubitus ». Le seuil de 30 mmHg est attribué à la revue Diabetologia 2024 dans la partie 1.1, mais figure dans la parenthèse « (ESC, 2018) » du bloc de critères formels. Attribution de source à rectifier par l’audit médical.

### Certitude

- **R-21** (`G99_b.html`) : « Les tests cardiovasculaires réflexes confirmeront la neuropathie ». Le futur de certitude « confirmeront » préjuge du résultat de l’examen ; « permettront de confirmer » changerait le raisonnement pédagogique du cas.
- **R-23** (`G99_c.html`) : « une tachycardie de repos chez la personne diabétique révèle l’atteinte vagale ». « Révèle » affirme un lien univoque ; « évoque » serait un autre énoncé (une tachycardie de repos a d’autres causes).

### Cohérence des sources

- **R-25** (`G99_pop1.html`) : « Il n’existe pas de source suisse lue sur ce sujet. ». La partie 1.2 cite la Revue médicale suisse 2024 sur la gastroparésie diabétique (résumé lu) ; la fenêtre affirme qu’aucune source suisse n’a été lue. Lu au résumé et non lu sont deux statuts distincts.

### Logique

- **R-27** (`G99_d.html`) : « doit être considéré comme hors indication si la fiche ne la prévoit pas ». La phrase précédente établit que les fiches lues ne mentionnent pas la gastroparésie ; la condition « si la fiche ne la prévoit pas » est donc déjà tranchée. Passer au catégorique (« relève d’un usage hors indication ») est une décision réglementaire.

## Observations hors périmètre

- **Sémiologie.** Aucun sous-onglet « Sémiologie » : la barre Sciences compte quatre disciplines (anatomie, histologie, physiologie, biochimie et génétique). L’exigence Vial (sixième sous-onglet) relève de l’audit médical ALPHA1-CLAUDE-G99-MED ; elle n’est pas traitée ici.
- **Figures.** Les cinq figures sont des schémas SVG dessinés (fig. 1, 2 et 5 : chaînes de quatre cases ; fig. 3 : moelle comprimée ; fig. 4 : section nerveuse) et non des images sourcées ; leur conformité à la règle sur les figures anatomiques IA relève de l’audit médical. Aucune annonce ni lecture de figure n’est rédigée dans le texte (STYLE_REDACTION § 4).
- **Accessibilité.** Les trois schémas en chaîne portent le même attribut aria-label="Schéma", non descriptif ; non proposé comme remplacement local car l’attribut est identique dans trois fichiers (ancien non unique sans reprendre tout le SVG).
- **Fenêtre g99-ho.** La fenêtre « Hypotension orthostatique : définition et mesure » contient un mot vert qui rouvre la même fenêtre (data-k="g99-ho"). Anomalie de structure, non linguistique.
- **Typographie.** Aucune espace insécable (U+00A0 ou U+202F) dans les sept fichiers : espaces avant « ; : ! ? », entre un nombre et « % », « mmHg », « mL/min » et dans « p. ex. », « art. 7 ». Correction globale différée (action de moteur ou de script), non proposée en 119 remplacements locaux.
- **Nombres.** Alternance chiffres et lettres pour des durées comparables (« six mois » / « 6 à 12 mois » ; « quatre heures » / « 4 heures » ; « 5 jours » / « dix ans »). Choix éditorial différé.
- **Lexique.** Alternance « colonne », « rachis » et « colonne vertébrale » pour la même structure (IRM de l’ensemble de la colonne / du rachis). Choix éditorial différé.
- **Formules.** Le bloc « Critères formels » et l’épilogue de la partie 13 emploient « = » comme verbe (« un test réflexe anormal = possible »). Conservé : encadré de synthèse, risque de changer la portée des critères.
- **Tableaux.** Plusieurs tableaux (e-2, p-1, p-2) ne sont pas suivis d’un paragraphe de lecture (STYLE_REDACTION § 4) : défaut pédagogique, non reformulable localement.

## Exemples de propositions

| Id | Fichier | Avant | Après |
|---|---|---|---|
| P-002 | `G99_a.html` | Ce cours étudie ces atteintes <b>secondaires</b>, c’est-à-dire dues à une maladie dont elles sont la manifestation nerveuse. | Ces atteintes sont dites <b>secondaires</b> : chacune est la manifestation nerveuse d’une maladie qui la cause. |
| P-005 | `G99_a.html` | Elle réunit ici trois grands ensembles de tableaux : la neuropathie autonome | Cette catégorie réunit ici trois grands ensembles de tableaux cliniques : la neuropathie autonome |
| P-006 | `G99_a.html` | Une anémie ou une hypovolémie peuvent toutefois la faire monter davantage : | Une anémie ou une hypovolémie peuvent toutefois faire monter davantage la fréquence cardiaque : |
| P-021 | `G99_a.html` | Les troubles mictionnels débutent par un retard d’initiation, puis un globe vésical, puis l’incontinence et l’atonie sphinctérienne aux stades tard… | Les troubles mictionnels débutent par un retard d’initiation, évoluent vers un globe vésical, puis vers l’incontinence et l’atonie sphinctérienne a… |
| P-029 | `G99_b.html` | Les diagnostics confondants sont la polyradiculonévrite inflammatoire chronique, | Les diagnostics différentiels sont la polyradiculonévrite inflammatoire démyélinisante chronique, |
| P-032 | `G99_b.html` | L’épidurite carcinomateuse est l’étiologie la plus fréquente. La conduite est : IRM de la totalité de la colonne sans délai ; corticothérapie systé… | L’épidurite carcinomateuse est la cause la plus fréquente. La conduite comprend une IRM de la totalité de la colonne sans délai, une corticothérapi… |
| P-040 | `G99_b.html` | L’adaptation diététique est retenue (85 %), ainsi que les antagonistes dopaminergiques D2 (86 %) et les agonistes de la sérotonine 5-HT4 (85 %). | Le consensus retient l’adaptation diététique (85 %), ainsi que les antagonistes dopaminergiques D2 (86 %) et les agonistes de la sérotonine 5-HT4 (… |
| P-056 | `G99_c.html` | ne figurent pas dans le dossier de recherche et ne sont donc pas reproduites | ne figurent pas dans les sources lues et ne sont donc pas reproduites |
| P-070 | `G99_c.html` | il explique le paradoxe d’une hypotension debout avec une hypertension couchée, et la surélévation de la tête du lit. | il explique le paradoxe d’une hypotension debout avec une hypertension couchée et justifie la surélévation de la tête du lit. |
| P-084 | `G99_pop1.html` | Compression asymptomatique à l’imagerie chez 59 % des 40-80 ans : l’image ne suffit pas. | Une compression asymptomatique est visible à l’imagerie chez 59 % des 40-80 ans : l’image ne suffit pas. |
| P-116 | `g99.py` | ('N','Neuro'),('M','gastroenterology and Motility') | ('N','Neurogastroenterology and'),('M','Motility') |

## Vérifications mécaniques

- Empreintes : les sept fichiers correspondent au manifeste (`lecture.empreintes_calculees` dans `rapport.json`).
- Unicité : `ancien.count(fichier) == 1` pour les 119 propositions et `ancre.count(fichier) == 1` pour les 28 renvois ; aucun chevauchement dans un même fichier.
- Abréviations : `build_medina.audit()` renvoie `{}` sur les six fichiers HTML avant et après application simulée ; `ast.parse` valide `glossary/g99.py` modifié.
- Structure : l’équilibre des balises est inchangé par les propositions.

## Lacunes

- Aucune source médicale n’a été rouverte : l’audit ne vérifie pas le fond. Les renvois sont des doutes de lecture, non des constats médicaux établis.
- Le rendu navigateur n’a pas été exécuté ; seul le texte source a été contrôlé.
- Les 119 propositions n’ont pas été relues par un lecteur humain.
- Les trois `aria-label="Schéma"` identiques ne sont pas remplaçables localement (ancien non unique).

## Tableau de bord final

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes | oui |
| Propositions | 119 |
| Renvois médicaux | 28 |
| Observations hors périmètre | 9 |
| Abréviations non couvertes après application | 0 |
| Source canonique modifiée | non |
