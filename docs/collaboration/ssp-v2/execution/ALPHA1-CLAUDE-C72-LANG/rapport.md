# Audit linguistique agressif — C72 (fragment S08)

*Mission ALPHA1-CLAUDE-C72-LANG · branche `claude/alpha1/c72-lang-g1` · base 32416a20 · génération 1 · 2026-10-16T05:59Z*

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

La leçon C72 (tumeur maligne de la moelle épinière, des nerfs crâniens et d’autres parties du système nerveux central) a été relue en entier : quatre onglets, deux fichiers de fenêtres et le glossaire. Les sept empreintes SHA-256 sont conformes au manifeste. La relecture produit **87 propositions locales**, sans modification du fond, et **49 renvois médicaux** : ce sont des formulations qui créent une causalité, une fréquence ou une chronologie qu’aucune source lue n’établit. Ces dernières ne sont pas corrigées.

| Indicateur | Valeur |
|---|---|
| Propositions locales | 87 |
| Renvois médicaux | 49 |
| Choix différés de Vial (listés, non appliqués) | 2 |
| Catégorie « registre » | 27 |
| Catégorie « ambiguite » | 11 |
| Catégorie « phrase_nominale » | 10 |
| Catégorie « grammaire » | 9 |
| Catégorie « lourdeur » | 8 |
| Catégorie « syntaxe » | 6 |
| Catégorie « repetition » | 4 |
| Catégorie « coherence_terminologique » | 4 |
| Catégorie « accord » | 2 |
| Catégorie « infinitif_injonctif » | 2 |
| Catégorie « ponctuation » | 1 |
| Catégorie « parallelisme » | 1 |
| Catégorie « typographie » | 1 |
| Catégorie « abreviation » | 1 |

| Fichier | Propositions | Renvois |
|---|---|---|
| `chapters/C72/C72_a.html` | 18 | 16 |
| `chapters/C72/C72_b.html` | 23 | 10 |
| `chapters/C72/C72_c.html` | 17 | 12 |
| `chapters/C72/C72_d.html` | 10 | 3 |
| `chapters/C72/C72_pop1.html` | 7 | 3 |
| `chapters/C72/C72_pop2.html` | 11 | 4 |
| `glossary/c72.py` | 1 | 1 |

## Choix différés par Vial (non appliqués)

- **D1** — Espaces insécables avant « ; : ! ? » et dans « 12 mg », « 5 % », « 50 Gy », « 1,8 Gy », etc. : Aucune espace insécable (U+00A0 ou U+202F) dans les sept fichiers ; espaces simples avant les signes doubles et entre nombre et unité ou symbole % (environ 128 occurrences de « nombre % » ; 59 « nombre Gy »). Règle non appliquée ici.
- **D2** — « fibrillation atriale » ou « fibrillation auriculaire » : Terme absent de la leçon C72 (0 occurrence dans les sept fichiers) : sans objet pour cette mission.

## Renvois médicaux (formulations non modifiées)

Chaque entrée cite l’extrait exact, présent une seule fois dans son fichier, et explique pourquoi une reformulation locale changerait le sens médical.


### `chapters/C72/C72_a.html`

- **R1** — « ne le permet presque jamais chez l’adulte » : « presque jamais » contredit la donnée de la section 3.1 (exérèse complète possible dans 13 à 38 % des astrocytomes de grade 2 à 4) et l’exception du pilocytique. La fréquence est une affirmation médicale : à trancher par l’audit médical, la formulation n’est pas modifiée.
- **R2** — « la limite floue de l’astrocytome l’interdit le plus souvent » : Fréquence (« le plus souvent ») qu’aucune source lue ne chiffre, en tension avec « presque jamais » (R1) et 13 à 38 % (section 3.1). Non modifié.
- **R3** — « parce que la moelle concentre dans un très petit volume toutes les voies motrices et sensitives » : Relation causale (« parce que ») entre taille de la moelle et gravité du retentissement, et universel « toutes les voies » : aucune source lue ne l’établit. Non modifié.
- **R4** — « et ceux de haut grade (3 et 4) environ 25 % » : Dénominateur ambigu : 25 % des astrocytomes, des gliomes intramédullaires ou des tumeurs intramédullaires ? La fenêtre « Astrocytomes médullaires » écrit « le haut grade représente environ 25 % » sans préciser. Seule la source (Tonn et al. 2024) tranche.
- **R5** — « Il s’entoure souvent de kystes polaires et de dépôts d’hémosidérine formant une coiffe, et s’accompagne fréquemment d’une syringomyélie. » : « souvent » et « fréquemment » : fréquences non chiffrées ; la fenêtre « Lacunes des sources » reconnaît que les fréquences de signes ne figurent pas dans les sources lues. Même remarque pour « souvent » dans la carte Examen (e-2) et dans le tableau Imagerie (7.1).
- **R6** — « chez l’adulte, aucun plan de clivage n’existe » : Absolu (« aucun ») appliqué à « l’astrocytome » en général, alors que la phrase suivante et la fenêtre « Plan de clivage » le restreignent à l’astrocytome diffus de l’adulte et que le pilocytique fait exception. À restreindre ou à confirmer par l’audit médical.
- **R7** — « ce qui explique le &lt;button class="w" data-k="c72-h3k27"> » : Relation causale « MGMT non méthylé → bénéfice incertain du témozolomide » : la fenêtre H3 K27 précise que le « lien mécanistique [est] tiré des recommandations sur les gliomes de l’adulte, sans section spécifique pour la moelle ». Association présentée comme mécanisme. Non modifié.
- **R8** — « prime ici sur l’aspect favorable d’une lésion bien limitée » : Hiérarchie entre facteurs pronostiques (« prime ») non établie par une source lue ; l’« aspect favorable d’une lésion bien limitée » est une interprétation. Non modifié.
- **R9** — « Jusqu’à 15 % des enfants avec gliome optique » : Le libellé inverse le dénominateur : la fenêtre NF1 écrit « jusqu’à 15 % des enfants atteints » (de NF1) d’un gliome des voies optiques, non « 15 % des enfants avec gliome optique ». Interprétation à confirmer dans ERN GENTURIS 2023 avant toute reformulation.
- **R10** — « 40 à 50 % deviennent symptomatiques et 15 à 20 % sont traités » : Sujet et dénominateur absents (40 à 50 % des gliomes des voies optiques ? des enfants NF1 ?). Le verbe « deviennent » introduit en outre une chronologie. À préciser d’après ERN GENTURIS 2023.
- **R11** — « ce qui explique les retards diagnostiques de plusieurs mois à plusieurs années » : Causalité (« ce qui explique ») entre début non spécifique et retard diagnostique, et fréquence (« souvent ») : ni l’une ni l’autre n’est chiffrée ni établie par une source lue (fenêtre « Lacunes des sources »). Non modifié.
- **R12** — « ce qui s’explique en partie par le caractère peu évocateur de ces plaintes sensitives diffuses » : Causalité ajoutée par le rédacteur (« s’explique en partie ») sans source ; « souvent retardé de mois à années » est une fréquence non chiffrée. Non modifié.
- **R13** — « L’examen suit l’ordre habituel : état général, puis examen neurologique complet, puis recherche des signes du syndrome du cône ou de la q… » : Chronologie de l’examen (« ordre habituel », « puis… puis ») et ordre « d’abord localiser, ensuite mesurer » : aucune source lue ne la fonde. Non modifié.
- **R14** — « signe une atteinte intramédullaire étendue » : « signe » (est le signe de) va au-delà de la source (« un syndrome transverse progressif impose un bilan ») et ajoute « intramédullaire étendue », absente de la source. Non modifié.
- **R15** — « apparaissent plus tard. » : Chronologie (« plus tard ») : la source dit seulement que les troubles sphinctériens sont « rares au début » d’un astrocytome. Non modifié.
- **R16** — « exige au moins deux éléments cardinaux : troubles sensitifs en selle, dysfonction vésicale, intestinale ou sexuelle » : Ambiguïté de décompte : la liste après les deux-points compte soit deux éléments (selle ; dysfonction), soit quatre (selle, vésicale, intestinale, sexuelle). « Au moins deux » n’a pas le même sens. Même formulation dans l’îlot 13 (alerte). À trancher par Nersesyan et al. 2025.

### `chapters/C72/C72_b.html`

- **R17** — « exige au moins deux éléments cardinaux (troubles sensitifs en selle ; dysfonction vésicale, intestinale ou sexuelle) » : Même ambiguïté de décompte que R16 (îlot 13, alerte « Critères formels »). Non modifié.
- **R18** — « l’immunohistochimie est alors positive avec perte de H3K27me3 » : « alors » suggère que l’immunohistochimie H3 K27M est toujours positive et s’accompagne toujours d’une perte de H3K27me3 ; or l’altération par surexpression d’EZHIP donne une perte de H3K27me3 sans mutation K27M. Précision de fond : audit médical.
- **R19** — « plus tôt la moelle est décomprimée, plus la fonction est préservée » : Relation dose-effet (« plus tôt… plus ») : la source (résumé de Spirig et al. 2011) dit que le pronostic « dépend de la durée et de la sévérité du déficit préopératoire », non que la décompression plus précoce préserve davantage la fonction. Causalité ajoutée. Non modifié.
- **R20** — « car les récidives peuvent être tardives et asymptomatiques » : Causalité (« car ») et chronologie (« tardives ») : l’EANO 2018 ne fixe pas d’intervalle de suivi (la phrase suivante le dit) et aucune source lue n’est citée pour la nature des récidives. Non modifié.
- **R21** — « du type moléculaire plus que du siège. » : Comparaison d’importance relative (« plus que ») : la fenêtre « Lecture du pronostic » écrit « plus que du seul siège ». Association pronostique présentée comme hiérarchie causale sur des séries rétrospectives. Non modifié.
- **R22** — « La radiothérapie fait passer la survie sans progression à dix ans du myxopapillaire de moins de 40 % à environ 70 %. » : « fait passer » énonce un effet causal ; la fenêtre associée précise « séries rétrospectives » (comparaison non randomisée, biais de sélection possible). Association → causalité. Non modifié.
- **R23** — « une réadaptation intensive a permis la reprise de la marche et de la continence » : Causalité attribuée à la seule réadaptation ; la fenêtre « Synthèses suisses de la Praxis » l’attribue à l’exérèse « et » à la réadaptation. Cas isolé (résumé Stienen et al. 2019). Non modifié.
- **R24** — « Neuf pièges reviennent à l’examen » : Fréquence/reprise à l’examen fédéral (« reviennent ») : aucune source lue (PROFILES, annales) ne l’établit. La phrase de 150 mots ne se réécrit pas localement (STYLE_REDACTION § 2 : une idée par phrase) ; réécriture à confier à un audit de rédaction.
- **R25** — « l’astrocytome est pédiatrique, excentré et infiltrant » : Simplification contredite par le cours : les astrocytomes de haut grade sont plus fréquents chez l’adulte (îlot 2) et le pilocytique est bien limité (îlot 3). « est pédiatrique » vaut pour une tendance, non une définition. Non modifié.
- **R26** — « est un MPNST jusqu’à preuve du contraire » : Formulation catégorique (« est un… ») : le cours ailleurs parle de suspicion et de signal d’alarme (« soupçon », « suspicion de MPNST »). Non modifié ; à aligner sur la source (ERN GENTURIS 2023).

### `chapters/C72/C72_c.html`

- **R27** — « parce que la lésion intramédullaire, par sa situation, ne se biopsie pas à l’aveugle » : Justification du rédacteur (« parce que ») pour la place de l’imagerie, non sourcée ; « vient ensuite » ajoute une chronologie. Non modifié.
- **R28** — « Ces éléments traduisent une croissance limitée. » : Inférence (« traduisent ») entre signes d’imagerie et mode de croissance, non sourcée dans la fiche. Non modifié.
- **R29** — « Ne pas attendre un statut IDH comme en intracrânien » : Ambiguïté de sens : ne pas attendre un résultat IDH (délai) ou ne pas s’attendre à une mutation IDH (probabilité) ? L’infinitif injonctif (STYLE_REDACTION § 2) ne se corrige donc pas localement sans trancher.
- **R30** — « elle fixe le grade et le traitement » : « fixe le traitement » est excessif : le grade OMS 2021 dépend de la biologie, le traitement de la décision collégiale (colloque). Non modifié.
- **R31** — « Une cytologie du LCR trop précoce après l’opération est difficile à interpréter. » : Raison énoncée comme un fait alors que la phrase suivante dit que « la source n’en donne pas la raison » : le texte est contradictoire sur le statut de l’explication. Non modifié.
- **R32** — « ou, après deux ans, » : « après deux ans » : deux ans de quoi (âge, durée de suivi, durée de non-conclusion) ? Précision clinique, non modifiée.
- **R33** — « ce qui explique qu’il irrite les racines (dysesthésies, douleurs) sans produire de parésie, très inhabituelle dans cette forme » : Causalité anatomique (« ce qui explique ») non sourcée dans la fenêtre « Du cône médullaire à la queue de cheval ». Non modifié.
- **R34** — « ils touchent d’emblée les voies sensitives et motrices longues » : Chronologie (« d’emblée ») qui contredit les cartes de l’anamnèse (dysesthésies diffuses, parésie « occasionnelle »). Non modifié.
- **R35** — « n’est pas encore un MPNST » : « pas encore » suggère une évolution fatale vers le MPNST : la source (OMS 2021 / ERN GENTURIS) dit que l’ANNUBP est une entité distincte, de potentiel biologique incertain. Chronologie ajoutée. Même formulation dans la clé de glossaire ANNUBP et dans le Pareto de neuropathologie.
- **R36** — « montre un principe : le grade suit le risque de récidive » : Généralisation d’un exemple unique (passage du myxopapillaire de 1 à 2) en principe (« le grade suit le risque de récidive, non l’aspect microscopique seul ») : inférence du rédacteur, non sourcée. Non modifié.
- **R37** — « Le statut MGMT non méthylé explique le bénéfice incertain du témozolomide. » : Même causalité que R7 (MGMT → témozolomide), présentée sans réserve dans l’onglet Sciences. Non modifié.
- **R38** — « pourquoi les doses spinales citées pour l’épendymome (45 à 54 Gy) restent en deçà de celles du gliome de la ligne médiane de l’encéphale … » : Explication causale avouée « lecture du rédacteur » ; de plus 54 Gy appartient aux deux fourchettes, donc « en deçà » est inexact au sommet. Non modifié.

### `chapters/C72/C72_d.html`

- **R39** — « aucun médicament ne se substitue à l’exérèse chez l’épendymome » : Universel négatif (« aucun médicament ») non sourcé. Non modifié.
- **R40** — « car elles guident le choix d’associer un médicament » : Causalité (« car ») sur le rôle des doses de radiothérapie dans le choix d’un médicament associé : non sourcée. De plus, la phrase précédente dit que le tableau « ne donne que les doses lues dans les informations professionnelles suisses », or deux lignes viennent de l’EANO. Non modifié.
- **R41** — « puis 6 cycles de 150 puis 200 mg/m² » : La fenêtre Temodal® écrit « 6 cycles de 150 à 200 mg/m² » : deux formulations d’une posologie (« puis » suggère un palier, « à » une fourchette). Dose : seule l’information professionnelle suisse tranche. Non modifié.

### `chapters/C72/C72_pop1.html`

- **R42** — « son bénéfice au-delà de la radiothérapie n’est donc pas établi » : « donc » : de « agit moins » (mécanisme) à « bénéfice non établi » (niveau de preuve), l’inférence n’est pas valide ; l’un relève de la biologie, l’autre des essais. Non modifié.
- **R43** — « la survie globale médiane moyenne est de 24 mois (13 à 40) » : « médiane moyenne » est contradictoire : moyenne de médianes de plusieurs séries ? Statistique à vérifier dans Watanabe et al. 2024. Non modifié.
- **R44** — « meilleure que la forme intracrânienne » : Accord et portée : l’adjectif singulier ne dit pas si les deux survies (globale et sans progression) sont meilleures. Le pluriel changerait le fond. Non modifié.

### `chapters/C72/C72_pop2.html`

- **R45** — « sa reconnaissance évite une biopsie ou un traitement inutile » : Bénéfice clinique affirmé (« évite ») sans source dans la fenêtre. Non modifié.
- **R46** — « les métastases intramédullaires du cône, du poumon ou du sein » : Sens ambigu : métastases du cône (siège) ou issues du cône ? Une métastase vient du poumon ou du sein ; « du cône » désigne vraisemblablement le siège, mais la phrase ne le dit pas. Non modifié.
- **R47** — « La radiothérapie fait passer la survie sans progression à 10 ans de moins de 40 % à environ 70 %. » : Même causalité que R22 (séries rétrospectives). Non modifié.
- **R48** — « ANNUBP n’est pas encore un MPNST. » : Même chronologie que R35. Non modifié.

### `glossary/c72.py`

- **R49** — « Ce neurofibrome atypique de la neurofibromatose de type 1 n’est pas encore un MPNST. » : Même chronologie que R35. Non modifié.

## Propositions locales

Les 87 propositions complètes (ancien, nouveau, motif, catégorie) figurent dans `propositions.json`. Les plus significatives :

- `C72-LANG-0001` (repetition) — « Leur rareté contraste avec leur retentissement : malgré sa fréquence faible, une tumeur » → « Leur rareté contraste avec leur retentissement : une tumeur ». Répétition : « rareté » et « fréquence faible » disent la même chose dans la même phrase.
- `C72-LANG-0002` (ambiguite) — « &lt;/button> change selon la tumeur. » → « &lt;/button> diffère entre l’adulte et l’enfant. ». Tautologie : une répartition « par type » ne peut pas « changer selon la tumeur » ; la phrase suivante, qui oppose adulte et enfant, donne le sens.
- `C72-LANG-0017` (lourdeur) — « sont les éléments de l’examen ophtalmologique d’un gliome des voies optiques » → « composent l’examen ophtalmologique d’un gliome des voies optiques ». Lourdeur : « sont les éléments de » se réduit à « composent ».
- `C72-LANG-0022` (registre) — « Une IRM postopératoire juge l’étendue de l’exérèse. » → « Une IRM postopératoire évalue l’étendue de l’exérèse. ». Impropriété : une IRM ne « juge » pas ; elle évalue.
- `C72-LANG-0023` (registre) — « la jeune femme porte une lésion intramédullaire » → « la jeune femme présente une lésion intramédullaire ». Registre : un patient « présente » une lésion ; il ne la « porte » pas.
- `C72-LANG-0027` (registre) — « définitive en règle, » → « définitive en règle générale, ». Locution incomplète : on dit « en règle générale ».
- `C72-LANG-0028` (ambiguite) — « Hypersignal T2 du cône jusqu’à 90 %, « flow voids » serpigineux ; angiographie de référence » → « Hypersignal T2 du cône (jusqu’à 90 % des cas), « flow voids » serpigineux ; angiographie de référence ». Dénominateur manquant : « jusqu’à 90 % » de quoi ? La fenêtre « Fistule durale artérioveineuse » écrit « 90 % des cas » ; la correction reprend ce libellé sans ajouter de donnée.
- `C72-LANG-0035` (phrase_nominale) — « Le témozolomide est contre-indiqué. Pour l’homme traité, aucune procréation pendant le traitement et trois moi » → « Le témozolomide est contre-indiqué pendant la grossesse et l’allaitement. Chez l’homme traité, aucune procréat ». Phrase sans verbe (STYLE_REDACTION § 2) et contre-indication non située : le titre de la carte (grossesse et allaitement) et la section pharmacologie donnent le contexte, la formulation « aucune procréation n’est permise » est celle de la leçon pharmacologie.
- `C72-LANG-0036` (phrase_nominale) — « : tableau d’épendymome. » → « : ce tableau évoque un épendymome. ». Phrase nominale (STYLE_REDACTION § 2).
- `C72-LANG-0039` (registre) — « Il signale aussi ce que les sources lues ne permettent pas d’affirmer. » → « Les limites des sources lues y sont aussi signalées. ». Méta-discours proscrit (STYLE_REDACTION § 3) : « Il » renvoyait à « Cet îlot ».
- `C72-LANG-0041` (lourdeur) — « usage hors indication&lt;/button>), et l’obligation s’étend aux tumeurs » → « usage hors indication&lt;/button>). L’obligation s’étend aux tumeurs ». Phrase trop longue (STYLE_REDACTION § 2, une idée par phrase) : deux informations sans rapport (témozolomide, déclaration) sont soudées par « et ».
- `C72-LANG-0066` (ambiguite) — « cette absence ne prouve pas l’absence d’autorisation et se vérifie sur le site de Swissmedic. » → « cette absence ne prouve pas l’absence d’autorisation, qui se vérifie sur le site de Swissmedic. ». Antécédent ambigu : « se vérifie » se rapporterait à « cette absence » ; c’est l’autorisation qui se vérifie.
- `C72-LANG-0076` (grammaire) — « Le document consulté est une aide-mémoire » → « Le document consulté est un aide-mémoire ». Genre : « aide-mémoire » est masculin.
- `C72-LANG-0087` (abreviation) — « [('MG','MéthylGuanine'),('M','Méthyl'),('T','Transférase')] » → « [('M','Méthyl'),('G','Guanine'),('M','Méthyl'),('T','Transférase')] ». Définition littérale lettre à lettre (règle 3 du projet) : le sigle MGMT compte quatre lettres, M-G-M-T ; la clé les découpait en trois éléments dont un « MG » qui n’est pas une lettre. Le développement complet (« O6-méthylguanine-ADN méthyltransférase ») est inchangé.

## Observations non locales (aucune proposition)

- Onglet Sciences : quatre disciplines réelles (Anatomie, Neuropathologie, Génétique, Radiobiologie, soit 4 attributs data-s) et aucun sous-onglet « Sémiologie fondamentale et analytique » : hors périmètre linguistique, à traiter dans l’audit médical (addendum lot 2, point 1).
- Onglet Diagnostic, tableau 7.1 : la ligne « Subépendymome » place un énoncé de tomodensitométrie dans la colonne « Aspect IRM » ; incohérence de structure, non corrigeable localement.
- Onglet Pathologie, carte « Enfant » (section 2) : elle contient une phrase sur l’adulte (« Chez l’adulte, les astrocytomes de haut grade… ») ; placement à revoir.
- Section 7.3 : le titre annonce un classement « par gravité » et le texte introductif un ordre danger immédiat → infection → inflammation → autre tumeur, mais le tableau est ordonné par niveau anatomique.
- Section 12.3 : la phrase « Neuf pièges reviennent à l’examen » (environ 150 mots, neuf propositions) dépasse la règle d’une idée par phrase (STYLE_REDACTION § 2) ; réécriture non locale, non proposée (voir R24).
- Fenêtres (pop1, pop2) : de nombreuses lignes sous étiquette « .lab » sont des énumérations nominales (« Liste », « Signes », « Recommandation »…) et les fenêtres « Pareto » sont des listes de propositions nominales. Elles sont conformes à leur fonction de listes ; seules les phrases nominales de texte courant ont été corrigées.

## Rubrique 21 — Sémiologie fondamentale et analytique

Hors périmètre d’un audit linguistique. Constat de structure à transmettre à l’audit médical : l’onglet Sciences compte quatre disciplines réelles et aucun sous-onglet de sémiologie (voir observation 1).

## Lacunes

- Aucun correcteur orthographique automatique (Antidote, LanguageTool) n’a été exécuté : la relecture est humaine-IA, par lecture intégrale ; des fautes isolées peuvent subsister.
- Aucun ouvrage de référence (Grevisse, Dictionnaire de l’Académie, Office québécois de la langue française, Lexique de l’Imprimerie nationale) n’a été consulté pendant cette mission : les corrections de grammaire, d’accord et de registre reposent sur la lecture et sur la cohérence interne de la leçon (corps, fenêtres, glossaire), non sur une règle citée.
- Les espaces insécables et les formes « fibrillation atriale/auriculaire » sont des choix différés par Vial : non traités (voir D1 et D2).
- Aucune source médicale n’a été lue : les 49 renvois signalent des formulations, non des erreurs démontrées ; leur statut médical reste à établir par l’audit médical.
- Les textes alternatifs et le texte des figures SVG (aria-label, texte interne) ont été lus mais non soumis à une analyse de lisibilité à 390 px (hors périmètre de cette mission).
- Le glossaire n’a pas été exécuté ; la présence des clés des abréviations a été contrôlée par recherche textuelle dans glossary/*.py ; aucune clé manquante n’a été trouvée hors l’unité « Gy ».

## Tableau de bord final

| Élément | État |
|---|---|
| Empreintes des 7 fichiers | conformes au manifeste |
| Propositions / renvois | 87 / 49 |
| Unicité des extraits | contrôlée par script, 136 extraits uniques |
| Sources canoniques modifiées | aucune |
| Choix de Vial respectés | espaces insécables et fibrillation : différés, listés |
