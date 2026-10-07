# Justification systématique des cours de Claude — avancement

Chaîne par cours : producteurs P1 et P2 (`TACHE_PRODUCTION.md`) → vérificateur indépendant (`TACHE_VERIFICATION.md`) → `appliquer_justifications.py <CODE> <CODE>/ --ecrire` → `manifeste.py <CODE>` → contrôles → commit.

| Cours | Production | Vérification | Application et contrôles | Commit |
| --- | --- | --- | --- | --- |
| I48 — Fibrillation et flutter auriculaires | fait (lot 4) | fait | fait | b1f19c3 |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | fait | fait (167 acceptés, 30 corrigés ; 12 fenêtres corrigées) | fait : test statique OK, 23 223 → 30 961 mots | voir journal |
| I33 — Endocardite infectieuse | fait | fait (125 acceptés, 20 corrigés, 6 ajouts du vérificateur ; 10 fenêtres corrigées) | fait : test statique OK, 24 133 → 33 006 mots | voir journal |
| I35 — Valvulopathies aortiques | fait | fait (145/146 compléments, 10 fenêtres corrigées) | fait : test statique OK, 26 480 → 34 279 mots | voir journal |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | fait | fait (132 acceptés, 26 corrigés, 8 ajouts du vérificateur ; 5 fenêtres corrigées) | fait : test statique OK, 27 812 → 33 788 mots | voir journal |
| I00 — Rhumatisme articulaire aigu | fait | fait (87 acceptés, 30 corrigés, 2 rejetés ; 12 fenêtres corrigées) | fait : test statique OK, 21 464 → 27 035 mots | voir journal |
| I40 — Myocardites | fait | fait (157 acceptés, 31 corrigés ; 11 fenêtres corrigées) | fait : test statique OK, 24 113 → 33 442 mots | voir journal |
| I42 — Cardiomyopathies | fait | fait (112 acceptés, 28 corrigés, 10 ajouts du vérificateur ; doublon FA fusionné) | fait : test statique OK, 29 325 → 35 839 mots | voir journal |
| I44 — Troubles de la conduction et bradycardies | en cours | | | |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires | | | | |
| I49 — Extrasystoles et autres arythmies | | | | |
| I46 — Arrêt cardiaque | | | | |
| Q21 — Cardiopathies congénitales de l’adulte | | | | |
| I71 — Anévrismes et dissections artérielles | | | | |
| I80 — Thrombose veineuse profonde et thromboses veineuses | | | | |

Reprise après interruption : les résultats partiels de chaque cours sont dans `<CODE>/`. Un producteur interrompu se relance sur ses seuls fichiers ; ses sorties existantes sont réutilisées si elles sont complètes.
