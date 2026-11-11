# Audit médical ALPHA77 — G94 · Autres affections du cerveau au cours de maladies classées ailleurs (fragment S08)

Mission `ALPHA1-CLAUDE-G94-MED` · branche `claude/alpha1/g94-med-g1` · base du manifeste `523832d9` · worktree sur `103745ba` · génération 1 · 2026-10-16.

Empreintes SHA-256 des sept fichiers : **conformes au manifeste**. Exécutant : sous-agent Claude Code, modèle et effort conformes au manifeste. Première source lue : information professionnelle suisse Benerva®, section « Posologie » (AmiKo, mise à jour avril 2019).

## Synthèse

| BLOQUANT | MAJEUR | MINEUR | ENRICHISSEMENT |
|---|---|---|---|
| 1 | 8 | 13 | 6 |

La leçon est honnête sur ses limites et très fidèle à ses sources sur la plupart des chiffres : 371 valeurs sur 388 grandeurs concordent mot pour mot avec la source lue. Trois défauts dominent néanmoins. Le cas corrigé n° 4 enseigne de retarder la correction d’une hypoglycémie pour donner d’abord la thiamine : c’est une conduite dangereuse présentée comme la bonne réponse. La posologie de la thiamine dans le Wernicke ignore la recommandation européenne la plus récente (ESPEN 2022) et désigne la dose plus basse de l’information professionnelle comme « texte de référence ». Enfin, la sémiologie fondamentale et analytique exigée par Vial est absente comme discipline, et l’onglet Sciences échoue au contrôle automatique.

## Constats classés par gravité

### BLOQUANT

**C03** — `chapters/G94/G94_c.html` — ancre : `B. De la thiamine avant tout glucide, après prélèvement sanguin de thiamine.`

Cas 4 de g94-e-5 : chez un alcoolique confus ET hypoglycémique, la réponse attendue est « thiamine avant tout glucide, après prélèvement sanguin de thiamine ». Elle enseigne de retarder la correction d’une hypoglycémie jusqu’au prélèvement puis à l’injection de thiamine. La règle EFNS « avant tout glucide » vise les apports glucidiques ; la revue de la littérature consacrée à cette question conclut qu’un retard du glucose chez l’hypoglycémique ne peut pas être recommandé. Les nuances manquent aussi dans l’alerte g94-8, le tableau des urgences, l’alerte g94-p-3 et le moyen mnémotechnique.

*Preuve.* [S14] résumé (revue américaine, signalée comme telle) — « a delay in giving glucose to hypoglycemic patients cannot be recommended at this time, although prompt thiamine supplementation after or concurrent with a return to normoglycemia is recommended »; [S14] résumé — « prolonged glucose supplementation without the addition of thiamine can be a risk factor »; [S7] résumé, recommandation 5 — « It should be given, before any carbohydrate, 200 mg thrice daily »

*Proposition.* propositions/G94_c_e5_cas4.html : nouvelle réponse B « corriger l’hypoglycémie sans délai et injecter la thiamine parentérale dans le même temps ; prélèvement seulement s’il ne retarde rien », correction raisonnée, et quatre nuances locales (G94_b.html ×2, G94_d.html, G94_pop2.html).

*Justification.* Mécanisme : l’hypoglycémie prive immédiatement le neurone de son substrat, alors que le risque de Wernicke vient d’apports glucidiques prolongés sans thiamine. Conséquence : retarder le glucose pour une séquence de prélèvement expose à une lésion cérébrale évitable. Décision : conduite dangereuse enseignée comme bonne réponse → BLOQUANT. Limite : aucune source suisse ou européenne lue ne traite explicitement l’hypoglycémie (LACUNE) ; la revue S14 n’est pas une recommandation.

### MAJEUR

**C01** — `chapters/G94/G94_c.html` — ancre : `data-s="g94-s-anat"`

Le sixième sous-onglet « Sémiologie fondamentale et analytique » est absent. Décompte réel des data-s de G94_c.html : 3 (g94-s-anat, g94-s-physio, g94-s-bioch) ; aucun g94-s-semio. La sémiologie existante se limite à l’anamnèse (g94-5) et à l’examen (g94-6) de l’onglet 1 : signes énumérés sans technique, sans valeur chiffrée par signe (hors délire), sans regroupement syndromique ni raisonnement en cinq étapes, sans cas corrigés consacrés aux signes.

*Preuve.* [S2] Clinical evaluation — « Clinical evaluation involves assessing the patient's mental status, motor responses, brainstem reflexes, and presence of abnormal movements »; [S6] Clinical evaluation — « Multifocal clinical impairment is highly suggestive of LM »; [S17] résumé — « The classic triad … was present in only 44 percent of episodes; however, 95 percent had at least two of the four symptoms »

*Proposition.* propositions/G94_c_semio.html (bouton g94-s-semio en tête de sci-bar ; sept îlots g94-sm-1 à -7 : priorité clinique, symptômes, signes, syndromes, raisonnement en cinq étapes, examen systématique, trois cas corrigés) ; propositions/G94_pop2_semio.html (sept fenêtres g94-sm-*, destinées à G94_pop2.html) ; propositions/glossary_g94_ajouts.py (CAM-ICU, ICDSC).

*Justification.* Mécanisme : sans technique ni raisonnement du signe au syndrome, le lecteur ne distingue pas une encéphalopathie diffuse d’une hypertension intracrânienne ou d’une atteinte leptoméningée. Conséquence : la station clinique et l’examen fédéral exigent ce passage. Décision : exigence de Vial du 15.10.2026 ; absence = MAJEUR, bloquant pour la clôture du cours et du lot.

**C02** — `chapters/G94/G94_c.html` — ancre : `id="g94-s-anat"`

tests/audit_sciences.py échoue (exécuté sur un checkout dont les sept fichiers G94 ont des empreintes identiques au manifeste) : les trois disciplines sont sous 280 mots (anatomie 263, physiologie 221, biochimie 256 ; décompte de l’audit), et il manque les libellés « Science → examen. », « Science → traitement. », « À retenir. » (anatomie), « Science → clinique. », « À retenir. » (physiologie), « À retenir. » (biochimie). Histologie et génétique sont absentes (trois disciplines seulement).

*Preuve.* [S2] Pathophysiology (résumé de la revue) — « neuroinflammation and ischemia »; [S10] Propriétés/Effets — « Sous forme de pyrophosphate de thiamine, la thiamine constitue le groupe actif de diverses enzymes »

*Proposition.* Compléter chaque discipline jusqu’à 280 mots par des faits déjà sourcés (S2, S3, S10, S12), ajouter les quatre encadrés exigés ; la discipline sémiologique proposée (C01) porte déjà ses quatre libellés.

*Justification.* Mécanisme : un contrôle automatique bloque la publication conforme. Conséquence : l’onglet Sciences ne relie pas chaque science à l’examen et au traitement. Décision : MAJEUR, à corriger avec C01.

**C04** — `chapters/G94/G94_d.html` — ancre : `l’information professionnelle suisse, plus basse pour la thiamine, reste le texte de référence en Suisse.`

La posologie de la thiamine dans le Wernicke repose sur l’EFNS 2010 (présentée comme « la plus récente lue ») et sur l’information professionnelle Benerva®, dont la dose parentérale (jusqu’à 200 mg/j) est désignée par le piège p-4 comme « texte de référence ». La recommandation européenne la plus récente (ESPEN 2022, première autrice CHUV) propose 500 mg × 3/j IV dans l’encéphalopathie d’étiologie incertaine dont le Wernicke, et 100–300 mg/j IV dès l’admission aux urgences ou en soins intensifs (grade B). Le paramètre clé « au plus 200 mg par jour (information professionnelle suisse) » est inexact hors voie parentérale : la FI admet 200–300 mg/j per os dans l’hypovitaminose grave (calcul R18e FAUX). La conduite « préférer la voie orale » (p-3) contredit la FI pour les carences graves (voie parentérale d’abord) et l’ESPEN (absorption faible chez l’alcoolique).

*Preuve.* [S12] § 13, tableau 8 — « Encephalopathy of uncertain etiology including Wernicke encephalopathy — 500 mg, 3 times a day, IV »; [S12] recommandation 14.5 — « thiamine (100–300 mg/day IV) should be prescribed without hesitation from admission for 3–4 days. Grade B »; [S10] Posologie — « 200-300 mg par jour par voie orale en présence de graves symptômes … par voie parentérale … doses quotidiennes pouvant atteindre 200 mg »; [S10] Instructions spéciales — « Dans les cas graves de carence en thiamine, il est recommandé d'avoir d'abord recours à la voie parentérale »; [S7] résumé, recommandation 6 — « The overall safety of thiamine is very good (Level B) »

*Proposition.* propositions/G94_d_thiamine.html (ligne ESPEN dans g94-p-2, paragraphe de divergence, cellule p-3, piège p-4, paramètre g94-12, phrase g94-9, fenêtre g94-thiamine avec contre-indications et interactions).

*Justification.* Mécanisme : la thiamine est la coenzyme du métabolisme du glucose ; un apport insuffisant laisse persister la lésion. Conséquence : le piège oriente vers 200 mg/j, trois à sept fois moins que les deux recommandations européennes. Décision : MAJEUR (source plus récente ignorée sur une dose d’urgence) ; à arbitrer par Vial, potentiellement bloquant si l’orientation vers la dose FI est maintenue.

**C05** — `chapters/G94/G94_d.html` — ancre : `<td>Dexaméthasone</td><td>Méningite de l’adulte</td><td>Non détaillée dans les lignes lues</td><td>Lacune</td>`

La dexaméthasone adjuvante de la méningite bactérienne de l’adulte, point décisionnel majeur d’une leçon qui traite l’hydrocéphalie de la méningite, est déclarée lacune. L’essai randomisé européen de référence fixe 10 mg 15–20 minutes avant ou avec la première dose d’antibiotique, puis toutes les 6 heures pendant 4 jours.

*Preuve.* [S13] résumé — « Dexamethasone (10 mg) or placebo was administered 15 to 20 minutes before or with the first dose of antibiotic and was given every 6 hours for four days »; [S13] résumé — « relative risk of death, 0.48 … pneumococcal meningitis … 26 percent … as compared with 52 percent »; [S11] Administration systémique — « formes subaiguës … méningo-encéphalites: … 8 à 12 mg i.v. ; … 4 mg … à 6 heures d'intervalle »

*Proposition.* propositions/G94_d_dexa_meningite.html (ligne du tableau g94-p-2 et fenêtre g94-dexa).

*Justification.* Mécanisme : la dexaméthasone réduit la réaction inflammatoire méningée déclenchée par la lyse bactérienne. Conséquence : réduction de la mortalité et des séquelles, surtout à pneumocoque. Décision : MAJEUR (lacune comblable par une source européenne primaire).

**C06** — `chapters/G94/G94_b.html` — ancre : `type II probable ou possible (cytologie négative ou douteuse avec clinique ou imagerie évocatrice)`

Critères formels (div.alert g94-12, e-3, fenêtre g94-ml) : le type II est défini « avec clinique ou imagerie évocatrice ». La recommandation EANO-ESMO exige un cancer histologiquement prouvé et distingue « probable » (clinique typique ET imagerie typique) de « possible » (l’une sans l’autre, ou clinique typique avec imagerie normale ou hydrocéphalie seule), et exclut tout diagnostic devant une clinique atypique avec imagerie normale ou hydrocéphalie seule (« lack of evidence »).

*Preuve.* [S6] Diagnostic criteria — « The diagnosis is probable in the presence of typical clinical findings and typical MRI findings … possible in the presence of typical MRI findings but without typical clinical findings or … hydrocephalus only or a normal MRI »; [S6] Diagnostic criteria — « presenting with atypical clinical signs of LM only and with normal MRI or hydrocephalus only, a diagnosis of LM should not be made »

*Proposition.* propositions/G94_b_1.html (trois remplacements : G94_b.html, G94_c.html, G94_pop2.html).

*Justification.* Mécanisme : la combinaison clinique + imagerie hiérarchise la probabilité. Conséquence : la formulation « ou » assimile probable et possible et fait passer une clinique atypique pour un diagnostic. Décision : MAJEUR (critère formel inexact).

**C07** — `chapters/G94/G94_b.html` — ancre : `dans la méningite bactérienne, 15 % des patients ont reçu une dérivation externe et 8 % des ponctions lombaires répétées`

Erreur de dénominateur : 15 % (4 patients) et 8 % (2 patients) se rapportent aux 26 patients hydrocéphales, non aux 577 méningites. Rapportés aux méningites, ces taux valent 0,7 % et 0,3 % (calculs R09 et R10 : FAUX).

*Preuve.* [S5] résumé — « Six patients underwent an intervention: 2 patients (8%) had serial lumbar punctures; 4 patients (15%) underwent external ventricular CSF catheter placement »

*Proposition.* propositions/G94_b_1.html : « dans la cohorte néerlandaise, parmi les 26 patients hydrocéphales (sur 577 méningites), 4 (15 %) ont reçu un drain ventriculaire externe et 2 (8 %) des ponctions lombaires répétées ».

*Justification.* Mécanisme : un pourcentage n’a de sens qu’avec son dénominateur. Conséquence : le lecteur surestime d’un facteur vingt la fréquence des dérivations dans la méningite. Décision : résultat de calcul faux → MAJEUR (EXIGENCE_CALCULS § 3).

**C08** — `chapters/G94/G94_a.html` — ancre : `<td>Encéphalopathie de Wernicke (carence en thiamine)</td>`

La leçon présente l’encéphalopathie de Wernicke comme « exemple documenté » du pôle métabolique de G94 (G94.30) et sa fenêtre g94-cim avoue ne pas avoir vérifié le codage. Dans la CIM-10-GM 2024, E51.2 « Wernicke-Enzephalopathie » est un code autonome sans croix ni astérisque ; seul le béribéri humide (E51.1†) renvoie à un astérisque (I98.8*). Un tiers de la leçon repose ainsi sur une entité qui n’est pas un sous-code de G94.

*Preuve.* [S20] E51.- — « E51.2 Wernicke-Enzephalopathie (sans †) »; [S1] G94.30* — « Enzephalopathie bei anderenorts klassifizierten endokrinen und Stoffwechselkrankheiten »

*Proposition.* propositions/G94_a_perimetre.html (cellule du tableau g94-1 ; limite de la fenêtre g94-cim). Le contenu clinique sur le Wernicke reste utile comme urgence du diagnostic différentiel.

*Justification.* Mécanisme : un code astérisque n’existe qu’en association avec la cause codée. Conséquence : confusion de périmètre pour l’examinateur (rubriques 2 et 19). Décision : MAJEUR de périmètre, contenu médical conservé.

**C09** — `chapters/G94/G94_c.html` — ancre : `aria-label="Figure 2 — Régions cérébrales vulnérables et espaces du liquide"`

Figure 2 (g94-s-anat-cours) : contour cérébral, ventricules, tronc et méninges dessinés en SVG, déclarés « schéma établi pour la leçon, non issu d’une source anatomique ». Classe ANATOMIQUE_IA (déclaration de l’auteur) selon la règle de Vial du 15.10.2026.

*Preuve.* [S21] métadonnées Commons — « Gray 720-emphasizing-corpus-callosum.png ; Gray727 latin.svg ; Gyrus cinguli.png — Henry Vandyke Carter, domaine public »

*Proposition.* propositions/G94_c_figure2.html : remplacement par une planche réelle (trois candidats du domaine public, contrôle visuel à faire) ; aucun candidat trouvé pour ventricules et artère basilaire (LACUNE).

*Justification.* Mécanisme : un dessin anatomique généré trahit les proportions et les rapports. Conséquence : apprentissage d’une anatomie inexacte. Décision : MAJEUR par règle.

### MINEUR

**C10** — `chapters/G94/G94_c.html` — ancre : `Cytologie : <b>gold standard</b> du type I (confirmé)`

Anglicisme et attribution inexacte : la source réserve « gold standard » à la résonance magnétique cérébrospinale ; la cytologie positive définit le type I.

*Preuve.* [S6] Neuroimaging — « Cerebrospinal magnetic resonance imaging … is the gold standard imaging method »

*Proposition.* propositions/G94_mineurs.html (C10).

*Justification.* Terminologie exacte, sans conséquence décisionnelle.

**C11** — `chapters/G94/G94_a.html` — ancre : `Le besoin quotidien est d’environ 0,4 mg pour 4200 kJ de glucides ingérés`

La FI dit « 0,4 mg de thiamine pour que soient produits environ 4200 kJ lors du métabolisme glucidique », sans « quotidien » ni « ingérés » ; l’équivalence 4200 kJ ≈ 1000 kcal (R19) aide le lecteur ; le délai d’épuisement des réserves (20 jours) est sourcé par l’ESPEN.

*Preuve.* [S10] Propriétés/Effets — « il faut en moyenne 0,4 mg de thiamine pour que soient produits environ 4200 kJ »; [S12] § 13.1 — « thiamine reserves are depleted as early as 20 days of inadequate oral intake »

*Proposition.* propositions/G94_mineurs.html (C11).

*Justification.* Précision de citation et unité usuelle.

**C12** — `chapters/G94/G94_d.html` — ancre : `Les contre-indications de la thiamine et de la dexaméthasone ne figurent pas dans les lignes lues des informations profe`

Lacune factice : la FI Benerva® lue contient contre-indications (hypersensibilité ; lactose et saccharose des comprimés) et interactions (thiosemicarbazone, 5-fluorouracile, antiacides). Le 5-fluorouracile concerne le patient oncologique de la leçon.

*Preuve.* [S10] Contre-indications — « Hypersensibilité connue au principe actif ou à l'un des excipients »; [S10] Interactions — « La thiosemicarbazone et le 5-fluorouracil, antagonistes de la thiamine, annulent l'action de la thiamine. Les antiacides inhibent l'absorption »

*Proposition.* propositions/G94_mineurs.html (C12, C12 bis).

*Justification.* Information réglementaire disponible, sans conséquence décisionnelle majeure.

**C13** — `chapters/G94/G94_b.html` — ancre : `hémoglobine supérieure à 7 g/dL`

Unité non suisse : les laboratoires suisses expriment l’hémoglobine en g/L (7 g/dL = 70 g/L, R23). Même occurrence dans g94-cibles (G94_pop1.html).

*Preuve.* [S2] Table 2 — « Hemoglobin > 7g/dL »

*Proposition.* propositions/G94_mineurs.html (C13).

*Justification.* Conversion exacte ; évite une erreur de lecture d’un facteur 10.

**C15** — `chapters/G94/G94_pop2.html` — ancre : `Une valeur de glucose du liquide paraît erronée dans la transcription de la source et n’est pas reprise.`

La valeur de la source (glucose < 600 mg/L dans 22–38 %) est écartée comme « erronée » sans preuve ; 600 mg/L = 3,33 mmol/L (R26), seuil plausible.

*Preuve.* [S6] CSF — « decreased glucose (<600 mg/l) in 22%-38% of patients »

*Proposition.* propositions/G94_mineurs.html (C15).

*Justification.* Une donnée lue ne se supprime pas sans démonstration ; conversion fournie.

**C16** — `chapters/G94/G94_pop2.html` — ancre : `Survie médiane des métastases leptoméningées : 4 à 8 mois selon la tumeur.`

Arrondi incohérent avec la source et avec g94-10 (3,8–8,1 mois ; R29, R29b ARRONDI).

*Preuve.* [S6] Prognosis — « 3.8-5.4 months in breast cancer, 4.2-8.1 months in lung cancer, 4.8 months in melanoma »

*Proposition.* propositions/G94_mineurs.html (C16).

*Justification.* Cohérence SEM-20 entre Pareto et texte.

**C17** — `chapters/G94/G94_b.html` — ancre : `Les auteurs n’en déduisent pas une inefficacité : les effectifs sont minimes et les patients dérivés étaient les plus gr`

Interprétation attribuée aux auteurs mais absente du résumé lu (seul niveau de lecture déclaré) : « les patients dérivés étaient les plus graves » n’est pas sourcé.

*Preuve.* [S5] résumé — « A minority of patients underwent neurosurgery and outcome was uniformly poor in these patients »

*Proposition.* propositions/G94_b_1.html (C17).

*Justification.* Loi 1 du prompt de vérité : rien au-delà de la lecture.

**C18** — `chapters/G94/G94_c.html` — ancre : `<td>Lésions chez plus de 50 % des patients</td>`

Population omise : plus de 50 % concerne les patients à encéphalopathie persistante, crises ou signes focaux, non tous les septiques.

*Preuve.* [S2] résumé — « In septic patients with persistent encephalopathy, seizures, and/or focal signs, magnetic resonance imaging detects brain injury in more than 50% of cases »

*Proposition.* propositions/G94_mineurs.html (C18).

*Justification.* Un pourcentage sans population induit en erreur.

**C19** — `chapters/G94/G94_c.html` — ancre : `Dosage de la thiamine totale sanguine, résonance magnétique`

Préciser le milieu : sang total ou érythrocytes (pyrophosphate de thiamine) ; le plasma ne convient pas ; le traitement n’attend pas le résultat.

*Preuve.* [S12] § 13.2 — « Plasma measurement is not used since virtually all circulating ThDP is in the erythrocytes … treatment should not be delayed by waiting for the laboratory result »

*Proposition.* propositions/G94_mineurs.html (C19).

*Justification.* Évite un prélèvement inutilisable.

**C20** — `chapters/G94/G94_a.html` — ancre : `Affections du cerveau au cours de maladies classées ailleurs</h1>`

Intitulé de l’en-tête sans « Autres » alors que la fenêtre g94-cim donne le libellé officiel « Autres affections… » (Sonstige Krankheiten …) ; K72.7 est un code secondaire « K72.7-! ».

*Preuve.* [S1] G94.-* — « Sonstige Krankheiten des Gehirns bei anderenorts klassifizierten Krankheiten ; Exkl.: Hepatische Enzephalopathie (K72.7-!) »

*Proposition.* propositions/G94_a_perimetre.html (C20).

*Justification.* Cohérence de libellé.

**C21** — `chapters/G94/G94_a.html` — ancre : `Le score de Glasgow quantifie la gravité`

Le score de Glasgow est employé en total (« Glasgow à 9 ») ; la référence recommande de décrire le patient par ses trois composantes ; le cas 1 (9/15) n’appartient à aucune des deux strates de risque citées (R31).

*Preuve.* [S15] résumé — « Individual patients are best described by the three components of the coma scale; whereas the derived total coma score should be used to characterise groups »

*Proposition.* propositions/G94_mineurs.html (C21).

*Justification.* Précision sémiologique.

**C22** — `chapters/G94/G94_c.html` — ancre : `Le dosage de thiamine se fait avant la première dose, car la recommandation demande de la doser immédiatement avant l’ad`

Justification circulaire (« car la recommandation le demande ») dans un encadré Science → examen ; le mécanisme est que le taux post-injection reflète l’apport.

*Preuve.* [S7] résumé, recommandation 3 — « Total thiamine in blood sample should be measured immediately before its administration (GPP) »; [S12] § 13.2 — « treatment should not be delayed by waiting for the laboratory result »

*Proposition.* propositions/G94_mineurs.html (C22).

*Justification.* STYLE_REDACTION § 1 : dire pourquoi. Le mécanisme proposé est une inférence de l’audit, signalée comme telle.

**C23** — `chapters/G94/G94_c.html` — ancre : `<text x="215" y="298" font-size="0"> </text>`

Artefacts techniques de la figure 2 : texte SVG invisible (font-size 0) et liste ol placée dans figure après figcaption.

*Preuve.* —

*Proposition.* propositions/G94_c_figure2.html (C23).

*Justification.* Propreté du contrat HTML ; sans conséquence médicale.

### ENRICHISSEMENT

**C14** — `chapters/G94/G94_pop1.html` — ancre : `La conduite thérapeutique précise (ajustement ou arrêt) n’est pas détaillée dans le dossier.`

Conduite face à la neurotoxicité du céfépime disponible : FI suisse (adaptation dès ClCr ≤ 50 mL/min, hémodialyse en surdosage) et revue (réduction ou arrêt, amélioration médiane 3 jours, dosage sérique, électroencéphalogramme).

*Preuve.* [S19] Posologie, insuffisance rénale — « taux de filtration glomérulaire ≤50 ml/min … requièrent une adaptation de la posologie »; [S19] Surdosage — « les taux sériques de céfépime peuvent être abaissés par une hémodialyse »; [S2] Antibiotics — « Symptoms usually improve with dose reduction or discontinuation of cefepime, with a median time to improvement of 3 days »

*Proposition.* propositions/G94_enrichissements.html (C14).

*Justification.* Rubrique 12 (prise en charge suisse, FI datée).

**C24** — `chapters/G94/G94_a.html` — ancre : `id="g94-5"`

La sémiologie de la méningite bactérienne (première cause d’hydrocéphalie de la leçon) n’est pas donnée : triade 44 %, au moins deux des quatre signes 95 %, coma 14 %.

*Preuve.* [S17] résumé — « classic triad … only 44 percent … 95 percent had at least two of the four symptoms … 14 percent of patients were comatose »

*Proposition.* propositions/G94_enrichissements.html (C24).

*Justification.* Rubrique 7 et point d’examen fédéral.

**C25** — `chapters/G94/G94_a.html` — ancre : `L’examen évalue l’<b>état mental</b> par un outil validé de dépistage du délire`

L’« outil validé » n’est ni nommé ni chiffré ; la méthode CAM-ICU a une sensibilité de 80,0 % et une spécificité de 95,9 %.

*Preuve.* [S16] résumé — « The pooled sensitivity of the CAM-ICU was 80.0% … pooled specificity was 95.9% »

*Proposition.* propositions/G94_enrichissements.html (C25) ; glossaire CAM-ICU.

*Justification.* Rubrique 8 (sensibilité/spécificité).

**C26** — `chapters/G94/G94_b.html` — ancre : `La thiamine parentérale est recommandée pour tous les sujets à risque admis aux urgences`

Prévention précisable par l’ESPEN 2022 : 100–300 mg/j IV dès l’admission aux urgences ou en soins intensifs pendant 3–4 jours (grade B) ; déplétion > 90 % en maladie critique.

*Preuve.* [S12] recommandation 14.5 et § 13.1 — « 100–300 mg/day IV … from admission for 3–4 days ; deficiency or depletion may be found in >90% of patients »

*Proposition.* propositions/G94_enrichissements.html (C26).

*Justification.* Rubrique 14 (prévention).

**C27** — `chapters/G94/G94_b.html` — ancre : `id="g94-11"`

Spécificités suisses absentes (rubrique 16) : déclaration obligatoire à l’OFSP des infections invasives à méningocoque, pneumocoque, de la listériose et de la tuberculose, causes de G94.0. Source non lue (guide OFSP inaccessible) : LACUNE, aucun texte proposé.

*Preuve.* —

*Proposition.* Lire le guide OFSP de la déclaration obligatoire (OMDT, RS 818.101.126) puis ajouter un paragraphe dans g94-11.

*Justification.* Rubrique 16 obligatoire du prompt de vérité.

**C28** — `chapters/G94/G94_a.html` — ancre : `L’interrogatoire cherche d’abord la maladie primaire, car elle désigne le pôle.`

Raisonnement inverse non enseigné : une encéphalopathie nouvelle peut être le premier signe d’un sepsis et impose de chercher une infection.

*Preuve.* [S2] Clinical evaluation — « SAE may be the first sign of early sepsis, and any new-onset encephalopathy must prompt clinicians to screen their patients for infection »

*Proposition.* propositions/G94_enrichissements.html (C28).

*Justification.* Rubrique 9 (drapeaux rouges).

## Calculs (EXIGENCE_CALCULS)

L’inventaire et le recalcul sont produits par `calculs/verifier.py`, conservé et rejouable ; ses sorties sont `calculs/inventaire.json` et `calculs/resultats.json`.

| Relevés | Grandeurs | Non calculables (dates, numéros, codes) | Concordance source | Vignettes | Non rapprochés | Calculables | Recalculés | Correct | Arrondi | Faux | Non vérifiable | Informatifs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 532 | 388 | 144 | 371 | 7 | 0 | 38 | 38 | 18 | 16 | 3 | 1 | 25 |

Le tableau suivant détaille chaque recalcul ; un écart dans la tolérance d’arrondi de la source est classé ARRONDI.

| Id | Verdict | Attendu | Trouvé | Formule | Source |
|---|---|---|---|---|---|
| R01 | ARRONDI | 4.5 | 5.0 | 26/577 hydrocéphalies | S5 |
| R02 | ARRONDI | 69.2 | 69.0 | 18/26 présentes à l'admission | S5 |
| R03 | ARRONDI | 53.8 | 54.0 | 14/26 S. pneumoniae | S5 |
| R04 | ARRONDI | 15.4 | 15.0 | 4/26 L. monocytogenes | S5 |
| R05 | CORRECT | 50.0 | 50.0 | 13/26 décès | S5 |
| R06 | ARRONDI | 69.2 | 69.0 | 18/26 évolution défavorable | S5 |
| R07 | ARRONDI | 7.7 | 8.0 | 2/26 ponctions lombaires répétées | S5 |
| R08 | ARRONDI | 15.4 | 15.0 | 4/26 drains ventriculaires externes | S5 |
| R09 | FAUX | 0.7 | 15.0 | « dans la méningite bactérienne, 15 % des patients ont reçu une dérivation externe » : 4/577 épisodes = 0,7 % | S5 (dénominateur réel : 26 patients hydrocéphales) |
| R10 | FAUX | 0.3 | 8.0 | 8 % de ponctions répétées rapportés à toutes les méningites : 2/577 = 0,3 % | S5 |
| R11 | CORRECT | 6 | 6.0 | 2 + 4 patients traités = 6 interventions | S5 « Six patients underwent an intervention » |
| R12 | ARRONDI | 7.78 | 7.81 | √(2,91 × 20,8) ≈ OR | S5 |
| R13 | CORRECT | 54.0 | 54.0 | 27/50 patients non sédatés | S2 |
| R14 | CORRECT | 17 | 17.0 | complément 100 − 83 (premières cytologies négatives) | S6 |
| R14b | CORRECT | 39.5 | 39.5 | complément 100 − 60,5 | S6 |
| R15 | CORRECT | 3.37 | 3.37 | √(2,82 × 4,03) ≈ HR GCS 3–8 | S2 |
| R16 | NON_VERIFIABLE | None | 1.38 | HR GCS 13–14 = 1,38 ; IC publié 1,09–1,38 (borne haute = estimation : coquille de la source) | S2 |
| R17a | CORRECT | 1.77 | 1.77 | √(IC) ≈ aHR pression | S4 |
| R17b | CORRECT | 1.78 | 1.78 | √(IC) ≈ aHR oxygénation | S4 |
| R17c | CORRECT | 1.46 | 1.46 | √(IC) ≈ aHR température | S4 |
| R17d | CORRECT | 1.41 | 1.41 | √(IC) ≈ aHR glycémie | S4 |
| R18 | CORRECT | 600 | 600.0 | 3 × 200 mg = 600 mg/j (EFNS) | S7 |
| R18b | INFORMATIF | 3.0 | None | rapport EFNS / FI parentérale = 3 | S7, S10 |
| R18c | INFORMATIF | 1500 | None | ESPEN 2022 : encéphalopathie d'étiologie incertaine dont Wernicke, 500 mg × 3 = 1500 mg/j IV | S12 (tableau 8) |
| R18d | CORRECT | 200.0 | 200.0 | plafond FI parentéral « doses quotidiennes pouvant atteindre 200 mg » | S10 |
| R18e | FAUX | 300.0 | 200.0 | « au plus 200 mg par jour (information professionnelle suisse) » présenté comme plafond global : la FI admet 200–300 mg/j per os dans l'hypovitaminose grave | S10 (Posologie, Traitement) |
| R18f | INFORMATIF | 15 | None | 1500 mg/j = 15 ampoules Benerva 100 mg/1 mL ; 600 mg/j = 6 ampoules | S10 (Présentation : ampoules 1 mL à 100 mg, boîte de 6) |
| R19 | INFORMATIF | 1004.0 | None | 4200 kJ ÷ 4,184 = 1004 kcal ≈ 1000 kcal | S10 ; facteur 1 kcal = 4,184 kJ |
| R20 | INFORMATIF | 0.6 | None | dexaméthasone enfant 0,15 mg/kg × 4/j = 0,6 mg/kg/j ; × 4 j = 2,4 mg/kg | S11 |
| R20b | INFORMATIF | 0.8 | None | 0,4 mg/kg × 2/j = 0,8 mg/kg/j ; × 2 j = 1,6 mg/kg | S11 |
| R20c | INFORMATIF | 3.0 | None | exemple 20 kg : 3 mg par dose toutes les 6 h | S11 |
| R21 | INFORMATIF | 16 | None | dexaméthasone adulte, entretien 4 mg × 4/j = 16 mg/j après 8–12 mg | S11 |
| R21b | INFORMATIF | 160 | None | méningite bactérienne de l'adulte : 10 mg × 4/j × 4 j = 160 mg (absent de la leçon) | S13 |
| R22 | INFORMATIF | 10.7 | None | PaO₂ 80 mmHg = 10,7 kPa | conversion |
| R22b | INFORMATIF | 16.0 | None | PaO₂ 120 mmHg = 16,0 kPa | conversion |
| R22c | INFORMATIF | 4.67 | None | PaCO₂ 35 mmHg = 4,67 kPa | conversion |
| R22d | INFORMATIF | 6.0 | None | PaCO₂ 45 mmHg = 6,00 kPa | conversion |
| R23 | INFORMATIF | 70 | None | hémoglobine 7 g/dL = 70 g/L (unité des laboratoires suisses) | conversion |
| R24 | INFORMATIF | 90 | None | glycémie 5 mmol/L = 90 mg/dL | conversion |
| R24b | INFORMATIF | 180 | None | glycémie 10 mmol/L = 180 mg/dL | conversion |
| R24c | INFORMATIF | 54 | None | hypoglycémie < 3 mmol/L = 54 mg/dL | conversion |
| R25 | INFORMATIF | 14.7 | None | pression d'ouverture 200 mm H₂O = 14,7 mmHg = 20 cm H₂O | conversion |
| R26 | INFORMATIF | 3.33 | None | glucose du LCS < 600 mg/L (S6) = 3,33 mmol/L : valeur physiologiquement plausible comme seuil bas | S6 + masse molaire 180,16 g/mol |
| R26b | INFORMATIF | 0.5 | None | protéines 500 mg/L = 0,5 g/L | conversion |
| R27a | ARRONDI | 4.7 | 5.0 | 9/190 infections | S6 |
| R27b | ARRONDI | 13.2 | 13.0 | 25/190 hygromes/hématomes | S6 |
| R27c | CORRECT | 6.3 | 6.3 | 12/190 symptomatiques | S6 |
| R27d | ARRONDI | 4.7 | 5.0 | 9/190 dysfonctions | S6 |
| R27e | ARRONDI | 7.9 | 8.0 | 15/190 externalisation/retrait/révision | S6 |
| R27f | ARRONDI | 78.9 | 79.0 | 150/190 sans complication | S6 |
| R27g | INFORMATIF | 21 | None | patients avec ≥ 1 complication = 21 % ; somme des catégories 5 + 13 + 5 + 8 = 31 % (catégories non exclusives) | S6 |
| R28 | ARRONDI | 19.8 | 20.0 | 63/318 survivantes > 1 an | S6 |
| R29 | ARRONDI | 3.8 | 4.0 | Pareto « 4 à 8 mois » : borne basse source 3,8 | S6 |
| R29b | ARRONDI | 8.1 | 8.0 | Pareto « 4 à 8 mois » : borne haute source 8,1 | S6 |
| R30 | CORRECT | 1.0 | 1.0 | céfépime : 7,7 < 20 < 38,1 mg/L (ordre des seuils) | S2 |
| R31 | CORRECT | 1.0 | 1.0 | GCS du cas 1 (9) dans l'échelle 3–15 ; catégorie 9–12 (ni 3–8 ni 13–14) | S2, S15 |
| R32 | INFORMATIF | 3.19 | None | RV+ de l'énolase = 0,542 / 0,17 = 3,19 | S2 |
| R32b | INFORMATIF | 0.55 | None | RV− de l'énolase = 0,458 / 0,83 = 0,55 | S2 |
| R33 | INFORMATIF | 40.0 | None | besoin 0,4 mg par 4200 kJ produits ; pour 8400 kJ de glucides : 0,8 mg | S10 |
| R34 | CORRECT | 4.0 | 4.0 | Wernicke : 4 critères EFNS/Caine, seuil 2 | S7 |
| R35 | INFORMATIF | 88.7 | None | 883/995 = 88,7 % avec au moins une agression systémique (non écrit dans la leçon) | S4 |
| R36 | CORRECT | 1.0 | 1.0 | méningite : 26 hydrocéphalies ; 69 % = 18 ; 54 % = 14 ; 15 % = 4 ; 50 % = 13 (cohérence des effectifs) | S5 |
| R37 | CORRECT | 600.0 | 600.0 | texte p-2 « 600 mg par jour répartis en trois prises » | S7 |

Lecture : les trois verdicts FAUX sont l’erreur de dénominateur de l’îlot g94-8 (R09, R10 → C07) et le plafond « au plus 200 mg par jour » attribué à l’information professionnelle (R18e → C04). Aucune dose pédiatrique ou adulte de dexaméthasone n’est fausse par rapport à la FI. La leçon ne contient ni débit, ni vitesse de correction, ni calcul de déficit. Les intervalles de confiance publiés sont cohérents, sauf celui du score de Glasgow 13–14 dans la source elle-même (1,09–1,38), que la leçon ne reprend pas.

## Rubrique 21 — Sémiologie fondamentale et analytique

Statut : **absente** — 3 data-s (g94-s-anat, g94-s-physio, g94-s-bioch), aucun `g94-s-semio` → constat **C01, MAJEUR**, bloquant pour la clôture.

*Fondamentale* : partielle dans l’onglet 1, absente comme discipline (g94-5, g94-6, g94-delire, g94-gcs, g94-sae-def). Manques : technique des gestes, mécanisme par signe, normal avant pathologique, valeur chiffrée hors délire (méningite S17, CAM-ICU S16 disponibles), pièges ; céphalées et signes leptoméningés non chiffrés dans les sources lues (LACUNE).

*Analytique* : absente. Manques : regroupement syndromique, raisonnement en cinq étapes, examen systématique, synthèse présentée, trois cas corrigés.

Proposition rédigée et sourcée : `propositions/G94_c_semio.html` (sept îlots, 2388 mots, un schéma de raisonnement non anatomique, trois cas corrigés dont un sur la valeur d’un signe et un sur la formulation d’une limite), fenêtres `propositions/G94_pop2_semio.html` (destinées à `G94_pop2.html`), glossaire `propositions/glossary_g94_ajouts.py`.

| Critère | Résultat |
|---|---|
| SEM-01 | non (aucun data-s g94-s-semio ; 3 data-s) |
| SEM-02 | non |
| SEM-03 | non (audit_sciences échoue, C02) |
| SEM-04 | oui (test_v7.py --static G94 : « G94 mots 10448 fenêtres 35 quiz 4 pareto 8 — OK ») |
| SEM-05 | non (tableau g94-5 sans colonnes mécanisme ni piège) |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | partiel (fréquences du délire sourcées ; autres signes non chiffrés et non déclarés) |
| SEM-09 | non |
| SEM-10 | partiel (pièges g94-5 et g94-6) |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | non (pas d’alert sémiologique ; l’alert g94-8 existe mais omet l’hypoglycémie, C03) |
| SEM-14 | partiel (g94-7 donne des indices, sans discriminant sémiologique sourcé) |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non (quatre quiz en e-5, aucun sur la valeur d’un signe ni sur une limite) |
| SEM-18 | non vérifiable sans navigateur ; mots verts g94-delire, g94-gcs existants |
| SEM-19 | non évaluable (absente) |
| SEM-20 | non évaluable |
| SEM-21 | non évaluable |
| SEM-22 | non (bouton absent) |
| SEM-23 | non (aucune capture possible) |
| SEM-24 | oui (chap-head : « Revue par intelligence artificielle · Aucune validation médicale humaine ») |

## Matrice des 20 rubriques (leçon telle qu’elle est)

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g94-0 (trois vignettes, cinq objectifs) |
| 2 | Définition et périmètre CIM-10-GM | partiel | g94-1, g94-cim ; codes conformes à S1, mais Wernicke hors G94 (C08) et intitulé (C20) |
| 3 | Classifications et stades | partiel | g94-12 (types I/II des métastases imprécis, C06) ; types A–D d’imagerie absents |
| 4 | Épidémiologie suisse puis européenne | partiel | g94-2 : européenne seulement ; aucune donnée suisse (déclaré) |
| 5 | Normal → pathologique | partiel | g94-3, g94-s-physio ; physiologie du liquide cérébrospinal absente (déclaré) |
| 6 | Étiologies et facteurs de risque | couvert | g94-4 |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g94-5 ; fréquences du délire seulement ; méningite non chiffrée (C24) |
| 8 | Examen clinique (sensibilité/spécificité) | partiel | g94-6 ; aucun outil nommé ni chiffré (C25) ; sémiologie absente (C01) |
| 9 | Drapeaux rouges et urgences | partiel | g94-8 ; hypoglycémie mal traitée (C03) |
| 10 | Examens complémentaires | couvert | g94-e-1 à g94-e-4 ; précisions C18, C19, C15 |
| 11 | Diagnostic différentiel | couvert | g94-7 (tableau hiérarchisé) |
| 12 | Prise en charge suisse | partiel | g94-9, g94-p-2 ; thiamine (C04), dexaméthasone adulte (C05), céfépime (C14) |
| 13 | Complications et pronostic | couvert | g94-8, g94-10 ; dénominateur faux (C07) |
| 14 | Suivi, prévention, dépistage | couvert | g94-10 ; ESPEN (C26) |
| 15 | Situations particulières | partiel | g94-11 : grossesse et sujet âgé absents (déclaré) |
| 16 | Spécificités suisses | absent | aucune (C27) |
| 17 | Critères formels du diagnostic (div.alert) | partiel | g94-12 : type II inexact (C06) |
| 18 | Paramètres clés chiffrés (div.key) | partiel | g94-12 : thiamine inexacte (C04) |
| 19 | Sous-codes CIM-10-GM couverts | partiel | G94.0–G94.8 listés (g94-cim, glossaire) ; G94.30 sans entité sourcée, G94.39 et G94.8 non développés (déclaré) |
| 20 | Points d’examen fédéral | partiel | pièges présents ; dexaméthasone de la méningite et sémiologie de la méningite absentes |

## Figures

| Fichier | Figure | Classe | Verdict |
|---|---|---|---|
| chapters/G94/G94_b.html | Figure 1 — Séquence diagnostique | SCHEMA_NON_ANATOMIQUE | recevable (étapes sourcées S2, S6, S7) |
| chapters/G94/G94_c.html | Figure 2 — Régions cérébrales vulnérables | ANATOMIQUE_IA | MAJEUR (C09) |
| chapters/G94/G94_c.html | Figure 3 — Chaîne physiopathologique | SCHEMA_NON_ANATOMIQUE | recevable (S2, S3) |
| chapters/G94/G94_c.html | Figure 4 — Thiamine et métabolisme | SCHEMA_NON_ANATOMIQUE | recevable (S10) |
| chapters/G94/G94_c.html | icônes de la barre des sciences (cercle et croix) | icône non anatomique | recevable |

## Lacunes

- Aucune source suisse de société savante (neurologie, médecine intensive, infectiologie) ni épidémiologie suisse lue ; guide OFSP de la déclaration obligatoire inaccessible (HTTP 502/403) : rubrique 16 non documentée (C27).
- Recommandation ESCMID 2016 sur la méningite bactérienne non lue (HTTP 403) ; dexaméthasone de l’adulte fondée sur l’essai de Gans 2002 (résumé).
- Aucune source suisse ou européenne lue sur l’ordre glucose/thiamine dans l’hypoglycémie : C03 repose sur une revue américaine (S14), signalée comme telle.
- EFNS 2010 et texte intégral EFNS inaccessibles (403) : lecture au niveau du résumé.
- Grille détaillée du score de Glasgow, technique des réflexes du tronc et items du CAM-ICU non lus dans une source de sémiologie suisse ou européenne ; aucune valeur sémiologique chiffrée pour les céphalées et vomissements d’hydrocéphalie ni pour les signes leptoméningés.
- Images candidates de la figure 2 : métadonnées seulement, contrôle visuel non réalisé ; aucun candidat pour ventricules et artère basilaire.
- Contrôle navigateur (SEM-18, SEM-22, SEM-23) et captures non réalisés dans ce rôle d’audit.
- Calculs : recalcules = calculables (38/38) ; aucune lacune de recalcul.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Cours | G94 — Autres affections du cerveau au cours de maladies classées ailleurs (S08-Neurologie) |
| Catégories couvertes | G94.0, G94.1, G94.2, G94.3 (G94.30, G94.31, G94.32, G94.39), G94.8 |
| Fichiers lus | 7 / 7, empreintes conformes |
| Sources lues | 22 (dont 3 informations professionnelles suisses datées ; 2 recommandations européennes en texte intégral ou section ; ESCMID non lue) |
| Constats | 1 bloquant, 8 majeurs, 13 mineurs, 6 enrichissements |
| Calculs | 532 relevés, 38 calculables, 38 recalculés, 3 faux |
| Contrôles | test_v7 --static : OK ; audit_sciences : échec (C02) |
| Propositions | 11 fichiers, 33 remplacements à ancre unique vérifiée |
| Alertes | C03 (hypoglycémie), C04 (dose de thiamine), C01 (sémiologie absente) |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
