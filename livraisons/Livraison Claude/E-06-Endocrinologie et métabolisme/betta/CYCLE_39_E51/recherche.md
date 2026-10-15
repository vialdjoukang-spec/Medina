# Dossier de recherche — E51 Carence en thiamine [carence en vitamine B1] (E-06-Endocrinologie et métabolisme)

Cycle Betta 39, leçon 2. Agent de recherche C39-A2-ENDO (Opus 5.5). Date : 15.10.2026.
Chaque affirmation renvoie à une source de `sources.json` (Sx), lue pendant cette session (texte intégral, résumé PubMed ou information professionnelle AmiKo). Rien n'est ajouté de mémoire ; ce qui n'a pas été trouvé figure en « Lacunes ». Recherche web générale indisponible (quota de session épuisé) : accès par PubMed/E-utilities, Europe PMC, sites ESPEN, DGE, SMOB, Revue Médicale Suisse et `tools/swissmedic_fi.py`.

## 0. Positionnement de la leçon
- E51 suit E50 dans le bloc E50–E64 « Autres carences nutritionnelles » [S1]. La thiamine est hydrosoluble, sans synthèse endogène utile, et les réserves sont faibles : la carence s'installe en quelques semaines dès que l'apport chute ou que les besoins montent [S2, S7, S10].
- En Suisse, la carence est **sous-diagnostiquée parce que sous-évoquée** ; ses facteurs de risque (alcool, malnutrition) sont pourtant fréquents [S5]. La leçon doit donc couvrir le modèle historique (béribéri des pays à faible revenu, béribéri infantile) et le patient suisse réel : alcool, chirurgie bariatrique, vomissements prolongés, renutrition, soins intensifs [S2, S5, S7].

### Sous-codes CIM-10-GM 2024 couverts [S1]
| Code | Intitulé |
|---|---|
| E51.1 | Béribéri (formes sèche et humide) |
| E51.2 | Encéphalopathie de Wernicke |
| E51.8 | Autres manifestations de la carence en thiamine |
| E51.9 | Carence en thiamine, sans précision |
Remarque : le relevé `nosology/fragments/S05.json` ne contient pas de sous-code E51.0 [S1]. Le syndrome de Korsakoff alcoolique relève d'un autre chapitre (F10.6) : à vérifier dans la CIM-10-GM avant de l'écrire (lacune, non lu).

## 1. Question clinique
Devant une confusion, des troubles oculomoteurs, une ataxie, une insuffisance cardiaque à haut débit ou une acidose lactique inexpliquée chez un patient à risque nutritionnel, il faut **penser à la thiamine, prélever si possible puis traiter immédiatement, sans attendre le résultat** [S2, S3, S7]. Le traitement est simple et peu coûteux ; le retard expose à la mort et aux séquelles (Korsakoff) [S5, S7].

## 2. Définition et terminologie
- Carence en thiamine (vitamine B1) : apport, absorption, stockage ou utilisation insuffisants face aux besoins [S7, S2].
- Trois entités cliniques classiques : **encéphalopathie de Gayet-Wernicke** (pouvant évoluer vers le **syndrome de Korsakoff**), **béribéri humide** (cardiovasculaire) et **béribéri sec** (neuropathie périphérique) [S5, S7].
- Béribéri humide : atteinte cardiovasculaire avec œdèmes ; sec : atteinte du système nerveux périphérique [S10]. **Shoshin béribéri** : forme fulminante du béribéri humide, choc cardiogénique avec acidose lactique et défaillance multiviscérale, **sans œdème**, qui peut mimer un sepsis [S10, S11].
- Terme parapluie proposé : « thiamine deficiency disorders » (TDD), pour le spectre chevauchant des présentations au cours de la vie [S10].
- Korsakoff : syndrome neuropsychiatrique chronique largement irréversible (amnésie globale, confabulation, apathie, troubles cognitifs) ; environ la moitié des survivants d'un Wernicke le développent [S7].

## 3. Classifications
| Axe | Catégories | Source |
|---|---|---|
| Clinique | Wernicke(-Korsakoff) ; béribéri humide (dont Shoshin) ; béribéri sec ; acidose lactique ; béribéri infantile | S5, S6, S7, S10 |
| Béribéri infantile (OMS 1999, repris) | formes cardiaque aiguë, pseudo-méningitique, aphonique (cri « silencieux ») | S10 |
| Étiologique (mécanisme) | apport diminué ; absorption diminuée ; stockage diminué ; utilisation cellulaire altérée ; consommation/pertes accrues | S7 |
| Contexte | lié à l'alcool / non lié à l'alcool (profils différents d'âge, sexe, mortalité) | S9, S7 |

## 4. Épidémiologie
- Autopsies : Wernicke chez environ **1 % de la population générale** et **12,5–35 % des patients dépendants à l'alcool** ; environ **80 % des cas ne sont pas diagnostiqués** du vivant [S7]. Prévalences autopsiques nationales 0,6–2,2 % (dont Autriche, France, Allemagne) [S7].
- Méta-analyse 2026 (12 études, 5510 patients) : 65,4 % d'hommes, âge moyen 60,7 ans ; alcool principal facteur de risque (90,7 %) ; hors alcool : malnutrition 30,2 %, infections 25,1 %, troubles psychiatriques 15,4 % ; **triade complète dans 32,7 % seulement** ; mortalité 5,1 %, plus élevée hors alcool (8,8 %) [S9].
- Hors alcool, les patients sont plus jeunes et plus souvent des femmes ; avec l'alcool, âge moyen > 40 ans et prédominance masculine [S7, S9]. (Attention : la figure 1 de S7 inverse les ratios du texte ; retenir le texte : 1,69 homme/femme si alcool ; 1,84 femme/homme hors alcool.)
- Soins intensifs : carence ou déplétion jusqu'à > 90 % des patients critiques [S2] ; 20–70 % des chocs septiques selon le seuil [S6]. Insuffisance cardiaque ambulatoire : 6 % [S2]. Bariatrique : la thiamine fait partie des micronutriments à plus haut risque, avant et après chirurgie [S2].
- Monde : problème de santé publique dans plusieurs pays à revenu faible ou intermédiaire (Asie du Sud et du Sud-Est, Afrique de l'Ouest) ; riz poli, manioc, thiaminases (poisson cru), antagonistes (noix de bétel, thé) ; risque maximal chez le nourrisson allaité par une mère carencée [S10, S11].
- Allemagne (proxy D-A-CH) : carence le plus souvent secondaire à une maladie (hyperemesis gravidarum, maladies digestives et hépatiques, alcoolisme chronique) [S12].
- Hyperemesis gravidarum : 177 cas publiés de Wernicke ; vomissements médians 7 semaines, perte 12,1 kg ; séquelles cognitives 65,4 %, perte de grossesse 50 %, décès maternel 5 % [S15].
- Bariatrique : 118 cas, bypass 52 %, sleeve aussi ; âge médian 33 ans ; vomissements 87,3 %, ataxie 84,7 %, troubles mentaux 76,3 %, oculomoteurs 73,7 % [S16].
- Pédiatrie : 88 cas (cancer 25, maladies digestives 19, malnutrition 17…) ; 37 % avaient reçu une nutrition parentérale sans thiamine [S17].
- Agonistes du GLP-1 : 15 cas de Wernicke (sémaglutide 8, tirzépatide 6), signal de disproportionnalité ROR 2,35 (IC 95 % 1,38–4,01) dans une base de pharmacovigilance ; presque tous avec symptômes digestifs (vomissements, perte pondérale) [S18]. Limite : base FAERS, signal et non causalité.

## 5. Physiologie normale
- Apports de référence (DGE, dérivation 2015) : adultes 19–25 ans 1,3 mg/j (H) et 1,0 mg/j (F) ; 25–65 ans 1,2/1,0 ; ≥ 65 ans 1,1/1,0 ; grossesse 1,2 (2e trim.) et 1,3 (3e trim.) ; allaitement 1,3 mg/j ; nourrissons 0,2–0,4 mg/j [S12]. ESPEN : EAR 0,9–1,0 mg/j, RDA 1,1–1,2 mg/j (valeurs non révisées depuis 1998) [S2].
- Besoin lié aux glucides : environ 0,4 mg de thiamine pour 4200 kJ de métabolisme glucidique (FI suisse) [S4]. D'où le danger d'une charge glucidique chez un carencé [S7].
- Sources : céréales complètes, légumineuses, viandes, noix, aliments enrichis [S2, S12] ; sensible à la chaleur, à l'oxygène et à l'eau (cuisson douce) [S12].
- Absorption : jéjunum et iléon, transport actif saturable (THTR2 apical, THTR1 basolatéral), diffusion passive aux fortes concentrations ; inhibée par l'alcool et la carence en folates [S2, S11].
- Formes : ThMP, **ThDP (= pyrophosphate de thiamine, forme active)**, ThTP ; environ 80 % des 25–30 mg corporels sous forme de ThDP [S2]. S7 indique 30–50 mg de réserves. Près de 80 % de la thiamine du sang total est érythrocytaire (ThDP) ; plasma pauvre [S2, S10].
- Fonctions du ThDP : coenzyme de la **pyruvate déshydrogénase** (glycolyse → cycle de Krebs), de l'**α-cétoglutarate déshydrogénase** (cycle de Krebs), de la **transcétolase** (voie des pentoses phosphates, NADPH), de la déshydrogénase des α-cétoacides ramifiés et de la 2-hydroxyacyl-CoA lyase [S6, S7, S10, S11]. Rôle dans l'excitation nerveuse et la transmission neuromusculaire [S4].
- Réserves et demi-vie : réserves épuisées en **environ 18–20 jours** à 6 semaines d'apport nul ou insuffisant [S2, S6, S7] ; demi-vie de 18 jours [S6] ; FI : demi-vie d'élimination 10–20 jours aux doses physiologiques [S4]. Élimination urinaire [S4, S6].

## 6. Mécanismes : du normal au pathologique
- Déficit en ThDP → blocage de la pyruvate déshydrogénase → accumulation de pyruvate → **lactate** ↑ → acidose lactique ; ATP ↓ [S6, S7, S11].
- Cerveau (forte demande énergétique) : acidose lactique focale, rupture de la barrière hémato-encéphalique, excitotoxicité glutamatergique (transporteurs astrocytaires du glutamate diminués), inflammation microgliale, déficit en ATP [S7]. Lésions périventriculaires : thalamus, hypothalamus, région périaqueducale, corps mamillaires, cervelet [S7].
- Béribéri sec : perturbations glutamatergiques et GABAergiques, myélinisation réduite par atteinte de la voie des pentoses [S11].
- Béribéri humide : vasodilatation périphérique → activation sympathique et rénine-angiotensine → rétention hydrosodée → baisse de postcharge + hypervolémie = insuffisance cardiaque **à haut débit** ; atteinte endothéliale (NO) possible avec hypertension pulmonaire et insuffisance droite ; dans le Shoshin, l'acidose lactique déprime la contractilité et aggrave la vasodilatation → choc [S11].
- Glucose chez le carencé : la charge glucidique augmente les besoins et précipite le Wernicke [S7] ; dans l'hyperemesis gravidarum, le Wernicke a été aggravé par du glucose IV dans 14,1 % des cas [S15]. EFNS : thiamine **avant tout glucide** [S3]. Nuance : des études récentes n'ont pas montré de différence entre thiamine avant ou après un glucose de courte durée (citées par S7) — la thiamine ne doit pas retarder la correction d'une hypoglycémie (inférence à formuler prudemment ; non énoncée telle quelle dans une recommandation lue).

## 7. Causes et facteurs de risque
Classement mécanistique [S7], complété par [S2, S10, S12] :
| Mécanisme | Exemples |
|---|---|
| Apport diminué | alcool, anorexie mentale, jeûne, malnutrition du sujet âgé, nutrition parentérale sans thiamine, vomissements (hyperemesis gravidarum), insécurité alimentaire |
| Absorption diminuée | alcool, maladie de Crohn, sténose pylorique, diarrhée chronique, résections, **chirurgie bariatrique** (vomissements + bypass) ; antiacides (FI) |
| Stockage diminué | insuffisance hépatique terminale, alcool |
| Utilisation altérée | variants de la transcétolase |
| Besoins/pertes accrus | charge glucidique, hyperthyroïdie, cancers à croissance rapide, sepsis/soins intensifs, grossesse, diurétiques au long cours, dialyse et épuration extra-rénale continue (pertes ≈ 4–5 mg/j) |
Sources : S2 (diurétiques, épuration continue, bariatrique, grossesse, alcool, cancers), S4 (antiacides, 5-fluorouracile et thiosemicarbazone antagonistes), S6 (pertes CRRT), S7 (tableau), S10 (thiaminases, nourrisson), S12. Hépatopathie : carences fréquentes en vitamines hydrosolubles, surtout thiamine ; risque de renutrition et de carence en thiamine chez le cirrhotique [S22].
- Syndrome de renutrition : complication de la renutrition d'un patient dénutri, associée à une mortalité accrue ; la thiamine est une priorité [S2, S13, S14]. Critères de dépistage suisses : IMC bas, perte de poids involontaire importante, apport faible ou nul, abus d'alcool ou de drogues [S13].
- Agonistes du GLP-1 avec vomissements/perte rapide : signal récent [S18].

## 8. Anamnèse
- Rechercher : alcool, apport alimentaire des jours précédents, vomissements (durée), chirurgie bariatrique ou digestive, nutrition parentérale, grossesse avec hyperemesis, cancer, dialyse, diurétiques, traitement GLP-1 [S2, S7, S15, S16, S18].
- Prodromes fréquents : **nausées et vomissements** (100 % dans l'hyperemesis ; 60 %/55 % chez l'enfant), vision double ou floue [S15, S17].

## 9. Examen clinique
- **Wernicke** : triade classique — 1) état mental altéré et/ou déficit mnésique ; 2) nystagmus, ophtalmoplégie ou autres troubles oculomoteurs ; 3) ataxie/troubles de la marche [S7]. Triade complète rare (≈ un tiers) [S9] ; près d'un cinquième des cas confirmés n'ont aucun de ces signes [S7].
- **Korsakoff** : amnésie globale, confabulation, apathie [S7].
- **Béribéri humide** : insuffisance cardiaque à haut débit, tachycardie, œdèmes des membres inférieurs, dyspnée, congestion hépatique et splénique, prédominance droite, hypertension pulmonaire [S11]. **Shoshin** : choc cardiogénique, lactate élevé, acidose métabolique, fatigue, anorexie, douleurs abdominales, sans œdème [S10, S11].
- **Béribéri sec** : polyneuropathie périphérique, faiblesse musculaire ; S6 cite aussi confusion, ataxie, nystagmus [S6, S11]. FI : polynévrite, bradycardie, altérations psychiques en carence prolongée [S4].
- **Béribéri infantile** (< 4 mois, mère carencée) : irritabilité, refus du sein, tachycardie, tachypnée, vomissements, cri strident puis aphonie ; puis insuffisance cardiaque (œdème pulmonaire, hépatomégalie, cyanose) ; plus tard : nystagmus, ophtalmoplégie, fontanelle bombée, troubles de conscience, piège méningite [S10].

## 10. Examens complémentaires
- **ThDP dans le sang total ou les érythrocytes** (HPLC, ± spectrométrie de masse) : examen de référence (ESPEN Recommandation 14.2, grade A) ; le plasma n'est pas utilisé ; pré-analytique strict (protection de la lumière, température) [S2]. Valeurs attendues du ThDP sanguin ≈ 70–180 nmol/L, sans seuil universel de carence [S10]. Le ThDP érythrocytaire n'est pas affecté par l'inflammation, contrairement à beaucoup de vitamines [S2].
- **Prélever avant la première dose**, mais ne jamais retarder le traitement : résultat différé, confirmation a posteriori [S2, S3, S7].
- Activité de la transcétolase érythrocytaire (coefficient d'activation ETKAC) : alternative indirecte si ThDP indisponible ; ≤ 1,15 adéquat, 1,15–1,25 risque modéré, > 1,25 risque élevé, béribéri généralement > 1,4 ; interprétation difficile si synthèse enzymatique altérée [S2, S10].
- Autres marqueurs : lactate, pyruvate, α-cétoglutarate, glyoxylate [S2].
- **IRM** : soutient le diagnostic (EFNS niveau B) [S3] ; hypersignal T2 thalamique paraventriculaire, hypothalamique, périaqueducal ; atrophie mamillaire et cérébelleuse ; lésions typiques seulement chez 58 % ; **sensibilité 53 %, spécificité 93 %** ; anomalies rapidement réversibles sous thiamine [S7]. La méta-analyse 2026 rapporte des lésions typiques chez 82 % des patients imagés et atypiques chez 44,8 % [S9] ; pédiatrie : sensibilité 85 % [S17]. Écart à signaler comme incertitude.
- **Test thérapeutique** : la réponse clinique à la thiamine confirme rétrospectivement (ESPEN : essai de supplémentation ; béribéri : diagnostic parfois seulement après amélioration) [S2, S10, S11].

## 11. Diagnostic et diagnostic différentiel
- **Critères de Caine (1997)** chez l'alcoolique : **2 signes sur 4** — carence alimentaire, signes oculaires, dysfonction cérébelleuse, état mental altéré ou trouble mnésique léger [S8] ; repris par l'EFNS (niveau B) [S3]. Fiabilité diagnostique 100 % entre évaluateurs ; sous-reconnaissance seulement en cas d'encéphalopathie hépatique associée (sensibilité 50 %) [S8]. S7 cite sensibilité 94 %, spécificité 99 %.
- EFNS : tenir compte des différences de présentation alcool / non-alcool (niveau C) ; suspecter le Wernicke dans toute situation pouvant mener à une carence (GPP) [S3].
- Différentiels documentés dans les sources lues : encéphalopathie hépatique (coexistence fréquente, masque le Wernicke) [S8] ; méningite (béribéri infantile) [S10] ; sepsis (Shoshin) [S10] ; ivresse masquant les signes aux urgences [S20]. Autres différentiels (AVC du tronc, sevrage, intoxications) : non lus → lacune.

## 12. Urgences
- Wernicke suspecté : thiamine IV immédiate, avant tout glucide [S3]. Aux urgences, thiamine parentérale à tout sujet à risque (EFNS, GPP) [S3] ; patients alcooliques à alimentation pauvre : vitamines B IV ou IM d'emblée, surtout si l'ivresse masque les signes (RCP Londres) [S20].
- Soins intensifs : thiamine 100–300 mg/j IV dès l'admission pendant 3–4 jours (ESPEN Rec. 14.5, grade B) [S2] ; Amrein/Berger : 300 mg IV/j chez les patients à risque et 100 mg chez les autres pendant les 48 premières heures, pour permettre la métabolisation du glucose 5 % [S6].
- Shoshin : choc cardiogénique réversible sous thiamine ; récupération en heures chez le nourrisson, fonction cardiaque normalisée en jours [S10].

## 13. Prise en charge (Suisse et Europe)
### 13.1 Doses (ESPEN 2022, tableau 8) [S2]
| Situation | Dose |
|---|---|
| Carence légère, ambulatoire | 10 mg/j pendant 1 semaine, puis 3–5 mg/j ≥ 6 semaines |
| Diurétiques au long cours | suggestion 50 mg/j per os |
| À risque de carence | 100 mg 3×/j IV |
| Forte suspicion ou carence prouvée | 200 mg 3×/j IV |
| Encéphalopathie d'étiologie incertaine, dont Wernicke | 500 mg 3×/j IV |
| Entretien d'une carence prouvée | 50–100 mg/j per os |
| Syndrome de renutrition | 300 mg IV avant la nutrition, puis 200–300 mg IV/j ≥ 3 jours |
| Épuration extra-rénale continue | 100 mg/j |
| Hospitalisé, maladie critique | 100–300 mg/j |
- ESPEN Rec. 14.6 (grade B) : tout patient hospitalisé avec apport réduit les jours précédents ou forte consommation d'alcool → 100–300 mg/j per os ou IV [S2]. Rec. 14.7 (grade 0) : bonne absorption orale sauf gastrite alcoolique ; en carence aiguë sévère, la voie IV est la plus efficace (3 × 100–300 mg/j) [S2]. Encéphalopathie chez l'alcoolique : 250 mg IV requis du fait de la mauvaise absorption [S2]. Carence chronique sans maladie aiguë : voie orale adéquate ; maladie aiguë : voie IV [S2].
- EFNS : **200 mg 3×/j, de préférence IV, avant tout glucide** (niveau C) ; sécurité très bonne (niveau B) [S3]. S7 rapporte : EFNS jusqu'à absence d'amélioration supplémentaire ; auteurs britanniques 500 mg 3×/j pendant 2–3 jours puis 250 mg/j.
- Cochrane 2013 : preuves randomisées **insuffisantes** pour fixer dose, fréquence, voie ou durée chez l'alcoolique ; un seul essai exploitable (200 mg/j > 5 mg/j sur un test cognitif) [S19]. Les doses sont donc consensuelles.
- Béribéri : 100–300 mg/j suffisent généralement, durée ≥ 6 semaines, voie orale possible ; Shoshin : voie parentérale à doses plus élevées ; dilution IV en soluté salé **sans glucose** ; rééducation si neuropathie [S11] (revue brésilienne : utiliser pour le mécanisme, les doses européennes priment).
- Hyperemesis gravidarum : 100 mg IV ou IM si vomissements persistants ou sévères tardifs pour prévenir le Wernicke ; traitement curatif « adéquat » défini > 500 mg/j IM ou IV dans la revue [S15].
- Bariatrique : suivi du statut en thiamine ≥ 6 mois (EFNS niveau B) et supplémentation parentérale (GPP) [S3] ; SMOB : multivitamines (minéraux et oligo-éléments compris) à long terme après anneau, sleeve et bypass proximal, à vie après chirurgie malabsorptive ; bilan annuel du statut vitaminique ; vérifier le succès du traitement d'une carence avérée [S21]. Traitement souvent insuffisant dans les cas publiés (77,2 %) [S16].
- Hépatopathie alcoolique : thiamine en routine pour prévenir Wernicke-Korsakoff ; première dose de thiamine avant de débuter une nutrition parentérale chez le patient à haut risque [S22].
- Renutrition (algorithme suisse Friedli/Stanga/Schuetz 2018) : dépistage, démarrage prudent avec augmentation progressive des apports énergétiques et hydriques, supplémentation en électrolytes et vitamines, surveillance clinique étroite [S13, S14]. Doses de thiamine : prendre ESPEN tableau 8 [S2] (doses détaillées de l'algorithme non lues : lacune).

### 13.2 Médicament suisse — Benerva® (thiamine HCl), FI Swissmedic, mise à jour avril 2019 [S4]
- Formes : comprimés 100 mg et 300 mg ; ampoules 1 ml = 100 mg (IM ou IV lente).
- Indications : carences par apport insuffisant, besoins accrus ou malabsorption (dont abus d'alcool) ; béribéri, encéphalopathie de Wernicke, myocardiopathie alcoolique.
- Posologie adulte/adolescent ≥ 12 ans : prophylaxie 100 mg un jour sur deux per os ; symptômes modérés 100 mg/j ; graves 200–300 mg/j per os ; carence sévère (Wernicke, béribéri, myocardiopathie) : parentéral jusqu'à 200 mg/j, puis relais oral dès que possible. **Écart notable** : la FI plafonne à 200 mg/j parentéral, alors qu'ESPEN/EFNS recommandent 600–1500 mg/j dans le Wernicke [S2, S3] → présenter comme contentieux (mot vert) : la source primaire la plus récente (ESPEN 2022) l'emporte pour la conduite, la FI reste la référence d'autorisation (usage hors FI à signaler).
- Mises en garde : IV réservée aux hospitalisés ; préférer l'oral quand possible pour prévenir les réactions anaphylactoïdes ; injection très lente.
- Interactions : 5-fluorouracile et thiosemicarbazone antagonisent la thiamine ; antiacides diminuent l'absorption.
- Effets indésirables : réactions allergiques/anaphylactiques ; digestifs (comprimés) ; réactions au point d'injection. Aucun cas d'hypervitaminose connu. Interférences : urobilinogène (Ehrlich) faux positif, théophylline (Schack-Waxler).
- Contre-indication : hypersensibilité ; comprimés 100 mg (lactose, saccharose) contre-indiqués en cas d'intolérance au galactose/fructose, déficit en lactase de Lapp, malabsorption glucose-galactose, déficit en sucrase-isomaltase.
- Grossesse/allaitement : doses de besoin possibles ; hautes doses seulement si nécessité absolue (pas d'études contrôlées).
- Autres produits suisses repérés mais **non lus** (combinaisons B1/B6/B12 injectables, Bécozyme forte) : ne pas citer sans lecture (lacune).

### 13.3 Sécurité de la thiamine
- Pas de limite supérieure (UL) ; excès éliminé dans l'urine ; anaphylaxie rare à haute dose IV ; > 400 mg peuvent provoquer nausées, anorexie, ataxie légère [S2]. Anaphylaxie : 4 cas par million d'administrations IV et 1 par 5 millions IM [S7]. Rapport bénéfice/risque très favorable au traitement empirique [S3, S7].

## 14. Suivi et pronostic
- Après Wernicke : ≈ 50 % de séquelles durables (mémoire, Korsakoff) ; dans le Wernicke alcoolique, ≈ 80 % évoluent vers Korsakoff et ≈ 40 % pourraient mourir de complications ; hors alcool, ≈ 20 % de guérison complète et ≈ 20 % de décès (chiffres d'une revue, sources secondaires) [S7]. Méta-analyse 2026 : mortalité globale 5,1 % (8,8 % hors alcool) [S9] → discordance à expliciter (séries anciennes vs récentes).
- Pédiatrie : rémission complète 61 % ; doses parentérales plus élevées associées à une récupération plus rapide [S17].
- Bariatrique : prophylaxie au long cours ; contrôles annuels du statut vitaminique [S21] ; suivi thiamine ≥ 6 mois [S3].
- Sujet alcoolique : la carence en thiamine est fréquente et contribue aux troubles cognitifs (revue systématique européenne, résumé non exploité en détail) — lacune partielle.

## 15. Situations particulières
- Grossesse : besoins accrus (DGE 1,2–1,3 mg/j) [S12] ; hyperemesis → Wernicke entre 10 et 15 semaines de gestation [S15].
- Nourrisson : béribéri infantile, surtout 2e–3e mois, allaitement exclusif par mère carencée [S10].
- Enfant : Wernicke non alcoolique (cancer, maladies digestives, nutrition parentérale sans thiamine) [S17].
- Soins intensifs, sepsis : carence fréquente ; essai 2 × 200 mg/j 7 jours : lactate en baisse, mortalité moindre dans le sous-groupe carencé (13 vs 46 %) — essai de petite taille [S6].
- Nutrition parentérale : ≥ 2,5 mg/j (ESPEN Rec. 14.4, grade B) ; entérale 1,5–3 mg/1500 kcal (Rec. 14.3) [S2]. L'oubli de la thiamine en nutrition parentérale est une cause évitable [S2, S17].
- Insuffisance cardiaque sous diurétiques : statut à doser en cas de cardiomyopathie (Rec. 14.1, grade 0) [S2].

## 16. Critères formels du diagnostic (pour `div.alert`)
1. Critères opérationnels de Caine / EFNS (Wernicke, alcoolique) : ≥ 2 sur 4 — carence alimentaire ; signes oculomoteurs ; dysfonction cérébelleuse ; état mental altéré ou trouble mnésique léger [S3, S8].
2. Confirmation biologique : ThDP bas dans le sang total ou les érythrocytes (sans seuil universel ; valeurs attendues ≈ 70–180 nmol/L) [S2, S10], ou ETKAC > 1,25 (risque élevé) [S10].
3. IRM compatible (soutien, niveau B) [S3, S7].
4. Réponse au traitement par thiamine (confirmation rétrospective) [S2, S10].
Aucune source lue ne donne de critères formels consensuels du béribéri adulte : diagnostic clinique + test thérapeutique [S10, S11].

## 17. Paramètres clés (pour `div.key`)
- Besoins adulte ≈ 1,0–1,3 mg/j [S12] ; réserves 25–50 mg [S2, S7] ; épuisement en ≈ 18–20 jours [S2, S6].
- ThDP sang total attendu ≈ 70–180 nmol/L [S10] ; ≈ 80 % érythrocytaire [S2, S10].
- Wernicke : 200 mg 3×/j IV (EFNS) à 500 mg 3×/j IV (ESPEN) ; à risque 100 mg 3×/j IV ; renutrition 300 mg IV avant d'alimenter [S2, S3].
- IRM : sensibilité 53 %, spécificité 93 % [S7] ; triade complète ≈ 33 % [S9].
- Benerva® : cp 100/300 mg, amp. 100 mg/1 ml ; parentéral jusqu'à 200 mg/j selon FI [S4].

## 18. Lacunes explicites
- Aucune recommandation suisse dédiée au Wernicke ou au béribéri trouvée en accès libre ; l'article de la Revue Médicale Suisse 2022 (HUG) n'a pu être lu qu'en résumé (accès abonné) [S5].
- Texte intégral EFNS 2010 inaccessible (403) : seul le résumé est utilisé [S3] ; doses de durée/relais non lues dans l'original.
- Recommandations suisses de médecine des addictions (SSAM) sur la thiamine dans le sevrage : non trouvées (recherche web épuisée).
- Doses de thiamine précises de l'algorithme suisse de renutrition (Friedli 2018) : résumé seulement [S13].
- Seuils de laboratoire suisses (ThDP, laboratoires universitaires) : non lus.
- Rôle du magnésium comme cofacteur (Wernicke réfractaire) : non trouvé dans les sources lues ; ne pas écrire.
- Codage du Korsakoff (F10.6 / E51.2 + F04) dans la CIM-10-GM : non vérifié.
- Différentiel détaillé (AVC vertébrobasilaire, sevrage, intoxications, encéphalopathies métaboliques) : non sourcé.
- Valeurs D-A-CH : la page lue est celle de la DGE ; adoption par la Société suisse de nutrition non vérifiée.
- Autres spécialités suisses à base de thiamine (associations) : FI non lues.
- Mention obligatoire : dossier de recherche IA ; audit différé ; distinct d'une validation médicale humaine.
