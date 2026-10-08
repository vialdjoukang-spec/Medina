# Contre-audit médical de l’harmonisation v5

**Avis favorable avec deux réserves mineures, aucun blocage ni réserve majeure sur les phrases modifiées de I83 — Varices des membres inférieurs (C-01-Cardiologie).** La réserve majeure de la v4 est levée. Cet avis permet au coordinateur de décider l’intégration sélective du paquet figé après ses contrôles techniques indépendants ; il ne certifie ni l’intégralité médicale du chapitre, ni un fragment achevé, ni la couverture CIM-11.

Tête reçue : `d5b46aa2502c91517f7f80c8ac158f42605257e8`. Base comparée : `3dac92808b055e235ee6f57cfec8e283455a85ca`. Lot : `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83-HARMONISATION-5/`. Les sept HTML et le complément `glossary/i83.py` sont relus sur leurs différences avec cette base, y compris les corrections conservées depuis v2–v4. Depuis v4 `e17107a`, seul `I83_b.html` change. Le JSON contient chaque différence, les numéros de lignes et les empreintes manifestées ; les seize empreintes déjà conformes sont documentées dans la [réception](../A41_REPRISE_MULTIAGENT/RECEPTION.md).

## Décision et preuve principale

Aux lignes 108 et 126 de `chapters/I83/I83_b.html`, la v5 ne prescrit plus de surveiller toute thrombose profonde jusqu’à sa résolution. Elle distingue l’ARTE traitée jusqu’à rétraction du thrombus et la TVP découverte, dont la conduite dépend du siège, des symptômes et du risque d’extension, avec renvoi à **I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie)**. Le texte intégral SVS/AVF/AVLS2023, §11.4.2, dit : « For patients who receive anticoagulation for ARTE following endovenous ablation, treatment should be continued until the thrombus retracts. » Les §11.3.1–11.3.3 distinguent TVP distale, symptômes graves/risque d’extension et TVP proximale. La nouvelle séparation est correcte ; la règle d’imagerie sériée de deux semaines ne vaut pas pour toute TVP.

| Thème relu | Avis sur le delta |
| --- | --- |
| Écho-Doppler post-ablation | La divergence ESVS2022 R27 IIa C / SVS2023 §11.1 est exposée correctement : risque moyen asymptomatique après thermique, symptômes, haut risque et technique non thermique sont distingués. |
| ARTE/EHIT et anticoagulation | Classes II <50 %, III >50 %, IV occlusive ; ARTE symptomatique ou asymptomatique III/IV reçoit un anticoagulant oral direct, jusqu’à rétraction. Grades/consensus concordent. Le glossaire EHIT ne conserve plus l’ancienne discordance de classe III. |
| CEAP et perforante du cas | C2/C3/C4a/C4c correspondent aux signes décrits. R50 peut être envisagée IIb C pour C4b/C5/C6, et le cas sans C4b ni ulcère reste traité d’abord au niveau tronculaire. La graphie exacte `C2,3,4a,c (s)` du guide AVF n’a pas pu être certifiée ; classes et raisonnement sont concordants. |
| Reflux et position | Le seuil >1 s est désormais limité aux veines fémorale commune, fémorale et poplitée. Le résumé ne généralise plus à tout le réseau profond. Recherche debout et provocation adaptée concordent ; les seuils tibiaux/fémorale profonde ne sont pas explicités dans ce résumé, sans assertion contraire. |
| Pansements/cadexomère | Cicatrisation complète, pas délai. Norman2018 : 59 essais en réseau, comparaison argent/non adhérent de certitude modérée dans un réseau de faible certitude. O’Meara2014 : quatre essais comparatifs parmi onze essais de cadexomère, cicatrisation à 4–12 semaines, RR2,17 [1,30–3,60]. Source et endpoint corrigés. |
| Génétique | Fukaya2018 soutient HR1,74 et analyse mendélienne de hauteur ; nouvelles hypothèses de validité/pléiotropie/structure de population correctement explicitées, mécanisme conservé comme hypothèse. |
| Sciences microvasculaires | Kf = conductivité × surface ; formule classique simplifiée, inférence Kf/σ non directement mesurée dans la maladie veineuse, fer/fibrine et fibrose qualifiés. L’ensemble évite une chaîne causale universelle présentée comme démontrée. |
| Saignement/anticoagulation | L’élévation/compression est limitée au saignement qu’elle arrête ; persistance/retentissement hémodynamique entraîne l’urgence, avec interruption ou antagonisation au cas par cas. Non-interruption pour ablation thermique concorde avec ESVS R94 III C. Aucune nouvelle dose ajoutée. |
| Œdème sous amlodipine | Après remplacement et réévaluation, le résidu gauche oriente sans exclure d’autre cause. Attribution désormais conditionnelle, pas exclusive. |
| Renvoi différentiel | Le titre **I50 — Insuffisance cardiaque (C-01-Cardiologie)** est précisé ; contenu inchangé. |

## Deux réserves mineures précises, communicables à Claude

### I83-V5-MIN-01 — « réserve l’appellation » est trop exclusif

Fichier : `chapters/I83/I83_c.html:43`. Phrase : « l’ESVS réserve l’appellation de perforante pathologique à une perforante située sous un ulcère ouvert ou cicatrisé (classe C5 ou C6). »

L’ESVS §4.6.6 décrit un usage fréquent du terme près d’un ulcère ouvert ou cicatrisé : « Often, the term “pathological PVs” has been used… ». Son §2.3.1.1 emploie aussi ce terme pour des perforantes répondant aux critères de reflux/calibre, notamment dans une zone d’altérations cutanées. Il ne pose donc pas ici une exclusivité universelle C5/C6.

Remplacement proposé : « L’ESVS décrit notamment comme “perforantes pathologiques” celles situées près d’un ulcère actif ou cicatrisé (§4.6.6) ; il emploie aussi ce terme pour des perforantes répondant aux critères hémodynamiques et de calibre, en particulier dans une zone d’altérations cutanées (§2.3.1.1). Cette qualification ne suffit pas à poser une indication thérapeutique. »

**Pourquoi cette nuance ne bloque pas :** la suite distingue correctement l’indication R50 IIb C. Mme R. reste C4a/C4c sans C4b ni ulcère ; traiter d’abord le reflux tronculaire et réévaluer la perforante demeure la conduite proposée. Cette nuance descriptive n’annule ni la correction C4b ni la v5.

### I83-V5-MIN-02 — préciser « thermique » dans trois reprises statistiques

Les taux 1,4 % (EHIT II–IV, désormais ARTE) et 1,7 % (EHIT II–IV ou TVP) proviennent, dans le rationale SVS §11.1.1, de 52 études/16 398 patients ayant eu une **ablation thermique de la grande saphène**, avec surveillance dans le premier mois. `chapters/I83/I83_b.html:64` donne déjà correctement cette portée. La définition ARTE toutes techniques est correcte, mais ne suffit pas à généraliser ces deux taux.

| Fichier et ligne | Correction minimale proposée |
| --- | --- |
| `chapters/I83/I83_pop2.html:46` | Remplacer « Les ARTE de classes II à IV surviennent dans 1,4 % des ablations de la grande saphène, et l’ensemble ARTE II à IV ou thrombose profonde dans 1,7 % » par « Après ablation thermique de la grande saphène, les ARTE de classes II à IV surviennent dans 1,4 % des cas, et l’ensemble ARTE II à IV ou thrombose profonde dans 1,7 % ». |
| `chapters/I83/I83_pop2.html:123` | Remplacer « survient dans 1,4 % des ablations de la grande saphène » par « survient dans 1,4 % des ablations thermiques de la grande saphène ». |
| `glossary/i83.py:7` | Remplacer « surviennent après 1,4 % des ablations de la grande saphène » par « surviennent après 1,4 % des ablations thermiques de la grande saphène ». |

**Pourquoi cette nuance ne bloque pas :** les valeurs et la conduite sont concordantes dans leur population source ; l’ajout précise seulement la portée de reprises statistiques. Il ne change ni indication, ni dose, ni surveillance stratifiée, ni traitement de l’ARTE. Le corps thérapeutique donne déjà la précision correcte.

## Primaires réellement lus et limites

Le texte intégral SVS/AVF/AVLS2023 a été lu au [service officiel EuropePMC/EBI](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11523430/fullTextXML), JATS 708 520 octets, SHA256 `46a0f5039bd083595e8d63ad1c0b7e30c6a2d95a4845cea4104a0469187dabd3`. ESVS2022 a été lu dans le [PDF primaire diffusé par ORBi](https://orbi.uliege.be/handle/2268/288479), 4 413 151 octets, SHA256 `cb07d1f152de0b30ec674607d333f0ae016f952f4d778c60fe892ee0216bc783`. R27, R50, R94 et les paragraphes concernés sont vérifiés au texte, indépendamment du producteur. Le passage conservé de `I83_pop2.html:47` sur l’occlusion de la veine fémorale commune est également vérifié : « When thrombus occludes the CFV (EHIT class IV), treatment by therapeutic anticoagulation is recommended. » Cette limite documentaire annoncée par le producteur est donc levée pour ce passage précis dans notre contrelecture.

Les résumés primaires EuropePMC/PubMed de O’Meara2014 (PMID24408354, CD003557.pub5), Norman2018 (PMID29906322, CD012583.pub2), Fukaya2018 (PMID30566020), Levick/Michel2010 (PMID20200043), Raffetto/Khalil2008 (PMID18453484) et Lurie2020 (PMID32113854) ont été lus. Les chiffres Cochrane et génétiques modifiés sont directement présents dans ces résumés. Ils ne sont pas présentés comme des téléchargements des textes intégraux correspondants. Le chiffre de 212 participants et les assertions négatives OFSP inchangées ne sont pas recertifiés.

Un HTTP200 sur PMC a parfois renvoyé une page CAPTCHA, et l’URL ESVS du producteur une page HTML : ces réponses ne sont pas prises pour des primaires. Le guide AVF de notation a répondu 403. Ces limites ne retirent pas les textes primaires effectivement obtenus via EBI/ORBi. Les preuves suisses et `I83_pop4.html`, inchangés ici, restent rattachés aux [audits antérieurs](../I83_DECISION_0974D85/DECISION.md), pas à une certification nouvelle dans ce périmètre.

Aucun code entrant exécuté, aucune source canonique ou mutation Git, aucune injection par ce poste. Les contrôles du producteur restent distincts des contrôles indépendants du coordinateur. Tout SHA postérieur devra être comparé séparément. Le complément de glossaire doit être inclus explicitement dans une éventuelle intégration sélective ; il est hors manifeste chapters-only.

Date de clôture de cette lecture : 2026-10-08T11:49:09.049791+00:00 UTC.
