Mission de Vial — 8 octobre 2026. Priorité confirmée : achever **C-01-Cardiologie**, puis passer à **P-02-Pneumologie**.

## Les quatre productions prioritaires restantes

| Responsable | Chapitre à produire | Périmètre |
| --- | --- | --- |
| Claude | **I83 — Varices des membres inférieurs** | Varices, reflux et hypertension veineuse, classifications cliniques, ulcère veineux et diagnostics différentiels, cartographie duplex, compression et traitements interventionnels. Les atteintes I87 couvertes doivent être déclarées explicitement ; ne pas assimiler toute jambe gonflée à des varices. |
| Claude | **I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques** | Lymphœdème primaire/secondaire, transport lymphatique, diagnostic, diagnostics différentiels, traitement décongestif et indications spécialisées. Distinguer lipœdème, œdème veineux, insuffisance cardiaque et adénopathie infectieuse ou tumorale. |
| Codex — lancé | **I73 — Autres maladies vasculaires périphériques** | Phénomène de Raynaud, thromboangéite oblitérante et atteintes vasculaires pertinentes du périmètre déclaré. Éviter les doublons avec I70, I71 et I80. |
| Codex — lancé | **I95 — Hypotension** | Hypotension orthostatique et postprandiale, mécanismes neurogènes, volémiques et médicamenteux, mesures couchée/debout, diagnostics différentiels, urgence et traitement. |

Ces quatre cours correspondent aux codes prioritaires manquants du registre `organisation/fragments.json`. Ils ne prouvent pas à eux seuls la complétude de toutes les catégories CIM-11. La relecture des vingt cours existants reste répartie **10 Codex / 10 Claude**, selon la mission actuelle ; les nouvelles livraisons historiques de Claude restent recevables, même lorsqu'elles concernent désormais des cours Codex.

## Commencer en un seul endroit

Dépôt : https://github.com/vialdjoukang-spec/Medina
Branche de référence : `codex/sciences-cs-fragments-20261007`.
Lire `AGENTS.md`, `CLAUDE.md`, `docs/collaboration/HANDOFF_LATEST.md`, `docs/collaboration/FRAGMENT_01_PRIORITE.md`, `CHAPTER_SPEC.md` et `docs/STYLE_REDACTION.md`. Les anciens chemins /home/claude sont des exemples : utiliser le clone réel.

```bash
git fetch origin
git switch -c claude/production-i83-i89-20261008 origin/codex/sciences-cs-fragments-20261007
git rev-parse HEAD
```

Noter ce SHA comme base. Ne pas repartir d'une ancienne copie de livraison. Ne modifier ni les cours déjà intégrés ni les fichiers communs de publication. Un cours par commit facilite la réception.

## Qualité attendue

1. Quatre onglets complets : Pathologie et prise en charge, Examens, Sciences fondamentales spécialisées, Pharmacologie propre à la maladie. Préserver le front-end, les icônes scientifiques et la navigation existants.
2. Chaque affirmation médicale expose sa raison : fonctionnement normal → perturbation → conséquence → décision. Choisir les mots natifs qui ouvrent des fenêtres contextualisées. Chaque fenêtre commence par une réponse directe, puis précise le mécanisme, son intérêt clinique, ses limites et la source. Un lien bibliographique seul ne justifie pas une affirmation.
3. Les examens sont reliés à une question précise. Le test de référence et ses limites sont nommés ; aucun « gold standard » n'est inventé lorsqu'il n'existe pas de test universel. Les valeurs sont accompagnées d'unités, de conditions de mesure et de populations.
4. Les signes cliniques et facteurs de risque expliquent pourquoi ils apparaissent ou changent la décision. Les diagnostics différentiels sont hiérarchisés par gravité. Inclure des cas ambulatoires, urgents et de personnes âgées.
5. Les sciences sont propres au chapitre. Présenter au moins les disciplines pertinentes, avec des SVG exacts, lisibles, légendés et reliés aux signes, examens ou traitements. Ne pas recopier cinq schémas génériques.
6. La pharmacologie distingue mécanisme, niveau de preuve, indication, posologie, contre-indications, interactions et surveillance. Vérifier les informations professionnelles suisses ; signaler explicitement l'usage hors indication ou une source étrangère. Ne pas prescrire un diurétique comme traitement du lymphœdème isolé par analogie avec un œdème cardiaque.
7. Les quiz expliquent la réponse correcte et pourquoi chaque distracteur est faux. Les résumés Pareto conservent toutes les restrictions utiles du texte principal.
8. Français professionnel, phrases complètes et courtes, sans métaphores, métadiscours ni répétitions. Aucun minimum ou multiplicateur de mots ne remplace la profondeur.
9. Sources primaires vérifiées et datées : sociétés suisses, recommandations européennes, informations professionnelles suisses, études originales. Comparer les changements récents aux versions précédentes quand ils changent la conduite. Ne pas présenter une association comme une causalité établie.
10. Tenir un registre d'affirmations par section : repère, affirmation, mécanisme ou raison clinique, source, limite, état de vérification. Ne déclarer une revue exhaustive que si les quatre onglets, fenêtres, figures, tableaux, quiz, Pareto et glossaire ont effectivement été contrôlés.

## Remise simple, un paquet par cours

Créer les sources natives :
- `chapters/I83/I83_a.html` à `I83_d.html`, puis `I83_pop*.html` ;
- `chapters/I89/I89_a.html` à `I89_d.html`, puis `I89_pop*.html` ;
- `glossary/i83.py` et `glossary/i89.py` ;
- rapports sous `audits/PRODUCTION_CARDIO_2026-10-08/`.

Le contrat réel du modèle I50 prime sur toute approximation : a/b = Pathologie, c = Examens + Sciences, d = Pharmacologie et fermeture du template. Les identifiants et fenêtres sont préfixés i83-/i89-. Les abréviations sont définies lettre par lettre.

Les paquets de remise vont sous :
`livraisons/Livraison Claude/C-01-Cardiologie/production/I83/`
et
`livraisons/Livraison Claude/C-01-Cardiologie/production/I89/`.

Le nouveau protocole `docs/collaboration/NEW_COURSE_DELIVERY.md` et `tools/new_course_delivery.py` sont préparés par Codex pour ces créations : `package`, `check`, puis injection `apply` par Codex. Le format ancien `apply-claude` concerne les cours déjà enregistrés et ne doit pas être détourné pour créer un cours. Si l'outil n'est pas encore dans la tête récupérée, livrer les sources, glossaire, rapport et SHA par PR suffit ; Codex reconstitue le paquet sans perdre la contribution.

Pousser la branche et ouvrir une PR **vers `codex/sciences-cs-fragments-20261007`**. Dans la PR, nommer les cours et fournir : SHA de base, SHA livré, fichiers, périmètre couvert, sources vérifiées, commandes réellement exécutées et réserves. Ne pas fournir seulement un HTML généré ni envoyer de secret.

## Réception et injection par Codex

Codex conserve les originaux et empreintes, contre-lit les points sensibles, vérifie les conflits et injecte les sources canoniques et le glossaire. Il enregistre les cours et leurs catégories, reconstruit MEDINA et C-01-Cardiologie, vérifie ordinateur/mobile et fenêtres, publie un reçu et confirme le déploiement. Les réserves médicales restent explicites jusqu'à leur résolution.

Une instruction publiée sur GitHub rend la mission accessible ; elle ne prouve pas que Claude a démarré. Le démarrage et la livraison doivent être attestés par ses commits et sa PR.

