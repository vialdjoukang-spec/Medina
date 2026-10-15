# Règle Vial (15.10.2026) — figures anatomiques générées par IA : NON RECEVABLES

Les schémas de structures anatomiques dessinés par une IA (SVG ou images produits pour MEDINA, sans source iconographique) sont **non recevables** : imprécis et indignes d'un cours de médecine.

## Ce que l'audit médical doit faire (ajout obligatoire)
1. Inventorier **toutes** les figures des 7 fichiers (`<svg>`, `<img>`, `<figure>`, canvas, dessins CSS) : id/ancre, fichier, légende, ce qu'elle représente, source déclarée.
2. Classer chacune :
   - `ANATOMIQUE_IA` — représente une structure anatomique (organe, vaisseau, nerf, os, coupe, territoire, histologie) sans source iconographique réelle → constat **MAJEUR** « figure anatomique générée, non recevable », proposition = **remplacement** par une image réelle sourcée.
   - Précision (revue PR #141) : `ANATOMIQUE_IA` exige une preuve positive d'origine IA (SVG créé par un agent IA dans l'historique du dépôt, marqueur de génération, déclaration) ; sans preuve, classer `ORIGINE_INCONNUE` = réserve, jamais recevable ni MAJEUR présumé.
   - `SCHEMA_NON_ANATOMIQUE` — algorithme, arbre décisionnel, frise, courbe de données, tableau graphique → recevable sous réserve d'exactitude : vérifier chaque valeur et chaque flèche contre la source.
   - `IMAGE_SOURCEE` — image réelle avec source et licence → vérifier source, licence, attribution.
3. Pour chaque `ANATOMIQUE_IA`, proposer au plus 3 candidats réels, avec URL de la page, URL du fichier, auteur, licence, texte d'attribution. Sources dans l'ordre : Wikimedia Commons (dont planches de Gray, domaine public, et Servier Medical Art, CC BY 4.0), BodyParts3D/Anatomography (CC BY-SA), figures PMC en libre accès (CC BY), Open-i (NLM), en vérifiant la licence de chaque figure.
   - Courtoisie réseau : **au plus 1 requête par seconde et par site**, uniquement les API officielles (Commons : `https://commons.wikimedia.org/w/api.php`), en-tête User-Agent `MEDINA-ImageCloFinder/0.1 (https://github.com/vialdjoukang-spec/Medina)`, aucun téléchargement massif, métadonnées seulement.
   - Ne jamais générer, dessiner ou redessiner une image.
4. Ajouter dans `rapport.json` une clé `figures` : `[{ancre, fichier, classe, description, constat_id, candidats: [{page, fichier_url, auteur, licence, attribution}]}]`, et une section « Figures » dans `rapport.md`.
