# MEDINA — reprise du 7 octobre 2026

La reprise conserve la version précédente et corrige des réserves documentées dans **I50 — Insuffisance cardiaque**, **J44 — Bronchopneumopathie chronique obstructive** et **J18 — Pneumonies de l'adulte**. Les modifications sont appliquées aux sources canoniques, puis reconstruites.

| Domaine | Résultat vérifié |
|---|---|
| Justifications | 7 fenêtres supplémentaires ; total **204 fenêtres / 205 cibles** dans les quinze cours Codex. Les cibles sont explicites et compilables. |
| I50 | BNP, bilan Na/K, hémodilution, hyponatrémie, digoxine, paramètres échographiques et conditions rénales harmonisés entre cours, quiz, fenêtres et Pareto. |
| J44 | Trois causalités de figures corrigées ; localisation des lymphatiques précisée ; trois fenêtres ajoutées. |
| J18 | Aspiration et territoires déclives cohérents ; shunt vrai distinct du rapport ventilation/perfusion bas ; limite du calcul sous oxygène explicitée ; une fenêtre ajoutée. |
| Corpus | **31 cours intégrés**, **22 fragments**, catalogue historique de **1 636 catégories** dans **265 blocs**. Aucun nouveau système n'est déclaré achevé. |
| Livraison Claude | 12 checkpoints du lot 4 I48 reçus et archivés byte-for-byte depuis `7651825416cc1326a85a28db81ced54a9ee6f617`. Aucune proposition non vérifiée n'est injectée. |

## Contrôles du contenu actuel

- Compilation et contrat statique des trois cours : réussis.
- Tests unitaires du compilateur : **25 réussis**.
- [Contrôle navigateur final des fenêtres](browser-final/targeted_justifications_results.json) : **1 057 vérifications**, aucune erreur JavaScript. Les 58 entrées des trois banques sont ouvertes sur ordinateur ; les 24 I50 le sont aussi sur mobile. Les références, le clavier, le focus, les retours imbriqués et J40 sont contrôlés.
- [Contrôle navigateur des figures](figures/figure-browser-results.json) : **191 vérifications**, aucune erreur JavaScript. Sept figures, zoom natif à 200 % pour les six figures Sciences, Escape, retour du focus et mobile 390 px à police 24 px. Six captures inspectées localement et [revue visuelle](figures/visual-review.json). Leur envoi GitHub attend une autorisation explicite après rejet automatique.
- Reconstruction et audit reproductible des **22 fragments** : réussis ; JavaScript valide.
- [Audit Sciences](SCIENCES.json) : **31 cours**, 145 disciplines et 150 figures, aucune erreur de contrat.
- Contrelectures ciblées : [I50](I50_COUNTER_REVIEW.md), [J44](J44.md), [J18](J18.md). Les sources effectivement accessibles et leurs limites sont indiquées.

Les fichiers sous `browser/` enregistrent une passe antérieure de cette reprise ; seul `browser-final/` est la preuve des sources finales. Les références sont ouvertes sous observation lors des tests, sans téléchargement des pages distantes. Les audits de contrat et de navigateur ne certifient pas l'exhaustivité médicale.

## Réception et publication

L'arbre de la version récupérée a été vérifié identique au commit GitHub **`a6f18a150b1a67a2a53c14b3a7ec0b7fe6c6c74a`**, puis publié sur les branches Codex d'intégration. Les historiques des lots Claude précédents sont conservés comme parents.

La promotion vers `main` a été **rejetée par la revue automatique** : elle considère le commit médical substantiel, la relecture exhaustive encore ouverte et l'autorisation de cette promotion insuffisamment explicite dans le transcript. Aucune promotion indirecte ni fusion contournant ce blocage n'est effectuée. La demande d'intégration finale rend les changements concrets et contrôlables avant la confirmation du propriétaire. Le site Pages, construit depuis `main`, ne reçoit donc pas encore ces modifications.

## Réserves restantes

- La justification exhaustive de toutes les affirmations des trente cours initiaux demeure ouverte. Les statuts ne sont pas modifiés en « validé » sur la seule présence de fenêtres.
- La couverture complète CIM-11 reste à établir ; le catalogue conservé est CIM-10-GM 2024.
- Le lot 4 I48 contient des propositions de travail non vérifiées. Ses incohérences d'ancres, d'identification des fenêtres et de couverture sont décrites dans [CLAUDE_DELTA.md](CLAUDE_DELTA.md).
- La réserve microbiologique J18 demeure ouverte. Le référentiel GOLD 2026 a été identifié, mais son PDF n'a pas été lu intégralement.
- Les captures locales ne sont pas incluses dans la publication de cette reprise : leur transfert GitHub a été rejeté par la revue automatique, qui les juge potentiellement sensibles et leur destination insuffisamment autorisée. Les sources et rapports textuels sont remis séparément.
- La figure Pathologie J18 ne possède pas de zoom natif. Les six figures Sciences disposent de ce zoom. Certains labels I50 restent petits en lecture mobile intégrée ; leur ouverture en grand fonctionne.
- La PR #6 accueil/QCM reste une contribution distincte.
