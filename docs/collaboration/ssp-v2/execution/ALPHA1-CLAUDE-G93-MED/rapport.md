# Audit médical ALPHA77 — G93, Autres affections du cerveau (S08, N-05-Neurologie)

Mission `ALPHA1-CLAUDE-G93-MED` · branche `claude/alpha1/g93-med-g1` · base `103745ba` (sources figées `523832d9`) · 16 octobre 2026 · modèle et effort conformes au manifeste.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse pour Vial

La leçon G93 est honnête : elle nomme ses lacunes et ne donne aucune dose sans source. Elle reste pourtant **en retard d’une version** sur la réanimation après arrêt cardiaque. Les recommandations ERC-ESICM 2025, lues ici en texte intégral, modifient le seuil d’entrée du pronostic, la cible thermique, la pression artérielle visée et la PaCO₂. La borne de PaCO₂ de la leçon contient en outre une **erreur d’unité** héritée du texte 2021 : 4,5 kPa valent 33,8 mmHg, non 35.
Côté pharmacologie, l’information professionnelle suisse du **topiramate**, que la leçon déclarait non lue, contre-indique ce médicament chez la femme en âge de procréer sans contraception hautement efficace, c’est-à-dire dans la population même de l’HII. Elle interdit aussi son association à l’acétazolamide. Le repère de **4 g/j d’acétazolamide** est exact, mais il vaut quatre fois la dose orale maximale du libellé suisse, ce que la leçon ne dit pas.
Enfin, la **sémiologie fondamentale et analytique** est absente. Les signes d’**engagement** (G93.5) manquent, une **figure anatomique** a été dessinée par IA, et les sciences ne remplissent pas leur contrat.

| BLOQUANT | MAJEUR | MINEUR | ENRICHISSEMENT |
|---|---|---|---|
| 0 | 10 | 9 | 5 |

**Lecture.** Les empreintes SHA-256 des sept fichiers sont conformes au manifeste. `test_v7.py --static G93` affiche OK. `tests/audit_sciences.py` échoue (C10).

## Constats classés par gravité

### MAJEUR (10)

**C01** — `chapters/G93/G93_b.html` — ancre : `Le patient doit rester comateux, avec une réponse motrice de 3 ou moins, à 72 heures ou plus du retour à une circulation`

Algorithme pronostique après arrêt cardiaque obsolète. La leçon applique ERC-ESICM 2021 (entrée à M ≤ 3) alors que la version 2025, publiée en octobre 2025 et lue ici en texte intégral, l'applique à tout patient qui n'obéit pas aux ordres (M < 6) à 72 h, ajoute des prédicteurs de bon pronostic (M4–5 dans les 4 jours, NSE < 17 µg/L dans les 72 h, absence de restriction de diffusion entre 72 h et 7 jours, EEG continu de voltage normal dans les 72 h), définit l'état de mal myoclonique (> 30 min, continu et généralisé, dans les 72 h), demande des NSE sériées et la répétition du scanner à 72–96 h. Surfaces touchées : g93-9 (texte, liste, À retenir), g93-16 (alert), g93-pronostic (pop1), pareto-g93-autres (pop2), référence g93-16. Recalcul R09 : FAUX par rapport à la source applicable la plus récente.

- Preuve : [S5] Evidence — Suggested prognostication strategy : « applies to unconscious patients, defined as not being awake and obeying commands (M < 6) at 72 h after ROSC » ; [S5] Prediction of good neurological outcome : « a withdrawal or localising response to pain (motor score of the Glasgow Coma Scale [GCS-M] 4–5) in the first 4 days after ROSC, normal (<17 mcg/L) NSE » ; [S4] Concise guidelines — prognostication : « In a comatose patient with M ≤ 3 at ≥ 72 h from ROSC »
- Proposition : propositions/remplacements.json M05–M10, M15, M16, M18 (texte exact de remplacement, unicité des anciens vérifiée par script)
- Justification : Mécanisme : le seuil M ≤ 3 laisse de côté la plupart des patients destinés à récupérer et ignore les signes favorables. Conséquence : un pronostic posé sur la règle 2021 peut méconnaître une discordance favorable (récupération 11 % contre 3 %). Décision : la source primaire applicable la plus récente l'emporte (consigne de Vial) ; mise à jour obligatoire.

**C02** — `chapters/G93/G93_b.html` — ancre : `Cible constante entre 32 et 36 °C pendant au moins 24 heures ; éviter la fièvre (plus de 37,7 °C) pendant au moins 72 he`

Cibles de réanimation post-arrêt obsolètes et piège devenu inexact. ERC-ESICM 2025 remplace la cible thermique constante 32–36 °C ≥ 24 h par la prévention active de la fièvre (cible 37,5 °C au plus) pendant 36 à 72 h, interdit de réchauffer activement une hypothermie légère, et vise une PAM > 60–65 mmHg (au lieu de ≥ 65). Le piège de g93-8 affirme que le texte 2025 n'a pas été lu ; il l'est désormais. Surfaces : g93-8 (tableau, piège), g93-16 (key), g93-postarret (pop1), pareto-g93-autres. Recalculs R08 (FAUX), R10 et R10b (ARRONDI).

- Preuve : [S5] Table 1 — Temperature Management : « Recommends actively preventing fever 37.5 °C for at least 72 h post-ROSC (symbole de comparaison illisible dans l'extraction) » ; [S5] Temperature control : « Prevent active fever for 36 to 72 h in post-cardiac arrest patients who remain comatose » ; [S5] Haemodynamic monitoring and management : « Avoid hypotension and target a mean arterial pressure (MAP) >60–65 mmHg after cardiac arrest »
- Proposition : propositions/remplacements.json M02–M04, M11, M13, M14, M17
- Justification : Mécanisme : aucune cible hypothermique n'a fait mieux qu'une cible normothermique (revues ILCOR) ; la fièvre aggrave la lésion. Conséquence : enseigner 32–36 °C comme cible constante est dépassé. Décision : remplacer par les cibles 2025, en gardant la mention historique.

**C03** — `chapters/G93/G93_b.html` — ancre : `PaCO₂ 4,5 à 6,0 kPa (35–45 mmHg)`

Erreur d'unité et valeur obsolète : 4,5 kPa = 33,8 mmHg, non 35 mmHg ; 35 mmHg = 4,67 kPa. L'incohérence vient du texte ERC-ESICM 2021, corrigé en 2025 (4,7–6,0 kPa, environ 35–45 mmHg). Présente 4 fois : g93-8 (tableau), g93-16 (key), corrélation clinique de g93-s-physio-cours, g93-postarret. Recalculs R04, R05, R07 : FAUX.

- Preuve : [S4] Concise guidelines — ventilation : « i.e. 4.5–6.0 kPa or 35–45 mmHg » ; [S5] Control of ventilation : « Target normocapnia – a partial pressure of carbon dioxide of 4.7–6.0 kPa (or approximately 35–45 mmHg) »
- Proposition : propositions/remplacements.json M01, M11, M12, M13
- Justification : Mécanisme : 1 kPa = 7,5006 mmHg ; la borne basse en kPa ne correspond pas à celle en mmHg. Conséquence : un lecteur qui vise 4,5 kPa tolère une hypocapnie de 33,8 mmHg, vasoconstrictrice. Décision : borne 4,7 kPa (règle EXIGENCE_CALCULS : unité erronée = MAJEUR).

**C04** — `chapters/G93/G93_d.html` — ancre : `Le topiramate ne se prescrit pas pendant la grossesse.`

Contre-indication incomplète dans la population exacte de la maladie. L'information professionnelle suisse Topamax® (juin 2026), lue ici, contre-indique le topiramate en prévention de la migraine pendant la grossesse ET chez toute femme en âge de procréer sans contraception hautement efficace, impose un programme de prévention de la grossesse (test avant instauration, réévaluation annuelle) et signale la baisse d'efficacité des contraceptifs hormonaux (induction du CYP3A4, méthode barrière associée). L'HII touche des femmes jeunes ; la leçon recommande pourtant le topiramate pour la perte de poids et la prophylaxie. La leçon déclare aussi « Information professionnelle suisse non lue » (g93-p-2, g93-topiramate).

- Preuve : [S14] Contre-indications — Prévention de la migraine : « Grossesse. Femmes en âge de procréer n'utilisant pas une méthode contraceptive hautement efficace » ; [S14] Programme de prévention de la grossesse : « Les femmes qui utilisent des contraceptifs hormonaux systémiques doivent utiliser également une méthode barrière »
- Proposition : propositions/remplacements.json M20, M22, M23
- Justification : Mécanisme : tératogène (malformations, retard de croissance) et inducteur enzymatique. Conséquence : prescription à une femme jeune sans contraception efficace contraire au libellé suisse. Décision : contre-indication complète, datée.

**C05** — `chapters/G93/G93_d.html` — ancre : `Interactions dangereuses et médicaments à éviter`

Îlot « Interactions dangereuses » sans les interactions des médicaments qu'il recommande : (1) topiramate + acétazolamide, deux inhibiteurs de l'anhydrase carbonique, association « à éviter » (calculs rénaux) selon la FI Topamax® ; (2) acétazolamide + acide acétylsalicylique à doses élevées : acidose métabolique sévère et toxicité centrale (FI Diamox®) ; (3) acétazolamide + lithium (excrétion accrue) et + ciclosporine (taux accrus). La leçon cite pourtant topiramate, aspirine, lithium et ciclosporine.

- Preuve : [S14] Mises en garde — Néphrolithiase : « La prise concomitante de Topamax avec d'autres inhibiteurs de l'anhydrase carbonique comme l'acétazolamide ... doit donc être évitée » ; [S11] Interactions : « L'utilisation concomitante de l'acétazolamide et de l'acide acétylsalicylique à doses élevées peut conduire à une acidose métabolique sévère »
- Proposition : propositions/remplacements.json M20 (encadré alert « Associations à éviter »)
- Justification : Mécanisme : effets additifs sur l'anhydrase carbonique rénale et sur l'équilibre acide-base. Conséquence : lithiase et acidose évitables. Décision : ajout à l'îlot p-3.

**C06** — `chapters/G93/G93_d.html` — ancre : `posologie à lire dans le produit`

Repère de dose trompeur. La case de l'acétazolamide renvoie à l'information professionnelle pour la posologie de l'HII ; or la FI Diamox® (juillet 2026) n'en donne aucune, et ses posologies orales maximales sont de 1000 mg/24 h (glaucome, épilepsie). La même case cite 4 g/j (IIHTT) sans dire qu'il s'agit de 16 comprimés et de 4 fois ce maximum, ni qu'il s'agit d'un usage hors indication. Recalculs R28–R30.

- Preuve : [S11] Posologie — Glaucome / Épilepsie : « 1-4 comprimés (250-1000 mg) en 24 heures ; 1-4 comprimés (250-1000 mg) par jour » ; [S2] Acetazolamide : « greater than 40% of patients were treated with 4 g of acetazolamide daily »
- Proposition : propositions/remplacements.json M21
- Justification : Mécanisme : effets indésirables dose-dépendants (48 % d'arrêts dès 1500 mg). Conséquence : le lecteur cherche dans la FI une dose qui n'existe pas et retient 4 g comme repère. Décision : écrire le maximum suisse, l'écart, le statut hors indication et la surveillance.

**C07** — `chapters/G93/G93_c.html` — ancre : `data-s="g93-s-anat"`

Sous-onglet « Sémiologie fondamentale et analytique » absent. Décompte réel des data-s de G93_c.html : 3 (g93-s-anat, g93-s-physio, g93-s-bioch) ; aucun g93-s-semio ; aucun marqueur data-semiology-clinical dans pA. La sémiologie existante (g93-5 : tableau des symptômes, cartes Anamnèse et Examen) est descriptive : pas de mécanisme par signe, pas de technique (réflexe cornéen, test de station debout), pas de valeur chiffrée des signes du coma, pas de regroupement syndromique, pas de raisonnement en cinq étapes, pas de cas sur la valeur d'un signe.

- Preuve : [S2] Other symptoms : « Unilateral or bilateral sixth-nerve palsy may occur in IIH causing horizontal diplopia » ; [S5] Ocular reflexes : « an absent corneal reflex predicts poor neurological outcome after 72 h from ROSC with 0 % false positive rate (95 % confidence interval 0–3.4 %) » ; [S6] Physical examination : « standing heart rate of >30/min above normal in patients older than 20 years and > 40/min above normal in younger patients »
- Proposition : propositions/G93_c_semio.html (bouton g93-tab-semio, panneau g93-s-semio, neuf sections data-semiology, figure non anatomique, trois cas corrigés) ; propositions/G93_a_semio_clinique.html (section data-semiology-clinical="G93" dans g93-5) ; propositions/G93_pop1_semio.html (douze fenêtres g93-sm-* et la fenêtre de calcul g93-unites, dans _pop1)
- Justification : Mécanisme : sans technique ni valeur, le lecteur ne passe pas du signe à l'hypothèse. Conséquence : l'examen fédéral et la pratique exigent ce passage. Décision : exigence de Vial du 15.10.2026 ; MAJEUR, bloquant pour la clôture.

**C08** — `chapters/G93/G93_a.html` — ancre : `Les sources retenues pour ce cours ne décrivent pas les types cliniques d’engagement ni leurs signes précis`

G93.5 (compression du cerveau avec engagement) sans aucun signe clinique : la leçon renvoie le lecteur à un traité. Le drapeau rouge le plus vital de la catégorie manque (rubrique 9). La recommandation ERC-ESICM 2025 lue ici décrit les signes de mort cérébrale imminente évoquant un engagement : pupilles fixes et dilatées, diabète insipide, bradycardie avec hypertension, instabilité hémodynamique inexpliquée ; mort cérébrale dans 5–10 % des décès après réanimation conventionnelle. Les syndromes topographiques (temporal, sous-falcoriel, amygdalien) restent non sourcés : LACUNE (ligne directrice DGN S1 « Intrakranieller Druck » 2023 inaccessible).

- Preuve : [S5] Suggested prognostication strategy : « fixed, dilated pupils, diabetes insipidus, and cardiovascular changes suggesting herniation, such as bradycardia associated with hypertension »
- Proposition : propositions/remplacements.json M30 ; fenêtre g93-sm-engagement (propositions/G93_pop1_semio.html) ; section « urgency » de G93_c_semio.html
- Justification : Mécanisme : la compression du tronc cérébral désorganise les réflexes pupillaires, la neurohypophyse et le contrôle cardiovasculaire. Conséquence : reconnaître ce tableau déclenche l'alerte de soins intensifs. Décision : ajout sourcé, lacune nommée pour le reste.

**C09** — `chapters/G93/G93_c.html` — ancre : `aria-label="Figure 2 — Globe, nerf optique et gaine"`

Figure anatomique dessinée par IA (classe ANATOMIQUE_IA) : globe, nerf optique et gaine tracés en SVG par l'agent de rédaction du cycle Betta 40 (son rapport.md déclare « 3 schémas SVG noir et blanc plus la figure de Monro-Kellie »). Règle de Vial du 15.10.2026 : non recevable. Le texte des SVG existants (viewBox 640, police 14) rend environ 7,8 px dans un conteneur de 358 px.

- Preuve : [S2] Fig. 3 et licence de l'article : « This article is distributed under the terms of the Creative Commons Attribution 4.0 International License »
- Proposition : propositions/G93_c_figures.html (candidats 1 et 2 : figures 3 et 4 de la recommandation EHF 2018, CC BY 4.0 ; candidat 3 non trouvé, Wikimedia Commons en HTTP 429)
- Justification : Mécanisme : un dessin approximatif fausse la topographie de l'espace périoptique. Conséquence : il trahit l'anatomie que l'imagerie montre. Décision : remplacement par un original sourcé après contrôle visuel.

**C10** — `chapters/G93/G93_c.html` — ancre : `class="sci-bar ui"`

Contrat des sciences non respecté : tests/audit_sciences.py échoue (3 disciplines de 217, 194 et 246 mots, sous le seuil de 280 ; les quatre libellés « Science → clinique. », « Science → examen. », « Science → traitement. », « À retenir. » absents, remplacés par « Corrélation clinique. »). Le validateur de sémiologie exige en outre au moins six sous-onglets data-s ; la leçon en a trois.

- Preuve : [S7] Aquaporins : « AQP4 localizes to brain-fluid interfaces including perivascular astrocyte endfeet, glia limitans » ; [S5] Electroencephalography : « burst suppression (50–99 % suppression periods), or suppression (>99 % activity with <10 µV amplitude) »
- Proposition : propositions/G93_c_sciences.html (partie A : quatre libellés pour chaque discipline, décomptes portés à 341, 313 et 344 mots ; partie B : disciplines Histologie et Neurophysiologie clinique, 411 et 371 mots, figures non anatomiques) ; avec le sous-onglet de sémiologie, total de six data-s
- Justification : Mécanisme : les sciences doivent expliquer le « pourquoi » des signes et des traitements. Conséquence : contrat CHAPTER_SPEC et STYLE_REDACTION § 6 non tenus. Décision : compléter.

### MINEUR (9)

**C11** — `chapters/G93/G93_pop2.html` — ancre : `par exemple 500 mL de Mannitol 20 % en 1 heure`

L'exemple de la FI (500 mL = 100 g) n'est une dose de 1–2 g/kg que pour 50 à 100 kg ; la monographie omet le délai et la durée d'action (baisse de la pression dès 15 min, maximum à 30–60 min, durée 3–8 h après la fin), l'osmolarité (environ 1100 mOsm/L), les interactions lithium et ciclosporine et l'interdiction de perfuser simultanément du sang sans électrolytes. Recalculs R23–R27.

- Preuve : [S12] Pharmacocinétique — Absorption : « La pression intracrânienne diminue déjà 15 minutes après le début de la perfusion de mannitol. L'effet est maximum en 30–60 minutes » ; [S12] Interactions : « Chez les patients qui reçoivent simultanément du mannitol et du lithium, le taux de lithium doit être régulièrement contrôlé »
- Proposition : propositions/remplacements.json M25
- Justification : Mécanisme : dose au poids ; effet osmotique transitoire. Conséquence : surdosage relatif chez un patient léger si l'exemple est lu comme une dose fixe. Décision : préciser.

**C12** — `chapters/G93/G93_b.html` — ancre : `seul médicament évalué par des essais randomisés ; bénéfice modeste`

Affirmation datée de 2018 : un essai randomisé contre placebo de l'exénatide (16 femmes, Brain 2023) a depuis été publié ; une méta-analyse de l'European Journal of Neurology (2025) étudie les agonistes du récepteur du GLP-1. Aussi dans g93-acetazolamide (pop2).

- Preuve : [S16] résumé : « Exenatide significantly and meaningfully lowered intracranial pressure at 2.5 h -5.7 ± 2.9 cmCSF » ; [S17] résumé : « lower risk of papilledema (RR: 0.25; 95% CI: 0.15-0.43 »
- Proposition : propositions/remplacements.json M40, M47 ; propositions/G93_b_enrichissements.html E2
- Justification : Mécanisme : réduction de la sécrétion du liquide par le récepteur du GLP-1. Conséquence : énoncé exact en 2018, inexact en 2026. Décision : dater l'énoncé.

**C13** — `chapters/G93/G93_a.html` — ancre : `L’indice pression-volume normal est d’environ 20 à 25 mL.</p>`

Deux unités de pression coexistent sans passerelle : cm d'eau (pression d'ouverture, seuil 25) et mmHg (pression intracrânienne, seuil 20–22). 25 cm d'eau = 18,4 mmHg ; 20–22 mmHg = 27,2–29,9 cm d'eau (R19–R22). La consigne de Vial du 11.10.2026 (§ 3) exige une fenêtre de calcul pour toute conversion. L'indice pression-volume n'est pas défini (volume qui multiplie la pression par dix).

- Preuve : [S7] Intracranial compliance : « PVI is the volume (mL) required to raise ICP 10-fold and is normally 20-25 mL »
- Proposition : propositions/remplacements.json M41 ; fenêtre g93-unites (propositions/G93_pop1_semio.html)
- Justification : Mécanisme : 1 cm d'eau = 98,0665 Pa ; 1 mmHg = 133,322 Pa. Conséquence : risque de comparer 25 et 22 comme s'ils partageaient l'unité. Décision : fenêtre de calcul.

**C14** — `chapters/G93/G93_pop1.html` — ancre : `HII diagnostiquée avec pression du liquide supérieure à 250 mm (280 mm chez l’enfant obèse)`

Unité incomplète : « 250 mm » sans « de liquide cérébrospinal » ; 250 mm de liquide = 25 cm, seuil identique à celui de Friedman (R17, R18).

- Preuve : [S2] Table 1 : « cerebrospinal fluid (CSF) pressure exceeds 250 mm CSF (or 280 mm CSF in obese children) »
- Proposition : propositions/remplacements.json M42
- Justification : Unité ambiguë sans conséquence décisionnelle.

**C15** — `chapters/G93/G93_b.html` — ancre : `Le plan associe une intervention multicomposante de perte de poids (indice de masse corporelle inférieur à 35 : grade B)`

Le cas récapitulatif n'applique pas le seuil à sa patiente : IMC 38 ≥ 35, donc chirurgie bariatrique à considérer (grade A) ; la phrase laisse les deux options ouvertes (R13).

- Preuve : [S3] résumé : « Bariatric surgery should be considered for women with IIH and a body mass index (BMI) ≥35 kg/m2 (grade A) »
- Proposition : propositions/remplacements.json M43
- Justification : Cas corrigé incomplet : le lecteur ne voit pas le seuil appliqué.

**C16** — `chapters/G93/G93_a.html` — ancre : `les recommandations du traumatisme crânio-cérébral fixent un seuil de traitement de la pression intracrânienne à 20 à 22`

Seuil décisionnel attribué à « les recommandations » sans préciser qu'il s'agit, via la revue de 2019, de lignes directrices américaines (Brain Trauma Foundation) ; aucune source suisse ou européenne lue sur ce point. Présent aussi dans g93-14, g93-16, g93-monro et la figure 3.

- Preuve : [S7] Introduction : « ICP elevation above the accepted threshold of 20–22 mmHg ... guidelines available to inform their management (Carney et al., 2017) »
- Proposition : propositions/remplacements.json M44
- Justification : Règle : aucune recommandation américaine comme fondement d'une conduite ; l'attribution doit être explicite.

**C17** — `glossary/g93.py` — ancre : `a('FOUR', [('F','Full'),('O','Outline'),('U','of UnResponsiveness'),('R','score')],`

Lettrage du sigle FOUR inexact : R ne signifie pas « score » ; FOUR = Full Outline of UnResponsiveness (U et R issus de UnResponsiveness).

- Preuve : [S8] résumé : « use the Full Outline of Unresponsiveness score instead of the Glasgow Coma Scale in the acute setting »
- Proposition : propositions/remplacements.json M45
- Justification : Définition littérale lettre à lettre exigée (CLAUDE.md, règle 3).

**C18** — `chapters/G93/G93_b.html` — ancre : `L’aspirine est restreinte dès 12 ans en cas d’infection virale.`

Formulation ambiguë : laisse croire que l'aspirine est libre avant 12 ans ; la FI exclut les formes à croquer et en granulé avant 12 ans et restreint l'usage dès 12 ans en cas de fièvre ou d'infection virale.

- Preuve : [S13] Posologie : « Chez les enfants de moins de 12 ans, l'utilisation d'Aspirine Comprimés à croquer et Granulé n'est pas indiquée »
- Proposition : propositions/remplacements.json M46
- Justification : Clarté d'une restriction de sécurité.

**C19** — `chapters/G93/G93_d.html` — ancre : `L’acétazolamide est contre-indiqué en cas d’hyponatrémie, d’hypokaliémie, d’insuffisance rénale ou hépatique grave, d’in`

Liste des contre-indications incomplète : le traitement au long cours est contre-indiqué dans le glaucome chronique non congestif à angle fermé (aggravation masquée).

- Preuve : [S11] Contre-indications : « Un traitement au long cours par Diamox est contre-indiqué en cas de glaucome chronique non congestif à angle fermé »
- Proposition : propositions/remplacements.json M24
- Justification : Contre-indication de traitement prolongé, pertinente car l'HII se traite des mois.

### ENRICHISSEMENT (5)

**C20** — `chapters/G93/G93_b.html` — ancre : `La pression d’ouverture normale monte jusqu’à 28 cm d’eau chez l’enfant.`

Situation pédiatrique sans posologie : Swisspeddose (intégré à la FI Diamox®) donne, pour une pression intracrânienne élevée, 8–10 mg/kg/dose × 3, maximum 100 mg/kg/j ; la FI précise que l'administration pédiatrique n'a pas été étudiée (R31).

- Preuve : [S11] Swisspeddose : « Indication: Pression intracrânienne élevée ... 8 - 10 mg/kg/dose ... 3 ... 100 mg/kg/jour »
- Proposition : propositions/remplacements.json M21 (phrase « Enfant »)
- Justification : Rubrique 15 (situations particulières) partielle.

**C21** — `chapters/G93/G93_b.html` — ancre : `Un antécédent d’HII seul ne modifie pas le mode d’accouchement.`

HII sans œdème papillaire non traitée comme forme : pas de risque visuel identifié, pas de surveillance visuelle au long cours, pas de chirurgie de routine.

- Preuve : [S2] IIHWOP : « As there is no threat to vision, long term visual monitoring is not required »
- Proposition : propositions/G93_b_enrichissements.html E1
- Justification : Rubrique 14 (suivi) partielle.

**C22** — `chapters/G93/G93_b.html` — ancre : `La baisse de pression est fortement corrélée à la perte de poids`

Essai randomisé IIH:WT absent : chirurgie bariatrique contre programme communautaire, −6,0 cm d'eau à 12 mois et −8,2 cm d'eau à 24 mois (R38) ; données GLP-1 (S16, S17).

- Preuve : [S15] résumé : « Intracranial pressure was significantly lower in the bariatric surgery arm at 12 months (adjusted mean [SE] difference, -6.0 [1.8] cm »
- Proposition : propositions/G93_b_enrichissements.html E2
- Justification : Rubrique 12 : preuve randomisée de la seule thérapie modificatrice.

**C23** — `chapters/G93/G93_b.html` — ancre : `La sévérité se classe en sévère (quasi confiné au domicile) et très sévère (quasi alité).</p>`

Encéphalomyélite myalgique : pronostic (guérison complète non habituelle, mortalité par suicide accrue) et données suisses (délai diagnostique de 6,7 ans, 2,6 erreurs diagnostiques) absents ; examen orthostatique non décrit.

- Preuve : [S6] Introduction : « full recovery is not the norm, particularly in adults » ; [S18] résumé : « The mean time from disease onset to diagnosis was 6.7 years »
- Proposition : propositions/G93_b_enrichissements.html E3 ; fenêtre g93-sm-orthostat
- Justification : Rubriques 4, 13 et 16 partielles.

**C24** — `chapters/G93/G93_a.html` — ancre : `Cette succession justifie de répéter l’évaluation clinique et l’imagerie plutôt que de supposer qu’un seul mécanisme per`

Œdème expansif d'infarctus (G93.6) sans la conduite européenne : décompression chirurgicale ≤ 60 ans dans les 48 h (preuves de haute qualité, ESO 2021).

- Preuve : [S19] résumé : « surgical decompression ... in adult patients aged up to and including 60 years ... within 48 hours of stroke onset »
- Proposition : propositions/G93_b_enrichissements.html E4
- Justification : Rubrique 12 ; recommandation européenne avec coauteur suisse.

## Calculs (EXIGENCE_CALCULS)

Script conservé : `calculs/verifier.py` (avec `calculs/inventaire_base.py`) ; sorties `calculs/inventaire.json` et `calculs/resultats.json`.

| Relevés | Grandeurs | Non calculables | Concordance source | Vignettes | Non rapprochées | Calculables | Recalculés | Corrects | Arrondis | Faux | Non vérifiables | Informatifs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 451 | 301 | 150 | 288 | 13 | 0 | 29 | 29 | 20 | 4 | 5 | 0 | 16 |

Les 301 grandeurs relevées sont toutes rapprochées d’une citation de source lue ou d’une vignette déclarée fictive. Les recalculs non informatifs sont tous faits (`recalcules = calculables`). Le tableau ci-dessous donne les résultats faux et arrondis, puis les contrôles de dose.

| Id | Verdict | Formule | Attendu | Trouvé | Source | Note |
|---|---|---|---|---|---|---|
| R03 | ARRONDI | PaO2 13 kPa × 7,5006 = 97,5 mmHg (écrit 100) | 97.5 | 100.0 | S4 | arrondi de la source (75–100 mmHg) ; écart 2,5 mmHg sans conséquence |
| R04 | FAUX | PaCO2 4,5 kPa × 7,5006 = 33,75 mmHg (écrit 35) | 33.8 | 35.0 | S4 (texte 2021) ; S5 corrige à 4,7 kPa | 4,5 kPa ≠ 35 mmHg ; 35 mmHg = 4,67 kPa. Incohérence d'unités reprise de la source 2021, corrigée en 2025 (4,7–6,0 kPa) : voir C03 |
| R05 | FAUX | 35 mmHg ÷ 7,5006 = 4,67 kPa (la leçon écrit 4,5) | 4.67 | 4.5 | S5 : « 4.7–6.0 kPa (or approximately 35–45 mmHg) » | borne basse fausse de 0,17 kPa ; valeur actuelle 4,7 kPa |
| R07 | FAUX | borne basse PaCO2 : 2025 = 4,7 kPa ; leçon = 4,5 | 4.7 | 4.5 | S5 Table 1 et « Control of ventilation » | C03 |
| R08 | FAUX | seuil de fièvre à prévenir : 2025 = 37,5 °C ; leçon = 37,7 °C | 37.5 | 37.7 | S5 « Actively prevent fever by targeting a temperature [≤]37.5 °C » | C02 ; signe ≤ illisible dans l'extraction PDF, sens explicite (prévenir la fièvre) |
| R09 | FAUX | seuil d'entrée de l'algorithme pronostique : 2025 = M < 6 (non-obéissance) ; leçon = M ≤ 3 | 6.0 | 3.0 | S5 « applies to unconscious patients, defined as not being awake and obeying commands (M < 6) at 72 h » | C01 |
| R10 | ARRONDI | PAM : 2025 = > 60–65 mmHg ; leçon = ≥ 65 mmHg | 60.0 | 65.0 | S5 « target a mean arterial pressure (MAP) >60–65 mmHg » | 65 reste dans la fourchette 2025 ; borne basse élargie : MINEUR (C02) |
| R10b | ARRONDI | durée de prévention de la fièvre : 2025 = 36 à 72 h ; leçon = au moins 72 h | 36.0 | 72.0 | S5 « active prevention of fever for 36 to 72 h » | 72 h est la borne haute de 2025 : ARRONDI, mais l'intervalle doit être donné |
| R11 | CORRECT | quiz 1 : 27 > 25 (dépasse le seuil adulte) | 1.0 | 1.0 | S2 |  |
| R12 | CORRECT | cas récapitulatif : 36 > 30 (au-delà de la zone grise) | 1.0 | 1.0 | S2 |  |
| R13 | CORRECT | vignette 1 : IMC 38 ≥ 35 → chirurgie bariatrique à considérer (grade A) | 1.0 | 1.0 | S3 | le cas récapitulatif laisse les deux options ouvertes au lieu d'appliquer le seuil à la patiente (C15) |
| R14 | CORRECT | quiz 2 : M2 ≤ 3 (critère 2021) et M2 < 6 (critère 2025) — l'entrée dans l'algorithme est remplie | 1.0 | 1.0 | S4 ; S5 | la réponse attendue (exclure la sédation d'abord) reste juste sous les deux versions |
| R23 | CORRECT | 500 mL × 200 g/L = 100 g (exemple de la FI) | 100.0 | 100.0 | S12 composition (200 g/1000 mL) | 100 g correspond à 1–2 g/kg seulement pour 50–100 kg : l'exemple n'est pas une dose fixe (C11) |
| R24 | INFORMATIF | patient de 70 kg : 1 g/kg = 70 g = 350 mL ; 2 g/kg = 140 g = 700 mL | 350.0 | None | S12 | 700 mL dépasse le plafond de 500 mL/24 h, mais ce plafond appartient à la posologie de l'oligurie : la leçon l'attribue correctement |
| R25 | INFORMATIF | osmolarité théorique : 200 g/L ÷ 182,17 g/mol = 1098 mOsm/L | 1098 | None | S12 ; S21 (masse molaire) | explique « solution hypertonique » et la contre-indication « hyperosmolarité préexistante » |
| R28 | INFORMATIF | 4 g/j = 16 comprimés de 250 mg | 16.0 | None | S2 ; S11 |  |
| R29 | INFORMATIF | 4 g/j (IIHTT) comparé à la dose orale maximale de la FI suisse (1000 mg/24 h, glaucome et épilepsie) | 1000.0 | 4000.0 | S11 Posologie | 4 fois la dose orale maximale de la FI : à signaler explicitement (C06) |
| R31 | INFORMATIF | Swisspeddose (pression intracrânienne élevée) : 8–10 mg/kg/dose × 3 = 24–30 mg/kg/j ≤ 100 mg/kg/j | 24.0 | None | S11 (Swisspeddose) | cohérence interne ; dose absente de la leçon (C20) |
| R37 | ARRONDI | « environ −27 kg » contre 27,2–27,8 kg (milieu 27,5) | 27.5 | 27.0 | S3 |  |

**Lecture.** Aucune dose ni aucun débit n’est faux par rapport à l’information professionnelle suisse. Les cinq résultats faux concernent la PaCO₂ (C03) et deux seuils remplacés en 2025 (C01, C02). Les quiz et cas sont tous cohérents avec leurs seuils (R11 à R16), sauf l’application incomplète du seuil d’IMC au cas récapitulatif (C15).

## 21 — Sémiologie fondamentale et analytique

Statut : **absente** ; décompte réel des `data-s` : 3 (g93-s-anat, g93-s-physio, g93-s-bioch). Constat C07, MAJEUR, bloquant pour la clôture.

| Critère | Résultat |
|---|---|
| SEM-01 | non (data-s : g93-s-anat, g93-s-physio, g93-s-bioch ; aucun g93-s-semio) |
| SEM-02 | non |
| SEM-03 | non (audit_sciences échoue, C10) |
| SEM-04 | oui (test_v7 --static G93 : OK sur la leçon actuelle) |
| SEM-05 | non (tableau g93-5 sans colonne mécanisme ni piège) |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | non (valeurs des signes non données ; lacunes non déclarées comme telles dans la leçon) |
| SEM-09 | non |
| SEM-10 | partiel (pièges g93-5, g93-6) |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | partiel (alert g93-14 sans signes d’engagement) |
| SEM-14 | partiel (tableau g93-6) |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non (quiz e-4 portent sur les examens) |
| SEM-18 | non (aucun mot vert sémiologique) |
| SEM-19 | non (pas de sémiologie à juger) |
| SEM-20 | sans objet |
| SEM-21 | sans objet |
| SEM-22 | non vérifiable (aucun bouton) |
| SEM-23 | non (aucune capture) |
| SEM-24 | oui (statut « Aucune validation médicale humaine ») |

Propositions : `propositions/G93_c_semio.html` (neuf sections `data-semiology`, figure de raisonnement, trois cas corrigés dont un sur la valeur d’un signe, un sur la formulation d’une limite et un de calcul), `propositions/G93_a_semio_clinique.html` (marqueur `data-semiology-clinical`), `propositions/G93_pop1_semio.html` (fenêtres dans `_pop1`), `propositions/G93_c_sciences.html` (cinquième et sixième sous-onglets).

## Matrice des 20 rubriques

| Rang | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g93-0 (deux vignettes) |
| 2 | Définition et périmètre CIM-10-GM | couvert | g93-1, g93-cim ; conformes à S1 |
| 3 | Classifications et stades | partiel | g93-3 (types d’œdème) ; Frisén et états de conscience non sourcés |
| 4 | Épidémiologie suisse puis européenne | partiel | g93-2 ; aucune donnée suisse (S18 proposée pour la fatigue, C23) |
| 5 | Normal → pathologique | partiel | g93-3 ; sciences sous le contrat (C10) |
| 6 | Étiologies et facteurs de risque | couvert | g93-4, g93-secondaires (S2 tableau 4) |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g93-5 ; fréquences de l’HII partielles ; malaise post-effort non caractérisé (C07) |
| 8 | Examen clinique (signes, Se/Sp) | partiel | g93-5 ; aucune valeur des signes du coma ; examen orthostatique absent (C07) |
| 9 | Drapeaux rouges et urgences | partiel | g93-14, g93-11 ; signes d’engagement absents (C08) |
| 10 | Examens complémentaires | couvert | g93-e-1, g93-e-2, g93-e-3 |
| 11 | Diagnostic différentiel (discriminant) | partiel | g93-6 (HII) ; coma post-anoxique et fatigue sans discriminants groupés (C07) |
| 12 | Prise en charge suisse (FI datées) | partiel | g93-7, g93-8, pP ; cibles 2021 obsolètes (C02, C03) ; topiramate (C04) ; dose d’acétazolamide (C06) |
| 13 | Complications et pronostic | partiel | g93-9 (algorithme 2021 obsolète, C01), g93-14 |
| 14 | Suivi, prévention, dépistage | partiel | g93-7, g93-9 ; HII sans œdème papillaire (C21) |
| 15 | Situations particulières | partiel | g93-15 ; posologie pédiatrique absente (C20) |
| 16 | Spécificités suisses | absent | directives ASSM (mort cérébrale), aptitude à la conduite, AI non lues ; seule donnée suisse proposée : S18 |
| 17 | Critères formels du diagnostic (div.alert) | partiel | g93-16 ; critère pronostique 2021 obsolète (C01) |
| 18 | Paramètres clés chiffrés (div.key) | partiel | g93-16 ; PaCO₂, PAM et fièvre à mettre à jour (C02, C03) |
| 19 | Sous-codes CIM-10-GM couverts | couvert | glossary/g93.py, g93-cim (G93.0–G93.9, G93.80, G93.88) |
| 20 | Points d’examen fédéral | partiel | quiz e-4 ; aucun cas de sémiologie (C07) |

## Figures

| Figure | Fichier | Classe | Vérification | Constat |
|---|---|---|---|---|
| `Figure 1 — Compartiments intracrâniens et loi de Monro-Kel` | chapters/G93/G93_a.html | SCHEMA_NON_ANATOMIQUE | rectangle arrondi et libellés ; schéma de compartiments sourcé à S7 ; texte environ 7,8 px à 390 px | — |
| `Figure 2 — Globe, nerf optique et gaine"` | chapters/G93/G93_c.html | ANATOMIQUE_IA | cercle et lignes figurant globe, nerf et gaine ; origine IA déclarée par le rapport du cycle Betta 40 | C09 |
| `Figure 3 — Relation pression-volume intracrânienne"` | chapters/G93/G93_c.html | SCHEMA_NON_ANATOMIQUE | courbe non chiffrée ; forme sourcée à S7 | — |
| `Figure 4 — Cellule et canaux de l'œdème cytotoxique"` | chapters/G93/G93_c.html | SCHEMA_NON_ANATOMIQUE | ellipse et libellés, légende « ne représente ni une cellule réelle » ; acteurs sourcés à S7 | — |

## Sources lues

| Id | Source | Niveau | Date |
|---|---|---|---|
| S1 | [ICD-10-GM 2024, bloc G90–G99 : G93 Sonstige Krankheiten des Gehirns](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-g90-g99.htm) | section | 2023-09-15 (version 2024) |
| S2 | [Hoffmann J, Mollan SP, Paemeleire K, Lampl C, Jensen RH, Sinclair AJ. European Headache Federation guideline o](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755569/) | texte_integral | 2018-10-01 |
| S3 | [Abbott S et al. Weight management interventions for adults with idiopathic intracranial hypertension: systemat](https://doi.org/10.1212/WNL.0000000000207866) | resume | 2023-10-09 |
| S4 | [Nolan JP, Sandroni C, Böttiger BW et al. European Resuscitation Council and European Society of Intensive Care](https://pmc.ncbi.nlm.nih.gov/articles/PMC7993077/) | texte_integral | 2021-03-25 |
| S5 | [Nolan JP, Sandroni C, Cariou A et al. European Resuscitation Council and European Society of Intensive Care Me](https://doi.org/10.1016/j.resuscitation.2025.110809) | texte_integral | 2025-10-22 |
| S6 | [Nacul L, Authier FJ, Scheibenbogen C et al. European Network on Myalgic Encephalomyelitis/Chronic Fatigue Synd](https://pmc.ncbi.nlm.nih.gov/articles/PMC8161074/) | texte_integral | 2021-05-19 |
| S7 | [Jha RM, Kochanek PM, Simard JM. Pathophysiology and treatment of cerebral edema in traumatic brain injury. Neu](https://pmc.ncbi.nlm.nih.gov/articles/PMC6309515/) | texte_integral | 2019-02-01 |
| S8 | [Kondziella D et al. European Academy of Neurology guideline on the diagnosis of coma and other disorders of co](https://doi.org/10.1111/ene.14151) | resume | 2020-02-23 |
| S9 | [Schrör K. Aspirin and Reye syndrome: a review of the evidence. Paediatr Drugs 2007;9(3):195-204 (PMID 17523700](https://doi.org/10.2165/00148581-200709030-00008) | resume | 2007 |
| S10 | [Rabiei K et al. Prevalence and symptoms of intracranial arachnoid cysts: a population-based study. J Neurol 20](https://doi.org/10.1007/s00415-016-8035-1) | resume | 2016-02-09 |
| S11 | [Information professionnelle suisse Diamox® (acétazolamide), avec données Swisspeddose intégrées](https://amiko.oddb.org/fr/fi?gtin=7680211910195) | texte_integral | 2026-07 (mise à jour de l'information) |
| S12 | [Information professionnelle suisse Mannitol 20% B. Braun](https://amiko.oddb.org/fr/fi?gtin=7680317540012) | texte_integral | 2025-11 (mise à jour de l'information) |
| S13 | [Information professionnelle suisse Aspirine® (comprimés à croquer, granulé)](https://amiko.oddb.org/fr/fi?gtin=7680495260320) | section | 2024-09 (mise à jour de l'information) |
| S14 | [Information professionnelle suisse Topamax® (topiramate)](https://amiko.oddb.org/fr/fi?gtin=7680535370149) | section | 2026-06 (mise à jour de l'information) |
| S15 | [Mollan SP, Mitchell JL, Ottridge RS et al. Effectiveness of bariatric surgery vs community weight management i](https://doi.org/10.1001/jamaneurol.2021.0659) | resume | 2021-06-01 |
| S16 | [Mitchell JL, Lyons HS, Walker JK et al. The effect of GLP-1RA exenatide on idiopathic intracranial hypertensio](https://doi.org/10.1093/brain/awad003) | resume | 2023-05-02 |
| S17 | [Stefanou MI, Chatziralli I, Lambadiari V et al. Efficacy and safety of GLP-1 and dual GIP/GLP-1 receptor agoni](https://doi.org/10.1111/ene.70358) | resume | 2025-09 |
| S18 | [Tschopp R, König RS, Rejmer P, Paris DH. Health system support among patients with ME/CFS in Switzerland. J Ta](https://pmc.ncbi.nlm.nih.gov/articles/PMC9957780/) | resume | 2023 |
| S19 | [van der Worp HB, Hofmeijer J, Jüttler E et al. European Stroke Organisation (ESO) guidelines on the management](https://doi.org/10.1177/23969873211014112) | resume | 2021-06 |
| S20 | [Deutsches Ärzteblatt. Neue Leitlinie zur idiopathischen intrakraniellen Hypertension (S1-Leitlinie DGN, 9 mai ](https://www.aerzteblatt.de/nachrichten/102896/Neue-Leitlinie-zur-idiopathischen-intrakraniellen-Hypertension) | resume | 2019-05-09 |
| S21 | [ChEMBL CHEMBL689 — mannitol (C6H14O6, masse molaire 182,17 g/mol)](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL689/) | section | base ChEMBL v34 |

Première source lue : https://amiko.oddb.org/fr/fi?gtin=7680211910195 — Information professionnelle Diamox® : Indications, Posologie, Contre-indications, Interactions, Swisspeddose (texte intégral, mise à jour juillet 2026).

## Lacunes

- Aucune source suisse de recommandation ni de sémiologie pour l’HII, l’œdème cérébral ou l’engagement ; WebSearch « Revue Médicale Suisse hypertension intracrânienne engagement » sans article suisse.
- Ligne directrice DGN S1 « Intrakranieller Druck (ICP) » 2023 (AWMF 030-105) : PDF du registre AWMF renvoyé en HTML anti-robot, page DGN vide ; non lue. Syndromes topographiques d’engagement non sourcés.
- Ligne directrice DGN S1 HII (2019, 030-093) : seul le compte rendu de presse de l’Ärzteblatt a été lu [S20].
- ERC-ESICM 2025 : PDF obtenu par un miroir public (certifico.com), les sites de l’éditeur exigeant un défi JavaScript ; les signes ≤/≥ sont parfois illisibles dans l’extraction (cible de 37,5 °C, indice pupillaire neurologique non repris pour cette raison).
- ESO 2021 (infarctus expansif), Abbott 2023, IIH:WT, exénatide, méta-analyse GLP-1, EAN 2020, Schrör 2007, Rabiei 2016, Tschopp 2023 : résumés seuls.
- Aucune sensibilité ni spécificité des signes de l’HII dans les sources lues ; classification de Frisén non lue ; critères de Friedman 2013 (figure) non lus.
- Spécificités suisses non lues : directives ASSM sur la mort cérébrale, aptitude à la conduite après dérivation, assurance-invalidité pour l’encéphalomyélite myalgique.
- Syndrome de Reye : critères, biologie (ammoniémie, transaminases), traitement et épidémiologie suisse non lus ; corticoïdes et sérum salé hypertonique (doses) non lus.
- Figure de remplacement : Wikimedia Commons en HTTP 429 (tools/image_clo_finder.py) ; candidats limités aux figures CC BY 4.0 de S2 ; contrôle visuel de l’original non fait.
- Rendu à 390 px et captures (SEM-22, SEM-23) non réalisés dans cet audit ; lisibilité des SVG estimée par calcul.
- Formule de la pression de perfusion cérébrale non trouvée dans les sources lues : aucun calcul de pression de perfusion n’est proposé.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G93 — Autres affections du cerveau (N-05-Neurologie, S08) |
| Catégories traitées | G93.0 à G93.9, G93.80, G93.88 |
| Fichiers audités | 7 (118 665 octets), empreintes conformes |
| Constats | 10 MAJEUR, 9 MINEUR, 5 ENRICHISSEMENT, 0 BLOQUANT |
| Calculs | 451 relevés, 29/29 recalculés, 5 faux, 4 arrondis |
| Remplacements locaux proposés | 33, ancres uniques vérifiées par script |
| Sémiologie | absente → proposition complète (9 sections, 13 fenêtres) |
| Figures | 1 ANATOMIQUE_IA, 3 schémas non anatomiques |
| Alertes | algorithme pronostique et cibles post-arrêt à mettre à jour (ERC-ESICM 2025) ; topiramate chez la femme jeune ; aucune validation médicale humaine |
