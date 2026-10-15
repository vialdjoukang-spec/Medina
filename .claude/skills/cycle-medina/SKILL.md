---
name: cycle-medina
description: Produire, auditer, injecter et publier un cycle MEDINA (4 leçons de la tétrade, plan organisation/plan_tetrade_30_cycles.json) avec la garde tools/cycle_claude.py. Usage /cycle-medina <n>.
---
# Cycle MEDINA n — chaîne économe (décision de Vial, 14.10.2026)

## Séquence 1–30 : lots Novo_TÉTRADE de douze (15 octobre 2026)

Lire `docs/collaboration/instructions/NOVO12_EXECUTION_VIAL_2026-10-15.md`.
Le cycle actif historique (notamment le 3) n'est pas migré. Après sa clôture réelle :
`python3 tools/cycle_claude_stage.py novo 1 --runtime ID_REEL` ouvre ensemble les
douze leçons des cycles 4–6 ; les lots suivants couvrent 7–9, puis 10–12, etc.
Ce plan est `organisation/novo_12/PLAN_NOVO_12.json` (108 leçons), **pas** le plan
`organisation/progression/plan-novo12.json` de l'autre session (cycles 42+).

Claude et chaque agent lisent d'abord le Prompt de vérité à vingt rubriques.
Chaque dossier garde `recherche.md` et `sources.json` ; porte `betta_verite.py`
avant rédaction. Les relevés utilisent `claude_cycle_gate.py --prompts novo`.
Dans leurs deux relevés auteur, rattacher les deux fichiers par deux
`--check sources_lues CHEMIN EXPLICATION` : leurs empreintes restent figées.
Les sous-cycles individuels gardent leurs dossiers `CYCLE_nn_CODE`, numéros et
auteurs. Préparer un cahier d'aperçu à quatre leçons par sous-cycle pour `--cahier`.

Après contrôle réel et quatre captures par leçon, les douze doivent être prêtes.
Le coordinateur peut injecter un préfixe consécutif (jusqu'aux douze) sur leurs
empreintes exactes, un reçu chacune, puis publier ce lot en un seul déploiement.
Chaque reçu public lie `site_manifest` au `publication.json` réellement téléchargé,
`pages_run` (id, head_sha, conclusion), `published_files` aux sources et images
contrôlées, la date de relecture et `public_images_http_200`. Relire les douze
leçons et leurs jauges ; clôturer seulement après leurs douze `PUBLIE_VERIFIE`.
Les audits croisés/contre-audits restent suspendus, pas les sources ni les
contrôles techniques. L'ancien script `claude_chaine_main.sh` ne doit pas être rejoué.

Les étapes historiques ci-dessous restent le protocole des cycles à quatre.

**Cycles 3 à 30 : recherche Opus effort élevé → rédaction Sonnet effort moyen → contrôle technique + 4 captures → publication directe. Étapes 3 et 4 (audits) différées après le Cycle 30** (`docs/collaboration/instructions/CYCLES_03_30_PUBLICATION_DIRECTE_VIAL_2026-10-14.md`). Interdit de rédiger faux.

Règle de Vial (14.10.2026) : Opus moyen→élevé → Sonnet moyen → Opus faible ; mécanique Sonnet moyen.
Principe : **recherche initiale exhaustive** (coûteuse une fois) → rédaction et audits **bon marché** fondés sur le dossier de sources.
Rapports au propriétaire : uniquement « captures + FIN PUBLIÉ + lien ». Aucun compte rendu intermédiaire.

| Étape | Modèle (Agent `model`) | Effort | Sortie |
|---|---|---|---|
| 1 Recherche | opus | medium (high seulement si insuffisant, jamais plus) | `livraisons/Livraison Claude/<FRAG>/travail/CYCLE_nn_<CODE>/preuves/dossier_sources.json` : chaque décision clé (doses FI Swissmedic du produit exact, seuils, critères, classifications, différentiels SSP par gravité, sous-codes CIM-10-GM, images Commons via `tools/images_ouvertes.py`) avec URL, date, section, passage, SHA du texte lu |
| 2 Rédaction | sonnet | medium | 7 sources (4 onglets, pop1, pop2, glossaire) **uniquement** depuis le dossier ; `source_ledger_claude.json`, `images_claude.json`, preuve auteur |
| 3 Audit croisé (binômes NEUR↔HEM, ENDO↔NEPH) | opus | low | grille `audit_moteur` ci-dessous ; passe 1 → corrections auteur (SendMessage au même agent) → passe 2 |
| 4 Contre-audit (4 agents neufs) | opus | low | même grille, contexte neuf, `fresh_context:true` |
| 5 Mécanique (gates, manifestes, stage, images) | sonnet | medium | `tools/claude_cycle_gate.py`, `tools/cycle_claude_stage.py` |
| 6 Contrôle + injection + publication | coordinateur | — | contrôle navigateur, **4 captures/leçon** (ouverture, fenêtre, figure, tableau), injection G→E→N→D une à une, PR, fusion, relecture publique |

## Moteur d'audit (Prompt de vérité, adapté à la leçon)
Scripts d'abord (zéro token) : `python3 test_v7.py --static <CODE>`, contrôle navigateur, garde `python3 tools/espace.py garde`.
Puis l'agent ne vérifie que ce qu'un script ne voit pas, contre le **dossier de sources** :
1. ≥ 10 chiffres (doses, seuils, critères) = passage du dossier (sinon relecture primaire ciblée).
2. Contre-indications, interactions, surveillance des FI suisses présentes.
3. Différentiels SSP : gravité → fréquence, discriminant, examen décisif.
4. Langue : phrases complètes, connecteurs, aucune phrase sur la fabrication du cours, calculs expliqués.
5. Images réelles conformes à la légende (Read), licences ouvertes, schémas « Schéma didactique ».
6. Dernier îlot : critères formels (`div.alert`) puis paramètres clés (`div.key`) ; Pareto.
Format des passes et reçus : `organisation/execution-20261014/CONTRAT_REVUES.md`.

## Règles fixes
Sources suisses puis européennes, aucune recommandation américaine décisionnelle ; aucune invention ; revue IA ≠ validation humaine ;
un seul cycle actif pour Claude ; autorité `docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md`.
Encre `#0f2c66`. Ni force-push, ni garde désactivée. Commit après chaque étape.
