# A15 — QA technique et visuelle du preview I-03

Contrôle du 8 octobre 2026. Sources A15 assemblées dans `/workspace/work/medina-resume/livraisons/Livraison Codex/I-03-Infectiologie/travail/PRODUCTION_FRAGMENT_2026-10-08/sources/chapters/A15/` ; preview courant `dist/apercus/infectiologie.html`. Cette revue porte sur la structure et l’interface, pas sur la justesse médicale.

## Structure

- Les fragments `a+b+c+d` sont équilibrés. Le cours possède quatre panneaux : `pA`, `pE`, `pS`, `pP` ; 14 îlots de pathologie, 5 d’examens, 6 de sciences et 5 de pharmacologie.
- Les 24 ancres de navigation ont des cibles uniques. Les six boutons scientifiques `data-s` ouvrent chacun leur `div.sci` correspondant.
- 36 appels `data-k` ont 36 fenêtres `data-pop` distinctes ; aucune cible ne manque. Les classes HTML respectent le contrat du projet ; aucune marque de placeholder `⟦…⟧` ne subsiste.
- Cinq quiz sont structurés correctement, dont trois en examens. Le manifeste contient A15 et les sept fichiers HTML requis plus `glossary/a15.py` ; les huit empreintes SHA-256 correspondent aux fichiers présents.

## Navigation et rendu

Essai Chromium headless à **390, 768 et 1440 px**, hauteur 900 px, sur `#/entry/A15`. Les quatre onglets s’ouvrent, les six sous-onglets scientifiques sont visibles après sélection, une fenêtre contextuelle s’ouvre et se ferme, et le retour d’un quiz apparaît. Le fil d’Ariane est cliquable à chaque largeur, avec défilement initial à 0 px. Un clic sur un îlot des examens défile jusqu’à cet îlot sans changer la route ni revenir en haut.

Le document reste exactement dans la largeur du viewport (390, 768 et 1440 px). Les panneaux visibles ne débordent pas ; aucune erreur JavaScript n’a été relevée. Captures et mesures : `/workspace/work/a15-qa-captures/` (`result.json`, captures des quatre panneaux et de la fenêtre pour chaque largeur).

**Réserve UX mineure à 390 px :** quand les sous-onglets scientifiques arrivent au bord inférieur de l’écran, le bouton flottant « Navigo · Plan » recouvre temporairement une partie du bouton « Physiologie » (chevauchement mesuré d’environ 1 012 px²). Le défilement rend le sous-onglet accessible ; les six sous-onglets ont été ouverts pendant l’essai. Capture : `/workspace/work/a15-qa-captures/a15-390-pS.png`. Aucun blocage de navigation persistant n’a été observé.

Conclusion technique : aucun défaut bloquant détecté sur cette version du preview. Aucun fichier clinique n’a été modifié pendant cette QA.
