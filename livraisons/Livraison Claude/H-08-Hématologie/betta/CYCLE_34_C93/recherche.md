# C93 — Leucémie monocytaire (H-08-Hématologie)

Dossier de recherche du cycle Betta 34, leçon 2 (agent C34-A3-HEM, Opus 5.5), consulté le 15.10.2026.
Chaque affirmation provient d'une source réellement lue ; la clé entre crochets renvoie à `sources.json`.
Statut : audit différé. Il s'agit d'une revue IA, distincte d'une validation médicale humaine.

## 0. Question clinique
Un homme de 76 ans a, sur une formule sanguine de routine, des monocytes à 1,4 G/l (> 10 % des leucocytes), persistants depuis plus de 3 mois, une anémie modérée et une rate palpable. Il faut écarter une **monocytose réactive** (infection, sepsis, tuberculose, VIH, maladie auto-immune), puis évoquer une **leucémie myélomonocytaire chronique (LMMC, C93.1)**, la confirmer par frottis, moelle, caryotype, biologie moléculaire et cytométrie, la stratifier (CPSS/CPSS-mol) et choisir entre surveillance, cytoréduction, agent hypométhylant ou allogreffe [ONKO-CMML2023 ; WHO5-2022].
Seconde situation : un adulte présente une **hyperplasie gingivale**, des nodules cutanés et une hyperleucocytose ; il faut penser à une **leucémie aiguë monoblastique/monocytaire (C93.0, AML M5)**, traiter les urgences (leucostase, CIVD, lyse tumorale) et orienter vers un centre d'hématologie [ONKO-AML2025 ; BFARM-C93].
Troisième situation, pédiatrique : un nourrisson de moins de 2 ans avec splénomégalie et monocytose > 1 G/l évoque une **leucémie myélomonocytaire juvénile (LMMJ, C93.3)** [JMML-2021].

## 1. Nosologie CIM-10-GM 2024 : sous-codes couverts
- **C93** « Leucémie monocytaire » (OFS) ; inclusion BfArM : « Monozytoide Leukämie ». Code additionnel C95.8! pour une leucémie réfractaire à l'induction standard [BFARM-C93 ; OFS-GM2024].
- 5e caractère : **0** = sans mention de rémission complète (inclut la rémission partielle) ; **1** = en rémission complète [BFARM-C93]. Sous-codes OFS : C93.00/.01, C93.10/.11, C93.30/.31, C93.70/.71, C93.90/.91 [OFS-GM2024 via nosology/fragments/S06.json].
- **C93.0** Leucémie monoblastique/monocytaire aiguë — inclut **AML M5, M5a, M5b** [BFARM-C93].
- **C93.1** Leucémie myélomonocytaire chronique — inclut leucémie monocytaire chronique, **LMMC-1, LMMC-2, LMMC avec éosinophilie** [BFARM-C93]. La LMMC est **exclue de C92.1** (LMC BCR::ABL1 positive) [BFARM-C93].
- **C93.3** Leucémie myélomonocytaire juvénile ; **C93.7** autres ; **C93.9** sans précision [BFARM-C93].
- Piège de codage : la **leucémie aiguë myélomonocytaire (AML M4, y compris M4Eo avec inv(16)/t(16;16)) est codée C92.5**, pas C93 [BFARM-C93].

## 2. Définitions et classifications
### 2.1 LMMC (WHO 5e édition 2022, reprise par Onkopedia 2023)
- **Prérequis** : monocytose persistante absolue **≥ 0,5 G/l** et relative **≥ 10 %** ; blastes (myéloblastes, monoblastes, **promonocytes comptés comme équivalents blastiques**) **< 20 %** dans le sang et la moelle ; exclusion de LMC BCR::ABL1+, autres NMP (MFP, PV, TE) et des néoplasies avec fusion de tyrosine kinase [WHO5-2022 ; ONKO-CMML2023].
- **Critères de soutien** : dysplasie d'au moins une lignée (> 10 % des cellules) ; anomalie clonale cytogénétique ou moléculaire acquise ; répartition anormale des sous-populations monocytaires en cytométrie [WHO5-2022 ; ONKO-CMML2023].
- **Règle** : monocytes ≥ 1,0 G/l → un critère de soutien suffit ; 0,5 à < 1,0 G/l → critères 1 **et** 2 requis [WHO5-2022]. L'abaissement de 1,0 à 0,5 G/l intègre la « LMMC oligomonocytaire » [WHO5-2022].
- **Sous-types** : **LMMC dysplasique (MD)** si leucocytes < 13 G/l ; **proliférative (MP)** si ≥ 13 G/l [WHO5-2022 ; ONKO-CMML2023].
- **Selon les blastes** : **LMMC-1** < 5 % sang et < 10 % moelle ; **LMMC-2** 5–19 % sang et 10–19 % moelle ; **LMMC-0 supprimée** ; ≥ 20 % = LAM [WHO5-2022 ; ONKO-CMML2023]. Incohérence notée dans Onkopedia : < 5 % dans le texte, ≤ 4 % dans le tableau 3 [ONKO-CMML2023].
- L'ICC 2022 diffère peu de l'OMS [ONKO-CMML2023]. Exclure **KIT D816V** pour ne pas méconnaître une mastocytose systémique associée [ONKO-CMML2023].
### 2.2 LAM à différenciation monocytaire (C93.0)
- LAM = ≥ 20 % de blastes (sang, moelle ou tissu), sauf entités définies génétiquement ; l'OMS 2022 supprime le seuil de 20 % pour la plupart des anomalies génétiques définissantes (sauf BCR::ABL1 et CEBPA) ; réarrangements **KMT2A** diagnosticables avec < 20 % de blastes ; l'ICC retient 10 % [WHO5-2022 ; ONKO-AML2025].
- **LAM monocytaire (OMS 2022, « définie par la différenciation »)** : ≥ 80 % de monocytes et/ou monoblastes/promonocytes, < 20 % de granuleux en maturation ; blastes et promonocytes exprimant ≥ 2 marqueurs monocytaires (CD11c, CD14, CD36, CD64) ou positifs à l'estérase non spécifique (NSE) [WHO5-2022].
- **LAM myélomonocytaire** (comparaison ; codée C92.5) : ≥ 20 % de monocytes et précurseurs et ≥ 20 % de granuleux en maturation ; ≥ 3 % de blastes MPO+ [WHO5-2022 ; BFARM-C93].
- **LAM avec réarrangement KMT2A** : chez l'adulte, blastose souvent élevée, **habituellement à différenciation monocytaire** ; partenaires fréquents MLLT3 (t(9;11)) et MLLT10 [WHO5-2022 ; ONKO-AML2025]. KMT2A réarrangé : 5–15 % des LAM, pronostic défavorable [ONKO-AML2025].
- Stratification génétique ELN 2022 (favorable/intermédiaire/défavorable) ; schéma ELN 2024 pour les traitements moins intensifs [ELN2022 ; ONKO-AML2025].
### 2.3 LMMJ (C93.3)
- Leucémie pédiatrique rare, à la frontière SMD/NMP ; **classée NMP par l'OMS 2022**, avec exclusion des réarrangements KMT2A et retrait de la monosomie 7 comme critère cytogénétique ; accent sur l'activation de la voie RAS [WHO5-2022 ; JMML-2021].
- > 90 % portent une mutation **PTPN11, NRAS, KRAS, NF1 ou CBL** [JMML-2021]. Diagnostic : variant pathogène de la voie RAS, phénotype de RASopathie, ou les deux [WHO5-2022].
- Critères biologiques : monocytes > 1 × 10⁹/l (sauf exception), blastes médullaires < 20 %, blastes sanguins médians 2 %, thrombopénie et anémie habituelles, splénomégalie presque constante [JMML-2021].
### 2.4 Lacune de définition
- Les seuils FAB distinguant **M5a (monoblastique)** et **M5b (monocytaire)** n'ont pas été lus dans une source de référence européenne (page Pathology Outlines inaccessible, HTTP 429) : **ne pas les chiffrer** dans la leçon ; se limiter à « M5a à prédominance de monoblastes, M5b à prédominance de promonocytes et monocytes » uniquement si une source est ajoutée, sinon citer l'inclusion BfArM sans seuil.

## 3. Épidémiologie
- **LMMC** : environ 20 % des SMD (cadre Onkopedia), incidence **0,5–1,0/100 000/an**, âge médian au diagnostic **≈ 76 ans**, prédominance masculine (≈ 3:1 en section épidémiologie, « environ deux fois » en section 3.2.2 — incohérence de la source) ; prévalence croissante avec le vieillissement [ONKO-CMML2023].
- **LAM (toutes formes)** : ≈ 3,7/100 000/an, > 100/100 000 après 70 ans ; âge médian 72 ans (registre suédois) [ONKO-AML2025]. Proportion spécifique des M5 : **lacune**.
- **LMMJ** : 1,2 enfant par million et par an, ≈ 2 % des hémopathies malignes pédiatriques ; moitié diagnostiquée avant 2 ans ; deux tiers de garçons [JMML-2021].
- Données suisses spécifiques (registre) : **lacune**.

## 4. Mécanismes : normal → pathologique
- Hématopoïèse clonale : mutations somatiques chez **> 90 %** des LMMC en NGS ; régulateurs épigénétiques (TET2 ≈ 60 %, ASXL1 ≈ 40 %, DNMT3A, IDH1/2, EZH2), épissage (SRSF2 ≈ 50 %, SF3B1, U2AF1), réparation de l'ADN (TP53), signalisation/transcription (JAK2, RAS 10–30 %, RUNX1) [ONKO-CMML2023].
- Monocytose : hypothèse d'**α-défensines des granuleux dysplasiques inhibant la différenciation des monocytes** [ONKO-CMML2023].
- Signature cytométrique : accumulation de **monocytes classiques CD14+/CD16−** ; seuil **> 94 %** distinguant LMMC et monocytose réactive [ONKO-CMML2023].
- LMMJ : hyperactivation de la voie RAS (PTPN11, NRAS, KRAS, NF1, CBL) ; hypersensibilité au GM-CSF historiquement décrite, aujourd'hui largement dispensable au diagnostic [JMML-2021].
- LAM monocytaire et vénétoclax : la différenciation monocytaire en cytométrie (blastes co-exprimant ≥ 2 marqueurs CD4, CD36, CD64) prédit une moindre réponse à vénétoclax-azacitidine [MONO-VENAZA2025].

## 5. Causes et facteurs de risque (LMMC)
- Solvants organiques, radiothérapie antérieure, iode radioactif, chimiothérapie ; benzène discuté (fumée de tabac) ; fumeurs à risque plus élevé [ONKO-CMML2023].
- **LMMC post-thérapeutique** ≈ 10 %, latence médiane ≈ 6 ans, pronostic défavorable [ONKO-CMML2023].
- Maladies auto-immunes et inflammation chronique ; rares mutations germinales (DDX41) [ONKO-CMML2023].
- LAM : rechercher une prédisposition germinale (DDX41, CEBPA, RUNX1) si histoire familiale évocatrice [ONKO-AML2025]. LAM myélo-monoblastique post-thérapeutique typiquement avec t(9;11) [ONKO-AML2025].
- LMMJ : syndrome de Noonan (trouble myéloprolifératif associé, souvent spontanément résolutif) ; mutation germinale CBL (résolution spontanée fréquente) [JMML-2021].

## 6. Anamnèse et examen clinique
- **LMMC** : souvent découverte fortuite ; forme MD : cytopénies (infections, saignements, besoins transfusionnels) ; forme MP : **splénomégalie ≈ 50 %**, infiltrations extramédullaires (peau, plèvre, péritoine) si hyperleucocytose ; manifestations auto-immunes ≈ 20 % (vascularite, PTI, psoriasis, polyarthrite rhumatoïde, syndrome de Sweet), parfois des années avant [ONKO-CMML2023].
- Une hausse isolée des monocytes ne prouve pas la progression : une infection peut la produire [ONKO-CMML2023].
- **LAM monocytaire** : symptômes des cytopénies ; leucocytose chez ≈ 60 % des LAM ; atteintes extramédullaires fréquentes dans les formes myélomonocytaires et monoblastiques : **infiltrats cutanés, hyperplasie gingivale, atteinte méningée, infiltration splénique ou hépatique** ; CIVD et hyperfibrinolyse possibles [ONKO-AML2025].
- **LMMJ** : splénomégalie presque constante, hépatomégalie, adénopathies ; atteinte pulmonaire (toux sèche, tachypnée, infiltrats interstitiels) ; lésions cutanées eczématiformes, papules ou nodules, pétéchies ; SNC rarement atteint [JMML-2021].

## 7. Examens complémentaires
### 7.1 LMMC (tableau 2 Onkopedia)
- **Obligatoires** : morphologie sang et moelle (dysplasie, blastes, monocytes, sidéroblastes en couronne ; coloration des estérases et du fer) ; **caryotype** (≈ 80 % normal ; del(7) et +8 les plus fréquents) ; FISH si caryotype insuffisant ; biologie moléculaire si méthodes non concluantes ; imagerie de la rate [ONKO-CMML2023].
- **Recommandés** : histologie médullaire (fibrose, cellularité) ; cytométrie (CD14+/CD16− > 94 %) [ONKO-CMML2023]. Gènes pronostiques : RUNX1, NRAS, SETBP1, ASXL1 [ONKO-CMML2023].
### 7.2 LAM (tableau 1 Onkopedia)
- Hémogramme, morphologie et cytochimie médullaires (biopsie obligatoire si ponction blanche), immunophénotypage (CD33, MPO ; CD4, CD56, CD123, TCL1 pour exclure un néoplasme à cellules dendritiques plasmacytoïdes blastiques) [ONKO-AML2025].
- Caryotype et FISH ; panel moléculaire : NPM1, FLT3-ITD (rapport allélique), FLT3-TKD, CEBPA, **KMT2A**, autres ; recherche de translocations [ONKO-AML2025].
- Bilan d'aptitude (ECOG, HCT-CI), chimie, **coagulation**, test de grossesse, sérologies hépatites/VIH, radiographie thoracique, ECG, échocardiographie, fonction pulmonaire ; typage HLA et statut CMV si candidat à la greffe [ONKO-AML2025].
- Ponction lombaire : obligatoire initialement en pédiatrie [ONKO-AML2025] ; chez l'adulte, recommandation non lue : **lacune**.
### 7.3 LMMJ
- Monocytes, blastes, HbF (pronostique), caryotype (≈ 2/3 normal ; monosomie 7 la plus fréquente), génétique de la voie RAS [JMML-2021].

## 8. Diagnostic différentiel
- **Monocytose réactive** : infection, sepsis, tuberculose, VIH, maladie auto-immune [ONKO-CMML2023].
- **Autres néoplasies clonales** : autres SMD/NMP, MFP, LMC atypique (NMP avec neutrophilie), mastocytose systémique, LMC, leucémie chronique à éosinophiles, néoplasies avec fusion TK, tricholeucocytose, leucémie à grands lymphocytes granuleux, LMMJ, LAM M4/M5 [ONKO-CMML2023].
- Autres causes de splénomégalie : hépatopathie, maladies de surcharge, infections [ONKO-CMML2023].
- LMMJ : infection disséminée par BCG avec hémophagocytose peut mimer une LMMJ (rapport de cas, non lu en texte intégral) : **mention seulement si source ajoutée**.

## 9. Urgences
- **Leucostase/hyperleucocytose** (≈ > 100 G/l) : hydroxyurée (jusqu'à 4–5 g/j), cytarabine si nécessaire ; anthracycline seulement quand les leucocytes < 30 G/l [ONKO-AML2025]. LAM monoblastique avec hyperleucocytose : cytoréduction rapide (p. ex. cytarabine) et soins de support [ONKO-AML2025].
- **Lyse tumorale** et **CIVD** : urgences à traiter d'emblée [ONKO-AML2025].
- Prévention de la lyse sous vénétoclax (LAM) : leucocytes **< 25 G/l** avant le début (cytoréduction si besoin), hydratation, hypo-uricémiant, potassium/urate/phosphate/calcium/créatinine avant la 1re dose, puis 6–8 h après chaque palier et 24 h après la dose cible [FI-VENCLYXTO ; ONKO-AML2025].

## 10. Prise en charge (Suisse : Onkopedia endossé par SGH-SSH et SSOM ; FI Swissmedic)
### 10.1 LMMC
- **Pronostic** : CPSS (LMMC-2, leucocytes > 13 G/l, dépendance transfusionnelle, cytogénétique) — Low 0, Int-1 1, Int-2 2–3, High 4–5 ; **CPSS-mol** ajoute ASXL1, NRAS, RUNX1, SETBP1 et un seuil blastique médullaire ≥ 5 % — Low 0, Int-1 1, Int-2 2–3, High ≥ 4 ; score de Düsseldorf sans cytogénétique ; survie médiane **12–36 mois** ; transformation en LAM **15–30 %** [ONKO-CMML2023].
- **Bas risque (Low, Int-1)** : habituellement pas de traitement spécifique, surveillance [ONKO-CMML2023].
- **Soutien** : transfusions érythrocytaires selon la clinique (Hb > 9 g/dl en coronaropathie sévère) ; plaquettes surtout en cas de saignement ; antibiothérapie libérale ; vaccins pneumocoque, COVID-19, grippe ; chélation du fer si espérance de vie > 2 ans et ≥ 20 CE ou ferritine > 1000 ng/ml ; ASE si EPO < 200 U/l, faible besoin transfusionnel (≤ 2 CE/8 semaines), blastes ≤ 10 %, forme dysplasique, réévaluation à 6 mois [ONKO-CMML2023].
- **Haut risque (Int-2, High)** : cytoréduction envisagée [ONKO-CMML2023].
  - **Hydroxyurée** : premier choix de la forme proliférative ; bénéfice de survie contre étoposide dans un essai randomisé [ONKO-CMML2023]. FI suisse Litalir : indication « LMC et autres syndromes myéloprolifératifs » — la LMMC n'y est pas nommée ; surveillance hémogramme, moelle, fonctions rénale et hépatique [FI-LITALIR].
  - **Azacitidine** : FI suisse — patients **non éligibles à l'allogreffe** avec **LMMC** (indication nommée) ; 75 mg/m²/j s.c. **7 jours tous les 28 jours**, au moins **6 cycles** avant d'évaluer la réponse [FI-AZACITIDIN ; ONKO-CMML2023]. Onkopedia : forme dysplasique avec excès de blastes ou leucocytes < 13 G/l [ONKO-CMML2023].
  - Décitabine contre hydroxyurée dans la LMMC proliférative avancée (phase III) : pas de bénéfice de survie [ONKO-CMML2023]. En Suisse, Dacogen n'est autorisé que pour la LAM non éligible à la chimiothérapie intensive [FI-DACOGEN].
  - Ruxolitinib hors indication (symptômes, splénomégalie) ; avapritinib/midostaurine si mastocytose associée ; irradiation splénique exceptionnelle ; autogreffe non indiquée [ONKO-CMML2023].
- **Allogreffe** : seule option curative, d'abord chez le sujet jeune, en bon état, à haut risque ; survie ≈ 30 % à 3–4 ans (EBMT n = 513 ; série française n = 73) ; échecs ≈ moitié rechute, moitié toxicité/GvH [ONKO-CMML2023].
### 10.2 LAM monoblastique/monocytaire (C93.0)
- **Induction intensive 7+3** : anthracycline 3 jours (daunorubicine 60 mg/m² ou idarubicine 10–12 mg/m² ou mitoxantrone 10–12 mg/m²) + cytarabine 100–200 mg/m² en continu 7 jours ; ajouts selon génétique (gemtuzumab ozogamicine si CD33+ et profil favorable ; quizartinib/midostaurine si FLT3) [ONKO-AML2025].
- LAM liée au traitement ou avec anomalies associées aux myélodysplasies : **CPX-351 (Vyxeos liposomal)** — FI : daunorubicine 44 mg/m² + cytarabine 100 mg/m² aux jours 1, 3 et 5 de la 1re induction, jours 1 et 3 de la 2e ; consolidation 29/65 mg/m² jours 1 et 3 [FI-VYXEOS ; ONKO-AML2025].
- **Consolidation** : cytarabine haute dose (favorable) ; **allogreffe en RC1** si risque intermédiaire ou défavorable, patient apte et donneur [ONKO-AML2025]. Le pronostic défavorable des réarrangements KMT2A rend ce point central [ONKO-AML2025].
- **Patient non apte** : **vénétoclax + azacitidine** standard de première priorité (VIALE-A : RC/RCi 66,4 % vs 28,3 % ; survie médiane 14,7 vs 9,6 mois) ; décitabine jugée d'efficacité semblable [ONKO-AML2025]. FI Venclyxto : paliers 100 → 200 → 400 mg (J1–J3) puis 400 mg/j avec azacitidine 75 mg/m² J1–7 ou décitabine 20 mg/m² J1–5 ; 600 mg/j avec cytarabine faible dose ; adaptation aux inhibiteurs du CYP3A (posaconazole, voriconazole…) [FI-VENCLYXTO ; ONKO-AML2025]. Cycle 1 hospitalier ; moelle à J21–28 [ONKO-AML2025].
- **Particularité monocytaire** : monoblastes ≥ 10 % des CD45+ en cytométrie → RC moins fréquentes (OR 0,24) et survie médiane 4,0 vs 14,9 mois sous vénétoclax-azacitidine, facteur indépendant (HR 1,95) [MONO-VENAZA2025].
- **Rechute** : allogreffe seule chance réelle ; inhibiteurs de ménine (révuménib) pour KMT2A réarrangé — réponse 64 % (AUGMENT-101) ; autorisation suisse **non vérifiée (lacune)** [ONKO-AML2025].
- Patient > 75 ans biologiques ou comorbide : traitement curatif intensif non recommandé (≈ 10 % de rémission prolongée) [ONKO-AML2025].
### 10.3 LMMJ
- **Allogreffe** = seule option curative pour la plupart : conditionnement busulfan-cyclophosphamide-melphalan (EWOG-MDS) ; survie globale 55–73 %, mortalité liée à la greffe 10–15 %, rechute 25–35 % [JMML-2021].
- **Azacitidine** pré-greffe (100 mg/m²/j × 5 j ou 75 mg/m²/j × 7 j, tous les 28 j, 6–9 cycles) ; d'emblée dans KRAS et nombreux PTPN11 [JMML-2021]. Statut d'autorisation pédiatrique suisse : **lacune**.
- Noonan, CBL germinal, certains NRAS avec HbF basse : surveillance possible (régression spontanée) [JMML-2021].

## 11. Suivi
- **LMMC** : taille de la rate annuelle (échographie si besoin) ; hémogramme et chimie fréquents au début puis tous les 3 mois ; moelle (morphologie, cytogénétique, mutations) si suspicion de progression (anémie ou thrombopénie nouvelle, blastes circulants) ; post-allogreffe : trimestriel la 1re année, tous les 4 mois la 2e, puis semestriel (chimérisme, MRD, néoplasies secondaires) [ONKO-CMML2023].
- **LAM** : hémogramme tous les 1–3 mois les années 1–2, puis 3–6 mois les années 3–5 ; moelle si suspicion de rechute ; MRD : MFC > 10⁻⁴ ou NPM1/CBF > 2 % en fin de consolidation = risque accru [ONKO-AML2025]. Critères de réponse : **RC** < 5 % blastes médullaires, pas d'atteinte extramédullaire, PNN ≥ 1 G/l, plaquettes ≥ 100 G/l, pas de blastes circulants ; RCh, RCi ; rechute ≥ 5 % blastes ou blastes circulants inexpliqués ou maladie extramédullaire [ONKO-AML2025].
- **LMMJ** : sans traitement, la survie décroît pendant 10 ans puis atteint un plateau ≈ 25 % ; facteurs de risque : âge ≥ 2 ans, HbF, plaquettes, mutations secondaires, classe de méthylation ; NF1/PTPN11 somatique/méthylation élevée → rechute post-greffe > 50 % [JMML-2021].

## 12. Situations particulières
- Grossesse : azacitidine contre-indiquée (tératogène, mutagène) [FI-AZACITIDIN].
- Interactions : vénétoclax + inhibiteurs puissants du CYP3A → adaptation de dose (posaconazole : 50–100 mg/j selon Onkopedia) [FI-VENCLYXTO ; ONKO-AML2025].
- Pédiatrie : voir LMMJ ; ponction lombaire initiale obligatoire dans la LAM de l'enfant [ONKO-AML2025].

## 13. Critères formels du diagnostic (pour `div.alert`)
- LMMC (OMS 2022) : monocytes ≥ 0,5 G/l **et** ≥ 10 %, persistants (Onkopedia : 3 mois) ; blastes + promonocytes < 20 % ; exclusion LMC/NMP/fusion TK ; ≥ 1 G/l → 1 critère de soutien ; 0,5–1 G/l → dysplasie **et** clonalité [WHO5-2022 ; ONKO-CMML2023].
- LAM monocytaire (OMS 2022) : ≥ 20 % blastes (ou anomalie génétique définissante) ; ≥ 80 % lignée monocytaire, < 20 % granuleux ; ≥ 2 marqueurs monocytaires ou NSE+ [WHO5-2022].
- LMMJ : monocytes > 1 G/l, blastes < 20 %, splénomégalie, mutation de la voie RAS et/ou phénotype de RASopathie ; KMT2A exclu [JMML-2021 ; WHO5-2022].

## 14. Paramètres clés (pour `div.key`)
- Monocytose : ≥ 0,5 G/l et ≥ 10 % ; seuil MD/MP : 13 G/l ; LMMC-2 : 5–19 % sang / 10–19 % moelle ; cytométrie CD14+/CD16− > 94 % [WHO5-2022 ; ONKO-CMML2023].
- LMMC : âge médian 76 ans ; incidence 0,5–1/100 000 ; TET2 60 %, SRSF2 50 %, ASXL1 40 % ; survie médiane 12–36 mois ; transformation 15–30 % [ONKO-CMML2023].
- Azacitidine 75 mg/m² × 7 j / 28 j, ≥ 6 cycles [FI-AZACITIDIN].
- Vénétoclax : leucocytes < 25 G/l avant début ; 100/200/400 mg [FI-VENCLYXTO].
- Leucostase ≈ > 100 G/l ; anthracycline si < 30 G/l [ONKO-AML2025].
- LMMJ : 1,2/million/an ; > 90 % mutation RAS ; moitié < 2 ans [JMML-2021].

## 15. Lacunes explicites
1. Aucun article du Swiss Medical Forum ni recommandation propre de la SGH-SSH lus ; le cadre suisse repose sur Onkopedia, **endossé par SGH-SSH et SSOM** (co-auteur LMMC : S. Blum, CHUV Lausanne ; J. Passweg parmi les auteurs LAM, affiliation non affichée).
2. Seuils FAB M5a/M5b non lus dans une source fiable (ne pas chiffrer).
3. Proportion des M5 parmi les LAM et épidémiologie suisse : non trouvées.
4. Ponction lombaire systématique chez l'adulte avec LAM monocytaire : non lue.
5. ESMO LAM 2020 (Heuser, Ann Oncol, doi 10.1016/j.annonc.2020.02.018) : HTTP 403, non lue ; ELN 2022 lue au niveau du résumé seulement.
6. Statut Swissmedic du révuménib et de l'azacitidine pédiatrique : non vérifié.
7. Mécanisme des α-défensines : hypothèse rapportée par Onkopedia, non vérifiée dans la source primaire.
8. C93.7 et C93.9 : codes résiduels sans entité individualisée dans les sources lues ; à traiter comme précision diagnostique insuffisante.
