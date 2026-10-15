# I68 — Troubles cérébrovasculaires au cours de maladies classées ailleurs (N-05-Neurologie)

Dossier de recherche, cycle Betta 33, leçon 2, agent C33-A1-NEUR (Opus 5.5), 15.10.2026.
Chaque fait porte sa référence `[Sx]` (détail dans `sources.json`). Rien n'est écrit de mémoire. Plusieurs sources n'ont été lues qu'en **résumé** (champ `limites`) : le rédacteur ne doit pas en tirer plus que ce qui figure ici. Les lacunes sont au § 17. Les propositions pédagogiques sont signalées comme telles ; ce ne sont pas des données.

---

## 0. Question clinique et angle pédagogique

I68 est une **catégorie astérisque (*)** : elle code la **manifestation cérébrovasculaire**, tandis que la maladie causale porte le code croix (†) [S1][S2]. La leçon doit donc répondre à une question unique : **« quelle maladie générale ou infectieuse abîme ici les vaisseaux cérébraux, et comment cette cause change-t-elle la conduite ? »**

Proposition de pondération (choix pédagogique) : l'**angiopathie amyloïde cérébrale (AAC, I68.0)** est l'entité dominante à l'examen et en pratique (cause principale d'hématome lobaire du sujet âgé, décisions antithrombotiques, immunothérapies anti-amyloïdes) [S3][S7]. Viennent ensuite les **artérites infectieuses (I68.1)** — syphilis méningovasculaire, tuberculose, Listeria — puis l'**artérite lupique (I68.2)** et la rubrique résiduelle **I68.8**.

## 1. Définition et classification (CIM-10-GM 2024)

| Code | Intitulé (OFS) | Code causal † cité par la classification | Source |
|---|---|---|---|
| I68* | Troubles cérébrovasculaires au cours de maladies classées ailleurs | — | [S1] |
| I68.0* | Angiopathie amyloïde cérébrale | E85.-† (amylose) | [S1] |
| I68.1* | Artérite cérébrale au cours de maladies infectieuses et parasitaires | Listeria A32.8† ; syphilis A52.0† ; tuberculose A18.8† | [S1][S2] |
| I68.2* | Artérite cérébrale au cours d'autres maladies classées ailleurs | lupus érythémateux disséminé M32.1† | [S1][S2] |
| I68.8* | Autres troubles cérébrovasculaires au cours de maladies classées ailleurs | aucune inclusion dans la version GM ; la CIM-10 OMS 2019 y cite l'« apoplexie urémique au cours d'une maladie rénale chronique » (N18.5†) | [S1][S2] |

- E85.- (amylose) comprend E85.0 non neuropathique héréditaire, E85.1 neuropathique héréditaire, E85.2 héréditaire SAI, E85.3 secondaire systémique, E85.4 limitée à un organe (« amylose localisée »), E85.8 autre, E85.9 SAI ; E85 exclut la maladie d'Alzheimer (G30.-) [S1]. Le choix du sous-code E85 pour l'AAC n'est pas précisé par la classification lue (lacune § 17).
- Titres français : registre MEDINA `nosology/fragments/S08.json` (I68, I68.0, I68.1, I68.2, I68.8), source OFS [S1].
- Note de codage : le système croix-astérisque impose deux codes (cause † + manifestation *) [S1][S2]. Un AVC ischémique ou un hématome avéré se code en outre dans I61/I63 selon les règles du bloc (règle non vérifiée pour I68 précisément — lacune).

## 2. Épidémiologie

**AAC (I68.0)**
- Maladie fréquente des petits vaisseaux ; prévalence ≈ 25 % chez les sujets âgés avec atteinte modérée à sévère et 30–50 % dans les cohortes hospitalières et chez les patients avec troubles cognitifs [S3].
- Méta-analyse (170 études, > 73 000 sujets) : chez les patients Alzheimer, prévalence anatomopathologique 48 % contre 22 % par microsaignements lobaires stricts ; population générale 23 % (pathologie) contre 7 % (IRM) ; sujets âgés cognitivement normaux 5–7 % ; hémorragie intracérébrale (HIC) toutes localisations 19–24 % ; **HIC lobaire 50–57 %** [S7].
- AAC et maladie d'Alzheimer : moins de 50 % des AAC remplissent les critères anatomopathologiques d'Alzheimer ; plus de 75 % des Alzheimer ont peu ou pas d'AAC ; l'Alzheimer « pur » ne se voit que dans 9 % des autopsies [S3].
- Épisodes neurologiques focaux transitoires (ENFT) : présentation la plus fréquente de l'AAC après l'HIC lobaire (14,5 % d'une cohorte européenne de 172 patients) ; environ 1 % des suspicions d'AIT pourraient relever de l'AAC [S8].
- Hémorragie sous-arachnoïdienne de la convexité non traumatique : l'AAC en explique environ un quart à un tiers, et ≈ 76 % après 60 ans [S8].
- AAC iatrogène : cas rapportés dans le monde après intervention exposant à une transmission d'Aβ (dure-mère cadavérique, instrumentation cérébrale ou médullaire) ; latence habituelle de trois à quatre décennies ; série de cinq cas ≥ 65 ans (latence 30–39 ans) [S11].

**Artérites infectieuses (I68.1)**
- Méningite bactérienne de l'adulte : complications cérébrovasculaires dans 15–40 % (vasculite, vasospasme, hyperperfusion corticale focale, autorégulation altérée, thrombose septique sinusale et veineuse corticale) [S17].
- Méningite tuberculeuse : AVC chez 15–57 % des patients, surtout aux stades avancés ; souvent asymptomatiques [S18].
- Neurosyphilis méningovasculaire : « l'une des manifestations les plus fréquentes » de la neurosyphilis ; pas de chiffre donné [S15].
- Listeria : germe à évoquer en troisième position, après pneumocoque et méningocoque, dans la méningite communautaire de l'adulte en Europe (recommandation 2) [S17] ; fréquence chiffrée non relevée dans la lecture (voir dossier G01).

**Lupus (I68.2)** : la maladie cérébrovasculaire fait partie des manifestations neuropsychiatriques **fréquentes** du lupus (incidence cumulée > 5 %) ; les anticorps antiphospholipides multiplient au moins par cinq le risque cérébrovasculaire [S22].

## 3. Rappel normal → pathologique (mécanismes)

**AAC**
- Normal : l'Aβ est éliminé du cerveau notamment par voie périvasculaire [S3].
- Pathologique : dépôt progressif d'**Aβ (surtout Aβ40, espèces plus courtes que dans les plaques d'Alzheimer)** dans la **média et l'adventice des petits vaisseaux corticaux et leptoméningés** [S3]. Altération de la clairance de l'Aβ → augmentation de l'Aβ vasculaire → clairance périvasculaire encore réduite (cercle vicieux) [S3].
- Conséquences : (1) **macrohémorragies lobaires** → déficits focaux souvent sévères ; (2) **microsaignements** → déclin cognitif à bas bruit ; (3) lésions de substance blanche (espaces périvasculaires élargis du centre semi-ovale, hypersignaux en « multispot ») ; (4) micro-infarcissements corticaux et petits infarctus sous-corticaux récents ; (5) ENFT [S3][S4].
- Profil cognitif : atteinte d'abord des fonctions exécutives et de la vitesse de traitement, par syndrome de déconnexion de la substance blanche [S3].
- Mécanisme probable des ENFT : **dépolarisation corticale envahissante** (≈ 3 mm/min) déclenchée par un saignement superficiel (HSA de la convexité, sidérose superficielle), ce qui explique la progression « en marche » ; preuve directe manquante [S8].
- Inflammation liée à l'AAC (AAC-ri) : sous-type rare, agressif, attribué à une réaction immunitaire contre l'Aβ vasculaire ; potentiellement réversible et corticosensible [S12][S13]. Anticorps anti-Aβ du LCR élevés en phase active, mais non validés pour le diagnostic [S12].
- ARIA sous anticorps anti-amyloïdes : œdème/effusion (ARIA-E) et hémorragie/dépôts d'hémosidérine (ARIA-H, microhémorragies ≤ 10 mm et sidérose superficielle) ; l'AAC concomitante augmente ce risque [S3][S14].

**Artérite tuberculeuse** : vaisseaux pris dans l'exsudat basal (artères striées médianes, thalamo-tubérales, thalamo-striées), étirés par l'hydrocéphalie → infarctus multiples, bilatéraux, des noyaux gris (« zone tuberculeuse » : caudé, thalamus antérieur, bras antérieur et genou de la capsule interne) ; atteinte possible des segments proximaux des artères cérébrales moyenne, antérieure, postérieure, de la carotide supraclinoïdienne et du tronc basilaire ; rôle évoqué du TNF-α, du VEGF, des métalloprotéinases et d'un état prothrombotique ; à l'autopsie, l'artérite est plus fréquente que l'infarctus [S18].

**Méningite bactérienne** : vasculite, vasospasme, troubles de l'autorégulation et thrombose septique veineuse → ischémie, parfois transformée en hémorragie [S17].

**Syphilis méningovasculaire** : atteinte vasculaire et méningée ; peut survenir quelques mois ou plusieurs années après l'infection ; classée selon les auteurs en neurosyphilis précoce, tardive ou les deux [S15][S16]. L'histologie (endartérite) n'est pas décrite dans les sources lues (lacune).

**VZV (vasculopathie à virus varicelle-zona)** : réactivation du virus latent dans les ganglions sensitifs → vasculite cérébrale → ischémie, chez l'enfant comme chez l'adulte [S21] ; risque accru chez l'immunodéprimé (atteinte multifocale) [S19][S20]. Rattachement de la vasculopathie VZV à I68.1 : non explicite dans la classification lue (lacune).

**Lupus** : la maladie cérébrovasculaire thrombotique est surtout liée aux anticorps antiphospholipides [S22].

## 4. Causes et facteurs de risque (synthèse)

| Entité | Facteurs | Source |
|---|---|---|
| AAC sporadique | âge ; association à l'Alzheimer ; APOE ε4 associé à l'HIC lobaire liée à l'AAC | [S3][S7][S9] |
| AAC iatrogène | neurochirurgie de l'enfance, dure-mère cadavérique, latence 30–40 ans | [S11] |
| AAC et ARIA | homozygotie APOE ε4 ; microsaignements ou sidérose préexistants | [S14] |
| AAC et trisomie 21 | taux plus élevé d'AAC et d'ARIA | [S14] |
| Listeria | âge, cancer, immunosuppression | [S17] |
| Syphilis méningovasculaire | AVC du sujet jeune, surtout de l'homme, sans profil de risque vasculaire | [S15] |
| VZV | infection VZV récente, CD4 < 200/µl (VIH) ; varicelle chez l'enfant non vacciné | [S20][S21] |
| Lupus | anticorps antiphospholipides | [S22][S23] |

## 5. Anamnèse

- AAC : âge ≥ 50 ans ; HIC spontanée lobaire ; épisodes transitoires stéréotypés ; déclin cognitif ; recherche d'une neurochirurgie dans l'enfance (iatrogène) [S4][S5][S11].
- ENFT : épisodes brefs (< 6 min dans 44 %, < 30 min dans 70 %, ≤ 3 h dans 96 %), **récidivants et stéréotypés**, s'étendant de proche en proche (main → bras → visage) ; symptômes positifs (paresthésies bouche/main 32 %) ou négatifs (faiblesse, dysphasie), mixtes dans 25 % [S8].
- AAC-ri : début aigu ou subaigu de céphalées, baisse de vigilance, troubles du comportement, déclin cognitif, crises, signes focaux ; âge typiquement ≥ 40 ans [S12].
- ARIA : céphalées, confusion, nausées, vomissements, vertiges, tremblement, troubles visuels et du langage, baisse de vigilance, crises ; le plus souvent asymptomatiques ; surtout dans les 24 premières semaines de traitement [S14].
- Syphilis : exposition sexuelle ; antécédent de syphilis secondaire ; AVC jeune sans facteur de risque [S15][S16].
- Méningite : fièvre, céphalée, raideur ; terrain à risque Listeria [S17].
- Zona ou varicelle récents (VZV) [S19][S21].
- Lupus connu, thromboses ou fausses couches (antiphospholipides) [S22][S23].

## 6. Examen clinique

- Déficit focal selon le territoire ; signes méningés ; atteinte des nerfs crâniens, du nerf optique (syphilis méningovasculaire) [S15].
- Fond d'œil avant ponction lombaire dans la syphilis ; examen neurologique, oculaire et otologique complet chez tout patient séropositif [S16].
- Recherche d'éruption zostérienne (zona ophtalmique compliqué) [S19].

## 7. Examens complémentaires

**AAC — IRM**
- Séquences sensibles au fer (**T2\*** et **SWI**) : microsaignements lobaires, sidérose superficielle corticale (SSc) ; FLAIR : hypersignaux « multispot » ; espaces périvasculaires du centre semi-ovale [S3][S4].
- Une SSc isolée dans un contexte suspect est fortement évocatrice d'AAC (OR 36,5 ; IC 95 % 8,7–153,9) [S3].
- Petites lésions de diffusion (≤ 10 mm) proches des saignements : possibles dans l'AAC, à ne pas confondre avec des infarctus emboliques [S8].
- Scanner : détecte l'HSA aiguë de la convexité ; l'IRM T2\*/SWI est supérieure en phase subaiguë [S8].

**AAC — scanner seul (critères d'Édimbourg)**
- Développés sur 110 autopsies (LINCHPIN) : chez 62 HIC lobaires, l'AAC modérée à sévère est associée à l'**HSA associée** (89 % contre 42 %), aux **projections digitiformes** (39 % contre 0 %) et au **portage APOE ε4** (50 % contre 8 %) ; c-statistique 0,92 ; règle d'inclusion : HSA + (APOE ε4 ou projections digitiformes) → spécificité 96 % [S9].
- Valeur pronostique (méta-analyse sur données individuelles, 8 cohortes dont Bern) : récidive d'HIC à 5 ans 12 % (bas risque), 16 % (risque intermédiaire, HR ajusté 1,68), 26 % (haut risque, HR 2,97) ; critères CT-APOE haut risque : récidive à 3 ans 15 % contre 8 % (HR 2,22) [S10]. Utile là où l'IRM manque [S10].

**AAC-ri** : IRM : hypersignaux FLAIR cortico-sous-corticaux uni- ou bilatéraux (œdème vasogénique ou effusion sulcale) + au moins un marqueur T2\*/SWI (microsaignements, SSc) ; LCR pour exclure infection ou tumeur ; protéinorachie élevée ≈ 71 %, pléiocytose ≈ 45 % [S12].

**Donanemab (ARIA)** : IRM initiale ≤ 3 mois, puis avant les 2e, 3e, 4e et 7e perfusions ; IRM supplémentaire avant la 12e chez les patients à risque (APOE ε4 hétérozygote, ARIA antérieur) ; FLAIR pour ARIA-E, T2\* GRE (ou SWI) pour ARIA-H ; IRM immédiate en cas de symptômes [S14].

**Syphilis** [S15][S16]
- LCR indiqué en cas d'atteinte neurologique, oculaire ou auriculaire, quel que soit le stade (1, C) [S16].
- LCR : protéines, cellules mononucléées, test tréponémique (TPHA/TPPA) et non tréponémique (VDRL) ; VDRL du LCR positif dans ≈ un tiers des neurosyphilis seulement ; TPHA du LCR négatif → neurosyphilis très improbable ; PCR peu utile [S16].
- Protéinorachie particulièrement élevée dans la forme méningovasculaire ; quotient albumine LCR/sérum (Reiber) recommandé pour évaluer la barrière [S15].

**Méningite bactérienne** [S17]
- Imagerie initiale : rechercher hydrocéphalie, œdème, ischémie, thrombose sinusale/veineuse (consensus fort, recommandation 11).
- IRM si signes inexpliqués par le scanner, aggravation sous traitement ou foyer incertain (recommandation 8).
- Doppler transcrânien envisageable comme dépistage chez les patients à risque d'ischémie par vasculopathie (recommandation 12).

**Méningite tuberculeuse** : l'IRM (diffusion en aigu, T2/FLAIR en chronique) est plus sensible que le scanner pour les infarctus [S18].

**VZV** : ADN VZV par PCR et IgG anti-VZV dans le LCR ; IRM avec lésions ischémiques ; l'imagerie vasculaire peut être normale [S19][S21].

**Lupus neuropsychiatrique** : bilan comparable à celui d'un patient non lupique présentant le même tableau, pour exclure d'autres causes : LCR (infection), EEG, tests neuropsychologiques, IRM (T1/T2, FLAIR, diffusion, T1 injecté) [S22].

## 8. Diagnostic et diagnostic différentiel

- **ENFT vs AIT** : l'ENFT progresse de proche en proche, est plus souvent sensitif et récidive à l'identique ; distinction capitale car les antithrombotiques peuvent être dangereux dans l'AAC [S8]. Autres imitateurs : aura migraineuse, crise focale (EEG de routine sans activité épileptiforme dans les ENFT) [S8].
- **AAC-ri vs AVC ischémique** : présentation pseudo-vasculaire possible ; l'IRM tranche [S13].
- **AAC-ri vs ARIA** : contre-indication du donanemab en cas d'images évoquant une AAC-ri [S14] ; une ARIA peut mimer un AVC ischémique [S14].
- **Exclusions des critères de Boston 2.0** : toute lésion hémorragique profonde en T2\* ; autre cause de saignement (traumatisme, transformation hémorragique d'un infarctus, malformation artério-veineuse, tumeur hémorragique, AVK avec INR > 3, vasculite) ; une hémorragie cérébelleuse n'est comptée ni comme lobaire ni comme profonde [S5].
- **Neurosyphilis** : penser à la forme méningovasculaire devant un AVC du sujet jeune sans profil vasculaire [S15].
- **Lupus** : évaluer et traiter d'abord comme chez un non-lupique, puis attribuer secondairement au lupus [S22].

## 9. Urgences

- **HIC lobaire** : prise en charge de l'hématome (cours I61). Chirurgie mini-invasive de l'hématome **suggérée** pour réduire la mortalité (faible niveau, recommandation faible ; bénéfice attribuable aux HIC lobaires, essai ENRICH) [S6].
- **HSA de la convexité aiguë** : suspendre les antithrombotiques au moins 24–48 h ; PAS < 140 mmHg raisonnable en phase aiguë [S8] (source de revue, non recommandation formelle).
- **ARIA symptomatique ou AVC sous donanemab** : **thrombolyse et anticoagulation contre-indiquées** ; un cas mortel d'HIC après thrombolyse pour un ARIA-E pris pour un AVC [S14].
- **Méningite bactérienne avec complication vasculaire** : héparine i.v. à dose thérapeutique en cas de thrombose veineuse sinusale (consensus fort, recommandation 27) ; nimodipine et/ou corticoïdes envisageables en cas de vasculopathie, avec mesure artérielle invasive si nimodipine i.v. (recommandation 26) [S17].
- **Benzylpénicilline à hautes doses** : risque de convulsions (perfusion trop rapide, insuffisance rénale, épilepsie) [S25] ; prophylaxie anticonvulsivante si crises antérieures ou EEG épileptiforme [S15].

## 10. Prise en charge (Suisse / Europe)

### 10.1 AAC
- Aucun traitement spécifique de l'AAC [S3].
- **Pression artérielle** : contrôle strict, cible **< 130/80 mmHg**, voire < 120/80 (SPRINT-MIND) à confirmer [S3]. ESO/EANS 2025 : cible ≤ 130/80 mmHg après HIC (qualité faible), contrôle tensionnel recommandé (recommandation forte) ; dans ERICH, un contrôle insuffisant s'associe à plus de récidives d'HIC lobaire (HR 3,53) [S6].
- **Antithrombotiques** : les éviter lorsque c'est possible ; éviter l'excès d'alcool [S3].
- **Anticoagulation orale après HIC** (ESO/EANS 2025, PICO 6.2) : un AOD « peut être envisagé » après évaluation individuelle (qualité faible) ; OAC → plus de récidives d'HIC (OR 3,62) mais moins d'événements cardiovasculaires majeurs (OR 0,64) ; AOD préférés aux AVK. Raisons d'éviter l'OAC citées : HIC liée à l'AAC avec SSc ou HSA de la convexité non anévrismale, HIC liée à l'AAC avec ≥ 5 microsaignements lobaires, HIC non liée à l'AAC avec ≥ 10 microsaignements, HTA non contrôlée ; l'essai ENRICH-AF a stoppé le recrutement des HIC lobaires/HSA de convexité pour excès de récidives (données non publiées) [S6].
- **Fermeture de l'auricule gauche** (PICO 6.3) : peut être envisagée chez les patients inaptes à une OAC au long cours, notamment avec AAC prouvée par l'imagerie ou l'anatomopathologie (qualité très faible) ; antithrombotiques péri-procéduraux selon l'ESC [S6].
- **Antiagrégants** (PICO 6.4, RESTART n = 537) : reprise pour une indication reconnue sûre mais effets globaux incertains (qualité modérée, recommandation faible) ; récidive d'HIC 4 % contre 9 % (OR 0,50 ; IC 0,24–1,03) [S6].
- **Statines** (PICO 6.5) : incertitude ; avis d'experts : les débuter en cas d'indication et de haut risque cardiovasculaire après balance individuelle ; essai SATURN en cours sur l'HIC lobaire [S6].
- **ENFT** : éviter l'anticoagulation ≈ 7–8 semaines (non fondé sur des essais) ; lévétiracétam ou topiramate possibles sans essai contrôlé ; rassurer : les accès ne traduisent généralement pas un nouveau saignement [S8].
- **Déclin cognitif lié à l'AAC** : suivi spécialisé avec bilan cognitivo-comportemental ; hygiène de vie [S3].

### 10.2 AAC-ri
- Corticothérapie empirique = traitement de choix, avec amélioration clinique et radiologique ; immunosuppression empirique défendue pour éviter la biopsie dans les formes probables [S12][S13].
- Schémas rapportés (série de cas, non recommandation) : dexaméthasone 4 mg/j 3 j ; 8 mg/j 15 j puis décroissance ; méthylprednisolone 1 g/j 5 j puis prednisone 80 mg/j en décroissance lente [S12].
- Amélioration spontanée possible dans les formes légères (3/7 sans immunothérapie) [S12].

### 10.3 AAC et immunothérapie anti-amyloïde (Kisunla®, donanemab) [S14]
- Indication suisse : trouble cognitif léger ou démence légère de type Alzheimer avec pathologie amyloïde prouvée, chez porteurs hétérozygotes ou non-porteurs d'APOE ε4.
- Contre-indications liées à l'AAC : HIC antérieure > 1 cm ; > 4 microhémorragies (≤ 1 cm en T2\*) ; sidérose superficielle ; ARIA-E ou images évoquant une AAC-ri ; > 2 infarctus lacunaires ou AVC de grand territoire ; Fazekas 3 ; AVC/AIT < 1 an ; HTA mal contrôlée ; anticoagulants ; thrombolyse ; plaquettes < 50 000 ou INR > 1,5 sans anticoagulant.
- Données : ARIA 33 % sous donanemab contre 13,5 % sous placebo (porteurs hétérozygotes et non-porteurs) ; ARIA-E 20,6 % ; ARIA-H 27,6 % ; HIC > 1 cm 0,4 % contre 0,3 % ; trois décès par ARIA graves (0,4 %) ; incidence d'ARIA : homozygotes ε4 55,9 %, hétérozygotes 37,6 %, non-porteurs 24,7 % ; récidive après reprise : ARIA-E 24,3 %, ARIA-H 35,9 %.
- Conduite : suspension jusqu'à résolution (ARIA-E) ou stabilisation (ARIA-H) ; arrêt définitif si ARIA-E cliniquement grave, ARIA-H grave, HIC > 1 cm ou récidives modérées à sévères ; corticoïdes possibles pour ARIA-E, efficacité non démontrée ; aspirine et antiagrégants concomitants admissibles ; génotypage APOE avant traitement.
- Lecanemab : aucune information professionnelle suisse trouvée (lacune).

### 10.4 Artérites infectieuses (I68.1)
**Neurosyphilis, y compris méningovasculaire**
- DGN S1 approuvée par la Société suisse de neurologie [S15] : **benzylpénicilline i.v.** 4 × 6 MUI/j, 5 × 5 MUI/j ou 3 × 10 MUI/j, **14 jours (au moins 10)** ; alternative **ceftriaxone 2 g i.v./24 h, 14 jours** ; doxycycline 2 × 200 mg/j 28 j envisageable (pas d'essai randomisé ; contre-indiquée en grossesse et avant 8 ans). Réaction de Jarisch-Herxheimer dans 1–2 % des neurosyphilis : AINS, sans interrompre l'antibiotique ; corticoïdes non recommandés en routine.
- IUSTI Europe 2020 [S16] : 1re ligne benzylpénicilline 18–24 MUI/j i.v. (3–4 MUI toutes les 4 h) 10–14 j (1, C) ; 2e ligne ceftriaxone 1–2 g i.v./j 10–14 j ou procaïne-pénicilline + probénécide (1, C) ; allergie : induction de tolérance puis 1re ligne (1, C).
- Information professionnelle suisse (Pénicilline « Grünenthal ») : infections graves (méningite) 20–60 MUI/j en 4–6 doses ; injection lente (≤ 0,5 MUI/min) au-delà de 2 MUI ; neurotoxicité dès 40–60 MUI/j (rein normal), 20 MUI/j (insuffisance rénale légère à modérée), 10 MUI/j (sévère) ; teneur en sodium (flacon 10 MUI : 386 mg) [S25].
- Suivi : LCR 3–6 mois après traitement puis tous les 6 mois jusqu'à normalisation des cellules (en général < 2 ans) ; échec à envisager si les cellules ne baissent pas en 6 mois [S15] ; LCR de contrôle 6 semaines–6 mois si anormal [S16].

**Méningite bactérienne / Listeria** (DGN S2k avec la Société suisse de neurologie) [S17]
- Empirique communautaire : ceftriaxone 2 × 2 g/j + **ampicilline 6 × 2 g/j** (couverture Listeria) ; Listeria : ampicilline, triméthoprime-sulfaméthoxazole ou méropénème ; traitement souvent ≥ 3 semaines.
- Dexaméthasone 10 mg i.v. 4×/j 4 jours si pneumocoque (recommandation 21, applicable à la Suisse), juste avant ou avec l'antibiotique (recommandation 22).
- Arrêt de la dexaméthasone en neurolistériose : déduction du dossier frère G01, non vérifiée ici (lacune).

**Méningite tuberculeuse** : corticoïdes + antituberculeux réduiraient mortalité et morbidité, mais leur effet sur les AVC n'est pas prouvé ; l'aspirine réduirait la mortalité, rôle sur les AVC à étudier [S18] (revue indienne, non recommandation européenne ; schémas suisses : voir dossier G01 et guide OFSP — lacune).

**Vasculopathie VZV** : aciclovir i.v. ± corticoïdes ± antiagrégant rapportés ; **niveau de preuve faible**, durée non standardisée (p. ex. 21 jours chez un immunodéprimé) [S19][S20][S21]. Information professionnelle suisse (Aciclovir Labatec® i.v.) : zona de l'immunodéprimé 10 mg/kg toutes les 8 h ≥ 5 jours ; encéphalite herpétique 10 mg/kg/8 h 10 jours ; réduction selon la clairance de la créatinine ; hydratation suffisante ; neurotoxicité et insuffisance rénale aiguë possibles [S24]. La vasculopathie VZV n'est pas une indication listée (usage hors indication — à signaler).

### 10.5 Lupus (I68.2) [S22][S23]
- Glucocorticoïdes et immunosuppresseurs si la manifestation reflète un processus inflammatoire ou une activité lupique généralisée ; **antiagrégant/anticoagulant** si la manifestation est liée aux antiphospholipides, en particulier la maladie cérébrovasculaire thrombotique [S22].
- Syndrome des antiphospholipides avec première thrombose artérielle : **AVK, INR 2–3 ou 3–4** selon le risque hémorragique/thrombotique ; **rivaroxaban à éviter en cas de triple positivité** ; récidive sous traitement adéquat : ajout d'aspirine, INR 3–4 ou HBPM [S23].

## 11. Suivi et pronostic

- HIC lobaire liée à l'AAC : récidive plus élevée que l'HIC liée à l'artériolosclérose [S9] ; voir chiffres d'Édimbourg (§ 7) [S10].
- ENFT : 24,5 % d'HIC symptomatique à 8 semaines (méta-analyse) ; HSA de convexité avec AAC probable : ≈ 19 %/an d'HIC ; dans une étude européenne, 50 % d'HIC lobaire symptomatique sur une médiane de 14 mois [S8].
- ARIA-E : résolution radiologique médiane ≈ 8,3 semaines ; symptômes résolus chez ≈ 80 % (médiane 3,9 semaines) ; ARIA-H persistent/se stabilisent [S14].
- Neurosyphilis : marqueurs tréponémiques (TPPA, FTA-ABS, ITpA) positifs à vie, inutiles au suivi ; VDRL du LCR baisse de 3–4 dilutions la première année ; normalisation plus lente si VIH [S15].

## 12. Situations particulières

- Trisomie 21 : AAC et ARIA plus fréquentes ; non étudiée sous donanemab [S14].
- AAC iatrogène chez le sujet âgé : difficile à distinguer de la forme sporadique [S11].
- VIH : CD4 < 200/µl et VZV récent comme facteurs de risque de vasculopathie VZV [S20] ; ponction lombaire discutée chez le séropositif avec syphilis tardive et CD4 ≤ 350/mm³ et/ou VDRL/RPR > 1:32 (2, D) [S16].
- Grossesse : doxycycline contre-indiquée [S15] ; donanemab contre-indiqué sans contraception adéquate [S14].
- Enfant : vasculopathie VZV post-varicelle (hémichorée rapportée) [S21].

## 13. Critères formels du diagnostic

**Critères de Boston version 2.0 (AAC)** [S4][S5]
- **AAC certaine** : autopsie cérébrale complète avec AAC sévère et vasculopathie, présentation compatible, absence d'autre lésion diagnostique.
- **AAC probable avec support anatomopathologique** : présentation compatible + AAC dans le tissu (hématome évacué ou biopsie corticale), absence d'autre lésion.
- **AAC probable** (≥ 50 ans, présentation compatible : HIC spontanée, ENFT, troubles cognitifs) : **≥ 2 lésions hémorragiques strictement lobaires** (HIC, microsaignements, foyers de SSc, HSA de convexité, en toute combinaison) **ou 1 lésion lobaire + 1 caractéristique de substance blanche** (espaces périvasculaires sévères du centre semi-ovale > 20 dans un hémisphère ; hypersignaux multispot > 10 points sous-corticaux bilatéraux).
- **AAC possible** : 1 lésion hémorragique strictement lobaire **ou** 1 caractéristique de substance blanche.
- Exclusions : toute lésion hémorragique profonde ; autre cause (voir § 8).
- Performance (autopsie) : sensibilité 74,5 % (IC 65,4–82,4), spécificité 95,0 % (IC 83,1–99,4), supérieure aux critères de Boston modifiés (sensibilité 64,5 %) [S4] ; performance bien moindre chez les asymptomatiques ou les seuls troubles cognitifs (sensibilité 28,6 %, spécificité 65,3 %) [S5].

**AAC-ri probable** : âge typiquement ≥ 40 ans ; début aigu/subaigu d'au moins un symptôme (céphalée, baisse de vigilance, trouble du comportement, déclin cognitif, crise, signe focal) ; hypersignaux FLAIR cortico-sous-corticaux (œdème vasogénique/effusion) ; ≥ 1 marqueur T2\*/SWI ; exclusion des causes néoplasiques, infectieuses et autres. **Certaine** : biopsie (inflammation vasculaire + amyloïde) [S12]. Formulation complète des critères Auriel 2016 non lue dans la source primaire (lacune).

**Neurosyphilis (DGN/SNG)** [S15] : **probable** = TPHA/TPPA et FTA-ABS sériques positifs + deux parmi (i) symptômes neuropsychiatriques subaigus/chroniques, (ii) LCR pathologique (pléiocytose, atteinte de barrière, réaction IgG intrathécale), (iii) réponse favorable au traitement ; **prouvée** = probable + production intrathécale d'anticorps (ITpA ou index TPHA) ; **confirmée** = prouvée + VDRL du LCR positif.

**Critères d'Édimbourg (scanner + APOE)** : voir § 7 [S9].

## 14. Paramètres clés (à retenir)

- HIC lobaire : AAC dans 50–57 % [S7].
- Boston 2.0 : ≥ 50 ans ; ≥ 2 lésions lobaires ou 1 + 1 marqueur de substance blanche ; EPV > 20 ; multispot > 10 [S5].
- Pression artérielle après HIC : ≤ 130/80 mmHg [S3][S6].
- OAC à éviter : AAC + SSc/HSA de convexité, ≥ 5 microsaignements lobaires [S6].
- ENFT : HIC 24,5 % à 8 semaines [S8].
- Donanemab : contre-indiqué si > 4 microhémorragies, SSc, HIC > 1 cm ; ARIA 33 % [S14].
- Neurosyphilis : benzylpénicilline i.v. 18–24 MUI/j, 10–14 j [S15][S16].
- Méningite bactérienne : complications vasculaires 15–40 % [S17] ; méningite tuberculeuse : AVC 15–57 % [S18].
- APS artériel : AVK INR 2–3 ou 3–4 ; pas de rivaroxaban si triple positivité [S23].

## 15. Médicaments — informations professionnelles suisses lues

| Médicament | Point utile | Source |
|---|---|---|
| Kisunla® (donanemab) | contre-indications AAC/ARIA, IRM de surveillance, conduite en cas d'ARIA | [S14] (juillet 2025) |
| Aciclovir Labatec® i.v. | 10 mg/kg/8 h ; ajustement rénal ; hydratation | [S24] (déc. 2025) |
| Pénicilline « Grünenthal » (benzylpénicilline) | 20–60 MUI/j dans les infections graves ; neurotoxicité ; vitesse d'injection | [S25] (mai 2023) |

## 16. Pareto (proposition pédagogique)

1. AAC = première cause d'HIC lobaire du sujet âgé ; IRM T2\*/SWI ; Boston 2.0.
2. ENFT ≠ AIT : pas d'antithrombotique réflexe.
3. AAC → décisions antithrombotiques et éligibilité aux anti-amyloïdes.
4. AVC du sujet jeune sans facteur de risque + sérologie syphilis → ponction lombaire et pénicilline i.v.
5. Méningite : 15–40 % de complications vasculaires ; couvrir Listeria.

## 17. Lacunes explicites

1. **Aucune recommandation suisse spécifique** (Société cérébrovasculaire suisse, SNG) sur l'AAC trouvée ; la source suisse principale est une revue de la Revue Médicale Suisse 2023 [S3]. L'article RMS « Angiopathie amyloïde cérébrale inflammatoire et immunothérapies anti-amyloïde » (Bugnon et al.) a été repéré mais **non lu** (accès réservé).
2. **Aucune recommandation ESO spécifique de l'AAC** lue ; seule la recommandation ESO/EANS 2025 sur l'HIC (sections prévention secondaire) a été lue ; ses sections diagnostiques (IRM, critères) n'ont pas été lues (texte tronqué).
3. Texte original des critères de Boston 2.0 lu en **résumé** [S4] et via une source secondaire (Radiopaedia) [S5] ; tableau original non lu.
4. Critères AAC-ri (Auriel 2016) : lus seulement via une série de cas italienne [S12] ; aucune recommandation thérapeutique formelle.
5. AAC héréditaire (type néerlandais, autres mutations) : aucune source lue.
6. Sous-code E85 adapté à l'AAC : non précisé par la classification lue ; règles de double codage I61/I63 + I68 non vérifiées.
7. I68.8 : aucune inclusion dans la version GM ; « apoplexie urémique » uniquement dans la CIM-10 OMS [S2] ; aucune source clinique lue sur cette entité.
8. Vasculopathie VZV : seulement des cas cliniques/revues de cas (niveau faible) ; aucune recommandation européenne ; rattachement à I68.1 non explicite ; indication hors information professionnelle.
9. Syphilis méningovasculaire : histopathologie (endartérite) et imagerie spécifique non décrites dans les sources lues ; la DGN S1 [S15] est échue (validité jusqu'au 30.04.2025) ; le projet IUSTI 2026 n'a pas été lu.
10. Listeria : ESCMID 2016 inaccessible (HTTP 403) ; ampicilline sans information professionnelle suisse vérifiée ici.
11. Méningite tuberculeuse : schémas thérapeutiques suisses (OFSP) non relus ici ; la source vasculaire [S18] est une revue indienne de 2011 (résumé).
12. Lupus : recommandations EULAR NPSLE 2010 lues en résumé [S22] ; mise à jour EULAR 2023 non lue.
13. Lecanemab : absent d'AmiKo lors de la consultation ; statut suisse non vérifié.
14. Épidémiologie suisse propre (incidence de l'AAC, des artérites infectieuses) : non trouvée.
