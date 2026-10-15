# Rapport de rédaction — G02, Méningite au cours d'autres maladies infectieuses et parasitaires classées ailleurs (N-05-Neurologie)

Cycle Betta 33, leçon 2. Agent C33-A4-NEUR (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- 31036 chapters/G02/G02_a.html
- 33136 chapters/G02/G02_b.html
- 30450 chapters/G02/G02_c.html
- 13649 chapters/G02/G02_d.html
- 33014 chapters/G02/G02_pop1.html
- 16585 chapters/G02/G02_pop2.html
- 7016 glossary/g02.py

Structure : quatre onglets (Pathologie 15 îlots 0 à 14, Examens 7 îlots, Sciences 4 disciplines avec schéma SVG, Pharmacologie 6 îlots), 60 fenêtres explicatives dont 10 Pareto, 7 quiz, 6 figures SVG, glossaire conditionnel (35 entrées, codes CIM compris).

## Sources utilisées
S1 à S18 de `sources.json` (BfArM/OFS, directive S1 DGN 2025, cohortes danoises, essai suédois, études CHUV et HUG, recommandation ECMM 2024, OMS 2024, OFSP, ESCMID 2012, informations professionnelles Swissmedic : aciclovir, valaciclovir, AmBisome, fluconazole). Aucune donnée extérieure au dossier de recherche.

## Auto-contrôle (cahier W)
- HTML bien formé (analyse de balises sur les six fichiers) : oui.
- Identifiants uniques et préfixés `g02-` : oui. Clés de fenêtres référencées existantes : oui (60/60, aucune orpheline). Ancres du sommaire et cibles Pareto : valides.
- Abréviations : `build_medina.audit()` renvoie `{}` avec le glossaire de G02 ; références de glossaire vers des fenêtres existantes.
- Transformation `build_medina.transform` + `pareto_ratios` + `wrap_html` : exécutée sans erreur sur les fichiers.
- Dernier îlot de la pathologie : `div.alert` (critères formels) puis `div.key` (paramètres clés).

## Arbitrages et lacunes
- Divergence aciclovir dans l'encéphalite herpétique : information professionnelle suisse (déc. 2025) 10 jours vs directive S1 (fév. 2025) au moins 14 jours ; fenêtre `g02-aciclovir-duree`, durée de l'information professionnelle retenue comme repère réglementaire, l'autre durée signalée.
- Lacunes déclarées dans le cours : aucune recommandation suisse dédiée ; candidose du SNC, coccidioïdomycose, maladie de Chagas sans source ; trypanosomiase (seuils de liquide, NECT, mélarsoprol, acoziborole) non lue ; pas d'information professionnelle suisse de la flucytosine ; palier aciclovir < 10 ml/min non relevé ; foscarnet et brivudine sans posologie ; textes britannique 2016 et EFNS/EAN non lus.
- Mécanismes limités à ce que le dossier documente (aucun mécanisme d'action pharmacologique ajouté de mémoire). Cas cliniques et exemple d'indice d'anticorps : fictifs et signalés comme tels.
- Aucune touche à `chapters/` racine, `glossary/` racine, `chapters.json` ni git.
