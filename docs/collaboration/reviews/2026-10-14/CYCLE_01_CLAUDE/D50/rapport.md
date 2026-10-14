# D50 — Anémie par carence en fer : audit et correction Claude, 14 octobre 2026

Revue par intelligence artificielle (sous-agent d'audit D50). Aucune validation médicale humaine. Aucun commit ni push.

## Portée

Les sept sources canoniques (`D50_a` à `_d`, `_pop1`, `_pop2`, `glossary/d50.py`) ont été lues intégralement en passe 1. Leurs empreintes avant et après figurent dans `audit.json`. Le glossaire est inchangé : aucune abréviation nouvelle n'a été introduite.

## Sources primaires relues le 14.10.2026

- OMS 2024 sur les seuils d'hémoglobine, tableaux 2 à 5.
- BSG 2021, texte intégral Europe PMC.
- Onkopedia avril 2025 avec SGH/SSH et SGMO.
- mediX « Eisenmangel » 08/2025.
- gynécologie suisse, avis n° 77 du 24.08.2022.
- Clénin, Swiss Med Wkly 2017.
- Huit informations professionnelles suisses (AmiKo) : Ferinject®, MonoFer®, Venofer®, Tardyferon®, ferro sanol®, Ferrum Hausmann®, Maltofer® et Feraccru®.

Vingt groupes de chiffres clés ont été vérifiés : doses, plafonds, durées, seuils, fréquences et critères de réponse. Aucune posologie fausse ni aucun seuil faux n'a été trouvé.

## Écarts de la passe 1 (17,5/20)

- **Exactitude.** Il manquait les contre-indications obstétricales du fer intraveineux selon l'avis SGGG : antécédent d'anaphylaxie, infection aiguë sévère, bactériémie et insuffisance hépatique décompensée. Le critère d'échec du traitement oral ne précisait pas « grossesse actuelle ou précédente ». L'exemple Ferinject® de l'îlot 10 était approximatif (« environ 1500 mg »). Enfin, la fenêtre Venofer® ne donnait pas le critère de réponse, alors que l'îlot 10 y renvoyait.
- **Complétude et SSP.** La pâleur (SSP 147) était absente de l'examen clinique. Le cours ne proposait aucun raisonnement partant de la situation (pâleur ou anémie découverte, SSP 165). Le diagnostic différentiel de la microcytose se limitait à trois entités. La correction OMS liée au tabagisme était citée sans valeurs, et le tableau d'altitude s'arrêtait à 1999 m.
- **Images.** Le cours ne contenait aucune image réelle. Les schémas portaient la mention « pédagogique », sans préciser qu'ils étaient didactiques.
- **Langue.** Le pronom « Elle » restait ambigu (îlot 7). Des paragraphes figuraient après le bloc de références dans quatre fenêtres. La ligne de statut était datée du 11.10.

## Corrections et enrichissements

- **Îlot 6.** Ajout de la pâleur cutanéo-muqueuse : mécanisme et fiabilité selon mediX (peau peu fiable, conjonctives plus fiables). Une nouvelle fenêtre `d50-paleur` la détaille. L'îlot accueille aussi la photographie 1 (koilonychie), commentée.
- **Îlot 7.** Nouvelle sous-partie « Partir de la situation : pâleur ou anémie découverte ». Elle expose le raisonnement en quatre temps et présente un tableau de sept hypothèses, classées par gravité puis par fréquence, avec pour chacune les éléments évocateurs et l'examen qui tranche. Un quiz sur l'anémie macrocytaire la complète. Une nouvelle fenêtre `d50-ssp-microcytose` reprend la classification par le volume globulaire moyen (SGGG, tableau 1) et les microcytoses sans carence (Onkopedia, tableau 3).
- **Fenêtre de l'hémoglobine.** Ajout de la correction pour 2000–2499 m (14 g/L) et du tableau OMS du tabagisme (3, 3, 5 et 6 g/L), avec exemples chiffrés et mécanisme. Les corrections sont désormais cohérentes dans les critères formels et l'îlot 0.
- **Grossesse et réponse au fer.** Ajout des contre-indications SGGG, de la mention « grossesse actuelle ou précédente » et de l'interdiction de doser la ferritine dans les trois à quatre semaines suivant une perfusion. Ajout des critères de réponse des informations professionnelles Ferrum Hausmann® et Venofer®.
- **Ordre et légendes.** Exemple Ferinject® de l'îlot 10 précisé. Légendes des cinq schémas renommées « Schéma didactique ». Quatre fenêtres réordonnées pour placer les références en dernier. Deux Pareto enrichis.

## Images réelles (vérifiées visuellement avec Read)

| Image | Licence | Emplacement |
|---|---|---|
| Frottis ferriprive, VGM 55 fl (Ed Uthman) | CC BY 2.0 | Sciences, hématologie cellulaire |
| Koilonychie (C. Heitz) | CC BY 2.0 | Îlot 6 |
| Chéilite angulaire bilatérale (Matthew Ferguson 57) | CC BY-SA 3.0 | Fenêtre `d50-phaneres` |

Les trois fichiers mesurent au plus 1200 px de large et pèsent 89 à 189 Ko. La provenance complète figure dans `assets/img/cycle1/d50/ATTRIBUTIONS.json`.

## Réserves (non bloquantes)

- **R1.** ESC 2026 : seul le support officiel a été lu, pas le texte intégral.
- **R2.** KDIGO 2026, Delphi 2019, OFSP, Hoving, Schaefer, Viollier, LUKS et le consensus de médecine du sport n'ont pas été relus dans cette passe. Leurs chiffres restent ceux qu'avait vérifiés l'audit croisé du 11.10.
- **R3.** Aucune performance chiffrée de la pâleur conjonctivale n'existe dans les sources suisses ou européennes lues.
- **R4.** Les anémies normocytaires et macrocytaires sont seulement orientées, avec renvoi au chapitre D64, qui n'existe pas encore.
- **R5.** Le format de `ATTRIBUTIONS.json` (`{code, images}`, celui que lit `night_cycle.py`) diffère de la liste écrite par `images_ouvertes.py importer`.
- **R6.** Les chemins relatifs des images supposent que le dossier `assets` soit copié à côté du HTML publié.

## Note de la passe 2 : 20/20

| Critère | Note |
|---|---|
| Exactitude | 4/4 |
| Complétude | 3/3 |
| Pédagogie | 3/3 |
| Corrélations | 2/2 |
| Sciences et schémas | 2/2 |
| Examens | 2/2 |
| Pharmacologie | 1/1 |
| Pareto | 1/1 |
| Langue | 1/1 |
| Interface | 1/1 |

La relecture complète a entraîné cinq retouches finales : l'intitulé « Altitude, tabac et unités », la cohérence des critères formels, la reformulation des causes locales de la chéilite, la phrase « le bilan martial puis l'étude de l'hémoglobine tranchent » et le pronom ambigu de l'îlot 7.

## Contrôles

- `python3 test_v7.py --static D50` : OK (89 fenêtres, 6 quiz, 10 Pareto, aucune abréviation non couverte).
- `python3 test_v7.py D50` sur une construction locale hors dépôt : OK.
