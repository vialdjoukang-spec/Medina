# G99 — Autres affections du système nerveux au cours de maladies classées ailleurs (N-05-Neurologie)

Dossier de recherche, cycle Betta 41, leçon 2 (agent C41-A3-NEUR, recherche Opus 5.5). Consultation : 15.10.2026.
Chaque fait est suivi de son identifiant `[Sx]`, détaillé dans `sources.json`. Rien n'est ajouté de mémoire. Ce qui n'a pas été trouvé ou lu figure sous « Lacunes ». Remarque d'exécution : le quota de recherche web (WebSearch) de la session était épuisé ; la recherche a été menée par PubMed, lecture directe d'URL (WebFetch/curl) et `tools/swissmedic_fi.py`.

## 0. Sous-codes et logique de codage (CIM-10-GM 2024)

G99* est une **catégorie astérisque** (manifestation) : la maladie causale est codée par son code croix (†) [S1][S2]. Aucune exclusion n'est listée pour G99 [S1].

| Sous-code | Intitulé (OFS) [S2] | Exemples de maladies causales (†) [S1] |
|---|---|---|
| G99.0* | Neuropathie du système nerveux autonome au cours de maladies endocriniennes et métaboliques | Neuropathie autonome amyloïde (E85.-†) ; neuropathie autonome diabétique (E10–E14, 4ᵉ caractère .4†) |
| G99.00* | Gastroparésie lors de neuropathie autonome au cours de maladies endocriniennes et métaboliques | idem |
| G99.08* | Autre neuropathie autonome au cours de maladies endocriniennes et métaboliques | idem |
| G99.1* | Autres affections du système nerveux autonome au cours d'autres maladies classées ailleurs | aucun exemple listé [S1] |
| G99.2* | Myélopathies au cours de maladies classées ailleurs | Syndrome de compression de l'artère spinale antérieure et de l'artère vertébrale (M47.0-†) ; myélopathie au cours d'atteintes discales (M50.0†, M51.0†), de tumeurs (C00–D48†), de spondylose (M47.-†) |
| G99.8* | Autres affections précisées du système nerveux au cours de maladies classées ailleurs | Paralysie urémique (N18.-†) |

Logique pédagogique : G99 rassemble trois grands tableaux d'examen — (1) la **neuropathie autonome diabétique ou amyloïde** (cardiovasculaire, digestive avec gastroparésie, génito-urinaire) ; (2) la **myélopathie secondaire** (dégénérative cervicale, discale, tumorale/métastatique) ; (3) l'atteinte neurologique **urémique**.

## 1. Question clinique

- Chez un diabétique : reconnaître la neuropathie autonome cardiovasculaire (tachycardie de repos, hypotension orthostatique, ischémie silencieuse) qui augmente la mortalité, et la gastroparésie (nausées, vomissements, plénitude) [S5][S3].
- Chez un sujet de plus de 50 ans avec maladresse des mains, troubles de la marche, paresthésies progressives : penser myélopathie cervicale dégénérative, IRM cervicale, avis spécialisé (« Time is Spine ») [S8][S10].
- Chez un patient cancéreux avec douleur rachidienne et signes neurologiques : compression médullaire métastatique = urgence absolue, IRM de tout le rachis sans délai [S13].
- Neuropathie autonome + polyneuropathie à progression rapide, perte de poids, canal carpien bilatéral, cardiopathie hypertrophique : rechercher une amylose ATTR [S7][S6].

## 2. Définitions et classifications

### 2.1 Neuropathie autonome cardiovasculaire (NAC) diabétique
- Complication microvasculaire sous-reconnue mais très fréquente [S5].
- **Hypotension orthostatique (HO) classique** : baisse progressive et soutenue de la PAS ≥ 20 mmHg ou de la PAD ≥ 10 mmHg ; la Task Force ESC ajoute une **PAS < 90 mmHg** debout comme anormale ; une chute diastolique isolée est très rare [S4]. En présence d'hypertension de décubitus, seuil de chute systolique ≥ 30 mmHg [S5].
- HO **neurogène** : élévation de la fréquence cardiaque à l'orthostatisme habituellement ≤ 10 bpm (peut être plus élevée en cas d'anémie ou d'hypovolémie) [S4].
- **Stadification de Toronto** (tests cardiovasculaires réflexes, CARTs) : 1 test de fréquence anormal = NAC possible/précoce ; ≥ 2 tests anormaux = NAC confirmée ; tests de fréquence anormaux + HO = NAC sévère/avancée [S5].

### 2.2 Gastroparésie (G99.00)
- Consensus UEG/ESNM : **symptômes associés à une vidange gastrique retardée en l'absence d'obstruction mécanique** (énoncé 1.1, accord 100 %, grade A) ; s'y ajoute une fonction motrice gastrique sévèrement perturbée (1.2, 85 %) [S3].
- Symptômes cardinaux : **nausées et vomissements** (1.3, 95 %) ; souvent plénitude postprandiale, satiété précoce, douleur épigastrique, ballonnement/éructations (1.4, 95 %) [S3].

### 2.3 Myélopathie
- « Myélopathie cervicale » : maladie de la moelle épinière à l'étage cervical, quelle qu'en soit l'origine, faite de symptômes et signes témoignant d'une atteinte des fibres descendantes et ascendantes [S9].
- **Myélopathie radiologique** : diminution du diamètre antéro-postérieur, hypersignal T2 médullaire, hyposignal T1, diminution de la surface de section ou de l'espace disponible pour la moelle [S9].
- **Myélopathie cervicale dégénérative (MCD, DCM)** : dysfonction médullaire par compression cervicale (ancien terme : myélopathie cervicarthrosique) ; causes dégénératives : hernie discale, hypertrophie ou ossification ligamentaire, ostéophytes = spondylose [S8].
- Sévérité par le score **mJOA** (modified Japanese Orthopaedic Association) : **léger 15–17, modéré 12–14, sévère ≤ 11** (AO Spine 2026, faible niveau de preuve) [S11].
- **Compression médullaire métastatique (MSCC)** : épidurite carcinomateuse = étiologie la plus fréquente [S13].

### 2.4 Neuropathie amyloïde (ATTR)
- Amylose ATTR avec polyneuropathie : maladie systémique progressive par dépôt endoneural de transthyrétine mal repliée ; polyneuropathie héréditaire de l'adulte la plus grave ; variant TTR héréditaire [S7].
- Stades de locomotion : **stade 1** atteinte limitée aux membres inférieurs, marche sans aide ; **stade 2** handicap net, aides à la marche ; **stade 3** fauteuil roulant ou alitement ; correspondance avec le score PND I–IV [S7].

## 3. Épidémiologie

- **NAC** : ≈ 20 % des diabétiques ; 29–54 % (type 1) et 12–73 % (type 2) selon population et définition ; 9–38 % dans le prédiabète (vs 0–18 % en normoglycémie) [S5]. Cohorte danoise (Steno, 822 DT1, 899 DT2) : neuropathie autonome 6–39 % (DT1) et 9–49 % (DT2) selon le test ; polyneuropathie et neuropathie autonome coexistent dans seulement 50 % des cas [S15]. Cohorte polonaise 2026 (728 diabétiques, critères de Toronto) : NAC 48,2 % (précoce 32,4 %, confirmée 15,8 %), associée à la rétinopathie (OR 2,26) [S16].
- **Gastroparésie** : épidémiologie réelle mal connue ; facteurs de risque : diabète (2.2, accord 100 %), chirurgie gastrique, certaines maladies neurologiques et du tissu conjonctif, médicaments (opioïdes, 2.8, 100 %) [S3]. Incidence cumulée à 10 ans : **5,2 % (DT1), 1,0 % (DT2), 0,2 % (témoins)** ; plus fréquente dans le DT1 [S3].
- **MCD** : prévalence opérée 1,6/100 000 (vraisemblablement sous-estimée) ; diagnostic surtout dans la cinquantaine, rare avant 40 ans ; compression médullaire asymptomatique à l'IRM chez 59 % (108/183) de volontaires de 40–80 ans (31,6 % à la 5ᵉ décennie, 66,8 % à la 8ᵉ) [S8]. La MCD est la cause la plus fréquente de lésion médullaire non traumatique (Balgrist, Zurich) [S10].
- **MSCC** : touche jusqu'à **5–10 %** des patients ayant des métastases ou atteintes tumorales osseuses [S13].
- **ATTRv** : pays endémiques Portugal, Japon, Suède, Brésil ; dysautonomie chez ≈ 73 % des patients [S7].

## 4. Mécanismes : du normal au pathologique

- **NAC** : hyperglycémie, dyslipidémie, stress oxydatif, inflammation médiée par les produits de glycation avancée, microangiopathie ; atteinte **longueur-dépendante** : le **nerf vague**, plus long nerf autonome, est touché en premier → déficit parasympathique puis prédominance sympathique → tachycardie de repos (jusqu'à ≈ 130 bpm), puis fréquence fixe et intolérance à l'effort aux stades avancés [S5].
- **HO neurogène** : défaut de vasoconstriction sympathique à l'orthostatisme ; dans la défaillance autonome, l'HO s'associe souvent à un profil tensionnel nocturne « non-dipper » ou « reverse-dipper » [S4].
- **Gastroparésie** : le panel UEG/ESNM n'a **pas** atteint de consensus sur la physiopathologie (perte de la fonction vagale 68 %, perte des cellules interstitielles de Cajal 60 %, non retenues) ; il n'a pas non plus retenu que le retard de vidange explique à lui seul les symptômes (28 %) [S3].
- **Myélopathie** : la moelle souffre par **compression directe** ou par **diminution de la microvascularisation et ischémie secondaire** [S9]. Le déficit dépend du niveau, de la cinétique de compression et de la réserve vasculaire [S9]. Les signaux intramédullaires IRM reflètent souvent une activité biologique en cours plutôt qu'une perte tissulaire fixée [S17].
- **Urémie** : l'hyperkaliémie chronique est le mécanisme principal proposé de la neuropathie urémique (corrélation forte kaliémie–altérations nerveuses, indépendamment de la cause de la maladie rénale) ; atteinte axonale longueur-dépendante (« dying back ») [S18].
- **ATTR** : dépôt amyloïde endoneural ; atteinte des petites fibres et autonome ; forme précoce (< 50 ans) familiale avec dysautonomie, forme tardive souvent sporadique à prédominance périphérique [S7].

## 5. Causes (codes †)

- Diabète (E10–E14.4†), amylose (E85.-†) → G99.0 [S1].
- Défaillance autonome secondaire selon l'ESC : diabète, amylose, lésion médullaire, neuropathies autonomes auto-immunes et paranéoplasiques, insuffisance rénale [S4] → G99.0 ou G99.1 selon la cause.
- Spondylose (M47†), discopathies (M50.0†, M51.0†), tumeurs (C00–D48†) → G99.2 [S1].
- Maladie rénale chronique (N18†) → G99.8 (paralysie urémique) [S1].

## 6. Anamnèse

- **NAC** : vertiges, lipothymies, syncopes à l'orthostatisme ; intolérance à l'effort ; questionnaires (COMPASS 31) utiles pour repérer le risque mais ne remplacent pas les CARTs [S5].
- **Gastroparésie** : nausées, vomissements, plénitude, satiété précoce ; médicaments (opioïdes) [S3].
- **ATTR** : impuissance (73 % des hommes), troubles digestifs (53 %), alternance constipation–diarrhée, incontinence urinaire (50 %), dysrégulation orthostatique (46 %), perte de poids (≈ 30 %) ; antécédents familiaux, canal carpien bilatéral [S7].
- **MCD** : douleur ou raideur cervicale ; faiblesse, engourdissement ou perte de dextérité des membres supérieurs ; raideur, faiblesse des membres inférieurs ; paresthésies ; troubles vésicaux/intestinaux, dysfonction érectile ; instabilité, chutes ; trait constant : **aggravation sur des mois** ; les symptômes peuvent précéder les signes [S8]. Retard diagnostique moyen 2,2 ans, 5,2 ± 3,6 consultations ; 43 % se présentent par engourdissement ou douleur de la main, souvent étiquetés canal carpien [S8]. Troubles de l'initiation mictionnelle en premier, puis globe, puis incontinence et atonie sphinctérienne aux stades tardifs [S9].
- **MSCC** : douleurs radiculaires, parésie, troubles sensitifs ou sphinctériens chez un patient porteur de métastases ou d'atteinte tumorale osseuse [S13].

## 7. Examen clinique

- **HO** : mesure de la PA couché puis debout (lever actif, sphygmomanomètre) suffisante pour HO classique et retardée [S4].
- **MCD** : faiblesse pyramidale, hyperréflexie, spasticité, clonus achilléen, **signe de Hoffmann**, **signe de Babinski**, faiblesse segmentaire, déficit sensitif, signe de Lhermitte (cas sévères), trouble de la marche ; examen **peu sensible mais spécifique** : un examen normal n'exclut pas la MCD [S8].
- **MSCC** : douleurs radiculaires, parésie avec syndrome pyramidal, hypo-/anesthésie, troubles sphinctériens, syndrome de la queue de cheval [S13].

## 8. Diagnostic et diagnostic différentiel

### 8.1 Neuropathie autonome
- Référence : **CARTs** — variabilité de la FC à la respiration profonde (rapport E/I), rapport de Valsalva, rapport 30:15 au lever, réponse tensionnelle au lever [S5].
- QT long : spécifique 86 %, sensible 28 % (méta-analyse) [S5]. Hypoglycémie : allongement du QTc (415 → 445 ms lors d'une hypoglycémie induite) [S5].
- Test d'inclinaison (tilt) : pour l'HO retardée manquée par le lever actif et pour le POTS ; MAPA de 24 h : hypertension nocturne, hypotension postprandiale [S4].

### 8.2 Gastroparésie
- **Endoscopie haute obligatoire** (5.1, 93 %, grade A) pour exclure une obstruction ; **test de vidange anormal obligatoire** (5.3, 95 %) ; scintigraphie valide (5.4, 98 %) ; test respiratoire valide (5.5, 95 %) ; imagerie pour exclure une occlusion du grêle (5.8, 88 %) [S3]. Pas de soutien pour la capsule motrice ni l'échographie gastrique [S3]. Rétention à 4 h > 20 % citée comme facteur pronostique [S3].

### 8.3 Myélopathie
- **IRM cervicale** = examen à demander ; urgente si progression ou retentissement important ; la sévérité de la compression et le signal médullaire corrèlent mal avec les symptômes [S8]. Séquence T2 la plus sensible et spécifique ; CT moins utile (artéfacts C6–D1), utile pour la sténose foraminale osseuse ; myélo-CT si IRM contre-indiquée ou peu concluante [S9].
- Électrophysiologie : PES (fibres myélinisées de gros calibre), PEM (premier motoneurone) [S9].
- Diagnostics trompeurs : canal carpien (43 % des présentations initiales de MCD) [S8]. Hémiparésie avec clonus/hyperréflexie : penser aussi à une cause cervicale si l'IRM cérébrale est normale (cas illustratif) [S9].
- **MSCC** : IRM de **l'ensemble** de la colonne sans délai [S13].
- Nouvelles approches (IRM quantitative, neurophysiologie avancée, métriques dynamiques) permettent de détecter des lésions subcliniques [S10].

### 8.4 Amylose ATTR
- Séquençage des 4 exons du gène **TTR** (une variante seule ne confirme pas : pénétrance incomplète) ; **biopsie** (rouge Congo, biréfringence vert pomme ; sites peu invasifs : glandes salivaires labiales, peau, graisse abdominale ; ≥ 2 sites si le premier est négatif) ; **scintigraphie osseuse** (DPD, HMDP, PYP) pour l'atteinte cardiaque ; typage de l'amylose (spectrométrie de masse) pour exclure AL [S7]. Diagnostics confondants : PIDC, polyneuropathie axonale idiopathique, canal lombaire étroit, plus rarement neuropathie diabétique, amylose AL [S7].
- Position ESC : définitions invasive et non invasive de l'amylose cardiaque, scénarios de suspicion et algorithme diagnostique [S6].

## 9. Urgences

- **MSCC** : urgence absolue ; IRM de tout le rachis sans délai ; corticothérapie systémique, radiothérapie ou laminectomie de décompression selon le contexte ; équipe multidisciplinaire (neurochirurgie, radiologie, oncologie, radiothérapie) [S13].
- **MCD** : la compression médullaire d'une hernie discale peut évoluer rapidement vers la plégie et les troubles sphinctériens [S9]. Manipulation cervicale **strictement contre-indiquée** [S8].
- **NAC** : HO associée à une mortalité accrue (ACCORD : HR 1,61 toutes causes ; HR 1,85 décès ou hospitalisation pour insuffisance cardiaque) ; ischémie myocardique silencieuse plus fréquente (RR 1,96) ; mortalité à 5 ans 25–50 % en cas de NAC avancée [S5].

## 10. Prise en charge (Suisse/Europe)

### 10.1 Neuropathie autonome diabétique — prévention
- Contrôle glycémique intensif (DCCT/EDIC) : prévalence NAC 28,9 % vs 35,2 % dans le DT1 [S5]. Prise en charge multifactorielle (Steno-2, n = 160) dans le DT2 [S5]. Exercice : amélioration de la fonction autonome cardiaque dans 15 études sur 18 [S5].
- Tachycardie de repos : bêtabloquants [S5]. Agonistes GLP-1 : augmentent la FC ; à éviter en cas de gastroparésie [S5]. Acide alpha-lipoïque : pas de recommandation internationale [S5].

### 10.2 Hypotension orthostatique (ESC 2018) [S4]
- Éducation ; arrêt/réduction des vasoactifs (antihypertenseurs, nitrés, diurétiques, neuroleptiques, antidépresseurs, dopaminergiques).
- **Eau 2–3 L/j et 10 g de NaCl/j** (si pas d'hypertension) ; ingestion rapide d'eau fraîche.
- Manœuvres de contre-pression (croiser les jambes, accroupissement) ; bas de contention/ceinture abdominale ; **tête du lit surélevée > 10°** (réduit polyurie et hypertension nocturnes).
- **Midodrine 2,5–10 mg 3×/j** en première ligne additionnelle dans la défaillance autonome chronique ; **fludrocortisone 0,1–0,3 mg/j** ; droxidopa : preuves insuffisantes pour l'usage prolongé.
- Ne traiter que l'HO symptomatique [S5]. Augmenter la PA debout de 10–15 mmHg suffit souvent à une amélioration fonctionnelle [S4].

### 10.3 Gastroparésie (UEG/ESNM) [S3]
- Adaptation diététique (6.1, 85 %) ; **antagonistes D2** efficaces (6.7, 86 %) ; **agonistes 5-HT4** (6.14, 85 %) ; agonistes motiline (érythromycine) non retenus (58 %) ; IPP et antiémétiques en première ligne non retenus ; nutrition entérale ou parentérale si perte de poids sévère ou vomissements réfractaires (6.39, 98 %).
- Pas de consensus pour toxine botulique pylorique, stimulation électrique gastrique, myotomie pylorique endoscopique, gastrectomie.
- Pronostic dépendant de la cause (7.2, 88 %) ; pas de consensus sur une espérance de vie raccourcie.

### 10.4 Myélopathie cervicale dégénérative
- AO Spine 2017 : **chirurgie recommandée pour MCD modérée et sévère** ; MCD légère : chirurgie ou essai supervisé de rééducation structurée, chirurgie si détérioration (recommandé) ou absence d'amélioration (suggéré) ; pas de chirurgie prophylactique chez le patient non myélopathique avec compression sans radiculopathie, mais information et suivi ; si radiculopathie associée, risque accru de myélopathie : chirurgie ou suivi rapproché [S12].
- Suisse : la myélopathie cervicale symptomatique pose **per se** l'indication chirurgicale ; dès qu'une myélopathie clinique est présente, plus de place pour le traitement conservateur ; décompression le plus souvent par discectomie antérieure avec cage [S9].
- Évaluation spécialisée pour toute MCD ; récupération maximale vers 6–12 mois ; traitement dans les 6 mois après les symptômes = meilleures chances (série AO Spine, 746 patients) ; douleur résiduelle fréquente [S8].
- Balgrist 2026 : décompression soutenue dans les formes modérées à sévères ; formes légères et sténose à risque : prise en charge interdisciplinaire, surveillance active ou chirurgie sélectionnée [S10]. AO Spine 2026 : chirurgie à discuter dans la MCD légère avec douleur et index d'incapacité cervicale élevés ; informer que les déficits sensitifs des membres supérieurs persistent fréquemment après décompression [S11].

### 10.5 MSCC
- Corticothérapie, radiothérapie, chirurgie de décompression selon le contexte, en équipe multidisciplinaire [S13].

### 10.6 Neuropathie urémique
- Restriction potassique alimentaire (avec résine échangeuse) neuroprotectrice à 24 mois dans un essai randomisé ; gabapentinoïdes en première ligne de la douleur neuropathique métabolique (sans posologie rénale fournie par la source) [S18]. Hémodiafiltration vs hémodialyse : essai FINESSE (protocole) — la majorité des hémodialysés ont des signes de neuropathie urémique, sans traitement modificateur connu [S19].

### 10.7 Médicaments — informations professionnelles suisses (AIPS via AmiKo, lues le 15.10.2026)
- **Midodrine (Gutron®)** [S20] : indications incluant l'**HO secondaire (p. ex. neuropathie diabétique)** et formes sévères (HO idiopathique, Shy-Drager). Formes sévères : début 3 × 2,5 mg/j, première dose 30–45 min avant le lever, adaptation hebdomadaire selon la PAS 3 min après le lever, jusqu'à 15 mg/j dans certains cas. Dernière dose **≥ 4 h avant le coucher** (hypertension de décubitus) ; PA couchée et assise ≥ 2×/semaine en début de traitement. CI : cardiopathie organique sévère, hypertension, arythmies, maladie rénale aiguë, insuffisance rénale sévère, rétention urinaire, **rétinopathie diabétique proliférante**, phéochromocytome, hyperthyroïdie, glaucome à angle fermé, grossesse/allaitement.
- **Fludrocortisone (Florinef®)** [S21] : indications suisses = insuffisance corticosurrénale (Addison), syndrome de perte de sel ; **l'HO n'est pas une indication autorisée** (usage hors indication si prescrit selon ESC). Adulte : 0,1 mg 3×/semaine à 0,2 mg/j ; rétention sodée, œdèmes, hypertension, hypokaliémie → contrôle électrolytique ; CI : hypertension artérielle sévère, ulcères GI aigus, mycoses systémiques, etc.
- **Dompéridone (Motilium®)** [S22] : indication suisse = nausées et vomissements (≥ 12 ans, ≥ 35 kg) ; 10 mg 3×/j, 15–30 min avant les repas ; **durée continue ≤ 1 semaine** ; CI : allongement QTc, troubles électrolytiques significatifs, insuffisance cardiaque, inhibiteurs puissants du CYP3A4 allongeant le QT, insuffisance hépatique modérée/sévère, prolactinome.
- **Métoclopramide (Paspertin®)** [S23] : 10 mg jusqu'à 3×/j, max 30 mg/j ou 0,5 mg/kg ; **durée maximale 5 jours** (dyskinésies tardives potentiellement irréversibles) ; réduction de 50 % (ClCr 15–60) et 75 % (ClCr ≤ 15) ; CI : Parkinson, antécédent de dyskinésie tardive, épilepsie, phéochromocytome, hémorragie/occlusion/perforation digestive, association à la L-dopa.
- **Tafamidis (Vyndaqel® 61 mg et 20 mg)** [S24] : indication suisse = **cardiomyopathie** amyloïde à transthyrétine (sauvage ou héréditaire) ; 61 mg tafamidis ou 80 mg tafamidis méglumine 1×/j ; non interchangeables mg pour mg. Aucune indication suisse lue pour la polyneuropathie ATTR (voir Lacunes).

## 11. Suivi

- ATTRv : réévaluation tous les **6–12 mois** selon sévérité et réponse (NIS, COMPASS-31, Sudoscan, NYHA) [S7].
- Patient non myélopathique avec compression : information sur les signes de myélopathie et suivi clinique [S12].
- Midodrine : contrôle régulier de la fonction rénale au long cours [S20] ; fludrocortisone : électrolytes [S21].

## 12. Situations particulières

- Personnes âgées : HO fréquente et sous-diagnostiquée ; chutes, vertiges, syncopes, confusion ; causes : vieillissement, médicaments, déshydratation, causes neurologiques [S25].
- Fracture de hanche : 18 % de patients sans diagnostic préalable avaient des signes évocateurs de MCD [S8].
- ATTRv leptoméningée : transplantation hépatique moins efficace (TTR produite par les plexus choroïdes) [S7].
- Diabète + hypoglycémie : risque accru d'arythmie (+42 %), de décès CV (+59 %), de mortalité toutes causes (+68 %) [S5].

## 13. Critères formels (pour le div.alert)

- **HO** (ESC 2018) : chute PAS ≥ 20 mmHg ou PAD ≥ 10 mmHg, ou PAS < 90 mmHg debout [S4] ; ≥ 30 mmHg si hypertension de décubitus [S5].
- **NAC** (Toronto) : 1 CART anormal = possible/précoce ; ≥ 2 = confirmée ; + HO = sévère [S5].
- **Gastroparésie** (UEG/ESNM) : symptômes + vidange retardée objectivée + absence d'obstruction mécanique (endoscopie) [S3].
- **MCD** : symptômes/signes médullaires + compression cervicale à l'IRM ; sévérité mJOA 15–17 / 12–14 / ≤ 11 [S8][S11].
- **ATTR-PN** : variante TTR + dépôt amyloïde à la biopsie + typage TTR [S7].

## 14. Paramètres clés (pour le div.key)

- NAC ≈ 20 % des diabétiques ; mortalité à 5 ans 25–50 % si avancée [S5].
- Gastroparésie : incidence à 10 ans 5,2 % (DT1) vs 1,0 % (DT2) [S3].
- MCD : retard diagnostique 2,2 ans ; compression asymptomatique 59 % à 40–80 ans ; traitement < 6 mois = meilleur pronostic [S8].
- MSCC : 5–10 % des patients avec métastases osseuses ; IRM de tout le rachis sans délai [S13].
- Midodrine : dernière dose ≥ 4 h avant le coucher [S20] ; métoclopramide ≤ 5 j [S23] ; dompéridone ≤ 1 semaine [S22].
- HO : eau 2–3 L/j, NaCl 10 g/j, tête du lit > 10° [S4].

## Lacunes

1. **Aucune source suisse spécifique lue** sur la neuropathie autonome diabétique, la gastroparésie diabétique ou la neuropathie urémique (pas de recommandation SSED/SGED ni Swiss Medical Forum trouvée ; quota WebSearch épuisé). L'article RMS 2025 sur l'HO du sujet âgé [S25] n'a été lu qu'au résumé (accès payant).
2. Seuils exacts de rétention scintigraphique (2 h/4 h) non trouvés dans la portion lue du consensus UEG/ESNM ; le délai de dépistage de la NAC (DT1 après x ans, DT2 au diagnostic) n'est pas donné par [S5].
3. Recommandations NICE NG234 (MSCC) non accessibles directement (HTTP 403) ; les points MSCC reposent sur RMS 2016 [S13]. Le dossier de la leçon G55 (cycle 37) contient une lecture NICE antérieure, non relue ici : à ne pas utiliser sans vérification.
4. Présentation clinique propre de la neuropathie/paralysie urémique (prévalence en dialyse, effet de la transplantation) non documentée par la source lue [S18] ; seule la mention « majorité des hémodialysés » de [S19].
5. G99.1 : la CIM-10-GM ne donne aucun exemple ; seules les causes de défaillance autonome secondaire de l'ESC [S4] l'illustrent.
6. Traitements spécifiques de la polyneuropathie ATTR (patisiran, vutrisiran, inotersen, eplontersen) : FI suisses non lues ; tafamidis autorisé en Suisse seulement pour la cardiomyopathie selon la FI lue.
7. Myélopathies tumorales intramédullaires, myélopathie par compression de l'artère spinale antérieure (M47.0) : aucune source spécifique lue.
8. Dates de mise à jour des FI non extractibles par l'outil (champ vide) ; consultation datée du 15.10.2026.
9. Guideline AO Spine 2017 [S12] : groupe international (AO Foundation, Davos) à forte participation nord-américaine ; utilisé comme référence internationale de chirurgie rachidienne, corroboré par l'équipe suisse du Balgrist [S10] et la RMS [S9].
