---
name: agent-distributor
description: Distribue les agents MEDINA par leçon (1re ligne), déploie 1 renfort (2e ligne) puis 2 (3e ligne) quand une leçon prend du retard, sur alerte de tools/distributor_veille.py. Usage /agent-distributor [état|déployer].
---
# Agent distributor — Projet Novo_12 (Vial, 15.10.2026)

## Trois lignes
| Ligne | Quand | Agents par leçon | Modèle |
|---|---|---|---|
| 1re | toujours, au lancement | 1 agent titulaire (recherche puis rédaction) | recherche Opus effort moyen ; rédaction Sonnet effort moyen |
| 2e | retard ≥ seuil 1 | +1 renfort | Sonnet effort moyen |
| 3e | retard ≥ seuil 2 | +1 renfort (2 au total) | Sonnet effort faible |

Leçon dans les temps : **aucun renfort**. Jamais plus de 2 renforts par leçon.

## Seuils de retard (sans sortie attendue)
| Étape | Sortie attendue | Seuil 1 | Seuil 2 |
|---|---|---|---|
| Recherche | `preuves/dossier_sources.json` | 45 min | 75 min |
| Rédaction | les 7 sources + `preuves/source_ledger_claude.json` | 35 min | 55 min |

## Un renfort ne réécrit jamais le travail du titulaire (un auteur par fichier)
Il prend une part **séparée**, dans le même dossier `CYCLE_nn_CODE/` :
- **Recherche** : renfort 1 → FI Swissmedic du produit exact (`preuves/renfort_fi.json`) ; renfort 2 → images ouvertes, une à la fois, pause 20 s (`assets/img/…`, `preuves/renfort_images.json`). Le titulaire fusionne.
- **Rédaction** : renfort 1 → `{CODE}_pop1.html` et `{CODE}_pop2.html` (fenêtres) ; renfort 2 → `glossary/{code}.py` et `preuves/images_claude.json`. Le titulaire garde les onglets a–d et le registre.
- Prévenir le titulaire (SendMessage) de la part retirée, pour qu'il ne l'écrive pas.

## Veille agressive
`tools/distributor_veille.py --boucle 300` lit `$DISTRIB_ROSTER` (registre des leçons en cours : code, dossier, étape, début, renforts déjà déployés). Tant que tout est dans les temps : aucun jeton consommé. Dès qu'une leçon franchit un seuil : la veille s'arrête et imprime l'action (« RENFORT 1 G40 rédaction ») ; le coordinateur déploie aussitôt l'agent, met à jour le registre (`renforts`) et relance la veille.
Règles fixes : sources lues seulement, aucune invention, revue IA sans validation médicale humaine, aucune commande git par les agents.
