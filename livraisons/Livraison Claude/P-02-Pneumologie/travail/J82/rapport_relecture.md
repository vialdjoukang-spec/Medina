# J82 — Éosinophilies pulmonaires (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J82 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/J82/chapters/J82/` (6 fichiers), `travail/J82/glossary/j82.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J82/` et `glossary/j82.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé et renforcé le texte. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, et corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Les sources ont été téléchargées indépendamment de l’auteur le 09.10.2026 :
- textes intégraux PMC par `efetch` (db=pmc) : Marchand et Cordier 2006, Agarwal (ISHAM) 2024, Valent 2023, Previtero 2026, Jackson 2022, Carnino 2021, MIRRA 2017 ;
- texte intégral HTML de nature.com : Emmi 2023 (16 énoncés) ;
- résumés PubMed par `efetch` pour les autres articles ;
- AIPS AmiKo par `tools/swissmedic_fi.py` (11 informations professionnelles).

## Réserves de l’auteur tranchées

| Réserve | Décision |
|---|---|
| Dose et durée des glucocorticoïdes dans la PAE (Philit 2002 inaccessible) | Philit est publié dans l’**Am J Respir Crit Care Med** (et non dans Medicine). Texte intégral refusé (atsjournals 403 ; Europe PMC : abonnement requis). **Durée sourcée** par Rhee et al., Eur Respir J 2013 (PMID 22599359), série de 137 PAE : 2 semaines aussi efficaces que 4, même en insuffisance respiratoire. Nouvelle fenêtre `j82-pae-duree`, avec ses limites (non randomisé, population coréenne). Texte intégral ERJ inaccessible (Cloudflare) : la **dose initiale reste une lacune nommée**. La revue européenne de Faverio 2018 (PMC5952859) a aussi été lue : elle ne donne pas de dose. |
| Ivermectine sans information suisse | Recherche `ivermectin`, `ivermectine`, `Stromectol` dans AmiKo le 09.10.2026 : aucune entrée. Dose tirée de Carnino 2021 (HUG et Swiss TPH), vérifiée mot à mot : 200 µg/kg, une dose, 2 à 4 doses si immunosuppression ou exposition récente, traitement empirique en urgence. Lacune maintenue et nommée. |
| Usages hors indication | Confirmés dans les AIPS : Nucala® (GEPA, SHE, asthme, polypose, BPCO ; pas la PCE) ; Fasenra® (asthme, GEPA, SHE) ; Xolair® (asthme allergique, urticaire, polypose) ; Sporanox® (aspergillose seulement en cas d’échec ou d’intolérance du traitement standard, **200 mg par jour**, soit la moitié de la dose ISHAM). Ce dernier écart de dose est désormais affiché dans les tableaux Pharmacologie et la monographie. |
| Cohérence avec M31 injecté | Vérifiée : mépolizumab 300 mg et benralizumab 30 mg toutes les 4 semaines, réservés aux formes récidivantes ou réfractaires sans menace d’organe ; MIRRA et MANDARA ; cyclophosphamide ou rituximab dans les formes sévères. M31 n’emploie pas le sigle GEPA ; aucune contradiction. |
| ISHAM | Défini dans `glossary/j12.py` (cours J12 enregistré) : le cours écrit désormais « groupe de travail ISHAM » dans les critères formels. |
| `tests/audit_sciences.py` | Contrat appliqué au fichier et satisfait. L’ajout de J82 à la liste des nouvelles productions sans base Git reste à faire par l’orchestrateur lors de l’enregistrement. |

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Anti-IL-5 en Suisse | « Autorisés seulement dans la GEPA et le SHE, en dehors de l’asthme » | AIPS Nucala® 12.2025 : aussi polypose nasosinusienne et BPCO | « Parmi les maladies de ce cours » ; indications complètes citées dans la fenêtre Nucala |
| Itraconazole, contre-indication cardiaque | « Insuffisance cardiaque présente ou passée » | AIPS Sporanox® 11.2024 | Signes de dysfonction ventriculaire, dont insuffisance cardiaque **décompensée** présente ou passée |
| Itraconazole et azithromycine | « La prudence s’impose avec l’azithromycine » | Absent de l’AIPS Sporanox® | Retiré ; QT : association « peut être contre-indiquée », risque de torsades de pointes |
| Itraconazole et rifampicine | « Devient indétectable » | AIPS : concentration sous la limite de détection, association non recommandée | Reformulé selon l’AIPS |
| Place de l’itraconazole dans l’ABPA | « En première intention à la place de la prednisolone » | ISHAM 2024 : prednisolone **ou** itraconazole ; itraconazole si glucocorticoïdes contre-indiqués | « Au même titre que la prednisolone » ; ajout de la courte corticothérapie (< 2 semaines) admise avec l’itraconazole |
| Critères ABPA | IgE totales ≥ 500 UI/mL obligatoires | ISHAM 2024, tableau 1, notes c et e | Valeur plus basse acceptable si tous les autres critères sont réunis ; mucus hyperdense suffisant pour confirmer |
| Biothérapie et amphotéricine nébulisée dans l’ABPA aiguë | « Inefficaces » | ISHAM 2024 : non recommandées en première intention ; efficacité faible de l’amphotéricine | « Non recommandés en première intention » |
| Daptomycine | « Récidivant à la réintroduction » | AIPS Cubicin® 11.2022 : arrêt et « toute réexposition devrait être évitée » | Reformulé ; « réintroduction proscrite » → « réexposition évitée » |
| Grossesse et GEPA | « Perte fœtale jusqu’à 20 % des grossesses » | Emmi 2023 : « pregnancy loss … up to 20 % of patients » | « Chez jusqu’à 20 % des patientes » |
| Score à cinq facteurs révisé | Ajouts seuls | Emmi 2023 | Ajout du retrait de l’atteinte du système nerveux central |
| Suivi de la GEPA | « Les éosinophiles peuvent rester bas pendant une rechute » | Emmi 2023, énoncé 15 | « Une rechute peut survenir sans hausse des éosinophiles » |
| Glivec® | « SHE, entre autres hémopathies » | AIPS Glivec® 07.2026 | SHE associé à un réarrangement du récepteur du PDGF ou à FIP1L1-PDGFRA |
| Forme lymphoïde du SHE | « Un clone T surproduit l’IL-5 (Jackson) » | Non trouvé chez Jackson ; Valent 2023 | Lymphocytes T de phénotype aberrant, le plus souvent CD3 négatif et CD4 positif, produisant des cytokines de type 2 |
| Récepteurs de l’éosinophile | Récepteur de l’IL-33 | Non trouvé chez Jackson | Chaîne alpha du récepteur de l’IL-5, récepteurs de motifs microbiens et de lésion, fixation des IgA et IgE |
| Syndrome de Löffler | « Sans signe digestif obligatoire » | Absent de Faridah 2026 | Retiré ; symptômes du résumé (toux, dyspnée, sibilants, hémoptysie) |
| SHE en différentiel | « Absence d’asthme dominant » | Non sourcé | Thrombus muraux et fibrose endocardique (Marchand et Cordier) |
| Vapotage, cigarette électronique | Cause citée | Aucune source lue | Remplacé par « autre exposition inhalée » (De Giacomi 2017) et « reprise récente du tabac » |
| Tabac et PAE | Délai d’« une semaine » dans l’exemple | Rhee 2013 : changement d’habitude 17 jours en médiane avant la maladie | Exemple et fenêtre Tabac alignés |
| ABPA, mécanisme | « Les bouchons muqueux dilatent les bronches » | ISHAM 2024 | La réaction produit bouchons et bronchectasies ; bouchons persistants → bronchectasies irréversibles ; stade avancé défini (bronchectasies étendues avec cœur pulmonaire ou insuffisance hypercapnique chronique) |
| Asthme et ABPA | « Par définition » | ISHAM 2024 : asthme ou mucoviscidose, plus rarement bronchectasies ou BPCO | Corrigé dans la fenêtre Asthme |
| Antifibrosants dans la PCE | « Justification théorique, aucune donnée » | Previtero 2026 | Rarement étudiés ; à envisager en cas de fibrose établie ou progressive selon la revue |
| Infiltrats de la GEPA | Attribués à Cottin 2016 | Emmi 2023 | Attribution corrigée |
| Corticostéroïde inhalé dans la PCE | « Est poursuivi ou débuté chez l’asthmatique » | Marchand et Cordier 2006 : proposé, rôle encore non résolu | Reformulé comme question ouverte |
| IgE totales, seuil 500 contre 1000 | Sans chiffre | ISHAM 2024 | Sensibilité 98 % contre 91 % |

### Sources et plan
- Rhee 2013 (Eur Respir J, PMID 22599359) et Faridah 2026 ajoutés aux références des îlots concernés ; Valent 2023 ajouté en Immunologie ; Philit et Cottin 2025 à l’îlot 5.
- La revue de Philit est identifiée par sa revue réelle (Am J Respir Crit Care Med).
- Aucune recommandation américaine ne fonde une conduite. Les séries Mayo (De Giacomi, Baqir rapportée par Previtero), la série coréenne de Rhee et les essais MIRRA et MANDARA sont cités comme données. ACR/EULAR 2022 est recevable au titre de l’EULAR. Emmi 2023 émane d’un panel d’experts européens.
- Plan monographique conservé ; aucun îlot ni tableau consacré au code CIM.

### Rédaction
Affirmations non sourcées ou excessives reformulées : « l’anamnèse est l’examen le plus rentable », « cinq questions orientent la majorité des diagnostics », « médicaments des six derniers mois », « les premières causes sont les plus fréquentes », « leur rareté explique le retard diagnostique », « ces trois réflexes préviennent la plupart des décès », « le premier geste causal est souvent le plus efficace ». Une phrase agrammaticale de l’Immunologie (« le rituximab, qui déplète…, et répond ») a été réécrite. La clé de l’îlot 5, ambiguë sur les durées, oppose désormais le tempo et la profondeur de l’hypoxémie.

## Corrections de la passe 2
La relecture intégrale du texte corrigé a encore modifié les points suivants :
- « disparaître » → « chuter » pour l’effet des glucocorticoïdes sur les éosinophiles ;
- tomodensitométrie : « peut montrer un verre dépoli invisible à la radiographie » ;
- exemple du patient ventilé : le lavage reconnaît la PAE et évite d’élargir l’antibiothérapie (formule causale non sourcée retirée) ;
- origine des séries de l’îlot 2 précisée (françaises, américaine, coréenne) ;
- Configurations diagnostiques : seule la dernière ligne partage l’imagerie de la PCE ;
- anatomie pathologique : les foyers de pneumopathie organisée « rapprochent » l’histologie, sans causalité affirmée ;
- *Strongyloides* « persiste des décennies » (Carnino) au lieu de « toute la vie » ;
- Pareto « Urgences, traitement et suivi » et monographie des glucocorticoïdes complétés par la durée de deux semaines dans la PAE ;
- une phrase de paramètres clés triplée par l’outil d’édition a été dédoublonnée.

## Sources vérifiées (28 liens, tous contrôlés le 09.10.2026)

**PubMed (19 liens), vérifiés par `esummary` ou `efetch` : premier auteur, année et revue concordants.**
9772920 Marchand 1998 Medicine · 12403693 Philit 2002 Am J Respir Crit Care Med · 12882444 Marchand 2003 Eur Respir J · 14738224 Cottin 2004 Eur Respir J · 15340881 Conen 2004 Swiss Med Wkly · 15932372 Cottin 2005 Allergy · 17495282 Jeong 2007 Radiographics · 20924692 Hoenigl 2010 Wien Klin Wochenschr · 22430939 Rigamonti 2012 Swiss Med Wkly · 22599359 Rhee 2013 Eur Respir J · 23258778 Cordier 2013 Eur Respir J · 27587545 Cottin 2016 Eur Respir J · 28286263 De Giacomi 2017 Chest · 35106968 Grayson 2022 Arthritis Rheumatol · 37055090 Cottin 2023 Immunol Allergy Clin North Am · 38393328 Wechsler (MANDARA) 2024 N Engl J Med · 40313018 Cordaillat 2025 Rev Med Suisse · 41110928 Cottin 2025 Clin Chest Med · 41161022 Faridah 2026 J Infect Public Health. Les pages pubmed.ncbi.nlm.nih.gov répondent 203 ou 429 (limitation de débit du proxy) ; leur contenu a été lu par l’API E-utilities.

Mode de lecture par le relecteur :
- **texte intégral PMC** (HTTP 200) : Marchand et Cordier (PMC1464381), Agarwal (PMC10991853), Valent (PMC9797433), Previtero (PMC13343205), Jackson (PMC9489126), Carnino (PMC8704417), MIRRA (PMC5548295) ;
- **texte intégral nature.com** (HTTP 200) : Emmi 2023 ;
- **résumé** : les autres.

**AIPS via AmiKo (date de mise à jour lue dans le texte)** : Nucala® (12.2025) ; Fasenra® (03.2026) ; Sporanox® (11.2024) ; Zentel® (10.2025) ; Vermox® 100 mg (07.2025) ; Prednisone Streuli® (06.2026) ; Spiricort® (06.2026) ; Solu-Medrol® (08.2025) ; Glivec® (07.2026) ; Cubicin® (11.2022) ; Dupixent® (01.2025) ; Xolair® (03.2025). Le lien générique swissmedicinfo.ch répond 200.

Doses et mises en garde vérifiées mot à mot dans l’AIPS :
- **mépolizumab** : 300 mg toutes les 4 semaines (GEPA dès 18 ans, SHE dès 12 ans) ; aucune étude de détermination de dose propre à la GEPA ; non étudié dans les atteintes menaçant un organe ou la vie ; helminthiase traitée avant la première dose ; surveillance de 30 minutes ; pas d’arrêt abrupt des corticostéroïdes ; grossesse seulement en cas de nécessité absolue ; baisse des éosinophiles de 83 % dans la GEPA ;
- **benralizumab** : 30 mg toutes les 4 semaines (GEPA, SHE) ; asthme : 3 doses toutes les 4 semaines puis toutes les 8 semaines ; liaison aux cellules NK par absence de fucose ; céphalées chez 17 % dans la GEPA ; passage placentaire accru aux deuxième et troisième trimestres ;
- **itraconazole** : aspergillose en cas d’intolérance ou d’échec du traitement standard, 200 mg par jour ; prise après un repas complet ; Cushing ou insuffisance surrénale avec fluticasone ou budésonide ; inotrope négatif ; hépatotoxicité ; perte auditive ; grossesse contre-indiquée sauf menace vitale ;
- **albendazole** : ascaridiose 400 mg en une prise ; strongyloïdose 400 mg par jour pendant 3 jours, posologie inadaptée à l’immunodéprimé avec atteinte viscérale ; inhibition supposée de la polymérisation de la tubuline ; action sur parasites intestinaux et tissulaires ; grossesse ;
- **mébendazole** : 100 mg matin et soir pendant 3 jours (ascaris, strongyloïdes) ; grossesse ;
- **méthylprednisolone** : perfusion d’au moins 30 minutes au-delà de 250 mg ; arythmies et arrêt cardiaque après plus de 0,5 g en moins de 10 minutes ; pneumopathie à éosinophiles (syndrome de Loeffler) non contrôlée par d’autres traitements parmi les indications ; grande prudence en cas de strongyloïdose ; vaccins vivants contre-indiqués sous doses immunosuppressives ;
- **prednisone** : 5 à 60 mg par jour ; arrêt par paliers au-delà de 8 à 10 jours ; insuffisance surrénale possible après 2 semaines ;
- **imatinib** : SHE 100 mg par jour, jusqu’à 400 mg ; interruption sous 1,0 G/L neutrophiles ou 50 G/L plaquettes ; chocs cardiogéniques au début dans le SHE cardiaque ; troponine et échocardiographie, glucocorticoïde 1 à 2 mg/kg pendant 1 à 2 semaines si anormales ;
- **daptomycine** : pneumopathie à éosinophiles 2 à 4 semaines après le début ; lavage, arrêt, corticothérapie, réexposition évitée ;
- **dupilumab** : pneumonies à éosinophiles et vascularites de GEPA, parfois lors de la réduction de la corticothérapie orale ; hyperéosinophilie systémique grave ;
- **omalizumab** : GEPA ou SHE rares chez l’asthmatique allergique sévère.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 48 `data-k` = 48 gabarits (42 fenêtres et 6 Pareto) ; aucun gabarit dupliqué ni orphelin ; préfixes `j82-` et `pareto-j82-` ; aucun identifiant dupliqué ; ancres du sommaire et couvertures Pareto valides |
| Classes | toutes dans la liste fermée de `CHAPTER_SPEC.md` |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; fenêtres bien formées |
| Glossaire | `glossary/j82.py` : PCE, PAE, GEPA, SHE, HTLV-1, en ajout conditionnel (`_a`). Aucune collision avec `glossary/*.py`, y compris `j67.py` et `r04.py` injectés en parallèle (contrôle final). ISHAM provient de `j12.py` |
| `build_medina.py J82` (copie superposée, J82 enregistré temporairement) | `J82 non couvertes: 0` ; Pareto : clinique 5 %, diagnostic 11 %, urgences-traitement-suivi 7 %, critères 16 %, examens 5 %, pharmacologie 4 % |
| Contrat Sciences (logique de `tests/audit_sciences.py`) | navigation complète ; 4 disciplines de 352 à 425 mots, une figure légendée et accessible chacune, les quatre liens présents |
| `build_front.py --fragment S02` (copie superposée) | construit : 5,89 Mo, compressé à 2,86 Mo |
| Chromium 1194, `#/entry/J82` | titre correct ; 4 onglets non vides ; 48 mots verts et boutons Pareto ouverts, tous avec contenu, aucune « Fiche absente » ; aucune erreur JavaScript ni de console ; bureau 1440 px et mobile 390 px sans défilement horizontal de page ; fenêtres contenues dans 390 px |
| `tools/capture_lecon.py` | `captures/j82-1-ouverture.png`, `captures/j82-2-explication.png` (statut : relu, injecté, non enregistré dans `chapters.json`) |

Le texte compte 14 709 mots hors références et SVG, contre 14 024 dans le brouillon. La hausse vient de la fenêtre nouvelle sur la durée de la corticothérapie de la PAE et des nuances de source.

## Réserves restantes (non bloquantes)

1. **Dose initiale des glucocorticoïdes dans la PAE** : non fixée par les sources lues ; Philit 2002 et Rhee 2013 inaccessibles en texte intégral. Lacune nommée dans l’îlot 9 et la fenêtre `j82-pae-duree`.
2. **Ivermectine** : aucune information professionnelle suisse dans AmiKo ; contre-indications et interactions non citables d’après un texte suisse.
3. **Usages hors indication** signalés dans le cours : anti-IL-5 dans la PCE (séries de cas), omalizumab dans l’ABPA, itraconazole dans l’ABPA (indication restreinte et dose double de l’AIPS), prednisone dans la PCE (indication non nommée).
4. **Données suisses d’épidémiologie absentes** pour PCE, PAE et syndrome de Löffler (lacune nommée).
5. **Lectures limitées au résumé** pour Philit, Marchand 1998 et 2003, De Giacomi, Rhee, Cottin 2004, 2005, 2016, 2023 et 2025, Cordier 2013, Jeong, Hoenigl, Faridah, Cordaillat, Conen, Rigamonti, Grayson et MANDARA ; chaque chiffre repris figure dans ces résumés.
6. **ISHAM 2024** est un consensus international (Delphi, près de la moitié des experts indiens) publié dans l’Eur Respir J ; il reste retenu faute de texte suisse ou européen plus récent. Le PNDS français OrphaLung n’a pas été exploité.
7. **Notions générales encore formulées sans citation mot à mot** : la lecture chronologique des examens (« le lavage prend la première place après une corticothérapie ») et l’exemple de l’interaction itraconazole-fluticasone découlent des sources citées mais n’y figurent pas textuellement.
8. `tests/audit_sciences.py` échouera pour J82 tant que le code n’est pas ajouté à la liste des nouvelles productions sans base Git ; `chapters.json` et `organisation/*` n’ont pas été modifiés : l’enregistrement revient à l’orchestrateur.

## Injection

- `chapters/J82/` : `J82_a.html`, `J82_b.html`, `J82_c.html`, `J82_d.html`, `J82_pop1.html`, `J82_pop2.html`.
- `glossary/j82.py` : glossaire de l’auteur, rendu conditionnel.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J82/captures/` : deux captures et `captures.json`.
- Entrée `chapters.json` proposée : `{"code": "J82", "covers": ["J82"], "title": "Éosinophilies pulmonaires", "integrated": true}`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
