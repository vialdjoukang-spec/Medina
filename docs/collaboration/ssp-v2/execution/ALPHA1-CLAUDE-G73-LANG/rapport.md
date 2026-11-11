# Audit linguistique G73 — Affections musculaires et neuromusculaires au cours de maladies classées ailleurs (S08)

Mission ALPHA1-CLAUDE-G73-LANG, tour 1, génération 1. Branche `claude/alpha1/g73-lang-g1`, base `103745ba` (la base du manifeste, `523832d9`, donne des sources identiques : `git diff` vide sur les sept fichiers). Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le français est globalement clair et sobre. Les défauts relevés tiennent à :

- **la terminologie de fabrication** : « le dossier » (32 occurrences sur 33) désigne la documentation lue de fabrication, non le patient ; le lecteur lit un cours ;
- **des constructions elliptiques ou ambiguës** : « que non tumorales » (4 occurrences), « aux premiers », « la faiblesse est musculaire » (dans un cours qui oppose jonction et muscle), « un petit cancer du poumon » pour le carcinome à petites cellules ;
- **des connecteurs sans prémisse** : « donc » après une phrase sans rapport, « inversement » qui n’oppose rien ;
- **des infinitifs injonctifs et des phrases nominales** dans les tableaux de conduite et les puces, que le guide de rédaction proscrit ;
- **des accords et articles** : « les créatine kinases », « mutation » sans article, « deuxième cas » sans article, « le plus important » accordé à « la tumeur ».

- **129 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; nombres et balises HTML identiques entre ancien et nouveau ; application simulée en mémoire suivie de `build_medina.audit()` : `{}` sur les six fichiers HTML.
- **20 renvois médicaux** : formulations dont la correction créerait ou retirerait une causalité, un chiffre ou une conduite. Ils ne sont pas corrigés ici.
- **1 constat hors périmètre** : mention de fabrication dans l’en-tête de la leçon.

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| registre | 31 |
| syntaxe | 19 |
| ambiguïté | 16 |
| style | 16 |
| grammaire | 13 |
| lexique | 12 |
| cohérence | 6 |
| terminologie | 6 |
| répétition | 4 |
| ponctuation | 4 |
| typographie | 2 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| `chapters/G73/G73_a.html` | 32 |
| `chapters/G73/G73_b.html` | 37 |
| `chapters/G73/G73_c.html` | 22 |
| `chapters/G73/G73_d.html` | 17 |
| `chapters/G73/G73_pop1.html` | 16 |
| `chapters/G73/G73_pop2.html` | 3 |
| `glossary/g73.py` | 2 |

## Renvois médicaux (hors correction linguistique)

Classés par ordre d’apparition. Chaque renvoi cite l’extrait exact de la leçon.

- **R-01** (chiffre/fréquence, `G73_a.html`) : « chez environ un patient sur deux ou sur trois, selon les séries ». Incohérence chiffrée : « un patient sur deux ou sur trois » (50 % ou 33 %) contredit le tableau juste au-dessus (50 à 60 % ; 51 %, soit 44 sur 87) et la fenêtre « CBPC ». Quelle fréquence écrire relève de la source (Lipka 2024, cohorte Leiden–Nottingham) : à trancher par l’audit médical.
- **R-02** (causalité, `G73_a.html`) : « ce qui rappelle que la forme non tumorale reste un terrain d’auto-immunité ». Le 38 % provient d’un registre de 38 patients SMLE sans distinction tumorale ou non ; la phrase l’impute à la forme non tumorale et en tire une conclusion (« terrain d’auto-immunité ») que le tableau ne porte pas. Retirer ou sourcer = changement de fond.
- **R-03** (causalité, `G73_a.html`) : « ces signes se cherchent donc à l’interrogatoire ». Le connecteur « donc » tire de l’appartenance d’un seul signe (dysfonction érectile) au score DELTA-P une conduite d’interrogatoire pour tous les signes de dysautonomie ; le lien n’est pas établi par les sources. Supprimer « donc » ou sourcer la conduite relève du fond.
- **R-04** (causalité, `G73_a.html`) : « ce qui explique que les muscles oculaires et bulbaires soient touchés en dernier ». Explication circulaire : l’ordre d’atteinte (membres inférieurs d’abord) est présenté comme la cause de l’atteinte tardive des muscles oculaires et bulbaires. Aucun mécanisme n’est donné ; reformulation = changement de fond.
- **R-05** (causalité/conduite, `G73_a.html`) : « Le médecin signale donc au patient qu’une aggravation initiale est possible avant l’amélioration. ». Conduite d’information déduite (« donc ») d’un cas pédiatrique unique ; généralisation à tout patient adulte ou enfant non établie par la source (Onishi 2025). À confirmer, nuancer ou retirer par l’audit médical.
- **R-06** (ambiguïté de portée, `G73_a.html`) : « dont 87 % dans la Région européenne de l’Organisation mondiale de la santé ». Le pourcentage peut porter sur les 65 818 cas, sur les 42 décès ou sur les deux ; la fenêtre g73-trichinellose répète la même ambiguïté. Préciser « des cas » exige de relire Murrell et Pozio 2011 : à trancher par l’audit médical.
- **R-07** (causalité/évolution, `G73_a.html`) : « elle s’accompagne d’une guérison complète et spontanée dans toute la série ». « Spontanée » est absent du résumé de la série et contredit la prudence de la fenêtre g73-myosite-enfant (« aucun traitement spécifique n’est décrit »). L’absence de traitement décrit n’établit pas une guérison spontanée ; les paramètres clés de la partie 14 répètent « guérison spontanée ».
- **R-08** (structure du tableau, `G73_a.html`) : `<tr><td>Zone active</td>`. La première colonne s’intitule « Forme » (paranéoplasique, non tumorale), mais la troisième ligne, « Zone active », n’est pas une forme de la maladie : le tableau mêle deux axes. Corriger l’en-tête ou la ligne change la classification présentée.
- **R-09** (causalité, `G73_a.html`) : « il impose une conséquence pratique ». Un cas isolé « impose » une conséquence pratique (élargir le bilan tumoral) alors que la phrase précédente affirme qu’un cas isolé ne fixe ni fréquence ni règle. La prescription de conduite tirée de deux observations est une affirmation médicale, non une question de langue.
- **R-10** (chiffre/seuil, `G73_b.html`) : « (PAMC de repos bas avec incrément supérieur à 60 %) ». Le seuil d’incrément est écrit « supérieur à 60 % » ici et dans l’alerte de la partie 14, « ≥ 60 % » dans les paramètres clés de la même partie, « Au moins 60 % » dans la figure de l’onglet Sciences et « supérieur à 60 % » dans la fenêtre g73-increment. L’exclusion ou l’inclusion de 60 % exacte relève de la source (Lipka 2020) : à trancher par l’audit médical.
- **R-11** (conduite, `G73_d.html`) : « l’une demande de réduire le médicament, l’autre de le renforcer ». Incohérence avec la partie 11 de l’onglet Pathologie (« Surdosage : arrêter et assurer le soutien respiratoire ») et la fenêtre g73-mestinon : « réduire » et « arrêter » sont deux conduites différentes pour la crise cholinergique ; « renforcer le traitement » n’est pas non plus précisé (dose, voie). À trancher d’après l’information professionnelle suisse.
- **R-12** (ambiguïté de portée, `G73_d.html`) : « Les anticholinergiques réduisent l’effet des deux substances. ». « Les deux substances » n’a pas d’antécédent dans le paragraphe, qui ne cite que l’amifampridine ; la pyridostigmine et d’autres molécules sont citées ailleurs. La fenêtre g73-firdapse-ci répète la formule. Désigner les substances exige de relire l’information professionnelle suisse de Firdapse® : à trancher par l’audit médical.
- **R-13** (provenance des sources, `G73_d.html`) : « Le score DELTA-P n’est pas lu dans son article original ». Incohérence interne : la fenêtre g73-lacunes affirme que le texte intégral de « la cohorte DELTA-P » (Maddison 2020) a été lu, la fenêtre g73-deltap que « l’article original n’a pas été lu », et l’onglet Pathologie cite Maddison 2020 comme source du score. La portée exacte de la lecture est à clarifier par l’audit médical.
- **R-14** (mention de fabrication, `G73_d.html`) : « (le quota de recherche était épuisé) ». La parenthèse expose une contrainte de production (quota) au lecteur ; la retirer supprime la justification de la lacune, la remplacer suppose de décider ce qu’on dit au lecteur. Décision de gouvernance, non de langue.
- **R-15** (précision numérique, `G73_b.html`) : « (médiane de 17 contre 7,0 mois) ». Les deux médianes n’ont pas la même précision (17 contre 7,0) ; aligner les décimales (17,0 ou 7) suppose de connaître la valeur de la source (Lipka 2019).
- **R-16** (phrases nominales dans une fenêtre de posologie, `G73_pop2.html`) : `<p>Dose de départ de 15 mg par jour en 3 ou 4 prises avec les repas.`. La fenêtre « Firdapse® : posologie » enchaîne des phrases nominales (« Dose de départ… », « Augmentation par paliers… », « Dose unique… »), contraires au guide de rédaction. Les réécrire en phrases complètes touche des doses, des intervalles et des plafonds : non proposé par ce rôle.
- **R-17** (ambiguïté de portée, `G73_b.html`) : « tabagisme au début ». « Au début » se rattache à la maladie ou au suivi : l’item du score porte sur le tabagisme à l’apparition des symptômes ou au diagnostic. La précision dépend de Maddison 2020.
- **R-18** (causalité, `G73_c.html`) : « Comme le diagnostic final combine la clinique et l’électrophysiologie, les auteurs recommandent le seuil de 60 %. ». Le connecteur « comme » donne la combinaison clinique-électrophysiologie pour raison de la recommandation de 60 % ; le résumé de l’étude de Leiden fonde plutôt la recommandation sur le gain de sensibilité. À confirmer par l’audit médical.
- **R-19** (chronologie, `G73_c.html`) : « Avec l’ancien seuil de 100 % ». « Ancien » affirme que 100 % était le seuil antérieurement en usage ; les sources lues ne le précisent pas.
- **R-20** (qualificatif, `G73_b.html`) : « Le risque est faible mais non nul ». « Faible » pour un risque de 18,8 % (score 1) est une appréciation clinique qui n’est pas dans les sources ; la fenêtre g73-deltap donne seulement le pourcentage.

## Constat hors périmètre

- **H-01** (`G73_a.html`) : Mention de fabrication dans l’en-tête visible : « cycle Betta 39 » et « audit différé ». Relève de la gouvernance du cours (statut), non d’une correction de langue ; non proposé.

## Propositions les plus utiles

- **P-008** (`G73_a.html`) : « Premièrement, la faiblesse est musculaire, parce que » devient « Premièrement, une faiblesse musculaire apparaît, parce que ». Ambiguïté dans un cours qui distingue jonction et muscle : « la faiblesse est musculaire » peut se lire comme une atteinte du muscle lui-même.
- **P-014** (`G73_a.html`) : « Inversement, ils sont aussi fréquents dans les formes paranéoplasiques que non tumorales ; leur présence ne dit pas » devient « De plus, ils sont aussi fréquents dans les formes paranéoplasiques que dans les formes non tumorales ; leur présence ne dit pas ». Connecteur inadapté (« inversement » n’oppose rien à la phrase précédente, il ajoute un argument) et comparatif elliptique (« que non tumorales »).
- **P-020** (`G73_a.html`) : « la recherche d’un petit cancer du poumon chez un fumeur » devient « la recherche d’un carcinome bronchique à petites cellules chez un fumeur ». Ambiguïté : « petit cancer » évoque une tumeur de petite taille, alors que la phrase vise le carcinome bronchique à petites cellules.
- **P-026** (`G73_a.html`) : « Les créatine kinases sont normales ou peu élevées. » devient « La créatine kinase est normale ou peu élevée. ». Grammaire : « créatine kinase » est un nom d’enzyme invariable au singulier (« la CK »), comme dans le reste du cours.
- **P-035** (`G73_b.html`) : `<td>Ne pas appliquer le traitement du SMLE à la myasthénie</td>` devient `<td>Le médecin n’applique pas le traitement du SMLE à la myasthénie</td>`. Style de rédaction : l’infinitif injonctif est proscrit, y compris dans les tableaux.
- **P-043** (`G73_b.html`) : « garde une aire de 84,5 % » devient « présente une aire de 84,5 % ». Lexique : « garde » suggère un maintien alors que 84,5 % dépasse 82,5 % ; « présente » est neutre.
- **P-057** (`G73_b.html`) : `distinguer la <b>crise cholinergique</b> du surdosage de la crise myasthénique.` devient `distinguer la <b>crise cholinergique</b>, due à un surdosage, de la crise myasthénique.`. Ambiguïté de la préposition : « la crise cholinergique du surdosage de la crise myasthénique » enchaîne deux compléments ; les virgules lèvent le doute (formulation du tableau : « par surdosage »).
- **P-059** (`G73_b.html`) : « n’est pas efficace en ajout à la pyridostigmine dans la myasthénie » devient « n’est pas efficace en complément de la pyridostigmine dans la myasthénie ». Anglicisme : « add-on » se rend par « en complément de ».
- **P-074** (`G73_c.html`) : « Un résultat SOX1 obtenu par line-blot commercial s’interprète donc avec réserve. » devient « Par ailleurs, un résultat SOX1 obtenu par line-blot commercial s’interprète avec réserve. ». Connecteur « donc » : la phrase précédente porte sur la méthode de détection des anti-VGCC et n’est pas la prémisse de la réserve sur SOX1 ; « par ailleurs » signale une idée ajoutée.
- **P-076** (`G73_c.html`) : « le CBPC apparaît dans les six mois chez 91 % » devient « le CBPC est découvert dans les six mois chez 91 % ». Cohérence avec la section 10.3 et la fenêtre « CBPC » : le délai porte sur la découverte, non sur l’apparition de la tumeur.
- **P-083** (`G73_c.html`) : « Contraction : SMLE au premier maillon » devient « Contraction de la fibre (lésion d’une myopathie) ». Incohérence d’étiquette de figure : le dernier maillon est celui de la myopathie ; la légende dit déjà que le SMLE atteint le premier maillon.
- **P-113** (`G73_pop1.html`) : « garde une aire de 84,5 % » devient « présente une aire de 84,5 % ». Lexique : « garde » suggère un maintien alors que 84,5 % dépasse 82,5 % ; « présente » est neutre.
- **P-116** (`G73_pop1.html`) : « un adénocarcinome pulmonaire mutant EGFR ont été rapportés » devient « un adénocarcinome pulmonaire porteur d’une mutation d’EGFR ont été rapportés ». Anglicisme (« EGFR-mutant ») : la tournure française emploie « porteur d’une mutation ».
- **P-123** (`G73_pop1.html`) : « n’est pas efficace en ajout à la pyridostigmine dans la myasthénie » devient « n’est pas efficace en complément de la pyridostigmine dans la myasthénie ». Anglicisme : « add-on » se rend par « en complément de ».
- **P-128** (`g73.py`) : « ('Care','nom du score, non développé dans le dossier lu') » devient « ('Care','nom des critères, non développé dans les sources lues') ». Cohérence : PNS-Care désigne des critères (entrée « Critères PNS-Care 2021 »), non un score ; registre de « dossier ».

## Figures

Texte des figures (étiquettes SVG et légendes) lu ; la provenance n’est pas évaluée par ce rôle.

- Figure « Chaîne de la transmission neuromusculaire » (G73_c.html, Physiologie) : schéma didactique non anatomique (cinq cases et flèches, SVG). aucune figure anatomique dessinée ; légende explicite (« Schéma didactique original, non à l’échelle ; ce n’est pas une image clinique »). Étiquette finale incohérente avec la légende (proposition P-083).
- Figure « Principe du calcul de l’incrément » (G73_c.html, Électrophysiologie) : schéma didactique non anatomique (quatre cases, SVG). aucune figure anatomique ; légende explicite. Texte de la dernière case (« Au moins 60 % ») : voir R-10.
- Figure « Myopathie cortisonique » (G73_c.html, Biochimie du muscle) : schéma didactique non anatomique (quatre cases, SVG). aucune figure anatomique ; légende explicite. Aucune proposition : libellés « Synthèse basse / dégradation haute » conservés, une reformulation plus longue risquerait de dépasser la largeur de la case.

## Choix différés, non appliqués

- Espaces insécables avant ; : ? et %, dans les guillemets « » et dans les grands nombres : non proposées, car aucun U+00A0 ni U+202F n’existe dans les sept fichiers. Occurrences à traiter par un passage mécanique commun : environ 167 pour « % », 254 pour « ; », 203 pour « : », 17 pour « ? », 8 paires de guillemets (hors balises). Il en est de même pour « 6 106 » et « 65 818 » (grands nombres avec espace sécable).
- Variantes lexicales intentionnelles non touchées : « paralysie périodique thyréotoxique » / « paralysie périodique hypokaliémique thyréotoxique » ; « pilier » et « levier » (métaphores mortes).
- Phrases nominales en cellules de tableau et en puces de fenêtres : seules celles des tableaux de conduite (infinitifs injonctifs) et des puces de la partie p-5 ont fait l’objet de propositions ; les cellules de comparaison (Examens, Sciences) restent brèves, comme l’autorise le guide.

## Observations

- Terminologie de production : le mot « dossier » (documentation lue) apparaît 33 fois dans les sept fichiers ; 32 occurrences ont reçu une proposition (« les sources lues », « ce cours »). La 33e (« aucun dossier réel », dossier de patient) est un emploi correct et n’est pas touchée.
- Cohérence interne vérifiée : exemples chiffrés recalculés (incrément (3,6−2,0)÷2,0×100 = 80 % ; (2,7−1,5)÷1,5×100 = 80 % ; (4,5−2,5)÷2,5×100 = 80 % ; 100−58,7 = 41,3 % de malades échappant au seuil de 100 %) : arithmétique exacte. Aucune vérification médicale des valeurs n’a été faite par ce rôle.
- Tableau de la partie 10.3 : l’ordre des lignes (DELTA-P 3 à 6, puis 0 à 1, puis 2) n’est pas croissant et le sous-titre 10.3 précède directement le tableau sans phrase d’introduction ; relève de la structure, non proposé.
- Tableau du 3.2 : la ligne « Zone active » ne correspond pas à l’en-tête « Forme » (voir R-08).
- Onglet Pharmacologie, partie p-2 : le paragraphe sur les précautions compte neuf phrases, au-delà des trois à six phrases du guide ; une scission est possible mais n’est pas une correction locale.

## Vérification mécanique

- Méthode : script Python : ancien.count(fichier) == 1 pour chacune des 129 propositions ; absence de chevauchement entre propositions d’un même fichier ; identité des nombres et des balises entre ancien et nouveau ; application simulée en mémoire de toutes les propositions, comparaison du comptage des balises HTML avant/après, puis build_medina.audit() sur les six fichiers HTML ; contrôle syntaxique (ast.parse) du glossaire modifié.
- Résultat : toutes les propositions sont uniques (True), sans chevauchement (True), nombres et balises identiques, audit des abréviations avant et après application : `{}`.
- Glossaire : modifications limitées à deux chaînes de g73.py (entrées PNS-Care et CK) ; syntaxe Python valide ; aucune clé ajoutée ou retirée ; chargement complet du glossaire non rejoué sur la copie modifiée (le chargeur importe 187 modules et a dépassé le délai imparti), seule la syntaxe est garantie.

## Lacunes

- Aucune vérification médicale n’a été faite : les renvois_medicaux signalent des formulations dont la correction changerait le fond ; ils ne sont ni confirmés ni infirmés.
- Aucun contrôle de rendu navigateur des propositions : l’application simulée a été faite en mémoire, aucun fichier canonique n’est modifié.
- Aucune lecture des sources primaires citées : les écarts avec les sources sont établis seulement par comparaison interne entre les sept fichiers de la leçon.
- Aucun correcteur orthographique automatique disponible dans l’environnement : l’orthographe et la grammaire reposent sur la lecture intégrale des textes et des contrôles par expressions régulières (espaces avant ponctuation, virgules, apostrophes, répétitions de mots).
- Le chargement complet du glossaire modifié n’a pas pu être rejoué (délai dépassé) ; seule la validité syntaxique de g73.py est établie.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus | 7 / 7 (empreintes conformes) |
| Propositions locales | 129 |
| Renvois médicaux | 20 |
| Hors périmètre | 1 |
| Audit des abréviations après application | `{}` (6 / 6 fichiers HTML) |
| Source canonique modifiée | aucune |

---
Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée
