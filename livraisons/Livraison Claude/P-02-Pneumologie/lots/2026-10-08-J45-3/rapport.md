# Lot J45-3 — J45 — Asthme (P-02-Pneumologie)

## Objet

Ce lot remplace `2026-10-08-J45-2` (tête `c3dd8cd`, reçu par Codex en `c545b79`, non intégré). Il lève la réserve bloquante **J45-MED-02**, qui demandait d'aligner les tests indirects et le mannitol sur la norme Hallstrand 2018, en partant de la [réception J45-2](../../../../../docs/collaboration/reviews/2026-10-08/PR12_C3DD8CD_J45_2/RECEPTION.md). Base : `main` `c545b79cb604347c7c1f38c5c8fe03126daafbc9`, sans changement des sources J45. Le détail figure dans `verification/corrections_codex_2.md`.

## Source primaire lue

Hallstrand TS et al., « ERS technical standard on bronchial challenge testing: pathophysiology and methodology of indirect airway challenge testing », Eur Respir J 2018;52:1801033. Le **texte intégral** est le PDF de l'éditeur, 18 pages, dont les pages 1 à 12 ont été lues. Il vient de la copie de l'Internet Archive, puisque l'ERJ, ersnet et Pure Amsterdam UMC renvoient 403, qu'il n'existe pas d'accès ouvert sur Europe PMC et aucun PMCID. La taille du fichier correspond à celle annoncée par l'Université de Gand.

## Corrections

| Fichier | Avant | Après (source) |
| --- | --- | --- |
| `J45_c.html`, § 3.2 | « Plus spécifiques, donc utiles pour confirmer, et reflètent l'inflammation » | « Tendent à être plus spécifiques de l'asthme mais moins sensibles ; ils aident à confirmer dans un contexte clinique compatible ; leur réponse est associée à l'inflammation » (introduction, figure 2) |
| `J45_c.html`, tableau, ligne mannitol | « Prédit la réponse aux corticostéroïdes » | « Sert à suivre l'effet du traitement de fond et à ajuster la dose de corticostéroïde inhalé » (p. 11) |
| `J45_c.html`, mécanismes, ligne effort | « Reflètent une inflammation active » | « Passe par des médiateurs de cellules des voies aériennes ; pas d'afflux cellulaire net après l'effort » (p. 4) |
| `J45_c.html`, encadrés | Affirmations catégoriques | Formulations alignées sur la norme (p. 5) ; référence DOI ajoutée |
| `J45_pop2.html`, tests indirects | Explications sans source | Mécanisme (mastocytes, éosinophiles, nerfs sensitifs) ; sensibilité semblable dans l'asthme léger ; spécificité limitée de tous les tests de provocation (GINA 2026, p. 34) ; adénosine réservée à la recherche |
| `J45_pop2.html`, mannitol | Seuil GINA seul | Positif pour une chute ≥ 15 % ou de 10 % entre deux doses ; sensibilité de 40 à 59 %, spécificité de 78 % à près de 100 % (p. 10-11) ; contre-indiqué si VEMS < 70 % ou < 1,5 L (p. 10) |
| `J45_pop2.html`, préparation et contre-indications | Causalité non sourcée | Délais du tableau 1 (8 h et 36 h) ; avant un test d'effort ou d'hyperventilation, VEMS ≥ 75 % et saturation > 94 % (p. 5) |
| `J45_pop4.html`, Pareto Examens | « Spécifiques, servent à confirmer » | « Plutôt spécifiques mais moins sensibles, aident à confirmer avec la clinique » |

**Divergence traitée selon la règle du propriétaire.** Pour l'hyperventilation eucapnique, GINA 2026 (encadré 1-2), plus récent, retient une chute ≥ 15 % et reste dans le texte. La norme ERS 2018 (p. 8) retient en général ≥ 10 %.

## Contrôles (base `main` `c545b79`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py J45` | `{}` |
| `test_v7.py --static J45` | OK — 38 844 mots, 47 fenêtres, 8 quiz, 8 Pareto |
| `tools/insert_justifications.py --course J45` | 15/15 |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs J45` (1 360 et 390 px) | 2 340 contrôles, 0 échec |
| `python3 -m unittest discover -s tests` | OK |
| `tools/livraison.py check-claude --root <main c545b79 propre>` | empreintes et chemins conformes |

## Réserves restantes

- Méthacholine : la norme ERS 2017 n'est toujours pas relue en texte intégral ; les catégories de PD20 et les contre-indications restent retirées.
- La relecture exhaustive relève de l'audit de Codex.
- Limitations de remboursement non relues ; CIM-11 non établie.
