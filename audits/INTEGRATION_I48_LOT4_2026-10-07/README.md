# Intégration du lot 4 — I48 — Fibrillation et flutter auriculaires

Le lot 4 de Claude est injecté dans les sources canoniques et contrôlé techniquement. La construction atomique a produit les 22 fragments. **Publication sur `main` : effectuée**, avec déploiement Pages réussi au commit `e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6`. L’utilisateur a confirmé explicitement la publication le 7 octobre 2026 à 23:11, heure de Zurich.

| Référence | Valeur |
| --- | --- |
| Fragment consommateur | C-01-Cardiologie |
| Cours | I48 — Fibrillation et flutter auriculaires |
| Lot reçu | `b1f19c3510c1a828650867da033ebe2fbf30142e` |
| Commit des sources publiées | `e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6` |
| Commit local testé | `201c9c1a4c5b60e4126338e944355a0b2a5e9cc1` |
| Arbre commun strictement identique | `81f5a8c5800f10eb9396ccb0dec2543ea77b0146` |
| Construction contrôlée | `dist/atomic-lot4/fragments/` |
| Empreintes de construction | [BUILD_HASHES.json](BUILD_HASHES.json) |

## Contenu intégré et adaptations

Les huit fichiers HTML du cours et ses fenêtres, ainsi que le glossaire I48, sont intégrés. Le contrôle ciblé des sources reçues confirme la conservation sur le fond des **11 arbitrages Codex antérieurs**. Des insertions mécanistiques ou de balisage empêchent parfois une correspondance strictement littérale ; le détail de chaque comparaison figure dans [ARBITRAGES_PRESERVES.json](ARBITRAGES_PRESERVES.json).

Les corrections médicales supplémentaires sont consignées dans [ADAPTATIONS_CODEX.json](ADAPTATIONS_CODEX.json). Elles portent sur l’anticoagulation après cardioversion, l’interprétation de CHAMPION-AF, les modalités d’administration de la digoxine et la distinction entre les seuils thérapeutiques de fraction d’éjection utilisés par l’ESC 2024 pour la fibrillation auriculaire et la nomenclature de l’insuffisance cardiaque de 2026.

Le moteur privilégie désormais la fenêtre mécanistique lorsqu’un mot vert contient une abréviation imbriquée. Le clic naturel, Enter et Espace produisent la même action. Les abréviations autonomes conservent leur définition dédiée.

| Mesure finale du cours | Valeur | Preuve |
| --- | ---: | --- |
| Volume des sources | 66 578 mots | [static.log](static.log) |
| Fenêtres propres à I48 | 100 | [static.log](static.log), [rapport natif](native_browser/results.json) |
| Occurrences natives de mots verts | 206 | [rapport natif](native_browser/results.json) |
| Boutons Pareto | 15 | [static.log](static.log), [rapport natif](native_browser/results.json) |
| Renvois entre fenêtres vérifiés | 36 | [rapport natif](native_browser/results.json) |

Le contrôle natif ouvre également la fenêtre externe `e-crepitants` : son total de 101 fenêtres correspond donc aux 100 fenêtres I48 et à ce renvoi partagé.

## Contrôles finaux

**80 tests unitaires et 7 891 contrôles navigateur réussis.** Les cinq séries navigateur totalisent `71 + 609 + 2 310 + 656 + 4 245 = 7 891` contrôles. Les rapports finaux ne signalent aucune erreur JavaScript ou console.

| Série | Nombre | Résultat final | Preuve |
| --- | ---: | --- | --- |
| Tests unitaires | 80 | Réussi | [unittest.log](unittest.log) |
| Navigation et lecture du fragment cardiologique | 71 | Réussi | [s01/browser-results.json](s01/browser-results.json) |
| Sciences fondamentales et sémiologie clinique | 609 | Réussi | [sciences_cs/science-cs-browser-results.json](sciences_cs/science-cs-browser-results.json) |
| Justifications contextualisées | 2 310 | Réussi | [justifications/justifications_results.json](justifications/justifications_results.json) |
| Organisation par catégories | 656 | Réussi | [categories/categories_results.json](categories/categories_results.json) |
| Fenêtres natives I48 et régression des abréviations imbriquées | 4 245 | Réussi | [native_browser/results.json](native_browser/results.json) |
| Total navigateur | **7 891** | **Réussi** | Cinq rapports ci-dessus |

Le contrôle natif couvre chaque occurrence de mot vert et de Pareto, les renvois, les retours, les fermetures et la restitution du focus. Il contrôle les quatre onglets et les disciplines scientifiques, avec une largeur mobile de 390 px et des tailles de texte de 17 et 24 px. Aucun débordement horizontal n’est constaté. Il comprend 499 activations par pointeur, 76 par clavier et sept captures.

Les vérifications statiques et de construction sont conservées dans [static.log](static.log), [build.log](build.log) et [fragments.log](fragments.log).

## Construction atomique et empreintes

Les 22 noms de fragments déclarés dans `BUILD_HASHES.json` correspondent aux 22 fichiers `MEDINA_*.html` de `dist/atomic-lot4/fragments/`. La comparaison SHA-256 indépendante est conforme : **22 empreintes identiques, aucun fragment déclaré manquant et aucun fragment de production supplémentaire**.

Le fragment cardiologique atomique est identique à celui utilisé pour le contrôle natif. Son empreinte est :

`08279a521cb0fa93de132809a526c02c80852e5d7bcc436d1c3b9e011970341a`

Les huit sources I48, le glossaire et le moteur sont restés inchangés pendant ce contrôle. Les premières tentatives de publication ont été rejetées automatiquement. Après confirmation explicite de l’utilisateur, le terminal Git ne disposait pas d’identifiants d’écriture ; la connexion du plugin GitHub a publié l’arbre contrôlé avec les parents `a6f18a1` et `fde806d`, en conservant la contribution originale Claude. Le commit API porte un SHA différent ; son arbre source est strictement identique au commit local testé.

Le [déploiement Pages](https://github.com/vialdjoukang-spec/Medina/actions/runs/37688889857) a réussi. Le fichier servi pèse 4 039 235 octets et porte le SHA-256 `776cb1d1a53bdd31bf53246ed014bfd21970d1c245b3a7b643bdf8930e62332e`. Sa différence avec l’empreinte locale est isolée au seul octet OS de l’en-tête gzip : 3 localement, 255 dans le build distant. Les templates décompressés et toute surface HTML hors paquet sont strictement identiques ; [preuve complète](publication/content_equivalence.json).

## Contrôle de la version publique

Le [contrôle public](publication/README.md) réussit 54 vérifications supplémentaires, sans erreur JavaScript ou console. Les quatre onglets et la fenêtre CHA₂DS₂-VA s’ouvrent par clic naturel sur le mot ou son abréviation imbriquée, sur ordinateur et mobile. L’environnement navigateur géré utilise une exception de confiance pour son proxy TLS ; le téléchargement HTTPS indépendant avec vérification du certificat a réussi.

## Portée de la relecture médicale

Le rapport de Claude annonce **505 affirmations traitées**. La réception et les contrôles techniques ne certifient pas une contre-lecture scientifique exhaustive de chacune de ces 505 affirmations. La relecture médicale Codex est **ciblée** sur les arbitrages antérieurs et les points sensibles documentés dans les adaptations. Elle ne conclut ni à la validation médicale exhaustive du cours ni à celle des autres leçons.

## Passages diagnostiques antérieurs

Les rapports finaux référencés dans le tableau constituent les résultats de validation. Les passages diagnostiques antérieurs restent conservés, sans modification des preuves :

- `native_browser/results_initial_probe.json` a révélé l’interception des clics sur les mots verts par leurs abréviations imbriquées. Son comparateur comptait aussi à tort les traits d’union conditionnels du moteur comme des différences de texte. Le défaut produit et le normaliseur du test ont été corrigés.
- `native_browser/results_focus_race_probe.json` contrôlait le focus avant l’exécution de l’événement natif `close`. Le test final attend cet événement, puis contrôle la restitution effective du focus.
- `justifications/failed_justifications_results.json` conserve un passage diagnostique antérieur. Le résultat de validation de cette série figure dans `justifications/justifications_results.json`.

Le comparateur natif final retire uniquement U+00AD et normalise les espaces. Il compare le titre et le texte intégral de chaque fenêtre à son template construit. La méthode et les captures sont détaillées dans [native_browser/README.md](native_browser/README.md).
