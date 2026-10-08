# Chaîne interne Claude — cahier commun du rédacteur et du relecteur différé

Application de `LEADERSHIP_CLAUDE_2026-10-08.md` (sections 2, 7, 8, 9 et 10). Ce cahier est remis à chaque agent de la chaîne.

## Références à lire avant d'écrire

1. `CHAPTER_SPEC.md` (contrat HTML : templates `ch-<CODE>`, quatre onglets `pA`, `pE`, `pS`, `pP`, classes de la liste fermée, identifiants préfixés par le code en minuscules, fenêtres `<template data-pop=…>`).
2. `docs/STYLE_REDACTION.md` et `docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md`.
3. Le modèle de densité : `chapters/J40/` (cours compact et complet) ; le modèle de profondeur : `chapters/J45/`.
4. `glossary/j40.py` : format des abréviations `a(clé, [(lettres, mot)…], définition, html)`.

## Règles de fond et de forme

- **Efficacité plutôt que volume** : chaque phrase apporte une information utile ; mécanisme → conséquence clinique → conduite ; détail approfondi dans les fenêtres.
- **Français merveilleux à lire** : riche, précis, rythmé, professionnel, sans excès ni ornement ; phrases complètes, jamais nominales ; termes médicaux dédiés définis à leur première occurrence.
- **Justification causale** de chaque affirmation, sources primaires datées : suisses d'abord (OFSP, sociétés suisses, Compendium), puis européennes (ERS, ESC…) et internationales acceptées en Suisse. Pour un contentieux, la source primaire applicable la plus récente l'emporte, présentée dans une fenêtre liée à un mot vert.
- Normal avant pathologique ; exemples chiffrés ; aucune métaphore ni plaisanterie.
- Dernier îlot de l'onglet Pathologie : critères formels (`div.alert`) puis paramètres clés (`div.key`). Pareto « perfectit » en fin de grande partie.
- Aucune abréviation sans clé dans `glossary/<code>.py` ; `build_medina.audit()` doit renvoyer `{}` pour le cours.
- Nomenclature : `code — intitulé (P-02-Pneumologie)` dans les rapports.
- Ne jamais présenter une revue IA comme une validation médicale.

## Rédacteur

Écrit **uniquement** dans `livraisons/Livraison Claude/<fragment>/travail/<CODE>/` (arborescence `chapters/<CODE>/…`, `glossary/<code>.py`, `rapport_auteur.md` avec sources consultées et réserves). Ne modifie aucun fichier canonique ni partagé. Ne fait aucune opération Git.

## Relecteur différé (« Auto-audit par Agent différé opus 5.5 »)

Agent distinct du rédacteur. Il :
1. relit intégralement fond, mécanismes, sources, chiffres, posologies et langue ;
2. **renforce les points faibles** et corrige directement les erreurs ;
3. **injecte** : copie vers `chapters/<CODE>/` et `glossary/<code>.py`, ajoute l'entrée `chapters.json` (`integrated: true`) et l'entrée `organisation/course_groups.json` (`owner` du fragment, `covers`, `scope`) ;
4. exécute les contrôles : `python3 -m unittest discover -s tests -p 'test_*.py'`, l'audit des abréviations, `python3 build_front.py --all-fragments` puis l'ouverture du cours dans le fragment ;
5. rédige `rapport_relecture.md` (corrections apportées, réserves restantes, contrôles) dans le dossier de travail.

Le relecteur ne fait aucune opération Git : l'assembleur Claude commit, pousse, produit les deux captures et demande l'audit Codex.

## Règle fondamentale (section 11 de LEADERSHIP_CLAUDE)

- Aucune affirmation de mémoire : chaque fait est rattaché à une source lue. Sinon : retirer ou nommer la lacune.
- Sources suisses puis européennes ; **aucune recommandation américaine** comme fondement (CDC, IDSA, ACCP, AHA/ACC, ATLS, FDA).
- Médicaments : `python3 tools/swissmedic_fi.py` (information professionnelle suisse, Swissmedic) en texte intégral.
- Plan monographique de PROMPT_MEDINA.md § 10 ; **aucun îlot, titre ou tableau consacré au code CIM** (code seulement dans l'en-tête).
