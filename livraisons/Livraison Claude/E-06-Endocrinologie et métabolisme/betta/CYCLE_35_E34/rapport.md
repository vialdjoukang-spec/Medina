# Rapport de rédaction : E34, Autres troubles endocriniens (E-06-Endocrinologie et métabolisme)

Cycle Betta 35, leçon 2. Agent C35-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
- `chapters/E34/E34_a.html` : 26068 octets
- `chapters/E34/E34_b.html` : 35021 octets
- `chapters/E34/E34_c.html` : 26942 octets
- `chapters/E34/E34_d.html` : 7423 octets
- `chapters/E34/E34_pop1.html` : 20804 octets
- `chapters/E34/E34_pop2.html` : 18979 octets
- `glossary/e34.py` : 51 entrées conditionnelles (ENETS, XY, 5-HIAA, TNE, GHRH, IGF-1, LH, FSH, AMH, codes CIM d'exclusion, etc.), ajoutées seulement si la clé est absente des glossaires existants.
- Fenêtres : 61 templates (11 Pareto, dont les deux contentieux et un troisième, l'âge de début de la somatropine chez l'enfant né petit pour l'âge gestationnel). Quiz : 6. Environ 15 000 mots.

## Structure
Quatre onglets : Pathologie (îlots 0 à 12, dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (5 îlots), Sciences (Anatomie, Histologie, Physiologie, Biochimie, Génétique, avec 5 schémas SVG), Pharmacologie (4 îlots). Plan monographique par entité (syndrome carcinoïde, hypersécrétions et ectopique, petite taille, haute taille, résistance aux androgènes, progéria), sans îlot ni tableau consacré au code CIM ; le périmètre est exposé en une phrase et un tableau d'entités.

## Contentieux en fenêtre verte
1. Dose initiale des analogues de la somatostatine : ENETS 2022 (30 mg / 120 mg) contre informations professionnelles suisses (20 mg / 60 mg) ; choix : texte suisse en vigueur, le texte ENETS restant accessible.
2. Moment de la gonadectomie dans l'insensibilité complète aux androgènes : Batista 2018 contre AWMF 2025 et CNE 20/2012 ; choix : source la plus récente (conservation jusqu'à la majorité).
3. Âge de début de la somatropine (petit pour l'âge gestationnel) : information Genotropin (2 ans) contre Noordam 2023 (4 ans).

## Sources utilisées (recherche.md / sources.json)
S1 à S24 ; citations dans le texte sous forme « (source, année) ». Aucune donnée extérieure au dossier. Les interprétations pédagogiques (rétrocontrôle de la LH) sont signalées comme telles.

## Auto-contrôle (cahier W)
HTML bien formé (aucune balise non fermée ou mal imbriquée) ; identifiants uniques, tous préfixés `e34` ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline ; tous les Pareto couvrent des îlots existants ; audit des abréviations (`build_medina.audit`) = `{}` avec le glossaire e34 ajouté. Contrôle exécuté hors racine, sans modifier `chapters/`, `glossary/` ni `chapters.json`.

## Lacunes (reprises du dossier, non comblées)
Aucun article du Swiss Medical Forum ni recommandation de la société suisse d'endocrinologie ; sources suisses = brochure SwissNET (financée par l'industrie), article Pädiatrie 2023, avis CNE 2012, informations professionnelles. ENETS 2023 et 2024 et EJE 2020 lues en résumé ; ESMO 2020 non lue. E34.1 strictement intestinal non pancréatique, dysfonction pinéale et petite taille psychosociale peu ou pas sourcés. Statut suisse de la mécasermine et du lonafarnib non établi ; doses de la somatropine, de la mécasermine et du lonafarnib non reprises. Les quatre types de flush, la grossesse, le sujet âgé et l'histologie détaillée ne sont pas documentés. Les cas et vignettes sont fictifs et signalés comme tels.
