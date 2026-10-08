# Réception Claude — C-01-Cardiologie — PR #16

## Décision

- **Repéré : oui.** Origine Claude établie par la branche, le manifeste, la remise et l’auto-revue.
- **Reçu et archivé : oui.** 297 objets manifestés et cinq fichiers de contexte sont conservés sous `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-PR16-95F921F/`.
- **Intégré : non.** Aucune source canonique, route, attribution ni valeur `active_chapter` n’est modifiée.
- **Contrôlé techniquement : partiel.** Empreintes, inventaire et structure statique contrôlés ; tests, builds et navigateur non reproduits.
- **Publié : réception documentaire seulement.** Aucun déploiement du site n’est requis.

## Provenance

- PR : https://github.com/vialdjoukang-spec/Medina/pull/16
- Tête réelle observée : `44856ce0f48823455cd7accdf0c1591750d5ccb0`
- Dernier commit modifiant le paquet C-01 : `95f921fa6c86dea97064a55c5b73df6244587046`
- Baseline `main` : `0604000a9acf8bc6f8217436064835777294c981`
- Manifeste : blob `984b20f3b5bc9f4778bdf380cd9d5df0a1503358`, SHA-256 `602aea84149471b837273d443b7ce4e2075c2f45006d7a093400bef7f5bec176`
- Inventaire : **30 cours, 76 catégories CIM-10-GM 2024, 76 couvertes**
- Complétude CIM-11 : **non établie**

Les commits postérieurs à 95f921f ajoutent des instructions et du travail P-02/J10/J47/J84/J90 hors périmètre ; ils ne modifient ni le manifeste C-01 ni ses sources. Le `base_commit` déclaré (`0bdb60ca82da208180ad706f981b0432afc434fa`) est un commit d’emballage, non la baseline `main`.

## Empreintes

Les **297/297 SHA-256** sont exacts : 83 objets proviennent du paquet Claude et 214 objets inchangés de `main`. Le dernier delta C-01 porte seulement sur `I97_d.html`, SHA-256 `cfdb9d30375a858273d98429dea0a029e9760baca73c6698c296c9982698e29b`.

`organisation/federal_exam.json` est haché mais absent de `sources/<chemin canonique>`; l’archive le conserve sans modification depuis son chemin direct. Aucun reçu antérieur sur `main` ne porte l’empreinte de ce manifeste ; b1, b6 et 8ce ne sont pas réappliqués.

## Blocages médicaux

1. **I85** : le propranolol est titré jusqu’à 160 mg deux fois par jour sans distinguer l’ascite, ce qui peut doubler la dose admissible chez le cirrhotique ascitique.
2. **I51** : la dose de charge du phenprocoumone repose sur une provenance suisse contradictoire/non vérifiée.
3. **I95** : le seuil 150/90 mmHg d’hypertension couchée doit être distingué du seuil définitionnel actuel 140/90 mmHg ; la formulation sur les symptômes d’hypotension orthostatique doit être précisée.
4. **I77** : l’aspirine ne doit pas être présentée comme systématique dans toute dysplasie fibromusculaire.
5. **R02** : le quiz doit séparer traitement empirique large et pénicilline-clindamycine après confirmation ou forte suspicion de clostridie.
6. **I51** : la mortalité « près de 80 % à 30 jours » d’une communication interventriculaire non opérée reste non confirmée.

Plusieurs affirmations reposent seulement sur des résumés, notices étrangères ou sources secondaires. Aucune relecture exhaustive des 30 cours n’est revendiquée.

## Audit technique

Exécuté : cohérence du manifeste et de l’inventaire, 297 empreintes, neuf ajouts, audit statique HTML/JSON/JS, templates/IDs/balises/fenêtres et correction I97.

Réserves : `m5` persiste dans I95, `m7` dans I85, d’autres réserves m1–m4/m8–m12 restent visibles, la baseline est mal qualifiée et la PR contient P-02 hors remise. La PR ne doit pas être fusionnée en bloc.

Non exécuté ici : `tools/livraison.py`, tests Python, reconstruction S01, navigateur ordinateur/mobile, débordements, journal JavaScript et déploiement. Les contrôles du producteur sont inventoriés, pas attribués à Codex.

## Conditions avant injection

Corriger les blocages et réserves ; réémettre une baseline explicite ; réconcilier avec le `main` vivant ; injecter sélectivement ; reconstruire ; tester ; contrôler ordinateur/mobile ; enregistrer un nouveau reçu.
