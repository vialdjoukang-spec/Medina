# Preuves ESC 2026 — I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)

Réserves levées : MED-01 (preuve reproductible) et MED-02 (formulation de l’ancre `I44_c-a1`), audit médical Codex du 8 octobre 2026. Provenance, empreintes et méthode de reproduction : `../PROVENANCE.md`. Citations limitées à la ligne du tableau et à ses notes.

Fichiers contrôlés : `out/i44-esc-2026-comparaison__P1.html`, `jobs/i44-esc-2026-comparaison__P1.json`, `edits/I44_a.json`, `edits/I44_b.json`, `verdicts/I44_a.json`, `verdicts/I44_b.json`.

## 1. Resynchronisation plutôt que stimulation ventriculaire droite dans le BAV de haut degré

- **Document** : 2026 ESC Guidelines for the management of heart failure, doi:10.1093/eurheartj/ehag100, publication en ligne du 28 août 2026.
- **Section et tableau** : section 6.2.2 (resynchronisation), **tableau de recommandations 7** (« Recommendations for cardiac resynchronization therapy implantation ») ; la même ligne figure au **tableau 6** (« Revised recommendations »), section « Management of chronic heart failure—Section 6 ».
- **Population** : patient en insuffisance cardiaque à fraction d’éjection réduite (HFrEF), quelle que soit la classe NYHA ou la largeur du QRS, qui a une indication de stimulation ventriculaire pour un BAV de haut degré.
- **Ligne** : « CRT, rather than RV pacing, should be considered in patients with HFrEF regardless of NYHA class or QRS width who have an indication for ventricular pacing for high-degree AV block in order to reduce the risk of HFH and death. »
- **Classe et niveau** : **IIa, B1** (référence 409 : BLOCK HF).
- **Notes du tableau** : a « Class of recommendation » ; b « Level of evidence » ; aucune note propre à cette ligne.
- **Définition de la population** (section 3.3.1 et section 13, « Key messages ») : « HFrEF: LVEF <50% + symptoms and/or signs of HF » ; « Stage B: pre-HF, defined as the presence of cardiac abnormalities without signs and symptoms of HF ». Tableau 4 : « HFrEF has been expanded to include LVEF up to 50% ».
- **Ligne antérieure comparée (1)** : ESC 2021 sur l’insuffisance cardiaque, colonne 2021 du **tableau 6 de l’ESC 2026** : « CRT rather than RV pacing is recommended for patients with HFrEF regardless of NYHA class or QRS width who have an indication for ventricular pacing for high degree AV block in order to reduce morbidity. This includes patients with AF. » — **I, A** (fraction réduite de 2021 : ≤ 40 %).
- **Ligne antérieure comparée (2)** : 2021 ESC Guidelines on cardiac pacing and cardiac resynchronization therapy, doi:10.1093/eurheartj/ehab364, section 6.5, tableau « Recommendation for patients with heart failure and atrioventricular block » : « CRT rather than RV pacing is recommended for patients with HFrEF (<40%) regardless of NYHA class who have an indication for ventricular pacing and high-degree AVB in order to reduce morbidity. This includes patients with AF. » — **I, A**. Note du tableau : « HFrEF = heart failure with reduced ejection fraction (<40%) according to the 2021 ESC HF Guidelines ».
- **Formulation retenue (MED-02)** : deux phrases distinctes. La règle de l’ESC 2021 sur la stimulation (classe I, niveau A, fraction < 40 %) n’est pas révisée par un texte de stimulation ; la règle de l’ESC 2026 sur l’insuffisance cardiaque (« should be considered », IIa, B1, insuffisance cardiaque à fraction < 50 %) est la plus récente. Aucune phrase n’attribue deux forces à une même recommandation.
- **Limite** : l’ESC 2026 n’explicite pas la raison de l’abaissement de la classe I à IIa.

## 2. Seuil < 50 % et essai BLOCK HF (≤ 50 %)

- **Document** : Curtis et al., *N Engl J Med* 2013;368:1585–93, doi:10.1056/NEJMoa1210356 (référence 409 de l’ESC 2026).
- **Population de l’essai (résumé, méthodes)** : « We enrolled patients who had indications for pacing with atrioventricular block; New York Heart Association (NYHA) class I, II, or III heart failure; and a left ventricular ejection fraction of 50% or less. »
- **Conséquence** : l’essai incluait des fractions ≤ 50 % ; la classification 2026 appelle « réduite » une fraction strictement < 50 %. Les deux seuils sont écrits distinctement dans la fenêtre, l’ancre et le complément `I44_b`.
- **Limite** : le texte de l’ESC 2021 sur la stimulation (section 6.5) décrit l’inclusion de BLOCK HF comme « <50% by inclusion criteria » ; la publication primaire (résumé) dit « 50% or less ». La fenêtre suit la publication primaire.

## 3. Niveau B1 : nouvelle échelle de preuve

- **Document** : ESC 2026 insuffisance cardiaque, **tableau 2** (« Levels of evidence—therapy and prevention »).
- **Ligne** : « B1 — Suggestive evidence from at least one adequately powered randomized controlled trial free of major bias, or a meta-analysis of such randomized controlled trials, with some evidence against the play of chance (e.g., P <0.05 for superiority). »
- **Conséquence** : B1 ne se compare pas terme à terme à l’ancien niveau A.

## 4. Mise à niveau vers une resynchronisation chez le patient appareillé

- **Document et tableau** : ESC 2026 insuffisance cardiaque, **tableau de recommandations 7**.
- **Population** : patient porteur d’un stimulateur ou d’un défibrillateur, fraction ≤ 35 %, aggravation de l’insuffisance cardiaque malgré un traitement optimal, part importante de stimulation ventriculaire droite.
- **Ligne** : « An upgrade to CRT should be considered in patients with an LVEF ≤35% who have received a conventional pacemaker or an ICD and subsequently develop worsening HF despite optimal FMT and who have a significant proportion of RV pacing in order to reduce the risk of HFH or death. »
- **Classe et niveau** : **IIa, B1**.
- **Ligne antérieure comparée** : ESC 2021 stimulation, section 6.4 : « Patients who have received a conventional pacemaker or an ICD and who subsequently develop symptomatic HF with LVEF ≤35% despite OMT, and who have a significant proportion of RV pacing, should be considered for upgrade to CRT. » — **IIa, B** ; note c : « A limit of 20% RV pacing for considering interventions for pacing-induced HF is supported by observational data. »

## 5. Vérifier la part de stimulation ventriculaire droite (nouvelle recommandation)

- **Document et tableaux** : ESC 2026 insuffisance cardiaque, **tableau 5** (« New recommendations ») et **tableau de recommandations 4** (« Investigations for patients with HFrEF »).
- **Population** : tout patient porteur d’un dispositif implantable avec une insuffisance cardiaque à fraction réduite nouvelle ou aggravée.
- **Ligne** : « Review of the proportion of RV pacing should be considered in all patients with CIED and de novo or worsening HFrEF. »
- **Classe et niveau** : **IIa, C**.
- **Ligne antérieure** : aucune (recommandation nouvelle, tableau 5).

## 6. Stimulation du système de conduction dans la fraction réduite

- **Document** : ESC 2026 insuffisance cardiaque, **section 6.2.3** (texte, sans tableau de recommandations).
- **Texte** : « no RCT with patient-centred outcomes has evaluated the efficacy or long-term safety of CSP in HFrEF. Therefore, no recommendations can currently be made. »
- **Référentiel antérieur** : consensus clinique ESC 2025 sur la stimulation du système de conduction (Glikson et al., référence 426 de l’ESC 2026). **Non relu** dans cette vérification.
- **Requalification** : la colonne 2021 de la fenêtre ne dit plus que ce consensus en fait une « alternative possible » ; elle le nomme seulement, « sans classe de recommandation ».

## 7. Enveloppe antibiotique chez l’hémodialysé ou le greffé rénal

- **Document** : 2026 ESC Guidelines for the management of cardiovascular disease and chronic kidney disease, doi:10.1093/eurheartj/ehag098, **section 9.2.3.1**, **tableau de recommandations 28** (« Recommendations for device management considerations when treating patients with chronic kidney disease »).
- **Population** : patient hémodialysé ou greffé rénal qui reçoit un dispositif implantable.
- **Ligne** : « Application of an antibiotic envelope may be considered in addition to peri-operative antibiotic prophylaxis in patients on haemodialysis or after kidney transplantation who undergo CIED implantation to reduce the risk of CIED-related infection. »
- **Classe et niveau** : **IIb, C**. Notes : a, b seulement.
- **Ligne antérieure comparée** : ESC 2021 stimulation, section 9.8, tableau « Recommendations regarding device implantations and peri-operative management » : « In patients undergoing a reintervention CIED procedure, the use of an antibiotic-eluting envelope may be considered. » — **IIb, B**.

## 8. Réadaptation après défibrillateur ou resynchronisation

- **Document** : 2026 ESC Guidelines on cardiac rehabilitation, doi:10.1093/eurheartj/ehag099, **section 5.6**, **tableau de recommandations 9** (« Recommendations for indications in patients with cardiac implantable electronic devices »).
- **Ligne** : « CR is recommended for patients after ICD or CRT device implementation to improve physical functioning (VO2peak, 6MWD). » — **I, B1**.
- **Constat** : ce tableau ne contient aucune ligne propre au stimulateur anti-bradycardique seul.
- **Ligne antérieure** : aucune recommandation classée de réadaptation dans l’ESC 2021 sur la stimulation (non recherchée au-delà de ce constat).

## Changements retirés ou requalifiés

- Retiré : la formule de l’ancre `I44_c-a1` « recommandée (ESC 2021, classe I ; ESC 2026 : classe IIa, fraction < 50 %) », qui donnait deux forces à une même phrase (MED-02).
- Requalifié : la colonne 2021 de la ligne « Stimulation du système de conduction » (consensus non relu).
- Corrigé : la source de la réadaptation (tableau de recommandations 9, et non « recommandations sur l’entraînement »).

## Limites

- Les tableaux 2026 sont lus sur l’extraction `pdftotext -layout` ; les PDF ne sont pas conservés.
- Le changement de classe est prouvé par le tableau ; sa validité clinique n’est pas réévaluée ici au-delà du texte de l’ESC.
