# Mission commune — justification systématique de chaque affirmation

Date : 7 octobre 2026. Demande du propriétaire, transmise à Codex et à Claude.

## Exigence

Toute affirmation d'un cours porte son **pourquoi**. Ce pourquoi est le mécanisme physiopathologique précis qui relie un fait à sa conséquence clinique, puis à la décision. Cette règle vaut pour les quatre onglets, les fenêtres, les tableaux, les listes, les quiz et les Pareto de tous les cours.

Le propriétaire a cité deux exemples :
- Un bilan qui écrit « anémie → facteur aggravant » doit expliquer par quel mécanisme l'anémie aggrave la situation.
- Un bilan qui cite le sodium ou le potassium doit justifier clairement pourquoi on les dose et ce que leur valeur change.

La forme préférée est la **fenêtre interactive** : un mot vert cliquable qui ouvre l'explication à l'endroit même de l'affirmation.

Les cellules de tableau laconiques sont proscrites. Une cellule qui énonce un fait doit, soit former une phrase complète qui donne la cause et la conséquence, soit porter un mot vert qui ouvre la fenêtre explicative. Une liste d'examens dit, pour chaque examen, pourquoi il est demandé et quelle valeur change quelle décision.

## Répartition des 30 cours (proposition de Claude, 7 octobre 2026)

La répartition suit le partage à 50 % demandé : 15 cours chacun. Claude garde le cœur de la cardiologie, où il a déjà lu l'ESC 2024 et relu I48, afin de préserver la cohérence des renvois entre cours cardiaques. Codex prend les cours vasculaires et congénitaux de S01 et les quatre autres fragments.

| Claude — 15 cours | Codex — 15 cours |
| --- | --- |
| I48 — Fibrillation et flutter auriculaires | I46 — Arrêt cardiaque |
| I50 — Insuffisance cardiaque | Q21 — Cardiopathies congénitales de l’adulte |
| I21 — Syndromes coronariens aigus et infarctus du myocarde | I71 — Anévrismes et dissections artérielles |
| I25 — Syndromes coronariens chroniques et angor | I80 — Thrombose veineuse profonde et thromboses veineuses |
| I10 — Hypertension artérielle | I70 — Athérosclérose périphérique, artériopathie des membres inférieurs et ischémie aiguë |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | J45 — Asthme |
| I33 — Endocardite infectieuse | J44 — Bronchopneumopathie chronique obstructive |
| I35 — Valvulopathies aortiques | J18 — Pneumonies de l’adulte |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | I26 — Embolie pulmonaire aiguë |
| I00 — Rhumatisme articulaire aigu | D84 — Déficits immunitaires |
| I40 — Myocardites | M32 — Lupus érythémateux systémique |
| I42 — Cardiomyopathies | M31 — Vascularites systémiques |
| I44 — Troubles de la conduction et bradycardies | T78 — Anaphylaxie et allergies |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires | M06 — Polyarthrite rhumatoïde |
| I49 — Extrasystoles et autres arythmies | A41 — Sepsis et choc septique de l’adulte |

Codex peut ajuster ce partage avant de commencer ; la version publiée la plus récente fait foi. Chaque agent remet ses cours selon `DELIVERY_PROTOCOL.md`. Codex injecte ensuite les remises de Claude dans les sources canoniques.

**Ordre d'intégration recommandé.** Le lot 3 de Claude, qui supprime les gabarits clonés des Sciences dans 20 cours dont J18, J44, J45 et I26, est en cours. Il conviendrait de l'injecter avant d'entreprendre les passes de justification sur ces cours, pour éviter des conflits sur les mêmes fichiers.

## Méthode commune

1. **Inventaire.** Relever, fichier par fichier, chaque affirmation sans mécanisme : cellule de tableau, item de liste, phrase isolée, encadré, Pareto, réponse de quiz.
2. **Choix de la forme.**
   - Une explication courte, de deux ou trois phrases, s'écrit dans le texte.
   - Une explication plus longue, ou une notion réutilisée à plusieurs endroits, devient une fenêtre, appelée par un mot vert `<button class="w" data-k="<code>-<clé>">…</button>`.
3. **Contenu d'une fenêtre.** La fenêtre suit l'ordre normal → perturbation → conséquence → décision. Elle se déclare par `<template data-pop="<code>-<clé>" data-title="…">`, avec ses rubriques `<div class="lab">…</div><p>…</p>`, dans un fichier `_pop*.html` existant du cours. Les rubriques usuelles sont « Physiologie normale », « Mécanisme », « Conséquence clinique », « Ce qui change la décision » et « Source ».
4. **Sources.** Un fait, un seuil ou une recommandation nouvellement écrit cite sa source primaire : organisme, année, section ou tableau, DOI. Une physiologie classique cite une référence de manuel ou une revue identifiée. Un mécanisme incertain est présenté comme tel.
5. **Contraintes techniques.**
   - La clé de fenêtre commence par le code du cours en minuscules.
   - Chaque bouton `data-k` doit avoir sa fenêtre.
   - Aucune abréviation n'est introduite sans entrée dans `glossary/`.
   - Les tests (`test_v7.py --static`, `audit_sciences.py`, les deux tests navigateur) doivent rester verts.
6. **Non-régression.** On ne retire aucune notion utile. On ne recopie pas une explication déjà présente ailleurs : on renvoie à la fenêtre existante.

## Exemples de référence

### Anémie dans le bilan d'une fibrillation auriculaire

Le contenu artériel en oxygène vaut environ 1,34 × hémoglobine (g/dL) × saturation + 0,003 × PaO₂ (mmHg), en mL d'oxygène par dL de sang. Quand l'hémoglobine baisse, ce contenu baisse dans la même proportion. L'organisme maintient l'apport d'oxygène en augmentant le débit cardiaque, sous l'effet d'une activation sympathique.

En FA, ce tonus sympathique accélère la conduction du nœud auriculoventriculaire, ce qui élève la fréquence ventriculaire. La diastole raccourcit, ce qui réduit le remplissage du ventricule gauche et la perfusion coronaire, qui a lieu surtout en diastole. Le contrôle de la fréquence devient plus difficile et une ischémie fonctionnelle peut apparaître.

Sous anticoagulant, une anémie est aussi un facteur de risque hémorragique modifiable (ESC 2024). Elle peut révéler un saignement occulte et elle réduit la réserve face à une hémorragie. Le bilan recherche donc sa cause avant de prescrire et pendant le suivi.

### Potassium et magnésium avant un antiarythmique ou une digoxine

Une hypokaliémie ralentit la repolarisation ventriculaire et favorise les post-dépolarisations précoces. Associée à un médicament qui allonge l'intervalle QT (sotalol, amiodarone), elle expose aux torsades de pointes.

Sous digoxine, le potassium entre en compétition avec la digoxine pour la pompe sodium-potassium. Une hypokaliémie augmente donc la fixation de la digoxine et sa toxicité.

Une hypomagnésémie entretient la fuite rénale de potassium et favorise elle aussi les torsades. On corrige donc le potassium et le magnésium avant d'introduire ces médicaments, et on les contrôle sous traitement.

## Remise et suivi

Chaque lot nomme ses cours par leur code et leur intitulé complet. Il donne :
- le nombre d'affirmations justifiées et de fenêtres créées ;
- les sources ;
- les réserves non résolues ;
- les contrôles exécutés.

La passation `HANDOFF_LATEST.md` indique l'avancement de chaque agent, cours par cours.
