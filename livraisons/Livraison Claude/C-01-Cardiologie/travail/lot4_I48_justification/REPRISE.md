# Lot 4 — justification systématique de I48 (cours pilote) : terminé

État au 7 octobre 2026. Le lot est livré sur `claude/loving-shannon-spwrhc`. Le [rapport](../../archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/rapport.md) donne les chiffres, les corrections et les réserves.

## Contenu du dossier

| Fichier | Rôle |
| --- | --- |
| `items_I48_*.json` | Inventaire des 505 affirmations |
| `resultats_partiels.json` | Plans, fusion en 53 fenêtres et 27 brouillons de la session interrompue |
| `resultats/jobs/` | Plan de chaque fenêtre, avec ses ancres |
| `resultats/out/` | Fenêtres finales (`.html`), vérification (`.json`) et contre-vérification (`.contreverif.json`) |
| `resultats/inline/`, `resultats/inline_out/` | Compléments proposés et verdicts du vérificateur |
| `resultats/*.md` | Consignes données aux agents (rédaction, vérification, contre-vérification) |
| `appliquer_lot4.py` | Application centrale, à blanc puis avec `--ecrire` |
| `workflow_justification.js` | Script du workflow initial (inventaire, plan, fusion) |

## Pour étendre la méthode à un autre cours

1. Inventaire des affirmations sans mécanisme, puis plan par fichier et fusion des thèmes en fenêtres.
2. Rédaction, vérification, puis **contre-vérification indépendante** de chaque fenêtre : dans I48, elle a encore corrigé sept erreurs de fond dans onze fenêtres déjà vérifiées.
3. Vérification un à un des compléments du texte.
4. Application par un script adapté de `appliquer_lot4.py`, d'abord à blanc.
5. Retrait des initiales d'auteurs dans les rubriques Source, que l'audit lit comme des sigles ; ajout au glossaire des noms d'essais nouveaux.
6. Contrôles : `test_v7.py --static`, build, `audit_fragments`, `audit_sciences`, `verify_sciences_cs.cjs`, `verify_s01_browser.cjs`, `check-claude`.

Le texte intégral de l'ESC 2024 sur la FA s'obtient avec `curl -sSL -o esc2024.pdf https://forening.sls.se/media/kfyncecr/2024-esc-guidelines.pdf`, puis `pdftotext -layout`. Pour les autres cours, il faut se procurer les recommandations propres à chaque maladie.
