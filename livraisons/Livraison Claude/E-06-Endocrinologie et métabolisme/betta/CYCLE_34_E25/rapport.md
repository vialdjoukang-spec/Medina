# Rapport de rédaction — E25 Anomalies génito-surrénaliennes (cycle Betta 34, leçon 1)

Agent : C34-A2-ENDO (Sonnet 5.5). Dossier de recherche utilisé : `recherche.md` et `sources.json` (17 sources S1 à S17). Aucune donnée extérieure au dossier.

## Fichiers produits (octets)
- `chapters/E25/E25_a.html` 21 744 (îlots 0 à 6) ; `E25_b.html` 16 144 (îlots 7 à 12, critères formels `div.alert` puis paramètres clés `div.key`) ; `E25_c.html` 21 475 (Examens : 4 îlots dont 4 cas cliniques ; Sciences : Anatomie, Physiologie, Biochimie, Génétique) ; `E25_d.html` 7 616 (Pharmacologie) ; `E25_pop1.html` 36 125 et `E25_pop2.html` 13 371 (58 fenêtres dont 13 Pareto) ; `glossary/e25.py` 9 944 (ajouts conditionnels, 40 clés).
- Empreintes SHA-256 : voir `sha256sum` sur le dossier (commande de preuve du cahier).

## Auto-contrôle (cahier W)
HTML bien formé ; identifiants uniques et préfixés `e25-` ; toutes les clés `data-k` ont une fenêtre, aucune fenêtre orpheline ; identifiants Pareto couverts existants ; `build_medina.audit()` renvoie `{}` (glossaire racine plus `e25.py`, banc de test hors dépôt).

## Sources utilisées
S1 à S17 (OFS, OMS, Endocrine Reviews 2022, Human Reproduction Update 2017, EJE 2019, Lancet 2023, J Endocr Soc 2025, dépistage néonatal suisse, brochure AGS 2023, J Pediatr Endocrinol Metab 2019, deux essais NEJM 2024, informations professionnelles suisses Alkindi, Hydrocortisone Galepharm, Solu-Cortef, Florinef). Le statut des sources abrégé seul est signalé dans les fenêtres.

## Lacunes (reprises du dossier, explicitées dans le cours)
Article SMF 2017 non utilisé ; aucune recommandation SSED ou ESE propre à l’HCS ; dose et moment du test à l’ACTH, stades de Prader, protocole de confirmation néonatale, valeurs de référence par âge non lus ; formes acquises non documentées ; statut suisse du crinécerfont non vérifié ; cadre légal suisse de la chirurgie génitale non lu ; contre-indications et interactions des informations professionnelles non relevées. L’histologie n’est pas traitée comme science séparée (aucune donnée dans le dossier) ; l’anatomie est volontairement limitée.

Audit différé — revue IA, distincte d’une validation médicale humaine.
