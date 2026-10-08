# Lot ESC 2026 — I34 — Valvulopathies mitrales, tricuspides et pulmonaires (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I34/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I34/I34_b.html` | remplacement | `145bd19cdbc5b955` | `9abaf9829fcbc2bb` |
| `chapters/I34/I34_pop_esc_comparison.html` | add | `—` | `31fddabcf9803580` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- aucune

Réserves :
- Toutes les classes vérifiées : 2026 TEER I, B1 et IIb, C (tableau 17) ; 2025 I, A et IIb, B ; tricuspide 2025 IIa, A ; réadaptation IIa, B2 et IIb, B2 ; ESC 2021 IIa, B (tableau 6 de l’ESC 2026).
- Fiche I34_d : furosémide et spironolactone citent l’ESC 2021 (spironolactone inchangée en 2026).

## Levée des réserves de l'audit croisé de Codex

`travail/esc2026/LEVEE_RESERVES.json` (extrait pour I34) : `{"date": null, "auteur": null, "audit_source": null, "provenance": null, "MED-01": null, "MED-02": null, "MED-03": null, "I42": null, "I35": null, "tests": null, "non_fait": null}`

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I34             # OK
verifier_sigles.py I34 chapters/I34/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I34                      # OK
node tests/verify_course_native.cjs I34      # 4075 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i34_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
