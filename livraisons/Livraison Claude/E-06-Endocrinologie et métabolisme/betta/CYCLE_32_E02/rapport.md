# Rapport de rédaction E02 : Hypothyroïdie par carence inapparente en iode

Cycle Betta 32, leçon 1, agent C32-A2-ENDO (rédaction Sonnet 5.5), fragment E-06-Endocrinologie et métabolisme. Rédigé le 14.10.2026.

**Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (dossier `chapters/E02/` et `glossary/`)
| Fichier | Contenu | Taille (octets) |
|---|---|---|
| E02_a.html | En-tête, onglets, plan, îlots 0 à 6 (question clinique à examen) | 24 346 |
| E02_b.html | Îlots 7 à 12 (diagnostic, urgences, prise en charge, suivi, particulières, critères formels et paramètres clés) | 20 838 |
| E02_c.html | Onglet Examens (e-1 à e-6, 4 cas cliniques) et onglet Sciences (Physiologie, Biochimie, Santé publique) | 23 389 |
| E02_d.html | Onglet Pharmacologie (p-1 à p-5) | 9 427 |
| E02_pop1.html | 32 fenêtres de notions | 33 893 |
| E02_pop2.html | 7 monographies et fiches de source, 16 fenêtres Pareto | 17 953 |
| glossary/e02.py | 14 abréviations ou codes définis lettre à lettre, ajouts conditionnels | 5 613 |

Total : 55 fenêtres (39 de contenu, 16 Pareto), 4 quiz de cas, 3 encadrés `alert`, 2 figures SVG noir et blanc légendées.

## Sources du dossier utilisées
S1 à S7 et S9 à S20 sont citées. S8 (Revue médicale suisse 2014) n'est pas citée, comme annoncé. Les fenêtres lient chaque affirmation à sa source ; les informations professionnelles suisses (S17 à S19) sont citées par leur numéro d'autorisation, sans lien web.

## Contrôles de l'auto-contrôle du cahier W
- HTML bien formé (analyse de balises) : aucune erreur, aucune balise ouverte.
- Identifiants uniques et préfixés `e02` ; clés de fenêtres préfixées `e02-` ou `pareto-e02-`.
- Toutes les clés `data-k` existent comme `data-pop` ; aucune fenêtre orpheline.
- Couvertures Pareto : tous les îlots cités existent.
- Audit d'abréviations `build_medina.audit()` : `{}`.
- Classes de la liste fermée uniquement.

## Respect du dossier et lacunes
- Aucune donnée absente du dossier n'a été utilisée. Les valeurs de la vignette (TSH de 5,8 mU/L, etc.) sont fictives et signalées comme telles.
- Les raisonnements de l'auteur (iode traite le substrat, lévothyroxine remplace le produit ; recontrôle de la TSH après correction de l'iode ; principe de sécurité des contre-indications) sont signalés comme tels dans le texte.
- Les critères formels de la section 12 sont une construction pédagogique, présentée comme telle : aucun critère publié propre à E02.
- Aucune recommandation suisse ou européenne propre à l'HIC iodoprive ; aucun essai iode contre lévothyroxine.
- ETA 2014 (grossesse, enfant) lue en résumé seul : seuils trimestriels de TSH et doses non repris. TRUST, méta-analyse bernoise, EFSA, Pearce 2016, Gowachirapant 2017, Segna 2018 lus en résumé.
- Sciences : l'anatomie et l'histologie de la thyroïde sont omises, car le dossier ne contient aucune source sur elles (seulement des éléments de goitre et d'échographie). Trois disciplines sont traitées : physiologie, biochimie, santé publique.
- Pharmacologie : la section des effets indésirables de l'information professionnelle d'Euthyrox n'a pas été reproduite dans le dossier ; elle est signalée comme lacune dans le chapitre. Posologie de l'iodure de potassium 65 mg non reprise.
- Valeurs D-A-CH et valeurs d'apport de l'OSAV en image : non utilisées.
- La divergence calcium, fer, aluminium (2 heures, information professionnelle 2023) et espacement de 4 heures (ETA 2013) est présentée telle quelle, la source suisse la plus récente primant.
