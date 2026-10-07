# Contrelecture ciblée de la remise Claude b6db50c — I00, I30, I33 et I34

Remise relue : `b6db50cb2911fcbe0b09e64b79df03aab294e3df`. Date de réception et de révision : 7–8 octobre 2026. Les originaux reçus restent dans `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/` ; les corrections décrites ci-dessous sont des propositions séparées. Aucune source canonique n’a été modifiée par cette contrelecture.

## Conclusion et portée

**Treize corrections ciblées sont proposées sur onze fichiers HTML avant injection.** Elles portent sur les formulations de décision nouvelles, les contradictions introduites ou renforcées par leur justification, et une précision physiopathologique. Les statuts canoniques « Révision des justifications en cours » doivent être préservés : la remise réintroduit des notes automatiques et une mention d’« audit indépendant en deux passes », qui ne constituent pas une certification médicale.

L’inventaire comparatif porte sur 38 HTML et 488 blocs modifiés (102, 140, 133 et 113 selon le cours). Ces nombres sont des unités techniques de différence, **pas un décompte exhaustif d’affirmations médicales validées**. La relecture a visé les ajouts, les fenêtres modifiées, les tableaux de prescription, la cohérence de leurs limites et les données structurelles. La recherche primaire a été concentrée sur les corrections et quelques chiffres nouvellement ajoutés, notamment l’étude de Kamblock de 2003 ; elle ne certifie pas toutes les références citées par Claude, toutes les doses ni toutes les indications des quatre cours.

| Cours canonique | HTML reçus | Blocs modifiés inventoriés | Fenêtres natives | SVG |
|---|---:|---:|---:|---:|
| I00 — Rhumatisme articulaire aigu | 10 | 102 | 69 → 71 | 15 |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | 10 | 140 | 78 → 79 | 15 |
| I33 — Endocardite infectieuse | 8 | 133 | 84 → 86 | 13 |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | 10 | 113 | 103 → 107 | 15 |

Les neuf fenêtres supplémentaires sont `i00-bpg-vagal`, `i00-crp-vs`, `i30-bilan`, `i33-fongique`, `i33-saureus`, `i34-anticoag-valve`, `i34-avk-interact`, `i34-congestion-renale` et `i34-marqueurs-imp`. Leur ajout contribue à expliquer les décisions, sans établir à lui seul la justification de toute assertion restante.

## Corrections proposées

| N° | Fichier | Motif précis | Sources consultées |
|---|---|---|---|
| 01 | `chapters/I00/I00_a.html` | Le critère OMS définit les patients pouvant recevoir une dose test surveillée ; il ne démontre pas une tolérance aux injections en cas d’allergie déclarée. | [source 1](https://www.ncbi.nlm.nih.gov/books/NBK609692/) ; [source 2](https://www.medicines.org.uk/emc/product/11043/smpc) |
| 02 | `chapters/I00/I00_b.html` | L’argument ajouté transforme une dose de prophylaxie en garantie de sécurité universelle, contraire aux précautions et adaptations du RCP consulté. | [source 1](https://www.medicines.org.uk/emc/product/11043/smpc) |
| 03 | `chapters/I00/I00_pop5.html` | Des études de patients avec exanthème sous amoxicilline pendant une mononucléose ont documenté une sensibilisation réelle ; la négation générale est fausse. | [source 1](https://pubmed.ncbi.nlm.nih.gov/25784943/) ; [source 2](https://pubmed.ncbi.nlm.nih.gov/39282619/) |
| 04 | `chapters/I00/I00_pop5.html` | L’induction enzymatique ne rend pas toutes les méthodes hormonales inefficaces ; le choix de méthode doit être individualisé. | [source 1](https://www.medicines.org.uk/emc/product/1041/smpc) |
| 05 | `chapters/I30/I30_a.html` | L’ajout justifie le collapsus des deux cavités droites en diastole alors que les phases typiques diffèrent ; préserver la précision échographique. | [source 1](https://pubmed.ncbi.nlm.nih.gov/6499153/) ; [source 2](https://assets.escardio.org/Assets/Presentations/OTHER2010/EAE-echo-emergency-belgrade/cardiac-tamponade-echo-guided-pericardiocentesis-pinto.pdf) |
| 06 | `chapters/I30/I30_b.html` | Le tableau ajoute une posologie utilisable en insuffisance rénale sévère, contradictoire avec la contre-indication suisse décrite plus loin ; la décision doit être visible au point de prescription. | [source 1](https://compendium.ch/fr/product/index/1481648) |
| 07 | `chapters/I33/I33_a.html` | Les entérocoques ne doivent pas être enseignés comme appartenant à la flore cutanée ; les deux groupes sont visés dans le contexte du TAVI. | [source 1](https://academic.oup.com/eurheartj/article/44/39/3948/7243107?searchresult=1) |
| 08 | `chapters/I33/I33_d.html` | Même assimilation erronée des entérocoques à la flore cutanée dans le volet thérapeutique. | [source 1](https://academic.oup.com/eurheartj/article/44/39/3948/7243107?searchresult=1) |
| 09 | `chapters/I33/I33_b.html` | Le mécanisme ajouté généralise abusivement la positivité et risque de banaliser un prélèvement unique à S. aureus, souvent significatif. | [source 1](https://academic.oup.com/eurheartj/article/44/39/3948/7243107?searchresult=1) ; [source 2](https://pubmed.ncbi.nlm.nih.gov/35071685/) |
| 10 | `chapters/I33/I33_c.html` | Le résultat unique doit être pris au sérieux sans remplacer la forte probabilité de bactériémie par un absolu biologiquement faux. | [source 1](https://pubmed.ncbi.nlm.nih.gov/35071685/) |
| 11 | `chapters/I34/I34_b.html` | La remise déduit une autorisation de prescription de la population exclue d’INVICTUS ; le texte général ESC 2025 et l’absence d’essais ne justifient pas cette généralisation. | [source 1](https://academic.oup.com/eurheartj/article/46/44/4635/8234488) |
| 12 | `chapters/I34/I34_d.html` | La liste de médicaments présente le rétrécissement dégénératif comme une indication ordinaire d’AOD malgré les exclusions des essais. | [source 1](https://academic.oup.com/eurheartj/article/46/44/4635/8234488) |
| 13 | `chapters/I34/I34_d.html` | Même réserve au point de lecture du tableau posologique. | [source 1](https://academic.oup.com/eurheartj/article/46/44/4635/8234488) |

Les corrections 01 à 03 évitent de transformer une précaution ou une probabilité en garantie de sécurité. La correction 06 rend la restriction rénale visible au point où le lecteur choisit une dose, plutôt que dans une fenêtre éloignée. Les corrections 09 et 10 gardent le niveau d’alerte d’une hémoculture unique positive sans confondre une forte probabilité et une impossibilité biologique. Les corrections 11 à 13 empêchent qu’une exclusion des essais devienne une autorisation générale de prescription.

La nuance I34 doit rester transparente : le texte général de l’ESC/EACTS 2025 mentionne une exclusion des AOD avec une surface mitrale ≤ 2,0 cm², alors que le tableau de recommandation décrit explicitement la forme rhumatismale. La copie corrigée conserve cette différence et demande un choix spécialisé dans la sténose dégénérative significative. Elle ne prétend pas qu’INVICTUS étudiait cette population.

## Conservation des structures et des arbitrages

La comparaison canonique → original reçu ne retire aucun ID de section ni aucune fenêtre existante dans ces quatre cours. Les attributs `data-ok` des réponses de quiz restent identiques, dans le même ordre. Les SVG restent identiques sauf un libellé du schéma I30 : « hémopéricarde : 150–200 mL » devient « 200–300 mL ». La géométrie est conservée ; ce volume reste une illustration et ne doit pas devenir un seuil clinique universel.

Pour les onze copies corrigées, tous les attributs `id`, `data-k`, `data-pop`, `data-title` et `data-ok`, ainsi que les SVG et les scripts, sont identiques à ceux de l’original reçu. Aucun nouvel identifiant, quiz ou dessin n’a été créé par les treize corrections. Ces contrôles statiques ne remplacent pas les essais du navigateur après reconstruction.

Les arbitrages connus concernant l’anticoagulation des valves mécaniques, les limites de l’essai INVICTUS, la distinction association/causalité et l’absence de certification humaine ne doivent pas être écrasés lors de l’injection. Les anciens en-têtes sont la divergence héritée explicitement repérée ; le paquet d’injection de Codex les conserve séparément.

## Réserves conservées

- **I00 — Rhumatisme articulaire aigu** : l’ancienne phrase « ne complique que l’infection pharyngée persistante » reste incompatible avec les autres passages discutant une origine cutanée possible. Le point n’a pas été réécrit ici car il est inchangé ; il doit rester dans le suivi médical. De même, l’anticoagulation en rythme sinusal est présentée trop restrictivement dans ce cours, alors qu’I34 discute aussi le contraste spontané dense et la dilatation auriculaire.
- **I00 — Rhumatisme articulaire aigu** : les nouveaux pourcentages pharmacocinétiques, les différences entre seuils de poids nationaux, les fréquences allergiques et plusieurs schémas pédiatriques restent à rapprocher des documents complets cités. Un taux sanguin inférieur à un seuil pharmacocinétique ne démontre pas que chaque patient devient immédiatement sans protection clinique. L’argument de « période sans protection » mérite encore d’être nuancé.
- **I30 — Péricardites, épanchement péricardique, tamponnade et constriction** : les différences entre tableaux ESC, autorisation suisse et choix en grossesse ou en insuffisance rénale doivent être contrôlées pour la spécialité effectivement prescrite. La contre-indication rénale suisse est rendue visible ici ; les autres différences ne sont pas certifiées exhaustivement. Les restrictions d’effort et les mécanismes proposés pour le frottement ou les récidives ne doivent pas être présentés comme des démonstrations expérimentales universelles.
- **I33 — Endocardite infectieuse** : les classes de recommandation, cibles pharmacocinétiques et dates de relais oral ajoutées ne constituent pas un protocole indépendant. Les situations de choc, d’accident vasculaire cérébral et de chirurgie restent des décisions d’équipe. Les dénominateurs et populations de chaque chiffre nouveau n’ont pas tous été vérifiés.
- **I34 — Valvulopathies mitrales, tricuspides et pulmonaires** : les prescriptions après réparation et valve percutanée, les seuils opératoires et les variantes d’anticoagulation demandent une relecture clinique du cas et des tableaux complets. Les formulations observationnelles bien distinguées d’un bénéfice causal ont été conservées. Cette contrelecture ne certifie pas toutes les nouveautés des recommandations de 2025 ni leurs éventuels corrigenda de 2026.

Les quatre cours restent **en révision**. Cette remise ne démontre ni l’achèvement des quatorze autres cours attendus de Claude, ni la complétude CIM-11, ni la justification systématique de toute affirmation des cours anciens.

## Paquet de correction remis à Codex

Le manifeste scratch `review_valves_b6/CORRECTIONS.json` contient les treize substitutions exactes, leurs sources, les chemins des copies et les contrôles statiques. Les copies sont dans `review_valves_b6/corrected/sources/chapters/`. Elles partent des octets originaux b6 ; Codex doit ensuite réappliquer les quatre statuts canoniques et effectuer l’injection contrôlée, la compilation et les vérifications du navigateur.

- `chapters/I00/I00_a.html` — original SHA-256 `e4ecadec07ae3655d281af82bf5f2ea900231d4302f35d39927d5fc0d52f6ad6` ; copie corrigée `0a2df7268a40ae97e799b6ce576eff6690188741f459c19cd07ee1654dde40cd`.
- `chapters/I00/I00_b.html` — original SHA-256 `228e9989de6f34e30a5d216b042f06d1decaece8e171b1c0fdf7620bc6a60caa` ; copie corrigée `0e0f8052051f6d91eee5500060416ebc1b19e57c549a206940dc8f32e2867abf`.
- `chapters/I00/I00_pop5.html` — original SHA-256 `9f804cecad325c3ab4ade127effa614c955df26409360fb04532b9661dbb745c` ; copie corrigée `c956f8aecba21e84908aa8e1c6c4f4231aa22f8d77c4d9d785c02720d7a7e8f9`.
- `chapters/I30/I30_a.html` — original SHA-256 `0a282ebecc8ad14c029c788a049eaa5b249f259a9c81755297d09e9f913d57ba` ; copie corrigée `4b0989132ddc30501f4f797e4a9662e52d73cea4720cca1c11bb796fbaeaef3b`.
- `chapters/I30/I30_b.html` — original SHA-256 `dc92b3ab1b3569aef786ae4791f79efa309b1fdc89857acb5ac068bd16ac29f3` ; copie corrigée `168ce45c9dda91843094103afe4723e8efa442d92cae0beb3300acb7cec7333b`.
- `chapters/I33/I33_a.html` — original SHA-256 `9642ff20f07b1f4165c5c6a81ffde95c752d911279215bf38a88a72bfdc2ac0a` ; copie corrigée `f76bf39caed20b8f9ce06f21308b6d85600abc63664c87d932a364eadf247e7b`.
- `chapters/I33/I33_b.html` — original SHA-256 `a9c65f45861913e605519261bee7715104ea7bb9ec979d18251e547009f0cefa` ; copie corrigée `dd5aea957d409ee1bbbee8ffa32a2e4c88fd11a09ed93670bc66efd5419b425f`.
- `chapters/I33/I33_c.html` — original SHA-256 `0df79d11f05a75dabd24ff110b5118251562be4116a38839aa92c5836265ce2a` ; copie corrigée `016a06b3a878f5e9a44405324e62ff11c0f2b83452e8d4c7f43f12200cdb7aa6`.
- `chapters/I33/I33_d.html` — original SHA-256 `3e4365f2f81e5a8751e2dc6df244aa30c2d4129eec33f5e372cb4dff8a23d5c6` ; copie corrigée `212b146f333edc80368941b85b8d3febfc075bfcefe9373da2ec152a26e60e41`.
- `chapters/I34/I34_b.html` — original SHA-256 `dd9918c4f1a37ca929d6cefe3135774307f630ff72d25567c402b75b3d236301` ; copie corrigée `145bd19cdbc5b955f659b91c6e2649e64a64a58ed1ac729d3d88e1441906ee8c`.
- `chapters/I34/I34_d.html` — original SHA-256 `f800732a33fa3a612586a2fa5be902ebda30c551834dc8c9e42c2606a9d2bff9` ; copie corrigée `96e534286ee06ba740a13bddb6b2722a952579cdd593b9d6b1c4c2ebf4516df5`.
