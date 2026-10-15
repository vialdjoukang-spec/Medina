# Audit linguistique agressif — D50, Anémie par carence en fer

Mission ALPHA1-CLAUDE-D50-LANG · génération 1 · branche `claude/alpha1/d50-lang-g1` · base `f664dd9e` · modèle et effort conformes au manifeste · agent : sous-agent Claude Code (voir accusé issue 107).

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*

## 1. Lecture et contrôle d'entrée

Les empreintes SHA-256 des 7 fichiers (`D50_a`, `_b`, `_c`, `_d`, `_pop1`, `_pop2`, `glossary/d50.py`) ont été recalculées avant l'analyse : **7/7 conformes** au manifeste. Les 7 fichiers ont été lus en entier (texte, tableaux, légendes, étiquettes SVG, quiz, Pareto, `div.alert`, `div.key`, glossaire). Le HEAD (`f664dd9e`) est postérieur au snapshot du manifeste (`bfc4576b`) par des commits d'activation seulement ; les sources sont identiques.

## 2. Résultat en bref

| Indicateur | Valeur |
|---|---|
| Propositions locales (`propositions.json`) | **164** (ancien exact, unique, sans chevauchement : 164/164) |
| dont cohérence typographique de « < », « > », « ≤ » (mécaniques) | 42 |
| dont corrections rédactionnelles et grammaticales | 122 |
| Renvois à instruction médicale ou à vérification de source | **11** |
| Constats structurels (non locaux) | 7 |
| Règle globale à arbitrer | 1 (espaces insécables, ~1 470 endroits) |
| Fond médical modifié | aucun (chiffre, dose, seuil et source intacts) |

Répartition par fichier : `D50_pop1` 77, `D50_b` 32, `D50_pop2` 20, `D50_c` 11, `D50_d` 11, `D50_a` 10, `glossary/d50.py` 3. Le texte est globalement soigné : aucune faute d'orthographe lexicale, de double espace, de mot répété ni d'apostrophe droite n'a été détectée par le balayage mécanique.

## 3. Ce qui mérite d'être corrigé en priorité

1. **Erreur de syntaxe visible** : « maladies inflammatoires chroniques de l'intestin inflammatoires » (fenêtre seuils de ferritine) ; « la biodisponibilité monter » (fenêtre bilan quotidien, verbe modal omis) ; « Le total hebdomadaire reste au plus de 1000 mg » (Ferinject®) ; « ponctuation `. ;` » entre deux références (fenêtre hypersensibilité).
2. **Ambiguïtés de référent** (8) : « son efficacité » sans antécédent (îlot 2), « si elle ne l'est pas » (ferritine ou protéine C réactive, îlot 7), « Elle » sans antécédent dans l'encadré de la fenêtre ferritine ng/mL, « Elle récidive » (carence ou anémie ?), « la réduit » (acidité ou absorption ?), « la fraction circulante est une protéine de phase aiguë » (la ferritine est visée).
3. **Verbes mal employés** : un produit qui « contre-indique » une intolérance (Tardyferon®, Ferrum Hausmann®) ; « aggrave la performance physique » ; « le choix pèse » ; « décider l'urgence » (×2) ; « rappelle de mesurer ».
4. **Style télégraphique et infinitifs injonctifs** (guide de rédaction § 2) : 11 énumérations sans articles (« exige personnel formé, réanimation disponible et surveillance ») et 8 cellules à l'infinitif (« Suspendre le fer habituel et réévaluer », « Éviter dimercaprol… »).
5. **Cohérence** : « 30 minutes » en chiffres partout sauf 9 occurrences en toutes lettres ; « Intestin inflammatoire » (deux endroits) et « Maladie inflammatoire intestinale » alignés sur « maladie inflammatoire chronique de l'intestin » ; « et coll. » / « et al. » ; « n°77 » / « n° 77 » ; espace « < 130 » homogène ; numérotation des figures dans l'ordre de lecture des onglets (la « Figure 5 » précède les figures 1 à 4 : cinq entrées à appliquer ensemble).
6. **Noms d'espèce** : *Helicobacter pylori* en italique (3 occurrences).

## 4. Renvois (aucune reformulation proposée)

Onze passages ne sont pas reformulés parce que le moindre changement pourrait déplacer un sens médical ou parce que la source n'a pas été lue :

- **« Plus de 20 cigarettes »** après « 10 à 19 » : la valeur 20 n'est couverte par aucune tranche ; formulation exacte à lire dans la table OMS 2024.
- **« baisse avec l'âge, jusqu'à 74 % »** (sérologie cœliaque) : baisse *de* 74 % ou *jusqu'à* 74 % ? À trancher sur la BSG 2021.
- **« seuils de 4 à 10 »** sans unité (test immunochimique fécal), **« carence persistante »** (fer ou phosphate ?), **« son seul seuil obstétrical de 30 µg/L »** (attribué au guide Onkopedia alors que le seuil appartient à l'avis de gynécologie suisse), **« rendement … environ deux tiers »** sans dénominateur, **« Normale basse ou haute »** (ferritine de l'anémie réfractaire), **« gélule » / « capsule »** pour ferro sanol®.
- **Graphies** « œso-gastrique » (×2) et « héphæstine » : aucune entrée de dictionnaire trouvée ; non tranché.

## 5. Constats structurels (non appliqués, suppression de contenu)

- Le paragraphe « Tri fécal actualisé » et sa référence sont quasi identiques dans `D50_b` (îlot 7) et `D50_c` (îlot e-4), alors qu'une fenêtre `d50-fit` existe.
- `D50_d`, îlot p-3 : le second encadré « Interactions importantes » reprend le premier, et l'alinéa « Association » reprend sa dernière phrase.
- Références doublées vers la même URL (BSG 2021) dans plusieurs îlots et fenêtres.
- « FI » (fenêtres) / « information professionnelle » (cours) et « KDIGO » / nom développé coexistent ; « Patient Blood Management » reste en anglais dans une fenêtre.
- Le mot vert « H1 » de la fenêtre hypersensibilité renvoie à la fenêtre qui le contient.

## 6. Règle globale à arbitrer — espaces insécables

Aucun des 7 fichiers ne contient d'espace insécable ; les cours I63, E11 et N17 (sondage sur les onglets `_a`) non plus, et aucun traitement n'existe dans le moteur. La typographie française standard exige une espace insécable avant « ; : ! ? » et « » », après « « », avant « % » et avant les unités. Le dry-run (`scripts/espaces_insecables_dryrun.py`) dénombre dans les nœuds texte : **871** positions avant ; : ! ? et », **8** après « « », **108** avant « % », **480** avant une unité. Un guide suisse (educa.ch, résumé obtenu par recherche web) indiquerait que l'administration fédérale omet cette espace ; la règle suisse n'est pas confirmée. Aucune proposition individuelle n'est donc émise : décision à prendre d'abord (Vial ou mission d'intégration), puis application scriptée sur les nœuds texte, suivie de `build_medina.audit()` et `test_v7.py`.

## 7. Vérification mécanique

`scripts/verifier_propositions.py` : chaque `ancien` apparaît **exactement une fois** dans son fichier (164/164, résultat dans `verification_unicite.json`), aucun chevauchement, application simulée en mémoire sans autre balise ajoutée que `<i>`, glossaire Python compilable. Aucun fichier source n'a été modifié.

## 8. Première vérification et lacunes

- Première vérification : usage de l'espace insécable en français de Suisse, [guide educa.ch](https://www.educa.ch/sites/default/files/2023-12/Guide_linguistique.pdf) — niveau **résumé** (le PDF n'a pas pu être chargé ; extrait restitué par recherche web).
- Lacunes : aucun dictionnaire lu en texte intégral ; convention fédérale suisse (bk.admin.ch) non lue ; aucun build ni rendu navigateur ; aucune vérification médicale ; étiquettes SVG lues sans proposition.

## Tableau de bord final

| Cours | Fichiers lus | Propositions | Renvois | Règle globale | Sources modifiées | Empreintes |
|---|---|---|---|---|---|---|
| D50 | 7/7 | 164 | 11 | 1 | 0 | 7/7 conformes |
