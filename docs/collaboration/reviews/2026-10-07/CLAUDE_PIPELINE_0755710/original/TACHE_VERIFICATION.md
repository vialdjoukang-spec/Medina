# Vérification indépendante — justification d'un cours

Tu n'es pas l'auteur ; ne lui accorde aucune confiance. Lis d'abord `CONSIGNES.md`, puis tous les résultats du dossier `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/<CODE>/` : `edits/`, `jobs/`, `out/`, `bilan_*.json`. Les sources sont dans `chapters/<CODE>/`.

## 1. Compléments du texte (`edits/<FICHIER>.json`)
Pour chaque édition, lis `old` dans son contexte, puis contrôle :
- l'exactitude du mécanisme et de chaque chiffre dans la source primaire ;
- la fidélité au sens de `old` et la conservation de toutes ses balises ;
- l'utilité réelle du complément et l'absence de redite avec le contexte ;
- le style et les sigles ;
- l'unicité de `old` dans le fichier.

Écris `verdicts/<FICHIER>.json` : `[{"id":…, "decision":"accepter"|"corriger"|"rejeter", "new_final":"texte complet si corriger", "probleme":"…"}]`, une entrée par édition et dans l'ordre. Si `old` est introuvable mais que le passage existe clairement, ajoute `old_reel` exact, et `fichier_reel` s'il se trouve dans un autre fichier.

## 2. Fenêtres (`jobs/` et `out/`)
- Contrôle chaque fenêtre comme ci-dessus : chiffres, classes, physiopathologie, surcertitude, cohérence avec le cours et concision.
- Corrige `out/<tag>.html` en place. Écris `out/<tag>.contreverif.json` : `{"verdict":"ok"|"corrigée", "erreurs":[…], "reserves":[…]}`.
- **Doublons.** Deux producteurs (P1 et P2) ont travaillé en parallèle.
  - Si deux fenêtres `creer` traitent le même mécanisme, garde la meilleure, enrichie au besoin. Dans le `out/<tag>.json` de l'autre, ajoute `"fusionnee_dans":"<clé gardée>"` : ses ancres pointeront vers la fenêtre gardée.
  - Si deux compléments `completer` visent la même clé, supprime les redites entre eux.
- Ancres : retire, dans `ancres_retirees` du `out/<tag>.json`, toute ancre placée dans la fenêtre qu'elle ouvre ou dont la fenêtre ne justifie pas l'affirmation. Un `label` corrigé va dans `label_modifies` et reste une sous-chaîne exacte de `old`.
- Contrôle `verifier_sigles.py` sur chaque `out/*.html` corrigé.

## 3. Réponse finale
En quelques lignes : les décisions sur les compléments (acceptés, corrigés, rejetés), les fenêtres corrigées, les erreurs de fond trouvées, les doublons fusionnés et les réserves. Écris aussi `verification.json` : les mêmes informations, sous forme structurée.
