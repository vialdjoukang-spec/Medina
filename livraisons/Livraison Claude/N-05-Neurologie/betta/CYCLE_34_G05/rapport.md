# Rapport de rédaction — G05 (cycle Betta 34, leçon 2, agent C34-A1-NEUR, Sonnet 5.5)

G05 — Encéphalite, myélite et encéphalomyélite au cours d’affections classées ailleurs (N-05-Neurologie). Rédaction fondée uniquement sur `recherche.md` et `sources.json` (18 sources, S1 à S18).

## Fichiers (octets) et empreintes SHA-256
```
  25774 chapters/G05/G05_a.html
  24499 chapters/G05/G05_b.html
  18968 chapters/G05/G05_c.html
  10406 chapters/G05/G05_d.html
  25428 chapters/G05/G05_pop1.html
  13387 chapters/G05/G05_pop2.html
   9623 glossary/g05.py
 128085 total
c254a19c2453be774ead01a42cc26817a38b6d482891abb8cc12ae6cd44b69c1  chapters/G05/G05_a.html
42be1157980dbeffc52f52c5acdc18619b0c36d674dbe3e406e9ea10f4cd5946  chapters/G05/G05_b.html
8addd26c54b67cb51a3c19f7a163f3d5c0896cdbb400f7dcb54ee7dbc47fdd12  chapters/G05/G05_c.html
92f3e5d43da21000f8b807f00b3f81559628eb96d8857fe09b25f65da2057fb5  chapters/G05/G05_d.html
df6b42575365734bfd689cc5ae4b10f610561c14e518172ac03b6e64ab15644a  chapters/G05/G05_pop1.html
f8ba41d1c49dc6cf8af4ff998549550e3deaad362dc7f2868a672e018f219460  chapters/G05/G05_pop2.html
a9b461a5c5e32c932c2cbf80d9b3964bb76f57737346cc7bbb28d632eccd2ec5  glossary/g05.py
```

## Contenu
- Quatre onglets : Pathologie (îlots 0 à 12 ; dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (5 îlots, tableau diagnostics × associations du liquide, 3 quiz de cas), Sciences (anatomie, immunologie, physiologie du liquide ; 2 schémas SVG légendés), Pharmacologie (5 îlots : classes, doses sourcées, alerte d’interactions, adaptation rénale, médicaments à éviter).
- 42 fenêtres `data-pop` dont 12 Pareto ; monographies : aciclovir, ganciclovir, foscarnet, amoxicilline/ampicilline, pénicilline G, pyriméthamine-sulfadiazine, brivudine ; deux contentieux présentés en fenêtre (durée de l’aciclovir : 10 jours suisse contre au moins 14 jours DGN ; dexaméthasone et Listeria) ; aide mnémotechnique marquée « non critère officiel ».
- Chaque paragraphe porte `data-src` (identifiants S1 à S18) ; section de références générée depuis `sources.json`.

## Auto-contrôle (cahier W)
- HTML bien formé sur a+b+c+d et sur les fenêtres ; identifiants uniques, tous préfixés `g05` ; toute clé `data-k` a son `template data-pop`, aucune fenêtre orpheline ; clés Pareto `pareto-g05-…` ; `data-cover` valides.
- Moteur `build_medina.audit` (copie hors dépôt, glossaire g05 ajouté) : 0 abréviation non couverte ; ratio Pareto calculé sans erreur. Aucun parcours navigateur exécuté.
- Aucun fichier hors du dossier de la leçon modifié ; aucun `git`.

## Lacunes (reprises du dossier, non comblées)
- Aucune source suisse spécifique à l’encéphalite ; incidences danoises et allemandes.
- ESCMID 2016, EAN/EFNS, texte intégral IUSTI 2020 non lus ; nombre de critères mineurs du consortium non lu (non donné) ; rattachement de l’encéphalite à EBV non confirmé ; fréquence suisse de la panencéphalite sclérosante subaiguë non lue.
- Aucune information professionnelle suisse lue pour foscarnet, brivudine, pyriméthamine, sulfadiazine, pénicilline G, ceftriaxone : mécanismes d’action et essais non repris. Valeurs normales du LCR absentes (seuils de décision seulement). Trypanosomiase, Chagas, Naegleria, méningo-encéphalite à éosinophiles, tuberculose : codage seulement.
- Les définitions de codes du glossaire reprennent les libellés du dossier (BfArM/OFS), non les libellés complets de la classification ; développements littéraux de SNG, TPLA, LCMV, FTA-ABS fournis par convention d’usage.

Audit différé — revue IA, distincte d’une validation médicale humaine.
