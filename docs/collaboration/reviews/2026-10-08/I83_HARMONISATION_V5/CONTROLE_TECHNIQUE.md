# Contrôle technique — I83 — Varices des membres inférieurs (C-01-Cardiologie)

**Avis technique favorable sur la copie isolée V5**, candidat `d5b46aa2502c91517f7f80c8ac158f42605257e8`, base canonique `918ef69a8526bf0be38ffdf4f88438ad61d9a8a7`. Les sources archivées sur cette base sont extraites dans `/workspace/medina-env/reprise-i83/v5-candidate/source`, sans Git, avec remplacement sélectif des sept HTML et du glossaire autorisés. Les 16 empreintes base/proposition correspondent au manifeste et les huit sources restent identiques après les contrôles. Pop4 reste inchangé, SHA256 `dede4bdcf1974bbff6c2b2874410b64ac1e15003371fc9d78b3436c4999174f4`.

Inspection préalable sans import entrant : 8 HTML, 4 panneaux pA/pE/pS/pP, 47 fenêtres, 85 data-k, 34 entrées du glossaire. Aucun script, gestionnaire JavaScript, iframe, objet actif, cible statique manquante ni collision d’identifiant ou de clé de glossaire. Le Python entrant contient uniquement `from cardio_1 import a, G` et des appels `a` aux arguments littéraux ; les corps HTML du glossaire sont également inspectés.

Les nouvelles preuves indépendantes sont terminées avec code0 :

- Compilation syntaxique du glossaire et audit des sigles : aucun sigle découvert non couvert.
- Construction globale et S01 sur la même copie figée.
- Statique I83 : 41 839 mots, 47 fenêtres, 6 quiz, 6 Pareto.
- Interface native I83 : **1 923 contrôles, 0 échec et 0 erreur de page**, PC et mobile ; 78 déclencheurs directs, 7 imbriqués et 47 fenêtres couverts par format.
- Routes I83 et I87 vers I83 : **41 assertions, 4 cas PC/mobile**, quatre onglets accessibles sans débordement ni erreur JavaScript.
- Interface générale S01 : **72 assertions réussies**, aucune erreur.
- Interface globale I83 : `test_v7.py I83` termine OK avec code0.

Les tests canoniques et constructeurs utilisés sont identiques aux objets de la base918ef69. Les helpers HTTP locaux conservent toutes leurs assertions ; ils fournissent les ressources modulaires embarquées après vérification SHA256 et bloquent les destinations externes. Ils ne désactivent aucune vérification ni la validation TLS. Les commandes, horaires UTC/EuropeZurich, journaux et empreintes de preuves sont dans `CONTROLE_TECHNIQUE.json`.

Artefacts reconstruits :

- Global : SHA256 `8604ee4aa481582b1697884012e62edb915cf7bb4795d833ef70fbb2217dad6c`, 9860298 octets.
- S01 : SHA256 `cdffa963b1fd671c7a3948be9a1e2cdf85422bb3a74defd108a6d429f4658c5e`, 4571819 octets.

Cet avis technique est distinct de l’avis médical favorable avec deux réserves mineures documenté par réception. Aucun fichier canonique, Git ou livrable de Claude n’a été modifié. Il autorise techniquement la copie sélective de ces empreintes par le coordinateur ; il ne prouve pas leur injection ou publication. Les contrôles après injection et la preuve de déploiement doivent être conservés séparément.
