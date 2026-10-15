# Rapport de rédaction — G73, Affections musculaires et neuromusculaires au cours de maladies classées ailleurs (N-05-Neurologie)

Cycle Betta 39, leçon 1. Agent C39-A3-NEUR (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- 29954 chapters/G73/G73_a.html
- 23753 chapters/G73/G73_b.html
- 28270 chapters/G73/G73_c.html
- 15715 chapters/G73/G73_d.html
- 22183 chapters/G73/G73_pop1.html
- 10706 chapters/G73/G73_pop2.html
- 9016 glossary/g73.py

Structure : quatre onglets (Pathologie 15 îlots 0 à 14, Examens 6 îlots, Sciences 4 disciplines avec 3 schémas SVG, Pharmacologie 6 îlots), 32 fenêtres explicatives dont 9 Pareto, 5 quiz fictifs, 21 tableaux, glossaire conditionnel (codes CIM compris).

## Sources utilisées
S1 à S38 de `sources.json` (S10b comprise), toutes citées en fin d'îlot. Aucune donnée extérieure au dossier de recherche. Les informations professionnelles suisses de Firdapse® et de Mestinon® (S16, S17) alimentent la pharmacologie et les fenêtres de posologie.

## Auto-contrôle (cahier W)
- HTML bien formé sur l'assemblage des six fichiers (analyse de balises) : oui.
- Identifiants uniques et préfixés `g73-` : oui. Clés de fenêtres référencées existantes : oui, aucune orpheline. Ancres du sommaire valides. Cibles Pareto (`data-cover`) valides.
- Abréviations : `build_medina.audit()` renvoie `{}` avec le glossaire de G73 ; références de glossaire vers des fenêtres existantes.
- Transformation `build_medina.transform` + `pareto_ratios` + `wrap_html` exécutée sans erreur.
- Dernier îlot de la pathologie : `div.alert` (critères formels) puis `div.key` (paramètres clés).

## Lacunes déclarées dans le cours
Aucune source suisse ni EAN ; article original DELTA-P (pondérations, seuil du Karnofsky) et tableaux PNS-Care non lus ; posologies des immunoglobulines, de la prednisolone et de l'azathioprine non lues ; remboursement de Firdapse® non vérifié ; aucune source clinique pour G73.0, G73.3, G73.6 et G73.7 (seules les inclusions CIM sont restituées, dans des encadrés « Limite documentaire ») ; CK et EMG des myopathies thyroïdiennes non sourcées ; trichinellose sans traitement ; paralysie périodique thyréotoxique et myopathie cortisonique présentées sans code CIM (rattachement non vérifié) ; aucune donnée suisse. La plupart des sources ne sont lues qu'en abstract : le texte ne leur attribue que ce que le dossier cite.
Cas cliniques et exemples chiffrés (incrément, vignette d'ouverture) : fictifs et signalés comme tels.
Aucune touche à `chapters/` racine, `glossary/` racine, `chapters.json` ni git.
