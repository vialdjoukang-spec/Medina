# Preuves ESC 2026 — I33 — Endocardite infectieuse (C-01-Cardiologie)

Réserve levée : MED-01 (preuve reproductible), audit médical Codex du 8 octobre 2026. Provenance et reproduction : `../PROVENANCE.md`. Fichiers contrôlés : `out/i33-esc-2026-comparaison__P1.html` et `jobs/i33-esc-2026-comparaison__P1.json` (aucun complément du texte).

## 1. Infarctus par embolie coronaire : « primaire » et non plus « type 2 »

- **Document** : Fifth Universal Definition of Myocardial Infarction (2026), ESC/ACC/AHA/WHF, doi:10.1093/eurheartj/ehag101, 28 août 2026. Document de consensus, sans classe.
- **Tableau** : **tableau 1** (« Comparison of the Fourth and Fifth Universal Definitions of Myocardial Infarction »).
- **Ligne 2026** : « Primary myocardial infarction — Includes all acute coronary pathologies: atherothrombosis; spontaneous coronary artery dissection; coronary embolism; vasospasm; and restenosis, stent thrombosis, or graft failure >30 days from procedure. »
- **Ligne antérieure comparée (quatrième définition, même tableau)** : « Type 2 myocardial infarction — Myocardial oxygen supply–demand imbalance due to either: • Acute coronary pathology other than atherothrombosis, including spontaneous coronary artery dissection, coronary embolism, and vasospasm ».
- **Infarctus secondaire (2026)** : « Myocardial oxygen supply–demand imbalance due to an alternative acute condition ».
- **Justification du tableau (colonne « Rationale for change »)** : « Promotes coronary angiography and adjunctive testing to confirm diagnosis and identify underlying acute coronary pathology ».
- **Conséquence** : classification, non indication thérapeutique.

## 2. Enveloppe antibiotique chez l’hémodialysé ou le greffé rénal

- **Document** : 2026 ESC Guidelines for the management of cardiovascular disease and chronic kidney disease, doi:10.1093/eurheartj/ehag098, section 9.2.3.1, **tableau de recommandations 28**.
- **Ligne** : « Application of an antibiotic envelope may be considered in addition to peri-operative antibiotic prophylaxis in patients on haemodialysis or after kidney transplantation who undergo CIED implantation to reduce the risk of CIED-related infection. » — **IIb, C**.
- **Texte de justification (section 9.2.3.1)** : WRAP-IT, 6983 patients, réduction des infections « without evidence of effect modification by baseline kidney function » ; score BLISTER incluant « eGFR <30 mL/min/1.73 m2 ».
- **Ligne antérieure comparée** : 2023 ESC Guidelines for the management of endocarditis, doi:10.1093/eurheartj/ehad193, **tableau de recommandations 20** (« cardiovascular implanted electronic device-related infective endocarditis ») : « Use of an antibiotic envelope may be considered in select high-risk patients undergoing CIED reimplantation to reduce risk of infection. » — **IIb, B**.

## 3. Défibrillateur sous-cutané chez l’hémodialysé

- **Document et tableau** : ESC 2026 maladie rénale chronique, **tableau de recommandations 28**.
- **Ligne** : « Where an ICD is indicated, implantation of a subcutaneous defibrillator may be considered as an alternative to transvenous ICD if there is no need for either bradycardia pacing, cardiac resynchronization, or ATP in patients with CKD on haemodialysis to reduce the risk of SCD and CIED-related infections. » — **IIb, C**.
- **Ligne antérieure** : aucune ligne correspondante relevée dans l’ESC 2023 sur l’endocardite.

## 4. Information de l’hémodialysé sur l’endocardite après prothèse

- **Document** : ESC 2026 maladie rénale chronique, **section 10** (texte, sans classe) : « patients on haemodialysis should be made aware of the increased risk of endocarditis after prosthetic valve intervention. »

## 5. Réadaptation et contrôle de l’infection

- **Document** : ESC 2026 réadaptation, doi:10.1093/eurheartj/ehag099, **tableau 4** (descriptif, sans classe) : « Acute systemic illness » (contre-indication à l’épreuve d’effort et à l’entraînement) ; « Recent embolism » (contre-indication à l’entraînement).
- **Constat** : le texte 2026 sur la réadaptation ne mentionne pas l’endocardite.
- **Ligne antérieure comparée** : ESC 2023 endocardite, **tableau de recommandations 18** (« post-discharge follow-up ») : « Cardiac rehabilitation including physical exercise training should be considered in clinically stable patients based on an individual assessment. » — **IIa, C**.

## Changements retirés ou requalifiés

- Aucun nouveau retrait dans cette passe. Les retraits antérieurs (extension de code CIM-11 « coronary embolism », classes de la réadaptation après chirurgie valvulaire) restent tracés dans `out/i33-esc-2026-comparaison__P1.json`.

## Limites

- La cinquième définition est un consensus ESC/ACC/AHA/WHF, non une recommandation au sens strict.
- Aucun essai n’a testé l’enveloppe chez le seul hémodialysé ; la classe IIb, C le reflète.
