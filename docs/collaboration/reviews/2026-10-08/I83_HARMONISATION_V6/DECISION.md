# I83 — décision du complément v6 (C-01-Cardiologie)

La remise Claude `8a6dc7f28bbdaa5251f9a4b75031875073bf7ccb` corrige exactement les deux réserves mineures du contre-audit v5. Les huit sources finales sont présentes, avec trois fichiers modifiés par rapport à v5 ; source injectée au commit `eb276b90465edcd238fd122b4bd178015a5cb8c0`.

Le delta est favorable : terminologie ESVS non exclusive et précision « thermique » des incidences. Le contre-audit v5 reste la preuve médicale de fond ; la v6 ferme ses deux réserves. Aucune réserve nouvelle identifiée dans ce périmètre, aucune certification exhaustive ou CIM-11 revendiquée.

Reconstruction canonique identique au candidat indépendamment testé : SHA256 `546806a6d8d9d7f9d4e040b810023c9d7d1e994fe9bfe1fb6e36d0ed98af918b`. Les 118 tests unitaires ont été réexécutés et passent. Sur v6 : builds global/S01, syntaxe, sigles, statique, navigateur global ordinateur/mobile et 41 vérifications de routage passent. Les 1923 tests natifs et 72 S01 appartiennent à la preuve v5, conservée comme historique ; ils ne sont pas présentés comme réexécutés sur v6.

Publication GitHub/Pages vérifiée au déploiement `c545b79cb604347c7c1f38c5c8fe03126daafbc9` (run `37781328939`). Les octets publics correspondent à l’artefact Pages ; leur contenu décodé est identique au candidat local. Le seul écart brut est le champ OS du header gzip, documenté sans modifier les fichiers. Les 41 assertions de routes I83/I87 ont aussi été exécutées sur le fichier réellement servi. [Preuve complète](PUBLICATION_PAGES.md). A41 reste exclusivement en copies de livraison ; aucun autre lot Claude n’est injecté par cette décision.
