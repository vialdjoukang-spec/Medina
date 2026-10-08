# Lot I83-HARMONISATION-3 — I83 — Varices des membres inférieurs (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I83-HARMONISATION-2` (tête `d6178b5`, reçu par Codex en `7b5ebff`, non injecté). Il en conserve toutes les corrections ([rapport v2](../2026-10-08-I83-HARMONISATION-2/rapport.md)) et lève les deux réserves de la [réception Codex](../../../../../docs/collaboration/reviews/2026-10-08/PR12_D6178B5_I83_HARMONISATION_2/RECEPTION.md). Base : `main` `7b5ebffcc12758886a569500d47813ce97b1edc5`, dont les sources I83 sont identiques à `8d6deee`. Le glossaire est inchangé depuis la v2.

## Réserve bloquante — écho-Doppler après ablation

**Constat de Codex, exact.** Sept passages prescrivaient encore un écho-Doppler systématique à une ou quatre semaines, en contradiction avec le paragraphe ARTE fondé sur les recommandations nord-américaines de 2023.

**Textes primaires relus.**
- ESVS 2022, recommandation 27 (texte local `esvs2022_cvd.txt`) : « duplex ultrasound surveillance should be considered one to four weeks after treatment », classe IIa, niveau C, consensus ; § 4.1.7 : contrôle de l'occlusion et de l'absence de thrombose profonde.
- SVS/AVF/AVLS 2023, partie II, § 11 :
  - 11.1.1 : contre l'écho-Doppler précoce systématique chez l'asymptomatique à risque moyen après ablation thermique, grade 1B ;
  - 11.1.2 : admis après ablation non thermique, consensus ;
  - 11.1.3 : prévu chez l'asymptomatique à haut risque, consensus ;
  - 11.1.4 : recommandé chez le symptomatique, grade 1A.

**Correction.** La divergence est exposée une fois, avec sa raison et une conduite stratifiée, dans l'îlot Suivi de `I83_b.html` : un symptôme ou un risque thromboembolique élevé imposent l'examen ; chez les autres patients, il se décide selon la technique et le protocole local. Les six autres passages renvoient à cette règle sans la contredire :

| Passage | Fichier |
| --- | --- |
| Prévention thromboembolique (fin de paragraphe) | `I83_b.html` |
| Encadré de synthèse des traitements | `I83_b.html` |
| À retenir du suivi et de la récidive | `I83_b.html` |
| Paramètres clés du dernier îlot | `I83_b.html` |
| Science → examen (cartographie et suivi) | `I83_c.html` |
| Pareto des traitements | `I83_pop2.html` |

Le bouton de `I83_c.html` vers `i83-thermique` est renommé « extension du thrombus liée à l'ablation ».

**Nuance « seulement ».** « Les classes I et II, que seul un dépistage échographique systématique découvre… » devient : « La portée clinique de la classe I, et probablement de la classe II, est minime ; ces formes sont surtout découvertes par un écho-Doppler fait en l'absence de symptôme. » Cette phrase suit le texte primaire : « the clinical relevance of ARTE I and likely even ARTE II is minimal ».

## Réserve mineure — K<sub>f</sub> et σ

L'augmentation de K<sub>f</sub> et la diminution de σ sont désormais présentées au conditionnel. Le texte précise qu'il s'agit d'une inférence tirée de la physiologie microvasculaire générale, non mesurée directement dans la maladie veineuse chronique.

## Contrôles (base `main` `7b5ebff`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I83` | `{}` |
| `test_v7.py --static I83` | OK — 41 707 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I83` (1 360 et 390 px) | 1 923 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` | 72 contrôles réussis |
| `test_v7.py I83` | OK |
| `tools/livraison.py check-claude --root <main 7b5ebff propre>` | empreintes et chemins conformes |
| Recherche des formulations résiduelles (« une à quatre semaines », « contrôle échographique », « thrombose induite par la chaleur ») | aucune occurrence non nuancée |

## Limites

Les limites de la v2 sont maintenues :
- le total de 212 participants de la donnée cadexomère n'est pas relu ;
- la recommandation ESVS sur l'occlusion de la veine fémorale commune n'est pas relue ;
- les affirmations négatives OFSP ne sont pas certifiées ;
- la couverture CIM-11 n'est pas établie.
