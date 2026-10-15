# Rapport G08 — Phlébite et thrombophlébite intracrâniennes et intrarachidiennes (N-05-Neurologie)

Cycle Betta 35 · leçon 1 · agent de rédaction C35-A1-NEUR (Sonnet 5.5) · 15.10.2026.
**Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (dossier `livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_35_G08/`)
- `chapters/G08/G08_a.html` : 20713 octets
- `chapters/G08/G08_b.html` : 27057 octets
- `chapters/G08/G08_c.html` : 21770 octets
- `chapters/G08/G08_d.html` : 8863 octets
- `chapters/G08/G08_pop1.html` : 37723 octets
- `chapters/G08/G08_pop2.html` : 10104 octets
- `glossary/g08.py` : 5311 octets

## Volumes
- Environ 12236 mots (balises exclues), 66 fenêtres explicatives (dont 14 Pareto), 5 quiz de cas, 3 schémas SVG noir et blanc légendés (anatomie, physiopathologie, microbiologie).
- Structure : pathologie (îlots 0 à 13 et références), examens (e-1 à e-5), sciences (anatomie, physiologie, microbiologie), pharmacologie (p-1 à p-4). Dernier îlot de la pathologie : critères formels (`div.alert`) puis paramètres clés ; Pareto en fin de chaque grande partie.

## Sources utilisées
Uniquement le dossier de recherche (`recherche.md`, `sources.json`) : S1 (CIM-10-GM 2024), S2 (ligne directrice S2k 2023), S4 (Int J Stroke 2025), S21 (Clexane, 02.2026), S22 (Pradaxa, 02.2024) en texte intégral ; S3, S5–S20, S23 au niveau du résumé. Les sources non européennes (S11, S12, S13, S18, S23) ne servent qu'à des données descriptives.

## Lacunes explicites (signalées dans le texte)
- Aucune incidence fiable de la forme septique ; aucune donnée suisse de fréquence.
- Aucun schéma d'antibiothérapie empirique ; aucune molécule proposée.
- Phlébite intrarachidienne : aucune clinique ni conduite ; périmètre seulement mentionné.
- Différentiel du syndrome du sinus caverneux (cellulite orbitaire, fistule carotido-caverneuse, Tolosa-Hunt) : cité sans règle de tri.
- Informations professionnelles de l'héparine non fractionnée, de l'acétazolamide, des antiépileptiques, des antagonistes de la vitamine K et des antibiotiques non lues : posologies non reprises.
- Seuils de décision du score de Berne non lus ; ESO 2017 lu au niveau du résumé ; critères formels du diagnostic septique : synthèse du cours, annoncée comme telle.
- Choix de rédaction : conformément à la règle du dépôt, pas d'îlot ni de tableau consacré au code CIM ; le périmètre septique/non septique est enseigné en clinique.

## Auto-contrôle (cahier W)
- HTML bien formé (a à d, pop1, pop2), identifiants uniques et préfixés `g08-`, aucune clé de fenêtre orpheline ni non référencée.
- `build_medina.audit()` sur les six fichiers avec glossaire G08 : `{}` (aucune abréviation non couverte) ; `bm.build` sans erreur Pareto (ratios calculés).
- Glossaire `glossary/g08.py` : ajouts conditionnels (`add_if_absent`), sans mutation des glossaires existants.
- Non fait : test navigateur complet (le moteur de test exige l'intégration au registre, interdite à cette étape) ; injection canonique non réalisée.
