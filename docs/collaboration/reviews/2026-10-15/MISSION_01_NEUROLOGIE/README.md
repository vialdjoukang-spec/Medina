# Mission 1 — inventaire technique Neurologie, 15 octobre 2026

Base de comparaison : `bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373` (main GitHub observé le 15 octobre). Périmètre : N-05-Neurologie, identifiant S08. Aucun texte médical, glossaire, rapport de recherche ou paquet de livraison n’a été réécrit.

## Résultat

Le catalogue de Neurologie contient 116 catégories. La base déclare 53 cours intégrés : I63, G45, I61 et 50 cours Betta. L’inventaire repère 59 dossiers de livraison vivants : 57 avec HTML et deux avec recherche seule. Tous les cours déclarés intégrés possèdent leurs sources canoniques.

Quatre autres cours possèdent six HTML et un glossaire : **R25 — Mouvements involontaires anormaux**, **R26 — Anomalies de la démarche et de la motilité**, **R27 — Autres troubles de la coordination**, **R47 — Troubles du langage, non classés ailleurs**. Ils sont copiés ici vers les chemins canoniques, strictement octet pour octet (28 fichiers). Aucun asset local supplémentaire n’est référencé. Leur publication en l’état nécessite encore les entrées de catalogue et le registre de publication gérés par le coordinateur ; ce commit ne les déclare pas publiés.

**R29 — Autres symptômes et signes relatifs aux systèmes nerveux et ostéo-musculaire** et **R48 — Dyslexie et autres troubles de la fonction symbolique, non classés ailleurs** ne possèdent que `recherche.md` et `sources.json` dans les dossiers Betta du cycle 42. Il n’existe aucun HTML partiel à publier pour ces deux codes à la base examinée. Ces documents restent conservés et peuvent être rendus accessibles comme documents de travail sans les présenter comme un cours rédigé.

## Versions et conflits

L’inventaire lit les arbres des 79 références `origin/*` présentes après le fetch global du coordinateur, hors références de PR. Les 78 têtes distinctes se regroupent en huit états de sources neurologiques. Tous les chemins de sources neurologiques présents sur ces références existent déjà dans main ; aucune livraison supplémentaire exclusive à une branche n’a été identifiée. Les anciennes versions et preuves sont inventoriées par leur identifiant de blob Git, sans fusion ni réinjection.

Le paquet de travail Codex I63 diffère des six HTML canoniques actuels. Les HTML canoniques sont conservés : republier la copie de travail écraserait une révision ultérieure. G45 et I61 correspondent à leurs livraisons vivantes ; les 50 dossiers Betta déjà intégrés correspondent à leurs six HTML canoniques. Le JSON `packages.json` détaille chaque dossier.

Les quatre nouveaux cours sont encore `A_FAIRE` dans les anciens registres, bien que leurs fichiers existent. Le cycle Betta 42 est transféré à Novo12. Le plan Novo12 place R25/R26/R27 au cycle 42 et R47 au cycle 43. `catalogue_propose.json` propose des métadonnées de publication en l’état, avec audit différé explicitement non réalisé, sans prétendre à une validation médicale.

## Contrôles réellement exécutés

- Égalité octet par octet des 28 copies et empreintes SHA-256 : réussite ; `copies_sha256.json`.
- Analyse syntaxique des quatre modules de glossaire : réussite.
- Structure des quatre cours : un template principal chacun, panneaux pA/pE/pS/pP, aucune clé de fenêtre manquante, aucun identifiant ou clé de fenêtre en double, aucun asset local absent. Nombre de fenêtres : R25 42, R26 59, R27 50, R47 44. Détails : `structural_checks.json`.
- `python3 test_v7.py --static R25 R26 R27 R47` : échec avant les contrôles de cours. Le chargeur refuse le schéma de découverte dynamique de `r27.py` (`GlossaryLoadError`). Correctif moteur confié au domaine infrastructure ; aucun glossaire n’a été modifié pour contourner ce refus.

Aucun audit médical nouveau, déploiement, push ou fusion n’a été réalisé par cet agent. Les réserves existantes restent présentes dans les sources copiées. La disponibilité publique sera vérifiée par le coordinateur après son intégration.
