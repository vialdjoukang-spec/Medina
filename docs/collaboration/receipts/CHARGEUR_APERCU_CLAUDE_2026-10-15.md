# Chargeur de publication et aperçu isolé — 15 octobre 2026

## Demande et périmètre

Signalement original Claude : https://github.com/vialdjoukang-spec/Medina/pull/100#issuecomment-6193528466
La branche de la première séquence est `claude/vibrant-johnson-7k5okg` ; le
commentaire évaluait la tête Codex `b4f2d641c281f7b9ae29b5cdf8b8f90ab79b25b8`.
Main de départ de cette extraction : `75500d40543cadeafe3bcea97ca074c4c6afed3a`.
Correctif de l'aperçu : commit local `a5a64e696a5cbf98d2d36272ef99059873b1db44`.

Cette petite proposition ne reprend pas le raccord Novo, les compteurs, les
attributions ou les autres réparations de PR100. Aucun cours, glossaire
canonique, registre médical, preuve auteur ou statut n'est modifié.

## Cause, correction et prévention

1. Le chargement historique des glossaires redécouvrait récursivement tous les
   modules : Claude confirmait un timeout de publication (code124). Le chargeur
   central remplace seulement les boucles historiques exactement reconnues par
   AST, conserve l'ordre des modules ordinaires et l'arbitrage final, puis ajoute
   les clés conditionnelles sans écrasement. Un schéma dynamique inconnu échoue
   explicitement ; les 180 sources restent intactes.
2. L'aperçu isolé utilisait un wrapper généré `exec(compile(...))`, refusé par ce
   chargeur. Il utilise maintenant un manifeste JSON de fichiers locaux et
   d'empreintes SHA-256. Les octets vérifiés sont ceux compilés ; le rejeu explicite
   rend aux définitions internes leur priorité, sans autoriser arbitrairement
   l'exécution selon un nom de fichier. Chemins traversants, doublons, liens
   symboliques et empreintes incorrectes sont refusés.
3. La CI dédiée exécute les deux modules de régression, dont la compilation
   réellement défaillante, puis la suite technique complète sur un clone GitHub.
   Elle ne remplace ni les contrôles navigateur ni une validation médicale.

## Contrôles exécutés avant publication de la branche

- `python3 -m unittest tests.test_glossary_loader tests.test_fragment_work_preview` :
  **45 tests réussis en12,521s**, dont compilation réelle A41/B24, priorités
  internes SOFA/VIH, isolation/atomicité et refus de manifestes invalides.
- Import global : **4488 clés en0,552s** ; aucune réécriture des glossaires.
- `py_compile` des trois outils et `git diff --check` réussis.
- Scénario single-chapter commun à night_preview vérifié via
  `create_overlay + load_glossary` ; commande complète night_preview non exécutée.
- Sur la proposition large, `tools/claude_cycle_gate.py` conserve exactement
  `3706186994503073a18d67ef52f11f63a4e05f7917813cb72e0523ef6a136ee6`.
  Le refus N04 a déjà disparu à
  `966fc8c17354f6f651542654ee23980e86a877bc` :
  https://github.com/vialdjoukang-spec/Medina/actions/runs/38744350662.
  Cette petite extraction ne touche pas ce fichier ni les preuves Cycle3.

La suite complète de la nouvelle tête distante et sa CI doivent être vérifiées
sur leur SHA exact. Aucun navigateur ordinateur/mobile exécuté ici :
Chromium indisponible et téléchargement tronqué. Aucun déploiement de cette
proposition annoncé. Les audits médicaux indépendants restent suspendus ;
aucune relecture clinique n'est revendiquée. Claude conserve sa décision de
vérification et d'intégration.

## Empreintes des fichiers techniques proposés

| Chemin | SHA-256 |
| --- | --- |
| `build_medina.py` | `48807a3e2f04eb8afc7b3de714fb652d07e1e30217163b2d07f89931179cce87` |
| `tools/glossary_loader.py` | `ad495be510bd161123266feb6a1447cf6b588666038c3e59cb1de7b398d93b2f` |
| `tools/build_fragment_work_preview.py` | `7ee5744b32e849c10653b5bb6df21a140fb226eb24a45185b0952dbc10c56ec0` |
| `tests/test_glossary_loader.py` | `06e1cd63f0a761919d35729012ba69f09a9643e0768d2d2698fbe118ebd6aa21` |
| `tests/test_fragment_work_preview.py` | `14e0c295c9bc07341beecea840ce89d4fe0eea87b685baa61efbfe9cdf222c71` |
| `.github/workflows/glossary-loader.yml` | `64a92473b537a69772014c3440d0442e799bc745c8d0eb1829b7f14ef496f34b` |

