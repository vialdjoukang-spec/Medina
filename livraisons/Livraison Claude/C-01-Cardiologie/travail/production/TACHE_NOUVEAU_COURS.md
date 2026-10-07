# Production d'un nouveau cours MEDINA (I83, I89) — consignes communes

Dépôt : `/home/user/Medina`. Dossier de travail du cours : `livraisons/Livraison Claude/C-01-Cardiologie/travail/production/<CODE>/`. Ne jamais écrire dans `chapters/`, `glossary/` ni `chapters.json` : l'orchestrateur y copiera le résultat vérifié.

## À lire avant d'écrire
- `CHAPTER_SPEC.md` (contrat HTML ; ses chemins `/home/claude/medina` correspondent à `/home/user/Medina`) et `docs/STYLE_REDACTION.md`.
- `docs/collaboration/FRAGMENT_01_PRIORITE.md` : fenêtres contextualisées (réponse directe d'abord), aucun objectif de longueur, comparaison ESC 2026 si une recommandation 2026 concerne le sujet.
- `livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/CONSIGNES.md` : exactitude, sources, sigles, confidentialité. **Ne jamais transmettre l'adresse e-mail ni aucune donnée personnelle du propriétaire à un service externe (pas d'Unpaywall).**
- Modèles de forme : `chapters/I80/` (cours vasculaire voisin, structure courte) et `chapters/I48/` ou `chapters/I50/` (gabarit complet, fenêtres justifiées). Imiter la forme, ne copier aucune phrase.

## Exigences de fond
- Chaque affirmation porte son pourquoi (mécanisme → conséquence clinique → décision), dans le texte ou dans une fenêtre ouverte par un mot vert. Distinguer association et causalité, recommandation et résultat d'essai.
- Sources suisses d'abord (Société suisse d'angiologie, OFSP, Swissmedic, compendium.ch si accessible), puis européennes (ESVS, ESC, International Society of Lymphology, etc.). Toute donnée chiffrée vient d'une source vérifiée en texte intégral ou sur PubMed ; sinon, pas de chiffre.
- Volume : complet sans remplissage. Repère : texte principal de 7 000 à 11 000 mots, fenêtres de 4 000 à 8 000 mots au total.
- Sigles : aucun sans entrée au glossaire. Les nouvelles entrées vont dans `glossary_<code>.py` du dossier de travail, au format de `glossary/i48.py` (`from cardio_1 import a, G` puis `a(...)`), définition lettre à lettre. Contrôler les textes avec `python3 "livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/verifier_sigles.py" <CODE> <fichiers>` : le résultat doit être `{}`, une fois le glossaire du cours pris en compte : `MEDINA_GLOSSAIRE_EXTRA="<chemin>/glossary_<code>.py:<autres>" python3 …/verifier_sigles.py <CODE> <fichiers>`.

## Rôles
- **Architecte** : écrit `PLAN.md` (périmètre CIM, plan détaillé des 4 onglets avec ids d'îlots, cas fil rouge chiffré, faits clés sourcés avec leurs références vérifiées, liste des fenêtres avec clé, titre, fichier pop et onglet propriétaire, partage des fichiers pop entre rédacteurs, liste des sigles et de leur glossaire), puis `glossary_<code>.py` initial et `src/` (recommandations téléchargées, jamais versionnées).
- **Rédacteur d'onglet** : écrit seulement ses fichiers (`brouillon/<CODE>_a.html`… et ses `brouillon/<CODE>_popN.html`), selon `PLAN.md`. Il ajoute ses sigles éventuels dans `glossary_<code>_<onglet>.py`. Il ne modifie ni le plan ni les fichiers des autres.
- **Vérificateur** : contrôle tout de façon indépendante (exactitude dans les sources, cohérence entre onglets, contrat HTML, sigles, concision, aucune redite), corrige en place et écrit `verification.json`.

## Contrat technique (rappel)
- `<CODE>_a.html` ouvre `<template id="ch-<CODE>"><div class="chap">`, l'en-tête, les quatre onglets et `pA` ; `<CODE>_d.html` se ferme par `</div></template>`. Reprendre exactement la structure d'en-tête et d'onglets de `chapters/I80/I80_a.html` et la fermeture de `I80_d.html`.
- Classes de la liste fermée seulement ; ids préfixés par le code en minuscules ; clés de fenêtres `<code>-…` ; chaque `data-k` a son `template data-pop`.
- Dernier îlot de l'onglet 1 : critères formels du diagnostic (`div.alert`) puis paramètres clés (`div.key`). Pareto à la fin de chaque grande partie volumineuse. Au moins trois quiz dans l'onglet Examens. Au moins un schéma SVG noir et blanc légendé.
