# Garde de remise par fragment — 8 octobre 2026

Travail effectué dans `/workspace/work/medina-resume`, initialement basé sur `a6f82b6`. Aucun réseau, push, commit ou changement des sources médicales canoniques n'a été effectué par cet agent. Les commits d'intégration sont gérés par le coordinateur.

## Périmètre livré

- `tools/espace.py` : détection du protocole `fragment-unique-2026-10-08`, consultation locale et garde des commits.
- `tests/test_espace_fragments.py` : 22 tests utilisant des dépôts Git temporaires, sans valeur clinique.
- `.github/workflows/espace.yml` : garde sur push, PR et déclenchement manuel, avec historique complet. `workflow_call` est également disponible, mais le coordinateur a choisi de brancher la garde directement dans `pages.yml` avant les tests et la construction.

Les commandes historiques `deposer`, `auditer` et `injecter` par cours échouent avant tout fetch, changement de worktree ou publication dès que le registre actif est présent. `ouvrir` devient une consultation du checkout ; `consulter ID_FRAGMENT` affiche le suivi local. Les anciennes opérations restent uniquement disponibles pour les historiques sans ce registre ; leurs preuves par cours ne sont jamais utilisées pour autoriser une injection sous le nouveau protocole.

Aucune nouvelle commande de remise finale n'est présentée comme opérationnelle : cet outil ne produit pas la revue médicale, ne déclare pas la complétude, et n'invente pas les rapports requis. Les fragments actuellement incomplets restent non transmissibles, non auditables et non injectables.

## Schéma de preuves exigé avant une remise finale

Le registre racine est `organisation/fragment_status.json`, schéma 1 et protocole fixé. Il contient exactement les 22 identifiants et libellés du registre public. Les états reconnus sont `A_COMPLETER`, `EN_PRODUCTION`, `PRET_A_TRANSMETTRE`, `EN_AUDIT_CROISE`, `AUDITE`, `INJECTE`.

Les entrées incomplètes acceptent l'auteur historique non attribué de S01. Une attribution initiale vers Claude ou Codex est permise avant toute revue réelle. Le propriétaire d'un fragment déjà attribué ne peut être remplacé.

Pour `complete: true`, les preuves suivantes sont toutes requises :

- `coverage.status: verifiee`, `coverage.scope: fragment_complet`, `coverage.files` (chemins relatifs et SHA-256), `inventory_path` et `inventory_sha256`.
- L'inventaire est un JSON effectivement présent : `fragment_id`, `scope: fragment_complet`, `complete: true`, `files` égal à la couverture, liste `categories` non vide et `uncovered_categories: []`.
- `internal_review` : `reviewer` égal à l'auteur, `scope: fragment_complet`, `files` égal à la couverture, `source_dir`, `report_path` et `report_sha256`.
- Le rapport est effectivement présent, non vide et à l'empreinte déclarée ; toutes les sources archivées sous `source_dir` correspondent exactement à `files`, sans fichier supplémentaire non inventorié.

Pour l'audit croisé unique :

- `cross_audit.auditor` désigne l'autre IA ; `scope: fragment_complet`, verdict favorable ; le rapport et ses sources archivées sont vérifiés.
- `input_files` égale la remise initiale auto-revue ; `files` décrit la version finale corrigée. Les fichiers initiaux ne peuvent être supprimés ; l'auditeur peut corriger leurs contenus et ajouter des sources.
- La remise complète et son auto-revue doivent déjà exister au commit antérieur à l'audit. Les preuves de cette remise restent inchangées lors de l'audit.
- L'audit peut être enregistré dans le même commit que l'injection : un seul tour suffit. Un deuxième audit, le retrait du premier ou la modification ultérieure de la remise auditée sont refusés.

Pour l'injection :

- `status: INJECTE` ; `injection.injector` égale l'auditeur croisé.
- `injection.files` et `locked_files` égalent les empreintes finales de l'audit ; les sources canoniques doivent posséder ces empreintes.
- L'entrée entière `INJECTE` devient immuable, y compris son statut et ses annotations. Toute modification, suppression ou substitution de ses fichiers est refusée.
- Toute modification de `chapters/`, `glossary/` ou `chapters.json` non couverte par une nouvelle injection complète et auditée est refusée. Les chemins absolus, traversées de répertoire et liens symboliques ne peuvent servir de sources ou de preuves.
- L'activation initiale du protocole exige 22 entrées incomplètes sans audit, injection ou verrou. Elle ne peut accompagner une modification médicale ; un registre ajouté artificiellement avec des injections n'autorise pas cette modification.

## Vérification

`python3 -m unittest discover -s tests -p test_espace_fragments.py` : 22 tests réussis. Ils couvrent le refus d'un fragment incomplet, le refus avant réseau des anciennes mutations, la lecture seule, l'auto-audit, l'injection par le producteur, l'audit unique, les corrections de l'auditeur, les empreintes divergentes, la réouverture, la suppression du contenu verrouillé et du registre, une fausse activation du protocole, les chemins et liens symboliques.

Compilation Python et `git diff --check` réussis. Les consultations réelles `consulter T1` et `ouvrir A41` réussissent sans mutation. L'ensemble des tests du dépôt, le rebase et la garde finale sur les commits d'intégration relèvent du coordinateur.

## Limites concrètes

Ces contrôles établissent la présence, l'intégrité et la relation des preuves. Ils ne certifient pas l'exactitude médicale d'un rapport, la validité d'un inventaire CIM-11 ou l'identité d'un rédacteur au-delà des traces déclarées dans le dépôt. Les validations clinique et documentaire restent un travail réel préalable.

Le verrou est défini par fichier. Inscrire un catalogue global ou un glossaire partagé dans `locked_files` le fixe pour toutes ses utilisations : son organisation doit être prévue avant la première injection. Aucun fragment réel n'est actuellement marqué complet ou injecté par ce travail.
