# Capacités administratives observées — 15 octobre 2026

Audit en lecture seule de `vialdjoukang-spec/Medina`, depuis la connexion disponible dans cette session. Aucun réglage distant, installation, permission ou protection n’a été modifié.

| Observation | Résultat | Portée réelle |
| --- | --- | --- |
| Profil du connecteur GitHub | `vialdjoukang-spec`, identifiant 302584639 | Compte propriétaire connecté ; ne constitue pas une identité distincte pour chaque IA. |
| Métadonnées du dépôt et permission collaborateur | `admin`, avec `admin`, `maintain`, `push`, `pull`, `triage` vrais | Rôle du compte ; ne prouve pas que chaque opération administrative est autorisée au jeton de l’installation. |
| Installations visibles à cette connexion (`GET /user/installations`) | Une : `chatgpt-codex-connector`, app 1144995, installation 165237313, sélection `all` | Inventaire visible au jeton courant ; ne prouve pas l’absence d’une autre intégration Claude dans le compte. |
| Permissions déclarées de cette installation | `actions:write`, `contents:write`, `issues:write`, `pull_requests:write`, `workflows:write` ; `checks:read`, `metadata:read`, `statuses:read` | Aucune permission `administration` ni `members` n’est indiquée. Les droits du propriétaire ne sont pas automatiquement ceux de l’app. |
| Protection classique de `main` (`GET /repos/vialdjoukang-spec/Medina/branches/main/protection`) | HTTP 403, `Resource not accessible by integration` | Lecture inaccessible à l’intégration actuelle ; état de protection inconnu. Ne pas conclure « aucune protection ». |
| Rulesets du dépôt (`GET /repos/vialdjoukang-spec/Medina/rulesets`) | Liste vide | Aucun ruleset renvoyé dans cette vue ; résultat distinct des protections classiques. |

L’égalité administrative locale Codex/Claude est définie dans [l’instruction commune](instructions/PUBLICATION_EN_ETAT_PARITE_2026-10-15.md). Aucune opération de cette mission ne prétend créer un rôle GitHub pour un modèle. Pour une égalité effective entre intégrations distinctes, le propriétaire doit disposer d’une installation Claude identifiable et vérifier les mêmes permissions sur le même dépôt ; ses droits ne sont pas observables par cette seule session. Les réglages de l’installation visible sont [sur GitHub](https://github.com/settings/installations/165237313).

La configuration de dépôt `.claude/settings.json` autorise désormais les commandes Bash et la lecture, l’édition et l’écriture dans le projet, ainsi que les outils de recherche web, avec acceptation locale des éditions. Ses hooks et sa ligne d’état sont conservés. Aucun fichier de configuration Codex propre au dépôt n’a été trouvé ; aucun format de configuration supposé n’a été créé. Cette session Codex dispose déjà de l’accès complet au système de fichiers et du mode d’approbation `never`, selon sa configuration d’exécution. Ces éléments ne modifient pas les politiques supérieures du client, de l’environnement, des outils ou de GitHub.

Le veto du projet est vérifié par `tools/espace.py garde` et le contrôle de publication prévu dans Pages. L’auteur du journal reste déclaratif. L’absence de lecture administrative de la protection et d’identités distinctes vérifiées empêche de certifier un veto imposé par GitHub. Un administrateur effectif pourrait modifier les workflows ou agir hors de ces chemins. Ce rapport ne présente donc ni l’égalité des droits des apps ni un veto universel inviolable comme réalisés.
