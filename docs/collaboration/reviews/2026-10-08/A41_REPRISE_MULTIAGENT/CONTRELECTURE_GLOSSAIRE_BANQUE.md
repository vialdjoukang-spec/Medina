# Actualisation de la contrelecture — 24 définitions et deux formulations éditoriales

**Avis favorable aux 24 nouvelles définitions d’A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie), ainsi qu’aux deux substitutions éditoriales de la banque, sans nouvelle réserve bloquante, majeure ou mineure dans ce périmètre.** Le contrôle initial est conservé ; cet avis reste distinct du nouveau contre-audit Claude du paquet final.

| Pièce figée | Empreinte SHA256 |
| --- | --- |
| Glossaire proposé, 59 appels et clés uniques, 36 nouvelles clés au total | `f7d9e45c7df4b04d4b746989fbf3b7808dfec9712415fef0de51533affc2d69a` |
| Banque proposée, 14 justifications, deux formulations développées | `c47273d990cbbc4e68a1f0d0620e4f17c6be96f507a1747e1866699a56c18822` |

Le delta depuis `ad22c21964b491c71776a07a5f4eaa350f8e2b3fcb50ba8ab6086ecf8b915840` contient **24 ajouts, 35 définitions antérieures identiques, zéro suppression et zéro modification antérieure**. L’identité est vérifiée sur les arguments littéraux AST normalisés ; aucun module entrant exécuté. L’absence de collision avec G runtime est la preuve du coordinateur, distincte de nos 59 clés locales uniques.

## Deux substitutions éditoriales de la banque

Dans `a41-j-vasopresseur-arythmies` :

| Chemin JSON | Avant | Après |
| --- | --- | --- |
| `entries[11].sources[0].title` | DeBacker2010, SOAPII | De Backer et coll., 2010 : noradrénaline et dopamine |
| `entries[11].mechanism[0]` (segment) | SOAPII compare dopamine et noradrénaline | L’essai de De Backer et coll. (2010) compare dopamine et noradrénaline |

Chaque nouveau segment existe une fois. Leur remplacement inverse reconstitue exactement le SHA initial `17491c0808ff4a5fb7bef7f636a2e350a27cca3cc9c0f7bea155914b3a20b81e` : **tous les autres octets sont identiques**, dont URLs, chiffres et formulations de conduite. Le texte du mécanisme change éditorialement ; son sens médical reste identique. Avis favorable aux deux développements, sans nouveau résultat ajouté.

## Périmètre du glossaire

| Nouvelle clé | Contrôle et limite |
| --- | --- |
| A32.7 | « Listeriensepsis » réellement lu ; code spécifique distinct d’A41, sans couverture exhaustive annoncée. |
| B37.7 | « Candida-Sepsis » réellement lu ; contexte et risque distingués, sans antifongique universel. |
| NEWS | National Early Warning Score correct ; alerte physiologique distincte d’infection et de définition du sepsis. |
| NEWS2 | Deuxième version du National Early Warning Score ; protocole et clinique nécessaires, aucun seuil thérapeutique inventé. |
| MEWS | Modified Early Warning Score correct et distinct de NEWS2 ; ne remplace ni examen ni diagnostic causal. |
| CAPITA | Community-Acquired Pneumonia Immunization Trial in Adults confirmé par analyse primaire. CAPiTA/CAPITA distingués ; PCV13 et adultes âgés corrects, sans prévention de tout sepsis déduite. |
| PCV13 | Pneumococcal Conjugate Vaccine, treize sérotypes ; essai historique distinct des recommandations actuelles. |
| SCCM | Society of Critical Care Medicine correct ; of hors découpage. Coédition avec ESICM, sans nouvelle prescription. |
| SAPS | Stop Antibiotics on Procalcitonin Guidance Study exact. Conseil d’arrêt en soins intensifs, sans diagnostic isolé ni début automatique d’antibiotique. |
| CHUV | Centre hospitalier universitaire vaudois correct ; plages attachées au document, à la méthode et à la matrice. |
| USZ | Universitätsspital Zürich correct ; découpage orthographique explicite, sans généralisation des plages à tous les laboratoires. |
| PAI-1 | Plasminogen Activator Inhibitor, type 1, correct. Inhibition d’activateurs et réduction possible de fibrinolyse, sans résumer tout l’état de coagulation. |
| dL | Décilitre = 0,1 L ; 1 mg/dL = 10 mg/L. Conversion exacte. |
| Garcia-Alvarez | Garcia-Alvarez, auteur de la revue Sepsis-associated hyperlactatemia de 2014, confirmé. Revue distinguée d’une étude primaire et modèles distingués des observations humaines. |
| Plasma-Lyte | Nom commercial de cristalloïdes équilibrés. Présentation et composition à vérifier ; toutes les formulations ne deviennent pas interchangeables. |
| SMART | Nom arrangé de Isotonic Solutions and Major Adverse Renal Events Trial conforme. Extension Medical Intensive Care Unit du registre distinguée ; composite incluant décès, pas gain de survie isolé. |
| BaSICS | Balanced Solution Versus Saline in Intensive Care Study exact. Absence de réduction significative de mortalité à 90 jours distincte d’une équivalence générale. |
| PLUS | Plasma-Lyte 148 versUs Saline Study concorde au briefTitle. Pas de bénéfice démontré sur mortalité ou atteinte rénale ; aucune généralisation à toutes les situations. |
| SAFE | Saline versus Albumin Fluid Evaluation confirmé par le titre de l’analyse primaire. Essai 2004 albumine/saline en soins intensifs, sans interchangeabilité en toute situation déduite. |
| ALBIOS | ALBumin Italian Outcome Sepsis exact dans officialTitle. Résumé primaire PMID 24635772 effectivement relu : absence de gain de survie à 28 et 90 jours ; pas d’indication universelle issue d’un sous-groupe. |
| DC | Débit cardiaque = volume éjecté par unité de temps, L/min. Son augmentation ne prouve pas la restauration de toute perfusion d’organe. |
| PVC | Pression veineuse centrale en mmHg. Mesure statique isolée non fiable pour prédire réponse aux liquides ; aucune cible universelle inventée. |
| CaO₂ | Contenu artériel en oxygène par volume de sang, mL/dL dans le chapitre ; dépend surtout de Hb et saturation. Saturation seule insuffisante, aucun seuil de prescription ajouté. |
| DO₂ | Apport global = DC × CaO₂ avec conversion ; L/min × mL/dL nécessite facteur 10 pour mL/min. Calcul distinct de répartition régionale et extraction cellulaire. |

## Lectures et limites

Les cinq captures officielles `saps_registry.json`, `basics_registry.json`, `plus_registry.json`, `albios_registry.json` et `smart_registry.json` ont été lues avec titres et identifiants. Les noms arrangés SMART/BaSICS/PLUS et le développement ALBIOS concordent aux registres. Le composite SMART reste distinct de la survie isolée. Le résumé primaire ALBIOS (PMID 24635772) est également relu dans la capture Pathologie2 : 1 818 patients, sans gain de survie à 28 ou 90 jours. La conclusion proposée est conservatrice ; cette lecture est distincte de la contrelecture de Pathologie2 et d’un texte intégral.

Les résumés primaires Pathologie2 de SAFE (PMID 15163774) et CAPiTA (PMID 25785969) sont effectivement relus. Deux analyses primaires supplémentaires accessibles confirment les noms développés : SAFE, PMID 17040925 ; CAPiTA, PMID 28173960. NCT00744263 confirme CAPITA et PCV13. Ces lectures ne prouvent ni interchangeabilité de tous les solutés ni prévention de tout sepsis ; elles sont distinguées de textes intégraux.

Les rubriques BfArM 2024 affichent **A32.7 Listeriensepsis** et **B37.7 Candida-Sepsis**, avec notes de codage réellement lues. La présence d’un code au glossaire ne signifie pas couverture complète ou certification CIM-11. NEWS/NEWS2/MEWS restent des alertes physiologiques, sans diagnostic infectieux automatique ni seuil thérapeutique ajouté. Les cartes SSC 2026 de dépistage et de mesures dynamiques sont relues dans leur capture.

DC, PVC, CaO₂ et DO₂ sont cohérents au niveau physiologique et dimensionnel : DC en L/min × CaO₂ en mL/dL nécessite la conversion par 10 pour DO₂ en mL/min. Les limites de perfusion régionale, extraction et réponse au liquide sont explicites. Cet avis ne certifie pas le Pareto entier à partir de ces définitions.

Les URL, textes lus, empreintes, dates et limites sont dans `delta_review` du JSON. La preuve initiale complète reste sous `initial_review`, et le texte initial est conservé ci-dessous. Les liens HTML de la banque ne sont pas réaudités dans cette mission limitée ; ils devront rester conformes dans le paquet final.

ESP03 reste partielle pour les normes suisses artérielles. Aucun chapitre ou fragment déclaré achevé, aucun contre-audit Claude réputé terminé, aucun canonique/Git modifié ni injection. Avis arrêté à 2026-10-08T12:52:27.537313+00:00 UTC.

---

# Preuve initiale conservée — glossaire ad22c219 et banque 17491c08

# Contrelecture du glossaire et de la banque

**Avis favorable sur le draft figé de A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie), sans nouvelle réserve bloquante, majeure ou mineure dans ce périmètre.** Les observations ESP27–32 sont correctement traitées dans la proposition. Cet avis Codex ne ferme pas le nouveau contre-audit Claude et n’autorise pas à lui seul l’injection du chapitre.

## Périmètre effectivement relu

Les fichiers relus sont exclusivement dans `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/sources/` :

| Fichier proposé | Empreinte SHA256 de cet avis |
| --- | --- |
| `glossary/a41.py` | `ad22c21964b491c71776a07a5f4eaa350f8e2b3fcb50ba8ab6086ecf8b915840` |
| `chapters/A41/A41_justifications.json` | `17491c0808ff4a5fb7bef7f636a2e350a27cca3cc9c0f7bea155914b3a20b81e` |

Le glossaire comporte **35 clés, dont 12 ajouts**, et la banque **14 entrées**. La proposition a évolué pendant la lecture : les deux derniers essais ProCESS/ARISE, puis ProMISe, ont été relus ; HLA-DR est finalement retiré des ajouts et utilise la définition globale déjà enregistrée par la boucle de `m06.py`. La preuve runtime du coordinateur (1 350 clés,12 ajouts sans collision) reste distinguée de notre lecture statique ; un simple scan des appels AST directs manquerait cette boucle.

Les canoniques ont été lus auparavant seulement pour situer l’ancienne version, avant que les bons chemins draft soient précisés. Aucune conclusion de cet avis ne prend le canonique pour la nouvelle proposition. Aucune écriture canonique ni mutation Git par ce poste.

## Résolution proposée des six observations

| Observation | Contrelecture et preuve |
| --- | --- |
| ESP27 — glycémie | Bose (PMID 27754788) est explicitement limité aux souris, dexaméthasone deux semaines et invalidation tissulaire. APROCCHSS (PMID 29490185) apporte une observation clinique d’hyperglycémie plus fréquente sous hydrocortisone+fludrocortisone, sans attribuer quantitativement cet effet à une molécule seule. La remarque 2021 sur 8–10 mmol/L reste distincte du seuil 2026 ≥ 10 mmol/L. |
| ESP28 — muqueuse gastrique | Menguy (PMID 4278107) est explicitement limité au choc hémorragique chez rat/lapin. L’énoncé 2026, RecomGroup 87 cible les facteurs de risque digestif et porte conditionnelle/modérée ; le seul diagnostic de sepsis ne suffit pas. |
| ESP29 — rendement des cultures | Mermel (PMID 8328734) :829 paires,8,7 contre 2,7 mL,92 contre 69 %,environ 3 %/mL. Cheng (PMID 31525774) :325 patients sélectionnés,31,4 contre 19,4 %,sensibilité 52,9 %,contrôle dans 120 min (médiane 70). Lee (PMID 17881544) :629 épisodes monomicrobiens,89,7 % avec deux cultures / 98,2 % avec trois, culture de 20 mL. Chiffres, populations et limites sont corrects ; pas de garantie individuelle déduite. |
| ESP30 — références précises/suisses | Énoncés SSC désormais individualisés par ancre 7, 25/26, 49, 87, 92 selon la question. Notices suisses 67023 et 60142 réellement téléchargées en direct et lues : stimulation bêta/inotropie/arythmies pour noradrénaline ; convulsions à doses élevées ou insuffisance rénale pour pipéracilline/tazobactam. DailyMed n’est plus leur seule preuve. |
| ESP31 — SOFA | Le nom d’origine Sepsis-related est ajouté, conformément à Singer (PMID 26903338) « Sequential [Sepsis-related] Organ Failure Assessment ». Score opérationnel et cause de la dysfonction restent distingués. |
| ESP32 — APROCCHSS | Les deux C sont séparés, and/for restent hors découpage. Le registre NCT00625209 confirme le titre développé ; le sigle publié APROCCHSS est conservé. Le champ acronym du registre contient APROCCHS, variante de métadonnée explicitement distinguée, sans correction supposée du nom publié. |

Ces six points sont **traités dans la proposition avec avis favorable du contrelecteur Codex** ; ils ne sont pas marqués comme un contre-audit Claude déjà terminé.

## Quatorze justifications

Les mécanismes et limites des14 entrées ont été relus. Les recherches animales ou cellulaires (Kim, Bose, Menguy, Schmidt, Van der Velden) ne sont plus présentées comme preuves cliniques directes du choc septique. La sélection résistante reste liée au risque précis et ne commande pas une couverture automatique. La gazométrie est distinguée du lactate sans décision de bicarbonate/épuration déduite. La toxicité rénale et le rythme restent contextualisés avec les notices suisses.

Les quatre compléments sont cohérents : solutés physiologiques/SMART versus essais de mortalité BaSICS/PLUS ; arythmies de SOAP II : 24,1 % contre 12,4 % avec population de chocs non exclusivement septiques ; essais EGDT distincts des recommandations de tests dynamiques ; retour veineux/charge ventriculaire dans la cohorte observationnelle Hamzaoui : 105 patients déjà remplis, sans bénéfice de survie universel.

Les sources solutés 2026, RecomGroup 44 (conditionnelle/modérée, exception traumatisme crânien), dynamique 49(conditionnelle/faible), vasopresseur 53(forte, haute pour comparaison dopamine), insuline 92(forte/modérée), XueBiJing 86(conditionnelle/très faible) ont été relues dans la **page officielle en direct**, avec force, certitude et remarques. La remarque glycémie 2021 est relue dans le texte primaire en cache. Les 14 textes cibles sont chacun uniques dans les HTML drafts et les 14 ancres présentes une fois ; leurs empreintes sont enregistrées dans le JSON. Les auteurs finalisant encore les HTML, ces liaisons devront rester conformes après leur dernière modification.

## Glossaire

Les 35 définitions sont relues ; les ajouts et modifications sont contrevérifiés dans ce périmètre. ProCESS/ARISE sont confirmés par les registres officiels NCT00510835/NCT00975793. ProMISe correspond au titre original PMID 26597979 et au plan PMID 24289513, avec résultat clinique PMID 25776532. A48.3 et les exclusions R57.8/A41.9 concordent au texte BfArM 2024. PCT est décrit comme biomarqueur qui ne confirme ni n’exclut seul le sepsis, avec usage d’arrêt conditionné ; XueBiJing n’est pas présenté comme autorisé en Suisse. Les définitions de résistance/exposition ne créent pas de prescription universelle nouvelle.

## Preuves et limites

Les résumés primaires PubMed ont été effectivement lus pour les chiffres et les modèles cités. Ils sont distingués de textes intégraux. Hamzaoui 2010 a été lu au texte intégral JATS d’EBI, SHA256 `0eafb5ffbaced218088d1343e0b6b23a78277c45f0e809b39bb495d253e2e4cf`. Notices suisses reçues : Labatec 60142SHA256 `100e3d38b1952a2be78631b525ce2ef7508b7486241b0cb8101f5289433991ca`, Sintetica 67023SHA256 `a0109dc89c990359d79e028cdd7d6665f679f4f02d6ed9655e8a58d88d97116b`. Les URL, hash et périmètres exacts sont détaillés dans le JSON.

**Les normes suisses artérielles manquantes d’ESP03 restent ouvertes**, voir [NORMES_GAZOMETRIE.md](NORMES_GAZOMETRIE.md). Une fenêtre de justification correcte ne ferme pas à elle seule ce manque dans le cours. Les définitions inchangées ne reçoivent pas une certification bibliographique exhaustive nouvelle. Aucun fragment déclaré achevé, aucune certification CIM-11, aucun code entrant exécuté ni injection par ce poste. Le nouveau paquet A41 corrigé devra être audité par Claude au SHA transmis avant la décision d’injection du coordinateur.

Lecture terminée à 2026-10-08T12:14:42.719738+00:00 UTC.
