# I48 — Fibrillation et flutter auriculaires : contre-relecture du lot Claude 8ce3e99

Relecture ciblée des deux propositions `I48_pop3.html` et `I48_pop4.html`, comparées aux originaux b6 et au canonique contre-corrigé après la fusion bibliographique du commit `9a77d27`. Le lot reçu comprend d’autres cours ; ils ne sont pas examinés dans cette sous-tâche.

**Décision : deux harmonisations cliniques ponctuelles sont proposées.** Le delta 8ce → b6 n’est pas exclusivement bibliographique. Il reprend surtout des corrections déjà présentes dans le canonique, dont la digoxine intraveineuse lente. Les deux apports encore absents du canonique précisent la règle et l’exception limitée d’anticoagulation après cardioversion dans une fenêtre explicative et dans le Pareto de physiopathologie.

## Originaux comparés

| Fichier reçu dans le lot 8ce3e99 | SHA Git du blob vérifié | SHA-256 |
| --- | --- | --- |
| `I48_pop3.html` | `9789990f5ddad3b0b6b728397b332249b75fe440` | `693446c5491de348fcc7d7c09f6c7bfedc3d8d7467905fea0b6be8d9462dee4f` |
| `I48_pop4.html` | `9547ae58ab9d112848aa7b26f5b469e52b5f3b04` | `cbb78cd5b17eacac2849823b8673eab9e6b0439d4b858806c1fea4de4b69eb32` |

Les deux SHA Git correspondent exactement aux valeurs transmises lors de la réception. Les propositions examinées sont sous `/workspace/scratch/6eaecafb4b19/latest_claude_8ce/originals/chapters/I48/`. La référence b6 est l’archive immuable `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07_B6DB50C_RECEPTION/nouvelles_propositions_I48/`.

## Inventaire du delta b6 → 8ce

| Fichier et fenêtre | Changement reçu | Décision de fusion |
| --- | --- | --- |
| `pop3 / i48-laao` | Remplacement du lien causal attribué aux risques résiduels de CHAMPION-AF par une distinction entre non-infériorité composite, saignement et AVC isolés. | Conserver le canonique : la limite causale et celle du critère composite y sont déjà explicites. |
| `pop3 / i48-24h` | Remplacement de « toute cardioversion » par la stratégie habituelle et l’exception individualisée de faible risque avec début certain et conversion précoce. | Conserver le canonique : il comporte déjà cette exception et attribue les délais de récupération et le chiffre de 98 % à leurs cohortes respectives. Le texte reçu conserve les généralisations sur la récupération auriculaire que le canonique a retirées. |
| `pop3 / i48-eto` | Ajout de l’exception limitée après cardioversion. | Conserver le canonique : il distingue déjà l’absence de thrombus visible de l’absence de risque ultérieur, et précise qu’une ETO normale ne constitue pas seule l’exception. |
| `pop3 / i48-rs-embolie` | Remplacement de « prescrite après toute cardioversion » par « habituellement prescrite après cardioversion », avec renvoi à la règle et à l’exception de la fenêtre des 24 heures. | **Reprendre cette seule ligne.** Elle corrige une contradiction résiduelle avec `i48-24h` sans changer l’explication du risque embolique au long cours. |
| `pop4 / pareto-i48-physio` | Ajout des conditions de l’exception dans l’item sur la sidération après cardioversion. | **Reprendre ce seul item de liste.** La règle habituelle d’au moins quatre semaines reste présente. |
| `pop4 / pareto-i48-pharma` | Remplacement du bolus de digoxine par l’administration intraveineuse lente, dose adaptée comprise. | Déjà identique au canonique. Ne pas remplacer toute la liste : le canonique conserve en plus la restriction de classe Ic en cas de dysfonction systolique, y compris une FEVG de 41 à 49 %. |
| `pop4 / i48-d-dig` | Dose initiale usuelle adaptée au patient et ajout du paragraphe d’administration HUG. | Déjà identique au canonique pour ces passages. Conserver l’ensemble canonique. |

Au total, `pop3` comporte quatre remplacements de lignes. `pop4` comporte trois remplacements et un ajout de ligne dans des fenêtres existantes. Aucun nouveau template, bouton, identifiant ou mécanisme physiopathologique n’est apporté par ce delta. La fusion sélectionnée est une harmonisation des conditions d’une conduite déjà expliquée.

## Vérification primaire de l’exception

Le texte intégral des recommandations ESC 2024 sur la fibrillation auriculaire a été consulté dans le [PDF reproduisant l’article primaire](https://forening.sls.se/media/kfyncecr/2024-esc-guidelines.pdf), doi:10.1093/eurheartj/ehae176. Le §7.2.1, la figure 12 et le tableau de recommandations 15 ont été lus ensemble, aux pages imprimées 3354–3355, soit les pages 41–42 du PDF.

Le tableau donne la règle générale d’anticoagulation après cardioversion ; le texte et la figure permettent une option limitée lorsque le début est certain, le retour en rythme sinusal précoce et le risque thromboembolique très faible. La fusion conserve donc une stratégie habituelle d’au moins quatre semaines et présente l’exception comme une possibilité individualisée. Elle n’en fait ni une obligation d’arrêter ni une conséquence automatique d’une ETO normale.

Cette vérification confirme la cohérence des deux harmonisations avec les arbitrages antérieurs. Elle ne revalide pas ici toute l’anticoagulation, les sous-critères de CHAMPION-AF ou toutes les indications et doses de digoxine. Les formulations canoniques issues de la contre-relecture du 7 octobre restent la référence pour ces sujets.

## Fusion proposée et conservation

La fusion est construite depuis le canonique courant, en remplaçant une ligne dans `i48-rs-embolie` et un seul élément `li` dans `pareto-i48-physio`. **Tous les autres octets sont conservés.** La comparaison inverse de ces deux substitutions reconstitue exactement les fichiers canoniques de départ.

Elle préserve donc les 61 corrections bibliographiques déjà fusionnées, les noms et titres, les arbitrages sur les cohortes non causales, le seuil de surface mitrale et les AOD, l’individualisation de l’INR, TRAPS, les restrictions de classe Ic et de dronédarone, la pompe sodium-potassium et toute l’administration lente de digoxine vérifiée dans le guide HUG.

| Fichier | SHA-256 canonique avant fusion | SHA-256 de la fusion proposée |
| --- | --- | --- |
| `I48_pop3.html` | `0c58ea49995321aea86d6358573f60c2b96144b29e61d86d5ebba489df5ba6b6` | `7bce4eca85a64bad91bd887f799dcea92ea6f584b6f5de831efcea35fd7a9fa6` |
| `I48_pop4.html` | `6cfc947f383677cf924d70b1b36dfd4d81ccd48f28b2fcfe4f8b914ecc78e913` | `5b56463ede860f3450d52dd0805d42494e0ec5a7a1476edda7e80ca67d17862e` |

Les propositions de fusion sont accessibles dans `/workspace/scratch/6eaecafb4b19/latest_claude_8ce/i48_fusion/` :

- `I48_pop3.html` et `I48_pop4.html` ;
- `fusion_ponctuelle.patch`, limité aux deux substitutions retenues ;
- `fusion_plan.json`, avec les SHA complets avant/après et les textes exacts ;
- `changeliste.json`, avec l’inventaire des apports et les décisions ;
- `I48_pop3.html.b6_to_8ce.diff` et `I48_pop4.html.b6_to_8ce.diff`, pour le delta reçu complet.

L’intégrateur doit vérifier les SHA canoniques avant de reprendre ces fichiers. En cas de modification intermédiaire, les deux substitutions seules doivent être réappliquées au nouvel état. Les originaux reçus demeurent intacts ; aucune régression présente dans leur contexte n’est réintroduite.

## Contrôles et limites

Les assertions locales de comparaison vérifient :

- mêmes ouvertures de templates, dans le même ordre : 29 dans `pop3`, 26 dans `pop4` ;
- mêmes ouvertures de boutons : 5 et 9 ;
- mêmes attributs `data-k`, scripts et blocs SVG ;
- conservation de chaque autre octet, ce qui inclut les questions et réponses éventuelles ;
- SHA Git exacts des deux propositions reçues.

Cette tâche n’a modifié aucun fichier canonique ni aucun moteur. Elle n’a exécuté ni reconstruction globale ni navigateur : ces contrôles reviennent au lot d’intégration après application de la fusion. Elle ne certifie ni l’exhaustivité des justifications médicales, ni les autres cours du lot, ni une complétude CIM-11.
