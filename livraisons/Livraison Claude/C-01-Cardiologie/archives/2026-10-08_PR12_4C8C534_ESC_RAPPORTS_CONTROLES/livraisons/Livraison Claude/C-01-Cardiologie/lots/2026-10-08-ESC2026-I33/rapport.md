# Lot ESC 2026 — I33 — Endocardite infectieuse (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I33/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I33/I33_b.html` | remplacement | `dd5aea957d409ee1` | `d58621760354fe07` |
| `chapters/I33/I33_pop2.html` | remplacement | `d56b33dbb981b147` | `f04bea3a6ff6f452` |
| `chapters/I33/I33_pop_esc_comparison.html` | add | `—` | `e4f66102035ac962` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- « La CIM-11 attribue à l’embolie coronaire une extension de code propre » : codes seulement proposés et en cours d’examen dans la cinquième définition ; retiré.
- Classe IIb de l’enveloppe attribuée à des « données observationnelles et modélisations » : l’essai WRAP-IT (population générale, sans modification d’effet selon la fonction rénale) y contribue ; reformulé.

Réserves :
- Cinquième définition : document de consensus, non recommandation au sens strict.

## Levée des réserves de l'audit croisé de Codex

`travail/esc2026/LEVEE_RESERVES.json` (extrait pour I33) : `{"date": null, "auteur": null, "audit_source": null, "provenance": null, "MED-01": null, "MED-02": null, "MED-03": null, "I42": null, "I35": null, "tests": null, "non_fait": null}`

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I33             # OK
verifier_sigles.py I33 chapters/I33/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I33                      # OK
node tests/verify_course_native.cjs I33      # 2997 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i33_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
