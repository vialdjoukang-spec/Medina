# Rapport de rédaction — G07, cycle Betta 34, leçon 2 (C34-A4-NEUR, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (sous `livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_34_G07/`)
- `chapters/G07/G07_a.html` (≈ 22 Ko) : en-tête, quatre onglets, pathologie îlots 0–6.
- `chapters/G07/G07_b.html` (≈ 24 Ko) : îlots 7–13 (dernier îlot : critères formels `alert` puis paramètres clés `key`), références, fin du panneau.
- `chapters/G07/G07_c.html` (≈ 23 Ko) : examens (e-1 à e-4) et sciences (anatomie, histologie, physiologie, biochimie ; 4 schémas SVG).
- `chapters/G07/G07_d.html` (≈ 11 Ko) : pharmacologie (p-1 à p-5), fermeture du modèle.
- `chapters/G07/G07_pop1.html`, `G07_pop2.html` (≈ 12 + 11 Ko) : 37 fenêtres (dont 13 Pareto, 9 monographies).
- `glossary/g07.py` : codes † et notations 2HRZE/10HR, IFT, PET-CT, POC-CCA, MetronidazoleSINT (ajouts conditionnels).

## Contenu
Quatre maladies causales vues sous l'angle de la lésion focale : tuberculose (tuberculome, abcès), granulome bilharzien, abcès amibien, abcès gonococcique. 14 îlots de pathologie, 4 îlots d'examens, 4 de sciences, 5 de pharmacologie, 4 quiz de cas, 6 Pareto de pathologie plus examens, sciences et pharmacologie.

## Sources utilisées
Uniquement les 29 sources de `sources.json` (CIM-10-GM 2024 BfArM/OFS ; guide OFSP V1.2024 ; lignes directrices 2026 sur la méningite tuberculeuse ; manuel OMS ; recommandation DTG 2017 échue ; IUSTI 2020 ; 13 résumés PubMed ; 6 informations professionnelles suisses). Aucune donnée extérieure.

## Lacunes (reprises du dossier, non comblées)
- Aucune recommandation suisse ou européenne spécifique aux lésions focales ; aucune source sur l'abcès cérébral gonococcique.
- Informations professionnelles suisses de l'isoniazide et du praziquantel non trouvées ; aucune posologie d'isoniazide.
- Histologie du tuberculome (caséum, foyer de Rich), différentiel radiologique (neurocysticercose, toxoplasmose, lymphome), score de Marais 2010, libellés français OFS des codes † : non sourcés, non écrits.
- Conciliation dexaméthasone / praziquantel, grossesse, durée du métronidazole et de la ceftriaxone en localisation cérébrale : non tranchées.
- Plusieurs références lues au niveau du résumé seulement.

## Auto-contrôle (cahier W)
HTML bien formé (équilibre des balises, concaténation a+b+c+d) ; identifiants uniques et préfixés `g07-` ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline ; Pareto couvrant des îlots existants (`build_medina.pareto_ratios` sans erreur) ; audit des abréviations de `build_medina.audit` : `{}` avec `glossary/g07.py`. Le contrôle navigateur (`test_preview.py`) n'a pas été exécuté (aucune injection dans `chapters/` racine).
