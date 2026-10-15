# Publication en l’état et assainissement de la tétrade — 15 octobre 2026

Instruction directe de Vial dans cette session : publier les cours existants tels quels, y compris les travaux en cours ; assainir les restrictions et problèmes techniques des quatre systèmes sans modifier les contenus ; établir la parité opérationnelle Codex/Claude et leur veto commun. Six sous-agents distincts travaillent avec le coordinateur.

## Référence et conservation

Référence distante initiale : `bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373`. Les quatre systèmes sont N-05-Neurologie (S08), E-06-Endocrinologie et métabolisme (S05), N-07-Néphrologie (S04) et H-08-Hématologie (S06).

- 98 cours déjà canoniques à cette référence ; leurs 686 fichiers HTML/glossaires sont conservés octet pour octet (`REFERENCE_AVANT.json`, `CONTENUS_PRESERVES.json`).
- Six cours supplémentaires copiés depuis les livraisons présentes dans ce même commit : R25, R26, R27, R47, E59 et D69. Les 50 fichiers ajoutés, images comprises, sont strictement identiques aux sources de livraison.
- Catalogue final de cette opération : 57 cours de neurologie, 26 d’endocrinologie, 6 de néphrologie, 15 d’hématologie, soit 104 cours accessibles. Aucun cours n’est inventé ni réécrit.
- R29, R48 et E60 ne contiennent que des préparations : les documents existants sont référencés comme tels, sans les compter comme cours.
- Les statuts d’audit et registres historiques ne sont pas promus. La publication des six ajouts porte le statut provisoire `en_etat` ; aucun nouvel audit médical ni validation humaine n’est revendiqué.

L’index public `/Medina/audit/` est produit depuis les sources du commit réellement construit. Son fichier `sources.json` et le manifeste `/Medina/publication.json` permettent de retrouver les empreintes et le commit déployé. Le reçu de publication distante est ajouté après vérification effective.

## Corrections techniques

Le chargeur reconnaît le préambule de découverte R27 par une forme AST précise, sans modifier le glossaire ni autoriser une exécution dynamique supplémentaire. Le scanner de collaboration compare désormais les livraisons à `main`, au lieu de la branche d’intégration historique du 7 octobre. La garde distingue une publication en l’état, liée aux vrais blobs de provenance, des anciennes transitions administratives et sait rejouer les envois comprenant plusieurs étapes. Les veto symétriques sont vérifiés par la garde et avant le déploiement Pages.

## Branches et historique

`BRANCHES.json` conserve les 79 têtes distantes examinées : 54 ancêtres de main, 2 têtes alignées, 23 divergentes. Quatorze simulations de fusion de branches anciennes rencontrent des conflits. Cinq branches divergentes ne portent plus de patch distinct de main. Les inventaires par système rapprochent toutes les variantes de sources : tous les cours rédigés repérés dans ces quatre systèmes sont pris en compte dans les 104 ci-dessus.

Les variantes historiques et leurs branches restent conservées. Aucune suppression, fusion forcée, réécriture d’historique ou restauration d’ancienne version médicale n’est faite. Les anciens conflits de fusion restent explicitement inventoriés ; ils ne sont pas présentés comme résolus dans toutes les branches. Le scanner complémentaire `LIVRAISONS_REPEREES.md` porte sa réserve d’accès API ; l’inventaire Git des 79 têtes est conservé séparément.

## Parité et droits effectifs

La nouvelle instruction de projet s’applique symétriquement à Codex et Claude. Leur journal de veto est commun et traçable ; un acteur ne lève pas le veto de l’autre. Les anciens STOP, leadership exclusif et ordres de cycle incompatibles ne bloquent pas cette publication en l’état.

La connexion GitHub actuelle rapporte `admin=true` pour le dépôt. Cela ne prouve pas les droits d’une session ou application Claude indépendante. L’API de protection de main renvoie HTTP 403 « Resource not accessible by integration » ; l’inspection d’installation demande une autre authentification (HTTP 401). Aucun rôle administrateur d’application, droit GitHub ni veto distant absolu n’est donc prétendu octroyé par un fichier de politique. La politique locale n’altère pas les règles supérieures des plateformes.

## Contrôles

Les résultats détaillés sont dans les rapports par système et le rapport infrastructure. Le contrôle central a réussi les six nouveaux cours (`test_v7.py --static`) et les comparaisons de conservation des 686 anciens fichiers et 50 copies nouvelles. Les résultats navigateur, tests Python, construction et déploiement sont consignés avec leur périmètre exact ; un succès technique n’est pas un audit médical.
