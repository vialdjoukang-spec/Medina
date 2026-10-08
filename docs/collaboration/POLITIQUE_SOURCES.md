# Politique des sources MEDINA — 8 octobre 2026 (version 2)

## Instruction de Vial, reformulée pour être applicable

**Objectif.** Chaque affirmation médicale de MEDINA repose sur des sources reconnues en Suisse. Claude Code et Codex doivent respecter cette règle dans chaque branche, chaque chapitre et chaque remise, sans dépendre de leur mémoire.

**Règle.**
0. **Exactitude médicale de la ressource : OBLIGATOIRE.** La source citée est la version en vigueur, réellement lue ; l'affirmation reproduit fidèlement ses chiffres, seuils, recommandations et niveaux de preuve. Cette exactitude se vérifie à la rédaction puis à l'audit croisé ; le contrôle automatique ne la prouve pas.
1. **Sources suisses d'abord (A)** : Swissmedic et FI (`ref/fi/`), OFSP, ASSM, sociétés savantes suisses, universités et hôpitaux universitaires suisses, Swiss Medical Weekly.
2. **Puis sources européennes applicables en Suisse (B)** : ESC, ERS, EMA, ECDC, ESCMID, EASL, ESMO, EULAR, etc.
3. **Recommandations et classifications internationales utilisées en Suisse (C)** : KDIGO, NICE, OMS/CIM, GINA, GOLD, Surviving Sepsis Campaign, critères ACR, etc. Elles passent **sans dérogation**, même si elles ne sont pas suisses (instruction de Vial du 8 octobre 2026).
4. **Recherche indexée (J)** : PubMed, Europe PMC, revues. Elle est acceptée si le champ `origine` déclare `CH` ou `EU`.
5. **Toute autre source (X)**, par exemple CDC ou DailyMed, exige un champ `derogation`. Ce champ explique pourquoi aucune source A ou B ne suffit.
6. **Médicaments** : aucune posologie, interaction ou contre-indication sans vérification dans `ref/fi/`.

La liste des domaines se trouve dans `organisation/sources_policy.json`. Elle est **proposée** et doit être validée par Vial. On l'élargit en modifiant ce seul fichier.

## Pourquoi la demande initiale a été reformulée

| Demande initiale | Limite | Réalisation faisable |
|---|---|---|
| Un code qui se réplique partout | Des copies de code divergent et un code auto-réplicant est dangereux | Un seul code central (`tools/sources_guard.py`) et des **pointeurs** de trois lignes déposés automatiquement |
| Exiger que Codex et Claude obéissent | Aucun fichier ne contraint techniquement une IA | Consigne lue au démarrage (`CLAUDE.md`, `AGENTS.md`) et **contrôle bloquant** en CI et au commit |
| Vérifier que la source est suisse ou européenne | L'origine d'une étude PubMed n'est pas lisible automatiquement | Liste de domaines et origine **déclarée** (`origine`), relue à l'audit croisé |
| Appliquer la règle à tout l'existant | Les écarts historiques bloqueraient tout | Les écarts historiques sont figés dans `organisation/sources_baseline.json` ; seuls les **nouveaux** écarts bloquent |

## Mécanismes d'application

| Déclencheur | Action |
|---|---|
| Ouverture d'une session Claude Code | Crochet `SessionStart` : dépôt des pointeurs manquants et rappel de la règle dans le contexte |
| Écriture d'un fichier par Claude Code | Crochet `PostToolUse` : pointeur déposé dans tout nouveau chapitre ou dossier de remise |
| Création ou changement de branche, commit local | Crochets git `post-checkout` et `pre-commit` (activation : `python3 tools/sources_guard.py install`) |
| Push sur toute branche, toute PR | Workflow `sources_guard.yml` : échec si une source nouvelle est hors politique ou si un pointeur manque |
| Codex | Lit `AGENTS.md` et subit le même contrôle CI ; c'est la seule contrainte réelle sur Codex |

## Commandes

`python3 tools/sources_guard.py check` contrôle les sources. `scaffold` dépose les pointeurs. `reminder` affiche la règle. `install` active les crochets git. `baseline` fige les écarts actuels : réservé à l'héritage, sur décision de Vial.

Cette politique ne remplace pas la validation médicale. Un contrôle automatique prouve la provenance déclarée, pas l'exactitude du contenu.
