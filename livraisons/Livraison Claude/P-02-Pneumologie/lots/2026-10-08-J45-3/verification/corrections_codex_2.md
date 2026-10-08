# J45 — Asthme (P-02-Pneumologie) : levée de la réserve J45-MED-02 (tests indirects)

**Source primaire lue en entier** : Hallstrand TS et al., *ERS technical standard… indirect airway challenge testing*, Eur Respir J 2018;52:1801033. J'ai lu le PDF de l'éditeur (18 p., 566 620 octets) dans sa copie Internet Archive (`web.archive.org/web/2020id_/…/1801033.full.pdf`), pages 1 à 12.

**Accès qui ont échoué** : Europe PMC (aucun PMCID, abonnement requis) ; PubMed MCP (aucun PMCID) ; ERJ et ersnet (403, Cloudflare) ; Pure Amsterdam UMC (403) ; UGent (accès réservé à l'université).

## Passages corrigés (avant → après)

### `J45_c.html`

- **§ 3.2** : « plus spécifiques, donc utiles pour confirmer, et reflètent l'inflammation » → « tendent à être plus spécifiques de l'asthme mais moins sensibles ; aident à confirmer, dans un contexte clinique compatible ; réponse associée à l'inflammation ». Source : introduction, figure 2.
- **Tableau, mannitol** : « prédit la réponse aux corticostéroïdes » → « suivre l'effet du traitement de fond et ajuster la dose de corticostéroïde inhalé ». Source : p. 11.
- **Tableau des mécanismes, effort** : « les tests indirects reflètent une inflammation active » → « passe par des médiateurs de cellules des voies aériennes ; pas d'afflux cellulaire net après l'effort ». Source : p. 4.
- **Encadré physiologie → examens** : « plus spécifiques d'une inflammation active » → « passent par les cellules inflammatoires et tendent à être plus spécifiques de l'asthme ».
- **Encadré physiologie → traitement** : « réduit surtout » → « pris régulièrement atténue… notamment la bronchoconstriction d'effort ». Source : p. 5.
- **Sources** : lien DOI Hallstrand 2018 ajouté.

### `J45_pop2.html`

- **Tests indirects** : nouvelle rédaction.
  - mécanisme : mastocytes, éosinophiles, nerfs (figures 1 et 2) ;
  - spécificité et sensibilité nuancées ; sensibilité semblable dans l'asthme léger ;
  - GINA 2026, p. 34 : spécificité limitée de tous les tests ;
  - associations inflammatoires par test, avec la réserve « études initiales » pour l'adénosine ;
  - mannitol : critère de 10 % entre deux doses, sensibilité de 40 à 59 %, spécificité de 78 % à près de 100 % (p. 10-11) ;
  - adénosine : outil de recherche.
- **Préparation** : l'explication causale non sourcée est remplacée par les délais du tableau 1 (8 h, 36 h) et la justification qu'en donne la norme.
- **Contre-indications** : ajout de VEMS ≥ 75 % et saturation > 94 % (p. 5), puis mannitol contre-indiqué si VEMS < 70 % ou < 1,5 L (p. 10).

### `J45_pop4.html`

- « spécifiques, servent à confirmer » → « plutôt spécifiques mais moins sensibles, aident à confirmer avec la clinique ».

## Contrôles

| Contrôle | Résultat |
|---|---|
| Sigles | `{}` |
| `test_v7.py --static J45` | OK (38 844 mots, 47 fenêtres, 8 quiz, 8 Pareto) |
| `insert_justifications.py` | 15/15 |

## Remarque hors périmètre

Pour l'hyperventilation eucapnique, la norme ERS 2018 retient en général une chute ≥ 10 % (p. 8). GINA 2026 (encadré 1-2) retient ≥ 15 %, seuil repris dans `J45_b.html` et `J45_pop1.html`, que je n'ai pas modifiés.
