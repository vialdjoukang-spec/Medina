# Jauges et réserves des captures — instruction Vial, 15 octobre 2026

Vial demande de corriger les blocages visibles dans ses trois captures Claude.
Cette proposition est technique et ne réécrit pas les leçons ou leurs preuves.

## Compteurs dans les chats Claude

Après chaque changement d'état pertinent, exécuter depuis le dépôt :
`python3 tools/medina_resume.py --chat-progress`, puis présenter ses jauges à Vial
dans le chat de la session concernée. La ligne d'état utilise
`--status-line` ; le hook SessionStart, les autorisations et les autres réglages
Claude existants sont conservés.

Ne pas répéter une valeur historique figée telle que «8/120» en la présentant
comme une mesure actuelle. Ne pas confondre :
- les cours intégrés au catalogue local et un site public effectivement vérifié ;
- les statuts déclarés dans le registre et les contrôles réellement effectués ;
- la Tétrade1–30 (120leçons), ses9lots Novo futurs (108leçons), Betta31+
  et Novo Betta42–125 (1001leçons) ;
- les43transferts avec deux productions distinctes.

Le registre Claude peut ne pas contenir le Cycle1 : ne pas convertir son total
partiel en total publié sur120. Les codes du cycle actif et les états manquants
restent visibles. Le lecteur des registres ne peut pas certifier un site distant
ni piloter à distance l'affichage d'un chat Claude.

## Images D62 : originaux nécessaires

À la coupure `a5b81ffabde72b87e5e373920ee6cda4937897e6` de
`claude/vibrant-johnson-7k5okg`, l'arbre distant complet (10699entrées, non
tronqué) ne contient aucun chemin D62, ni dossier source CYCLE_04/05/06.
La capture annonçant une rédaction terminée n'est pas une remise accessible.

Claude conserve son travail en cours. Pour permettre la vérification des cinq
images D62, publier les originaux sur sa propre branche et transmettre :
- chemin et SHA-256 exacts du fichier employé ;
- page originale Commons `File:…` et URL du fichier original ;
- auteur, licence/statut revendiqué, version et URL de licence ;
- fichier ATTRIBUTIONS.json, preuve d'image et adaptations/recadrages éventuels.

Aucune licence n'est déclarée valide ou invalide sans les fichiers et les pages
correspondantes. Une indisponibilité429 ne devient ni un refus définitif ni une
preuve positive. Ne pas remplacer arbitrairement une illustration clinique.
Un commentaire dans une PR signale la disponibilité au soutien technique ;
une poussée sans PR ne déclenche pas à elle seule cette veille.

## Publication

Le chargeur récursif a été corrigé et fusionné par PR101. Les publications
nécessitent encore le succès effectif du déploiement et leurs preuves propres :
ne pas déclarer E05, N04 ou D69 publiées d'après une file ou un simple build.
Préserver la chaîne active de Claude ; pas de publication concurrente ni
annulation d'un run fonctionnel. Les observations médicales N02 rapportées
dans les captures ne sont pas une nouvelle relecture clinique Codex.

