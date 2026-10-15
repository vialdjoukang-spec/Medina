# I66 — Occlusion et sténose des artères cérébrales, n'entraînant pas un infarctus cérébral (N-05-Neurologie)

Dossier de recherche, cycle Betta 32, leçon 2, agent C32-A1-NEUR (Opus 5.5), 14.10.2026.
Chaque fait est suivi de sa source (S1–S29, voir `sources.json`). Rien n'est écrit de mémoire. Les éléments non trouvés ou non lus figurent au § 17 (lacunes). Plusieurs sources n'ont été lues qu'en **résumé** (indiqué dans `sources.json`, champ `limites`) ; le rédacteur ne doit pas en extraire davantage que ce qui est écrit ici.

---

## 0. Question clinique et angle pédagogique

I66 code une sténose ou une occlusion d'une artère **cérébrale** (intracrânienne : cérébrale moyenne, antérieure, postérieure, cérébelleuses, perforantes) **sans infarctus cérébral résultant** [S1]. Le substrat dominant est la **maladie athéroscléreuse intracrânienne** (ICAD/ICAS) [S2][S6].

Question pivot : **après un AIT dû à une sténose intracrânienne, faut-il dilater/stenter ou traiter médicalement ?** Réponse des essais et de l'ESO : traitement médical intensif (double antiagrégation transitoire + contrôle agressif des facteurs de risque) ; le stenting de première intention augmente les AVC et décès précoces [S2][S12][S13][S14][S15].

Fil conducteur proposé : anatomie (artères distales du polygone, peu de collatérales) → mécanismes (thrombose in situ, embolie artère-artère, occlusion de branche perforante, bas débit) → syndromes transitoires par territoire → imagerie (exclure par TCD/ARM, confirmer par angio-TDM/ARM/ASD, méthode WASID) → différentiel non athéroscléreux → traitement médical → place résiduelle de l'endovasculaire.

## 1. Définition et classification (CIM-10-GM 2024)

- **I66** « Verschluss und Stenose zerebraler Arterien ohne resultierenden Hirninfarkt ». Inclusions : embolie, obstruction (complète ou partielle), sténose, thrombose des artères cérébrales (moyenne, antérieure, postérieure, cérébelleuses) **sans infarctus cérébral résultant**. Exclusion : comme cause d'un infarctus cérébral → **I63.-** [S1].
- Sous-codes [S1] (titres français : registre MEDINA `nosology/fragments/S08.json`, source OFS) :

| Code | Intitulé |
|---|---|
| I66.0 | Occlusion et sténose de l'artère cérébrale moyenne |
| I66.1 | Occlusion et sténose de l'artère cérébrale antérieure |
| I66.2 | Occlusion et sténose de l'artère cérébrale postérieure |
| I66.3 | Occlusion et sténose des artères cérébelleuses |
| I66.4 | Occlusion et sténose des artères cérébrales, multiples et bilatérales |
| I66.8 | Occlusion et sténose d'une autre artère cérébrale (inclut : artères perforantes / « Stammganglienarterien ») |
| I66.9 | Occlusion et sténose d'une artère cérébrale, sans précision |

- Codes voisins [S1] : **I65** = artères **précérébrales** (vertébrale, **basilaire**, carotide) — attention, la basilaire et la carotide (y compris siphon) relèvent de I65, pas de I66 ; **I63.3/I63.4/I63.5** = infarctus par thrombose / embolie / occlusion-sténose non précisée des artères cérébrales ; **I67.2** = athérosclérose cérébrale (athéromatose des artères cérébrales) ; **G45.-** = AIT (codé séparément).

## 2. Définitions et classifications cliniques

- **ICAD** : plaque athéroscléreuse des grandes artères intracrâniennes à tout stade, y compris non sténosante ; **ICAS** : plaque responsable d'un rétrécissement significatif, en général **> 50 %**, documenté par angiographie ou Doppler transcrânien (DTC) [S2].
- **Sténose de haut grade** : > 70 % **et/ou** retentissement hémodynamique [S2].
- **Retentissement hémodynamique** : baisse du débit antérograde avec recrutement de collatérales ; sévère quand les collatérales ne maintiennent plus la perfusion. Indices : fluctuations posturales ou post-prandiales des déficits, infarctus de jonction (borderzone) [S2].
- **Symptomatique** : un événement ischémique cérébral est attribuable à la plaque ; **asymptomatique** : sujet sans AVC ou événement expliqué par une autre cause [S2].
- **AIT (ESO)** : symptômes neurologiques transitoires, vraisemblablement dus à une ischémie focale cérébrale ou oculaire, < 24 h. **AIT à haut risque** notamment si maladie significative d'une grosse artère ipsilatérale, **y compris sténose intracrânienne** [S4].
- **Mesure du degré (méthode WASID)** : % sténose = [1 − (D sténose / D normal)] × 100 ; D normal = diamètre du segment proximal normal (à défaut : segment distal, puis artère nourricière). Concordance interobservateur 71–100 % (écart ≤ 10 %) [S10].

## 3. Épidémiologie

- ICAD : jusqu'à **10 %** des AVC ischémiques chez les Caucasiens ; cause la plus fréquente chez les personnes d'ascendance asiatique ; jusqu'à 40 % des occlusions de grosses artères (LVO) en Asie [S2].
- Proportion d'AVC ischémiques liés à l'ICAS : Inde ≈ 50 %, Chine 47 %, Corée 25 %, pays occidentaux **10–16 %** [S6].
- Europe (≥ 50 %) : Grèce 9,2 %, Allemagne 6,5 % (DTC), Espagne 12,4 %, Pays-Bas 3 % (angio-TDM, ≥ 50 %) ; France 17,8 % (≥ 30 %, autopsies d'AVC fatals) [S7].
- ICAS **asymptomatique ≥ 50 %** : Barcelona-AsIA (Espagne) 9 %, Royaume-Uni 11 %, Japon 6 % [S7].
- Revue bernoise : les sténoses athéroscléreuses intracrâniennes sont la cause la plus fréquente d'AVC ischémique **dans le monde** [S3].

## 4. Anatomie et physiologie (normal → pathologique)

- Les artères intracrâniennes sont d'origine mésodermique, à média et adventice minces, peu de fibres élastiques et peu de vasa vasorum [S6].
- Les lésions intracrâniennes sont **distales au polygone de Willis** : elles disposent de moins de suppléance collatérale que les lésions extracrâniennes [S6].
- Histologie comparée : plus de fibrose proliférative, moins de lésions compliquées, moins d'infiltration lipidique et d'inflammation intimale qu'en extracrânien ; LDL, LDL oxydées et macrophages intimaux plus bas ; activité enzymatique antioxydante plus élevée [S6].
- Paroi normale en IRM de paroi : épaisseur concentrique uniforme, lumière lisse, pas de rehaussement [S7].

## 5. Mécanismes de l'ischémie (physiopathologie)

Quatre mécanismes, souvent associés [S6][S7] :
1. **Rupture de plaque → thrombose in situ** (occlusion locale) [S6][S7].
2. **Embolie artère-artère** depuis le segment sténosé ; signaux microemboliques fréquents au DTC dans les sténoses symptomatiques de l'ACM à la phase aiguë [S6][S16].
3. **Occlusion de branche** : la plaque recouvre l'ostium d'une perforante → infarctus lacunaire possible même avec une sténose légère [S6][S7].
4. **Bas débit hémodynamique** : sténose serrée → baisse du débit antérograde, aggravée par hypotension ou hypovolémie ; infarctus volontiers en territoire de jonction [S7][S2].
- Embolie artère-artère et occlusion de branche sont décrites comme relativement plus fréquentes [S7].
- Progression : environ un tiers des sténoses progressent malgré le traitement médical [S2].

## 6. Causes et facteurs de risque

- Athérosclérose : âge, hypertension, diabète, hypercholestérolémie, tabagisme, sédentarité, syndrome métabolique ; ethnie (populations noires et asiatiques) [S6].
- Marqueurs lipidiques associés à la sévérité : rapport apoB/apoA1 élevé, adiponectine basse, lipoprotéine(a) élevée [S6].
- Variant **RNF213 p.R4810K** associé à l'ICAD en Asie de l'Est, absent hors populations asiatiques [S7].
- Causes **non athéroscléreuses** de sténose/occlusion intracrânienne (différentiel, § 10) : dissection, vasculite, syndrome de vasoconstriction cérébrale réversible (SVCR), angiopathie de moyamoya / vasculopathie RNF213 [S6][S23][S24] ; occlusion **embolique** d'origine cardiaque ou carotidienne (ex. ACA : embolie carotidienne ou cardiaque dans 63 % des infarctus ACA du registre lausannois) [S17].

## 7. Anamnèse et présentation clinique (par territoire)

I66 exclut l'infarctus constitué : la présentation typique est un **AIT** du territoire concerné, ou une découverte d'imagerie (asymptomatique). Les tableaux par territoire ci-dessous proviennent de séries d'**infarctus** (registre de Lausanne et séries parisiennes) ; ils décrivent les déficits que l'ischémie transitoire peut reproduire [S17–S22].

| Artère (sous-code) | Signes rapportés | Source |
|---|---|---|
| ACM superficielle (I66.0) | Territoire le plus fréquent des infarctus sylviens ; troubles de la personnalité, du jugement, de la synchronisation motrice, désorientation, hémianopsie, héminégligence selon la branche | [S22] |
| ACA (I66.1) | Hémiparésie, hémihypoesthésie, mutisme initial, aphasie motrice transcorticale, troubles des tâches conflictuelles, troubles de l'humeur ; plus rarement incontinence, grasping, héminégligence, confusion, apraxie gauche unilatérale. 1,8 % des AVC du registre | [S17] |
| ACP superficielle (I66.2) | Hémianopsie 67 %, quadranopsie 22 %, déficit bilatéral 7 % ; troubles mnésiques 17,5 %, dysphasie, hallucinations, négligence visuelle, agnosie visuelle, prosopagnosie, dysnomie des couleurs | [S18] |
| PICA (I66.3) | Vertige aigu et ataxie axiale (PICA médiale) ; instabilité, ataxie des membres, dysmétrie sans dysarthrie (PICA latérale) | [S19] |
| AICA (I66.3) | Atteinte constante de nerfs crâniens : paralysie faciale, trouble sensitif trigéminal, surdité ± acouphènes, syndrome vestibulaire, paralysie de latéralité ; ataxie ; mécanisme surtout thrombose sur sténose athéromateuse | [S20][S19] |
| ACS / SCA (I66.3) | Dysarthrie, instabilité et/ou vertige, ataxie des membres, dysmétrie ; formes graves avec syndrome du sommet basilaire, coma | [S19][S21] |

- Indices d'un mécanisme hémodynamique : fluctuations posturales ou post-prandiales [S2].
- Petits infarctus multiples cérébelleux associés à l'athérosclérose vertébro-basilaire (8/12) ; grands infarctus PICA/ACS surtout cardio-emboliques [S19].

## 8. Examen clinique

- Examen neurologique orienté par territoire (tableau § 7). Aucune source lue ne décrit un signe clinique spécifique de la sténose intracrânienne elle-même (lacune § 17).

## 9. Examens complémentaires

- **ESO TIA** : angio-IRM ou angio-TDM recommandée chez les patients avec AIT pour confirmer une sténose d'une grosse artère ≥ 50 % ; évaluation spécialisée dans les **24 h** [S4].
- **DTC** : signes de sténose = augmentation focale de la vitesse moyenne, baisse distale de la vitesse, index de pulsatilité augmenté [S7]. **SONIA** (vs angiographie, sténose 50–99 %) : DTC VPP 36 %, VPN 86 % ; ARM VPP 59 %, VPN 91 % → DTC et ARM **excluent** bien une sténose ; un résultat anormal exige une confirmation (angiographie) [S11].
- **ARM TOF (3 T)** : sensibilité 75–85 %, spécificité 95 % pour 50–99 % ; surestime la sténose (artefact de flux) [S7]. **Angio-TDM** : très sensible et spécifique pour > 50 % (valeurs non chiffrées dans la source) [S7].
- **Angiographie numérisée (ASD)** : étalon-or, invasive, ne montre pas la paroi [S6] ; mesure selon WASID [S10].
- **IRM de paroi haute résolution** (en général 3 T) [S6][S7] : athérosclérose = épaississement excentrique, rehaussement de la chape fibreuse, possible hémorragie intraplaque ; dissection = flap, double lumière, hématome intramural ; vasculite = épaississement concentrique multifocal rehaussé ; SVCR = épaississement concentrique peu rehaussé, régressif ; RNF213/moyamoya = rehaussement concentrique, diamètre externe réduit, collatérales basales. Marqueurs de plaque symptomatique : rehaussement (≥ hypophyse), remodelage positif, hypersignal T1, irrégularité de surface [S7].
- **Perfusion** : MTT allongé dans le territoire d'une sténose 50–99 % → risque d'AVC ipsilatéral accru (souvent en jonction) ; mismatch Tmax > 6 s ≥ 15 mL associé aux récidives [S7].

## 10. Diagnostic différentiel

- Dissection intracrânienne (céphalées, douleur cervicale postérieure ; flap/double lumière) [S6][S24].
- Vasculite (aspect « en chapelet », sténoses distales en angiographie) [S6].
- SVCR (céphalée en coup de tonnerre ; régression à l'imagerie de contrôle) [S6].
- Angiopathie de moyamoya (collatérales « moyamoya » ; ESO : antiagrégation au long cours en forme non hémorragique ; revascularisation chirurgicale selon le retentissement hémodynamique) [S6][S23].
- Occlusion embolique (cardiaque, carotidienne) [S17][S18].
- Lésion **précérébrale** (carotide, vertébrale, basilaire) → I65 [S1].
- Infarctus constitué à l'IRM → I63, non I66 [S1].

## 11. Urgences

- AIT avec sténose intracrânienne = **AIT à haut risque** ; double antiagrégation (clopidogrel + aspirine) de courte durée recommandée fortement par l'ESO dans l'AIT non cardio-embolique à haut risque (ABCD2 ≥ 4) ; revue spécialisée < 24 h [S4].
- Risque précoce (ICAD symptomatique) : récidive 5,5 % à 30 jours, 14,9 % à 1 an, 17,2 % à 2 ans ; infarctus du myocarde 3,4 % la 1re année ; mortalité 4,5 % sur 2 ans [S2].
- Occlusion aiguë sur ICAD (LVO) : définition opérationnelle ESO — absence de fibrillation atriale, absence de signe de l'artère hyperdense/de susceptibilité, infarctus de jonction, occlusion de type tronculaire, sténose résiduelle après passage du stent-retriever ou réocclusion précoce. Inhibiteurs GP IIb/IIIa ou angioplastie/stent de sauvetage : pas de recommandation fondée sur les preuves (très faible certitude) ; consensus d'experts en faveur des anti-GP IIb/IIIa de sauvetage (8 pour / 4 contre) [S2]. (Relève surtout de I63, mentionné pour le différentiel.)

## 12. Prise en charge (Suisse / Europe)

### 12.1 Traitement antithrombotique
- **Antiagrégants plutôt qu'anticoagulants** (ESO, preuve modérée) [S2]. WASID (569 patients, sténose 50–99 %) : warfarine vs aspirine 1300 mg → critère principal 21,8 % vs 22,1 % (HR 1,04) ; décès 9,7 % vs 4,3 % ; hémorragie majeure 8,3 % vs 3,2 % ; IDM/mort subite 7,3 % vs 2,9 % ; essai arrêté pour sécurité [S8].
- **Double antiagrégation** (ESO, preuve faible) : recommandée comme traitement de choix chez l'ICAD symptomatique, à maintenir **90 jours** (consensus d'experts) [S2]. Données : aspirine + inhibiteur P2Y12, récidive d'AVC ou décès OR 0,69 (10,6 % vs 14,7 %) [S2] ; CLAIR : clopidogrel + aspirine réduit les signaux microemboliques à J2 vs aspirine seule (RRR 42,4 %) chez des patients majoritairement avec sténose intracrânienne symptomatique [S16].
- ESO prévention secondaire : **éviter** la bithérapie aspirine + clopidogrel **au-delà de 90 jours** [S5].
- Cilostazol : non-infériorité à l'aspirine chez des Asiatiques ; données d'association [S6][S2] — **non trouvé dans l'AIPS suisse** (voir § 12.4).

### 12.2 Facteurs de risque (traitement médical intensif)
- ESO ICAD : contrôle agressif des facteurs de risque (lipides, mode de vie, activité physique) — recommandation faible [S2]. LDL cible cité par l'ESO ICAD : **< 1,4 mmol/L (55 mg/dL)** selon ESC/EAS 2019 [S2] ; l'ESO prévention secondaire recommande une statine avec cible **LDL < 1,8 mmol/L (70 mg/dL)** et ézétimibe ou inhibiteur PCSK9 si cible non atteinte [S5] → **divergence à présenter** (mot vert).
- Pression artérielle : ESO prévention secondaire **< 130/80 mmHg** sauf sous-groupes à risque [S5] ; ESO ICAD : contrôle strict dès la phase subaiguë ; essai PAS < 120 vs < 140 sans différence à 24 semaines [S2]. Pression permissive en phase aiguë d'une ICAD de haut grade : pas de recommandation [S2].
- Atorvastatine 40 vs 10 mg (n = 120) : récidive à 52 semaines 13,5 % vs 26,3 % [S2].
- SAMMPRIS — bras médical : antiagrégation, contrôle intensif des facteurs de risque et programme de modification du mode de vie ; l'inactivité physique prédit les événements à 3 ans [S2][S13].
- HbA1c < 53 mmol/mol (7 %) chez le diabétique (consensus) ; pioglitazone à considérer [S5].

### 12.3 Revascularisation
- **Angioplastie/stenting (PTAS) en première intention : recommandation forte contre** (ESO) [S2]. Données :
  - SAMMPRIS (451 patients, 70–99 %, stent Wingspan) : AVC/décès à 30 j **14,7 % vs 5,8 %** ; primaire à 1 an 20,0 % vs 12,2 % [S12] ; suivi médian 32,4 mois 23 % vs 15 % ; tout AVC 26 % vs 19 % ; hémorragie majeure 13 % vs 4 % [S13]. Aucun sous-groupe (y compris symptômes hémodynamiques) ne bénéficie du stent [S25].
  - VISSIT (stent expansible par ballon, arrêté précocement) : critère de sécurité à 30 j 24,1 % vs 9,4 % ; AVC/AIT même territoire à 1 an 36,2 % vs 15,1 % [S2].
  - CASSISS (Chine, 358 patients, > 3 semaines après l'événement, territoires non perforants) : AVC/décès 8,0 % vs 7,2 % (HR 1,10) ; aucune différence à 2 et 3 ans ; mortalité à 3 ans 4,4 % vs 1,3 % (NS) [S14].
  - Cochrane 2023 (4 ECR, 989 patients) : ET + traitement médical augmente probablement décès/AVC à court terme (RR 2,93) et à long terme (RR 1,49) ; AVC hémorragique précoce RR 13,49 [S15].
- Place résiduelle : **sauvetage** chez des patients sélectionnés avec ICAS symptomatique de haut grade et **récidive malgré traitement médical optimal** (consensus ESO) ; défaillance hémodynamique avec collatérales pauvres et embolie artère-artère orientent vers la PTAS [S2] ; revue bernoise : à envisager chez des patients soigneusement sélectionnés avec AVC récidivants attribués à la sténose malgré traitement médical [S3].
- **Chirurgie** (pontage extra-intracrânien, EDAS) : recommandation forte contre en première ligne [S2]. EC-IC Bypass Study (1377 patients) : événements ischémiques à 30 j 12,2 % vs 3,4 % [S2]. Chirurgie de revascularisation rarement retenue (revue bernoise) [S3].
- **Conditionnement ischémique à distance** : suggestion faible, à considérer en complément et dans des essais (preuve faible/très faible, études à haut risque de biais) [S2].

### 12.4 Médicaments — information professionnelle suisse (AIPS via AmiKo, consultée le 14.10.2026)
- **Aspirine® Cardio 100/300** (MAJ mars 2026) : indication « prophylaxie des accidents cérébro-vasculaires suite à l'apparition de stades précurseurs (AIT) » ; posologie libellée pour l'AIT 100 mg 3×/j ou 300 mg 1×/j ; indications cardiovasculaires générales 100 mg 1×/j. Mécanisme : inhibition irréversible de la thromboxane A2 plaquettaire. CI : ulcère actif, diathèse hémorragique, MICI, insuffisance hépatique sévère, 3e trimestre [S26].
- **Plavix®** (clopidogrel ; MAJ sept. 2022) : indication de prévention secondaire après AVC récent (7 jours à env. 6 mois) en monothérapie 75 mg/j ; la bithérapie avec AAS est libellée pour SCA, stent coronaire et FA — **la bithérapie après AIT/AVC n'est pas une indication libellée** (usage selon recommandations ESO). Prodrogue activée par CYP450 (CYP2C19 : réponse diminuée chez les métaboliseurs lents) ; inhibition irréversible du récepteur P2Y12 ; triple antiagrégation (clopidogrel + aspirine + dipyridamole) déconseillée dans l'AVC ; arrêt 7 jours avant chirurgie [S27].
- **Sortis®** (atorvastatine ; MAJ avril 2025) : dose 10–80 mg/j ; SPARCL (4731 patients, AVC/AIT < 6 mois, 80 mg) ; analyse post-hoc : plus d'AVC hémorragiques sous 80 mg, surtout chez les patients avec antécédent d'AVC hémorragique ou lacunaire. CI : hépatopathie active, transaminases > 3× persistantes, grossesse/allaitement [S28].
- **Brilique®** (ticagrélor ; MAJ nov. 2025) : indications suisses limitées au SCA et à l'antécédent d'IDM ; **aucune indication libellée AVC/AIT** [S29].
- **Cilostazol** : recherche AIPS (« cilostazol », « pletal ») sans résultat le 14.10.2026 → ne pas présenter comme disponible en Suisse sans vérification complémentaire.

## 13. Suivi

- Récidive et progression : un tiers des sténoses progressent ; récidive cumulée 17,2 % à 2 ans [S2].
- Prédicteurs de récidive dans le territoire (WASID) : sténose ≥ 70 % (HR 2,03), inclusion précoce ≤ 17 jours après l'événement (HR 1,69), sexe féminin (HR 1,59, limite) ; la localisation et le type d'événement ne sont pas prédictifs [S9]. 73 % des AVC ultérieurs surviennent dans le territoire de l'artère sténosée [S9].
- Autres marqueurs : défaillance hémodynamique, profil perfusionnel (Tmax), rehaussement de plaque persistant et hémorragie intraplaque [S7] ; PAS moyenne associée à la progression (SAMMPRIS post hoc) [S6].
- Arrêt de la bithérapie après 90 jours, puis monothérapie (bras médical CASSISS : DAPT 90 j puis monothérapie) [S2][S5][S14].

## 14. Situations particulières

- **ICAD asymptomatique** : pas de recommandation ESO sur le dépistage ni sur l'antiagrégation (pas d'ECR) ; HR ajusté d'AVC futur 1,85 (faible certitude) ; consensus marginal pour une antiagrégation (7 pour / 5 contre) [S2] ; revue bernoise : traitement conservateur recommandé chez l'asymptomatique [S3].
- **Sténose 50–69 %** : aucune donnée d'ECR sur la PTAS [S2].
- **Patient d'ascendance asiatique** : prévalence et part des LVO plus élevées [S2][S6][S7].
- **Moyamoya** : revascularisation chirurgicale directe/combinée si retentissement hémodynamique, 6–12 semaines après le dernier événement ; antiagrégation au long cours en forme non hémorragique [S23].
- **Dissection intracrânienne** avec HSA : intervention endovasculaire ou chirurgicale précoce (ESO) [S24].

## 15. Critères formels (pour l'îlot `div.alert`)

- I66 = sténose ou occlusion d'une artère cérébrale (ACM, ACA, ACP, cérébelleuses, perforantes) **sans infarctus cérébral constitué** ; si infarctus → I63 [S1].
- ICAS = rétrécissement > 50 % ; haut grade = > 70 % et/ou retentissement hémodynamique [S2] ; mesure WASID [S10].
- Symptomatique = événement ischémique attribuable à la plaque [S2].

## 16. Paramètres clés (pour l'îlot `div.key`)

| Paramètre | Valeur | Source |
|---|---|---|
| Part des AVC ischémiques (Occident) | ≈ 10 % (10–16 %) | [S2][S6] |
| Récidive ICAD symptomatique | 5,5 % (30 j) ; 14,9 % (1 an) ; 17,2 % (2 ans) | [S2] |
| Seuils | > 50 % = ICAS ; > 70 % = haut grade | [S2] |
| DAPT | 90 jours puis monothérapie | [S2][S5] |
| SAMMPRIS AVC/décès 30 j | 14,7 % (stent) vs 5,8 % (médical) | [S12] |
| LDL cible | < 1,8 mmol/L (ESO 2022) ; < 1,4 mmol/L cité par ESO ICAD | [S5][S2] |
| PA cible long terme | < 130/80 mmHg | [S5] |
| Anticoagulation (WASID) | non : plus de décès et d'hémorragies, sans bénéfice | [S8] |

## 17. Lacunes explicites

1. **Aucune recommandation suisse spécifique** (SSN / Swiss Stroke Society / Swiss Medical Forum) trouvée sur la sténose intracrânienne ; seule source suisse : revue bernoise Krasteva et al. 2021 lue **en résumé** [S3] ; ESO ICAD co-rédigée à Bâle [S2].
2. Seuils de vélocité DTC (ACM ≥ 50 % / ≥ 70 %) non trouvés dans les sources lues.
3. Chiffres de sensibilité/spécificité de l'angio-TDM non chiffrés dans la source lue.
4. Épidémiologie suisse propre à l'ICAS : non trouvée.
5. Signes cliniques spécifiques de I66 sans infarctus (sémiologie des AIT par territoire) : seulement par extrapolation des séries d'infarctus [S17–S22] ; « limb-shaking TIA » non documenté.
6. Ticagrélor + aspirine (THALES) dans l'ICAS : mentionné par l'ESO ICAD sans recommandation spécifique ; pas d'indication suisse [S29].
7. Disponibilité du cilostazol en Suisse non confirmée (AIPS négative).
8. Codage CIM-11 non établi.
9. Essais WASID, SAMMPRIS, VISSIT, CASSISS : populations américaines et chinoises ; utilisés comme **preuves** reprises par l'ESO, non comme recommandations américaines.
