# I63 — audit croisé, passe 1

C01-R-HEM (`/root/c01_r_hem`), 2026-10-11T19:42:29.673699+00:00 → 2026-10-11T20:08:43.344587+00:00.

**Verdict : défavorable, corrections requises. Note motivée : 17/20.** Revue IA, sans validation médicale humaine. La seconde passe n’a pas commencé.

Les conduites décisives relues concordent avec leurs sources propres : le chapitre distingue notamment INR FI 1,3/protocole bernois 1,7, les restrictions de Plavix et la double antiagrégation précoce, le palier suisse de Metalyse 17,5 mg, les règles suisses d’Eliquis et la thrombose veineuse I63.6. Les 36 vérifications numériques détaillent population, unité, localisation et limites dans `passe_1.json`.

## Corrections requises

### I63-P1-R1

Le registre local conditionnel ne remplace pas les anciennes entrées réellement chargées. GLA développe G=Ga-/L=-Lactosidase/A=Alpha ; FI sépare artificiellement Fachinformation/information professionnelle lettre par lettre. ATP, calcium/sodium, CYP3A4 et LDL ouvrent des contextes myocardiques, coronariens ou un produit non audité. AVC ne possède aucune définition clinique. Sept approfondissements référencés depuis les glossaires sont absents du fragment S08 et donc silencieusement non proposés (i21-plaquette, i48-aod, i25-d-clopi, sarcomere, i21-d-statine, i48-inr, i21-d-p2y12). Plusieurs définitions générales correctes ne constituent pas en elles-mêmes des erreurs médicales ; la réserve vise les développements erronés, les exemples non vérifiés pour ce chapitre et les approfondissements manquants.

Dans le seul chapitre, développer les termes problématiques et leur donner des fenêtres I63 contextualisées (titres peuvent conserver un symbole officiel présenté comme symbole, sans expansion inventée). Ne pas modifier G partagé. Reprendre les distinctions sodium intracellulaire/natrémie, calcium neuronal/sarcomère, métabolisme de l’apixaban/ivabradine, cible lipidique AVC/ACS et critère ARISTOTLE ischémique/composite. Relire toutes les occurrences, y compris SVG, fenêtres, quiz et Pareto ; actualiser matrice et preuves sur les définitions réellement présentes puis tester tous les clics.

### I63-P1-R2

La génétique donne les phénotypes NOTCH3/Fabry, la transmission et le choix du test mais n’expose pas la fonction normale ni le mécanisme pathologique des gènes/protéines ; la figure 7 reste un parcours de bilan. L’îlot Histologie et biologie cellulaire expose correctement les gradients ioniques et l’œdème cytotoxique, mais aucune architecture tissulaire normale ni lésion morphologique de l’infarctus n’y est enseignée. Il manque ainsi les développements explicitement exigés par le guide §6, au-delà d’une répétition clinique.

Compléter, sur des textes primaires réellement lus, la fonction normale puis la perturbation des modèles génétiques pertinents et leurs liens vasculaires, avec figure commentée ; compléter la dimension histologique annoncée par une architecture normale et des lésions élémentaires pertinentes, en distinguant bien mécanisme cellulaire et morphologie. Garder les corrélations clinique/examen/traitement et les limites des modèles. Ne pas ajouter de seuil, de chronologie de nécrose ou de mécanisme de mémoire sans passage primaire.

## Précision des preuves

Dans le ledger auteur, les 1005 source_passage_summary sont identiques à leur claim ; cette identité n’invalide pas une reformulation fidèle, mais les vignettes fictives (âge, délai, heures de découverte) sont aussi présentées comme des passages primaires. Le cours déclare honnêtement son cas fil rouge fictif ; la matrice doit préserver cette distinction.

Marquer les données inventées de vignette comme données pédagogiques et associer séparément le principe médical réellement confirmé à sa source. Un âge fictif n’est pas une observation d’un article.

## Frontend

Copie exacte des sept SHA, production_cycle:1 en scratch seulement, build explicite --fragment S08, charge utile reconstruite identique à chacune des six sources, SHA du fichier servi 98463445923fe322e80d3ac30861089c66c1bfc51f97ac372ff93755fa5bd5b1. test_v7.py --url : OK. Ordinateur 1440×1000/mobile 390×844 : quatre onglets, cinq sciences, 32 fenêtres, sept SVG, quatre quiz et leurs bonnes/mauvaises options réellement exercés. 22 glossaires du corps/fenêtres plus CIM-10-GM du titre cliqués. Zéro erreur JS ou débordement. Captures réellement vues ; les anciennes références G absentes sont silencieusement omises par le moteur, et non un bouton cassé.

Les captures `i63-1-ouverture.png`, `i63-2-explication.png`, `i63-1440-cours.png`, `i63-390-cours.png`, `i63-gla-glossaire.png` et `i63-aristotle-sans-approfondissement.png` ont réellement été vues. Le test officiel passe. Son succès ne valide ni les définitions ni le contenu scientifique.

## Portée

Aucune modification des sources I63, D50, des glossaires partagés, du registre ou de la coque n’a été effectuée. Les primaires restent dans le scratch privé. L’auteur seul corrige ; la passe 2 sera datée après la remise des nouvelles empreintes. Le cycle 2 et l’injection restent fermés.
