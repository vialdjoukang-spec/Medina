# Rapport Sciences — J45 — Asthme (P-02-Pneumologie)

## 1. Fichiers modifiés
- `chapters/J45/J45_c.html` : **panneau pS seulement** (pE identique octet pour octet à HEAD, vérifié). Panneau réécrit : sept disciplines au lieu de six.
  - j45-sa Anatomie : innervation en tableau avec niveau de preuve (vague/M3, autorécepteur inhibiteur, sympathique, voie NANC au monoxyde d’azote) ; bêtabloquants : composante cholinergique (Ind 1989), GINA 2026 p. 67.
  - j45-sh Histologie et remodelage : tableau « démontré / supposé » (Saglani, Grainge, Dunican, Berry, Persson, CASCADE).
  - j45-sp Physiologie : Poiseuille et limites, inspiration profonde (Skloot), hyperréactivité directe/indirecte (tableau), limitation du débit, distension dynamique.
  - j45-si Immunologie : alarmines, ILC2, réponses immédiate/tardive chiffrées, tableau des voies avec essais, non type 2 (brodalumab négatif).
  - **Nouveau** j45-s-crise / j45-sx : virus, rapport ventilation/perfusion, hypercapnie sous oxygène, épuisement, acidose lactique, pouls paradoxal, ventilation mécanique, asthme mortel ; figure 9 ; tableau étapes → décision.
  - j45-sb Biochimie : tolérance bêta-2, salmétérol seul, corticorésistance du fumeur.
  - j45-sg Génétique et environnement : héritabilité, 17q21, cadhérine CDHR3 (écrite en toutes lettres), filaggrine, hypothèse hygiéniste et limites, tableau.
  - Sections « Interprétation guidée » génériques supprimées ; sources en `p.src` (liens `data-reference-source`) ; bouton `pareto-j45-sci`.
- `chapters/J45/J45_pop4.html` : nouveau `pareto-j45-sci` ; `pareto-j45-urg` réaligné sur l’onglet 2 et GINA 2026 ; corrections ponctuelles dans clin, diag, crit.

Identifiants conservés. Cibles de justification préservées : « distension dynamique » (occurrence 1 dans j45-sp), « transrépression » (unique dans j45-sb), « Les éosinophiles, les IgE et la FeNO » (occurrence 1 dans j45-si).

## 2. Matrice des corrections (accès : PubMed = résumé lu ; GINA = texte intégral lu, PDF du 05.2026, consulté le 08.10.2026)
| Passage | Problème | Correction | Source |
|---|---|---|---|
| Anat., bêtabloquants | Mécanisme réduit au blocage de l’adrénaline | Composante cholinergique, mécanisme incomplet | Ind, Am Rev Respir Dis 1989 (résumé) ; GINA 2026 p. 67 |
| Immuno., ILC2 | « produisent IL-4 » | Surtout IL-5 et IL-13 | Smith, JACI 2016 (résumé) |
| Immuno., anti-TSLP | « reste efficace car en amont » (causal) | Réduction 56 % ; 41 % si éos < 300 ; « en amont » = interprétation | Menzies-Gow, NEJM 2021 ; Diver, Lancet Respir Med 2021 (résumés) |
| Immuno., réponse tardive | « 4 à 8 h » | Début 3–4 h, pic 6–12 h | Gauvreau, Eur Respir J 2015 (résumé) |
| Physio., oxygène | Cible 93–95 % seule | GINA 2026 : O₂ si < 92 %, cible 92–95 %, ≤ 96 % adulte | GINA 2026 p. 20, 180, 185 |
| Physio., hyperréactivité | Non traitée | Tableau mécanismes + éosinophiles dissociés de l’HRB | Leckie 2000 ; Brightling 2002 ; Skloot 1995 ; Hallstrand 2005 |
| Biochimie, transactivation | « responsable des effets indésirables » | Gènes anti-inflammatoires et métaboliques | Consensus, sans source primaire relue |
| Génétique, héritabilité | « 50–70 % » non sourcé | 82 % (25 306 jumeaux) | Ullemar, Allergy 2016 |
| Génétique, filaggrine | Prévention par traitement précoce « discutée » | Émollients sans effet sur la dermatite à 12 mois | Skjerven, Lancet 2020 |
| Génétique, GWAS | « plus d’une centaine de régions » non vérifié | Régions de l’étude GABRIEL ; IgE non causales | Moffatt, NEJM 2010 |
| Pareto urg | Fréquence cardiaque, saturation < 90 %, 4–10 bouffées/20 min, O₂ 94–98 %, PaCO₂ > 42 | Critères et doses GINA 2026 identiques à l’onglet 2 | GINA 2026 p. 20, 179–185 |
| Pareto crit | « saturation ≥ 95 % » en grossesse, absent de l’onglet 2 | Formulation de l’onglet 2 | — |
| Pareto clin/diag | Seuils approximatifs | ≥ 3 cartouches/an, ≥ 1/mois (associations) ; ≥ 12 % et ≥ 200 mL | GINA 2026 p. 28, 41 |

## 3. Confirmé sans changement
Générations 0–16/17–23, petites voies < 2 mm ; Poiseuille, 1/0,8⁴ ≈ 2,4 ; point d’égale pression ; spirales de Curschmann, cristaux de Charcot-Leyden, corps de Creola ; voie Gs–AMPc–PKA, voie Gq–M3 ; transrépression NF-κB/AP-1 ; hypokaliémie par redistribution.

## 4. Propositions hors périmètre
1. `J45_pop1.html`, `j45-gaz`, « Épuisement : PaCO₂ &gt; 42 mmHg (5,6 kPa), acidose respiratoire. » → « Insuffisance respiratoire : PaO₂ &lt; 60 mmHg (8 kPa) avec PaCO₂ normale ou élevée, surtout &gt; 45 mmHg (6 kPa) (GINA 2026, p. 185). »
2. `J45_pop1.html`, `j45-remod`, Prévention : « (chaque exacerbation sévère accélère la perte de fonction) » → « Aucun médicament n’a démontré une régression du remodelage. Chez l’homme, des bronchoconstrictions répétées suffisent à épaissir la paroi (Grainge, 2011). Le lien entre exacerbations sévères et perte de fonction est une association. »
3. `J45_b.html`, 8.2 Oxygène : « L’oxygène pur augmente en effet la PaCO₂, notamment parce qu’il lève la vasoconstriction hypoxique et aggrave les inégalités ventilation-perfusion. » → « L’oxygène pur augmente la PaCO₂ (essai randomisé, Perrin 2011) ; la levée de la vasoconstriction hypoxique, qui aggrave les inégalités ventilation-perfusion, en est l’explication proposée. »
4. `J45_a.html`, 3.5 : « Une PaCO₂ normale ou élevée pendant une crise signe l’épuisement respiratoire. » → « Une PaCO₂ normale ou élevée pendant une crise signale une ventilation devenue insuffisante ; sa trajectoire et le contexte indiquent l’épuisement. » La cible « PaCO₂ normale ou élevée » est conservée.
5. **Bloquant** : la copie de travail actuelle de `J45_a.html` contient deux fois « limitation variable du débit expiratoire » dans j45-1. `j45-j-variabilite` échoue (« cible ambiguë (2) »). Il faut ajouter `"occurrence": 1` dans `J45_justifications.json` ou supprimer le doublon.
6. Les Pareto `clin`, `diag`, `tt`, `crit`, `exam` et `pharma` de pop4 résument les autres onglets. L’assembleur doit les resynchroniser après les remises finales.

## 5. Réserves
Hogg 1968 et Strachan 1989 : résumés indisponibles, contenu repris de la physiologie classique. Bochkov 2015 : titre seul consulté. Mécanisme du pouls paradoxal et absence d’innervation sympathique : physiologie classique, sans source primaire relue. Corticostéroïdes et transcription du récepteur bêta-2 : non vérifié, présenté comme in vitro sans importance clinique établie. Le tableau de doses du Box 9-6 de GINA est une image non extractible ; les doses du Pareto suivent l’onglet 2.

## 6. Contrôles
- `python3 test_v7.py --static J45` : **OK** (40 174 mots, 46 fenêtres, 8 quiz, 8 Pareto).
- `verifier_sigles.py J45` : `{}`.
- Sciences Pareto : 3 % du texte couvert.
- `insert_justifications.py --course J45` : 15/15 cibles compilées si `J45_a.html`, `J45_b.html` et `J45_d.html` sont à HEAD ; échec actuel dû à `J45_a.html` (point 5).
- Balises équilibrées dans les deux fichiers.
