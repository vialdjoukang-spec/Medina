# B24 — Infection par le VIH de l’adulte (I-03-Infectiologie) — Sciences

Production interne du 8 octobre 2026. Auteur unique des deux fichiers attribués ; aucun autre fichier du dépôt, source canonique, état de fragment ou élément Git modifié.

## Production

`B24_c.html` contient exclusivement le panneau `pS`, fermé et initialement masqué. Six sous-panneaux suivent l’architecture `sci-bar` / `sci` du cours A41 ; leurs identifiants sont préfixés `b24-`. Le fragment ne ferme pas la coque du chapitre ni un template externe.

`B24_pop_sciences_revision.html` contient 19 templates autonomes correspondant exactement aux 19 clés interactives introduites. Deux schémas SVG possèdent un titre et une description accessibles ; deux quiz comportent chacun une bonne réponse et un retour explicatif. La fenêtre Pareto clôt les Sciences.

Les thèmes demandés sont présents : anatomie digestive, histologie folliculaire, physiologie normale des CD4, cycle viral, latence/clonalité, perte des CD4 et activation, IRIS et diagnostic différentiel, barrières et tests de résistance. Chaque mécanisme rejoint une question clinique. Le cas de M. L., 34 ans, conserve tous les éléments fournis, sans symptômes supplémentaires.

## Sources et limites

Le registre `sources_lues.json` contient 18 entrées finales datées, dont une correction bibliographique. Les études mécanistiques originales forment le socle ; une revue est identifiée comme telle. Les fiches officielles sont réservées aux intervalles de laboratoire et aux principes diagnostiques. Les degrés d’accès sont distingués : passages de texte intégral, résumé primaire, communication courte et recommandation officielle.

Les métadonnées décrivent la version réellement affichée, même ancienne ; aucune version2026 ou base de résistance nouvelle n’est inventée. Les données des États-Unis ne décrivent pas l’offre suisse. La distinction VIH-1/VIH-2 figure dans le cours et une fenêtre dédiée. Les sources indisponibles ne sont pas utilisées comme preuves intégrales. Aucun extrait verbatim n’est repris. Les volumes attribués dans les deux HTML et les courts périmètres/limites du registre restent inférieurs à200 mots par source.

## Vérifications effectivement exécutées

Commande : `python3 /workspace/work/infectiologie-reprise-20261008/b24-sciences/validate_sciences.py`. Résultat PASS, détails dans `checks.json`.

- Balises équilibrées et racine unique `div.panel#pS[hidden]`.
- Six boutons de sous-navigation pointent vers six panneaux existants ; un seul sous-panneau visible initialement.
- Aucun panneau `pA`, `pE`, `pP`, wrapper de chapitre ni template dans le fichier c.
- Aucun identifiant ni template dupliqué ; chaque clé interactive possède sa fenêtre.
- Préfixe b24 vérifié, titres/descriptions des deux SVG présents ; deux quiz valides.

L’intégration au constructeur et le contrôle de navigation dans le navigateur relèvent du coordinateur et de l’agent aperçu. Aucun résultat navigateur n’est revendiqué ici. Cette production interne et ces contrôles techniques ne constituent ni audit croisé final, ni validation médicale humaine, ni clôture du fragment.

## Agrégation des sources communes — mise à jour avant gel

Les normes chiffrées et la préanalytique de laboratoire restent dans les Examens. Les Sciences conservent la physiologie normale des CD4, les données imposées du cas et un renvoi explicite vers les références de mesure. Leur part ZetLab est de 0 mot scientifique.

La part Sciences de NIH Drug-Resistance Testing est réduite à 43 mots HTML et 13 mots de périmètre/limites au registre, soit 56. Le mécanisme expérimental des résistances et de la sensibilité reste appuyé par Mesplède. Les paramètres de présentation des URL sont normalisés pour le contrôle commun.

L’auteur Examens annonce un budget prudent inférieur ou égal à 130 mots pour cette même page. Pharmacologie cite également cette URL : l’agrégation des trois contributions a été signalée au coordinateur avant gel. Aucun budget global du chapitre assemblé n’est annoncé ici.

Le contrôle statique a été relancé après ces changements : PASS ; 19 fenêtres, six sous-panneaux, deux SVG et deux quiz conservés. Le registre final compte 18 entrées utilisées et conserve séparément la trace de la source de laboratoire retirée.

## Empreintes finales

- `B24_c.html` : 26612 octets, SHA256 `7c68301dd36ee1f8d5325ef96799c51798c1d64646a01ab1dc34c22debaeed13`.
- `B24_pop_sciences_revision.html` : 14826 octets, SHA256 `e881e8b2d62b77c3c7ba8413e70b390d03d3f9d0438cca5648034f8c6865d989`.
