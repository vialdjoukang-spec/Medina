# Complément primaire PCT — A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

8 octobre 2026 (Europe/Zurich). Sources humaines ciblées pour `audit_examens_sciences_pharmacologie-01`. **Deux études réellement lues soutiennent des contextes précis d’élévation. Aucun nouveau seuil ni clôture externe.**

## Après chirurgie cardiaque sous CEC

**Delannoy et coll., Critical Care 2009, DOI 10.1186/cc8166, PMID 19912638 / PMC2811936.** Cohorte prospective monocentrique de 32 adultes ASA III/IV à Lyon. Parmi eux, 11 étaient classés SIRS non septiques et 5 avaient un sepsis postopératoire documenté (toutes pneumonies). La PCT augmentait après CEC et ne séparait pas les pics des groupes septiques/non septiques dans ce petit échantillon. La classification finale reposait sur deux experts et les critères SIRS/infection documentée de 1991.

> In our study, we found that PCT was significantly increased after CPB but we found that this increase was significantly higher in SIRS group than in no SIRS group. However, PCT failed to discriminate between sepsis and non-septic SIRS patients in the present study.

Repères : Materials and methods / Study sample et Diagnosis of SIRS and sepsis ; Results ; Discussion / Study limitations. Limites : 32 patients, population opératoire sélectionnée, pas de standard diagnostique parfait, pas de généralisation hors CEC. L’article affiche les concentrations en ng/L ; le complément conserve une conclusion qualitative et n’invente aucune correction d’unité ni seuil de pic.

[Texte intégral public XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2811936/fullTextXML), HTTP 200. Cache `/tmp/a41-pct-PMC2811936.xml`, SHA-256 `fdf8dc947ed5fb7b3d8e7e2ad9a63edce3f214fc40827944edae2830d635a5b1`.

## Maladie rénale chronique surtout avancée

**Wu et coll., Journal of Clinical Laboratory Analysis, en ligne le 16 octobre 2019 / numéro de février 2020, DOI 10.1002/jcla.23065, PMID 31617251 / PMC7031592.** Étude cas-témoins chinoise : 361 patients rénaux et 119 témoins, 80,1 % des patients au stade 5. La PCT moyenne était 0,44 ±0,67 ng/mL contre 0,04 ±0,06 chez les témoins (Table 2).

> In order to exclude the existence of infection, all potential study participants were subjected to blood culture before enrollment, and only those who have a negative result were selected.

> The PCT level in CKD patients (0.44 ± 0.67 ng/mL) was significantly higher than that in healthy controls (0.04 ± 0.06 ng/mL).

Repères : §2.1, §3.1/3.2, Tables 1–2, §3.6 ROC et Discussion. Limites : hémocultures négatives sans exclusion exhaustive des infections ; majorité au stade 5 ; mécanismes d’inflammation/clairance seulement proposés. Le seuil ROC 0,075 distingue les patients rénaux des témoins sains : **il ne distingue pas infection/non-infection et ne doit pas devenir un seuil antibiotique.** La moyenne ne signifie pas que tous les patients dépassent 0,5 µg/L.

[Texte intégral public XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7031592/fullTextXML), HTTP 200. Cache `/tmp/a41-pct-PMC7031592.xml`, SHA-256 `e06008473c758a1152e64ea667ea15a48b6043c9e7a1c2ad3b61b47371b5bb56`.

## Proposition transmise à l’auteur C

Une élévation de la procalcitonine ne prouve pas une infection. Après une chirurgie cardiaque sous circulation extracorporelle, une petite cohorte prospective a observé une augmentation chez des adultes classés comme présentant une réponse inflammatoire non septique. Une étude cas-témoins a aussi retrouvé une PCT moyenne plus élevée chez des patients atteints de maladie rénale chronique, majoritairement au stade 5, sélectionnés avec hémocultures négatives. Ces contextes exigent une interprétation clinique et de la trajectoire ; ils ne donnent ni seuil universel ni indication antibiotique. Des hémocultures négatives n’excluent pas à elles seules toute infection.

Les extraits verbatim complets, populations, critères de sélection, unités et empreintes figurent dans COMPLEMENT_PCT.json. L’auteur C conserve l’écriture exclusive de ses candidats. Aucun HTML, canonique, glossaire, banque de justification ou Git n’a été modifié par ce complément.

Les deux XML sont persistés, empreintes vérifiées, sous `/workspace/medina-env/reprise-a41/sources/pathologie1/`. Les chemins sont consignés dans `persistent_cache` du JSON et le manifeste `ARCHIVAGE.json`.
