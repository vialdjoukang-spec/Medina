# G81 — Hémiparésie et hémiplégie (N-05-Neurologie) — dossier de recherche

Cycle Betta 39, leçon 1 · agent C39-A4-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Note de méthode : le quota WebSearch de la session était épuisé ; la recherche a été faite par PubMed, WebFetch d'URL connues et `tools/swissmedic_fi.py`.

## 0. Question clinique
Un patient présente une faiblesse d'un hémicorps. En aigu, il faut d'abord reconnaître un AVC traitable (thrombolyse, thrombectomie) et écarter un simulateur. À distance, l'hémiparésie devient un syndrome séquellaire : faiblesse, spasticité, posture en flexion du membre supérieur, risque de chute, douleur d'épaule. Comment la décrire, la mesurer, la rééduquer et traiter la spasticité selon les règles suisses et européennes ?

## 1. Définition et périmètre CIM-10-GM
- G81.- Hemiparese und Hemiplegie, bloc G80–G83 (Paralysies cérébrales et autres syndromes paralytiques) [S1].
- Règle d'usage : code primaire seulement si l'hémiparésie est sans précision, ancienne ou de longue date avec cause non précisée ; sinon code supplémentaire pour signaler une hémiparésie de toute cause (p. ex. après AVC) [S1].
- Exclusion : paralysie cérébrale congénitale et infantile (G80.-) [S1].
| Code | Libellé |
|---|---|
| G81.0 | Hémiparésie et hémiplégie flasques |
| G81.1 | Hémiparésie et hémiplégie spastiques |
| G81.9 | Hémiparésie et hémiplégie, sans précision |
- Voisins à distinguer dans le bloc [S1] : G83.2 monoparésie d'un membre supérieur ; G83.1 d'un membre inférieur ; G83.5 locked-in ; G83.6 parésie faciale centrale (exclut G51.0, paralysie faciale périphérique) ; G83.8 inclut la paralysie postcritique de Todd ; G80 exclut la paraplégie spastique héréditaire (G11.4).
- Titre OFS de la leçon : « Hémiparésie et hémiplégie » ; libellés français des sous-codes = traduction du libellé BfArM lu (« schlaffe », « spastische », « nicht näher bezeichnet ») [S1] → à vérifier contre la version OFS française (lacune L1).

## 2. Définitions physiopathologiques
- Spasticité (définition de Lance) : trouble moteur caractérisé par une augmentation, dépendante de la vitesse, des réflexes toniques d'étirement ; elle n'est qu'une composante du syndrome du motoneurone supérieur (SMNS) [S4].
- Elle dépend aussi de la longueur musculaire (quadriceps : plus forte muscle court ; triceps sural : plus forte muscle long) [S4].
- Phénomène du couteau à cran d'arrêt : forte résistance au début de l'étirement d'un muscle court, puis disparition brutale [S4].
- Signes négatifs du SMNS : faiblesse, perte de dextérité, hypotonie, réflexes ostéotendineux diminués — ils apparaissent en premier [S4]. → justifie G81.0 (forme flasque) en phase initiale.
- Signes positifs : spasticité, hyperréflexie, clonus, spasmes en flexion/extension, signe de Babinski, réaction de soutien positive, cocontraction, dystonie spastique, réactions associées ; la spasticité apparaît typiquement plus tard ; le Babinski apparaît tôt [S4]. → G81.1 (forme spastique).
- La cocontraction (perte de l'inhibition réciproque) est décrite comme la forme d'hyperactivité la plus invalidante [S4].

## 3. Épidémiologie
- Suisse, Genève 2018–2019 (Swiss Stroke Registry + dossiers) : incidence annuelle du premier AVC, standardisée sur la population européenne, 127,0/100 000 (ischémique 107,3 ; hémorragie intracérébrale 13,2 ; HSA 6,0) ; âge médian 75,8 ans ; létalité à 30 jours HIC 32,5 %, HSA 17,2 %, ischémique 10,8 % [S7].
- La définition CIM-11 de l'AVC ischémique (inclut les événements < 24 h avec ischémie prouvée à l'imagerie) augmente de 18,3 % les cas par rapport à la CIM-10 [S7].
- Jeunes adultes suisses (18–55 ans, 3995 patients, 2014–2022) : causes dominantes chez les plus jeunes = foramen ovale perméable et dissection artérielle cervicale ; athérosclérose des grosses artères et maladie des petits vaisseaux augmentent avec l'âge [S8].
- Spasticité post-AVC (méta-analyse) : prévalence 25,3 % ; 26,7 % après un premier AVC ; 39,5 % chez les patients avec parésie ; spasticité invalidante (MAS ≥ 3) 9,4 % des patients parétiques ; facteurs de risque : parésie modérée à sévère (OR 6,57), AVC hémorragique (OR 1,88), trouble sensitif [S5].
- Le déficit moteur est « l'une des conséquences les plus fréquentes de l'AVC » ; aucune proportion chiffrée dans la partie lue [S2].

## 4. Mécanismes : normal → pathologique
- Normal : à des vitesses d'étirement cliniques (60–180°/s), aucun réflexe d'étirement n'apparaît chez le sujet sain ; il n'apparaît qu'au-delà d'environ 200°/s ; le tonus normal est donc biomécanique [S4].
- Pathologique : dans la spasticité, l'activité EMG croît avec la vitesse d'étirement [S4].
- Contrôle supraspinal : le faisceau réticulospinal dorsal est inhibiteur ; les faisceaux réticulospinal médian et vestibulospinal sont facilitateurs ; la spasticité résulte de la prédominance de la facilitation ; une lésion pyramidale pure ne suffit pas à causer une spasticité [S4].
- Mécanismes spinaux : réduction des inhibitions post-synaptiques (Ib, Ia réciproque, récurrente) et présynaptique ; réduction de la dépression post-activation, surtout par immobilisation, corrélée à la sévérité de la spasticité après AVC [S4].
- Le délai entre lésion et spasticité plaide contre un simple phénomène de libération et suggère une plasticité spinale et cérébrale [S4].
- Hypertonie non réflexe (intrinsèque) : l'immobilisation en position courte réduit les sarcomères en série et augmente le tissu conjonctif → résistance indépendante de la vitesse ; composantes réflexe et non réflexe difficiles à séparer cliniquement [S4].
- Posture hémiplégique : membre supérieur fléchi et en adduction, membre inférieur en extension (contribution de la dystonie spastique) [S4].
- Douleur et spasticité s'entretiennent mutuellement [S4].

## 5. Causes
- Principale cause traitée dans les sources lues : AVC ischémique et hémorragique [S2][S5][S7].
- Causes de l'AVC ischémique du sujet jeune en Suisse : FOP, dissection cervicale ; puis athérosclérose, petits vaisseaux [S8].
- Paralysie postcritique de Todd (G83.8) : déficit transitoire après crise, de quelques minutes à plusieurs jours, surtout en cas de lésion cérébrale structurelle [S1][S12] (rapport de cas, niveau faible).
- Pseudo-AVC (« stroke mimics ») parmi les AVC ischémiques suspectés : 24,8 % ; types les plus fréquents : vestibulopathie périphérique 23,2 %, toxique/métabolique 13,2 %, crise épileptique 13 %, trouble fonctionnel 9,7 %, migraine 7,76 % [S6].
- Lacune : tumeurs, abcès, SEP, traumatisme, hématome sous-dural comme causes d'hémiparésie — non documentés par une source lue (L2).

## 6. Anamnèse et examen
- Heure de début / dernière heure vu en bonne santé : conditionne la thrombolyse (< 4,5 h ; fenêtres étendues selon imagerie) [S9].
- Anticoagulant oral direct : 27 % des non-thrombolysés dans la fenêtre à Zurich ; activité anti-Xa non testée chez 50 % d'entre eux [S10].
- Pseudo-AVC : plus jeunes, plus souvent des femmes, moins de facteurs de risque vasculaire, tension artérielle presque normale, symptômes moins sévères ; aide clinique : HINTS (vertige) et signe de Hoover (trouble fonctionnel) [S6].
- Déficit moteur discret du membre supérieur par lésion corticospinale (17 AVC moteurs purs légers) : sensibilité du thumb rolling 88 %, forearm rolling 65 %, index finger rolling 65 %, épreuve de pronation (pronator drift) 47 % ; ces tests sont plus souvent anormaux que les tests de force, tonus ou réflexes ; les segments distaux sont plus atteints que les proximaux [S13].
- Échelles de mesure citées par l'ESO : FMA-UE, ARAT, WMFT, MAL ; marche : 6MWT, test de marche 5 m, FAC, FGA, Rivermead ; équilibre : Berg, TUG ; indépendance : MIF, Barthel [S2].
- Échelle d'Ashworth modifiée (MAS) : seuil ≥ 3 = spasticité invalidante dans la méta-analyse [S5] ; la FI tizanidine mentionne l'échelle d'Ashworth [S16].

## 7. Diagnostic et différentiel
- En aigu, hémiparésie = suspicion d'AVC jusqu'à preuve du contraire ; imagerie CT ou IRM ; le CT de perfusion peut faussement suggérer une ischémie chez un patient en postcritique [S9][S12].
- IRM de diffusion ou perfusion : rôle dans le différentiel des pseudo-AVC, à mieux évaluer [S6].
- Thrombolyse de pseudo-AVC : HIC 0,7 % vs 9,4 % dans les AVC, décès 1,9 % vs 11,3 % → profil de sécurité rassurant, mais évaluation par un médecin expérimenté recommandée [S6].
- Différentiel de codage : G81 (hémicorps) vs G83.2/G83.1 (monoparésie), G83.6 (facial central) vs G51.0 (périphérique), G80 (PC infantile) [S1].

## 8. Urgences — phase aiguë
- ESO 2021 : < 4,5 h → thrombolyse IV par altéplase (forte, haute qualité) ; 4,5–9 h avec seul CT natif → contre la thrombolyse ; 4,5–9 h avec mismatch core/perfusion, sans thrombectomie prévue → altéplase ; AVC du réveil avec mismatch DWI-FLAIR → altéplase (forte, haute qualité) ; dose des essais 0,9 mg/kg [S9].
- Zurich 2020–2022 : 51,5 % des AVC arrivés < 4,5 h non thrombolysés ; motifs : symptômes légers 41,8 %, AOD 27 %, infarctus « démarqué » 8,3 % (dont 41,2 % reclassés en signes précoces) [S10].
- Dysphagie post-AVC > 50 % en aigu ; dépistage recommandé chez tous (qualité modérée) pour prévenir pneumonie et mortalité précoce [S11].
- Mobilisation précoce : guide pratique suisse non contraignant (Swiss Stroke Society, réseaux Therapy et Nursing), application dès janvier 2026 ; preuves insuffisantes pour fixer dose et intensité [S3]. Détails chiffrés non lus (L3).

## 9. Prise en charge suisse et européenne — rééducation motrice (ESO 2025) [S2]
| Question | Énoncé | Force / qualité |
|---|---|---|
| Membre supérieur | ≥ 20 h supplémentaires de pratique répétitive (souvent 3–5×/sem sur 4–6 sem) | faible, très faible |
| Marche, dose | ≥ 20 h supplémentaires de marche | consensus d'experts |
| Marche à haute intensité | phase chronique (> 6 mois), état cardiovasculaire stable : endurance | forte, modérée |
| idem, vitesse de marche | | faible, faible |
| Paquet de transfert | avec entraînement spécifique du MS | consensus |
| Groupe vs individuel | thérapie de groupe spécifique non inférieure (équilibre, vitesse, endurance) | faible, très faible |
| Assis-debout | entraînement supplémentaire pour l'équilibre, nombreuses répétitions | faible, modérée |
- Haute intensité = 60–84 % de la FC de réserve, ou 77–93 % FC max, ou Borg 14–16/20 [S2].
- Discordance relevée dans la guideline : le résumé grand public dit « fortement recommandé » pour vitesse et endurance ; abstract et PICO 3 : fort pour endurance, faible pour vitesse [S2].
- Interface cerveau-ordinateur (Cochrane 2026, 43 ECR) : amélioration possible légère de la fonction du MS vs thérapie conventionnelle (FMA MD 4,67), certitude faible ; pas d'effet sur la spasticité [S14].
- Mobilisation, étirements individualisés, positionnement, attelles et plâtres, éviter les positions raccourcies prolongées : essentiels pour prévenir et traiter spasticité et hypertonie intrinsèque [S4].

## 10. Traitement de la spasticité — médicaments (FI Swissmedic)
### Toxine botulinique A (BOTOX®, FI mise à jour mai 2025) [S15]
- Mécanisme : bloque la libération présynaptique d'acétylcholine par clivage de SNAP-25.
- Indication : traitement symptomatique de la spasticité focale des membres supérieurs et inférieurs chez l'adulte (et dès 2 ans).
- MS adulte, doses initiales : biceps 50–200 U (≤ 4 sites) ; FDP 7,5–30 U ; FDS 7,5–30 U ; FCR 15–60 U ; FCU 10–40 U ; total ≤ 360 U dans les études ; en général ≤ 6 U/kg ; amélioration en 2 semaines, effet maximal 4–6 semaines ; réinjection après disparition de l'effet, intervalle ≥ 2 mois ; guidage EMG / stimulation nerveuse utile ; ne remplace pas la rééducation standard.
- MI adulte : 300–400 U, maximum 400 U par séance (gastrocnémien médial et latéral 75 U chacun, soléaire 75, tibial postérieur 75, FHL 50, FDL 50, FDB 25) ; réinjection pas avant 12 semaines.
- Précautions : pas pour cheville/pied après AVC si aucun gain fonctionnel, antalgique ou de soins n'est attendu ; risque de chute accru ; prudence chez les âgés comorbides ; spasticité du MI post-AVC traitée après évaluation par des médecins expérimentés ; décès post-commercialisation (parfois pneumonie d'aspiration) et diffusion à distance.
- Autres BoNT-A avec indication de spasticité focale en Suisse (titres AIPS lus, textes non lus) : Dysport® (MS et MI dès 2 ans), Xeomin (MS et MI adulte) [S18].
- Consensus européen (5 experts) : BoNT-A = option de première ligne de la spasticité post-AVC ; épaule pattern A (adduction, élévation, flexion, rotation interne) → grand pectoral, grand rond (± subscapulaire) ; pattern B (abduction/adduction, extension, rotation interne) → deltoïde postérieur, grand rond, grand dorsal ; choisir selon la limitation fonctionnelle et les attentes du patient [S17].
- Anticorps neutralisants après BoNT pour spasticité des membres : ≈ 1 % ; sensibilité 56 %, spécificité 99,6 % pour expliquer une non-réponse secondaire ; l'immunogénicité n'est pas la cause la plus fréquente de non-réponse [S19].
### Tizanidine (Tizanidine axapharm, FI janvier 2026) [S16]
- Indications : spasmes douloureux ; spasticité de SEP, de lésions médullaires et **de lésions cérébrales**.
- Mécanisme : agoniste alpha-2 présynaptique → baisse de la libération d'acides aminés excitateurs (récepteurs NMDA) → inhibition polysynaptique des interneurones spinaux.
- Posologie spasticité : ≤ 6 mg/j en 3 prises au départ, + 2–4 mg 1–2×/sem ; optimum 12–24 mg/j en 3–4 prises ; maximum 36 mg/j ; marge thérapeutique étroite, forte variabilité.
- CI : insuffisance hépatique sévère ; inhibiteurs puissants du CYP1A2 (fluvoxamine, ciprofloxacine). Inhibiteurs modérés : déconseillés.
- Arrêt brusque : rebond hypertensif et tachycardie, jusqu'à événements cérébrovasculaires → arrêt progressif. ClCr < 25 ml/min : exposition ×6, débuter 2 mg 1×/j.
### Baclofène oral (Liorésal®, FI janvier 2025) [S20]
- Indication suisse : spasticité grave réversible de la SEP ; spasticité médullaire (infectieuse, dégénérative, traumatique, néoplasique). **Pas d'indication cérébrale/post-AVC dans la FI** → usage hors indication à signaler.
- FI : « mauvaise tolérance au baclofène, principalement à la suite d'un AVC » → prudence particulière.
- Mécanisme : agoniste GABA-B médullaire, inhibe réflexes mono- et polysynaptiques.
- Adulte : 3 × 5 mg/j, + 5 mg par prise tous les 3 jours ; 30–80 mg/j ; 100–120 mg/j sous surveillance hospitalière ; réévaluer si aucune amélioration 6–8 semaines après la dose maximale ; arrêt progressif sur ~3 semaines (risque d'anxiété, confusion, hallucinations, convulsions, hyperthermie, rebond).
- Prudence : la spasticité peut être utile au maintien debout et à la marche (risque de chute) ; rétention urinaire si hypertonie sphinctérienne ; insuffisance rénale terminale ; suicidalité, abus.
- Forme intrathécale : Liorésal intrathécal® (titre AIPS lu, texte non lu) [S18].

## 11. Suivi, complications, situations particulières
- Douleur et spasticité se renforcent mutuellement ; le maintien du mouvement prévient l'hypertonie intrinsèque [S4].
- Risque de chute : explicitement cité dans les FI BOTOX et baclofène [S15][S20].
- Dysphagie : pneumonie d'aspiration, dénutrition, déshydratation [S11].
- Pédiatrie : la paralysie cérébrale infantile relève de G80 ; registre suisse Swiss-CP-Reg (titre lu seulement) [S1][S21].

## 12. Critères formels (pour l'îlot final)
- Codage G81 : hémiparésie/hémiplégie ; .0 flasque, .1 spastique, .9 sans précision ; code primaire seulement si cause non précisée ou séquelle ancienne ; sinon code additionnel [S1].
- Spasticité : augmentation du tonus dépendante de la vitesse d'étirement (Lance) [S4].
- Spasticité invalidante : MAS ≥ 3 [S5].

## 13. Paramètres clés
- Incidence premier AVC Genève 127/100 000/an [S7] ; spasticité 25 % des AVC, 39,5 % des AVC parétiques [S5] ; pseudo-AVC 24,8 % [S6].
- Thrombolyse < 4,5 h ; altéplase 0,9 mg/kg [S9].
- Rééducation : +20 h MS ; marche haute intensité 60–84 % FC réserve [S2].
- BOTOX MS ≤ 360 U, MI ≤ 400 U ; intervalles ≥ 2 mois (MS) / ≥ 12 sem (MI) [S15].
- Tizanidine max 36 mg/j ; baclofène 30–80 mg/j [S16][S20].

## 14. Sous-codes couverts
G81.0, G81.1, G81.9 (toutes les sous-catégories CIM-10-GM 2024 de G81) ; voisins G83.x et G80 pour le différentiel.

## 15. Lacunes
- L1 : version française OFS du libellé des sous-codes non lue (lecture BfArM allemande).
- L2 : causes non vasculaires d'hémiparésie (tumeur, abcès, SEP, HSD, traumatisme, hypoglycémie) — aucune source lue ; ne pas les détailler sans source.
- L3 : contenu détaillé du guide suisse de mobilisation précoce (smw.ch indisponible, HTTP 503) ; abstract seul lu.
- L4 : aucune recommandation suisse spécifique sur la spasticité (Société suisse de neurologie / Swiss Medical Forum) lue — recherche web bloquée (quota).
- L5 : guideline ESO thrombolyse lue sur 100 000 / 421 000 caractères ; pas de recommandation spécifique « pseudo-AVC » lue.
- L6 : FI Dysport, Xeomin, Liorésal intrathécal non lues (titre et indication seulement).
- L7 : pronostic de récupération motrice (modèles prédictifs), douleur d'épaule hémiplégique, échelles Ashworth/Tardieu (définitions détaillées) non sourcés.
- L8 : épidémiologie suisse de l'hémiparésie en tant que telle inexistante dans les sources lues ; seulement l'incidence de l'AVC.
