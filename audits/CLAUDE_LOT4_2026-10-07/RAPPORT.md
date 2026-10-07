# I48 — réception et injection du lot 4

Livraison figée : PR #12, tête `b1f19c3510c1a828650867da033ebe2fbf30142e`, base `a6f18a150b1a67a2a53c14b3a7ec0b7fe6c6c74a`. Les treize fichiers reçus (huit sources, manifeste, trois archives, glossaire) égalent les blobs GitHub. Les huit empreintes de départ du manifeste correspondent aux sources canoniques avant application. `apply-claude` a injecté les huit sources ; les cinq entrées de glossaire ont été reprises séparément. Original de Claude conservé dans son dossier de livraison.

Le complément de branche `5f08102` contient du travail en cours sur d’autres cours. Les huit sources I48, le manifeste et le glossaire y sont identiques à la livraison figée : preuve `LATE_BRANCH_CHECK.json`. Ces productions intermédiaires ne sont pas injectées ni déclarées vérifiées.

## Réconciliation avec la publication concurrente

Pendant l’interruption de l’envoi, une autre session a publié le lot I48 au commit `e856ed1` dans `main` et la branche d’intégration. Ses huit sources canoniques, ses adaptations médicales, ses entrées HUG/DOI au glossaire, son correctif de focus et sa construction atomique sont conservés. Les compléments de cette reprise sont appliqués sur cet arbre publié, sans remettre l’ancienne version en tête. Les contrôles sont relancés sur le résultat réconcilié.

## Résultat et adaptations d’intégration

- I48 — Fibrillation et flutter auriculaires : **66 778 mots, 101 fenêtres natives, quatre quiz, quinze Pareto**. Claude livrait 66 339 mots et 100 fenêtres ; les 505 affirmations, 360 compléments et 133 nouveaux mots verts restent des volumes déclarés par Claude, sans certification indépendante exhaustive.
- Les **onze arbitrages** sont conservés : huit textes continus après neutralisation du balisage et trois textes vérifiés par clauses, avec intercalation de mécanismes ou adaptation de ponctuation. Les onze formulations antérieures exactes sont absentes. Voir `ARBITRAGES.json`.
- Deux fenêtres comparatives ESC 2026 ont été ajoutées, une dans I48 et une dans I50. Elles séparent la nouvelle classification de l’insuffisance cardiaque des seuils spécifiques de l’ESC FA 2024. Le texte sur les antiarythmiques en FEVG 41–49 % a été harmonisé avec la figure 5 de l’ESC FA 2024.
- I50 : 17 069 mots et 68 fenêtres natives ; suppression d’une mention de validation interne et d’une attribution suisse non étayée. Les banques de justifications comptent **204 fenêtres pour 205 cibles explicites dans quinze cours**, distinctes des fenêtres natives.
- Correction du moteur : un mot vert clinique contenant une abréviation ouvrait parfois le glossaire de cette abréviation. Le clic et le clavier préfèrent maintenant le lien clinique englobant. Les entrées isolées du glossaire restent accessibles.

## Vérifications de la version injectée

| Contrôle | Résultat |
|---|---|
| Tests unitaires | 80 réussis |
| Sources I48 / I50 | Contrôle statique réussi |
| Fragments | 22 construits ; audit de périmètre, syntaxe JavaScript et reproductibilité réussi |
| Sciences | Contrats des 31 cours intégrés : aucune erreur |
| I48 et comparaisons I48/I50 | 931 vérifications navigateur, 1360 px et 390 px ; les 101 fenêtres I48 sont ouvertes, y compris les Pareto, retours imbriqués et restitution du focus |
| Justifications | 2 400 vérifications, quinze cours, 204 entrées ; aucune erreur |
| Accueil et navigation S01 | 71 vérifications ; aucune erreur |

Une première tentative globale a trouvé le fichier compilé T1 vide. La reconstruction ciblée T1 puis l’audit et les vérifications ont réussi. Le rapport de cette tentative est conservé sous `initial_attempt_missing_T1.json` ; il ne constitue pas le résultat final. Les nouvelles captures restent locales, hors de la publication GitHub ; les rapports textuels conservent leur portée exacte.

## Contrelecture et limites

Contrelecture ciblée du texte intégral **ESC FA 2024**, notamment figure 5, tableaux des traitements et recommandations de contrôle de fréquence/rythme. Vérification de la publication officielle **ESC 2026** sur l’insuffisance cardiaque : https://www.escardio.org/news/press/press-releases/major-changes-made-to-the-esc-guidelines-on-heart-failure/ . Cette vérification porte sur les comparaisons ajoutées ; elle ne certifie pas l’ensemble du nouveau référentiel ou toutes les affirmations du cours.

Réserves de Claude conservées comme historique : informations professionnelles suisses et guide EHRA non contrôlés intégralement, extrapolation TRAPS. La publication concurrente a harmonisé les formulations après cardioversion et le schéma de digoxine ; ses adaptations documentées sont conservées. La réussite technique ne clôt pas la relecture médicale exhaustive.

Le Fragment 01 reste prioritaire et inachevé. Partage actuel : dix cours présents Codex / dix Claude ; I00 reste à Claude car commencé, I47 passe à Codex. Les quatre productions prioritaires sont partagées deux chacun. Aucun minimum de mots ni multiplicateur de volume n’est imposé. La cartographie complète CIM-11 et les autres entrées prévues restent ouvertes. Anthropic Serif est absente du dépôt et des polices installées ; elle n’a pas été appliquée.
