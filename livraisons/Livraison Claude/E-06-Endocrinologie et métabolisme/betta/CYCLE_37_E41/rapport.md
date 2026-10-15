# Rapport de rédaction : E41, Marasme nutritionnel (E-06-Endocrinologie et métabolisme)

Cycle Betta 37, leçon 1. Agent C37-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
- `chapters/E41/E41_a.html` : 32690 octets (en-tête, plan, îlots 0 à 6)
- `chapters/E41/E41_b.html` : 56297 octets (îlots 7 à 18 ; dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`)
- `chapters/E41/E41_c.html` : 36276 octets (Examens, 5 îlots ; Sciences : Physiologie, Biochimie, Histologie, Immunologie)
- `chapters/E41/E41_d.html` : 15678 octets (Pharmacologie, 5 îlots)
- `chapters/E41/E41_pop1.html` : 32691 octets ; `E41_pop2.html` : 35280 octets
- `glossary/e41.py` : 10 entrées conditionnelles (GLIM, ESPEN, NRS, EFFORT, ReSoMal, IGF-1, kJ, HC, E44.0, E44.1), ajoutées seulement si la clé est absente des glossaires existants.
- Environ 14 000 mots de cours et 7 400 mots de fenêtres ; 57 fenêtres (dont 10 Pareto) ; 6 quiz de cas ; 6 schémas SVG noir et blanc légendés ; 4 onglets.

## Structure
Plan monographique : question clinique, définition, classifications, épidémiologie, trois îlots de physiopathologie, causes, anamnèse, examen, diagnostic et différentiel, urgences, stabilisation de l'enfant, réhabilitation, adulte hospitalisé en Suisse, syndrome de renutrition, suivi, situations particulières, critères formels. Aucun îlot ni tableau consacré au code CIM ; les codes voisins (E40, E42, E43, E44, E46) sont cités en prose et en fenêtre.

## Contentieux en fenêtre verte
1. Dose d'amoxicilline : schéma décrit par Dipasquale (15 mg/kg toutes les 8 heures, soit 45 mg/kg/jour) contre information professionnelle suisse d'août 2024 (50 à 100 mg/kg/jour, enfant de 40 kg ou moins) ; texte suisse retenu comme cadre autorisé, schéma OMS accessible, ligne directrice OMS 2023 non lue donc non arbitrée.
2. Thiamine : consensus suisse (200 à 300 mg avant la renutrition) contre Benerva® (200 à 300 mg/jour par voie orale, parentérale limitée à 200 mg/jour, renutrition non libellée) ; consensus retenu pour la dose, information professionnelle pour les voies.
3. Phosphate : doses du consensus (0,3 à 0,6 mmol/kg/jour) supérieures à la dose libellée du Glycophos® (10 à 20 mmol/jour chez l'adulte), avec charge de sodium de 2 mmol par mmol de phosphate ; calcul du cours signalé comme tel.
4. Estimations de mortalité (174 000, 875 000, 540 000 décès) : trois définitions, trois années, non additionnables.
5. Débit cardiaque du marasme : Dipasquale (réduit) contre Bhutta (normal rapporté à la surface corporelle) ; prudence du remplissage retenue.

## Sources utilisées (recherche.md / sources.json)
S1 à S19, citées sous forme de liens (S1 : base OFS locale, non liée). Aucune donnée extérieure au dossier. Les raisonnements du cours (liens entre déficits immunitaires et discrétion des infections, paliers de correction, calculs de volumes et de sodium, charge de sodium du Glycophos®, définitions générales de statistique) sont signalés comme tels dans le texte.

## Auto-contrôle (cahier W)
HTML bien formé (aucune balise non fermée ou mal imbriquée, fenêtres comprises) ; 42 identifiants uniques, tous préfixés `e41` (hors `pA`, `pE`, `pS`, `pP`) ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline, clés préfixées `e41-` et `pareto-e41-` ; tous les Pareto couvrent des îlots existants (ratios de 5 à 14 %). Audit des abréviations `build_medina.audit` = `{}` (« E41 non couvertes: 0 ») avec le glossaire e41. Construction et chargement navigateur vérifiés hors racine dans une copie temporaire (liens symboliques vers le dépôt), sans toucher `chapters/`, `glossary/` ni `chapters.json` : `test_preview.py` ne signale que l'erreur préexistante du module `lesson-core.js` absent du dépôt, étrangère à ce chapitre (même constat qu'en E40). Fenêtres, onglets et mode livre fonctionnent.

## Lacunes (reprises du dossier, non comblées)
Aucune recommandation suisse propre au marasme (SSED/SGED, Swiss Medical Forum). Seuils GLIM de stade 1 et 2 et de masse musculaire non lus (le cours n'écrit que les seuils de perte de poids et d'indice de masse corporelle rapportés par l'étude de Madrid). Ligne directrice OMS 2023 non lue (doses, critères d'hospitalisation, test d'appétit à vérifier). Seuils OMS d'hypoglycémie et d'hypothermie non lus ; aucune conduite devant l'hypothermie. ESPEN : résumés seuls, cibles énergétiques et protéiques non chiffrées. Anorexie mentale, grossesse, insuffisance hépatique non couvertes. Informations professionnelles de la gentamicine, de la ceftriaxone, de l'ampicilline, du potassium et du magnésium non lues ; effets indésirables et contre-indications de Benerva® et de l'amoxicilline non relus. Exclusions de bloc de la CIM-10-GM (malabsorption, cachexie liée au VIH, séquelles, inanition) non relues pour E41. Sens exact du critère « phosphate en baisse de plus de 30 % sous la limite inférieure » à confirmer dans Reber 2019. Détail du calcul du NRS 2002 non lu. Ni épidémiologie suisse propre au code E41, ni correspondance CIM-11 vérifiée. Les cas et vignettes sont fictifs et signalés comme tels.
