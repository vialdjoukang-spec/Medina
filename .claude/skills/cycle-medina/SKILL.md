---
name: cycle-medina
description: Produire, auditer, injecter et publier un cycle MEDINA (4 leçons de la tétrade, plan organisation/plan_tetrade_30_cycles.json) avec la garde tools/cycle_claude.py. Usage /cycle-medina <n>.
---
# Cycle MEDINA n — chaîne économe (décision de Vial, 14.10.2026)

Principe : **recherche initiale exhaustive** (coûteuse une fois) → rédaction et audits **bon marché** fondés sur le dossier de sources.
Rapports au propriétaire : uniquement « captures + FIN PUBLIÉ + lien ». Aucun compte rendu intermédiaire.

| Étape | Modèle (Agent `model`) | Effort | Sortie |
|---|---|---|---|
| 1 Recherche | opus | high | `livraisons/Livraison Claude/<FRAG>/travail/CYCLE_nn_<CODE>/preuves/dossier_sources.json` : chaque décision clé (doses FI Swissmedic du produit exact, seuils, critères, classifications, différentiels SSP par gravité, sous-codes CIM-10-GM, images Commons via `tools/images_ouvertes.py`) avec URL, date, section, passage, SHA du texte lu |
| 2 Rédaction | sonnet | medium | 7 sources (4 onglets, pop1, pop2, glossaire) **uniquement** depuis le dossier ; `source_ledger_claude.json`, `images_claude.json`, preuve auteur |
| 3 Audit croisé (binômes NEUR↔HEM, ENDO↔NEPH, mêmes agents que les auteurs) | sonnet | low | grille `audit_moteur` ci-dessous ; passe 1 → corrections auteur (SendMessage au même agent) → passe 2 |
| 4 Contre-audit (4 agents neufs) | sonnet | low | même grille, contexte neuf, `fresh_context:true` |
| 5 Mécanique (gates, manifestes, stage) | haiku | low | `tools/claude_cycle_gate.py`, `tools/cycle_claude_stage.py` |
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
