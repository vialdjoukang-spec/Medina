# I27 — Hypertension pulmonaire et autres maladies des vaisseaux pulmonaires (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant I27 et I28 (CIM-10-GM 2024 ; codes dans l’en-tête seulement).
Sources relues : `travail/I27/chapters/I27/` (6 fichiers) et `travail/I27/glossary/i27.py`. Aucun `rapport_auteur.md` n’était présent. Le brouillon de l’auteur est conservé intact dans ce dossier ; la version relue est injectée dans `chapters/I27/` et `glossary/i27.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.** Les tests techniques non plus.

## Règles appliquées

`LEADERSHIP_CLAUDE_2026-10-08.md` (sections 7 à 13 : efficacité, français, règle fondamentale de la section 11, double audit en quatre dimensions de la section 13), `CHAPTER_SPEC.md`, `PROMPT_MEDINA.md` § 10, `docs/STYLE_REDACTION.md`, `CONSIGNES_INTERACTION_DENSITE_SOURCES.md`. Modèle suivi : J84 injecté.

## Accès aux sources primaires

| Source | Accès obtenu | Usage |
|---|---|---|
| ESC/ERS 2022 (Humbert, Eur Heart J 2022 ; version ERJ 2023;61:2200879) | **Texte intégral** (PDF de l’éditeur, 145 pages, dépôt institutionnel de l’Université de Copenhague, curis.ku.dk) ; les sites ESC/ERS/OUP renvoient 403 | Toutes les définitions, tableaux 5, 8, 10, 11, 12, 14, 16, 17, 18, 19, 20 et tableaux de recommandations 3, 5, 6, 7, 8A, 12, 13, 22A/B, 23A/B, 24A ; sections 5, 6, 7.7, 10 |
| 7e Symposium mondial 2024, Eur Respir J 64(4) | **Texte intégral** Europe PMC : Kovacs (PMC11533989), Chin (PMC11525349), Dardi (PMC11525341), Preston (PMC11525332), Kim (PMC11525345), Shlobin (PMC11525344), Savale (PMC11525343), Austin (PMC11525347), Guignabert (PMC11533988), Hemnes (PMC11525331) | Mise à jour 2024 et arbitrages |
| COMPERA 2.0 (Hoeper 2022, PMC9260123), DETECT (Coghlan 2014, PMC4078756), Schneider 2024 (PMC10821358), BTS voyage aérien 2022 (PMC8938676), Gupta 2020 (PMC7052473, BioC) | Texte intégral | Strates de risque, dépistage, altitude, vol, anévrisme |
| Essais (STELLAR, ZENITH, Hyperion, AMBITION, SERAPHIN, GRIPHON, CHEST-1, PATENT-1), registre suisse, Coquoz, Kovacs 2009, Hoeper 2006, BTS 2017 (fistules), Faughnan 2011/2020, Harjola 2016 | Résumés PubMed (efetch) | Chiffres d’essais ; HR 0,16 de STELLAR lu dans Chin 2024 |
| Informations professionnelles suisses (AIPS via AmiKo, `tools/swissmedic_fi.py`, texte intégral) | Tracleer® (06.2025), Volibris® (09.2025), Opsumit® (01.2026), Revatio® (02.2026), Adcirca® (08.2023), Adempas® (07.2025), Uptravi® (02.2023), Veletri® (07.2025), Remodulin® (02.2026), Ventavis® (07.2020), Winrevair® (02.2026) ; Norvasc®, Dilzem®, nifédipine (indications seulement) | Doses, contre-indications, interactions, surveillance |
| Swissmedic, page d’autorisation de Winrevair | HTTP 200, lue | Autorisation 13.09.2024 ; SwissPAR d’extension publié le 02.04.2026 |

## Passe 1 — constats et corrections

### Dimension 2 : exactitude médicale et doses

Le brouillon s’est révélé largement fidèle à l’ESC/ERS 2022, vérifiée phrase par phrase en texte intégral (épidémiologie 1 %, 6 et 48–55 par million, 50–60 % idiopathiques ; > 2 ans de délai ; tableaux 16, 18, 19 ; recommandations). Corrections :

1. **Macitentan** : « contraception poursuivie au moins un mois après l’arrêt » introuvable dans l’AIPS Opsumit® : retiré. Test de grossesse mensuel désormais attribué au bosentan **et** au macitentan (AIPS).
2. **Sotatercept** : règles de report complétées selon l’AIPS (quatre critères, dont Hb > 2 g/dL au-dessus de la limite supérieure ; pas d’initiation si plaquettes < 50 × 10⁹/L ; reprise à 0,3 mg/kg après > 9 semaines) ; « contre-indiqué pendant la grossesse » corrigé en « non recommandé » (AIPS) ; date non vérifiée « classe IV depuis le 05.02.2026 » remplacée par l’extension attestée (FI février 2026, SwissPAR 02.04.2026) ; effets indésirables chiffrés (AIPS, Chin).
3. **Inhibiteurs calciques** : réévaluation « 3 à 6 mois » alignée sur la recommandation de classe I (3 à 4 mois) ; critères de bonne réponse (classe I–II, PAPm < 30, RVP < 4) ; absence d’indication suisse vérifiée (AIPS Norvasc®, Dilzem®, nifédipine) ; « dépriment le ventricule droit » remplacé par les effets cités par l’ESC (hypotension sévère, syncope, défaillance droite).
4. **Valeurs normales** : PAPO « 6 à 12 mmHg » (non sourcé) → ≤ 15 mmHg, limite supérieure 13 mmHg (7e Symposium) ; RVP « environ 1 » → 0,3–2,0 unités Wood (ESC tableau 11) ; débit « 5 L/min », « 20 L/min à l’effort », « PAM 90 mmHg » remplacés par 4–8 L/min (ESC) et 14 ± 3 mmHg (Kovacs 2009).
5. **Vasoréactivité** : répondeurs « < 10 % » (ESC) complétés par 12 % (idiopathique, médicamenteuse) et < 5 % (héritable) selon le 7e Symposium ; seuil ≤ 40 (ESC) / < 40 mmHg (7e Symposium) présenté avec arbitrage ; « jamais avec un inhibiteur calcique » (non sourcé) remplacé par « adénosine non recommandée » (ESC).
6. **Biologie** : anti-topo-isomérase I et anti-RNP (non retrouvés) remplacés par anti-Ro, acide urique, TSH et dépistage urinaire des stupéfiants (ESC 5.1.9, Kovacs).
7. **ECG** : signes réalignés sur le tableau 8 de l’ESC (P > 0,25 mV en II, axe > 90°, R/S > 1 avec R > 0,5 mV en V1, R V1 + S V5 > 1 mV, BBD, surcharge, QTc) ; arythmies auriculaires 3–25 % en 5 ans.
8. **Imagerie** : « TDM ≥ 30 mm ou plus large que l’aorte » → rapport AP/aorte > 0,9 et triade prédictive (ESC 5.1.7) ; scintigraphie VPN 98 %, angioscanner Se 76 % / Sp 96 %, défauts non appariés dans 7–10 % des maladies veino-occlusives et HTAP (au lieu de « plus sensible », non chiffré).
9. **Tableau des groupes (examens)** : DLCO des groupes 2, 3 et 4 corrigées selon le tableau 14 de l’ESC.
10. **Défaillance droite** : enrichie et sourcée (ESC 6.3.7, Savale 2024) : bilan hydrique négatif, dobutamine 2,5 puis ≤ 5–7,5 µg/kg/min, noradrénaline ou vasopressine, éviter l’intubation, ECMO veino-artérielle sous anesthésie locale ; « confusion » (non sourcée) retirée ; arythmie : éviter bêtabloquants et inhibiteurs calciques (Savale). **Nouvelle fenêtre d’arbitrage** `i27-pam-cible` : PAM > 60 mmHg (ESC 2022, texte en vigueur) contre 70–75 mmHg (7e Symposium, plus récent, sans étude dédiée).
11. **Groupe 3** : « les vasodilatateurs aggravent l’hypoxémie » nuancé (risque théorique, rare dans les essais selon Chin et Shlobin) ; préjudices démontrés nommés (ARTEMIS, RISE-IIP, PERFECT) ; INCREASE ; tréprostinil inhalé signalé **non autorisé en Suisse** (aucune entrée AIPS au 09.10.2026).
12. **HTP-TEC** : AOD « utilisés dans les autres cas » nuancé (récidives plus fréquentes que sous AVK dans plusieurs études, Kim 2024) ; SAPL ≈ 10 % ; endartériectomie (normalisation 70–75 %, mortalité ≈ 2 %) et angioplastie (lésion pulmonaire ≈ 10 % des séances) chiffrées ; définition alignée sur le texte ESC.
13. **Grossesse, altitude, chirurgie** : mortalité maternelle 11–25 % ; ESC (déconseiller, décision partagée si maladie contrôlée) ; conduite pendant la grossesse (Preston 2024) ; **données suisses ajoutées** : essais zurichois à 2500 m (journée : −11 % de capacité d’effort, SpO₂ 83 % ; nuit : 14/27 événements, surtout hypoxémie nocturne corrigée par l’oxygène) ; BTS 2022 pour le vol ; mortalité périopératoire 2 % / 15 % (ESC).
14. **Fistules et anévrismes** : affirmations limitées à ce que disent les sources lues (BTS 2017 : > 1 patient sur 4 avec AVC paradoxal, abcès ou infarctus ; hémorragie ≈ 1 grossesse sur 100 ; Faughnan : prévalence ≥ 1/5000) ; échographie de contraste, antibioprophylaxie et filtres (non lus) retirés ; anévrismes et compressions sourcés (ESC 6.3.10.3, Gupta 2020) ; obstructions non thrombotiques rattachées au groupe 4 (Kovacs).
15. **Divers** : bendopnée et souffle de Graham Steell ajoutés (Kovacs) ; manœuvre de Carvallo, épaisseur du ventricule droit (3–5 mm), tailles artérielles (500/100 µm), canaux potassiques de la vasoconstriction hypoxique, « 30 m de couloir », « 3 cm au-dessus de l’angle sternal », mécanisme sérotonine/kinases des toxiques, AINS « rétention sodée » : retirés faute de source lue ; carence martiale définie (ESC 6.3.1.6) ; transplantation alignée sur le tableau 20 ; dasatinib/interféron réversibles, méthamphétamines non (Chin).
16. **Cas récapitulatif** : la syncope survenue lors d’un effort intense est un critère **intermédiaire** (note a du tableau 16) ; le risque élevé est désormais justifié par la marche < 165 m, le NT-proBNP > 1100 ng/L et les signes de défaillance droite ; débit ajouté pour rendre le calcul des RVP vérifiable.

### Dimension 3 : sources et liens

- 16 liens dans le brouillon, tous vérifiés ; **1 lien cassé** (forschung.kssg.ch, HTTP 468) remplacé par PubMed 25661477 ; 3 liens doi.org (Chin) remplacés par PubMed 39209476 (doi vérifié par Crossref mais doi.org renvoie 403 aux robots).
- 35 liens dans la version finale (liste ci-dessous) ; chaque fenêtre et chaque îlot porteur de données a désormais sa référence.
- Aucune recommandation américaine ne fonde une conduite. Hoeper 2006 (J Am Coll Cardiol) est une étude multicentrique européenne citée comme donnée ; Gupta 2020 est une revue citée comme donnée.

### Dimension 1 : rédaction

- Faux mot « vasoconstricte » corrigé ; métaphores légères retirées (« conçu pour », « taillé pour », « le tableau connaît un raccourci », « stratège ») ; mots verts isolés en phrases nominales convertis en phrases complètes (une dizaine) ; « À retenir » nominaux ou à l’infinitif réécrits ; lien vers un autre fragment (`#/entry/I26`) remplacé par un renvoi textuel (séparation des spécialités).
- Aucune phrase de fabrication. Le code CIM reste confiné à l’en-tête.

## Passe 2 — relecture intégrale du résultat de la passe 1

Relecture complète des quatre onglets, des 64 fenêtres, des 3 quiz, des 5 Pareto et du glossaire. Corrections :

1. Formulations nominales résiduelles (alerte de l’îlot 8, îlot 9, îlots 12, 13, 15, onglet Examens, alerte de pharmacologie, fenêtre des voies) réécrites en phrases complètes.
2. « ESC/ERS 2022, recommandations 8 et 9 / 22 à 24 » remplacés par les numéros réels des tableaux de recommandations.
3. Cohérence : riociguat « sensibilise au monoxyde d’azote » (non lu) → « en présence comme en l’absence de NO endogène » (ESC 6.3.3.3.3) ; CYP2C8 « active et élimine le sélexipag » (non lu) → « gemfibrozil × 11 sur le métabolite actif » (AIPS Uptravi®), aussi dans le glossaire ; demi-vie de l’époprosténol 3–5 min ; dyspepsie et rares pertes de vision ou d’audition des IPDE5 (Chin).
4. Pièges du NT-proBNP (âge, rein, obésité : non retrouvés) remplacés par la formulation de l’ESC (non spécifique, variabilité).
5. Hémoptysie : terrains corrigés (HTAP héritable et cardiopathies congénitales, ESC) ; angor : compression du tronc commun traitée par endoprothèse (ESC).
6. Hypertension portopulmonaire : « surveiller le foie » remplacé par les contre-indications hépatiques exactes des trois antagonistes de l’endothéline (AIPS).
7. Pareto enrichis (HTP-TEC, défaillance droite, doses suisses) ; Pareto pharmacologique corrigé (sotatercept et sélexipag « évités », non « tératogènes »).
8. Glossaire : expansions inventées de CHEST-1 et PATENT-1 retirées (« nom d’essai, non développable ») ; COMPERA, DETECT, ARTEMIS, RISE-IIP, INCREASE, PERFECT, SwissPAR et AmiKo ajoutés ; TBX4 redéfini selon le 7e Symposium. « Hyperion » est écrit en casse mixte pour ne pas déclencher la clé `HYPERION` de `i46.py` (autre essai).
9. Titre h1 aligné sur l’intitulé complet de la leçon.

## Sources vérifiées (URL et preuve)

Vérification PubMed par `esummary` (premier auteur, année, revue, volume, pages concordants avec la citation) le 09.10.2026 :

| Lien | Preuve |
|---|---|
| https://pubmed.ncbi.nlm.nih.gov/36017548/ | Humbert M, 2022, Eur Heart J 43:3618-3731 — ESC/ERS 2022 |
| https://pubmed.ncbi.nlm.nih.gov/39209475/ | Kovacs G, 2024, Eur Respir J 64 — définition, classification, diagnostic |
| https://pubmed.ncbi.nlm.nih.gov/39209476/ | Chin KM, 2024, Eur Respir J 64 — algorithme thérapeutique (Crossref : 10.1183/13993003.01325-2024) |
| https://pubmed.ncbi.nlm.nih.gov/39209472/ | Dardi F, 2024 — stratification du risque |
| https://pubmed.ncbi.nlm.nih.gov/39209477/ | Preston IR, 2024 — situations particulières |
| https://pubmed.ncbi.nlm.nih.gov/39209473/ | Kim NH, 2024 — maladie thromboembolique chronique |
| https://pubmed.ncbi.nlm.nih.gov/39209469/ | Shlobin OA, 2024 — HTP des maladies respiratoires |
| https://pubmed.ncbi.nlm.nih.gov/39209471/ | Savale L, 2024 — transplantation et assistance |
| https://pubmed.ncbi.nlm.nih.gov/39209474/ | Guignabert C, 2024 — anatomopathologie |
| https://pubmed.ncbi.nlm.nih.gov/39209481/ | Austin ED, 2024 — génétique |
| https://pubmed.ncbi.nlm.nih.gov/39209482/ | Hemnes AR, 2024 — ventricule droit |
| https://pubmed.ncbi.nlm.nih.gov/34737226/ | Hoeper MM, 2022, Eur Respir J 60 — COMPERA 2.0 |
| https://pubmed.ncbi.nlm.nih.gov/19324955/ | Kovacs G, 2009, Eur Respir J 34:888-94 — PAPm 14,0 ± 3,3 mmHg |
| https://pubmed.ncbi.nlm.nih.gov/17174196/ | Hoeper MM, 2006, J Am Coll Cardiol 48:2546-52 — 1,1 % et 0,055 % |
| https://pubmed.ncbi.nlm.nih.gov/23687283/ | Coghlan JG, 2014, Ann Rheum Dis 73:1340-9 — DETECT |
| https://pubmed.ncbi.nlm.nih.gov/25661477/ | Mueller-Mottet S, 2015, Respiration 89:127-40 — registre suisse |
| https://pubmed.ncbi.nlm.nih.gov/29563171/ | Coquoz N, 2018, Eur Respir J 51 — 11 centres suisses, 0,79 % |
| https://pubmed.ncbi.nlm.nih.gov/38079468/ | Schneider SR, 2024, Eur Heart J 45:309-311 — nuit à 2500 m |
| https://pubmed.ncbi.nlm.nih.gov/38423623/ | Müller J, 2024, Eur Respir J 63 — effort à 2500 m |
| https://pubmed.ncbi.nlm.nih.gov/35228307/ | Coker RK, 2022, Thorax 77:329-350 — BTS voyage aérien |
| https://pubmed.ncbi.nlm.nih.gov/29141890/ | Shovlin CL, 2017, Thorax 72:1154-1163 — BTS fistules |
| https://pubmed.ncbi.nlm.nih.gov/19553198/ | Faughnan ME, 2011, J Med Genet 48:73-87 |
| https://pubmed.ncbi.nlm.nih.gov/32894695/ | Faughnan ME, 2020, Ann Intern Med 173:989-1001 |
| https://pubmed.ncbi.nlm.nih.gov/32166017/ | Gupta M, 2020, Pulm Circ 10 — anévrisme |
| https://pubmed.ncbi.nlm.nih.gov/26995592/ | Harjola VP, 2016, Eur J Heart Fail 18:226-41 — HFA/ESC |
| https://pubmed.ncbi.nlm.nih.gov/36877098/ | Hoeper MM, 2023, N Engl J Med 388:1478-1490 — STELLAR |
| https://pubmed.ncbi.nlm.nih.gov/40167274/ | Humbert M, 2025, N Engl J Med 392:1987-2000 — ZENITH |
| https://pubmed.ncbi.nlm.nih.gov/41025556/ | McLaughlin VV, 2025, N Engl J Med 393:1599-1611 — Hyperion |
| https://pubmed.ncbi.nlm.nih.gov/26308684/ | Galiè N, 2015, N Engl J Med 373:834-44 — AMBITION |
| https://pubmed.ncbi.nlm.nih.gov/23984728/ | Pulido T, 2013, N Engl J Med 369:809-18 — SERAPHIN |
| https://pubmed.ncbi.nlm.nih.gov/26699168/ | Sitbon O, 2015, N Engl J Med 373:2522-33 — GRIPHON |
| https://pubmed.ncbi.nlm.nih.gov/23883377/ | Ghofrani HA, 2013, N Engl J Med 369:319-29 — CHEST-1 |
| https://pubmed.ncbi.nlm.nih.gov/23883378/ | Ghofrani HA, 2013, N Engl J Med 369:330-40 — PATENT-1 |
| https://www.swissmedic.ch/swissmedic/de/home/humanarzneimittel/authorisations/new-medicines/winrevair-pulver-sotaterceptum.html | HTTP 200 ; « Zulassungsdatum: 13.09.2024 » lu |
| https://swissmedic.ch/dam/swissmedic/en/dokumente/zulassung/swisspar/69129-winrevair-01-swisspar-20241105.pdf.download.pdf/SwissPAR%20Winrevair.pdf | HTTP 200 (application/pdf, 1,5 Mo) |

## Réserves restantes (non bloquantes)

1. **Signes physiques** : la figure 3 de l’ESC/ERS 2022 (signes cliniques) est une image non lisible en texte ; l’impulsion parasternale, le reflux hépatojugulaire, la technique jugulaire et le tableau « signe → groupe » restent des notions cliniques classiques, sourcées seulement indirectement (Kovacs 2024, ESC 5.1.1 et 7.7.1).
2. **Mécanismes de manuel** : loi de Poiseuille (r⁴), dépendance de la perfusion coronaire droite à la pression aortique (énoncée par Savale 2024), conversion 1 unité Wood = 80 dyn·s·cm⁻⁵, recrutement capillaire à l’effort : formulations générales non rattachées à une phrase précise d’une source lue.
3. BTS 2017 (fistules), Faughnan 2011/2020, Harjola 2016 et les essais NEJM : **résumés** seulement (textes intégraux inaccessibles, 403).
4. Aucune recommandation suisse spécifique (Société suisse de pneumologie, groupe suisse d’hypertension pulmonaire) n’a été identifiée : lacune nommée ; les données suisses proviennent du registre national, de Coquoz 2018 et des essais zurichois.
5. Sotatercept en classe IV : la date exacte de l’extension n’a pas été lue ; seules la FI (février 2026) et la publication du SwissPAR (02.04.2026) sont attestées.
6. Tréprostinil inhalé : absent de l’AIPS au 09.10.2026 (« non autorisé en Suisse » repose sur cette absence de résultat).
7. Seuil de vasoréactivité ≤ 40 (ESC 2022) contre < 40 mmHg (7e Symposium) : divergence affichée, sans conséquence pratique notable.
8. Contrôle `tests/audit_sciences.py` : I27 n’a pas de version de base ni d’exemption ; le contrat a été vérifié avec les fonctions du script (anatomie 354 mots, histologie 297, physiologie 324, biologie moléculaire 359 ; une figure accessible et les quatre liens « Science → » / « À retenir » chacune). L’orchestrateur devra ajouter I27 à l’exemption s’il exécute ce script (fichier hors de mon périmètre).
9. Volume : 12 711 → 16 016 mots (6 fichiers). La hausse vient surtout des références ajoutées à chaque fenêtre et des données vérifiées nouvelles (altitude suisse, arbitrages, AIPS) ; aucune répétition n’a été ajoutée.
10. Les captures et le test navigateur ont été produits sur une construction locale du fragment S02 dans le bloc-notes, avec une copie temporaire de `chapters.json` et de `course_groups.json` hors dépôt ; le rendu réel attend l’enregistrement par l’orchestrateur.

## Contrôles

| Contrôle | Résultat |
|---|---|
| Audit des sigles (`build_medina.build` sur I27 seul, glossaire complet) | `I27 non couvertes: 0` |
| Glossaire `i27.py` | 28 clés ; aucune collision avec les autres `glossary/*.py` ; aucun doublon ; toutes les fenêtres de renvoi existent |
| Contrat HTML | 64 `data-k`, 64 gabarits, aucun orphelin dans un sens ou l’autre ; clés et identifiants tous préfixés `i27` ; aucun identifiant dupliqué ; classes toutes dans la liste fermée ; balises équilibrées ; ancres internes valides ; Pareto : îlots couverts existants (fractions 3 à 5 %) |
| Liens | 35 liens externes, tous `target="_blank" rel="noopener"`, tous vérifiés (tableau ci-dessus) |
| `python3 -m unittest discover -s tests -p 'test_*.py'` (après injection) | 237 tests, OK |
| `build_front.py --fragment S02` (racine temporaire) | Fragment construit, 4 644 892 octets |
| Chromium (playwright), ordinateur 1440 px et mobile 390 px | 4 onglets non vides ; 67 mots verts cliqués par format (4 disciplines comprises), 67 fenêtres ouvertes avec contenu ; 3 quiz, rétroaction visible ; aucun débordement horizontal ; aucune erreur JavaScript ni de console |
| `tools/capture_lecon.py … I27` | `I27 : 2 captures` — `captures/i27-1-ouverture.png`, `captures/i27-2-explication.png` (plus `captures/i27-mobile.png`), dans ce dossier |

## Injection

- `chapters/I27/` : 6 fichiers relus. `glossary/i27.py` : glossaire de l’auteur corrigé et complété.
- **Non modifiés** : `chapters.json`, `organisation/*`, tests, autres cours. Entrée proposée pour l’orchestrateur : `{"code": "I27", "covers": ["I27", "I28"], "title": "Hypertension pulmonaire et autres maladies des vaisseaux pulmonaires", "integrated": true}` ; dans `organisation/course_groups.json`, `owner` « S02 ».
- Aucune opération Git.

Empreintes SHA-256 des fichiers injectés :

```
0d228b95b59c55ccf22e0eacb07351fab0c66662b1bc84a51fc453035749dd3d  chapters/I27/I27_a.html
454ae2fc662fd32064fe8c4246be53194bac1049aa43824dc755749b316886b0  chapters/I27/I27_b.html
5635a06e25a7a311c1e06830b603855c149e54a86c2b7a8ff9c21feb84ad7cf8  chapters/I27/I27_c.html
b67698c0549cedb05c27a5c30d74f54239e56e503631d7d66d792638675df67c  chapters/I27/I27_d.html
476da1539a779e88b217f3d48614d210c05335356bc244da0d16032412f60631  chapters/I27/I27_pop1.html
f565fba0c1570c87535a243de721eb1d390769f0097b96d3a9c4f384fb0a56a2  chapters/I27/I27_pop2.html
dfa7df252cbe3f5e5e9e2ea0413c025858e489816cc84ffb22327818240b6963  glossary/i27.py
```

Statut : injecté après deux passes sans réserve bloquante. Revue IA, non validation médicale.
