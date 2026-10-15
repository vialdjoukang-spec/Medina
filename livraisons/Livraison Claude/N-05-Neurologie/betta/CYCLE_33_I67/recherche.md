# I67 — Autres maladies cérébrovasculaires (N-05-Neurologie)

Dossier de recherche, cycle Betta 33, leçon 1, agent C33-A1-NEUR (Opus 5.5), 15.10.2026.
Chaque fait est suivi de sa source (S1–S24, voir `sources.json`). Rien n'est écrit de mémoire. Plusieurs sources n'ont été lues qu'en **résumé** ou **partiellement** (pages tronquées, voir `sources.json`, champ `limites`) : le rédacteur ne doit pas en extraire davantage que ce qui figure ici. Les lacunes sont au § 17.

---

## 0. Question clinique et angle pédagogique

I67 est une **catégorie hétérogène** : elle regroupe des maladies cérébrovasculaires qui ne sont ni une hémorragie (I60–I62), ni un infarctus (I63), ni une occlusion/sténose sans infarctus (I65–I66) [S1]. Elle juxtapose des affections **artérielles** (dissection, anévrisme, athérosclérose, moyamoya, artérite, vasospasme), **veineuses** (thrombose veineuse cérébrale), **microvasculaires** (leucoencéphalopathie vasculaire) et **hémodynamiques** (encéphalopathie hypertensive) [S1].

Proposition de fil conducteur (choix pédagogique, non une donnée) : une seule question unificatrice — **« quelle structure vasculaire est atteinte, et le cerveau souffre-t-il d'ischémie, d'hémorragie, d'œdème ou d'hypertension intracrânienne ? »** — puis une monographie courte par sous-code, en donnant le plus de poids aux entités fréquentes ou urgentes à l'examen : **thrombose veineuse cérébrale (I67.6)**, **anévrisme non rompu (I67.10)**, **encéphalopathie hypertensive / PRES (I67.4)**, **vasospasme après HSA (I67.80)**, **dissection intracrânienne (I67.0)**, **maladie des petites artères (I67.3)**, puis moyamoya (I67.5) et angéite primitive du SNC (I67.7).

Céphalée en coup de tonnerre : le diagnostic différentiel vasculaire couvre HSA anévrismale, SVCR (RCVS), dissection, TVC [S19][S2] (voir § 8).

## 1. Définition et classification (CIM-10-GM 2024)

Règles de codage lues [S1] :
- **I67** : les séquelles de ces affections sont codées **I69.8** (exclusion).
- **I67.0** Dissection d'artères cérébrales : si une hémorragie cérébrale est documentée, coder d'abord **I60–I62**.
- **I67.1-** Anévrisme cérébral et fistule artério-veineuse cérébrale : même consigne (I60–I62 d'abord si hémorragie).
  - **I67.10** anévrisme cérébral **acquis** ; exclusion : anévrisme congénital → **Q28.-**.
  - **I67.11** fistule artério-veineuse cérébrale **acquise** ; exclusion : congénitale → **Q28.-**.
- **I67.2** Athérosclérose cérébrale ; inclusion : athéromatose des artères cérébrales.
- **I67.3** Leucoencéphalopathie vasculaire progressive ; inclusion : **maladie de Binswanger** ; exclusion : démence vasculaire sous-corticale → **F01.2**.
- **I67.4** Encéphalopathie hypertensive.
- **I67.5** Maladie de moyamoya.
- **I67.6** Thrombose non pyogène du système veineux intracrânien ; inclusion : thrombose non pyogène des veines cérébrales ou des sinus veineux intracrâniens ; exclusion : comme cause d'un infarctus cérébral → **I63.6**.
- **I67.7** Artérite cérébrale, non classée ailleurs.
- **I67.8-** Autres maladies cérébrovasculaires précisées : **I67.80!** vasospasme au cours d'hémorragie sous-arachnoïdienne (code marqué « ! », code secondaire) ; **I67.88** autres (inclusion : insuffisance cérébrovasculaire aiguë SAI ; ischémie cérébrale chronique).
- **I67.9** Maladie cérébrovasculaire, sans précision.
- **I69** (séquelles) s'applique aux séquelles de I60–I67.1 et I67.4–I67.9 ; « séquelle » = affection décrite comme telle ou persistant **≥ 1 an** après le début [S1].

Titres français (OFS) : registre MEDINA `nosology/fragments/S08.json` (I67, I67.0, I67.1, I67.10, I67.11, I67.2, I67.3, I67.4, I67.5, I67.6, I67.7, I67.8, I67.80, I67.88, I67.9) [S1].

Classification de la TVC : **septique** versus **aseptique** ; dans la forme septique, le traitement du foyer infectieux et l'antibiothérapie priment ; le reste de la prise en charge ne diffère pas [S2]. (La forme septique/pyogène sort de I67.6, qui ne vise que la thrombose **non pyogène** [S1].)

## 2. Épidémiologie (par entité)

| Entité | Donnée | Source |
|---|---|---|
| TVC | ~75 % de femmes | [S3] |
| TVC | âge médian 41 ans (IQR 28–51), 63 % de femmes dans la cohorte DOAC-CVT (619 patients) | [S5] |
| Anévrisme non rompu | jusqu'à **3 %** des adultes ; prévalence 1,6 × plus élevée chez la femme ; similaire Europe/Amérique du Nord/Japon | [S7] |
| Anévrisme non rompu | rupture 1,04 %/personne-année chez la femme vs 0,74 % chez l'homme (9 cohortes, 9940 patients) ; HR ajusté femme/homme 1,39 | [S8] |
| HSA anévrismale | létalité ≈ **40 %** (≈ 40 % décèdent dans les 3 mois) | [S9] |
| Dissection extracrânienne | incidence 2,6–3,0/100 000/an ; âge moyen 44 ans | [S6] |
| Dissection intracrânienne | ≈ 11 % des dissections en Europe (27 % Amérique latine, 67–78 % Asie de l'Est) ; âge moyen 50 ans | [S6] |
| Moyamoya | Japon ≤ 0,54/100 000 ; pays occidentaux 0,047–0,086/100 000 (≈ 10 × moins) | [S17] |
| Angéite primitive du SNC | 2,4/1 000 000/an ; sex-ratio 1:1 ; âge médian 50 ans ; délai moyen diagnostic 170 jours | [S18] |
| SVCR (RCVS) | incidence standardisée ≈ 3/million/an | [S21] |
| SVCR | âge moyen 39,9 ans, 81,2 % de femmes (191 cas publiés) | [S22] |
| Maladie des petites artères | cause d'environ un quart des AVC ischémiques (lacunaires) | [S12][S13] |
| Encéphalopathie hypertensive | 10–15 % des patients avec hypertension maligne | [S16] |

## 3. Rappel du normal → mécanismes pathologiques

### 3.1 Drainage veineux et TVC (I67.6)
- Définition DACH : thrombose des conduits veineux cérébraux avec **trouble de l'écoulement veineux** [S2].
- Conséquence : stase → œdème de stase et/ou hémorragie (« Stauungsödem und/oder Hämorrhagie ») ; l'œdème cérébral est visible chez jusqu'à **50 %** des patients [S2][S3].
- La meilleure « thérapie de l'hypertension intracrânienne » est une anticoagulation suffisante, car elle améliore l'écoulement veineux et réduit la pression intracrânienne ; éviter la restriction volémique [S2].
- Facteurs de risque (fréquence chez les patients TVC) [S3] : contraception hormonale combinée **40–50 %** des femmes avec TVC (risque × 7,6 ; IC 95 % 3,82–15,09) ; thrombophilie 34–40 % ; grossesse (surtout 3e trimestre) et post-partum 10–20 % ; infection locale ≈ 10 % ; mutation JAK2 V617F 6–7 % ; néoplasie myéloproliférative ≈ 4 % ; traitement hormonal substitutif 3–4 % ; néoplasie cérébrale ≈ 2 % ; idiopathique 10–20 % ; **VITT** (thrombose avec thrombopénie dans les premières semaines après vaccin SARS-CoV-2 à vecteur viral) [S3][S2]. Collagénoses (lupus, Sjögren) listées parmi les étiologies [S2].

### 3.2 Autorégulation et encéphalopathie hypertensive (I67.4)
- Élévation brutale des résistances et natriurèse de pression → activation du système rénine-angiotensine → hausse supplémentaire de la PA et lésion microcirculatoire (cercle vicieux) [S16].
- Lorsque la PA est très élevée et que l'**autorégulation cérébrale** ne peut plus empêcher la hausse de pression, un **œdème cérébral** se constitue ; prédominance **postérieure** car l'innervation sympathique y est moins dense (amortissement moindre des oscillations tensionnelles) [S16].
- Histologie : œdème, micro-hémorragies, infarctus [S16].
- La **vitesse** d'élévation de la PA compte davantage que la valeur absolue ; il n'existe pas de seuil tensionnel spécifique [S16].
- PRES : physiopathologie incomplètement comprise ; hypothèses : poussée tensionnelle avec faillite de l'autorégulation (hyperperfusion), vasoconstriction/hypoperfusion, dysfonction endothéliale (facteur clé), activation immunitaire, rupture de la barrière hémato-encéphalique [S19][S20].

### 3.3 Petites artères (I67.3)
- Marqueurs IRM couverts par l'ESO : hyperintensités de la substance blanche et lacunes ; les lésions s'étendent habituellement avec le temps, mais peuvent régresser [S12].
- Débit sanguin cérébral réduit et autorégulation altérée démontrés ; le mécanisme principal ne serait pas athérothrombo-embolique ; l'angiopathie amyloïde contribue chez certains sujets âgés [S12].
- STRIVE-1 puis **STRIVE-2 (2023)** standardisent les marqueurs IRM de la maladie des petites artères (recherche) [S14].

### 3.4 Moyamoya (I67.5)
- Sténo-occlusion **bilatérale progressive** de la carotide interne supraclinoïdienne et de ses branches principales, avec réseau collatéral fragile dans les régions profondes [S17].
- **Maladie** (idiopathique) versus **syndrome** de moyamoya (associé : trisomie 21, neurofibromatose de type 1, drépanocytose, radiothérapie cervico-céphalique) [S17].
- Variant **RNF213 p.R4810K** : effet fondateur est-asiatique (95,1 % des cas familiaux, 79,2 % des cas sporadiques japonais), absent chez les patients occidentaux [S17].

### 3.5 Dissection (I67.0)
- Patrons : sténose segmentaire, occlusion, anévrisme disséquant, souvent combinés [S6].

### 3.6 Vasospasme et ischémie cérébrale retardée (I67.80)
- Le lien causal entre spasme macrovasculaire et ischémie cérébrale retardée est « de plus en plus remis en question » [S9].
- La nimodipine dilate les vaisseaux cérébraux et augmente la perfusion, préférentiellement des régions mal perfusées [S10].

## 4. Causes et facteurs de risque (synthèse)
- TVC : voir § 3.1 [S3][S2].
- Anévrisme : tabac et hypertension (formation, croissance, rupture) ; antécédent familial d'HSA ; ≥ 2 apparentés au 1er degré avec HSA ; polykystose rénale [S7].
- Facteurs de rupture : âge ≥ 70 ans, HTA, HSA antérieure, taille, localisation, région géographique, morphologie irrégulière (HR 1,63) ; la **croissance** (≥ 1 mm) est un facteur fort (rupture 2,9 % à 6 mois, 4,3 % à 1 an, 6,0 % à 2 ans) [S7]. HTA non contrôlée : HR 16,7 pour la rupture [S7].
- Dissection extracrânienne : HTA, migraine ; déclencheurs : traumatisme cervical mineur, infection récente ; facteurs de la dissection intracrânienne moins connus [S6].
- PRES : insuffisance rénale (IRC terminale), fluctuations tensionnelles, cytotoxiques/anti-angiogéniques, maladies auto-immunes, éclampsie/pré-éclampsie, transplantation, sepsis [S19][S20][S16].
- SVCR : substances vasoactives (41,4 %), grossesse/post-partum (20,9 %), rapport sexuel (10,5 %) [S22] ; aussi produits sanguins, traumatisme crânien, procédures neurochirurgicales [S19].
- Hypertension maligne : cause secondaire chez 20–40 % des patients aux urgences (surtout néphropathie parenchymateuse, sténose de l'artère rénale) [S16].

## 5. Anamnèse et clinique (par entité)

### TVC
- Crises épileptiques chez **40–50 %** ; un tiers fait une crise précoce (≤ 7 jours) ; risque accru si thrombose superficielle, déficit focal, sang sulcal/sous-arachnoïdien, lésion parenchymateuse, infarctus hémorragique [S2].
- Crises tardives (> 7 jours) ≈ 11 %, médiane 5 mois ; récidive après une crise tardive 70 % [S2].
- Signes d'hypertension intracrânienne (céphalée, troubles visuels) peuvent être le **seul indice** d'une TVC chronique : exclure un trouble de l'écoulement veineux chez tout « pseudotumor cerebri » [S2].
- Fréquence globale de la céphalée et des déficits focaux : non trouvée dans les sources lues (lacune § 17).

### Encéphalopathie hypertensive [S16]
- Définition ESC : HTA sévère + ≥ 1 de : **crises**, **léthargie**, **cécité corticale**, **coma**, sans autre explication.
- Somnolence, léthargie, crises tonico-cloniques et cécité corticale peuvent précéder la perte de connaissance.
- Un **déficit focal** est rare et doit faire suspecter une hémorragie ou un infarctus.
- Rétinopathie avancée absente chez jusqu'à un tiers.
- Mesurer la PA aux deux bras et à un membre inférieur ; répéter les mesures.

### PRES [S19][S20]
- Céphalée, troubles visuels/amputation du champ, confusion, crises, troubles de la conscience ; formes frustes possibles (un seul symptôme).

### SVCR [S19][S22]
- Céphalée en coup de tonnerre (céphalée sévère maximale en < 1 min), souvent récidivante ; ≈ 25 % de complications (HSA corticale, crises, ischémie) ; déficits focaux si lésion.

### Dissection [S6]
- Extracrânienne : céphalée, cervicalgie, syndrome de Horner, paralysies de nerfs crâniens ; ischémie chez 2/3 à 3/4, souvent des heures à jours plus tard.
- **Intracrânienne** : HSA (≈ 50–60 %) ou ischémie (30–78 %) ; céphalée prodromique ≈ 80 % ; compression du tronc/nerfs crâniens possible.

### Moyamoya [S17]
- Adulte : AIT, AVC ischémique et hémorragique, HSA ; hémorragie chez ≈ 25–60 % des adultes (moins chez les Occidentaux).
- Enfant : surtout ischémique ; hémorragie ≈ 3 % ; progression rapide plus fréquente.
- Les deux : déficits cognitifs, épisodes pseudo-migraineux, troubles psychiatriques et du mouvement.

### Angéite primitive du SNC [S18]
- Céphalée, psychose, AVC (souvent multiples, plusieurs territoires) ; présentation variable et non spécifique.

### Maladie des petites artères « couverte » [S12]
- Découverte fortuite sans AVC/AIT, trouble cognitif, de la marche ou de l'humeur ; augmente le risque d'AVC, de démence et de décès.

## 6. Examen clinique
- Encéphalopathie hypertensive : **fond d'œil** si suspicion d'hypertension maligne (hémorragies en flammèches bilatérales, nodules cotonneux, œdème papillaire) [S16].
- TVC : œdème papillaire implicite dans la question « hypertension intracrânienne / troubles visuels » [S2] (fréquence non lue).

## 7. Examens complémentaires

### TVC [S2][S3][S4]
- **CT et IRM, chacune avec angiographie veineuse, équivalentes** pour les thromboses sinusiennes ; **IRM supérieure** pour les thromboses de veines corticales ; IRM préférée chez le sujet jeune et pendant la grossesse (consensus 93,3 %).
- Scanner natif : détecte les petites hémorragies de stase mais **n'exclut pas** une TVC ; signes indirects (empty triangle, cord sign) devenus secondaires face à l'angio-CT (coupes 1–1,5 mm, phase veineuse).
- IRM native n'exclut pas : combiner IRM + angio-IRM ; détection directe du thrombus en T1, T2*, SWI ; piège : hypersignal du thrombus riche en méthémoglobine en TOF à ne pas prendre pour du flux.
- ASD seulement si discordance.
- **D-dimères** : non recommandés en routine (consensus 100 %) ; seule exception : faible probabilité (céphalée isolée, examen neurologique normal, symptômes < 30 jours), où des D-dimères normaux excluent la TVC avec une sécurité > 95 % ; faux négatifs si thrombus d'une veine corticale isolée ou symptômes > 30 jours.
- **Thrombophilie** : pas de dépistage systématique ; l'envisager si sujet jeune, TVC spontanée, récidive, antécédents familiaux de MTEV, et si le résultat modifie le traitement. ESO : pas de dépistage systématique de thrombophilie ni de cancer [S4].

### Encéphalopathie hypertensive / urgence hypertensive [S16]
| Catégorie | Examens |
|---|---|
| Laboratoire de routine | hémoglobine, plaquettes ; créatinine, Na, K, LDH, haptoglobine ; protéinurie quantitative ; sédiment urinaire |
| Systématique | ECG ; fond d'œil |
| Selon indication | troponine, CK ; frottis (schizocytes) ; radiographie thoracique ; échocardiographie ; **CT ou IRM cérébrale** ; angio-CT thoraco-abdominal ; échographie rénale |
- IRM : hypersignal T2/FLAIR confirmant l'encéphalopathie ; CT pour exclure une hémorragie.
- Microangiopathie thrombotique : hémolyse Coombs négative + thrombopénie, ADAMTS13 normale ou peu abaissée (très basse dans le PTT) ; s'améliore en 24–48 h avec la baisse tensionnelle.

### PRES [S19][S20]
- Œdème vasogénique sous-cortical bilatéral, pariéto-occipital dans > 90 % ; autres patrons : holohémisphérique de jonction, sillon frontal supérieur ; hémorragie ≈ 15 % ; restriction de diffusion, prise de contraste et vasoconstriction compatibles avec le diagnostic ; LCR normal ou quasi normal ; résolution en jours à semaines.

### SVCR [S19][S22]
- Sténoses segmentaires multifocales (84 %), aspect en « collier de perles » (82,4 %) ; lésions ischémiques 47,6 %, hémorragie (surtout HSA de convexité) 35,1 % ; artériographie = référence, angio-IRM/CT utiles ; vasoconstriction réversible en ≈ 3 mois ; œdème de type PRES chez 17–38 %.

### Dissection intracrânienne [S6]
- Diagnostic certain si ≥ 1 : sténose/occlusion évoluant vers un anévrisme fusiforme ou irrégulier en site non bifurcatif ; hématome intramural, flap intimal ou double lumière ; confirmation anatomopathologique.

### Anévrisme non rompu [S7]
- Suivi des anévrismes traités : angio-IRM après coiling, angio-CT après clipping, ASD si non concluant. Score ELAPSS pour planifier le suivi de croissance.

### Vasospasme / ischémie retardée après HSA [S9]
- Doppler transcrânien : sensibilité 66,7 %, spécificité 89,5 % vs ASD ; « n'exclut pas de façon fiable » un vasospasme.
- Perfusion CT : allongement du MTT prédit l'ischémie retardée avant l'infarctus ; CT/perfusion-CT utiles en cas d'aggravation ou d'examen clinique impossible ; monitorage invasif, EEG et monitorage complexe non recommandés en routine.

### Moyamoya [S17]
- Critères angiographiques : sténose/occlusion **bilatérale** de la carotide interne terminale et/ou de l'ACA/ACM proximales + réseau collatéral ; atteinte de l'ACP variable (35 % dans une cohorte pédiatrique européenne).
- IRM/angio-IRM de plus en plus utilisées ; **ASD** pour confirmer et évaluer les collatérales.
- **Évaluation hémodynamique** chez tous (y c. asymptomatiques) : Doppler transcrânien, perfusion CT/IRM (± acétazolamide), SPECT, PET H2(15O) (PET la plus utile car quantitative) ; réserve cérébrovasculaire altérée + origine est-asiatique + AIT antérieur : risque annuel d'AVC de 0,5 % à 20 %.
- Dépistage systématique de RNF213 p.R4810K non suggéré (consensus 8/10).

### Angéite primitive du SNC [S18]
- Critères de **Calabrese et Mallek (1988)** : déficit neurologique acquis inexpliqué ; aspect angiographique ou histologique classique d'angéite ; absence de vascularite systémique ou d'affection mimant.
- **Birnbaum et Hellmann (2009)** : *certaine* = histologie (biopsie/autopsie) ; *probable* = angiographie de haute probabilité + IRM anormale + LCR compatible (seulement forme des gros/moyens vaisseaux).
- Angiographie de haute probabilité : rétrécissements et dilatations segmentaires alternés, occlusions multiples, pas d'athérosclérose proximale.
- **LCR** : anormal ≈ 77,8 % (pléiocytose ≈ 46 %, hyperprotéinorachie ≈ 70 %) ; sensibilité 77,7 %, spécificité 68,3 % ; un LCR normal n'exclut pas.
- IRM : aucun patron spécifique (ex. lésions ischémiques multiples 18,6 %, prise de contraste parenchymateuse 20,4 %, ICH/HSA 13,6 %, pseudotumorale 4,1 %).
- **ASD plutôt que angio-IRM** (recommandation forte contre l'angio-IRM en remplacement de l'ASD ; évidence très faible) ; ASD à envisager si angio-IRM normale (faible).
- Biopsie : envisager si suspicion de forme des petits vaisseaux avec angiographie normale ; biopsie ciblée d'une lésion rehaussée.

## 8. Diagnostic différentiel
- **Céphalée en coup de tonnerre** : le SVCR en est « la cause la plus importante » selon [S19] ; différentiel lu : HSA, dissection, TVC [S19].
- **PRES vs SVCR** : chevauchement ; ≈ 10 % des SVCR présentent des lésions de type PRES [S19].
- **Angéite primitive vs SVCR** : les critères de Birnbaum visaient à séparer les deux ; autres mimes : vascularites secondaires (post-infectieuses, VZV, Treponema, VIH), athérosclérose, inflammation liée à l'angiopathie amyloïde, encéphalite auto-immune [S18].
- **Encéphalopathie hypertensive** : un déficit focal oriente vers hémorragie ou infarctus [S16].
- **TVC vs pseudotumor cerebri idiopathique** : exclure un trouble de l'écoulement veineux [S2].
- Cardinal pratique : corticoïdes et vasodilatateurs intra-artériels associés à un mauvais pronostic dans le SVCR [S19] → ne pas traiter un SVCR comme une vascularite (déduction pédagogique à formuler prudemment).

## 9. Urgences et complications
- **TVC** : décompression chirurgicale si lésions parenchymateuses (œdème de stase et/ou hémorragie) avec engagement imminent, pour prévenir le décès (recommandation, consensus 100 %) [S2][S3][S4].
- **HSA** par dissection intracrânienne : traitement endovasculaire ou chirurgical **précoce** suggéré ; mortalité ≈ 55 % sous traitement médical seul vs ≈ 10 % avec intervention ; resaignement ≈ 46 % vs ≈ 32 %, ≈ 2 % après sécurisation [S6].
- **HSA anévrismale** : traiter l'anévrisme dans les **24 h** si l'équipe la plus spécialisée est disponible ; unité neuro-intensive/high care dans un centre ≥ 70 HSA/an (≥ 35 en région isolée) [S9].
- **Encéphalopathie hypertensive** : baisse immédiate mais prudente (§ 10.2) ; chute > 50 % de la PAM associée à AVC ischémique et décès [S16].
- **PRES** sévère : morbidité/mortalité surtout par hémorragie aiguë ou œdème massif de fosse postérieure (hydrocéphalie, compression du tronc) [S20].

## 10. Prise en charge (Suisse / Europe)

### 10.1 TVC (I67.6) — ligne directrice DACH S2k 2023, co-signée par la **Société suisse de neurologie (SNG)** [S2][S3] ; ESO 2017 [S4]
| Phase | Conduite | Force / consensus |
|---|---|---|
| Aiguë | **Héparine à dose thérapeutique**, même en présence d'une hémorragie intracrânienne | forte, 100 % [S3] |
| Aiguë | **HBPM préférée à l'HNF** (méta-analyse 179 vs 352 : pas de différence significative de mortalité/fonction) ; HNF avant chirurgie/procédure ou si insuffisance rénale sévère | modérée, 100 % [S3] |
| Aiguë | AOD **non recommandés** en phase aiguë (instabilité ou surveillance) | [S2][S4] |
| Aggravation sous anticoagulation | recanalisation endovasculaire **dans des cas individuels** en centre neuro-interventionnel (TO-ACT arrêté précocement, sans bénéfice) | faible, 100 % [S2][S3] |
| Engagement imminent | **craniectomie décompressive** | 100 % [S2] |
| Crises | antiépileptique **seulement après une crise** ; pas de prophylaxie (aucun sous-groupe ne la justifie) ; durée 3–6 mois, jusqu'à 12 mois si risque élevé | 100 % [S2] ; ESO : antiépileptique si crise précoce + lésion supratentorielle [S4] |
| HTIC | pas de corticoïdes (prothrombotiques, inefficaces ; exception : Behçet, lupus) ; pas d'acétazolamide en phase aiguë ; PL thérapeutique possible si HTIC sans hémorragie/infarctus de stase (balance avec l'interruption d'anticoagulation) | [S2][S4] |
| Relais | **AOD préférés aux AVK** pendant **3 à 12 mois** (exception : SAPL triple positif → AVK) | modérée, 100 % [S3][S2] |
| Durée | ≥ 3 mois ; arrêt après 3 (à 12) mois si risque faible ; prophylaxie prolongée si risque accru ; ne pas prolonger pour seulement recanaliser (recanalisation surtout dans les 3–6 mois) | [S3] |

- Données comparatives AOD vs AVK (méta-analyse DACH) : MTEV RR 0,17 ; récidive de TVC RR 0,37 ; hémorragie majeure RR 0,35 (tendance non significative) [S3]. Cohorte prospective DOAC-CVT : événement primaire (MTEV symptomatique + hémorragie majeure à 6 mois) 3 % vs 3 % (OR pondéré 0,99 ; IC 0,37–3,38) [S5].
- Récidive : 2–5 % la première année après arrêt [S3] ; cohorte de 706 patients : TVC récidivante 4,4 %, thrombose extracérébrale 6,5 % ; 63 % des récidives la première année (autre cohorte, 624 patients) [S2].
- **Grossesse/contraception** [S2][S3] : TVC pendant la grossesse/post-partum → HBPM thérapeutique jusqu'à ≥ 6 semaines post-partum (≥ 3 mois au total) ; AOD et AVK contre-indiqués (passage placentaire) ; renoncer à la contraception œstroprogestative ; progestatif seul et DIU au lévonorgestrel sans hausse du risque ; une TVC antérieure n'est pas une contre-indication à une grossesse ; prophylaxie HBPM pendant la grossesse et ≥ 6 semaines post-partum ; récidive de TVC lors d'une grossesse ultérieure 0–1,2 %.
- **Statut réglementaire suisse** : ni l'information professionnelle de Clexane® (énoxaparine) ni celle de Pradaxa® (dabigatran) ne mentionnent la TVC dans leurs indications ; indications : TVP/EP (Clexane : 1 mg/kg s.c. 2×/j ou 1,5 mg/kg 1×/j ; Pradaxa : 150 mg 2×/j après ≥ 5 jours d'héparine) [S23][S24]. L'emploi dans la TVC est donc **hors étiquette**, appuyé par les lignes directrices [S2][S3].

### 10.2 Encéphalopathie hypertensive (I67.4) — ESC Council on Hypertension [S16]
| Présentation | Délai / cible | 1re ligne | Alternatives |
|---|---|---|---|
| Encéphalopathie hypertensive | **immédiat**, PAM −20 à −25 % | **labétalol** | nitroprussiate, nicardipine |
| Hypertension maligne ± MAT ou IRA | quelques heures, PAM −20 à −25 % | labétalol | nitroprussiate, nicardipine, urapidil |
- Labétalol : préserve relativement le DSC à baisse tensionnelle égale et n'augmente pas la PIC ; bolus 0,25–0,5 mg/kg ; perfusion 2–4 mg/min puis 5–20 mg/h ; contre-indiqué en BAV 2e/3e degré, insuffisance cardiaque systolique, asthme, bradycardie.
- Nicardipine 5–15 mg/h (début 5 mg/h, +2,5 mg toutes 15–30 min) ; urapidil 12,5–25 mg bolus, 5–40 mg/h ; nitroprussiate 0,3–10 µg/kg/min (toxicité cyanure).
- Chute brutale : soluté salé (déplétion volémique par natriurèse de pression).
- Pas d'ECR pour la plupart des stratégies.
- FI suisses de labétalol/nicardipine/urapidil **non lues** (lacune).

### 10.3 PRES et SVCR [S19][S22]
- PRES : traitement tensionnel urgent associé à une amélioration en heures/jours ; retirer le facteur déclenchant (implicite dans les causes ; non formalisé dans la source) ; pronostic favorable, séquelles/décès 3–6 %, jusqu'à 30 % de décès dans les formes hémorragiques/malignes.
- SVCR : inhibiteurs calciques (nimodipine/vérapamil) les plus utilisés (44,5 % des cas publiés) — usage observationnel, **sans essai** ; corticoïdes et vasodilatateurs intra-artériels associés à un mauvais pronostic ; bon pronostic 78–90 % ; handicap permanent ou décès 5–10 % des formes fulminantes ; mortalité 1–5 %, surtout grossesse/post-partum.

### 10.4 Vasospasme après HSA (I67.80) — ESO/EANS/ESMINT 2026 [S9] et FI Swissmedic [S10][S11]
- **Nimodipine orale recommandée** (évidence élevée) : réduit l'évolution défavorable (OR 0,56 ; 0,40–0,76), pas la létalité (OR 0,74 ; 0,53–1,02) [S9].
- Contre : tirilazad, statines, sulfate de magnésium, antagonistes des récepteurs de l'endothéline (clazosentan) — réduction éventuelle de l'ischémie retardée sans gain fonctionnel [S9].
- Pas de recommandation pour l'hypertension induite (essai arrêté à 41/240) : à envisager seulement après sécurisation de l'anévrisme et échec du remplissage ; angioplastie/traitement endovasculaire du vasospasme = sauvetage de dernière ligne (OR 2,33 pour évolution défavorable dans 2 ECR) [S9].
- **FI suisse Nimotop®** (août 2025) : indication = prévention et traitement des déficits neurologiques ischémiques dus aux spasmes vasculaires cérébraux après HSA anévrismale ; bénéfice prouvé seulement en prophylaxie chez les opérés [S10].
  - Perfusion : 1 mg/h (≈ 15 µg/kg/h) pendant 2 h, puis 2 mg/h (≈ 30 µg/kg/h) si bonne tolérance ; 0,5 mg/h si < 70 kg ou PA instable ; **cathéter central**, pompe, co-perfusion 1:4, tubulures en **polyéthylène** (adsorption par le PVC) ; 10 g d'éthanol par flacon de 50 ml ; perfusion 5–14 jours [S10].
  - Comprimés : 6 × 60 mg/j (intervalle ≥ 4 h) pendant ≈ 7 jours après la perfusion [S11].
  - Contre-indication : **rifampicine** ; antiépileptiques inducteurs (phénobarbital, phénytoïne, carbamazépine) non recommandés ; inhibiteurs CYP3A4 : surveiller la PA ; éviter le pamplemousse (effet jusqu'à 4 jours) ; prudence si PAS < 100 mmHg ; insuffisance hépatique (cirrhose) ou rénale sévère : biodisponibilité accrue, risque d'hypotension [S10][S11].
- **Contentieux** : l'ESO 2026 recommande la voie **orale** ; la FI suisse décrit un schéma **IV 5–14 j puis oral ≈ 7 j**. Durée orale exacte selon l'ESO non lue (tableau 3 en image). À présenter comme fenêtre « mot vert » (source primaire la plus récente : ESO 2026 ; texte réglementaire suisse en vigueur : FI août 2025).

### 10.5 Anévrisme non rompu (I67.10) — ESO 2022 [S7]
- Occlusion préventive suggérée si le risque de rupture estimé à 5 ans dépasse le risque du traitement (faible, très faible évidence) ; risque de rupture à 5 ans moyen 3,4 % (0,3 % à > 15 %) ; risque à 1 an 0,81 %.
- Risque de mauvais pronostic (mRS > 2) à 1 an après traitement 3,6–4,2 % (données intermédiaires d'ECR).
- Pas de préférence endovasculaire vs microchirurgie (complications 4,96 % vs 8,34 % ; retraitement 10,6 % vs 4,6 %) ; flow diverters seulement en absence d'autre option à faible risque.
- Non traités : surveillance radiologique, arrêt du tabac (41 % de rupture chez les fumeurs persistants vs 0/11 chez ceux qui ont arrêté), contrôle tensionnel ; ni statine ni AAS dans le but de prévenir la rupture (ne pas arrêter l'AAS s'il a une autre indication).
- Organisation (consensus) : équipe multidisciplinaire neurochirurgie–neuroradiologie–neurologie, centres > 100 consultations UIA/an, traitement par opérateurs > 30 anévrismes/an ; décision partagée.

### 10.6 Dissection intracrânienne (I67.0) — ESO 2021 [S6]
- Ischémie : thrombolyse IV à envisager après exclusion d'un saignement sous-arachnoïdien subtil (consensus) ; traitement endovasculaire de la lésion en phase hyperaiguë selon le risque hémorragique (consensus).
- HSA : intervention précoce (§ 9). Céphalée isolée avec anévrisme disséquant : données insuffisantes.
- Dissection extracrânienne (rappel, hors I67) : antiagrégant ou anticoagulant au choix (deux ECR de phase 2 sans différence).

### 10.7 Maladie des petites artères (I67.3) — ESO 2021 (couverte) et 2024 (lacunaire) [S12][S13]
- Couverte + HTA : contrôle tensionnel ; pas de cible ni de classe précise ; cibles plus basses pourraient freiner la progression ; pas de baisse tensionnelle chez le normotendu.
- **Pas d'antiagrégant** sans autre indication (potentiellement délétère vers ≥ 70 ans).
- Arrêt du tabac, activité physique, alimentation saine, sommeil, poids ; pas de preuve pour le contrôle glycémique hors diabète ni pour les traitements anti-Alzheimer.
- AVC lacunaire : thrombolyse IV selon les règles générales ; prévention secondaire = **une** antiagrégation au long cours, contrôle tensionnel, hypolipémiant [S13].
- LACI-2 (phase 2, Royaume-Uni) : mononitrate d'isosorbide et cilostazol faisables et sûrs ; signaux à confirmer en phase 3 [S15] → ne pas présenter comme traitement établi.

### 10.8 Moyamoya (I67.5) — ESO 2023 [S17]
- **Antiagrégation au long cours** dans les formes non hémorragiques (consensus 9/9).
- Adulte avec présentation hémorragique : **pontage direct** recommandé (JAM : resaignement 11,9 % vs 31,6 % ; HR 0,36) — faible.
- Adulte ischémique / enfant : revascularisation (directe ou combinée plutôt qu'indirecte) si symptômes et/ou altération hémodynamique ; délai **6–12 semaines** après l'événement ; éviter déshydratation, fièvre, hyperventilation, hypotension.
- Asymptomatique adulte : conservateur sauf altération hémodynamique + lésions ischémiques silencieuses dans le même territoire.
- Centre de référence, neurochirurgien expérimenté ; suivi IRM/angio-IRM + hémodynamique au long cours.

### 10.9 Angéite primitive du SNC (I67.7) — ESO 2023 [S18]
- Induction : glucocorticoïdes + immunosuppresseur chez la plupart (cyclophosphamide ou mycophénolate mofétil) ; glucocorticoïdes seuls envisageables dans les formes légères après discussion pluridisciplinaire.
- Entretien (MMF suggéré) ≥ 2 ans sans récidive avant d'envisager l'arrêt ; aspirine si atteinte des gros/moyens vaisseaux ; AVC aigu : thrombolyse/thrombectomie selon critères standard.
- Prise en charge en centre expert, équipe pluridisciplinaire. Presque toutes les recommandations sont non gradées.

### 10.10 I67.2, I67.11, I67.88, I67.9
- I67.2 athérosclérose cérébrale : renvoi au dossier I66 (cycle 32) pour la maladie athéroscléreuse intracrânienne ; aucune source propre lue ici.
- I67.11 fistule artério-veineuse durale acquise : **aucune source lue** (lacune).

## 11. Suivi et pronostic
- TVC : recanalisation surtout en 3–6 mois, peu après 12 mois [S3] ; épilepsie tardive § 5 [S2].
- Moyamoya : imagerie au long cours, y compris des formes asymptomatiques [S17].
- Anévrisme : imagerie après occlusion (récidive) et des anévrismes surveillés (croissance) [S7].
- PRES : récidive possible [S19] ; SVCR : symptômes résolutifs en ≈ 3 semaines, vasoconstriction en ≈ 3 mois [S19].
- Angéite lymphocytaire semble plus bénigne que les formes nécrosantes/granulomateuses (faible évidence ; l'histologie ne doit pas guider le traitement) [S18].

## 12. Situations particulières
- **Grossesse et post-partum** : TVC (10–20 % des cas) [S3] ; SVCR (20,9 % des cas publiés) [S22] ; PRES (éclampsie) [S20] ; IRM préférée pour la TVC [S2].
- **Enfant** : TVC → HBPM médiane 3 mois ; rivaroxaban non inférieur (EINSTEIN-Junior) [S3] ; moyamoya pédiatrique ischémique, chirurgie suggérée si ischémie persistante [S17].
- **Vaccin SARS-CoV-2 à vecteur** : VITT [S3].

## 13. Critères formels du diagnostic (pour `div.alert`)
- **Encéphalopathie hypertensive (ESC)** : HTA sévère + ≥ 1 parmi crises, léthargie, cécité corticale, coma, sans autre explication [S16].
- **Hypertension maligne (ESC)** : PA habituellement > 200/120 mmHg + rétinopathie avancée (hémorragies en flammèches bilatérales, nodules cotonneux ou œdème papillaire) [S16].
- **TVC** : imagerie avec angiographie veineuse (CT ou IRM) démontrant la thrombose ; IRM pour veines corticales [S2].
- **Angéite primitive (Calabrese & Mallek 1988 ; Birnbaum & Hellmann 2009)** : § 7 [S18].
- **Dissection intracrânienne certaine** : § 7 [S6].
- **Moyamoya** : sténo-occlusion bilatérale ACI terminale/ACA/ACM proximales + collatérales [S17].

## 14. Paramètres clés (pour `div.key`)
- TVC : crises 40–50 % ; contraception combinée 40–50 % des femmes ; HBPM puis AOD 3–12 mois ; D-dimères non fiables [S2][S3].
- Encéphalopathie hypertensive : PAM −20 à −25 % immédiatement ; jamais > 50 % ; labétalol [S16].
- Anévrisme non rompu : prévalence ≈ 3 % ; rupture 5 ans ≈ 3,4 % [S7].
- HSA : létalité ≈ 40 % ; nimodipine orale ; anévrisme traité < 24 h [S9].
- Moyamoya : revascularisation 6–12 semaines après l'événement [S17].
- Angéite primitive : 2,4/million/an ; ASD > angio-IRM ; entretien ≥ 2 ans [S18].

## 15. Pharmacologie (FI Swissmedic lues)
- **Nimotop®** solution pour perfusion et comprimés (Future Health Pharma GmbH), mise à jour août 2025 [S10][S11] : voir § 10.4. PK : liaison protéique ≈ 99 % ; métabolisme hépatique (CYP3A4) ; ≈ 50 % urines, 35 % selles en 4 jours [S10].
- **Clexane®** (énoxaparine), mise à jour février 2026 : posologie TVP 1 mg/kg s.c. toutes 12 h (ou 1,5 mg/kg 1×/j hors situations compliquées ; 2×/j chez l'obèse ou le cancéreux) [S23].
- **Pradaxa®** (dabigatran), mise à jour février 2024 : TVP/EP 150 mg 2×/j après ≥ 5 jours d'héparine [S24].

## 16. Sous-codes couverts
I67.0 ✔ · I67.1/I67.10 ✔ · I67.11 ✘ (lacune) · I67.2 renvoi I66 · I67.3 ✔ · I67.4 ✔ (+ PRES) · I67.5 ✔ · I67.6 ✔ · I67.7 ✔ · I67.80 ✔ · I67.88 codage seulement · I67.9 codage seulement · SVCR (codage CIM non vérifié : probablement I67.88, **non confirmé**).

## 17. Lacunes explicites
1. **Aucune recommandation propre d'une société suisse** (Société cérébrovasculaire suisse / Swiss Stroke Society) trouvée ; seul ancrage suisse : S2k DACH co-signée par la SNG [S2], auteurs suisses dans ESO [S9] ; Swiss Medical Forum : aucun article trouvé.
2. Ligne directrice ESO TVC 2017 : **résumé seulement** (texte intégral Wiley 403) [S4] ; fréquences cliniques de la TVC (céphalée, déficit focal, œdème papillaire), incidence adulte et mortalité **non lues**.
3. ESO HSA 2026 : dose/durée de la nimodipine orale et définitions de l'ischémie retardée **non lues** (tableau en image).
4. Fistule artério-veineuse durale (I67.11) : aucune source lue (classifications de Cognard/Borden non vérifiées).
5. SVCR : pas de ligne directrice européenne ; critères ICHD-3 et score RCVS2 **non lus** ; sources = revue italienne et revue systématique (résumé).
6. PRES : revue descriptive américaine (Mayo, Lancet Neurol 2015, résumé) utilisée seulement pour la description, non pour une conduite ; revue italienne [S19] pour le reste.
7. FI suisses non lues : labétalol, nicardipine, urapidil, nitroprussiate, vérapamil, cyclophosphamide, mycophénolate, acétazolamide.
8. ESO maladie des petites artères couverte : seuil d'âge, prévalence, échelle de Fazekas non lus (texte tronqué) ; noter que la publication PMID 34414305 est une **double publication rétractée** — citer PMID 34414301 [S12].
9. PHASES : composantes du score non lues (seulement mention dans [S8]).
10. I67.2 athérosclérose cérébrale et I67.88 ischémie cérébrale chronique : pas de source spécifique lue.
11. Moyamoya : stades de Suzuki et « ivy sign » non lus.
