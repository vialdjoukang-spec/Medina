# Lot I83-HARMONISATION-2 — I83 — Varices des membres inférieurs (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I83-HARMONISATION` (tête `b526d9d`, reçu par Codex en `dbe4063`, non injecté). Il reprend toutes les harmonisations de ce lot et répond aux six réserves de la [réception Codex](../../../../../docs/collaboration/reviews/2026-10-08/PR12_B526D9D_I83_HARMONISATION/RECEPTION.md). Base : `main` `dbe40639e38bd2666641731bcf500ed5a75d147f`, dont les sources I83 sont identiques à `8d6deee`. I83 reste le seul chapitre actif de Claude.

Les citations ont été relues par un sous-agent documentaliste dans les textes primaires (PubMed et copies locales des référentiels), avant rédaction.

## Réponse aux réserves de la réception

| Réserve Codex | Décision | Correction et preuve |
| --- | --- | --- |
| Glossaire bloqué : EHIT → ARTE (SVS/AVF/AVLS 2023) | **Corrigé, et étendu au cours** | Nouvelle entrée `ARTE` (Ablation Related Thrombus Extension) ; `EHIT` devient l'ancien terme (E = Endovenous, graphie de la recommandation 11.1.1). Le cours suit la même terminologie dans `I83_b.html` (îlot ablation), `i83-thermique` (Complications, Conduite) et le Pareto des traitements. Conduite actuelle : pas d'écho-Doppler précoce systématique chez l'asymptomatique à risque moyen (11.1.1, 1B) ; écho-Doppler devant un symptôme (11.1.4, 1A) et chez l'asymptomatique à haut risque (11.1.3, consensus) ; ARTE symptomatique : anticoagulant oral direct plutôt qu'antagoniste de la vitamine K (11.3.4, 1C) ; ARTE III–IV asymptomatique : même traitement (11.4.1, consensus), jusqu'à rétraction, durée au jugement du clinicien (11.4.2, consensus) ; thromboprophylaxie suggérée chez le patient à haut risque (11.2.1, 2C). Les conduites 2021 des classes I et II sont présentées comme rarement applicables. Source : Gloviczki et al., J Vasc Surg Venous Lymphat Disord 2023, partie II, § 11 (PMID 37652254). |
| *(erreur découverte en vérifiant)* fréquence de 1,7 % | **Corrigé** | Le texte primaire donne 1,7 % pour l'ensemble « EHIT II à IV ou thrombose profonde », 1,4 % pour les classes II à IV seules. Le cours et le glossaire attribuaient 1,7 % à l'EHIT seule. |
| Pansements : ne pas extrapoler au « délai » | **Corrigé** | `i83-ulcere-local` : « aucun pansement n'a montré de bénéfice fiable sur la cicatrisation complète » ; la mention du délai est retirée. |
| Iode cadexomère : sous-ensemble méta-analysé | **Corrigé, avec source exacte** | La donnée provient d'O'Meara et al., Cochrane 2014 (CD003557.pub5), et non de Norman 2018 : 11 essais inclus, RR 2,17 (IC 95 % 1,30–3,60) sur **quatre** essais, cicatrisation complète entre 4 et 12 semaines. L'ESVS 2022 (§ 6.1.3) écrit par erreur « 11 essais ». Le total de 212 participants n'a pas pu être relu (texte intégral Cochrane inaccessible) et n'est donc pas écrit. L'argent est rattaché à Norman 2018 (avantage face au pansement non adhérent seulement). |
| Recommandation 50 : force exacte | **Corrigé** | Texte primaire : « treatment may be considered » pour une perforante incompétente isolée ou résiduelle, jugée significative, en C4b–C6 ; classe IIb, niveau C. `I83_b.html` et `I83_c.html` emploient « peut être envisagé (classe IIb, niveau C) ». |
| CEAP : graphie « C2,3,4a,c,S » | **Maintenu en `C2,3,4a,c (s)`, justification** | Lurie 2020 prescrit un indice s (symptomatique) ou a (asymptomatique) pour chaque classe clinique, sans exemple complet. Le guide de notation de l'American Venous Forum précise : « should be in lower case, in parenthesis at the end of the C designation. Example: … C2,3(s) ». La graphie « C2,4b,S » est celle d'Eklöf 2004, antérieure à la révision. La graphie du cours suit donc la convention 2020 ; le descripteur (s) figure dans les deux notations complètes du cas. |
| Traçabilité SCI-03 et K<sub>f</sub> | **Complété** | Synthèse inflammatoire : références Bergan et al. 2006 et Raffetto et Khalil 2008, déjà citées dans le développement. Starling : la forme classique est présentée comme simplifiée, indiquant le sens des variations sans quantifier l'œdème individuel (Levick et Michel, 2010). |

## Harmonisations reprises du lot précédent

Notation CEAP du cas ; seuil de reflux de 1 s limité aux veines fémorale commune, fémorale et poplitée (trois Pareto et îlot écho-Doppler) ; recherche du reflux debout ; perforante (convention descriptive séparée de l'indication) ; hémorragie sous apixaban ; renvoi I50 ; randomisation mendélienne ; modèle inflammatoire ; K<sub>f</sub> et σ ; œdème sous amlodipine. Le détail figure dans [le rapport du lot précédent](../2026-10-08-I83-HARMONISATION/rapport.md).

## Périmètre

Sept fichiers `chapters/I83/` dans `livraison.json`. `glossary/i83.py` (entrées ARTE et EHIT) est hors du périmètre de `tools/livraison.py` : il figure sous `complements/`, avec empreintes, dans `complements_hors_manifeste`. Diff complet contre `main` : `controles/diff_main.diff`.

## Contrôles (base `main` `dbe4063`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I83` | `{}` (ARTE défini) |
| `test_v7.py --static I83` | OK — 41 409 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I83` (1 360 et 390 px) | 1 923 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` | 72 contrôles réussis |
| `test_v7.py I83` | OK |
| `tools/livraison.py check-claude --root <main dbe4063 propre>` | empreintes et chemins conformes |

## Limites

- Non relus dans le texte primaire : le total de 212 participants et la certitude GRADE de la donnée cadexomère ; la recommandation ESVS 2022 sur l'occlusion de la veine fémorale commune, conservée sans changement dans `i83-thermique`.
- Les affirmations négatives de disponibilité OFSP restent non certifiées.
- Couverture CIM-11 non établie ; aucun fragment n'est déclaré achevé.
