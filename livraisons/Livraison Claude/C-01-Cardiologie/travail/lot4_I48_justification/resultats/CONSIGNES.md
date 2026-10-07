# Consignes communes — lot 4, justification de I48 (Fibrillation et flutter auriculaires)

Contexte : cours MEDINA I48, préparation de l'examen fédéral suisse de médecine humaine. Exigence du propriétaire : chaque affirmation porte son **pourquoi**, c'est-à-dire le mécanisme physiopathologique précis qui relie le fait à sa conséquence clinique, puis à la décision. Lire `/home/user/Medina/docs/STYLE_REDACTION.md` (règles de rédaction) avant d'écrire.

## Rédaction
- Français médical professionnel, phrases courtes et complètes, jamais nominales. Typographie : apostrophe ’, guillemets « ».
- Ordre : physiologie normale → mécanisme → conséquence clinique → décision.
- Aucune métaphore, aucune plaisanterie, aucun métadiscours (« le lecteur », « cette fenêtre », « ce cours », « nous allons »).
- **Concision obligatoire.** Aucune répétition, aucun remplissage, aucune redite de ce que la fenêtre existante ou le texte d'ancrage disent déjà. Chaque phrase justifie une affirmation ancrée ou la décision qui en découle. Repères : une fenêtre créée compte environ 1 500 à 4 000 caractères ; les rubriques ajoutées à une fenêtre existante, environ 600 à 2 500 caractères. Ne dépasser ces repères que si un mécanisme indispensable l'exige.
- **Sigles** : n'employer que ceux déjà définis pour I48 : AOD, INR, ETO, ETT, EHRA, AF-CARE, CHA₂DS₂-VASc, CHA₂DS₂-VA, HAS-BLED, ABC, UI, VIH, VP, T3, T4, B1, B4, RR, PR, QT, QTc, aVF, ECG, FA, FEVG, AVC, IRM, BNP, NT-proBNP, TSH. « AIT » et « HTA » sont interdits (écrire « accident ischémique transitoire », « hypertension artérielle »). Pour tout autre sigle, vérifier par `grep "a('SIGLE'" /home/user/Medina/glossary/*.py` ; en cas de doute, écrire en toutes lettres. Tout autre terme s'écrit en toutes lettres (« bloc auriculoventriculaire », « nœud auriculoventriculaire », « débit de filtration glomérulaire »).
- HTML autorisé dans une fenêtre : `<div class="lab">…</div><p>…</p>`, `<b>`, `<i>`, `<sub>`, `<sup>`. Rien d'autre.

## Exactitude et sources
- Tout chiffre, seuil, dose, classe ou niveau de recommandation provient d'une source identifiée et vérifiée.
- ESC 2024 sur la FA (Van Gelder et al., Eur Heart J 2024;45:3314-3414, doi:10.1093/eurheartj/ehae176) en texte intégral : `/tmp/claude-0/-home-user-Medina/eea4eb75-fb19-5942-b0fe-ceaa24acce07/scratchpad/esc/esc2024.txt` (chercher avec Grep). Citer « ESC 2024, section X » ou « tableau Y ».
- Physiologie classique : manuel identifié (Guyton & Hall 14e éd., Braunwald 12e éd., Zipes & Jalife) ou revue identifiée (auteurs, revue, année).
- Un mécanisme débattu est présenté comme tel. Pas de surcertitude. Ne jamais inventer une référence ; si une source ne peut être vérifiée, retirer le chiffre ou le formuler sans chiffre.
- Cohérence avec le reste du cours I48 : `/home/user/Medina/livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/` (fichiers a, b, c, pop1-4) et `/home/user/Medina/chapters/I48/I48_d.html`. Ne pas contredire le cours ; signaler une contradiction si le cours a tort.
- Dernière rubrique de chaque fenêtre créée ou complétée : `<div class="lab">Source</div><p>…</p>` (références compactes). Pour une fenêtre complétée qui a déjà une rubrique Source, écrire une rubrique « Source complémentaire ».

## Ne jamais modifier les fichiers du dépôt. Écrire seulement dans le dossier `out/` ou `inline_out/` du scratchpad indiqué.
