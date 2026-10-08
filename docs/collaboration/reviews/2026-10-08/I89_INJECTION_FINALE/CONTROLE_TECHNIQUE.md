# Injection finale I89 — contrôle bloqué

**I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie) : non admissible sous la condition technique obligatoire actuelle.** Source `04cb95729d44648cc65339f28cf6631574babbb2`, contrôle sur main `61a841b3c96b3bd4f3ad58ec5870d06945e63292`, constat `2026-10-08T15:44:56.930074+02:00`. Tentative arrêtée ; aucune injection, aucun Git ou canonique modifié.

`tools/livraison.py check-claude` a terminé avec le code 2 avant tout overlay :

```text
Livraison interrompue : Code ou titre de cours incohérent : {'code': 'I89', 'title': 'Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques', 'covers': ['I89', 'I97'], 'owner_fragment': 'S01'}
```

La cause est le contrat du checker : son catalogue contient seulement les cours déjà intégrés, et I89 n’y figure pas. Le message générique ne prouve pas que le titre médical soit erroné. Le code lu limiterait ensuite les fichiers aux chemins `chapters/<code>/<fichier>` ; catalogue, glossaire et test de cette création n’entrent pas dans ce contrat. Ce second obstacle est une lecture de code, pas un autre contrôle exécuté. Aucun manifeste, catalogue ni checker n’a été modifié pour obtenir un résultat favorable.

Inspection documentaire indépendante : 11/11 empreintes proposées conformes, neuf ajouts absents, deux empreintes de remplacement conformes à main. Huit HTML sans contenu actif, quatre panneaux, 43 fenêtres natives, 45 clés de glossaire aux arguments littéraux ; aucune collision d’ID/fenêtre dans le chapitre. Le glossaire n’a pas été importé. Le catalogue proposé ajoute seulement I89, avec ses rattachements I89/I97, de 32 à 33 cours globaux.

Le fichier et le diff complets de `verify_s01_browser.cjs` ont été lus : une seule attente passe de 21 à 22 cours. Toutes les autres assertions et boucles restent identiques ; la boucle des cours inclurait I89. Aucune assertion I97 spécifique n’est ajoutée. Le test entrant n’a pas été exécuté. Les objets applicatifs sélectionnés de main 61a841b et HEAD 5f04f5d sont identiques.

Conformément à la demande d’arrêt si une condition obligatoire échoue, aucun build, audit des fragments, test natif, unitaire ou navigateur de ce candidat n’est lancé. Les résultats producteurs du manifeste ne sont pas attribués à cette sentinelle. A41 canonique reste inchangé ; J45 reste non injecté.

[CONTROLE_TECHNIQUE.json](CONTROLE_TECHNIQUE.json) conserve les commandes, horaires Europe/Zurich, empreintes, chemins et limites. Preuves externes : `/workspace/medina-env/reprise-i89/injection-finale/controls`. Aucun contournement ; tentative close avec ce blocage.
