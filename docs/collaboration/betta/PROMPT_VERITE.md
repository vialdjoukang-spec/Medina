# PROMPT DE VÉRITÉ — moteur de recherche rigoureuse et exhaustive (entrée de chaque leçon)

Instruction de Vial du 15 octobre 2026. Lu **en premier** par tout agent qui ouvre une leçon (recherche puis rédaction), avant toute autre lecture. Objectif : qu'à l'audit différé **il n'y ait rien à ajouter**. Il complète le cahier R/W de `.claude/skills/cycle_Betta-medina/SKILL.md` sans le remplacer ; en cas de conflit, la règle la plus exigeante s'applique.

## 1. Les cinq lois
1. **Rien de mémoire.** Chaque fait porte `[Sx]` ; `Sx` existe dans `sources.json` et a été **lu** (niveau indiqué). Un fait non sourcé est supprimé ou déclaré lacune.
2. **Hiérarchie des sources.** Suisse (SMF/RMS, sociétés suisses, OFSP, Swissmedic, Suva, swissnoso, Pharmavista/Compendium) → européenne (EAN, ESC, ESE, EASL, ERA/KDIGO accepté en Suisse, EHA, ESMO, ERS, ESPGHAN, EULAR) → revues et synthèses. **Jamais** une recommandation américaine comme fondement d'une conduite.
3. **Médicament = FI suisse.** Toute dose, contre-indication, interaction ou adaptation rénale/hépatique vient de l'information professionnelle Swissmedic (`python3 tools/swissmedic_fi.py`), avec sa date de mise à jour.
4. **Lecture réelle et traçable.** Niveau dans `sources.json` : `texte_integral`, `section`, `resume`. Une conduite thérapeutique ou un seuil ne se fonde pas sur un résumé seul si le texte intégral est accessible.
5. **Lacune déclarée > invention.** Ce qui n'a pas pu être lu figure dans « Lacunes », avec la requête tentée.

## 2. Économie de jetons (obligatoire)
- **Réutiliser avant de chercher** : `grep -l "<code ou thème>" "livraisons/Livraison Claude/"*/betta/*/sources.json`. Une source déjà lue dans le même bloc est reprise avec sa section, sans relecture complète.
- **Ordre d'outils** : URL connue (WebFetch ciblé) → PubMed MCP/E-utilities (métadonnées, puis texte PMC si besoin) → `swissmedic_fi.py` → WebSearch en dernier recours. Une requête précise vaut mieux que trois requêtes larges.
- **Lire la section utile**, pas le document entier ; noter section/page pour que l'auditeur vérifie en une lecture.
- Ne jamais recopier une source dans le dossier : extraire le fait, la valeur, la référence.

## 3. Matrice d'exhaustivité (section obligatoire de `recherche.md`)
Titre exact : `## Matrice de complétude`. Une ligne par rubrique, au format
`| rubrique | statut | sources |` avec statut `✔` (couvert), `∅` (sans objet, avec raison) ou `LACUNE` (requête tentée).

Rubriques obligatoires (dans cet ordre) :
1. Question clinique et enjeu pour l'examen fédéral
2. Définition et périmètre CIM-10-GM (libellés OFS, inclusions, exclusions, notes BfArM)
3. Classifications et stades
4. Épidémiologie suisse puis européenne (incidence, prévalence, âge, sexe)
5. Normal → pathologique (anatomie, physiologie, mécanisme causal)
6. Étiologies et facteurs de risque
7. Anamnèse et symptômes (fréquences)
8. Examen clinique (signes, sensibilité/spécificité si disponibles)
9. Drapeaux rouges et urgences (seuil, délai, action)
10. Examens complémentaires (indication, valeur normale, seuil, interprétation, pièges)
11. Diagnostic différentiel (élément discriminant pour chaque diagnostic)
12. Prise en charge suisse (niveaux de soins, conduite, médicaments FI datés)
13. Complications et pronostic
14. Suivi, prévention, dépistage
15. Situations particulières (grossesse, enfant, âgé, insuffisance rénale/hépatique)
16. Spécificités suisses (déclaration OFSP, Suva/LAA, aptitude à la conduite, AI, remboursement LS/LiMA)
17. Critères formels du diagnostic (→ `div.alert`)
18. Paramètres clés chiffrés (→ `div.key`)
19. Sous-codes CIM-10-GM couverts (liste complète `X00.0`… et leur traitement)
20. Points d'examen fédéral (objectifs PROFILES/SSP, pièges classiques)

## 4. Contrôle d'entrée en rédaction (porte de vérité)
Avant toute rédaction : `python3 tools/betta_verite.py "<dossier de la leçon>"` doit afficher `VÉRITÉ OK`. En cas d'échec, la recherche est complétée, jamais contournée.

## 5. Rédaction (agent W)
- N'écrire que ce que le dossier prouve ; chaque rubrique `✔` de la matrice apparaît dans la leçon, chaque `LACUNE` est signalée dans `rapport.md`.
- Français soutenu, extrême de clarté : phrases complètes et courtes, terme médical exact, mécanisme → conséquence → décision, chiffres avec unité et normal avant pathologique.
- `rapport.md` reprend la matrice avec, pour chaque rubrique, l'onglet et l'identifiant HTML où elle est traitée : l'auditeur différé contrôle par échantillonnage, sans rien rechercher.
- Mention finale : « Audit différé — revue IA, distincte d'une validation médicale humaine ».
