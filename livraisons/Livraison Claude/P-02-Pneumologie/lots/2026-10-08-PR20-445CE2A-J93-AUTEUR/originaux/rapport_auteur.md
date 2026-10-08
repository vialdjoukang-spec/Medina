# Rapport d’auteur — J93 — Pneumothorax (P-02-Pneumologie)

Rédacteur : chaîne interne Claude, 08.10.2026. Version de travail, non injectée. Aucune validation médicale humaine : la relecture IA et les contrôles techniques ne valent pas validation par un médecin.

## Fichiers

- `chapters/J93/J93_a.html` : en-tête, onglets, îlots 0 à 6 de l’onglet Pathologie.
- `chapters/J93/J93_b.html` : îlots 7 à 13 (dernier îlot : critères formels `div.alert`, puis paramètres clés `div.key`).
- `chapters/J93/J93_c.html` : onglets Examens (4 îlots, 3 quiz) et Sciences (anatomie, histologie, physiologie, génétique ; 4 figures SVG légendées).
- `chapters/J93/J93_d.html` : onglet Pharmacologie (3 îlots), fermeture du template.
- `chapters/J93/J93_pop1.html`, `J93_pop2.html` : 43 fenêtres explicatives et 6 Pareto (49 templates `data-pop`).
- `glossary/j93.py` : BTS, ACCP, ATLS, GRADE, FLCN, TSC1, TSC2, CFTR, J93.0, J93.1, J93.8, J93.9, J95.80, S27.0, P25.1.

## Plan

Pathologie : 0 question clinique ; 1 définition, classification, codage et exclusions (S27.0, J95.80, P25.1, A15–A16, J86, traités par renvoi en fenêtre) ; 2 épidémiologie et récidive ; 3 physiopathologie (pression pleurale, rétraction, effet shunt, mécanisme valvulaire, résorption) ; 4 étiologies (tabac, causes secondaires, génétique, cataménial) ; 5 anamnèse ; 6 examen clinique ; 7 diagnostic et différentiels ; 8 tension et complications (`alert`) ; 9 prise en charge BTS 2023 (algorithme, essais Brown 2020, Hallifax 2020, Marx 2023, fenêtre de contentieux BTS 2023 / ERS 2015 / BTS 2010) ; 10 prévention des récidives ; 11 suivi, tabac, avion, plongée ; 12 situations particulières (secondaire, mucoviscidose, grossesse, endométriose, patient ventilé, VIH) et cas récapitulatif ; 13 critères formels et paramètres clés.

Examens : hiérarchie et gold standard (scanner) ; lecture et mesure radiographiques (BTS, ACCP, Collins) ; échographie et scanner ; 3 quiz. Sciences : 4 disciplines de 378 à 417 mots, chacune avec figure et liens Science → clinique, examen, traitement, À retenir. Pharmacologie : classes, doses adulte, risques (`alert`).

Volume : environ 13 000 mots tous fichiers confondus, dont la majorité dans les fenêtres ; 59 mots verts ; 3 quiz ; 6 Pareto.

## Sources consultées le 08.10.2026

| Source | Accès | Usage |
|---|---|---|
| Roberts ME et al., BTS Guideline for pleural disease, Thorax 2023, doi:10.1136/thorax-2022-219784 | Texte intégral (PDF BTS) | Définitions, recommandations A1 à A5, haut risque, conseils de sortie, vol, plongée, grossesse, cataménial, mucoviscidose, familial, iatrogène et traumatique, indications chirurgicales, méta-analyses de récidive |
| BTS 2023, annexe 1, parcours du pneumothorax | Texte intégral (PDF BTS) | Six caractéristiques à haut risque, seuil de 2 cm, rythme de surveillance |
| BTS, déclaration sur les gestes pleuraux 2023, annexe 12 | Résumé par moteur de recherche du PDF BTS | Lidocaïne 3 mg/kg, maximum 250 mg avant talc ; talc 4–5 g dans 50 mL |
| Tschopp JM et al., ERS task force PSP, Eur Respir J 2015;46:321-335 | Résumé PubMed | Approche fondée sur les symptômes, talc calibré, vidéothoracoscopie |
| Brown SGA et al., N Engl J Med 2020;382:405-415 | Résumé PubMed ; chiffres de récidive (16,8 % contre 8,8 %) via commentaires secondaires | Surveillance |
| Hallifax RJ et al., Lancet 2020 | Résumé PubMed | Dispositif ambulatoire |
| Marx T et al., Am J Respir Crit Care Med 2023;207:1475-1485 | Résumé PubMed | Aspiration contre drain |
| Walker SP et al., Eur Respir J 2018 | Résumé PubMed | Récidive 29 % à un an, 32 % au total ; sexe féminin ; arrêt du tabac |
| Melton LJ et al., Am Rev Respir Dis 1979 ; Bense L et al., Chest 1987 | Résumés PubMed | Incidence, risque tabagique |
| Collins CD et al., Am J Roentgenol 1995 | Résumé PubMed | Formule de taille |
| Alrajhi K et al., Chest 2012 ; Lichtenstein D et al., Intensive Care Med 2000 | Résumés PubMed | Performances de l’échographie, point poumon |
| Tschopp JM et al., Eur Respir J 2002 (essai suisse de talcage) | Résumé PubMed | Pleurodèse |
| O’Driscoll BR et al., BTS oxygène, Thorax 2017 | Métadonnées PubMed ; cibles connues | Cibles de saturation |
| Lott C et al., ERC 2021, Resuscitation 2021;161:152-219 | Résumé PubMed | Thoracostomie dans l’arrêt traumatique |
| BfArM, CIM-10-GM 2024, bloc J90–J94 (extrait du dépôt) | Extrait du catalogue | Codes et exclusions |
| Compendium suisse, Paracétamol Sandoz eco 500 mg | Repris du cours J40 (vérifié par son auteur) | Dose de paracétamol |

Aucune recommandation nationale suisse sur le pneumothorax n’a été identifiée ; la déclaration ERS 2015 est présidée par J.-M. Tschopp (Montana, Valais) et l’essai de talcage 2002 est suisse. La recommandation allemande AWMF de 2018 est signalée expirée par son éditeur.

## Réserves pour le relecteur

1. **ATLS** : site d’exsufflation de l’adulte (4e–5e espace intercostal en avant de la ligne axillaire moyenne) et longueur de cathéter d’environ 8 cm vérifiés seulement par des sources secondaires ; manuel ATLS non lu. Vérifier si une 11e édition a modifié la règle.
2. **ERC** : les recommandations ERC 2025 (Resuscitation, vol. 215, suppl. 1) n’ont pas pu être lues ; la mention de la thoracostomie au doigt est attribuée à l’ERC 2021. À contrôler contre ERC 2025.
3. **BTS 2010** (doi:10.1136/thx.2010.136986) : texte intégral inaccessible (403). Les chiffres de résorption (1,25 à 2,2 % par jour, jusqu’à quatre fois sous oxygène), la limite d’aspiration de 2,5 L et la définition « 2 cm au hile ≈ 50 % » sont cités de mémoire documentaire et corroborés par des sources secondaires.
4. **Brown 2020** : chiffres de récidive à 12 mois issus de commentaires secondaires concordants (dénominateurs 149 et 159), non du texte intégral.
5. **Annexe 12 BTS** (lidocaïne, talc) lue via un résumé du PDF, non directement.
6. **Glossaire** : la clé `BTS` est aussi définie dans le dossier de travail J96 (non canonique) ; garder une seule définition à l’injection. J86 et J90 pourraient l’utiliser.
7. **Contrôle des sciences** (`tests/audit_sciences.py`) : il exige une version de base Git pour tout cours intégré sauf J40 ; J93 étant nouveau, le test devra être adapté comme pour J40.
8. Les noms composés (Birt‑Hogg‑Dubé, Ehlers‑Danlos, Boyle‑Mariotte, Nouvelle‑Zélande, Royaume‑Uni, Jean‑Marie) emploient un trait d’union insécable (U+2011) pour ne pas être pris pour des sigles par l’audit.

## Contrôles effectués (copie de travail dans le scratchpad)

- `build_medina.py J93` : `J93 non couvertes: 0`, Pareto calculés sans erreur.
- `test_v7.py --static J93` : OK (clés, préfixes, classes de la liste fermée, aucun style en ligne).
- Contrôle Playwright ad hoc sur l’aperçu : 59 mots verts ouvrent une fenêtre non vide ; quatre onglets affichés ; seule erreur JavaScript : `lesson-core.js` introuvable en aperçu, tolérée par `test_v7.py`. Le test navigateur complet de `test_v7.py` échoue sur l’aperçu par interception de clic de la barre latérale ; le même échec se produit avec J40 dans les mêmes conditions (environnement d’aperçu, non spécifique à J93).
- Contrat sciences vérifié avec les fonctions de `tests/audit_sciences.py` : 4 disciplines, figure et quatre liens présents dans chacune.
