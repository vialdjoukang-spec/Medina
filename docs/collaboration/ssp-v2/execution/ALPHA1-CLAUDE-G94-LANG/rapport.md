# Audit linguistique G94 — Autres affections du cerveau au cours de maladies classées ailleurs (S08)

Mission ALPHA1-CLAUDE-G94-LANG, tour 1, génération 1. Branche `claude/alpha1/g94-lang-g1`, base du worktree `103745ba` (base du manifeste `523832d9` ; sources figées identiques, empreintes conformes). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le texte est globalement correct sur le plan orthographique (aucune coquille repérée) : les défauts tiennent surtout à trois familles. D'abord, des phrases nominales ou à l'infinitif là où le guide de rédaction exige des phrases complètes : les encadrés « Piège » et « Erreur fréquente », les épilogues « À retenir », une grande partie des lignes des fenêtres et des puces des Pareto. Ensuite, des formules de chantier (« dossier de sources », « dépôt », « la leçon ne les invente pas », « aucune dose n'est inventée »). Enfin, quelques constructions fautives ou ambiguës : « la sédation évite le midazolam », « un coma inexpliqué par occlusion basilaire », « ne confirme et n'exclut rien », « l'énolase supérieure à 24,15 µg/L », un intitulé amputé du mot « Autres ».

- **123 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement, aucun nombre modifié ; application simulée en mémoire suivie de `build_medina.audit()` : aucune abréviation non couverte (résultat `{}` avant et après), glossaire compilable.
- **21 renvois médicaux** : formulations dont la correction créerait ou retirerait un fait, un dénominateur, une causalité ou un choix de classification. Ils ne sont pas corrigés ici.
- **Choix différés, non appliqués** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers) ; harmonisation « liquide cérébrospinal » / « liquide céphalo-rachidien » ; harmonisation des mesures (« odds ratio », « hazard ratio », « rapport de risque »).

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| phrase_nominale | 62 |
| registre | 20 |
| syntaxe | 14 |
| ambiguité | 10 |
| grammaire | 6 |
| calque | 6 |
| intitulé | 2 |
| cohérence | 2 |
| répétition | 1 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| chapters/G94/G94_a.html | 22 |
| chapters/G94/G94_b.html | 22 |
| chapters/G94/G94_c.html | 15 |
| chapters/G94/G94_d.html | 7 |
| chapters/G94/G94_pop1.html | 19 |
| chapters/G94/G94_pop2.html | 37 |
| glossary/g94.py | 1 |

## Propositions les plus utiles

- **P-001** (G94_a.html) : « Neurologie · Affections du cerveau au cours de maladies classées ailleurs</div> » devient « Neurologie · Autres affections du cerveau au cours de maladies classées ailleurs</div> ». Même intitulé que le catalogue et la fenêtre g94-cim (mot « Autres » omis dans le bandeau).
- **P-031** (G94_b.html) : « La sédation évite le midazolam ; la dexmédétomidine n’a pas réduit délire ou coma par rapport à la sédation standard dans deux essais random » devient « Pour la sédation, le médecin évite le midazolam ; dans deux essais randomisés, la dexmédétomidine n’a réduit ni le délire ni le coma par rapport à la sédation s ». Personnification absurde (« la sédation évite ») et négation mal construite : « n’a pas réduit délire ou coma » doit se dire « n’a réduit ni le délire ni le coma ».
- **P-028** (G94_b.html) : « (2) un coma inexpliqué par <button » devient « (2) un coma inexpliqué, qui doit faire évoquer une <button ». Contresens apparent : « inexpliqué par occlusion basilaire » se lit « non expliqué par l’occlusion » ; le sens voulu est celui de la carte clinique (« doit faire penser à une occlusion de l’artère basilaire »).
- **P-048** (G94_c.html) : « elle ne confirme et n’exclut rien. » devient « elle ne permet ni de confirmer ni d’exclure le diagnostic. ». Négation mal coordonnée : « ne confirme et n’exclut rien » ; la coordination négative attendue est « ni … ni ».
- **P-058** (G94_c.html) : « L’énolase neurone-spécifique supérieure à 24,15 µg/L donne » devient « Un taux d’énolase neurone-spécifique supérieur à 24,15 µg/L donne ». Ce n’est pas l’enzyme qui est « supérieure à 24,15 µg/L » mais son taux sanguin.
- **P-021** (G94_a.html) : « Piège</span> Examiner un patient sédaté. Les sédatifs confondent l’évaluation clinique » devient « Piège</span> On tombe dans ce piège en interprétant l’examen d’un patient sédaté sans tenir compte de la sédation. Les sédatifs brouillent l’évaluation clinique ». Deux défauts : l’infinitif « Examiner un patient sédaté » énonce un conseil absurde au lieu de l’erreur (interpréter sans tenir compte de la sédation, ce que la phrase suivante explique) ; « confondre » est un calque de « confound » (les sédatifs brouillent ou faussent, ils ne confondent pas).
- **P-095** (G94_pop2.html) : « <div class="lab">Qui y penser</div><p>Tout patient avec un cancer du sein, du poumon ou un mélanome présentant des symptômes neurologiques » devient « <div class="lab">Chez qui y penser</div><p>Il faut y penser chez tout patient ayant un cancer du sein, du poumon ou un mélanome et présentant des symptômes neur ». Intitulé agrammatical (« Qui y penser ») et phrase nominale sans verbe.
- **P-006** (G94_a.html) : « c’est la présence du sepsis qui bascule vers la seconde. » devient « c’est la présence du sepsis qui fait basculer le diagnostic vers la seconde. ». « Basculer » est intransitif : « la présence du sepsis bascule » est fautif ; il faut « fait basculer » avec son complément.
- **P-030** (G94_b.html) : « contrôler le retentissement cérébral et prévenir les agents qui l’aggravent » devient « contrôler le retentissement cérébral et éviter les agents qui l’aggravent ». « Prévenir » ne se construit pas avec un agent causal à éviter ; on évite un médicament.
- **P-017** (G94_a.html) : « Cancer connu, surtout du sein, du poumon ou mélanome (<button class="w" data-k="g94-ml">signes d’alerte des métastases leptoméningées</butto » devient « Le médecin recherche un cancer connu, surtout du sein ou du poumon, ou un mélanome (<button class="w" data-k="g94-ml">signes d’alerte des métastases leptoméning ». Énumération de mots-clés sans verbe (proscrite, guide § 2) et parallélisme fautif « du sein, du poumon ou mélanome » (deux compléments de nom puis un nom nu).
- **P-040** (G94_b.html) : « C’est le facteur principal de neurotoxicité du céfépime, avec un délai médian de quatre jours : confusion (93 %), myoclonies (37 %), crises  » devient « C’est le facteur principal de neurotoxicité du céfépime. Celle-ci apparaît après un délai médian de quatre jours et se manifeste par une confusion (93 %), des m ». Rattachement ambigu : le délai médian de quatre jours et la liste de signes se lisent comme des attributs de l’insuffisance rénale alors qu’ils décrivent la neurotoxicité.
- **P-009** (G94_a.html) : « 5 % (26 épisodes sur 577) ; 69 % déjà présente à l’admission » devient « 5 % (26 épisodes sur 577) ; déjà présente à l’admission dans 69 % des cas ». Accord et antécédent : « 69 % déjà présente » ne dit pas ce que désigne le pourcentage (les hydrocéphalies) ; la formule « dans 69 % des cas » lève l’ambiguïté.

## Renvois médicaux (hors correction linguistique)

Classés par type de risque pour le fond. Chaque renvoi cite l'extrait exact de la leçon.

- **R-01** (unité, G94_a.html) : « Incidence d’environ 9 pour 100 000 ». Une incidence sans période est inexploitable (par an ?). La fenêtre g94-hsa (G94_pop2) répète la même formulation. Ajouter « par an » est un ajout de fait : à vérifier dans l’article de l’European Stroke Organization (2013).
- **R-02** (terminologie / classification, G94_a.html) : « Encéphalopathie métabolique ». Le troisième pôle est nommé « métabolique » dans le tableau du § 1 (et dans G94.30 « maladies endocriniennes et métaboliques »), mais « carentielle » dans les objectifs du § 0 et dans le Pareto, tandis que la seule entité traitée est l’encéphalopathie de Wernicke (carence en thiamine) ; la fenêtre g94-cim précise que le code croix de la carence (E51) n’est pas vérifié. Le choix du nom du pôle relève de la classification : à trancher par l’audit médical.
- **R-03** (force de la recommandation, G94_a.html) : « et sa présence interdit le traitement intrathécal ». La source rapportée dans G94_pop2 (g94-flux) dit que le traitement intrathécal « n’est pas approprié » en présence d’un blocage ; « interdit » est plus fort. Choisir entre « déconseille », « n’est pas approprié » et « interdit » modifie la portée de la recommandation.
- **R-04** (terminologie / périmètre, G94_a.html) : « pas seulement chez l’alcoolique ». « L’alcoolique » (ici, § 6, § 12, cas 4 et fenêtres) est la formule de la recommandation EFNS 2010 ; la terminologie actuelle privilégie « patient présentant un trouble de l’usage de l’alcool ». Changer le terme modifie le périmètre des critères « deux signes sur quatre », définis chez l’alcoolique : à décider par l’audit médical.
- **R-05** (causalité / chronologie, G94_a.html) : « une carence se constitue donc en quelques semaines ». Le « donc » déduit un délai d’installation de la demi-vie (10 à 20 jours) ; la fenêtre g94-thiamine-meca ne donne que la demi-vie. L’inférence n’est pas dans la source Benerva citée.
- **R-06** (dénominateur, G94_b.html) : « 15 % des patients ont reçu une dérivation externe et 8 % des ponctions lombaires répétées ». Le tableau place ces pourcentages dans « la méningite bactérienne » et le lecteur les rapporte aux 577 épisodes. Les fenêtres (G94_pop2, g94-meningite-hydro) donnent 4 patients (15 %) et 2 patients (8 %) : les dénominateurs sont les 26 hydrocéphalies (4/26 = 15,4 % ; 2/26 = 7,7 %). Le dénominateur doit être explicité, ce qui ajoute une donnée.
- **R-07** (causalité non sourcée, G94_b.html) : « les patients dérivés étaient les plus graves ». La fenêtre g94-meningite-hydro ne cite que « effectifs minimes et biais d’indication » ; l’affirmation que les patients dérivés étaient les plus graves n’y figure pas. À confirmer dans la source (résumé seul lu) ou à retirer.
- **R-08** (cohérence terminologique, G94_b.html) : « la reprise chirurgicale (8 %) ». La fenêtre g94-dvp (G94_pop2) donne « externalisation, retrait ou révision 8 % » ; « reprise chirurgicale » est un autre périmètre. Choix du libellé à confirmer sur la source EANO-ESMO 2023.
- **R-09** (nature de la mesure, G94_pop1.html) : « pour un score de 3 à 8, le rapport de risque est de 3,37 ». La leçon emploie « rapport de risque » (ici), « odds ratio » (G94_a, G94_b, G94_c, G94_pop2), « hazard ratio » (g94-cibles) et « rapport de taux d’incidence ». Le type exact de mesure (risque relatif, rapport de risques instantanés) n’est pas précisé pour le score de Glasgow ; sa traduction française dépend de la source. À vérifier avant d’harmoniser.
- **R-10** (source non identifiée, G94_d.html) : « La recommandation sur les délires conseille d’éviter les agents neurotoxiques. ». Aucune « recommandation sur les délires » ne figure dans les références de G94_b ni dans les fenêtres ; la phrase attribue un conseil à une source non nommée. À sourcer ou retirer.
- **R-11** (cohérence de la conduite, G94_d.html) : « Préférer la voie orale lorsque c’est possible ». Pour la thiamine, la même phrase de la table p-3 préfère la voie orale, alors que l’encéphalopathie de Wernicke est traitée « de préférence par voie intraveineuse » (G94_b § 9, G94_d p-2). La portée du conseil (hors Wernicke ?) n’est pas dite ; à clarifier par l’audit médical.
- **R-12** (généralisation, G94_pop2.html) : « Dexaméthasone : effet après 1 à 2 heures, jamais seule. ». Le Pareto affirme « jamais seule » ; le texte (G94_b § 9, G94_d) limite la restriction à « l’œdème cérébral aigu menaçant ». Reformulation = changement de fond.
- **R-13** (incohérence, G94_c.html) : « une cellule vide signifie ». Le tableau e-4 ne contient aucune cellule vide ; la phrase de lecture décrit une situation absente. Retrait ou ajout de cellules « non lu » = changement de fond.
- **R-14** (causalité / force du terme, G94_c.html) : « la rupture de la première permet l’entrée de cellules immunitaires ». Le texte parle de « rupture » de la barrière, alors que le § 3 et les fenêtres disent « altération » ; de plus, « l’altération de la deuxième réduit l’adaptation du débit » et « celle de la troisième désorganise la communication » ne figurent pas dans les fenêtres (g94-sae-meca, g94-bhe). Mécanismes à sourcer ou à atténuer.
- **R-15** (causalité non sourcée, G94_c.html) : « reflètent l’hétérogénéité des populations et des définitions ». La fenêtre g94-imagerie-sae dit seulement « fourchettes larges selon les séries » ; l’explication par l’hétérogénéité des populations et des définitions est une interprétation de la leçon.
- **R-16** (notation isotopique, G94_c.html) : « ⁹⁹Tc-MAA ». Le technétium-99m s’écrit ⁹⁹ᵐTc ; « ⁹⁹Tc » désigne l’isotope 99 stable (non métastable), alors que le texte écrit ailleurs « technétium-99m-MAA ». La correction implique un caractère (ᵐ, U+1D50) dont la couverture dans la police du lecteur n’est pas vérifiée : décision partagée entre audit médical et intégration.
- **R-17** (vérifiabilité, G94_pop2.html) : « Une valeur de glucose du liquide paraît erronée dans la transcription de la source et n’est pas reprise. ». Remarque éditoriale non vérifiable par le lecteur : la valeur n’est pas donnée et la source n’est pas précisée. À reformuler par l’audit médical (soit donner la valeur vérifiée, soit supprimer la remarque).
- **R-18** (portée d’une inclusion, G94_pop1.html) : « bactérien, fongique, à protozoaires ou viral sans précision ». « Sans précision » peut qualifier « viral » seul ou chacun des quatre types (renvois A41.9, B48.80, B60.80, B34.80). Toute correction de ponctuation fixerait un sens de classification : à trancher sur le texte BfArM.
- **R-19** (intitulé, G94_b.html) : « Critères officiels et paramètres décisifs ». L’intitulé parle de critères « officiels » ; l’encadré réunit une définition tirée d’une revue narrative (encéphalopathie septique), un critère d’une recommandation EFNS de 2010 (Wernicke) et une classification EANO-ESMO. La fenêtre g94-mnemo précise « non critère officiel » pour les moyens mnémotechniques. Un intitulé exact est un choix de fond (« critères de référence » ?).
- **R-20** (fenêtre rattachée, g94.py) : « Protéine d’origine cérébrale mesurée dans le sang ». La clé S100B est rattachée à la fenêtre g94-eeg (électroencéphalogramme), qui ne traite pas ce marqueur sanguin ; la fenêtre adéquate n’existe pas. Rattachement à décider par l’intégration.
- **R-21** (terminologie suisse romande, G94_a.html) : « liquide cérébrospinal ». La leçon emploie partout « liquide cérébrospinal » (une trentaine d’occurrences, clé de glossaire comprise), alors que la terminologie francophone usuelle en Suisse romande est « liquide céphalo-rachidien (LCR) ». Choix global non appliqué ici : il touche le glossaire, les clés et chaque fichier (voir les choix différés).

## Figures

- Figure 2 (G94_c.html, régions cérébrales vulnérables et espaces du liquide) — classe : ORIGINE_INCONNUE ; statut : réserve. Seule figure anatomique dessinée (SVG : contour de tête, ventricules, tronc cérébral) ; sa légende la dit « schéma établi pour la leçon, non issu d'une source anatomique » et « non à l'échelle ». Provenance et exactitude topographique à vérifier par l'audit MED ; la règle des figures anatomiques d'origine IA s'applique. Défauts de forme : la légende numérotée figure deux fois (texte de la légende et liste ol), et un élément SVG vide (font-size 0) subsiste.
- Figures 1, 3, 4 (SVG de flux : séquence diagnostique, chaîne physiopathologique, thiamine et glucides) — classe : non évaluée par ce rôle (schémas non anatomiques d’après leur légende) ; statut : transmis à l’audit MED. Aucune provenance vérifiée. Forme : aucune des quatre figures n'est annoncée dans le texte ni suivie d'un paragraphe de lecture (guide de rédaction § 4).

## Observations et choix différés

- Structure (hors correction locale) : les quatre figures ne sont ni annoncées ni lues dans le texte, contrairement au § 4 du guide de rédaction ; la figure 2 répète sa légende dans une liste.
- Les « Pareto » (neuf fenêtres) restent des listes de mots-clés : les puces nominales ou à l’infinitif des neuf fenêtres sont réécrites en phrases (propositions P-114 à P-122), les puces déjà verbales sont conservées.
- Terminologie : « odds ratio », « hazard ratio » et « rapport de risque » coexistent ; « liquide cérébrospinal » est employé au lieu de « liquide céphalo-rachidien » (usage suisse romand) ; « résonance magnétique cérébrospinale » ; « glucose » et « glucide » alternent pour la règle de la thiamine (« avant tout glucide », « avant le glucose »). Aucune harmonisation proposée : elle touche aussi les clés de glossaire et relève d’un choix global (voir R-21 et R-09).
- Nombres : « 4200 kJ », « 1000 » sans espace, « 100 000 » avec espace ; « tous les deux mois pendant six mois » (chiffres en toutes lettres) et « toutes les 6 à 12 semaines » (chiffres) : convention numérique à fixer globalement.
- Les Pareto, tableaux et quiz utilisent des infinitifs et des groupes nominaux brefs dans les cellules (colonne « Erreur fréquente » du tableau e-2, options de quiz, tableaux de conduite) ; le guide les tolère dans les cellules à condition que le tableau soit introduit et lu. Aucune proposition sur ces cellules.
- **Différé** : Espaces insécables globales (avant ; : ! ?, dans les guillemets « », entre un nombre et « % » ou une unité) : non appliquées ni proposées une à une. Les sept fichiers ne contiennent aucun U+00A0 ni U+202F : la correction relève d'un traitement mécanique d'intégration (plusieurs centaines d'occurrences).
- **Différé** : Harmonisation « liquide cérébrospinal » / « liquide céphalo-rachidien » : non appliquée (voir R-21).

## Vérifications mécaniques

- Unicité : `ancien.count(fichier) == 1` pour les 123 propositions ; chevauchements : aucun.
- Application simulée en mémoire puis `build_medina.audit()` sur les six fichiers HTML : `{}` avant et après ; `compile()` du glossaire modifié : réussi.
- Nombres : l'ensemble des nombres de chaque `ancien` est identique à celui du `nouveau` (liste des écarts vide).

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire (texte uniquement) ; aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Aucun correcteur orthographique ou grammatical automatique n’était disponible dans l’environnement (ni aspell, ni hunspell, ni LanguageTool) : l’orthographe et la grammaire reposent sur la lecture intégrale des sept fichiers et sur un balayage des 665 mots à occurrence unique, sans coquille repérée.
- La couverture du caractère ᵐ (U+1D50) par la police du lecteur n’a pas été testée (voir R-16).

## Tableau de bord final

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes conformes au manifeste | oui |
| Propositions | 123 |
| Renvois médicaux | 21 |
| Fichiers canoniques modifiés | 0 |
| Abréviations non couvertes après application | 0 |

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
