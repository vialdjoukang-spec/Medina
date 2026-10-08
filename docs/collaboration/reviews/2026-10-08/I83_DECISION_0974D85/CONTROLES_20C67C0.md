# I83 — Varices des membres inférieurs : contrôles finaux de 20c67c0

Les **six opérations techniques sont réussies, toutes avec un code de sortie
0**, sur la copie finale de la remise
`20c67c011e57eccd25b105b15f465becf7df7f2e`, préparée depuis
`e5bde2b5f94852851a6b2542b48e541ce6a72ef5`. Le navigateur natif valide
**1 923 assertions, zéro échec et zéro erreur JavaScript**. Les routes I83 et I87
valident **41 assertions dans quatre cas**, avec leurs quatre onglets accessibles
sur ordinateur et mobile.

Ces preuves peuvent être rattachées à la réception sélective de ce SHA source.
Elles établissent le comportement technique et la stabilité du périmètre
examiné ; la clôture des réserves médicales relève des rapports médicaux.
Aucune injection, publication ou mutation Git n'a été effectuée par ce contrôle.

## Comparaison complète des entrées

La copie `/workspace/medina-env/reprise-i83/candidate-20c67c0` a été comparée
aux **2 075 blobs** de la base main e5bde2b. Elle présente exactement :

- Les huit HTML I83 et les deux glossaires autorisés ajoutés ; les dix SHA-256
  correspondent au manifeste avant exécution.
- Aucun fichier retiré.
- Une seule modification d'un fichier préexistant : `chapters.json`. En retirant
  l'entrée I83 de la copie, son JSON est identique à celui de la base. L'entrée
  ajoute `I83 — Varices des membres inférieurs`, intégrée, couvrant I83 et I87.
- Tous les autres fichiers préexistants identiques à la base, notamment les
  registres, compilateurs, moteurs, scripts de confiance et tests.

Par rapport à la copie 20bee19, **seuls deux fichiers sources changent** :

| Source finale | SHA-256 |
| --- | --- |
| `chapters/I83/I83_d.html` | `d6a339fea23ae2ffb8aa16268972ec0e9708b997fbd44403b3a2478387bbc88f` |
| `chapters/I83/I83_pop4.html` | `04ef2f3e5d1985dc9a338f60c4a921a908b9d16c630b28cbb52fec3b05f18574` |

La comparaison avec 20bee19 conserve séparément les différences documentaires
de la base plus récente. Les glossaires et inscriptions n'ont pas changé par
rapport au périmètre de réception précédent.

Après tous les contrôles, **les 2 085 fichiers de la copie candidate sont
inchangés**, avec les mêmes SHA-256 avant et après, sans ajout ni suppression.
Les résultats des têtes précédentes restent intacts dans leurs dossiers et JSON.

## Résultats réellement exécutés

Horaires du **8 octobre 2026 à Europe/Zurich, UTC+02:00**. Les horaires UTC
et les durées précises sont aussi enregistrés dans `20C67C0_COMMANDES.json`.

| Opération | Début–fin à Zurich | Durée | Code de sortie | Résultat |
| --- | --- | ---: | ---: | --- |
| Construction globale | 11:48:13–11:48:25 | 12,61 s | 0 | HTML global reconstruit ; aucun `non couvertes` annoncé |
| Construction S01 | 11:48:13–11:48:22 | 9,38 s | 0 | Fragment propriétaire C-01-Cardiologie reconstruit |
| Statique I83 | 11:49:01–11:49:01 | 0,61 s | 0 | `OK` ; 40 786 mots, 47 fenêtres, 6 quiz et 6 Pareto |
| Navigateur global I83 | 11:49:01–11:49:25 | 24,09 s | 0 | `OK`, bureau 1300 × 900 et mobile 390 × 844 |
| Natif I83 dans S01 | 11:49:01–11:49:52 | 51,58 s | 0 | 1 923 assertions ; zéro échec et zéro erreur JavaScript |
| Routes I83 et I87 dans S01 | 11:49:01–11:49:06 | 5,54 s | 0 | 41 assertions ; quatre cas ; zéro erreur JavaScript |

Dans chaque viewport du contrôle natif, **78 déclencheurs directs**, dont
72 mots verts, et **7 déclencheurs imbriqués** ouvrent réellement les
**47 fenêtres sources sur 47**. Les attentes sont calculées depuis les HTML
finaux, notamment D et pop4 ; le texte et les titres compilés sont comparés à
ces sources. Retour, Échap, focus, sources et absence de débordement restent
contrôlés. Les empreintes des entrées propres au test restent stables.

Le complément demande réellement `#/entry/I83` puis `#/entry/I87`, à
1360 × 900 et 390 × 844. Chaque cas affiche un seul cours I83, avec quatre
onglets ; chacun est cliqué, sa visibilité et sa sélection sont assertées.
Aucun onglet ne produit de débordement horizontal. Aucun `pageerror` n'est relevé.

Les dimensions mobiles sont des viewports Chromium de bureau, sans revendication
de validation Safari/iOS ni de matériel tactile.

## Commandes, environnement et transport

```text
python3 /workspace/medina-env/reprise-i83/candidate-20c67c0/build_front.py
python3 /workspace/medina-env/reprise-i83/candidate-20c67c0/build_front.py --fragment S01
python3 /workspace/medina-env/reprise-i83/candidate-20c67c0/test_v7.py --static I83
python3 /workspace/medina-env/reprise-i83/controls-20c67c0/global-http.py
node -r /workspace/medina-env/reprise-i83/controls-20c67c0/http-preload.cjs /workspace/medina-env/reprise-i83/candidate-20c67c0/tests/verify_course_native.cjs
node -r /workspace/medina-env/reprise-i83/controls-20c67c0/http-preload.cjs /workspace/medina-env/reprise-i83/controls-20c67c0/routes-i83-i87.cjs
```

Leurs arguments exacts, environnement ciblé, répertoire courant, journaux et
codes de sortie figurent dans `20C67C0_COMMANDES.json`. Variables principales :

```text
PYTHONDONTWRITEBYTECODE=1
MEDINA_ROOT=/workspace/medina-env/reprise-i83/candidate-20c67c0
MEDINA_OUT=/workspace/medina-env/reprise-i83/output-20c67c0
MEDINA_FRAGMENTS=/workspace/medina-env/reprise-i83/output-20c67c0/fragments
MEDINA_NATIVE_CODE=I83
MEDINA_CHROMIUM=/usr/bin/chromium
MEDINA_CHROMIUM_PATH=/usr/bin/chromium
TMPDIR=/workspace/medina-env/reprise-i83/controls-20c67c0/tmp
```

Les helpers sont externes au checkout. Les navigations `file://` sont converties
en **HTTP local sur loopback**, avec les destinations externes HTTP(S) bloquées.
Aucune tentative externe n'est enregistrée par le contrôle global. Les liens
sources du contrôle natif restent vérifiés sans téléchargement externe.
Aucune assertion fonctionnelle ou clinique n'a été désactivée ; aucun contenu
candidat ou script de confiance n'a été modifié pour obtenir les résultats.
La portabilité directe `file://` n'a pas été établie par ces exécutions HTTP.

Les unités, catégories, audit des 22 fragments et contrôle S01 historique n'ont
pas été répétés, puisque leurs outils, inscriptions et glossaires sont inchangés
par rapport au périmètre déjà contrôlé. Leurs résultats antérieurs restent
rattachés à leurs versions. La reproductibilité globale n'a pas été mesurée à
nouveau sur 20c67c0 et n'est pas annoncée comme une preuve nouvelle de cette tête.

## Artefacts et pièces jointes

| HTML construit | Taille | SHA-256 |
| --- | ---: | --- |
| Global `MEDINA.html` | 9 856 351 octets | `aa1a737062342edcdfdb9a16dda98c5708041546a04cdc7bef0e4be13dff91fa` |
| S01 `MEDINA_S01_cardiovasculaire.html` | 4 567 880 octets | `391e633e9fd51fb33f698bc46dfbeb7124599ce908d3e028b8b155d4be37bb33` |

Les onze JSON préfixés `20C67C0_` conservent :

- `MANIFESTE`, `PERIMETRE_MAIN` et `DELTA_20BEE19` : SHA, comparaison exhaustive
  des blobs de la base et delta des sources.
- `INTEGRITE` : stabilité des 2 085 fichiers candidats pendant les contrôles.
- `COMMANDES` et `LOGS` : six opérations, horaires réels et journaux complets.
- `RESULTATS_NATIFS` et `ROUTES_I83_I87` : 1 923 et 41 assertions détaillées.
- `RESEAU_GLOBAL`, `HELPERS` et `ARTEFACTS` : transport, sources et empreintes
  des helpers externes, empreintes des HTML reconstruits.

**Statut final : contrôles techniques du périmètre source 20c67c0 réussis.**
Toute intégration conserve son propre commit et ses vérifications de la version
injectée ; ce rapport identifie précisément la copie source examinée.
