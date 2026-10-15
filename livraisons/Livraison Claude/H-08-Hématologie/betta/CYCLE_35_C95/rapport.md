# Rapport — C95 Leucémie à cellules non précisées (cycle Betta 35, leçon 2, agent C35-A3-HEM, rédaction Sonnet 5.5)

Date : 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (dossier `livraisons/Livraison Claude/H-08-Hématologie/betta/CYCLE_35_C95/`)
chapters/C95/ : C95_a.html 33 633 o ; C95_b.html 25 748 o ; C95_c.html 28 421 o ; C95_d.html 9 790 o ; C95_pop1.html 21 060 o ; C95_pop2.html 18 568 o ; glossary/c95.py 14 173 o ; rapport.md. Environ 14 000 mots, 4 quiz de cas fictifs, 3 schémas SVG noir et blanc légendés.

## Contenu
- Onglet 1 : 15 îlots (question clinique, nosologie CIM-10-GM 2024 et sous-codes, épidémiologie, mécanismes dont le changement de lignée, causes, anamnèse, examen, diagnostic d'exclusion et différentiel, urgences, choix du protocole, LAPM Ph+/LAI/thérapies ciblées, allogreffe en RC1, réponse/réfractaire/MRD, pronostic et situations particulières, critères formels `div.alert` puis paramètres clés `div.key`), 3 Pareto.
- Onglet 2 : 5 îlots (questions-examens, immunophénotype, configurations biologiques, génétique, 4 quiz), 1 Pareto.
- Onglet 3 : 4 sciences (hématologie cellulaire, immunophénotype, génétique, biochimie), 3 schémas, 1 Pareto.
- Onglet 4 : 5 îlots (classes et place, doses, précautions, effets indésirables, erreurs à éviter), 1 Pareto.
- Fenêtres : 43 (dont 6 Pareto). Glossaire `glossary/c95.py` : entrées conditionnelles (codes, gènes, marqueurs CD, sigles de réponse).

## Sources utilisées
Les 20 sources de `sources.json` : BfArM et OFS (CIM-10-GM 2024), rapport OFS 2021, Onkopedia LMA 2025 et LLA 2026, Haematologica 2025, EBMT 2017 et 2026, iBFM-AMBI2012, Karasek 2025, Kirtek 2025, Weinberg 2024, cytométrie 2025, LLA-T CD3 négative, Hrusak 2024, FGFR1 2024, Glivec®, Iclusig®, Fasturtec®, Litalir®. Aucune donnée hors dossier ; quelques explications de mécanisme (CD3, précipitation de l'acide urique, sélection du clone) relèvent du raisonnement physiopathologique général et sont signalées comme tel quand elles ne sont pas sourcées.

## Lacunes (reprises du dossier, non comblées)
Aucune recommandation suisse, ESMO ou EHA dédiée à la LALA ; Ars Medici 2013 introuvable (404), donc pas de conduite de premier recours ; C95.1- et C95.7- sans entité clinique ; aucun chiffre suisse propre à C95 ; survie nord-américaine seulement descriptive ; LAPM Ph+ et thérapies ciblées hors étiquette ; informations professionnelles du vénétoclax, du blinatumomab et des inhibiteurs de ménine non relues ; molécules des protocoles de type LLA non décrites ; interactions pharmacocinétiques non détaillées ; date de révision de Fasturtec® non extraite.

## Auto-contrôle (cahier W)
- HTML bien formé (analyseur de balises, pile vide), identifiants uniques et préfixés `c95-` ; clés de fenêtres `c95-` / `pareto-c95-`.
- Toutes les clés `data-k` ont leur `template data-pop` ; aucune fenêtre inutilisée.
- Pareto : tous les îlots couverts existent (`build_medina.pareto_ratios` sans erreur).
- `build_medina.audit()` avec le glossaire du dépôt + `c95.py` : aucune abréviation non couverte (`{}`).
- Aucun fichier hors du dossier de la leçon n'a été modifié ; ni `chapters.json`, ni git.
