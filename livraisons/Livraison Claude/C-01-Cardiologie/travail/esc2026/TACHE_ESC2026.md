# Comparaison ESC 2026 dans un cours de Claude

Consigne (`docs/collaboration/FRAGMENT_01_PRIORITE.md`) : présenter les changements **ESC 2026** entre parenthèses ou dans une fenêtre comparative avec le référentiel antérieur. Modèles : `chapters/I48/I48_pop_esc_comparison.html` et `chapters/I50/I50_pop_esc_comparison.html`, et leurs mots verts dans `I48_b.html` et `I48_d.html`.

Lis aussi `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/CONSIGNES.md` (exactitude, sigles, confidentialité : **aucune donnée personnelle transmise à un service externe, pas d'Unpaywall**).

## Pour chaque cours confié
1. Base de travail : la copie livrée `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/<CODE>/` (elle contient la justification du lot 5), et pour les fichiers absents, `chapters/<CODE>/`.
2. Recense, sur le site de l'ESC (escardio.org) et dans la littérature, **toutes les recommandations ESC publiées en 2026** et retiens celles qui touchent le cours, directement (recommandation propre) ou indirectement (par exemple la nouvelle définition de l'insuffisance cardiaque pour les cardiomyopathies, les myocardites ou les valvulopathies). Lis-en le texte intégral ou, à défaut, le communiqué officiel et le résumé publié. Ne rapporte que ce qui est vérifié.
3. Si aucune recommandation 2026 ne touche le cours, écris seulement `bilan.json` avec la liste examinée et la conclusion.
4. Sinon, produis dans `livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/<CODE>/` :
   - `jobs/<code>-esc-2026-comparaison__P1.json` et `out/<code>-esc-2026-comparaison__P1.html` (action `creer`, `fichier_cible` = un nouveau fichier `<CODE>_pop_esc_comparison`, à créer vide par l'orchestrateur), avec une à trois ancres sur les passages concernés ; le libellé annonce « ESC 2026 : … » ;
   - si une phrase du cours est devenue fausse, un complément `edits/<FICHIER>.json` qui ajoute la donnée 2026 entre parenthèses, au format de `travail/justification/TACHE_PRODUCTION.md` ;
   - `bilan.json` : recommandations examinées, changements retenus, sources, réserves.
5. La fenêtre commence par une réponse directe, compare l'ancien et le nouveau référentiel (tableau `table.t` autorisé), puis dit ce qui change pour la décision ; elle distingue une nouvelle classification d'une indication médicamenteuse. Sources en liens HTTPS comme dans le modèle.
6. Ne modifie ni `chapters/` ni les copies livrées : l'orchestrateur appliquera après vérification.
