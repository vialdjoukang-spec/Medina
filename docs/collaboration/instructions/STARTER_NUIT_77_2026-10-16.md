# Ordre Vial — Starter nocturne, partage équitable et STOP 77

Date de transmission : 16 octobre 2026, Europe/Zurich.
Destinataires : Codex et Claude Code, chacun responsable de son propre runtime et de ses agents.
Statut à la transmission : ORDRE_TRANSMIS ; renforcement du code et exécution des agents NON_CONFIRMÉS.

## Message de Vial, conservé textuellement

```text
Augmente la puissance de ton Starter, actif en permanence toute cette nuit et greffé dans le code tous tes agents, 

Lorsque un Tour s'arrête, le Starter intime l'ordre de Vial de relancer le travail.

Fait le , ensuite ton Starter doit fonctionner 

Merci de lancer cela.

Et STOP au chapitre 77
________

Et le Starter s'active pour vous demander de vous partager équitablement le nombre de leçons restantes...

Puis lancer la production
```

Vial demande que cette instruction soit adressée à Codex et soumise avec insistance à Claude jusqu'à son exécution. Cette transmission ne constitue pas un accusé de réception de l'une ou l'autre IA.

## Exécution demandée aux deux responsables

Lire la tête distante, AGENTS.md, CLAUDE.md, les consignes actuelles du chantier S08/S05/S04/S06 et le contrat MOTEURS_INDEPENDANTS_7_STARTER_2026-10-15.md. Réutiliser le Starter existant plutôt que créer une seconde chaîne concurrente. Codex et Claude restent à égalité ; aucune validation préalable de Codex n'est imposée à Claude.

Renforcer et tester effectivement le mécanisme de reprise dans le code : point de reprise persistant, événement de fin de tour, détection d'une interruption, reprise sur l'état réel, protection contre le double lancement et journal des agents réellement exécutants. Mobiliser les agents effectivement disponibles dans chaque environnement, avec missions et fichiers distincts ; aucun agent fictif, aucune multiplication récursive sans limite et aucun écrasement d'un travail concurrent.

Lorsqu'un tour s'arrête avant la borne autorisée, le Starter doit présenter l'ordre de reprise de Vial et utiliser un canal d'exécution réellement disponible. Si le lot est inachevé, reprendre ce lot ; ne pas déclarer sa clôture pour démarrer le suivant. Si le lot est réellement clôturé, vérifier ses preuves puis démarrer le suivant selon le contrat. Une fin de message, un rapport poussé ou une réservation libérée ne prouvent pas une clôture.

Vérifier en priorité le canal d'exécution. La PR #143 documentait un backend natif dépendant d'un coordinateur actif et un échec de rafraîchissement du jeton CLI. Recontrôler cet état : ne pas le supposer encore bloqué, mais ne pas supposer sa réparation. Un commentaire GitHub, un workflow d'inventaire ou un heartbeat synthétique ne remplace pas une session exécutante. En cas d'authentification ou de quota bloquant, conserver le checkpoint et le diagnostic ; ne jamais publier de jeton ni contourner une permission.

## Borne 77 et partage du reliquat

Conserver le plafond 77 du chantier Starter concerné, premier lot inclus. Ne pas confondre ce rang avec le code CIM C77. Ne pas remettre le compteur à zéro, créer 77 tâches supplémentaires ou démarrer un rang 78 dans cette campagne.

Avant de lancer la production demandée, publier l'inventaire réellement restant : code, intitulé, statut, responsable, mission et branche. Séparer clairement audit/correction et production nouvelle. Le plan historique distingue 52 audits et 77 productions par IA ; la file Starter Codex observée contient 52 cours existants et 25 productions. Ces nombres ne sont pas interchangeables.

Partager équitablement le reliquat de production entre Codex et Claude : écart maximal d'une leçon pour les nouvelles attributions. Préserver les travaux déjà en cours ; tout transfert nécessaire doit être explicite et atomique dans le registre, sans deux auteurs simultanés. Utiliser le manifeste canonique et nommer exactement les leçons attribuées. Le partage et la production ne valent pas extension implicite au-delà du STOP 77 ; si la portée des compteurs ne concorde pas, consigner l'écart et avancer uniquement dans le périmètre déjà non ambigu.

## Nuit concernée et contrôle d'arrêt

La demande arrive le 16 octobre à environ 02 h 15, heure suisse : la nuit concernée est celle du 15 au 16 octobre 2026. Pour la relance programmée depuis ChatGPT, la borne technique retenue est le 16 octobre 2026 à 08 h 00 Europe/Zurich (06 h 00 UTC), sauf arrêt plus tôt. Ce choix opérationnel n'est pas une heure citée par Vial.

Tout nouvel ordre STOP/PAUSE de Vial ou `/medina off` sur le fil de contrôle #97 prévaut immédiatement sur les relances. Aucun mécanisme ne doit redémarrer après un arrêt volontaire. À la borne 77, désactiver la relance de cette campagne et conserver les preuves. À la fin de la fenêtre nocturne, sauvegarder et suspendre les relances nocturnes ; ne pas prolonger silencieusement le mandat.

## Preuves attendues dans le fil de transmission

Chaque IA répond avec son identité déclarée, sa session/job réel, la branche et le SHA, le manifeste et le compteur employés, les agents effectivement lancés, le lot repris et le premier résultat vérifiable. Pour le Starter renforcé : fournir le commit du code, les tests réellement exécutés, le canal de déclenchement et une preuve de reprise après un arrêt non volontaire, sans simuler un succès.

Distinguer les états ORDRE_TRANSMIS, REÇU, EN_COURS, BLOQUÉ et TERMINÉ. Un simple « reçu » ne prouve ni le renforcement du Starter ni le lancement de la production. En cas de panne persistante, diagnostiquer plutôt que multiplier les mêmes appels. Les relances externes doivent être bornées et dédupliquées ; elles ne doivent pas interrompre un agent dont l'activité est vérifiée.

Les exigences médicales, de sémiologie, de provenance des images, de traçabilité et les contrôles réellement applicables restent inchangés. Ce document ne modifie aucun contenu médical et ne prétend pas activer un moteur à lui seul.
