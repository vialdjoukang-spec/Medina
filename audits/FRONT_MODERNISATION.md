# FRONT_MODERNISATION — phase 2 (26.09.2026)

**Objet** : moderniser et styliser le front-end de Medina partout, sans changer son architecture ni son identité (REPRISE_CLAUDE_CODE.md, phase 2).
**Périmètre technique** : couche `shell/polish.css` et `shell/polish.js` (section « modernisation du front-end (phase 2) » et correctifs de revue) ; `build_front.py` et `build_medina.py` pour deux corrections de construction. La coque d’origine `shell/medina_front.html` n’est pas modifiée ; aucune fonction n’est retirée.

## 1. Principes

- **Identité conservée** : barre latérale verte, Georgia dans les cours, titres et numéros rouges soulignés, texte justifié, insigne fluorescent « 100 % rédigé » (halo pulsé) réservé aux cours achevés ; le vert lime n’est plus employé ailleurs (repère actif, sélection, focus).
- **Thème respecté** : les jetons dérivent des variables du thème actif (`--t1`…`--t4`) ; les 100 palettes du studio de thèmes restent cohérentes.
- **Modernité sobre** : ombres en trois niveaux, rayons homogènes, hiérarchie typographique, micro-animations désactivées par `prefers-reduced-motion` (pseudo-éléments et défilements compris).
- **Accessibilité** : contrastes WCAG 2.2 (≥ 4,5:1 texte, ≥ 3:1 composants) mesurés en clair et en sombre ; focus clavier fin et visible, jamais masqué par les éléments collants ; libellés « ✓ / ✗ » en plus de la couleur dans les quiz.

## 2. Réalisations

| Domaine | Avant | Après |
|---|---|---|
| Barre supérieure | Déclarée collante mais inopérante (`overflow:hidden` de `html`, `body` et `.app`) | Réellement collante (`overflow-x:clip`) ; boutons jamais rognés de 390 à 1 600 px ; atlas ECG en icône et badge masqué aux largeurs intermédiaires |
| Onglets du cours | Défilaient hors de l’écran | Collants sous la barre sur grand écran, libellés entiers, non collants s’ils dépassent 96 px ; changement d’onglet ramené au début du panneau |
| Ancres et focus | — | `scroll-padding-top` mesuré (barre + onglets) : titres et focus clavier jamais masqués |
| Navigo | Bouton flottant recouvrant le texte à droite | Onglet vertical en marge réservée dès 761 px ; bouton en bas sur mobile ; saut correct en mode livre |
| Barre d’outils du cours | Masquée après le repositionnement de 200 px de la coque | Toujours visible à l’ouverture d’un cours (interception du repositionnement) |
| Mode sombre | Absent | Facultatif (bouton, choix mémorisé) ; conversion automatique des couleurs claires codées en dur de la coque, figures et tracés conservés sur papier blanc, jauges et anneaux préservés |
| Insignes | Un seul état | « 100 % rédigé » (achevé) et « cours · en révision » (intégré, audit en attente), sans débordement |
| Quiz | Bonne réponse en ambre | Bonne réponse verte ✓, mauvaise rouge ✗ ; survol limité aux options non répondues |
| Plan du cours | Numéroté à partir de 1, îlots à partir de 0 | Même numérotation que les îlots |
| Notification | Pouvait recouvrir Navigo ou le bouton directeur | Toujours fermable, positionnée hors des commandes |
| Messages techniques | Erreur brute « lesson-core.js » dans le Carnet | Explication en français |
| Construction | Feuille Google Fonts bloquée par la politique de sécurité ; icône SVG mal formée ; constructions non reproductibles | Lien retiré ; icône corrigée à la construction ; horodatage gzip fixé (`mtime=0`) |

## 3. Revues adverses

1. **Première revue** (trois angles indépendants : visuel, accessibilité, fonction ; captures et mesures Playwright) : 45 constats (2 bloquants, 20 majeurs, 23 mineurs) — tous traités.
2. **Seconde revue** (vérification des 45 correctifs et recherche de régressions) : 36 correctifs confirmés ; 9 points mal corrigés et 15 régressions ou défauts nouveaux, surtout aux largeurs intermédiaires (701–1 279 px) — tous traités et remesurés.
3. **Troisième revue** (vérification des 24 correctifs de la seconde) : voir § 5.

Décision assumée : la pulsation de l’insigne fluorescent est maintenue (exigence d’identité du propriétaire).

## 4. Captures

`audits/FRONT_captures/avant/` et `audits/FRONT_captures/apres/` : 21 vues (accueil, directeur, bouton directeur, notification, spécialité, système, entrée CIM, cours : en-tête, îlot, fenêtre, quiz, Pareto, Navigo, Police Taille, mode livre, sciences ; Examen fédéral, Carnet, recherche, méthode, atlas ECG) à 1 360 px et 390 px, plus 10 vues en mode sombre (`_pc-sombre`). Script : `python3 captures_front.py <jeu> [fichier.html]`.

## 5. Contrôles

- `test_v7.py` étendu : barre supérieure collante, mode sombre aller-retour sans résidu (en plus des contrôles de phase 1). Résultat sur `MEDINA_final.html` : **OK sur les 30 chapitres**, PC 1300 × 900 et mobile 390 × 844.
- **Troisième revue** : les 24 constats de la seconde revue sont corrigés et remesurés (contrastes en clair et en sombre de 4,26:1 à 14,49:1 pour les éléments concernés ; 0 texte sous Navigo de 761 à 899 px ; barre d’outils placée de 8 à 18 px sous la barre supérieure sur 20 ouvertures directes ; notification fermable de 701 à 1 360 px ; coût de la conversion sombre divisé par deux). Deux régressions nouvelles, issues des correctifs, ont été corrigées et remesurées par l’intégrateur : champ de recherche de 76 à 375 px utiles entre 701 et 1 000 px (aucun bouton rogné, aucun défilement horizontal) ; aucun fragment de libellé hors de son onglet, y compris J44 en police 24 px (onglets alors non collants par décision : libellés entiers).
- Réserve assumée : sur un processeur lent (×4), la bascule vers le mode sombre reste une tâche longue (150 à 230 ms), due surtout au recalcul de style de la feuille sombre elle-même ; elle n’a lieu qu’au clic sur le bouton.
