# G02 — paquet de revue du 2 novembre 2026

Ouvrir **G02-apercu-autonome.html**. Il contient le moteur natif, ouvre G02 et embarque les octets originaux de la planche anatomique. Les autres leçons du fragment restent dans la navigation héritée ; seule G02 fait l’objet de cette reprise. Aucun déploiement distant n’est déclaré.

## Résultat vérifié

- 14 points monographiques présents ; 20 rubriques inventoriées. La présence des sections ne vaut pas certification de complétude médicale.
- 6 sciences, dont sémiologie initiale en 9 sections et anatomie. Sciences : 2957 mots contre 1083 à la base.
- 61 fenêtres définies, 60 termes distincts appelants, aucun renvoi absent, aucun identifiant dupliqué, aucune abréviation non couverte.
- Une planche anatomique humaine originale Carter/Gray1918, affichée dans deux contextes pédagogiques, sans retouche des pixels ; 3 annotations françaises autour de l’image. Les schémas causaux hérités restent identifiés comme schémas didactiques, pas comme anatomie.
- Chromium local : 1440 et390 pixels, requêtes externes interdites, images lazy décodées après défilement (648pixels chacune), fenêtres, Livre24px, dernière section pharmacologique et sources accessibles ; aucun débordement du document ni erreur JavaScript. La fenêtre fexinidazole de 3692 caractères conserve sa dernière source accessible à 24 pixels, sans débordement horizontal.
- 23 lectures réelles indexées avec leur profondeur. Les résumés ne sont pas décrits comme des textes intégraux.

## Fichiers probants

- `G02-apercu-autonome.bundle.json` : SHA du rendu natif, du bundle et de l’image.
- `source-binding.json` : empreintes des six HTML, du glossaire, de l’image et du bundle après contrôles ; `visual-self-review.json` : inspection visuelle réellement effectuée.
- `browser-autonomous.json` et `captures/autonomous-*` : contrôles actuels. Les captures sans préfixe autonomous et `browser-check.json` documentent une passe intermédiaire.
- `sciences-check.json`, `structural-checks.json`, `monograph-14.json` : contrôles techniques et limites médicales.
- `recherche_G02/sources.json` : passages paraphrasés/lectures, identifiants S19–S41 ; les textes téléchargés restent en cache temporaire hors dépôt.
- `recherche_G02/recherche.md` : matrice20 et lacunes.

## Réserves qui empêchent une clôture médicale

1. Erratum du15octobre2025 du guide candidose non obtenu. Les principes du texte2025 sont lus ; aucune nouvelle posologie chiffrée du schéma SNC n’est certifiée.
2. FI suisse flucytosine et traitements des causes rares non complétées ; distinction stricte des doses par produit, âge, indication et fonction rénale maintenue.
3. Le guide WHO 2024 et le RCP Fexinidazole Winthrop 2025 sont désormais lus. Le statut suisse et les autres produits de la trypanosomiase restent à vérifier. Coccidioïdomycose et Chagas sont encore insuffisamment documentées.
4. Critères du consortium encéphalite : table DGN consultée, source primaire non obtenue ; ne pas inventer les détails manquants. L’absence de données ne constitue pas un résultat négatif.
5. BfArM2024 relu ; applicabilité administrative suisse2026 et obligations déclaratives non certifiées. Cartographie PROFILES héritée non revalidée.
6. Rapports finaux MED, LANG et SEMIO non clos. Les corrections relèvent de self_review avec empreintes ; une revue indépendante systématique n’est pas exigée par README-V2 §7. Aucune validation humaine ni indépendante n’est revendiquée.

## Corrections de portée clinique

Les concordances corps/fenêtres/Pareto ont été corrigées sur : triade28%, fièvre rapportée71% contre mesurée42%, seuil1000cellules non absolu, procalcitonine non exclusive, pronostic mesuré après sortie, causalité non déductible du délai antiviral, nouveau-né HSV distinct de l’échovirus, durée FI10jours versus directive≥14jours non arbitrée par simple date, délai4semaines après brivudine, indication Brivex limitée au zona de l’adulte immunocompétent, AmBisome FI dans sa population VIH, distinction antigène/culture cryptococcique et actualisation des principes candidose2025.

## Reproduction

Depuis le worktree exclusif : construire le fragment avec `MEDINA_OUT=<dossier>/preview python3 build_front.py --fragment S08`, puis utiliser `harness/bundle_native.py` depuis le harness parent. Exécuter `node <dossier>/browser-check.cjs --autonomous`. Les captures concernent le bundle exact ; le serveur local est éphémère et fermé après le contrôle.

Aucune prochaine leçon n’est ouverte tant que les réserves et les revues requises de G02 ne sont pas levées. Le rapport08hEurope/Zurich n’est pas une consigne d’arrêt.

## Actualisation documentaire suivante

Le guide WHO 2024 et le produit exact Fexinidazole Winthrop, version EMA du 17 octobre 2025, documentent maintenant les stades, les choix par population, les doses pondérales, le repas, la surveillance et le suivi. Les différences de seuil (≥100 OMS ; >100 RCP) et de surveillance à domicile sont explicites. Le statut suisse reste non établi. Le contrôle statique natif a également supprimé quatre styles en ligne et deux classes hors contrat ; les annotations de la figure demeurent du texte HTML.
