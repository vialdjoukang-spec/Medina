# Contrelecture ciblée — I46, I47 et I49, remise e82a85c

Date : 8 octobre 2026. Proposition examinée : `e82a85c`, sous `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/`. Base de comparaison des cours : sources canoniques `a6f18a1`. L’examen porte sur les ajouts et les passages décisionnels concernés ; il ne constitue pas une validation médicale exhaustive des 28 HTML de ces trois cours.

## Verdict

Six substitutions de prose sont proposées dans quatre HTML avant reconstruction. Les doses de réanimation et plusieurs changements ERC 2025 ont été rapprochés des sources primaires accessibles. Aucun statut de validation ne doit être ajouté. Les cours restent en révision.

| Repère | Source à corriger | Problème et correction |
| --- | --- | --- |
| I46-01 | `chapters/I46/I46_a.html` | L’ajout déduit une sédation obligatoire de la présence d’un pouls, qui ne démontre pas la conscience. Le piège révisé distingue une TV monomorphe avec pouls de l’arrêt circulatoire et conditionne la sédation à la conscience, avec surveillance du risque hémodynamique et sans retarder le choc urgent. |
| I46-02 | `chapters/I46/I46_a.html` | La justification du choc non synchronisé invoque une mauvaise reconnaissance de QRS larges et variables alors que la ligne décrit des QRS réguliers. Le motif pertinent est l’arrêt circulatoire et la nécessité d’un choc sans attendre une synchronisation. |
| I47-01 | `chapters/I47/I47_b.html` | La phrase héritée « traiter une TSV comme une TV [...] est sans danger » est renforcée par le nouvel argument. Elle est trop générale : l’amiodarone IV est notamment contre-indiquée dans la FA pré-excitée. Le correctif conserve la prudence devant une tachycardie régulière à QRS larges et rend les exceptions visibles. |
| I47-02 | `chapters/I47/I47_b.html` | Le nouvel argument dit que le vérapamil n’arrête pas « la TV », alors que le cours explique les TV fasciculaires sensibles au vérapamil. Employer « la plupart des TV », sans rendre le vérapamil utilisable dans une tachycardie à QRS larges non identifiée. |
| I49-01 | `chapters/I49/I49_b.html` | L’ajout « sans essai randomisé » ne reste exact que pour l’époque des recommandations ESC 2021. Un essai randomisé de 68 patients a été publié en 2024. Le correctif distingue cette chronologie sans extrapoler le petit essai à tous les patients. |
| I49-02 | `chapters/I49/I49_pop3.html` | Le passage obstétrical conserve la règle fixe de quatre/cinq minutes sous le titre ERC 2025, avec une justification nouvelle. Il contredit I46 actualisé. Préparer immédiatement une hystérotomie et la réaliser dès que possible sur place ; présenter quatre/cinq minutes comme l’ancien repère. |

## Sources primaires consultées

1. **ERC 2025 — réanimation avancée adulte** : Soar et al., *Resuscitation* 2025;215:110769, [DOI](https://doi.org/10.1016/j.resuscitation.2025.110769). La [version officielle du Resuscitation Council UK](https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/adult-advanced-life-support-guidelines) indique une sédation/anesthésie soigneuse chez le patient conscient et le risque de détérioration hémodynamique. Elle décrit les chocs, la synchronisation et les doses vérifiées ci-dessous. I46-01 et I46-02 s’appuient sur ces distinctions ; l’explication de I46-02 est une interprétation clinique de l’algorithme, et non une citation de preuve comparative.
2. **ESC 2019 — tachycardies supraventriculaires** : Brugada et al., *European Heart Journal* 2020;41:655–720, [texte officiel](https://academic.oup.com/eurheartj/article/41/5/655/5556821?searchresult=1). Les recommandations sur la FA pré-excitée classent l’amiodarone IV comme non recommandée et dangereuse. Le [rappel officiel ESC](https://www.escardio.org/communities/councils/cardiology-practice/scientific-documents-and-publications/ejournal/volume-18/arrhythmias-devices-novelties-at-esc-2019/) confirme cette exception. Le texte intégral Oxford n’a pas été relu dans son ensemble ; les passages indexés et ce rappel officiel ont été utilisés pour I47-01.
3. **ESC 2022 — arythmies ventriculaires** : Zeppenfeld et al., *European Heart Journal* 2022;43:3997–4126, [DOI](https://doi.org/10.1093/eurheartj/ehac262). La TV fasciculaire constitue l’exception déjà correctement décrite dans le cours qui motive I47-02. Cette vérification de cohérence ne prétend pas certifier tous les tableaux de recommandations ESC 2022.
4. **Essai randomisé ablation/stimulation** : Cho et al., *BMC Cardiovascular Disorders* 2024;24:246, [publication primaire](https://link.springer.com/article/10.1186/s12872-024-03920-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/38730404/). Après deux retraits de consentement, 68 patients avec FA paroxystique et syndrome tachycardie-bradycardie ont été analysés. Le correctif I49-01 établit l’existence du comparateur randomisé, sans affirmer une supériorité universelle ni décrire tous les résultats.
5. **ERC 2025 — circonstances particulières** : [PDF officiel](https://www.erc.edu/media/wwufbysp/gl2025-06-spec-circ-e.pdf), section arrêt pendant la grossesse. L’hystérotomie doit être réalisée dès que possible sur le lieu de l’arrêt par une équipe compétente. Le [texte de la publication](https://www.sciencedirect.com/science/article/abs/pii/S0300957225002655) distingue l’ancien repère quatre/cinq minutes de l’absence de données imposant un délai fixe. Les passages indexés de la publication et du PDF ont été consultés ; le PDF entier n’est pas certifié.
6. **ERC–ESICM 2025 — soins post-réanimation** : [PDF officiel](https://www.erc.edu/media/atqopqm4/gl2025-07-post-resus-e.pdf). Le passage vérifié confirme la prévention de la fièvre à une température ≤ 37,5 °C durant 36–72 heures chez le patient restant comateux.

## Contrôles ciblés sans correction proposée

- Les séquences adrénaline 1 mg, amiodarone 300 puis 150 mg, lidocaïne 100 puis 50 mg et les intervalles correspondent aux passages ERC 2025 consultés.
- Les trois chocs regroupés dans un arrêt observé et monitoré avec défibrillateur immédiatement disponible sont comptés comme le premier choc pour le calendrier des médicaments.
- Le passage ERC 2025 sur l’hypothermie permet une dose unique d’adrénaline sous 30 °C lorsque la réanimation extracorporelle n’est pas imminente ; les doses suivantes sont espacées à 30–35 °C. Le changement n’a pas été corrigé par réflexe vers l’ancienne règle d’abstention.
- La prévention de la fièvre pendant 36–72 heures et les objectifs ciblés après RACS ne nécessitent pas de correction dans cette lecture.

## Application et réserves

Le script scratch `/workspace/scratch/d102f3e40172/fix_rhythm.py` contient les six substitutions exactes et attend que les propositions e82 soient injectées dans les sources canoniques. **Il n’a pas été exécuté par l’agent de contrelecture.** Il exige une occurrence exacte de chaque ancienne cible, vérifie l’absence de modification des identifiants, attributs interactifs, réponses de quiz, SVG et scripts, puis écrit les quatre sources seulement après le contrôle préalable de toutes les cibles.

Le script ne vérifie pas les fenêtres ailleurs dans le corpus, la compilation, les tests navigateur ni les empreintes d’une copie finale qui n’existe pas encore. Après application, Codex doit reconstruire les consommateurs, vérifier l’interface et tracer les empreintes et le commit d’intégration. Les posologies suisses, toutes les références, les pourcentages, les mécanismes anciens et les classes de recommandations non ciblées restent à contrôler. Aucun des trois cours n’est déclaré médicalement achevé.
