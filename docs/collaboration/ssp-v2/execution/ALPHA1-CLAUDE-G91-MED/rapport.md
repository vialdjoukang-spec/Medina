# Audit médical ALPHA77 — G91 Hydrocéphalie (S08, Neurologie)

Mission ALPHA1-CLAUDE-G91-MED · branche `claude/alpha1/g91-med-g1` · base `103745ba` · sources figées conformes au manifeste (sept empreintes SHA-256 identiques) · exécutant : sous-agent Claude Code, modèle conforme au manifeste · 16 octobre 2026.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

La leçon est exacte sur l’essentiel de ses chiffres : sur 438 grandeurs relevées, 424 concordent avec la citation de la source lue, et aucune dose ni aucun seuil n’est faux par rapport à sa source. Ses défauts sont ailleurs. La sémiologie fondamentale et analytique manque, les sciences échouent au contrôle automatique, la génétique est absente, et la ligne directrice européenne de 2025 sur l’hydrocéphalie de l’enfant n’est pas utilisée. La pharmacologie confond l’hypertension intracrânienne idiopathique de l’enfant avec l’hydrocéphalie, ne signale pas que la limite de 100 mg/kg/jour d’acétazolamide dépasse les doses adultes chez l’adolescent, et écrit « conduite non détaillée » là où l’information professionnelle suisse la donne. La ventriculocisternostomie est présentée comme une option « moins efficace » de l’iNPH alors que la ligne directrice la juge sans efficacité suggérée.

| BLOQUANT | MAJEUR | MINEUR | ENRICHISSEMENT |
|---|---|---|---|
| 0 | 8 | 13 | 5 |

Première source lue : [S1] ligne directrice japonaise 2021, critères de l’iNPH possible et probable (texte intégral PMC7905302).

## Constats MAJEUR

### C01 — `chapters/G91/G91_c.html`

**Ancre** : « data-s="g91-s-anat" »

**Constat.** Le sous-onglet « Sémiologie fondamentale et analytique » est absent. Décompte réel des data-s de G91_c.html : 4 (g91-s-anat, g91-s-histo, g91-s-physio, g91-s-bioch) ; aucun g91-s-semio, aucun marqueur data-semiology-clinical dans pA. La sémiologie existante (îlot g91-5, cartes nourrisson et enfant, triade, signes frontaux) est descriptive : pas de technique d’examen du nourrisson, pas d’examen de la dérivation, pas de regroupement syndromique, pas de raisonnement en étapes ni de cas sur la valeur d’un signe.

**Preuve.** [S19] chap. 5 et 6.1 : « Allen Altersklassen gemeinsam ist die Zunahme des Kopfumfanges bzw. das Ausbrechen aus der Perzentile » ; [S2] Diagnosis : « bulging fontanelle, splayed skull sutures, up gaze paresis » ; [S1] CQ-1 : « small-step gait, magnet gait, and broad-based gait »

**Proposition.** propositions/G91_c_semio.html (bouton g91-tab-semio, panneau g91-s-semio, neuf sections data-semiology, figure non anatomique lisible à 390 px, trois cas corrigés) ; propositions/G91_a_semio_clinique.html (section data-semiology-clinical="G91" dans g91-5) ; propositions/G91_pop1_semio.html (six fenêtres g91-sm-*) ; propositions/glossary_g91_ajouts.py.

**Justification.** Mécanisme : sans technique ni valeur du signe, le lecteur ne sait pas passer d’un périmètre crânien ou d’une marche à une hypothèse. Conséquence : l’examen fédéral et la pratique exigent ce passage, et l’enfant dérivé n’est pas examiné. Décision : exigence de Vial du 15.10.2026 ; MAJEUR, bloquant pour la clôture.

### C02 — `chapters/G91/G91_c.html`

**Ancre** : « <b>Corrélation clinique.</b> Un obstacle à l’aqueduc »

**Constat.** tests/audit_sciences.py (base 103745ba) échoue sur les quatre disciplines : anatomie 195 mots, histologie 146, physiologie 153, biochimie 147, pour un minimum de 280 ; aucune ne porte les libellés « Science → clinique. », « Science → examen. », « Science → traitement. », « À retenir. » (encadrés « Corrélation clinique. »).

**Preuve.** [S4] Choroid plexus epithelium : « the ventricular ependymal wall does not serve a secretory function » ; [S2] Box 1 : « The ependyma in humans is not fully developed until 6 months after term birth » ; [S1] Imaging : « even if EI is <0.3 … it is acceptable to diagnose possible iNPH »

**Proposition.** propositions/G91_c_sciences_liens.html (paragraphe sourcé et quatre encadrés par discipline).

**Justification.** Mécanisme : le contrat des sciences vérifie le lien science → décision. Conséquence : la leçon échoue au contrôle automatique et ses sciences restent minces. Décision : compléter et renommer les encadrés.

### C03 — `chapters/G91/G91_c.html`

**Ancre** : « data-s="g91-s-bioch" »

**Constat.** La discipline Génétique est absente alors que l’étiologie congénitale (L1CAM, sténose de l’aqueduc) est citée en g91-4. Le validateur semiology de tools/starter_codex.py exige au moins six boutons data-s : la leçon n’en aurait que cinq avec la sémiologie.

**Preuve.** [S19] chap. 3.7 : « Mutationen in L1CAM-Gen werden bei ca. 10% aller männlichen Patienten mit einer isolierten Form des Hydrozephalus nachgewiesen » ; [S2] Mechanisms : « mutations in L1CAM result in disordered neuronal migration »

**Proposition.** propositions/G91_c_genetique.html (discipline g91-s-gen de 444 mots, figure non anatomique, quatre encadrés, Pareto).

**Justification.** Mécanisme : le mode de transmission fixe le risque familial. Conséquence : un garçon avec pouces en adduction n’est pas orienté vers le conseil génétique. Décision : ajouter la discipline ; condition technique de clôture.

### C04 — `chapters/G91/G91_a.html`

**Ancre** : « aucune recommandation suisse ni européenne spécifique à l’hydrocéphalie n’a pu être lue »

**Constat.** Hiérarchie des sources non respectée pour l’enfant : la ligne directrice européenne S2k AWMF 006-102 « Hydrozephalus im Kindesalter » (sociétés allemandes et autrichiennes, état 17.04.2025) existe et est accessible ; la leçon fonde l’îlot g91-9 et la surveillance de l’enfant sur une revue nord-américaine. Points absents : IRM de référence et scanner réservé à l’urgence, tout symptôme neurologique nouveau chez l’enfant dérivé = dysfonction jusqu’à preuve du contraire avec appel immédiat du neurochirurgien, contrôle au moins annuel du périmètre crânien, indications des cathéters imprégnés, ETV des formes non communicantes.

**Preuve.** [S19] Empfehlung 25 : « Bis zur Falsifizierung soll bei Shuntpatienten bei neu aufgetretener neurologischer Symptomatik eine Shuntfehlfunktion ausgeschlossen werden » ; [S19] Empfehlung 22 : « Die kranielle Computertomografie soll … vor allem der Notfallsituation vorbehalten sein » ; [S19] Empfehlung 24 : « mindestens jährlich »

**Proposition.** propositions/G91_b_1.html (six insertions sourcées dans g91-0, g91-6, g91-7, g91-9, g91-10, g91-11).

**Justification.** Mécanisme : la source européenne applicable prime sur une revue nord-américaine. Conséquence : l’enfant dérivé symptomatique n’a pas de conduite européenne explicite. Décision : intégrer la ligne directrice et corriger l’affirmation de g91-0.

### C05 — `chapters/G91/G91_d.html`

**Ancre** : « Hypertension intracrânienne (enfant, hors AMM) »

**Constat.** Le tableau de g91-p-1 présente l’« hypertension intracrânienne (enfant) » comme un phénotype de l’hydrocéphalie traité par acétazolamide. La source vise l’hypertension intracrânienne idiopathique de l’enfant, maladie distincte ; la ligne directrice européenne n’attend des médicaments aucun succès durable dans l’hydrocéphalie et rapporte un essai randomisé sans bénéfice. Risque : retarder la dérivation d’une hydrocéphalie hypertensive.

**Preuve.** [S2] Management : « Acetazolamide can be used to treat select paediatric patients with idiopathic intracranial hypertension … although the efficacy is limited » ; [S19] 7.1 : « lassen in der Regel keinen dauerhaften Therapieerfolg erwarten » ; [S18] Posologie : « l'administration chez les enfants et les adolescents n'a pas été étudiée »

**Proposition.** propositions/G91_d_1.html, bloc C05 (deux lignes de tableau et un piège).

**Justification.** Mécanisme : l’acétazolamide réduit la sécrétion sans lever l’obstacle. Conséquence : un traitement médical d’attente expose à l’aggravation d’une hypertension intracrânienne. Décision : distinguer l’IIH et écrire que la dérivation est le traitement.

### C06 — `chapters/G91/G91_d.html`

**Ancre** : « 8–10 mg/kg/dose, 3 fois par jour, per os ; maximum 100 mg/kg/jour »

**Constat.** La posologie pédiatrique reprend fidèlement la ligne Swisspeddose, mais sans signaler qu’elle ne fixe aucun plafond absolu : le recalcul (R36) donne 2000 mg/j à 20 kg et 6000 mg/j à 60 kg, au-delà de toutes les doses orales adultes de la FI (≤ 1000 mg/j) ; la même base plafonne l’épilepsie à 1000 mg/j. La leçon omet aussi que la FI n’a pas étudié l’enfant, que l’acétazolamide peut ralentir la croissance, et que SwissPedDose n’est plus mis à jour depuis fin 2025.

**Preuve.** [S18] Swisspeddose : « 8 - 10 mg/kg/dose … 3 … 100 mg/kg/jour » ; [S18] Posologie, Glaucome et Épilepsie : « 250-1000 mg » ; [S18] Effets indésirables : « L'administration d'acétazolamide chez l'enfant peut provoquer un ralentissement de la croissance » ; [S20] SwissPedDose : « dès fin 2025 … ne sont pas mises à jour par l'OFSP »

**Proposition.** propositions/G91_d_1.html, bloc C06 (ligne de tableau, calcul de contrôle, piège).

**Justification.** Mécanisme : une limite par kilogramme croît sans fin avec le poids. Conséquence : chez l’adolescent lourd, la limite autorise une dose six fois supérieure aux doses adultes. Décision : écrire le calcul, l’absence de plafond et la décision spécialisée.

### C07 — `chapters/G91/G91_d.html`

**Ancre** : « l’information professionnelle ne précise pas de fréquence de contrôle dans les passages lus »

**Constat.** Le tableau de g91-p-3 écrit quatre fois « Conduite non détaillée dans le passage lu », alors que la FI suisse datée de juillet 2026 donne la conduite : arrêt immédiat et contre-indication définitive après PEAG ; arrêt, traitement de soutien et aucune réadministration après œdème pulmonaire non cardiogénique ; correction de l’acidose par bicarbonate ; surveillance de la formule sanguine et des électrolytes avant et pendant le traitement. Sont omis les réactions mortelles aux sulfamides (SJS/NET, agranulocytose, anémie aplasique), l’épanchement choroïdien, et les interactions avec phénytoïne, ciclosporine, lithium, diurétiques et digoxine.

**Preuve.** [S18] Mises en garde : « En cas de diagnostic de PEAG, le traitement par acétazolamide doit être interrompu et toute administration ultérieure d'acétazolamide est contre-indiquée » ; [S18] Mises en garde : « La surveillance des cellules sanguines et des niveaux d'électrolytes est recommandée avant le début du traitement, puis régulièrement » ; [S18] Effets indésirables : « On peut remédier à l'acidose métabolique par la prise de bicarbonate »

**Proposition.** propositions/G91_d_1.html, bloc C07 (six lignes de tableau, phrase de surveillance, interactions).

**Justification.** Mécanisme : la FI datée fixe la conduite. Conséquence : un effet grave reste sans conduite dans la leçon. Décision : reprendre la FI.

### C08 — `chapters/G91/G91_b.html`

**Ancre** : « Moins efficace dans cet essai »

**Constat.** Le tableau des dérivations de l’iNPH présente la ventriculocisternostomie comme « moins efficace dans cet essai ». La ligne directrice japonaise juge l’ETV sans efficacité suggérée dans l’hydrocéphalie communicante, signale que l’essai brésilien a pu inclure des formes congénitales tardives et cite une mortalité de 3,2 % contre 0,5 % et des complications de 17,9 % contre 11,8 % dans une comparaison de registre américaine.

**Preuve.** [S1] CQ-10 : « ETV treatment for communicating hydrocephalus with decreased CSF turnover is suggested to have no efficacy » ; [S1] CQ-10 : « a mortality of 3.2% vs. 0.5%, respectively, and surgical complication rates of 17.9% vs. 11.8% »

**Proposition.** propositions/G91_b_etv.html.

**Justification.** Mécanisme : l’ETV contourne un obstacle ; l’iNPH est communicante. Conséquence : présenter l’ETV comme une option moins efficace laisse croire à une alternative. Décision : écrire qu’elle n’est pas retenue dans l’iNPH.

## Constats MINEUR

### C09 — `chapters/G91/G91_b.html`

**Ancre** : « et 92 % des 16 opérés en ont une à 6 semaines. »

**Constat.** Calcul faux (R10) : 92 % de 16 n’est pas un effectif entier (14/16 = 87,5 % ; 15/16 = 93,8 %). La source rapporte 92 % parmi les 12 patients revus à la première consultation postopératoire (11/12 = 91,7 %). Même erreur dans la fenêtre g91-lausanne.

**Preuve.** [S8] Results : « Among the 12 patients seen at the first postoperative consultation » ; [S8] Abstract : « A total of 92% reported gait improvement at 6 weeks »

**Proposition.** propositions/G91_mineurs.html (C09, deux remplacements).

**Justification.** Dénominateur faux sans conséquence décisionnelle ; corriger.

### C10 — `chapters/G91/G91_c.html`

**Ancre** : « révèle 25,7 % de répondeurs supplémentaires »

**Constat.** Calcul faux (R29, R30) : 25,7 % est la part des répondeurs repérés seulement en double tâche (29/113), non un surcroît de 25,7 % par rapport à la marche simple (29/84 = 34,5 %). Même formulation dans g91-marche et pareto-g91-examens.

**Preuve.** [S9] Results : « 25.7% of responders were identified only through dual-task conditions »

**Proposition.** propositions/G91_mineurs.html (C10, trois remplacements).

**Justification.** Lecture du pourcentage ; corriger.

### C11 — `chapters/G91/G91_pop1.html`

**Ancre** : « apathie 70,3 % »

**Constat.** Attribution fausse (R13) : l’apathie de 70,3 % vient d’une enquête japonaise distincte sur les symptômes comportementaux, non de la série de 26 patients ; 70,3 % de 26 n’est pas un effectif entier.

**Preuve.** [S1] Characteristics and evaluation of cognitive impairment : « A BPSD survey conducted in Japan reported that apathy was seen at a rate of 70.3% »

**Proposition.** propositions/G91_mineurs.html (C11).

**Justification.** Attribution ; corriger.

### C12 — `chapters/G91/G91_b.html`

**Ancre** : « rapporte à 1 an une amélioration chez 69 % »

**Constat.** Dénominateur non précisé : les pourcentages de l’étude Eu-iNPH portent sur les 115 patients réexaminés à 12 mois, non sur les 142 inclus (R24 : 81 %).

**Preuve.** [S7] Abstract : « Re-examinations, 12 months after surgery, were performed in 115 patients »

**Proposition.** propositions/G91_mineurs.html (C12, deux remplacements).

**Justification.** Précision méthodologique.

### C13 — `chapters/G91/G91_a.html`

**Ancre** : « Pollakiurie et impériosité 90,9 % »

**Constat.** La source écrit « 90.9% experience urine dribbling » ; « pollakiurie et impériosité » n’est pas ce que dit la version lue. Le caractère d’incontinence par impériosité est, lui, sourcé.

**Preuve.** [S1] Characteristics and evaluation of urinary incontinence : « 90.9% experience urine dribbling, and 74.5% urinary incontinence »

**Proposition.** propositions/G91_mineurs.html (C13).

**Justification.** Fidélité à la source.

### C14 — `chapters/G91/G91_c.html`

**Ancre** : « Technique de mesure non détaillée dans le dossier »

**Constat.** La technique de l’angle calleux et la définition de l’index d’Evans figurent dans la source lue ; la leçon les dit absentes. La leçon ne dit pas non plus qu’un index d’Evans d’au plus 0,3 n’exclut pas l’iNPH (z-EI > 0,42, BVR < 1,0, angle calleux < 90°).

**Preuve.** [S1] Imaging : « measured at the slice through the posterior commissure (PC) and perpendicular to the … AC–PC line » ; [S1] Imaging : « even if EI is <0.3 … it is acceptable to diagnose possible iNPH »

**Proposition.** propositions/G91_mineurs.html (C14, deux remplacements) ; G91_c_sciences_liens.html (anatomie).

**Justification.** Interprétation d’imagerie plus juste.

### C15 — `chapters/G91/G91_c.html`

**Ancre** : « Le drainage continu n’est pas supérieur au tap test »

**Constat.** Surinterprétation : la source dit que la supériorité du drainage continu n’est pas établie, non qu’il n’est pas supérieur.

**Preuve.** [S1] CQ-6 : « It has not been established whether the continuous CSF drainage test is more predictive »

**Proposition.** propositions/G91_mineurs.html (C15, deux remplacements).

**Justification.** Nuance.

### C16 — `chapters/G91/G91_b.html`

**Ancre** : « le drainage est recommandé en cas de baisse de vigilance »

**Constat.** La recommandation ESO présente le drainage en cas de baisse de vigilance comme une déclaration d’experts (résumé grand public ; tableau 3 non lu) ; l’indication clinique ou radiologique est débattue et l’EVD a ses risques propres, non cités.

**Preuve.** [S3] Résumé grand public : « drainage is recommended when there is a reduced level of consciousness » ; [S3] PICO 7 : « there is a debate regarding the indications for EVD placement »

**Proposition.** propositions/G91_mineurs.html (C16).

**Justification.** Nature de la preuve.

### C17 — `chapters/G91/G91_b.html`

**Ancre** : « une pression fixe à 12 cmH2O a produit 9 hyperdrainages sur 34 »

**Constat.** Présentation partielle : l’essai en double aveugle ne montre pas de différence d’efficacité et la ligne directrice juge le réglage initial à 12 cmH2O adéquat ; la dérivation lombo-péritonéale, d’efficacité comparable dans SINPHONI-2 et majoritaire au Japon (55,1 %), est réduite à « alternative ».

**Preuve.** [S1] CQ-13 : « There were no differences in efficacy between the two groups » ; [S1] CQ-13 : « initially setting the pressure at 12 cmH2O is adequate » ; [S1] CQ-10 : « LP shunts for 55.1% »

**Proposition.** propositions/G91_mineurs.html (C17, deux remplacements).

**Justification.** Équilibre de la présentation.

### C18 — `glossary/g91.py`

**Ancre** : « sigle de la base Swisspeddose pour l’usage hors AMM »

**Constat.** Le glossaire définit HARM comme l’usage hors autorisation, sans source. Swisspeddose affiche aussi « HARM » pour des usages autorisés (céfazoline, utilisation générale) ; la base reposait sur des recommandations harmonisées. Le statut hors autorisation de l’acétazolamide pédiatrique découle de la FI (enfants non étudiés).

**Preuve.** [S21] Swisspeddose : « Indication: Utilisation générale … Type d'utilisation: HARM » ; [S20] SwissPedDose : « harmoniser les dosages de 230 substances actives »

**Proposition.** propositions/G91_d_1.html, bloc C18.

**Justification.** Définition non sourcée ; corriger.

### C19 — `chapters/G91/G91_pop2.html`

**Ancre** : « PENS +0,21 m/s à 3 mois »

**Constat.** « +0,21 m/s » (Pareto et paramètres clés de g91-13) présente la différence entre groupes comme un gain absolu (le gain du bras actif est 0,23 m/s) ; 0,23 − 0,03 = 0,20 (R16), la source calcule 0,21 sur des moyennes non arrondies. La leçon mêle aussi mmH2O et cmH2O (R22, R47).

**Preuve.** [S5] Abstract : « resulting in a treatment difference of 0.21 m per second »

**Proposition.** propositions/G91_mineurs.html (C19, trois remplacements).

**Justification.** Arrondi et formulation.

### C20 — `chapters/G91/G91_c.html`

**Ancre** : « Figure 2 — Schéma anatomique simplifié »

**Constat.** Les cinq SVG (viewBox de 640) rendent un texte de 6,7 à 7,3 px à 390 px (mesure Chromium) : illisible sur téléphone. La figure 2, faite de rectangles et d’ellipses, est légendée « schéma anatomique » alors qu’elle n’est qu’un schéma de circulation ; aucune structure anatomique n’est dessinée.

**Preuve.** [S1] — : « Règle de Vial du 15.10.2026 sur les figures anatomiques IA (classement SCHEMA_NON_ANATOMIQUE) »

**Proposition.** propositions/G91_mineurs.html (C20).

**Justification.** Lisibilité et exactitude de la légende.

### C21 — `chapters/G91/G91_d.html`

**Ancre** : « le cathéter à l’argent n’est pas supérieur (5,9 %) »

**Constat.** Les cathéters imprégnés d’antibiotiques sont présentés comme mesure générale ; la ligne directrice européenne en précise les indications et la ligne directrice japonaise rappelle le risque de résistance.

**Preuve.** [S19] Empfehlung 49 : « Antibiotika-beschichtete Shuntsysteme sollen nach Infektionen … und im Rahmen der Erstanlage eingesetzt werden » ; [S1] CQ-12 : « AICs should only be used as required »

**Proposition.** propositions/G91_mineurs.html (C21) ; G91_b_1.html (bloc 5).

**Justification.** Indication précisée.

## Constats ENRICHISSEMENT

### C22 — `chapters/G91/G91_a.html`

**Ancre** : « Aucune donnée suisse d’incidence de l’hydrocéphalie n’a été trouvée »

**Constat.** Rubrique 16 « Spécificités suisses » absente (AI, aptitude à la conduite, remboursement LS/LiMA des valves, carte de valve) ; aucune donnée suisse d’épidémiologie. Seules les études de Lausanne et Bâle sont suisses.

**Preuve.** [S8] Methods : « Lausanne University Hospitals (Switzerland) » ; [S9] Author information : « University Department of Geriatric Medicine FELIX PLATTER, Basel »

**Proposition.** Recherche ciblée à conduire (OFSP, AI, SSN, Swiss Medical Forum) ; aucune proposition rédigée faute de source lue.

**Justification.** Lacune déclarée.

### C23 — `chapters/G91/G91_b.html`

**Ancre** : « Chez le prématuré, des solutions temporaires existent »

**Constat.** Les signes précoces de l’hydrocéphalie post-hémorragique du prématuré (hausse du besoin en oxygène, hyperglycémie, chute de l’hématocrite) et la sémiologie selon l’âge manquent.

**Preuve.** [S19] chap. 5 : « Erhöhung des O2-Bedarfs, Erhöhung des Blutzuckers, Abfall des Hämatokrits »

**Proposition.** propositions/G91_c_semio.html (section urgency) et G91_a_semio_clinique.html.

**Justification.** Situation particulière.

### C24 — `chapters/G91/G91_d.html`

**Ancre** : « L’antibioprophylaxie peropératoire est mentionnée par la ligne directrice japonaise sans autre détail dans le dossier. »

**Constat.** L’antibioprophylaxie de la dérivation est documentée par la FI suisse de la céfazoline et Swisspeddose (30 mg/kg i.v. 30–60 min avant, répétée après 4 h) et par la ligne directrice européenne (30 mg/kg ; PIGS 25 mg/kg).

**Preuve.** [S21] Swisspeddose : « 30 mg/kg/dose … 30 à 60 minutes avant l'intervention, répéter la dose après 4 heures » ; [S19] Empfehlung 39 : « Cefazolin mit 30 mg/KG i.v. als single-shot »

**Proposition.** propositions/G91_d_1.html, bloc C24.

**Justification.** Point pratique documenté.

### C25 — `chapters/G91/G91_c.html`

**Ancre** : « La cognition et la vessie s’améliorent plus tard que la marche. »

**Constat.** Absents : faux négatifs du test de soustraction plus fréquents avec la durée des symptômes ; tests de dynamique du LCS (pression de base, ondes B, résistance à l’écoulement) ; probabilité de réponse quand triade et DESH coexistent.

**Preuve.** [S1] CQ-6 : « the longer the period between appearance of symptoms and CSF drainage, the higher the frequency of false negatives » ; [S1] CQ-8 : « High outflow resistance (Rout) of the CSF measured by infusion test correlates with effective shunt intervention »

**Proposition.** propositions/G91_c_sciences_liens.html (physiologie) et G91_c_semio.html (interprétation).

**Justification.** Examens et interprétation.

### C26 — `chapters/G91/G91_b.html`

**Ancre** : « tous les 3 mois jusqu’à 18 mois »

**Constat.** Le suivi de l’enfant dérivé ne dispose d’aucun rythme européen : la ligne directrice AWMF demande au moins un contrôle annuel du périmètre crânien et du développement, et une carte de valve.

**Preuve.** [S19] Empfehlung 24 : « ab dem Säuglingsalter mindestens jährlich » ; [S19] 7.7 : « Jedes Kind benötigt einen Ventilausweis »

**Proposition.** propositions/G91_b_1.html (bloc 6).

**Justification.** Suivi.

## Calculs (exigence du 16.10.2026)

Le script `calculs/verifier.py` relève par expression régulière toutes les occurrences numériques des sept fichiers, les classe, rapproche chaque grandeur de la citation de sa source et recalcule toutes les grandeurs dérivables. Il est exécuté et conservé ; ses sorties sont `calculs/inventaire.json` et `calculs/resultats.json`.

| Indicateur | Valeur |
|---|---|
| Occurrences relevées | 664 |
| Grandeurs | 438 |
| Identifiants, dates, dénominateurs | 226 |
| Grandeurs concordantes avec la citation de la source | 424 |
| Valeurs de cas fictifs | 13 |
| Grandeurs non rapprochées | 0 |
| Grandeurs calculables | 45 |
| Recalculées | 45 |
| CORRECT | 31 |
| ARRONDI | 11 |
| FAUX | 3 |
| NON_VERIFIABLE | 0 |
| Calculs informatifs de l’audit (absents de la leçon) | 8 |

Les trois résultats faux sont des pourcentages mal rapportés à leur dénominateur, sans conséquence décisionnelle :

- **R10** : 92 % de 16 opérés : 0,92 × 16 = 14,72 ; aucun effectif entier k/16 ne donne 92 % (14/16 = 87,5 ; 15/16 = 93,8) — attendu 93.8, trouvé 92.0. le dénominateur réel est 12 patients revus : 11/12 = 91,7 % ≈ 92 % (voir C08)
- **R13** : 70,3 % attribué à la série de 26 (fenêtre g91-front) : 18/26 = 69,2 ; 19/26 = 73,1 — attendu 69.2, trouvé 70.3. attribution erronée (voir C12)
- **R30** : « répondeurs supplémentaires » rapportés aux répondeurs de marche simple = 29/84 — attendu 34.5, trouvé 25.7. lecture de la phrase de la leçon : 34,5 % attendu (voir C09)

Les arrondis relevés (AVIM 6,25 → 6 % et 12,5 → 12 %, 17,3 → 17 %, série de 26 patients, PENS 0,20 contre 0,21 publié, HR 0,38 contre risque relatif brut 0,37) sont ceux des sources elles-mêmes. Le contrôle de la posologie d’acétazolamide (R34 à R37) confirme 24–30 mg/kg/jour et montre qu’à 100 mg/kg/jour la dose atteint 2000 mg/jour à 20 kg et 6000 mg/jour à 60 kg, au-delà des doses orales adultes de la FI (constat C06). Les vignettes (index d’Evans 0,34 et 0,36, pressions 170 et 180 mmH2O, 40 et 50 mL retirés) respectent les seuils des critères.

## Matrice des 20 rubriques et rubrique 21

| Rang | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g91-0 (deux vignettes, cinq objectifs) |
| 2 | Définition et périmètre CIM-10-GM | couvert | g91-1, g91-cim ; codes conformes à S16 |
| 3 | Classifications et stades | couvert | g91-1 (communicante/obstructive, classification japonaise, CHiA) |
| 4 | Épidémiologie suisse puis européenne | partiel | g91-2 ; aucune donnée suisse ; données suédoises via S1 (C22) |
| 5 | Normal → pathologique | partiel | g91-3 complet ; sciences sous le seuil (C02) |
| 6 | Étiologies et facteurs de risque | partiel | g91-4 ; génétique absente des sciences (C03) |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g91-5 ; fréquences de l’iNPH, aucune chez l’enfant (lacune) |
| 8 | Examen clinique (signes, Se/Sp) | partiel | g91-5 ; aucune technique d’examen de l’enfant ni de la dérivation ; sémiologie absente (C01) |
| 9 | Drapeaux rouges et urgences | partiel | g91-7 alert ; conduite européenne de l’enfant dérivé absente (C04) |
| 10 | Examens complémentaires | couvert | e-1 à e-4 ; nuances C14, C15, C25 |
| 11 | Diagnostic différentiel | couvert | g91-6 (Alzheimer, synucléinopathies, vasculaire) |
| 12 | Prise en charge suisse | partiel | g91-8 (Lausanne), g91-9 ; source européenne pédiatrique absente (C04) ; ETV (C08) ; acétazolamide (C05–C07) |
| 13 | Complications et pronostic | couvert | g91-10, g91-11 |
| 14 | Suivi, prévention, dépistage | partiel | g91-11 ; rythme européen absent (C26) |
| 15 | Situations particulières | partiel | g91-12 ; prématuré sans sémiologie (C23) |
| 16 | Spécificités suisses | absent | aucune (C22) |
| 17 | Critères formels du diagnostic | couvert | g91-13 alert (critères japonais, conformes à S1) |
| 18 | Paramètres clés chiffrés | couvert | g91-13 key ; formulation PENS (C19) |
| 19 | Sous-codes CIM-10-GM couverts | couvert | g91-1 (G91.0 à G91.9) |
| 20 | Points d’examen fédéral | partiel | objectifs de g91-0 ; aucun rattachement PROFILES |
| 21 | Sémiologie fondamentale et analytique | absent | aucun g91-s-semio (C01) |

## 21 — Sémiologie fondamentale et analytique

La leçon ne possède aucun sous-onglet de sémiologie : la barre de l’onglet Sciences compte quatre boutons (anatomie, histologie, physiologie, biochimie). L’îlot g91-5 décrit les signes du nourrisson, de l’enfant et du sujet âgé, mais sans technique d’examen, sans examen de la dérivation, sans mécanisme signe par signe et sans raisonnement analytique. Statut : **absente**, constat C01 MAJEUR, bloquant pour la clôture. La proposition rédigée (`propositions/G91_c_semio.html`) suit le contrat SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE : neuf sections, trois cas corrigés, une figure de raisonnement lisible à 390 px, sources liées passage par passage ; elle est complétée par la section clinique de l’onglet 1, six fenêtres et la discipline de génétique qui porte la barre à six boutons.

| Critère | Résultat |
|---|---|
| SEM-01 | non (aucun data-s g91-s-semio) |
| SEM-02 | non |
| SEM-03 | non (audit_sciences échoue, C02) |
| SEM-04 | oui (test_v7 --static G91 : OK sur la leçon actuelle) |
| SEM-05 | non |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | non |
| SEM-09 | non |
| SEM-10 | non |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | non (pas d’alert sémiologique ; l’alert g91-7 existe) |
| SEM-14 | non |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non (quatre quiz en e-5, aucun sur la valeur d’un signe ou une limite) |
| SEM-18 | non |
| SEM-19 | non évaluable (absente) |
| SEM-20 | non évaluable |
| SEM-21 | non évaluable |
| SEM-22 | non (bouton absent) |
| SEM-23 | non (aucune capture possible) |
| SEM-24 | oui (statut « revue IA, distincte d’une validation médicale humaine » dans chap-head) |

## Figures

Les cinq figures sont des schémas SVG faits de rectangles, d’ellipses et de flèches ; aucune ne dessine une structure anatomique (classement SCHEMA_NON_ANATOMIQUE). Toutes rendent un texte de 6,7 à 7,3 px sur un téléphone de 390 px, ce qui les rend illisibles (C20) ; la figure 2 est légendée à tort « schéma anatomique ».

## Lacunes

- Aucune recommandation ni source de sémiologie suisse : WebSearch « hydrocéphalie à pression normale Revue Médicale Suisse OR Swiss Medical Forum Normaldruckhydrozephalus » sans article suisse.
- Ligne directrice allemande S1 030-063 (Normaldruckhydrozephalus, 2018, « abgelaufen ») : PDF du registre AWMF renvoyé en HTML (anti-robot), page du registre bloquée ; texte non lu.
- ESO 2026 : tableau 3 (recommandations et déclarations de consensus) en image, non lu ; la déclaration PICO 7 n’est lue que dans le résumé grand public.
- Résumés seuls : PENS, BASICS, Eu-iNPH, Bâle, méta-analyse neuropsychiatrique, Pyrgelis, hyperdrainage, Tullberg, Hellström, Fakhry, Carswell, Lancet 2016.
- AWMF 006-102 : les fréquences des graphiques de la série de 107 enfants ne sont pas lisibles dans le texte extrait.
- Aucune sensibilité ni spécificité des signes du nourrisson dans les sources lues ; mécanisme de la parésie du regard vers le haut non détaillé.
- Spécificités suisses (AI, aptitude à la conduite, remboursement LS/LiMA) : non recherchées dans cet audit faute de source ciblée identifiée.
- Recommandation PIGS (2005) lue seulement par citation de l’AWMF ; développement littéral de HARM non publié dans les sources lues.
- BfArM et page OFSP SwissPedDose lus par un outil de synthèse (citations limitées).
- Captures SEM-22 et SEM-23 impossibles : aucune sémiologie publiée.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G91 — Hydrocéphalie (S08, Neurologie) |
| Catégories traitées | G91.0, G91.1, G91.20, G91.21, G91.29, G91.3, G91.8, G91.9 |
| Fichiers audités | 7 (empreintes conformes) |
| Contrôles | test_v7 --static OK ; audit_sciences en échec (C02) ; rendu Chromium 390 px |
| Sources lues | 22 (dont 7 en texte intégral : S1, S2, S3, S4, S8, S18, S19) |
| Constats | 8 MAJEUR, 13 MINEUR, 5 ENRICHISSEMENT, 0 BLOQUANT |
| Calculs | 664 relevés ; 45 calculables, 45 recalculés ; 31 corrects, 11 arrondis, 3 faux |
| Propositions | 10 fichiers dans `propositions/` |
| Alertes | Sémiologie absente ; génétique absente ; acétazolamide (IIH, plafond, conduite FI) ; ETV dans l’iNPH ; ligne directrice européenne pédiatrique non utilisée |
