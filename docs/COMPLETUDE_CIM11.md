# MEDINA — règle de complétude CIM-11

Instruction du propriétaire du 7 octobre 2026. Cette règle prime sur les critères historiques CIM-10-GM des prompts du dépôt.

## Condition d'achèvement

Un système est incomplet dès qu'une catégorie ou sous-catégorie pertinente de la CIM-11 n'a pas d'enseignement spécifique, accessible et relu. La présence d'un titre, d'un code, d'un plan, d'un compteur ou d'un renvoi vers un cours futur ne constitue pas un enseignement livré.

Les cours peuvent partager une source commune entre plusieurs systèmes. Chaque entité reste visible dans chacun des systèmes concernés, sous son code, avec un lien vers le passage qui la traite effectivement. Un regroupement de maladies ne permet pas d'omettre leurs particularités diagnostiques et thérapeutiques. Un renvoi ne devient recevable qu'après vérification du passage cible et de son accès dans le fragment autonome.

## Référentiel à inventorier

La base de travail est la [CIM-11 pour les statistiques de mortalité et de morbidité, version 2026-01, français](https://icd.who.int/browse/2026-01/mms/fr), disponible sur le site de l'OMS et consultée le 7 octobre 2026. Les [versions officielles](https://icd.who.int/browse/releases/mms/en) permettent de suivre les changements. Le navigateur donne accès au tableur et aux tables de correspondance officielles.

L'inventaire conserve chaque code et identifiant d'entité, son intitulé officiel, sa hiérarchie, sa version et ses rattachements pédagogiques. Les catégories, sous-catégories et catégories résiduelles sont contrôlées. Les blocs organisateurs sont conservés dans la hiérarchie ; ils ne sont pas comptés comme des leçons supplémentaires. Les codes de précision sont rattachés à l'enseignement concerné et ne sont pas supprimés silencieusement.

La classification MMS, la Fondation OMS et les systèmes pédagogiques MEDINA ont des fonctions distinctes. Le rattachement au système est documenté ; une affection à manifestations pulmonaires peut aussi appartenir à l'infectiologie, à l'immunologie ou à la génétique. Ces rattachements multiples ne justifient pas son absence de la pneumologie.

## Matrice obligatoire

| Donnée par entité | Preuve attendue |
| --- | --- |
| Référence CIM-11 | Code, identifiant OMS, intitulé, parent, version et URL |
| Système MEDINA | Tous les rattachements pertinents et leur justification |
| Enseignement | Fichier, cours, onglet et repère stable du passage spécifique |
| Couverture | Notions propres à l'entité, sous-catégories et limites du regroupement |
| Accès | Lien ouvert avec succès dans le fragment distribué |
| Relecture | Rapport médical et rédactionnel indépendant, commit effectivement relu |
| État | Absent / plan / rédigé / intégré / relu / contrôlé, sans confusion entre ces états |

Les correspondances CIM-10 → CIM-11 ne sont pas supposées bijectives. Elles sont vérifiées à partir des ressources officielles. Renommer les anciens codes ou ajouter quelques correspondances dans les textes ne constitue pas un inventaire CIM-11 exhaustif.

## Mesure et présentation

La couverture CIM-11 est le nombre d'entités attendues disposant d'un enseignement spécifique accessible et vérifié, rapporté au nombre total d'entités attendues dans l'inventaire officiel versionné du système. Le nombre de cours et le nombre de rubriques pédagogiques sont présentés séparément. Les entités partagées entre systèmes restent dans le dénominateur de chacun des systèmes concernés.

Tant que cet inventaire n'est pas constitué et contrôlé, la couverture CIM-11 porte la mention **non établie**, jamais un pourcentage calculé à partir du catalogue CIM-10. La couverture rédactionnelle, la qualité linguistique, l'exactitude médicale et la réussite technique restent des mesures distinctes. Une valeur de 100 % exige l'absence de catégorie manquante et les relectures et contrôles requis.

Le [relevé du 7 octobre 2026](../audits/COMPLETUDE_2026-10-07/README.md) décrit les lacunes des cinq fragments actuellement livrés. Aucun de ces fragments n'est certifié complet en CIM-11. Les anciennes listes `DONE_SYS` et `DONE_COURSES` expriment des statuts historiques ; elles ne prouvent pas l'achèvement selon cette nouvelle règle ni la validation des révisions récentes.
