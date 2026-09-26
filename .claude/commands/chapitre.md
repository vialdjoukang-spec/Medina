Rédige et intègre le chapitre MEDINA : $ARGUMENTS

Procédure obligatoire :
1. Relire PROMPT_MEDINA.md (§ 4 à § 16) et un chapitre de référence complet (chapters/J45 ou chapters/T78).
2. Vérifier dans `medora-data` (shell/medina_front.html) le système (champ `system`) de chaque catégorie couverte ; fixer `wave` en conséquence. Vérifier `chapters.json` pour éviter les doublons.
3. Rechercher les recommandations à jour (Suisse d’abord : sociétés savantes suisses, OFSP, Swissmedic, compendium.ch ; puis ESC, EULAR, ERS, etc.), environ douze recherches ciblées, sans chiffre inventé.
4. Écrire `chapters/<CODE>/<CODE>_a.html` … `_d.html` et `_pop*.html` selon le contrat : 4 onglets, cas fil rouge, physiopathologie avec figure SVG, clinique, démarche diagnostique avec algorithme, urgences, traitement, suivi, situations particulières, cas récapitulatif, dernier îlot = critères formels + paramètres clés ; examens avec au moins trois quiz ; sciences avec corrélations ; pharmacologie avec doses suisses et interactions ; Pareto par grande partie. **Aucune condensation** : viser le niveau de J45.
5. Ajouter les abréviations manquantes dans `glossary/<code>.py` ; `B.audit(...)` doit renvoyer `{}`.
6. Déclarer le chapitre dans `chapters.json` (code, covers, title, integrated, wave, added = date du jour) ; mettre à jour `RENVOIS`, `PLAN`, `DONE_SYS` dans `shell/data.py` si nécessaire.
7. Exécuter `/livrer`.
