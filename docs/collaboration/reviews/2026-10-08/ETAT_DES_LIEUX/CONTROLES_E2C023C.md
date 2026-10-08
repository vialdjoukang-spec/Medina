# I83 — Varices des membres inférieurs : contrôles du delta E2C023C

**Les six opérations ciblées sur le canonique sont réussies, avec un code de
sortie 0.** Le contrôle natif PC/mobile valide **1 923 assertions sans échec** ;
les routes I83 et I87 valident **41 assertions dans quatre cas**, sans erreur
JavaScript. Le delta médical est traité séparément dans `DELTA_E2C023C.md`.

La phrase reçue au SHA `e2c023c8ea255809d53561ccdb1273cb1641813f` est présente
dans le fichier canonique testé. Le HEAD local avant et après ces contrôles est
`72ccab4ea2197f8890d090270d212bb54184e0d0` : ce rapport identifie le contenu de
travail contrôlé et ne présente pas la phrase comme déjà committée sur ce HEAD.
Aucun fichier source ni aucune référence Git n'ont été modifiés par ces
contrôles. **Les 21 entrées sources/outils surveillées restent inchangées.**

## Identité du fichier et de la copie de livraison

`chapters/I83/I83_d.html` et
`livraisons/Livraison Codex/C-01-Cardiologie/sources/chapters/I83/I83_d.html`
portent tous deux exactement le SHA-256 demandé :

```text
72a6ddb28a8379f9ab54323d3323220e3f4f102129f1f948d5ccf8c58c5b0e06
```

Le fichier D canonique conserve cette empreinte après les contrôles. Les huit
HTML I83, glossaires concernés, inscriptions et outils inclus dans l'instantané
ont les mêmes empreintes avant et après. Les scripts de confiance sont inchangés
par rapport aux contrôles précédents. L'option vérifiée du compilateur pour S01
est bien `--fragment S01`.

## Résultats et horaires réels

Horaires du **8 octobre 2026 à Europe/Zurich, UTC+02:00**. Les timestamps UTC,
durées exactes, arguments et environnement sont archivés dans le JSON principal.

| Opération | Début–fin à Zurich | Durée | Code de sortie | Résultat |
| --- | --- | ---: | ---: | --- |
| Construction globale | 12:11:19–12:11:31 | 11,58 s | 0 | HTML global construit ; aucun `non couvertes` annoncé |
| Construction S01 | 12:11:19–12:11:28 | 8,79 s | 0 | Fragment C-01-Cardiologie construit |
| Statique I83 | 12:12:12–12:12:13 | 0,74 s | 0 | `OK` ; 40 865 mots, 47 fenêtres, 6 quiz et 6 Pareto |
| Navigateur global I83 | 12:12:12–12:12:37 | 24,88 s | 0 | `OK` à 1300 × 900 et 390 × 844 |
| Natif I83 dans S01 | 12:12:12–12:13:06 | 54,53 s | 0 | 1 923 assertions ; zéro échec et zéro erreur JavaScript |
| Routes I83/I87 dans S01 | 12:12:12–12:12:19 | 6,60 s | 0 | 41 assertions ; quatre cas ; zéro erreur JavaScript |

Dans chacun des deux viewports natifs, 1360 × 900 et 390 × 844, les
**78 déclencheurs directs**, dont 72 mots verts, et les **7 déclencheurs imbriqués**
ouvrent réellement les **47 fenêtres sources sur 47**. Les titres et textes
compilés sont comparés aux HTML canoniques actuels, incluant la phrase reçue.
Retour, Échap, focus, sources et absence de débordement restent contrôlés.

Pour les quatre cas I83/I87 × bureau/mobile, un seul cours primaire I83 s'affiche.
Chaque onglet est réellement ouvert puis contrôlé pour visibilité, sélection
et absence de débordement horizontal. Aucun `pageerror` n'est relevé.

## Commandes et sorties indépendantes

```text
python3 /workspace/Medina/build_front.py
python3 /workspace/Medina/build_front.py --fragment S01
python3 /workspace/Medina/test_v7.py --static I83
python3 /workspace/medina-env/reprise-i83/e2-canonical/controls/global-http.py
node -r /workspace/medina-env/reprise-i83/e2-canonical/controls/http-preload.cjs /workspace/Medina/tests/verify_course_native.cjs
node -r /workspace/medina-env/reprise-i83/e2-canonical/controls/http-preload.cjs /workspace/medina-env/reprise-i83/e2-canonical/controls/routes-i83-i87.cjs
```

Les constructions utilisent `MEDINA_ROOT=/workspace/Medina` et leurs sorties
distinctes : `MEDINA_OUT=.../e2-canonical/global` pour l'HTML global,
`MEDINA_OUT=.../e2-canonical/s01` pour S01. Le natif lit
`MEDINA_FRAGMENTS=.../e2-canonical/s01/fragments`.
`MEDINA_CHROMIUM` et `MEDINA_CHROMIUM_PATH` désignent `/usr/bin/chromium` ;
`PYTHONDONTWRITEBYTECODE=1` évite de créer des caches dans les sources.
Les journaux et helpers restent sous `.../e2-canonical/controls`.

Les helpers de `controls-20c67c0` ont été adaptés uniquement aux chemins de
ces sorties externes. Les assertions des scripts de confiance restent identiques
et actives. Le transport est **HTTP local sur loopback**, avec les destinations
externes HTTP(S) bloquées ; le global ne rapporte aucune tentative externe.
La portabilité directe `file://` et une émulation Safari/iOS ou matérielle ne
sont pas établies par ces contrôles de viewports Chromium.

Les 118 unités, la suite S01 de 72 contrôles et l'audit des 22 fragments n'ont
pas été rejoués pour cette seule phrase. Leurs preuves antérieures restent
rattachées à leur périmètre ; ce rapport n'en annonce pas une nouvelle exécution.

## Artefacts et pièces jointes

| HTML construit | Taille | SHA-256 |
| --- | ---: | --- |
| `e2-canonical/global/MEDINA.html` | 9 856 579 octets | `86129250ed54f7fa2fd853caa37b294b6e169acd8a1ea111bbc86580688ba183` |
| `e2-canonical/s01/fragments/MEDINA_S01_cardiovasculaire.html` | 4 568 108 octets | `8b606a9fef09a12a1fbb28f810f78692a634861e638c34eb02869b4ab3cc4290` |

- `CONTROLES_E2C023C.json` : identité des sources et HEAD, empreintes avant/après,
  six commandes, environnement ciblé, horaires et journaux complets, synthèses,
  artefacts, isolation réseau et code/empreintes des helpers.
- `CONTROLES_E2C023C_NATIFS.json` : les 1 923 assertions et la couverture détaillée.
- `CONTROLES_E2C023C_ROUTES.json` : les 41 assertions et les quatre cas réels.

**Statut technique : vert sur le contenu canonique contrôlé.** Le commit
complémentaire et sa publication restent des opérations du coordinateur.
