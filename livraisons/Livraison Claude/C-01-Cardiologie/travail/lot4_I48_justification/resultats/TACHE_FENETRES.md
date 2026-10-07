# Tâche fenêtres (rédaction ou vérification)

Pour chaque clé confiée, lire `jobs/<cle>.json` (dossier scratchpad). Champs : `cle`, `titre`, `action` (`creer` ou `completer`), `fichier_cible`, `contenu_attendu` (plan validé), `ancres` (affirmations du cours que la fenêtre doit justifier ; `label` deviendra le mot vert), `fenetre_existante` (si `completer`), `brouillon_html` et `brouillon_sources` (si une rédaction antérieure existe, non vérifiée).

## Production attendue
- `out/<cle>.html` :
  - action `creer` : le template complet `<template data-pop="CLE" data-title="TITRE">` … `</template>`, rubriques Physiologie normale, Mécanisme, Conséquence clinique, Ce qui change la décision, Source (intitulés adaptables s'ils sont plus précis) ;
  - action `completer` : seulement les rubriques nouvelles `<div class="lab">…</div><p>…</p>` à ajouter à la fin de la fenêtre existante, sans redire l'existant, terminées par « Source complémentaire ».
- `out/<cle>.json` : `{"cle":…, "action":…, "sources":[références complètes vérifiées], "verification":"ok" | "corrigée", "problemes_corriges":[…], "ancres_retirees":[{"id":…, "motif":…}], "label_modifies":[{"id":…, "label":…}], "reserves":[doutes non résolus]}`.
  - Retirer une ancre si l'affirmation est déjà justifiée sur place ou si la fenêtre ne la justifie pas. Un `label` modifié doit rester une sous-chaîne exacte de `old`, sans balise.

## Vérification médicale sceptique (obligatoire avant d'écrire la version finale)
Relire chaque phrase comme un examinateur : exactitude physiopathologique, chiffres, doses, classes et niveaux de recommandation contrôlés dans le texte ESC 2024 par Grep, absence de surcertitude, cohérence avec le cours I48, absence de sigle non autorisé, HTML conforme, concision (supprimer toute redite). En cas de brouillon : le brouillon est un point de départ, souvent trop long ; le condenser aux repères de longueur et corriger toute erreur.
