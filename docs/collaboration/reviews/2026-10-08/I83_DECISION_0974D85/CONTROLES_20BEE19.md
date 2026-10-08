# I83 — Varices des membres inférieurs : vérification de la tête 20bee19

Les **six opérations techniques demandées sur la nouvelle tête réussissent**,
toutes avec un code de sortie 0. La remise examinée est
`20bee19a6329f0a62126e9180bfc909207055e38`, simulée sur la base de confiance
`ea105ace0046c71492cc6a69ff4c61698ef2ce34`. Le contrôle natif retrouve
**1 923 assertions réussies, zéro échec et zéro erreur JavaScript**. Les deux
routes I83 et I87 passent leurs 41 assertions sur ordinateur et mobile.

Cette conclusion porte sur le comportement technique. Elle ne constitue ni
une décision médicale, ni une injection dans `main`, ni une publication.
Les rapports de la tête 0974d85 restent fixés à cette première version et
n'ont pas été remplacés par les résultats ci-dessous.

## Delta et entrées exactes

La comparaison des deux copies trouve une seule différence dans leurs sources :
`chapters/I83/I83_pop4.html`, dont le SHA-256 devient
`79ca90654e97fe00619ed3d76ad1847734b41c8f9019af32146b47d18f3d58d9`.
Les 52 fichiers `.pyc` préexistants de la première copie n'ont pas été emportés
dans la seconde ; ce sont des caches, distincts des sources du delta.
Les autres HTML, les glossaires, l'entrée de `chapters.json` couvrant I83/I87,
les outils et les scripts de contrôle restent identiques entre les copies.

- Nouvelle copie inspectée :
  `/workspace/medina-env/reprise-i83/candidate-20bee19`.
- Manifeste : `20BEE19_MANIFESTE.json`, dont les dix empreintes ont été vérifiées
  avant exécution ; SHA antérieur 0974d85 également enregistré.
- Sorties distinctes : `/workspace/medina-env/reprise-i83/output-20bee19`.
- Contrôles distincts : `/workspace/medina-env/reprise-i83/controls-20bee19`.
- **2 079 fichiers inchangés pendant les contrôles**, sans fichier ajouté,
  supprimé ou modifié dans la copie candidate.

## Résultats et horaires réels

Les horaires sont ceux du **8 octobre 2026 à Europe/Zurich, UTC+02:00**.
Les timestamps UTC précis figurent aussi dans `20BEE19_COMMANDES.json`.

| Opération | Début–fin à Zurich | Durée | Code de sortie | Résultat |
| --- | --- | ---: | ---: | --- |
| Construction globale | 11:37:06–11:37:19 | 13,06 s | 0 | HTML global reconstruit ; aucun `non couvertes` annoncé |
| Construction S01 | 11:37:06–11:37:16 | 9,77 s | 0 | Fragment propriétaire C-01-Cardiologie reconstruit |
| Statique I83 | 11:38:15–11:38:15 | 0,75 s | 0 | `OK` ; 40 735 mots, 47 fenêtres, 6 quiz et 6 Pareto |
| Navigateur global I83 | 11:38:15–11:38:39 | 24,06 s | 0 | `OK`, bureau 1300 × 900 et mobile 390 × 844 |
| Natif I83 dans S01 | 11:38:15–11:39:07 | 52,09 s | 0 | 1 923 assertions ; zéro échec et zéro erreur JavaScript |
| Routes I83 et I87 dans S01 | 11:38:15–11:38:21 | 6,09 s | 0 | 41 assertions ; quatre cas ; zéro erreur JavaScript |

Dans chaque viewport du contrôle natif, **78 déclencheurs directs**, dont
72 mots verts, et **7 déclencheurs imbriqués** ouvrent réellement les
**47 fenêtres sources sur 47**. Les attentes incluent le texte source mis à
jour de `I83_pop4.html`. Les titres, contenus, liens, Retour, Échap, focus et
débordements sont contrôlés avec les mêmes assertions de confiance que pour
la première tête. Les empreintes des entrées avant et après restent stables.

Le complément de routes vérifie successivement `#/entry/I83` et `#/entry/I87`
à 1360 × 900 puis 390 × 844. Chaque cas affiche un seul cours primaire I83.
Les quatre onglets sont réellement ouverts et leur visibilité/sélection est
assertée ; aucun ne déborde horizontalement.

Les dimensions mobiles sont des viewports Chromium de bureau ; aucune
validation Safari/iOS ou matérielle tactile n'est revendiquée.

## Exécution et transport

Commandes réellement exécutées dans la copie inspectée :

```text
python3 /workspace/medina-env/reprise-i83/candidate-20bee19/build_front.py
python3 /workspace/medina-env/reprise-i83/candidate-20bee19/build_front.py --fragment S01
python3 /workspace/medina-env/reprise-i83/candidate-20bee19/test_v7.py --static I83
python3 /workspace/medina-env/reprise-i83/controls-20bee19/global-http.py
node -r /workspace/medina-env/reprise-i83/controls-20bee19/http-preload.cjs /workspace/medina-env/reprise-i83/candidate-20bee19/tests/verify_course_native.cjs
node -r /workspace/medina-env/reprise-i83/controls-20bee19/http-preload.cjs /workspace/medina-env/reprise-i83/controls-20bee19/routes-i83-i87.cjs
```

`20BEE19_COMMANDES.json` conserve leurs arguments, code de sortie, durée,
horodatages et environnement ciblé complet. Variables principales :

```text
PYTHONDONTWRITEBYTECODE=1
MEDINA_ROOT=/workspace/medina-env/reprise-i83/candidate-20bee19
MEDINA_OUT=/workspace/medina-env/reprise-i83/output-20bee19
MEDINA_FRAGMENTS=/workspace/medina-env/reprise-i83/output-20bee19/fragments
MEDINA_NATIVE_CODE=I83
MEDINA_CHROMIUM=/usr/bin/chromium
MEDINA_CHROMIUM_PATH=/usr/bin/chromium
TMPDIR=/workspace/medina-env/reprise-i83/controls-20bee19/tmp
```

Les mêmes helpers de transport sont copiés sous le dossier externe de cette
tête. Les URL `file://` sont remplacées par **HTTP local sur loopback**, et les
destinations externes HTTP(S) restent bloquées. Aucune tentative externe n'est
enregistrée par le contrôle global. Les liens sources du contrôle natif restent
vérifiés sans téléchargement externe. Toutes les assertions fonctionnelles
restent actives ; aucun fichier candidat ni script de confiance n'a été édité.
La portabilité directe `file://` n'a pas été établie par ces exécutions HTTP.

Les suites de catégories, l'audit des 22 fragments, les unités et le test S01
historique n'ont pas été rejoués : aucune inscription, aucun glossaire et aucun
outil n'ont changé. Leurs preuves antérieures restent rattachées à 0974d85.
La reproductibilité globale n'a pas été réévaluée sur 20bee19 ; elle n'est donc
pas annoncée comme un résultat nouveau de cette tête.

## Artefacts et pièces jointes

| HTML construit | Taille | SHA-256 |
| --- | ---: | --- |
| Global `MEDINA.html` | 9 856 167 octets | `e11412e12773b05ef0cf0cc387944639f695ef1e287f00e183922219b668f80b` |
| S01 `MEDINA_S01_cardiovasculaire.html` | 4 567 696 octets | `66b7b83e4e17e00af44605e382d0ce48721c92ca828b6107fae2d109e707b059` |

Les dix JSON préfixés `20BEE19_` conservent :

- `MANIFESTE`, `DIFFERENCES_COPIES` et `INTEGRITE` : tête/périmètre, différences
  exactes entre les copies et stabilité de la copie courante.
- `COMMANDES` et `LOGS` : les six opérations et leurs journaux complets.
- `RESULTATS_NATIFS` et `ROUTES_I83_I87` : les 1 923 et 41 assertions détaillées.
- `RESEAU_GLOBAL`, `HELPERS` et `ARTEFACTS` : isolation réseau, source et
  empreintes des helpers externes, empreintes des deux HTML reconstruits.

**Statut final de cette vérification : contrôles techniques du delta 20bee19
réussis.** La décision de réception et d'injection reste à prendre au regard des
rapports médicaux et de leurs réserves, au même SHA source.
