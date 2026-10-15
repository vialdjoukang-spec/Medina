# Rapport de rédaction : E40, Kwashiorkor (E-06-Endocrinologie et métabolisme)

Cycle Betta 36, leçon 2. Agent C36-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
- `chapters/E40/E40_a.html` : 32774 octets (en-tête, plan, îlots 0 à 6)
- `chapters/E40/E40_b.html` : 67901 octets (îlots 7 à 18 ; dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`)
- `chapters/E40/E40_c.html` : 46737 octets (Examens, 5 îlots ; Sciences : Physiologie, Biochimie, Histologie, Immunologie et microbiote)
- `chapters/E40/E40_d.html` : 20338 octets (Pharmacologie, 5 îlots)
- `chapters/E40/E40_pop1.html` : 30704 octets ; `E40_pop2.html` : 37900 octets
- `glossary/e40.py` : 9 entrées conditionnelles (ET, OSAV, SSP, ReSoMal, ATPE, E64.0, T73.0, HC, Roux-en-Y), ajoutées seulement si la clé est absente des glossaires existants.
- Environ 22 500 mots ; 60 fenêtres (dont 11 Pareto) ; 8 quiz de cas ; 6 schémas SVG noir et blanc légendés ; 4 onglets.

## Structure
Plan monographique : question clinique, définition, classifications, épidémiologie, trois îlots de physiopathologie (œdème ; glucose, foie, stress oxydatif, microbiote ; hormones, immunité, intestin, cœur, cerveau), causes, anamnèse, examen, diagnostic et différentiel, urgences, orientation OMS, stabilisation, réhabilitation, renutrition en Suisse (adulte, causes secondaires), suivi, situations particulières, critères formels. Aucun îlot ni tableau consacré au code CIM ; les codes voisins (E41, E42) et les exclusions de bloc sont cités en prose.

## Contentieux en fenêtre verte
1. Gradation de l'œdème : Bhutta 2017 (3 niveaux) contre Dipasquale 2020 (4 grades) ; OMS 2023 utilise « +++ » sans définition lue ; choix : trois niveaux de 2017, compatibles avec la notation OMS.
2. Dose d'amoxicilline : schéma décrit (15 mg/kg toutes les 8 h, soit 45 mg/kg/jour) contre informations professionnelles suisses (orale 50 à 100 mg/kg/jour, août 2024 ; intraveineuse 20 à 200 mg/kg/jour, septembre 2026) ; choix : texte suisse en vigueur, le schéma OMS restant accessible.
3. Thiamine : consensus suisse et européen (200 à 300 mg avant la renutrition, adulte) contre information professionnelle Benerva (100 mg/jour, avril 2019, sans mention de la renutrition) ; choix : consensus pour la renutrition, en signalant que la dose ne vient pas de l'information professionnelle.

## Sources utilisées (recherche.md / sources.json)
S1 à S24, citées dans le texte sous forme de liens datés. Aucune donnée extérieure au dossier. Quelques rappels de physiologie générale (rôle de l'albumine, glycolyse, pompe sodium-potassium, hypersensibilité retardée, gradient d'albumine sérum-ascite) sont signalés comme tels dans le texte. Les raisonnements du cours (diagnostic différentiel des œdèmes avec protéines basses, déductions sur l'orientation ambulatoire, calcul des apports protéiques du F-75 et du F-100) sont signalés comme tels.

## Auto-contrôle (cahier W)
HTML bien formé (aucune balise non fermée ou mal imbriquée) ; identifiants uniques, tous préfixés `e40` ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline, clés préfixées `e40-` et `pareto-e40-` ; tous les Pareto couvrent des îlots existants ; audit des abréviations (`build_medina.audit`) = `{}` avec le glossaire e40 ajouté. Construction et chargement navigateur vérifiés hors racine, dans une copie temporaire du dépôt, sans toucher `chapters/`, `glossary/` ni `chapters.json` : `build_medina.py` affiche « E40 non couvertes: 0 » ; `test_preview.py` affiche OK une fois ignorée l'erreur préexistante du module `lesson-core.js` (absent du dépôt, étranger à ce chapitre). Les codes de recommandation de l'OMS (B2, B3, B5…) ont été remplacés par des intitulés, car B2 et B3 sont des clés du glossaire cardiologique avec un autre sens.

## Lacunes (reprises du dossier, non comblées)
Aucune recommandation suisse ou européenne propre au kwashiorkor. Instructions de la Société suisse de pédiatrie de 2020 inaccessibles (seul le communiqué a été lu). Définition littérale des grades d'œdème de l'OMS non lue. Version de la recommandation de l'OMS auto-générée. Aucune source dédiée au diagnostic différentiel des œdèmes avec protéines basses. Ni épidémiologie suisse, ni correspondance CIM-11 vérifiée. Aucune information professionnelle suisse pour le F-75, le F-100, le ReSoMal et l'aliment thérapeutique prêt à l'emploi ; informations de la gentamicine et de la ceftriaxone non lues. Conduite devant une hypothermie, test d'appétit, moment d'introduction du fer chez l'enfant, intervalles de référence pédiatriques et équivalent suisse de la nutrivigilance non documentés. Les cas et vignettes sont fictifs et signalés comme tels.
