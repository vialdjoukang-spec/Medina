# Rapport de rédaction : E30, Anomalies de la puberté, non classées ailleurs (E-06-Endocrinologie et métabolisme)

Cycle Betta 34, leçon 2. Agent C34-A2-ENDO (rédaction, Sonnet 5.5). Date : 15.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers
- `chapters/E30/E30_a.html` : 27220 octets
- `chapters/E30/E30_b.html` : 23924 octets
- `chapters/E30/E30_c.html` : 27893 octets
- `chapters/E30/E30_d.html` : 10014 octets
- `chapters/E30/E30_pop1.html` : 19895 octets
- `chapters/E30/E30_pop2.html` : 14295 octets
- `glossary/e30.py` : 24 entrées conditionnelles (PPC, PPP, GnRH, LH, FSH, hCG, hMG, DHEAS, RCCP, DGKED, SIAMS, Endo-ERN, LA, MKRN3, DLK1, KISS1, KISS1R, GNAS, XY, McCune-Albright, Silver-Russell, Wyk-Grumbach, Testosteron-Mepha, ICD-10-GM), chacune ajoutée seulement si la clé est absente des glossaires existants.
- Fenêtres : 51 templates (10 Pareto, dont mnémotechnique « aide pédagogique, non critère officiel »). Quiz : 5 (4 dans l'onglet Examens, 1 dans la pathologie). Environ 14 500 mots.

## Structure
Quatre onglets : Pathologie (îlots 0 à 12, dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (5 îlots dont hiérarchie avec référence fonctionnelle nommée, fiches, tableau diagnostics × biologie, 4 quiz de cas), Sciences (Anatomie, Histologie, Physiologie, Biochimie, Génétique ; un schéma SVG légendé par science, blocs « Science → clinique »), Pharmacologie (4 îlots : stratégie, doses sourcées, mises en garde, monographies en fenêtres). Plan monographique, sans îlot ni tableau consacré au code CIM ; le périmètre n'est évoqué qu'en une phrase (la PPC idiopathique relève d'une autre rubrique).

## Sources utilisées (recherche.md / sources.json)
S1 à S20 ; S21 (Hess et Zumsteg 2017) non utilisée faute d'accès. Aucune donnée extérieure au dossier. Citations dans le texte sous forme « (source, année) ».

## Auto-contrôle (cahier W)
HTML bien formé (aucune balise non fermée ou mal imbriquée) ; identifiants uniques, tous préfixés `e30` ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline ; tous les Pareto couvrent des îlots existants ; audit des abréviations (`build_medina.audit`) = `{}` avec le glossaire e30 ajouté. Contrôle exécuté hors racine, sans modifier `chapters/`, `glossary/` ni `chapters.json`.

## Lacunes (reprises du dossier, non comblées)
Aucune recommandation suisse de société savante lue ; guide danois en version de consultation ; aucune incidence suisse (cohorte de Zurich de 1983 seulement) ; Endo-ERN et SIAMS lues en partie ; FI de Decapeptyl retard absente (monographie sans dose) ; traitement du McCune-Albright et de la testotoxicose chez la fille non documenté ; mécanisme de désensibilisation par les analogues de la GnRH, mécanisme d'avance de l'âge osseux et mécanisme de l'hCG non lus ; définition détaillée des cinq stades de Tanner non reprise ; aucune donnée d'interaction médicamenteuse ni FI des progestatifs, gels de testostérone et gonadotrophines. Les vignettes et le cas récapitulatif sont fictifs et signalés comme tels. Divergences présentées sans arbitrage : IRM du garçon (SIAMS, guide danois, revue italienne), fréquence des lésions cérébrales du garçon (6 à 8 % contre 25 à 60 %).
