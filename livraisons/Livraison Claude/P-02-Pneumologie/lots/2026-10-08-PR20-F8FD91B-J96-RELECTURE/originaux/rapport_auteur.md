# Rapport d’auteur — J96 — Insuffisance respiratoire aiguë et chronique (P-02-Pneumologie)

Rédacteur : chaîne interne Claude, 08.10.2026. Statut : **version de travail**, non injectée, non relue par le relecteur différé, **non validée par un médecin**. Les contrôles techniques ci-dessous ne valent pas validation médicale.

## Périmètre

Cours unique couvrant la catégorie CIM-10-GM 2024 **J96 — Insuffisance respiratoire, non classée ailleurs** : J96.0 aiguë, J96.1 chronique, J96.9 sans précision, avec le cinquième caractère du type (0 hypoxémique, 1 hypercapnique, 9 non précisé) et le double codage de l’acutisation (J96.0 + J96.1). Entrée proposée pour `chapters.json` et `organisation/course_groups.json` : `code` J96, `covers` ["J96"], titre « Insuffisance respiratoire aiguë et chronique », `owner` S02.

## Fichiers produits

| Fichier | Contenu | Mots | Octets |
|---|---|---|---|
| `chapters/J96/J96_a.html` | En-tête, onglets, îlots 0 à 7 de l’onglet Pathologie | 2 987 | 26 717 |
| `chapters/J96/J96_b.html` | Îlots 8 à 14 (prise en charge, chronicité, critères formels, références) | 3 114 | 25 377 |
| `chapters/J96/J96_c.html` | Onglets Examens (5 îlots, 5 quiz) et Sciences (4 disciplines, 4 figures SVG) | 3 812 | 35 277 |
| `chapters/J96/J96_d.html` | Onglet Pharmacologie (4 îlots), fermeture du gabarit | 1 199 | 10 781 |
| `chapters/J96/J96_pop1.html` | 50 fenêtres de l’onglet Pathologie et 4 Pareto | 6 472 | 58 050 |
| `chapters/J96/J96_pop2.html` | 14 fenêtres Examens et Pharmacologie et 2 Pareto | 1 976 | 18 668 |
| `glossary/j96.py` | 28 clés nouvelles | — | 8 664 |

Totaux : environ 19 600 mots, **66 fenêtres** (dont 6 Pareto), **71 mots verts**, **5 quiz**, **4 figures** SVG noir et blanc légendées.

## Plan

**Pathologie et prise en charge** : 0 question clinique chiffrée (pneumonie de type 1 et BPCO acutisée sous oxygène excessif) ; 1 définitions gazométriques, types, temporalité et codage ; 2 physiologie normale (échangeur et pompe, ventilation alvéolaire et espace mort) ; 3 cinq mécanismes de l’hypoxémie (tableau gradient × réponse à l’oxygène) ; 4 hypercapnie (commande, capacité, charge ; sommeil ; acutisation) ; 5 causes par niveau ; 6 clinique et signes de gravité ; 7 démarche diagnostique ; 8 urgence et oxygénothérapie titrée ; 9 oxygène nasal à haut débit ; 10 ventilation non invasive ; 11 intubation ; 12 insuffisance chronique (oxygénothérapie de longue durée, ventilation à domicile selon la Société suisse de pneumologie) ; 13 suivi et situations particulières ; 14 critères formels (`div.alert`) puis paramètres clés (`div.key`). Pareto : mécanismes (0–5), clinique (6–7), supports (8–11), chronicité et critères (12–14).

**Examens** : hiérarchie question → examen → statut (gazométrie artérielle = référence) ; gazométrie (prélèvement, lecture en six étapes, compensation, exemples calculés) ; oxymétrie, capnographie, PtcCO₂ ; imagerie, fonction respiratoire, sommeil, tableau de six profils gazométriques ; 5 quiz.

**Sciences** : physiologie (rapport ventilation/perfusion, équation des gaz alvéolaires) ; biochimie (courbe de dissociation, contenu en oxygène, transport du dioxyde de carbone, effet Haldane) ; neurophysiologie (chémorécepteurs, sommeil, émoussement chronique) ; physiopathologie de l’hypercapnie induite par l’oxygène (levée de la vasoconstriction hypoxique, effet Haldane, baisse modeste de la commande). Chaque discipline : figure, liens Science → clinique, examen, traitement, À retenir.

**Pharmacologie** : l’oxygène comme médicament (dispositifs et FiO₂) ; toxicité (IOTA, atélectasies, bléomycine et paraquat) ; sédation et analgésie autour de la ventilation (morphine 2,5–5 mg par voie intraveineuse selon la BTS et l’Intensive Care Society) ; traitement de la cause par renvoi bref à J44, J45, J18 et I26.

## Sources consultées (08.10.2026)

| Source | Accès | Usage |
|---|---|---|
| O’Driscoll et al., BTS guideline for oxygen use in adults, Thorax 2017 ; 72 Suppl 1 | **Texte intégral lu** (PDF BTS) ; résumé hospitalier (annexe 3) lu ; revue BTS 2019 lue en résumé | Cibles, dispositifs, débits, contrôle à 30–60 min, rebond, F16, CO, grossesse, physiologie |
| Rochwerg et al., ERS/ATS NIV guidelines, Eur Respir J 2017 ; 50 : 1602426 | **Texte intégral lu** (copie ATS) | Indications, forces de recommandation, RR mortalité 0,63, intubation 0,41 |
| Davidson et al., BTS/Intensive Care Society, Thorax 2016 ; 71 Suppl 2 | **Texte intégral lu** | Seuils de début, réglages IPAP/EPAP, échec, intubation, sédation, acétazolamide |
| Oczkowski et al., ERS HFNC guidelines, Eur Respir J 2022 ; 59 : 2101574 | **Résumé lu** (PubMed ; texte intégral refusé, erreur 403) | Huit recommandations conditionnelles |
| Janssens et al., Société suisse de pneumologie, Respiration 2020 ; 99 : 867–902 | **Texte intégral lu** (archive ouverte UNIGE) | Ventilation à domicile (BPCO, syndrome obésité-hypoventilation, maladies neuromusculaires et de la paroi), critères nocturnes, essais RESCUE, HOT-HMV, germano-autrichien |
| GOLD 2026, guide de poche | **Texte lu** ; les figures (images) n’ont pas pu être extraites | Critères d’oxygénothérapie de longue durée |
| Haidl et al., recommandation germanophone sur l’oxygénothérapie de longue durée, 2020 (participation de la Société suisse de pneumologie) | Fiche Guidelines Schweiz lue ; **texte intégral inaccessible** (AWMF erreur 500, Thieme protection anti-robot) ; critères vérifiés par sources secondaires | Seuils et répétition des mesures |
| Société allemande de pneumologie, prise de position 2014 | Texte intégral lu | Données des essais du Medical Research Council et NOTT |
| Ligue pulmonaire suisse, pages et formulaires de prescription (2022) | **Lus en résumé** par moteur de recherche ; accès direct refusé (403) | 16 h/jour, prescription, rôle de la Ligue, oxygène liquide |
| OFSP, modifications de la MiGeL au 01.07.2025 | Titre et existence vérifiés ; contenu non lu | Cadre de remboursement |
| CIM-10-GM 2024, bloc J95–J99 | Extrait embarqué dans `shell/medina_front.html` | Codage, exclusions, cinquième caractère |
| Essais : Austin (BMJ 2010), FLORALI (NEJM 2015), IOTA (Lancet 2018), Roca (2019), Sjoding (NEJM 2020), Berend (NEJM 2014), Lichtenstein (Chest 2008) | Résumés PubMed lus ; Sjoding en texte intégral (PMC) | Chiffres cités |
| ATS/ERS statement on respiratory muscle testing 2002 | Non relu ce jour ; référence connue | PImax &gt; 80 cm H₂O |

## Réserves

1. **Validation** : aucune relecture médicale humaine ; le relecteur différé doit vérifier fond, chiffres et langue.
2. **Recommandation suisse d’oxygénothérapie de longue durée** : le texte germanophone 2020 n’a pas été lu en intégral ; sa validité affichée sur Guidelines Schweiz est « 2025 ». Aucune version plus récente n’a été trouvée. Le nombre de mesures (trois en quatre semaines) provient de sources secondaires.
3. **Ligue pulmonaire et MiGeL** : contenus lus en résumé ; la durée de 16 h/jour et les modalités de prescription sont attribuées au formulaire de la Ligue pulmonaire sans lecture directe.
4. **ERS 2022 haut débit** : seules les huit recommandations du résumé sont citées ; la phrase sur l’œdème pulmonaire cardiogénique (texte de 2017 non contredit) est une interprétation de l’auteur, signalée comme choix dans la fenêtre de contentieux.
5. **Oxygène médicinal** : la monographie suisse n’a pas pu être consultée (Compendium et base ODDB inaccessibles) ; la fenêtre le dit explicitement.
6. **Repères non relus ce jour** : règle âge/4 + 4 du gradient (présentée comme aide pédagogique), seuil de cyanose (50 g/L), règles de compensation (Berend 2014, résumé), PImax &gt; 80 cm H₂O (ATS/ERS 2002), durée d’action de la naloxone, seuil HACOR non chiffré, essai britannique de 2022 dans la COVID-19 cité sans nom ni chiffre. Aucune posologie de naloxone, d’hypnotique ou de curare n’est donnée.
7. **Épidémiologie** : aucune donnée suisse d’incidence n’a été retenue faute de source vérifiée ; l’îlot épidémiologique de la grille historique est remplacé par des données pronostiques sourcées (ERS/ATS, Austin, IOTA).
8. **Contrôle `tests/audit_sciences.py`** : ce script lève une erreur pour tout cours absent du commit de base, sauf J40. À l’injection, le relecteur devra ajouter J96 à cette exception ou adapter le contrôle ; les critères de fond (≥ 280 mots, figure accessible, quatre liens) sont satisfaits (430 à 500 mots par discipline).
9. **Renvoi vers l’insuffisance cardiaque** : le cours I50 appartient au fragment de cardiologie ; le texte le désigne sans lien pour éviter un renvoi étranger.

## Contrôles techniques (copie temporaire du dépôt dans le scratchpad, fichiers canoniques intacts)

- `python3 build_medina.py J96` : **J96 non couvertes : 0** ; ratios Pareto calculés (11 à 15 %).
- Toutes les clés `data-k` ont leur `<template data-pop>` ; aucune clé sans préfixe `j96-` ; aucun identifiant dupliqué ; classes limitées à la liste fermée.
- Clés de glossaire : aucune redéfinition d’une clé existante (vérifié contre les 1 386 clés).
- `python3 build_front.py --fragment S02` (avec entrées temporaires dans `chapters.json` et `organisation/course_groups.json` de la copie) : construction réussie, aucune abréviation non couverte.
- `node tests/verify_course_native.cjs J96` sur le fragment construit : **passed**, 1 905 contrôles, 71 déclencheurs directs sur ordinateur et mobile, 66 gabarits couverts, 0 échec.
- `python3 -m unittest discover -s tests -p 'test_*.py'` : 176 tests OK.
- `test_preview.py` : échec « lesson-core.js » en `file://`, identique pour J40 ; défaut préexistant du banc, sans lien avec J96.
- Captures de contrôle (ouverture, fenêtre de l’équation des gaz alvéolaires, figure de la courbe de dissociation) : rendu correct ; chevauchement de deux étiquettes de la figure 2 corrigé.
