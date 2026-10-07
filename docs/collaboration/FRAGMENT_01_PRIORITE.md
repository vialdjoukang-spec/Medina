# Fragment 01 — priorité et partage actuels

Consigne de Vial du 7 octobre 2026 : achever **C-01-Cardiologie**, puis avancer à **P-02-Pneumologie**. Ce partage remplace le partage historique 15/15, qui portait sur trente cours répartis dans plusieurs fragments. La priorité actuelle porte sur les vingt cours présents en cardiologie, encore ouverts à la relecture exhaustive.

| Responsable | Cours existants à achever |
|---|---|
| Codex — 10 | I50 — Insuffisance cardiaque ; I21 — Syndromes coronariens aigus et infarctus du myocarde ; I25 — Syndromes coronariens chroniques et angor ; I10 — Hypertension artérielle ; I70 — Athérosclérose périphérique, artériopathie des membres inférieurs et ischémie aiguë ; I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires ; I49 — Extrasystoles et autres arythmies ; I46 — Arrêt cardiaque ; I71 — Anévrismes et dissections artérielles ; I80 — Thrombose veineuse profonde et thromboses veineuses. |
| Claude — 10 | I48 — Fibrillation et flutter auriculaires ; I30 — Péricardites, épanchement péricardique, tamponnade et constriction ; I33 — Endocardite infectieuse ; I35 — Valvulopathies aortiques ; I34 — Valvulopathies mitrales, tricuspides et pulmonaires ; I40 — Myocardites ; I42 — Cardiomyopathies ; I44 — Troubles de la conduction et bradycardies ; I00 — Rhumatisme articulaire aigu ; Q21 — Cardiopathies congénitales de l’adulte. |

I00 reste à Claude, dont le travail est déjà commencé selon son avancement à `5f08102`. I47 passe à Codex pour conserver le partage 10/10. Les résultats intermédiaires sur sa branche restent du travail en cours ; ils ne sont pas injectés comme une livraison validée.

Les quatre productions manquantes de la liste prioritaire sont partagées également : Codex prend **I73 — Autres maladies vasculaires périphériques** et **I95 — Hypotension** ; Claude prend **I83 — Varices des membres inférieurs** et **I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques**. Les autres entrées prévues du catalogue ne sont pas effacées : leur regroupement et leur périmètre doivent être explicités avant de déclarer le fragment complet. Le rattachement actuel d’A43 — Nocardiose à la cardiologie reste à corriger. La cartographie complète CIM-11 reste ouverte.

## Fenêtres et volume

Les consignes déjà données par Vial permettent de poursuivre la rédaction : justifier chaque affirmation par une explication causale ou clinique claire, de préférence dans une fenêtre ouverte par le mot concerné. Une fenêtre commence par une réponse directe, puis développe le mécanisme, la conséquence clinique, les limites et les sources. Elle distingue une association d’une causalité et une recommandation d’un résultat d’essai.

Le lot I48 est conservé pour son contrôle et son intégration. Son passage de 25 712 à 66 339 mots ne devient pas une cible pour les autres cours. Aucun multiplicateur ni minimum de mots n’est imposé. Préserver les notions utiles, réduire les répétitions entre texte et fenêtres, répartir les longues explications par sous-titres ; conserver une réponse initiale courte. Une donnée indispensable à la décision reste explicite dans le texte principal.

Présenter les changements **ESC 2026** entre parenthèses ou dans une fenêtre comparative avec le référentiel antérieur. Distinguer la nouvelle définition de l’insuffisance cardiaque des seuils propres à l’ESC FA 2024. Les premières fenêtres comparatives sont dans I50 — Insuffisance cardiaque et I48 — Fibrillation et flutter auriculaires. Une comparaison vérifiée de classification ne valide pas toutes les nouvelles posologies.

**Anthropic Serif** n’est présente ni dans le dépôt ni dans les polices installées de cette session. Ne pas prétendre l’avoir appliquée ni remplacer son nom par une autre police. Cette préférence est enregistrée pour son application lorsqu’un fichier de police utilisable sera disponible.

## Reprise et remise

Reprendre les sources canoniques à la tête de `codex/sciences-cs-fragments-20261007`, en lisant la passation et les reçus. Le lot I48 a été publié dans `main` et la branche d’intégration au commit `e856ed1` pendant cette reprise ; les compléments de comparaison et de partage sont remis ensuite sur la branche d’intégration. Ne pas écraser la livraison I48 ni les fenêtres comparatives avec une ancienne copie. Les réserves héritées restent ouvertes jusqu’à leur contrôle primaire, notamment les informations professionnelles suisses.

Remettre les sources et les glossaires selon `DELIVERY_PROTOCOL.md`. Les rapports de contrôles doivent porter sur la version exacte remise. Codex injecte dans `chapters/<CODE>/`, reconstruit, contrôle le navigateur et publie un reçu. Chaque cours ne sera clos qu’après la vérification intégrale des quatre onglets et de leurs contenus associés ; le nombre de fenêtres et la réussite technique ne suffisent pas.
