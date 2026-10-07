# Contrelecture ciblée — I71, I80 et Q21

**Remise exacte :** `8ce3e99a18b96f6e6774d3d00bc709655e7ccb84`. **Conclusion :** intégrer les propositions après application des corrections décrites ci-dessous et réconciliation des statuts et de la prose par Codex. Cette contrelecture ne certifie ni toutes les assertions de ces cours, ni leur complétude dans la CIM-11.

## Portée effectivement relue

| Cours canonique | HTML proposés | Blocs de différence inventoriés et relus |
|---|---:|---:|
| I71 — Anévrismes et dissections artérielles | 6 | 46 |
| I80 — Thrombose veineuse profonde et thromboses veineuses | 6 | 43 |
| Q21 — Cardiopathies congénitales de l’adulte | 11 | 166 |
| **Total** | **23** | **255** |

Les ajouts ont été lus avec leur contexte, notamment les mécanismes des fenêtres, les décisions diagnostiques, les doses et durées modifiées, les restrictions de fermeture des shunts, la prévention thrombotique du Fontan, les explications génétiques et les résumés. Le nombre de blocs est un inventaire textuel, **pas un nombre d’assertions validées**. Les sources primaires ont été recherchées pour les problèmes retenus ; toutes les statistiques et toutes les monographies du cours n’ont pas été revérifiées indépendamment.

La réception authentifiée et ses SHA sont consignées dans le dossier `RECEPTION_8CE3E99`. Les comparaisons utilisent les originaux de la remise et le canonique présent au moment de la revue. Les bases immuables `75505d8` sont disponibles pour la réconciliation par la racine.

## Corrections proposées

Les copies préparées contiennent **34 substitutions dans 15 HTML**. Les identifiants des substitutions correspondent exactement au manifeste scratch `latest_claude_8ce/review_I71_I80_Q21/CORRECTIONS.json`. Ce manifeste donne le texte avant/après, la justification, les sources primaires et les SHA256 de chaque original et de chaque copie adaptée.

| Fichier | Correction retenue | Preuve primaire |
|---|---|---|
| `I71_a.html` | Dater les estimations historiques de mortalité et retirer leur présentation comme progression horaire universelle ; garder l’urgence chirurgicale et la réponse du quiz. | [Harris et al., IRAD, 2022](https://pubmed.ncbi.nlm.nih.gov/36001309/) |
| `I71_a.html` | Le début brutal oriente vers une dissection sans exclure une cause coronarienne ; supprimer le mécanisme affirmant que l’ischémie myocardique s’installe nécessairement progressivement. | [Recommandation douleur thoracique AHA/ACC 2021](https://doi.org/10.1161/CIR.0000000000001029) |
| `I71_a.html` | Dans la seule cellule du tableau des maladies héréditaires, réserver les 40–45 mm à certaines formes de Loeys-Dietz ; préciser l’absence de seuil standard dans l’Ehlers-Danlos vasculaire et la décision individualisée. La ligne Marfan reste identique. | [ESC 2024, section 10.1.2.4](https://doi.org/10.1093/eurheartj/ehae179) |
| `I71_c.html` | Les 51 ans correspondent à une **survie médiane de cohorte**, variable selon le variant et le sexe, plutôt qu’à une espérance de vie moyenne individuelle. | [Pepin et al., 2014](https://pubmed.ncbi.nlm.nih.gov/24922459/) |
| `I71_pop.html` | Ne pas fonder la chirurgie sur la seule comparaison d’un taux annuel à un risque opératoire ponctuel ; prendre en compte l’horizon de surveillance. Harmoniser le seuil tubulaire : **au-delà de 52 mm**. | [ESC 2024, sections 9.2.2 et 9.2.5](https://doi.org/10.1093/eurheartj/ehae179) |
| `I80_a.html` | La disparition d’un facteur transitoire ne s’applique pas à l’âge, l’obésité et les varices figurant dans le même tableau. | [ASH 2020, facteurs de risque](https://doi.org/10.1182/bloodadvances.2020001830) |
| `I80_b.html` | Les anticoagulants directs évitent la surveillance de routine par INR ; ils ne dispensent pas du suivi biologique adapté. | [ASH 2018, gestion des anticoagulants](https://doi.org/10.1182/bloodadvances.2018024893) |
| `I80_a.html`, `I80_b.html` | Corriger uniquement la bibliographie EASL : le document sur les maladies vasculaires du foie cité est publié en 2016 ; celui de 2022 porte sur le saignement et la thrombose dans la cirrhose. Ne pas revendiquer une révision clinique splanchnique complète. | [Document vasculaire, 2016](https://pubmed.ncbi.nlm.nih.gov/26516032/) ; [document cirrhose, 2022](https://pubmed.ncbi.nlm.nih.gov/35300861/) |
| `I80_c.html`, `I80_pop.html` | Présenter le dosage anti-Xa comme conditionnel, y compris dans le Pareto ; retirer l’indication de routine pour toute obésité, insuffisance rénale ou grossesse et la cible universelle incertaine. | [ASH 2018, gestion](https://doi.org/10.1182/bloodadvances.2018024893) ; [ASH 2018, grossesse](https://doi.org/10.1182/bloodadvances.2018024802) |
| `I80_c.html` | Des antiphospholipides persistants seuls ne définissent pas le syndrome : leur interprétation exige un contexte clinique compatible. | [ACR/EULAR 2023](https://doi.org/10.1136/ard-2023-224609) |
| `I80_c.html`, `I80_pop.html` | En cas de thrombopénie induite par l’héparine, éviter la transfusion plaquettaire de routine ; conserver la possibilité de saignement actif **ou risque hémorragique élevé**. | [ASH 2018, recommandation 3.6](https://doi.org/10.1182/bloodadvances.2018024489) |
| `I80_pop.html` | La protamine neutralise **aussi partiellement l’anti-Xa** de l’énoxaparine ; l’explication ajoutée limitant son action à l’anti-IIa est fausse. | [Information officielle Lovenox, rubrique surdosage](https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020164s129lbl.pdf) |
| `I80_pop.html` | Distinguer le diagnostic de thrombose profonde pendant la grossesse de celui d’embolie pulmonaire : les D-dimères ont une place dans un algorithme de grossesse prospectivement validé, pas comme résultat isolé. | [van der Pol et al., 2019](https://doi.org/10.1056/NEJMoa1813865) |
| `I80_pop.html` | Retirer l’obligation de pleine dose chez **tout** cancer actif. Après au moins six mois, l’essai API-CAT 2025 étaye une réduction **de l’apixaban**, chez des patients sélectionnés avec thrombose proximale ou embolie ; ne pas généraliser aux autres molécules ou à tous les cancers. Le résumé de prolongation reprend cette restriction et présente la réduction comme une option conditionnelle, sans affirmer une équivalence générale des doses. | [Mahé et al., 2025](https://doi.org/10.1056/NEJMoa2416112) ; [ASH 2020, recommandation 22 et limites des essais](https://doi.org/10.1182/bloodadvances.2020001830) |
| `I80_pop_sciences.html` | Une thrombophilie sévère peut peser dans la décision ; elle ne fixe pas seule une durée indéfinie et une pleine dose. | [ASH 2023, décision de tester selon le contexte](https://doi.org/10.1182/bloodadvances.2023010177) |
| `Q21_a.html` | Un CD4 supérieur à 500/µL n’est pas un critère suffisant pour autoriser un vaccin vivant en cas de délétion 22q11.2. Conserver l’évaluation immunologique spécialisée et les critères conjoints propres au vaccin. | [Consensus immunologique 2023](https://doi.org/10.1007/s10875-022-01418-y) ; [AAP 2025](https://doi.org/10.1542/peds.2025-072717) |
| `Q21_b.html`, `Q21_c.html` | Distinguer les résistances favorables à l’opérabilité de la définition actuelle d’hypertension pulmonaire. Retirer les garanties de fermeture « sans risque » ; la fonction gauche et les autres critères restent essentiels. | [ESC 2020, CIA](https://doi.org/10.1093/eurheartj/ehaa554) ; [ESC/ERS 2022, définition](https://doi.org/10.1093/eurheartj/ehac237) |
| `Q21_b.html`, `Q21_d.html`, `Q21_pop6.html`, `Q21_pop7.html` | Mettre corps, pharmacologie, fenêtre et Pareto en cohérence avec la prévention thrombotique Fontan recommandée en 2025. L’agent dépend du risque ; l’abstention n’est plus présentée comme une option générale hors contre-indication. | [ACC/AHA 2025, Fontan](https://doi.org/10.1016/j.jacc.2025.09.006) |
| `Q21_pop6.html` | Préciser la portée Eisenmenger de l’anticoagulation conditionnelle citée dans le paragraphe « Patient cyanosé ». Chez un Fontan cyanosé, conserver la prévention propre au Fontan et l’évaluation du risque hémorragique. | [ESC/ERS 2022, cardiopathies congénitales avec hypertension pulmonaire](https://doi.org/10.1093/eurheartj/ehac237) ; [ACC/AHA 2025, Fontan](https://doi.org/10.1016/j.jacc.2025.09.006) |
| `Q21_b.html` | Remplacer l’impossibilité universelle de stimulation ventriculaire transveineuse par les contraintes d’accès ; la voie épicardique est fréquente, avec alternatives spécialisées pour certains patients. | [Étude primaire 2025, stimulation endocavitaire après Fontan](https://pubmed.ncbi.nlm.nih.gov/41333880/) |
| `Q21_d.html` | Le bosentan n’a pas aggravé la saturation moyenne pendant les 16 semaines de l’essai retenu ; ce résultat n’exclut pas tout risque individuel. | [BREATHE-5, 2006](https://pubmed.ncbi.nlm.nih.gov/16801459/) |
| `Q21_pop4.html` | Une clairance fécale **anormalement élevée** de l’alpha-1-antitrypsine étaye la perte protéique ; la simple présence dans les selles ne la prouve pas. | [Étude avec sujets normaux, 1990](https://pubmed.ncbi.nlm.nih.gov/2210245/) ; [méthode et valeurs de référence Mayo](https://www.mayocliniclabs.com/test-catalog/Overview/604982) |

Les ajustements de l’explication du quiz I71, du texte plaquettaire I80, du tableau vasculaire, des résumés anti-Xa et de prolongation et du périmètre de la cyanose évitent des contradictions entre les ajouts, le corps et les fenêtres. Ils ne changent ni les questions, ni les choix proposés, ni les réponses attendues. La contradiction du tableau vEDS signalée dans la première version du rapport est désormais corrigée ; les réserves numériques non vérifiées restent ouvertes.

**Gel complémentaire :** les six substitutions ajoutées au premier gel sont `i71-veds-seuil-tableau`, `i80-antixa-pareto`, `i80-dose-prolongee-resume`, `q21-fontan-cyanose-perimetre`, `i80-easl-annee-entete` et `i80-easl-reference-exacte`. Le manifeste régénéré a pour SHA256 `e0f0a62cc533c9567947fac8b9cd7e218194276c69451c584849cabb0d1288c8`. Le fichier scratch `FREEZE_CHECKS.json` consigne la revérification des SHA des 15 copies, la conservation des structures et l’identité de la ligne Marfan. La correction textuelle de l’ancien en-tête EASL ne remplace pas le statut canonique que la racine conserve.

## Glossaire TBX1 proposé hors manifeste

Le fichier reçu `latest_claude_8ce/glossary_q21.original.py` a pour SHA Git `ec0d1d672c54470c30a6ebc228de9c0d83d02e06`. Le seul changement substantiel concerne la définition de TBX1 ; une ligne vide terminale s’ajoute.

**Avis favorable à la fusion sélective du paragraphe TBX1.** L’expression dans le mésoderme, l’endoderme et l’ectoderme pharyngés est documentée ; l’influence sur la migration de la crête neurale est indirecte. Cette précision corrige le raccourci ancien. Les données viennent de modèles embryologiques et n’impliquent pas une expression directe dans la crête neurale.

Preuves : [Garg et al., 2001](https://pubmed.ncbi.nlm.nih.gov/11412027/), [Zhang et al., 2006](https://pubmed.ncbi.nlm.nih.gov/16914493/), [relation au second champ cardiaque, 2006](https://pubmed.ncbi.nlm.nih.gov/16556915/) et [signalisation ectodermique vers la crête neurale, 2009](https://pubmed.ncbi.nlm.nih.gov/19700621/). Aucun glossaire canonique n’a été modifié par cette contrelecture.

## Conservation technique et arbitrages

- Pour les **15 copies corrigées**, comparaison automatisée de chaque nom de balise et de chaque attribut avant/après : identité complète. Cela comprend `id`, `data-k`, `data-pop`, `data-title`, `data-ok`, attributs SVG et paramètres des questions. SVG et scripts sont identiques.
- Entre la proposition Claude et le canonique, aucun `id`, `data-k`, `data-pop`, `data-title` ou `data-ok` existant n’est supprimé dans les 23 fichiers. Les ajouts comprennent six fenêtres I71, six I80 et une Q21. Les SVG et scripts proposés sont identiques au canonique dans ce périmètre.
- L’arbitrage antérieur I71 est conservé : **tension** `T = P × r` et **contrainte** `σ = P × r / e`, avec les limites du modèle et le facteur quatre si rayon doublé et épaisseur divisée par deux. Le titre canonique de chaque cours demeure complet.
- La racine préserve les statuts canoniques et la correction de prose locale `I80_c.html` repérée par la réception. Les copies médicales partent des originaux exacts ; elles ne remplacent pas cette réconciliation.
- Aucun fichier canonique, moteur ou glossaire n’a été modifié. Seul ce rapport est committé par l’agent de revue ; la racine réalise l’injection, le build et les contrôles transversaux.

## Réserves explicites

1. Les chiffres de fréquence, mortalité, sensibilité et risque relatif ajoutés n’ont pas tous été confrontés à leur publication d’origine. Leur présence ne vaut pas certification numérique exhaustive. Certains sont historiques ou dépendent fortement du recrutement.
2. Les critères mWHO des grossesses, les cadres d’anticoagulation des localisations splanchniques et l’ensemble des adaptations rénales des monographies n’ont pas fait l’objet d’un audit indépendant exhaustif. L’attribution bibliographique EASL 2016/2022 est corrigée ; l’actualisation clinique complète selon la [nouvelle recommandation vasculaire EASL](https://pubmed.ncbi.nlm.nih.gov/41224629/), publiée en ligne en novembre 2025 puis dans le numéro de février 2026, reste à effectuer et n’est pas revendiquée dans les cours.
3. Les recommandations de thrombophilie citées comme ESVS 2021 demeurent datées ; l’ASH 2023 propose des exceptions conditionnelles après certains événements hormonaux ou transitoires non chirurgicaux. La contrelecture n’affirme pas que tous ces arbitrages ont été actualisés.
4. Les comparaisons statiques ne remplacent pas les tests d’injection ni la vérification de chaque fenêtre dans la plateforme. Ces contrôles relèvent du build et de la recette de la racine.
5. La nomenclature actuelle de ces sources est **CIM-10-GM 2024**. Ni ce rapport, ni les 23 propositions ne démontrent la couverture complète des catégories de la CIM-11 exigée par l’utilisateur.

La formulation de livraison doit rester « contrelecture ciblée et corrections appliquées », sans note autoattribuée ni mention de validation humaine exhaustive.
