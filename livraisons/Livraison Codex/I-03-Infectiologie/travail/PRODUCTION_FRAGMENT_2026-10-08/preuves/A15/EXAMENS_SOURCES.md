# A15 — préparation documentaire des examens (I-03-Infectiologie)

**État :** cadrage préalable, 8 octobre 2026 ; aucun cours définitif, traitement ou code suisse actuel déduit sans source. Aucun fichier du dépôt modifié.

## Libellé et limites du catalogue

Le référentiel **historique MEDINA** est la CIM-10-GM 2024. La [page BfArM A15–A19](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-a15-a19.htm#A15), lue directement, nomme A15.- : **« Tuberkulose der Atmungsorgane, bakteriologisch, molekularbiologisch oder histologisch gesichert »**, soit « tuberculose des organes respiratoires confirmée bactériologiquement, par biologie moléculaire ou histologiquement ». Le bloc A15–A19 inclut les infections à *Mycobacterium tuberculosis* et *M. bovis* ; il exclut notamment tuberculose congénitale, séquelles et pneumoconiose associée.

| Sous-code BfArM 2024 | Portée exacte à vérifier lors de la rédaction |
| --- | --- |
| A15.0 | Tuberculose pulmonaire confirmée par **microscopie des expectorations**, avec ou sans confirmation par culture ou méthode moléculaire. |
| A15.1 | Tuberculose pulmonaire confirmée **seulement par culture**. |
| A15.2 | Tuberculose pulmonaire confirmée **histologiquement**. |
| A15.3 | Tuberculose pulmonaire confirmée par un autre procédé ou un procédé non précisé ; le BfArM inclut explicitement la **confirmation moléculaire**. |
| A15.4 | Tuberculose des ganglions **intrathoraciques** confirmée. |
| A15.5 | Tuberculose du larynx, de la trachée ou des bronches confirmée. |
| A15.6 | Pleurésie tuberculeuse confirmée. |
| A15.7 | Tuberculose **primaire** des organes respiratoires confirmée. |
| A15.8 | Autre tuberculose respiratoire confirmée ; comprend médiastin, nez, sinus et nasopharynx. **Sous-code présent dans les éditions officielles BfArM et OFS 2024, omis dans l’inventaire I-03 local.** |
| A15.9 | Tuberculose respiratoire confirmée, localisation non précisée. |

L’inventaire local I-03 (`docs/collaboration/reviews/2026-10-08/REPRISE_FRAGMENTS/INVENTAIRE_I03.json`) n’est pas le catalogue officiel : il passe de A15.7 à A15.9 et déclare neuf sous-codes au lieu de dix. Son libellé français d’A15.9 dit « par biologie moléculaire **et** histologique » ; cette rédaction figure aussi dans la [version française officielle OFS de la CIM-10-GM 2024, p. 8/PDF 18](https://dam-api.bfs.admin.ch/hub/api/dam/assets/32686249/master), bien que le BfArM allemand emploie « oder » (« ou »). Il ne faut donc pas qualifier ce « et » d’erreur de copie locale. Ajouter A15.8 à l’inventaire dans le processus de gouvernance, sans éditer ce catalogue pendant cette mission. **A16** est la catégorie respiratoire *non confirmée* bactériologiquement/moléculairement/histologiquement ; les autres localisations ou formes disséminées du bloc relèvent d’autres catégories A17–A19. Le code A15 ne se substitue pas au **diagnostic clinique** et une définition de cas OFSP de surveillance ne dicte pas à elle seule le sous-code exact. L’[OFS](https://www.bfs.admin.ch/bfs/fr/home/statistiques/sante/nomenclatures/medkk.html) confirme que la CIM-10-GM est utilisée en Suisse, mais la page BfArM **2024** ne certifie pas le millésime de facturation suisse **2026**.

## Sources primaires réellement consultées

1. **Suisse — OFSP et Ligue pulmonaire suisse**, [*Tuberculose en Suisse : guide à l’usage des professionnels de la santé*, V1.2024](https://www.bag.admin.ch/dam/fr/sd-web/fPW7HAdyOiZ0/tuberkulose-handbuch.pdf), PDF intégral de 63 pages, notamment chapitre 3.3–3.4, pp. 15–16, et chapitre 6.1–6.3, pp. 31–34. La [Ligue pulmonaire](https://www.liguepulmonaire.ch/centre-de-competence-tuberculose/directives) le publie comme édition d’octobre 2024. La Société suisse d’infectiologie figure parmi les organisations participantes ; la recherche dans les pages SSI accessibles n’a pas fait apparaître de recommandation SSI autonome portant ce titre, donc ne pas inventer un lien SSI tuberculose.
2. **Suisse — OFSP**, [*Guide de la déclaration obligatoire. Maladies infectieuses et agents pathogènes 2026*](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf), fiche « Tuberculose », pp. **116–117**, texte intégral lu.
3. **Europe — ECDC**, [*Handbook on tuberculosis laboratory diagnostic methods in the European Union*, mise à jour 2026](https://www.ecdc.europa.eu/sites/default/files/documents/handbook-tuberculosis-lab-diagnostics-2026.pdf), PDF intégral consulté, notamment introduction et chapitres consacrés aux tests immunologiques, à la microscopie, aux cultures, aux méthodes moléculaires et à la sensibilité/résistance. Il s’agit d’un **manuel de laboratoire européen**, pas d’une règle suisse d’isolement ou de déclaration.
4. **Nomenclature — BfArM**, [CIM-10-GM 2024, bloc A15–A19](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-a15-a19.htm#A15), page officielle lue.

## Périmètre clinique utilisable, sans vignette inventée

Le guide suisse, chapitre 3.3–3.4, décrit une suspicion fondée sur **contexte épidémiologique, symptômes, examen et imagerie**, sans signe pathognomonique. Une toux avec expectoration, des symptômes généraux ou une image thoracique peuvent conduire au bilan, mais l’imagerie seule ne distingue pas activité, inactivité ou séquelle. La radiographie thoracique ou une tomodensitométrie adaptée précède l’échantillonnage ; une image compatible appelle des examens microbiologiques. Le chapitre 6 distingue les prélèvements respiratoires d’une tuberculose pulmonaire des prélèvements de ganglions intrathoraciques, de plèvre ou d’autres sites. Le futur cours A15 doit couvrir les **organes respiratoires confirmés**, sans absorber les formes non confirmées ou extrapulmonaires distinctes.

Pour une suspicion pulmonaire, chapitre 6.2 : premier échantillon d’expectoration sur place pour amplification directe, puis second échantillon selon la procédure décrite ; chapitre 6.3 : microscopie, amplification et culture remplissent des rôles différents. La microscopie est une preuve présomptive de forte charge mais ne distingue pas à elle seule le complexe tuberculeux des mycobactéries non tuberculeuses ; l’amplification identifie rapidement des acides nucléiques, la culture augmente la sensibilité et permet des tests phénotypiques de sensibilité. Un résultat moléculaire peut rester positif après traitement et **ne prouve pas à lui seul la viabilité ni la guérison**. Ces faits préparent l’enseignement, sans imposer encore un algorithme individuel hors cas.

Le guide suisse, chapitre 6.1, est explicite : **IGRA et test cutané ne prouvent pas une tuberculose active** ; un résultat positif peut refléter une réponse immunitaire antérieure, et un résultat négatif n’exclut pas la maladie. Ils ne doivent donc pas être présentés comme la confirmation d’A15. L’OFSP 2026, fiche tuberculose, exclut expressément la déclaration d’un simple diagnostic ou traitement d’**infection tuberculeuse** fondé sur TCT/IGRA.

## Déclaration suisse : à distinguer du codage et du diagnostic

Selon l’[OFSP 2026, fiche 58 « Tuberculose », pp. 116–117](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf) :

| Déclarant | Déclencheur résumé fidèlement | Délai / destinataire |
| --- | --- | --- |
| Médecin | Début d’un traitement par au moins trois antituberculeux, mise en évidence du complexe tuberculeux, ou découverte fortuite répondant aux critères de la fiche. **Pas** de déclaration du seul TCT/IGRA positif. | **1 semaine**, médecin cantonal. |
| Laboratoire | Résultat positif par culture, analyse de séquences/PCR ou microscopie ; communiquer aussi les résultats de résistance de première intention demandés dans la fiche, et signaler un résultat initialement positif non confirmé ensuite par culture. | **24 heures**, OFSP. |

Les isolats accompagnés du résultat de résistance à la rifampicine sont envoyés au Centre national des mycobactéries à Zurich, selon la fiche. **Nuance majeure :** la fiche OFSP classe ses cas de surveillance selon ses critères cliniques et de laboratoire ; une PCR seule peut y être un critère de *cas probable*, tandis qu’A15.3 du catalogue historique inclut une tuberculose pulmonaire moléculairement confirmée. Ne pas présenter « cas probable OFSP » et « A15 interdit » comme une équivalence automatique. Le statut clinique, les règles de codage et la surveillance répondent à trois questions distinctes.

## Questions d’examens à résoudre avant rédaction du cours

1. **Quelle présentation et quel site ?** Interroger durée, signes respiratoires et généraux, exposition, immunodépression, puis examiner et réaliser l’imagerie appropriée ; identifier poumon, voies aériennes, ganglions intrathoraciques ou plèvre. Source suisse : guide 2024, chap. 3.3–3.4 et 6.1.
2. **Quelle preuve microbiologique est disponible, sur quel échantillon ?** Expectoration spontanée ou induite, puis prélèvement bronchique ou tissulaire si indiqué ; distinguer qualité et nombre d’échantillons. Guide 2024, chap. 6.2–6.3.
3. **Que prouve chaque résultat ?** Frottis positif = bacilles acido-résistants sans identification d’espèce ; amplification du complexe = ADN détecté avec limites de viabilité ; culture = isolement et sensibilité. Une imagerie compatible ou un IGRA positif ne constituent pas à eux seuls la confirmation d’A15. Guide 2024, chap. 3.4 et 6.1–6.3 ; ECDC 2026 pour méthodes.
4. **Résistance ?** Vérifier résultats de résistance rifampicine et autres médicaments selon laboratoire et déclaration OFSP ; ne pas convertir « rifampicine non détectée résistante » en sensibilité universelle. Guide 2024, chap. 6.3 ; OFSP 2026, p. 116. Aucune prescription ou dose dans cette préparation.
5. **Que faire d’un résultat négatif si la suspicion demeure ?** Prévoir réévaluation clinique, échantillonnage complémentaire ou autre diagnostic selon site et imagerie. Le manuel suisse discute notamment bronchoscopie/biopsie si résultats directs négatifs mais image suspecte. Ne pas écrire une règle générale d’exclusion par une seule PCR négative. Guide 2024, chap. 6.2.
6. **Qui déclare, quoi et quand ?** Séparer médecin (1 semaine), laboratoire (24 h) et absence de déclaration du seul test d’infection tuberculeuse. OFSP 2026, pp. 116–117.

**Avant le cours final :** fixer une vignette clinique commune sans résultat fabriqué, vérifier les règles de codage suisse du millésime applicable, corriger l’inventaire A15.8, puis rattacher chaque décision à un passage primaire suisse daté. Aucun schéma thérapeutique ou posologie n’a été préparé ici.
