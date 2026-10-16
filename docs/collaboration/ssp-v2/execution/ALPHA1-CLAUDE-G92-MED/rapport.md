# Audit médical ALPHA77 — G92 Encéphalopathie toxique (S08, Neurologie)

Mission `ALPHA1-CLAUDE-G92-MED`, branche `claude/alpha1/g92-med-g1`, base `103745ba` (instantané des sources `523832d9`). Exécutant : sous-agent Claude Code (voir accusé issue 107) ; modèle et effort conformes au manifeste. Du 2026-10-16T09:52:37Z au 2026-10-16T10:23:48Z. Les sept fichiers lus ont des empreintes SHA-256 conformes au manifeste.

## Synthèse

La leçon est solide sur le cœur de l’ICANS : la classification CIM-10-GM, la grille du consensus, les chiffres de l’information professionnelle de Yescarta et du tocilizumab sont exacts. Trois erreurs touchent pourtant la décision. La décroissance de méthylprednisolone du grade 4 perd la mention « toutes les 12 heures » pour 125 et 60 mg, ce qui divise la dose par deux à la lecture. La grille des paramètres clés range tout ICE à 0 en grade 4, alors qu’un patient éveillé avec aphasie globale reste en grade 3. Les contre-indications du valproate sont sous-évaluées : POLG est une contre-indication, non une prudence. La sémiologie fondamentale et analytique manque, les sciences échouent au contrôle automatique, et les posologies de l’ICANS ne disent pas qu’elles sont hors indication suisse.

| BLOQUANT | MAJEUR | MINEUR | ENRICHISSEMENT |
|---|---|---|---|
| 0 | 7 | 13 | 4 |

**Les trois constats les plus graves.**

1. **C02** — Méthylprednisolone au grade 4 : 125 et 60 mg sans « toutes les 12 heures » (G92_b, G92_d, G92_pop2) ; cumul lu 1370 mg au lieu de 1740 mg (recalcul R08).
2. **C03** — « Grade 4 = 0 ou non évaluable » : l’ICE à 0 d’un patient éveillé et aphasique est un grade 3 selon le consensus (R06).
3. **C04** — Valproate : mutations de POLG, déficit primaire en carnitine et grossesse sont des contre-indications de la FI suisse ; la leçon écrit « prudence » et déclare la grossesse « non abordée ».

## Constats MAJEUR

### C01 — `chapters/G92/G92_c.html`

**Ancre** : `data-s="g92-s-immuno"` (1 occurrence).

**Constat.** Le sous-onglet « Sémiologie fondamentale et analytique » est absent. Décompte réel des boutons data-s du panneau pS de G92_c.html : 4 (g92-s-immuno, g92-s-neuro, g92-s-bioch, g92-s-imagerie) ; aucun g92-s-semio, aucun marqueur data-semiology ni data-semiology-clinical. La sémiologie existante (g92-5, g92-6, g92-ecriture) est descriptive : aucune technique de geste, aucun mécanisme par signe, aucune valeur chiffrée, aucun raisonnement analytique ni cas corrigé de sémiologie.

**Preuve.** [S3] description clinique ; tableau 5 : « The earliest manifestations of ICANS are tremor, dysgraphia, mild difficulty with expressive speech » ; [S3] description clinique : « developing in 19 of 22 patients who went on to develop severe neurotoxicity » ; [S2] § 10, Key surveillance points : « ICE screening every 8–12 hours during the first 7 days; handwriting test at each neurological assessment »

**Proposition.** propositions/G92_c_semio.html (bouton g92-tab-semio, panneau g92-s-semio, neuf sections data-semiology, trois cas corrigés, figure non anatomique de 11,9 px à 390 px) ; propositions/G92_pop1_semio.html (six fenêtres g92-sm-*, dans _pop1) ; propositions/G92_a_semio_clinique.html (section data-semiology-clinical="G92" dans pA, îlot g92-6) ; propositions/glossary_g92_ajouts.py. Simulation : validateur semiology de tools/starter_codex.py satisfait (6 boutons, titre exact, 9 sections, liens https, marqueur clinique).

**Justification.** Mécanisme : sans technique d’examen ni lecture du signe vers le grade, le lecteur ne sait pas transformer une dysgraphie ou une aphasie en décision. Conséquence : le grade, donc la corticothérapie, est mal fixé. Décision : exigence de Vial du 15.10.2026 (contrat SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE) ; absence = MAJEUR, bloquant pour la clôture du cours.

### C02 — `chapters/G92/G92_b.html`

**Ancre** : `125 mg pendant 2 jours, 60 mg pendant 2 jours ; osmothérapie` (1 occurrence).

**Constat.** Décroissance de méthylprednisolone au grade 4 mal transcrite : la source prévoit 250 mg, puis 125 mg, puis 60 mg toutes les 12 heures pendant 2 jours chacun ; la leçon écrit « toutes les 12 heures » pour 250 mg seulement. Lue littéralement, la dose quotidienne est divisée par deux pour 125 et 60 mg (cumul de la décroissance 1370 mg au lieu de 1740 mg ; recalcul R08, verdict FAUX). Même erreur en G92_d.html (g92-p-2) et G92_pop2.html (g92-methylpred).

**Preuve.** [S2] tableau 3, grade 4 : « taper at 250 mg every 12 hrs for 2 days, then 125 mg every 12 hrs for 2 days, then 60 mg every 12 hrs for 2 days »

**Proposition.** propositions/G92_remplacements.json P01, P02, P03 : « puis 125 mg toutes les 12 heures pendant 2 jours, puis 60 mg toutes les 12 heures pendant 2 jours ».

**Justification.** Mécanisme : une décroissance trop rapide des corticoïdes après un grade 4 expose à la récidive de la neurotoxicité. Conséquence : sous-dosage de moitié sur quatre jours. Décision : corriger les trois occurrences ; pas de surdosage, donc MAJEUR et non BLOQUANT.

### C03 — `chapters/G92/G92_b.html`

**Ancre** : `grade 3 = 0 à 2, grade 4 = 0 ou non évaluable.` (1 occurrence).

**Constat.** Grille ICE mal formulée dans les paramètres clés (div.key de g92-12) : « grade 4 = 0 ou non évaluable » classe tout ICE à 0 en grade 4. Le consensus classe l’ICE à 0 d’un patient éveillé avec aphasie globale en grade 3, et réserve le grade 4 au patient inaccessible incapable de passer l’ICE (recalcul R06, FAUX). Le piège de g92-6 (« très bas ou non évaluable ») ne tranche pas ; les formulations de g92-e-2 et g92-ice sont exactes mais muettes sur ce cas.

**Preuve.** [S3] tableau 6, note ^ : « A patient with an ICE score of 0 may be classified as having Grade 3 ICANS if the patient is awake with global aphasia » ; [S3] tableau 6 : « 0 (patient is unarousable and unable to perform ICE) »

**Proposition.** propositions/G92_remplacements.json P04 (g92-12), P05 (g92-6), P06 (g92-e-2), P07 (g92-ice).

**Justification.** Mécanisme : l’aphasie globale éveillée annule l’ICE sans coma. Conséquence : le surclassement en grade 4 impose à tort la méthylprednisolone à 1 g et l’osmothérapie, ou masque la nuance d’examen. Décision : grille du consensus, score mal compté = MAJEUR (EXIGENCE_CALCULS § 3).

### C04 — `chapters/G92/G92_pop2.html`

**Ancre** : `<p>Déficit du cycle de l’urée ; prudence avec mutations de POLG.</p>` (1 occurrence).

**Constat.** Contre-indications du valproate incomplètes et inexactes : l’information professionnelle classe les maladies mitochondriales connues dues à des mutations de POLG (et l’enfant de moins de 2 ans suspect d’une telle maladie) en contre-indication, non en « prudence » ; le déficit systémique primaire en carnitine non corrigé et la grossesse (hors absence d’alternative) sont aussi des contre-indications absentes de la leçon. g92-11 déclare que la grossesse n’est « pas abordée » alors que la source lue par la leçon la contre-indique.

**Preuve.** [S8] Contre-indications : « Patients connus pour avoir des maladies mitochondriales causées par des mutations du gène nucléaire codant pour l'enzyme mitochondriale polymérase gamma (POLG » ; [S8] Contre-indications : « Patients présentant une déficience systémique primaire en carnitine sans correction de ce déficit » ; [S8] Contre-indications : « Chez les femmes enceintes, sauf si aucune alternative thérapeutique ne rentre en ligne de compte »

**Proposition.** propositions/G92_remplacements.json P09 (g92-valproate), P10 (g92-3), P11 (g92-11, grossesse) ; P33 (sciences).

**Justification.** Mécanisme : POLG et déficit en carnitine aggravent l’atteinte mitochondriale et l’hyperammoniémie que le valproate provoque. Conséquence : risque d’insuffisance hépatique fatale et d’encéphalopathie. Décision : FI suisse datée (septembre 2025) ; contre-indication sous-évaluée = MAJEUR.

### C05 — `chapters/G92/G92_d.html`

**Ancre** : `<td>Jusqu’à 12 mg/kg/jour, typiquement 800 mg/jour par voie intraveineuse</td>` (1 occurrence).

**Constat.** Posologies de l’ICANS présentées sans statut réglementaire suisse : dexaméthasone, méthylprednisolone, anakinra i.v. et triple intrathécale viennent d’une revue européenne ; l’ICANS n’est l’indication d’aucune information professionnelle suisse lue. Aucune FI suisse d’anakinra n’a été retrouvée sur AmiKo (« Kineret », « anakinra », 16.10.2026). Les règles d’administration de Solu-Medrol (doses > 250 mg en ≥ 30 minutes ; lésions hépatiques à partir d’environ 1 g/j ; fortes doses normalement ≤ 48–72 h) sont absentes (R29, NON_VERIFIABLE). Les recalculs arithmétiques sont exacts (R10, R11, R12).

**Preuve.** [S2] § 5.4, srICANS : « High-dose IV anakinra (up to 12 mg/kg/day, typically 800 mg/day) » ; [S10] Posologie : « celle de doses supérieures à 250 mg, de 30 minutes au minimum » ; [S10] Mises en garde : « Lorsque la méthylprednisolone était utilisée à des doses élevées (généralement à partir d'1 g par jour), des lésions hépatiques » ; [S11] Posologie : « administrer la dose initiale de 40 à 100 mg i.v. »

**Proposition.** propositions/G92_d_1.html (tableau « Ce que dit l’information professionnelle suisse » et tableau de dose du céfépime).

**Justification.** Mécanisme : une dose citée par une revue n’engage pas l’autorisation suisse. Conséquence : le lecteur peut croire ces schémas approuvés et ignorer la durée de perfusion et la surveillance hépatique. Décision : loi 3 du PROMPT_VERITE (médicament = FI suisse datée) ; point décisionnel non sourcé = MAJEUR.

### C06 — `chapters/G92/G92_b.html`

**Ancre** : `puis une dose de charge de lévétiracétam. Un état de mal exige un avis neurologique urgent.` (1 occurrence).

**Constat.** Le lévétiracétam est proposé en dose de charge pour les crises et à l’approche de l’état de mal, sans signaler que l’information professionnelle suisse de Keppra en perfusion déclare son efficacité non démontrée dans l’état de mal épileptique et ne l’y recommande pas. Même omission dans le tableau de g92-9 (« lorazépam puis lévétiracétam en cas de crise ») et g92-p-1.

**Preuve.** [S12] Mises en garde, État de mal épileptique : « L'efficacité pour le traitement de l'état de mal épileptique n'a pas été démontrée » ; [S2] tableau 3, grade 3 : « Treat seizures with lorazepam IV or other benzodiazepines as needed, followed by loading with levetiracetam »

**Proposition.** propositions/G92_remplacements.json P12 ; propositions/G92_d_1.html (ligne lévétiracétam).

**Justification.** Mécanisme : la FI suisse fixe le cadre d’usage. Conséquence : un état de mal traité par un produit non recommandé sans décision neurologique explicite. Décision : signaler la divergence et confier le choix au neurologue ; MAJEUR.

### C07 — `chapters/G92/G92_c.html`

**Ancre** : `<div class="key"><b>Corrélation clinique.</b> Une écriture dégradée est un signe précoce` (1 occurrence).

**Constat.** tests/audit_sciences.py (base 103745ba) échoue : les quatre disciplines comptent 219, 166, 122 et 123 mots (seuil 280) et aucune ne porte les quatre libellés « Science → clinique. », « Science → examen. », « Science → traitement. », « À retenir. » (20 erreurs). Les sciences ne présentent pas le fonctionnement normal du cerveau ni la pharmacocinétique qui explique l’accumulation. Avec la seule sémiologie, la barre compterait 5 boutons ; le validateur semiology en exige 6.

**Preuve.** [S6] Pharmacocinétique : « Cela indique que la céfépime est presque exclusivement éliminée par voie rénale » ; [S7] Interactions : « L’inhibition du CYP3A4 peut aussi entraîner la formation accrue d’un métabolite d’ifosfamide associé à des effets toxiques sur le SNC »

**Proposition.** propositions/G92_c_pharmacocinetique.html (sixième discipline, 557 mots) ; propositions/G92_remplacements.json P31 à P37 (quatre libellés par discipline et paragraphes sourcés). Simulation de toutes les propositions : audit_sciences « passed » (345, 346, 304, 291, 557 et 2680 mots), test_v7 --static G92 « OK » après conversion des repères [Sx].

**Justification.** Mécanisme : sans corrélations explicites, la science ne guide ni l’examen ni le traitement. Conséquence : contrôle automatique en échec et contrat Temps Betta non tenu. Décision : MAJEUR.

## Constats MINEUR

### C08 — `chapters/G92/G92_b.html`

**Ancre** : `L’IRM (ou à défaut le scanner) est demandée en cas de grade 3 ou plus.` (1 occurrence).

**Constat.** Indication de l’IRM restreinte au grade 3 ou plus ; la source la demande aussi devant un signe focal, une crise ou une absence d’amélioration, et son calendrier de surveillance la prévoit dès le grade 2 ou devant tout nouveau signe neurologique. Même restriction en g92-e-1.

**Preuve.** [S2] § 5.4 : « brain MRI should be obtained whenever focal signs, seizures, or failure to improve raise the possibility of a structural or alternative cause » ; [S2] tableau 7 : « Brain MRI if ICANS ≥ G2 or new neurological signs »

**Proposition.** propositions/G92_remplacements.json P13, P14.

**Justification.** Mécanisme : un signe focal évoque une lésion structurelle. Conséquence : retard d’imagerie au grade 2. Décision : MINEUR (la leçon prévoit déjà l’imagerie pour exclure d’autres causes).

### C09 — `chapters/G92/G92_b.html`

**Ancre** : `et la proximité du centre pendant au moins deux semaines.` (1 occurrence).

**Constat.** Le cadre suisse (FI : 7 jours de surveillance quotidienne, 2 semaines de proximité) est exact, mais la pratique européenne rapportée par la revue (14 jours d’hospitalisation selon le manuel EBMT-EHA ; environ 4 semaines près du centre avec un proche) n’est pas mentionnée.

**Preuve.** [S4] Posologie/Mode d'emploi : « Les patients doivent rester à proximité d'un centre de traitement qualifié ou d'un établissement clinique disposant d'un personnel adéquatement formé pendant au moins 2 semaines » ; [S2] § 10 : « patients are generally advised to remain close to the treating center with a caregiver for approximately four weeks given the risk of late ICANS »

**Proposition.** propositions/G92_remplacements.json P15.

**Justification.** Mécanisme : l’ICANS tardif survient au-delà de 2 semaines. Conséquence : planification de sortie. Décision : MINEUR, la FI restant le minimum réglementaire.

### C10 — `chapters/G92/G92_c.html`

**Ancre** : `Le barème des points par item n’a pas été lu dans une source accessible et n’est pas reproduit ici.` (1 occurrence).

**Constat.** La leçon déclare le barème du score ICE « non lu », alors que la source qu’elle cite comme lue en texte intégral (consensus ASTCT) le donne : orientation 4, dénomination 3, ordres 1, écriture 1, attention 1 (total recalculé 10, R07). Même mention en g92-ice.

**Preuve.** [S3] tableau 5 : « Orientation: Orientation to year, month, city, hospital: 4 points »

**Proposition.** propositions/G92_remplacements.json P06, P08.

**Justification.** Mécanisme : le barème permet de coter et de comparer. Conséquence : lacune déclarée à tort. Décision : MINEUR.

### C11 — `chapters/G92/G92_b.html`

**Ancre** : `méthylprednisolone 1000 mg par jour pendant 3 jours puis décroissance rapide ;` (1 occurrence).

**Constat.** Grade 3 : la condition « jusqu’à amélioration au grade 1 » et l’exemple de décroissance (250, 125 puis 60 mg, un jour chacun) manquent (R09, ARRONDI) ; la durée de perfusion d’un bolus de 1000 mg n’est donnée nulle part (R29).

**Preuve.** [S2] tableau 3, grade 3 : « methylprednisolone 1000 mg/day for 3 days until improvement to Grade 1 »

**Proposition.** propositions/G92_remplacements.json P16 ; propositions/G92_d_1.html.

**Justification.** Mécanisme et conséquence : schéma incomplet sans erreur de dose. Décision : MINEUR.

### C12 — `chapters/G92/G92_a.html`

**Ancre** : `dont le débit de filtration glomérulaire estimé est de 24 mL/min/1,73 m², reçoit du céfépime à dose standard pour une pneumonie.` (1 occurrence).

**Constat.** Vignette du céfépime incalculable : l’information professionnelle adapte la dose à la clairance de Cockcroft (mL/min), que ni le poids ni la créatinine de l’énoncé ne permettent de calculer ; le DFGe normalisé n’est pas la grandeur de l’IP (R13, R14 NON_VERIFIABLE). Le tableau de dose de l’IP manque à la leçon.

**Preuve.** [S6] Posologie : « La clairance de la créatinine peut être déterminée approximativement au moyen de l'équation de Cockcroft »

**Proposition.** propositions/G92_remplacements.json P17 (65 kg, créatinine 220 µmol/L : Cockcroft-Gault 21,1 mL/min, DFGe CKD-EPI 2021 25,2 ; 1 g/24 h contre 4 g/j, recalcul R36) ; propositions/G92_d_1.html (tableau de l’IP).

**Justification.** Mécanisme : la dose dépend de la clairance réelle, non normalisée. Conséquence : exemple inutilisable pour décider. Décision : énoncé incomplet = MINEUR.

### C13 — `chapters/G92/G92_pop2.html`

**Ancre** : `<p>Dans 85 % des cas d’une série de 73 patients, résolution en 1 à 5 jours.</p>` (1 occurrence).

**Constat.** Dénominateurs faux : dans la revue de 73 cas, 71 % (début aux jours 2 à 5) et 85 % (résolution aux jours 1 à 5) portent chacun sur 29 cas, donc sur environ 41 et 34 cas documentés, non sur 73 (R15, FAUX). Même ambiguïté en g92-2.

**Preuve.** [S14] résumé : « Most cases of cefepime-induced neurotoxicity occurred between days two and five (n=29, 71%) »

**Proposition.** propositions/G92_remplacements.json P18, P19.

**Justification.** Mécanisme : un pourcentage sans dénominateur surestime la précision. Décision : MINEUR.

### C14 — `chapters/G92/G92_b.html`

**Ancre** : `le tocilizumab donné une heure avant la perfusion chez 26 patients de 70 ans et plus` (1 occurrence).

**Constat.** Effectifs faux : à Zurich, seuls 7 des 26 patients ont reçu le tocilizumab prophylactique, contre 19 témoins (R17, FAUX) ; même erreur en g92-tocilizumab. Le registre CIBMTR : les 95 % de début avant le jour 15 portent sur 150 patients dont la date est connue, non sur les 877 (R18, FAUX).

**Preuve.** [S16] résumé : « comparing those who received prophylactic Tocilizumab (N = 7) versus standard treatment (N = 19) » ; [S17] résumé : « Of 150 patients with reported onset date, 95% had onset ≤day 15 after infusion »

**Proposition.** propositions/G92_remplacements.json P20, P21, P22.

**Justification.** Mécanisme : un effectif gonflé donne un faux poids à une série minuscule. Décision : MINEUR (aucune recommandation n’en découle).

### C15 — `chapters/G92/G92_a.html`

**Ancre** : `et les formes de grade 3 ou plus concernent 3 à 30 % d’entre eux, selon le produit.` (1 occurrence).

**Constat.** La fourchette « 20 à 60 % » (et « 3 à 30 % » pour le grade ≥ 3) est contredite par le tableau qu’elle introduit : axicabtagène 64 %, brexucabtagène 69 %, idécabtagène 18 % ; grade ≥ 3 : 28–32 % et 31 % (R19). L’incohérence vient de la source, reprise sans le signaler ; même phrase dans le Pareto.

**Preuve.** [S2] § 5.1 et tableau 1 : « ICANS occurs in 20–60% of all CAR-T recipients »

**Proposition.** propositions/G92_remplacements.json P23.

**Justification.** Décision : signaler l’écart ; MINEUR.

### C16 — `chapters/G92/G92_b.html`

**Ancre** : `dans la population de comparaison citée, que le dossier ne précise pas.` (1 occurrence).

**Constat.** Deux paraphrases inexactes de la FI Yescarta : la population de comparaison de l’œdème cérébral est précisée (« LDGCB et d’autres indications ») ; les 3,6 % sont 10 patients morts « pour des raisons qui n’étaient pas en rapport » avec les effets neurologiques, non « sans lien avec le traitement » (R20, R21 exacts sur les chiffres).

**Preuve.** [S4] Mises en garde : « par rapport à 0,7% au total (0,2% de cas fatals) chez les patients atteints de LDGCB et d'autres indications » ; [S4] Effets indésirables : « à l'exception de 10 patients (3,6% des patients traités par YESCARTA dans ZUMA-1 et ZUMA-7) »

**Proposition.** propositions/G92_remplacements.json P24, P25.

**Justification.** Décision : MINEUR.

### C17 — `chapters/G92/G92_a.html`

**Ancre** : `Il s’agit d’un raisonnement déduit de ces deux données, non d’une affirmation de la source.` (1 occurrence).

**Constat.** L’élimination rénale du céfépime est présentée comme une déduction de l’auteur ; l’information professionnelle l’affirme et donne la pharmacocinétique (clairance rénale 110 sur 120 mL/min, t½ 1,7 h, 13 h chez le dialysé).

**Preuve.** [S6] Pharmacocinétique : « La demi-vie moyenne chez les patients dialysés est de 13 h lors d'hémodialyse »

**Proposition.** propositions/G92_remplacements.json P26 ; propositions/G92_c_pharmacocinetique.html.

**Justification.** Décision : MINEUR.

### C18 — `chapters/G92/G92_a.html`

**Ancre** : `L’inflammation cytokinique explique le calendrier de l’ICANS (début vers le jour 5, pic des cytokines aux jours 7 à 14)` (1 occurrence).

**Constat.** Lien causal non soutenu : le début des signes (jour 5 environ) précède le pic des cytokines (jours 7 à 14) ; la source décrit une corrélation avec l’expansion des CAR-T, non une explication du calendrier. Même formulation en g92-s-immuno-cours.

**Preuve.** [S2] § 3 : « Peak cytokine levels typically occur within 7–14 days of infusion and correlate with CAR-T in vivo expansion kinetics »

**Proposition.** propositions/G92_remplacements.json P27, P28.

**Justification.** Mécanisme : association temporelle ≠ causalité (consigne de Vial du 07.10.2026). Décision : MINEUR.

### C19 — `chapters/G92/G92_a.html`

**Ancre** : `href="https://amiko.oddb.org (GTIN 7680669860011)"` (4 occurrences).

**Constat.** 49 liens vers les informations professionnelles ont un href invalide (espace et parenthèse : « https://amiko.oddb.org (GTIN …) ») dans les six fichiers HTML ; le lecteur n’atteint pas la monographie.

**Preuve.** [tools/swissmedic_fi.py] fonction texte (adresse réelle d’une IP sur AmiKo) : « page = get(f"{BASE}/{lang}/fi?gtin={urllib.parse.quote(gtin)}") »

**Proposition.** propositions/G92_remplacements.json G01 à G06 (remplacement global par https://amiko.oddb.org/fr/fi?gtin=<GTIN>).

**Justification.** Décision : MINEUR (traçabilité des sources).

### C20 — `chapters/G92/G92_a.html`

**Ancre** : `font-size="14"><defs><marker id="g92-ar1"` (1 occurrence).

**Constat.** Les six figures SVG (schémas non anatomiques, viewBox de 640 de large, police de 14 unités) rendent un texte de 7,8 px à 390 px (mesure Chromium, conteneur 358 px), sous le seuil de lisibilité retenu par les audits précédents ; aucun débordement.

**Preuve.** [AUDIT] controles.rendu_390px (Chromium headless, conteneur 358 px) : « police_rendue_px 7,8 pour les six figures ; viewBox 640, font-size 14 »

**Proposition.** Redessiner sur une largeur de 360 unités avec une police de 12 unités (11,9 px rendus), comme les deux figures proposées, ou porter la police à 24 unités en élargissant les cadres.

**Justification.** Décision : MINEUR (forme).

## Constats ENRICHISSEMENT

### C21 — `chapters/G92/G92_b.html`

**Ancre** : `Ils imposent les soins intensifs, l’avis d’un neurologue et un traitement immédiat, sans attendre le bilan complet.</div>` (1 occurrence).

**Constat.** Rubrique 16 (spécificités suisses) partielle : Tox Info Suisse (145, 24 h sur 24) n’est pas cité pour une catégorie consacrée aux encéphalopathies toxiques ; aucune donnée suisse sur les centres CAR-T ou le remboursement n’a été lue (lacune).

**Preuve.** [S29] page d’accueil : « Notfall Telefon 145 (24/7) »

**Proposition.** propositions/G92_remplacements.json P29 ; alerte de la sémiologie (G92_c_semio.html, g92-sm-7).

**Justification.** Décision : ENRICHISSEMENT.

### C22 — `chapters/G92/G92_pop2.html`

**Ancre** : `le bleu de méthylène peut être envisagé (posologie non lue).</p>` (1 occurrence).

**Constat.** La FI d’Holoxan contient des données utiles absentes : encéphalopathie très fréquente (10–20 %), récidive possible après plusieurs cycles sans incident, majoration du métabolite neurotoxique par les inhibiteurs du CYP3A4, hémodialyse rapide en cas de surdosage.

**Preuve.** [S7] Effets indésirables : « Très fréquent : Encéphalopathie (10-20%) » ; [S7] Mises en garde : « Une récidive d'encéphalopathie-toxicité du SNC après plusieurs cycles de traitement sans incident a été rapportée »

**Proposition.** propositions/G92_remplacements.json P30.

**Justification.** Décision : ENRICHISSEMENT.

### C23 — `chapters/G92/G92_a.html`

**Ancre** : `<b>Vigilance</b> : éveil spontané, à la voix, au seul stimulus tactile, stupeur ou coma.` (1 occurrence).

**Constat.** Pour G92.9 (encéphalopathie médicamenteuse du sujet âgé), aucun outil de dépistage du délire n’est proposé : le score ICE n’est validé que pour l’ICANS. Le 4AT (sensibilité 0,88, spécificité 0,88 chez les 65 ans et plus) et le score FOUR en cas de coma (EAN) manquent.

**Preuve.** [S24] résumé : « The pooled sensitivity was 0.88 » ; [S26] résumé : « use the Full Outline of Unresponsiveness score instead of the Glasgow Coma Scale in the acute setting »

**Proposition.** propositions/G92_c_semio.html (g92-sm-2, g92-sm-4) ; propositions/G92_pop1_semio.html (g92-sm-4at, g92-sm-vigilance) ; propositions/G92_a_semio_clinique.html.

**Justification.** Décision : ENRICHISSEMENT.

### C24 — `chapters/G92/G92_a.html`

**Ancre** : `faute de source lue.</p>` (1 occurrence).

**Constat.** Rubrique 6 partielle : lithium, monoxyde de carbone, solvants, métaux lourds et encéphalite sous inhibiteurs de points de contrôle ne sont pas traités (lacune déclarée par la leçon). L’audit n’a pas lu de source sur ces agents : aucune proposition de contenu n’est faite.

**Preuve.** [S20] résumé : « drugs of abuse, and environmental toxins »

**Proposition.** Mission de production dédiée : lire la FI suisse du lithium, une source de Tox Info Suisse et une recommandation européenne sur l’intoxication au monoxyde de carbone avant toute rédaction.

**Justification.** Décision : ENRICHISSEMENT, sans contenu inventé.

## Calculs (exigence du 16.10.2026)

Toutes les grandeurs des sept fichiers ont été relevées par script (`calculs/verifier.py`, exécuté et conservé) ; chaque grandeur est rapprochée d’une citation exacte de la source lue, et chaque citation a été retrouvée mot pour mot dans la copie locale du texte de la source.

| Indicateur | Valeur |
|---|---|
| Occurrences relevées | 537 |
| Grandeurs | 330 |
| Identifiants, dates, numéros | 129 |
| Libellés de grade (contrôlés par R01–R06, R26) | 78 |
| Grandeurs concordantes avec la citation de la source | 307 |
| Valeurs de cas fictifs et unités | 23 |
| Grandeurs non rapprochées | 0 |
| Grandeurs calculables de la leçon | 30 |
| Recalculées | 30 |
| CORRECT | 20 |
| ARRONDI | 2 |
| FAUX | 5 |
| NON_VERIFIABLE | 3 |
| Calculs informatifs de l’audit (valeurs des propositions) | 6 |
| Citations retrouvées mot pour mot | 96/96 |

| Recalcul | Objet | Attendu | Trouvé | Verdict |
|---|---|---|---|---|
| R01 | ICE 8, éveil spontané → grade selon ASTCT | 1 | 1 | CORRECT |
| R02 | ICE 8 + crise clinique brève → paramètre le plus sévère | 3 | 3 | CORRECT |
| R03 | ICE 5, éveil à la voix | 2 | 2 | CORRECT |
| R04 | ICE 4, éveil à la voix, sans crise | 2 | 2 | CORRECT |
| R05 | Conduite du grade 1 | "soins de support + ICE deux fois par jour" | "réponse B" | CORRECT |
| R06 | grade_ice(0, éveillé) = 3 ; grade_ice(0, inaccessible) = 4 | "ICE 0 éveillé → grade 3 ; ICE 0 inaccessible → grade 4" | "« grade 4 = 0 ou non évaluable »" | FAUX |
| R07 | orientation 4 + dénomination 3 + exécution d'ordres 1 + écriture 1 + attention 1 | 10 | 10 | CORRECT |
| R08 | cumul = 1000×3 + (250×2/j)×2 + (125×2/j)×2 + (60×2/j)×2 ; lecture littérale de la leçon :  | 4740 | 4370 | FAUX |
| R09 | Schéma du grade 3 | "1000 mg/j × 3 j jusqu'à amélioration au grade 1, puis 250–125–60 mg u | "1000 mg/j × 3 j puis décroissance rapide" | ARRONDI |
| R10 | 10–20 mg toutes les 6 h → 4 prises/j → 40–80 mg/j | [40, 80] | [40.0, 80.0] | CORRECT |
| R11 | 8 mg/kg plafonné à 800 mg → plafond atteint à 800/8 = 100 kg ; 12 mg/kg sous 30 kg reste < | {"poids_plafond_kg": 100, "dose_29_9_kg_mg": 358.8, "doses_max": 4} | {"poids_plafond_kg": 100.0, "dose_29_9_kg_mg": 358.8, "doses_max": 4} | CORRECT |
| R12 | 800 / 12 = 66,7 kg | "800 mg/j ≤ 12 mg/kg/j si poids ≥ 66,7 kg" | 66.7 | CORRECT |
| R13 | Exemple chiffré proposé : homme 82 ans, 65 kg, créatinine 220 µmol/L → Cockcroft-Gault 21. | "dose d'entretien selon la clairance de Cockcroft (IP)" | "« DFGe 24 mL/min/1,73 m², dose standard »" | NON_VERIFIABLE |
| R14 | Cas 1 de g92-e-2 : la réponse B (« réviser la dose en fonction de la fonction rénale ») re | "clairance de Cockcroft nécessaire" | "« DFG 25 mL/min/1,73 m² »" | NON_VERIFIABLE |
| R15 | n = 29 / proportion → 29/0,71 = 40,8 ; 29/0,85 = 34,1 | {"denominateur_debut": 73, "denominateur_resolution": 73} | {"denominateur_debut": 40.8, "denominateur_resolution": 34.1} | FAUX |
| R16 | 14/40 et 10/40 ; effectif total 80 | [0.35, 0.25, 80] | [0.35, 0.25, 80] | CORRECT |
| R17 | 7 + 19 = 26 ; 7/26 = 26,9 % seulement ont reçu le tocilizumab | {"traites_par_tocilizumab": 7, "temoins": 19} | {"traites_par_tocilizumab": 26} | FAUX |
| R18 | 27 % × 877 = 237 ICANS ; date de début connue pour 150 (63 %) ; 95 % portent sur ces 150 | {"denominateur_95_pct": 150} | {"denominateur_implicite": 877, "icans_estimes": 237} | FAUX |
| R19 | comparaison de chaque ligne du tableau à la fourchette du texte | "valeurs du tableau dans 20–60 % (tous grades) et 3–30 % (grade ≥ 3)" | {"hors_20_60": ["axi-cel", "brexu-cel", "ide-cel"], "hors_3_30": ["axi | ARRONDI |
| R20 | 1,6 / 0,7 ; létalité 0,8/1,6 = 50 % contre 0,2/0,7 = 28,6 % | "rapport des taux d'œdème cérébral" | 2.29 | CORRECT |
| R21 | 10 patients / effectif traité ZUMA-1 + ZUMA-7 (≈ 278, déduit de 10/0,036) | 3.6 | 3.6 | CORRECT |
| R22 | moyenne géométrique des bornes de l'IC à 95 % | 10.06 | 10.06 | CORRECT |
| R23 | demi-vie apparente sous dialyse = 3·ln2 / −ln(0,32) | "fraction éliminée 68 % en 3 h" | 1.82 | CORRECT |
| R24 | 8 items × 0–4 points | 32 | 32 | CORRECT |
| R25 | 24/12 = 2 ; 24/8 = 3 ; escalade cohérente | "q8–12 h (2 à 3/j) ; grade 1 : 2/j ; grade 2 : 3–4/j" | "toutes les 8 à 12 h ; 2/j ; 3 à 4/j" | CORRECT |
| R26 | union des classes {10} ∪ [7,9] ∪ [3,6] ∪ [0,2] = [0,10] | "partition 0–10 sans trou" | "10 = normal ; 7–9 ; 3–6 ; 0–2 ; 0 inaccessible" | CORRECT |
| R27 | comparaison de seuils | "seuil de risque < 30 (DFGe) inclus dans le seuil d'adaptation ≤ 50 (c | "30 < 50" | CORRECT |
| R28 | 100 mg/j du jour 0 au jour 6 = 7 doses | 700 | 700 | CORRECT |
| R29 | règle d'administration de l'IP | "≤ 250 mg en ≥ 5 min ; > 250 mg en ≥ 30 min" | "durée de perfusion absente" | NON_VERIFIABLE |
| R30 | comparaison | "1,6 % > 0,7 %" | "risque accru LMPGB" | CORRECT |
| R31 | 19/22 | 86.4 | 86.4 | CORRECT |
| R32 | clairance rénale / clairance totale = 110/120 ; t½ dialysé / t½ normal = 13/1,7 | {"fraction_renale": 0.917, "rapport_demi_vies": 7.6} | {"fraction_renale": 0.917, "rapport_demi_vies": 7.6} | CORRECT |
| R33 | 4 demi-vies ; fraction de l'équilibre atteinte = 1 − 0,5⁴ (cinétique d'ordre 1, hypothèse  | {"normal_h": 6.8, "dialyse_h": 52.0, "fraction_equilibre": 0.9375} | {"normal_h": 6.8, "dialyse_h": 52, "fraction_equilibre": 0.9375} | CORRECT |
| R34 | RV+ = Se/(1−Sp) ; RV− = (1−Se)/Sp | {"RV+": 7.3, "RV-": 0.14} | {"RV+": 7.33, "RV-": 0.136} | CORRECT |
| R35 | RV+ = Se/(1−Sp) ; RV− = (1−Se)/Sp | {"RV+": 9.4, "RV-": 0.026} | {"RV+": 9.39, "RV-": 0.026} | CORRECT |
| R36 | Cockcroft-Gault (µmol/L, homme) ; CKD-EPI 2021 sans coefficient ethnique ; tableau IP | {"cockcroft_mL_min": 21, "dfge": 25, "dose_g_par_24h": 1, "rapport_sur | {"cockcroft_mL_min": 21.1, "dfge": 25.2, "dose_g_par_24h": 1.0, "rappo | CORRECT |

Aucune dose, aucun débit ni seuil faux pouvant conduire à un surdosage ; la seule dose fausse est la décroissance de méthylprednisolone sous-dosée de moitié (C02). Les trois NON_VERIFIABLE (R13, R14, R29) sont des énoncés incomplets traités en C12 et C11.

## Matrice des 20 rubriques et rubrique 21

| Rang | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g92-0 (deux vignettes, objectifs) ; vignette céfépime incalculable (C12) |
| 2 | Définition et périmètre CIM-10-GM | couvert | g92-1 ; G92.0, G92.9, note de codage et exclusion G93.4 conformes à S1 |
| 3 | Classifications et stades | couvert | g92-1, g92-grade (grille ASTCT) ; formulation de l’ICE à 0 (C03) |
| 4 | Épidémiologie suisse puis européenne | partiel | g92-2 ; aucune donnée suisse (lacune déclarée) ; fourchette incohérente (C15) |
| 5 | Normal → pathologique | partiel | g92-3, g92-bhe ; aucune discipline du normal, pharmacocinétique absente (C07) |
| 6 | Étiologies et facteurs de risque | partiel | g92-4 ; lithium, CO, solvants absents (C24) |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g92-5 ; fréquences de la FI Yescarta exactes ; dénominateurs (C13) |
| 8 | Examen clinique (signes, Se/Sp) | partiel | g92-6 ; aucune technique ni valeur ; sémiologie absente (C01) |
| 9 | Drapeaux rouges et urgences | couvert | g92-8 alert ; lévétiracétam (C06), Tox Info Suisse (C21) |
| 10 | Examens complémentaires | couvert | g92-e-1, g92-e-2 ; indication de l’IRM (C08) |
| 11 | Diagnostic différentiel | couvert | g92-7 (infection, AVC, crise, leptoméninges, métabolique) |
| 12 | Prise en charge suisse | partiel | g92-9 ; décroissance de méthylprednisolone (C02) ; statut FI (C05, C06) |
| 13 | Complications et pronostic | couvert | g92-8, g92-10 ; paraphrase de la FI (C16) |
| 14 | Suivi, prévention, dépistage | couvert | g92-10 ; proximité européenne (C09) ; effectifs zurichois (C14) |
| 15 | Situations particulières | partiel | g92-11 ; grossesse déclarée non abordée alors que la FI du valproate la contre-indique (C04) |
| 16 | Spécificités suisses | partiel | g92-9.2 (FI Yescarta, conduite) ; Tox Info Suisse absent (C21) |
| 17 | Critères formels du diagnostic | couvert | g92-12 alert (ASTCT ; faisceau de synthèse pour G92.9 déclaré comme tel) |
| 18 | Paramètres clés chiffrés | partiel | g92-12 key ; grade 4 « 0 ou non évaluable » (C03) |
| 19 | Sous-codes CIM-10-GM couverts | couvert | G92.0 et G92.9 (S1) |
| 20 | Points d’examen fédéral | partiel | objectifs de g92-0 ; aucun rattachement PROFILES |
| 21 | Sémiologie fondamentale et analytique | absent | aucun g92-s-semio (C01) |

## 21 — Sémiologie fondamentale et analytique

Statut : **absente** (MAJEUR, bloquant pour la clôture du cours). Décompte réel des boutons data-s du panneau pS : 4 (g92-s-immuno, g92-s-neuro, g92-s-bioch, g92-s-imagerie). Sémiologie fondamentale : partielle dans l’onglet 1, absente comme discipline — manques : normal avant pathologique, technique par geste, mécanisme par signe, valeur chiffrée (aphasie 19/22 disponible ; autres signes non chiffrés dans les sources lues : LACUNE), pièges. Sémiologie analytique : absente — manques : regroupement syndromique, raisonnement en cinq étapes, examen systématique numéroté, synthèse présentée, trois cas corrigés.

Proposition rédigée et sourcée : propositions/G92_c_semio.html ; propositions/G92_pop1_semio.html ; propositions/G92_a_semio_clinique.html ; propositions/glossary_g92_ajouts.py ; propositions/G92_c_pharmacocinetique.html (sixième data-s). Sa simulation sur une copie de la leçon satisfait le validateur `semiology` de `tools/starter_codex.py`, `tests/audit_sciences.py` et `test_v7.py --static`.

| Critère | Résultat sur la leçon actuelle |
|---|---|
| SEM-01 | non (4 data-s, aucun g92-s-semio) |
| SEM-02 | non |
| SEM-03 | non (audit_sciences échoue, C07) |
| SEM-04 | oui (test_v7 --static G92 : OK sur la leçon actuelle) |
| SEM-05 | non |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | non |
| SEM-09 | non |
| SEM-10 | non (pièges présents en g92-5, g92-6, hors sémiologie) |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | non (pas d’alert sémiologique ; l’alert g92-8 existe) |
| SEM-14 | non |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non (trois quiz en g92-e-2, aucun sur la valeur d’un signe) |
| SEM-18 | non |
| SEM-19 | non évaluable (absente) |
| SEM-20 | non évaluable |
| SEM-21 | non évaluable |
| SEM-22 | non (bouton absent) |
| SEM-23 | non (aucune capture possible) |
| SEM-24 | oui (chap-head : « Revue par intelligence artificielle · Aucune validation médicale humaine ») |

## Figures et contrôles

6 figures, toutes des schémas non anatomiques (aucune figure anatomique dessinée par IA). Chromium headless : figures existantes 7,8 px rendus (viewBox 640, police 14) ; figures proposées 11,9 px, aucun texte hors cadre.

| Contrôle | Résultat |
|---|---|
| test_v7_static | G92 mots 9968 fenêtres 32 quiz 5 pareto 11 — OK (leçon actuelle) ; après simulation de toutes les propositions et conversion des repères [Sx] : mots 15834 fenêtres 38 quiz 8 — OK |
| audit_sciences | leçon actuelle : failed, 20 erreurs (4 disciplines de 122 à 219 mots, quatre libellés absents) ; simulation des propositions : passed (6 disciplines, 291 à 2680 mots) |
| validateur_semiologie_simule | 6 boutons data-s, g92-tab-semio premier et sélectionné, panneau visible, titre exact, 9 sections non vides, liens https, marqueur data-semiology-clinical dans pA : conformes |
| image_clo_finder_inventory | 6 figures SVG non anatomiques, aucune image, 4 icônes de 24 px |
| rendu_390px | Chromium headless : figures existantes 7,8 px rendus (viewBox 640, police 14) ; figures proposées 11,9 px, aucun texte hors cadre |
| propositions_ancres_uniques | 37 remplacements uniques vérifiés par script (1 occurrence chacun) ; 6 remplacements globaux (49 liens) |
| citations_calculs | 96/96 citations retrouvées mot pour mot dans la copie locale des sources lues |

## Lacunes

- Aucune information professionnelle suisse d’anakinra (Kineret) trouvée : requêtes AmiKo « Kineret » et « anakinra » (fr et de) vides le 16.10.2026, compendium.ch inaccessible sans connexion, AIPS du 08.10.2026 partiel ; statut d’autorisation suisse non vérifié.
- Aucune source suisse de sémiologie neurologique de l’encéphalopathie toxique ou du délire : WebSearch « Forum Médical Suisse délirium dépistage 4AT recommandations suisses » sans résultat suisse.
- Sensibilité et spécificité de la dysgraphie, de l’aphasie et de l’astérixis non chiffrées dans les sources lues ; seul 19/22 (aphasie expressive) est disponible.
- Recommandations EBMT-JACIE-EHA 2021 et manuel européen des CAR-T non lus en texte intégral par l’audit ; leurs contenus ne sont cités qu’au travers de la revue [S2].
- Disponibilité suisse du lorazépam intraveineux et de la glucarpidase non vérifiée.
- Lithium, monoxyde de carbone, solvants, métaux lourds, encéphalite sous inhibiteurs de points de contrôle : aucune source lue (C24).
- Résumés seulement pour S13 à S24, S26 et S27 ; aucune conduite n’est fondée sur un résumé seul, sauf les seuils de suivi du céfépime, déjà présentés par la leçon comme proposition d’une méta-analyse.
- Captures réelles SEM-22 et SEM-23 non réalisables : le sous-onglet n’existe pas encore dans la leçon.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G92 — Encéphalopathie toxique (S08, N-05-Neurologie) |
| Catégories traitées | G92.0, G92.9 |
| Système | Neurologie (S08) |
| Fichiers audités | 7, empreintes conformes |
| Sources lues | 29 (12 informations professionnelles ou classifications en texte intégral ou section) |
| Constats | 0 BLOQUANT, 7 MAJEUR, 13 MINEUR, 4 ENRICHISSEMENT |
| Calculs | 537 relevés, 30 calculables recalculés, 5 FAUX, 3 NON_VERIFIABLE |
| Propositions | 7 fichiers ; 37 remplacements uniques et 6 globaux vérifiés par script |
| Alertes | décroissance de méthylprednisolone (C02) ; grade de l’ICE à 0 (C03) ; contre-indications du valproate (C04) ; sémiologie absente (C01) |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
