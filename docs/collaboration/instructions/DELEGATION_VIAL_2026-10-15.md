# Delegation operationnelle de Vial a Claude — 15 octobre 2026

Provenance : demande directe dans ChatGPT du 15 octobre 2026, vers 14 h Europe/Zurich.
Cette instruction remplace les interdictions historiques de demander a nouveau
l'autorisation de Vial pour les operations courantes du projet MEDINA.
Il s'agit d'une delegation explicite, pas d'un clone humain ni d'un role GitHub administrateur.

## Effet immediat

Claude est decisionnaire prioritaire sur son travail MEDINA : recherche,
redaction, corrections, organisation, choix techniques, branches, PR et livraison.
Un ancien STOP, une echeance de session passee ou une attribution historique
ne suffisent plus a lui interdire une nouvelle proposition. Claude peut proposer
et tester l'adaptation precise d'une garde devenue incompatible, en conservant
les autres controles et leurs preuves. Ne pas supprimer indistinctement les gardes.
Les reserves de reception sont des constats, pas un veto personnel de Codex.
Une absence d'audit ne vaut pas interdiction de poursuivre la preparation.

L'accord ne change ni les permissions effectivement accordees par GitHub,
ni les obligations de veracite. Un audit differe reste differe ; une CI echouee
reste echouee. Ne pas certifier une validation humaine ou un site non controle.
Les corrections medicales exigent toujours les sources applicables et les
precautions visibles. Pas de suppression d'historique ni de secret publie.

## Preservation du travail actif

Le moteur ne pousse, ne fusionne, ne rebase et ne force aucune branche.
Il n'edite ni les sources medicales ni les registres de production ou les audits.
Il inspecte toutes les branches et PR avec pagination ; les alertes de delegation
ne concernent que les PR internes `claude/*`, sans inferer l'identite depuis
le compte partage. Les branches sans PR sont inventoriees seulement.
Claude choisit quand et comment traiter une alerte dans sa session active.
Le moteur n'est pas un service capable de lancer Claude Code.

## Cinq minutes et controle utilisateur

Une nouvelle combinaison tete/base/blocages recoit une alerte horodatee.
Au premier scan apres au moins 300 secondes sans reponse du compte proprietaire
dans ce fil, une notification unique rappelle la delegation a Claude pour des
decisions operationnelles reversibles. Cela ne donne aucun droit de contourner
une protection GitHub, d'ecraser le travail concurrent ou d'effacer une reserve.
Tout changement de tete ou de base ouvre un nouveau delai ; l'heure de reception
de l'evenement n'est pas substituee a l'heure reelle du commentaire GitHub.

Dans l'issue de controle indiquee par `organisation/deblocage_vial.json` :

- `/medina off` : arreter alertes et delegations au prochain scan.
- `/medina on` : reprendre.

Seules les commandes exactes du compte proprietaire non-bot sont acceptees.
Ce compte etant partage, GitHub ne distingue pas Vial de Claude : Claude ne doit
pas utiliser ces commandes sans demande de Vial. Une reponse de ce compte dans
une PR suspend par precaution la delegation automatique de cette alerte.
Le bouton GitHub Actions « Disable workflow » fournit aussi un arret immediat
des nouvelles executions ; annuler un run deja en cours si necessaire.

Cadence demandee : cinq minutes ; GitHub peut retarder ses executions.
Les cinq minutes sont un minimum, pas une garantie de reaction a la seconde.
Les problemes inconnus exigent le diagnostic de Claude, pas une levee fictive.

## Mise a jour — progression souple et triage neutre (Vial, 15 octobre 2026)

Les audits médicaux indépendants et contre-audits sont suspendus jusqu'à nouvel
ordre. Leur absence, leur report ou un résultat non encore obtenu ne bloque pas
la préparation, la correction ou la proposition d'une livraison. Ils ne sont
jamais présentés comme réussis. Les échecs techniques détectés restent visibles
comme faits à examiner, sans veto automatique du moteur.

Le moteur ne bloque pas une PR sur un commentaire dans son fil. Après l'alerte
et 300 secondes minimales, il publie une délégation unique pour la tête/base
concernée. Claude peut accepter ou rejeter le rapport et choisir la correction.
Les signaux de contenu se limitent aux marqueurs manifestement provisoires
(TODO/TBD/FIXME, texte de remplissage, fichier de cours ajouté vide) ; ce sont
des suggestions, jamais une correction ni un jugement médical automatique.

Le seul contrôle d'arrêt du moteur reste `/medina off` dans l'issue de contrôle
97, réactivable par `/medina on`. Il ne s'agit pas d'un veto sur une livraison.
Le compte GitHub étant partagé, le moteur ne peut pas authentifier séparément
Vial et Claude : Claude n'utilise pas ces commandes sans instruction de Vial.

La lecture préalable du [Prompt de vérité](../betta/PROMPT_VERITE.md) reste
obligatoire pour Claude et chaque agent qui ouvre une leçon. La suspension des
audits ne suspend ni cette lecture ni la porte documentaire avant rédaction.
Le moteur rappelle la règle, mais ne prétend pas pouvoir prouver qu'une lecture
a eu lieu.
