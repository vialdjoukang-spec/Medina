# Publication Alpha : texte accessible par la navigation du cours

La garde reconnaît le template unique `ch-CODE` du cours demandé. Elle extrait son texte initial et celui des seuls panneaux locaux rendus accessibles par les boutons `data-p` de `.tabs`, puis `data-s` de `.sci-bar` dans `pS`. Une cible doit être unique, de classe `panel` ou `sci`, et `aria-controls`, si présent, doit correspondre. Le runtime de référence est `engine/medina_course.js` ; cette analyse statique ne remplace aucun contrôle réel du navigateur.

Les scripts, styles, templates étrangers ou imbriqués, contrôles masqués/désactivés et cibles inaccessibles restent exclus. Une racine de cours absente, dupliquée ou imbriquée ne permet pas de fournir une réserve extérieure. Les fixtures historiques sans template de cours conservent leur extraction générique ; aucun contenu de template arbitraire ne devient une preuve.

Les réserves provisoires, blocages MED/LANG et attributions sont recherchés dans ce texte accessible. Les six parties HTML sont concaténées dans l’ordre déterministe `a`, `b`, `c`, `d`, `pop1`, `pop2`. Les droits, octets originaux, preuves visuelles, empreintes des rapports, reçus et gardes historiques restent requis. Une publication `provisional` ne clôture aucune leçon et ne vaut jamais validation médicale humaine.

Validation : `python3 -m unittest tests.test_alpha_publication`. Les cas de régression couvrent les onglets imbriqués, réserves, crédits, cibles étrangères/dupliquées, ARIA incohérent, contrôle masqué et templates étrangers. Les versions réelles N17/I63/E10 conservées au relais sont également comparées sans nouvelle affirmation médicale.
