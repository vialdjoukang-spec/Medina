# Preuves ESC 2026 — I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie)

Réserves levées : MED-01 (preuve reproductible) et MED-03 (seuil de troponine et qualification de myopéricardite), audit médical Codex du 8 octobre 2026. Provenance et reproduction : `../PROVENANCE.md`.

Fichiers contrôlés : `out/i30-esc-2026-comparaison__P1.html`, `jobs/i30-esc-2026-comparaison__P1.json`, `edits/I30_c.json` (nouveau), `verdicts/I30_c.json` (nouveau).

## 1. Lésion myocardique aiguë : seuil propre au sexe

- **Document** : Fifth Universal Definition of Myocardial Infarction (2026), ESC/ACC/AHA/WHF, doi:10.1093/eurheartj/ehag101, publication du 28 août 2026. Document de consensus : il définit, il ne classe pas (aucune classe ni niveau).
- **Section et encadré** : section 6.1 et **encadré 1** (« Box 1: Criteria for acute myocardial injury »).
- **Population** : tout patient dont la troponine est dosée.
- **Ligne** : « Acute myocardial injury is defined as a rise and/or fall in cardiac troponin I or T with at least one value above the sex-specific 99th percentile URL. »
- **Phrase associée (section 6.1)** : « Sex-specific thresholds are necessary to avoid a systematic bias and the under-recognition of myocardial injury in female patients (see Section 14.1.1). »
- **Section 14.1.1** : « For high-sensitivity cardiac troponin I and T assays, the 99th percentile URL in females is lower than the uniform URL. In contrast, the 99th percentile URL in males is above the uniform URL. »
- **Référentiel antérieur comparé** : même document, section 6 : la troisième définition décrivait la lésion myocardique par « at least one value above the 99th percentile URL » ; section 2 : les définitions de 2007, 2012 et 2018 ont « promoted the use of sex-specific diagnostic criteria ».
- **Conséquence retenue (MED-03)** : la valeur se juge sur le 99e percentile validé pour la méthode et pour le sexe ; une variation jugée sur un seuil global commun aux deux sexes ne suffit pas ; seule une hausse ou une baisse avec au moins une valeur au-delà du seuil propre au sexe documente l’atteinte.
- **Limite** : aucun seuil chiffré par méthode n’est donné. La section 14.1.1 indique que, pour la troponine T, le seuil féminin vaut la moitié du seuil masculin « in a large and representative global healthy reference population » ; cette proportion, propre à une population de référence, n’est pas un seuil utilisable et est **retirée** de la fenêtre. Le chiffre de 14 ng/L (seuil unique du fabricant cité par le cours) n’est lu dans aucune source primaire de ce lot : il est **retiré** de la fenêtre et de la ligne canonique `I30_c` par le complément `I30_c-esc1`.

## 2. Qualification de myopéricardite

- **Document** : 2025 ESC Guidelines for the management of myocarditis and pericarditis, doi:10.1093/eurheartj/ehaf192, **section 8** (« Inflammatory myopericardial syndrome »), texte sans tableau de recommandations.
- **Définition** : « The diagnosis of predominant pericarditis with myocardial involvement, or ‘myopericarditis’, can be clinically established if patients with definite criteria for AP show elevated biomarkers of myocardial injury, without newly developed focal or diffuse impairment of LV function on TTE or CMR. »
- **Suite** : une altération nouvelle de la fonction ventriculaire gauche avec biomarqueurs élevés et critères de péricardite « suggests predominant myocarditis with pericardial involvement » ; « patients with perimyocarditis should be managed as patients with pure myocarditis ».
- **Conséquence retenue** : trois conditions, écrites dans la ligne `I30_c` et dans la fenêtre : critères de péricardite aiguë ; atteinte myocardique documentée (troponine au-delà du 99e percentile propre à la méthode et au sexe, définition n° 1) ; fonction ventriculaire gauche évaluée sans altération nouvelle.

## 3. Cathétérisme dans la constriction

- **Document** : ESC 2026 insuffisance cardiaque, doi:10.1093/eurheartj/ehag100, section 5.3, **tableau de recommandations 4** (« Investigations for underlying aetiology in patients with HFpEF or HFrEF »).
- **Population** : insuffisance cardiaque établie que l’on attribue à une constriction péricardique ou à une cardiopathie congénitale.
- **Ligne** : « Right heart catheterization[e] should be considered in patients where HF is thought to be due to constrictive pericarditis or congenital heart disease. » — **IIa, C**.
- **Note e** : « Right and left heart catheterization needed for the differential diagnosis of constrictive pericarditis and restrictive cardiomyopathy. »
- **Ligne antérieure comparée** : ESC 2025 myocardites et péricardites, section 11.9, **tableau de recommandations 24** (« Recommendations for constrictive pericarditis ») : « Cardiac catheterization for haemodynamic assessment should be considered in patients with suspected constrictive pericarditis when multimodality imaging is inconclusive. » — **IIa, C**.

## 4. Peptides natriurétiques abaissés dans la constriction

- **Document** : ESC 2026 insuffisance cardiaque, section 5.1.1, **tableau 9** (« Causes for increase or decrease in natriuretic peptide levels »), rubrique « Causes for decreased natriuretic peptide levels » : « Constrictive pericarditis ». Tableau descriptif, sans classe.
- **Référentiel antérieur comparé** : ESC 2025, section 4.5.5 : « The classic clinical picture is usually characterized by isolated right HF with normal or nearly normal natriuretic peptide levels. » L’ESC 2021 sur l’insuffisance cardiaque ne tabulait que les causes d’élévation (tableau 7).
- **Requalification** : la colonne « Avant 2026 » ne parle plus de « séries cliniques » non citées ; elle cite l’ESC 2025.

## 5. Effort après péricardite aiguë

- **Document** : ESC 2026 réadaptation, doi:10.1093/eurheartj/ehag099, section 4, **tableau 4** (« Clinical conditions that should be considered as contraindications to exercise testing, and/or training, or increased risk for exercise training »), colonne « Contraindications to exercise testing and training » : « Acute myocarditis and pericarditis ». Tableau descriptif, sans classe.
- **Ligne antérieure comparée** : ESC 2025, **tableau de recommandations 26** : « Restriction of physical exercise until remission, for at least 1 month, is recommended in athletes and non-athletes after IMPS using an individualized approach to accelerate recovery. » — **I, C**.

## Changements retirés ou requalifiés

- Retirés : « 14 ng/L » (fenêtre et ligne canonique), « environ la moitié du seuil masculin », et la phrase qui laissait une simple variation sous le seuil global signer une myopéricardite.
- Requalifiés : ligne « Troponine » (définitions antérieures citées d’après la section 2 et la section 6 de la cinquième définition) ; ligne « Peptides natriurétiques » (ESC 2025, section 4.5.5).

## Limites

- La cinquième définition est un document de consensus ; aucune classe n’y est attribuée.
- Les exemples Abbott de la même cellule canonique (16 ng/L chez la femme, 34 ng/L chez l’homme) n’ont pas été relus dans une notice du fabricant ; ils sont hors du champ de la réserve MED-03 et restent à vérifier.
