# Lot ESC 2026 — I44 — Troubles de la conduction et bradycardies (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I44/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I44/I44_a.html` | remplacement | `a4a3d5102b9f8395` | `e2a14511d2ec0a05` |
| `chapters/I44/I44_b.html` | remplacement | `dc2c91516ed5e7be` | `5b12b78bfa8e90f2` |
| `chapters/I44/I44_c.html` | remplacement | `f7499e2e6a5fe05d` | `833f5a0e23437416` |
| `chapters/I44/I44_pop_esc_comparison.html` | add | `—` | `9ee5d101bb48c80c` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- Ancres sans champ « new » et labels hors libellé « ESC 2026 : … » : format non conforme ; réécrites. Ancre I44_b-a2 (rubrique des sources) retirée.
- Comparaison du niveau B1 à « l’ancien niveau B » alors que la classe antérieure était I, A ; corrigé.

Réserves :
- Raison de l’abaissement I → IIa non explicitée par l’ESC 2026.
- BLOCK HF : fraction ≤ 50 % ; classification 2026 : < 50 %.

## Levée des réserves de l'audit croisé de Codex

- **MED-01 (preuves reproductibles)** : statut global « levée côté producteur : chaque changement ESC 2026 est rattaché à une ligne de tableau citée (document, DOI, date, section, tableau, population, ligne, classe et niveau, notes, ligne antérieure comparée, provenance du fichier lu). Contrelecture indépendante de Codex à refaire au commit de remise. » ; accès primaire : Textes intégraux 2026 lus sur les extractions pdftotext locales des PDF de l’éditeur (tampon « by guest on 07 October 2026 », empreintes SHA-256 dans PROVENANCE.md), non versionnés. Accès automatisé à academic.oup.com refusé depuis cet environnement (HTTP 403, vérification anti-robot) ; ESC 2021 sur la stimulation relu sur PubMed Central (PMC13179788) ; ESC 2024 sur la fibrillation auriculaire relu sur le jeu de diapositives officiel de l’ESC.. Pour I44 : {"preuves": "livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I44/PREUVES.md", "changements_retires": ["formule de l’ancre I44_c-a1 « recommandée (ESC 2021, classe I ; ESC 2026 : classe IIa, fraction < 50 %) »", "« alternative possible » attribuée au consensus ESC 2025 sur la stimulation du système de conduction (non relu ; requalifié « sans classe de recommandation »)", "référence « recommandations sur l’entraînement » (→ tableau de recommandations 9 de la réadaptation)"]}.
- **MED-02 (I44)** : statut « levée ». Ancre I44_c-a1 réécrite : … : l’ESC 2021 sur la stimulation recommande alors la resynchronisation (classe I, niveau A). L’ESC 2026 sur l’insuffisance cardiaque ne la place plus qu’« à envisager » (ESC 2026 : classe IIa, niveau B1) chez le patient en insuffisance cardiaque dont la fraction est < 50 % et qui a besoin d’une stimulation ventriculaire pour un BAV de haut degré ; ce seuil strict diffère du « ≤ 50 % » d’inclusion de l’essai BLOCK HF.

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I44             # OK
verifier_sigles.py I44 chapters/I44/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I44                      # OK
node tests/verify_course_native.cjs I44      # 3427 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i44_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
