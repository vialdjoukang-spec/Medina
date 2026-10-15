# H-08-Hématologie — réception en l’état, 15 octobre 2026

Base inspectée : `bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373`. Instantané des **79 branches distantes origin**, toutes examinées avec les chemins Unicode réels (`git ls-tree -z`). Les treize références PR historiques locales ont également été inspectées ; elles ne contiennent aucun HTML H08. La demande actuelle de Vial autorise la publication des cours existants, y compris en fabrication. Aucun texte médical n’est réécrit et aucun audit médical n’est inventé.

## Résultat de l’inventaire

Le catalogue propriétaire S06/H-08-Hématologie contient **44 catégories**. Toutes branches confondues, **15 cours** possèdent des sources HTML ; **14 sont canoniques et figurent déjà dans le manifeste public**. D69 est le seul cours HTML disponible qui manque aux sources canoniques de cette base. Les 29 autres catégories n’ont aucun cours HTML retrouvé dans cet instantané ; leur simple présence au catalogue ne constitue pas une rédaction.

Le manifeste public lu à `https://vialdjoukang-spec.github.io/Medina/publication.json` annonce le commit `fab6d25376247328b7d050702aae768098b10b86`, construit le 15 octobre 2026 à 14:21:35 UTC. Les empreintes des sept sources de chacun des 14 cours canoniques correspondent au manifeste. Cette constatation porte sur le manifeste servi ; le déploiement suivant relève du coordinateur.

| Code | Intitulé | Canonique et présent au manifeste public | Versions distinctes |
| --- | --- | --- | --- |
| C77 | Tumeur maligne des ganglions lymphatiques, secondaire et non précisée | Oui | 1 |
| C85 | Lymphome non hodgkinien, de types autres et non précisés | Oui | 1 |
| C86 | Autres lymphomes à cellules T/NK spécifiés | Oui | 1 |
| C93 | Leucémie monocytaire | Oui | 1 |
| C94 | Autres leucémies à cellules précisées | Oui | 1 |
| C95 | Leucémie à cellules non précisées | Oui | 1 |
| C96 | Tumeurs malignes des tissus lymphoïde, hématopoïétique et apparentés, autres et non précisées | Oui | 1 |
| D50 | Anémie par carence en fer | Oui | 8 |
| D63 | Anémie au cours de maladies chroniques classées ailleurs | Oui | 1 |
| D64 | Autres anémies | Oui | 2 |
| D69 | Purpura et autres affections hémorragiques | Non — candidat à réception | 1 |
| D71 | Anomalies fonctionnelles des granulocytes neutrophiles | Oui | 1 |
| D73 | Maladies de la rate | Oui | 1 |
| D74 | Méthémoglobinémie | Oui | 1 |
| D77 | Autres maladies du sang et des organes hématopoïétiques au cours de maladies classées ailleurs | Oui | 1 |

Les **23 versions distinctes** sont entièrement décrites avec leurs chemins, commits de branche, empreintes Git et SHA-256 dans `inventaire-branches.json`. D50 possède huit versions et D64 deux. Les anciens brouillons D50 présents dans les livraisons diffèrent du canonique public actuel ; ils restent conservés et ne doivent pas le remplacer. Le brouillon D64 de main est identique au canonique actuel. Aucune autre version H08 plus récente à recevoir n’a été identifiée ; D69 possède une seule version de ses sept sources dans les branches inspectées.

## Réception D69 préparée

Source : `livraisons/Livraison Claude/H-08-Hématologie/travail/CYCLE_03_D69/` sur la base indiquée. Le registre Claude portait déjà D69 `PRET_A_INJECTER`, avec un contrôle technique daté du 15 octobre 2026 ; ce statut historique n’est pas présenté comme un audit médical.

Le commit `ff418791baedbb00e416711e23cecc96c74d387a` contient uniquement la copie exacte de six HTML dans `chapters/D69/`, du glossaire dans `glossary/d69.py` et des huit fichiers d’images/attributions dans `assets/img/cycle3/d69/`. **Les 15 fichiers sont byte-identiques aux sources de livraison.** Les documents d’auteur, preuves et archives restent inchangés. Les empreintes et égalités sont consignées dans `copie-d69-identique.json`.

`chapters.json` est modifié seulement dans ce worktree pour permettre les contrôles locaux ; il est volontairement exclu du commit de copie. Le coordinateur centralise la ligne du catalogue avec les autres spécialités et les règles de réception en l’état. Aucun registre Claude et aucune garde globale ne sont modifiés ici.

## Vérification technique

Les contrôles statiques passent pour les 14 canoniques et pour D69 : abréviations couvertes, fenêtres référencées, préfixes, classes autorisées et absence de styles en ligne. `controle-statique.json` consigne les commandes réellement exécutées et leurs résultats.

La construction S06 avec les 15 cours réussit : 642 gabarits, sortie autonome de 3 696 389 octets. `build-s06.log` conserve la sortie. Le catalogue local temporaire est utilisé pour ce contrôle ; le HTML construit n’est pas ajouté au dépôt.

**Le contrôle navigateur final passe sur les 30 surfaces** (15 cours × 1440 px et 390 px), avec **3 248 ouvertures de mots interactifs**, les quatre onglets de chaque cours, aucune fenêtre manquante, aucune erreur JavaScript, aucune image cassée et aucun débordement horizontal. Quatre captures réelles D69 (ouverture et fenêtre, bureau/mobile) sont conservées ; les deux captures mobiles ont aussi été inspectées visuellement. `controle-navigateur.json` consigne les contrôles et leurs empreintes.

Les premiers essais D50/D64/D69 signalaient les images locales absentes du serveur temporaire. Le dossier `fragments/assets/img/` prévu par `.github/workflows/pages.yml` a été rattaché ; les six surfaces de ces trois cours ont été reprises avec succès, sans modification des sources. Cette reprise et l’échec de configuration initial restent tracés dans `controle-navigateur-assets-complets.json` et le rapport consolidé.

Ces vérifications portent sur l’intégrité, le routage et le fonctionnement de l’interface. Elles ne constituent pas une relecture médicale exhaustive, une nouvelle vérification des recommandations ou une validation médicale humaine. Les audits différés restent différés.

## Limite de concurrence

Claude poursuit des travaux sur main et ses branches. Avant de recevoir/pousser ce commit, le coordinateur doit comparer la tête actuelle : si D69 a été injecté entre-temps, conserver la version existante et contrôler les empreintes, sans double injection ni rétablissement d’un ancien catalogue. Aucun push, fusion, publication ou suppression de branche n’est effectué par cet agent.
