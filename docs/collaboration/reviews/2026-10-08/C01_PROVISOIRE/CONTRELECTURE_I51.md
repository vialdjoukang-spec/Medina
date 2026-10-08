# I51 — Complications des cardiopathies et atteintes cardiaques au cours d’autres maladies (C-01-Cardiologie)

Contrelecture ciblée et intégration locale provisoire, 8 octobre 2026. Statut : **PROVISOIRE_AVEC_RESERVES**, sans clôture du fragment et sans validation médicale humaine. La publication GitHub et le déploiement doivent être vérifiés séparément après ce gel.

## Provenance, comparaison et périmètre

La PR [16](https://github.com/vialdjoukang-spec/Medina/pull/16) vient de `claude/vigilant-mayer-cevhwj`. La branche, les rapports et les fichiers de remise identifient Claude ; le compte utilisateur partagé ne suffit pas. Tête observée : `19c6798641f8c870e6d3949280037d73df5cd5f2`. Main de réconciliation : `a34f19752562376a84d74de5141a0593029eca4b`.

La V2 livrée à `625138a1d831eb0d6b1d0e96f3d890f0e2015728` déclare la base `7e5a648535164d64638db9bc5a90b0fe5917ec45`. Les 297 sources sont archivées sans modification : 83 présentes dans la remise, 214 récupérées à la base explicite avec confrontation de chaque SHA-256 au manifeste. Comparaison avec la V1 reçue : 268 identiques, 29 modifiées. Les 214 sources existantes concordent avec main ; aucune n’est réappliquée. Le dossier C01 est inchangé entre la livraison V2 et la tête 19c6798. Le renouvellement de SHA lié aux autres travaux n’est pas une nouvelle livraison C01.

Archive V2 : `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-PR16-625138A-V2/`. Les originaux V1 restent conservés. Adaptations séparées : `livraisons/Livraison Codex/C-01-Cardiologie/travail/INTEGRATION_PROVISOIRE_2026-10-08/sources/`.

Seul I51 est ajouté dans les huit HTML canoniques, son glossaire et le catalogue réellement consommés. Les six sources I51 modifiées par la V2 sont rapprochées de l’adaptation : précisions Marcoumar et GUSTO conservées, avec limites supplémentaires ci-dessous. Les huit autres nouveaux cours ne sont pas injectés : I73 — Autres maladies vasculaires périphériques ; I77 — Autres affections des artères et artérioles ; I85 — Varices œsophagiennes ; I89 — Autres affections non infectieuses des vaisseaux et ganglions lymphatiques ; I95 — Hypotension ; I97 — Troubles de l’appareil circulatoire après un acte à visée diagnostique ou thérapeutique, non classés ailleurs ; R00 — Anomalies du rythme cardiaque ; R02 — Gangrène, non classée ailleurs. Ils appartiennent à C-01-Cardiologie ; leurs titres de cours regroupés restent ceux des remises archivées.

La campagne historique 30 cours 15/15, le backlog cardiologique 20 cours 10/10 et les attributions de 21 fragments 11 Claude/10 Codex restent distincts. Aucune attribution, aucun chapitre actif, aucun statut final de fragment ne change. J40 — Bronchite et ses regroupements J20/J40/J41/J42 sont intacts. Les anciens paquets b1, b6 et 8ce ne sont pas réappliqués. ESC2026 reste archivé, non injecté ; MED-01, MED-02 et MED-03 ne sont pas réputées levées.

## Adaptations médicales ciblées

| Zone | Adaptation et raison clinique | Conditions et limites |
| --- | --- | --- |
| Marcoumar, cours et fenêtres | Délai d’effet complet corrigé à environ sept jours ; dose initiale liée à la coagulation de départ. L’augmentation de dose ne remplace pas l’anticoagulation immédiate nécessaire. | Version suisse allemande 103 D d’octobre 2020 réellement consultée. Schéma de monographie, non prescription uniforme du thrombus ventriculaire. INR et terrain individualisent le choix. |
| AOD, tableaux et rappels | Les réductions de dose de fibrillation auriculaire ne sont plus présentées comme automatiquement valides pour le thrombus ventriculaire. | Emploi hors indication suisse, décision spécialisée documentée ; fonction rénale, interactions et risque hémorragique restent visibles. Réserve rouge ouverte. |
| Énoxaparine et TIH | Doses rattachées aux indications sources ; augmentation de l’exposition en insuffisance rénale et précautions de TIH expliquées. | Schéma de TVP extrapolé au thrombus ventriculaire, non indication autorisée. TIH récente de 100 jours ou anticorps circulants : contre-indication ; réexposition au-delà spécialisée. La monographie suisse actuelle conserve la limite rénale <30 mL/min ; ne pas la remplacer par une règle d’un autre pays. |
| Choc du Tako-tsubo, quiz et rappels | Le mécanisme d’obstruction est distingué de la défaillance de pompe. Les médicaments renforçant le gradient ne sont pas proposés comme solution systématique. | Remplissage seulement après évaluation et sans congestion importante ; pas d’initiation de bêtabloquant dans le choc aigu, l’œdème pulmonaire ou la défaillance sévère. Réserve rouge ouverte, sans protocole posologique de choc prétendument validé. |
| Lévosimendan | Une inotropie peut aggraver une obstruction dynamique ; l’option systématique est retirée des résumés. | Monographie suisse actuelle et sélection clinique non établies dans cette revue. Pas de dose proposée comme conduite validée ; réserve rouge ouverte. |
| GEIST 2025, fenêtres et glossaire | Association observationnelle de prescription à la sortie et mortalité distinguée d’un effet causal et de la prévention des récidives. | Résumé primaire lu ; analyse observationnelle, pas essai randomisé. Pas de bénéfice sur récidive établi. Liens GEIST/HR vers une fenêtre existante, puis retour de glossaire testés. |
| Diagnostic d’amylose ATTR | Nouvelle explication contextuelle de la voie non invasive ; exclusion d’une composante monoclonale indispensable. | Imagerie compatible, scintigraphie grade 2/3, localisation myocardique par SPECT, chaînes légères libres et immunofixations sérique et urinaire. Le résultat isolé ne suffit pas. |
| Conduction et étiologies | La recherche de Lyme, Chagas ou sarcoïdose ne retarde pas une stimulation urgente nécessaire. | Stabilisation prioritaire ; étiologie documentée ensuite, sans raccourci universel de traitement causal. |
| Thrombus et Tako-tsubo | Akinésie décrite comme contexte fréquent, non critère anatomique nécessaire ; exploration coronaire contextualisée. | Angioscanner seulement chez un patient stable et dans un contexte approprié, pas remplacement universel de la coronarographie urgente. |
| SCA et antithrombotiques | La trithérapie courte est une stratégie par défaut, non une durée maximale universelle. | Risques ischémique et hémorragique individualisés ; exceptions expliquées dans la fenêtre associée. |
| GUSTO-I | Chiffres historiques clairement rattachés aux groupes décrits dans le résumé primaire de Crenshaw 2000. | Groupes médicaux et chirurgicaux non randomisés ; pas estimation causale du bénéfice chirurgical ni prédiction individuelle actuelle. La mention AHA 2021 n’est pas déclarée fausse sur la seule différence de cohorte. |

## Sources primaires et niveau d’accès

Consultation du 8 octobre 2026. Les versions anciennes ci-dessous restent les versions applicables trouvées ; leur année n’est pas changée artificiellement.

- [Marcoumar, Swissmedic 19395](https://www.swissmedicinfo-pro.ch/showText.aspx?authNr=19395&lang=DE&supportMultipleResults=1&textType=FI), octobre 2020 : texte professionnel allemand lu.
- [Eliquis, Swissmedic 61549](https://www.swissmedicinfo-pro.ch/showText.aspx?authNr=61549&lang=FR&supportMultipleResults=1&textType=FI), août 2026 : texte professionnel français lu ; contre-indication Child-Pugh C suisse confirmée, sans lui substituer un libellé étranger.
- [Clexane, Swissmedic 49456](https://www.swissmedicinfo-pro.ch/showText.aspx?authNr=49456&lang=DE&supportMultipleResults=1&textType=FI), février 2026 : texte professionnel allemand lu.
- [Xarelto, Swissmedic 58728](https://www.swissmedicinfo-pro.ch/showText.aspx?authNr=58728&lang=DE&supportMultipleResults=1&textType=FI), mai 2025 : texte professionnel allemand lu.
- [Rapport international Tako-tsubo 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11589216/) : sections sur obstruction, choc et médicaments lues en texte intégral.
- [GEIST 2025, PMID 39918532](https://pubmed.ncbi.nlm.nih.gov/39918532/) : résumé primaire, pas article intégral.
- [Position ESC amylose 2021, DOI 10.1002/ejhf.2140](https://doi.org/10.1002/ejhf.2140) : critères non invasifs et exclusion monoclonale lus dans le texte intégral.
- [Crenshaw, GUSTO-I 2000, PMID 10618300](https://pubmed.ncbi.nlm.nih.gov/10618300/) : résumé primaire, pas article intégral.
- [AHA complications mécaniques 2021](https://doi.org/10.1161/CIR.0000000000000985) : accès intégral bloqué pour cette reprise ; éléments bibliographiques et indexés seulement, sans prétendre à une lecture complète.
- [ESC stimulation 2021](https://doi.org/10.1093/eurheartj/ehab364) et [ESC SCA 2023](https://doi.org/10.1093/eurheartj/ehad191) : consultation primaire ciblée par l’agent de contrelecture, accès intégral non reproduit par le coordinateur. Cette limite reste ouverte dans l’audit final.

## Réserves rouges à reprendre par Claude

| Identifiant stable | Emplacement canonique | Action attendue |
| --- | --- | --- |
| C01-I51-AOD-DOSE | I51_d.html, i51-reserve-aod | Documenter les schémas propres au thrombus ventriculaire et leurs conditions ; ne pas transposer automatiquement une réduction de dose FANV. |
| C01-I51-LEVOSIMENDAN-STATUT | I51_d.html, i51-reserve-levo | Vérifier la monographie suisse actuelle et délimiter les situations sans obstruction ; conserver l’avertissement jusqu’à correction sourcée. |
| C01-I51-CHOC | I51_b.html, i51-reserve-choc | Achever la contrelecture primaire du traitement du choc selon obstruction, congestion et hémodynamique ; aucune recette universelle. |

Les marqueurs ont `data-claude-reservation`, `data-reservation-status="open"` et `data-review-owner="Claude"`. Le texte rouge explique la réserve ; sa couleur ne transforme pas un traitement incertain en conduite applicable. Le registre append-only porte les empreintes exactes, les preuves et les actions.

## Contrôles réellement exécutés

[Inventaire distant paginé](REMOTE_SNAPSHOT_FINAL.json) : 20 branches, 15 PR, pages terminales vides ; 279 fichiers PR16 en 100/100/79/0. Les diffs de toutes les autres branches ne sont pas audités et aucune autre contribution n’est fusionnée.

[Résumé des contrôles](CONTROLES_EXECUTES.json) : 212 tests unitaires réussis ; audit statique explicite I51 (22 464 mots, 72 fenêtres, 5 quiz, 8 Pareto) ; builds global, 22 fragments et reconstruction finale S01 ; audit des 22 fragments, syntaxe JavaScript et deux builds reproductibles.

[Navigation native](browser/i51_native_results.json) : 1 971 assertions réussies, 0 échec, 90 déclencheurs directs et 72 fenêtres par format 1360×900 et 390×844 ; ouvertures, retour, fermeture, quiz, routes, titres, débordements et erreurs JavaScript contrôlés. [Réserves visibles](reserves/i51_reservations_results.json) : 90 assertions réussies, desktop 1440×900 et contexte mobile tactile 390×844, contraste rouge lisible, identifiants, onglets, glossaires imbriqués et captures réelles. Aucun moteur clinique n’est certifié par ces tests.

[Navigation enregistrée](reserves/I51_navigation_enregistree_2026-10-08.gif) : quatre captures successives du navigateur réel, pas flux en direct ni simulation. Les empreintes des images figurent dans le rapport navigateur. Atkinson Hyperlegible Next, le thème clair, les routes stables et les spécialités séparées sont conservés.

## Ce qui reste à faire

Réserves cliniques ci-dessus ; contrelecture exhaustive de chaque affirmation, tous onglets, tableaux, figures, quiz, fenêtres et glossaires d’I51 et des autres cours. Les précautions corrigées restent visibles dans le cours. Les huit autres nouveautés C01 attendent leur propre revue et leur propre contrôle. Aucune relecture exhaustive des 30 cours, validation médicale humaine, clôture INJECTE ou complétude CIM-11 n’est déclarée. Cette tranche ne modifie que le catalogue CIM-10 actuel. La réussite de CI, la disponibilité des fichiers distants et le déploiement servi ne sont pas attribués avant constat séparé.
