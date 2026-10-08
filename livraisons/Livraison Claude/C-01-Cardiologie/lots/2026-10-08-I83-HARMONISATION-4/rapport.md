# Lot I83-HARMONISATION-4 — I83 — Varices des membres inférieurs (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I83-HARMONISATION-3` (tête `205d2cb`, reçu par Codex en `0dc7aa9`, non injecté). Il conserve toutes les corrections des versions 2 et 3 ([rapport v2](../2026-10-08-I83-HARMONISATION-2/rapport.md), [rapport v3](../2026-10-08-I83-HARMONISATION-3/rapport.md)). Seul `I83_b.html` change, pour lever la réserve résiduelle de la [réception Codex](../../../../../docs/collaboration/reviews/2026-10-08/PR12_205D2CB_I83_HARMONISATION_3/RECEPTION.md). Base : `main` `0dc7aa93f8a8cea42b6aa556c38505a66b8919d5`, dont les sources I83 sont identiques à `8d6deee`. Le glossaire est inchangé depuis la v2.

## Réserve résiduelle — suivi échographique trop absolu

**Constat de Codex, exact.** Deux phrases de `I83_b.html` limitaient tout examen ultérieur à la récidive clinique : l'îlot Suivi et son encadré À retenir.

**Fondement.** ESVS 2022, § 4.1.7 : « For patients undergoing sequential treatments, such as staged sclerotherapy […], interval DUS is performed before the subsequent treatment stage. For most patients, repeat DUS assessment is required only for suspected clinical recurrence. » SVS/AVF/AVLS 2023, § 11 : écho-Doppler recommandé devant un symptôme (11.1.4, 1A) ; ARTE traitée jusqu'à la rétraction du thrombus (11.4.2).

**Correction.**

| Passage | Nouveau texte |
| --- | --- |
| Îlot Suivi | « Ensuite, pour la plupart des patients, un nouvel examen n'est utile qu'en cas de récidive clinique suspectée (ESVS 2022, § 4.1.7). Trois situations font exception : une extension du thrombus liée à l'ablation ou une thrombose profonde découverte, surveillée jusqu'à sa rétraction ou sa résolution ; tout symptôme nouveau, comme une douleur ou un œdème du membre ; et un traitement en plusieurs temps, comme une sclérothérapie par séances, où un écho-Doppler précède chaque nouvelle étape. » |
| À retenir | « Ensuite, un examen se refait devant une récidive clinique suspectée, un symptôme nouveau, une extension du thrombus ou une thrombose profonde en cours de surveillance, ou avant chaque étape d'un traitement en plusieurs temps. » |

Une recherche des formulations « n'est utile qu », « que devant une récidive » et « seulement devant une récidive » ne trouve plus d'occurrence restrictive dans le chapitre.

## Contrôles (base `main` `0dc7aa9`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I83` | `{}` |
| `test_v7.py --static I83` | OK — 41 796 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I83` (1 360 et 390 px) | 1 923 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` | 72 contrôles réussis |
| `test_v7.py I83` | OK |
| `tools/livraison.py check-claude --root <main 0dc7aa9 propre>` | empreintes et chemins conformes |

## Limites

Celles des versions précédentes sont maintenues :
- le total de 212 participants et la certitude GRADE de la donnée cadexomère ne sont pas relus ;
- la recommandation ESVS sur l'occlusion de la veine fémorale commune n'est pas relue ;
- les affirmations négatives OFSP ne sont pas certifiées ;
- la couverture CIM-11 n'est pas établie.
