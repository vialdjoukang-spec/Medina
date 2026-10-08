# Auto-revue interne — C-01-Cardiologie, 9 cours nouveaux du 8 octobre 2026

Auteur : sous-agent auto-réviseur de Claude (revue IA interne). Ce n'est ni l'audit croisé de Codex ni une validation médicale humaine. Aucun fichier de cours n'a été modifié.

Périmètre : I51, I73, I77, I85, I89, I95, I97, R00, R02 (`chapters/<CODE>/`), confrontés aux 21 cours existants du fragment et aux cours voisins cités (A41, M31, J18, etc.).

## 1. Bilan

| Gravité | Nombre |
|---|---|
| Bloquant | 0 |
| Majeur | 1 |
| Mineur | 11 |

### Contrôles sans anomalie

- **Couverture CIM.** `organisation/pile_fragments.json` compte 76 catégories. Chaque catégorie pointe vers un cours dont `covers` (`chapters.json`) la contient. Aucune catégorie n'est déclarée deux fois. Chaque sous-catégorie attendue est effectivement traitée dans le texte : I51.3–I51.81, I52, I73.0/.1/.8, I77–I79 (dont I77.6 et I78.0), I85, I86.0–I86.8, I88, I89, I95.0–I95.8, R03.0/R03.1, I97.0–I97.9, I98, I99, R00, R01, R02.
- **Liens `#/entry/<CODE>`** des 9 cours (A41, I00, I21, I30, I33, I34, I35, I44, I46, I47, I48, I49, I70, I71, I73, Q21). Tous visent un cours existant et thématiquement correct.
- **Mentions « cours Xnn »** : toutes visent un cours existant. Seules exceptions : A46, J90, B74 et L03, cités par I89 comme cours d'autres fragments encore à écrire (voir constat m6). Le renvoi de I51 vers « le cours I42 détaille la sarcoïdose cardiaque » est exact : I42 traite la sarcoïdose dans ses onglets a, b et c et dans ses fenêtres.
- **Cohérence chiffrée entre cours** (aucune contradiction trouvée) :
  - Atropine : 500 µg jusqu'à 3 mg (R00, I44, I46).
  - Adénosine : 6-12-18 mg, 3 mg par voie centrale (R00, I47).
  - Prophylaxie de l'endocardite : amoxicilline 2 g, 30–60 min avant le soin, 50 mg/kg chez l'enfant (R00, I33). Les alternatives de l'ESC 2023 (I77) concordent.
  - Colchicine et aspirine du syndrome post-péricardiotomie, colchicine contre-indiquée sous 30 mL/min (I97, I30).
  - Critères du rétrécissement aortique serré (R00, I35, ESC/EACTS 2025).
  - Définition de l'hypotension orthostatique ESC 2018 (I95, R00).
  - Critère du POTS ≥ 30/min (I95, I49).
  - Ischémie chronique menaçant le membre : pression d'orteil < 30 mmHg et ischémie depuis plus de 2 semaines (R02, I70).
  - Antithrombotiques de l'artériopathie : clopidogrel, ou aspirine avec rivaroxaban 2,5 mg × 2 (R02, I70).
  - Seuils tensionnels hors cabinet : I95 renvoie à I10, sans divergence.
  - Règle des 24 heures avant cardioversion d'une FA (R00, I48). Seul I97 s'en écarte (constat M1).
- **Doublons de contenu.** Tako-tsubo (I42 vs I51), syndrome post-péricardiotomie (I30 vs I97) et lymphœdème après mastectomie (I89 vs I97) sont recouverts sans contradiction. Les renvois sont explicites (« renvoie entièrement »).

### Affirmations à fort enjeu vérifiées

Les vérifications portent sur les sources primaires ou des sources suisses ; celles marquées † ont été vérifiées en ligne le 08.10.2026.

| Cours | Affirmation | Verdict |
|---|---|---|
| I85 | TIPS préemptif dans les 72 h (idéalement < 24 h) : Child C 10–13, B > 7 avec saignement actif, ou HVPG ≥ 20 mmHg ; âge < 75 ans, créatinine < 3 mg/dL, pas d'insuffisance cardiaque | Conforme à Baveno VIII (préversion acceptée, J Hepatol 2026, doi 10.1016/j.jhep.2026.07.030, énoncé 5.31 et figure) † |
| I85 | Hémoglobine cible 70–80 g/L ; vasoactif 2–5 j, 24 h possibles ; érythromycine 250 mg IV 30–90 min avant l'endoscopie | Conforme à Baveno VIII † |
| I85 | Terlipressine 1–2 mg/4–6 h, max 12 mg/24 h pendant 36 h puis 6 mg/24 h | Conforme à la fiche de la pharmacie des HUG (hug.ch/pharmacie, terlipressine) † ; d'autres résumés des caractéristiques du produit (RCP) européens diffèrent (Vidal : 48 h au plus) |
| I85 | Villanueva 2013 (921 patients, seuil 70 vs 90 g/L) ; García-Pagán 2010 (63 patients, survie à 1 an 86 % vs 61 %) ; PREDESCI (16 % vs 27 %) | Conforme aux publications |
| I95 | Midodrine (Gutron 10 mg/mL) : 7 gouttes ≈ 2,3 mg (30 gouttes/mL), 2 fois par jour, max 30 mg/j | Conforme (compendium.ch : 30 gouttes = 10 mg ; information professionnelle allemande : 7 gouttes ≈ 2,5 mg, max 30 mg/j) † |
| I95 | Hypotension orthostatique ≥ 20/10 mmHg en 3 min ou systolique < 90 mmHg ; forme initiale > 40/20 mmHg en 15 s ; hypertension de décubitus ≥ 150/90 | Conforme à l'ESC 2018 et aux consensus de 2011 et 2017 |
| R00 | Adénosine 6-12-18 mg ; atropine 0,5 → 3 mg ; isoprénaline 5 µg/min ; adrénaline 2–10 µg/min | Conforme à l'ERC et à l'ESC 2019 |
| R00 | Tachycardie sinusale inappropriée : repos > 100/min, moyenne sur 24 h > 90/min | Conforme à l'ESC 2019 |
| R00 | Amoxicilline 2 g, 30–60 min avant le soin | Conforme à l'ESC 2023 |
| I51 | Thrombus ventriculaire gauche : anticoagulation 3–6 mois (ESC 2023, IIa C), imagerie vers 3 mois | Conforme |
| I51 | Complications dans les 28 jours d'un infarctus codées I23 | Conforme à la CIM-10 |
| I51 | Rupture septale non opérée : « près de 80 % » de décès à 30 jours | Non confirmé, voir m9 |
| I77 | PATH-HHT : pomalidomide 4 mg/j, 144 patients, 2:1, 24 semaines | Conforme (NEJM 2024) |
| I77 | Bévacizumab 5 mg/kg ; aspirine 75–100 mg dans la dysplasie fibromusculaire | Conforme aux recommandations HHT 2020 et au consensus FMD 2019 |
| I77 | ESVS 2025 sur les artères et veines mésentériques et rénales | Existe (EJVES 2025;70:153-218, doi 10.1016/j.ejvs.2025.06.010) † |
| I97 | BASEL-PMI 8,9 % vs 1,5 % ; COPPS-2 19,4 % vs 29,4 % ; POISE (8 351 patients, 200 mg) ; délais P2Y12 3–5 / 5 / 7 j ; 6 mois après une angioplastie programmée et 12 mois après un SCA ; amiodarone préventive I A | Conforme à l'ESC 2022, à l'ESC 2024 FA et aux publications |
| I97 | Délai avant cardioversion de la FA postopératoire : 48 h | **Erreur, voir M1** |
| I89 | PATCH I : pénicilline V 250 mg × 2 pendant 12 mois, 22 % vs 37 % de récidives | Conforme |
| I89 | Chylothorax : triglycérides > 1,24 mmol/L et cholestérol < 5,18 mmol/L | Conforme |
| R02 | WIfI ischémie 3 : index ≤ 0,39, pression de cheville < 50 mmHg, pression d'orteil ou TcPO₂ < 30 mmHg | Conforme |
| R02 | Ischémie chronique menaçante non revascularisée : environ 22 % de décès et 22 % d'amputations à 1 an | Conforme aux GVG 2019 |
| R02 | Vancomycine 15–20 mg/kg/8–12 h (charge 25–30 mg/kg) ; amoxicilline-clavulanate 2,2 g × 3–4 | Conforme aux informations professionnelles citées |
| I73 | Nifédipine LP 30 → 120 mg ; sildénafil 20 mg × 3 ; iloprost 0,5–2 ng/kg/min 6 h/j ; bosentan 62,5 → 125 mg × 2 | Conforme aux informations professionnelles citées |

## 2. Tableau des constats

| # | Cours | Fichier | Extrait | Problème | Gravité | Correction proposée (texte de remplacement exact) | Source |
|---|---|---|---|---|---|---|---|
| M1 | I97 | `chapters/I97/I97_b.html` (paragraphe sur la fibrillation postopératoire, îlot 2) | « Une cardioversion non urgente d’une fibrillation de 48 heures ou plus suit les règles habituelles : thrombus exclu par ETO, ou trois semaines d’anticoagulation. » | Le seuil de 48 h vient de l'ESC 2020. L'ESC 2024 FA, que I97 cite pourtant dans ses référentiels et dont il utilise le score CHA₂DS₂-VA, l'a abaissé à 24 h. I48 et R00 appliquent la règle des 24 heures : la contradiction entre cours est chiffrée et touche le risque embolique. | **Majeur** | « Une cardioversion non urgente d’une fibrillation de plus de 24 heures, ou de durée inconnue, suit les règles habituelles de l’ESC 2024 : thrombus exclu par ETO, ou trois semaines d’anticoagulation préalable, comme dans le cours I48. » | ESC 2024 FA (Van Gelder et al., Eur Heart J 2024) ; `chapters/I48/` (« Durée > 24 heures ou inconnue : trois semaines d’anticoagulation ou ETO ») |
| M1 bis | I97 | `chapters/I97/I97_b.html` (dernier îlot, « Paramètres clés ») | « cardioversion programmée après ETO ou trois semaines d’anticoagulation si ≥ 48 heures. » | Même erreur dans les paramètres clés. | **Majeur** (même constat) | « cardioversion programmée après ETO ou trois semaines d’anticoagulation si la fibrillation dure plus de 24 heures ou depuis une durée inconnue. » | Idem |
| m1 | I97 | `chapters/I97/I97_d.html` (encadré « À retenir » sur les antithrombotiques) | « Aspirine poursuivie après stent ; P2Y12 arrêtés 3 à 5, 5 ou 7 jours avant selon la molécule ; AOD sans relais par héparine et à pleine dose à la reprise ; reprise des antiplaquettaires dans les 48 heures. » | Encadré en phrases nominales, interdit par STYLE_REDACTION § 2 et § 3. | Mineur | « À retenir. L’aspirine est poursuivie chez le patient porteur d’un stent. Si un inhibiteur P2Y12 doit être arrêté, le ticagrélor s’arrête 3 à 5 jours avant, le clopidogrel 5 jours et le prasugrel 7 jours. Les AOD s’interrompent sans relais par héparine et reprennent à pleine dose. Les antiplaquettaires interrompus reprennent dans les 48 heures si l’hémostase le permet. » | ESC 2022 (chirurgie non cardiaque) |
| m2 | R02 | `chapters/R02/R02_c.html` (« À retenir » de l'imagerie) | « Écho-Doppler d’abord, puis angiographie incluant la cheville et le pied avant toute décision de non-revascularisation. » | Première phrase nominale. | Mineur | « Le médecin demande d’abord un écho-Doppler, puis une angiographie qui inclut la cheville et le pied avant toute décision de non-revascularisation. » | STYLE_REDACTION § 2 |
| m3 | R02 | `chapters/R02/R02_c.html` (« À retenir » de l'histologie) | « Coagulation pour la gangrène sèche, liquéfaction pour la gangrène humide, lyse toxinique avec peu de polynucléaires pour la gangrène gazeuse ; pas de granulation sans perfusion. » | Phrase nominale. | Mineur | « La gangrène sèche correspond à une nécrose de coagulation, la gangrène humide à une nécrose de liquéfaction. Dans la gangrène gazeuse, les toxines lysent les tissus et laissent peu de polynucléaires. Sans perfusion, aucun tissu de granulation ne se forme. » | STYLE_REDACTION § 2 |
| m4 | R02 | `chapters/R02/R02_c.html` (« À retenir » de la microbiologie) | « Cocci à Gram positif dans l’infection légère, flore polymicrobienne avec anaérobies dans la nécrose ischémique, toxines clostridiennes dans la gangrène gazeuse. » | Phrase nominale. | Mineur | « Les cocci à Gram positif dominent l’infection légère. La nécrose ischémique abrite une flore polymicrobienne avec anaérobies. La gangrène gazeuse est due aux toxines des clostridies. » | STYLE_REDACTION § 2 |
| m5 | I95 | `chapters/I95/I95_a.html` (3 occurrences), `chapters/I95/I95_b.html` (1 occurrence) | « Le chapitre suivant mesure… », « Le chapitre suivant classe… », « Le chapitre suivant organise… », « Le chapitre final rassemble… » | « Chapitre » y désigne un îlot. Dans MEDINA, un chapitre est un cours entier : le lecteur peut croire à un renvoi vers un autre cours. | Mineur | Remplacer respectivement par « L’îlot suivant mesure la fréquence de ces situations. », « L’îlot suivant classe les causes selon ces maillons. », « L’îlot suivant organise ces résultats en démarche diagnostique. » et « Le dernier îlot rassemble les critères formels et les paramètres à surveiller. » | Contrat HTML (CLAUDE.md, règles 2 et 4) |
| m6 | I89 | `chapters/I89/I89_a.html`, `I89_b.html`, `I89_pop1.html` | « traitée dans B74 — Filariose (I-03-Infectiologie) » ; « relève de L03 — Phlegmon (D-16-Dermatologie) » | B74 et L03 n'ont pas encore de cours. A46 et J90 sont correctement annoncés comme « futur cours » ; B74 et L03 sont présentés comme existants. | Mineur | « traitée dans le futur cours B74 — Filariose (I-03-Infectiologie) » ; « relève du futur cours L03 — Phlegmon (D-16-Dermatologie) » | `organisation/pile_fragments.json` (`course: null` pour B74 et L03) |
| m7 | I77, I85 | `chapters/I77/I77_a.html` (3), `I77_b.html` (2), `I77_c.html` (4), `I77_d.html` (2), `chapters/I85/I85_a.html`, `I85_c.html` (2), `I85_d.html` | « Le lecteur regarde d’abord la colonne… », « Le lecteur commence par la rénine », « le lecteur cherche d’abord si le foie lui-même est malade » | Formule centrée sur la lecture du cours plutôt que sur la décision clinique, proche des formules de fabrication proscrites (STYLE_REDACTION § 3). Les autres cours écrivent « Le médecin… ». | Mineur | Remplacer « Le lecteur » ou « le lecteur » par « Le médecin » ou « le médecin » dans chaque occurrence. Exemple : « Le médecin cherche d’abord si le foie lui-même est malade… » | STYLE_REDACTION § 3 et § 4 |
| m8 | R02 | `chapters/R02/R02_c.html` (tableau des examens) | « Index orteil-bras ≥ 0,70 ; pression ≥ 60 mmHg pour l’ischémie WIfI 0 » | La cellule juxtapose deux référentiels : le seuil de 0,70 vient de l'IWGDF 2023 (artériopathie moins probable) et 60 mmHg du WIfI. Le lecteur peut croire que 0,70 est un critère WIfI. Le grade 0 du WIfI repose sur un index de cheville ≥ 0,80, une pression de cheville > 100 mmHg et une pression d'orteil ou une TcPO₂ ≥ 60 mmHg. | Mineur | « Index orteil-bras ≥ 0,70 : artériopathie moins probable (IWGDF 2023) ; pression d’orteil ≥ 60 mmHg : ischémie WIfI de grade 0 » | IWGDF 2023 ; SVS WIfI (Mills 2014) |
| m9 | I51 | `chapters/I51/I51_a.html`, `chapters/I51/I51_pop4.html` | « près de 80 % à 30 jours pour une communication interventriculaire non opérée » | Chiffre non retrouvé dans la déclaration AHA 2021 (Damluji, Circulation 2021;144:e16) au cours de cette revue. Les séries récentes rapportent environ 90 % ou plus de décès à 30 jours sous traitement médical seul (93,6 % dans une série monocentrique de 127 patients, Front Cardiovasc Med 2021). L'erreur n'est pas démontrée, mais la valeur paraît sous-estimée. | Mineur (à vérifier) | Si la vérification en texte intégral de l'AHA 2021 ne confirme pas 80 % : « une mortalité supérieure à 90 % à 30 jours pour une communication interventriculaire non opérée selon les séries publiées » ; sinon, conserver et citer la page exacte. | Damluji et al., Circulation 2021 ; Front Cardiovasc Med 2021 (doi 10.3389/fcvm.2021.679148) |
| m10 | I73, I77 vs I10, I71, I35, M31, I97 | `chapters/I73/*`, `chapters/I77/*` | Asymétrie de pression entre les bras « > 15 mmHg » (I73, I77) ; « ≥ 10 mmHg » (I10) ; « > 20 mmHg » (I35, I71) ; « > 10 mmHg » (M31) ; « 15 à 20 mmHg » (I97) | Seuils hétérogènes entre cours pour un même signe. Leurs usages diffèrent : choix du bras de référence, sténose subclavière, dissection. Aucun cours n'explique cette différence, et le lecteur voit une contradiction. | Mineur | Dans I73 et I77, après le seuil, ajouter : « Ce seuil de 15 mmHg vise la sténose sous-clavière ; le cours I10 retient 10 mmHg pour choisir le bras de référence, et une asymétrie supérieure à 20 mmHg avec douleur thoracique fait évoquer une dissection aortique (cours I71). » | ESC 2024 HTA ; ESC 2024 artériopathies périphériques |
| m11 | I51, I73, I95, I97, R00, R02 | multiples | « cours I42 », « chapitre I70 », « cours I10 », « cours I48 »… | Les consignes (CLAUDE.md, organisation des fragments) exigent la forme **code — intitulé (libellé du fragment)** pour nommer un cours. I77, I85 et I89 la respectent ; les autres cours emploient majoritairement le code seul, et I73 écrit « chapitre I70 ». Les mentions ne sont pas cliquables, contrairement aux liens `#/entry/`. | Mineur | À la première mention dans chaque onglet, écrire par exemple « I70 — Athérosclérose périphérique, artériopathie des membres inférieurs (C-01-Cardiologie) » ; les mentions suivantes peuvent garder « cours I70 ». Dans I73, remplacer « chapitre I70 » par « cours I70 ». | CLAUDE.md, « Organisation des fragments » |
| m12 | 9 cours | `chapters/<CODE>/<CODE>_a.html` (bandeau) | Bandeau d'en-tête | Hétérogénéité de forme : le libellé « C-01-Cardiologie » figure seulement dans I73, R00 et R02. R02 (gangrène) est classé « Cœur et hémodynamique » alors que son contenu est vasculaire. I89 annonce couvrir aussi I97.2 et I97.8, alors que `chapters.json` attribue I97 au cours I97 (renvoi cohérent, mais deux déclarations). | Mineur | Ajouter « · C-01-Cardiologie » au bandeau des 6 autres cours. Pour R02, écrire « Vaisseaux et microcirculation ». Pour I89, écrire « couvre I88, I89 ; lymphœdèmes après actes médicaux (I97.2, I97.8) traités ici sur renvoi du cours I97 ». | `organisation/fragments.json` ; `chapters.json` |

## 3. Style : observations générales

- Aucune formule de fabrication proscrite (« cet îlot présente », « cette section », « il est important de », « nous allons ») n'a été trouvée dans les 9 cours. Seule exception : les « Le lecteur… » de I77 et I85 (m7).
- Les épilogues « À retenir » se terminent souvent par une phrase de transition (« L’îlot suivant… », « La partie suivante… »). STYLE_REDACTION § 3 l'autorise, puisque l'épilogue annonce le lien avec la partie suivante. Plusieurs transitions n'apportent toutefois aucune information : I77 (8 occurrences), R02 (6), I85 et I89 (4 chacun). Les ramener à une phrase qui porte le lien causal allégerait le texte, par exemple « La physiopathologie explique ces chiffres » plutôt que « L’îlot suivant aborde… ». Aucune n'est bloquante.
- Les seules phrases nominales relevées dans les encadrés sont m1 à m4. Les cellules de tableau courtes restent conformes, car les tableaux examinés sont introduits et commentés.

## 4. Limites de cette revue

- Revue IA interne : elle ne remplace ni l'audit croisé de Codex ni une validation par un médecin.
- La vérification en ligne a porté sur un échantillon d'affirmations à fort enjeu par cours, pas sur chaque phrase.
- Le texte intégral de l'AHA 2021 et l'information professionnelle suisse de Marcoumar (dose de charge du jour 1 dans I51) n'ont pas pu être lus. Aucune erreur n'est démontrée sur ces deux points.
- Les sous-codes CIM-10-GM détaillés cités (I72.6, I77.80, I97.20, I97.83) n'ont pas été rapprochés du texte BfArM 2024 dans cette revue.
