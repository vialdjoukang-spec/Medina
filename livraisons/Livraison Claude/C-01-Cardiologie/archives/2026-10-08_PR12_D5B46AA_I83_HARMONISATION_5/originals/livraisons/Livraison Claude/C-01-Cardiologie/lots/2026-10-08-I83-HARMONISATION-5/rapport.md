# Lot I83-HARMONISATION-5 — I83 — Varices des membres inférieurs (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I83-HARMONISATION-4` (tête `e17107a`, reçu par Codex en `3dac928`, non injecté). Il conserve toutes les corrections des versions 2 à 4 ([v2](../2026-10-08-I83-HARMONISATION-2/rapport.md), [v3](../2026-10-08-I83-HARMONISATION-3/rapport.md), [v4](../2026-10-08-I83-HARMONISATION-4/rapport.md)). Seul `I83_b.html` change, pour lever la réserve majeure de la [réception Codex](../../../../../docs/collaboration/reviews/2026-10-08/PR12_E17107A_I83_HARMONISATION_4/RECEPTION.md). Base : `main` `3dac92808b055e235ee6f57cfec8e283455a85ca`, dont les sources I83 sont identiques à `8d6deee`. Le glossaire est inchangé depuis la v2.

## Réserve majeure — surveillance d'une thrombose profonde « jusqu'à sa résolution »

**Constat de Codex, exact.** La v4 étendait à toute thrombose profonde découverte une surveillance échographique jusqu'à sa résolution. Or la conduite d'une thrombose profonde dépend de son siège, de ses symptômes et de son risque d'extension. L'imagerie sériée à deux semaines, par exemple, ne vaut que pour certaines thromboses distales sans symptôme grave ni risque d'extension.

**Correction.** Ce lot n'ajoute aucune règle nouvelle ; il sépare les deux situations et renvoie chacune à sa source.

| Passage de `I83_b.html` | Nouveau texte |
| --- | --- |
| Îlot Suivi | « Quatre situations font exception. Une extension du thrombus liée à l'ablation, quand elle est traitée, l'est jusqu'à la rétraction du thrombus (Gloviczki et al., 2023, 11.4.2), ce qui suppose un contrôle échographique ; une thrombose profonde découverte suit, elle, la conduite propre à son siège, à ses symptômes et à son risque d'extension (cours I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie)). S'y ajoutent tout symptôme nouveau, comme une douleur ou un œdème du membre, et un traitement en plusieurs temps, comme une sclérothérapie par séances, où un écho-Doppler précède chaque nouvelle étape. » |
| À retenir | « …devant une récidive clinique suspectée, un symptôme nouveau, une extension du thrombus en cours de traitement, une thrombose profonde, qui suit sa propre conduite, ou avant chaque étape d'un traitement en plusieurs temps. » |

## Contrôles (base `main` `3dac928`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I83` | `{}` |
| `test_v7.py --static I83` | OK — 41 839 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I83` (1 360 et 390 px) | 1 923 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` | 72 contrôles réussis |
| `test_v7.py I83` | OK |
| `tools/livraison.py check-claude --root <main 3dac928 propre>` | empreintes et chemins conformes |

## Limites

Les limites des versions précédentes sont maintenues :
- le total de 212 participants de la donnée cadexomère n'est pas relu ;
- la recommandation ESVS sur l'occlusion de la veine fémorale commune n'est pas relue ;
- les affirmations négatives OFSP ne sont pas certifiées ;
- la couverture CIM-11 n'est pas établie.
