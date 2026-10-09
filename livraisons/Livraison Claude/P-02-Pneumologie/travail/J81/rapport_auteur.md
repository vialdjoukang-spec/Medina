# Rapport d’auteur — J81 — Œdème pulmonaire non cardiogénique (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. **Version de travail** : ni relue par l’agent différé, ni injectée. **Revue par IA uniquement : aucune validation médicale humaine.**

## Fichiers

- `chapters/J81/J81_a.html` : en-tête (code CIM seulement dans l’en-tête discret), quatre onglets, Pathologie îlots 0 à 6 (Pareto clinique).
- `chapters/J81/J81_b.html` : îlots 7 à 12 (Pareto diagnostic, traitements, critères). Le dernier îlot contient les critères formels (`div.alert`), puis les paramètres clés (`div.key`).
- `chapters/J81/J81_c.html` : Examens (4 îlots, 4 quiz, Pareto) et Sciences (Anatomie, Physiologie, Physiologie de l’altitude, Immunologie, Neurophysiologie). Chaque discipline a une figure SVG légendée et des encadrés Science → clinique / examen / traitement / À retenir.
- `chapters/J81/J81_d.html` : Pharmacologie (4 îlots, Pareto). Ce fichier ferme le template.
- `chapters/J81/J81_pop1.html` (28 fenêtres) et `J81_pop2.html` (12 fenêtres et 6 Pareto) : 46 gabarits au total, tous atteints par un `data-k`.
- `glossary/j81.py` : 6 clés nouvelles, OPHA, TRALI, TACO, ISBT, UIAA et HNA. Aucune ne figure dans `glossary/*.py` ni dans les glossaires de travail, vérification du 09.10.2026.

Toutes les références sont des liens `<a … data-reference-source="1">`, convention déjà reconnue par `build_medina.audit` (A41, A53). Ce choix évite que des noms d’auteurs à trait d’union soient pris pour des sigles. Le cours compte 7 figures, 5 quiz (1 en Pathologie, 4 en Examens) et environ 14 500 mots hors références et SVG (J84 : 11 300 selon la même mesure). Le cours traite huit entités.

## Plan (monographique)

0. Question clinique : OPHA à 4559 m, fil rouge.
1. Définition et classification par mécanisme : hydrostatique sans cardiopathie, origine artérielle pulmonaire, lésionnel, mixte. Un tableau donne la conséquence thérapeutique.
2. Épidémiologie et pronostic, avec un tableau par entité et des données suisses d’hémovigilance pour 2024.
3. Physiopathologie : Starling, facteurs de sécurité, rapport des protéines, clairance alvéolaire, voies propres à chaque entité (figure 1).
4. Causes, délais et terrains, avec un tableau.
5. Anamnèse : formes typique et trompeuses, erreur fréquente.
6. Examen clinique.
7. Diagnostic : quatre questions, échographie, rapport des protéines, algorithme (figure 2), différentiels classés par gravité, quiz.
8. Urgences et complications (`alert`).
9. Traitement selon le mécanisme : OPHA, TACO/TRALI, neurogénique, pression négative, immersion, opioïdes, acétazolamide, réexpansion. Un tableau de synthèse indique les gestes à éviter.
10. Suivi et prévention : profil d’ascension, prophylaxie, transfusion lente, plasma masculin, plongée.
11. Situations particulières : grossesse, sujet âgé, insuffisance rénale et hépatique, enfant (renvoi), cas récapitulatif.
12. Critères formels : TRALI I et II (2019), TACO (ISBT 2018), œdème des opioïdes (Sporer), OPHA (diagnostic clinique UIAA). Puis les paramètres clés.

## Sources consultées (09.10.2026)

Les liens PubMed ont été vérifiés par `esummary` d’eutils (auteur, année, revue concordants). Les pages PubMed renvoient le code HTTP 203 au client automatique. Les URL officielles et AmiKo renvoient le code 200.

| Source | Mode d’accès réel |
|---|---|
| Commission médicale de l’UIAA (siège à Berne), déclaration de consensus n° 2, version 3.3, 2012, révisée en 2024 | PDF intégral téléchargé (theuiaa.org), lu en entier |
| Swissmedic, Hémovigilance, rapport annuel 2024 (FR) | PDF intégral téléchargé, chapitres réactions et TACO/TRALI lus |
| ISBT/IHN/AABB, définition du TACO 2018 (web 03.2019) | PDF intégral téléchargé (isbtweb.org) |
| Vlaar et al., Transfusion 2019, PMID 30993745, PMC6850655 | texte intégral (PMC) |
| Luks, Swenson et Bärtsch, Eur Respir Rev 2017, PMID 28143879 | texte intégral (Europe PMC), sections OPHA, prévention et traitement |
| Davison et al., Crit Care 2012, PMID 22429697 | texte intégral (PMC) |
| Beretta et al., Front Physiol 2021, PMID 34987415 | texte intégral (Europe PMC) |
| Komiya et al., Crit Care 2017, PMID 28841896 | texte intégral (Europe PMC) |
| Grünig et al., Front Physiol 2017, PMID 28912730 | texte intégral (Europe PMC) |
| Bhaskar et Fraser, Saudi J Anaesth 2011, PMID 21957413 | texte intégral (Europe PMC) |
| Gargani et Volpicelli, Cardiovasc Ultrasound 2014, PMID 24993976 | texte intégral (Europe PMC) |
| Copetti et al., Cardiovasc Ultrasound 2008, PMID 18442425 | résumé et tableau, avec reproduction dans Komiya |
| Grasselli et al., ESICM 2023, PMID 37326646 | texte intégral, passages sur la définition |
| Maggiorini 2006 (17015867), Bärtsch 1991 (1922223), Sartori 2002 (12023995), Oelz 1989 (2573760), Scherrer 1996 (8592525), Maggiorini 2001 (11319198), Bärtsch 2005 (15703168), Swenson 2002 (11980523) | résumés PubMed (eutils efetch) |
| Bhattacharya 2016 (27063348), Feller Kopman 2007 (17954079), Lentz 2019 (30772283), Sporer 2001 (11713145), Ware 2001 (11371404), Matthay 2014 (24881936) | résumés PubMed |
| Berlin 2012 (22797452), Mueller/HFA 2019 (31222929), Pichler Hefti/UIAA 2023 (37906126), Banham 2024 (39675743), Wiersum Osselton 2019 (31080132) | résumés PubMed |
| BfArM, CIM-10-GM 2024, bloc J80-J84 | page officielle, inclusions et exclusions de J81 (en-tête seulement) |
| AIPS via `tools/swissmedic_fi.py` (AmiKo) : Nifedipin Mepha 20 retard (01.2026), Fortecortin® cp (01.2022), Lasix® inj (03.2025), Diamox® (07.2026), tadalafil générique Spirig (11.2025), naloxone générique Orpha (07.2026), Serevent® (07.2021) | texte intégral : indications, posologie, contre-indications, grossesse, mises en garde |

Sources non retenues ou inaccessibles : ESC 2021 sur l’insuffisance cardiaque (texte intégral bloqué, code 403 ; les seuils aigus des peptides n’ont pas été lus et ne sont pas cités) ; texte intégral HFA 2019 (code 403 ; résumé seul utilisé) ; recommandation pleurale BTS 2023 (code 403) ; Volpicelli 2012 (accès payant) ; Ware et Matthay, N Engl J Med 2005, et Bärtsch et Swenson, N Engl J Med 2013 (sans résumé exploitable, non cités). Aucune recommandation américaine ne fonde une conduite. Les essais nord-américains (Feller Kopman, Lentz, Sporer) sont cités comme données.

## Réserves honnêtes

1. **Aucune incidence globale** suisse ou européenne de l’œdème non cardiogénique : cette lacune est nommée dans l’îlot 2.
2. **OPHA, absence de recommandation suisse lue** : la conduite repose sur l’UIAA (organisme international établi à Berne), la revue Luks 2017 (European Respiratory Review) et les essais suisses. Tous les médicaments de l’OPHA sont **hors indication en Suisse**, ce que le cours signale. La dose de salmétérol de prévention (125 µg toutes les 12 heures) dépasse le maximum de l’AIPS Serevent®.
3. **Doses de nifédipine divergentes** : 20 mg retard à répéter (UIAA) contre 30 mg toutes les 12 heures (Luks). Les deux sont présentées avec leur source. La forme suisse lue est le comprimé retard de 20 mg.
4. **Critères de l’œdème neurogénique** : il s’agit d’une proposition d’auteurs (Davison 2012), présentée comme telle. Le traitement par α-bloquant reste expérimental.
5. **Œdème de réexpansion** : aucune source suisse ou européenne n’a été lue. Les données proviennent de deux études nord-américaines.
6. **Lectures limitées au résumé** pour plusieurs essais (liste ci-dessus) et pour la déclaration SPUMS/UKDMC 2024 et Pichler Hefti 2023.
7. **Notions physiologiques générales non rattachées mot à mot à une source** : correction barométrique comme effet de la pression inspirée d’oxygène ; principe du caisson hyperbare (pression accrue, donc pression inspirée d’oxygène accrue) ; recrutement par pression expiratoire positive ; crépitants comme traduction du liquide alvéolaire. Ces notions sont à sourcer à la relecture.
8. **Enfant** : la recommandation UIAA n° 9 n’a pas été lue ; l’îlot 11 renvoie seulement à son existence.
9. **Captures** produites sur un frontend de fragment construit dans un environnement superposé (scratchpad), non publié : `j81-1-ouverture.png` et `j81-2-explication.png`. Ces fichiers ne sont pas déposés dans le dépôt.

## Contrôles réalisés (environnement superposé, aucun fichier partagé modifié)

| Contrôle | Résultat |
|---|---|
| `build_medina.py J81` (glossaire racine + j81.py) | `J81 non couvertes: 0` ; Pareto calculés sans erreur |
| Clés, gabarits et identifiants | 46 `data-k` = 46 gabarits ; aucun identifiant dupliqué ; ancres internes valides ; couvertures Pareto existantes |
| Faux sens de sigles existants | vérifié : le sigle `A1` du glossaire (albuminurie) a été évité, de même que `A5`, `Royaume-Uni`, `Pays-Bas` et `MR-proANP` |
| `build_front.py --fragment S02` avec J81 temporairement intégré dans la copie superposée | construit (4,66 Mo, puis 2,44 Mo compressé) |
| Chromium 1194, `#/entry/J81` | titre correct ; 4 onglets non vides ; 58 mots verts visibles cliqués, 58 fenêtres avec contenu ; aucune erreur JavaScript ni console ; mobile 390 px sans défilement horizontal ; 7 figures contrôlées visuellement (figures 6 et 7 corrigées pour un débordement de texte) |
| `test_preview.py` sur l’aperçu autonome | échec `lesson-core.js` (import dynamique en `file://`), identique pour J84 : défaut d’environnement, sans lien avec J81 |

Aucune opération Git. Aucun fichier modifié hors de `travail/J81/`. Ni `chapters.json`, ni `organisation/*`, ni `chapters/` ou `glossary/` à la racine n’ont été touchés.
