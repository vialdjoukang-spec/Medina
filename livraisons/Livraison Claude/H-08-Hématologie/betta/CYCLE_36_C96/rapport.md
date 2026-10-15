# Rapport — C96 Tumeurs malignes des tissus lymphoïde, hématopoïétique et apparentés, autres et non précisées (cycle Betta 36, leçon 1, agent C36-A3-HEM, rédaction Sonnet 5.5)

Date : 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (dossier `livraisons/Livraison Claude/H-08-Hématologie/betta/CYCLE_36_C96/`)
chapters/C96/ : C96_a.html 28919 o ; C96_b.html 37110 o ; C96_c.html 33815 o ; C96_d.html 15838 o ; C96_pop1.html 19568 o ; C96_pop2.html 18852 o ; glossary/c96.py 13139 o ; rapport.md. Environ 15 600 mots, 4 quiz de cas fictifs, 4 schémas SVG noir et blanc légendés, 40 fenêtres (dont 6 Pareto).

## Contenu
- Onglet 1 : 16 îlots (question clinique à trois vignettes, nosologie CIM-10-GM 2024 et exclusions D47.0/C94.3-/Q82.2, épidémiologie, mécanismes des trois familles, causes, anamnèse, examen, diagnostic et différentiel, urgences, HCL de l'adulte, HCL de l'enfant, tumeur à mastocytes, sarcomes, pronostic et suivi, situations particulières, critères formels `div.alert` puis paramètres clés `div.key`), 3 Pareto.
- Onglet 2 : 6 îlots (questions-examens avec gold standard, immunohistochimie et BRAF V600E, imagerie/poumon/axe hormonal, tryptase et KIT D816V, configurations biologiques, 4 quiz), 1 Pareto.
- Onglet 3 : 4 sciences (histologie, génétique, biochimie, physiologie), 4 schémas, 1 Pareto.
- Onglet 4 : 5 îlots (classes et place avec indication suisse nommée, doses, interactions, effets indésirables, erreurs à éviter), 1 Pareto.

## Sources utilisées
Les 20 sources de `sources.json` : BfArM et intitulés OFS, Euro-Histio-Net adulte et enfant 2013, consensus Histiocyte Society 2022, registre anglais, SCCSS, BRAF et seconds cancers, perte auditive, critères ECNM 2021, Onkopedia mastocytose 2024, registres ECNM (leucémie à mastocytes, allogreffe), revue du sarcome histiocytaire, deux séries de sarcome dendritique folliculaire, FI Swissmedic Rydapt, Ayvakyt, Litak, Zelboraf. Aucune donnée chiffrée hors dossier. Quelques explications de mécanisme (diabète insipide, anaphylaxie, signe de Darier, génétique de la rechute après inhibiteurs) relèvent de la physiopathologie générale ; elles sont signalées comme telles dans le texte.

## Lacunes (reprises du dossier, non comblées)
Aucune recommandation suisse propre sur l'HCL ni sur les sarcomes ; aucune incidence suisse ; résultats LCH-IV et critères du syndrome d'activation mastocytaire non lus ; classement B/C des cytopénies ambigu (seuils retenus comme critères de dommage d'organe, signalé) ; sarcomes à cellules de Langerhans et dendritiques interdigités sans revue thérapeutique ; rien de spécifique pour C96.7 et C96.9 ; FI du dabrafénib, du trametinib, du cobimétinib, de la cytarabine, de la vinblastine et du zolédronate non lues (posologies correspondantes attribuées aux recommandations d'experts) ; aucun chiffre d'adaptation en insuffisance rénale ou hépatique.

## Auto-contrôle (cahier W)
- HTML bien formé (analyseur de balises, pile vide sur la concaténation a-b-c-d), identifiants uniques et préfixés `c96-` ; clés de fenêtres `c96-` / `pareto-c96-`.
- Toutes les clés `data-k` ont leur `template data-pop` ; aucune fenêtre inutilisée.
- Pareto : `build_medina.pareto_ratios` sans erreur.
- `build_medina.audit()` avec le glossaire du dépôt + `c96.py` : aucune abréviation non couverte (`{}`).
- Aucun fichier hors du dossier de la leçon n'a été modifié ; ni `chapters.json`, ni git. Test navigateur non lancé (nécessite l'intégration à la racine).
