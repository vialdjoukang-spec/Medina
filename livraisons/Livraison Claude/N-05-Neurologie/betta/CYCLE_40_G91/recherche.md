# G91 — Hydrocéphalie (N-05-Neurologie) — dossier de recherche

Cycle Betta 40, leçon 1 · agent C40-A3-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Note de méthode : le quota WebSearch de la session était épuisé ; recherche faite par PubMed (résumés, métadonnées), WebFetch de textes intégraux PMC (S2, S6, S9, S13), BfArM, et `tools/swissmedic_fi.py` (S14). Aucune ligne directrice suisse ni EAN spécifique à l'hydrocéphalie n'a été trouvée ; la ligne directrice japonaise (S2, 3e éd.) est la seule ligne directrice iNPH complète lue ; elle n'est ni suisse ni européenne et doit être présentée comme telle. L'essai PENS (S4) est nord-américain avec un co-investigateur suédois : c'est un essai randomisé, pas une recommandation ; il peut être cité comme donnée probante.

## 0. Question clinique
Deux visages : (1) l'hydrocéphalie aiguë obstructive ou post-hémorragique, urgence neurochirurgicale par hypertension intracrânienne ; (2) la triade lente du sujet âgé (marche, cognition, vessie) avec ventricules dilatés et pression de LCS normale — l'hydrocéphalie à pression normale idiopathique (iNPH), cause traitable de troubles de la marche et de déclin cognitif, à distinguer de la maladie d'Alzheimer, du parkinsonisme et de la maladie des petits vaisseaux. Comment classer, coder (G91 vs Q03/P91.7), confirmer (imagerie, test de soustraction de LCS) et traiter (dérivation, ventriculocisternostomie) ?

## 1. Définition et périmètre CIM-10-GM
- G91.- « Hydrozephalus » ; Inkl. : hydrocéphalie acquise. Exkl. : hydrocéphalie congénitale (Q03.-), hydrocéphalie acquise du nouveau-né (P91.7), hydrocéphalie due à la toxoplasmose congénitale (P37.1) [S1].
- Sous-codes : G91.0 communicante ; G91.1 obstructive (occlusus) ; G91.2- à pression normale : G91.20 idiopathique, G91.21 secondaire, G91.29 non précisée ; G91.3 post-traumatique sans précision ; G91.8 autres ; G91.9 sans précision [S1 ; libellés français OFS dans `nosology/fragments/S08.json`].
- Définition classique : dilatation active et progressive des ventricules due à un écoulement insuffisant du LCS entre ses sites de production et de résorption [S6]. Communicante : sans obstacle ; non communicante (obstructive) : obstacle partiel ou complet intra- ou extraventriculaire [S6].
- iNPH : conçue comme un trouble de la résorption du LCS sans maladie ou lésion antérieure pouvant l'expliquer ; c'est un « concept » plutôt qu'une définition diagnostique, car la réponse à la dérivation n'est mesurable qu'après chirurgie [S2].

## 2. Classifications
- Communicante vs non communicante ; congénitale vs acquise (hémorragie, infection, tumeur) [S6].
- Classification NPH (ligne directrice japonaise, 3e éd.) : iNPH ; NPH secondaire (après hémorragie sous-arachnoïdienne ou méningite) ; NPH congénitale/développementale (dont LOVA — ventriculomégalie longtemps évolutive de l'adulte, et PaVM), séparée de l'iNPH ; forme familiale mentionnée. LOVA est en général non communicante (sténose de l'aqueduc) [S2].
- Hydrocéphalie chronique de l'adulte (CHiA) : revue systématique et Delphi (Göteborg, Londres, Japon) ; 33 études utilisaient 48 termes ; regroupement en 7 entités cliniques ; nouvelle classification proposée [S12] (détail des 7 entités non lu → lacune).
- Pédiatrie : congénitale (sténose de l'aqueduc ; myéloméningocèle avec Chiari II ; Dandy-Walker ; forme liée à l'X par mutation L1CAM) ; acquise : post-hémorragique du prématuré (HIV grade III/IV, < 1500 g), post-infectieuse, tumorale (fosse postérieure, 4e ventricule) [S6].

## 3. Épidémiologie
- iNPH, population (Suède, scanner) : 3,7 % au total ; 8,9 % et 5,9 % au-delà de 80 ans selon deux études ; 1,5 % avec les critères japonais [S2].
- Japon : moyenne pondérée 1,6 % (4 études populationnelles) [S2].
- Méta-analyse mondiale 2018 : 175/100 000 ; 400/100 000 à ≥ 80 ans ; Japon 660/100 000, hors Japon 53/100 000 [S2].
- Données hospitalières : 2–10/100 000, 30–60/100 000 vers 65–70 ans et plus [S2].
- AVIM (ventriculomégalie asymptomatique avec aspect IRM d'iNPH) : progression vers l'iNPH 6–12 %/an (4/8 sur 4–8 ans) et ≈ 17 %/an (27/52 en 3 ans) [S2].
- Pédiatrie (monde) : ≈ 400 000 nouveaux cas/an, > 80 % dans les pays à revenu faible ou intermédiaire ; congénitale ≈ moitié ; jusqu'à 85 % des myéloméningocèles développent une hydrocéphalie ; incidence des anomalies du tube neural < 1/1000 naissances après supplémentation en folates ; post-hémorragique > 6000 cas/an dans les pays à haut revenu ; post-traumatique 0,7–3,7 % des traumatismes crâniens ; > 50 % des enfants avec tumeur cérébrale développent une hydrocéphalie ; jusqu'à 85 % des méningites tuberculeuses de l'enfant [S6].
- Hémorragie sous-arachnoïdienne anévrismale : hydrocéphalie chez ≈ 25 % ; létalité ≈ 40 % ; l'hydrocéphalie est un déterminant majeur du mauvais pronostic fonctionnel [S9].

## 4. Mécanismes (normal → pathologique)
- Normal : le LCS est sécrété en continu par l'épithélium des plexus choroïdes des quatre ventricules, source dominante ; l'épendyme n'est pas un site de sécrétion active ; chez l'animal, 30–40 % du LCS se forme en amont de l'aqueduc [S13]. Transporteurs clés : Na+/K+-ATPase, NKCC1 (≈ 50 % de la sécrétion chez l'animal), transporteurs HCO3- ; l'anhydrase carbonique intervient — l'acétazolamide réduit la sécrétion de LCS chez l'animal [S13].
- Résorption/drainage : voies lymphatiques le long des gaines des nerfs crâniens et spinaux, lame criblée, nerf optique ; granulations arachnoïdiennes qui mûrissent pendant la petite enfance ; système glymphatique (qualitatif) [S6].
- Modèle moderne : au-delà de l'obstruction au flux, rôle des pulsations cérébrales, de la compliance cérébrale et des mécanismes de transport d'eau ; causes acquises touchant l'écoulement ventriculaire, la fonction de l'espace sous-arachnoïdien ou la compliance veineuse [S7].
- Acquis pédiatrique : blocage des voies du LCS et dérégulation inflammatoire de la sécrétion et de la clairance [S6].
- iNPH : trouble de la résorption du LCS [S2] ; une ventriculomégalie communicante asymptomatique peut se développer chez des personnes âgées saines et devenir symptomatique, avec une réponse variable à la dérivation ; causes sous-jacentes discutées [S19, résumé].
- Pathologie associée : synucléinopathie concomitante chez 14–33 % des iNPH selon la méthode ; non prédictive d'une mauvaise réponse à la dérivation dans les données disponibles [S15].

## 5. Clinique
### 5a. Nourrisson et enfant [S6]
- Nourrisson : accélération du périmètre crânien, fontanelle bombante, sutures disjointes, parésie du regard vers le haut (« signe du coucher de soleil »), œdème papillaire, vomissements, irritabilité, bradycardie ou apnées sans autre cause.
- Enfant plus âgé : céphalées, vomissements, œdème papillaire, parésie du regard vers le haut, paralysie du VI.
### 5b. iNPH (sujet âgé) [S2]
- Fréquences : trouble de la marche 94–100 % ; trouble cognitif 78–98 % ; trouble urinaire 60–92 % ; triade complète ≈ 60 % (12,1 % dans une enquête japonaise de 1524 patients).
- Marche : petits pas, marche « magnétique », élargissement du polygone, freezing, pieds en dehors, grande variabilité de la longueur du pas ; contrairement à la maladie de Parkinson, les indices externes aident peu.
- Vessie : pollakiurie/impériosité (90,9 %), incontinence (74,5 %) ; hyperactivité détrusorienne ≈ 70 %.
- Cognition : ralentissement psychomoteur, atteinte attentionnelle et de la mémoire de travail, profil frontal ; rappel libre altéré avec reconnaissance relativement préservée ; désorientation et troubles mnésiques plus légers que dans l'Alzheimer.
- Signes frontaux : réflexe de museau 84 %, glabellaire 77 %, paratonie 65 %, palmo-mentonnier 61 % (série de 26) ; apathie 70,3 %.
- Méta-analyse : apathie 69,2 %, dépression 30,1 %, agitation 22,6 %, anxiété 21,9 % [S16].
### 5c. Lausanne (CHUV) [S3]
- 86 patients (âge moyen 76 ans) : plainte de marche 94,2 %, cognitive 75,6 %, urinaire 60,5 %.

## 6. Examens
- Imagerie iNPH [S2] : index d'Evans > 0,3 (moyenne SINPHONI 0,356) ; angle calleux < 90° (seuil 90° : sensibilité 97 %, spécificité 88 % vs Alzheimer) ; DESH = ventriculomégalie + dilatation des vallées sylviennes + étroitesse des espaces sous-arachnoïdiens de haute convexité/médians ; DESH présent chez 64 % des iNPH ; VPP 77 %, VPN 25 % pour une iNPH certaine.
- Ponction lombaire : pression ≤ 200 mmH2O et contenu normal pour une iNPH probable [S2].
- Test de soustraction (tap test) : sensibilité 58 % (26–87), spécificité 75 % (33–100) ; 30 ou 50 mL sans différence ; évaluation à 2–4 h, ≈ 24 h puis plusieurs fois la première semaine ; cognition et vessie s'améliorent plus tard que la marche ; drainage continu non supérieur au tap test pour prédire la réponse [S2]. Une réponse négative n'exclut donc pas une réponse à la dérivation (spécificité/sensibilité limitées) [S2].
- Évaluation de la marche : TUG, marche courte en ligne droite [S2] ; à Bâle (Felix Platter), la double tâche identifie 25,7 % de répondeurs supplémentaires au drainage, invisibles en marche simple [S17].
- Échelles : iNPHGS (marche, démence, incontinence, 0–4 chacune) ; MMSE, FAB, codes/symboles WAIS-III [S2] ; Eu-iNPH : RAVLT, Grooved Pegboard, Stroop discriminants (AUC 0,86–0,95) [S11].
- Biomarqueurs LCS : Aβ42 abaissé comme dans l'Alzheimer, mais p-tau et t-tau plus bas que dans l'Alzheimer [S2].
- Pédiatrie : échographie prénatale à 18–20 semaines, IRM fœtale ; postnatal échographie, scanner ou IRM ; pression d'ouverture ou monitorage de PIC ; ponction lombaire évitée en cas d'obstruction par masse [S6].
- Hémorragie sous-arachnoïdienne : imagerie (CT, CT de perfusion) en cas d'aggravation [S9].

## 7. Diagnostic (critères iNPH japonais) [S2]
- Possible : ≥ 1 symptôme de la triade ; symptômes non expliqués par une autre maladie ; aucune cause évidente de dilatation ventriculaire (HSA, méningite, traumatisme, hydrocéphalie congénitale, sténose de l'aqueduc).
- Probable : critères de possible + pression du LCS ≤ 200 mmH2O avec contenu normal + soit DESH avec trouble de la marche typique, soit amélioration après tap test/drainage.
- Certaine : amélioration objective après dérivation.

## 8. Diagnostic différentiel [S2, S15]
- Maladie d'Alzheimer : atrophie hippocampique plus marquée ; angle calleux et DESH discriminent ; profil tau.
- Synucléinopathies/Parkinson : maladie à corps de Lewy suspectée chez 21/127 iNPH certaines ; indices orientant vers une synucléinopathie : rigidité des membres supérieurs, anosmie, hallucinations, dysautonomie, fluctuations [S15].
- Maladie vasculaire : leucopathie périventriculaire plus fréquente dans les iNPH sévères, non nécessaire, suggère une composante ischémique [S2].

## 9. Urgences
- Hydrocéphalie aiguë après HSA : drainage recommandé en cas de baisse de vigilance ; drain ventriculaire externe pratique quasi universelle et seule option en cas d'hydrocéphalie obstructive ; drainage lombaire ou PL possibles seulement en forme communicante ; dérivation lombaire en cas d'obstruction ou d'œdème important = risque d'engagement amygdalien et de décès ; dérivation permanente si le drain ne peut être retiré [S9].
- Enfant : bradycardie, apnées, vomissements, œdème papillaire, irritabilité = HTIC [S6].
- Dysfonction de dérivation (enfant) : irritabilité, baisse d'activité, anorexie, nausées, vomissements, céphalées ; obstruction proximale le plus souvent ; < 6 mois plus à risque [S6].

## 10. Prise en charge
### 10a. iNPH
- Preuve randomisée : PENS (99 patients répondeurs au drainage ; valve ouverte 110 mmH2O vs placebo > 400 mmH2O) : vitesse de marche +0,23 vs +0,03 m/s à 3 mois (différence 0,21 ; IC95 % 0,12–0,31) ; Tinetti amélioré ; MoCA et vessie non significatifs ; chutes 24 % vs 46 % ; hématome sous-dural 12 % vs 2 % ; céphalées posturales 59 % vs 28 % [S4]. Commentaire néerlandais : première preuve de niveau I, validité externe et durabilité limitées [S5].
- Eu-iNPH (13 centres européens, 142 patients, dérivation ventriculo-péritonéale programmable, sélection clinique et radiologique seule) : à 1 an, amélioration 69 % (mRS) et 84 % (échelle iNPH) ; vie autonome (mRS 0–2) 53 % → 82 % ; complications 28 % (13 % conservatrices, 15 % chirurgicales) ; ni la classification ni la comorbidité n'ont modifié l'amélioration [S10].
- Type de dérivation : ventriculo-péritonéale, lombo-péritonéale, ventriculo-atriale ; valve programmable recommandée (grade 1, niveau B) ; dispositif anti-siphon/gravitationnel si hypotension intracrânienne [S2]. Complications : 10 % (VP) vs 14 % (LP) ; VA vs VP : hématome sous-dural 12,7 % vs 5,5 %, occlusion 6,7 % vs 15,3 % [S2]. Ventriculocisternostomie (ETV) : 50 % vs 76,9 % (VP) améliorés à 12 mois (petit essai brésilien) [S2].
- Réglage : départ haut avec baisse progressive (moins d'hyperdrainage, amélioration plus lente) vs pression fixe 12 cmH2O (hyperdrainage 9/34) [S2].
- Résultats à long terme : amélioration mRS 63–84 % à 1 an, 69 % à 2 ans, 60–74 % à 3–6 ans ; marche 60–77 %, cognition 61–69 %, incontinence 52 % ; index de comorbidité de Kiefer ≤ 3 : 93 % améliorés à 2 ans ; ≥ 6 : aucune amélioration attendue ; pas d'âge limite énoncé [S2]. Lausanne : > 80 ans rapportent plus souvent une amélioration de la marche ; 92 % d'amélioration de la marche à 6 semaines (16 opérés) [S3].
- Parcours suisse (CHUV) : évaluation neurologique au Leenaards Memory Center → neuropsychologie → tap test avec évaluation physiothérapeutique avant et 24 h après → consultation interdisciplinaire neurochirurgien-neurologue → board ; suivi 6 semaines, 6 et 12 mois ; 44 candidats discutés, 27 recommandés pour dérivation VP [S3].
### 10b. Enfant [S6]
- Dérivation VP = pilier ; ETV ± cautérisation des plexus choroïdes (ETV-CPC) préférée pour les causes obstructives (sténose de l'aqueduc) ; ETV-CPC surtout < 2 ans ; solutions temporaires chez le prématuré : drain ventriculaire externe, cathéter intrathécal lombaire, dérivation ventriculo-sous-galéale, réservoir d'accès ventriculaire avec ponctions répétées.
- Échec d'ETV possible jusqu'à 8 ans après.
- Ponctions lombaires répétées, acétazolamide et fibrinolytiques intraventriculaires n'ont pas réduit l'hydrocéphalie post-hémorragique.
### 10c. Infection de dérivation
- BASICS (Royaume-Uni/Irlande, 1605 patients, nouveau-nés à 91 ans) : infection 6,0 % (standard), 2,2 % (imprégné d'antibiotiques, rifampicine + clindamycine ; HR 0,38), 5,9 % (argent, non supérieur) ; échec toutes causes 25 % sans différence [S8]. Enfant, pays à haut revenu : infection 3–11 % [S6].
### 10d. Hyperdrainage
- Définition consensuelle (Delphi, 18 experts, majoritairement européens) : céphalées posturales soulagées en décubitus (irritabilité chez le nourrisson) ; collapsus ventriculaire (< 18 ans) ; collections sous-durales non traumatiques (tous âges) ; définitions distinctes < 1 an, 1–7 ans, > 7 ans, adulte [S18]. Symptômes chez l'enfant : céphalées, nausées, vomissements, vision floue, vertiges [S6].

## 11. Pharmacologie
- Acétazolamide (Diamox®, FI Swissmedic, mise à jour juillet 2026) [S14] : inhibiteur de l'anhydrase carbonique ; indications suisses incluant les « œdèmes cérébraux », pas l'hydrocéphalie ; contre-indications : hyponatrémie/hypokaliémie, atteinte rénale ou hépatique grave (cirrhose), insuffisance surrénalienne, acidose hyperchlorémique, allergie aux sulfamides ; effets : acidose métabolique, hypokaliémie, lithiase, paresthésies, somnolence ; PEAG ; œdème pulmonaire non cardiogénique ; interaction AAS à haute dose (acidose sévère) ; grossesse à éviter. Swisspeddose (intégré) : « pression intracrânienne élevée », per os 8–10 mg/kg/dose ×3, max 100 mg/kg/j, 1 mois–18 ans, usage hors AMM (HARM).
- Données probantes : efficacité limitée de l'acétazolamide dans l'hypertension intracrânienne idiopathique et sans effet sur l'hydrocéphalie post-hémorragique du prématuré [S6]. Aucune pharmacothérapie de l'iNPH lue → lacune.
- Antibioprophylaxie peropératoire et cathéters imprégnés : [S2, S8].

## 12. Suivi et pronostic
- iNPH : résultats à court terme dépendants des complications, de la durée et de la sévérité, de la réponse au tap test et du DESH ; à long terme, des comorbidités (AVC, cancer, Alzheimer, Parkinson) [S2]. Coût-efficacité : modèle suédois +2,2 années de vie, +1,7 QALY pour 13 000 € [S2].
- Enfant : mortalité liée à la dérivation 8 % à 20–40 ans ; 67 % scolarité ordinaire, 56 % socialement autonomes, 42 % employés ; seuls ≈ 20 % ont un bilan neurocognitif standardisé [S6]. Surveillance du périmètre crânien au moins tous les 3 mois jusqu'à 18 mois (recommandation américaine AAP citée dans S6 → ne pas utiliser comme fondement) [S6].

## 13. Situations particulières
- HSA : centres ≥ 70 HSA/an (≥ 35 si éloignés) avec soins intensifs neurologiques [S9]. Tranexamique : pas d'augmentation significative de l'hydrocéphalie (ULTRA, OR 1,23 ; IC 0,93–1,63) [S9].
- Tuberculose méningée de l'enfant : traitement médical possible en première ligne pour la forme communicante [S6].

## 14. Critères formels (pour l'îlot final)
- Critères japonais iNPH possible/probable/certaine (§7) [S2] ; index d'Evans > 0,3 ; angle calleux < 90° ; DESH ; pression LCS ≤ 200 mmH2O [S2].

## 15. Paramètres clés
Evans > 0,3 ; angle calleux < 90° ; tap test 30–50 mL, réévaluation 2–4 h et 24 h, sensibilité 58 %, spécificité 75 % [S2] ; PENS +0,21 m/s à 3 mois, HSD 12 % [S4] ; Eu-iNPH 84 % améliorés à 1 an, complications 28 % [S10] ; infection de dérivation 6,0 % vs 2,2 % avec cathéter antibiotique [S8] ; HSA : hydrocéphalie ≈ 25 % [S9].

## Sous-codes couverts
G91.0, G91.1 (§1, §2, §9, §10b) ; G91.20 (§2–§12) ; G91.21 (§2 : après HSA, méningite ; §9) ; G91.29 ; G91.3 (épidémiologie pédiatrique post-traumatique §3, données adultes non lues) ; G91.8, G91.9 (définition seule). Exclusions Q03, P91.7, P37.1 (§1).

## Lacunes
- Aucune ligne directrice suisse (SSN, Swiss Medical Forum) ni européenne (EAN, EANS) spécifique à l'hydrocéphalie ou à l'iNPH lue ; recherche WebSearch impossible (quota épuisé).
- Volume total et débit de production du LCS chez l'humain : non trouvés dans les sources lues (S13 ne donne que des données animales) — ne pas chiffrer.
- Recommandations formelles ESO/EANS/ESMINT 2026 sur le drain ventriculaire (texte du tableau 3 en image) : non lues ; sevrage du drain non traité.
- Hydrocéphalie post-traumatique de l'adulte (G91.3) et hydrocéphalie de l'adulte d'origine tumorale : pas de source dédiée.
- Score de succès de l'ETV (ETVSS), taux d'échec des dérivations à 1–2 ans : non lus.
- Histoire naturelle de l'iNPH non opérée : non lue.
- 7 entités CHiA de S12 : seul le résumé lu.
- Triade de Cushing : non présente dans les sources lues.
- AAN 2015 (américaine) identifiée mais non retenue comme fondement.
