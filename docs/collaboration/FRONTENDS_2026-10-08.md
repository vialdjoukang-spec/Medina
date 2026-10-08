# Frontends par spécialité — 8 octobre 2026

## Demande de Vial

Accès visuel aux cours et refonte majeure : un frontend distinct par fragment, contenant uniquement sa spécialité ; accueil clair et agréable ; rectangles de catégories aux intitulés sobres, relief discret. La demande initiale Anthropic Serif est remplacée par l’instruction directe suivante : « Pas de conflit avec Claude. Aligne toi avec la Police qu’il a trouvé ». Cette demande directe de l’utilisateur complète le protocole du PDF, sans transformer une consultation de rédaction en remise pour l’audit final.

## Réalisation

Le portail index présente les 22 spécialités et permet de chercher leur nom. Chaque lien ouvre un HTML autonome propre, avec son accueil, sa navigation, ses catégories et ses cours. Le titre public et l’accent sont spécifiques à la spécialité. Les cours disponibles sont visibles dès l’accueil, sans passer par une interface de production. Le carnet reste local et distinct par fragment.

La surface haute lisibilité de Claude est reprise depuis ses commits `e9b7192ffef7cbb44e53bb05165c244d3d11d796` puis `f92867451d3e46cb160a53379f7196248e4f41a6`, avec son attribution conservée (`c114c4d`, `e05191a`). **Atkinson Hyperlegible Next v2.001** est embarquée en quatre WOFF2 originaux : romain 400, italique 400, romain 600 et romain 700. Les cartes de catégories et de spécialités utilisent ses couleurs distinctes, texte blanc à contraste vérifié d’au moins 4,5:1 et relief discret ; les surfaces de lecture restent claires et le texte principal presque noir. Le rendu est responsive et les animations respectent la préférence de réduction de mouvement.

Les adaptations d’intégration conservent notre navigation strictement locale, y compris les repères de lecture, et les réglages du lecteur. L’exclusion des cours, fenêtres et Navigo de la règle globale forcée permet de choisir réellement une autre famille ; Anthropic Serif reste une option. Les en-têtes et onglets Navigo gardent un contraste élevé. Le moteur garde les quatre onglets, les fenêtres et le mode livre. La famille choisie améliore la distinction des glyphes ; aucun « standard universel de lecture » ou bénéfice clinique non mesuré n’est revendiqué.

Seuls les commits frontend Claude sont repris : les sources médicales en cours dans sa branche restent conservées à leur emplacement, sans intégration implicite de sa réécriture J09.

`fragment_surface.py` centralise le périmètre frontend par spécialité primaire et propriétaire du cours canonique. A43, B18 et A04 rejoignent l’infectiologie dans le frontend ; l’ancien catalogue documentaire demeure conservé. Les variantes d’un cours restent rattachées à leur cours propriétaire. Les glossaires embarqués ne contiennent que les termes des cours présents et leurs dépendances. Les anciens catalogues globaux et plans médicaux génériques sont retirés des fragments. L’inventaire CIM-11 complet n’est pas déclaré établi.

Le script `tools/build_work_preview.py` vérifie les dix empreintes du dossier interne A41, reconstruit un overlay temporaire et publie uniquement un aperçu consultable. La bannière explicite le statut de travail ; les indicateurs de validation et de complétude sont vides/faux ; le carnet est séparé. Les sources médicales canoniques et les statuts d’injection ne sont pas modifiés.

## Liens

- Accueil : https://vialdjoukang-spec.github.io/Medina/
- Infectiologie : https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_T1_agents-therapeutique.html
- Cours A41 en rédaction : https://vialdjoukang-spec.github.io/Medina/apercus/infectiologie.html#/entry/A41

## Vérifications

Les résultats exacts sont consignés dans le reçu FRONTENDS_2026-10-08, le reçu ALIGNEMENT_ATKINSON_2026-10-08 et leurs contrôles associés. Ils portent sur le fonctionnement technique et le périmètre affiché ; ils ne constituent pas une validation médicale finale des cours ou des fragments.

La tête distante 9fa4651 dépose J09 dans l’ancien espace partagé ; elle est conservée lors de l’intégration frontend. Ce dépôt de chapitre n’est pas traité comme un fragment entier prêt pour l’audit unique.

## Publication vérifiée

Le commit frontend `04a67ee5372df53946bbe619b0d6b00f98afe28c` est déployé, workflow Pages `37805755015` réussi. Les 24 pages publiques (portail, 22 spécialités, aperçu) répondent HTTP 200 et embarquent les quatre fichiers Atkinson originaux. Le navigateur contrôle les titres du portail, de l’infectiologie et de la cardiologie, puis le cours A41 en rédaction avec ses quatre onglets et une fenêtre explicative : vraies fontes Atkinson rendues, aucun débordement bureau/mobile ni erreur JavaScript. Preuves `reviews/2026-10-08/ALIGNEMENT_ATKINSON/live-*.json`.
