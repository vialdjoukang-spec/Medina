# Frontends par spécialité — 8 octobre 2026

## Demande de Vial

Accès visuel aux cours et refonte majeure : un frontend distinct par fragment, contenant uniquement sa spécialité ; accueil clair et agréable ; rectangles de catégories aux intitulés sobres, relief discret ; police Anthropic Serif. Cette demande directe de l’utilisateur complète le protocole du PDF, sans transformer une consultation de rédaction en remise pour l’audit final.

## Réalisation

Le portail index présente les 22 spécialités et permet de chercher leur nom. Chaque lien ouvre un HTML autonome propre, avec son accueil, sa navigation, ses catégories et ses cours. Le titre public et l’accent sont spécifiques à la spécialité. Les cours disponibles sont visibles dès l’accueil, sans passer par une interface de production. Le carnet reste local et distinct par fragment.

Les cartes utilisent du blanc et de l’ivoire, un titre sérif régulier et une ombre à plusieurs niveaux discrète. Le rendu est responsive et les animations respectent la préférence de réduction de mouvement. La véritable Anthropic Serif romaine et italique est embarquée en WOFF2 ; les fichiers d’origine, copyright et provenance sont conservés dans assets/fonts/PROVENANCE.json. Les glyphes absents, notamment grecs, utilisent une famille sérif de secours. Le moteur garde les quatre onglets, les fenêtres, le mode livre et les réglages de lecture.

`fragment_surface.py` centralise le périmètre frontend par spécialité primaire et propriétaire du cours canonique. A43, B18 et A04 rejoignent l’infectiologie dans le frontend ; l’ancien catalogue documentaire demeure conservé. Les variantes d’un cours restent rattachées à leur cours propriétaire. Les glossaires embarqués ne contiennent que les termes des cours présents et leurs dépendances. Les anciens catalogues globaux et plans médicaux génériques sont retirés des fragments. L’inventaire CIM-11 complet n’est pas déclaré établi.

Le script `tools/build_work_preview.py` vérifie les dix empreintes du dossier interne A41, reconstruit un overlay temporaire et publie uniquement un aperçu consultable. La bannière explicite le statut de travail ; les indicateurs de validation et de complétude sont vides/faux ; le carnet est séparé. Les sources médicales canoniques et les statuts d’injection ne sont pas modifiés.

## Liens

- Accueil : https://vialdjoukang-spec.github.io/Medina/
- Infectiologie : https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_T1_agents-therapeutique.html
- Cours A41 en rédaction : https://vialdjoukang-spec.github.io/Medina/apercus/infectiologie.html#/entry/A41

## Vérifications

Les résultats exacts sont consignés dans le reçu FRONTENDS_2026-10-08 et ses contrôles associés. Ils portent sur le fonctionnement technique et le périmètre affiché ; ils ne constituent pas une validation médicale finale des cours ou des fragments.

La tête distante 9fa4651 dépose J09 dans l’ancien espace partagé ; elle est conservée lors de l’intégration frontend. Ce dépôt de chapitre n’est pas traité comme un fragment entier prêt pour l’audit unique.
