# Mise à jour prioritaire — reprise Sol6.1 élevée

Le2novembre2026, après notifications de quota des trois agents Astra, Vial demande explicitement trois agents GPT6.1Sol high. Trois nouveaux auteurs réels sont lancés : `/root/sol_neurologie`, `/root/sol_endocrinologie`, `/root/sol_nephrologie`. Les identifiants internes `astra_*` sont conservés pour ne pas réécrire les reçus historiques ; le modèle et le nom runtime courants sont affichés séparément. Le parent conserve son modèle de session, qu’il ne peut pas modifier par outil. Neurologie conserve la coordination clinique. Le registre et les chemins exclusifs restent requis ; aucun cinquième auteur simultané. Les treize clôtures Astra/Codex existantes ne deviennent pas des travaux Sol.

# MEDINA — mandat, affectations et continuité du 2 novembre 2026

L'ordre utilisateur de cette conversation est la règle opérationnelle actuelle.
Échéance confirmée : **2 novembre 2026, 08:00 Europe/Zurich (07:00 UTC)**.
Les règles historiques de lots de sept sont remplacées pour cette campagne par
une leçon active par spécialité, quatre filières parallèles. Les réservations
distantes préexistantes restent intactes. Aucune PR vers main avant présentation
des cours, images injectées dans leur aperçu et annotations à Vial.

| Agent réel | Modèle demandé au lancement | Spécialité | Première leçon libre | Rôle |
|---|---|---|---|---|
| astra_neurologie | GPT-6 Astra, high | Neurologie | G02 | Auteur et référent d'orchestration clinique |
| astra_endocrinologie | GPT-6 Astra, high | Endocrinologie | E00 | Auteur |
| astra_nephrologie | GPT-6 Astra, high | Néphrologie | N04 | Auteur |
| codex_hematologie | Codex, modèle de session | Hématologie | C85 | Auteur et exécution des outils d'orchestration |

Le parent ne peut pas changer son propre modèle. Le référent Astra donne l'avis
clinique d'orchestration ; Codex exécute les opérations. Aucun rôle Astra fictif.
Les identifiants des trois sous-agents sont les identifiants réellement retournés
par l'outil collaboration. Leurs noms portent leur spécialité. La réaffectation
nécessitera un nouvel intitulé et une nouvelle réservation après clôture réelle
de la spécialité précédente ; aucune création silencieuse d'un cinquième auteur.

## Prévention des collisions

1. Consulter le registre distant paginé et les PR avant toute acquisition.
2. Acquérir une mission existante libre avec `ai_session_guard.py acquire`.
3. Créer le worktree dédié sur le SHA exact de son manifeste ; réussir `start`.
4. Un agent ne modifie que les chemins de son manifeste et de sa leçon.
5. Les rapports préparatoires vivent dans `harness/agents/<specialite>/` ; leur
   auteur est le seul écrivain. L'index Git du harness appartient au parent.
6. Aucun auteur ne modifie moteur, catalogue partagé, cours d'autrui ou main.
7. Un bail périmé est signalé, jamais récupéré automatiquement. Une réservation
   distante demeure active jusqu'à libération explicite et motivée.
8. Les modifications partagées et l'intégration seront sérialisées après revue ;
   la rédaction dans les quatre worktrees est parallèle.

## Portes obligatoires

Avant production : catalogue bracelet, prompt empreinté, quatre affectations,
HTML de plan, tests négatifs réussis sur le code exact et veille saine récente.
Le reçu d'acquisition réel est ensuite requis pour ouvrir une leçon.

Avant achèvement : 14 points monographiques reliés aux passages sources, matrice
20 rubriques Medina, quatre onglets, sémiologie, FI suisses exactes, provenance
et droits des figures, annotations, contrôles ordinateur/mobile, revues médicale
et linguistique attribuées avec corrections relues. Le contrat SSP V2 §7 accepte
l'auto-relecture et interdit de la nommer indépendante : le mode `self_review`
est donc explicite. Une vérification distincte ciblée reste proportionnée au risque.
Les contrôles de balises ne
remplacent jamais ces revues. Une lacune bloque la clôture, pas sa déclaration.

## Économie et métriques

Réutiliser les passages attribués et empreintés ; extraire au plus 200 lignes et
24 Ko ; ne pas recharger une extraction identique. Les doses, unités, négations,
limites et populations ne sont jamais compressées sémantiquement. Les 20 outils
du bracelet sont catalogués, pas réputés installés. Aucun appel LLM automatique
payant. Tokens/coût réels restent `null` sans mesure du fournisseur ; les octets
évités sont une métrique séparée. Les sections/heure sont des déclarations de
production, pas des leçons médicalement validées ni une économie financière.

## Veille et reprise

`python3 harness/medina_harness.py daemon` observe chaque 600 secondes, conserve
ses journaux et reconstruit `dashboard.html` et `status.json`. Il ne renouvelle
jamais l'activité déclarée d'un agent. Après 20 minutes sans déclaration, l'agent
est signalé comme activité non confirmée. Un observateur distinct sur GitHub
doit lire les commits publiés et produire ses propres preuves toutes les dix
minutes ; GitHub Actions peut retarder ses déclenchements. Le workflow ne réveille
pas les modèles natifs de ce chat. Toute absence de backend d'auteur persistant
doit rester visible ; ne pas annoncer une production autonome hors session.

À partir de 08:00 Zurich, la première observation fige `rapport-08h00.html` avec
l'heure réelle de génération. Le tableau courant continue à se mettre à jour.
Les artefacts GitHub et leurs logs servent de preuve de continuité et d'alerte.
Les scripts et données restent versionnés pour reprise ; un processus local
seul ne constitue pas un hébergement permanent.

Commandes : `bracelet.py '<tâche>'`, `medina_harness.py self-test`, `watch`,
`gate`, `claim`, `progress`, `extract`, `report`, `validate`, `daemon`.

### Surveillance indépendante de l'environnement de travail

Le cron GitHub natif reste absent de main. Une autre voie a été testée :
`workflow_dispatch` par identifiant accepte la branche de travail (HTTP204 et
run41374061103 réussi). `remote_watchdog.py` utilise ce mécanisme pour demander
un successeur, après une observation et une attente jusqu'à600secondes. Le
successeur utilise toujours la branche du harness ; aucune PR ni écriture main.
Chaque passage conserve un artefact autonome. Le contrôle signale un état source
ancien, une activité auteur ancienne ou un garde fermé ; il ne les rafraîchit pas.
Une erreur d'observation reste visible même après le lancement du successeur.

La chaîne doit être confirmée par un premier passage puis son successeur effectif,
et cette preuve reste dans `monitor.json`. L'absence de nouveaux commits de cours
n'est jamais présentée comme une production médicale. Les pannes GitHub, quotas,
révocations de droits et retards restent possibles. `watchdog-control.json` permet
l'arrêt explicite ; arrêter le run actif donne un arrêt immédiat. Une seule chaîne
est autorisée par le groupe de concurrence. Aucun appel LLM ne sert à la veille ;
un runner standard attend entre les contrôles, ce qui consomme du temps Actions.


## Passage à la leçon suivante

Les opérations du registre utilisent désormais `python3 /workspace/Medina-harness/harness/registry_guard.py --root CHEMIN_WORKTREE SOUS_COMMANDE ARGUMENTS`. Le wrapper exécute le garde existant sans changer ses contrôles de base approuvée, mission, périmètre, génération ou transaction CAS. Son fetch utilise une référence locale UUID temporaire puis la supprime ; il ne lit ni n’écrit le FETCH_HEAD partagé entre worktrees. Cette séparation empêche deux observations concurrentes de confondre leurs résultats de fetch. Trois tests couvrent l’isolation, l’échec réseau sans repli vers un ancien résultat et la validation du nom de remote. Le publisher inclut le wrapper et ses tests ; la suite du harness compte45tests depuis le2novembre à04:35UTC.

La commande `python3 harness/medina_harness.py complete AGENT DOSSIER` vérifie le manifeste à14points, les20rubriques couvertes avec preuves, les revues attribuées, les images et l’absence de réserve bloquante. Le reçu `source-binding.json` doit correspondre aux octets actuels des six fichiers du cours, du glossaire et de l’aperçu. Toute modification invalide ce reçu ; la veille le signale sans le renouveler. La commande conserve l’historique des achèvements et autorise ensuite une nouvelle acquisition exclusive. Elle ne crée aucune PR, ne libère pas automatiquement le registre et ne certifie pas la médecine. Les achèvements sont conservés dans completed_lessons ; un nouveau claim ne les efface pas. Les limites documentaires neutralisées restent visibles, distinctes des réserves bloquantes. L’achèvement de projet ne déclenche pas une PR.


## Consultation du suivi et rapport figé

Le tableau de bord courant récupère les états toutes les 60 secondes ; leur publication et leur observation logicielle suivent une cadence de 600 secondes. Ouvert comme fichier téléchargé, il utilise la branche publique GitHub sans jeton ; en HTTP, il lit status.json à côté du HTML. Une erreur réseau conserve le dernier état et affiche son ancienneté. Le rapport08h porte report_frozen_at et ne récupère pas les états ultérieurs.

Le navigateur de cet environnement interdit la navigation file:// ; cette politique n’a pas été contournée. Le suivi nonHTTP a été testé sur une origine about:blank avec réponse CORS interceptée, et le serveur public a répondu200 avec Access-Control-Allow-Origin:*. Le navigateur HTTP a vérifié les quatre filières, les340lignes historiques/campagne, l’absence de débordement, le filtre, les actualisations initiale et à60secondes (horloge de navigateur avancée) et l’affichage d’une source périmée. Un test de navigateur distinct vérifie zéro requête réseau pour le rapport figé.


## Relais du2novembre2026,13h10:17Europe/Zurich

La file néphrologique actuelle est achevée :N04,N29,N00,C64,N02,N03,N05,N06, soit8livraisons enregistrées, sans certification humaine. N17 appartient à un mandat concurrent et n’est pas repris. Conformément à la demande de Vial de passer à une autre spécialité, l’auteur technique `/root/sol_nephrologie` poursuit sous le nom de production **Sol-Hématologie-D77**. Son identifiant historique du harness reste `astra_nephrologie` pour ne pas réécrire les reçus précédents. Le champ `specialty` désigne désormais pour ce slot sa filière d’origine ; `active_specialty` indique le relais hématologique.

D77 est retiré de la file du parent et ajouté uniquement à ce slot. Le parent conserveD63,puisC92 ; aucune édition deD63 par le relais, aucune édition deD77 par le parent. L’acquisition distante, le worktree, la branche et les chemins exclusifs restent obligatoires avant rédaction. Les quatre auteurs travaillent en parallèle ; deux peuvent désormais couvrir des leçons différentes de l’hématologie après épuisement d’une filière. L’exclusivité porte sur les leçons et chemins réservés.

## Renforcement effectif de la veille sémiologique

Depuis le2novembre2026 à13h02heure suisse, le harness impose sept règles structurelles natives supplémentaires avant toute nouvelle clôture :six onglets, premier onglet sémiologique/ARIA correct, panneau visible et lié, titre h3 exact, neuf rubriques nommées contenant du texte, lienHTTPS dans sources, marqueur clinique sur un élément contenant de la prose danspA.53tests réussissent avec des cas négatifs représentant les défauts observés. La veille600s relit les sources des achèvements, conserve les réserves historiques et ne renouvelle ni activité auteur ni source-binding. Une réserve historique ne transforme pas une livraison en publication autorisée ; elle doit être traitée avant intégration sous mandat approprié.


## Relais réservé après D77 — 2026-11-02T13:01:56.169261+00:00

C92 est une création et réserve `chapters.json` avec sa mission. D62, D65, D66, C82 et C88 nécessitent également ce fichier partagé : ils ne sont pas acquis en parallèle. Pour maintenir quatre auteurs sans collision, G09 (cours existant, aucun droit sur `chapters.json`) est retiré de la file du créneau neurologie initial et attribué exclusivement au créneau natif `/root/sol_nephrologie`, après achèvement réel, push vérifié et libération de D77. Affichage futur : **Sol-Neurologie-G09**. L’identifiant technique historique `astra_nephrologie` est conservé pour ne pas perdre ses huit achèvements rénaux et son relais D77. G06 puis G07/G08 restent au premier auteur neurologie. Le classement de G09 dans le système neurologie du plan ne change pas.


### Relais E40 — 2 novembre 2026

Après les dix livraisons du slot historique astra_nephrologie (huit rénales dont C64, D77, G09), E40 — Kwashiorkor est transféré exclusivement de la queue future astra_endocrinologie vers ce slot, sous le nom de production Sol-Nutrition-E40 et active_specialty nutrition. Autorisation ciblée de root, auteur E35 prévenu et exclusion opérationnelle confirmée ; root n’édite pas cette config en parallèle. Identité technique sol_nephrologie et historique conservés. L’appartenance statistique E40 au système S05 et au plan Codex historique reste intacte ; aucun fichier du plan ou cours scellé modifié. Mission existante sans chapters.json ; C92 parent et G07/E35 concurrents intacts.
