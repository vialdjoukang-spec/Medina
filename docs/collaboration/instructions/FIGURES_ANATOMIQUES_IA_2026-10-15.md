# Figures anatomiques générées par IA — règle de Vial, 15 octobre 2026

Périmètre : chantier SSP V2 (S08/S05/S04/S06). Les autres systèmes restent inchangés.

## Règle
Les schémas de structures anatomiques (organe, vaisseau, nerf, os, coupe, territoire, histologie, frottis) générés ou dessinés par une IA, y compris un SVG écrit par un modèle de langage, **ne sont pas recevables** : imprécis, ils trahissent la médecine. Une telle figure démontrée constitue un constat **MAJEUR** et doit être remplacée par un **original existant**, sourcé et licencié. Une origine non démontrée reste une réserve, jamais un label « recevable ».

## Classement en audit
| Classe | Définition | Exigence |
|---|---|---|
| `ANATOMIQUE_IA` | structure anatomique dessinée sans source iconographique | MAJEUR ; au plus 3 candidats réels avec page, original, auteur, licence, attribution |
| `SCHEMA_NON_ANATOMIQUE` | algorithme, frise, courbe, chaîne causale | recevable si chaque valeur et chaque flèche est sourcée |
| `IMAGE_SOURCEE` | photographie, imagerie, micrographie, planche réelle | source, licence propre à la figure et attribution vérifiées |

Une icône décorative de très petite taille en forme d'organe n'est pas un schéma d'enseignement : constat MINEUR (remplacement par une icône non anatomique ou suppression).

## Sources admises (ordre)
Wikimedia Commons (planches de Gray, domaine public ; Servier Medical Art, CC BY), figures d'articles en libre accès dont la licence **de la figure** est vérifiée (CC BY, CC BY-SA, CC0), BodyParts3D/Anatomography (CC BY-SA). Licences NC/ND refusées.

## Outils et sobriété
`tools/image_codex_finder.py` (moteur commun : courtier local, cache, budget journalier, délais d'attente partagés) et `tools/image_clo_finder.py` (couche Claude : inventaire hors ligne, candidats filtrés, attribution proposée, état). Un seul courtier par machine ; aucune recherche parallèle indépendante entre machines tant qu'aucun courtier commun n'est hébergé ; aucun nouvel essai en boucle.

## Limites
Le filtre de métadonnées ne prouve ni l'origine humaine, ni la licence, ni l'exactitude anatomique. Aucune image n'est publiée sans contrôle visuel. Une revue par IA n'est pas une validation médicale humaine.
