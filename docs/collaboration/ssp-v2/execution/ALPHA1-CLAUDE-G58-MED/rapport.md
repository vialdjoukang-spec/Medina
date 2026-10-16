# Audit médical Alpha, tour 1 — G58 Autres mononévrites (S08, N-05-Neurologie)

Mission `ALPHA1-CLAUDE-G58-MED` · branche `claude/alpha1/g58-med-g1` · base `32416a20` · génération 1 · effort conforme au manifeste · 16 octobre 2026.

Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Lecture

Les sept fichiers de la leçon ont été lus en entier (onglets, tableaux, figures, quiz, fenêtres, Pareto, `div.alert`, `div.key`, glossaire). Leurs empreintes SHA-256 sont **identiques au manifeste** (7/7). `test_v7.py --static G58` affiche OK ; `tests/audit_sciences.py` échoue (19 erreurs). Première source lue : information professionnelle suisse Lyrica® (AmiKo, juillet 2026), rubriques Indications et Posologie, tableau rénal.

## Synthèse

| Bloquant | Majeur | Mineur | Enrichissement |
|---|---|---|---|
| 0 | 6 | 9 | 3 |

Le fond médical vérifié est solide : les critères de la Peripheral Nerve Society, le résumé EULAR 2022, les données de Blaes, Ruffer, Koike et Shamoun, ainsi que les doses suisses de la prégabaline, de la gabapentine, du cyclophosphamide et de la prednisone sont fidèles aux sources. Aucune erreur dangereuse n’a été démontrée. Les faiblesses sont structurelles (sémiologie absente, quatre disciplines au lieu de cinq, contrôle des sciences en échec) et pharmacologiques (emplois hors indication non signalés, précautions d’immunosuppression et mises en garde de la gabapentine absentes).

## Constats majeurs

**C01 — `chapters/G58/G58_c.html`.** Sémiologie fondamentale et analytique absente : aucun bouton data-s="g58-s-semio", aucun div.sci homonyme, aucune formule « Pour la leçon : quelle est la sémiologie fondamentale et analytique ? ». Les îlots g58-5 et g58-6 listent symptômes et signes sans mécanisme par signe, sans technique (cotation de la force, cartographie sensitive), sans normal, sans tableau de syndromes, sans raisonnement en cinq étapes ni cas consacrés au signe. Le signe de Carnett, critère publié de l’ACNES, manque.  
*Proposition :* Insérer propositions/G58_c_1.html (bouton en tête de barre et div.sci g58-s-semio, sept îlots g58-sm-1 à -7, une figure non anatomique, trois cas) et créer chapters/G58/G58_pop3.html depuis propositions/G58_pop3_1.html.  
*Preuves :* S1 (Présentation et examen clinique) ; S2 (Introduction, Motor testing) ; S3 (Methods)

**C02 — `chapters/G58/G58_c.html`.** L’onglet Sciences ne compte que quatre disciplines réelles (data-s : g58-s-anat, g58-s-histo, g58-s-physio, g58-s-bioch) ; l’addendum du lot 2 en exige cinq, plus la sémiologie. Les mécanismes immunitaires visés par le rituximab, l’avacopan et le mépolizumab ne sont expliqués nulle part.  
*Proposition :* Ajouter la discipline « Immunologie » de propositions/G58_c_2.html (bouton après Biochimie, div.sci g58-s-immuno, figure 7 non anatomique, quatre libellés, fenêtre Pareto).  
*Preuves :* S17 (Mécanisme d’action) ; S19 (Mécanisme d’action) ; S18 (Mécanisme d’action)

**C03 — `chapters/G58/G58_c.html`.** tests/audit_sciences.py échoue (19 erreurs, base 32416a20) : histologie 236 mots, physiologie 219, biochimie 235 (minimum 280) ; dans les quatre disciplines, les libellés « Science → clinique. », « Science → examen. », « Science → traitement. » et « À retenir. » manquent (remplacés par « Anatomie → clinique. » etc.) et les encadrés contiennent des phrases nominales (« Perte axonale = neuropathie axonale. »).  
*Proposition :* Appliquer propositions/G58_c_3.html : remplacer les quatre encadrés par les libellés conformes et ajouter trois paragraphes sourcés (rendement de la biopsie, deux familles de fibres et asymétrie d’amplitude, mesna et élimination rénale de la prégabaline).  
*Preuves :* S8 (Sensibilité de la biopsie) ; S1 (Présentation et examen clinique) ; S15 (Posologie)

**C04 — `chapters/G58/G58_d.html`.** Les emplois hors indication en Suisse ne sont jamais signalés (addendum, point 5). Rituximab : la FI ne couvre que la GPA et la polyangéite microscopique ; la leçon le propose dans la cryoglobulinémie, la vascularite rhumatoïde et la NSVN. Méthotrexate : aucune indication de vascularite. Azathioprine : indiquée dans la périartérite noueuse, non dans l’entretien de la GPA, de la MPA ou de la NSVN. Duloxétine et gabapentine : douleur diabétique (et postherpétique pour la gabapentine) seulement. Lidocaïne en emplâtre : névralgie postherpétique, non recommandée avant 12 ans, alors que la leçon cite l’ACNES de l’enfant.  
*Proposition :* Remplacer le paragraphe par le tableau de statut suisse de propositions/G58_d_1.html et mettre à jour la fenêtre g58-ritux avec propositions/G58_pop2_1.html.  
*Preuves :* S17 (Indications) ; S21 (Indications) ; S20 (Indications) ; S23 (Indications) ; S24 (Indications ; Enfants)

**C05 — `chapters/G58/G58_d.html`.** Les précautions décisionnelles avant immunosuppression manquent : dépistage de l’hépatite B (HBsAg et anti-HBc) obligatoire avant le rituximab, prophylaxie de la pneumonie à Pneumocystis jirovecii recommandée dans les vascularites à ANCA sous rituximab, numération leucocytaire avant chaque cyclophosphamide avec seuils d’abstention (leucocytes < 2500/µl, plaquettes < 50 000/µl), bilan hépatique et sérologie VHB avant l’avacopan.  
*Proposition :* Ajouter l’encadré alert « Avant d’immunosupprimer » de propositions/G58_d_1.html dans l’îlot g58-p-1 (ou g58-p-3).  
*Preuves :* S17 (Mises en garde, hépatite B) ; S17 (Posologie GPA/PAM) ; S15 (Mises en garde) ; S19 (Posologie)

**C06 — `chapters/G58/G58_d.html`.** La gabapentine est présentée sans ses mises en garde suisses : dépression du SNC et respiratoire avec les opiacés (alors que la leçon rapporte l’association gabapentine-opioïdes comme « utile » selon l’EFNS) et risque de malformations au premier trimestre. La carte Grossesse de l’îlot g58-11 et l’îlot g58-p-4 ne visent que la prégabaline, ce qui peut orienter à tort vers la gabapentine chez la femme enceinte.  
*Proposition :* Appliquer les quatre remplacements de propositions/G58_d_2.html (G58_d.html g58-p-3 et g58-p-4, G58_b.html g58-11, fenêtre g58-neurontin).  
*Preuves :* S14 (Mises en garde) ; S14 (Mises en garde) ; S11 (Résumé)

## Constats mineurs

**C07 — `chapters/G58/G58_pop1.html`.** Koike donne une positivité des ANCA d’environ 80 % dans la MPA comme dans la GPA, sans chiffre propre au sous-type MPO ou PR3. La leçon (même erreur dans G58_c.html, extrait « <td>MPA (environ 80 % des cas), EGPA (30–40 %) ») attribue 80 % à chaque sous-type.  
*Proposition :* Remplacer par : « Les ANCA sont présents chez environ 80 % des patients avec polyangéite microscopique ou granulomatose avec polyangéite ; les anti-MPO s’associent à la première, les anti-PR3 à la seconde ; dans l’EGPA, la positivité n’est que de 30 à 40 % (Koike). »  
*Preuves :* S8 (Laboratory findings)

**C08 — `chapters/G58/G58_a.html`.** Le chiffre ne figure pas chez Blaes ; Koike le rapporte pour des patients avec MPA et GPA (10 décès sur 40 avec neuropathie), non pour toutes les vascularites à ANCA.  
*Proposition :* Remplacer « (Blaes ; Koike) » par « chez des patients avec MPA ou GPA (Koike) ».  
*Preuves :* S8 (Prognosis) ; S6 (Texte intégral)

**C09 — `chapters/G58/G58_d.html`.** La FI suisse parle d’« étourdissements (30,7 %) » ; « vertiges » y désigne un autre effet (rubrique oreille et labyrinthe, fréquent). Même terme dans la fenêtre g58-lyrica (« Vertiges (30,7 %), somnolence (16,4 %) »).  
*Proposition :* Remplacer « vertiges (30,7 %) » par « étourdissements (30,7 %) » dans G58_d.html et G58_pop2.html.  
*Preuves :* S13 (Effets indésirables)

**C10 — `chapters/G58/G58_b.html`.** Relation causale non établie par la source (addendum, point 3) : Shamoun décrit l’aggravation par l’inspiration profonde, la toux et la rotation, sans en donner le mécanisme. Même causalité dans G58_c.html (« étirent ou compriment le nerf intercostal, ce qui explique leur effet déclenchant »).  
*Proposition :* Remplacer par : « La source décrit cette aggravation sans en préciser le mécanisme. » et, en physiologie, supprimer la proposition causale.  
*Preuves :* S5 (Clinical presentation)

**C11 — `chapters/G58/G58_b.html`.** Trois relations causales sans source lue ; la persistance après cicatrisation n’est pas décrite par Shamoun.  
*Proposition :* Remplacer par : « La douleur a les caractères d’une douleur neuropathique (brûlure, éclair) et répond aux molécules de première ligne de la douleur neuropathique [Shamoun]. »  
*Preuves :* S5 (Texte intégral)

**C12 — `chapters/G58/G58_b.html`.** Affirmation non sourcée : Ruffer, Blaes et la PNS 2010 (résumé) lus ne la contiennent pas.  
*Proposition :* Remplacer par : « Les sources lues ne chiffrent pas l’effet d’une corticothérapie préalable sur la biopsie ; le médecin programme néanmoins l’électrophysiologie, le bilan et la biopsie le plus tôt possible. » La suite de l’encadré est conservée.  
*Preuves :* S7 (Texte intégral)

**C13 — `chapters/G58/G58_b.html`.** L’EFNS dit que doxycycline orale et ceftriaxone IV sont équivalentes lorsque les symptômes sont limités au système nerveux périphérique, méningite comprise ; les manifestations centrales relèvent de la ceftriaxone IV, et la doxycycline est contre-indiquée avant 8 ans.  
*Proposition :* Remplacer par : « équivalentes lorsque l’atteinte est limitée au système nerveux périphérique, méningite comprise (niveau A, EFNS) ; une atteinte centrale relève de la ceftriaxone IV pendant 14 jours, et la doxycycline est contre-indiquée avant 8 ans. »  
*Preuves :* S12 (Recommendations)

**C14 — `chapters/G58/G58_pop2.html`.** La revue systématique citée porte sur les douleurs chroniques abdominales et thoraciques (fourchette 55,8–100 %), non sur la seule névralgie intercostale.  
*Proposition :* Ajouter « dans les douleurs chroniques abdominales et thoraciques (55,8 à 100 %) ».  
*Preuves :* S5 (Treatment)

**C15 — `chapters/G58/G58_a.html`.** Ruffer rapporte une neuropathie chez « environ 50 % » des patients avec périartérite noueuse, non « jusqu’à 50 % ».  
*Proposition :* Remplacer par « Environ 50 % (Ruffer, 2024) ».  
*Preuves :* S7 (Klinik)

## Constats enrichissements

**C16 — `chapters/G58/G58_b.html`.** Les critères cliniques publiés de l’ACNES (point douloureux < 2 cm au bord latéral du grand droit, trouble sensitif, pincement, signe de Carnett, réponse à l’infiltration) sont absents.  
*Proposition :* Remplacer la phrase par propositions/G58_b_1.html ; fenêtres g58-sm-carnett et g58-sm-pincement dans G58_pop3_1.html.  
*Preuves :* S3 (Methods)

**C17 — `chapters/G58/G58_b.html`.** Rubrique 16 (spécificités suisses) absente et seule source suisse de clinique non exploitée : drapeaux rouges de la médecine interne suisse, vascularite possible avec biologie normale, lèpre importée, inaptitude possible à la conduite automobile.  
*Proposition :* Insérer les trois ajouts de propositions/G58_b_2.html (îlots g58-5, g58-7, g58-10).  
*Preuves :* S1 (Implications pratiques) ; S1 (Vasculites) ; S1 (Prise en charge spécifique)

**C18 — `chapters/G58/G58_a.html`.** La faiblesse de la biopsie n’est pas chiffrée alors qu’une source lue la donne : au plus 50 à 60 % pour une vascularite certaine.  
*Proposition :* Compléter : « la sensibilité de la biopsie nerveuse pour une vascularite certaine ne dépasse pas 50 à 60 % (Koike) ». Voir aussi propositions/G58_c_3.html (histologie).  
*Preuves :* S8 (Nerve biopsy)

## Matrice des 20 rubriques

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g58-0 |
| 2 | Définition et périmètre CIM-10-GM | couvert | g58-1, fenêtre g58-cim (vérifié BfArM 2024 [S25]) |
| 3 | Classifications et stades | couvert | g58-1 (deux tableaux PNS 2010) |
| 4 | Épidémiologie suisse puis européenne | partiel | g58-2 ; aucune donnée suisse (lacune déclarée) |
| 5 | Normal → pathologique | couvert | g58-3, sciences g58-s-anat à g58-s-bioch |
| 6 | Étiologies et facteurs de risque | couvert | g58-4 |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g58-5 ; seule fréquence : signes généraux 80 % / 50 % |
| 8 | Examen clinique (signes, Se/Sp) | partiel | g58-6 ; Se/Sp du seul scratch collapse test ; technique et Carnett absents (C01, C16) |
| 9 | Drapeaux rouges et urgences | partiel | g58-8 alert ; délai non chiffré, drapeaux rouges suisses absents (C17) |
| 10 | Examens complémentaires | couvert | g58-e-1 à g58-e-6 |
| 11 | Diagnostic différentiel | couvert | g58-7 (tableau à discriminants) |
| 12 | Prise en charge suisse | partiel | g58-9, onglet Pharmacologie ; emplois hors indication non signalés (C04), sécurité (C05, C06) |
| 13 | Complications et pronostic | couvert | g58-2, g58-8, g58-10 |
| 14 | Suivi, prévention, dépistage | partiel | g58-10 ; prévention du zona non traitée (lacune) |
| 15 | Situations particulières | partiel | g58-11 ; gabapentine et grossesse absente (C06) |
| 16 | Spécificités suisses | absent | aucune (conduite automobile, LAA/Suva, AI) ; proposition C17 |
| 17 | Critères formels du diagnostic | couvert | g58-12 div.alert |
| 18 | Paramètres clés chiffrés | couvert | g58-12 div.key |
| 19 | Sous-codes CIM-10-GM couverts | partiel | G58.0 et G58.7 traités ; G58.8 et G58.9 seulement définis |
| 20 | Points d’examen fédéral | partiel | quiz g58-7, g58-11, g58-e-6 ; objectifs PROFILES non cités (lacune) |

## 21 — Sémiologie fondamentale et analytique

**Statut : absente (MAJEUR, C01).** La leçon ne possède ni bouton `g58-s-semio`, ni discipline sémiologique. Les îlots `g58-5` et `g58-6` donnent une liste de symptômes et quelques signes (Schepelmann, palpation, scratch collapse test chiffré), sans mécanisme par signe, sans technique, sans normal, sans syndromes ni raisonnement. La proposition `propositions/G58_c_1.html` (sept îlots, figure non anatomique, trois cas) et `propositions/G58_pop3_1.html` (dix fenêtres) comblent l’ensemble, sur une source suisse en texte intégral (Revue Médicale Suisse 2019), le guide européen du Medical Research Council et les critères néerlandais de l’ACNES.

| Critère | Résultat |
|---|---|
| SEM-01 | non |
| SEM-02 | non |
| SEM-03 | non (discipline absente ; disciplines existantes en échec, C03) |
| SEM-04 | oui (test_v7.py --static G58 : OK, état actuel) |
| SEM-05 | non |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | non (une seule valeur chiffrée, sans section dédiée) |
| SEM-09 | non |
| SEM-10 | partiel (pièges g58-5, g58-7) |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | non (alert g58-8 hors discipline, sans seuil ni délai) |
| SEM-14 | oui pour g58-7 |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non |
| SEM-18 | non vérifié au navigateur |
| SEM-19 | partiel (Shamoun nord-américain pour faits descriptifs) |
| SEM-20 | sans objet |
| SEM-21 | sans objet |
| SEM-22 | non vérifié (aucune capture) |
| SEM-23 | non (aucune capture) |
| SEM-24 | oui (statut « revue IA, aucune validation médicale humaine ») |

Critères bloquants en « non » : SEM-01, SEM-02, SEM-03, SEM-08, SEM-13. SEM-04 est satisfait pour l’état actuel ; il devra être revérifié après intégration.

## Figures

Six schémas SVG, tous `SCHEMA_NON_ANATOMIQUE` (boîtes et flèches de raisonnement), aucune image, aucune figure anatomique générée. `viewBox` de 380 de large ; texte rendu à 13,2 px à 390 px, sans débordement (mesure Chromium). Les quatre icônes SVG de la barre des sciences n’ont pas d’`aria-hidden` (remarque d’accessibilité).

## Lacunes

- Texte intégral EULAR 2022 inaccessible (HTTP 403 ard.bmj.com ; non libre dans Europe PMC) : statut de la neuropathie comme atteinte menaçant un organe non vérifié
- Aucune recommandation de société suisse (SSN, SSR) sur la neuropathie vasculitique ni sur la névralgie intercostale lue
- Recommandation OFSP de vaccination contre le zona : téléchargement du PDF OFSP refusé (HTTP 502, 16.10.2026) ; non rédigée
- Critères suisses d’aptitude à la conduite en cas de neuropathie non lus
- Objectifs PROFILES de l’examen fédéral non consultés
- Fréquences, sensibilités et spécificités des symptômes de la mononévrite multiple : non chiffrées dans les sources lues
- Muscles testant le nerf tibial : non relevés dans le guide MRC lu ; Koike lu sur ses 100 000 premiers caractères seulement
- Mise à jour de la ligne directrice PNS 2010 : recherche PubMed sans résultat exploitable

Faits repris du dossier Betta 38 sans relecture dans cet audit : Théaudin 2022 (RMS, petites fibres) ; Pereira 2025 ; Pacut 2024 ; Soulages 2022 ; Aladawi 2022 ; Redmond 2025 ; Benditz 2025 ; Chaudhuri 1997 ; Tascón Padrón 2025 ; Yavuz 2026 ; Kidoguchi 2026 : faits repris du dossier Betta 38, non relus dans cet audit.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G58 — Autres mononévrites (S08, N-05-Neurologie) |
| Fichiers lus / empreintes conformes | 7 / 7 |
| Constats | 0 bloquant, 6 majeurs, 9 mineurs, 3 enrichissements |
| Sources lues | 28 : 13 suisses (Revue Médicale Suisse et douze informations professionnelles), 15 européennes, internationales ou revues (dont Shamoun, nord-américaine, pour des faits descriptifs seulement) |
| Propositions | 10 fichiers dans `propositions/` |
| Contrôles | `test_v7.py --static` OK ; `audit_sciences.py` en échec (C03) ; 33 ancres uniques vérifiées |
| Figures | 6 schémas non anatomiques, lisibles à 390 px |
| Sémiologie (rubrique 21) | absente → proposition complète |
| Alerte | Aucune erreur dangereuse ; intégrer C04 à C06 avant toute republication de l’onglet Pharmacologie |

Audit différé — revue IA, distincte d’une validation médicale humaine.
