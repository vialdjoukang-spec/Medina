# C95 — Leucémie à cellules non précisées (H-08-Hématologie)

Dossier de recherche du cycle Betta 35, leçon 2 (agent C35-A3-HEM, Opus 5.5), consulté le 15.10.2026.
Chaque affirmation provient d'une source réellement lue ; la clé entre crochets renvoie à `sources.json`.
Statut : audit différé. Il s'agit d'une revue IA, distincte d'une validation médicale humaine.

## 0. Question clinique
C95 n'est pas une maladie mais une **catégorie de codage** : elle reçoit les leucémies dont la lignée cellulaire n'est pas attribuée ou ne peut pas être déterminée [BFARM-C95]. Son contenu clinique réel est double :
- la **leucémie aiguë de lignée ambiguë** (LALA, en anglais ALAL), c'est-à-dire la leucémie aiguë à phénotype mixte (LAPM, en anglais MPAL : biphénotypique ou bilinéale) et la leucémie aiguë indifférenciée (LAI, en anglais AUL), explicitement incluses en C95.0- [BFARM-C95 ; HAEM-ALAL2025] ;
- la leucémie « sans précision » (C95.9-) : diagnostic provisoire ou incomplet, que le bilan de référence doit précisément faire disparaître [BFARM-C95 ; ONKO-AML2025].
Leçon clinique : devant une leucémie aiguë, la lignée commande le traitement (protocole de type LLA ou LMA) ; une lignée ambiguë est une situation à haut risque qui relève d'un centre d'hématologie [HAEM-ALAL2025 ; ONKO-ALL2026].

## 1. Nosologie CIM-10-GM 2024 : sous-codes couverts
Intitulés français OFS [OFS-GM2024] et notes BfArM [BFARM-C95] :
| Code | Intitulé |
|---|---|
| C95.0- | Leucémie aiguë à cellules non précisées (inclut : leucémie aiguë biphénotypique, bilinéale, de lignée mixte ; leucémie à cellules souches de lignée incertaine ; exclut : exacerbation aiguë d'une leucémie chronique sans précision → C95.1-) |
| C95.1- | Leucémie chronique à cellules non précisées |
| C95.7- | Autres leucémies à cellules non précisées |
| C95.8! | Leucémie, réfractaire au traitement d'induction standard (code additionnel, sans 5e caractère) |
| C95.9- | Leucémie, sans précision |
- 5e caractère pour C90–C95 : **0** = sans mention de rémission complète (inclut « rémission partielle » et « sans indication de rémission ») ; **1** = en rémission complète [BFARM-C95 ; OFS-GM2024]. La page BfArM 2024 lue ne définit pas de 5e caractère « 2 » [BFARM-C95].
- Règle : C95.0–C95.7 et C95.9 ne s'emploient que si la lignée n'est pas attribuée ou n'est pas déterminable ; C95.8! signale en plus une leucémie réfractaire à l'induction standard [BFARM-C95].

## 2. Définitions
- **LALA** : leucémie aiguë rare, à haut risque, dont on ne peut pas attribuer une lignée unique ; elle regroupe LAPM et LAI [HAEM-ALAL2025].
- **LAPM** : blastes exprimant des marqueurs de plus d'une lignée ; **biphénotypique** (une seule population porte les marqueurs de deux lignées) ou **bilinéale** (deux populations distinctes, ≥ 20 % de blastes au total) [HAEM-ALAL2025].
- **LAI** : aucun marqueur définissant une lignée ; au plus un marqueur associé par lignée ; la plupart des cas expriment un marqueur myéloïde, CD34, HLA-DR et TdT [HAEM-ALAL2025 ; CD3NEG2025].
- Seuil commun OMS 5e édition (WHO-HAEM5) et ICC 2022 : **≥ 20 % de blastes** dans le sang ou la moelle [HAEM-ALAL2025].
- Rappel du seuil des leucémies aiguës : LMA ≥ 20 % de blastes (sauf anomalies génétiques définissantes) [ONKO-AML2025] ; dans la nomenclature allemande (GMALL), LLA ≥ 25 % de blastes médullaires, en dessous lymphome lymphoblastique [ONKO-ALL2026].

## 3. Classification (WHO-HAEM5 / ICC 2022)
Critères d'attribution de lignée [HAEM-ALAL2025] :
| Lignée | Critère |
|---|---|
| Myéloïde | MPO positive (> 50 % de l'intensité des neutrophiles matures, ou profil type progéniteurs CD34+ normaux) ; si MPO faible/absente : ≥ 2 des 5 marqueurs monocytaires (CD11c, CD14, CD64, lysozyme, estérase non spécifique) |
| T | CD3 cytoplasmique ou membranaire > 50 % de l'intensité des lymphocytes T matures, sur au moins une partie des blastes |
| B | CD19 > 50 % de l'intensité des progéniteurs B normaux + ≥ 1 de CD10, CD22, CD79a ; CD19 plus faible : ≥ 2 marqueurs supplémentaires |
- Sous-types : B/myéloïde (≈ deux tiers), puis T/myéloïde ; rares B/T, B/T/myéloïde, T/mégacaryoblastique [HAEM-ALAL2025]. Karasek 2025 : B/myéloïde 59 %, T/myéloïde 35 % [MPAL-REV2025].
- Sous-groupes génétiquement définis : **BCR::ABL1** (15–20 % des LAPM, sujets plus âgés, phénotype B/myéloïde), **KMT2A réarrangé** (≈ 10 %, surtout nourrissons et enfants), **ZNF384 réarrangé** (jusqu'à 50 % des LAPM B/myéloïdes pédiatriques, rare chez l'adulte), **activation de BCL11B** (10–15 % des LAPM, ≈ un tiers des T/myéloïdes) [HAEM-ALAL2025].
- Onkopedia LMA (tableau 4) liste : leucémie aiguë de lignée incertaine, LAI, LAPM avec t(9;22) BCR::ABL1, avec réarrangement KMT2A, B/myéloïde SAI, T/myéloïde SAI [ONKO-AML2025].
- **Diagnostic d'exclusion** : les entités LMA définies priment ; une leucémie au phénotype ambigu mais portant une cytogénétique ou des mutations liées à la myélodysplasie (ASXL1, BCOR, EZH2, SF3B1, SRSF2, STAG2, U2AF1, ZRSR2) se classe LMA-MR ; RUNX1 fait exception [HAEM-ALAL2025 ; MR-ALAL2025]. Fréquence de mutations MR : ≈ 32 % des LAPM et ≈ 59 % des LAI [MR-ALAL2025].
- Seuil bilinéal : une publication ICC suggère qu'une sous-population divergente > 5 % peut suffire [HAEM-ALAL2025].
- Bâtonnets d'Auer : quasi exclusifs des hémopathies myéloïdes ; cas exceptionnels en LALA à phénotype surtout lymphoïde [AUER2024].

## 4. Épidémiologie
- Suisse (2013–2017) : ≈ 1150 leucémies (C91–C95) par an, ≈ 700 hommes et 450 femmes, un peu moins de 3 % des cancers ; risque cumulé 1,4 % (H) et 0,9 % (F) ; ≈ 600 décès/an, ≈ 3,5 % des décès par cancer [OFS-CANCER2021, p. 116–119].
- Âge médian au diagnostic en Suisse : leucémie myéloïde 69 ans ; leucémie lymphoïde 68 ans (H) et 70 ans (F) [OFS-CANCER2021].
- LALA : ≈ 2–3 % des leucémies aiguës ; incidence SEER 0,35/1 000 000 personnes-années [HAEM-ALAL2025] ; LAPM 1–5 % des leucémies aiguës selon Karasek [MPAL-REV2025].
- LMA : ≈ 3,7/100 000/an, > 100/100 000 après 70 ans [ONKO-AML2025]. LLA : 1,1/100 000/an, pic < 5 ans (5,3/100 000), second pic > 80 ans [ONKO-ALL2026].
- Facteurs de risque des leucémies (OFS) : benzène, formaldéhyde, oxyde d'éthylène, 1,3-butadiène ; agents alkylants et inhibiteurs de topoisomérase II (étoposide) ; rayonnements ionisants ; tabac ; trisomie 21 [OFS-CANCER2021].

## 5. Mécanismes : du normal au pathologique
- Normal : les précurseurs médullaires produisent les leucocytes ; la leucémie naît quand des précurseurs immatures prolifèrent sans contrôle et passent dans le sang à un stade non fonctionnel ou en excès ; la distinction lymphoïde/myéloïde dépend du précurseur atteint [OFS-CANCER2021].
- La classification attribue une lignée par ressemblance des blastes aux progéniteurs normaux ; la LALA échappe à cette attribution (absence d'engagement ou engagement dans plus d'une lignée) [WEINBERG2024].
- Génétique : anomalies cytogénétiques jusqu'à 90 % des LAPM, surtout caryotypes complexes [MPAL-REV2025] ; fusions définissantes BCR::ABL1, KMT2A, ZNF384, activation BCL11B [HAEM-ALAL2025].
- **Changement de lignée (lineage switch)** : sous pression thérapeutique spécifique de lignée (CAR-T anti-CD19, blinatumomab), une LLA-B peut basculer en LMA (75,7 %) ou en LAPM/LAI (24,3 %) ; survient dans les 6 mois chez 81,4 % ; survie médiane après bascule 4,8 mois ; KMT2A réarrangé dans 64 % des bascules LLA-B → LMA [HAEM-ALAL2025].
- Conséquence physiopathologique commune à toute leucémie aiguë (insuffisance médullaire) : anémie (fatigue, pâleur), neutropénie (infections bactériennes, mycoses), thrombopénie (pétéchies, ecchymoses, épistaxis, ménorragies) [ONKO-AML2025].

## 6. Anamnèse et examen clinique
- Installation en quelques jours ; un tiers environ des LLA se présentent avec infection ou hémorragie [ONKO-ALL2026].
- Signes lymphoïdes : adénopathies ≈ 60 %, splénomégalie aussi fréquente, masse médiastinale 14 % (60 % des LLA-T), atteinte du SNC 7 % [ONKO-ALL2026].
- Signes myéloïdes : infiltrats cutanés, atteinte méningée, hyperplasie gingivale, hépatosplénomégalie, plus fréquents dans les formes myélomonocytaires/monoblastiques ; CIVD et hyperfibrinolyse [ONKO-AML2025].
- Hyperleucocytose fréquente (≈ 60 %) mais un compte normal ou bas n'exclut pas la leucémie [ONKO-AML2025 ; ONKO-ALL2026].
- LAPM : facteurs pronostiques défavorables = leucocytose élevée, atteinte extramédullaire [MPAL-REV2025].
- Lacune : aucune source lue ne décrit un tableau clinique propre à la LALA distinct de celui des LMA/LLA [HAEM-ALAL2025 donne peu de détails].

## 7. Diagnostic et différentiel
Bilan initial (référence Onkopedia, applicable aux leucémies aiguës) [ONKO-AML2025 ; ONKO-ALL2026] :
- formule sanguine complète et frottis ; ponction-aspiration médullaire obligatoire, biopsie si ponction « sèche » ;
- **immunophénotypage par cytométrie en flux** (pivot pour la LALA [FLOW-ALAL2025]) ; cytochimie (MPO) ;
- cytogénétique et génétique moléculaire : BCR::ABL1 (transcrit p190 ou p210), KMT2A, panel myéloïde (ASXL1, RUNX1, TP53…), fusions (PML::RARA, CBFB::MYH11, RUNX1::RUNX1T1…) ;
- coagulation, chimie, analyse d'urine, test de grossesse, sérologies VHB/VHC/VIH, typage HLA (et fratrie) si allogreffe envisageable, statut CMV, radiographie thoracique, ECG, échocardiographie ; ponction lombaire avec cytologie (et chimiothérapie intrathécale) dans les LLA ; conseil de fertilité.
- FISH FGFR1 recommandée devant une leucémie de lignée mixte ou changeante [FGFR1-2024].
Différentiel (à exclure avant de retenir C95.0) [HAEM-ALAL2025 ; ONKO-AML2025] :
- LMA avec anomalie génétique définissante, LMA-MR, LMA post-thérapeutique au phénotype mixte (pronostic plus sombre que la LAPM : survie médiane 10,3 vs 42,8 mois) ;
- LLA avec coexpression myéloïde (≈ 29 % des LLA de l'adulte, sans valeur pronostique) [ONKO-ALL2026] ; LLA-T précoce (ETP) [AUER2024] ;
- crise blastique de LMC (code C94.8!/C92.1-) ; néoplasie à cellules dendritiques plasmacytoïdes blastiques (CD4, CD56, CD123, TCL1) [ONKO-AML2025].

## 8. Urgences
- **Hyperleucocytose/leucostase** : risque au-delà de ≈ 100 000/µl ; hypoxie, infiltrats pulmonaires, hémorragies rétiniennes, signes neurologiques ; urgence hématologique ; hydroxyurée 4–5 g/j, cytarabine si insuffisant, leucaphérèse exceptionnelle et toujours associée à la chimiothérapie ; anthracyclines seulement après leucocytes < 30 G/l [ONKO-AML2025].
- Syndrome de lyse tumorale et CIVD décompensée : traitement intensif urgent [ONKO-AML2025] ; LLA : préphase dexaméthasone ± cyclophosphamide ≈ 5 jours pour prévenir la lyse [ONKO-ALL2026].
- Rasburicase (Fasturtec®) : traitement et prophylaxie de l'hyperuricémie aiguë des leucémies aiguës à forte masse tumorale ; 0,20 mg/kg/j jusqu'à 7 jours ; **contre-indiquée en cas de déficit en G6PD** (hémolyse par H₂O₂) ; risque de méthémoglobinémie et d'anaphylaxie ; sans effet direct sur hyperkaliémie, hyperphosphatémie, hypocalcémie [FI-FASTURTEC].
- Suspicion de LAP (PML::RARA) : ATRA immédiat — elle exclut par définition une LALA [ONKO-AML2025].

## 9. Prise en charge (centre d'hématologie ; aucune recommandation suisse spécifique trouvée)
- **Induction de type LLA** recommandée pour la plupart des LAPM [HAEM-ALAL2025] ; Onkopedia LLA 2026 : LAPM (WHO-HAEM5) et LAB (EGIL) sont traitées selon les protocoles LLA [ONKO-ALL2026].
  - Enfant, iBFM-AMBI2012 (233 cas, 5 continents, essentiellement européens) : SSE à 5 ans 80 ± 4 % (type LLA) vs 36 ± 7,2 % (type LMA) vs 50 ± 12 % (combiné) ; LMA-type préféré seulement pour une minorité CD19-négative sans autre caractère lymphoïde ; changement de protocole seulement si ≥ 5 % de blastes après induction [IBFM-AMBI2018].
  - Méta-analyse (1499 patients) : rémissions et survie supérieures avec induction de type LLA ; régimes hybrides associés à une survie inférieure (HR 2,11) [HAEM-ALAL2025].
- **LAPM Ph+** : ajouter un ITK ; pronostic proche de la LLA Ph+ (médiane de survie 53,6 mois, survie à 5 ans 49 % dans une cohorte réelle) [HAEM-ALAL2025].
  - Imatinib (Glivec®) : indication suisse = LLA Ph+ adulte et pédiatrique **en association avec une chimiothérapie standard**, 600 mg/j chez l'adulte, 340 mg/m²/j chez l'enfant ; hépatotoxicité de grade 3/4, parfois fatale, en association ; surveillance FEVG chez cardiaques [FI-GLIVEC]. La LAPM Ph+ n'est pas une indication nommée : usage hors étiquette à signaler.
  - Ponatinib (Iclusig®) : LLA Ph+ avec mutation T315I ou si les autres ITK ne conviennent pas ; 45 mg/j ; risque d'événements artériels occlusifs dose-dépendant [FI-ICLUSIG].
- **LAI** : approche optimale inconnue, traitement individualisé [HAEM-ALAL2025].
- **Allogreffe en RC1** chez l'adulte éligible :
  - EBMT ALWP 2017 (519 adultes, 2000–2014, âge médian 38 ans) : à 3 ans rechute 31,4 %, mortalité non liée à la rechute 22,1 %, survie sans leucémie 46,5 %, survie globale 56,3 % ; conditionnement myéloablatif avec ICT associé à une meilleure SSL ; effet greffon contre leucémie probable [EBMT-2017].
  - EBMT ALWP 2026 (195 adultes, 2014–2023, centre de Zurich participant) : à 2 ans survie globale 70,7 %, SSL 56,4 %, rechute 29,8 %, MNR 13,8 % ; conditionnement myéloablatif meilleur (OS HR 0,5) ; cellules souches périphériques : moins de rechutes [EBMT-2026].
  - Enfant : pas de bénéfice global démontré, à réserver aux mauvais répondeurs [IBFM-AMBI2018].
- Thérapies ciblées émergentes (données de cas) : vénétoclax (+ FLAG/FLAG-Ida ou + azacitidine), blinatumomab, inhibiteurs de ménine, CAR-T anti-CD19 ; risque de changement de lignée [HAEM-ALAL2025].

## 10. Suivi et réponse
- Rémission complète (critères Onkopedia/ELN) : blastes médullaires < 5 %, pas d'atteinte extramédullaire, neutrophiles ≥ 1000/µl, plaquettes ≥ 100 000/µl, pas de blastes circulants ; RCh, RCi, MLFS définies [ONKO-AML2025].
- **Réfractaire** (→ C95.8!) : absence de RC/RCh/RCi au jalon prévu (par ex. après 2 cycles d'induction intensive) ; non-réponse à une ou deux inductions = réfractaire primaire [ONKO-AML2025 ; BFARM-C95].
- MRD : MRD négative associée à une meilleure survie ; pédiatrie (112 cas) MRD positive en fin d'induction → SSE HR 6,00, survie HR 9,57 ; ne pas fonder seule une décision majeure hors essai [HAEM-ALAL2025]. Méthodes ≥ 10⁻⁴, contrôles tous les 3 mois en LLA [ONKO-ALL2026].
- Rôle du médecin de premier recours : complications entre les cycles (fièvre en neutropénie, saignement) — lacune : source suisse en texte intégral non accessible (article Ars Medici 2013 introuvable, 404).

## 11. Pronostic
- LALA à haut risque ; SEER : risque de décès +59 % vs LLA et +26 % vs LMA ; cohorte réelle (4756 adultes, âge médian 68 ans) : survie médiane 4,2 mois, mortalité à 30 jours 33 % ; LAI : survie médiane 1,4 mois [HAEM-ALAL2025] (données nord-américaines, descriptives seulement).
- Pronostic meilleur chez l'enfant que chez l'adulte [MPAL-REV2025] ; en Suisse, le pronostic des leucémies est très bon chez l'enfant et moins favorable chez l'adulte et dans les formes aiguës [OFS-CANCER2021].

## 12. Situations particulières
- Nourrisson : LAPM KMT2A réarrangée [HAEM-ALAL2025].
- Après immunothérapie anti-CD19 : penser au changement de lignée (≈ 8 % des LLA-B après CAR-T) [HAEM-ALAL2025].
- Sujet âgé/fragile : vénétoclax + azacitidine ou cytarabine faible dose (cas rapportés) [HAEM-ALAL2025].
- Patient sous hydroxyurée (Litalir®) : indication suisse = LMC et autres néoplasies myéloprolifératives ; contre-indiquée en grossesse/allaitement ; surveillance hématologique hebdomadaire au début ; pneumopathie interstitielle possible [FI-LITALIR]. Son emploi cytoréducteur en leucostase de LMA est une recommandation Onkopedia, non une indication nommée de l'information professionnelle.

## 13. Critères formels (proposition pour `div.alert`)
1. Leucémie aiguë : ≥ 20 % de blastes (sang ou moelle) [HAEM-ALAL2025].
2. Exclusion préalable d'une LMA définie génétiquement, d'une LMA-MR, d'une LMA post-thérapeutique, d'une crise blastique de LMC [HAEM-ALAL2025].
3. LAPM : critères de ≥ 2 lignées remplis (tableau §3) ; LAI : aucun critère de lignée, ≤ 1 marqueur par lignée [HAEM-ALAL2025].
4. Codage : C95.0- si lignée ambiguë ; C95.9- si leucémie non encore caractérisée ; 5e caractère selon rémission complète ; C95.8! si réfractaire à l'induction standard [BFARM-C95 ; OFS-GM2024].

## 14. Paramètres clés (proposition pour `div.key`)
- Seuil blastique 20 % ; MPO > 50 % ; CD19 > 50 % ; cCD3 > 50 % des intensités de référence.
- Leucostase > 100 000/µl ; anthracycline seulement < 30 G/l ; hydroxyurée 4–5 g/j.
- RC : blastes < 5 %, PNN ≥ 1000/µl, plaquettes ≥ 100 000/µl.
- BCR::ABL1 15–20 % des LAPM ; imatinib 600 mg/j (LLA Ph+ adulte).
- EBMT 2017 : survie globale 56,3 % à 3 ans après allogreffe en RC1.
- Suisse : ≈ 1150 leucémies/an, ≈ 600 décès/an.

## 15. Lacunes explicites
- Aucune recommandation suisse (SSH, SAKK, Swiss Medical Forum) spécifique de la LALA trouvée ; Ars Medici 2013 (Rosenfluh) en 404 ; Passweg et al., RMS 2008, seulement référencé sans texte intégral.
- Aucune recommandation ESMO/EHA dédiée à la LALA ; ELN 2022 non relu ici (voir dossier C93/C94).
- C95.1- et C95.7- : aucune entité clinique décrite par les sources ; ce sont des codes de documentation incomplète.
- Données de survie de grande taille (SEER, cohortes réelles) nord-américaines : descriptives, pas de fondement de conduite.
- Pas de données suisses d'incidence spécifiques à C95.
- Pharmacologie : aucun médicament n'a d'indication suisse nommée « LAPM » ; vénétoclax, blinatumomab et inhibiteurs de ménine en LALA = hors étiquette (FI non relues pour ce dossier).
