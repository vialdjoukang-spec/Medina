# Tâche textes — vérification des compléments intégrés au texte

Fichier d'entrée : `inline/<FICHIER>.json` (scratchpad). Champs : `source` (chemin du HTML actuel), `inline` = liste `{id, old, new, motif, source}`. `old` est un passage exact du HTML actuel ; `new` est sa réécriture proposée, avec l'explication du mécanisme intégrée. Ces propositions n'ont jamais été vérifiées.

Pour chaque édition, en VÉRIFICATEUR MÉDICAL ET STYLISTIQUE SCEPTIQUE :
1. Lire `old` dans son contexte du fichier source (paragraphe, cellule, liste). Si `old` est introuvable, décision `rejeter`.
2. Exactitude : mécanisme, chiffres, doses, seuils, classes contrôlés dans le texte ESC 2024 (Grep) ou une source classique identifiée.
3. Fidélité : `new` garde tout le sens et toutes les balises HTML de `old` (boutons `<button class="w" data-k=…>`, `<b>`, etc. intacts) ; aucune balise ouverte non fermée.
4. Utilité : `new` ajoute un vrai pourquoi absent du contexte immédiat ; sinon `rejeter`. Supprimer toute redite avec la phrase précédente ou suivante.
5. Style et sigles : phrases complètes, concises ; dans une cellule de tableau, une à deux phrases au plus ; sigles autorisés seulement (voir CONSIGNES.md).

Décisions : `accepter` (new tel quel), `corriger` (donner `new_final` complet, corrigé et condensé), `rejeter` (motif). 

Sortie : `inline_out/<FICHIER>.json` = liste `[{"id":…, "decision":…, "new_final": texte final si accepter ou corriger, "probleme": "…", "source": référence vérifiée}]`, une entrée par édition, dans l'ordre.
