# Justification systématique des cours de Claude — avancement

Chaîne par cours : producteurs P1 et P2 (`TACHE_PRODUCTION.md`) → vérificateur indépendant (`TACHE_VERIFICATION.md`) → `appliquer_justifications.py <CODE> <CODE>/ --ecrire` → `manifeste.py <CODE>` → contrôles → commit.

| Cours | Production | Vérification | Application et contrôles | Commit |
| --- | --- | --- | --- | --- |
| I48 — Fibrillation et flutter auriculaires | fait (lot 4) | fait | fait | b1f19c3 |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | en cours | | | |
| I33 — Endocardite infectieuse | en cours | | | |
| I35 — Valvulopathies aortiques | fait | fait (145/146 compléments, 10 fenêtres corrigées) | fait : test statique OK, 26 480 → 34 279 mots | voir journal |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | en cours | | | |
| I00 — Rhumatisme articulaire aigu | en cours | | | |
| I40 — Myocardites | fait | fait (157 acceptés, 31 corrigés ; 11 fenêtres corrigées) | fait : test statique OK, 24 113 → 33 442 mots | voir journal |
| I42 — Cardiomyopathies | en cours | | | |
| I44 — Troubles de la conduction et bradycardies | en cours | | | |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires | | | | |
| I49 — Extrasystoles et autres arythmies | | | | |
| I46 — Arrêt cardiaque | | | | |
| Q21 — Cardiopathies congénitales de l’adulte | | | | |
| I71 — Anévrismes et dissections artérielles | | | | |
| I80 — Thrombose veineuse profonde et thromboses veineuses | | | | |

Reprise après interruption : les résultats partiels de chaque cours sont dans `<CODE>/`. Un producteur interrompu se relance sur ses seuls fichiers ; ses sorties existantes sont réutilisées si elles sont complètes.
