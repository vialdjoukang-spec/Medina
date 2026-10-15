# Reprise MEDINA — état dynamique, 15 octobre 2026

Ce fichier est un point d'entrée, pas une photographie figée de l'avancement.
Claude et chaque agent lisent **d'abord**
`docs/collaboration/betta/PROMPT_VERITE.md` avant d'ouvrir une leçon ; appliquer
sa porte documentaire avant rédaction. Lire aussi les instructions actuelles
de `CLAUDE.md` et `AGENTS.md`. Aucun résultat ou contrôle non réalisé n'est réputé acquis.

## État réel avant toute action

Exécuter `python3 tools/medina_resume.py`. Ce relevé local en lecture seule distingue :

- la séquence Tétrade 1–30 : 120 leçons prévues, entrées canoniques déclarées dans
  `chapters.json`, états du registre `organisation/CYCLES_CLAUDE.json` ;
- Novo **Tétrade** : `organisation/novo_12/PLAN_NOVO_12.json`, neuf lots de douze
  couvrant les anciens cycles 4–30, sans modifier leurs attributions ;
- Betta **31+** : `organisation/betta_status.json`, production distincte. Son propre
  Novo **42–125** a son propre `organisation/novo12_status.json` ; les 43 transferts
  ne se comptent pas deux fois. Ce n'est ni Novo Tétrade ni la jauge des 120 leçons.

Une entrée au catalogue n'est pas une preuve de publication. `PUBLIE_VERIFIE`
est un état enregistré, pas une nouvelle vérification publique par cet outil.
Les fichiers manquants ou invalides sont signalés « indisponibles », jamais assimilés
à zéro progression. Comparer ensuite les têtes distantes de main et de la branche
de travail actuelle, les reçus et le déploiement réellement réussi.

## Reprendre sans écraser

Terminer la publication du Cycle 3 **selon ses états courants dans le registre** :
ne pas recommencer une injection ou un contrôle déjà enregistré sur la même version.
Préserver les cours, reçus, empreintes et contributions concurrentes ; ne pas modifier
le cycle actif pour le convertir en lot Novo. Les audits médicaux indépendants restent
suspendus jusqu'à nouvel ordre ; sources et contrôles techniques réels restent tracés.
Un seul cycle/lot actif par IA responsable ; un auteur par fichier. La chaîne
`.claude/skills/cycle-medina/SKILL.md` et les gardes actuelles restent applicables.
Les choix de modèles existants de Claude sont conservés.
Le distributeur `.claude/skills/agent-distributor/SKILL.md` et
`tools/distributor_veille.py` restent disponibles. Les revues auteur sont réellement
datées après le démarrage de leur lot ; ne jamais réécrire une date. Chaque injection
actualise l'intégrité du catalogue et ses jauges avec les outils prévus.

Transmettre aussitôt tout refus reproductible à Codex dans la **PR courante** avec
`[CLAUDE->CODEX][BLOCAGE]`, SHA et reproduction. Une copie dans l'issue 97 reste utile,
mais ne déclenche pas à elle seule le soutien. Lire
`docs/collaboration/instructions/SOUTIEN_TECHNIQUE_CLAUDE_2026-10-15.md`.

Après Cycle 3 réellement `CLOTURE`, l'option autorisée est :

```bash
python3 tools/cycle_claude_stage.py novo 1 --runtime ID_REEL
```

Lire `docs/collaboration/instructions/NOVO12_EXECUTION_VIAL_2026-10-15.md`
avant exécution. Novo Tétrade 1 est une seule entrée active d'ancre 4, représentant
les anciens cycles 4, 5 et 6 et douze leçons ; le lot suivant a l'ancre 7.
Employer l'identifiant réel de session, sans inventer de preuve ou de lecture.

L'ancien `tools/claude_chaine_main.sh` est désactivé : il reconstruisait main depuis
des arbres historiques et pouvait écraser des contributions nouvelles. Utiliser
la branche réelle et une réconciliation Git préservant l'historique ; aucun
force-push ni ancien arbre substitué à main. Les protections et permissions
effectives GitHub restent applicables.

## Jauge et compte rendu

La ligne d'état `medina_resume.py --status-line` présente séparément les 120 leçons
de la Tétrade, Betta historique et Novo Betta. Ne pas afficher une jauge
historique fixe comme état actuel ni confondre « canonique », « livré », « injecté »
et « publié ». Un compte rendu reste concis, avec les faits nouveaux, les liens
vérifiés et les réserves réelles.
