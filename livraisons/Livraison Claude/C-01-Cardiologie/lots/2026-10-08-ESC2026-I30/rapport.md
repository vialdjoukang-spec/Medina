# Lot ESC 2026 — I30 — Péricardites, épanchement péricardique, tamponnade et constriction (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I30/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I30/I30_c.html` | remplacement | `5dfeb9e062d5c51e` | `1cfdaf4e82dcec46` |
| `chapters/I30/I30_pop_esc_comparison.html` | add | `—` | `57a37d024c8cc77e` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- Ligne « Troponine » : « avant 2026, 99e percentile de la méthode » est inexact ; la quatrième définition (2018) recommandait déjà des seuils propres au sexe avec les dosages ultrasensibles (cinquième définition, section 14.1). La cinquième les rend nécessaires à la définition de la lésion.
- Réserve erronée : la cardiomyopathie restrictive n’a pas disparu du texte 2026 ; la note e du tableau de recommandations 4 exige le cathétérisme droit et gauche pour la distinguer de la constriction.

Réserves :
- Le texte 2026 ne chiffre pas de seuil par dosage ; seuil féminin de la troponine T ≈ moitié du seuil masculin.
- La phrase de I30_c « seuil commun aux deux sexes » décrit le fabricant ; un complément du texte reste à décider.

## Levée des réserves de l'audit croisé de Codex

- **MED-01 (preuves reproductibles)** : statut global « levée côté producteur : chaque changement ESC 2026 est rattaché à une ligne de tableau citée (document, DOI, date, section, tableau, population, ligne, classe et niveau, notes, ligne antérieure comparée, provenance du fichier lu). Contrelecture indépendante de Codex à refaire au commit de remise. » ; accès primaire : Textes intégraux 2026 lus sur les extractions pdftotext locales des PDF de l’éditeur (tampon « by guest on 07 October 2026 », empreintes SHA-256 dans PROVENANCE.md), non versionnés. Accès automatisé à academic.oup.com refusé depuis cet environnement (HTTP 403, vérification anti-robot) ; ESC 2021 sur la stimulation relu sur PubMed Central (PMC13179788) ; ESC 2024 sur la fibrillation auriculaire relu sur le jeu de diapositives officiel de l’ESC.. Pour I30 : {"preuves": "livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I30/PREUVES.md", "changements_retires": ["« 14 ng/L » (fenêtre et ligne canonique I30_c, par edits/I30_c.json)", "« environ la moitié du seuil masculin » (proportion d’une population de référence, non un seuil)", "décision « une troponine qui monte ou baisse sous cette valeur peut signer une atteinte myocardique »", "« séries cliniques » non citées (ligne peptides natriurétiques, requalifiée d’après l’ESC 2025, section 4.5.5)"]}.
- **MED-03 (I30)** : statut « levée côté producteur ». Aucun seuil chiffré ajouté ("aucun"). Précision de lésion aiguë ou chronique (encadrés 1 et 2 de la cinquième définition) ajoutée après la réception `315280c` : voir PREUVES.md.

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I30             # OK
verifier_sigles.py I30 chapters/I30/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I30                      # OK
node tests/verify_course_native.cjs I30      # 2787 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i30_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
