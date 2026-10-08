# Réception PR #12 — I89-2 — tête de67651

## Décision

- **Repéré : oui.** Origine Claude établie par la branche `claude/loving-shannon-spwrhc`, le signal, le manifeste et le rapport.
- **Reçu : oui.** Dix-huit originaux sont archivés sans modification, avec leurs objets Git et une provenance vérifiable.
- **Intégré : non.**
- **Contrôlé techniquement de manière indépendante : non.**
- **Publié : documentation de réception seulement.** Aucune source canonique ni sortie du site n'est modifiée.

La branche a ensuite avancé à `8a6dc7f28bbdaa5251f9a4b75031875073bf7ccb` par ajout d'un lot I83 distinct ; le contenu I89-2 reçu demeure celui de `de67651b882d3b75c8044813be23824edb41074a`.

## Contenu et empreintes

Le manifeste I89-2 est basé exactement sur `main` `1c39691289c49cb701345026b5ab9334f5330225`. Les 11 propositions SHA-256 concordent ; les baselines de `chapters.json` et `tests/verify_s01_browser.cjs` concordent ; les neuf chemins déclarés en ajout sont absents de cette baseline.

Par rapport à I89 v1 déjà reçu, cinq propositions sont identiques (`chapters.json`, `I89_a`, `I89_b`, `I89_pop1`, test S01) et six sont réellement modifiées (`I89_c`, `I89_d`, `I89_pop2`, `I89_pop3`, `I89_pop4`, glossaire). I89-2 est donc une remise substantielle qui remplace v1 dans l'historique ; aucune partie inchangée n'est réappliquée.

Archive : `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_DE67651_I89_2`  
Arbre des originaux : `80269438f508aed6fe0d22dc23ba67ec52481cce`  
Arbre avec provenance : `8c13eafa47305222fd769f6658d7dae1ece179c9`

## Relecture médicale ciblée

Réserves levées : doses/durées d'octréotide retirées ; prégabaline corrigée ; Verdye limité aux juridictions et dates effectivement documentées ; preuves animales FOXC2/PIEZO1 et schéma habituel du conduit lymphatique droit explicités.

Réserves bloquant l'intégration :

1. `I89_d.html` et `I89_pop4.html` attribuent au minoxidil une baisse de pression de perfusion rénale à partir d'une source qui formule ce mécanisme pour l'hydralazine ; il faut une source directe, ou retirer/dissocier l'extrapolation.
2. Plusieurs mécanismes restent appuyés par des revues plutôt que par les sources primaires requises : myxœdème–glycosaminoglycanes, AINS, corticoïdes, vasodilatateurs directs et pénicilline–peptidoglycane.

Le statut et la disponibilité suisses de Verdye en 2026 restent non vérifiés, sans que le cours ne les affirme. Cette contrelecture est ciblée et ne certifie pas exhaustivement les 30 cours.

## Contrôles

Contrôles producteurs archivés : 118 tests unitaires, 2 595 contrôles natifs et 73 contrôles S01 annoncés sans échec. Ils n'ont pas été reproduits. Le workspace de cette itération ne fournit pas le dépôt local, `tools/livraison.py`, la reconstruction ni la vérification navigateur ordinateur/mobile nécessaires. Aucun contrôle non exécuté n'est attribué.

## Chaîne et périmètre

I83 demeure le chapitre actif Claude tant que sa dernière harmonisation n'est pas intégrée et publiée ; aucune attribution n'est modifiée. Restent distincts : campagne historique 30 cours (15/15), backlog cardiologique 20 cours (10/10), 21 fragments (11 Claude / 10 Codex). Le catalogue reste CIM-10 ; aucune complétude CIM-11 n'est revendiquée.
