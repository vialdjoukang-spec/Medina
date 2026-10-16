# Audit linguistique G93 — Autres affections du cerveau (S08)

Mission ALPHA1-CLAUDE-G93-LANG, tour 4, génération 1. Branche `claude/alpha1/g93-lang-g1`, base de la mission `523832d9`. Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est globalement intelligible et sobre. Les défauts relevés tiennent surtout à des phrases nominales ou à l’infinitif injonctif que le guide de rédaction proscrit, à des constructions fautives (« à 20 à 22 mmHg », « Éviter moins de 65 mmHg », « Associer mannitol et … néphropathie »), à des sujets mal choisis (« L’osmothérapie surveille », « Il commence par exclure »), à des anglicismes (« gold standard », « stenting », « terme parapluie »), à des personnifications, à des parenthèses imbriquées dans les libellés de liens, à la forme tronquée « hypertension idiopathique » qui évoque l’hypertension artérielle, et à du jargon de fabrication (« dossier »).

- **145 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire, suite des balises HTML identique, puis `build_medina.audit()` : aucune abréviation non couverte (résultat `{}` avant et après).
- **17 renvois médicaux** : formulations dont la correction créerait, retirerait ou préciserait un fait (causalité, chiffre, périmètre, unité, cohérence du cas clinique). Ils ne sont pas corrigés ici.
- **Choix différé, non appliqué** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers ; volume relevé et règle de traitement mécanique dans `rapport.json`, clé `differes`).

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 38 |
| registre | 25 |
| style | 25 |
| ambiguïté | 17 |
| terminologie | 13 |
| grammaire | 11 |
| typographie | 7 |
| répétition | 7 |
| cohérence | 2 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| chapters/G93/G93_a.html | 17 |
| chapters/G93/G93_b.html | 45 |
| chapters/G93/G93_c.html | 22 |
| chapters/G93/G93_d.html | 12 |
| chapters/G93/G93_pop1.html | 31 |
| chapters/G93/G93_pop2.html | 17 |
| glossary/g93.py | 1 |

## Renvois médicaux (hors correction linguistique)

Classés par ordre de fichier. Chaque renvoi cite l'extrait exact de la leçon.

- **R-01** (causalité/généralisation, G93_a.html) : « Le fil conducteur est unique : un cerveau enfermé dans un volume rigide tolère mal tout gonflement ou toute privation d’oxygène ». Le « fil conducteur unique » est posé comme valable pour toute la leçon ; or l’encéphalomyélite myalgique, le syndrome de Reye (trouble métabolique) et les kystes arachnoïdiens ne relèvent pas d’un gonflement ni d’une privation d’oxygène dans un volume rigide. Reformuler change le périmètre affirmé : à trancher par l’audit médical.
- **R-02** (fréquence/construction, G93_a.html) : « plus de 90 à 95 % des patients sont obèses ; survenue ». « Plus de 90 à 95 % » associe un minorant (« plus de ») et une fourchette : l’expression est contradictoire en elle-même. Même formule dans le paragraphe de la partie 4 (« et plus de 90 à 95 % des patients sont obèses. Une prise »), où elle double en outre « des femmes obèses » dans la même phrase. Le choix entre « plus de 90 % » et « 90 à 95 % » est un chiffre : à trancher par l’audit médical d’après la source.
- **R-03** (causalité, G93_a.html) : « c’est la raison pour laquelle les traitements médicamenteux visent la sécrétion de liquide cérébrospinal ». L’ignorance de l’étiologie est présentée comme la raison du choix de cibler la sécrétion de liquide cérébrospinal. Le lien causal n’est pas établi par la source citée (la cible thérapeutique découle de l’efficacité de l’acétazolamide, non de l’étiologie inconnue). Reformulation = changement de fond.
- **R-04** (comparaison de deux objets, G93_b.html) : « mais une asymétrie existe aussi chez 50 % des sujets sains ». La phrase oppose une « sténose » (90 % des HII) à une « asymétrie » des sinus (50 % des sujets sains) : deux grandeurs différentes comparées par « mais … aussi ». Même juxtaposition dans G93_c (fiche Veinographie). Quelle grandeur doit être comparée est une question de fond : à trancher par l’audit médical.
- **R-05** (ordre annoncé, G93_b.html) : « Ils s’ordonnent comme suit, du plus utile au plus invasif. ». Le tableau suivant est présenté comme ordonné du plus utile au plus invasif ; l’étape 3 (prise en charge des céphalées) est moins invasive que l’étape 2 (acétazolamide) et aucune source ne classe l’utilité. L’annonce ou l’ordre doivent être corrigés sur le fond.
- **R-06** (ambiguïté de fond, G93_b.html) : « Tous les survivants sont suivis dans les trois mois (troubles cognitifs, émotionnels, fatigue) ». La parenthèse ne dit pas si ces troubles sont recherchés (dépistage) ou traités : « suivis (troubles…) » est ambigu. Le choix du verbe (rechercher, dépister, traiter) change la conduite décrite ; la source ERC-ESICM 2021 doit trancher.
- **R-07** (causalité non sourcée, G93_b.html) : « Cette règle repose sur le fait que le niveau de conscience peut dépasser ce que l’examen clinique seul laisse voir. ». La justification de la règle de classement « au niveau le plus élevé » est absente de la fenêtre g93-conscience (qui indique seulement le classement) et le résumé seul de la recommandation a été lu. À sourcer ou retirer.
- **R-08** (causalité non sourcée, G93_b.html) : « parce que le malaise post-effort est le symptôme central que la gestion de l’énergie cherche à ne pas déclencher ». Le « parce que » justifie la règle des deux tiers par le malaise post-effort ; la fenêtre g93-pacing énonce la règle sans cette justification. À sourcer ou retirer ; la correction de forme seule (proposition « vise à ne pas déclencher ») ne règle pas ce point.
- **R-09** (omission, G93_b.html) : « La sévérité se classe en sévère (quasi confiné au domicile) et très sévère (quasi alité). ». La phrase annonce que la sévérité « se classe en » deux niveaux ; les niveaux léger et modéré sont omis. Ajouter ou nuancer = changement de fond.
- **R-10** (ambiguïté de fond, G93_b.html) : « la famille et l’école sont impliquées ». « Impliquées » ne dit pas dans quoi (prise en charge, adaptation scolaire, facteur déclenchant) ; l’énoncé de fond est à préciser d’après EUROMENE 2021.
- **R-11** (cohérence du cas, G93_b.html) : « Le plan associe une intervention multicomposante de perte de poids (indice de masse corporelle inférieur à 35 : grade B) ou la chirurgie bariatrique (35 ou plus : grade A) ». La patiente de la vignette 1 a un indice de masse corporelle de 38 kg/m² (G93_a) : le cas devrait retenir la chirurgie bariatrique (grade A) et non présenter l’alternative « inférieur à 35 ». Le cas récapitulatif énumère les deux branches sans choisir. Rétablir la cohérence est une décision clinique (la proposition de forme remplace seulement « associe » par « comprend »).
- **R-12** (unité, G93_pop1.html) : « pression du liquide supérieure à 250 mm (280 mm chez l’enfant obèse) ». L’unité est incomplète (« mm » seul) alors que tous les autres seuils de la leçon sont en cm d’eau (25 et 28 cm d’eau) : 250 mm correspondrait à 25 cm. L’unité exacte et la substance (liquide cérébrospinal ou eau) sont un fait nominal à vérifier dans la source ; non corrigé par ce rôle.
- **R-13** (renvoi interne, G93_pop1.html) : « Les traitements de l’œdème sont décrits dans la pharmacologie : l’osmothérapie ». La fenêtre annonce que les traitements (dont craniectomie décompressive et hypothermie) sont « décrits dans la pharmacologie » ; l’onglet Pharmacologie (G93_d) ne traite ni la craniectomie ni l’hypothermie. Incohérence de contenu à résoudre par l’audit médical (ajout ou retrait).
- **R-14** (ambiguïté de fond, G93_pop1.html) : « estime à 2–4 le nombre de médecins spécialisés par million d’habitants ». « Estime à 2–4 le nombre » peut signifier un besoin (« il faut 2 à 4 médecins… ») ou un effectif existant ; le sens change la conclusion. À vérifier dans EUROMENE 2021.
- **R-15** (formulation médicale, G93_pop2.html) : « Il n’existe pas de prophylaxie systématique. ». « Il n’existe pas de prophylaxie » est littéralement inexact (la phrase parle d’une pratique, non d’une existence) ; le sens voulu paraît être « la prophylaxie systématique n’est pas recommandée » (ou « déconseillée »). Entre « non recommandée » et « déconseillée », la force de la recommandation ERC-ESICM 2021 est un fait à vérifier.
- **R-16** (intitulé, G93_pop2.html) : « Mécanisme du risque ». L’intitulé annonce un mécanisme, mais le paragraphe contient une définition du syndrome de Reye et une réserve sur la causalité ; aucun mécanisme n’est décrit. Renommer (« Risque » / « Définition ») ou ajouter le mécanisme relève du fond.
- **R-17** (exactitude du développement, g93.py) : « ('U','of UnResponsiveness'),('R','score') ». Le développement lettre à lettre attribue à la lettre R le mot « score », alors que le nom complet donné par la même entrée (« Full Outline of UnResponsiveness ») ne contient aucun mot « score » : les quatre lettres F-O-U-R ne correspondent pas aux quatre éléments listés (« of UnResponsiveness » est rattaché à U, R reçoit « score »). Correction nominale à sourcer ; non appliquée par ce rôle.

## Propositions les plus utiles

- **P-08** (G93_a.html) : « les recommandations du traumatisme crânio-cérébral fixent un seuil de traitement de la pression intracrânienne… » devient « les recommandations sur le traumatisme crânio-cérébral fixent un seuil de traitement de la pression intracrâni… ». Préposition impropre (« recommandations du traumatisme ») et construction fautive « à 20 à 22 » : une fourchette s’exprime par « entre … et … ».
- **P-36** (G93_b.html) : « Éviter moins de 65 mmHg ; viser » devient « Éviter une pression inférieure à 65 mmHg ; viser ». « Éviter moins de 65 mmHg » est agrammatical : on évite une pression, non une quantité.
- **P-93** (G93_d.html) : « <b>Associer mannitol et médicaments néphrotoxiques ou néphropathie expose à l’insuffisance rénale.</b> » devient « <b>Associer le mannitol à des médicaments néphrotoxiques, ou l’administrer en cas de néphropathie, expose à l’… ». On n’« associe » pas un médicament à une maladie : « néphropathie » est coordonné par erreur à « médicaments néphrotoxiques ». Même sens que la fenêtre g93-mannitol.
- **P-96** (G93_d.html) : « L’osmothérapie par le mannitol surveille la pression veineuse centrale » devient « L’osmothérapie par le mannitol impose de surveiller la pression veineuse centrale ». Faux agent : une thérapeutique ne surveille pas ; elle impose une surveillance.
- **P-65** (G93_c.html) : « <b>Gold standard</b> : mesure » devient « <b>Examen de référence</b> : mesure ». Anglicisme ; cohérence avec la phrase d’introduction.
- **P-115** (G93_pop1.html) : « Le stenting des sinus veineux est débattu : resténose adjacente, un tiers des patients retraités, et rarement … » devient « La pose de stents dans les sinus veineux est débattue : une resténose adjacente est décrite, un tiers des pati… ». Anglicisme « stenting » ; « retraités » signifie en français « à la retraite » (faux-ami de retreated) ; énumération nominale sans verbe.
- **P-52** (G93_b.html) : « enfant fébrile viral » devient « enfant fébrile atteint d’une infection virale ». « Fébrile viral » n’est pas une locution française correcte ; l’adjectif « viral » qualifie l’infection.
- **P-42** (G93_b.html) : « Il commence par exclure les facteurs confondants » devient « La démarche commence par l’exclusion des facteurs confondants ». Sujet fautif : « Il » renvoie au pronostic, qui n’exclut rien ; le sujet exact est la démarche.
- **P-02** (G93_a.html) : « d’indice de masse corporelle à 38 kg/m² » devient « dont l’indice de masse corporelle est de 38 kg/m² ». Construction fautive : un indice « est de » une valeur, il n’est pas « à » cette valeur.
- **P-76** (G93_c.html) : « l’hypocapnie vasoconstricte et baisse le débit, l’hypercapnie l’augmente avec la pression intracrânienne » devient « l’hypocapnie provoque une vasoconstriction et diminue le débit, l’hypercapnie augmente le débit ainsi que la p… ». « Vasoconstricte » n’est pas un verbe attesté ; « l’augmente avec la pression » est ambigu. Même énoncé que l’îlot de la partie 8 : « l’hypercapnie augmente le débit et la pression intracrânienne ».
- **P-108** (G93_pop1.html) : « L’ophtalmologie comprend l’acuité » devient « L’examen ophtalmologique comprend l’acuité ». Une discipline ne « comprend » pas des mesures ; c’est l’examen.
- **P-100** (G93_pop1.html) : « participent aussi à la maladie. » devient « participent aussi à l’œdème. ». « La maladie » est imprécis (l’œdème, l’hypertension ?) ; la partie 5 du cours dit « à l’œdème ».

## Choix différés

- Espaces insécables globales : non appliquées, ni proposées. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F. Volume mécaniquement relevé dans le texte (hors balises et attributs) : 159 espaces avant « ; », 166 avant « : », 14 avant « ? », 60 avant « % », 13 paires de guillemets « » à espaces ordinaires, environ 130 couples nombre-unité (mmHg, kPa, cm, mL, mg, kg, g, µg, °C, heures, minutes, mois, ans). Règle proposée pour un traitement mécanique unique par le coordinateur : espace insécable fine avant ; : ! ? %, espace insécable à l’intérieur des guillemets et entre un nombre et son unité, appliquée aux seuls nœuds de texte (jamais aux attributs, aux URL ni aux balises). Une proposition locale par occurrence serait inapplicable (extraits non uniques).

## Observations

- Chiffres écrits « 20–22 mmHg », « 10–13 kPa », « 4,5 à 6,0 kPa » : l’intervalle est noté tantôt par un tiret demi-cadratin, tantôt par « à » (« 94 à 98 % », « 20 à 22 mmHg » en partie 3). Harmonisation typographique à décider globalement ; non proposée faute de forme canonique imposée.
- Nombres : « 1235 » et « 1500 mg » sont écrits sans espace insécable de milliers, « 100 000 » avec espace ordinaire ; relève du choix différé sur les espaces insécables.
- Les figures 1 à 4 ne sont annoncées ni commentées dans le texte courant (le mot « Figure » n’apparaît que dans l’étiquette accessible et la légende) : le guide de rédaction (§ 4) exige une annonce puis une lecture. Remarque de structure, non corrigée par une proposition locale.
- Figure 3 : la légende dit « Les axes ne sont pas chiffrés » alors que le schéma porte l’étiquette « Au-delà du seuil de 20 à 22 mmHg » : chiffre dans un schéma déclaré non chiffré (à arbitrer par l’audit médical).
- Le cours recourt à de nombreux encadrés « Piège » pour des avertissements de portée de lecture (« n’a pas été lu dans ce dossier / pour ce cours ») qui ne décrivent aucun piège clinique (g93-8 « Piège » sur la version 2025 de l’ERC-ESICM, g93-10, g93-12, d p-1). Intitulé à reconsidérer (par exemple « Limite de la source »).
- De nombreuses fenêtres (g93-secondaires, g93-emsfc « Bilan », g93-mannitol « Contre-indications » et « Surveillance », g93-acetazolamide « Effets indésirables ») juxtaposent des mots-clés sous une étiquette, sans verbe : le guide de rédaction (§ 2) proscrit « l’énumération de mots-clés à la place d’une explication ». Seules les phrases nominales entières ont fait l’objet de propositions.
- G93_pop1 (g93-cim, « Sous-catégories ») : un paragraphe de plus de 250 mots énumère douze sous-catégories ; le guide limite les paragraphes à trois à six phrases. Découpage proposé au rédacteur (un paragraphe par sous-catégorie), non réalisé ici car il suppose un remaniement de balisage.
- Cellules de tableau à l’infinitif injonctif conservées (sans proposition) lorsque l’infinitif nomme l’action attendue dans une colonne « Mesure » ou « Piège » (G93_d p-4 : « Réévaluer la tolérance », « Évoquer un syndrome de Reye » ; G93_b « Cible » : « Éviter … ; viser … ») : à trancher selon la tolérance du guide pour les cellules brèves.
- Terminologie : « pseudotumeur cérébrale » (G93_a) et « pseudotumor cerebri » (g93-friedman, g93-cim) désignent la même entité sous deux formes ; la forme latine n’est pas mise en italique. Harmonisation à décider.
- « Sourcée / non sourcée » (G93_d) : néologisme fréquent dans le corpus MEDINA ; conservé, une alternative serait « référencée ».
- Tableau 4 (G93_c) : l’en-tête « Lecture et lésion élémentaire » emprunte un terme de dermatologie qui s’applique mal aux valeurs de laboratoire ; conservé car il peut relever d’un gabarit commun.

## Figures

- Le contrôle a porté sur le texte des figures (étiquettes accessibles, légendes, étiquettes internes des SVG), pas sur leur provenance. La vérification de la provenance est transmise à l'audit MED.
- Figure 2 (G93_c.html, globe, nerf optique et gaine) : classe ORIGINE_INCONNUE ; statut réserve. Seule figure anatomique dessinée (SVG) ; sa légende la dit « ni à l’échelle ni calibrée ». Provenance à vérifier par l'audit MED ; la règle des figures anatomiques d’origine IA s’applique.
- Figures 1, 3, 4 (SVG : compartiments de Monro-Kellie, courbe pression-volume, cellule et canaux) : classe non évaluée par ce rôle (schémas conceptuels non anatomiques d'après leur légende) ; statut transmis à l'audit MED. Aucune provenance vérifiée. Figure 1 : étiquette accessible « loi de Monro-Kellie » harmonisée par la proposition correspondante. Figure 3 : voir observation sur le chiffre « 20 à 22 mmHg » dans un schéma déclaré non chiffré.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire, aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées par la leçon : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers.
- Le correcteur orthographique mécanique utilisé (pyspellchecker, dictionnaire français) ne vérifie ni les accords ni la syntaxe ; ceux-ci reposent sur la lecture intégrale. Aucun correcteur grammatical (type LanguageTool) n’était disponible dans l’environnement.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes conformes au manifeste | oui |
| Propositions locales | 145 |
| Renvois médicaux | 17 |
| Abréviations non couvertes après application simulée | aucune |
| Suite des balises HTML après application simulée | identique |
| Espaces insécables globales | différées (aucune occurrence existante) |
| Sources canoniques modifiées | aucune |

Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.
