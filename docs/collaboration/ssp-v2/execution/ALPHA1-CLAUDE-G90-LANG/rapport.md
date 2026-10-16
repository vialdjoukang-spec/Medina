# Audit linguistique G90 — Affections du système nerveux autonome (S08)

Mission ALPHA1-CLAUDE-G90-LANG, tour 1, génération 1. Branche `claude/alpha1/g90-lang-g1`, base `103745ba` (le manifeste porte `523832d9` ; les empreintes des sept fichiers sont conformes dans les deux cas). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. L'orthographe et l'accord sont globalement sûrs (peu de fautes d'orthographe pures, aucune ponctuation doublée, aucun mot répété, aucune apostrophe droite). Les défauts relevés sont d'une autre nature : **la syntaxe de chantier** (infinitifs injonctifs et phrases nominales que le guide de rédaction proscrit, § 2), **des métonymies** (« l'ESC 2018 distingue »), **des calques et du jargon de chantier** (« désavantagé », « causes lues », « conduite lue », « gold standard »), **quelques connecteurs et accords fautifs** (« donc », « sources américaine », « Elle est portée »), **des graphies hétérogènes** (« anti-hypotenseur », « post-ganglionnaires », « post-prandiale ») et **un point-virgule orphelin dans la figure 3**.

- **154 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte ; le glossaire compile après application.
- **23 renvois médicaux** : formulations dont la correction créerait ou retirerait une causalité, une fréquence, un dénominateur ou une portée que la source ne porte pas. Ils ne sont pas corrigés ici.
- **Choix différés, non appliqués** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers) ; uniformisation des plages (tiret ou « à ») ; délimitation des références en fin de phrase.
- **3 constats hors périmètre** transmis à l'audit MED, dont l'absence du sous-onglet Sémiologie.

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 87 |
| registre | 22 |
| orthographe | 12 |
| typographie | 7 |
| grammaire | 7 |
| cohérence | 6 |
| ambiguïté | 6 |
| ponctuation | 3 |
| répétition | 3 |
| unités | 1 |
| **Total** | **154** |

| Fichier | Propositions |
|---|---|
| G90_a.html | 46 |
| G90_b.html | 24 |
| G90_c.html | 25 |
| G90_d.html | 11 |
| G90_pop1.html | 27 |
| G90_pop2.html | 20 |
| g90.py | 1 |

## Les trois constats les plus graves

1. **Une phrase d’environ cent quinze mots, sans verbe principal, énumère onze mesures de prise en charge du syndrome douloureux régional complexe** (G90_b, section 10) : c’est le contre-exemple exact du guide (§ 2). Elle est reprise en une suite de phrases courtes sans retirer un élément (P-61).
2. **Un « donc » qui tire d'une rareté une absence d'immunité** et un « devient rare » sans état antérieur, dans l'interprétation de la fréquence de la dysréflexie autonome (G90_a, section 2) : la logique de la phrase est inversée. Le sens de la correction relève du fond ; elle est consignée en renvoi (R-04) avec le dénominateur douteux « 48 à 91 % des lésions » (R-03, R-22).
3. **Des formulations qui peuvent induire un contresens clinique** : « ≥ 6e segment thoracique » (inversion de lecture d'un rang anatomique, P-152), « dont 6 douloureux » d'accord indéterminé (R-09), « qui interrompt la transmission » d'antécédent indéterminé (R-18) et « l'iris … ne s'ouvre plus : la dilatation est retardée » (R-06).

## Propositions les plus utiles

- **P-61** (G90_b.html, syntaxe) : « Standards de la European Pain Federation, dont la task force inclut Balgrist (Zurich) <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6593444/" target="_blank" rel="noo… » devient « Les standards de la European Pain Federation, dont le groupe de travail inclut Balgrist (Zurich) <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6593444/" target="_blan… ». Paragraphe d’une seule phrase d’environ cent quinze mots, fait d’une énumération nominale de onze éléments séparés par des points-virgules (guide § 2 : phrases courtes et complètes, jamais nominales). Chaque élément est conservé et mis en phrase ; « task force » devient « groupe de travail » ; guillemets avec espaces insécables ; « sur-spécialisé » est corrigé en « surspécialisé » (préfixe soudé).
- **P-03** (G90_a.html, syntaxe) : « Les objectifs sont les suivants. Définir avec leurs seuils l’hypotension orthostatique, sa forme neurogène et l’hypertension de décubitus neurogène. Reconnaître le syndro… » devient « Cinq compétences sont attendues. Le médecin définit avec leurs seuils l’hypotension orthostatique, sa forme neurogène et l’hypertension de décubitus neurogène. Il reconna… ». Les infinitifs injonctifs en liste (« Définir », « Reconnaître », « Appliquer », « Mener », « Prescrire ») sont proscrits par le guide de rédaction (§ 2) ; les objectifs deviennent des phrases complètes à sujet exprimé, au contenu identique.
- **P-58** (G90_b.html, syntaxe) : « se prend en charge en dormant le lit entier incliné d’environ 12° au moins (relever seulement la tête du lit est moins efficace), en évitant le décubitus diurne et en ada… » devient « se prend en charge par un sommeil sur un lit entier incliné d’environ 12° au moins (relever seulement la tête du lit est moins efficace), par l’évitement du décubitus diu… ». Gérondifs sans sujet cohérent (« l’hypertension … en dormant ») : une maladie ne dort pas ; les gérondifs deviennent des compléments nominaux. Graphie « antihypotenseurs » alignée.
- **P-21** (G90_a.html, syntaxe) : « la pression élevée couché provoque une perte urinaire de sodium et d’eau pendant la nuit, d’où nycturie, perte volémique nocturne et aggravation de l’hypotension orthosta… » devient « la pression élevée en position couchée provoque une perte urinaire de sodium et d’eau pendant la nuit, d’où une nycturie, une perte volémique nocturne et une aggravation … ». « Couché » ne s’accorde pas avec « pression » et se rapporte au patient : « en position couchée » lève l’ambiguïté. Les trois noms après « d’où » reçoivent leur article (guide § 2 : pas de série nominale).
- **P-53** (G90_b.html, syntaxe) : « prévaut et la directive allemande 3.0 sur le sondage intermittent (2026) traite aussi ce sujet, mais son texte intégral n’a pas été lu » devient « prévaut. La directive allemande 3.0 sur le sondage intermittent (2026) traite aussi ce sujet, mais son texte intégral n’a pas été lu ». Phrase de plus de soixante mots à trois propositions coordonnées par « et » puis « mais » : elle est coupée en deux.
- **P-95** (G90_c.html, syntaxe) : « Le syndrome douloureux régional complexe associe inflammation (cytokines pro-inflammatoires, inflammation neurogène par substance P et CGRP), auto-immunité (auto-anticorp… » devient « Le syndrome douloureux régional complexe associe plusieurs mécanismes : une inflammation (cytokines pro-inflammatoires, inflammation neurogène par substance P et CGRP), u… ». Énumération de noms sans article ni terme collectif (guide § 2) ; « plusieurs mécanismes » et les articles sont ajoutés, sans toucher à aucun mécanisme cité.
- **P-107** (G90_pop1.html, syntaxe) : « La baisse est progressive et soutenue : pression systolique d’au moins 20 mmHg ou diastolique d’au moins 10 mmHg par rapport à la valeur de base, ou pression systolique i… » devient « La baisse est progressive et soutenue. Elle atteint au moins 20 mmHg pour la pression systolique ou au moins 10 mmHg pour la pression diastolique par rapport à la valeur … ». Après les deux-points, le groupe nominal « pression systolique d’au moins 20 mmHg » ne complète pas la phrase (la baisse n’est pas une pression) ; la phrase est coupée et complétée, avec les mêmes seuils.
- **P-89** (G90_c.html, ponctuation) : « <text x="190" y="173">petite zone frontale ; dissection carotidienne</text><text x="190" y="190">; imagerie vasculaire urgente si douleur</text> » devient « <text x="190" y="173">petite zone frontale ; dissection carotidienne ;</text><text x="190" y="190">imagerie vasculaire urgente si douleur</text> ». Dans la figure 3, la dernière ligne commence par un point-virgule orphelin (retour à la ligne mal placé) ; le signe est reporté en fin de la ligne précédente.
- **P-152** (G90_pop2.html, ambiguïté) : « dysréflexie 48–91 % ≥ 6e segment thoracique » devient « dysréflexie 48–91 % pour une lésion au niveau ou au-dessus du 6e segment thoracique ». Le symbole « ≥ » appliqué à un rang ordinal inverse la lecture (le 6e segment thoracique est plus bas que le 5e) ; la formule du texte principal est reprise.
- **P-135** (G90_pop2.html, syntaxe) : « Le consensus de 2018 a introduit le seuil de 90 mmHg ; ne pas écarter le diagnostic » devient « Le consensus de 2018 a introduit le seuil de 90 mmHg ; il ne faut pas écarter le diagnostic ». Infinitif injonctif greffé sur une phrase déclarative (guide § 2). L’attribution du seuil fait l’objet d’un renvoi.
- **P-147** (G90_pop2.html, grammaire) : « Sources américaine et revue systématique ; aucune posologie ni information professionnelle suisse lue : aucune dose n’est donnée dans ce cours. » devient « Les sources sont une revue américaine et une revue systématique ; aucune posologie ni information professionnelle suisse n’a été lue : aucune dose n’est donnée dans ce co… ». « Sources américaine » : nom pluriel accordé avec un adjectif singulier ; phrase sans verbe.
- **P-94** (G90_c.html, ambiguïté) : « Elle est portée par une personne sur 30 parmi » devient « La mutation est portée par une personne sur 30 parmi ». Le pronom « Elle » a trois antécédents possibles (mutation, exon, protéine Elongator-1, qui est le plus proche) ; le sujet réel, la mutation, est nommé. Cohérent avec G90_a (« porte la mutation fondatrice »).
- **P-84** (G90_c.html, grammaire) : « La classe de référence est : légère » devient « La classification de référence est la suivante : légère ». Une classification se compose de grades ; « la classe de référence » les confond (la question parle de « grade »).
- **P-01** (G90_a.html, cohérence) : « <a href="#g90-7">Démarche diagnostique et différentiel</a> » devient « <a href="#g90-7">Démarche diagnostique et diagnostic différentiel</a> ». L’intitulé du plan (« … et différentiel », adjectif sans nom) ne correspond pas au titre de la section 7 dans G90_b (« Démarche diagnostique et diagnostic différentiel »).
- **P-23** (G90_a.html, grammaire) : « ganglionopathie autonome auto-immune</button> associe des anticorps » devient « ganglionopathie autonome auto-immune</button> s’associe à des anticorps ». Une maladie n’« associe » pas des anticorps (verbe transitif sans agent) ; « s’associe à » exprime le lien rapporté.
- **P-12** (G90_a.html, syntaxe) : « Le diagnostic d’hypotension orthostatique est une définition mesurée » devient « Le diagnostic d’hypotension orthostatique repose sur une définition mesurée ». Un diagnostic n’« est » pas une définition (attribut illogique) ; il repose sur elle.
- **P-85** (G90_c.html, registre) : « La conduite lue : asseoir le patient, mesurer la pression à intervalles rapprochés et supprimer le déclencheur ; le traitement de la pression vient ensuite si elle reste … » devient « La conduite décrite consiste à asseoir le patient, à mesurer la pression à intervalles rapprochés et à supprimer le déclencheur ; le traitement de la pression vient ensui… ». « Conduite lue » est un tour de chantier ; la phrase nominale est complétée ; l’injonction finale (« suivre ») est mise à l’indicatif comme dans le paragraphe correspondant de la section 8 (« le protocole du centre spécialisé … prévaut »).
- **P-118** (G90_pop1.html, syntaxe) : « Mesurer la pression toutes les 2 à 5 minutes, asseoir le patient, supprimer le déclencheur (vider la vessie, soins intestinaux, recherche d’escarre, vêtement serré, lésio… » devient « Le médecin mesure la pression toutes les 2 à 5 minutes, assoit le patient et supprime le déclencheur (vidange de la vessie, soins intestinaux, recherche d’escarre, retrai… ». Infinitifs injonctifs mêlés à des groupes nominaux hétérogènes dans la parenthèse (guide § 2) ; « Si nécessaire, nitrate » est sans verbe. Le médicament et sa concentration sont conservés.
- **P-54** (G90_b.html, syntaxe) : « Devant une crise hypertensive chez un blessé médullaire haut, asseoir, chercher et supprimer le déclencheur (la vessie dans environ 85 % des cas), puis seulement traiter … » devient « Devant une crise hypertensive chez un blessé médullaire haut, le médecin assoit le patient, cherche et supprime le déclencheur (la vessie dans environ 85 % des cas), puis… ». Infinitifs injonctifs (guide § 2) dans l’encadré de synthèse ; sujet exprimé, mêmes gestes dans le même ordre.
- **P-30** (G90_a.html, orthographe) : « sous traitement anti-hypotenseur <a » devient « sous traitement antihypotenseur <a ». Le cours écrit « antihypertenseur » et « prohypertenseur » sans trait d’union ; « antihypotenseur » est aligné (huit occurrences dans les sept fichiers).
- **P-36** (G90_a.html, registre) : « sont désavantagés, car la pression chute rapidement » devient « sont peu adaptés, car la pression chute rapidement ». « Désavantagé » est un calque de l’anglais « disadvantaged » appliqué à un objet ; « peu adapté » rend l’idée en français.

La liste complète figure dans `propositions.json`.

## Renvois médicaux (hors correction linguistique)

Classés par fichier. Chaque renvoi cite l'extrait exact de la leçon.

- **R-01** (logique, G90_a.html) : « c’est-à-dire une accélération habituellement de 10 battements par minute ou moins ». « Absence d’accélération cardiaque » est glosée par « une accélération de 10 battements par minute ou moins » : une accélération existe donc encore. L’équivalence entre « absente » et « ≤ 10 » est une convention clinique à formuler par l’audit médical.
- **R-02** (ambiguïté, G90_a.html) : « après chirurgie thyroïdienne endoscopique : 0,03 à 0,48 % ». Le dénominateur du pourcentage n’est pas nommé (0,03 à 0,48 % de quoi : des opérés, des interventions ?). La précision change la donnée chiffrée : à compléter par l’audit médical d’après la source (Xie 2025, lue en résumé).
- **R-03** (fréquence, G90_a.html) : « 48 à 91 % des lésions au niveau ou au-dessus du 6e segment thoracique ; début habituel ». Une fréquence se rapporte à des patients et non à des « lésions » : « 48 à 91 % des lésions » est incorrect. Le dénominateur exact (patients blessés médullaires au niveau ou au-dessus de T6 ? tous blessés médullaires ?) change la donnée chiffrée : à trancher par l’audit médical d’après Eldahan et Rabchevsky 2017. Même formule dans la fenêtre g90-da.
- **R-04** (causalité, G90_a.html) : « la dysréflexie autonome devient rare dans le premier mois après la lésion (5,7 % seulement) et fréquente après 3 à 6 mois : un blessé médullaire récent n’est donc pas à l’abri ». Deux défauts de forme (« devient rare » sans état antérieur, « donc » qui tire de la rareté une absence d’immunité, alors que le sens est une opposition) dont la correction (« est rare … devient fréquente … n’est toutefois pas à l’abri ») redéfinit la chronologie et le lien logique. Les 5,7 % ne sont pas rapportés à un dénominateur. À trancher par l’audit médical.
- **R-05** (terminologie, G90_a.html) : « ou faux énophtalmos ». Le terme français usuel est « énophtalmie » (« pseudo-énophtalmie » pour le faux enfoncement du globe) ; « énophtalmos » est un emprunt direct. L’expression figure aussi dans la fenêtre g90-horner. Choix lexical à valider avec la terminologie ophtalmologique.
- **R-06** (cohérence, G90_a.html) : « l’iris sans dilatateur actif ne s’ouvre plus : la dilatation est retardée ». « Ne s’ouvre plus » (absence totale) et « la dilatation est retardée » (ralentissement) sont contradictoires dans la même phrase. Le choix entre « s’ouvre mal » et « s’ouvre avec retard » relève du physiologique : audit médical.
- **R-07** (lexique, G90_a.html) : « considéré comme pathologique et non psychopathologique ». Le couple « pathologique / psychopathologique » est lexicalement bancal (« pathologique » s’oppose à « normal », non à « psychopathologique »). Une formulation correcte (par exemple « d’origine organique ») modifie l’énoncé médical sur l’étiologie : à trancher par l’audit médical.
- **R-08** (logique, G90_a.html) : « la rechercher d’abord est donc la première mesure thérapeutique ». « Rechercher » une cause n’est pas une mesure thérapeutique ; la formulation exacte (retirer / réviser le médicament en cause ?) change la conduite énoncée : audit médical.
- **R-09** (accord, G90_a.html) : « dont 6 douloureux ». « 7 étaient des dissections, dont 6 douloureux » : l’adjectif masculin renvoie à « Horner » et non à « dissections » (féminin). Le sens attendu (6 Horner douloureux parmi les 7 dissections ? 6 dissections douloureuses ?) engage le dénombrement : à lever par l’audit médical d’après Maamouri 2023.
- **R-10** (terminologie, G90_b.html) : « décrite comme pathognomonique) ». « Pathognomonique » est un terme absolu (signe suffisant à lui seul) ; il figure dans l’onglet Examens et dans les fenêtres sous la même forme, rapporté à l’ESC 2018. Sa conservation, son atténuation ou son attribution exacte sont un choix médical.
- **R-11** (intitulé de source, G90_b.html) : « Spondylose cervicale de type artère carotide interne (perspective) ». L’intitulé de cette référence, cité à l’appui de la dissection carotidienne, est peu intelligible (spondylose cervicale « de type artère carotide interne ») et sans lien visible avec un Horner. L’intitulé exact, la pertinence de la source et son niveau de preuve sont à vérifier par l’audit médical.
- **R-12** (source, G90_b.html) : « Cette conduite provient d’une revue américaine qui cite les recommandations du Veterans Affairs ». Le texte reconnaît lui-même que la conduite aiguë de la dysréflexie repose sur une source américaine, alors que la règle du projet exclut une recommandation américaine comme fondement d’une conduite. Hors périmètre linguistique : transmis à l’audit médical.
- **R-13** (omission, G90_b.html) : « avec pour objectifs la morbimortalité et la qualité de vie ». Une morbimortalité ou une qualité de vie ne sont pas des objectifs en soi : le verbe manque (réduire la morbimortalité, améliorer la qualité de vie ?). Le sens attendu est évident mais le compléter revient à énoncer l’objectif d’une démarche de la Revue médicale suisse 2025 lue en résumé : audit médical.
- **R-14** (cohérence, G90_b.html) : « environ 12° au moins ». « Environ » et « au moins » se contredisent (valeur approchée / minimum). La suite du cours écrit « lit incliné ≥ 12° » ou « environ 12° ou plus ». Le choix entre valeur approchée et seuil minimal engage la prescription : audit médical d’après le consensus AAS/EFAS.
- **R-15** (cohérence, G90_b.html) : « Aucune source lue ne traite la grossesse, l’insuffisance rénale ou hépatique pour ces entités ; la tachycardie posturale peut être déclenchée par une grossesse ». La phrase affirme qu’aucune source ne traite la grossesse, puis cite la grossesse comme déclencheur de la tachycardie posturale. La nuance (conduite en grossesse non traitée, déclenchement traité) est une précision de fond : audit médical.
- **R-16** (ambiguïté, G90_c.html) : « l’apprentissage de la reconnaissance des prodromes et des manœuvres de contre-pression ». On peut reconnaître des prodromes ; on pratique des manœuvres. « Apprentissage de la reconnaissance des … manœuvres » est ambigu (reconnaître ou exécuter ?). La fenêtre g90-ttt reprend la même formule. La précision change le contenu de l’éducation thérapeutique : audit médical.
- **R-17** (cohérence, G90_c.html) : « l’hypersensibilité atteint 40 % chez les hommes âgés sans symptôme ». Le piège dit que l’hypersensibilité « atteint 40 % », alors que la section Fréquence (G90_a) et la fenêtre g90-sinus écrivent « jusqu’à 40 % ». Une valeur maximale n’est pas une valeur typique : le choix entre « jusqu’à 40 % » et « 40 % » modifie la donnée et relève de l’audit médical.
- **R-18** (ambiguïté, G90_c.html) : « qui interrompt la transmission dans les ganglions autonomes ». L’antécédent du pronom « qui » (verbe au singulier) n’est pas déterminé : ganglionopathie, récepteur ou acétylcholine ; les anticorps (pluriel) sont exclus par l’accord. Désigner l’agent de l’interruption de transmission (anticorps bloquants ? maladie ?) est un énoncé physiopathologique : audit médical.
- **R-19** (logique, G90_d.html) : « La pharmacologie des affections autonomes est plus limitée que leur sémiologie ». La comparaison oppose deux termes de nature différente (arsenal thérapeutique et richesse des signes). Le sens voulu (peu de médicaments pour des tableaux cliniques variés ?) est un jugement de fond : à confirmer par l’audit médical avant reformulation.
- **R-20** (ambiguïté, G90_d.html) : « bradycardie réflexe (atropine), rétention urinaire fréquente ». La parenthèse « (atropine) » n’indique pas son rôle (traitement de la bradycardie ? médicament en cause ?). La fenêtre g90-midodrine la reprend. Elle engage une conduite : audit médical d’après l’information professionnelle.
- **R-21** (terminologie, G90_d.html) : « syndrome de perte de sel de l’hyperplasie congénitale ». Le nom est incomplet : « hyperplasie congénitale » sans complément (des surrénales). La formule est reprise à l’identique dans la fenêtre g90-fludro. La précision du libellé de l’indication suisse est un énoncé de pharmacologie : audit médical d’après l’information professionnelle.
- **R-22** (fréquence, G90_pop1.html) : « 48 à 91 % des lésions au niveau ou au-dessus du 6e segment thoracique selon la complétude ». Même formule que dans G90_a : « % des lésions » au lieu de « % des patients ». Dénominateur à trancher par l’audit médical ; non corrigée ici.
- **R-23** (attribution, G90_pop2.html) : « Le consensus de 2018 a introduit le seuil de 90 mmHg ». Cette fenêtre attribue le seuil de 90 mmHg au « consensus de 2018 », alors que la section 1 de G90_a l’attribue à l’ESC 2018 par rapport au consensus de 2011 ; deux textes de 2018 coexistent dans le cours (ESC et AAS/EFAS). La source citée au bout de la phrase est l’ESC. Le choix de l’attribution relève de l’audit médical.

## Constats transmis à l'audit MED

- **H-01** (MAJEUR, G90_c.html) : L'onglet Sciences ne compte que trois sous-onglets (data-s : g90-s-anat, g90-s-physio, g90-s-genet) ; le sous-onglet « Sémiologie fondamentale et analytique » exigé par Vial est absent, et l'histologie et la biochimie ne sont pas représentées. Hors périmètre linguistique : transmis à l'audit MED (AGENTS.md).
- **H-02** (à évaluer par MED, G90_b.html) : La conduite aiguë de la dysréflexie autonome repose sur une revue américaine (le texte le dit : section 8 « Limite des sources », onglet Examens cas 4, onglet Pharmacologie, fenêtre g90-da-urgence) ; la règle du projet exclut une recommandation américaine comme fondement d'une conduite. À arbitrer par l'audit MED.
- **H-03** (à évaluer par MED, G90_b.html) : Les références « Information professionnelle suisse Midodrin Substipharm (AIPS) » et « Information professionnelle suisse Florinef 0,1 mg (AIPS) » pointent vers la page d'accueil https://amiko.oddb.org (sans fiche précise) ; la date de consultation figure dans la liste des références (15 octobre 2026) mais pas l'identifiant de la fiche. À vérifier par l'audit MED.
- **Figures** : Le contrôle a porté sur le texte des six figures SVG (légendes, étiquettes, ponctuation), pas sur leur provenance. Les six sont des schémas de texte en boîtes et flèches (aucun dessin anatomique : uniquement des rectangles, des flèches et des textes), annoncés « Schéma didactique » dans leur légende. Un seul défaut de langue : la ligne finale de la figure 3 commençait par un point-virgule orphelin (P-89).
- Aucune proposition n'affaiblit une obligation clinique.

## Choix différés

- Espaces insécables globales (avant ; : ? et !, entre nombre et unité ou pourcentage) : non appliquées en masse, car chacune est une opération mécanique et non une reformulation, et le critère d'unicité interdit d'en faire des centaines de propositions. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F. Volumes approximatifs hors balises : {"a": {"point_virgule": 39, "deux_points": 36, "interrogation": 0, "pourcent": 19, "nombre_unite": 31}, "b": {"point_virgule": 66, "deux_points": 35, "interrogation": 1, "pourcent": 18, "nombre_unite": 41}, "c": {"point_virgule": 44, "deux_points": 54, "interrogation": 14, "pourcent": 13, "nombre_unite": 48}, "d": {"point_virgule": 17, "deux_points": 10, "interrogation": 2, "pourcent": 0, "nombre_unite": 26}, "pop1": {"point_virgule": 46, "deux_points": 47, "interrogation": 0, "pourcent": 15, "nombre_unite": 29}, "pop2": {"point_virgule": 44, "deux_points": 63, "interrogation": 0, "pourcent": 15, "nombre_unite": 36}}. Seuls les guillemets français (6 occurrences : « neurogène », « brouillard cérébral », « à considérer », « malin », « pas de Horner », « vingt-dix ») et les séparateurs de milliers (4 occurrences) ont fait l'objet de propositions ponctuelles. Une règle globale sûre est : ' ;'→'\u00a0;', ' :'→'\u00a0:' (hors URL et attributs), ' ?'→'\u00a0?', chiffre+' '+{mmHg, mg, g, mm, s, min, %, °}→ espace insécable.
- Plages de valeurs : le cours mêle le tiret demi-cadratin (30–45 minutes, 140–159/90–99, 2–3 semaines, 15–45 ans, 5,5–26,2, 4e–5e segment) et la forme « de 2 à 3 mm », « 48 à 91 % ». Non uniformisées : le tiret est acceptable dans un tableau et change parfois la lecture (« à 30–45 minutes » = lecture à ce moment, non durée). Seules « 2–3 premières semaines » (G90_c) et « 15–45 ans » (G90_pop1) ont été corrigées lorsque la construction était fautive.
- Références insérées en fin de phrase : les liens <a> suivent le texte sans parenthèses ni crochets (ex. « … dont 6 douloureux Syndrome de Claude Bernard-Horner (Maamouri 2023). »). Le rendu navigateur n'a pas été contrôlé : si le moteur les affiche en texte courant, une convention de délimitation est à décider globalement ; si le moteur les transforme en renvois, rien à faire. Non proposé en masse.
- Pareto : les fenêtres de synthèse (pop2) sont rédigées en puces télégraphiques par construction ; seuls les fragments sans verbe, ambigus ou d'orthographe incohérente (4 cas) ont été repris.

## Observations

- Jargon de chantier : le cours emploie 36 fois « lu / lue / lues / non lu » (« causes lues », « conduite lue », « source lue en résumé »). Il traduit la règle « rien de mémoire » mais encombre le texte. Six occurrences ont été reformulées (trois en-têtes de colonnes, trois « conduite lue ») ; le reste relève d'un choix éditorial global.
- Terminologie : « antihypotenseur » (huit occurrences, cinq fichiers) est aligné sur « antihypertenseur » et « prohypertenseur » ; « postganglionnaire » (dix occurrences) sur l'unique « post-ganglionnaires » ; « postprandiale » sur « post-prandiale » (deux occurrences) ; « surspécialisé ».
- Le cours désigne parfois une société savante ou une année à la place du texte (« l'ESC 2018 distingue », « suit l'ESC 2018 », « Dose de l'ESC 2018 », « L'usage repose sur l'ESC 2018 ») ; six occurrences sont proposées en « les recommandations ESC 2018 ». Les mentions entre parenthèses « (ESC 2018, consensus fort) » et « (ESC 2018) » sont laissées.
- « Horner » employé seul (comme nom de syndrome) est un raccourci cohérent dans tout le cours après la première définition ; non modifié.
- Les titres des fenêtres et les étiquettes des boutons Pareto divergeaient pour trois paires ; trois propositions de cohérence (plan et deux boutons).
- Le cours contient de nombreux infinitifs injonctifs et phrases nominales dans les cartes, les fenêtres et les corrigés ; le guide de rédaction (§ 2) les proscrit. Les cas où la reformulation ne touche que la syntaxe sont proposés (87 propositions de catégorie syntaxe) ; les listes de mots-clés de type Pareto et les cellules de tableaux sont laissées.

## Lacunes

- Aucune vérification médicale n'a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l'application simulée a été faite en mémoire, aucun fichier canonique n'est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Aucun correcteur orthographique automatique n'était disponible dans l'environnement (hunspell, aspell, enchant absents) : l'orthographe a été contrôlée par relecture intégrale, par recherche de ponctuation doublée, de mots répétés et par inspection manuelle des 675 mots employés une seule fois.
- Les espaces insécables avant les signes doubles et entre nombres et unités ne sont pas proposées en masse (voir differes).
- Le manifeste et la consigne donnent deux base_sha différents (`523832d9` contre `103745ba`) ; les empreintes des sept fichiers sont conformes.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes | oui |
| Propositions | 154 |
| Propositions à ancien unique | 154 sur 154 |
| Renvois médicaux | 23 |
| Constats hors périmètre | 3 |
| Choix différés | 4 |
| Abréviations non couvertes après application | 0 |
| Glossaire compilable après application | oui |
| Source canonique modifiée | non |

Horodatage : date_debut non relevé (null) ; date_fin `2026-10-16T09:33:27Z` relevée par date -u avant le commit.
