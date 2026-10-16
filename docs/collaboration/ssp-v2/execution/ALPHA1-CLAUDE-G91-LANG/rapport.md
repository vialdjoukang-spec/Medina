# Audit linguistique G91 — Hydrocéphalie (S08)

Mission ALPHA1-CLAUDE-G91-LANG, tour 1, génération 1. Branche `claude/alpha1/g91-lang-g1`, base `103745ba` (le manifeste porte `523832d9` ; empreintes des sept fichiers conformes dans les deux cas). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. La langue est globalement correcte, dense et précise, mais quatre familles de défauts reviennent : (1) des phrases nominales ou des infinitifs injonctifs dans les encadrés de synthèse, les algorithmes et les énoncés de cas, que le guide de rédaction proscrit (§ 2) ; (2) des constructions fautives ou ambiguës (antécédent de « qui », « atteint » pour « complique », « céder par ses sutures », « Les adultes ne disposent pas de dose ») ; (3) des mentions de fabrication du cours (« Ce chapitre apprend… », « Il nomme… », « îlot 10 »). La quatrième tient à des raccourcis de registre (« dans Alzheimer », « l’Alzheimer », « Dérivation VP = pilier »).

- **89 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte, avant comme après ; glossaire modifié compilé sans erreur.
- **27 renvois médicaux** : formulations où une correction créerait ou retirerait une causalité, une portée, un chiffre ou une dénomination que la source ne porte pas. Ils ne sont pas corrigés ici.
- **Choix différés, non appliqués** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers ; 436 espaces simples avant « ; : ? ! », 46 guillemets, 184 occurrences « nombre % » relevés) ; choix entre « tap test » et « test de soustraction de LCS ».

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 45 |
| registre | 17 |
| ambiguïté | 7 |
| cohérence | 6 |
| grammaire | 5 |
| terminologie | 4 |
| ponctuation | 2 |
| répétition | 2 |
| typographie | 1 |

## Propositions les plus utiles

- **P-01** (G91_a.html) : « Ce chapitre apprend à reconnaître ces deux visages, à les classer, à confirmer le diagnostic par l’imagerie et le test de soustraction de LCS, puis à choisir entre dérivation et  » devient « Il faut savoir reconnaître ces deux visages, les classer, confirmer le diagnostic par l’imagerie et le test de soustraction de LCS, puis choisir entre dérivation et  ». Personnification du chapitre (« apprend ») et annonce de plan, proscrites par le guide de rédaction (§ 3) ; la phrase énonce directement les compétences visées.
- **P-02** (G91_a.html) : « Il nomme aussi ce que les sources lues ne permettent pas d’affirmer : aucune recommandation suisse ni européenne spécifique à l’hydrocéphalie n’a pu être lue. » devient « Les limites des sources lues sont aussi signalées : aucune recommandation suisse ni européenne spécifique à l’hydrocéphalie n’a pu être lue. ». Personnification du chapitre (« Il nomme ») et description de la fabrication du cours, proscrites par le guide de rédaction (§ 3).
- **P-04** (G91_a.html) : « c’est un trouble de l’écoulement du LCS, qui prend une forme aiguë chez l’enfant » devient « c’est un trouble de l’écoulement du LCS ; ce trouble prend une forme aiguë chez l’enfant ». L’antécédent de « qui » est ambigu (le LCS ou le trouble) ; la reprise par « ce trouble » lève l’ambiguïté.
- **P-11** (G91_a.html) : « la pression intracrânienne se manifeste par céphalées, vomissements et œdème papillaire » devient « l’hypertension intracrânienne se manifeste par des céphalées, des vomissements et un œdème papillaire ». La pression ne « se manifeste » pas ; c’est son élévation (hypertension intracrânienne), terme déjà employé dans le cours. Articles ajoutés à l’énumération.
- **P-13** (G91_a.html) : « atteint jusqu’à 85 % des méningites tuberculeuses de l’enfant » devient « complique jusqu’à 85 % des méningites tuberculeuses de l’enfant ». Sens du verbe inversé : l’hydrocéphalie complique la méningite, elle ne « l’atteint » pas.
- **P-25** (G91_b.html) : « <li>Écarter une cause évidente de dilatation » devient « <li>Le médecin écarte une cause évidente de dilatation ». Infinitif injonctif proscrit par le guide de rédaction (§ 2) ; phrase complète à sujet explicite.
- **P-30** (G91_b.html) : « D’abord les causes secondaires d’hydrocéphalie ci-dessus, parce qu’elles changent le traitement. Ensuite les maladies qui miment la triade ou coexistent avec elle ( » devient « Il faut d’abord envisager les causes secondaires d’hydrocéphalie citées ci-dessus, parce qu’elles changent le traitement. Il faut ensuite envisager les maladies qui miment la triade ou coexistent avec elle ( ». Deux phrases nominales sans verbe (guide § 2) ; « ci-dessus » ne qualifie pas directement un nom (« citées ci-dessus »).
- **P-33** (G91_b.html) : « sont détaillés dans l’îlot 10 » devient « sont détaillés dans la partie 10 ». « Îlot » est un terme de fabrication du cours, que le lecteur ne voit pas ; l’interface parle de « parties » (boutons Partie suivante/précédente).
- **P-36** (G91_b.html) : « de niveau I, de validité externe et de durabilité limitées » devient « de niveau I, mais de validité externe et de durabilité limitées ». L’énumération laisse croire que « niveau I », « validité externe » et « durabilité » sont trois qualités ; « mais » précise l’opposition avec « limitées ».
- **P-38** (G91_b.html) : « L’index de comorbidité de Kiefer ≤ 3 prédit 93 % d’améliorés à 2 ans » devient « Un index de comorbidité de Kiefer ≤ 3 prédit 93 % de patients améliorés à 2 ans ». C’est une valeur de l’index (≤ 3), non « l’index » lui-même, qui prédit ; « d’améliorés » est un substantif familier.
- **P-49** (G91_b.html) : « Un homme de 76 ans, marche à petits pas depuis 18 mois, impériosité mictionnelle, ralentissement. » devient « Un homme de 76 ans marche à petits pas depuis 18 mois et présente une impériosité mictionnelle ainsi qu’un ralentissement. ». Virgule fautive entre le sujet et le verbe, puis énumération sans verbe (guide § 2).
- **P-75** (G91_d.html) : « Les adultes ne disposent pas de dose lue pour cette indication » devient « Aucune dose adulte n’a été lue pour cette indication ». Faute de sens : les adultes ne « disposent » pas d’une dose ; c’est la source qui n’en fournit pas.
- **P-23** (G91_b.html) : « soit amélioration après tap test ou drainage</td> » devient « soit amélioration après test de soustraction (tap test) ou drainage</td> ». « Tap test » apparaît ici pour la première fois dans le texte, alors que le cours emploie « test de soustraction de LCS » ; l’équivalence est donnée à la première occurrence.
- **P-48** (G91_b.html) : « cet écart signale un suivi neuropsychologique à systématiser » devient « ce faible taux montre que le suivi neuropsychologique est à systématiser ». « Cet écart » n’a pas de référent (écart entre quoi et quoi ?) ; « signale un suivi à systématiser » est une construction incorrecte.

La liste complète figure dans `propositions.json`.

## Renvois médicaux (hors correction linguistique)

Classés par type de risque pour le fond. Chaque renvoi cite l'extrait exact de la leçon.

- **R-14** (force de l’assertion, G91_b.html) : « L’amélioration après tap test confirme l’hypothèse ». « Confirme » est plus fort que « Soutient l’iNPH probable » (tableau de la partie e-3) et que « soutient » des critères japonais ; la hiérarchie des termes (confirmer, soutenir, suggérer) est un choix médical.
- **R-21** (force de l’assertion, G91_c.html) : « Évitée en cas d’obstruction par une masse ». La ligne du tableau écrit « Évitée » dans la colonne Examen et « Contre-indiquée dans ce cas » dans la colonne Statut : éviter et contre-indiquer n’ont pas la même portée. Harmoniser suppose de trancher.
- **R-25** (force de l’assertion, G91_c.html) : « nulle sur l’hydrocéphalie post-hémorragique du prématuré ». « Nulle » (de même « sans effet » dans la fenêtre « Acétazolamide (Diamox®) : fiche rapide ») est plus fort que « n’ont pas réduit l’hydrocéphalie post-hémorragique » (parties 9 et p-4) : absence de preuve d’efficacité ou efficacité nulle.
- **R-03** (généralisation, G91_a.html) : « Ici, le liquide cérébrospinal (LCS) ne s’écoule plus ». Formule absolue appliquée à la vignette du nourrisson, sans préciser la forme (obstructive ou communicante) ; la partie 3 avertit que « le liquide ne passe plus » ne décrit que la forme obstructive. Préciser la forme suppose un choix médical.
- **R-04** (généralisation, G91_a.html) : « La conduite diffère entièrement. ». « Entièrement » est un absolu ; de même, « forme aiguë chez l’enfant » généralise (la partie 5 distingue l’enfant plus âgé, à boîte crânienne rigide). Nuancer suppose de décider de la portée clinique.
- **R-07** (portée, G91_a.html) : « L’hémorragie sous-arachnoïdienne produit une hydrocéphalie chez environ un patient sur quatre ». Le tableau de la partie 2 et la fenêtre « Hydrocéphalie aiguë après hémorragie sous-arachnoïdienne » limitent la valeur d’environ 25 % à l’hémorragie sous-arachnoïdienne anévrismale ; l’encadré la généralise à toute hémorragie sous-arachnoïdienne. « Produit » énonce de plus une causalité plus forte que « se complique de ».
- **R-15** (portée, G91_b.html) : « Parcours de sélection (modèle suisse). ». Un seul centre (Lausanne) est décrit ; « modèle suisse » généralise à la Suisse. Le titre exact dépend de ce que la source autorise à affirmer.
- **R-08** (antécédent, G91_a.html) : « elle suit 0,7–3,7 % des traumatismes crâniens ». Dans la phrase, « elle » reprend grammaticalement « l’hydrocéphalie post-hémorragique » ; la fenêtre « Épidémiologie pédiatrique » rattache ce chiffre à l’hydrocéphalie post-traumatique. Corriger l’antécédent exige de trancher entre les deux entités.
- **R-18** (antécédent, G91_b.html) : « 67 % ont une scolarité ordinaire ». Le sujet des trois pourcentages (« 67 % », « 56 % », « 42 % ») n’est pas précisé : population de la cohorte, survivants, ou sujets évalués. Préciser la population est une affirmation de fond.
- **R-09** (terminologie statistique, G91_a.html) : « sans valeur prédictive négative démontrée de la réponse à la dérivation ». « Valeur prédictive négative » est un terme de performance diagnostique, ici employé au sens de « ne prédit pas une mauvaise réponse » (formulation de la fenêtre associée). Remplacer le terme change le contenu statistique affirmé.
- **R-17** (terminologie statistique, G91_b.html) : « (rapport de risque 0,38) ». Le texte écrit « rapport de risque » ici, alors que la partie p-4 et les fenêtres emploient « HR » (hazard ratio, rapport de risques instantanés). Les deux mesures ne sont pas interchangeables ; le choix du terme dépend de la source.
- **R-11** (dénominateur absent, G91_a.html) : « hyperactivité détrusorienne d’environ 70 % ». Le pourcentage n’a ni dénominateur (patients iNPH ? patients avec trouble urinaire ?) ni source ; il ne figure pas dans la fenêtre « Cognition de l’iNPH ». À sourcer avant de reformuler.
- **R-19** (dénominateur absent, G91_b.html) : « pour 13 000 € ». Le coût de 13 000 € n’est rapporté ni à un patient ni à une période (par patient ? sur la vie restante ?) ; la formulation « pour 13 000 € » est ambiguë. À préciser d’après le modèle suédois.
- **R-01** (classification clinique, G91_a.html) : « Deux patients, deux urgences de nature opposée ». La phrase présente les deux vignettes comme deux « urgences », alors que la partie 1 décrit l’iNPH comme un « tableau lent » et la partie 0 la qualifie elle-même de « cause traitable ». Qualifier l’iNPH d’urgence ou non est un choix clinique, pas une correction de forme.
- **R-02** (certitude diagnostique, G91_a.html) : « possible, c’est-à-dire une cause traitable de troubles de la marche et de déclin cognitif ». « Possible, c’est-à-dire une cause traitable » identifie le niveau « possible » (hypothèse à tester, partie 6) à une cause traitable ; le niveau de certitude de traitabilité n’est atteint qu’après la dérivation. La formulation exacte relève du fond.
- **R-05** (dénomination, G91_a.html) : « Institut fédéral allemand des médicaments (BfArM) ». Le texte désigne le BfArM comme « Institut fédéral allemand des médicaments » ; la dénomination officielle complète de l’institut n’a pas été vérifiée dans une source lue. À confirmer sur la source avant correction.
- **R-06** (classification, G91_a.html) : « La rubrique G91 inclut l’hydrocéphalie acquise. ». La phrase suit l’énumération des exclusions, dont P91.7 (hydrocéphalie acquise du nouveau-né) : le lecteur peut croire à une contradiction. La limite exacte de l’inclusion (acquise de l’enfant et de l’adulte hors période néonatale) est un fait de classification à confirmer.
- **R-10** (ellipse, G91_a.html) : « Manifestation : crâne qui s’élargit chez le nourrisson, pression et triade lente chez l’adulte. ». L’ellipse masque une assertion : « pression … chez l’adulte » (hypertension intracrânienne ? elle caractérise surtout l’enfant plus âgé, selon la partie 3, alors que l’iNPH est à pression normale). Rédiger la phrase complète oblige à choisir le sens.
- **R-12** (fréquence, G91_a.html) : « Elle n’est complète que chez environ 60 % des iNPH. ». L’encadré donne « environ 60 % » comme valeur unique ; le tableau précédent rapporte aussi 12,1 % dans une enquête japonaise de 1524 patients. Le choix de la valeur de synthèse est un jugement de fond.
- **R-13** (ordre annoncé, G91_b.html) : « Diagnostic différentiel, par ordre de gravité décroissante. ». L’intitulé annonce un classement par gravité décroissante, mais la phrase suivante justifie l’ordre par l’influence sur le traitement (« parce qu’elles changent le traitement ») et le tableau ne classe pas les entités par gravité. Retirer la promesse ou classer la liste change le fond.
- **R-16** (cohérence arithmétique, G91_b.html) : « 92 % des 16 opérés en ont une à 6 semaines ». 92 % de 16 n’est pas un nombre entier (14,7) ; 15 sur 16 donne 93,75 %, 12 sur 13 donne 92,3 %. Soit le pourcentage, soit l’effectif est inexact (la fenêtre associée reprend « 92 % … chez 16 opérés »). À vérifier dans la source.
- **R-20** (force de la recommandation, G91_b.html) : « La recommandation européenne souhaite des centres ». « Souhaite » ne correspond à aucun degré de recommandation usuel (recommande, suggère, propose) ; le choix du verbe dépend du libellé de la recommandation.
- **R-22** (ambiguïté de fond, G91_c.html) : « ces volumes ne diffèrent pas ». La phrase dit que les volumes (30 mL, 50 mL) ne diffèrent pas, ce qui est faux littéralement ; la source (fenêtre : « sans différence entre les deux volumes ») ne précise pas sur quoi porte l’absence de différence (réponse clinique, valeur prédictive). Toute reformulation ajoute un fait.
- **R-23** (mesure d’incertitude, G91_c.html) : « sa spécificité de 75 % (33–100) ». Les parenthèses « (26–87) » et « (33–100) » ne précisent pas leur nature (intervalle de confiance, étendue des études). La nature de ces bornes est un fait de source.
- **R-24** (exclusivité, G91_c.html) : « accessible à l’ETV ». L’encadré attribue l’ETV à la forme obstructive et la dérivation à la forme communicante, alors que la partie 9 fait de la dérivation ventriculo-péritonéale le pilier du traitement de l’enfant dans les deux formes. « Accessible à » est de plus un calque. La correction suppose de trancher la portée clinique.
- **R-26** (critère omis, G91_c.html) : « Réponse B. DESH avec trouble typique de la marche et pression ≤ 200 mmH2O font une iNPH probable ». Les critères de l’iNPH probable exigent aussi un « contenu normal » du LCS (parties 6 et 13) ; l’énoncé du cas et la correction ne le mentionnent pas. Ajouter ce critère modifie le cas.
- **R-27** (référence interne, G91_pop1.html) : « Données issues d’un résumé (S11) ». « S11 » est un identifiant interne de source, sans signification pour le lecteur. Le remplacer exige de retrouver la référence bibliographique exacte.

## Constats transmis à l'audit MED

- **H-01** (MAJEUR (transmis à l’audit MED), G91_c.html) : L’onglet Sciences compte 4 sous-onglets (data-s : Anatomie, Histologie, Physiologie, Biochimie) ; le sous-onglet « Sémiologie fondamentale et analytique » est absent, ainsi que la discipline génétique ou microbiologie prévue par le guide (§ 6).
- **H-02** (réserve (transmis à l’audit MED), G91_a.html ; G91_c.html) : Les cinq figures sont des schémas SVG dessinés ; leur provenance n’a pas été vérifiée par ce rôle (voir clé figures).
- **Figures** : la Figure 2 (voies du LCS et sites d'obstacle, SVG dessiné) est classée ORIGINE_INCONNUE, en réserve. Les Figures 1, 3, 4 et 5 sont des schémas conceptuels d'après leur légende, non évalués. Le contrôle a porté sur le texte des figures, pas sur leur provenance.
- Aucune proposition n'affaiblit une obligation clinique.

## Choix différés

- Espaces insécables : non appliquées, ni proposées. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F. Relevé pour la décision globale : 436 espaces simples avant « ; : ? ! » dans le texte visible, 46 guillemets « » sans insécable intérieure, 184 occurrences « nombre % » sans insécable. Une application mécanique par le moteur est préférable à des propositions locales.
- Choix « tap test » / « test de soustraction de LCS » : non tranché ; une équivalence est posée à la première occurrence du terme (P-23), le reste du cours conserve les deux termes.

## Observations

- Vocabulaire de fabrication et de provenance : « dossier » (16 occurrences), « lu », « lue », « lues », « lus » (35 occurrences) et, dans l’en-tête de la leçon, « Cycle Betta 40 … audit différé » décrivent la fabrication du cours, ce que le guide de rédaction (§ 3) proscrit ; ils portent aussi les mentions de lacune exigées par la règle de vérité. Le retrait ou la reformulation est un choix éditorial pour l’intégrateur ; seules les occurrences personnifiant le chapitre (« Ce chapitre apprend », « Il nomme ») et le terme « îlot » ont fait l’objet de propositions.
- Objectifs de la partie 0 : cinq infinitifs injonctifs (« Définir… », « Distinguer… », « Poser… », « Reconnaître… », « Choisir… ») que le guide de rédaction (§ 2) proscrit ; non reformulés, car un objectif pédagogique à l’infinitif est un usage établi et sa réécriture relèverait d’un choix de conception de la leçon (sauf le zeugme de l’objectif 5, proposé).
- Répétitions entre parties : la phrase sur les ponctions lombaires répétées, l’acétazolamide et les fibrinolytiques apparaît quatre fois (partie 9 ×2, tableau p-1, partie p-4) ; le suivi lausannois à 6 semaines, 6 et 12 mois figure dans les parties 8 et 11 ; la dysfonction par obstruction proximale dans les parties 7 et 10 ; la supplémentation en folates dans les parties 4 et 11. Seule la redite immédiate de la partie 9 a fait l’objet d’une proposition ; les autres relèvent de la structure du cours.
- Le bouton Pareto « Anamnèse et examen » est placé à la fin de la partie 5 mais sa fenêtre couvre aussi la partie 6 (data-cover g91-5,g91-6) ; la position du bouton relève de la structure.
- Partie e-2 : le paragraphe commence par l’étiquette « Normal avant pathologique. », qui reprend une règle d’écriture du guide, puis précise que le dossier ne donne pas de valeur normale de l’index d’Evans ; l’étiquette est sans objet pour le lecteur.
- Nombres : « 6000 », « 1500 g », « 1605 », « 1524 », « 1000 » sont écrits sans espace, « 100 000 » et « 13 000 € » avec espace ; l’harmonisation dépend du choix différé sur les espaces insécables.
- Notation chimique et unités : « mmH2O », « cmH2O », « HCO3- », « Na+/K+-ATPase » sont écrits sans indice ni exposant ; les clés du glossaire reposent sur ces graphies, qu’un changement de balisage casserait. Non proposé.
- HTML : 10 caractères « < » non échappés dans le texte courant (G91_a ×1, G91_b ×3, G91_c ×3, G91_pop1 ×2, G91_pop2 ×1) et 5 « > » ; ils sont tolérés par l’analyseur tant qu’ils sont suivis d’un espace ou d’un chiffre, mais « &lt; » et « &gt; » sont attendus. Relève de l’intégrateur.
- Anglicismes conservés : « freezing » (G91_a ×2, G91_pop1 ×1), « board » (parcours lausannois), « Timed Up and Go », « tap test » (employé 16 fois avec « test de soustraction » ; équivalence posée à la première occurrence par la proposition P-23), « double tâche ». Le choix d’un terme unique est éditorial.
- Glossaire : la clé CT devient inutilisée dans le texte si la proposition sur « Imagerie (CT, CT de perfusion) » est appliquée ; neuf définitions de codes répètent « Code CIM-10-GM 2024. » sans plus ; plusieurs définitions sont des phrases nominales (« Test cognitif global. », « Mesure d’efficience. ») ; acceptables pour un glossaire, non modifiées.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire, aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Le manifeste porte base_sha 523832d9 alors que la consigne et la branche reposent sur 103745ba ; les empreintes des sept fichiers sont conformes au manifeste, donc les sources figées sont identiques.
- Heure de début non relevée au démarrage de l’audit : date_debut est laissé à null plutôt que d’être estimé.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 sur 7 |
| Empreintes conformes | oui |
| Propositions | 89 |
| Propositions à ancien unique | 89 sur 89 |
| Renvois médicaux | 27 |
| Choix différés | 2 |
| Abréviations non couvertes après application | 0 |
| Source canonique modifiée | non |

Horodatage : date_debut non relevé (null) ; date_fin 2026-10-16T09:27:47Z relevée par date -u avant le commit.
