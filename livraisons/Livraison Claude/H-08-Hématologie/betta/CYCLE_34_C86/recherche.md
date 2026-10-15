# C86 — Autres lymphomes à cellules T/NK spécifiés (H-08-Hématologie)

Dossier de recherche du cycle Betta 34, leçon 1 (agent C34-A3-HEM, Opus 5.5), consulté le 15.10.2026.
Chaque affirmation provient d'une source réellement lue dans cette session ; la clé entre crochets renvoie à `sources.json`.
Statut : audit différé. Il s'agit d'une revue IA, distincte d'une validation médicale humaine.

## 0. Questions cliniques
1. Un homme de 45 ans présente une obstruction nasale unilatérale, des épistaxis et une ulcération nécrotique du palais. Il faut évoquer un **lymphome extranodal NK/T (C86.0)**, obtenir une biopsie profonde avec recherche d'EBV (EBER), doser l'**ADN d'EBV plasmatique**, faire une TEP-TDM et une IRM du massif facial, puis proposer une **radiothérapie ≥ 50 Gy associée à une chimiothérapie sans anthracycline contenant de l'asparaginase** [ESMO-EHA2025 ; TSE2022 ; ONKO-PTCL2025].
2. Un homme de 25 ans traité pour une maladie de Crohn par thiopurine et anti-TNF présente fièvre, splénomégalie, hépatomégalie et thrombopénie, **sans adénopathie**. Il faut évoquer un **lymphome hépatosplénique T (C86.1)** et faire une biopsie ostéomédullaire [CARVAO2019 ; ESMO-EHA2025].
3. Des papules récidivantes qui **régressent spontanément** en quelques semaines évoquent une **papulose lymphomatoïde (C86.6)** : maladie au pronostic excellent, à ne pas traiter par polychimiothérapie [KEMPF2011 ; WHO-EORTC2018].

## 1. Nosologie CIM-10-GM 2024 : sous-codes couverts
Intitulés français OFS (nosology/fragments/S06.json) ; inclusions et exclusions BfArM [BFARM-C86 ; OFS-GM2024].
- **C86** Autres lymphomes à cellules T/NK spécifiés. **Exclut** le lymphome anaplasique à grandes cellules ALK positif (**C84.6**) et ALK négatif (**C84.7**) [BFARM-C86].
- **C86.0** Lymphome extranodal à cellules T/NK, type nasal.
- **C86.1** Lymphome hépatosplénique à cellules T ; inclut les types alpha/bêta et gamma/delta [BFARM-C86].
- **C86.2** Lymphome à cellules T de type entéropathique ; inclut le lymphome T associé à une entéropathie (EATL) [BFARM-C86].
- **C86.3** Lymphome sous-cutané à cellules T de type panniculite.
- **C86.4** Lymphome blastique à cellules NK ; **inclut le néoplasme blastique à cellules dendritiques plasmacytoïdes (BPDCN)** [BFARM-C86].
- **C86.5** Lymphome angio-immunoblastique à cellules T ; inclut la lymphadénopathie angio-immunoblastique avec dysprotéinémie (AILD) [BFARM-C86].
- **C86.6** Syndrome lymphoprolifératif cutané primitif à cellules T, CD30 positif ; inclut la **papulose lymphomatoïde**, le **lymphome anaplasique à grandes cellules cutané primitif** et le lymphome cutané primitif CD30+ à grandes cellules T [BFARM-C86].
- Exclusions croisées : C84.5 (autres lymphomes T/NK matures) exclut explicitement toutes les entités C86.0–C86.6 ; C84.7 exclut C86.6 [BFARM-C86].
- Conséquence pédagogique : C86 regroupe **sept maladies distinctes**, de la plus indolente (papulose lymphomatoïde, survie spécifique à 5 ans 99 %) à la plus grave (lymphome T γδ et NK/T, survie à 5 ans < 20 %) [WHO-EORTC2018 tableau 1]. La leçon doit les présenter comme une famille, avec un tronc commun (lymphome T périphérique) et des fiches individuelles.

## 2. Définition et classifications
- Les lymphomes T périphériques (PTCL) sont des lymphomes agressifs au phénotype de cellules **T post-thymiques matures ou NK**, nodaux ou extranodaux. Le traitement systémique de première ligne a une intention curative. Sans traitement, la plupart des entités progressent rapidement ; exceptions : papulose lymphomatoïde, mycosis fongoïde, T-LGL et formes indolentes [ONKO-PTCL2025 §1].
- Classifications actuelles : **OMS 5e édition (WHO-HAEM5) et ICC 2022**, largement superposables [ONKO-PTCL2025 ; WHO-HAEM5].
- Correspondances avec la nomenclature actuelle [WHO-HAEM5 ; ONKO-PTCL2025] :
  - C86.0 → **lymphome extranodal NK/T (ENKTL)** ; l'OMS 5e édition **abandonne le qualificatif « type nasal »**, car la maladie touche aussi d'autres sites extranodaux [WHO-HAEM5].
  - C86.1 → **lymphome T hépatosplénique (HSTL)** : environ 75 % TCRγδ, 25 % TCRαβ, 5 % TCR silencieux ; 49 % seulement des patients ont moins de 60 ans dans une série récente, la maladie n'est donc « pas nécessairement une maladie du jeune » [WHO-HAEM5].
  - C86.2 → **EATL** (associé à la maladie cœliaque) ; le **MEITL** (lymphome T intestinal épithéliotrope monomorphe) est une entité **séparée**, sans lien avec la maladie cœliaque, à mutations SETD2 et JAK3/STAT5B ; l'EATL porte des mutations JAK1/STAT3 et des gains 9q34 [WHO-HAEM5].
  - C86.3 → **SPTCL** (lymphome T sous-cutané de type panniculite), réservé au phénotype **αβ** depuis l'étude EORTC ; la forme γδ est un lymphome T γδ cutané primitif, de pronostic très différent [WILLEMZE2008].
  - C86.4 → **BPDCN**, néoplasme dérivé des précurseurs des **cellules dendritiques plasmacytoïdes** ; depuis l'OMS 2016, entité propre classée avec les néoplasmes myéloïdes et leucémies aiguës, et non plus parmi les lymphomes NK [NGUYEN2023]. Le code CIM-10-GM C86.4 reste donc un **héritage nosologique**.
  - C86.5 → **lymphome T folliculaire helper nodal, type angio-immunoblastique (nTFHL-AI)** ; nouveau nom de l'AITL dans l'OMS 5e édition [WHO-HAEM5].
  - C86.6 → **proliférations lymphoïdes T CD30+ cutanées primitives** : papulose lymphomatoïde (LyP) et lymphome anaplasique à grandes cellules cutané primitif (pcALCL), inchangés [WHO-HAEM5 ; WHO-EORTC2018].

## 3. Épidémiologie
- Suisse : les lymphomes T représentent **environ 10 à 15 % des nouveaux lymphomes par an** (données NICER citées) ; âge médian entre la 6e et la 7e décennie ; légère prédominance masculine ; fréquence accrue en cas de **maladie auto-immune ou d'immunosuppression prolongée** [ZANDER2021].
- Europe : 10 à 15 % des LNH ; incidence globale < 1/100 000 ; rapport hommes/femmes 1,7:1 ; l'ENKTL a son incidence la plus élevée en Asie ; en Europe, les sous-types les plus fréquents sont nTFH, PTCL-NOS et ALCL [ONKO-PTCL2025 §2].
- ENKTL : nette prédominance asiatique et sud-américaine ; cas occidentaux de plus en plus rapportés [TSE2022]. Forme nasale ≈ 80 %, non nasale 15–20 % (peau, tube digestif, testicule, glandes salivaires), forme leucémique agressive < 5 % [TSE2022].
- HSTL : < 1 % des lymphomes ; environ 30 % surviennent sur immunosuppression chronique ; risque maximal chez l'**homme < 35 ans** atteint de Crohn sous thiopurine + anti-TNF ≥ 2 ans ; risque absolu estimé 1/7404 sous thiopurine seule et 1/3534 sous association [CARVAO2019]. Onkopedia : âge médian 40–60 ans ; immunosuppression préexistante, souvent iatrogène, dans environ 20 % [ONKO-PTCL2025].
- EATL : 80–90 % naissent d'une maladie cœliaque réfractaire ; risque relatif 10 à 20 fois accru [ONKO-PTCL2025].
- Lymphomes cutanés (registres néerlandais et autrichien 2002–2017) : LyP 12 % des lymphomes cutanés, pcALCL 8 %, SPTCL 1 %, NK/T extranodal < 1 % ; les CD30+ forment le 2e groupe de lymphomes T cutanés (≈ 25 %) [WHO-EORTC2018].
- BPDCN : ≈ 0,44 % des hémopathies malignes ; rapport H/F ≈ 3:1 ; surtout 7e décennie, pics bimodaux > 60 ans et < 20 ans [NGUYEN2023].
- **Lacune** : aucun chiffre suisse par sous-code C86.x n'a été trouvé.

## 4. Mécanismes : du normal au pathologique
- **Normal** : les lymphocytes T matures quittent le thymus ; les cellules NK expriment CD56 et des granules cytotoxiques (perforine, granzyme B, TIA1) sans réarrangement du récepteur T (TCR) [TSE2022]. Les T folliculaires helper (TFH) expriment CD10, BCL6, PD1, ICOS, CXCL13 [ONKO-PTCL2025].
- **ENKTL** : l'EBV est présent dans pratiquement toutes les cellules tumorales (latence II, oncoprotéine LMP1). Les cellules en apoptose libèrent de l'ADN viral dans le plasma, d'où un **marqueur de masse tumorale** [TSE2022]. Les cellules NK expriment fortement la **glycoprotéine P** (phénotype de multirésistance), ce qui explique l'**inefficacité des anthracyclines (CHOP)** [TSE2022 ; ESMO-EHA2025]. Les cellules à faible activité **asparagine synthétase** sont sensibles à l'asparaginase [TSE2022].
- **nTFHL-AI (C86.5)** : mutations acquises par étapes ; **TET2 et DNMT3A** précoces dans la cellule souche hématopoïétique (hématopoïèse clonale), **RHOA G17V et IDH2 R172** dans la cellule TFH tumorale [WHO-HAEM5 ; ONKO-PTCL2025]. RHOA G17V jusqu'à 80 % ; IDH2 ≈ un tiers [ONKO-PTCL2025]. Conséquences cliniques : hypergammaglobulinémie polyclonale, anémie hémolytique à Coombs positif, proliférations B EBV+ [ONKO-PTCL2025].
- **EATL (C86.2)** : maladie cœliaque → maladie cœliaque réfractaire de type II (lymphocytes intraépithéliaux aberrants > 20 %) → lymphome ; les patients RCD-II sont plus souvent **homozygotes HLA-DQ2** (44–60 %) ; la jéjunite ulcéreuse est par définition une RCD-II [ESSCD2019].
- **HSTL (C86.1)** : stimulation antigénique chronique et immunosuppression ; anomalies cytogénétiques **isochromosome 7q**, anomalies des chromosomes 8 et 13 [CARVAO2019].
- **SPTCL (C86.3)** : variants germinaux **perte de fonction de HAVCR2 (TIM-3)** dans environ 60 % des cas ; p.Ile97Met chez les patients d'ascendance européenne, p.Tyr82Cys en Asie de l'Est ; défaut d'expression membranaire de TIM-3 → activation immunitaire persistante, TNF-α et IL-1β accrus → **SLH** [GAYDEN2018]. Le sexe masculin et les mutations HAVCR2 augmentent le risque de SLH (OR ajusté 2,93 ; hétérozygote 4,77 ; homozygote 8,48) [MOONLA2023].
- **CD30+ cutanés (C86.6)** : réarrangements DUSP22-IRF4 dans ≈ 25 % des pcALCL ; contrairement à l'ALCL systémique, pas de translocation ALK dans la majorité des cas ; une expression ALK doit faire rechercher une atteinte cutanée secondaire d'un ALCL systémique ALK+ [WHO-EORTC2018].

## 5. Anamnèse et examen clinique
- Tronc commun PTCL : adénopathies indolores progressives et/ou atteintes extranodales (tube digestif, ORL, peau) ; **symptômes B** typiques ; infections, parfois opportunistes [ONKO-PTCL2025].
- ENKTL nasal : cavité nasale, sinus, naso- et oropharynx, voies aérodigestives supérieures ; destruction médiane (palais dur, ancien « granulome malin centrofacial ») [TSE2022].
- HSTL : splénomégalie (11/11), hépatomégalie (7/11), symptômes généraux 73 %, thrombopénie, anémie 86 %, leucopénie 71 % ; patient index sans adénopathie [CARVAO2019]. Seul PTCL non leucémique avec **atteinte médullaire presque constante**, typiquement **intrasinusoïdale** [ESMO-EHA2025].
- EATL : contexte de maladie cœliaque réfractaire ; risque de **perforation** intestinale [ESMO-EHA2025 ; ESSCD2019]. **Lacune** : tableau clinique détaillé de l'EATL non trouvé dans une source lue (perte pondérale, douleurs, saignement non sourcés).
- SPTCL αβ : nodules et plaques sous-cutanés, généralement confinés à l'hypoderme ; SLH dans 17 % [WILLEMZE2008].
- nTFHL-AI : hypergammaglobulinémie polyclonale, anémie hémolytique auto-immune [ONKO-PTCL2025].
- LyP : papules ou nodules papulonécrotiques **récidivants et autorésolutifs**, chaque lésion régresse en semaines à mois [KEMPF2011 ; WHO-EORTC2018].
- pcALCL : nodules ou tumeurs solitaires, groupés, rarement multifocaux, souvent ulcérés ; régression spontanée jusqu'à 44 % ; dissémination extracutanée 10–15 % [KEMPF2011 ; WHO-EORTC2018].
- BPDCN : plaques ou nodules érythémateux à violacés, jusqu'à 10 cm, tronc, membres, visage ; cytopénies (surtout thrombopénie) en cas d'atteinte médullaire ; ganglions, SNC possibles ; rarement sans atteinte cutanée [NGUYEN2023].

## 6. Examens complémentaires et diagnostic
- **Histologie** : biopsie chirurgicale excisionnelle ou incisionnelle chaque fois que possible (II, A) ; diagnostic posé ou confirmé par un hématopathologiste expérimenté [ESMO-EHA2025]. La concordance entre pathologie primaire et de référence est souvent faible ; nouvelle histologie à la rechute [ONKO-PTCL2025].
- Immunohistochimie : antigènes pan-T (CD2, CD3, CD5, CD7), CD4/CD8, clonalité TCR ; phénotype TFH si ≥ 2 marqueurs parmi CD10, BCL6, PD1, ICOS, CXCL13 ; **CD30** toujours testé ; **EBER** pour l'ENKTL [ONKO-PTCL2025 ; ZANDER2021].
- ENKTL : critère OMS = EBV positif + CD56 ou molécules cytotoxiques ; CD3 de surface négatif, CD3ε cytoplasmique positif, TCR germinal ; ADN d'EBV **plasmatique** (et non sang total) [TSE2022] ; ADN d'EBV quantitatif au diagnostic et pendant le traitement (II, A) ; IRM du massif facial, du SNC et des voies aérodigestives [ESMO-EHA2025].
- **Bilan d'extension** : TEP-TDM préférée au diagnostic et en fin de traitement (I, B) ; environ 10 % des PTCL sont peu ou pas avides de FDG [ESMO-EHA2025 ; ONKO-PTCL2025]. Biopsie ostéomédullaire recommandée (I, A) [ESMO-EHA2025]. Stadification selon la classification de **Lugano** [ZANDER2021].
- Laboratoire : hémogramme, chimie, LDH, sérologies **VIH, HTLV-1, hépatites B et C** ; bilan cardiaque avant anthracyclines [ZANDER2021].
- EATL/RCD-II : vidéocapsule, entéroscopie, TEP, entéro-IRM [ESSCD2019 ; ESMO-EHA2025].
- LyP typique : imagerie optionnelle, pas de biopsie médullaire. pcALCL : TDM thoraco-abdomino-pelvien injecté ± TEP ; moelle optionnelle si atteinte purement cutanée ; biopsie de tout ganglion > 1,5 cm. Stadification **TNM ISCL/EORTC** des lymphomes cutanés non MF, car Ann Arbor classerait à tort une LyP diffuse en stade IV [KEMPF2011].
- BPDCN : CD123+, CD4+, CD56+, TCL1+, marqueurs de lignée négatifs ; CD303, HLA-DR, CD7, CD33 possibles ; cytométrie et biopsie médullaire [NGUYEN2023].

## 7. Pronostic et index
- IPI (âge > 60, LDH, ECOG 2–4, stade ≥ III, > 1 site extranodal) ; **PIT** (âge, PS, LDH, atteinte médullaire) ; mPIT (Ki-67) [ONKO-PTCL2025 ; ZANDER2021]. PTCL sans ALCL ALK+ : survie à 5 ans selon PIT 75 %, 30 %, 15 %, 0 % [ZANDER2021].
- **PINK** : âge > 60, stade III/IV, atteinte ganglionnaire à distance, sous-type non nasal ; **PINK-E** ajoute l'ADN d'EBV détectable [TSE2022].
- Survie spécifique à 5 ans (lymphomes cutanés) : LyP 99 %, pcALCL 95 %, SPTCL 87 %, T γδ cutané 11 %, NK/T 16 % [WHO-EORTC2018].
- SPTCL αβ : survie globale à 5 ans 82 % ; **91 % sans SLH vs 46 % avec SLH** ; forme γδ 11 % [WILLEMZE2008].
- PTCL toutes entités : survie globale à 5 ans ≈ 30 % ; ≈ 30 % réfractaires primaires [ONKO-PTCL2025 ; ZANDER2021].
- BPDCN : survie médiane 12–14 mois ; 23 mois avec allogreffe en première rémission [NGUYEN2023].

## 8. Diagnostic différentiel (sourcé)
- ALCL systémique ALK+/ALK− (C84.6/C84.7, hors C86) ; une expression ALK sur une lésion cutanée oriente vers un ALCL systémique [BFARM-C86 ; WHO-EORTC2018].
- LyP : simule pcALCL, MF tumoral, lymphome de Hodgkin classique (type A), MF en plaques (type B), lymphome cytotoxique CD8+ épidermotrope (type D), ENKTL (type E angiocentrique) [WHO-EORTC2018].
- SPTCL : lymphome T γδ cutané primitif (atteinte (épi)dermique, ulcération, CD56±) [WILLEMZE2008]. **Lacune** : la panniculite lupique n'a pas été lue dans une source.
- HSTL : la dysmyélopoïèse médullaire peut mimer un SMD [WHO-HAEM5].
- BPDCN : LAM, lymphomes cutanés non hodgkiniens [NGUYEN2023].
- RCD-II : exclure EATL et jéjunite ulcéreuse [ESMO-EHA2025].
- Distinction réactive/tumorale : analyse de clonalité TCR [ZANDER2021].

## 9. Urgences et complications
- **Syndrome d'activation lymphohistiocytaire (SLH)** : cause la plus fréquente de SLH secondaire de l'adulte = lymphomes agressifs, notamment T γδ cutané et HSTL ; traitement rapide du lymphome [ONKO-PTCL2025]. SPTCL : SLH 17 %, pronostic divisé par deux [WILLEMZE2008].
- Perforation intestinale (EATL, troubles lymphoprolifératifs digestifs) : évaluation endoscopique du risque, résection limitée possible [ESMO-EHA2025].
- Toxicités : **syndrome de fuite capillaire** sous tagraxofusp (18 %, médiane J6, fatal 1,3 %) [ELZONRIS-FI] ; LEMP et neuropathie sous brentuximab védotine [ADCETRIS-FI] ; pancréatite et thrombose sous pégaspargase [ONCASPAR-FI].
- **Lacune** : critères HLH-2004 non lus dans ce dossier.

## 10. Prise en charge (Europe, statut suisse)
### 10.1 Principes généraux
- Inclusion dans un essai clinique chaque fois que possible (II, A) [ESMO-EHA2025].
- PTCL-NOS et nTFH : **CHOP ou CHOEP** (II, B) ; autogreffe de consolidation chez les répondeurs à haut risque (III, B) [ESMO-EHA2025]. 6–8 cycles CHOP standard ; autogreffe → survie à 5 ans ≈ 50 % chez des patients sélectionnés [ZANDER2021].
- **BV-CHP** (brentuximab védotine + cyclophosphamide, doxorubicine, prednisone ; vincristine retirée en raison de la neurotoxicité commune) : ECHELON-2 (> 450 patients, CD30 ≥ 10 %) RC 68 % vs 56 %, SSP médiane 48,8 vs 20,8 mois, bénéfice de survie globale ; bénéfice surtout dans l'ALCL [ZANDER2021 ; ONKO-PTCL2025]. ESMO-EHA : pas d'amélioration dans PTCL-NOS/TFHL, pas d'autorisation européenne pour ces entités [ESMO-EHA2025].
- **Statut suisse** : l'information professionnelle Adcetris® (juin 2025) autorise la BV avec CHP dans le **lymphome T périphérique CD30+ non prétraité** de l'adulte (formulation plus large que l'Union européenne, limitée à l'ALCL selon Onkopedia), 1,8 mg/kg i.v. toutes les 3 semaines, 6–8 cycles ; et dans le **lymphome T cutané CD30+** après traitement systémique [ADCETRIS-FI ; ONKO-PTCL2025]. En 2021, BV-CHP était autorisé en Suisse mais nécessitait une garantie de prise en charge de l'assurance [ZANDER2021] (**statut de remboursement 2026 non vérifié : lacune**).
- Allogreffe : réservée aux formes réfractaires ou en rechute ; recherche de donneur immédiate dans PTCL-NOS, nTFH à la rechute, **dès le diagnostic dans l'EATL et l'HSTL** [ONKO-PTCL2025].
- Suivi : examen clinique tous les 3 mois la 1re année, puis tous les 6 mois pendant 2 ans (sans autogreffe) ou 4 ans (avec) (IV, C) ; pas d'imagerie systématique en RC (III, D) ; arrêt possible après 3 ou 5 ans [ESMO-EHA2025]. TEP 6–8 semaines après la fin du traitement pour décider autogreffe, allogreffe ou radiothérapie [ONKO-PTCL2025].

### 10.2 ENKTL (C86.0)
- Stades I–II, patient apte : **radiothérapie IS ≥ 50 Gy** avec chimiothérapie concomitante, intercalée ou séquentielle **sans anthracycline, contenant de la L-asparaginase** (II, A) [ESMO-EHA2025]. Doses < 50 Gy → plus de rechutes locorégionales ; IMRT supérieure (SSP 5 ans 68,9 % vs 58,2 %) ; radiothérapie seule non recommandée (rechutes systémiques) [TSE2022]. 50–56 Gy + DeVIC : RC 77 %, survie à 2 ans 78 % [ONKO-PTCL2025].
- Stades III–IV : DDGP ou mSMILE (éligibles greffe), AspaMetDex ou P-GemOx (non éligibles) (III, B) ; SMILE : RG 81 %, survie à 5 ans 50 % ; DDGP vs SMILE : SSP à 1 an 86 % vs 38 % ; crisantaspase en cas d'hypersensibilité à l'asparaginase d'E. coli (III, A) [ESMO-EHA2025].
- Objectif : ADN d'EBV indétectable et Deauville ≤ 3 en fin de traitement [TSE2022].
- Rechute : pembrolizumab ou nivolumab (non autorisés EMA dans cette indication) (III, B) [ESMO-EHA2025].
- **Statut suisse** : Oncaspar® (pégaspargase) n'est autorisé que dans la **leucémie lymphoblastique aiguë** [ONCASPAR-FI] ; son emploi dans l'ENKTL est donc **hors étiquette** en Suisse (déduction à partir de l'indication autorisée).

### 10.3 HSTL (C86.1)
- Régime plus intensif que CHOP (III, A) ; **ICE** préféré (IV, B) ; méta-analyse (n = 166) : RG 82 % vs 52 %, survie médiane 37 vs 18 mois pour les schémas non-CHOP [ESMO-EHA2025].
- Consolidation par greffe, de préférence **allogénique** (III, A) ; EBMT : SSP à 3 ans 51 %, survie 55 % [ESMO-EHA2025 ; ONKO-PTCL2025]. Réponse confirmée par biopsie médullaire et si possible hépatique (III, A) [ESMO-EHA2025].
- Prévention : limiter l'association thiopurine + anti-TNF à 2 ans chez le jeune homme (recommandations citées) [CARVAO2019].

### 10.4 EATL (C86.2)
- Patient apte : 1 cycle CHOP/CHOEP puis 3 cycles IVE alternant avec méthotrexate à dose intermédiaire, puis autogreffe (III, B) ; survie à 5 ans 60 % (n = 26) [ESMO-EHA2025 ; ONKO-PTCL2025]. Patient fragile : CHOP-like ou BV-CHP [ESMO-EHA2025].
- RCD-II : exclure l'EATL par capsule et TEP (III, A) ; surveillance de l'intestin grêle tous les 6–12 mois (IV, B) [ESMO-EHA2025].

### 10.5 SPTCL (C86.3)
- SPTCL αβ sans SLH : pronostic excellent, la polychimiothérapie de première intention doit être remise en question [WILLEMZE2008]. Les patients HLH-SPTCL porteurs de TIM-3 muté bénéficient de l'**immunomodulation** [GAYDEN2018]. **Lacune** : schémas précis (corticoïdes, ciclosporine) non lus dans une recommandation européenne ; ESMO-EHA renvoie les lymphomes cutanés à un document séparé (ESMO 2018, texte intégral inaccessible, HTTP 403).

### 10.6 BPDCN (C86.4)
- **Tagraxofusp** (Elzonris®, protéine de fusion dirigée contre CD123) autorisé en Suisse en **première ligne chez l'adulte** ; 12 µg/kg en 15 min, J1–J5 d'un cycle de 21 jours ; 1er cycle hospitalier ; albumine ≥ 3,2 g/dl avant traitement ; RC/RCc 56,9 % chez 65 patients naïfs [ELZONRIS-FI].
- Allogreffe en première rémission, autogreffe si absence de donneur ; venetoclax et inhibiteurs BET en investigation [NGUYEN2023].

### 10.7 nTFHL-AI (C86.5)
- CHOP ou CHOEP (II, B) ; 3–4 cycles si forme limitée favorable (IV, B) ; ISRT 30–40 Gy (IV, B) ; autogreffe chez les répondeurs à haut risque (III, B) [ESMO-EHA2025].
- Rechute : azacitidine orale (III, B) ; romidepsine RG < 40 % ; ciclosporine et lénalidomide actifs [ESMO-EHA2025]. Évolution parfois indolente à prendre en compte [ZANDER2021].

### 10.8 CD30+ cutanés (C86.6)
- **LyP** : surveillance légitime ; aucun traitement ne modifie l'évolution ni ne prévient un second lymphome ; méthotrexate faible dose (5–30 mg/semaine) RC 34 %, rechute 63 % ; PUVA RC 26 %, rechute 84 % ; **polychimiothérapie à éviter** ; suivi **à vie** ; second lymphome (MF, ALCL, Hodgkin) chez **4–25 %** [KEMPF2011].
- **pcALCL** : excision ou radiothérapie des lésions solitaires/groupées (RC ≥ 95 %, rechute ≈ 40 %) ; multifocal : méthotrexate faible dose ; CHOP (RC 85 %, rechute 71 %) **n'est plus recommandé** pour une atteinte purement cutanée ; chimiothérapie systémique seulement si dissémination extracutanée ; survie à 5 ans 76–96 % [KEMPF2011].
- Brentuximab védotine autorisée en Suisse dans le lymphome T cutané CD30+ après traitement systémique [ADCETRIS-FI].

## 11. Situations particulières
- Maladie inflammatoire de l'intestin sous thiopurine ± anti-TNF : HSTL [CARVAO2019].
- Enfant/adolescent : SLH-SPTCL associé à l'âge < 18 ans et aux mutations HAVCR2 [MOONLA2023].
- Implant mammaire : BIA-ALCL (hors C86) [ONKO-PTCL2025].
- **Lacune** : grossesse non documentée.

## 12. Critères formels (pour `div.alert`)
- ENKTL : EBV+ (EBER) **et** CD56+ ou molécules cytotoxiques ; si les deux manquent → PTCL EBV+ [TSE2022].
- nTFH : ≥ 2 marqueurs TFH parmi CD10, BCL6, PD1, ICOS, CXCL13 [ONKO-PTCL2025].
- RCD-II : villosités atrophiques malgré régime sans gluten strict > 12 mois + LIE aberrants > 20 % [ESSCD2019].
- pcALCL : CD30 sur ≥ 75 % des cellules tumorales, sans LyP, MF ni atteinte extracutanée [KEMPF2011].
- BPDCN : CD123+, CD4+, CD56+, TCL1+, lignées négatives [NGUYEN2023].

## 13. Paramètres clés (pour `div.key`)
- Lymphomes T ≈ 10–15 % des lymphomes en Suisse [ZANDER2021].
- ENKTL : radiothérapie ≥ 50 Gy ; pas d'anthracycline ; asparaginase [ESMO-EHA2025 ; TSE2022].
- HSTL : ICE puis allogreffe ; 1/3534 sous thiopurine + anti-TNF (homme < 35 ans) [ESMO-EHA2025 ; CARVAO2019].
- SPTCL αβ : 5 ans 91 % sans SLH vs 46 % avec SLH [WILLEMZE2008].
- LyP : 5 ans 99 % ; second lymphome 4–25 % [WHO-EORTC2018 ; KEMPF2011].
- BV 1,8 mg/kg toutes les 3 semaines ; tagraxofusp 12 µg/kg J1–J5/21 j [ADCETRIS-FI ; ELZONRIS-FI].

## 14. Lacunes explicites
1. Aucune recommandation suisse spécifique (SSH, Swiss Medical Forum) sur les PTCL : seule source suisse = revue SZO 2021 (Zander, Renner).
2. Pas de chiffres suisses par sous-code C86.x.
3. Recommandation ESMO 2018 des lymphomes cutanés : texte intégral non accessible (HTTP 403) ; remplacée par WHO-EORTC 2018 et le consensus EORTC/ISCL/USCLC 2011.
4. Traitement précis du SPTCL (corticoïdes, ciclosporine), panniculite lupique, critères HLH-2004 : non lus.
5. Tableau clinique détaillé de l'EATL ; ICC 2022 non lue en texte intégral.
6. Statut de remboursement suisse 2026 de BV-CHP non vérifié (liste des spécialités non consultée).
7. Le consensus EORTC/ISCL/USCLC 2011 inclut un consortium américain (USCLC) : utilisé pour sa composante européenne (EORTC, auteur principal zurichois), non comme recommandation américaine.
