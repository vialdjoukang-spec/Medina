# G92 — Encéphalopathie toxique (N-05-Neurologie) — dossier de recherche

Cycle Betta 40, leçon 2 · agent C40-A3-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Méthode : WebSearch indisponible (quota épuisé) ; recherche par PubMed (métadonnées, résumés, textes intégraux PMC), WebFetch BfArM, `tools/swissmedic_fi.py` (AIPS via AmiKo). Texte intégral EBMT-JACIE-EHA 2021 (Annals of Oncology) et ESMO 2022 inaccessibles (403 / hors PMC) : seuls leurs résumés et leur citation par S2 sont utilisés.

## 0. Question clinique et logique de la leçon
G92 regroupe les atteintes cérébrales diffuses causées par un agent toxique exogène [S1]. Depuis la CIM-10-GM, la catégorie est scindée en G92.0 (encéphalopathie toxique sous immunothérapie, dont l'ICANS) et G92.9 (autres et sans précision) [S1]. Plan proposé : (1) socle commun « encéphalopathie toxique » (définition, mécanismes, imagerie, démarche) ; (2) ICANS après cellules CAR-T, sujet moderne et le mieux documenté ; (3) encéphalopathies médicamenteuses fréquentes en Suisse documentées par l'information professionnelle (céfépime, ifosfamide, valproate, métronidazole, méthotrexate) ; (4) critères formels et paramètres clés.

## 1. Définition et périmètre CIM-10-GM 2024 [S1]
- G92.- Encéphalopathie toxique. Note de codage : pour indiquer l'agent toxique, ajouter un code du chapitre XX (causes externes).
- G92.0 Encéphalopathie toxique sous immunothérapie ; inclusion : syndrome de neurotoxicité associé aux cellules effectrices immunitaires (ICANS).
- G92.9 Encéphalopathie toxique, autres et sans précision.
- Aucune exclusion listée sous G92 ; pas de cinquième position ; pas de G92.8 dans la version GM 2024 [S1].
- Repère de codage voisin (déjà lu pour G93) : G93.4 « Encéphalopathie SAI » exclut l'encéphalopathie alcoolique (G31.2) et toxique (G92.-) [S1 bis = S1 du dossier G93, même page BfArM].
- Libellés français OFS : G92 « Encéphalopathie toxique », G92.0 « Encéphalopathie toxique sous immunothérapie », G92.9 « Encéphalopathie toxique, autres et sans précision » (nosology/fragments/S08.json, OFS 2024).

## 2. Socle commun : encéphalopathie toxique (G92.9)
### 2.1 Définition et mécanismes
- Les encéphalopathies toxico-métaboliques sont des affections où une substance exogène ou endogène provoque une atteinte neuronale transitoire ou permanente ; elles constituent une cause importante d'encéphalopathie aiguë potentiellement réversible [S8].
- Signes et symptômes souvent peu spécifiques ; tests toxicologiques pas toujours disponibles ; l'imagerie oriente le diagnostic, la suite des examens et le pronostic [S8].
- Leucoencéphalopathies toxiques : causes exogènes très variées — irradiation crânienne, chimiothérapie, antiépileptiques, drogues, toxiques environnementaux ; aucun tableau clinique typique [S9].
- IRM : atteinte bilatérale et symétrique de la substance blanche, hypersignal T2/FLAIR, restriction de diffusion à la phase aiguë ; d'autres zones à haut métabolisme peuvent être touchées [S9].
- La plupart des anomalies sont réversibles, surtout si l'agent est reconnu et arrêté tôt [S9].
- Diagnostic différentiel radiologique et clinique : maladies démyélinisantes, leucodystrophies, encéphalopathie hépatique, maladie vasculaire, états hypoxo-ischémiques [S9].
- Message clé : garder un haut indice de suspicion devant tout déficit neurologique récent et rechercher une exposition neurotoxique [S9].
- Chez l'enfant, deux tableaux d'imagerie fréquents : syndrome d'encéphalopathie postérieure réversible (PRES) et leucoencéphalopathie toxique aiguë, liés surtout à la chimiothérapie et à l'immunosuppression ; autre tableau : lésions réversibles du splénium [S10].
- En réanimation (COVID-19 grave), l'encéphalopathie aiguë, présentation neurologique la plus fréquente, est associée à l'hypoxémie, aux désordres toxiques/métaboliques et à l'inflammation systémique ; bilan multimodal (LCS, IRM, EEG) ; en l'absence de lésion structurelle, un coma prolongé est généralement réversible, d'où prudence pronostique [S11].

### 2.2 Exemples médicamenteux documentés par l'information professionnelle suisse
**Céfépime** [S12] (FI Cefepim Leman, mise à jour septembre 2025)
- Risque d'encéphalopathie (troubles de conscience avec confusion, hallucinations, stupeur, délire, coma), myoclonies, convulsions y compris état de mal non convulsif, surtout en cas de surdosage et/ou d'insuffisance rénale, en particulier chez le sujet âgé.
- La plupart des cas : insuffisants rénaux ayant reçu des doses supérieures aux doses recommandées ; symptômes en général résolutifs après l'arrêt et/ou une hémodialyse ; quelques cas mortels.
- Adapter la posologie si clairance de la créatinine ≤ 50 mL/min ; une hémodialyse de 3 h élimine environ 68 % du céfépime présent.
- Méta-analyse (23 articles) : DFGe < 30 mL/min/1,73 m² = principal facteur de risque (OR 10,06 ; IC 95 % 5,05–20,03) ; autres : anomalies du SNC, âge, poids, albumine, diabète, HTA, BPCO/maladie pulmonaire chronique, posologie inadaptée ; perfusion continue associée à un OR plus bas ; seuils de suivi thérapeutique proposés : creux 20 mg/L (intermittent), concentration à l'équilibre 63 mg/L (continu) [S13].
- Série de cas (73 cas) : 52 % ≥ 65 ans ; survenue surtout J2–J5 (71 %) ; résolution surtout en 1–5 jours (85 %) ; dose rarement adaptée à la fonction rénale [S14] (revue de cas, niveau de preuve faible).
**Ifosfamide** [S15] (FI Holoxan, avril 2023)
- Peut provoquer encéphalopathie et autres effets neurotoxiques ; survenue dans les heures ou jours après l'administration ; résolution le plus souvent en 48–72 h après l'arrêt ; parfois persistance ou guérison incomplète ; cas mortels rapportés ; interrompre l'ifosfamide si toxicité du SNC.
- Symptômes : confusion, somnolence, coma, hallucinations, vision trouble, réaction psychotique, trouble extrapyramidal, incontinence urinaire, convulsions.
- Toxicité dose-dépendante. Facteurs de risque : hypoalbuminémie, atteinte rénale, mauvais état général, maladie pelvienne (tumeur du bas abdomen, maladie abdominale volumineuse), traitement néphrotoxique antérieur ou concomitant dont le cisplatine. Facteurs moins prouvés : dysfonction hépatique, bilirubine et hémoglobine basses, leucopénie, acidose, bicarbonates bas, troubles électrolytiques, hyponatrémie/SIADH, intoxication hydrique, faibles apports hydriques, métastases cérébrales, maladie ou irradiation cérébrale antérieure, sexe féminin, adiposité.
- Prudence ou arrêt des dépresseurs du SNC (antiémétiques, sédatifs, opioïdes, antihistaminiques, alcool) ; surveillance étroite des symptômes ; le bleu de méthylène peut être envisagé.
**Valproate** [S16] (FI Depakine, septembre 2025)
- Le valproate peut abaisser la carnitine tissulaire et plasmatique, perturber la bêta-oxydation et le cycle de l'urée et provoquer une hyperammoniémie pouvant aboutir à une encéphalopathie hyperammoniémique.
- Explorations métaboliques avant traitement si suspicion de déficit du cycle de l'urée (contre-indication).
- Hyperammoniémie isolée modérée sans symptôme : n'impose pas l'arrêt ; avec symptômes neurologiques : investigations complémentaires.
- Association topiramate ou acétazolamide : encéphalopathie et/ou hyperammoniémie rapportées ; surveiller.
- Effets occasionnels : coma, encéphalopathie, léthargie, syndrome parkinsonien réversible, ataxie ; rares : démence réversible avec atrophie cérébrale.
- Surdosage avec hyperammoniémie : carnitine IV possible ; hémodialyse/hémoperfusion en cas de surdosage massif.
- Maladies mitochondriales (mutations POLG, syndrome d'Alpers-Huttenlocher) : risque accru d'insuffisance hépatique fatale.
**Métronidazole** [S17] (FI MetronidazoleSINT i.v., février 2026)
- Très rares : encéphalopathie, céphalées, somnolence, vertiges, troubles visuels, ataxie, dysarthrie, convulsions.
- Arrêter le traitement si convulsions, myoclonies, neuropathie périphérique, ataxie, vertiges ou confusion ; prudence en cas de troubles sévères préexistants du SNC ou périphériques ; réduire la dose en insuffisance hépatique sévère.
**Méthotrexate** [S18] (revue 2025, résumé)
- Neurotoxicité du MTX de quelques heures à plusieurs années après administration, transitoire à sévère ; facteurs de risque : prédisposition génétique, interactions, insuffisance rénale, radiothérapie concomitante ; prévention et atténuation : hydratation, sauvetage par acide folinique (leucovorine), glucarpidase.

## 3. G92.0 — Encéphalopathie toxique sous immunothérapie : ICANS
### 3.1 Définition
- Définition consensuelle : affection caractérisée par un processus pathologique touchant le SNC après toute immunothérapie qui active ou engage des lymphocytes T endogènes ou perfusés et/ou d'autres cellules effectrices immunitaires ; signes possibles : aphasie, altération de la conscience, troubles cognitifs, faiblesse motrice, convulsions, œdème cérébral [S5] (définition reprise par la revue européenne S2).
- Ancien terme : CRES (CAR-T-related encephalopathy syndrome) ; le terme ICANS couvre aussi les anticorps bispécifiques [S5].
- Exclus de la définition (moins spécifiques, traitement symptomatique, ne déclenchent pas de corticoïdes) : céphalées, tremblement, myoclonies, astérixis, hallucinations ; faiblesse de déconditionnement ; hémorragie intracrânienne liée à la coagulopathie [S5].
- Caractère distinctif : patient éveillé, mutique, ne répondant ni verbalement ni physiquement [S5].

### 3.2 Épidémiologie et chronologie
- ICANS : 20–60 % des receveurs de CAR-T ; grade ≥ 3 : 3–30 % ; varie selon le produit [S2].
- Par produit (EMA, essais pivots) : axicabtagène ciloleucel 64 % (G≥3 28–32 %) ; brexucabtagène 69 % (G≥3 31 %) ; tisagenlecleucel 21–40 % (G≥3 13 %) ; lisocabtagène 27–30 % (G≥3 10 %) ; obécabtagène 22,8 % (G≥3 7,1 %) ; idécabtagène 18 % (G≥3 3 %) ; ciltacabtagène 23–26 % (G≥3 10 %) ; tabelecleucel (VST) : pas d'ICANS [S2]. Taux non comparables entre produits (essais hétérogènes) [S2].
- Délai moyen d'apparition ≈ 5 jours après la perfusion ; environ 10 % des cas surviennent > 3 semaines après le CRS ; ICANS concomitant au CRS, après sa résolution, ou tardif [S2]. Complications précoces en général J7–J30, ICANS tardif jusqu'à 6–8 semaines [S2].
- FI suisse YESCARTA : effets neurologiques chez 62 % (ZUMA-1/ZUMA-7), grade ≥ 3 chez 25 % ; 75 % dans les 7 premiers jours ; délai médian 6 jours (1–133) ; durée médiane 10 jours ; 56 % dans ZUMA-5 (grade ≥ 3 15 %, délai médian 7 jours, 1–177) ; manifestations : encéphalopathie 51 %, céphalées 33 %, tremblements 28 %, vertiges 22 %, délire 13 % ; état de mal épileptique post-commercialisation (0,3 %) ; œdème cérébral grave voire fatal (LMPGB 1,6 % dont 0,8 % fatal vs 0,7 % dont 0,2 % fatal) [S3].
- Liso-cel (essais n = 702 ; registre CIBMTR n = 877) : 88 % des événements neurologiques ≤ J15 ; ICANS réel 27 % (G≥3 10 %), 95 % ≤ J15, résolution médiane 5,5 jours [S20] (source registre américain, données descriptives, non une recommandation).

### 3.3 Mécanismes (normal → pathologique)
- Après lymphodéplétion, les CAR-T reconnaissent l'antigène tumoral, s'activent, prolifèrent et sécrètent IL-6, IFN-γ, IL-1, TNF-α ; l'activation macrophagique amplifie la cascade (CRS) [S2].
- L'inflammation active l'endothélium et augmente la perméabilité (VEGF) : rupture de la barrière hémato-encéphalique → ICANS [S2] ; CAR-T et cytokines élevées dans le LCS dans les formes sévères [S2].
- Pic des cytokines J7–J14, corrélé à l'expansion des CAR-T [S2] ; FI : pic IL-6, IL-8, IL-10, IL-15, TNF-α, IFN-γ, sIL2Rα dans les 14 premiers jours, retour à la base en 28 jours [S3].
- Rôle discuté : glutamate et acide quinolinique (agonistes NMDA) élevés dans le LCS ; cytokines pro-inflammatoires et cellules myéloïdes [S5].
- Tocilizumab prophylactique non recommandé en routine : le blocage du récepteur IL-6 élève l'IL-6 circulante, qui peut franchir la BHE, associé à un ICANS plus fréquent ou plus sévère [S2].
- Facteurs de risque de toxicité sévère : forte masse tumorale, lymphodéplétion fludarabine/cyclophosphamide, marqueurs inflammatoires élevés avant traitement, nombreuses lignes antérieures [S2] ; antécédents SNC (convulsions, ischémie) [S3] ; LMPGB avec masse médiastinale/syndrome cave supérieur pour l'œdème cérébral [S3].

### 3.4 Clinique
- Signes précoces : tremblement, dysgraphie, difficulté d'expression (dénomination), troubles de l'attention, apraxie, léthargie légère [S5] ; détérioration de l'écriture = signe d'alerte précoce [S2].
- Aphasie expressive : symptôme très spécifique (19/22 patients avec neurotoxicité sévère dans un essai) ; progression possible vers aphasie globale, patient éveillé mais mutique et akinétique [S5].
- Formes modérées : aphasie expressive et réceptive, agitation, léthargie, troubles de la mémoire immédiate ; sévères : obnubilation, stupeur, crises tonico-cloniques, état de mal, œdème cérébral, coma [S2].
- Crises souvent après l'aphasie globale ; œdème cérébral diffus rare, parfois fulminant et sans signes avant-coureurs [S5].
- Céphalée isolée : marqueur non utile [S5].
- Enfant : présentation atypique (irritabilité, comportement anormal, régression) ; ICE inadapté < 12 ans ; Cornell Assessment of Pediatric Delirium (CAPD, 8 items, 0–21 ans) ; CAPD ≥ 9 = délire probable [S2] ; ≥ 9 à considérer comme ICANS grade 3 [S5].

### 3.5 Examens et diagnostic
- Diagnostic clinique ; IRM et LCS rarement diagnostiques mais nécessaires pour exclure infection du SNC, atteinte leptoméningée maligne, LEMP, accident vasculaire [S2].
- EEG pour tout ICANS ≥ 2 (crises non convulsives) [S2].
- Infections opportunistes (HHV-6, LEMP) à évoquer devant tout événement neurologique [S3].
- ICANS vs infection du SNC : PCR LCS HSV, CMV, EBV, HHV-6, VZV en cas de doute ; un événement neurologique précoce isolé sans CRS impose un bilan infectieux élargi [S2].
- Score ICE (Immune effector Cell-associated Encephalopathy) : outil de dépistage sur 10 points (orientation, dénomination, exécution d'ordres, écriture, attention), dérivé du CARTOX-10 (éléments du MMSE) avec ajout d'un item de compréhension [S2, S5] ; dépistage toutes les 8–12 h en phase aiguë [S2].

### 3.6 Classification : grade ICANS (le paramètre le plus sévère fixe le grade) [S2, S5]
| Grade | ICE | Conscience | Crises | Motricité | HTIC / œdème |
|---|---|---|---|---|---|
| 1 | 7–9 | éveil spontané | — | — | — |
| 2 | 3–6 | éveil à la voix | — | — | — |
| 3 | 0–2 | éveil au seul stimulus tactile | crise clinique brève ou crise EEG résolutive sous traitement | — | œdème focal à l'imagerie |
| 4 | 0 (non évaluable) | stupeur/coma, stimulation vigoureuse | crise > 5 min ou crises répétées sans retour à l'état de base | déficit moteur profond (hémi-/paraparésie) | œdème diffus, posture de décérébration/décortication, paralysie VI, œdème papillaire, triade de Cushing |

### 3.7 Prise en charge (Europe ; Suisse via FI)
- Cadre suisse (FI YESCARTA) : centre qualifié avec accès immédiat aux soins intensifs ; ≥ 4 doses de tocilizumab disponibles avant perfusion ; surveillance quotidienne ≥ 7 jours (hospitalisation envisageable) ; rester à proximité du centre ≥ 2 semaines ; information que les effets peuvent survenir au-delà de 4 semaines ; corticoïdes préventifs déconseillés en routine ; pas de conduite ni de machines dangereuses ≥ 2 semaines ou jusqu'à disparition des effets neurologiques ; prise en charge selon recommandations nationales ou européennes/internationales [S3].
- Recommandations européennes EBMT-JACIE-EHA 2021 : couvrent tout le parcours (sélection, toxicités, suivi à long terme) [S4] (texte intégral non lu).
- Par grade [S2] :
  - Grade 1 : soins de support ; ICE deux fois par jour.
  - Grade 2 : dexaméthasone 10–20 mg IV toutes les 6 h ; ICE 3–4×/j ; envisager EEG et avis neurologique.
  - Grade 3 : soins intensifs + neurologue ; dexaméthasone 10–20 mg IV/6 h ou méthylprednisolone 1000 mg/j 3 jours puis décroissance rapide ; benzodiazépine IV (lorazépam) puis charge en lévétiracétam pour les crises ; IRM (ou CT) et EEG.
  - Grade 4 : méthylprednisolone 1000 mg/j 3 jours puis 250 mg/12 h 2 j, 125 mg/12 h 2 j, 60 mg/12 h 2 j ; état de mal : avis neurologique urgent ; HTIC : tête surélevée, hyperventilation, osmothérapie (mannitol / salé hypertonique) avec neurologie et réanimation.
- ICANS réfractaire aux corticoïdes (pas d'amélioration d'un grade 3/4 après 3 jours de fortes doses) : anakinra IV haute dose (jusqu'à 12 mg/kg/j, typiquement 800 mg/j), réponse globale ≈ 77 %, preuves observationnelles ; alternative : triple intrathécale (hydrocortisone 50 mg + méthotrexate 12 mg + cytarabine 50 mg) ; siltuximab, ruxolitinib, dasatinib : preuves insuffisantes [S2].
- Tocilizumab : traitement du CRS (pas de l'ICANS isolé) ; FI suisse Actemra (septembre 2026) : SRC 8 mg/kg (≥ 30 kg) ou 12 mg/kg (< 30 kg) IV sur 60 min, jusqu'à 3 doses supplémentaires, intervalle ≥ 8 h, ≤ 800 mg/perfusion [S6] ; corticoïdes indiqués si ICANS concomitant [S2].
- Données suisses : Berne (n = 80, rétrospectif) — anakinra prophylactique 100 mg s.c. J0–J6 : ICANS 35 % vs 25 % (p = 0,464), grade 3 20 % vs 18 % ; pas de réduction ; hospitalisation numériquement plus courte [S19]. Zurich (n = 26, ≥ 70 ans) — tocilizumab prophylactique 1 h avant perfusion : moins de complications composites (p = 0,039), petite série rétrospective [S21]. Ces données ne fondent pas une recommandation.

### 3.8 Suivi
- FI : surveiller immunoglobulines (aplasie B), prophylaxies infectieuses selon recommandations locales [S3] ; S2 : prophylaxie antivirale et anti-Pneumocystis ≥ 6 mois et jusqu'à CD4 > 200/µL.
- Résolution : 66 % des effets neurologiques atténués en 3 semaines (ZUMA-1/7) ; persistance chez 3,6 % au décès (non liée) [S3].
- Réadaptation : livre blanc 2026 (EMBMT, non européen strict) — suivi ambulatoire 12–18 mois proposé [S22] (faible poids).

## 4. Critères formels (proposition pour le dernier îlot)
- ICANS (G92.0) : définition consensuelle [S5] + grade ICE/conscience/crises/motricité/œdème [S2, S5] ; diagnostic d'exclusion clinique (infection SNC, LEMP, AVC, leptoméninges) [S2].
- Encéphalopathie toxique G92.9 : pas de critères formels publiés retrouvés ; faisceau = exposition à un neurotoxique + encéphalopathie aiguë/subaiguë + exclusion d'autres causes + amélioration à l'arrêt [S9, S12, S15] (synthèse, à formuler comme telle).

## 5. Paramètres clés
- ICE 10 points ; grade 1 = 7–9, grade 2 = 3–6, grade 3 = 0–2, grade 4 = 0/non évaluable [S2].
- Début ICANS ≈ J5 (médiane FI 6–7 j) ; 75 % dans les 7 jours [S2, S3].
- Surveillance ≥ 7 jours, proximité du centre ≥ 2 semaines, pas de conduite ≥ 2 semaines [S3].
- Dexaméthasone 10–20 mg IV/6 h (grades 2–3) ; méthylprednisolone 1 g/j × 3 j (grades 3–4) [S2].
- Tocilizumab 8 mg/kg (max 800 mg), ≤ 4 doses, ≥ 8 h d'intervalle [S6].
- Céfépime : risque majeur si DFGe < 30 (OR ≈ 10) ; adapter si ClCr ≤ 50 [S12, S13].
- Ifosfamide : résolution 48–72 h après arrêt ; bleu de méthylène envisageable [S15].

## 6. Lacunes explicites
- Aucune source suisse de recommandation (Swiss Medical Forum, SSN, Tox Info Suisse) lue sur l'encéphalopathie toxique ou l'ICANS : WebSearch épuisé.
- Texte intégral EBMT-JACIE-EHA 2021 [S4] et ESMO 2022 (toxicités des immunothérapies, dont encéphalite sous inhibiteurs de points de contrôle ; PMID 36270461) non lus → encéphalite/neurotoxicité sous inhibiteurs de checkpoint NON documentée ; ne pas rédiger cette partie.
- Barème détaillé des items du score ICE (points par item) non lu dans une source accessible (table absente du texte PMC) ; ne citer que les cinq domaines.
- Bispécifiques (téclistamab, etc.), lithium, intoxication au CO, plomb, solvants, encéphalopathie de Wernicke (hors G92), leucoencéphalopathie radique : non documentés ici.
- Épidémiologie suisse de G92 : aucune donnée.
- Bleu de méthylène dans l'encéphalopathie à l'ifosfamide : posologie non lue (FI Holoxan ne la donne pas).
- Grade ICANS : la source de grading (ASTCT 2019, S5) est un consensus américain ; reprise et appliquée par les sources européennes (S2 indique son adoption par EBMT et JACIE) ; à présenter comme outil de classement international, non comme recommandation de conduite.
