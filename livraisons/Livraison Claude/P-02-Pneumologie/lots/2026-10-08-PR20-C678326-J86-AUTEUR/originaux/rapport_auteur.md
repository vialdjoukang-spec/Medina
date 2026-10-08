# Rapport d’auteur — J86 — Pyothorax (P-02-Pneumologie)

Leçon : **J86 — Pleurésies purulentes et abcès du poumon (P-02-Pneumologie)**, couvrant **J85 — Abcès du poumon et du médiastin** et **J86 — Pyothorax**.
Rédacteur : chaîne interne Claude, 08.10.2026. Statut : version de travail, non relue, non injectée. Revue IA et tests techniques ne valent pas validation médicale.

## Fichiers

- `chapters/J86/J86_a.html` : en-tête, onglets, îlots 0 à 6 de l’onglet Pathologie.
- `chapters/J86/J86_b.html` : îlots 7 à 12 (dernier îlot : `div.alert` critères formels puis `div.key` paramètres clés).
- `chapters/J86/J86_c.html` : onglet Examens (5 îlots, 4 quiz) et onglet Sciences (anatomie, physiologie, biochimie, microbiologie ; 4 schémas SVG noir et blanc).
- `chapters/J86/J86_d.html` : onglet Pharmacologie (4 îlots), fermeture du template.
- `chapters/J86/J86_pop1.html`, `J86_pop2.html` : 50 fenêtres et 6 Pareto.
- `glossary/j86.py` : BTS, ESTS, MIST1, MIST2, RAPID, PILOT, SLIM, J85.0–J85.3, J86.0, J86.00–J86.09, J86.9.

Entrée `chapters.json` proposée : `{"code": "J86", "covers": ["J85", "J86"], "title": "Pleurésies purulentes et abcès du poumon"}`.

## Plan

Pathologie : 0 question clinique ; 1 définitions et codes (continuum simple → compliqué → empyème, abcès, gangrène, médiastin, fistules) ; 2 épidémiologie et pronostic (PILOT, Maskell ; lacune suisse nommée) ; 3 physiopathologie (phases exsudative, fibrinopurulente, organisée ; nécrose liquéfiante) ; 4 agents et terrains (groupe *S. anginosus*, anaérobies, *S. aureus* ; inhalation, dents, alcool) ; 5 anamnèse ; 6 examen ; 7 démarche diagnostique (échographie, ponction, seuils BTS 2023, différentiels : cancer excavé, tuberculose, emboles septiques, mimes du pH bas) ; 8 gravité et complications ; 9 traitement (antibiotique, drain ≤ 14 F, alteplase + dornase, VATS ; abcès) ; 10 suivi, RAPID, prévention ; 11 médiastinite descendante, terrains, cas récapitulatif ; 12 critères formels et paramètres clés.
Examens : hiérarchie question → examen → statut avec examens de référence nommés ; tableau du liquide pleural (normal → empyème) ; imagerie ; microbiologie ; 4 quiz.
Pharmacologie : classes et place ; doses suisses ; enzymes intrapleurales (hors indication) ; risques et interactions.

Chiffres : environ 12 400 mots (corps et fenêtres), 56 fenêtres (dont 6 Pareto), 4 quiz.
Renvois sans répétition : `J18 — Pneumonies de l’adulte`, `A41 — Sepsis`.

## Sources consultées (08.10.2026)

| Source | Accès | Usage |
|---|---|---|
| Roberts ME et al. BTS Guideline for pleural disease. Thorax 2023;78:1143–56. doi:10.1136/thorax-2023-220304 | Texte intégral du résumé des recommandations (PDF) | Seuils pH ≤ 7,2 / 7,2–7,4 / ≥ 7,4 ; LDH > 900 UI/L ; glucose < 3,3 et ≤ 4,0 mmol/L ; flacons d’hémoculture ; drain ≤ 14 F ; RAPID ; alteplase 10 mg + DNase 5 mg ×2/j 3 jours, 5 mg si risque hémorragique ; consentement ; pas de chirurgie d’emblée ; VATS préférée à la thoracotomie ; streptokinase et agent unique non recommandés |
| Rahman NM et al. MIST2. N Engl J Med 2011;365:518–26. doi:10.1056/NEJMoa1012740 | Résumé PubMed | Chiffres de l’essai |
| Maskell NA et al. MIST1. N Engl J Med 2005;352:865–74. doi:10.1056/NEJMoa042473 | Résumé PubMed | Échec de la streptokinase |
| Corcoran JP et al. PILOT. Eur Respir J 2020;56:2000130. doi:10.1183/13993003.00130-2020 | Résumé + PDF auteur (tableau RAPID) | Mortalité 10 %/19 %, par catégorie RAPID, points du score, 18 % de mauvaise hygiène dentaire |
| Rahman NM et al. RAPID. Chest 2014;145:848–55. doi:10.1378/chest.13-1558 | Résumé PubMed | Dérivation du score |
| Bedawi EO et al. ERS/ESTS statement. Eur Respir J 2023;61:2201062. doi:10.1183/13993003.01062-2022 | Résumé PubMed (texte intégral refusé, 403) | Incidence en hausse, avis chirurgical précoce, RAPID non encore interventionnel |
| Maskell NA et al. Am J Respir Crit Care Med 2006;174:817–23. doi:10.1164/rccm.200601-074OC | Résumé PubMed | Bactériologie et mortalité par germe et origine |
| Hassan M et al. SLIM. ERJ Open Res 2023. doi:10.1183/23120541.00635-2022 | Résumé (recherche web) | Durée d’antibiothérapie |
| Kuhajda I et al. Ann Transl Med 2015;3:183. doi:10.3978/j.issn.2305-5839.2015.07.08 | Texte intégral PMC | Définition de l’abcès, flore, durée 28–48 jours, réponse, drainage percutané, chirurgie, mortalité, aminosides |
| Noppen M et al. Am J Respir Crit Care Med 2000;162:1023–6 | Résumé PubMed | Volume (0,26 mL/kg) et cellularité du liquide pleural normal |
| Light RW et al. Ann Intern Med 1972;77:507–13 | Métadonnées PubMed | Critères de Light (contenu classique, non relu en texte intégral) |
| Chaulk RC et al. Mediastinum 2025;9:9. doi:10.21037/med-24-29 | Résumé PubMed | Médiastinite nécrosante descendante |
| BfArM, CIM-10-GM 2024, bloc J85–J86 | Page officielle | Codes et intitulés |
| Compendium : Co-Amoxicillin Labatec 2,2 g ; Augmentin 1 g | Page produit (date de monographie non affichée) | Doses IV 2,2 g 3–4×/j ; orale 1 g 2–3×/j ; contre-indications |
| Actilyse, résumé britannique des caractéristiques (mis à jour le 08.05.2026) | Page EMC | Indications autorisées (thrombolyse) ; usage intrapleural hors indication |

## Réserves

1. **Recommandations suisses (SSI)** : non consultables en texte intégral pour l’empyème et l’abcès (site non rendu) ; le cours renvoie au protocole local et l’indique dans la fenêtre `j86-antibio-pleural`.
2. **Compendium Actilyse et Pulmozyme** : recherche soumise à connexion ; monographies suisses non lues. Indications attribuées au résumé britannique (Actilyse lu ; Pulmozyme via résumés européens). À vérifier par le relecteur.
3. **Clindamycine** : posologie attribuée à Kuhajda 2015, pas à une monographie suisse. **Métronidazole** : aucune dose donnée.
4. **Adaptation rénale** de l’amoxicilline-acide clavulanique : non affichée sur la page Compendium consultée ; aucun chiffre donné.
5. **Critères scanographiques** (empyème vs abcès), **segments déclives**, **hémothorax (hématocrite > 50 %)**, **hippocratisme absent dans la BPCO non compliquée** : connaissances classiques non rattachées à une source primaire relue.
6. **Seuil radiographique de 200 mL** et **examen clinique peu sensible sous 300 mL** : valeurs classiques non sourcées dans le texte.
7. **Contentieux de seuil** : BTS 2023 « pH ≤ 7,2 » contre « < 7,2 » ailleurs ; la source la plus récente est retenue et expliquée dans `j86-seuils-ph`.
8. **Collision de glossaire** : la clé `BTS` est aussi définie dans les dossiers de travail J90, J93 et J96 ; le relecteur ne doit en conserver qu’une à l’injection.
9. **Contrôles** : construction en copie scratch (`build_medina.py J86`) : 0 abréviation non couverte ; toutes les clés `data-k` ont leur fenêtre, aucun identifiant dupliqué, préfixes conformes ; `test_preview.py J86` : OK, après neutralisation d’une erreur d’environnement (`lesson-core.js` introuvable en `file://`), identique sur le cours témoin J40.
