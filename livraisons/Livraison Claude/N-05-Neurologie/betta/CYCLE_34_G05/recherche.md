# G05 — Encéphalite, myélite et encéphalomyélite au cours d'affections classées ailleurs (N-05-Neurologie)

Dossier de recherche du cycle Betta 34, leçon 2 (agent C34-A1-NEUR, recherche Opus 5.5). Consultation : 15.10.2026.
Chaque fait porte l'identifiant `[Sx]` détaillé dans `sources.json`. Rien n'a été ajouté de mémoire. Ce qui n'a pas été lu figure sous « Lacunes ».

## 0. Question clinique et logique de codage (CIM-10-GM 2024)

G05.-* est une **catégorie astérisque** : elle code la *manifestation* encéphalitique, myélitique ou encéphalomyélitique d'une maladie dont le code primaire (†) se trouve dans un autre chapitre. Le code astérisque ne s'emploie jamais seul [S1]. La catégorie inclut aussi la méningo-encéphalite et la méningomyélite au cours d'affections classées ailleurs [S1].

| Sous-code | Intitulé (OFS) [S2] | Codes primaires † cités par la BfArM [S1] |
|---|---|---|
| G05.0* | … au cours d'infections bactériennes classées ailleurs | Listeria A32.1† ; méningocoque A39.8† ; syphilis congénitale A50.4† ; syphilis tardive A52.1† ; tuberculose A17.8† |
| G05.1* | … au cours d'infections virales classées ailleurs | entérovirus A85.0† ; adénovirus A85.1† ; grippe J09†, J10.8†, J11.8† ; herpès simplex B00.4† ; rougeole B05.0† ; oreillons B26.2† ; rubéole B06.0† ; varicelle B01.1† ; zona B02.0† ; cytomégalovirus B25.88† |
| G05.2* | … au cours d'autres maladies infectieuses et parasitaires classées ailleurs | trypanosomiase africaine B56.-† ; maladie de Chagas chronique B57.4† ; Naegleria B60.2† ; toxoplasmose B58.2† ; méningo-encéphalite à éosinophiles B83.2† |
| G05.8* | … au cours d'autres maladies classées ailleurs | encéphalopathie du lupus érythémateux systémique M32.1† |

**Pièges de codage, tous lus :**
- L'**encéphalite à tiques** (FSME, A84 / A84.1) ne porte **ni †, ni lien vers G05.1*** ; elle se code directement en A84 [S3]. Il en va de même pour l'encéphalite virale sans précision (A86) [S3].
- G04 exclut l'encéphalopathie alcoolique (G31.2), toxique (G92.-) ou sans précision (G93.4), la sclérose en plaques (G35.-), l'encéphalomyélite myalgique (G93.3), la myélite transverse aiguë (G37.3) et le syndrome de Foix-Alajouanine (G37.4) [S1].
- G09 code les **séquelles** des affections inflammatoires de G00–G08, **à l'exclusion des catégories astérisque** ; la séquelle se définit comme un état persistant **un an ou plus** après le début de la maladie causale [S1].

**Question d'examen :** devant une encéphalite, l'enjeu n'est pas le code mais l'**agent causal traitable** : HSV et VZV (aciclovir), Listeria (amoxicilline/ampicilline), neurosyphilis (pénicilline G), toxoplasmose (pyriméthamine-sulfadiazine), CMV (ganciclovir) [S4][S7][S10][S12].

## 1. Définition et critères

- Critères cliniques du consortium international de l'encéphalite (Venkatesan 2013), **repris par la ligne directrice DGN/SNG** [S4, tab. 2] :
  - critère majeur : baisse de vigilance, modification de la personnalité ou manifestation psychiatrique **> 24 h** sans autre cause ; aucune diagnostic alternatif ;
  - critères mineurs : fièvre ≥ 38 °C dans les 72 h avant/après la présentation ; crises épileptiques non expliquées par une épilepsie connue ; nouveaux signes focaux ; leucocytes du LCR ≥ 5/mm³ ; imagerie nouvelle évocatrice ; EEG anormal compatible sans autre cause [S4].
  - Lacune : le nombre de critères mineurs requis (possible/probable) n'est pas indiqué dans le tableau lu → à ne pas inventer.
- **Méningite virale** vs **méningo-encéphalite** : la méningite associe céphalées, nausées, raideur de nuque, photo- et phonophobie, **sans signe focal ni trouble de conscience**, LCR < 1000 cellules/µl, protéines et lactate peu ou pas augmentés ; résolution spontanée en jours à semaines [S4, §1.2]. L'encéphalite associe des troubles quantitatifs et qualitatifs de la conscience, souvent (non obligatoirement) des signes focaux (parésies, aphasie, crises) ; le méningisme peut manquer [S4, §1.2].
- Prodromes : la (méningo-)encéphalite suit souvent une maladie générale (rubéole, rougeole, oreillons, varicelle, exanthème subit) ou un stade prodromique (HSV, FSME, entérovirus) [S4, §1.2].

## 2. Épidémiologie

- Danemark 2015–2023 (cohorte prospective nationale, adultes, critères du consortium) : incidence **1,18/100 000/an** ; âge médian 70 ans ; étiologies : **VZV 32 %**, **HSV-1 31 %**, FSME 5 %, autres virus 8 %, **inconnue 24 %** [S5].
- Présentation : confusion 80 %, céphalées 59 %, changement de personnalité 42 % ; admission aux soins intensifs 22 % ; mortalité 8 % à 30 jours, **15 % à 6 mois** [S5].
- Facteurs de mortalité à 6 mois : immunodépression (RR ajusté 2,91), encéphalite HSV-1 (2,34), GCS < 12 (2,03) [S5].
- Zones tempérées : incidence des encéphalites virales estimée 3,5–7,5/100 000 [S4, §1.3]. Encéphalite herpétique : **1–3 par million**, encéphalite sporadique la plus fréquente d'Europe occidentale ; 1/3 des cas avant 20 ans, la moitié après 50 ans ; pas de saisonnalité [S4, §1.3, §3.2.1].
- Enfants et jeunes adultes : les encéphalites auto-immunes (anti-NMDAR) représentent environ 20–30 % des cas [S4, §1.1].
- Rougeole : encéphalite chez environ **1 cas sur 1000** [S15]. Varicelle : manifestations du SNC chez environ 0,1 % [S4, §3.2.2].
- Listériose en Suisse : jusqu'à 100 cas déclarés par an, létalité jusqu'à 20 % ; groupes à risque : immunodéprimés, femmes enceintes, nouveau-nés, personnes âgées [S9].
- Neurolistériose (France, MONALISA) : méningo-encéphalite chez 84 % des 252 neurolistérioses ; **atteinte du tronc cérébral dans 17 %** seulement [S8].
- FSME : maladie à déclaration obligatoire en Suisse ; tous les cantons sauf le Tessin sont zones à risque ; incidence en hausse ces dernières années [S14]. 245 cas en Suisse en 2023 selon la ligne directrice DGN [S4, §1.3].

## 3. Mécanismes (du normal au pathologique)

- **Lésion directe et lésion immunitaire** : à côté des dommages directs par l'agent, surviennent des pathologies secondaires immunologiques (vascularites, encéphalites auto-immunes) [S4, §1.1].
- **HSV → anti-NMDAR** : l'encéphalite herpétique peut déclencher une encéphalite à anticorps anti-récepteur NMDA, des semaines à des mois après l'infection ; à évoquer devant des symptômes nouveaux ou progressifs malgré l'aciclovir ; l'immunothérapie est indiquée si l'auto-immunité est confirmée ou probable [S4, §1.1]. Jusqu'à 25 % de cours récurrents après HSVE, par réactivation virale ou par mécanisme immun [S4, §3.2.1].
- **Myélite transverse aiguë** : plus souvent immuno-médiée que directement infectieuse (grippe, mycoplasme, adénovirus) [S4, §1.1].
- **Topographie** : HSVE = lésions temporales médio-basales, s'étendant vers le frontobasal et le cingulaire ; arbovirus (FSME, encéphalite japonaise) = atteinte asymétrique des noyaux gris centraux [S4, §2, §3.2.1]. HSV-1 donne chez l'adulte une encéphalite nécrosante focale ; HSV-2 donne chez l'adulte plutôt une méningite bénigne, mais chez le nouveau-né une encéphalite hémorragique nécrosante diffuse [S4, §3.2.1].
- **Immunodépression** : EBV et CMV encéphalitiques augmentent chez les patients sida, transplantés et sous chimiothérapie [S4, §1.3] ; l'encéphalite zostérienne touche préférentiellement leucémies, lymphomes et autres immunodéficits [S4, §3.2.2].
- **Infections lentes** : panencéphalite sclérosante subaiguë (PESS, rougeole) et panencéphalite rubéoleuse progressive : incubation de mois à années, évolution progressive généralement mortelle [S4, §3.2.7].
- **Lupus** : les manifestations neuropsychiatriques du lupus (G05.8 pour l'encéphalopathie) relèvent soit d'un processus inflammatoire, soit d'un mécanisme lié aux anticorps antiphospholipides (thrombotique) ; cette distinction oriente le traitement [S13].

## 4. Causes principales par sous-code (ce qui est lu)

### G05.1* — virales
- **HSV-1 (B00.4†)** : évolution biphasique : stade grippal (céphalées, forte fièvre), amélioration brève, puis troubles de conscience, fièvre et signes focaux facultatifs ; non traitée, létale dans ≥ 70 % ; sous traitement 20–30 % [S4, §1.1, §3.2.1]. Le herpès labial récidivant n'accroît pas le risque [S4, §3.2.1]. Cohorte française 2015–2022 : mortalité 16,5 % (20,8 % chez les patients de soins intensifs), réhospitalisation 10,1 % à 6 mois [S4, §1.1].
- **VZV (B01.1†, B02.0†)** : deuxième cause infectieuse dans les pays industrialisés [S4, §3.2.2] ; première cause dans la cohorte danoise [S5]. Encéphalite varicelleuse 4–8 jours après l'éruption, syndrome cérébelleux dans la moitié des cas ; encéphalite zostérienne quelques jours à semaines après les vésicules, le plus souvent céphaliques ; tableau proche de l'HSVE, moins rapide et généralement moins sévère ; séquelles et décès non rares [S4, §3.2.2].
- **CMV (B25.88†)** : presque exclusivement chez l'immunodéprimé (sida : encéphalite, choriorétinite) ; LCR parfois à prédominance granulocytaire ; diagnostic par PCR du LCR [S4, §3.2.3].
- **EBV** : surtout chez l'immunodéprimé (transplanté) ; fièvre, confusion, nausées, vomissements, trouble de vigilance ; PCR LCR avec risque de faux positifs en cas de pléiocytose [S4, §3.2.4]. (EBV n'est pas cité parmi les inclusions BfArM de G05.1 ; rattachement de codage à confirmer — lacune.)
- **Rougeole (B05.0†), oreillons (B26.2†), rubéole (B06.0†)** : prévenues par la vaccination ; la vaccination antiourlienne a fait nettement reculer la méningo-encéphalite ourlienne [S4, §1.3, §3.1]. Vaccin ROR (préférence ROR-V depuis 2023) : 2 doses à 9 et 12 mois ; rattrapage à tout âge chez la personne non immune [S15].
- **Entérovirus (A85.0†), adénovirus (A85.1†), grippe (J09–J11†)** : pas de traitement antiviral spécifique validé pour l'encéphalite à entérovirus ; pour la grippe, seuls les inhibiteurs de la neuraminidase sont cliniquement actifs, sans étude contrôlée dans les méningo-encéphalites [S4, Was gibt es Neues].

### G05.0* — bactériennes
- **Listeria (A32.1†)** : fréquence nettement plus élevée chez les sujets âgés, les patients atteints de cancer et sous immunosuppression [S7]. Hémocultures indispensables : 35 des 252 neurolistérioses identifiées uniquement par hémoculture [S7]. Antibiotiques sur germe identifié : ampicilline, triméthoprime-sulfaméthoxazole ou méropénème, association avec fosfomycine ou rifampicine possible ; traitement souvent ≥ 3 semaines [S7, tab. 4]. Ampicilline 6 × 2 g/j [S7, tab. 5]. Amoxicilline i.v. suisse : 2 g en perfusion courte 3 à 6 fois/j, maximum 12 g/j ; L. monocytogenes figure dans le spectre ; diffusion faible dans le LCR sans inflammation méningée [S18].
- **Méningocoque (A39.8†)** : rattachement de codage seulement [S1] ; prise en charge dans G01/A39 (cycle 33).
- **Syphilis (A52.1†, A50.4†)** : la paralysie générale est une **encéphalite chronique progressive** (troubles cognitifs, du jugement, épisodes psychotiques, troubles de la parole, anomalies pupillaires, tremblement lingual et facial, crises, puis démence sévère) [S10]. Des formes récentes simulent une encéphalite temporale herpétique ou limbique [S10]. La neurosyphilis méningovasculaire est aujourd'hui l'une des manifestations les plus fréquentes ; y penser devant un AVC du sujet jeune sans facteur de risque [S10]. Épidémie européenne de syphilis précoce, surtout chez les HSH [S11].
- **Tuberculose (A17.8†)** : rattachement de codage seulement [S1] ; renvoi au cycle 33 (G01).

### G05.2* — parasitaires
- **Toxoplasmose (B58.2†)** chez la personne vivant avec le VIH : diagnostic présomptif standard = symptômes, IgG anti-toxoplasme sériques, lésions focales typiques à l'imagerie **et réponse au traitement empirique** ; diagnostic définitif par mise en évidence tissulaire ; PCR toxoplasme du LCR spécifique (95–100 %) mais peu sensible (50 %) [S12].
- Trypanosomiase, Chagas, Naegleria, méningo-encéphalite à éosinophiles : codage seulement [S1] ; aucune source clinique lue (lacune).

### G05.8* — autres
- **Lupus (M32.1†)** : le bilan d'une manifestation neuropsychiatrique suspecte est le même que hors lupus et vise d'abord à exclure une autre cause ; la ponction lombaire sert à exclure une infection du SNC ; IRM (T1/T2, FLAIR, diffusion, T1 injecté), EEG, tests neuropsychologiques [S13]. Facteurs de risque forts : antécédent de lupus neuropsychiatrique sévère, anticorps antiphospholipides [S13].

## 5. Anamnèse (orientation étiologique)

À rechercher [S4, §2] : cas dans l'entourage (oreillons, varicelle, polio) ; piqûre de tique (FSME), d'insecte (arbovirus), morsure animale (rage) ; appartenance à un groupe à risque VIH ; transfusion, transplantation (VIH, CMV, parvovirus B19) ; immunosuppression (CMV, JCV, VZV, HHV-6, EBV, HSV ; entérovirus 71 sous anti-CD20) ; voyages (rage, dengue ; Italie : virus Toscana ; Méditerranée : virus du Nil occidental ; Asie du Sud-Est : encéphalite japonaise, Nipah). Ajouter : alimentation à risque de Listeria (lait cru, fromages, charcuterie, poisson, salades emballées) [S9] ; exposition sexuelle (syphilis) [S10] ; vésicules cutanées (VZV) [S4].

## 6. Examens

- **Sang** : lymphocytose relative ; **procalcitonine normale (< 0,5 ng/ml)** dans l'infection virale, élevée dans l'infection bactérienne aiguë ; CRP rarement > 50 mg/l dans les viroses du SNC [S4, §2]. Au moins **2 paires d'hémocultures** avant antibiotique si l'origine bactérienne est possible [S7, recommandation 6].
- **LCR viral** : pléiocytose mixte les 4–48 premières heures (25–1000/µl), puis lymphocytaire ; protéines et lactate normaux ou peu élevés (encéphalite virale : lactate **≤ 4,0 mmol/l**) ; synthèse intrathécale spécifique (indice d'anticorps > 1,5) après > 10 jours pour HSV, VZV, CMV, FSME [S4, §2]. Formule de l'indice d'anticorps (Reiber) : (Ac LCR × IgG sérum) / (IgG LCR × Ac sérum) [S4, §2].
- **LCR HSVE** : 5–350 cellules/µl, **normal initialement dans 5 %** ; protéines modérément à nettement augmentées ; lactate max. 4,0 mmol/l ; PCR HSV : sensibilité 95–100 % les premiers jours, peut se négativer ensuite ; synthèse intrathécale dès la fin de la 2e semaine [S4, §3.2.1].
- **LCR bactérien** : > 1000 cellules/µl à granulocytes, protéines > 100 mg/dl, glucose LCR/sérum abaissé, lactate > 3,5 mmol/l ; un tiers des méningites bactériennes ont < 1000 cellules/µl [S7, tab. 1].
- **Ordre de recherche virale** (paliers) : 1) virus traitables : HSV-1/2, VZV, CMV (PCR ADN), VIH (PCR ARN, sérologie) ; 2) EBV, entérovirus ; 3) FSME (sérologie sang + LCR, indice d'anticorps ; PCR précoce), adénovirus, HHV-6, grippe, rougeole, rubéole, JCV ; 4) situations spéciales (rage, polio, HTLV-1, LCMV, hantavirus, voyage) [S4, tab. 3]. Panels PCR multiplex et séquençage de nouvelle génération (NGS) si l'étiologie reste inconnue après le bilan standard [S4, §2].
- **IRM = examen de choix** ; le scanner n'est qu'un substitut (contre-indication, complications) et reste souvent normal les **4 premiers jours** de l'HSVE ; une IRM normale rend l'HSVE peu probable [S4, §2, §3.2.1].
- **EEG** : ralentissement généralisé et **décharges épileptiformes latéralisées périodiques (PLED)** dans l'HSVE ; complexes de Radermecker dans la PESS ; « extreme delta brush » dans l'encéphalite anti-NMDAR [S4, §2].
- **Neurosyphilis** : sérologie tréponémique sérique (TPPA/TPHA/TPLA, confirmation FTA-ABS ou ELISA) puis LCR : cellules, protéines, lactate, profil de Reiber, indice d'anticorps anti-tréponème (ITpA) ; VDRL du LCR très spécifique mais sensibilité 30–85,7 % ; PCR LCR non recommandée [S10].
- **Biopsie cérébrale** : utile devant une lésion focale IRM, surtout prenant le contraste ou chez l'immunodéprimé [S4, §1.1].

## 7. Diagnostic différentiel

- **Méningite bactérienne** : tant qu'elle n'est pas exclue, ajouter un antibiotique (céphalosporine de 3e génération + ampicilline, à cause de Listeria) [S4, §3.1] ; procalcitonine sérique et lactate du LCR aident à séparer viral et bactérien [S4, Was gibt es Neues].
- **Encéphalite auto-immune** (G04.8, hors G05) : à évoquer si aucun agent n'est trouvé. Critères Graus 2016 de l'encéphalite auto-immune « possible », tous trois requis : 1) troubles de la mémoire à court terme, symptômes psychiatriques ou altération de conscience d'installation subaiguë (< 3 mois) ; 2) au moins un : nouveaux signes focaux, pléiocytose > 5/mm³, crises inexpliquées, IRM évocatrice ; 3) exclusion raisonnable des autres causes [S4, §2].
- **ADEM** et **myélite transverse aiguë (G37.3)** : processus immunitaires post- ou para-infectieux [S4, §1.1, §2][S1].
- Encéphalopathies toxiques, métaboliques (G92, G93.4) [S1] ; encéphalopathie à l'aciclovir chez l'insuffisant rénal ou le sujet âgé [S16].

## 8. Urgences et conduite initiale

- **Aciclovir i.v. immédiat dès la suspicion clinique d'HSVE, sans attendre la PCR** ; en cas d'hypertension intracrânienne ou d'autre contre-indication à la ponction, commencer sans analyse du LCR [S4, Empfehlungen, §3.2.1]. Un retard (début > 24 h après l'admission) est associé à une létalité accrue [S4, §3.2.1].
- Ajouter l'antibiothérapie si une origine bactérienne reste possible [S4, §3.1]. À l'inverse, toute méningite bactérienne suspecte reçoit de l'aciclovir tant qu'une HSVE reste plausible [S7, recommandation 18].
- **Scanner avant ponction lombaire** seulement en cas de trouble sévère de la conscience, de déficit focal nouveau ou de crise récente ; dans ces cas, débuter dexaméthasone et antibiotiques **après les hémocultures, sans attendre l'imagerie** [S7, recommandations 15–17]. Antibiotique si possible dans l'heure, jamais au-delà de 3 h [S7, recommandation 14].
- **Soins intensifs** recommandés pour l'encéphalite virale aiguë [S4, Empfehlungen].
- Mesures générales : traitement de l'œdème cérébral (osmothérapie ; bénéfice de la craniectomie non établi) ; antiépileptique seulement en cas de crise ou d'état de mal ; neuroleptiques (halopéridol, melpérone, olanzapine) avec prudence car ils abaissent le seuil épileptogène ; thromboprophylaxie ; correction d'une perte de sel ou d'un diabète insipide ; nutrition et gestion thermique [S4, §3.1].

## 9. Prise en charge spécifique

| Agent | Traitement | Durée | Source |
|---|---|---|---|
| HSV | aciclovir i.v. 10 mg/kg toutes les 8 h, hydratation, adaptation rénale | DGN : **≥ 14 j** ; FI suisse : **10 j** (≥ 3 mois d'âge) | [S4][S16] |
| HSV, PCR négative mais suspicion persistante sans autre cause | aciclovir | ≥ 10 j | [S4] |
| HSV résistant (sida, transplanté) | foscarnet 60 mg/kg i.v. en 1 h toutes les 8 h | 3 semaines | [S4] |
| VZV (varicelle, zona) | aciclovir i.v. même dose ; foscarnet si échec | non précisée | [S4] |
| CMV | ganciclovir 5 mg/kg/12 h i.v. + foscarnet (60 mg/kg/8 h ou 90 mg/kg/12 h) en phase initiale | 3 semaines, puis ganciclovir seul 3 sem. (immunocompétent) ou 6 sem. (immunodéprimé) ; entretien si sida | [S4] |
| Listeria | ampicilline 6 × 2 g/j (amoxicilline i.v. 2 g × 3–6/j, max. 12 g) ; alternatives TMP-SMX, méropénème | souvent ≥ 3 semaines | [S7][S18] |
| Neurosyphilis | pénicilline G i.v. 4 × 6, 5 × 5 ou 3 × 10 MUI/j ; alternative ceftriaxone 2 g/j ; doxycycline 2 × 200 mg 28 j envisageable | 14 j (au moins 10) | [S10] |
| Toxoplasmose (VIH) | pyriméthamine 200 mg J1 puis 75 mg/j (≥ 60 kg) ou 50 mg/j (< 60 kg) + sulfadiazine 3000 mg 2×/j (≥ 60 kg) ou 2000 mg 2×/j + acide folinique 10–15 mg/j ; ou TMP-SMX 5/25 mg/kg 2×/j | 6 semaines puis prophylaxie secondaire | [S12] |
| Lupus neuropsychiatrique inflammatoire | glucocorticoïdes et immunosuppresseurs ; antiagrégant/anticoagulant si mécanisme antiphospholipide thrombotique | — | [S13] |

Précisions pharmacologiques :
- **Aciclovir (FI suisse)** : élimination rénale par filtration et sécrétion tubulaire ; dose espacée à 12 h si clairance 25–50 ml/min, 24 h si 10–25 ml/min, demi-dose/24 h si < 10 ml/min ou hémodialyse ; surveiller la fonction rénale à forte dose (encéphalite), surtout en cas de déshydratation ; insuffisance rénale aiguë très rare, réversible avec réhydratation ; effets neurologiques très rares (confusion, hallucinations, convulsions, encéphalopathie, coma), surtout chez l'insuffisant rénal ou âgé ; prudence avec ciclosporine et tacrolimus [S16].
- **Contentieux de durée (HSVE)** : la FI suisse (déc. 2025) indique 10 jours ; la ligne directrice DGN/SNG (janv. 2025) recommande au moins 14 jours. Source primaire la plus récente : FI (déc. 2025) pour l'autorisation ; la ligne directrice traduit la pratique d'experts. À présenter comme contentieux (mot vert) [S4][S16].
- **Corticoïdes dans l'HSVE** : bénéfice non démontré ; essai GACHE arrêté faute de recrutement ; association aciclovir-dexaméthasone = décision individuelle, hors indication ; résultats de DexEnceph non publiés selon la ligne directrice [S4, §3.2.1]. Valaciclovir oral 90 jours après l'aciclovir i.v. : pas de meilleur résultat cognitif (Gnann 2015) [S4, §3.2.1].
- **Dexaméthasone et Listeria** : la ligne directrice germanophone (valable pour l'Allemagne, l'Autriche et la Suisse) recommande la dexaméthasone 10 mg i.v. 4×/j en cas de suspicion de méningite bactérienne communautaire, poursuivie 4 jours si pneumocoque [S7, recommandation 21] ; MONALISA observe une mortalité plus élevée des neurolistérioses sous dexaméthasone adjuvante (OR 4,58), donnée observationnelle [S8]. Contentieux à signaler sans trancher au-delà des sources.
- **Ganciclovir (FI suisse)** : 5 mg/kg en 1 h toutes les 12 h pendant 14–21 jours chez l'adulte à fonction rénale normale ; contre-indiqué si neutrophiles < 500/µl ou plaquettes < 25 000/µl ; neutropénie < 1000/mm³ chez 38 % ; potentiellement tératogène et cancérogène ; adaptation rénale [S17].
- **Brivudine** : contre-indication absolue avec 5-fluorouracile, capécitabine, tégafur, flucytosine (toxicité potentiellement mortelle jusqu'à 4 semaines après) [S4, §3.2.2]. FI suisse non lue (lacune).
- **Jarisch-Herxheimer** (neurosyphilis) : 1–2 %, 12–24 h après le début ; traitement symptomatique par AINS, ne pas interrompre l'antibiotique ; corticoïdes de routine non recommandés [S10].
- **Sulfadiazine** : cristallurie, insuffisance rénale, lithiase → hydratation, surveillance rénale et du sédiment ; pyriméthamine myélotoxique ; dexaméthasone seulement si effet de masse, à arrêter dès que possible [S12].

## 10. Prévention et santé publique

- Vaccination ROR(V) en Suisse : 2 doses à 9 et 12 mois [S15].
- FSME : vaccination recommandée à tous les adultes et enfants dès 3 ans vivant en zone à risque (toute la Suisse sauf le Tessin) ; à discuter individuellement à 1–2 ans [S14]. Immunisation passive non indiquée pour la FSME [S4, §3.1].
- Listeria : hygiène de cuisine, dates et températures de conservation, éviter crudités, viande ou poisson crus, fromages à pâte molle et au lait cru chez les personnes à risque [S9].
- Toxoplasmose (VIH) : prophylaxie primaire si CD4 < 200/µl (ou < 14 %), par TMP-SMX ; arrêt si CD4 > 100/µl et charge virale indétectable 3 mois ; prophylaxie secondaire jusqu'à CD4 > 200/µl et charge indétectable 6 mois [S12].

## 11. Suivi et pronostic

- Mortalité 15 % à 6 mois toutes encéphalites infectieuses confondues (Danemark) [S5] ; HSVE 20–30 % sous traitement [S4].
- Après HSVE : surveiller une rechute (jusqu'à 25 %) et l'encéphalite anti-NMDAR secondaire [S4, §3.2.1].
- Neurosyphilis : contrôle clinique et du LCR 3–6 mois après, puis tous les 6 mois jusqu'à normalisation des cellules (habituellement < 2 ans) ; baisse du VDRL du LCR ; TPPA, FTA-ABS et ITpA restent positifs à vie et ne servent pas au suivi ; séquelles chez 41,8 % [S10].
- Séquelles persistant ≥ 1 an : codage G09 ne s'applique pas aux catégories astérisque [S1].

## 12. Situations particulières

- **Immunodéprimé** : CMV, EBV, VZV, JCV, HHV-6 ; HSV résistant à l'aciclovir ; toxoplasmose ; Listeria [S4][S7][S12].
- **Nouveau-né** : HSV-2 = encéphalite diffuse hémorragique nécrosante ; aciclovir 14–21 jours selon la FI [S4][S16].
- **Grossesse** : Listeria → fausse couche ; transmission materno-fœtale [S9]. Tétracyclines contre-indiquées (alternative doxycycline de la neurosyphilis exclue) [S10].
- **Enfant** : PESS chez l'enfant non ou tardivement vacciné contre la rougeole ; myoclonies, complexes de Radermecker, indice d'anticorps antirougeoleux > 1,5 ; évolution mortelle [S4, §3.2.7].
- **Sujet âgé / insuffisant rénal** : adaptation de l'aciclovir et risque neurotoxique [S16].

## 13. Critères formels (pour l'îlot `div.alert`)

1. Encéphalite (consortium international, repris DGN/SNG) : critère majeur = altération de conscience/personnalité/psychiatrique > 24 h sans autre cause ; mineurs : fièvre ≥ 38 °C (± 72 h), crises inexpliquées, signes focaux nouveaux, LCR ≥ 5 leucocytes/mm³, imagerie nouvelle, EEG compatible [S4].
2. Encéphalite auto-immune possible (Graus 2016) : 3 critères cumulatifs (voir §7) [S4].
3. Neurosyphilis probable (critères germanophones) : toujours sérologie tréponémique sérique positive + deux parmi : symptômes neuropsychiatriques subaigus/chroniques ; pléiocytose ou atteinte de la barrière sang-LCR ; effet favorable du traitement ; certaine si synthèse intrathécale d'anticorps antitréponème [S10].
4. Toxoplasmose cérébrale présomptive : symptômes + IgG sériques + lésions focales typiques + réponse au traitement empirique [S12].
5. Codage : G05.x* jamais seul, toujours avec le code † de la maladie causale ; FSME = A84 sans G05 [S1][S3].

## 14. Paramètres clés (pour l'îlot `div.key`)

- Incidence des encéphalites infectieuses de l'adulte : 1,18/100 000/an (Danemark) ; VZV 32 %, HSV-1 31 %, inconnue 24 % [S5].
- HSVE : 1–3/million/an ; létalité ≥ 70 % non traitée, 20–30 % traitée [S4].
- Aciclovir 10 mg/kg/8 h i.v. ; 10 j (FI) vs ≥ 14 j (DGN) [S16][S4].
- PCR HSV LCR : sensibilité 95–100 % précoce ; LCR normal initialement 5 % [S4].
- Lactate LCR encéphalite virale ≤ 4,0 mmol/l ; PCT < 0,5 ng/ml [S4].
- Scanner normal jusqu'à J4 dans l'HSVE ; IRM normale → HSVE peu probable [S4].
- Neurolistériose : tronc cérébral 17 % ; traitement ≥ 3 semaines ; ampicilline 6 × 2 g/j [S8][S7].
- Neurosyphilis : pénicilline G i.v. 14 j (≥ 10 j) [S10].
- Toxoplasmose : 6 semaines ; PCR LCR sensibilité 50 % [S12].
- Encéphalite rougeoleuse ≈ 1/1000 rougeoles [S15].

## Lacunes explicites

- **Aucune source suisse spécifique à l'encéphalite** (Swiss Medical Forum, SSI) trouvée ; la ligne directrice DGN 2025 inclut toutefois un représentant de la Société suisse de neurologie et déclare « aucune particularité pour la Suisse » [S4] ; la ligne directrice neurosyphilis est approuvée par la SNG [S10].
- Ligne directrice ESCMID 2016 (méningite bactérienne) : page éditeur inaccessible (403), non lue.
- Ligne directrice européenne de l'encéphalite (EAN/EFNS 2010, Steiner) et ligne directrice EAN FSME (Taba 2017) citées par S4 mais non lues directement.
- Texte intégral de l'IUSTI 2020 (syphilis) non lu ; seuls le résumé et la ligne directrice germanophone ont été lus.
- Nombre de critères mineurs (consortium) pour encéphalite possible/probable : non lu.
- Chiffres suisses annuels FSME : 245 cas (2023) selon S4 ; page OFSP sans chiffres ; tableau de l'Université de Vienne vu seulement en résultat de recherche (non retenu).
- Aucune FI suisse lue pour : foscarnet, brivudine, pyriméthamine, sulfadiazine, pénicilline G, ceftriaxone (voir dossiers G01/G03 pour les deux dernières).
- Trypanosomiase, Chagas, Naegleria, méningo-encéphalite à éosinophiles, tuberculose : codage seulement, pas de source clinique lue pour cette leçon.
- Rattachement de l'encéphalite à EBV (non listée dans les inclusions BfArM de G05.1) : à confirmer.
- PESS : fréquence suisse non lue.
