# Lot ESC 2026 — I42 — Cardiomyopathies (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I42/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I42/I42_a.html` | remplacement | `b7d0bd707a66bdde` | `7dbf4f56ace86ae5` |
| `chapters/I42/I42_b.html` | remplacement | `9bb3db0bd27cfce9` | `6c86175e957d7a75` |
| `chapters/I42/I42_d.html` | remplacement | `f96f42ccf223c4e7` | `6051d21e7eb64112` |
| `chapters/I42/I42_pop2.html` | remplacement | `e3913844c5c2118e` | `a6b6f0a7e1030d84` |
| `chapters/I42/I42_pop5.html` | remplacement | `60fa151f6db2b722` | `e20d967904e06055` |
| `chapters/I42/I42_pop6.html` | remplacement | `84ece3298f6e0b8e` | `d4e6402a105c5090` |
| `chapters/I42/I42_pop_esc_comparison.html` | add | `—` | `c610391caa77dd14` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- Après fusion, la clé i42-esc-2026-comparaison existe déjà (fenêtre canonique Codex) : l’action « creer » aurait écrasé ou dupliqué la clé ; job converti en « completer » (fichier_cible I42_pop_esc_comparison), rubriques sans redite.
- Indication médicamenteuse à FEVG 45 % présentée sans la note e du tableau 5 (aucun grand essai randomisé limité à 41–49 %).
- Déduction « l’entraînement attend la réduction du gradient » et rappel de l’échocardiographie d’effort ESC 2023 : hors ESC 2026 et redite du cours ; retirés.

Réserves :
- La rubrique canonique de Codex « ne suffit pas à attribuer une nouvelle classe ESC 2026 » peut coexister ; les classes sont désormais lues dans le tableau.

## Levée des réserves de l'audit croisé de Codex

`travail/esc2026/LEVEE_RESERVES.json` (extrait pour I42) : `{"date": null, "auteur": null, "audit_source": null, "provenance": null, "MED-01": null, "MED-02": null, "MED-03": null, "I42": null, "I35": null, "tests": null, "non_fait": null}`

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I42             # OK
verifier_sigles.py I42 chapters/I42/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I42                      # OK
node tests/verify_course_native.cjs I42      # 3039 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i42_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.

**Particularité de `main` :** la fenêtre `i42-esc-2026-comparaison` n'existe pas sur `main`. Le lot la crée en reprenant le contenu de Codex (`83bff14:chapters/I42/I42_pop_esc_comparison.html`), suivi des rubriques de Claude. Voir `travail/esc2026/I42_variante_main/`.
