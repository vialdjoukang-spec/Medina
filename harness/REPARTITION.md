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
et droits des figures, annotations, contrôles ordinateur/mobile, revue médicale
et linguistique distinctes avec corrections relues. Les contrôles de balises ne
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
