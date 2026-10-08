# B24 — Pharmacologie adulte, production du 8 octobre 2026

Deux fichiers rédigés uniquement dans la copie de production : `B24_d.html` et `B24_pop_pa.html`. Aucun autre fichier du dépôt, aucune commande Git, aucune source canonique et aucun état d’audit médical externe modifiés.

Le panneau `pP` comporte six îlots : mécanismes, choix initial, doses et fonction rénale, interactions et VHB, prophylaxies primaires, réévaluation et situations particulières. Quatorze fenêtres couvrent les médicaments, les mécanismes, le démarrage du cas et le Pareto. Deux quiz ont une seule réponse correcte et un retour initialement masqué. Le fichier `d` ferme le panneau, `.chap` et le template ouverts dans `a`.

## Décisions documentaires

| Point | État et décision |
|---|---|
| BIC/TAF/FTC et DTG avec deux INTI | Confirmé dans NIH du 24 septembre 2026 et tableau initial de la publication EACS 13. |
| DTG/3TC, CD4 86, ARN 180 000 | Le CD4 bas n’est pas présenté comme une contre-indication universelle. Dans ce dossier, génotype et VHB inconnus excluent le démarrage rapide par DTG/3TC. Aucun résultat n’est inventé. |
| Évolution du plafond ARN | NIH septembre 2026 retire le plafond initial sous conditions de sensibilité 3TC/VHB. EACS 13, tableau des auteurs publié en ligne le 15 octobre 2025, conserve <500 000. Dates et portée sont distinguées. |
| Biktarvy | FI primaire française AIPS lue, Swissmedic 66834, juillet 2026. Dose, restrictions rénales, cations et rifampicine vérifiés. |
| Dovato | FI primaire allemande AIPS lue, Swissmedic 67313, août 2025. Clairance <30 non recommandée ; surveillance à 30–49. Supplément DTG en cas de rifampicine, pas deux Dovato. Co-trimoxazole à fortes doses de traitement PJP contre-indiqué, sans assimiler toute prophylaxie à ce traitement. |
| Tivicay | Texte professionnel suisse indexé Compendium réellement lu : août 2025, Swissmedic 63052/67861. Pelliculé adulte 50 mg/j sans résistance ; formes dispersibles non équivalentes. Rein, rifampicine, calcium/fer et metformine lus. Accès direct AIPS indisponible. |
| TDF/FTC Mepha | FI primaire française AIPS 66181, août 2024, version interne 13.1. FTC 200 + disoproxil 245 mg ; prise avec repas ; clairance 30–49 toutes 48 h, restriction <30/dialyse. Sa FI décrit l’association initiale avec INNTI/IP ; la recommandation internationale avec DTG n’est pas assimilée à une indication explicite de cette FI. |
| Darunavir et TAF/FTC | Doses NIH effectivement lues et étiquetées américaines. FI suisses actuelles intégrales Prezista/Symtuza/Descovy non vérifiées : aucune autorisation suisse de régime non lu affirmée. |
| VHB | Couverture continue TAF/TDF + FTC/3TC dans un ART suppressif ; alternatives et risque d’arrêt vérifiés dans NIH du 24 septembre 2026. |
| PJP | Prophylaxie primaire indiquée à CD4 86. NIH DS quotidien préféré ; FI Bactrim forte 48306, mars 2023, un forte trois fois/semaine. La différence est explicite. |
| Toxoplasmose | Prévention primaire conditionnée aux IgG positives, inconnues dans le cas. DS quotidien NIH couvre les deux indications. |
| MAC | Pas de prévention primaire à CD4 86. Le seuil <50 et l’efficacité de l’ART sont les conditions pertinentes. Aucune dose empirique MAC n’est proposée dans ce cas. |

## Sources et limites

`sources_lues.json` trace 26 ressources effectivement consultées, leur URL, date/version propre, langue, sections lues et limites. Il conserve quatre accès ou états non vérifiés séparément : FI suisses Prezista/Symtuza, FI Descovy, comprimé oral suisse TMP/SMX 80/400 actuel, interface interactive EACS complète. La page EACS confirme la version 13 ; son tableau initial est attribué à la publication officielle des auteurs réellement lue, pas à une interface inaccessible.

Les sources NIH n’ont pas toutes la même date : résistance 12 septembre 2024 ; initiation 25 septembre 2025 ; choix initial 24 septembre 2026 ; périnatal 31 mars 2026. Les fenêtres conservent ces dates. Les vues rénale et interactions IP sans date précise accessible sont signalées comme telles, sans date de révision inventée.

Le texte français est une synthèse originale, sans citation textuelle brute. Les blocs factuels sont attribués par `data-source` pour limiter la dérivation de chaque ressource ; le contrôle enregistre moins de 200 mots par source dans ces blocs. La synthèse pédagogique et les quiz ont été relus avec leurs sources déjà attribuées ; ils ne fournissent ni doses nouvelles ni résultats supposés. Cette allocation est locale au panneau pharmacologique : vérifier les doublons de source avec les autres panneaux lors de l’assemblage final.

## Contrôle interne

Validation locale par `HTMLParser` : aucune fermeture incorrecte ou balise restante dans les deux fichiers, raccord `a+b+c+d` équilibré, quatorze identifiants de fenêtres uniques, aucune référence interactive manquante, six ancres de navigation présentes, deux quiz avec une seule bonne réponse et feedback `hidden`. Le détail et les empreintes sont dans `verification_structure.json`.

Ce contrôle vérifie la structure et la cohérence documentaire locale. Il ne constitue ni audit médical externe, ni validation d’une prescription réelle, ni vérification visuelle de l’application complète. Le contrôle visuel et la revue de l’ensemble du fragment appartiennent à l’assemblage par l’agent principal.

## Ajustement final des allocations partagées

Drug-Resistance Testing ne fournit plus que 27 mots au panneau pharmacologique, contre 105 auparavant. Un renvoi aux Examens retire les répétitions méthodologiques ; les conditions importantes restent dans le fragment. Deux ressources primaires supplémentaires ont réellement été lues : Co-Receptor Tropism Assays (25 octobre 2018) et Virologic Failure (12 septembre 2024). Le registre indique les emplacements et comptes, sans reprendre les résumés cliniques de ces trois ressources.

Allocation groupée par URL normalisée (paramètre view et fragments neutralisés) : Drug-Resistance Testing 27 + Sciences 56 + réserve Examens 110 = 193 mots ; Virologic Failure 6 + compte conservateur Examens 191 = 197 mots ; Co-Receptor Tropism Assays 10 mots, aucun autre usage détecté. Le registre porte ces comptes et leur provenance. Aucune nouvelle dose ni autorisation suisse ajoutée.

Contrôle final : 14 fenêtres et 2 quiz toujours conformes, raccords des deux fichiers équilibrés, toutes les références interactives présentes. Empreintes actualisées dans verification_structure.json. Les deux fichiers sont gelés après ce contrôle.
