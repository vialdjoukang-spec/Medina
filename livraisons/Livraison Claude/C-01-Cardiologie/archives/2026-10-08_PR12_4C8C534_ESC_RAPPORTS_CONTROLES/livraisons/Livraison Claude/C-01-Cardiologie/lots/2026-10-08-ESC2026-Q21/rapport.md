# Lot ESC 2026 — Q21 — Cardiopathies congénitales de l’adulte (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/Q21/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/Q21/Q21_a.html` | remplacement | `c587dd51051198c4` | `c155a1f8d4c5dddb` |
| `chapters/Q21/Q21_b.html` | remplacement | `b4ca685cf9881e61` | `78367ae0b907724f` |
| `chapters/Q21/Q21_pop_esc_comparison.html` | add | `—` | `0e4f79a3874ad45e` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- Causalité non démontrée : l’hypertension, le diabète et l’obésité étaient présentés comme expliquant le risque d’insuffisance cardiaque multiplié par huit ; ce chiffre est un risque relatif global par rapport à des témoins (section 4.1.4.8). Reformulé.
- Ancres sans champ « new » et labels hors libellé « ESC 2026 : … » : réécrites.

Réserves :
- Aucune indication 2026 propre au Fontan, au ventricule droit systémique ni aux cardiopathies cyanogènes.

## Levée des réserves de l'audit croisé de Codex

`travail/esc2026/LEVEE_RESERVES.json` (extrait pour Q21) : `{"date": null, "auteur": null, "audit_source": null, "provenance": null, "MED-01": null, "MED-02": null, "MED-03": null, "I42": null, "I35": null, "tests": null, "non_fait": null}`

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static Q21             # OK
verifier_sigles.py Q21 chapters/Q21/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py Q21                      # OK
node tests/verify_course_native.cjs Q21      # 3947 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/q21_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
