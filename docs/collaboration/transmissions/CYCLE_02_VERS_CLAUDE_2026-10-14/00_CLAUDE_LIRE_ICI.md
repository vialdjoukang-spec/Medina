# MEDINA — CYCLE 2 : TRANSMISSION FORMELLE À CLAUDE

**À lire en premier.** Ordre direct de Vial, 14 octobre 2026, 22 h 29 (Europe/Zurich) : le travail de préparation doit être entièrement accessible sur GitHub. **Claude prend la suite : audit exigeant, corrections, injections et création de la pull request.** Le transmetteur s'arrête après cette remise. Aucun démarrage de Cycle 3.

## Identités exactes

Dépôt : `vialdjoukang-spec/Medina`.
Branche de remise (consultation/reprise) : `codex/cycle2-remise-claude-20261014`, issue de `codex/cycles-20261014-0800` au commit `030f30f76034b02428734e6b662da4aaea32e87e`.
`main` au constat : `c768557034ad17f515ebd3aed82c3c225b1da356`. Claude doit relire les têtes effectives avant chaque modification ; ces valeurs sont un point de comparaison, non un verrou perpétuel.
**Aucun cours du Cycle 2 n'a été injecté ni publié par cette transmission. Aucune PR n'est ouverte par le transmetteur.**

Cycle 2 : **G45 (AIT), E10 (diabète de type 1), N18 (maladie rénale chronique), D64 (autres anémies)**. Quatre cours, 21 parties chacun et 74 sous-codes au cahier ; 32 illustrations déjà présentes dans les brouillons, 9/9/8/6. Les images, les licences et le rendu final doivent être recontrôlés sur les versions corrigées.

## Où sont les travaux (tous dans cette branche)

- **G45** : `livraisons/Livraison Codex/N-05-Neurologie/travail/CYCLE_02_G45/`
- **E10** : `livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/travail/CYCLE_02_E10/`
- **N18** : `livraisons/Livraison Codex/N-07-Néphrologie/travail/CYCLE_02_N18/`
- **D64** : `livraisons/Livraison Codex/H-08-Hématologie/travail/CYCLE_02_D64/`
- **Cahier** : `organisation/execution-20261014/cahier-cycle2.json`
- **Rapports historiques de passe 1** : `docs/collaboration/reviews/2026-10-14/CYCLE_02/cross/{G45,E10,N18,D64}/`
- **Registre d'exécution historique** : `organisation/execution-20261014/status.json`
- **Contrat de relecture** : `organisation/execution-20261014/CONTRAT_REVUES.md`
- **Ancien script des corrections préparatoires** : `tools/cycle2_reprise_01_safety.py`
- **Workflow de cet ancien script** : `.github/workflows/cycle2-reprise-corrections.yml`
- **Proposal G45-R1/R3, conservée ici distincte des autres corrections** : `docs/collaboration/transmissions/CYCLE_02_VERS_CLAUDE_2026-10-14/G45_R1_R3_PROPOSITION.json`
- **Inventaire localisé des 25 réserves** : `docs/collaboration/transmissions/CYCLE_02_VERS_CLAUDE_2026-10-14/01_RESERVES_A_RESORBER.md`
- **Méthode opérationnelle confiée à Claude** : `docs/collaboration/transmissions/CYCLE_02_VERS_CLAUDE_2026-10-14/02_MISSION_CLAUDE_AUDIT_INJECTION_PR.md`
- **Traçabilité et limites de preuve** : `docs/collaboration/transmissions/CYCLE_02_VERS_CLAUDE_2026-10-14/03_PREUVES_ET_INCIDENT_TECHNIQUE.md`

La chaîne `tools/cycle2_reprise_01_safety.py` a été exécutée **une fois en CI** le 14.10 à 20:17 UTC : 16 modifications dans 8 fichiers **dans l'espace temporaire du runner**, puis échec du contrôle de chemin (`?? docs/collaboration/reprises/`). **Les tests suivants, le commit et le push ont été sautés. Aucune des 16 modifications n'est enregistrée par cette exécution.** L'ancien workflow ne doit pas être pris pour une injection réussie. Détails dans le document 03.

## Préséance, propriété et séquencement

Le présent transfert constitue une nouvelle instruction de reprise **du seul Cycle 2**, après expiration de l'exécuteur nocturne prévu jusqu'à 08 h 00. Conserver ce dernier document historique sans prétendre que son exécution serait toujours active. Le transfert de responsabilité à **Claude** remplace, pour ce cycle, la responsabilité Codex historique. Les règles scientifiques, les revues indépendantes, les gardes et la protection des sources canoniques restent intégrales.

**Claude audite lui-même, fait corriger/complète, exerce le contrôle final, prépare et crée sa PR, obtient une intégration autorisée, puis vérifie le rendu public.** Il peut utiliser des agents réellement indépendants lorsqu'ils sont disponibles, dans la limite du protocole. La création de ce dossier et d'une issue ne démarre pas un processus autonome dans Claude Code ; elle rend la mission explicitement consultable et exécutable.

### STOP du transmetteur

Aucune retouche des cours canoniques, injection, merge, déploiement ou PR par le transmetteur. La branche et l'issue constituent la remise. Après celle-ci, **Claude est l'unique responsable de la suite** ; ne pas commencer le Cycle 3.
