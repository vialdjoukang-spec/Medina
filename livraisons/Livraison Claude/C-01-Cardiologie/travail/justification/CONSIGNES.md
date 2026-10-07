# Justification systématique d'un cours MEDINA — consignes communes

Exigence de Vial (`docs/collaboration/MECHANISMS_CLAUDE.md`, à lire) : chaque affirmation médicale porte son **pourquoi**. Il s'agit du mécanisme causal précis qui relie le fait à sa conséquence clinique, puis à la décision. Cela vaut pour les quatre onglets, les fenêtres, les tableaux, les listes, les figures, les quiz, les Pareto et les rétroactions. Pour un bilan, chaque dosage dit pourquoi on le demande, comment on l'interprète et quelle valeur change quelle décision. Pour un traitement, distinguer le mécanisme, le bénéfice démontré, les indications et les risques. Une association n'est jamais présentée comme une causalité.

Le cours pilote I48 montre le niveau attendu : `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/fenetres_types.html`.

## Rédaction (`docs/STYLE_REDACTION.md`)
- Français médical professionnel, phrases courtes et complètes, jamais nominales. Apostrophe ’ et guillemets « ».
- Ordre : physiologie normale → mécanisme → conséquence clinique → décision.
- Aucune métaphore, aucune plaisanterie, aucun métadiscours (« le lecteur », « cette fenêtre », « cet îlot », « nous verrons »).
- **Concision.** Aucune répétition et aucun remplissage. Ne rien redire de ce que le texte voisin ou la fenêtre existante disent déjà. Repères : un complément dans le texte compte une à trois phrases, et une à deux phrases dans une cellule de tableau. Une fenêtre créée compte 1 500 à 4 000 caractères ; les rubriques ajoutées à une fenêtre existante, 600 à 2 500 caractères.
- **Sigles** : aucun sigle nouveau sans entrée au glossaire. Contrôler chaque texte produit avec `python3 livraisons/Livraison\ Claude/C-01-Cardiologie/travail/justification/verifier_sigles.py <CODE> <fichier.html>`, qui doit afficher `{}`. Sinon, écrire le terme en toutes lettres. Pour un nom d'essai indispensable, le signaler dans `reserves`. Dans les rubriques Source, écrire « Dupont et al. », sans initiales.
- HTML autorisé dans une fenêtre : `<div class="lab">…</div><p>…</p>`, `<b>`, `<i>`, `<sub>`, `<sup>`. Un renvoi vers une autre fenêtre du même cours s'écrit `<button class="w" data-k="CLE">mot</button>`, au plus deux par fenêtre, vers une clé existante.

## Exactitude et sources
- **Confidentialité : ne jamais transmettre l'adresse e-mail du propriétaire, son nom ni aucune donnée personnelle à un service externe** (Unpaywall, API, formulaires). Un service qui exige une adresse ne s'utilise pas.
- Tout chiffre, seuil, dose, classe ou niveau de recommandation provient d'une source primaire identifiée et **vérifiée** : recommandations ESC ou suisses en texte intégral, publication originale, PubMed, information professionnelle (compendium.ch si accessible, sinon résumé européen des caractéristiques du produit).
- Télécharger les recommandations de référence du cours dans `<dossier du cours>/src/`, si elles n'y sont pas déjà (`curl -sSL -o x.pdf URL`, puis `pdftotext -layout x.pdf x.txt`), et y chercher avec Grep. Une autre session y a peut-être déjà déposé le texte.
- Une affirmation invérifiable est retirée ou formulée sans chiffre. Ne jamais inventer une référence. Un mécanisme débattu est présenté comme tel.
- Cohérence avec le reste du cours. Si le cours contredit une source primaire, le corriger dans un complément du texte et le signaler dans `reserves`.
- Ne jamais toucher aux sources canoniques (`chapters/`) ni aux fichiers livrés : écrire seulement dans le dossier de résultats du cours.
