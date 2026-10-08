> **RÈGLE FONDAMENTALE (section 11)** : aucun cours produit de mémoire — chaque affirmation vient d'une source lue ; **sources suisses puis européennes, aucune recommandation américaine** ; médicaments selon l'information professionnelle suisse Swissmedic (`tools/swissmedic_fi.py`) ; **plan monographique classique**, sans îlot ni tableau consacré au code CIM. Toute invention ou tricherie est interdite.

> **Règle universelle du 8 octobre 2026.** Efficacité plutôt que volume : information efficace, puissante, extrêmement didactique, claire, en termes dédiés. Deux captures réelles par leçon, présentées dans le panneau latéral. Voir `LEADERSHIP_CLAUDE_2026-10-08.md`, sections 7 et 8.

> **Protocole remplacé pour les travaux nouveaux, 8 octobre 2026.** Lire [le protocole par fragment](PROTOCOLE_FRAGMENTS_2026-10-08.md) et [COORDINATION.md](../../COORDINATION.md). Fragment entier achevé et auto-revu avant audit croisé unique ; l’autre IA corrige puis injecte, INJECTÉ immuable, HTML clair. Les dispositions incompatibles ci-dessous sont conservées comme historique et ne donnent plus d’ordre d’action. Aucun chapitre isolé ne constitue une remise finale.

# Consignes communes — interaction, densité et sources cliniques

Consignes reçues de Vial le 8 octobre 2026, applicables à Claude et Codex. Elles complètent le cahier partagé et priment sur les anciennes préférences de rédaction.

## Travail parallèle dans le chapitre actif

Répartir entre plusieurs sous-agents les catégories, panneaux et sujets du même chapitre. Un auteur par fichier réel ; les autres agents relisent. Remettre le chapitre complet avec les sources exactes et les réserves à l’autre IA pour audit. Ne pas ouvrir le chapitre suivant pendant sa production. Une fois le chapitre produit et effectivement remis pour audit, le chapitre suivant peut commencer ; les corrections reçues restent prioritaires. Les 11 fragments Claude et 10 fragments Codex restent attribués entiers ; les catégories restent dans leur fragment. L’audit, l’injection et la publication conservent leurs contrôles et leurs preuves. Pour les chapitres Claude, [REGLES_INJECTION_CLAUDE.md](REGLES_INJECTION_CLAUDE.md) autorise la revue interne et les contrôles avant injection, puis l’audit Codex après injection ; pour les chapitres Codex, la contrelecture Claude reste préalable.

## Interaction et densité

Les précisions de sens doivent être accessibles dans une fenêtre après clic sur le mot concerné. Le tableau 18 ESC 2026 sera cité dans I42 — Cardiomyopathies (C-01-Cardiologie) dans une fenêtre accessible depuis un mot vert ; « C » y désigne l’insuffisance cardiaque chronique des stades B à D. Cette demande reste dans la file de révision I42, sans ouvrir une seconde production. Une décision binaire utile doit être formulée clairement, avec le contexte nécessaire dans la fenêtre. Ne pas exposer les procédures internes des agents dans les cours.

Privilégier les tableaux lorsqu’ils rendent une classification, une comparaison ou une énumération plus lisible. Titres explicites, colonnes stables, cellules courtes et cohérentes ; définir les sigles par interaction et indiquer les unités et conditions. Tester la lisibilité sur ordinateur et mobile. Ne pas convertir systématiquement la prose en tableaux : explications causales et mécanistiques gardent le texte nécessaire. Éliminer répétitions et remplissage ; aucun plafond de mots arbitraire n’a été fixé.

## Arbitrage clinique et accès aux textes

En cas de contentieux, la source primaire applicable la plus récente l’emporte. Rendre la recommandation retenue accessible par un mot vert interactif, avec son périmètre, sa date, son niveau de preuve et ses limites. La fenêtre donne aussi accès au texte actuellement en vigueur lorsqu’il est plus ancien, et précise la relation entre les deux sources. Vérifier la version et l’applicabilité à la population, à l’indication et au contexte suisse ; une date plus récente sans contenu lu ne prouve pas l’applicabilité.

Pour les médicaments, utiliser les monographies suisses en vigueur et les sources primaires pertinentes. Le Compendium proposé par Vial est un point d’accès : https://compendium.ch/product/931-aldomet-cpr-250-mg/mpro. Lire la monographie réellement accessible, confirmer le produit, la date et les conditions ; ne pas importer une dose ou une indication d’un produit hors sujet. Conserver les résultats d’accès et distinguer accès impossible, résumé et texte intégral.

## Relecture et état de validation

Le choix de source est documenté dans le rapport d’audit ; toute réserve non résolue reste visible. Une contrelecture IA ou des tests techniques ne prouvent pas une validation par un médecin. Aucune relecture humaine planifiée ou effectuée n’est annoncée sans preuve. Le propriétaire peut examiner un échantillon court du chapitre ; cela ne vaut pas validation médicale de son ensemble.

La session Claude externe a reçu ces mêmes consignes et les a consignées au commit `c68d96afe6c1`. Son texte original est conservé sous [REGLES_CLAUDE_C68D96A](reviews/2026-10-08/REGLES_CLAUDE_C68D96A/REGLES_VIAL_2026-10-08.md). Son helper Compendium est une piste à lire puis vérifier localement avant utilisation ; sa présence sur sa branche ne prouve pas son installation dans ce checkout.

## Injection autonome de Claude

La règle reçue à `de9af27`, avec la file initiale créée à `66f1bd93a8bef1bb067d0051f2f4c6fcef961311`, prime sur les anciennes mentions d’audit Codex préalable à une injection Claude. Avant injection, Claude termine la revue par sous-agents et vérificateur indépendant, le rapport complet, `check-claude`, et les contrôles prescrits sur la tête actuelle de main : sigles vides, statique, build de tous les fragments, audit des fragments, natifs sans échec, tests unitaires. Aucune réserve bloquante Codex ne peut rester ouverte. Chaque injection Claude entre dans [FILE_AUDIT_CODEX.json](FILE_AUDIT_CODEX.json) au statut `a_auditer` ; Codex traite l’ordre de la file et lie son rapport au statut `audite_favorable` ou `reserves`. Le tableau de bord indique « en audit croisé » jusqu’à un audit favorable. Une nouvelle remise ou archive seule n’ajoute pas d’entrée d’injection. Claude tranche les désaccords non bloquants de ses chapitres ; une erreur médicale démontrée reste à corriger en priorité.
