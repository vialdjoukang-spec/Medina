# 7_Starter_Codex — moteur indépendant, campagne de 77 leçons

Instruction Vial transmise le 15 octobre 2026. Le total est **77, premier lot compris** : 52 leçons existantes attribuées à Codex, puis 25 nouvelles prises dans son plan de production. Aucun cours Claude. Les missions et cette configuration doivent être approuvées dans `main` par la gouvernance, jamais par l'ouvrier. Le premier lot I63/G01/E10/E05/N17/D69/D64 est adopté : ses quatorze rapports sont des livraisons, pas des clôtures. Ne pas redistribuer ces audits.

Le moteur n'est ni une validation clinique humaine, ni une permission d'ignorer les gardes. L'exception d'indépendance concerne le moteur : aucun courtier commun avec Claude n'est nécessaire pour ses états et son orchestration. Les contraintes de provenance et de recherche des figures restent applicables.

## Exécution locale

```sh
python3 tools/starter_codex.py --root /chemin/depot verify
python3 tools/starter_codex.py --root /chemin/depot status
python3 tools/starter_codex.py --root /chemin/depot tick
python3 tools/starter_codex.py --root /chemin/depot run
```

`verify` contrôle les preuves sans créer de mission, worktree, processus IA ni état distant. `tick` effectue une décision et attend au plus la durée bornée de son ouvrier. `run` poursuit avec un intervalle de 60 à 120 secondes, par défaut 90. Le CLI Codex doit être réellement authentifié ; aucun secret n'est affiché. Il est lancé avec `-a never exec --json -m gpt-6.1 -c model_reasoning_effort="high"`, sans contournement. Les sous-missions médicales emploient GPT6.1 high ; les linguistiques GPT6.1 medium.

La configuration `.medina/7-starter-codex.json` est exclusivement lue dans le SHA courant de `origin/main` ; une copie de travail ne peut pas approuver ses propres missions. Une fois la campagne engagée, son empreinte est figée dans l'état. L'environnement local et les connexions Git/GitHub/Codex doivent exister ; pas de secrets dans le dépôt, ni de cron ou workflow ajoutés.

## Contrat de configuration version 1

Champs : `schema_version: 1`, `queue` de 77 objets uniques, `batches` de onze objets et `image_tasks_done` liste facultative de preuves complémentaires. Options : `worker_backend: "native_handoff" | "codex_cli"` (défaut CLI), `poll_seconds` 60–120, `worker_timeout_seconds` 60–14400 (défaut 3600), `codex_binary` (défaut `/opt/codex/bin/codex`).

Chaque entrée de `queue` porte `code`, `owner: "Codex"`, `mode: "existing" | "production"`, `closure_path`, `missions: {"MED": ID, "LANG": ID, "INTEGRATE": ID}`. Les 25 nouvelles portent aussi `missions.PRODUCE` et `production_receipt` ; `PRODUCE` peut être la même mission source que `INTEGRATE`. Il reste un seul auteur source. Le reçu de production devra relier cette mission, `complete: true` et `final_files` identiques aux sources auditées. Ne pas auditer une leçon inexistante.

Chaque objet de `batches` porte `coordinator_mission`, mission intégrateur approuvée pour ces sept codes, limitée à son dossier de coordination. Les sources passent séparément par les missions `INTEGRATE` du code. Chaque mission est acquise au registre via `ai_session_guard.py acquire`, puis son worktree propre est créé au SHA exact courant de main et `start` doit réussir. Le moteur ne crée ni n'approuve de manifeste. Il vérifie l'acteur, le propriétaire, les codes, les chemins et le modèle/effort des audits dans les manifestes approuvés.

## État distribué et reprise

La branche dédiée `medina/7-starter-codex` ne contient que `state.json`. Toutes les transitions créent un commit avec pour parent le SHA précédemment lu et font un push normal, sans force. Deux clones concurrents ne peuvent gagner la même transition. `SPAWN_INTENT` est publié avant toute acquisition et tout lancement. L'état contient le propriétaire unique, le lot, les codes clôturés, le worktree et les événements de l'ouvrier : hôte, PID, démarrage, fichier JSONL et `thread_id` extrait de `thread.started` dès sa réception.

Un état `SPAWN_INTENT` ou `RUNNING` déjà présent ne déclenche jamais de second lancement, même ancien. Une exception, une durée dépassée ou un ouvrier terminé sans les sept preuves donne `NEEDS_RECONCILIATION`. Aucune expiration de bail ne relance une IA ambiguë. L'administrateur inspecte les événements, la session, le registre et les branches avant toute nouvelle transition d'état. Ne pas simplement remettre `IDLE` : retrouver ou clôturer l'exécution originale ; si des preuves complètes existent, vérifier ces preuves et effectuer une transition administrative tracée. Un retour de processus 0 ne vaut jamais clôture.

L'ouvrier CLI est limité en durée et en événements à 32 Mio. Aucun plafond global de tokens n'est prétendu ; l'option non vérifiée `model_max_output_tokens` a été retirée. La durée borne l'exécution totale. Le contrôleur ne signale que son groupe de processus créé par lui, pendant qu'il le possède. Il ne tue jamais des PID redécouverts ou les moteurs Claude. Les détails bruts d'authentification ne sont pas imprimés ; les erreurs de prérequis arrêtent l'exécution au lieu d'une boucle de tentatives.

## Preuve stricte de clôture d'une leçon

Le fichier `closure_path` approuvé, normalement `docs/collaboration/ssp-v2/execution/<INTEGRATE-ID>/closure.json`, est un reçu versionné dans main. Structure :

```json
{
  "schema_version": 1,
  "code": "I63",
  "owner": "Codex",
  "complete": true,
  "blocking_reserves": 0,
  "final_files": {"chapters/I63/I63_a.html": "SHA256"},
  "reports": {
    "MED": {"mission": "ALPHA1-CODEX-I63-MED", "path": "CHEMIN_RAPPORT_MED", "sha256": "SHA256", "final_files": {"chapters/I63/I63_a.html": "SHA256"}},
    "LANG": {"mission": "ALPHA1-CODEX-I63-LANG", "path": "CHEMIN_RAPPORT_LANG", "sha256": "SHA256", "final_files": {"chapters/I63/I63_a.html": "SHA256"}}
  },
  "figure_validation": {"status": "passed", "path": "CHEMIN_PREUVE_FIGURES", "sha256": "SHA256", "final_files": {"chapters/I63/I63_a.html": "SHA256"}},
  "integration": {"pr": 123, "merge_sha": "SHA40"},
  "publication": {
    "main_sha": "SHA40",
    "manifest_path": "CHEMIN_MANIFESTE_PUBLICATION",
    "manifest_sha256": "SHA256",
    "probes": [{"url": "https://SITE/PAGE", "sha256": "SHA256_REPONSE_PUBLIQUE"}]
  }
}
```

Les champs SHA de cet exemple sont des emplacements, jamais des preuves. `final_files` doit inventorier toutes les sources finales réellement couvertes. Chaque preuve MED/LANG et figures doit porter exactement cette table. Une ancienne empreinte n'est pas silencieusement renouvelée : reprendre l'audit affecté ou documenter la revalidation réelle.

Le moteur vérifie les octets des sources et rapports dans main ; la PR doit être fusionnée vers main, son SHA exact doit correspondre et tous ses contrôles CI doivent avoir terminé avec succès (ou résultat neutre/ignoré explicite). Il faut au moins un contrôle CI. Le SHA de publication doit descendre du SHA de fusion et être ancêtre du main actuel. Les fichiers sources de ce SHA de publication doivent égaler les empreintes finales.

Le manifeste de publication est un JSON portant exactement `main_sha`, `final_files` et `probes` du reçu. Il est enregistré **après** la publication dans main : son SHA de publication est antérieur, ce qui évite une empreinte Git autoréférente. Chaque probe HTTPS retourne HTTP 200 et des octets correspondant à son SHA256 (limite 16 Mio). Adapter les URL aux vraies pages publiées. Une preuve provisoire, des rapports seuls, une PR ouverte ou une reconstruction locale ne ferment rien. Les réserves bloquantes doivent être réellement résolues et les figures effectivement contrôlées selon leur provenance et licence.

Un lot suivant peut commencer seulement après les sept clôtures du précédent, revérifiées sur main. Une régression d'une preuve déjà comptée bloque la campagne. Les 77 codes sont recomptés sans ajouter le premier lot une seconde fois.

## Fin et images

Après 77 clôtures, chacune avec sa preuve figures réelle `complete: true`, `status: "passed"`, `pending: []`, et les éventuels reçus complémentaires `image_tasks_done` vérifiés dans main (`{path, sha256}` pointant vers des JSON avec `owner: "Codex", complete: true`), l'état passe à `STOPPED`, `campaign_execution_enabled: false`, `image_execution_enabled: false`. Aucun historique, image, cache ou outil n'est supprimé. Le finder indépendant doit lire ce drapeau avant ses tâches ; le drapeau seul n'arrête pas un finder qui ne le consulte pas. Ce branchement est un prérequis d'activation de l'arrêt effectif des recherches.

Validation locale : `python3 -m unittest discover -s tests -p test_starter_codex.py -v`. Les tests utilisent des dépôts temporaires et ne lancent aucune IA ni audit réel.


## Durcissement de la clôture

`closure.json` doit porter `medical_human_validation: false` et `alpha_receipt: {"path": "organisation/alpha-publications/Codex/CODE/0001.json", "sha256": "SHA256_REEL"}`. Le reçu doit appartenir aux chemins approuvés de la mission source `INTEGRATE`, porter son ID, le bon code, `actor: "Codex"`, `phase: "completed"` et `medical_human_validation: false`. Ses `files` doivent donner exactement les empreintes de `final_files`. Un reçu provisoire est refusé.

Les sept chemins obligatoires sont `chapters/CODE/CODE_{a,b,c,d,pop1,pop2}.html` et `glossary/code.py` en minuscules pour le glossaire. Les seuls compléments autorisés sont les assets propres `assets/img/code/alpha/codex/`. Un fichier d'un autre cours ou un inventaire incomplet est refusé.

Les rapports `reports.MED/LANG` pointent vers les **JSON finaux réels**, dans le dossier de la mission source `INTEGRATE`. Les références doivent être identiques à `alpha_receipt.audits.MED/LANG`, et les octets doivent exister à l'identique dans le `source_commit` du reçu Alpha. Chaque JSON exige `actor`, `code`, `kind`, `status: "closed"`, `medical_human_validation: false`, `reviewed_files_sha256` exactement égal à `final_files`, `unresolved_blockers: []`, `findings` et une liste `evidence` non vide. Chaque constat est `resolved` ou `non_blocking` avec preuve. Les métadonnées externes seules ne remplacent jamais ce JSON réel.

La preuve figures est également un JSON dans le dossier source propre, avec `actor: "Codex"`, le code, `status: "passed"`, `reviewed_files_sha256`, `medical_human_validation: false` et `evidence` non vide. Les preuves narratives et les sources réellement examinées doivent être liées aux JSON ; renseigner des champs ne constitue pas un contrôle médical.

## Reprise CLI explicite dans la même session

Un ouvrier CLI qui termine proprement mais a encore du travail peut demander au plus trois reprises **de sa session exacte**, avec les mêmes worktrees. Avant de terminer avec succès il écrit `docs/collaboration/ssp-v2/execution/<COORD-ID>/continuation.json` dans son worktree :

```json
{"schema_version":1,"status":"resumable","coordinator_mission":"COORD-ID","batch":0,"thread_id":"ID_REEL","turn_complete":true,"resume_number":1,"remaining_codes":["I63"],"reason":"Travaux restants explicitement décrits"}
```

`remaining_codes` doit être exactement la liste ordonnée des leçons encore ouvertes, `resume_number` le numéro suivant. Retour non nul, thread inconnu, divergence de reçu, crash ou ambiguïté interdisent la reprise automatique. Le contrôleur publie un nouvel intent CAS puis exécute `codex exec resume ID_REEL`, sans nouvelle session. La durée est bornée par tour et le nombre total de reprises à trois. Aucune répétition silencieuse d'une session neuve.

## Handoff natif réel et limite d'authentification

Le test réel du CLI du 15 octobre a échoué au rafraîchissement du jeton ; `login status` seul ne prouve pas qu'un appel modèle fonctionne. La configuration peut sélectionner `worker_backend: "native_handoff"` pour utiliser la session gérée réelle. Le moteur prépare le worktree et publie `NATIVE_REQUESTED`, un `request_id`, l'empreinte du prompt et le prompt dans `state.handoff`, sans lancer le CLI ni prétendre démarrer une IA.

Le coordinateur racine démarre ou reprend explicitement un agent géré puis lui fournit la demande. Cet agent attache le nonce unique avant tout travail :

```sh
python3 tools/starter_codex.py --root /chemin/depot attach-native --request-id NONCE --agent-id IDENTIFIANT_AGENT
python3 tools/starter_codex.py --root /chemin/depot complete-native --request-id NONCE --agent-id IDENTIFIANT_AGENT
```

L'attachement passe par CAS de `NATIVE_REQUESTED` à `NATIVE_RUNNING` ; un nonce faux ou un second attachement est rejeté. L'identifiant est déclaratif, pas une authentification supplémentaire. `complete-native` exige le même agent et revérifie les sept clôtures ainsi que les précédentes avant `IDLE`. Le prochain `tick` prépare le lot suivant ; le même agent géré peut prendre ce nouveau nonce dans son nouveau worktree. Les ticks sur une demande ou un agent en cours ne lancent aucun doublon. L'orchestration native dépend du coordinateur géré actif ; aucune permanence hors de ce runtime n'est promise.


## Publication Pages et sémiologie — exigence actuelle

Le reçu de publication doit aussi porter `publication.run_id`. Le moteur vérifie via GitHub API que ce run appartient au dépôt `vialdjoukang-spec/Medina`, au workflow `.github/workflows/pages.yml` (ID 368800567), à la branche main, au SHA exact `publication.main_sha`, avec état terminé et conclusion succès. Les probes et leur réponse finale ne peuvent viser que `https://vialdjoukang-spec.github.io/Medina/MEDINA.html` ou le frontend propre du fragment sous `Medina/fragments/MEDINA_<fragment>_<slug>.html`. Une redirection ou un site arbitraire est refusé. La preuve doit donc relier les sources finales à une publication Pages effectivement réussie, puis aux octets publics.

Toutes les leçons, y compris les sept actuelles, doivent désormais apporter la sémiologie fondamentale et analytique dans l'onglet sciences fondamentales, selon le modèle Cardiologie sans modifier la Cardiologie. Les anciens audits inchangés restent conservés ; ils ne dispensent pas de l'audit final réel du nouveau contenu. Chaque JSON MED/LANG final déclare `requirements_reviewed.fundamental_analytical_semiology: true` et lie ses empreintes de sources de départ et de fichiers finaux au reçu Alpha.

`closure.requirement_evidence.semiology` est une référence `{path, sha256}` **strictement identique** à `alpha_receipt.audits.SEMIO`. Le JSON SEMIO réel est dans la mission source propre et au même contrat que les audits : `kind: "SEMIO"`, `requirement: "fundamental_analytical_semiology"`, `status: "closed"`, code, acteur Codex, absence de validation médicale humaine, `source_files_sha256`, `reviewed_files_sha256`, aucune réserve bloquante, constats résolus/non bloquants et preuves réelles. Il porte aussi `tab_id: "code-s-semio"` et `source_path: "chapters/CODE/CODE_c.html"`.

Dans `_c.html`, le moteur analyse réellement le HTML : le panneau pS contient au moins six boutons locaux `data-s`, dont le bouton `role="tab"`, `id="code-tab-semio"`, `aria-controls="code-s-semio"`, `data-s="code-s-semio"`, intitulé exactement « Sémiologie fondamentale et analytique ». Son panneau `div.sci#code-s-semio` est dans pS et porte `aria-labelledby="code-tab-semio"`.

Ce panneau contient neuf sections `.ilot`, chacune avec un h3 non vide et du texte réel au-delà du titre : `data-semiology="normal|signs|mechanisms|examination|interpretation|differentials|urgency|limits|sources"`. La section sources comporte des références HTTPS liées. La section limites couvre notamment le contexte suisse et les populations particulières, à contrôler médicalement dans l'audit. Le moteur n'invente aucun seuil de mots comme preuve de qualité médicale. Il vérifie aussi un marqueur `data-semiology-clinical="CODE"` avec un contenu réel dans le panneau pathologie pA des sources `_a.html`/`_b.html`. Les liens causaux, signes discriminants, techniques d'examen et citations nécessitent une revue effective ; les marqueurs seuls ne constituent pas une validation.

Le total des 77 preuves figures complètes, sans attente et liées aux sources finales, suffit au gate terminal images. Des reçus `image_tasks_done` peuvent renforcer ces preuves, mais aucun hash futur inconnaissable n'est obligatoire dans la configuration de départ. Les actions `attach-native` et `complete-native` vérifient désormais aussi l'empreinte de configuration figée : une modification pendant un lot ne peut substituer la file ou ses preuves.


Configuration livrée : backend natif, 77 codes approuvés, onze lots de sept, pause de 90 secondes. Les 25 reçus de production sont attendus dans le dossier de leur mission `INTEGRATE` sous `production.json` ; aucun reçu futur n'est présenté comme déjà réalisé. Les premiers rapports sont adoptés puis actualisés pour la nouvelle exigence de sémiologie. Vérifications de cette livraison : 19 tests Starter et 13 tests finder réussis localement, sans lancement d'IA ni appel réel supplémentaire aux fournisseurs.
