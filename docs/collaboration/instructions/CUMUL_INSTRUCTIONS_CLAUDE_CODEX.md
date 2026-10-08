# MEDINA — Cumul des instructions en vigueur pour Claude Code et Codex

Version du 8 octobre 2026, établie par Claude Code à la demande de Vial. Ce document rassemble en un seul endroit **toutes les instructions valides** dispersées dans le dépôt. Il s’applique à parts égales à Claude Code et à Codex. En cas de conflit, la règle la plus récente l’emporte. Si deux règles de même date divergent, la plus exigeante pour la qualité s’applique. Les documents sources restent la référence de détail ; ce cumul en donne l’état consolidé.

## 0. Message de Vial à Codex (8 octobre 2026)

- « Tu es dans un fragment. Fais progressivement pour éviter de doubler le travail de Claude Code. »
- « Prends connaissance des principales règles et instructions rendues disponibles par Claude Code et applique le cumul de ses instructions. »
- « Confirme-moi lorsque tu détecteras tout le cumul des instructions livré par Claude Code, pour que tu te mettes à la page. »
- Codex confirme en remplissant la liste de contrôle de la section 12, sans écrire de phrases étranges : français professionnel, phrases complètes, contenu vérifiable.

## 1. Organisation : 22 fragments, catégories, chapitres

- L’atlas compte exactement **22 fragments**, organisés **Fragment → Catégories → Chapitres**. Registre : `organisation/fragments.json`, `organisation/production_plan.json`, `COORDINATION.md`.
- **Claude** : C-01-Cardiologie (achevée et remise), puis P-02, G-04, E-06, H-08, G-10, M-12, R-14, O-17, O-18, M-19, E-22.
- **Codex** : I-03-Infectiologie (actif), puis N-05, N-07, O-09, O-11, I-13, U-15, D-16, D-20, M-21.
- Nommer un fragment par **initiale - ordre - nom littéral** (`C-01-Cardiologie`) et un cours par **code — intitulé (libellé complet du fragment)**, par exemple **J45 — Asthme (P-02-Pneumologie)**.
- **Ne jamais doubler le travail de l’autre IA** : vérifier la pile (`organisation/PILE_FRAGMENTS.html`), les espaces de remise et les zones de travail avant d’ouvrir un cours. Un cours existant ou déposé est repris, pas réécrit en parallèle.

## 2. Processus continu

- Aucune IA n’attend qu’on lui demande de continuer. Arrêt seulement quand tous ses fragments sont remis, ou sur **STOP** explicite de Vial.
- Une correction demandée par Vial passe en priorité absolue, est livrée, puis la production reprend en arrière-plan.
- Arrêt global après les 22 fragments rédigés, auto-revus, audités et injectés.

## 3. Complétude CIM sans lacune

- **Toutes les catégories CIM** rattachées à un fragment reçoivent un cours fondé sur la CIM, seul ou regroupé dans un cours déclaré (`covers`). Aucune catégorie sans cours.
- Chaque sous-code CIM-10-GM 2024 est vérifié sur klassifikationen.bfarm.de et traité ou renvoyé explicitement.
- La cible finale reste la **CIM-11** : sa complétude n’est déclarée qu’avec l’inventaire officiel versionné ; un catalogue CIM-10-GM ne la prouve pas.

## 4. Production par fragment, audit croisé unique, injection

- Unité de remise : **fragment entier complet et auto-revu** (inventaire catégorie → cours, fichiers et empreintes SHA-256, rapport, sources, contrôles).
- **Claude audite les fragments Codex ; Codex audite les fragments Claude.** Un seul tour : l’auditeur corrige lui-même, injecte dans le canonique et reconstruit.
- **Le producteur n’écrit jamais dans le canonique** (`chapters/`, `glossary/`, `chapters.json`). Ses cours vivent dans `livraisons/Livraison <IA>/<fragment>/travail/sources/`, puis dans `espace_partage/FRAGMENTS_<IA>_A_AUDITER_PAR_<autre>/<fragment>/` (REMISE.md, MANIFESTE.json, `sources/`, `chapters_additions.json`). La garde CI `tools/espace.py garde` le vérifie.
- Statut **INJECTÉ** : immuable. Aucun fragment incomplet transmis ni injecté.
- **Remise en cours** : C-01-Cardiologie (76/76 catégories, 30 cours) attend l’audit de Codex dans `espace_partage/FRAGMENTS_CLAUDE_A_AUDITER_PAR_CODEX/C-01-Cardiologie/`.

## 5. Parallélisme

- Mode multi-agent obligatoire : plusieurs sous-agents en parallèle, **un par catégorie** (ou cours regroupé) du fragment actif.
- **Un auteur par fichier.** Un intégrateur unique tient les registres de travail, la pile et les reconstructions.
- La préparation du fragment suivant (inventaire, pile, recherches) peut commencer pendant l’audit du précédent ; elle ne rouvre jamais un fragment INJECTÉ.

## 6. Contenu d’un cours

- Contrat HTML : `chapters/<CODE>/<CODE>_a.html` à `_d.html` et `_pop*.html`, `<template id="ch-<CODE>">`, **quatre onglets** (Pathologie et prise en charge, Examens complémentaires, Sciences fondamentales spécialisées, Pharmacologie), identifiants préfixés par le code en minuscules, classes de la liste fermée. Modèles : I48, J45, I50.
- Pathologie : cas fil rouge, définitions et classifications, épidémiologie, physiopathologie avec figure SVG, étiologies, anamnèse, examen (normal avant pathologique), démarche diagnostique avec algorithme, urgences, traitement, suivi, situations particulières.
- **Pareto « perfectit »** à la fin de chaque grande partie. **Dernier îlot** : critères formels du diagnostic (`div.alert`) puis paramètres clés (`div.key`).
- Examens : au moins trois quiz. Sciences : corrélations anatomo-physio-cliniques. Pharmacologie : doses suisses, interactions, contre-indications.
- Abréviations : aucune sans clé dans `glossary/<code>.py`, définition lettre à lettre ; `build_medina.audit()` renvoie `{}`.

## 7. Justification et sources

- **Justifier chaque affirmation** : mécanisme causal, conséquence clinique, limites, source primaire datée. Ne pas confondre association et causalité.
- Sources suisses d’abord (sociétés savantes, OFSP, Swissmedic, monographies Compendium lues et datées), puis européennes et internationales acceptées en Suisse. Aucun chiffre ni posologie inventés ; distinguer accès impossible, résumé et texte intégral.
- **Contentieux** : la source primaire applicable la plus récente l’emporte, présentée dans une fenêtre liée à un **mot vert**, avec accès au texte en vigueur même plus ancien.
- Revue IA, tests automatiques et validation par un médecin ne sont jamais assimilés. Statut affiché : « non validé par une revue humaine ».

## 8. Rédaction

- `docs/STYLE_REDACTION.md` : le lecteur comprend, il ne devine pas. Phrases courtes et complètes, jamais nominales ni à l’infinitif injonctif ; annonce, développement, épilogue « À retenir » ; tableaux introduits et commentés.
- **Tout évoquer sans bavardage** : chaque phrase apporte une information, un mécanisme ou une décision. Aucun remplissage, aucune répétition, aucun plafond de mots.
- Pas de métaphores, jeux de mots ni plaisanteries ; exemples chiffrés. Une annonce expose le problème médical, jamais la fabrication du cours.
- Les explications détaillées s’ouvrent dans une fenêtre au clic sur le mot interactif ; tableaux pour classifications et énumérations, cellules courtes et cohérentes.

## 9. Frontend

- Un HTML et une navigation propres à chaque fragment, limités à sa spécialité (`fragment_surface.py`).
- **Thème clair exclusif**, contrastes élevés, police par défaut **Atkinson Hyperlegible Next** embarquée ; réglages de police et de taille du lecteur conservés ; une couleur vive par spécialité et par catégorie.
- **Bouton « Isolate Federal – CH Exam »** dans chaque fragment : les catégories restent, les chapitres de pratique quotidienne et d’examen fédéral passent en poudre d’or. Liste centralisée `organisation/federal_exam.json`, que chaque producteur complète pour ses fragments.
- **Sémiologie CS** pour chaque fragment où l’examen clinique s’applique : module `modules/<nom>_cs.{html,css,js}` déclaré dans `modules/cs_registry.json`. Le module respiratoire est prêt en zone de travail P-02.

## 10. Visibilité et traçabilité

- **Captures d’écran réelles** (ordinateur et mobile) à chaque livraison, montrées dans la conversation.
- **Pile visible** des fragments actifs et suivants, avec toutes leurs catégories et leçons : `organisation/PILE_FRAGMENTS.html`, régénérée par `tools/pile_fragments.py`.
- Accusé de chaque remise, audit et injection dans `docs/collaboration/receipts/`. Recenser branches et PR (`tools/collaboration_sync.py`) avant toute conclusion sur les livraisons.
- Tableau de bord en fin de livraison : cours, catégories, fragment, poids, alertes.

## 11. Documents sources de ce cumul

`CLAUDE.md`, `AGENTS.md`, `COORDINATION.md`, `docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md`, `docs/collaboration/instructions/CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE.pdf`, `docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md`, `docs/collaboration/FRONTENDS_2026-10-08.md`, `docs/STYLE_REDACTION.md`, `CHAPTER_SPEC.md`, `PROMPT_MEDINA.md`, `docs/COMPLETUDE_CIM11.md`, `docs/collaboration/DELIVERY_PROTOCOL.md`.

## 12. Liste de contrôle d’alignement (à confirmer par Codex)

Codex crée `docs/collaboration/receipts/CODEX_ALIGNEMENT_CUMUL_2026-10-08.md` et y confirme chaque point par « lu et appliqué », avec le commit lu :

- [ ] 1. 22 fragments, attribution et nommage ; aucune duplication du travail de Claude.
- [ ] 2. Processus continu ; STOP seul arrêt ; corrections prioritaires.
- [ ] 3. Complétude CIM sans lacune, cible CIM-11.
- [ ] 4. Fragment entier, audit croisé unique, producteur hors canonique, INJECTÉ immuable ; audit de C-01-Cardiologie à conduire.
- [ ] 5. Sous-agents par catégorie, un auteur par fichier.
- [ ] 6. Contrat HTML, quatre onglets, Pareto, dernier îlot, glossaire.
- [ ] 7. Justification, sources suisses datées, contentieux par mot vert, aucune validation humaine présumée.
- [ ] 8. Style : phrases complètes, sans bavardage.
- [ ] 9. Frontend clair, Atkinson, bouton fédéral, Sémiologie CS.
- [ ] 10. Captures, pile visible, accusés, tableau de bord.
