# Rapport d’auteur — J84 — Pneumopathies interstitielles diffuses (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 08.10.2026. Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.

## Fichiers

- `chapters/J84/J84_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (Pareto clinique).
- `chapters/J84/J84_b.html` — îlots 7 à 13 (Pareto diagnostic, traitements, critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/J84/J84_c.html` — Examens (4 îlots, 3 quiz, Pareto) et Sciences (Anatomie, Histologie, Physiologie, Biologie cellulaire, Génétique ; 5 figures SVG légendées, liens Science → clinique / examen / traitement / À retenir).
- `chapters/J84/J84_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J84/J84_pop1.html`, `J84_pop2.html` — 41 fenêtres `j84-…` et 6 Pareto.
- `glossary/j84.py` — 41 clés nouvelles, aucune présente dans `glossary/` du dépôt ni dans les dossiers de travail J09/J96 au 08.10.2026. Choix délibéré : `ATS/ERS/JRS/ALAT` est une clé composée pour ne pas créer une clé `ALAT` qui capterait l’alanine aminotransférase dans d’autres cours.

## Plan

Pathologie : 0 question clinique ; 1 définitions, classification ATS/ERS 2013, tableau J84.0/J84.1/J84.8/J84.9 et exclusions (J67, D86 par renvoi) ; 2 épidémiologie et histoire naturelle ; 3 physiopathologie (micro-lésions, réparation aberrante, foyers fibroblastiques, MUC5B, télomères) ; 4 causes à rechercher ; 5 anamnèse ; 6 examen ; 7 diagnostic (TDM UIP/probable/indéterminée/alternative, sérologie, EFR/DLCO, discussion multidisciplinaire, LBA, cryobiopsie, différentiels hiérarchisés) ; 8 exacerbation aiguë et complications ; 9 traitement de la FPI (nintédanib, pirfénidone, nérandomilast, oxygène, réhabilitation, vaccins, à éviter, transplantation ISHLT) ; 10 connectivites, PINS, FPP (critères 2022, INBUILD, ERS/EULAR 2025) ; 11 suivi, GAP, soins palliatifs ; 12 situations particulières et cas récapitulatif ; 13 critères formels et paramètres clés.

## Sources consultées (08.10.2026)

| Source | Accès |
|---|---|
| Raghu et al., ATS/ERS/JRS/ALAT 2022, AJRCCM 205:e18 (PMC9851481) | texte intégral partiel (tableaux 3 et 4, recommandations cryobiopsie, antiacides, chirurgie antireflux) ; aucune mise à jour 2025 identifiée |
| Raghu et al., ATS/ERS/JRS/ALAT 2018 (diagnostic) | citée, non relue intégralement |
| Travis et al., classification ATS/ERS 2013 (PMID 24032382) | métadonnées PubMed |
| Collard et al., exacerbation aiguë 2016 (PMID 27299520) | métadonnées PubMed |
| Naccache et al., EXAFIP, Lancet Respir Med 2022 (doi 10.1016/S2213-2600(21)00354-4) | résumé PubMed |
| Richeldi et al., FIBRONEER-IPF, NEJM 2025 (doi 10.1056/NEJMoa2414108) ; Maher et al., FIBRONEER-ILD (doi 10.1056/NEJMoa2503643) | résumés PubMed (chiffres repris) |
| Leard et al., consensus ISHLT 2021 (doi 10.1016/j.healun.2021.07.005) | résumé PubMed ; critères d’orientation/inscription repris de mémoire du texte, à vérifier en intégral |
| Ley et al., indice GAP 2012 (PMID 22586007) ; Raghu et al., PANTHER-IPF 2012 (PMID 22607134) | métadonnées PubMed ; chiffres connus du texte original |
| Maher et al., incidence/prévalence 2021 (PMC8261998) | résumé |
| Antoniou et al., ERS/EULAR 2025 PID des connectivites (doi 10.1016/j.ard.2025.08.021) | résumés secondaires seulement |
| Funke-Chambour et al., Respiration 2017 (position suisse) | résumé seulement |
| Ofev (nintédanib) RCP britannique révisé 02.10.2025 | texte intégral partiel (posologie, foie, contre-indications, interactions) |
| Esbriet (pirfénidone) RCP | extraits via recherche |
| FDA (nérandomilast, octobre 2025) ; EMA, Jascayd (CHMP 21.05.2026, autorisation UE juillet 2026) | communiqués et pages de recherche |
| compendium.ch (Ofev, Esbriet, nérandomilast) | **accès impossible** (connexion exigée) |

## Réserves

1. **Monographies suisses non lues** (compendium.ch inaccessible) : doses et contre-indications issues des RCP européens/britanniques ; indications suisses d’Ofev (FPP, sclérodermie) non confirmées.
2. **Nérandomilast** : autorisation Swissmedic non confirmée au 08.10.2026 ; présenté comme autorisé FDA/UE. Restriction « 9 mg non recommandé avec la pirfénidone » attribuée à l’étiquetage américain.
3. Critères ISHLT 2021 de la fenêtre `j84-transplantation` : à vérifier en texte intégral (seuils d’inscription).
4. Recommandation ERS/EULAR 2025 : lue par résumés secondaires ; les choix de molécules par connectivite sont à confirmer dans le texte primaire.
5. Ciprofloxacine → pirfénidone 534 mg trois fois par jour, surveillance hépatique pirfénidone (mensuelle six mois puis trimestrielle) : RCP européen, non relu en intégral pour la version 801 mg.
6. Chiffres non vérifiés en texte intégral mais issus des publications primaires connues : INPULSIS (−113,6 contre −223,5 mL), ASCEND (47,9 %), INBUILD (−80,8 contre −187,8 mL), SENSCIS (−52,4 contre −93,3 mL), PANTHER (8 contre 1 décès), GAP (5,6/16,2/39,2 %), réhabilitation (≈ 40 m, Cochrane 2021), LBA normal, épaisseur de barrière, compliance 200 mL/cm d’eau.
7. Aucune donnée épidémiologique suisse identifiée ; lacune nommée dans le cours.
8. Recommandation suisse : seule la position de 2017 (Funke-Chambour) a été trouvée ; aucune recommandation plus récente de la Société suisse de pneumologie identifiée.
9. `tests/audit_sciences.py` compare chaque cours intégré à un commit de base où J84 n’existe pas ; seul J40 y est exempté. L’injection exigera d’ajouter J84 à cette exception (décision du relecteur).

## Contrôles effectués (copie scratchpad, glossaire complet du dépôt + j84.py)

- `python3 build_medina.py J84` : `J84 non couvertes: 0`, Pareto calculés (exemple : 91 mots sur 1941, 5 %).
- Toutes les clés `data-k` ont leur `template data-pop` ; toutes préfixées `j84-` ou `pareto-j84-` ; aucun identifiant dupliqué. Deux fenêtres (`j84-fpi-def`, `j84-genetique`) servent uniquement de renvoi depuis le glossaire.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 5 disciplines de 334 à 374 mots, une figure SVG `role="img"` légendée chacune, les quatre liens présents.
- `test_preview.py J84` (Chromium 1194) : **OK**, après filtrage d’une erreur d’environnement sans lien avec le cours (`preview/lesson-core.js` absent de la coque). Clic des 59 mots verts des quatre onglets : aucune « Fiche absente », aucune erreur JavaScript.
- Volume : environ 14 200 mots (cours et fenêtres), 41 fenêtres, 6 Pareto, 3 quiz.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires du dépôt, injection.
