# Rapport de rédaction — G06 Abcès et granulome intracrâniens et intrarachidiens (N-05-Neurologie)

Cycle Betta 34, agent C34-A4-NEUR, leçon 1. Rédaction Sonnet 5.5 sur le dossier `recherche.md` + `sources.json` (18 sources lues). Date : 15.10.2026.

## Fichiers (octets)
-  32889 chapters/G06/G06_a.html
-  26224 chapters/G06/G06_b.html
-  33963 chapters/G06/G06_c.html
-  14991 chapters/G06/G06_d.html
-  22558 chapters/G06/G06_pop1.html
-  19561 chapters/G06/G06_pop2.html
-   4071 glossary/g06.py
- 154257 total
- `rapport.md`

## Contenu
- Onglet Pathologie : 16 îlots (g06-0 à g06-15), dont critères formels (`alert`) puis paramètres clés (`key`) en dernier ; 3 Pareto (clinique, urgences et prise en charge, suivi et critères).
- Onglet Examens : 5 îlots, standard de référence nommé (IRM avec diffusion + microbiologie du pus), tableau question-examen-statut, fiches d'interprétation, tableau des configurations, 5 quiz de cas, 1 Pareto.
- Onglet Sciences : 4 sciences (Anatomie, Histologie et évolution, Microbiologie, Pharmacocinétique), 4 schémas SVG noir et blanc légendés, encadrés « Science → clinique », 4 Pareto.
- Onglet Pharmacologie : 5 îlots (classes, doses comparées ligne directrice / information professionnelle suisse, précautions, effets indésirables, à éviter), 1 Pareto ; monographies en fenêtres (ceftriaxone, métronidazole, méropénem, vancomycine, céfotaxime, anti-infectieux du terrain, dexaméthasone, lévétiracétam).
- 42 fenêtres (dont 9 Pareto), environ 14 600 mots, 5 quiz, 4 SVG ; glossaire `g06.py` (DGN, SNG, QJM, codes G06.0–G06.2, A06.6, A54.8, A17.8, A17.1), ajouts conditionnels sans écraser l'existant.

## Sources utilisées
S1 BfArM CIM-10-GM 2024 ; S2 OFS ; S3 ligne directrice S1 DGN/SNG 2021 (validité échue) ; S4 ESCMID 2024 (résumé) ; S5 à S14 cohortes et séries (Brouwer 2014, Bodilsen 2020, Eriksen 2026, Liechti 2026, Perea 2026, Sendi 2008, Zimmerer 2011, Skaaby 2014, Kraus 2024, Luque Paz 2026) ; S15 à S18 informations professionnelles suisses (ceftriaxone, métronidazole, méropénem, vancomycine). Hiérarchie : la source primaire la plus récente prime (ESCMID 2024 sur la ligne directrice 2021) ; divergences exposées dans la fenêtre `g06-divergences`.

## Lacunes (reprises du dossier, signalées dans le cours)
1. Aucune recommandation suisse spécifique ; la ligne directrice co-signée par la SNG est échue.
2. ESCMID : résumé seul lu ; doses pédiatriques et tableaux détaillés non vérifiés.
3. Abcès épidural spinal : aucune recommandation européenne lue (durée, antibiothérapie empirique non sourcées) ; empyème rachidien sous-dural et abcès intramédullaire non documentés.
4. Granulomes non bactériens (tuberculome, cysticercose) renvoyés à G07* ; pédiatrie non documentée au-delà des informations professionnelles.
5. Informations professionnelles suisses non lues : céfotaxime, linézolide, cotrimoxazole, voriconazole, dexaméthasone, lévétiracétam. Mécanisme d'action des médicaments non repris (absent du dossier).
6. Valeurs de référence de laboratoire (protéine C réactive, etc.) absentes du dossier ; le cours renvoie au laboratoire du patient. Mécanisme tissulaire de la prise de contraste annulaire non détaillé par les sources.
7. Aucun critère diagnostique formel validé : faisceau retenu présenté comme tel.

## Auto-contrôle (cahier W)
- HTML bien formé (pile de balises vide), identifiants uniques et préfixés `g06-`, toutes les clés `data-k` ont leur `template data-pop`, aucune fenêtre orpheline, fenêtres préfixées `g06-` / `pareto-g06-`.
- `build_medina.audit` (glossaire fusionné avec `g06.py`) : abréviations non couvertes = 0 ; ratios Pareto calculés sans erreur.
- Aperçu navigateur : seul message d'erreur = module `lesson-core.js` absent de l'environnement d'aperçu temporaire (infrastructure, non lié au chapitre).

Audit différé — revue IA, distincte d'une validation médicale humaine.
