# Image_Codex_Finder

Moteur Python 3 sur POSIX/Linux (verrous `fcntl.flock`), bibliothèque standard, duplicable hors MEDINA. Recherche de **métadonnées et d’originaux existants** ; aucune génération, aucun téléchargement d’image, aucune importation ni publication automatique. Les contenus médicaux canoniques restent hors périmètre. Dans MEDINA, cette livraison vise uniquement S08/S05/S04/S06 ; les autres systèmes restent inchangés.

Règle de Vial : les images ou schémas de structures anatomiques générés ou dessinés par IA, y compris un SVG dessiné par un LLM, ne sont pas recevables. Une origine `ANATOMIQUE_IA` prouvée constitue un défaut **MAJEUR**, à remplacer par un original existant sourcé. Une origine non prouvée reste une réserve, sans label « recevable ». Les schémas non anatomiques sont distincts ; leurs flèches et valeurs exigent néanmoins des sources. Le filtre de métadonnées aide au repérage, sans certifier ces points.

```sh
python3 tools/image_codex_finder.py --cache /chemin/partage/images.sqlite3 serve
python3 tools/image_codex_finder.py search "renal histology" --broker http://127.0.0.1:8765 --limit 4
# Mode explicite sans broker : même fichier SQLite partagé entre tous les processus locaux.
python3 tools/image_codex_finder.py --cache /chemin/partage/images.sqlite3 search "renal histology" --direct
python3 tools/image_codex_finder.py search "renal histology" --provider europepmc --broker http://127.0.0.1:8765
python3 -m unittest tests.test_image_codex_finder -v
```

Le broker est recommandé pour les clients multiples. Un échec du broker termine la commande : aucun repli direct caché. `serve` accepte uniquement `127.0.0.1`. Accès distant privé éventuel par tunnel SSH vers ce port ; aucune exposition réseau ni aucun déploiement automatique. Une exposition future exige une infrastructure TLS authentifiée. Le fichier SQLite est local au serveur, sur un système de fichiers fiable : des copies indépendantes, plusieurs machines ou plusieurs fichiers **ne partagent pas** quotas ni verrous. Ne pas poser SQLite sur un partage réseau. Conserver les mêmes paramètres de budget pour tous les utilisateurs d’une base.

## API v1

`GET /search?q=renal%20histology&provider=commons&limit=4` : requête de 1 à 300 caractères, 1 à 20 résultats, fournisseurs fixes `commons` ou `europepmc`. En-tête obligatoire `X-Medina-Client: Image_Codex_Finder/1.0`, ajouté automatiquement par le client CLI. Cet en-tête non simple empêche les requêtes navigateur de type image/navigation ; aucun CORS ni prévol n’est autorisé. Ce mécanisme anti-CSRF ne constitue pas une authentification. Aucun paramètre URL arbitraire. JSON : `schema_version: 1`, `provider`, `query`, `retrieved_at` UTC, `results`, `publication_ready: false`, `automatic_import: false`. Échec : HTTP 400 avec `error` ; le client ne doit pas réessayer en boucle. Le broker n’est pas une API publique authentifiée ; n’y transmettre aucun identifiant de patient.

Commons associe recherche `generator=search` et `imageinfo` dans **un seul appel**, avec `maxlag=5` et User-Agent explicite. Les résultats donnent page source, URL originale, auteur, source déclarée, crédit, licence, URL de licence et preuves brutes des métadonnées. Les redirections HTTP sont refusées. Europe PMC sert uniquement à découvrir des articles et fournit leurs identifiants et liens. `isOpenAccess` n’autorise **jamais** une figure : `figure_license_approved: false`.

Le filtre refuse les marqueurs IA connus (`REJECTED_AI`) et les licences NC/ND (`REJECTED_LICENSE`). Seules les formes exactes CC BY, CC BY-SA, CC0 ou domaine public avec URL Creative Commons cohérente et provenance déclarée peuvent être `RIGHTS_CANDIDATE`. Origine, auteur ou licence incomplets : `NEEDS_REVIEW`. L’absence d’un marqueur IA ne démontre pas une origine humaine. **Toute sortie conserve `publication_ready: false`** ; les statuts ne valent ni approbation médicale, ni garantie juridique. Ouvrir la page et l’original ; vérifier visuellement l’anatomie/la légende, l’origine humaine, la licence propre à la figure, les restrictions éventuelles et l’attribution avant tout usage manuel. Une revue par IA n’est pas une validation médicale humaine.

## Sobriété et limites

SQLite coordonne les processus : dédoublonnage des requêtes normalisées, un appel actif par fournisseur et intervalle d’au moins une seconde **après la fin** de chaque appel ; un minimum est également enregistré avant le départ pour résister à un arrêt brutal. Verrous de fichiers POSIX tenus pendant toute la requête et libérés automatiquement par le système après arrêt du processus ; conserver le dossier `.locks` avec la base et ne jamais supprimer ses fichiers pendant un service actif. Les appels HTTP ont un délai socket de 12 s, une limite de lecture totale contrôlée entre blocs (au plus un délai socket supplémentaire) et 2 Mio maximum. Cache positif 30 jours, négatif une heure ; les erreurs ne deviennent pas des résultats vides. Date de consultation conservée dans le cache : recontrôler les droits sur l’original avant usage.

Budget persistant par fournisseur et jour UTC, 100 réservations par défaut (`--daily-budget`), seuil partagé en base ne pouvant être que réduit par un client, y compris appels échoués. Un slot réservé puis annulé par un cooldown peut consommer le budget. HTTP 429/503 et `maxlag` enregistrent un cooldown partagé ; `Retry-After` secondes ou date est respecté sans raccourcissement, défaut 60 s. Trois erreurs successives ouvrent le circuit au moins 600 s, y compris 429/503 (ou davantage si `Retry-After` l’exige). Aucun nouvel essai automatique ; les clients concurrents attendent seulement un appel déjà engagé ou un créneau limité. Un redémarrage conserve budget, cache et cooldown.

Politiques de référence : [MediaWiki API etiquette](https://www.mediawiki.org/wiki/API:Etiquette), [maxlag](https://www.mediawiki.org/wiki/Manual:Maxlag_parameter), [User-Agent](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy), [réutilisation Commons](https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia), [Europe PMC REST](https://europepmc.org/RestfulWebService), [Europe PMC copyright](https://europepmc.org/Copyright). Etiquette et réutilisation Commons consultées le 15 octobre 2026 dans le chantier de coordination ; Commons ne garantit pas les licences. La page de politique API Europe PMC a renvoyé HTTP 403 durant cette session : aucune lecture réussie de cette politique n’est revendiquée. Pas de collecte de figures ni d’API Open-i dans cette version.

## Vérification livrée

Le 15 octobre 2026 : **11 tests automatisés réussis**, dont quatre processus demandant la même recherche, sérialisation de recherches différentes, arrêt SIGKILL pendant HTTP, budget persistant, erreurs429/503/maxlag et refus d’un appel navigateur sans header. Test réel borné : **1 appel Commons et 1 appel Europe PMC**, trois résultats par source ; répétition de chaque recherche depuis le cache, **zéro appel supplémentaire**. [Reçu du test](IMAGE_CODEX_FINDER_SMOKE_2026-10-15.json). Les deux appels réussis ne garantissent pas la disponibilité future des fournisseurs. Les candidats renvoyés n’ont pas été validés visuellement pour publication.

Instruction Vial du 15 octobre 2026 : les moteurs Codex et Claude sont indépendants ; aucun courtier commun entre eux n’est requis. Les copies locales du moteur Codex partagent sa base, ses verrous et ses limites. Cette indépendance ne crée aucun partage implicite de quotas entre machines ; cache, cooldowns et budgets restent conservés dans chaque installation. Un broker local peut coordonner plusieurs clients ; sa panne ne déclenche jamais de repli direct caché.


## Arrêt de campagne 7_Starter_Codex

Chaque appel de la campagne transmet le fichier de contrôle local commun :

```sh
python3 tools/image_codex_finder.py --campaign-state /workspace/scratch/7-starter-codex-runtime/control.json search "renal histology" --direct
```

`MEDINA_IMAGE_CAMPAIGN_STATE` fournit aussi ce chemin par défaut. `Finder.search` relit le JSON avant tout résultat de cache ; une seconde vérification précède HTTP. Lorsque ce fichier est configuré, son absence, un JSON invalide, un schéma différent ou `image_execution_enabled` autre que `true` refuse la recherche, sans appel réseau. Le client broker vérifie également son contrôle local avant l'appel ; le serveur peut être configuré avec le même fichier. Le mode sans fichier conserve le fonctionnement autonome existant pour les recherches hors campagne.

Le Starter écrit atomiquement `control.json` après ses transitions CAS distantes, notamment `image_execution_enabled: false` après les 77 clôtures et leurs preuves figures complètes. Toutes les copies **locales de cette campagne** doivent employer ce même fichier. Ce fichier local ne garantit aucun arrêt intermachines ; une autre machine doit lire son état de campagne et actualiser son propre contrôle avant de chercher. Aucun historique, image, cache, verrou ni code outil n'est supprimé.

Tests ajoutés : arrêt malgré un cache déjà rempli ; fichier absent, malformé ou désactivé avec zéro appel HTTP. Les 13 tests du finder réussissent localement ; aucun appel réel aux fournisseurs n'a été ajouté pour cette évolution.
