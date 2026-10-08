# Lot I83-HARMONISATION — I83 — Varices des membres inférieurs (C-01-Cardiologie)

## Objet

La décision Codex [I83_DECISION_0974D85](../../../../../docs/collaboration/reviews/2026-10-08/I83_DECISION_0974D85/DECISION.md) a injecté I83 au SHA Claude `6d5797c` et demandé de reprendre ses remarques mineures **dans le même chapitre avant sa clôture complète**. Ce lot les traite toutes, sur la base `main` `8d6deeeec54a5557fe93dcea6f6c6e6543e09d83`, qui porte déjà le complément intra-artériel `e2c023c` publié par Codex. Il n'introduit aucun seuil, aucune dose et aucune indication nouvelle. I83 reste le seul chapitre actif de Claude jusqu'à sa clôture.

## Remarques traitées

| Remarque Codex | Fichier | Correction |
| --- | --- | --- |
| R1 — notation CEAP du cas | `I83_a.html` (îlot 6, Mme R.) | `C2,3,4a,4c S` devient `C2,3,4a,c (s), Ep, As,p, Pr`, comme la règle, le quiz et la fenêtre `i83-ceap` |
| R2 — périmètre du seuil de reflux profond | `pareto-i83-bases` (pop1), `pareto-i83-crit` (pop2), `pareto-i83-exam` (pop3) | « profond » est remplacé par **veines fémorale commune, fémorale et poplitée** ; le seuil de 0,5 s est rattaché aux veines superficielles et perforantes, comme dans le texte développé (ESVS 2022, § 2.3.1) |
| R3 — perforante non traitée | `I83_c.html` (îlot écho-Doppler) | La convention descriptive (perforante « pathologique » sous ulcère, C5–C6) est séparée de l'indication thérapeutique (recommandation 50 : C4b–C6). Mme R. est C4a et C4c, sans C4b ni ulcère ; ce n'est plus « C4 » en général qui écarte le geste |
| R4 — pansements | `I83_pop2.html` (`i83-ulcere-local`) | Les critères de jugement sont explicités : aucun pansement n'a raccourci le **délai** de cicatrisation ; l'iode cadexomère et l'argent augmentent peut-être la **proportion** cicatrisée à une date donnée, avec une certitude faible, sans remplacer la compression |
| R4 — hémorragie sous apixaban | `I83_b.html` (Mme F.) | La règle « comprimer, ne pas arrêter » est limitée au saignement que la compression arrête ; un saignement persistant ou retentissant relève de l'urgence, où interruption ou antagonisation se décident au cas par cas |
| Nomenclature | `I83_pop1.html` (Autres causes) | Renvoi écrit **I50 — Insuffisance cardiaque (C-01-Cardiologie)** |
| SCI-01 — reflux « que debout » | `I83_c.html` (`Science → examen`) | « Le reflux se recherche de préférence debout, avec une manœuvre de provocation adaptée au segment ; un examen couché peut le sous-estimer » |
| SCI-02 — randomisation mendélienne | `I83_pop3.html` (`i83-gen`) | Variants employés comme instruments ; réduction de certains biais sous les hypothèses de validité ; limites par pléiotropie (définie) et structure de population |
| SCI-03 — fer et TGF-β | `I83_c.html` (À retenir, îlot microcirculation) et `pareto-i83-sci` | La chaîne est présentée comme modèle inflammatoire ; le rôle propre du fer reste imparfaitement établi ; le TGF-β « participerait » à la fibrose |
| Précision Kf (facultative) | `I83_c.html` (Starling) | K<sub>f</sub> est défini comme coefficient de filtration, produit de la conductivité hydraulique par la surface d'échange |
| Cohérence œdème (Pharmacologie) | `I83_d.html:75` | Seule la composante bilatérale a disparu ; la part gauche persistante oriente vers la maladie veineuse, sans exclure une autre cause |
| EHIT III dans le glossaire | `glossary/i83.py` (annexe) | Les classes III et IV relèvent d'une anticoagulation curative, la classe III avec échographie hebdomadaire jusqu'à rétraction (American Venous Forum et Society for Vascular Surgery, 2021) |

## Vérification indépendante et précisions ajoutées

Un sous-agent vérificateur, en lecture seule, a relu le diff contre les rapports Codex et recherché les occurrences résiduelles. Il ne relève **aucune correction bloquante**. Ses cinq précisions non bloquantes sont appliquées :

| Point | Fichier | Correction |
| --- | --- | --- |
| Occurrence résiduelle du seuil profond | `I83_c.html` (À retenir, îlot écho-Doppler) | 0,5 s superficiel ou perforante ; 1 s fémorale commune, fémorale et poplitée |
| Ambiguïté « recommandation 50 » | `I83_b.html`, `I83_c.html` | « recommandation 50 de l'ESVS 2022 », distincte de la recommandation 50 de l'ESVS 2021 sur la thrombose superficielle |
| Cohérence avec la nouvelle définition de K<sub>f</sub> | `I83_c.html` (Starling) | L'inflammation augmente K<sub>f</sub> et diminue σ ; la fuite protéique relève de σ |
| Argent face au pansement non adhérent | `I83_pop2.html` (Pansements, Source) | Seul résultat de certitude modérée du réseau de Norman 2018 mentionné ; référence ajoutée à la rubrique Source |
| Fer et manchons de fibrine | `I83_pop1.html` | « le fer pourrait entretenir un stress oxydatif » ; rôle des manchons dans l'ulcère qualifié d'hypothèse discutée |

Le vérificateur a confirmé le nombre de 59 essais du réseau (78 essais inclus) sur le résumé PubMed de Norman 2018 ; il n'a pas relu le texte primaire de l'ESVS 2022 ni de l'AVF/SVS 2021.

## Périmètre et annexe

Sept fichiers `chapters/I83/` sont déclarés dans `livraison.json`. `glossary/i83.py` est hors du périmètre de `tools/livraison.py` (seuls les fichiers `chapters/` y sont acceptés) : il figure sous `complements/glossary/i83.py`, avec empreintes d'origine et proposée dans `complements_hors_manifeste`. Le diff complet contre `main` `8d6deee` est dans `controles/diff_main_8d6deee.diff`.

## Contrôles (base `main` `8d6deee`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I83` | `{}` |
| `test_v7.py --static I83` | OK — 41 239 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| `build_front.py` puis `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I83` (1 360 et 390 px) | 1 923 contrôles, 0 échec (`controles/i83_native_results.json`) |
| `tests/verify_s01_browser.cjs` | 72 contrôles réussis (`controles/s01_browser_results.json`) |
| `test_v7.py I83` | OK |
| `tools/livraison.py check-claude --root <main 8d6deee propre>` | empreintes et chemins conformes |

## Limites

- Couverture CIM-11 non établie ; aucun fragment n'est déclaré achevé.
- Les sources primaires citées (ESVS 2022, Cochrane, AVF/SVS 2021) n'ont pas été téléchargées de nouveau pour ce lot ; les formulations restent en deçà de ce qu'elles établissent.
- Les affirmations négatives de disponibilité OFSP signalées par Codex restent non certifiées par un téléchargement indépendant.
