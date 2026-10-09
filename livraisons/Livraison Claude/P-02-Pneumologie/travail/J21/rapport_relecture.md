# J21 — Bronchiolite aiguë et infections respiratoires basses non précisées (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J21 (J21.0, J21.1, J21.8, J21.9) et J22 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/J21/chapters/J21/` (6 fichiers), `travail/J21/glossary/j21.py`, `rapport_auteur.md` (arbitrages 1-7, réserves 1-9). Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J21/` et `glossary/j21.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil, dose et attribution à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé, sourcé ou retiré les affirmations fautives. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, et corrigé les défauts restants (formulations causales non sourcées, tableaux non introduits, redondances). Ensuite sont venus les contrôles techniques, les captures et l’injection.

Sources téléchargées indépendamment de l’auteur le 09.10.2026 :
- PDF intégraux : OFSP/CFV, recommandations VRS 2026 (bulletin) ; Plan de vaccination suisse 2026 ; Haute Autorité de santé 2019 ; SAPP 2003 (Paediatrica) ; Barben, Regamey et Hammer, Forum Médical Suisse 2020 (PDF intégral via CLOCKSS, résolu depuis le DOI) ;
- pages HTML lues en entier : NICE NG9 (recommandations 1.1 à 1.6 et justifications 2021) ; Pédiatrie Suisse, listes « smarter medicine » 2021 (FR) et 2024 (DE) ; OFSP, page VRS ;
- textes intégraux Europe PMC (XML) : Woodhead ERS/ESCMID 2011 (PMC7128977), Pickles et DeVincenzo 2015 (PMC5638117), Øymar 2014 (PMC4230018), Jartti/EAACI 2019 (PMC6587559) ;
- résumés PubMed (`efetch`) des 23 PMID cités ;
- informations professionnelles suisses (AIPS via AmiKo, `tools/swissmedic_fi.py`), texte intégral : Beyfortus® (07.2026), Enflonsia® (11.2025), Abrysvo® (07.2026), Arexvy (06.2026), mRESVIA (08.2026), Dafalgan® enfant sirop (09.2025), Rinosedin® 0,05 % gouttes nasales (02.2025), Otrivin Rhume (02.2025).

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Causalité VRS → asthme | « Les essais d’immunoprophylaxie chez le prématuré, qui réduisent les sifflements récidivants, plaident pour une part causale du VRS » | Jartti/EAACI 2019, texte intégral : le palivizumab réduit les sifflements rapportés par les parents, **non l’asthme diagnostiqué à 6 ans** ; « RSV infection is not causal to the asthma » | Sens inversé corrigé : association sans causalité démontrée ; vulnérabilité commune. Libellé du mot vert de l’îlot 2 ajusté |
| Interférence du clesrovimab | Absente ; « le nirsévimab ne perturbe pas les tests » généralisé (Sciences) | AIPS Enflonsia® : peut fausser les **tests antigéniques rapides** ; RT-PCR non perturbée. AIPS Beyfortus® : tests visant les sites I, II ou IV non perturbés | Ajout dans la fenêtre Recherche virale, la monographie, les précautions, la clé Science → examen (site Ø contre site IV) et le Pareto |
| Transmission par les cellules desquamées | « Restent probablement infectieuses, ce qui favorise la transmission » | Pickles 2015 : ce matériel infecté « may influence further spread of RSV infection » (extension dans l’arbre bronchique) | Reformulé : extension intrabronchique possible, non transmission interhumaine |
| Facteurs d’environnement (HAS) | Crèche, allaitement, naissance péri-épidémique et fratrie présentés comme valables pour tout nourrisson | HAS 2019, § 1.2 : ces critères sont établis **chez le prématuré de moins de 35 SA** | Tableau restructuré par population ; ajout du grade C du transfert en réanimation lié au tabagisme passif |
| Colonne « Indice » du diagnostic différentiel (réserve 6 de l’auteur) | « Nouveau-né, fièvre, altération de l’état général » ; « Détresse disproportionnée, nouveau-né, souffle » ; « bronchodilatateur d’épreuve justifié » ; « cassure pondérale » non sourcés | HAS 2019 (définitions : infection néonatale, insuffisance cardiaque ; fièvre bien tolérée du nouveau-né ; suivi 4-6 semaines, retentissement pondéral) ; NICE 1.1.6-1.1.7 ; Barben 2020 ; SAPP 2003 (essai de bêta-2-mimétique si hyperréactivité connue) | Colonne renommée « Ce qui la fait évoquer » ; chaque indice rattaché à une source ; « souffle » et « disproportionnée » retirés |
| Seuil d’adressage au cabinet | Absent | NICE 1.2.2 (2021) : 92 % maintenu pour **envisager l’adressage** depuis les soins primaires (marge de sécurité, oxymétrie moins fiable) | Ajouté à la fenêtre d’arbitrage des seuils et à la fenêtre NICE/SSPP |
| HARMONIE | « 0,3 % contre 1,5 % » sans comparateur | Drysdale 2023 : comparaison aux **soins habituels sans intervention** (essai ouvert) | Comparateur précisé (monographie, glossaire) |
| Efficacité 70,1 % | « Chez les prématurés de 29 à 35 semaines » sans critère | AIPS Beyfortus® (étude D5290C00003) | Précisé : contre l’infection médicalement prise en charge |
| Guillain-Barré (Abrysvo®, Arexvy®) | « Une étude après commercialisation » unique | AIPS : deux études observationnelles américaines distinctes ; Abrysvo® RR 2,02 (IC 0,93-4,40), 9/10⁶ ; Arexvy 7/10⁶, causalité non établie avec certitude | Pluriel, origine et intervalle de confiance rétablis (donnée, non fondement de conduite) |
| Adjuvant d’Arexvy | « Déjà utilisé dans le vaccin contre le zona » sans source | Bulletin OFSP 2026, ch. 5.3 (AS01E, Shingrix®) ; AIPS (QS-21, MPL) | Attribué à l’OFSP ; clé AS01E ajoutée au glossaire |
| Revaccination Arexvy | « N’a pratiquement rien ajouté » sans source | Bulletin OFSP 2026, ch. 6.2 (Ison 2024-2025) | Attribué au bulletin |
| Récepteur Fc néonatal | « Qui recycle les immunoglobulines G » (ajout de passe 1) | Absent des AIPS | Retiré |
| Infiltrat péribronchiolaire | « Infiltrat de cellules mononucléées » | Pickles 2015 : « peribronchiolar infiltration and submucosal oedema » | Corrigé |
| CRP de l’adulte | « Une élévation modérée s’observe aussi dans les infections virales » (attribué à Barben, article pédiatrique) | Woodhead 2011 (B1) ; marqueurs bactériens déconseillés en soins primaires (A1) | Phrase non sourcée retirée ; limites reformulées sur la recommandation |
| Alimentation | « Critère le plus fréquent d’hospitalisation » | Aucune source | Remplacé par « à elle seule un critère d’hospitalisation » (NICE, SSPP) |
| Désobstruction (HAS) | « Déconseille les aspirations nasopharyngées profondes » | HAS 2019 : les aspirations nasopharyngées « ont plus d’effets secondaires et ne sont pas recommandées » | Citation alignée |
| Suivi | « Conduisent au pneumopédiatre » | HAS 2019 : « avis spécialisé » | Corrigé |
| Haut débit | « 2 L/kg/min » et « plus de 2 L/kg/min » selon les îlots | HAS 2019 : 2 L/kg/min ; Barben 2020 : > 2 L/kg/min | Harmonisé : « environ 2 L/kg/min (HAS) ; plus de 2 L/kg/min (SSPP) » |
| ProHOSP | « Événements indésirables à 30 jours » | Schuetz 2009 : critère composite (décès, soins intensifs, complications, récidive) | Précisé |
| Réinfections | « La règle à tout âge » ; rôle des adultes « dans la contamination des nourrissons » | OFSP 2026 : réinfection possible à tout moment ; conseil d’éloigner les personnes qui toussent | Reformulé sur la source |
| Site d’injection | « Cuisse antérolatérale » | AIPS Beyfortus® et Enflonsia® : pas la région fessière (nerf sciatique) | Précision ajoutée ; « seringue différente » non sourcée retirée |
| Personne âgée, nirsévimab chez le prématuré | « Efficacité plus faible chez le prématuré ou < 2500 g » sans origine | Bulletin OFSP 2026, ch. 6.2 (Núñez 2025, Espagne, nirsévimab) | Origine précisée |
| Persistance des prescriptions | « La pression des parents et la volonté de faire quelque chose expliquent… » | Aucune source | Retiré ; constat de pratique suisse sourcé (SAPP 2003, Barben 2020) |
| Arexvy, Abrysvo, vaccins adultes (tableau 3 OFSP) | Ligne « Poumon » incomplète | OFSP 2026, tableau 3 | Emphysème, bronchectasies, mucoviscidose, fibrose, asthme avec exacerbations ajoutés |

Vérifiés sans changement (confrontés mot à mot) : toutes les données épidémiologiques suisses (2410/100 000, 2,4 %, 3,7 %, 55 %, 4,4 jours, 5-10 %, 0,012 %, 75-90 %, 56 %, 6,4 %/10,7 %) ; registre de Stucki (3575, 2487, 902, 118 jours, 74 ans, 7,2 %, 90,8 %) ; grille SSPP (tableau 2) et grille HAS ; critères NICE (1.1 à 1.6) ; seuils HAS de réanimation (capnie 46-50 mmHg, pH 7,34) ; leucocytose et CRP de la SAPP 2003 ; virologie d’Øymar ; 120/250 µm et ventilation collatérale (Pickles) ; toutes les données d’essais (Gadomski, Hartling, Fernandes, Zhang, Roqué-Figuls, Gajdos, Rochat, Franklin, Cunningham, Little, Smith, Schuetz, Hammitt, Drysdale, Zar, Kampmann, Walsh, Papi) ; toutes les doses et contre-indications des AIPS (nirsévimab 50/100/200 mg et doses après CEC ; clesrovimab 105 mg ; Abrysvo® 32 0/7-36 0/7 ; mRESVIA contre-indiqué avant 8 mois, rappel ≥ 12 mois ; Dafalgan® 15 mg/kg, 3-4 prises, 6-8 h, 75 mg/kg/j, 3 jours, intervalles 6 et 8 h selon la clairance, maladie de Gilbert ; Rinosedin® 0,05 % interdit avant 1 an) ; algorithme suisse 2026, exceptions et deuxième saison ; groupes adultes ; non-remboursement adulte (état automne 2026).

### Sources et plan
- Plan monographique conservé (14 îlots, de la question clinique aux critères formels puis paramètres clés). Le code CIM n’apparaît que dans l’en-tête discret ; aucun îlot ni tableau ne lui est consacré.
- Titre harmonisé avec `organisation/FILE_FRAGMENTS_CLAUDE.json` : « Bronchiolite aiguë et infections respiratoires basses non précisées » (h1, en-tête, glossaire, rapport).
- Aucune recommandation américaine ne fonde une conduite. Les études américaines (Guillain-Barré, MEDLEY, cohortes citées par l’EAACI) sont rapportées comme données ; la définition américaine de la bronchiolite n’est citée que pour expliquer la lecture des essais.
- Références ajoutées : Øymar (îlot 3, anatomie), Barben (anatomie, pharmacologie p-4), SAPP (fenêtres bronchodilatateurs, asthme, configurations), OFSP page VRS (îlot 4, microbiologie), NICE 1.6.1 (signes d’alerte), NICE 1.5.1 et HAS (physiologie), OFSP ch. 2.2/6.3/6.4 (précautions), sources de l’îlot Examens 3 (auparavant sans références).

### Fenêtres fusionnées (consigne de l’orchestrateur)
- `j21-fr` (fréquence respiratoire) et `j21-tirage` (signes de lutte) fusionnées dans `j21-gravite` (« signes, seuils et pièges »).
- `j21-sibilants` fusionnée dans `j21-crepitants` (auscultation) et `j21-asthme-diff`.
- `j21-diametre` supprimée (contenu dans l’îlot 3 et l’onglet Sciences).
- `j21-nice` fusionnée dans `j21-sspp` (textes suisses et NICE, arbitrage).
- `j21-atelectasie` fusionnée dans `j21-ns2` (« De la protéine NS2 à l’hypoxémie »).
- Résultat : **60 fenêtres** (54 + 6 Pareto) contre 66 dans le brouillon.

### Rédaction
- Phrases causales non démontrées reformulées en concordances (« ce mécanisme concorde avec l’échec démontré… ») ; renvoi « (îlot 9) » remplacé par une phrase complète.
- Tableaux de fenêtres non introduits (seuils d’oxygène, sortie, virus, diagnostics imitateurs, environnement) : introduction et lecture ajoutées (STYLE_REDACTION § 4).
- Légende de la figure 1 complétée par son sens de lecture.
- Noms propres signalés par l’audit des abréviations (« DeVincenzo », « Vidal-Quadras ») remplacés par « et al. ».

## Corrections de la passe 2
La relecture intégrale du texte corrigé a encore modifié les points suivants :
- grille HAS : « SpO₂ supérieure à 90 % et au plus égale à 92 % » (forme modérée), au lieu d’une formule ambiguë ;
- vaccins de l’adulte : paragraphe d’efficacité redondant avec les monographies remplacé par une fourchette exacte (67 à 86 % selon le vaccin et la définition) ;
- fenêtre CRP : seuils et limites resserrés ; fenêtre antibiotiques de l’adulte : doublon avec l’îlot 10 retiré ;
- monographies : doses de base renvoyées au tableau des doses, seules les doses après CEC et les divergences (rappel mRESVIA : AIPS contre OFSP) conservées ;
- fenêtres bronchodilatateurs, adrénaline, corticoïdes, sérum hypertonique, hyponatrémie, antibiotiques du nourrisson, NICE, désobstruction, alimentation, chronologie : redondances retirées ;
- îlot Examens 2 : biologie et radiographie regroupées ; piège de l’oxymétrie condensé ; « À retenir » redondant retiré ;
- îlot 12 : nourrisson de moins de 6 semaines et terrains à risque regroupés ;
- Pareto réécrits plus serrés.

## Volume
Mesure identique pour les deux versions (texte hors SVG) : brouillon 19 903 mots avec références (17 715 sans), version relue **19 981 avec références (17 679 sans)**. Le volume est donc **stable** : les fusions et suppressions de redondances (six fenêtres en moins, Pareto et fenêtres resserrés) ont été compensées par les corrections et ajouts sourcés exigés par l’audit (interférence du clesrovimab, causalité EAACI, seuil d’adressage du NICE, études MEDLEY et MUSIC, comparateur d’HARMONIE, regroupement HAS par population, indices du diagnostic différentiel, introductions de tableaux). Aucune information utile n’a été retirée.

## Sources vérifiées (34 liens, tous contrôlés le 09.10.2026)

**PubMed (23), vérifiés par `esummary` (premier auteur, année, revue concordants) ; pages servies en HTTP 203 par le proxy :**
19738090 Schuetz 2009 JAMA · 20927359 Gajdos 2010 PLoS Med · 21678340 Hartling 2011 Cochrane · 21927808 Rochat 2012 Eur J Pediatr · 23265995 Little 2013 Lancet Infect Dis · 23733383 Fernandes 2013 Cochrane · 24694087 Øymar 2014 Scand J Trauma Resusc Emerg Med · 24937099 Gadomski 2014 Cochrane · 25302625 Pickles 2015 J Pathol · 26382998 Cunningham 2015 Lancet · 28626858 Smith 2017 Cochrane · 29562151 Franklin 2018 N Engl J Med · 30276826 Jartti 2019 Allergy · 35235726 Hammitt 2022 N Engl J Med · 36791160 Papi 2023 N Engl J Med · 37010196 Roqué-Figuls 2023 Cochrane · 37014057 Zhang 2023 Cochrane · 37018468 Walsh 2023 N Engl J Med · 37018474 Kampmann 2023 N Engl J Med · 38157500 Drysdale 2023 N Engl J Med · 39137355 Hayes Vidal-Quadras 2024 Swiss Med Wkly · 39328156 Stucki 2024 Euro Surveill · 40961446 Zar 2025 N Engl J Med.

Mode de lecture : texte intégral pour Pickles, Øymar, Jartti et Woodhead ; résumé pour les autres.

**URL officielles (HTTP 200, contenu lu)**
- OFSP et CFV, recommandations VRS, mise à jour 2026 : https://www.bag.admin.ch/dam/fr/sd-web/BPXrATSRdad7/Bulletin-2026-Recommandations-VRS.pdf (chapitres 1 à 7 lus ; tableaux 3 et 4)
- Plan de vaccination suisse 2026 : https://www.bag.admin.ch/dam/fr/sd-web/Oj0BSN-w-Ggs/Plan%20de%20vaccination%20suisse_2026_FR_Web_final.pdf (chapitres 1.1.a, 3.1.i, figure 1)
- OFSP, page VRS : https://www.bag.admin.ch/fr/virus-respiratoire-syncytial-humain-vrs
- Barben, Regamey, Hammer, Forum Médical Suisse 2020 : https://doi.org/10.4414/fms.2020.08460 (PDF intégral lu, tableaux 1 à 6)
- SAPP, Paediatrica 2003 : https://files.paediatrieschweiz.ch/production/uploads/2021/09/18-22-1.pdf
- Haute Autorité de santé, novembre 2019 : https://www.has-sante.fr/upload/docs/application/pdf/2019-11/hascnpp_bronchiolite_texte_recommandations_2019.pdf
- NICE NG9, version du 09.08.2021 : https://www.nice.org.uk/guidance/ng9/chapter/Recommendations
- Woodhead, ERS/ESCMID 2011 : https://pmc.ncbi.nlm.nih.gov/articles/PMC7128977/ (lu via Europe PMC)
- Pédiatrie Suisse, smarter medicine 2021 et 2024 : https://www.smartermedicine.ch/fr/liste-top-5/pediatrie ; https://www.smartermedicine.ch/de/top-5-listen/paediatrie-2024
- Swissmedic (AIPS) : https://www.swissmedicinfo.ch/ — textes lus via AmiKo : Beyfortus® 7680690390020 (07.2026), Enflonsia® 7680701450019 (11.2025), Abrysvo® 7680696910017 (07.2026), Arexvy 7680693100015 (06.2026), mRESVIA 7680699950010 (08.2026), Dafalgan® enfant sirop 7680438380023 (09.2025), Rinosedin® 0,05 % 7680533490139 (02.2025), Otrivin Rhume 7680588570039 (02.2025).

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 60 `data-k` = 60 gabarits (54 fenêtres et 6 Pareto), tous préfixés `j21-` ou `pareto-j21-` ; aucun identifiant dupliqué ; couvertures Pareto valides |
| Classes | toutes dans la liste fermée (`CLASSMAP` de `build_medina.py`) |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; pop1 et pop2 bien formés |
| `build_medina.py J21` (copie superposée, entrée J21 temporaire dans une copie de `chapters.json`) | `J21 non couvertes: 0` ; Pareto calculés : 4 %, 10 %, 7 %, 6 %, 8 % et 7 % |
| Glossaire | `glossary/j21.py` à ajout conditionnel : 19 clés propres, aucune collision avec les modules du dépôt. `glossary/j12.py`, injecté en parallèle et chargé avant, définit déjà CFV et mRESVIA : ces deux entrées ne sont pas écrasées ; build relancé avec `j12.py` présent : `J21 non couvertes: 0` |
| Contrat sciences (logique de `tests/audit_sciences.py`) | 4 disciplines, navigation complète, 335 / 387 / 385 / 574 mots, 1 figure légendée et nommée chacune, 4 encadrés de corrélation chacune : aucune erreur |
| `build_front.py --fragment S02` (copie superposée) | 5,47 Mo, compressé à 2,73 Mo |
| Chromium 1194, `#/entry/J21` | titre correct ; 4 onglets ; 60 mots verts distincts ouverts dans les 4 onglets et les 4 disciplines, aucun « Fiche absente » ; aucune erreur JavaScript ni de console ; mobile 390 px sans défilement horizontal sur les 4 onglets |
| `tools/capture_lecon.py` | `captures/j21-1-ouverture.png`, `captures/j21-2-explication.png` (fenêtre « Degrés de gravité de la bronchiolite : signes, seuils et pièges ») ; statut : relu, injecté, non enregistré dans `chapters.json` |
| Liens | 34 URL uniques : 11 en HTTP 200, 23 PubMed en HTTP 203 (proxy) avec existence confirmée par `esummary` |

## Réserves restantes (non bloquantes)

1. **Pas de recommandation suisse gradée** de prise en charge depuis 2003 : la mise à jour SSPP 2020 est un article de revue. La conduite s’appuie aussi sur le NICE (britannique) et la Haute Autorité de santé (française), avec arbitrages exposés en fenêtre.
2. **ERS/ESCMID 2011** reste la seule recommandation européenne lue pour l’infection respiratoire basse de l’adulte ; elle est ancienne. La conduite détaillée de la pneumonie est renvoyée au cours J18.
3. **Lectures limitées au résumé** pour les essais et revues Cochrane ; chiffres d’efficacité de mRESVIA (83,7 %) et revaccination d’Arexvy repris du bulletin OFSP 2026, publications originales non lues.
4. **Tableau 3 de la SSPP 2020** (« Enfants < 6–8 ans ») : coquille manifeste, non reprise.
5. **Déductions physiologiques directes** (« l’oxygène corrige l’hypoxémie sans lever l’obstruction », « la voie orogastrique laisse les narines libres ») restent formulées sans citation mot à mot.
6. **Glossaire** : CFV et mRESVIA affichent les définitions de `glossary/j12.py` si ce module est présent ; s’il était retiré, celles de `j21.py` prendraient le relais (ajout conditionnel).
7. **Volume** stable (voir ci-dessus) malgré la fusion de six fenêtres : le resserrement a été compensé par les corrections sourcées.
8. Données de sécurité américaines (Guillain-Barré) citées comme données, via les AIPS et le bulletin OFSP, non comme fondement de conduite.
9. `chapters.json` et `organisation/*` n’ont pas été modifiés, comme demandé : l’enregistrement revient à l’orchestrateur. Les contrôles ont été faits sur une copie superposée.

## Injection

- `chapters/J21/` : `J21_a.html`, `J21_b.html`, `J21_c.html`, `J21_d.html`, `J21_pop1.html`, `J21_pop2.html`.
- `glossary/j21.py` : glossaire révisé (ajout conditionnel ; MATISSE et mRESVIA sans développement inventé ; MEDLEY, MUSIC et AS01E ajoutés).
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J21/captures/` : deux captures et `captures.json`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
