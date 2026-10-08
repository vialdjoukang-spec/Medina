# I83 — Varices des membres inférieurs : contrôles indépendants de 0974d85

Les contrôles techniques ciblés sont réussis sur la copie inspectée de la remise
`0974d854db292ae0311e435b3daea5fbed187e25`, avec les compilateurs et tests de la
base `ea105ace0046c71492cc6a69ff4c61698ef2ce34`. Le contrôle historique S01 échoue
sur son compteur fixe de 20 cours, alors que la copie contient réellement 21
cours. Ce résultat reste conservé séparément des suites dynamiques réussies.

**Aucune injection, publication ni certification médicale n'a été effectuée par
ces contrôles.** Aucun fichier de la copie candidate n'a été modifié : les
2 131 fichiers présents avant et après ont les mêmes SHA-256, sans ajout ni
suppression. La base et la remise restent identifiées séparément ; la copie
candidate n'est pas présentée comme un commit Git d'intégration.

## Entrées et exécution

- Copie inspectée : `/workspace/medina-env/reprise-i83/candidate`.
- Modification simulée : les huit HTML I83, les deux glossaires autorisés et
  l'entrée I83 dans `chapters.json`, couvrant I83 et I87.
- Les dix empreintes de fichiers du manifeste sont vérifiées avant exécution.
- Sorties : `/workspace/medina-env/reprise-i83/output`.
- Journaux et helpers : `/workspace/medina-env/reprise-i83/controls`.
- Date : **8 octobre 2026**, horaires Europe/Zurich (UTC+02:00). Les horodatages
  UTC complets et les durées précises figurent dans `0974D85_COMMANDES.json`.
- Chromium : `/usr/bin/chromium` ; Python 3.12.14, Node v24.19.0 et Playwright
  disponibles. Les empreintes des scripts de confiance sont celles consignées
  dans `PROTOCOLE_CONTROLES.md`, identiques à la base.

## Résultats réellement obtenus

| Contrôle | Début–fin à Zurich | Durée | Code de sortie | Résultat |
| --- | --- | ---: | ---: | --- |
| Construction globale | 11:29:40–11:29:53 | 13,52 s | 0 | HTML global construit ; aucune abréviation `non couvertes` annoncée |
| Construction de tous les fragments | 11:29:40–11:30:01 | 21,10 s | 0 | 22 HTML de fragments construits |
| Statique I83 | 11:31:09–11:31:10 | 1,13 s | 0 | `OK` ; 40 640 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| Navigateur global I83 | 11:31:09–11:31:39 | 29,94 s | 0 | `OK` à 1300 × 900 et 390 × 844 |
| Natif I83 dans S01 | 11:31:09–11:32:09 | 59,91 s | 0 | 1 923 assertions ; zéro échec, zéro erreur JavaScript |
| Catégories dynamiques S01 | 11:31:09–11:31:22 | 13,54 s | 0 | 76 contrôles ; zéro erreur ; bureau et mobile |
| Audit complet des fragments | 11:31:09–11:31:53 | 43,78 s | 0 | 22 fragments ; JavaScript valide ; deux constructions globales identiques |
| S01 historique, une seule exécution | 11:31:09–11:31:15 | 5,70 s | 1 | Assertion périmée « 20 cours uniques disponibles » |
| Routes I83 et I87 | 11:33:44–11:33:48 | 3,61 s | 0 | 41 assertions ; quatre cas réels ; zéro erreur JavaScript |

Le contrôle natif ouvre, **dans chacun des deux viewports**, les 78 déclencheurs
directs, dont 72 mots verts, et les 7 déclencheurs imbriqués. Les **47 fenêtres
sources sur 47** sont réellement ouvertes et contrôlées : compilation unique,
titre et texte attendus, Retour, Échap, restitution du focus, sources et absence
de débordement. Les empreintes des entrées du test restent stables. Les modèles
partagés externes, lorsque présents, sont distingués des attentes canoniques du
cours dans le rapport détaillé.

Le complément de routes demande réellement `#/entry/I83` puis `#/entry/I87`,
à 1360 × 900 et 390 × 844. Chaque cas affiche **un seul cours I83**, propose
quatre onglets, puis les ouvre un à un. Leur sélection et visibilité sont
assertées ; aucune vue ne déborde horizontalement. Les quatre cas et leurs
dimensions figurent dans `0974D85_ROUTES_I83_I87.json`.

Les dimensions mobiles sont des viewports Chromium ; aucune validation de
Safari/iOS ou de matériel tactile n'est revendiquée.

## Commandes et adaptations appliquées

Chaque ligne ci-dessous a été exécutée dans la copie inspectée. Le jeu commun
d'environnement, la ligne exacte, les arguments, horaires et codes de sortie
de chaque processus sont enregistrés dans `0974D85_COMMANDES.json`.

```text
python3 /workspace/medina-env/reprise-i83/candidate/build_front.py
python3 /workspace/medina-env/reprise-i83/candidate/build_front.py --all-fragments
python3 /workspace/medina-env/reprise-i83/candidate/test_v7.py --static I83
python3 /workspace/medina-env/reprise-i83/controls/global-http.py
node -r /workspace/medina-env/reprise-i83/controls/http-preload.cjs /workspace/medina-env/reprise-i83/candidate/tests/verify_course_native.cjs
node -r /workspace/medina-env/reprise-i83/controls/http-preload.cjs /workspace/medina-env/reprise-i83/candidate/tests/verify_categories.cjs
python3 /workspace/medina-env/reprise-i83/controls/audit-external-temp.py
node -r /workspace/medina-env/reprise-i83/controls/http-preload.cjs /workspace/medina-env/reprise-i83/candidate/tests/verify_s01_browser.cjs
node -r /workspace/medina-env/reprise-i83/controls/http-preload.cjs /workspace/medina-env/reprise-i83/controls/routes-i83-i87.cjs
```

Variables principales :

```text
PYTHONDONTWRITEBYTECODE=1
MEDINA_ROOT=/workspace/medina-env/reprise-i83/candidate
MEDINA_OUT=/workspace/medina-env/reprise-i83/output
MEDINA_FRAGMENTS=/workspace/medina-env/reprise-i83/output/fragments
MEDINA_NATIVE_CODE=I83
MEDINA_CATEGORY_FRAGMENT_IDS=S01
MEDINA_CHROMIUM=/usr/bin/chromium
MEDINA_CHROMIUM_PATH=/usr/bin/chromium
TMPDIR=/workspace/medina-env/reprise-i83/controls/tmp
```

`MEDINA_QA_OUT` est distinct pour chaque suite sous le dossier de contrôles.
`I83_CONTROL_ROOT`, `I83_CONTROL_OUT` et `I83_CONTROL_REPORTS` désignent les mêmes
emplacements pour les helpers externes. La source et le SHA-256 de chacun des
helpers utilisés sont archivés dans `0974D85_HELPERS.json`.

Les navigations utilisent **HTTP local sur loopback** : les helpers convertissent
les URL `file://` vers les HTML construits et laissent uniquement passer le
serveur local. Les requêtes externes HTTP(S) restent bloquées. Le contrôle global
n'a enregistré aucune tentative externe (`0974D85_RESEAU_GLOBAL.json`) ; le
contrôle de catégories rapporte zéro ressource distante demandée. Le contrôle
natif conserve ses assertions de liens de sources sans téléchargement externe.
La portabilité directe `file://` n'a pas été établie par cette exécution HTTP.

Pour `audit_fragments.py`, les seuls appels `tempfile` dont le répertoire était
le `ROOT` de la copie sont redirigés vers `controls/tmp`. Toutes ses assertions
restent actives, y compris la comparaison SHA-256 de ses deux constructions.
Les fichiers HTML et JavaScript temporaires sont ainsi hors de la copie.

Aucune assertion clinique ou fonctionnelle n'a été désactivée ; aucun fichier
de test ou de contenu candidat n'a été corrigé pour obtenir ces résultats.

## Fixture S01 historique et artefacts

`0974D85_INVENTAIRE_S01.json` constate **21 cours originaux uniques**, dont I83,
et `integrated_count = 21`. Le test historique attend exactement 20. Sa première
assertion de spécialité réussit, puis son assertion de compteur échoue ; les
étapes suivantes de cette suite n'ont pas été exécutées. Son échec ne doit pas
être confondu avec un test intégral de S01 réussi. Les contrôles dynamiques
de catégories et les interactions natives I83 constituent la couverture utile
effectivement exécutée.

HTML global produit : **9 855 855 octets**, SHA-256
`0462e8680ed004cf370609d96b87b3d6bbde1a1048b00ecc14c3842b81850f93`.
Les empreintes des 23 HTML construits (global et 22 fragments) figurent dans
`0974D85_ARTEFACTS.json`.

## Pièces jointes

- `0974D85_MANIFESTE.json` : périmètre simulé et empreintes des dix fichiers.
- `0974D85_COMMANDES.json` et `0974D85_LOGS.json` : processus réellement exécutés,
  environnement ciblé, horaires, codes de sortie et journaux complets.
- `0974D85_RESULTATS_NATIFS.json` : 1 923 assertions et couverture détaillée.
- `0974D85_CATEGORIES_S01.json` et `0974D85_ROUTES_I83_I87.json` : contrôles
  dynamiques et vérification des deux routes dans leurs quatre cas.
- `0974D85_S01_HISTORIQUE.json` et `0974D85_INVENTAIRE_S01.json` : échec de
  fixture historique et nombre de cours effectivement construit.
- `0974D85_RESEAU_GLOBAL.json`, `0974D85_HELPERS.json`, `0974D85_INTEGRITE.json`
  et `0974D85_ARTEFACTS.json` : transport, code de contrôle externe, stabilité
  de la copie et empreintes des résultats de construction.

La validation médicale et l'audit croisé restent à rattacher à leurs propres
rapports et commits. Une modification ultérieure de la remise exige les
contrôles adaptés sur sa propre copie ; ces preuves restent fixées à 0974d85.
