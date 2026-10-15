# Rapport de rédaction : E12, Diabète sucré de malnutrition (E-06-Endocrinologie et métabolisme)

Cycle Betta 33, leçon 1. Agent C33-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
- `chapters/E12/E12_a.html` : 23325 octets
- `chapters/E12/E12_b.html` : 25323 octets
- `chapters/E12/E12_c.html` : 23553 octets
- `chapters/E12/E12_d.html` : 8916 octets
- `chapters/E12/E12_pop1.html` : 13673 octets
- `chapters/E12/E12_pop2.html` : 10644 octets
- `glossary/e12.py` : 17 entrées (FCPD, IDF, HaPanEU, SIDD, PDX-1, MafA, SPINK1, PRSS1, PRSS2, N34S, anti-GAD65, CA 19-9, DFGe, CT, DEXA, SANS, Hugh-Jones), chacune conditionnelle à l'absence d'une clé existante.
- Fenêtres : 40 templates (dont 10 Pareto et 30 fenêtres explicatives, mnémotechnique SANS signalée « aide pédagogique, non critère officiel »).

## Structure
Quatre onglets : Pathologie (îlots 0 à 12, dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (5 îlots, 3 quiz de cas ; 7 quiz au total), Sciences (Anatomie, Histologie, Physiologie, Biochimie, Génétique, schéma SVG par science), Pharmacologie (4 îlots). Plan monographique, sans îlot ni tableau consacré au code CIM. Six schémas SVG noir et blanc légendés, dont un chiffré avec les données de Vellore.

## Sources utilisées (dossier recherche.md / sources.json)
S1 à S16 ; S17 (CIM-11 5A12) volontairement non reprise faute de vérification auprès de l'OMS. Aucune donnée extérieure au dossier. Citations dans le texte sous forme « (source, année) ».

## Auto-contrôle (cahier W)
HTML bien formé (aucune balise non fermée, aucune erreur d'imbrication) ; identifiants uniques, tous préfixés `e12` ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline ; tous les Pareto couvrent des îlots existants ; `build_medina.audit()` renvoie `{}` avec le glossaire e12 ajouté.

## Lacunes (reprises du dossier, non comblées)
Aucune source suisse ou européenne propre à E12 ou au « type 5 » ; documents OMS de 1985, 1999 et 2019 non lus directement ; code CIM-11 5A12 non vérifié ; aucun essai thérapeutique ; aucune information professionnelle lue pour sulfonylurées, glinides, inhibiteurs de la DPP-4 (monographies correspondantes sans dose) ; aucune donnée de prévalence en Suisse ou chez les migrants ; pas de conduite détaillée de l'hypoglycémie sévère ni de l'acidocétose (hors dossier). La vignette d'ouverture et le cas récapitulatif sont fictifs et signalés comme tels.
