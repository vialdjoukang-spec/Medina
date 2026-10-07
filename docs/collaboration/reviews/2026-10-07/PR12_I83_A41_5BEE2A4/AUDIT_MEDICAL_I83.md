# Audit médical ciblé — I83 — Varices des membres inférieurs (C-01-Cardiologie)

Date de contrôle : 7 octobre 2026, 23:45 UTC. Remise examinée : `8dfa6ba453fc872591b79e5720c914ce47964470`, branche `claude/loving-shannon-spwrhc`, PR #12. Le coordinateur a signalé la tête ultérieure `5bee2a48ef1804a0e3452d64a1041e0bd1b50691` et l'identité des huit blobs du cours et du rapport ; cet audit porte sur ces contenus identiques, pas sur d'autres changements de branche.

**Conclusion : réception et archivage possibles ; injection médicale non recevable en l'état. Deux erreurs bloquantes sont établies.** Aucun fichier de cours n'a été modifié. Cet audit ciblé ne certifie ni l'ensemble des assertions de ce nouveau cours, ni les trente cours historiques, ni une complétude CIM-11.

## I83-MED-01 — Contre-indication suisse du polidocanol rétrogradée sans preuve

**Bloquant — sécurité de prescription.**

Localisation : `chapters/I83/I83_d.html`, ligne 47, section `i83-p-3` ; fenêtre `i83-d-polidocanol` dans `I83_pop4.html`, ligne 26. Le rapport original reconnaît cette décision d'interprétation.

Le texte principal propose que le médecin considère le diabète comme une contre-indication relative au polidocanol. Les pages suisses actuelles d'Aethoxysklerol et Sclerovein le listent au contraire sous les contre-indications, sans qualificatif relatif. Le texte professionnel Sclerovein récupéré par la recherche confirme `Diabetes mellitus` dans cette rubrique [S1, S2]. L'absence dans un autre référentiel ne justifie pas une rétrogradation du libellé suisse.

Correction attendue : conserver explicitement le diabète comme contre-indication selon l'information professionnelle suisse ; exposer séparément l'écart avec les recommandations européennes, sans donner une instruction clinique contraire au libellé. Harmoniser le corps, la fenêtre, les synthèses et le rapport. Faire apparaître les précautions indispensables dans le cours visible.

Mécanisme et limite : le sclérosant provoque une lésion endothéliale et un thrombus local ; une mauvaise perfusion ou une neuropathie diabétique rendent plausible un risque cutané et de détection tardive d'une complication. **Ce raisonnement n'est pas la justification démontrée du libellé suisse** ; la source consultée n'en donne pas la raison. Ne pas transformer cette plausibilité en mécanisme réglementaire certain, ni proposer une levée automatique selon le seul état artériel.

## I83-MED-02 — Anticoagulation curative omise pour EHIT III

**Bloquant — conduite susceptible de laisser sans traitement une extension profonde.**

Localisation : `chapters/I83/I83_b.html`, ligne 64, section `i83-10` ; `chapters/I83/I83_pop2.html`, ligne 120, fenêtre `pareto-i83-pec`. La fenêtre `i83-thermique`, ligne 45 du même fichier, décrit les classes mais ne corrige pas la conduite.

Ces passages réservent l'anticoagulation curative à EHIT IV. Le texte primaire AVF/SVS intégral effectivement lu prescrit aussi le curatif pour EHIT III, avec échographie hebdomadaire puis arrêt après rétraction/résolution à la jonction : recommandation 3.4, grade 1B [S3].

Correction attendue : distinguer I, II, III et IV ; II relève habituellement d'une surveillance hebdomadaire, avec traitement individualisé chez les patients à haut risque ; III reçoit le curatif et une surveillance échographique ; IV est prise en charge comme une TVP provoquée, selon le risque hémorragique et les recommandations pertinentes. Actualiser aussi le Pareto et la fenêtre liée.

Mécanisme : en classe III, le thrombus occupe plus de la moitié de la lumière profonde ; l'extension profonde expose à propagation et embolie malgré l'absence d'occlusion complète. La régression fréquente des formes mineures ne s'extrapole pas à ce groupe. Limites : la recommandation s'appuie largement sur séries et consensus ; cette limite ne justifie pas l'omission du curatif.

## Réserves à vérifier avant clôture, sans certification apportée ici

- **CEAP** : `I83_a.html:40,179,193` appelle C4a la classe la plus élevée malgré la corona C4c ; `I83_b.html:125` et `I83_pop1.html:14` reprennent C4a. Éviter une hiérarchie non expliquée entre sous-classes C4 ; distinguer la classe C4, les manifestations a/c et les notations élémentaire/complète. Le résumé PubMed de Lurie 2020 ne suffit pas à vérifier leur règle de notation. Le texte intégral éditeur a renvoyé 403 ; réserve non levée.
- **Seuil des varices** : `I83_a.html:25` et `I83_b.html:129` restent indirects (« au-delà du calibre réticulaire »). Le seuil exact, la position debout et la convention CEAP doivent être vérifiés dans le consensus primaire accessible avant d'être présentés comme critères formels. Les anciennes tailles de la monographie sclérosante ne doivent pas servir de seuil CEAP.
- **Ulcère et artériopathie** : `I83_b.html:133` et `I83_c.html:82,84` risquent de transformer le seuil IPS 0,8 de choix de compression en définition étiologique exclusive. Décrire l'origine veineuse sur clinique/imagerie, puis la composante artérielle et la tolérance de compression ; garder l'avertissement sur l'IPS faussement élevé.
- **SVT** : `I83_b.html:17,22`, fenêtre `i83-tvs` et `pareto-i83-pec` donnent une interdiction absolue d'intervention aiguë sur la base ESVS 2021. Contrôler explicitement le périmètre des recommandations plus récentes et les éventuelles exceptions sélectionnées. Le renvoi I80 ne remplace pas la lecture de ses sources et doses consommées. Aucune validation exhaustive des posologies fondaparinux/AOD n'est revendiquée ici.
- **Mousse et diamètre** : `I83_c.html:34` et `I83_pop3.html:62` écrivent qu'elle ne se discute/ne vise *que* les troncs <6 mm. Vérifier la portée de IIb B avant de transformer un critère de choix favorable en interdiction technique.
- **Tumescence** : `I83_pop4.html`, fenêtre `i83-d-tumescence`, associe l'absorption retardée à 20–30 minutes ; vérifier que ce délai provenant de lidocaïne injectable convient à la tumescence périveineuse décrite. Le rappel que 15 mg/kg n'est pas une posologie suisse autorisée est utile, mais ne valide pas la durée de surveillance.
- **Complétude de couverture** : le cours déclare I87 couvert mais ne développe principalement que I87.0/I87.1/I87.2. Les entrées I87.8/I87.9 ne sont pas certifiées développées ; aucun inventaire CIM-11 validé.
- **Justifications** : de nombreuses fenêtres explicitent les mécanismes ; des synthèses réintroduisent des formulations absolues et certains passages ne comportent pas de source locale suffisante. Les contrôles mécaniques du rédacteur ne constituent pas une validation de chaque affirmation.

## Posologie suisse du polidocanol : concordance ciblée, pas validation globale

Le tableau `I83_d.html:38–42` concorde avec le texte professionnel Aethoxysklerol récupéré par recherche [S4] : réticulaires 0,25–0,5 %, petites 1 %, moyennes 2–3 %, volumes spécifiques ; plafond 2 mg/kg/j. Pour 70 kg, 140 mg correspondent à 4,67 mL à 3 % et 14 mL à 1 % : calcul revérifié. **Ne pas substituer la monographie allemande**, dont les concentrations diffèrent. Les limites propres à la mousse et à chaque spécialité nécessitent leur vérification séparée.

## Sources effectivement consultées et limites d'accès

- **S1. Aethoxysklerol, page produit suisse Compendium**, résumé public lu en entier ; diabète et plafond 2 mg/kg/j vérifiés. https://compendium.ch/de/product/index/80113-aethoxysklerol-sol-inj-0-25 — références de recherche `turn3view0` / `turn4view0`. La page complète ouverte ne rendait pas toutes les sections professionnelles ; ne pas dire que cette ouverture a validé toute la monographie.
- **S2. Sclerovein, information professionnelle suisse reproduite par Compendium**, section contre-indications et suite professionnelles effectivement restituées dans la réponse de recherche `turn6search0` ; version indiquée mai 2022. https://compendium.ch/de/product/index/1287425-sclerovein-sol-inj-2-i-v — contre-indication également visible à l'ouverture `turn3view1` / `turn4view1`.
- **S3. Kabnick et al., AVF/SVS, Classification and treatment of endothermal heat-induced thrombosis**, publication 2020/2021, DOI 10.1177/0268355520953759 ; texte intégral lu, notamment recommandations 3.2–3.5 et discussion du traitement. https://pmc.ncbi.nlm.nih.gov/articles/PMC7820569/ — `turn5view1`, lignes 192–203 et 507–531. Le document reste référencé par la liste officielle AVF consultée le jour de contrôle : https://www.venousforum.org/resources/guidelines/ (`turn16search3`).
- **S4. Aethoxysklerol, information professionnelle suisse**, section dosages effectivement rendue par recherche `turn8search0`, version suisse à ne pas confondre avec version allemande : https://compendium.ch/de/product/1384457-aethoxysklerol-inj-los-2 . Concordance limitée aux doses explicitement lues.
- **ESVS 2022** : référence et dépôt auteur identifiés ; PDF référencé https://orbi.uliege.be/handle/2268/288479 . L'ouverture initiale a identifié le PDF et ses métadonnées, les lectures ciblées suivantes ont échoué par timeout ; le site ESVS a redirigé vers login. **Pas de prétention à lecture intégrale indépendante de cette source.**
- **SVS/AVF/AVLS 2023** : primaire identifié https://pmc.ncbi.nlm.nih.gov/articles/PMC11523430/ ; les résultats de recherche corroborent ARTE III/IV, mais les ouvertures ont renvoyé reCAPTCHA/403. Ce texte n'est pas utilisé ici pour prétendre à une revue complète de sa recommandation.
- **Lurie 2020 CEAP** : référence primaire identifiée https://pubmed.ncbi.nlm.nih.gov/32113854/ ; https://doi.org/10.1016/j.jvsv.2019.12.075 . Accès intégral éditeur refusé ; les réserves de notation demeurent ouvertes.

## Empreintes des huit sources reçues

```text
b60613277a80529d4feac3a87efcefed5674ce4d00707e95476e8b210df42625  I83_a.html
44743819426b8be95732354cea5433f16fefcd611109bd4d127591e058910f9f  I83_b.html
941a6ddc75ea1e557fb79d7f8e0d848897275240b1e2338a203860ffaf859ebf  I83_c.html
bd249ffc67290ac2992e26b2ba4e38a2258b64475b3ba3890000589bbdbf7413  I83_d.html
fc9e9b44c50f6e5266a9240bcd627a62a816492ea01c0d7ef3cb42f60919905b  I83_pop1.html
ef1db4dbddf234683bf3b4b38b60e2e399c1b5c3fe141be93193c9da85e43c34  I83_pop2.html
06a2d0657d71a6fee93df018698afe90dd4b00f799b080b0907a43d402087de9  I83_pop3.html
0ad840034b898f1240bd68e36669e6ef93ba1bf70f769b580a71d2177e74cc6a  I83_pop4.html
```

## Contrôles réellement effectués

Lecture d'AGENTS.md et du rapport original ; extraction des contenus des huit HTML, recherche globale des assertions prioritaires et lecture des passages concernés dans tous les onglets et fenêtres ; SHA-256 des huit fichiers, concordants avec le rapport ; recherches et lectures primaires décrites ci-dessus ; recalcul des conversions de dose. **Aucun test navigateur, build, CI ou déploiement exécuté par cet auditeur.** Aucune réserve du lot ESC2026 n'est déclarée levée par ce contrôle d'I83.
