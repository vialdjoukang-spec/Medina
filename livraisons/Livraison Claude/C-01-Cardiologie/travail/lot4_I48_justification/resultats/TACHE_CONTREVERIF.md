# Contre-vérification indépendante d'une fenêtre rédigée

Pour chaque clé : lire `jobs/<cle>.json` (plan, ancres, fenêtre existante), `out/<cle>.html` (texte proposé) et `out/<cle>.json` (sources, réserves du rédacteur). Tu n'es pas l'auteur ; ne lui accorde aucune confiance.

1. Contrôler chaque chiffre, dose, seuil, classe, niveau, numéro de section ou de tableau dans le texte ESC 2024 par Grep, ou dans la source citée (PubMed si nécessaire). Une affirmation invérifiable est retirée ou formulée sans chiffre.
2. Contrôler la physiopathologie : mécanisme exact, absence de surcertitude, débat signalé.
3. Contrôler la cohérence avec le cours I48 et l'absence de redite avec la fenêtre existante ou une autre fenêtre du lot (`out/*.html`).
4. Contrôler le style (CONSIGNES.md) et les sigles. Initiales d'auteurs : écrire « Drew et al. » sans initiales.
5. Renvois : un renvoi vers une autre fenêtre d'I48 peut s'écrire `<button class="w" data-k="CLE">mot</button>`, à condition que la clé existe (`grep -o 'data-pop="[^"]*"'` dans les fichiers pop du cours, ou `jobs/*.json` avec action `creer`). Pas plus de deux renvois par fenêtre.

Si tout est juste, ne rien réécrire. Sinon corriger `out/<cle>.html` en place. Dans tous les cas, écrire `out/<cle>.contreverif.json` = `{"cle":…, "verdict":"ok"|"corrigée", "erreurs":[…], "reserves":[…]}`.
