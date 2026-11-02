# G02 — paquet relu du 2 novembre 2026

L’[aperçu autonome](G02-apercu-autonome.html) ouvre G02 dans le moteur natif, avec l’original anatomique incorporé. SHA256 : `76c59b4fba209a09fb186f6a5554541e81397722633547ce89a3b61ecda435db`. La navigation des autres cours est héritée ; cette livraison porte uniquement sur G02. Aucun déploiement distant n’est affirmé.

39 lectures de cette session, 14 points monographiques et 20 rubriques revus. Six disciplines scientifiques et neuf sections sémiologiques ; original Carter/Gray1918 annoté en français dans le HTML, sans modification des pixels ni anatomie produite par IA. Les schémas causaux sont distincts de cet original.

La reprise documente les causes virales, cryptococcose, candidose, coccidioïdomycose, trypanosomiase africaine et Chagas. Elle corrige les répétitions sur populations, délais, seuils, causalité, codage et traitements. Les critères Consortium2013 et les correspondances pédagogiques PROFILES2023 ont été relus à leur source.

## Preuves de lecture et de couverture

- [Ledger des passages lus](recherche_G02/sources.json) : URL, version, section, population, limite, paraphrase et empreinte ; textes complets hors Git.
- [14 points](monograph-14.json) et [20 rubriques](matrix-20.json), avec [raisonnement et limites](recherche_G02/recherche.md).
- [Revue médicale](reviews/medical.json), [langue](reviews/language.json), [sémiologie](reviews/semiology.json), toutes en `self_review` avec empreintes. Aucune validation indépendante ou humaine revendiquée.
- [Provenance de la figure](figure-provenance.json), [inspection visuelle](visual-self-review.json) et [contrat](lesson-manifest.json).

## Contrôles du paquet exact

Le contrôle statique natif passe : 23 362 mots, 64 fenêtres, 7 quiz, 11 Pareto. Sciences : 3 000 mots contre 1 083 à la base, 6 figures et 6 disciplines. La croissance n’est pas une mesure de qualité.

Le [rapport navigateur](browser-autonomous.json) vérifie 1440 et 390 pixels, les deux images après défilement et décodage (largeur naturelle648), les trois annotations, les six onglets et neuf sections, absence de débordement/erreurJavaScript, livre24px, et cinq fenêtres longues avec derniers liens accessibles. Toutes les requêtes externes sont bloquées pendant le test. Le serveurHTTP local est éphémère et fermé après le contrôle.

Le [reçu de liaison](source-binding.json) relie les sixHTML, le glossaire et l’image à l’aperçu effectivement testé. Le fragment natif temporaire reste dans `preview/` horsGit ; `content-snapshot.html` est une copie textuelle empreintée pour la vérification des ancres.

## Limites conservées

L’erratum candidose d’octobre2025 reste inaccessible : aucun schéma chiffré douteux n’est publié. Les produits rares ne sont pas déclarés disponibles en Suisse sur la seule base d’une autorisation. L’incidence suisse actuelle et l’applicabilité administrative2026 ne sont pas inventées. Les produits de recours ne deviennent pas un protocole prescriptif exhaustif. Les études lues au niveau résumé restent signalées ainsi.

Ces limites sont jugées non bloquantes pour le périmètre pédagogique effectivement couvert, car les assertions dépendantes ont été circonscrites ou retirées. Ce jugement d’auteur ne certifie pas la médecine. Aucun passage à une nouvelle leçon, PR ou écriture surmain n’est réalisé par ce paquet.

## Reproduction

Construire avec `MEDINA_OUT=<dossier>/preview python3 build_front.py --fragment S08`, puis `harness/bundle_native.py <fragment> <worktree> G02 <aperçu>`. Exécuter `node <dossier>/browser-check.cjs --autonomous`, `python3 test_v7.py --static G02`, l’audit sciences et `tools/betta_verite.py <dossier>/recherche_G02`. Les contrôles doivent être relancés si les sources changent avant d’actualiser le reçu.
