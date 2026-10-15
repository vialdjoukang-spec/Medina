# C94 — Autres leucémies à cellules précisées (H-08-Hématologie)

Dossier de recherche du cycle Betta 35, leçon 1 (agent C35-A3-HEM, Opus 5.5), consulté le 15.10.2026.
Chaque affirmation provient d'une source réellement lue ; la clé entre crochets renvoie à `sources.json`.
Statut : audit différé. Il s'agit d'une revue IA, distincte d'une validation médicale humaine.

## 0. Question clinique
C94 est une catégorie « tiroir » qui regroupe des hémopathies rares et hétérogènes. La leçon doit apprendre à reconnaître chacune, à éviter le piège de codage et à orienter vers un centre d'hématologie :
- un adulte âgé avec pancytopénie et blastes érythroïdes en excès, souvent TP53 muté : **leucémie aiguë érythroïde (C94.0)** [WHO5-2022 ; BFARM-C94] ;
- un enfant avec trisomie 21 et blastes exprimant CD41/CD61 : **leucémie aiguë mégacaryoblastique (C94.2)**, liée à une mutation GATA1 [WHO5-2022 ; ONKO-AML2025] ;
- une tryptase très élevée, des mastocytes ≥ 20 % sur l'aspiration médullaire et des atteintes d'organe : **leucémie à mastocytes (C94.3)** [ONKO-SM2024] ;
- une moelle « sèche » à la ponction, fibrotique, avec blastes ≥ 20 % : **panmyélose aiguë avec myélofibrose (C94.4)** [SEER-APMF ; BFARM-C94] ;
- un patient porteur d'une LMC qui perd sa réponse et présente ≥ 20 % de blastes : **crise blastique de LMC (code additionnel C94.8!)** [ONKO-CML2026 ; BFARM-C94].

## 1. Nosologie CIM-10-GM 2024 : sous-codes couverts
- **C94** « Autres leucémies à cellules précisées » (OFS). Exclusions : leucémie à tricholeucocytes (« Leukämische Retikuloendotheliose », C91.4-) et leucémie à plasmocytes (C90.1-) [BFARM-C94].
- Code additionnel **C95.8!** pour une leucémie réfractaire à l'induction standard [BFARM-C94].
- 5e caractère : **0** = sans mention de rémission complète (inclut « sans mention de rémission » et rémission partielle) ; **1** = en rémission complète [BFARM-C94]. Sous-codes OFS : C94.00/.01, C94.20/.21, C94.30/.31, C94.40/.41, C94.60/.61, C94.70/.71 et C94.8! [OFS-GM2024 via nosology/fragments/S06.json].
- **C94.0** Polyglobulie primitive aiguë et érythroleucose (OFS) — inclut **AML M6 (a) et (b)**, érythroleucémie [BFARM-C94 ; OFS-GM2024].
- **C94.2** Leucémie aiguë à mégacaryocytes — inclut leucémie aiguë mégacaryocytaire, **AML M7** [BFARM-C94].
- **C94.3** Leucémie à mastocytes [BFARM-C94].
- **C94.4** Panmyélose aiguë avec myélofibrose — inclut myélofibrose aiguë [BFARM-C94].
- **C94.6** Maladie myélodysplasique et myéloproliférative, non classifiable [BFARM-C94].
- **C94.7** Autres leucémies précisées — inclut **leucémie agressive à cellules NK** et **leucémie aiguë à basophiles** [BFARM-C94].
- **C94.8!** Crise blastique au cours d'une LMC : code « point d'exclamation », donc secondaire, ajouté au code de la LMC [BFARM-C94 ; OFS-GM2024]. Absence de C94.1 et C94.5 dans la GM 2024 [BFARM-C94].
- Note de passage : la classification OMS 2022 renomme « MDS/MPN, unclassifiable » en **MDS/MPN, NOS** [WHO5-2022].

## 2. Définitions et classifications (OMS 5e édition 2022, ICC 2022)
### 2.1 Règle générale LAM
- Le seuil de 20 % de blastes sépare toujours SMD et LAM ; la plupart des LAM à anomalie génétique définissante n'exigent plus de seuil, sauf BCR::ABL1 et CEBPA (≥ 20 %) ; les LAM définies par la différenciation exigent en général ≥ 20 % de blastes, **à l'exception de la LAE** [WHO5-2022].
- ICC 2022 : ≥ 10 % de blastes pour les anomalies génétiques récurrentes, ≥ 20 % sinon, catégorie SMD/LAM à 10–19 % [ONKO-AML2025].
- Dans l'OMS 2022, « érythroleucémie aiguë » et « leucémie aiguë mégacaryoblastique » figurent parmi les LAM **définies par la différenciation** [ONKO-AML2025 ; WHO5-2022].
### 2.2 Leucémie aiguë érythroïde (C94.0)
- Prédominance érythroïde, habituellement **≥ 80 %** des éléments médullaires, avec **≥ 30 % de proérythroblastes** ; des cas < 80 % sont admis s'ils partagent les mêmes caractères clinico-pathologiques [WHO5-2022].
- Altérations **bialléliques de TP53** très fréquentes ; terme apparenté accepté : « leucémie érythroïde pure » ; la LAE prime sur la LAM-MR [WHO5-2022].
- Le changement de définition depuis l'OMS 2001 déplace des cas vers les SMD ; dans une série rétrospective monocentrique, les patients relevant des SMD selon l'OMS 2022 survivent nettement mieux, tandis que la LAE OMS 2022 évolue mal quel que soit le traitement (chimiothérapie intensive ou hypométhylant) [AEL-HMA2025]. Limite : série américaine rétrospective, utilisée pour un fait pronostique, non pour une conduite.
### 2.3 Leucémie aiguë mégacaryoblastique (C94.2)
- Blastes exprimant au moins une glycoprotéine plaquettaire : **CD41, CD61 ou CD42b** [WHO5-2022].
- Trois groupes : enfants avec syndrome de Down, enfants sans syndrome de Down, adultes ; immunophénotype « RAM » corrélé à **CBFA2T3::GLIS2** [WHO5-2022].
- Syndrome de Down : mutations somatiques de **GATA1** (exons 2 ou 3) ; **myélopoïèse anormale transitoire** limitée aux 6 premiers mois de vie et **leucémie myéloïde du syndrome de Down (ML-DS)** [WHO5-2022]. Traitement d'intensité réduite : survie ≈ 90 % ; rechutes très difficiles à traiter [ONKO-AML2025].
- Une biopsie ostéomédullaire peut être nécessaire en cas de myélofibrose (ponction blanche) [ONKO-AML2025].
### 2.4 Leucémie à mastocytes (C94.3)
- Mastocytose : trois types (systémique, cutanée, sarcome mastocytaire) ; sous-types de MS : médullaire, indolente, « smoldering », agressive, avec néoplasie hématologique associée (SM-AHN), **leucémie à mastocytes (MCL)** [WHO5-2022].
- **Critère majeur MS** : infiltrats mastocytaires compacts multifocaux (≥ 15 cellules) en histologie. **Critères mineurs** : mastocytes atypiques fusiformes, mutation KIT, expression aberrante CD2/CD25/CD30, tryptase sérique persistante > 20 µg/l (corrigée en cas d'α-tryptasémie héréditaire). Diagnostic : 1 majeur + 1 mineur, ou 3 mineurs [ONKO-SM2024 ; WHO5-2022].
- **MCL** : ≥ **20 % de mastocytes** sur l'aspiration médullaire (hors grumeaux) ; **aiguë** si signes C, **chronique** sinon ; forme **aleucémique** (fréquente) ou **leucémique** (rare) ; primaire ou secondaire [ONKO-SM2024].
- KIT codon 816 muté dans > 90 % des MS [WHO5-2022] ; les MCL KIT D816V-négatives sont plus fréquentes et de pronostic plus mauvais [ONKO-SM2024].
- **Signes B** : infiltration médullaire > 30 % avec tryptase > 200 µg/l, charge KIT ≥ 10 %, dysplasie ou myéloprolifération, organomégalie sans dysfonction [ONKO-SM2024 ; WHO5-2022].
- **Signes C** : cytopénies (neutrophiles < 1 G/l, Hb < 10 g/dl, plaquettes < 100 G/l), hépatopathie, splénomégalie avec hypersplénisme, malabsorption avec hypoalbuminémie et amaigrissement, atteinte d'organe menaçante, ostéolyses étendues avec fractures pathologiques [ONKO-SM2024].
- Diagnostic différentiel : leucémie aiguë à basophiles (C94.7) — blastes métachromatiques au bleu de toluidine, MPO/SBB/NSE négatifs, **sans forte expression de CD117**, ce qui exclut la MCL [WHO5-2022].
### 2.5 Panmyélose aiguë avec myélofibrose (C94.4)
- Prolifération panmyéloïde aiguë avec blastes **≥ 20 %** (moelle ou sang) et fibrose médullaire ; aspiration habituellement infructueuse ; **biopsie avec immunohistochimie indispensable** ; anomalies -5/del(5q), -7/del(7q) ; marqueurs CD13, CD33, CD34, CD117 [SEER-APMF].
- Très rare, surtout adulte ; survie « de quelques mois » ; listée dans la table des LAM de l'OMS 5e édition selon SEER [SEER-APMF]. **Lacune** : statut exact dans OMS 2022/ICC 2022 non confirmé par une source européenne lue (le résumé OMS 2022 lu ne la mentionne pas) [WHO5-2022]. Source registre américaine utilisée uniquement pour la définition, non pour une conduite.
### 2.6 SMD/NMP non classifiable → MDS/MPN, NOS (C94.6)
- Cas associant caractères SMD et NMP sans critères d'un type précis ; définitions des cytopénies identiques aux SMD [WHO5-2022]. **Lacune** : seuils chiffrés (leucocytes, plaquettes) non lus.
### 2.7 Leucémie agressive à cellules NK (C94.7)
- Hémopathie lymphoproliférative rare, très maligne, liée à l'**EBV**, surtout en Asie et Amérique latine [ANKL-HSCT2025] ; forme leucémique disséminée apparentée aux lymphomes NK/T [NKT-REV2019].
- Méta-analyse (6 études, 295 patients) : l'allogreffe améliore la survie globale (HR 0,47 ; IC 95 % 0,32–0,68) et la survie sans progression (HR 0,22) [ANKL-HSCT2025]. Les schémas à base de L-asparaginase sont recommandés dans les lymphomes NK/T disséminés, les anthracyclines étant inefficaces (P-glycoprotéine) [NKT-REV2019]. Limite : sources asiatiques, pas de recommandation européenne lue.
### 2.8 Crise blastique de LMC (C94.8!)
- **OMS 2022 (recommandée par Onkopedia)** : ≥ 20 % de blastes myéloïdes dans le sang ou la moelle, **ou** augmentation des lymphoblastes, **ou** prolifération blastique extramédullaire ; la **phase accélérée est supprimée** [WHO5-2022 ; ONKO-CML2026].
- ICC 2022 : ≥ 20 % de blastes ; lymphoblastes > 5 % → évoquer une phase blastique lymphoïde ; ELN 2020 : ≥ 20 % + atteinte extramédullaire [ONKO-CML2026].
- Patients à 20–30 % de blastes : survie plus proche de ≥ 30 % que de 10–20 % [ONKO-CML2026].

## 3. Épidémiologie
- LAM (toutes formes) : ≈ 3,7/100 000/an, > 100/100 000 après 70 ans, âge médian 72 ans (registre suédois) [ONKO-AML2025]. Proportion spécifique de LAE et de LAMK : **lacune**.
- MS indolente ≈ 1/100 000 ; MS avancée ≈ 1–2 par million [ONKO-SM2024].
- Crise blastique de LMC : devenue rare sous ITK dans les pays occidentaux, plus fréquente là où le diagnostic est tardif [ONKO-CML2026].
- Leucémie agressive NK : prédominance Asie/Amérique latine [ANKL-HSCT2025].
- Données suisses (registre) : **lacune**.

## 4. Mécanismes : normal → pathologique
- LAE : perte biallélique de TP53 → instabilité génomique, caryotype complexe fréquent, mauvaise réponse aux traitements [WHO5-2022 ; AEL-HMA2025].
- LAMK/ML-DS : mutation acquise de GATA1 (facteur de transcription de la lignée mégacaryocytaire/érythroïde) sur fond de trisomie 21 [WHO5-2022 ; ONKO-AML2025].
- Mastocytose : KIT D816V → activation de KIT indépendante du ligand, prolifération mastocytaire ; libération de médiateurs (symptômes, risque d'anaphylaxie) ; infiltration d'organes → signes C [WHO5-2022 ; ONKO-SM2024].
- LMC → crise blastique : acquisition d'anomalies chromosomiques additionnelles à haut risque (réarrangements 3q26.2, -7, i(17q), caryotype complexe) et de mutations du domaine kinase BCR::ABL1 (T315I) [ONKO-CML2026].
- Leucémie NK agressive : transformation de cellules NK infectées par l'EBV [ANKL-HSCT2025 ; TX-EBV2022].

## 5. Anamnèse et examen clinique
- Leucémies aiguës : signes d'insuffisance médullaire (fatigue, infections, saignements), douleurs osseuses, perte de poids [SEER-APMF ; ONKO-AML2025].
- Mastocytose avancée : symptômes de médiateurs ; organomégalie ; malabsorption ; fractures ; patient porteur d'un kit d'urgence avec adrénaline auto-injectable [ONKO-SM2024].
- LMC : surveiller les signes d'alerte sous ITK (absence de rémission hématologique complète, résistance à deux ITK, anomalies additionnelles, mutations complexes) [ONKO-CML2026].
- Examen clinique détaillé spécifique (hépatosplénomégalie quantifiée, signes cutanés) : **lacune** partielle.

## 6. Examens complémentaires
- Bilan LAM obligatoire (Onkopedia tableau 1) : hémogramme, cytologie et biopsie médullaires (**biopsie obligatoire en cas de ponction blanche**), immunophénotypage, caryotype, panel moléculaire (FLT3-ITD/TKD, NPM1, CEBPA, IDH1/2, TP53, RUNX1, ASXL1…), recherche de fusions (PML::RARA, CBFB::MYH11, RUNX1::RUNX1T1, BCR::ABL1, KMT2A), bilan de l'aptitude (ECOG, HCT-CI, fonctions d'organes, typage HLA, CMV, sérologies hépatites/VIH, échocardiographie, fonction pulmonaire) [ONKO-AML2025].
- LAMK : CD41/CD61/CD42b en cytométrie ; GATA1 si syndrome de Down [WHO5-2022].
- Mastocytose : histologie médullaire, KIT D816V (charge allélique), CD2/CD25/CD30, tryptase basale, exclusion d'une α-tryptasémie héréditaire [ONKO-SM2024].
- Crise blastique : cytométrie pour le phénotype myéloïde/lymphoïde, mutations du domaine kinase BCR::ABL1, cytogénétique, NGS ciblé (IDH1/2, NRAS, FLT3 parfois exploitables), recherche rapide de donneur [ONKO-CML2026].
- Stratification ELN 2022 (favorable/intermédiaire/défavorable) ; TP53 muté, caryotype complexe, -7 = défavorable [ONKO-AML2025].

## 7. Urgences
- Hyperleucocytose : hydroxyurée (jusqu'à 4–5 g/j si leucocytes > 50–100 G/l) ; anthracyclines seulement après baisse < 30 G/l [ONKO-AML2025].
- Syndrome de lyse tumorale : hydratation, rasburicase ; leucostase souvent révélée par des symptômes pulmonaires [ONKO-AML2025].
- Mastocytose : anaphylaxie → adrénaline auto-injectable ; anti-H1 et anti-H2 en prophylaxie de base [ONKO-SM2024].

## 8. Prise en charge (Onkopedia, applicable en Suisse ; FI Swissmedic)
### 8.1 LAE, LAMK, panmyélose (traitement de LAM)
- Patient apte : induction « 7+3 » (anthracycline 3 j, p. ex. daunorubicine 60 mg/m², + cytarabine 100–200 mg/m²/j en continu 7 j) ; CPX-351 pour LAM liée aux myélodysplasies ou post-thérapeutique ; consolidation par cytarabine haute dose ou allogreffe selon le risque [ONKO-AML2025].
- Allogreffe en RC1 pour risque intermédiaire ou défavorable si patient apte et donneur disponible [ONKO-AML2025].
- Patient inapte : vénétoclax + azacitidine en première priorité (VIALE-A : RC/RCi 28,3 % → 66,4 % ; survie médiane 9,6 → 14,7 mois) ; démarrage si leucocytes < 25 G/l, montée de dose sur 3 jours, prophylaxie de lyse, premier cycle hospitalier ; adaptation avec inhibiteurs du CYP3A (posaconazole : 50–100 mg/j) [ONKO-AML2025].
- LAE : pronostic mauvais quel que soit le schéma (intensif ou hypométhylant) [AEL-HMA2025].
- ML-DS de l'enfant : traitement d'intensité réduite, survie ≈ 90 % [ONKO-AML2025].
### 8.2 Leucémie à mastocytes
- **Midostaurine (Rydapt®)** : indiquée en Suisse dans la mastocytose systémique avancée (MSA, MS-AHN, MCL) ; **100 mg 2×/j** ; prophylaxie antiémétique (Onkopedia : anti-5-HT₃) ; étude D2201 (n = 116) : réponse globale 59,6 %, survie globale médiane 26,8 mois dans la population évaluable ; précautions : pneumopathie interstitielle, QT, interactions CYP3A4 (éviter les inducteurs puissants), éthanol dans la capsule [FI-RYDAPT ; ONKO-SM2024].
- **Avapritinib (Ayvakyt®)** : en Suisse, MS avancée **après au moins un traitement systémique** ; **200 mg 1×/j** (dose maximale) ; non recommandé si plaquettes < 50 G/l ; risques : hémorragie intracrânienne (accrue si plaquettes < 50 G/l et dose ≥ 300 mg), effets cognitifs, QT ; éviter inhibiteurs/inducteurs puissants ou modérés du CYP3A (si inhibiteur modéré inévitable : 50 mg/j) [FI-AYVAKYT]. Onkopedia rapporte aussi l'autorisation européenne dans la MS indolente symptomatique (fin 2023) [ONKO-SM2024].
- Cladribine (hors indication) 0,14 mg/kg × 5 j, 3–6 cycles ; polychimiothérapie intensive dans la MCL rapidement progressive, souvent suivie d'allogreffe, **seule option potentiellement curative** [ONKO-SM2024].
- Traitement antimédiateur (anti-H1/anti-H2) et kit d'urgence avec adrénaline [ONKO-SM2024].
### 8.3 Crise blastique de LMC
- Chimiothérapie combinée intensive + ITK, idéalement **dasatinib ou ponatinib**, puis allogreffe ; inaptes : chimiothérapie à faible dose ou épigénétique (azacitidine + vénétoclax) avec ITK ; T315I : ponatinib ou asciminib (2 × 200 mg/j) ; viser une seconde phase chronique avant greffe ; greffe d'un patient résistant non recommandée hors étude ; surveiller le SNC en phase lymphoïde (meilleur pronostic) [ONKO-CML2026].
### 8.4 Leucémie agressive NK
- Allogreffe associée à un bénéfice de survie [ANKL-HSCT2025] ; régimes contenant de la L-asparaginase [NKT-REV2019]. **Lacune** : aucune recommandation suisse/européenne lue.

## 9. Suivi
- LAM : contrôle de rémission à J14 environ (« ponction précoce »), après récupération, avant chaque consolidation ; hémogramme tous les 1–3 mois les années 1–2, puis tous les 3–6 mois les années 3–5 ; MRD par cytométrie multiparamétrique ou RT-qPCR selon la cible [ONKO-AML2025].
- Mastocytose indolente/stable : contrôle au moins annuel ; hausse de la tryptase basale ou de la charge KIT D816V = signe précoce de progression [ONKO-SM2024].

## 10. Pronostic
- MCL : survie médiane ≈ 0,5–1,5 an (MS agressive ≈ 4 ans ; MS-AHN 2–3 ans) [ONKO-SM2024].
- Panmyélose avec myélofibrose : quelques mois [SEER-APMF].
- LAE OMS 2022 : mauvaise quel que soit le traitement [AEL-HMA2025].
- Crise blastique de LMC : mauvaise, améliorée modestement par l'allogreffe [ONKO-CML2026].

## 11. Critères formels du diagnostic (pour `div.alert`)
- LAE : érythroïdes ≥ 80 % + proérythroblastes ≥ 30 % [WHO5-2022].
- LAMK : blastes ≥ 20 % exprimant CD41, CD61 ou CD42b [WHO5-2022].
- MCL : critères de MS (1 majeur + 1 mineur, ou 3 mineurs) + mastocytes ≥ 20 % sur l'aspiration ; aiguë si signes C [ONKO-SM2024].
- Crise blastique LMC (OMS 2022) : blastes myéloïdes ≥ 20 % ou lymphoblastes augmentés ou atteinte extramédullaire [WHO5-2022 ; ONKO-CML2026].

## 12. Paramètres clés (pour `div.key`)
- Seuil SMD/LAM 20 % ; ICC 10 % pour anomalies génétiques récurrentes [WHO5-2022 ; ONKO-AML2025].
- Tryptase > 20 µg/l (mineur) ; > 200 µg/l avec infiltration > 30 % (signe B) [ONKO-SM2024].
- Signes C : neutrophiles < 1 G/l, Hb < 10 g/dl, plaquettes < 100 G/l [ONKO-SM2024].
- Midostaurine 100 mg 2×/j ; avapritinib 200 mg 1×/j, non recommandé si plaquettes < 50 G/l [FI-RYDAPT ; FI-AYVAKYT].
- Vénétoclax-azacitidine : démarrer si leucocytes < 25 G/l [ONKO-AML2025].

## 13. Lacunes explicites
1. Aucune source suisse primaire (SSH, Swiss Medical Forum) lue : l'article de la Revue Médicale Suisse sur la mastocytose est resté inaccessible (délai dépassé).
2. Statut de la panmyélose aiguë avec myélofibrose dans OMS 2022/ICC 2022 non confirmé par source européenne.
3. Seuils chiffrés du MDS/MPN, NOS non lus.
4. Leucémie aiguë à basophiles : seulement critères OMS ; épidémiologie et traitement non lus.
5. Leucémie agressive NK : aucune recommandation européenne ; sources asiatiques seulement.
6. Données d'incidence suisses et proportions de LAE/LAMK parmi les LAM.
7. Recommandations ELN 2022 lues indirectement via Onkopedia (article original non lu).
8. FI Swissmedic du vénétoclax, de la cytarabine, du dasatinib/ponatinib non lues dans ce dossier.
