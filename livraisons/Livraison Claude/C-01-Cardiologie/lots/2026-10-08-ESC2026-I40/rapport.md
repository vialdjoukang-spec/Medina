# Lot ESC 2026 — I40 — Myocardites (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I40/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I40/I40_b.html` | remplacement | `7a5ab7c9a875e07e` | `2dae7b62d3f8499a` |
| `chapters/I40/I40_pop_esc_comparison.html` | add | `—` | `ca84f5b02d36d401` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- Biopsie 2026 décrite comme visant « toute insuffisance cardiaque d’origine incertaine » : surgénéralisation ; le tableau de recommandations 4 vise l’aggravation rapide malgré le traitement ou la suspicion d’inflammation, d’infiltration ou de surcharge non identifiable autrement.
- Arrêt progressif présenté sans sa condition : l’ESC 2026 le réserve à la préférence du patient (« to accommodate patient preference ») et le dit exceptionnel.

Réserves :
- Hors ESC 2026, non corrigé : I40_b « FEVG modérément réduite » pour 41–49 %, que l’ESC 2025 nomme « légèrement réduite » (mildly reduced).

## Levée des réserves de l'audit croisé de Codex

- **MED-01 (preuves reproductibles)** : statut global « levée côté producteur : chaque changement ESC 2026 est rattaché à une ligne de tableau citée (document, DOI, date, section, tableau, population, ligne, classe et niveau, notes, ligne antérieure comparée, provenance du fichier lu). Contrelecture indépendante de Codex à refaire au commit de remise. » ; accès primaire : Textes intégraux 2026 lus sur les extractions pdftotext locales des PDF de l’éditeur (tampon « by guest on 07 October 2026 », empreintes SHA-256 dans PROVENANCE.md), non versionnés. Accès automatisé à academic.oup.com refusé depuis cet environnement (HTTP 403, vérification anti-robot) ; ESC 2021 sur la stimulation relu sur PubMed Central (PMC13179788) ; ESC 2024 sur la fibrillation auriculaire relu sur le jeu de diapositives officiel de l’ESC.. Pour I40 : {"preuves": "livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I40/PREUVES.md", "changements_retires": []}.
- **Écart signalé « FEVG modérément réduite »** : l’expression est absente des sources I40 de `main` `315280c` (recherche dans tous les HTML de `chapters/I40/`). L’écart venait de l’ancienne base d’intégration ; il ne concerne pas ce lot.

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I40             # OK
verifier_sigles.py I40 chapters/I40/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I40                      # OK
node tests/verify_course_native.cjs I40      # 3127 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i40_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
