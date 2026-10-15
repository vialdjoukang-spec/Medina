# Jauge d’audit Codex

La jauge distingue les rapports poussés et les leçons réellement clôturées. Elle concerne uniquement les77leçons de la file Codex, par11lots de7. Aucun cours Claude n’entre dans ses compteurs et aucune clôture IA ne vaut validation médicale humaine.

## Calcul depuis les preuves réelles

`tools/audit_gauge.py` lit la configuration et les manifests de missions dans le `main` distant. Le lot courant provient du champ `batch` (0à10) de la branche `medina/7-starter-codex`. Pour ses sept codes, le script utilise les missions MED/LANG configurées et leur branche exacte déclarée par le manifest dans `main`. Chaque mission compte au plus un rapport commité et poussé `rapport*.md` ou `rapport*.json`, placé directement dans son dossier d’exécution. Les fichiers vides, JSON vides ou invalides, preuves seules et brouillons non commités ne comptent pas.

Le script examine les clôtures déclarées par l’état distant **et** les reçus de clôture des sept codes courants présents dans `main`, même si un travail natif n’a pas encore actualisé `state.closed`. Chaque candidat passe le moteur strict `Repository.closure_proof` ou `Repository.closure`, avec le moteur local identique à celui du `main` distant. Un champ `complete` isolé ou une déclaration d’état ne suffit jamais. La barre représente les clôtures du lot. TOTAL additionne seulement les clôtures vérifiées. SEMIO compte ici les clôtures du lot dont le moteur a également vérifié l’exigence sémiologique ; il ne prétend pas compter les travaux sémiologiques intermédiaires.

Pour la seule commande exacte `gh api repos/vialdjoukang-spec/Medina/actions/runs/<entier positif>`, le module de vérification reçoit un transport HTTPS public en lecture vers `api.github.com`, sans jeton ni secret, avec timeout15secondes, taille bornée et redirections refusées. Les autres commandes gardent leur transport original. Le fichier du moteur doit toujours être identique à `main` et sa méthode `pages_run` reste inchangée : dépôt, workflow, SHA, branche et succès doivent tous correspondre. Une erreur HTTP/authentification ou un workflow échoué ne produit jamais de clôture validée.

Les lectures réseau utilisent Git ; la vérification stricte d’une clôture peut aussi consulter GitHub et les preuves de publication selon le moteur Starter. Aucun push, modification de sources ou téléchargement d’image n’est effectué. Des objets Git et un cache local peuvent être actualisés. Une preuve non vérifiable ne compte pas ; si la configuration distante manque ou ne peut être lue, le calcul échoue sans publier de compteurs supposés. Les erreurs de clôture figurent dans la sortie JSON et ajoutent « vérification incomplète » à la ligne : un échec réseau ou d’authentification ne prouve pas une absence de clôture.

## Usage et validation du brouillon

Depuis le dépôt :

```bash
python3 tools/audit_gauge.py --fresh
python3 tools/audit_gauge.py --format json
python3 tools/audit_gauge.py --fresh --update-output /tmp/medina-gauge-receipt.json
python3 tools/audit_response_gate.py /tmp/reponse-finale.txt
```

Copier dans le brouillon réel la ligne exacte obtenue, y compris `[G:empreinte8:nonce8]`. Puis passer ce brouillon au validateur immédiatement avant l’envoi, après la dernière action qui pourrait changer l’état. Il refuse une jauge absente, différente, ambiguë, un jeton incorrect et un instantané vieux de30secondes ou plus. Si le calcul a expiré, recalculer puis remplacer la ligne et revalider. Le validateur retourne0 en cas d’accord et2 sinon. Il accepte aussi le texte brut sur stdin avec le chemin `-`.

`--root` choisit le dépôt ; par défaut, c’est la racine au-dessus de `tools`. `--cache` choisit le cache local (TTL30secondes). `--update-output` écrit un reçu JSON hors du dépôt, en créant son dossier parent. `--local-snapshot` sert aux tests : il n’accorde jamais de clôture à une assertion du fichier. Ce mode ne remplace pas une collecte réelle et ne doit pas être utilisé pour une réponse de production.

## Hook Stop préparé et limites de l’interface

`.codex/hooks.json` contient un adaptateur au contrat documenté du hook Codex `Stop` : lecture JSON de `last_assistant_message` sur stdin et sortie JSON `decision: block` lorsqu’une preuve manque. Une entrée JSON invalide ou une collecte indisponible bloque également. `stop_hook_active` ne permet jamais de contourner le contrôle : un second passage invalide demande encore la réparation. Le script n’a aucune boucle interne ; pour éviter les continuations répétées, recalculer la jauge puis reprendre sa ligne exacte comme dernière action avant validation.

Cette configuration est **préparée, pas déclarée activée dans ce chat**. La documentation primaire [Codex Hooks](https://learn.chatgpt.com/docs/hooks) précise que ChatGPT Work Cloud sans orchestration locale ou personnelle n’exécute pas les command hooks. Sur un hôte Codex compatible, les hooks non gérés nécessitent la revue et l’approbation de confiance de l’utilisateur via `/hooks`. Ne pas modifier les empreintes de confiance et ne pas contourner cette revue. Le test direct de l’adaptateur prouve son comportement de programme, pas son exécution par une interface donnée.

Test direct sans preuve, attendu : une décision `block` :

```bash
printf '%s' '{"hook_event_name":"Stop","stop_hook_active":false,"last_assistant_message":"Réponse sans jauge"}' | python3 tools/audit_response_gate.py --stop-hook
```

Aucune API de statut fixe ou de ligne permanente n’est exposée dans cette interface. La jauge apparaît dans les réponses finales de coordination selon `AGENTS.md` ; aucun statut permanent ni surveillance entre sessions n’est annoncé.

## Vérification

```bash
python3 -m unittest discover -s tests -p test_audit_gauge.py
```

Les tests couvrent notamment les rapports sans clôture, faux reçus, clôture partielle sans déclaration d’état, deuxième lot et branches de manifests, fichiers MD/JSON vides, empreintes altérées, preuves périmées et entrée Stop invalide. La validation native exhaustive reste celle du moteur Starter et de ses propres tests.
