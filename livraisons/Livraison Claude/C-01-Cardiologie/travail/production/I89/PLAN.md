# PLAN — I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques

Architecte : Claude, 07.10.2026. Fragment **C-01-Cardiologie**, vague 9, système « Vaisseaux et microcirculation » (libellé du catalogue : « Angiologie et autres affections circulatoires »).
Ce plan est le contrat commun des quatre rédacteurs (A, B, C, D). Aucun rédacteur ne le modifie. En cas de contradiction entre ce plan et une source primaire, le rédacteur suit la source, écrit la correction dans son texte et la signale dans `reserves_<onglet>.txt`.

---

## 0. Ce qu’il faut lire avant d’écrire

1. `TACHE_NOUVEAU_COURS.md` (dossier parent), `CHAPTER_SPEC.md`, `docs/STYLE_REDACTION.md`, `docs/collaboration/FRAGMENT_01_PRIORITE.md`, `travail/justification/CONSIGNES.md`.
2. Modèles de forme : `chapters/I80/` (en-tête, onglets, barre des sciences, fermetures) et `chapters/I48/I48_pop2.html` (fenêtres justifiées avec `<div class="lab">`). Imiter la forme, ne copier aucune phrase.
3. `src/INDEX.txt` : carte des sources téléchargées. Toute donnée chiffrée vient de la section 5 de ce plan ou d’une vérification personnelle dans `src/` ou sur PubMed.

**Confidentialité.** Aucun service externe ne reçoit l’adresse e-mail ni le nom du propriétaire (pas d’Unpaywall, pas de paramètre `email=` dans les E-utilities).

---

## 1. Identité du cours

| Élément | Valeur exacte |
|---|---|
| Identifiant du gabarit | `<template id="ch-I89"><div class="chap">` |
| Ligne de code (div.code) | `I89 · couvre I89 et les lymphœdèmes après actes médicaux (I97.2, I97.8) · CIM-10-GM 2024 · Vaisseaux et microcirculation` |
| Titre h1 | `Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques` |
| Statut (span.status) | `Rédaction du 07.10.2026 · référentiels ISL 2023, AWMF S2k 058-001 (2017), OPAS annexe 1 et LiMA (édition du 1.7.2026) · non validé par une revue humaine` |
| Onglet 1 | `⚕ Pathologie et prise en charge` (panneau `pA`) |
| Onglet 2 | `🔬 Examens complémentaires` (panneau `pE`) |
| Onglet 3 | `⚛ Sciences fondamentales spécialisées` (panneau `pS`) |
| Onglet 4 | `💊 Pharmacologie du lymphœdème et du chyle` (panneau `pP`) |
| Entrée proposée pour `chapters.json` (orchestrateur) | `{"code":"I89","covers":["I89","I97"],"title":"Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques","integrated":true,"wave":9,"added":"2026-10-xx"}` |
| Renvois proposés (orchestrateur, `shell/data.py`) | I88 — Lymphadénite non spécifique : articulée dans I89 (îlot 13) ; cours complet « Adénopathies » à créer (R59, I88, L04). Q82.0 — Lymphœdème héréditaire : traité cliniquement dans I89 (catégorie Q82 rattachée au système Peau). J94.0 — Épanchement chyleux : mécanisme et diagnostic dans I89 (îlot 12) ; prise en charge pleurale complète dans le futur cours des épanchements pleuraux (P-02-Pneumologie). |

Le cours se nomme toujours « I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques ». Le lymphœdème en est le centre parce qu’il représente l’essentiel des sous-codes (I89.00 à I89.09) et des situations cliniques de l’examen fédéral.

---

## 2. Arbitrage du périmètre CIM (justification)

Source des intitulés : catalogue intégré `shell/medina_front.html` (CIM-10-GM 2024, BfArM). La cartographie CIM-11 n’est pas établie : aucun rédacteur ne cite de code CIM-11.

| Code | Intitulé CIM-10-GM 2024 | Décision | Justification |
|---|---|---|---|
| I89.0- (I89.00 à I89.09) | Lymphœdème, non classé ailleurs ; stades I à III, membres ou autre localisation (tête, cou, paroi thoracique, région génitale) ; I89.08 « stade de latence » ; inclut la lymphangiectasie | **Traité en entier** (centre du cours) | Les stades du code reprennent ceux de l’ISL ; le stade de latence correspond au stade 0. La lymphangiectasie intestinale primaire (maladie de Waldmann) relève de I89.0 par l’inclusion « Lymphangiectasie ». |
| I89.1 | Lymphangite chronique, subaiguë ou sans précision | **Traité** (îlots 1 et 11) | La lymphangite aiguë est exclue (L03.-) : elle est infectieuse et appartient aux infections cutanées. La forme chronique résulte surtout d’épisodes répétés avec lymphangiosclérose (ISL 2023). |
| I89.8 | Autres atteintes non infectieuses précisées : chylocèle non filarienne, réticulose lipomélanique ; codes additionnels pour fistule lymphatique cutanée, lymphocèle, kyste lymphatique dermique, reflux chyleux | **Traité** (îlots 12 et 13) | Ces atteintes partagent le mécanisme de fuite ou de reflux lymphatique. La réticulose lipomélanique (lymphadénopathie dermatopathique) est présentée dans l’îlot 13 avec les adénopathies. |
| I89.9 | Atteinte non infectieuse des vaisseaux et ganglions lymphatiques, sans précision | Mention (îlot 1) | Code de défaut ; le cours apprend à préciser le diagnostic. |
| I97.2- | Lymphœdème après mastectomie (partielle), stades I à III | **Traité** (cas fil rouge) | Le lymphœdème après traitement d’un cancer est la forme la plus fréquente dans les pays industrialisés. Le codage correct est un piège d’examen : un lymphœdème après tumorectomie et curage se code I97.2x, non I89.0x. |
| I97.80 à I97.88 | Lymphœdème après acte diagnostique ou thérapeutique (cervical, axillaire, inguinal, urogénital, autres) | **Traité** | Même mécanisme que I97.2- (destruction chirurgicale ou radique du drainage). |
| I97.0, I97.1 | Syndrome post-cardiotomie ; troubles fonctionnels après chirurgie cardiaque | **Renvoi** | I97.0 est déjà traité dans I30 (péricardites) ; I97.1 relève de I50. |
| I97.89, I97.9 | Autres troubles circulatoires après actes médicaux | Mention | Sans contenu lymphatique propre. |
| Q82.0- | Lymphœdème héréditaire (système Peau dans le catalogue) | **Traité cliniquement**, catégorie non couverte | Le lymphœdème primaire est au centre de la demande ; la catégorie Q82 contient aussi des maladies cutanées sans rapport. |
| E88.20 à E88.22 | Lipœdème, stades I à III | **Diagnostic différentiel détaillé**, non couvert | Le catalogue exige de coder séparément un lipœdème associé. Le traitement complet relève d’un futur cours métabolique. |
| J94.0 | Épanchement chyleux (système Poumon) | **Îlot dédié** (îlot 12), non couvert | Le chylothorax est une atteinte du canal thoracique. Le mécanisme et le diagnostic biochimique sont enseignés ici ; la gestion pleurale fine est renvoyée au cours P-02. |
| I88.- | Lymphadénite non spécifique (I88.0 mésentérique, I88.1 chronique, I88.8) | **Articulation** (îlot 13), non couvert | Consigne : articuler sans traiter en entier. Le cours enseigne la conduite devant une adénopathie dans un territoire lymphœdémateux. |
| A46, L03.- | Érysipèle, phlegmon | Complication (îlot 11) ; doses de l’épisode aigu renvoyées au cours d’infectiologie | Les posologies suisses de l’épisode aigu n’ont pas été vérifiées dans une source suisse primaire (réserve R4). |
| B74.- | Filariose | Étiologie mondiale (îlot 4) ; traitement renvoyé à l’infectiologie | Données OMS 2024 vérifiées. |
| I83, I87 | Varices, insuffisance veineuse | Différentiel (îlot 7) ; renvoi au cours I83 | I83 est produit en parallèle par Claude. |

**Recommandation ESC 2026.** Aucune recommandation ESC 2026 ne porte sur le système lymphatique (recommandations du 28.08.2026 : insuffisance cardiaque, réadaptation cardiaque, maladie cardiovasculaire et maladie rénale chronique ; 5e définition universelle de l’infarctus). La seule comparaison utile concerne l’œdème d’origine cardiaque : la fenêtre `i89-oed-systemique` (B) indique entre parenthèses que l’ESC 2026 parle d’« insuffisance cardiaque décompensée » et regroupe les fractions d’éjection en deux phénotypes (réduite &lt; 50 %, préservée ≥ 50 %), contre trois phénotypes dans l’ESC 2021 et sa mise à jour 2023. Aucune autre fenêtre comparative ESC n’est créée.

---

## 3. Répartition du travail

| Rédacteur | Fichiers écrits (dans `I89/brouillon/`) | Contenu | Volume visé |
|---|---|---|---|
| **A** | `I89_a.html`, `I89_pop1.html`, éventuellement `../glossary_i89_a.py` | En-tête, 4 onglets, ouverture de `pA`, sommaire complet de `pA` (îlots 0 à 16), îlots `i89-0` à `i89-6`, Figure 1, Pareto `pareto-i89-bases`, 9 fenêtres | texte ≈ 2 300 mots ; fenêtres ≈ 1 700 mots |
| **B** | `I89_b.html`, `I89_pop2.html`, `../glossary_i89_b.py` | Îlots `i89-7` à `i89-16`, Figure 2, 2 quiz, références, fermeture de `pA`, Pareto `pareto-i89-pec`, 13 fenêtres | texte ≈ 3 200 mots ; fenêtres ≈ 2 900 mots |
| **C** | `I89_c.html`, `I89_pop3.html`, `../glossary_i89_c.py` | Panneau `pE` (îlots `i89-e-1` à `i89-e-8`, 5 quiz, Figure 3) et panneau `pS` (4 disciplines, Figure 4), Pareto `pareto-i89-exam` et `pareto-i89-sciences`, 9 fenêtres | texte ≈ 3 400 mots ; fenêtres ≈ 2 000 mots |
| **D** | `I89_d.html`, `I89_pop4.html`, `../glossary_i89_d.py` | Panneau `pP` (îlots `i89-p-1` à `i89-p-6`), 1 quiz, fermeture `</div></template>`, Pareto `pareto-i89-pharma`, 7 fenêtres | texte ≈ 1 200 mots ; fenêtres ≈ 1 500 mots |

Total visé : texte principal ≈ 10 000 mots, fenêtres ≈ 8 000 mots. Ce sont des repères, non des objectifs : aucune phrase de remplissage.

### 3.1 Frontières HTML exactes

- **A** commence par `<template id="ch-I89"><div class="chap">`, puis l’en-tête et les onglets copiés sur `chapters/I80/I80_a.html` (mêmes attributs `role`, `aria-controls`, `data-p`, `aria-selected`), puis `<div class="panel" id="pA">`, `<nav class="toc ui">` (sommaire des 17 îlots avec les titres exacts de la section 6), `<div class="chap-body">`. A termine par la balise `</section>` de `i89-6` (le bouton `pareto-i89-bases` est juste avant cette balise).
- **B** commence par `<section class="ilot" id="i89-7">` et termine par `</section>` de `i89-16`, puis `</div><div class="pager ui"><button class="prev">← Îlot précédent</button><span></span><button class="next">Îlot suivant →</button></div></div>` (ferme `chap-body` et `pA`).
- **C** commence par `<div class="panel" id="pE" hidden>` et termine `pE` comme `I80_c.html` (pager puis `</div>`), puis ouvre `<div class="panel" id="pS" hidden><div class="sci-bar ui" role="tablist">` (quatre boutons, icônes SVG copiées de I80) et `<div class="chap-body sci-body">`. C termine par `</section></div></div></div>` (ferme la dernière section, le dernier `div.sci`, `sci-body`, `pS`).
- **D** commence par `<div class="panel" id="pP" hidden>` et termine par `</section>`, `</div><div class="pager ui">…</div></div>` puis `</div></template>`.

### 3.2 Règles communes de rédaction (rappel ciblé)

- Phrases courtes et complètes ; jamais de phrase nominale ni d’infinitif injonctif, y compris dans les encadrés, cellules longues et rétroactions de quiz. Chaque îlot : annonce du problème médical → développement du normal au pathologique → encadré `<div class="key"><b>À retenir.</b> …</div>`.
- Aucun métadiscours : « cet îlot », « ce cours », « le lecteur », « nous verrons », « cette fenêtre » sont interdits.
- Chaque tableau est précédé d’une question clinique et suivi d’un paragraphe de lecture avec un exemple de patient.
- Chaque affirmation porte son pourquoi (mécanisme → conséquence → décision). Une association n’est jamais présentée comme une causalité (exemple : l’IMC élevé est associé au risque de lymphœdème ; l’effet d’une perte de poids n’est que faiblement démontré, ISL 2023).
- Distinguer **recommandation** (ISL, AWMF), **résultat d’essai** (Thomas 2013, Webb 2020…) et **règle de remboursement** (OPAS, LiMA).
- Mots verts : `<button class="w" data-k="i89-…">libellé (destination annoncée)</button>`. Chaque clé existe dans un `template data-pop`. Clés nouvelles toutes préfixées `i89-`. Aucune réutilisation des clés d’autres cours.
- Fenêtres : 1 500 à 3 000 caractères le plus souvent (4 000 au maximum). Structure imposée :
  `<template data-pop="i89-…" data-title="Titre"><div class="lab">Réponse directe</div><p>…</p><div class="lab">Mécanisme</div><p>…</p><div class="lab">Conséquence clinique</div><p>…</p><div class="lab">Limites</div><p>…</p><div class="lab">Source</div><p>Auteur et al., revue année ; ou ISL 2023, section …</p></template>`.
  Les intitulés peuvent varier (« Technique », « Lecture », « Piège ») si la réponse directe vient en premier et si la source termine la fenêtre. Au plus deux renvois `<button class="w">` par fenêtre, vers des clés de ce plan.
- Pareto : `<button class="pareto-btn ui" data-k="pareto-i89-…">▲ Loi de Pareto — …</button>` ; le gabarit commence par `<p class="ratio" data-cover="ids"></p>` puis une `<ul>` de phrases complètes.
- Figures : `<figure><svg viewBox="…" role="img" aria-label="…" font-family="Georgia,serif" font-size="11">` noir et blanc (`#222`, gris `#bbb` au plus), puis `<figcaption>Figure n — …</figcaption>`. La figure est annoncée avant et lue après. Aucun sigle hors glossaire dans le SVG.
- Quiz : `<div class="quiz ui"><p>Cas…</p><button data-ok="1">…</button><button data-ok="0">…</button><button data-ok="0">…</button><p class="fb" hidden>explication complète</p></div>`.
- Typographie : apostrophe ’, guillemets « », espace insécable avant % et unités si possible ; « /jour » et non « /j » ; « par voie intraveineuse », jamais « IV ».
- Classes : liste fermée de `CHAPTER_SPEC.md` seulement. Aucun style en ligne. Identifiants préfixés `i89-`.

### 3.3 Mots et sigles interdits (collisions ou absences du glossaire)

| Ne pas écrire | Écrire | Raison |
|---|---|---|
| PATCH, PATCH I | « l’essai de Thomas et al. (2013) » | La clé PATCH désigne déjà un essai d’hydroxychloroquine (glossaire I44). |
| CIM seul | CIM-10-GM ou CIM-11 | Clé absente. |
| CDT, TDC, CDP, KPE | thérapie décongestive complexe | Sigles absents ; TDC désignerait aussi la constante diélectrique tissulaire. |
| MLD, DLM | drainage lymphatique manuel | Absents. |
| LVA, VLNT, LLA, ILR | anastomose lymphaticoveineuse ; transfert (ou transplantation) de ganglions lymphatiques vascularisés ; reconstruction lymphatique immédiate | Absents. |
| BCRL | lymphœdème après cancer du sein | Absent. |
| TVP, EP, AOMI, IPS, ITB | thrombose veineuse profonde ; embolie pulmonaire ; artériopathie oblitérante des membres inférieurs ; index de pression systolique (forme de I70) | Absents. |
| TG, TCM, MCT | triglycérides ; triglycérides à chaîne moyenne | Absents. |
| LAM | lymphangioléiomyomatose | Absent (et ambigu). |
| ALAT, ASAT, NFS, FT4, SAI, NCA | transaminases ; formule sanguine ; thyroxine libre ; écrire l’intitulé complet | Absents. |
| 99mTc, Tc-99m | technétium 99m | Serait signalé comme sigle. |
| Kaposi-Stemmer, Nonne-Milroy, Gorham-Stout, Parkes-Weber | signe de Stemmer ; maladie de Milroy ; maladie de Gorham ; écrire autrement | Éponymes composés absents du glossaire. |
| PREVENT, MILES, ALERT (noms d’essais ou de programmes) | « essai randomisé international de Ridner et al. (2022) », « essai de McCormack et al. (2011) », « série australienne de 2024 » | Clés absentes ; non nécessaires. |
| DXA, MRL, NIRF, LAS, PSM, LYMQOL, ICF | écrire en toutes lettres | Absents. |

Sigles disponibles (dépôt ou `glossary_i89.py`) : ISL, AWMF, S2k, ESC, ESVS, OMS, OFSP, LAMal, OPAS, LiMA, IMC, IRM, TDM, TEP-TDM, FDG, SPECT, CRP, LDH, NT-proBNP, BNP, TSH, DFG, IgG, ADN, CD4, Th2, IL-4, IL-13, TGF-β, mTOR, CYP3A4, AINS, VIH, AMAROS, PAL, LYMPHA, ICG, BIS, L-Dex, VEGF, VEGF-C, VEGF-D, VEGFR-3, FLT4, FOXC2, CCBE1, FAT4, GJC2, PIEZO1, GATA2, SOX18, PROX1, LYVE-1, PIK3CA, RASA1, TSC1, TSC2, CD31, PECAM-1, ERG, MYC, D2-40, CEAP, CLOVES, Stewart-Treves, Klippel-Trénaunay, Q82.0, E88.2, E88.20, E88.21, E88.22, J94.0, L03.1, L98.4, B74.0, R59.0, R59.9 ; tous les codes « I » décimaux (I89.00, I97.20…) et les codes sans décimale (L03, A46, B74, I88) sont acceptés par le moteur.

Tout sigle nouveau d’un rédacteur va dans `glossary_i89_<a|b|c|d>.py` (format de `glossary_i89.py`) et doit être vérifié : la clé ne doit pas exister ailleurs avec un autre sens.

---

## 4. Cas fil rouge (fictif, chiffré, cohérent pour les quatre onglets)

**Mme R., 52 ans**, enseignante, droitière.

| Temps | Données (ne pas modifier) |
|---|---|
| Il y a 20 mois | Cancer du sein gauche. Tumorectomie gauche et curage axillaire de niveaux I et II : 16 ganglions retirés, 3 envahis. Chimiothérapie adjuvante comprenant du docétaxel. Radiothérapie du sein et de la région sus-claviculaire gauche. Hormonothérapie par létrozole en cours. Mesures de référence préopératoires : volume du bras gauche 2 480 mL, du bras droit 2 500 mL. |
| Consultation initiale (mois 0 du cas) | Depuis 4 mois : lourdeur et tension du bras gauche, bague serrée le soir, manche serrée. La gêne diminue nettement après une nuit. Aucune fièvre. Poids 82 kg, taille 1,63 m, IMC 30,9 kg/m² (poids préopératoire 81 kg). Pression artérielle 132/80 mmHg, fréquence cardiaque 72/min, température 36,8 °C. Godet net à l’avant-bras. Signe de Stemmer négatif à la main. Peau normale. Aucune adénopathie sus-claviculaire ni axillaire palpable. Aucune circulation veineuse collatérale thoracique. Examen neurologique du membre normal. |
| Mesures du jour | Volume calculé (circonférences tous les 4 cm, formule du tronc de cône) : bras gauche 2 950 mL, bras droit 2 500 mL. Excès absolu 450 mL ; excès relatif 450 / 2 500 = **18 %** → sévérité **minimale** (> 5 % et &lt; 20 %, ISL 2023). Stade **ISL I** (réduction à l’élévation, godet). Code **I97.20** (lymphœdème après mastectomie partielle avec lymphadénectomie, stade I). |
| Bilan | Écho-Doppler veineux du membre supérieur gauche normal (pas de thrombose axillo-sous-clavière). Aucune imagerie lymphatique : le diagnostic est clinique dans ce contexte typique (ISL 2023). Aucun signe d’alarme de récidive. |
| Traitement initial | Manchon de compression de classe 2 à maillage circulaire (LiMA 17.02, indication « lymphœdème stade 1 »), soins cutanés, éducation, programme d’exercice progressif (au moins 150 minutes par semaine d’activité modérée mixte, ISL 2023), objectif pondéral. Drainage lymphatique manuel non indispensable à ce stade. |
| 6 mois plus tard | Excès 6 % ; port quotidien du manchon. |
| Mois 10 | **Érysipèle** du bras gauche : frissons, température 39,1 °C, placard érythémateux chaud et douloureux, CRP 148 mg/L. Antibiothérapie antistreptococcique ; compression suspendue jusqu’à l’effet de l’antibiotique (AWMF 2017), puis reprise. Intertrigo absent ; petite plaie de jardinage au dos de la main. |
| Mois 18 | Deuxième érysipèle. Discussion d’une prophylaxie par pénicilline orale (pénicilline V 250 mg deux fois par jour pendant 12 mois dans l’essai de Thomas et al. 2013, réalisé sur des érysipèles de jambe : extrapolation au bras à signaler). |
| Mois 30 | Excès 24 % (sévérité modérée), consistance plus ferme, godet moins net : **stade ISL II**. Code **I97.21**. Thérapie décongestive complexe phase I (drainage lymphatique manuel, bandages multicouches peu élastiques, exercices, soins) puis manchon plat sur mesure (LiMA 17.15). |
| Mois 44 | Malgré 12 mois de thérapie décongestive conforme et documentée, la gêne fonctionnelle persiste. Lymphographie au vert d’indocyanine : vaisseaux linéaires à l’avant-bras, reflux dermique de type « éclaboussure » au bras. Discussion d’une anastomose lymphaticoveineuse (OPAS annexe 1 : garantie préalable spéciale de l’assureur). |

Rôles : A présente le cas (îlot 0), l’anamnèse et l’examen ; B l’utilise pour le diagnostic, la thérapie, les infections, la chirurgie, le suivi et le cas récapitulatif (îlot 15) ; C pour la fiche de calcul du volume et le quiz 1 ; D pour la prophylaxie par pénicilline et le quiz de pharmacologie.

---

## 5. Faits clés vérifiés (seuls chiffres autorisés sans nouvelle vérification)

| N° | Fait | Valeur exacte | Source vérifiée (fichier dans `src/`) |
|---|---|---|---|
| F1 | Stades | Stade 0 latent (transport altéré, pas de gonflement visible, peut précéder de mois ou d’années) ; stade I : liquide relativement riche en protéines, diminue à l’élévation, godet possible ; stade II : élévation seule le réduit rarement, godet net, puis godet moins net avec graisse et fibrose ; stade III : éléphantiasis, godet souvent absent, altérations trophiques (acanthose, épaississement, verrucosités). Un membre peut présenter plusieurs stades. | ISL 2023, section II (`isl_one.txt`) |
| F2 | Sévérité | Excès de volume minimal > 5 % et &lt; 20 % ; modéré 20 à 40 % ; sévère > 40 %. Certains centres : > 5–10 % minimal, > 10–&lt; 20 % léger. | ISL 2023, section II |
| F3 | Lymphœdème infraclinique | Détectable à 3–5 % d’excès par rapport à la mesure de référence, en mesurant les deux membres. Surveillance prospective : mesure préopératoire, puis par exemple tous les 3 mois la première année. | ISL 2023, section I |
| F4 | Part des formes secondaires | « Peut-être 85 % » des lymphœdèmes dans le monde | ISL 2023, section I |
| F5 | Lymphœdème primaire | Incidence estimée à la naissance ≈ 1/6 000 ; prévalence avant 20 ans ≈ 1/87 000 ; prédominance féminine (rapport homme/femme 1/4,5 à 1/6,1) | AWMF S2k 2017, chapitre 2 |
| F6 | Cancer du sein | Incidence globale du lymphœdème du bras 16,6 % (21,4 % dans les cohortes prospectives) ; 19,9 % après curage contre 5,6 % après ganglion sentinelle ; augmentation jusqu’à 2 ans | DiSipio et al., Lancet Oncol 2013 (PubMed 23540561) |
| F7 | Curage ou radiothérapie axillaire | Signes cliniques de lymphœdème à 5 ans : 23 % après curage, 11 % après radiothérapie axillaire ; contrôle axillaire comparable | Donker et al., Lancet Oncol 2014, AMAROS (`amaros_pmc.txt`) |
| F8 | Facteurs de risque | IMC élevé (surtout > 25–30), curage étendu, chirurgie étendue, radiothérapie ou chimiothérapie adjuvante, activité insuffisante. Avec curage, irradiation et taxane, la plupart des études rapportent un risque &lt; 50 %. | ISL 2023, section I |
| F9 | Gynécologie | Incidence d’environ 20 % après lymphadénectomie pour cancer gynécologique ; certaines séries 47 à 60 % | AWMF S2k 2017, chapitre 2 |
| F10 | Filariose | OMS, 21.11.2024 : 51 millions de personnes infectées en 2018 ; base mondiale : plus de 15 millions de lymphœdèmes et 25 millions d’hydrocèles ; au moins 36 millions de personnes gardent ces manifestations ; Wuchereria bancrofti ≈ 90 % des cas | OMS (page vérifiée, `INDEX.txt`) |
| F11 | Érysipèle | Facteurs indépendants (cas-témoins) : lymphœdème rapport de cotes 71,2 (intervalle 5,6 à 908) ; rupture de la barrière cutanée 23,8 ; intertrigo interdigital : risque attribuable 61 % | Dupuy et al., BMJ 1999 (PubMed 10364117) |
| F12 | Prophylaxie par pénicilline | Pénicilline V 250 mg deux fois par jour pendant 12 mois, patients avec ≥ 2 érysipèles de jambe : récidive 22 % contre 37 % (rapport de risque 0,55 ; nombre à traiter 5) ; après l’arrêt, effet perdu (27 % dans les deux groupes) | Thomas et al., NEJM 2013 (PubMed 23635049) |
| F13 | Compression et érysipèle | Œdème chronique de jambe et érysipèles récidivants : récidive 15 % contre 40 % (rapport de risque 0,23) ; essai monocentrique, non aveugle, 84 patients, arrêté pour efficacité | Webb et al., NEJM 2020 (PubMed 32786188) |
| F14 | Renforcement musculaire | 141 femmes, lymphœdème stable du bras, manchon porté pendant l’effort : augmentation ≥ 5 % du volume chez 11 % contre 12 % ; poussées 14 % contre 29 % | Schmitz et al., NEJM 2009, essai PAL (PubMed 19675330) |
| F15 | Activité physique | Viser progressivement au moins 150 minutes par semaine d’activité modérée mixte (aérobie et résistance) ; port de la compression pendant l’effort à décider au cas par cas | ISL 2023, section IV.A.1.f |
| F16 | Thérapie décongestive | Deux phases. Phase I : soins cutanés, drainage lymphatique manuel, bandages multicouches, exercices, une à deux fois par jour ; durée habituelle jusqu’à 21 jours (stade I), 28 jours (stade II), 35 jours (stade III, souvent hospitalier). Phase II : vêtement plat sur mesure, renouvelé environ tous les 6 mois, soins, exercice, autotraitement. | AWMF S2k 2017, chapitre 6 |
| F17 | Contre-indications | Absolues : insuffisance cardiaque décompensée, thrombose veineuse profonde aiguë (pour le drainage manuel ; la compression reste indiquée), érysipèle aigu sévère, dermatoses érosives, artériopathie des stades III et IV. Relatives : lymphœdème malin, infections cutanées, dermatoses bulleuses, artériopathie des stades I et II. | AWMF S2k 2017, question 7 |
| F18 | Drainage manuel | Valeur additive limitée sur la réduction de volume dans le lymphœdème après cancer du sein (ISL 2023). Essai de Dayes : réduction de l’excès 29,0 % contre 22,6 % (différence non significative) | ISL 2023 ; Dayes et al., J Clin Oncol 2013 (PubMed 24043733) |
| F19 | Compression | Classe la plus haute tolérée (≈ 20 à 60 mmHg) ; prescription médicale ; contre-indications : artériopathie, syndrome post-thrombotique douloureux, néoplasie occulte, infection aiguë | ISL 2023, section IV.A.1.a |
| F20 | Bioimpédance | Essai randomisé, 879 patientes analysées : progression vers une thérapie décongestive après intervention précoce 7,9 % (bioimpédance) contre 19,2 % (mètre ruban) ; risque relatif 0,41 | Ridner et al., Lymphat Res Biol 2022 (PubMed 35099283) |
| F21 | Lymphoscintigraphie | Série monocentrique de 227 patients : sensibilité 96 %, spécificité 100 % ; tous les faux négatifs étaient des lymphœdèmes primaires | Hassanein et al., Plast Reconstr Surg Glob Open 2017 (PubMed 28831342) |
| F22 | Vert d’indocyanine | Profil linéaire normal ; reflux dermique en « éclaboussure », « poussière d’étoiles », puis « diffus » avec la progression | Yamamoto et al., 2011 et 2016 (PubMed 21681123, 26422172) |
| F23 | Reconstruction immédiate | Résultats préliminaires d’un essai randomisé : lymphœdème cumulé 9,5 % contre 32 % (suivi incomplet : 40 patientes à 24 mois) | Coriddi et al., Ann Surg 2023 (PubMed 37314177) |
| F24 | Anastomose lymphaticoveineuse | Analyse intermédiaire d’un essai randomisé néerlandais à 6 mois : pas de réduction de volume significative ; 41 % des opérées ont partiellement ou totalement arrêté la compression (0 % dans le groupe conservateur) | Jonis et al., Sci Rep 2024 (PubMed 38278856) |
| F25 | Liposuccion | Série prospective, 5 ans : bras, différence de volume médiane 1 061 mL avant, 22 mL à 5 ans ; jambe, 3 447 mL avant, 263 mL à 1 an, 669 mL à 5 ans ; compression continue obligatoire | Série australienne 2024 (PubMed 37114928) ; ISL 2023 |
| F26 | Transfert ganglionnaire | Méta-analyse d’études non randomisées : réduction moyenne de la différence de volume 40,31 % | J Vasc Surg Venous Lymphat Disord 2022 (PubMed 34508873) |
| F27 | Stewart-Treves | Revue systématique de 369 patients : début en moyenne 14,9 ans après le lymphœdème ; mortalité 53,9 % ; survie à 5 ans 22,4 % ; meilleure survie après exérèse (43,3 % à 5 ans) | Int J Dermatol 2022 (PubMed 34196958) |
| F28 | Angiosarcome secondaire | Amplification de haut niveau de MYC dans 55 % des angiosarcomes secondaires à l’irradiation ou au lymphœdème, absente des formes primaires | Manner et al., Am J Pathol 2010 (PubMed 20008140) |
| F29 | Chylothorax, diagnostic | Triglycérides pleuraux > 1,24 mmol/L (110 mg/dL) avec cholestérol &lt; 5,18 mmol/L (200 mg/dL) ; zone intermédiaire 0,56 à 1,24 mmol/L → recherche de chylomicrons (électrophorèse des lipoprotéines) ; exsudat discordant (protéines élevées, LDH basse), à prédominance lymphocytaire | Breathe 2022 (`chylothorax_breathe2022.txt`) ; Chest 2008 (PubMed 18339791) |
| F30 | Chyle | Environ 2,4 L de chyle transportés chaque jour par le canal thoracique ; triglycérides à chaîne longue → chylomicrons → chylifères ; triglycérides à chaîne moyenne absorbés par la veine porte | Breathe 2022 |
| F31 | Chylothorax, causes | Non traumatique : cancer en tête, lymphome = 70 à 75 % des chylothorax malins ; aussi lymphangioléiomyomatose, syndrome des ongles jaunes, maladie de Gorham, tuberculose, sarcoïdose, cirrhose, insuffisance cardiaque ; jusqu’à 9 % idiopathiques. Traumatique : chirurgie thoracique (œsophagectomie). Médicament : dasatinib (cas rares, régression à l’arrêt). | Breathe 2022 ; Eur J Cardiothorac Surg 2007 (PubMed 17580118) ; PubMed 32248338 |
| F32 | Chylothorax, traitement | Traiter la cause ; régime pauvre en graisses avec triglycérides à chaîne moyenne, puis nutrition parentérale si échec ; octréotide (adulte : 50 µg toutes les 8 heures par voie sous-cutanée, sans consensus de dose ; effets : diarrhée, vertiges, hépatotoxicité, thrombopénie, arythmie) ; embolisation du canal thoracique (moins morbide que la chirurgie dans les séries) ; ligature chirurgicale ; pleurodèse | Breathe 2022 ; Curr Opin Pulm Med 2013 (PubMed 23715291) |
| F33 | Physiologie | En régime stable, la filtration capillaire nette persiste même dans les veinules ; la réabsorption n’est que transitoire (principe de Starling révisé, glycocalyx). Presque tout le liquide interstitiel devient de la lymphe. | Levick et Michel 2010 (PubMed 20200043) ; ISL 2023 |
| F34 | Lymphatiques initiaux | Jonctions discontinues « en boutons » entre cellules en feuille de chêne (entrée du liquide) ; jonctions continues « en fermeture éclair » dans les collecteurs | Baluk et al., J Exp Med 2007 (PubMed 17846148) |
| F35 | Inflammation | Modèles murins et biopsies humaines : la stase induit une inflammation lymphocytaire CD4 de type Th2, nécessaire à la fibrose, au dépôt adipeux et à la dysfonction lymphatique ; le blocage d’IL-4 ou IL-13 la prévient chez la souris | Avraham et al., FASEB J 2013 (PubMed 23193171) |
| F36 | Composition de la lymphe | Cellules : lymphocytes T ≈ 80 %, cellules de Langerhans 6–10 %, monocytes 2–8 %, lymphocytes B 1–4 % | AWMF S2k 2017, chapitre 1 |
| F37 | Lipœdème | Toujours douloureux ; disproportion symétrique du tissu adipeux ; pieds et mains épargnés ; ecchymoses faciles ; signe de Stemmer négatif, mais pouvant devenir positif aux stades avancés ; lymphoscintigraphie et vert d’indocyanine habituellement normaux aux stades précoces | AWMF S2k lipœdème 2024 (`awmf_lipoedema_s2k_2024_en.txt`) ; ISL 2023 |
| F38 | Signe de Stemmer | Impossibilité ou difficulté de soulever un pli cutané à la base de la phalange proximale du 2e ou 3e orteil ou doigt ; un signe négatif n’exclut pas un lymphœdème | AWMF S2k 2017, chapitre 3 (`awmf_lymphoedem_s2k_2017.txt`, ligne ≈ 754) |
| F39 | Coumarine | 200 mg deux fois par jour pendant 6 mois : aucune réduction de volume ; toxicité hépatique biologique chez 6 % | Loprinzi et al., NEJM 1999 (PubMed 9929524) |
| F40 | Diurétiques | Bénéfice marginal au long cours, risque hydroélectrolytique ; place limitée : comorbidité, début de phase I, lymphœdème malin (cure courte), épanchements des cavités, soins palliatifs | ISL 2023, section IV.A.2.d |
| F41 | Biopsie ganglionnaire | Éviter l’exérèse d’un ganglion dans un territoire lymphœdémateux (information rarement utile, aggravation possible) ; préférer la cytoponction si un cancer est suspecté | ISL 2023, section III.C |
| F42 | Génétique | Test recommandé en cas de lymphœdème primaire suspect (panel de séquençage de nouvelle génération) ; FOXC2 (lymphœdème-distichiasis), FLT4/VEGFR-3 et VEGF-C (Milroy et formes apparentées), SOX18, CCBE1 et FAT4 (Hennekam), GJC2, PIEZO1, GATA2 (Emberger), syndromes de Turner, Noonan, Klinefelter, trisomie 21 | ISL 2023, section III.B |
| F43 | Suisse, chirurgie | Anastomose lymphoveineuse et transplantation de ganglions lymphatiques vascularisés : prise en charge « en cours d’évaluation » du 1.7.2021 au 31.12.2028 si la thérapie décongestive complexe conforme et documentée (drainage manuel, exercices, compression, soins cutanés) a échoué pendant au moins 12 mois ; garantie préalable spéciale de l’assureur après avis du médecin-conseil | OPAS annexe 1, édition du 1.7.2026 (`suisse/opas_annexe1_2026-07.txt`) |
| F44 | Suisse, compression | LiMA 1.7.2026 : 17.02 bas de classe 2 (23–32 mmHg) à maillage circulaire pour le lymphœdème de stade 1 et après chirurgie ganglionnaire (au plus 2 paires par an ; 1 paire par an en postopératoire) ; 17.15 bandages sur mesure à maillage rectiligne pour les stades 2–3, l’œdème génital, thoracique, le lipœdème 2–3 ; 17.06 systèmes ajustables (stades II–III ; un set par membre et par 6 mois ; non cumulables sur la même période avec 17.02, 17.03 et 17.15, qui sont remboursables après la thérapie décongestive) ; 17.20 compression pneumatique intermittente : stades II–III, échec de la compression conventionnelle, garantie spéciale, réduction ≥ 100 mL lors d’un essai | LiMA (`suisse/lima_2026-07.txt`) |
| F45 | Suisse, physiothérapie | Position tarifaire 7311 (traitement complexe) si lymphœdème primaire ou secondaire et physiothérapeute diplômé en physiothérapie lymphologique (≥ 90 heures) ; œdème post-traumatique transitoire : position 7301 | physioswiss, novembre 2025 (`suisse/physioswiss_lymphologie_2025_de.txt`) |
| F46 | Lymphangiectasie intestinale | Entéropathie exsudative : hypoalbuminémie, lymphopénie, hypogammaglobulinémie ; clairance fécale de l’alpha-1-antitrypsine élevée ; régime pauvre en graisses avec triglycérides à chaîne moyenne | Vignes et al., Orphanet J Rare Dis 2008 (PubMed 18294365) |
| F47 | Syndrome des ongles jaunes | Triade : ongles jaunes, atteinte respiratoire (toux, bronchectasies, épanchement pleural), lymphœdème des membres inférieurs ; souvent après 50 ans ; parfois paranéoplasique | Vignes et al., Orphanet J Rare Dis 2017 (PubMed 28241848) |
| F48 | Sirolimus | Lymphangioléiomyomatose : stabilisation du VEMS sous sirolimus contre déclin sous placebo (− 12 ± 2 mL par mois contre + 1 ± 2 mL par mois), VEGF-D abaissé ; reprise du déclin à l’arrêt | McCormack et al., NEJM 2011 (PubMed 21410393) |
| F49 | Colorant bleu, lymphographie huileuse | Colorant bleu : réaction allergique, parfois anaphylaxie ; lymphographie huileuse réservée aux reflux chyleux et lésions du canal thoracique | ISL 2023, section III.A |
| F50 | Compression pneumatique | Risque de déplacer l’œdème vers la racine du membre ou les organes génitaux et d’induire un anneau fibreux à la racine | ISL 2023, section IV.A.1.e |

**Pas de chiffre** en dehors de ce tableau sans vérification personnelle dans une source primaire, consignée dans `reserves_<onglet>.txt` avec la référence et le PMID. En particulier : aucune donnée épidémiologique suisse n’existe dans les sources trouvées ; la lacune est nommée telle quelle.

---

## 6. Plan détaillé des quatre onglets

Les flèches « → `clé` (X) » indiquent un mot vert vers une fenêtre écrite par le rédacteur X.

### Onglet 1 — Pathologie et prise en charge (`pA`)

Sommaire (écrit par A, titres exacts) :
0 Question clinique et objectifs · 1 Définitions, classification et codage · 2 Épidémiologie · 3 Physiopathologie · 4 Étiologies et facteurs de risque · 5 Anamnèse · 6 Examen clinique · 7 Démarche diagnostique et diagnostics différentiels · 8 Urgences et complications · 9 Thérapie décongestive complexe et compression · 10 Traitements chirurgicaux · 11 Érysipèle et prévention des infections · 12 Chylothorax et autres atteintes lymphatiques centrales · 13 Adénopathies et lymphadénite non spécifique · 14 Suivi, pronostic et prise en charge en Suisse · 15 Situations particulières et cas récapitulatif · 16 Critères formels du diagnostic

#### Rédacteur A — `I89_a.html`

**`i89-0` Question clinique et objectifs.** Présenter Mme R. (consultation initiale, section 4). Question structurante en gras : s’agit-il d’un lymphœdème, quel stade, quelle cause éliminer, quel traitement, comment prévenir l’aggravation et les infections, que rembourse l’assurance obligatoire ? Objectifs en phrases (pas de liste télégraphique). `div.key` « Prérequis » : → `i89-s-lymphangion` (C) pour la circulation lymphatique, → `i89-debit` (A) pour les trois mécanismes d’œdème.

**`i89-1` Définitions, classification et codage.**
- Définition (ISL 2023) : manifestation d’une insuffisance du système lymphatique avec transport réduit ; défaillance « à bas débit ». Opposer l’œdème « à haut débit » (cirrhose, syndrome néphrotique, insuffisance cardiaque droite, insuffisance veineuse) et la forme mixte. → `i89-debit` (A).
- Deux cartes `div.two` : **Primaire** (dysplasie lymphatique ; congénital, d’apparition péripubertaire ou tardive ; formes syndromiques et génétiques) ; **Secondaire** (acquis : chirurgie ganglionnaire, radiothérapie, tumeur obstructive, infections répétées, traumatisme, filariose, obésité massive). → `i89-primaire` (A).
- Stades ISL 0 à III (F1) et sévérité par l’excès de volume (F2) : tableau introduit (question : « quel stade et quelle sévérité ? ») et commenté avec Mme R. (stade I, 18 %, minimal). → `i89-e-volume` (C).
- Codage : I89.0x (acquis non iatrogène, stade dans le 5e caractère), I97.2x (après mastectomie partielle ou totale avec curage), I97.8x (après acte, par territoire), Q82.0x (héréditaire), E88.2x (lipœdème associé, codé séparément), codes additionnels (fistule, lymphocèle, reflux chyleux I89.8 ; ulcère lymphogène L97, L98.4). I89.1 lymphangite chronique ; la lymphangite aiguë (L03) est infectieuse. CIM-11 : correspondance non établie. → `i89-codage` (A).
- `key` À retenir.

**`i89-2` Épidémiologie.** F4, F5, F6, F7, F9, F10 ; aucune donnée suisse publiée retrouvée (lacune nommée). Expliquer pourquoi l’incidence après cancer du sein augmente jusqu’à 2 ans (délai de saturation des voies de suppléance), pourquoi le ganglion sentinelle a réduit le risque (moins de collecteurs interrompus), pourquoi la radiothérapie axillaire en donne moins que le curage (AMAROS : association dans un essai randomisé, donc lien causal avec la stratégie). Distinguer l’incidence (nouveaux cas) de la prévalence. → `i89-risque-cancer` (A).

**`i89-3` Physiopathologie.** Chaîne : normal (filtration nette continue F33, entrée par les jonctions en boutons F34, propulsion par les lymphangions, ganglions, canal thoracique F30) → rupture (capacité de transport &lt; charge lymphatique) → accumulation de liquide riche en protéines → inflammation CD4 Th2 (F35), fibrose, dépôt adipeux précoce (ISL) → baisse de l’immunité locale et érysipèles (F11) → lymphangiosclérose → aggravation. → `i89-s-lymphangion` (C), → `i89-cercle` (A), → `i89-s-fibrose` (C).
- **Figure 1** (A) : « Trois mécanismes d’œdème ». Trois panneaux côte à côte : capillaire sanguin, interstitium, vaisseau lymphatique. Panneau 1 « Haut débit » : grosse flèche de filtration, lymphatique normal débordé. Panneau 2 « Bas débit (lymphœdème) » : filtration normale, lymphatique interrompu, accumulation de protéines (points). Panneau 3 « Forme mixte » : filtration augmentée et lymphatique altéré. Légende : flèche = flux de liquide ; points = protéines ; trait interrompu = lymphatique lésé. Lecture après la figure : pourquoi un diurétique agit sur le panneau 1 et presque pas sur le panneau 2.
- `key` À retenir.

**`i89-4` Étiologies et facteurs de risque.**
- Primaires : congénital (maladie de Milroy, FLT4), péripubertaire ou tardif (lymphœdème-distichiasis, FOXC2), syndromes (Turner, Noonan, Hennekam, Emberger) — détails génétiques renvoyés à C. → `i89-primaire` (A), → `i89-s-vegfc` (C).
- Secondaires après cancer (F8) avec chaque facteur expliqué : nombre de ganglions retirés (interruption de collecteurs), radiothérapie (fibrose et oblitération lymphatique), taxanes (rétention liquidienne et charge accrue ; association), IMC (charge de filtration, compression des collecteurs : association), sédentarité (pompe musculaire). → `i89-risque-cancer` (A).
- Tumeur obstructive ou récidive, lymphome ; érysipèles répétés ; traumatisme ; chirurgie veineuse ou orthopédique ; filariose (B74, F10) ; obésité massive ; insuffisance veineuse chronique (phlébolymphœdème) ; immobilité et déclivité (forme mixte) ; médicaments → `i89-d-oedeme-medic` (D).
- `key` À retenir.

**`i89-5` Anamnèse.**
- Antécédents cliquables : cancer et traitements exacts (type de chirurgie, nombre de ganglions, champs d’irradiation, taxanes) → `i89-risque-cancer` (A) ; érysipèles antérieurs → `i89-erysipele` (B) ; histoire familiale, âge de début → `i89-primaire` (A) ; séjour en zone d’endémie filarienne ; maladies cardiaques, rénales, hépatiques, thyroïdiennes → `i89-oed-systemique` (B) ; médicaments → `i89-d-oedeme-medic` (D) ; poids.
- Symptômes par fréquence, cliquables : gonflement, lourdeur, tension, vêtements et bijoux serrés → `i89-s-lourdeur` (A) ; douleur → `i89-s-douleur` (A) (douleur intense, rapide, nocturne ou neurologique = signal d’alarme) ; limitation de mobilité ; épisodes fébriles avec rougeur ; écoulement de lymphe ; retentissement psychologique et social (ISL : facteur de non-adhésion).
- `div.two` formes typique et atypiques : typique = bras après cancer du sein (Mme R.) ; atypiques = membre inférieur primaire de l’adolescente, lymphœdème génital, tête et cou après cancer ORL et radiothérapie, tronc et sein, lymphœdème bilatéral asymétrique, lymphœdème rapide et douloureux (malin).
- `key` À retenir.

**`i89-6` Examen clinique.** Deux colonnes (`div.two`) :
- Colonne 1 : état général ; signes vitaux ; poids, taille, IMC (Mme R. 30,9 kg/m²) ; mesures circonférentielles bilatérales à points fixes → `i89-e-volume` (C).
- Colonne 2, signes ciblés cliquables : godet et consistance → `i89-godet-peau` (A) ; signe de Stemmer → `i89-stemmer` (A) ; plis cutanés approfondis, orteils carrés, papillomatose, kystes lymphatiques, lymphorrhée, hyperkératose → `i89-godet-peau` (A) ; intertrigo et mycose interdigitale (porte d’entrée, F11) ; aires ganglionnaires (récidive) ; circulation veineuse collatérale (obstruction veineuse) ; pouls et index de pression systolique avant toute compression (F17, F19) ; signes cardiaques de congestion → `i89-oed-systemique` (B) ; examen neurologique du membre (plexopathie, envahissement tumoral) → `i89-malin` (B).
- Piège (`div.trap` avec `span.k`) : un signe de Stemmer négatif n’exclut pas un lymphœdème débutant (F38) ; un godet absent n’exclut pas un lymphœdème avancé.
- `key` À retenir. Bouton `pareto-i89-bases` (couvre `i89-0,i89-1,i89-2,i89-3,i89-4,i89-5,i89-6`) avant `</section>`.

#### Rédacteur B — `I89_b.html`

**`i89-7` Démarche diagnostique et diagnostics différentiels.**
- Principe (ISL) : diagnostic clinique dans la plupart des cas ; examens réservés au doute, aux formes primaires, à la recherche de cause et au bilan préchirurgical → `i89-e-scinti` (C).
- Algorithme en texte puis **Figure 2** (B) « Démarche devant un gros membre » : arbre noir et blanc. Racine « Gros membre » → « Aigu (&lt; 72 heures) ou douloureux ? » oui → exclure thrombose veineuse profonde, érysipèle, rupture de kyste poplité, récidive tumorale ; non → « Unilatéral ? » oui → contexte de cancer ou de chirurgie ganglionnaire (lymphœdème secondaire probable ; signes d’alarme ?) / sans contexte (primaire possible ; écho-Doppler, puis lymphoscintigraphie) ; « Bilatéral ? » → symétrique avec pieds épargnés et douleur (lipœdème) ; avec signes systémiques (cœur, rein, foie, thyroïde, médicaments) ; avec signes veineux (insuffisance veineuse chronique). Lecture de la figure avec Mme R.
- Diagnostics différentiels hiérarchisés par gravité : thrombose veineuse profonde ; lymphœdème malin (récidive, obstruction) → `i89-malin` (B) ; érysipèle ; insuffisances cardiaque, rénale, hépatique, hypoalbuminémie, hypothyroïdie → `i89-oed-systemique` (B) ; œdème médicamenteux → `i89-d-oedeme-medic` (D) ; insuffisance veineuse chronique et phlébolymphœdème → `i89-ddx-veineux` (B) ; lipœdème → `i89-lipoedeme` (B) ; obésité ; œdème de déclivité ; malformations vasculaires (Klippel-Trénaunay).
- Tableau introduit puis commenté : colonnes « Lymphœdème », « Œdème veineux chronique », « Lipœdème », « Œdème systémique » ; lignes : topographie, atteinte du pied, godet, signe de Stemmer, douleur, ecchymoses, effet de l’élévation, peau, examen utile. Lecture : regarder d’abord les pieds et la symétrie ; exemple d’une patiente bilatérale avec pieds épargnés.
- Quiz 1 (B) : homme de 58 ans, antécédent de mélanome de la cuisse droite avec curage inguinal il y a 2 ans, gros membre inférieur droit apparu en 3 semaines, douloureux la nuit. Bonne réponse : écho-Doppler veineux et imagerie de recherche de récidive (TDM ou TEP-TDM selon l’oncologue) avant toute thérapie décongestive. Leurres : thérapie décongestive immédiate ; diurétique de l’anse.
- `key` À retenir.

**`i89-8` Urgences et complications.** Encadré `div.alert` d’abord (gravité décroissante) : érysipèle avec sepsis ou nécrose (urgence) → `i89-erysipele` (B) ; thrombose veineuse profonde associée ; lymphœdème malin (récidive) → `i89-malin` (B) ; angiosarcome de Stewart-Treves → `i89-stewart` (B) ; chylothorax compressif → `i89-chylothorax` (B). Puis complications chroniques : lymphorrhée et ulcère lymphogène, mycoses, papillomatose, limitation fonctionnelle, retentissement psychologique. F27, F28. `key` À retenir.

**`i89-9` Thérapie décongestive complexe et compression.**
- Objectifs hiérarchisés (AWMF) : réduire le volume, ramener à un stade inférieur, stabiliser, prévenir infections et progression, préserver la fonction et la qualité de vie.
- Moyens : soins cutanés ; drainage lymphatique manuel → `i89-dlm` (B) ; bandages multicouches peu élastiques ; exercices ; éducation ; phase I et phase II (F16) → `i89-tdc` (B). Compression seule en stade précoce (ISL : données solides dans le lymphœdème après cancer du sein) ; classes (F19) ; vêtements circulaires ou plats (F44). Compression pneumatique intermittente : place limitée, risque F50. Activité physique et renforcement musculaire (F14, F15) en texte, sans fenêtre propre. Perte de poids (ISL : association forte avec le risque, preuves faibles pour l’effet thérapeutique). Ce qu’il ne faut pas faire : massage classique isolé, « tuyautage » (ISL).
- Contre-indications → `i89-ci-tdc` (B) (F17).
- Choix justifiés selon le stade (tableau introduit et commenté : stade 0/infraclinique, I, II, III → moyens et durée) ; application à Mme R. (stade I : manchon classe 2 ; stade II au mois 30 : thérapie décongestive phase I).
- Surveillance et critères de modification : volume mesuré aux deux membres, tolérance, peau, fonction ; échec confirmé seulement après prise en charge intensive dans un centre spécialisé (ISL).
- `key` À retenir.

**`i89-10` Traitements chirurgicaux.**
- Indications (ISL) : sélection stricte ; après échec documenté ou en stade précoce pour la microchirurgie ; imagerie indispensable (vert d’indocyanine, lymphoscintigraphie).
- Techniques : dérivations (anastomoses lymphaticoveineuses), reconstructions (greffe de collecteur lymphatique), transferts de ganglions lymphatiques vascularisés (risque de lymphœdème au site donneur), liposuccion des formes sans godet à prédominance adipeuse, résections (procédure de Charles à éviter ; transposition d’épiploon sans preuve). → `i89-chir-micro` (B), → `i89-liposuccion` (B). F24, F25, F26.
- Prévention chirurgicale : ganglion sentinelle, cartographie inverse, LYMPHA et reconstruction immédiate (F23), dans `i89-chir-micro`.
- Prise en charge suisse (F43) en une phrase, détails dans l’îlot 14.
- Application à Mme R. (mois 44).
- `key` À retenir.

**`i89-11` Érysipèle et prévention des infections.**
- Mécanisme en deux phrases (renvoi à la science → `i89-s-fibrose` (C)) ; F11 ; présentation (fièvre, frissons, placard) ; diagnostic clinique ; distinguer l’érythème inflammatoire sans signes systémiques (ISL : pas forcément bactérien) ; lymphangite aiguë infectieuse (L03) contre lymphangite chronique (I89.1).
- Traitement de l’épisode : antibiothérapie antistreptococcique selon les recommandations suisses d’infectiologie (posologies non fixées ici, réserve R4) ; thérapie décongestive suspendue sur le membre jusqu’à l’effet de l’antibiotique, puis reprise (AWMF). → `i89-erysipele` (B).
- Prévention : soins cutanés, traitement de l’intertrigo et des mycoses, compression (F13), prophylaxie antibiotique si récidives malgré une thérapie optimale (ISL ; F12) → `i89-d-penicilline` (D). Application à Mme R. (mois 10 et 18).
- `key` À retenir.

**`i89-12` Chylothorax et autres atteintes lymphatiques centrales.**
- Chyle (F30), mécanisme de fuite ou de reflux.
- Chylothorax : présentation (dyspnée, épanchement laiteux ou non), diagnostic (F29) → `i89-e-chyle` (C) ; causes (F31) ; conduite (F32) → `i89-chylothorax` (B), → `i89-d-octreotide` (D). Le liquide peut ne pas être laiteux chez un patient à jeun (moins de chylomicrons).
- Ascite chyleuse, chylocèle non filarienne (I89.8), reflux chyleux cutané ou génital ; lymphangiectasie intestinale (F46) ; lymphocèle et fistule lymphatique postopératoires ; syndrome des ongles jaunes (F47) ; lymphangioléiomyomatose (sirolimus, F48) → `i89-d-sirolimus` (D).
- Renvoi explicite au futur cours des épanchements pleuraux (P-02) pour la technique pleurale.
- `key` À retenir.

**`i89-13` Adénopathies et lymphadénite non spécifique.**
- Problème : une adénopathie dans un territoire lymphœdémateux évoque une récidive ou un lymphome, mais l’exérèse aggrave le lymphœdème (F41) : cytoponction guidée d’abord.
- Lymphadénite non spécifique (I88) : mésentérique (I88.0), chronique hors mésentère (I88.1) ; signes qui imposent une biopsie (ganglion dur, fixé, > 2 semaines sans cause, signes généraux) — formuler sans seuil chiffré non vérifié. Adénopathie sans précision : R59.0, R59.9.
- Réticulose lipomélanique (I89.8) : ganglions réactionnels aux dermatoses chroniques étendues ; diagnostic histologique, non tumoral.
- Renvoi au futur cours « Adénopathies ».
- `key` À retenir.

**`i89-14` Suivi, pronostic et prise en charge en Suisse.**
- Pronostic : maladie chronique, rarement guérissable ; traitement à vie comparable à la compression de l’insuffisance veineuse (ISL) ; la précocité améliore le résultat.
- Surveillance prospective après cancer (F3, F20) → `i89-e-bis` (C) ; mesures recommandées (excès calculé à partir des deux membres).
- Conseils de « réduction du risque » : la plupart des interdits (chaleur, prises de sang) sont anecdotiques (ISL) ; éviter les peurs inutiles ; garder les mesures fondées (poids, activité, soins cutanés, traitement rapide des infections). Aucune interdiction chiffrée non sourcée.
- Prise en charge en Suisse → `i89-suisse` (B) : physiothérapie (F45), LiMA (F44), OPAS (F43). Tableau introduit et commenté : prestation → condition → source.
- `key` À retenir.

**`i89-15` Situations particulières et cas récapitulatif.** `div.two` en cartes :
- Enfant : formes primaires, rôle des parents dans la thérapie (AWMF), prudence microchirurgicale (ISL).
- Grossesse : formuler seulement ce qui est sourcé (compression possible ; examens isotopiques différés si non urgents — si le rédacteur ne trouve pas de source, il omet cette phrase).
- Sujet âgé, immobile : forme mixte de déclivité ; pompe musculaire absente.
- Insuffisance cardiaque : thérapie décongestive contre-indiquée en cas de décompensation (F17) ; terme ESC 2026 « insuffisance cardiaque décompensée ».
- Artériopathie : compression adaptée après mesure de l’index de pression systolique (F17, F19).
- Cancer actif et soins palliatifs : thérapie décongestive palliative, diurétique en cure courte (ISL, F40).
- Obésité : lymphœdème de l’obésité massive ; lipœdème associé.
- Voyageur ou migrant : filariose (renvoi infectiologie).
- **Cas récapitulatif** : Mme R. du mois 0 au mois 44, en un paragraphe qui relie chaque décision à son mécanisme. Quiz 2 (B) : au mois 18, deuxième érysipèle ; bonne réponse = soins cutanés, poursuite de la compression et discussion d’une prophylaxie par pénicilline orale ; leurres = diurétique au long cours ; arrêt définitif de la compression.
- `key` À retenir.

**`i89-16` Critères formels du diagnostic** (dernier îlot de l’onglet).
- `div.alert` : **Lymphœdème** = gonflement chronique compatible (histoire, topographie, consistance) + contexte ou mécanisme lymphatique + exclusion des causes à haut débit et des urgences ; confirmation par imagerie lymphatique si doute (lymphoscintigraphie, examen de référence) ; stade ISL 0 à III (F1) ; sévérité par l’excès de volume (F2) ; infraclinique si excès ≥ 3–5 % par rapport à la référence (F3). **Chylothorax** : F29. **Lipœdème** (différentiel) : F37. **Stewart-Treves** : lésions violacées sur lymphœdème chronique, preuve histologique (CD31, ERG ; MYC).
- `div.key` « Paramètres clés à surveiller » : excès de volume (même méthode, deux membres) ; stade ; nombre d’érysipèles ; état cutané et intertrigo ; poids ; tolérance et renouvellement de la compression (environ 6 mois) ; fonction et qualité de vie ; signes d’alarme (douleur, progression rapide, lésions violacées).
- Bouton `pareto-i89-pec` (couvre `i89-7,i89-8,i89-9,i89-10,i89-11,i89-12,i89-13,i89-14,i89-15,i89-16`).
- `div.src` « Références principales » (section 9 de ce plan).

### Onglet 2 — Examens complémentaires (`pE`) — Rédacteur C

Sommaire : 1 Hiérarchie des examens · 2 Mesure du volume et détection précoce · 3 Lymphoscintigraphie, examen de référence · 4 Lymphographie au vert d’indocyanine et autres imageries · 5 Écho-Doppler veineux et biologie des diagnostics différentiels · 6 Analyse d’un épanchement chyleux · 7 Génétique et biopsie · 8 Entraînement

**`i89-e-1` Hiérarchie des examens.** Tableau introduit (question → examen → statut indiqué/conditionnel/non systématique → ce que le résultat change) puis commenté avec Mme R. **Examen de référence nommé : la lymphoscintigraphie** (ISL : a remplacé la lymphographie huileuse). Lignes : volume (indiqué) ; écho-Doppler veineux (indiqué si unilatéral récent, douloureux, ou doute veineux) ; lymphoscintigraphie (conditionnelle) ; vert d’indocyanine (conditionnel, préchirurgical) ; biologie ciblée (si bilatéral ou systémique) ; imagerie oncologique (si signe d’alarme) ; génétique (primaire suspect) ; biopsie (lésion suspecte) ; analyse du liquide (épanchement).

**`i89-e-2` Mesure du volume et détection précoce.** Fiche d’interprétation : mètre ruban non extensible et formule du tronc de cône ; volumétrie par déplacement d’eau ; périmétrie optoélectronique (sans main ni pied ; membre perpendiculaire) ; bioimpédance spectroscopique et constante diélectrique tissulaire (F3, F20). Pièges : membre dominant, variation de poids, heure de la mesure, atteinte bilatérale (comparer à la référence de chaque membre). Calcul détaillé pour Mme R. (2 950 − 2 500 = 450 mL ; 18 %). → `i89-e-volume` (C), → `i89-e-bis` (C).

**`i89-e-3` Lymphoscintigraphie, examen de référence.** Principe (colloïde marqué au technétium 99m injecté en intradermique ou sous-cutané interdigital, images dynamiques et tardives), normal (progression le long de collecteurs, fixation ganglionnaire), anomalies (retard ou absence de transit, reflux dermique, collatérales, absence ou faible fixation ganglionnaire, aplasie ou hyperplasie dans les formes primaires) ; performances (F21) et biais ; contre-indication relative : érysipèle au site d’injection (AWMF) ; protocole non standardisé (ISL). **Figure 3** (C) : deux silhouettes de jambes schématiques, à gauche « normal » (deux collecteurs, ganglions inguinaux visibles), à droite « lymphœdème » (absence de collecteur, plage de reflux dermique hachurée, ganglions absents). → `i89-e-scinti` (C).

**`i89-e-4` Lymphographie au vert d’indocyanine et autres imageries.** Vert d’indocyanine (F22), usage préchirurgical, absence de rayonnement, autorisation variable selon les pays (ISL) ; IRM lymphographique ; échographie haute fréquence ; lymphographie huileuse (F49) ; TDM et IRM pour une cause obstructive ; TEP-TDM si récidive suspectée. → `i89-e-icg` (C).

**`i89-e-5` Écho-Doppler veineux et biologie des diagnostics différentiels.** Pourquoi l’écho-Doppler d’abord (ISL) ; tableau « diagnostics × examens biologiques » introduit et commenté : insuffisance cardiaque (NT-proBNP), syndrome néphrotique (protéinurie, albumine), cirrhose (albumine, bilan hépatique), hypothyroïdie (TSH), dénutrition (albumine), entéropathie exsudative (albumine, lymphocytes, IgG, alpha-1-antitrypsine fécale, F46), lymphœdème et lipœdème (biologie normale). Chaque dosage dit pourquoi on le demande et ce qu’il change. Seuils : uniquement ceux d’une source vérifiée ; sinon « valeurs du laboratoire ».

**`i89-e-6` Analyse d’un épanchement chyleux.** Fiche : aspect, triglycérides, cholestérol, chylomicrons, protéines et LDH, cytologie (F29) ; pièges : patient à jeun, pseudochylothorax (cholestérol élevé, pleurésie ancienne), zone intermédiaire ; erreur fréquente : se fier à l’aspect laiteux. → `i89-e-chyle` (C).

**`i89-e-7` Génétique et biopsie.** Indication du test génétique (F42), analyse de ségrégation, conseil ; biopsie cutanée de toute lésion violacée persistante sur lymphœdème (angiosarcome : CD31, ERG, D2-40 ; amplification de MYC, F28) ; pas d’exérèse ganglionnaire de principe (F41). → `i89-e-genet` (C).

**`i89-e-8` Entraînement** : cinq quiz.
1. Mme R. au mois 0 : 2 950 et 2 500 mL, godet, réduction après la nuit. Bonne réponse : stade I, sévérité minimale (18 %), diagnostic clinique sans lymphoscintigraphie. Leurres : stade II modéré ; lymphoscintigraphie obligatoire.
2. Femme de 38 ans, augmentation symétrique des jambes depuis la puberté, pieds épargnés, douleur à la pression, ecchymoses faciles, signe de Stemmer négatif. Bonne réponse : lipœdème probable ; diagnostic clinique ; pas de diurétique. Leurres : lymphœdème primaire bilatéral ; lymphoscintigraphie systématique.
3. Adolescente de 16 ans, œdème du dos du pied gauche depuis 8 mois, signe de Stemmer positif, sans antécédent. Bonne réponse : écho-Doppler veineux, puis lymphoscintigraphie, et discussion d’un panel génétique. Leurres : diurétique ; biopsie ganglionnaire inguinale.
4. Homme de 64 ans, 5e jour après œsophagectomie, drain thoracique laiteux à 1 200 mL par jour ; triglycérides pleuraux 4,1 mmol/L, cholestérol 2,0 mmol/L. Bonne réponse : chylothorax postopératoire ; arrêt des graisses à chaîne longue (triglycérides à chaîne moyenne ou nutrition parentérale) et discussion précoce d’une fermeture du canal thoracique (embolisation ou ligature). Leurres : pseudochylothorax ; simple surveillance.
5. Femme de 71 ans, lymphœdème du bras depuis 15 ans après mastectomie et curage, plusieurs macules violacées apparues en 6 semaines. Bonne réponse : biopsie cutanée rapide (angiosarcome de Stewart-Treves). Leurres : ecchymoses de la compression ; antibiotique pour érysipèle.
Bouton `pareto-i89-exam` (couvre `i89-e-1` à `i89-e-7`) avant la fin de `i89-e-8`.

### Onglet 3 — Sciences fondamentales spécialisées (`pS`) — Rédacteur C

Barre des sciences (libellés sans sigle) : « Anatomie et histologie » (`i89-s-anat`, section `i89-sa`) ; « Physiologie » (`i89-s-physio`, section `i89-sp`) ; « Immunologie et biologie tissulaire » (`i89-s-immuno`, section `i89-si`) ; « Génétique et développement » (`i89-s-gen`, section `i89-sg`). Chaque discipline : annonce de la question clinique éclairée, normal puis pathologique, schéma ou tableau commenté, encadrés `key` « Science → clinique », « Science → examen », « Science → traitement », puis « À retenir ».

- **Anatomie et histologie** : lymphatiques initiaux (borgnes, cellules en feuille de chêne, jonctions en boutons F34, filaments d’ancrage) ; précollecteurs ; collecteurs (lymphangions, valvules, muscle lisse, jonctions continues) ; ganglions ; troncs ; citerne du chyle ; canal thoracique et abouchement au confluent veineux jugulo-sous-clavier gauche ; réseaux superficiel et profond ; territoires de drainage (bras et quadrant thoracique vers l’aisselle) ; marqueurs (PROX1, LYVE-1, VEGFR-3, podoplanine reconnue par D2-40). **Figure 4** (C) : « Du lymphatique initial au canal thoracique » : capillaire lymphatique borgne avec filaments d’ancrage → précollecteur → collecteur segmenté en lymphangions séparés par des valvules → ganglion → tronc → canal thoracique → veine sous-clavière gauche. Corrélations : pourquoi le curage axillaire interrompt le drainage du bras ; pourquoi le signe de Stemmer explore le derme ; pourquoi l’anastomose lymphaticoveineuse exige des collecteurs encore contractiles. → `i89-s-lymphangion` (C).
- **Physiologie** : principe de Starling révisé et glycocalyx (F33) ; formation de la lymphe ; propulsion intrinsèque (contraction des lymphangions) et extrinsèque (muscles, respiration, pulsations artérielles, compression externe) ; capacité de transport, charge lymphatique, insuffisance mécanique (bas débit), dynamique (haut débit) et mixte (« valve de sécurité ») ; chyle (F30) ; effets physiologiques de la compression (AWMF : baisse de l’ultrafiltration, entrée accrue dans les lymphatiques initiaux, hausse du flux résiduel). Corrélations : pourquoi le diurétique échoue (F40) ; pourquoi l’élévation réduit le stade I ; pourquoi les triglycérides à chaîne moyenne réduisent le débit de chyle.
- **Immunologie et biologie tissulaire** : composition cellulaire de la lymphe (F36) ; trafic des cellules dendritiques vers les ganglions ; stase → inflammation CD4 Th2, IL-4, IL-13, TGF-β, fibrose, adipogenèse (F35, données surtout murines : le dire) ; macrophages ; défense locale altérée et érysipèles (F11) ; lymphangiosclérose après infections répétées ; angiosarcome (MYC, F28). → `i89-s-fibrose` (C). Corrélations : pourquoi traiter tôt ; pourquoi la prophylaxie des infections ralentit l’aggravation (raisonnement mécanistique, preuve clinique limitée : le dire).
- **Génétique et développement** : lymphangiogenèse (PROX1 → identité ; VEGF-C → VEGFR-3 → bourgeonnement ; CCBE1 nécessaire à la maturation du VEGF-C ; FOXC2 et PIEZO1 → valvules) ; tableau gène → syndrome → transmission → conséquence clinique (F42 ; GATA2 → suivi hématologique) ; variants somatiques (PIK3CA : Klippel-Trénaunay, CLOVES ; ISL) ; prédisposition génétique au lymphœdème secondaire (ISL : données limitées). → `i89-s-vegfc` (C). Bouton `pareto-i89-sciences` (couvre `i89-sa,i89-sp,i89-si,i89-sg`) à la fin de la section `i89-sg`.

### Onglet 4 — Pharmacologie du lymphœdème et du chyle (`pP`) — Rédacteur D

Sommaire : 1 Stratégie · 2 Anti-infectieux · 3 Diurétiques et benzopyrones · 4 Médicaments des épanchements chyleux et des anomalies lymphatiques · 5 Médicaments qui provoquent ou aggravent un œdème · 6 Agents de diagnostic, interactions et surveillance

**`i89-p-1` Stratégie : ce que les médicaments peuvent et ne peuvent pas faire.** Aucun médicament ne traite le lymphœdème périphérique (ISL : facteurs lymphangiogéniques et anti-inflammatoires sans valeur clinique démontrée). Classification fonctionnelle : traiter et prévenir l’infection ; traiter une cause ou un épanchement chyleux ; éviter les médicaments inutiles ou nocifs ; agents de diagnostic. Tableau introduit et commenté (classe → place → niveau de preuve → source).

**`i89-p-2` Anti-infectieux : traitement et prophylaxie des érysipèles.** Épisode aigu : principe antistreptococcique, posologies renvoyées au cours d’infectiologie (réserve R4). Prophylaxie (F12) → `i89-d-penicilline` (D) ; antifongiques locaux de l’intertrigo (ISL). Tableau des doses : seulement les doses vérifiées (pénicilline V 250 mg deux fois par jour, essai de Thomas) ; formes disponibles en Suisse à vérifier dans l’information professionnelle (compendium.ch ou swissmedicinfo.ch) ; sinon l’écrire comme dose d’essai et le consigner en réserve. Encadré `alert` : allergie aux bêtalactamines (alternative macrolide : préciser seulement si vérifiée), interactions.

**`i89-p-3` Diurétiques et benzopyrones : pourquoi les éviter au long cours.** F40 → `i89-d-diuretiques` (D) ; F39 → `i89-d-benzopyrones` (D). Médicaments à éviter : diurétique au long cours, coumarine, injections sclérosantes ou hyaluronidase (ISL : bénéfice incertain, peut-être nocif).

**`i89-p-4` Médicaments des épanchements chyleux et des anomalies lymphatiques.** Régime pauvre en graisses avec triglycérides à chaîne moyenne (mécanisme F30) ; octréotide (F32) → `i89-d-octreotide` (D) — hors indication autorisée en Suisse pour le chylothorax si l’information professionnelle le confirme ; sirolimus (lymphangioléiomyomatose F48, malformations lymphatiques ISL ; à l’inverse, lymphœdèmes rapportés sous sirolimus, ISL) → `i89-d-sirolimus` (D) ; agents sclérosants des malformations (doxycycline, éthanol ; ISL) en une phrase.

**`i89-p-5` Médicaments qui provoquent ou aggravent un œdème.** Dihydropyridines (vasodilatation précapillaire → pression capillaire accrue ; le diurétique corrige peu), glitazones, anti-inflammatoires non stéroïdiens, corticoïdes, minoxidil, gabapentinoïdes, docétaxel (rétention liquidienne), inhibiteurs de mTOR, dasatinib (épanchements pleuraux, chylothorax rare, F31). Chaque mécanisme et chaque fréquence vérifiés (information professionnelle suisse ou PubMed) ; sans vérification, citer la classe sans fréquence. → `i89-d-oedeme-medic` (D).

**`i89-p-6` Agents de diagnostic, interactions et surveillance.** Colloïdes marqués au technétium 99m, vert d’indocyanine (contenu iodé et précautions : seulement si vérifié dans l’information du produit), colorant bleu (F49) → `i89-d-traceurs` (D). Encadré `div.alert` « Interactions et dangers » : sirolimus et inhibiteurs ou inducteurs du CYP3A4 (vérifier), octréotide et glycémie (vérifier), coumarine et foie (F39), diurétique et hypokaliémie. Surveillance. Quiz (D) : Mme R. au mois 18 ; bonne réponse = pénicilline V 250 mg deux fois par jour pendant 12 mois en discutant l’extrapolation au bras et la perte d’effet à l’arrêt ; leurres = furosémide ; coumarine. Bouton `pareto-i89-pharma` (couvre `i89-p-1` à `i89-p-6`).

---

## 7. Fenêtres (38) et Pareto (5)

| Clé | Titre (data-title) | Fichier | Rédacteur | Contenu attendu (réponse directe d’abord) |
|---|---|---|---|---|
| `i89-debit` | Œdème à bas débit, à haut débit et forme mixte | pop1 | A | Définitions ISL ; exemples ; pourquoi la distinction change le traitement |
| `i89-cercle` | Pourquoi le lymphœdème s’aggrave | pop1 | A | Stase → inflammation → fibrose et graisse → infections → lymphangiosclérose ; F35 (murin), F11 |
| `i89-risque-cancer` | Facteurs de risque après traitement d’un cancer | pop1 | A | F6, F7, F8 ; association ou causalité pour chaque facteur |
| `i89-primaire` | Lymphœdèmes primaires : âge de début et syndromes | pop1 | A | Congénital, péripubertaire, tardif ; syndromes ; quand penser génétique (renvoi `i89-e-genet`) |
| `i89-s-lourdeur` | Lourdeur, tension et gonflement | pop1 | A | Caractérisation, variation diurne, effet de l’élévation selon le stade |
| `i89-s-douleur` | Douleur dans un membre lymphœdémateux | pop1 | A | Douleur modérée habituelle ; douleur intense = thrombose, érysipèle, récidive, plexopathie, lipœdème |
| `i89-stemmer` | Signe de Stemmer | pop1 | A | Technique, mécanisme (épaississement dermique), valeur et limites (F38, F37) |
| `i89-godet-peau` | Godet, consistance et altérations cutanées | pop1 | A | Godet selon le stade (F1) ; papillomatose, kystes, lymphorrhée, intertrigo |
| `i89-codage` | Coder un lymphœdème en CIM-10-GM | pop1 | A | I89.0x, I97.2x, I97.8x, Q82.0x, E88.2x, codes additionnels ; exemple Mme R. |
| `pareto-i89-bases` | Pareto — Notions, clinique et mécanismes | pop1 | A | ratio `i89-0` à `i89-6` |
| `i89-ddx-veineux` | Œdème veineux chronique et phlébolymphœdème | pop2 | B | Haut débit devenu mixte ; signes veineux ; CEAP ; renvoi au cours I83 |
| `i89-lipoedeme` | Lipœdème | pop2 | B | F37 ; codage E88.2x ; lipo-lymphœdème ; OPAS liposuccion (F43, ligne lipœdème) |
| `i89-oed-systemique` | Œdèmes systémiques : cœur, rein, foie, thyroïde, nutrition | pop2 | B | Mécanisme de chaque cause ; examen utile ; terminologie ESC 2026 entre parenthèses |
| `i89-malin` | Lymphœdème malin | pop2 | B | Signes d’alarme ; mécanisme d’obstruction ; imagerie ; thérapie palliative |
| `i89-stewart` | Syndrome de Stewart-Treves | pop2 | B | F27, F28 ; présentation ; biopsie ; exérèse précoce |
| `i89-tdc` | Thérapie décongestive complexe : phases et intensité | pop2 | B | F16 ; bandages multicouches ; éducation |
| `i89-dlm` | Drainage lymphatique manuel | pop2 | B | Mécanisme (étirement cutané, contractions des lymphangions, AWMF) ; preuves F18 ; limites |
| `i89-ci-tdc` | Contre-indications de la thérapie décongestive | pop2 | B | F17 avec le pourquoi de chacune |
| `i89-chir-micro` | Microchirurgie lymphatique et prévention chirurgicale | pop2 | B | Anastomoses, transferts, greffes ; F23, F24, F26 ; LYMPHA ; risque au site donneur |
| `i89-liposuccion` | Liposuccion du lymphœdème avancé | pop2 | B | Indication (sans godet, adipeux) ; F25 ; compression à vie |
| `i89-erysipele` | Érysipèle sur lymphœdème | pop2 | B | Reconnaître, traiter (principe), suspendre puis reprendre la compression, prévenir |
| `i89-chylothorax` | Chylothorax : mécanismes et conduite | pop2 | B | F29 à F32 ; postopératoire contre non traumatique |
| `i89-suisse` | Prise en charge des coûts en Suisse | pop2 | B | F43, F44, F45 ; prescription, garantie préalable |
| `pareto-i89-pec` | Pareto — Diagnostic et prise en charge | pop2 | B | ratio `i89-7` à `i89-16` |
| `i89-e-volume` | Calcul du volume et seuils de sévérité | pop3 | C | Formule du tronc de cône ; F2, F3 ; pièges |
| `i89-e-bis` | Bioimpédance et surveillance prospective | pop3 | C | Principe ; F20 ; L-Dex ; mesure de référence |
| `i89-e-scinti` | Lymphoscintigraphie : technique et lecture | pop3 | C | F21 ; anomalies ; contre-indication relative |
| `i89-e-icg` | Lymphographie au vert d’indocyanine | pop3 | C | F22 ; usage préchirurgical |
| `i89-e-chyle` | Analyse d’un liquide chyleux | pop3 | C | F29 ; pièges |
| `i89-e-genet` | Quand demander un test génétique | pop3 | C | F42 ; ségrégation ; GATA2 |
| `i89-s-lymphangion` | Lymphangion et propulsion de la lymphe | pop3 | C | Jonctions en boutons (F34), valvules, pompe intrinsèque et extrinsèque |
| `i89-s-fibrose` | Inflammation, fibrose et adipogenèse lymphostatiques | pop3 | C | F35, F36 ; limites des modèles murins |
| `i89-s-vegfc` | Voie VEGF-C – VEGFR-3 | pop3 | C | Signalisation ; Milroy ; échec clinique des facteurs lymphangiogéniques (ISL) |
| `pareto-i89-exam` | Pareto — Examens | pop3 | C | ratio `i89-e-1` à `i89-e-7` |
| `pareto-i89-sciences` | Pareto — Sciences fondamentales | pop3 | C | ratio `i89-sa,i89-sp,i89-si,i89-sg` |
| `i89-d-penicilline` | Prophylaxie par pénicilline orale | pop4 | D | F12 ; indication ; durée ; limites (jambes, effet perdu à l’arrêt) |
| `i89-d-diuretiques` | Diurétiques dans le lymphœdème | pop4 | D | F40 ; mécanisme de l’échec |
| `i89-d-benzopyrones` | Benzopyrones et coumarine | pop4 | D | F39 ; ISL ; ne pas confondre avec les antivitamines K (coumariniques) |
| `i89-d-octreotide` | Octréotide dans le chylothorax | pop4 | D | Mécanisme (somatostatine : débit splanchnique et motilité) ; F32 ; statut hors indication à vérifier |
| `i89-d-sirolimus` | Sirolimus et système lymphatique | pop4 | D | F48 ; malformations ; lymphœdème sous sirolimus (ISL) |
| `i89-d-oedeme-medic` | Médicaments qui provoquent un œdème | pop4 | D | Mécanisme par classe ; distinction avec le lymphœdème |
| `i89-d-traceurs` | Agents de diagnostic lymphatique | pop4 | D | Colloïdes marqués, vert d’indocyanine, colorant bleu (F49) |
| `pareto-i89-pharma` | Pareto — Pharmacologie | pop4 | D | ratio `i89-p-1` à `i89-p-6` |

Chaque clé ci-dessus doit exister exactement une fois. Les mots verts d’un rédacteur peuvent ouvrir les fenêtres d’un autre rédacteur : les clés et le contenu sont fixés ici, il n’attend pas l’autre pour écrire son texte.

### 7.1 Propriété des notions (éviter les redites)

| Notion | Développée dans | Ailleurs : une phrase et un mot vert seulement |
|---|---|---|
| Stades et sévérité | `i89-1` (A) et `i89-e-volume` (C) | `i89-16` (rappel formel) |
| Mécanisme de l’œdème lymphatique | `i89-3` (A), science physiologie (C) | Les autres îlots |
| Inflammation, fibrose, infection | science immunologie (C), `i89-s-fibrose` | `i89-3`, `i89-11` |
| Érysipèle : clinique | `i89-11`, `i89-erysipele` (B) | `i89-8` |
| Érysipèle : médicaments | `i89-p-2`, `i89-d-penicilline` (D) | `i89-11` |
| Chylothorax : conduite | `i89-12`, `i89-chylothorax` (B) | `i89-e-6` (diagnostic), `i89-p-4` (médicaments) |
| Différentiels | `i89-7` et fenêtres B | `i89-e-5` (examens seulement) |
| Génétique | science génétique (C), `i89-e-genet` | `i89-4`, `i89-primaire` (une phrase par gène au plus) |
| Remboursement suisse | `i89-14`, `i89-suisse` (B) | `i89-9`, `i89-10` (une phrase) |
| Médicaments œdématogènes | `i89-p-5`, `i89-d-oedeme-medic` (D) | `i89-4`, `i89-5`, `i89-7` |

---

## 8. Figures, quiz et Pareto (récapitulatif)

| Élément | Rédacteur | Emplacement |
|---|---|---|
| Figure 1 — Trois mécanismes d’œdème | A | `i89-3` |
| Figure 2 — Démarche devant un gros membre | B | `i89-7` |
| Figure 3 — Lymphoscintigraphie normale et pathologique (schéma) | C | `i89-e-3` |
| Figure 4 — Du lymphatique initial au canal thoracique | C | section `i89-sa` |
| Quiz : 2 (B, `i89-7` et `i89-15`), 5 (C, `i89-e-8`), 1 (D, `i89-p-6`) | — | — |
| Pareto : `pareto-i89-bases` (A), `pareto-i89-pec` (B), `pareto-i89-exam` et `pareto-i89-sciences` (C), `pareto-i89-pharma` (D) | — | — |

---

## 9. Références principales (contenu du `div.src` de `i89-16`, écrit par B)

- Executive Committee of the International Society of Lymphology. The diagnosis and treatment of peripheral lymphedema: 2023 Consensus Document. Lymphology 2023;56:133-151.
- Gesellschaft Deutschsprachiger Lymphologen. S2k-Leitlinie Diagnostik und Therapie der Lymphödeme, AWMF 058-001, 2017 (en révision).
- Deutsche Gesellschaft für Phlebologie und Lymphologie. S2k guideline Lipoedema, AWMF 037-012, 2024.
- Département fédéral de l’intérieur. OPAS, annexe 1, et Liste des moyens et appareils, éditions du 1.7.2026 ; physioswiss, application tarifaire de la physiothérapie lymphologique, 2025.
- DiSipio et al., Lancet Oncology 2013 ; Donker et al., Lancet Oncology 2014 (AMAROS) ; Thomas et al., New England Journal of Medicine 2013 ; Webb et al., New England Journal of Medicine 2020 ; Schmitz et al., New England Journal of Medicine 2009 (PAL) ; Dupuy et al., BMJ 1999 ; Ridner et al., Lymphatic Research and Biology 2022 ; Levick et Michel, Cardiovascular Research 2010 ; revue de Breathe 2022 sur le chylothorax non traumatique ; Organisation mondiale de la santé, aide-mémoire sur la filariose lymphatique, 2024.

Écrire les auteurs sous la forme « Dupont et al. », sans initiales. Les sigles des revues sont développés (pas de « NEJM »).

---

## 10. Réserves connues (à reprendre dans `reserves_<onglet>.txt` si concernées)

- **R1.** Une S3-Leitlinie allemande sur le lymphœdème est annoncée en 2026 ; sa publication n’a pas été vérifiée. Ne pas la citer.
- **R2.** Aucune donnée épidémiologique suisse sur le lymphœdème n’a été trouvée : écrire la lacune, ne pas extrapoler.
- **R3.** La revue de Breathe 2022 se contredit sur la part des cancers dans les chylothorax non traumatiques (« trois quarts » dans le résumé, « près d’un tiers » dans le texte) : ne citer aucune proportion globale.
- **R4.** Les posologies suisses de l’érysipèle aigu (Société suisse d’infectiologie) n’ont pas pu être lues (site inaccessible au téléchargement). Pas de dose de l’épisode aigu dans I89.
- **R5.** L’essai de Thomas et al. porte sur les érysipèles de jambe ; l’extrapolation au bras est un raisonnement, non une preuve.
- **R6.** Les données sur l’inflammation Th2 sont surtout murines (avec des biopsies humaines) ; aucune thérapie anti-IL-4 ou anti-IL-13 n’est validée dans le lymphœdème.
- **R7.** Les autorisations suisses de l’octréotide, du sirolimus, du vert d’indocyanine et de la pénicilline V doivent être vérifiées par D dans l’information professionnelle ; à défaut, l’écrire sans affirmer de statut réglementaire.
- **R8.** Les résultats de la reconstruction lymphatique immédiate (Coriddi 2023) et de l’essai néerlandais d’anastomoses (Jonis 2024) sont préliminaires ou intermédiaires.

---

## 11. Contrôles avant remise (chaque rédacteur)

```bash
cd /home/user/Medina
D="livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I89"
MEDINA_GLOSSAIRE_EXTRA="$PWD/$D/glossary_i89.py:$PWD/$D/glossary_i89_a.py" \
  python3 "livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/verifier_sigles.py" I89 "$D/brouillon/I89_a.html" "$D/brouillon/I89_pop1.html"
```
Le résultat doit être `{}` (adapter la lettre de l’onglet ; ne lister dans la variable que les glossaires qui existent).

Contrôles complémentaires : chaque `data-k` du fichier existe dans la liste de la section 7 ; ids uniques et préfixés ; aucune classe hors liste ; aucune phrase nominale ; aucun chiffre hors section 5 sans réserve écrite ; mots comptés (`python3 -c "import re,sys;print(len(re.sub(r'<[^>]+>',' ',open(sys.argv[1]).read()).split()))" fichier`).

Remise : fichiers dans `I89/brouillon/`, glossaire éventuel `I89/glossary_i89_<onglet>.py`, réserves dans `I89/brouillon/reserves_<onglet>.txt`. Aucun fichier dans `chapters/`, `glossary/` ni `chapters.json`. Aucun commit.
