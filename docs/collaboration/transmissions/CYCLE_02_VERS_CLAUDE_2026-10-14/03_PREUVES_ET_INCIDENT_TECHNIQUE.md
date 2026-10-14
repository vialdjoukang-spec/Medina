# Travail effectivement disponible et preuve de ses limites

## 1. Scripts et dossiers GitHub accessibles
- Quatre remises auteurs : répertoires `livraisons/Livraison Codex/*/travail/CYCLE_02_{code}`.
- Examen et retours : `docs/collaboration/reviews/2026-10-14/CYCLE_02/cross/`.
- Correctif préparatoire **dans le dépôt** : [tools/cycle2_reprise_01_safety.py](../../../../tools/cycle2_reprise_01_safety.py). Son texte porte les modifications, leurs cibles et la création d'un reçu local après application. Ce script n'est pas une version auditée.
- Workflow en échec : [cycle2-reprise-corrections.yml](../../../../.github/workflows/cycle2-reprise-corrections.yml). Exécution : [GitHub Actions 38630788715](https://github.com/vialdjoukang-spec/Medina/actions/runs/38630788715).
- Version antérieure de proposition G45, **transférée dans cette remise sous forme de JSON texte**, avec empreintes attendues et références suisses : [G45_R1_R3_PROPOSITION.json](G45_R1_R3_PROPOSITION.json). Elle diffère structurellement du script à 16 opérations : choisir après comparaison, ne pas juxtaposer aveuglément.

## 2. Faits établis par les journaux
À l'exécution 38630788715 (14.10.2026, vers 20 h 17 UTC), le runner a imprimé : « 16 corrections appliquées dans 8 fichiers; audits et injection non attestés. » Ensuite : « Chemin hors périmètre: ?? docs/collaboration/reprises/ » ; le job a échoué, les tests complets ainsi que l'enregistrement ont été sautés. La cause est l'usage de `git status --porcelain -z` qui regroupe un dossier non suivi, alors que le contrôle attend un chemin fichier. Piste **à tester et non à accepter aveuglément** : `git status --porcelain -z --untracked-files=all`. Claude doit décider si le script est conservé, amendé ou remplacé.

Le registre `organisation/execution-20261014/status.json` est plus ancien : 4 premières passes défavorables et 25 réserves ; aucun contre-audit, aucune injection. Cette photographie n'est pas un reçu d'activité présente.

## 3. Travail G45 effectué hors GitHub dans l'ancienne session
Une proposition G45-R1/R3 visant deux fichiers (`G45_d.html`, `G45_pop2.html`) a été construite depuis un instantané de travail confirmé par 2 467 empreintes de fichiers. **21 tests mécaniques** ont été réussis dans le contexte précédent (fixtures et vérifications de reconstitution) ; des contrôles complémentaires ont préservé ancres, cibles de fenêtres et absence de nouveau script pour ces deux fichiers.
Anciennes SHA-256 des fichiers source :
- `G45_pop2.html` avant : `24270e022b649d72d4008e735bddf5d3ce072f55d2922cb35e95d5b7b074de51` ; proposition hors dépôt : `88d0c1113d23a39df09832fe9b1d6a769a306f050b37a42745686923fe2947b1`.
- `G45_d.html` avant : `f51094b4b82d6ba11730f0ebbf962f69e63e6936f56e5f48974be25990b4c356` ; proposition hors dépôt : `15e5b18c4ab28d28e8233253bb2c27b3c3fa817d13336454a6ca63ead4360ba3`.

**Transparence** : les tests originaux en Python, la proposition HTML de 2 fichiers et les archives de sources complètes de cet instantané ne sont **pas** intégrés à cette transmission. Le JSON de proposition permet de revoir le contenu médical et de reproduire les insertions après vérification des SHA Git/identifiants ; les 21 tests historiques restent une observation rapportée, non une nouvelle CI passée sur GitHub. Claude doit renouveler tests, traçabilité et validation sur sa propre version. Il ne faut pas présenter ce travail comme complet, certifié ni déjà injecté.

## 4. Empreintes et changements concurrents
Branche initiale : `codex/cycles-20261014-0800` à `030f30f76034b02428734e6b662da4aaea32e87e`.
`main` au constat : `c768557034ad17f515ebd3aed82c3c225b1da356`.
L'historique du Cycle 1 produit par Claude a continué sur `main`. Il ne doit pas être remplacé par une copie intégrale de la branche Cycle 2. Claude fait un `git fetch` puis des comparaisons/rebases prudents, selon gardes et diffs effectifs.
