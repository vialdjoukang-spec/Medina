# A04 — audit de nomenclature et des examens (I-03-Infectiologie)

**État :** audit documentaire en lecture seule, 8 octobre 2026. Aucun fichier du cours ni du dépôt MEDINA modifié. Les propositions ci-dessous demandent une contextualisation clinique dans le futur cours ; elles ne constituent pas un diagnostic individuel.

## 1. Périmètre du code

Le catalogue historique utilisé dans MEDINA est la **CIM-10-GM 2024** du BfArM. La rubrique A04.- est « autres infections intestinales bactériennes » (`Sonstige bakterielle Darminfektionen`) ; elle exclut les intoxications alimentaires classées ailleurs et l'entérite tuberculeuse A18.3. Son extension exacte est la suivante ([BfArM, bloc A00–A09, A04](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-a00-a09.htm#A04), consulté le 08.10.2026) :

| Code | Libellé officiel rendu en français | Limite utile |
| --- | --- | --- |
| A04.0 | Infection intestinale due à *E. coli* entéropathogène | EPEC ; n'assimile pas tous les *E. coli* détectés. |
| A04.1 | … *E. coli* entérotoxinogène | ETEC. |
| A04.2 | … *E. coli* entéroinvasif | EIEC. |
| A04.3 | … *E. coli* entérohémorragique | EHEC, dont STEC/VTEC dans la terminologie de surveillance OFSP. |
| A04.4 | Autres infections intestinales dues à *E. coli* | Inclut l'entérite à *E. coli* sans autre précision ; n'est pas un synonyme d'A04.3. |
| A04.5 | Entérite due à *Campylobacter* | Distincte des salmonelloses et shigelloses. |
| A04.6 | Entérite due à *Yersinia enterocolitica* | Le BfArM exclut la yersiniose extra-intestinale A28.2. |
| A04.7- | Entérocolite due à *Clostridium difficile* | **Libellé de codage historique** ; la SSI 2026 emploie le nom taxonomique *Clostridioides difficile*. Inclut colite pseudomembraneuse. Une récidive codée exige en plus U69.40!. |
| A04.70 / .71 | Sans mégacôlon, respectivement sans / avec autre complication d'organe | Pour .71, ajouter le(s) code(s) de complication selon BfArM. |
| A04.72 / .73 | Avec mégacôlon, respectivement sans / avec autre complication d'organe | Pour .73, ajouter le(s) code(s) de complication. |
| A04.79 | Entérocolite à *C. difficile*, sans précision | Ne décrit ni la sévérité ni une récidive. |
| A04.8 / .9 | Autre infection intestinale bactérienne précisée / non précisée | Éviter d'inférer un agent précis. |

**Frontières à montrer sobrement :** Salmonella non typhique relève d'A02.-, Shigella d'A03.-, la fièvre typhoïde/paratyphoïde d'A01.- ; A05.- recouvre certaines intoxications alimentaires bactériennes et exclut explicitement les infections à *E. coli* A04.0–A04.4, à *C. difficile* A04.7- et à Salmonella A02.- ([BfArM, même bloc, A01–A05](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-a00-a09.htm)). A04 n'est donc ni « toutes les diarrhées bactériennes », ni un synonyme de CDI. Les autres causes virales, parasitaires ou non infectieuses d'une diarrhée ne doivent pas être absorbées par A04.

**Rattachement MEDINA :** le catalogue frontend courant affecte A04 au fragment T1 = I-03-Infectiologie. Un inventaire JSON historique le conserve sous S03 ; traiter cela comme décalage documentaire à corriger dans l'inventaire, sans déplacer le cours vers l'ancienne spécialité. Source interne : `fragment_surface.frontend_catalog(Path('.'))[1]['A04'] == 'T1'`, signalement du coordinateur du 08.10.2026, et `docs/collaboration/FRONTENDS_2026-10-08.md`.

## 2. Décisions diagnostiques étayées

| Question à poser dans le cours | Donnée réellement étayée | Conséquence et limite |
| --- | --- | --- |
| Y a-t-il une maladie à *C. difficile* ou seulement une détection ? | La [SSI, recommandations CDI, version 4.0 du 27.01.2026, « Definitions », pp. 2–4 et fig. 1 p. 12](https://zenodo.org/records/18503894/files/SSI_2026_CDI.pdf?download=1) associe tableau clinique compatible (dans ce texte, diarrhée définie comme **>3 selles molles Bristol 6–7/24 h**, ou iléus), preuve microbiologique, idéalement toxines libres, et absence d'autre diagnostic. | Ne pas présenter NAAT/PCR positif isolé comme preuve d'entérocolite active. Il peut traduire une colonisation. Le seuil `>3` est la formulation exacte de la SSI, à conserver sans le substituer par un autre seuil de mémoire. |
| Quel échantillon et quel algorithme CDI ? | SSI 2026 pp. 3–4 : dépistage sensible GDH puis toxines A/B par immunoessai ou immunochromatographie ; NAAT en élément d'algorithme ou seule **chez les symptomatiques**, avec réserve explicite de colonisation ; écouvillon rectal par NAAT possible en cas d'iléus après information du laboratoire. La SSI précise conservation à 4 °C si analyse dans 72 h, à −80 °C au-delà, et déconseille −20 °C pour les toxines. | Associer résultat et syndrome. Ne pas prescrire de prélèvement rectal comme routine de diarrhée. La culture toxinogène et le test de cytotoxicité sont des références méthodologiques mais peu utilisés en routine selon SSI. |
| Que dit la directive européenne de diagnostic ? | [ESCMID, Crobach et al., *Clin Microbiol Infect* 2016;22 Suppl 4:S63–S81, DOI 10.1016/j.cmi.2016.03.010, résumé PubMed/Europe PMC](https://doi.org/10.1016/j.cmi.2016.03.010) : aucun test commercial unique n'a une valeur prédictive positive suffisante si la prévalence est basse ; algorithme en deux étapes ; GDH/NAAT/culture toxinogène positifs avec toxines libres négatives exigent une évaluation clinique pour séparer infection et portage. | Comparaison européenne cohérente avec la réserve suisse. **Limite de lecture :** le texte intégral européen 2016 n'était pas accessible ici ; seule la notice avec résumé a été consultée. Ne pas lui attribuer de sous-algorithme ou de seuil non visible dans ce résumé. La source suisse intégrale fonde la proposition locale. |
| Qu'est-ce qui distingue EHEC/STEC des autres *E. coli* d'A04 ? | [OFSP, Guide 2026, « Infection à *E. coli* entérohémorragique », pp. 55–56](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf) : critères microbiologiques = isolement de STEC/VTEC, détection des gènes **stx1/stx2** par PCR, ou détection des shigatoxines libres par ELISA. | Pour une décision de surveillance EHEC, un résultat « *E. coli* positif » sans facteur de virulence ni caractérisation pertinente ne suffit pas. Le guide donne une **définition de cas**, pas un algorithme universel de prescription d'un panel multiplex. |
| Comment lire les tests des autres agents A04 ? | [OFSP 2026, « Campylobactériose », pp. 14–15](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf) : culture ou PCR pathogène dans prélèvement clinique. | La définition de surveillance n'établit pas qu'une coproculture/NAAT soit systématique pour toute diarrhée. Envisager selon contexte et indication clinique documentée. A04.6 (*Y. enterocolitica*) n'a pas de fiche spécifique dans ce guide OFSP consulté ; ne pas inventer un test « suisse recommandé » ni une obligation de déclaration. |
| Quels éléments distinguent une forme compliquée de CDI ? | SSI 2026 « Definitions », p. 4 : hypotension, choc septique, lactate élevé, iléus, mégacôlon toxique, perforation, détérioration fulminante attribuables à CDI ; la recommandation donne aussi des critères de forme sévère. | Le bilan et l'imagerie servent à apprécier les complications si signes cliniques. Ne pas conclure à une complication d'organe ni au sous-code .71/.73 par le seul test de selles. Ne pas reprendre les unités du seuil leucocytaire sans vérification éditoriale (le PDF indique `cells/mL`, formulation possiblement erronée). |

**Point de critique de source :** le PDF SSI 2026, p. 4, introduit une « approche européenne 2023 » mais sa référence `[4]` est le texte ESCMID de **traitement** de 2021. Il ne faut ni dater cette recommandation diagnostique « ESCMID 2023 » ni l'étayer par ce renvoi contradictoire. Les éléments d'algorithme SSI explicitement formulés pp. 3–4 restent utilisables comme position de la société suisse ; la référence diagnostique européenne vérifiée ici est Crobach 2016, au niveau de son résumé.

## 3. Déclarations et laboratoire en Suisse

Le [Guide OFSP 2026](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf) est un guide de **surveillance**, à ne pas transformer en protocole thérapeutique ou en indication de test chez chaque patient. Les fiches lues donnent :

| Entité | Médecin | Laboratoire | Localisation source |
| --- | --- | --- | --- |
| Campylobactériose A04.5 | Aucune déclaration individuelle pour le moment. | Tous résultats positifs par culture ou PCR, à l'OFSP dans les **24 h** ; espèce si connue ; isolats au NENT sur demande. | Guide, pp. 14–15. |
| EHEC/STEC A04.3 | Résultat de laboratoire positif au médecin cantonal dans les **24 h**. | Résultat positif par culture, analyse de séquences ou antigène à l'OFSP dans les **24 h** ; type de toxine si connu ; isolats au NENT sur demande. | Guide, pp. 55–56. |
| Salmonellose A02.-, hors périmètre A04 | Aucune déclaration individuelle pour le moment. | Culture ou PCR positive à l'OFSP dans les **24 h** ; isolats non Enteritidis au NENT, Enteritidis sur demande. | Guide, pp. 100–101. |
| Shigellose A03.-, hors périmètre A04 | Aucune déclaration individuelle pour le moment. | Culture ou PCR positive à l'OFSP dans les **24 h** ; tous isolats au NENT. Pour la **classification des cas publiés**, culture = confirmé, PCR seule = probable (pp. 102–103) : ne pas confondre notification de résultat positif et catégorie « confirmé ». | Guide, pp. 102–103. |
| *C. difficile* A04.7- | Pas de fiche individuelle *C. difficile* identifiée dans le Guide 2026 consulté. **Des flambées hospitalières exceptionnelles** impliquant notamment cet agent sont déclarables par l'hôpital au médecin cantonal dans les **24 h** après confirmation des critères ; pas de déclaration du laboratoire dans cette fiche. | Ne pas généraliser la règle de flambée à chaque CDI isolée. | Guide, « Flambée exceptionnelle en milieu hospitalier », p. 7. |
| *Y. enterocolitica* A04.6 et EPEC/ETEC/EIEC A04.0–.2 | Aucune fiche spécifique trouvée dans le Guide 2026 consulté ; seule la peste à *Y. pestis* y figure sous le nom *Yersinia*. | La non-présence dans ce guide ne prouve pas l'absence de toute exigence cantonale ou de signalement de flambée. | Guide, sommaire et index intégral ; portée négative limitée à ce document. |

## 4. Garde-fous pour la rédaction A04

1. Faire suivre le **syndrome et le contexte** par le test indiqué et sa limite d'interprétation. Ne pas raconter A04 comme un seul tableau ou un seul panel de selles : la codification rassemble des agents et mécanismes distincts.
2. Garder deux branches lisibles : **CDI** (syndrome compatible → toxines/algorithme suisse → écarter autre cause → gravité) et **autres infections intestinales** (recherche d'agent selon le contexte → type de preuve microbiologique → obligations OFSP propres à l'agent). Pour EHEC, expliciter stx1/stx2 ou toxine ; pour Campylobacter, culture/PCR reconnues par OFSP.
3. Ne pas convertir la présence d'un organisme ou d'un gène dans un panel multiplex en preuve automatique de causalité, de viabilité, de sensibilité antibiotique ou de code A04 précis. **La SSI établit explicitement ce risque pour NAAT *C. difficile*.** Pour les autres agents, une règle de panel multiplex plus détaillée exige encore une source primaire spécifique.
4. Ne pas importer ici de dose, traitement ou seuil d'indication de coproculture sans avoir lu la recommandation suisse correspondante. Cet audit cible la nomenclature et le diagnostic ; la SSI 2026 devra être relue séparément pour le traitement, et chaque produit requerra sa FI suisse.

## 5. Sources effectivement consultées et limites

- **BfArM**, CIM-10-GM **2024**, [bloc A00–A09, A04 et A05](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-a00-a09.htm#A04), page officielle HTML lue le 08.10.2026. Référence du **catalogue historique MEDINA**, sans prétendre établir par elle seule la version de facturation suisse en vigueur en 2026.
- **SSI**, Guery et al., [*2026 Swiss Society of Infectious Diseases recommendations for Clostridioides difficile Infection*, version étendue 4.0, 27.01.2026](https://zenodo.org/records/18503894/files/SSI_2026_CDI.pdf?download=1), PDF intégral de 35 pages lu le 08.10.2026 ; sections « Definitions », « Microbiological methods », fig. 1. Consensus suisse endossé par la SSI ; les données de diagnostic concernent une maladie suspectée, non le dépistage universel de portage.
- **OFSP**, [*Guide de la déclaration obligatoire. Maladies infectieuses et agents pathogènes 2026*](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf), PDF intégral consulté le 08.10.2026 ; pp. 7, 14–15, 55–56, 100–103. Les délais et destinataires cités sont ceux de ces fiches 2026 ; vérifier leur éventuelle modification lors de la publication du cours.
- **ESCMID**, Crobach et al., [mise à jour diagnostique 2016, DOI 10.1016/j.cmi.2016.03.010](https://doi.org/10.1016/j.cmi.2016.03.010), **résumé intégral de la notice** Europe PMC/PubMed lu le 08.10.2026, texte intégral non obtenu ; appui limité aux conclusions exprimées dans ce résumé.
