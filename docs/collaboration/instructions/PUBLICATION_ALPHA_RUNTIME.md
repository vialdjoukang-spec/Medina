# Publication Alpha : texte accessible par la navigation du cours

La garde reconnaît le template unique `ch-CODE` du cours demandé. Elle extrait son texte initial et celui des seuls panneaux locaux rendus accessibles par les boutons `data-p` de `.tabs`, puis `data-s` de `.sci-bar` dans `pS`. Une cible doit être unique, de classe `panel` ou `sci`, et `aria-controls`, si présent, doit correspondre. Le runtime de référence est `engine/medina_course.js` ; cette analyse statique ne remplace aucun contrôle réel du navigateur.

Une feuille CSS embarquée ou liée active dans le contexte du cours rend la preuve statique indisponible : aucune visibilité calculée n’est inventée. Les dialogues fermés et les masquages inline explicites sont exclus. Les classes de navigation doivent utiliser la syntaxe effectivement transformée par le constructeur. Les cibles imbriquées dans un autre panneau de même type sont refusées, car le runtime masque leur parent.

Les scripts, styles, templates étrangers ou imbriqués, contrôles masqués/désactivés et cibles inaccessibles restent exclus. Une racine de cours absente, dupliquée ou imbriquée ne permet pas de fournir une réserve extérieure. Les fixtures historiques sans template de cours conservent leur extraction générique ; aucun contenu de template arbitraire ne devient une preuve.

Les réserves provisoires, blocages MED/LANG et attributions sont recherchés dans ce texte accessible. Les six parties HTML sont concaténées dans l’ordre déterministe `a`, `b`, `c`, `d`, `pop1`, `pop2`. Les droits, octets originaux, preuves visuelles, empreintes des rapports, reçus et gardes historiques restent requis. Une publication `provisional` ne clôture aucune leçon et ne vaut jamais validation médicale humaine.

Validation : `python3 -m unittest tests.test_alpha_publication`. Les cas de régression couvrent les onglets imbriqués, réserves, crédits, cibles étrangères/dupliquées, ARIA incohérent, contrôle masqué et templates étrangers. Les versions réelles N17/I63/E10 conservées au relais sont également comparées sans nouvelle affirmation médicale.

## Inventaire GitHub et quota de publication

Le run Pages `38810149213` a réussi sa construction, puis son déploiement a échoué en HTTP403 : « API rate limit exceeded for installation ». L’inventaire complet des branches et PR, avec leurs comparaisons, consomme de nombreuses lectures API. Pour réduire cette pression répétitive, seul le step réseau « Repérer toutes les branches et pull requests » de `collaboration.yml` est réservé au déclenchement manuel `workflow_dispatch`.

Les tests du scanner restent exécutés sur chaque push et PR. Les rapports et artefacts disponibles sont conservés. Les gardes mission, Alpha et historique, la suite technique et Pages restent inchangés ; aucun droit, secret ou proxy n’est modifié. Ce correctif ne réinitialise pas le quota et ne garantit pas la réussite immédiate d’un déploiement : respecter les limites et éventuels `Retry-After`.

À chaque reprise manuelle du chantier, l’inventaire complet distant reste obligatoire, avec pagination des branches et PR et lecture des contributions : `python3 tools/collaboration_sync.py --integration-branch main --out work/collaboration-reprise`. Le workflow peut aussi être lancé explicitement pour produire son rapport. Un rapport partiel conserve ses réserves ; l’absence de rapport automatique sur un push ou une PR n’établit aucune absence de livraison.
