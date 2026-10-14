# I63 — Infarctus cérébral : audit, correction et enrichissement Claude (14 octobre 2026)

Acteur : Claude, sous-agent d'audit I63, branche `claude/great-cerf-uizsml`. Revue par intelligence artificielle, sans validation médicale humaine. Les empreintes avant et après figurent dans `audit.json`.

## Notes

| Critère | Passe 1 | Passe 2 |
|---|---|---|
| Exactitude et actualité (4) | 3,5 | 3,75 |
| Complétude (3) | 2 | 2,75 |
| Pédagogie (3) | 2 | 2,5 |
| Corrélations vertes (2) | 1,5 | 2 |
| Sciences et schémas (2) | 1,5 | 1,75 |
| Examens (2) | 1,5 | 2 |
| Pharmacologie (1) | 1 | 1 |
| Pareto (1) | 1 | 1 |
| Langue (1) | 0,5 | 0,75 |
| Interface (1) | 1 | 0,75 |
| **Total** | **15,5/20** | **18,25/20** |

L'interface baisse en passe 2 par honnêteté : le contrôle statique est OK, mais aucun test navigateur n'a été exécuté après les ajouts.

## Passe 1 — écarts constatés

- Aucune erreur de tolérance zéro : 24 chiffres clés revérifiés sans écart. Sources : FI suisses Actilyse, Metalyse, Eliquis, Plavix, Aspirine Cardio, Sortis et Clexane ; protocole bernois 08/2026 ; ESO pression 2026, dont le tableau 11 lu en image ; ESO bithérapie 2021.
- Lacunes de fond pour l'Examen fédéral :
  - aucun tableau des syndromes par territoire artériel (sylvien, cérébral antérieur, cérébral postérieur, thalamus, Wallenberg, cervelet, basilaire) ;
  - aucun syndrome lacunaire ;
  - pas de diagnostics différentiels hiérarchisés ni de raisonnement par situation de départ ;
  - ni score RACE, ni examen HINTS ;
  - fréquences étiologiques bernoises absentes ;
  - recommandation ESO 2 (ticagrelor) absente ;
  - seuils de durée de fibrillation atriale absents.
- Images : aucune image réelle. Les schémas SVG en boîtes n'étaient pas qualifiés de didactiques, et leur numérotation était désordonnée.
- Langue et interface :
  - doublon dans la ligne de statut ;
  - phrase fautive dans la fenêtre Eliquis ;
  - autoréférences de fenêtres (i63-imagerie, i63-energie) ;
  - style dominé par les négations et pauvre en connecteurs.
- Précisions manquantes :
  - plafond de l'héparine sous-cutanée après thrombolyse (10 000 UI/jour dans la FI) ;
  - divergence bernoise 185/105 mmHg.

## Corrections

**Médicales et de précision (3) :**
- ajout du plafond de 10 000 UI/jour pour l'héparine sous-cutanée (deux fichiers) ;
- ajout de la divergence tensionnelle bernoise et de son mécanisme ;
- alignement de la phrase sur l'autorégulation avec le texte ESO 2026.

**Linguistiques et d'interface (une vingtaine) :**
- ligne de statut ;
- phrase Eliquis, avec l'acronyme d'essai évité ;
- quatre autoréférences supprimées ;
- numérotation séquentielle des figures 1 à 13 et mention « Schéma didactique » ;
- connecteurs logiques ;
- deux abréviations non couvertes, corrigées.

## Enrichissements majeurs

1. Section « Relier les signes à l'artère » : tableau de huit syndromes, exemple commenté et piège postérieur (risque de méconnaissance multiplié par trois). Sources : Hoyer et Szabo 2021, Bern p. 5.
2. Étiologie :
   - fréquences bernoises ;
   - sous-section sur la lacune, avec la Figure 2 réelle ;
   - tableau des cinq syndromes lacunaires et de leurs fréquences (Rudilosso, Arboix 2022) ;
   - piège des 16,6 % de syndromes lacunaires non dus à une lacune (Arboix 2010).
3. Tableau des diagnostics différentiels hiérarchisés par gravité (rangs 1 à 4), avec l'élément discriminant et l'examen décisif.
4. Nouvelles fenêtres :
   - **i63-ssp** : dix situations de départ (205, 103, 99, 20, 100/96, 18/39, 104, 126/216, 145, 101, 23), chacune suivie de l'hypothèse, des concurrents et de l'examen décisif ;
   - **i63-hints** : d'après Tarnutzer et collègues 2025, premier auteur suisse ;
   - **i63-race** : d'après Bern p. 5 et Kägi 2021.
5. Prévention :
   - recommandation ESO 2 (aspirine–ticagrelor, sans posologie non vérifiée) ;
   - seuils de fibrillation atriale (30 s au Holter, 6 min sur dispositif implantable) ;
   - délais de début d'anticoagulation (48 h, ou jour 6 pour un grand infarctus).
6. Critères bernois de l'infarctus malin, sylvien et cérébelleux, avec le mécanisme de la craniectomie.
7. Donnée suisse : 70 à 80 % des patients sans occlusion d'un gros vaisseau, 20 à 30 % avec occlusion.
8. Deux quiz supplémentaires (hypoglycémie imitatrice ; vertige aigu avec scanner normal), soit six au total. Ajout d'une ligne glycémie aux paramètres clés et d'un Pareto enrichi.

## Images (vérifiées visuellement avec Read)

| Fichier | Contenu | Licence | Emplacement |
|---|---|---|---|
| `dens_media_sign_mit_mediainfarkt_cct_001.jpg` | Scanner : signe de l'artère dense, puis hypodensité sylvienne | CC BY-SA 3.0, Hellerhoff | Examens, Figure 4 |
| `ct_of_lacunar_strokes.jpg` | Scanner : deux lacunes capsulo-lenticulaires | CC BY-SA 3.0, Prashanthsaddala | Étiologie, Figure 2 |
| `histopathology_of_thalamus_infarction_at_approximately_24_ho.jpg` | Hématoxyline-éosine : neurone normal et neurone rouge avec neutrophiles | CC0, M. Häggström | Histologie, Figure 8 |
| `mca_stroke_brain_human_1.jpg` | Coupe d'autopsie d'un infarctus sylvien aigu, lésion non délimitée | CC BY-SA 3.0, Marvin 101 | Histologie, Figure 9 |

Les attributions complètes et les empreintes figurent dans `assets/img/cycle1/i63/ATTRIBUTIONS.json`.

## Réserves ouvertes

- **Sources non relues :** plusieurs sources vérifiées le 11.10 n'ont pas été relues le 14.10, car Europe PMC renvoyait une erreur 500. Il s'agit d'ESO IVT 2021, ESO ténectéplase 2023, ESO prévention 2022, ESO basilaire 2024, Weimar 2024, Analytica et SSED.
- **Explications sans passage primaire lu :** les mécanismes de l'examen HINTS et la radiodensité de la lacune relèvent de la physiologie de base.
- **Fréquence des imitateurs :** elle reste qualitative, faute de proportions publiées dans les sources lues.
- **Correspondance avec les situations de départ :** elle est pédagogique, car l'annexe SSP ne contient pas de fiche I63.
- **Source américaine :** une revue descriptive américaine (Wallace et Liberman) n'est citée que pour un fait sémiologique, sans valeur décisionnelle.
- **Langue :** le style hérité reste très prudent et négatif dans les sections non réécrites.
- **Schémas SVG anciens :** ils conservent des couleurs de remplissage en ligne qui n'étaient pas dans ce périmètre.
- **Rendu non vérifié :** il n'y a eu ni test navigateur ni capture, et l'affichage des images dépend de la publication du dossier `assets/img/cycle1/i63/`.

## Contrôle technique

`python3 test_v7.py --static I63` : **OK** (35 813 mots, 53 fenêtres, 6 quiz, 4 Pareto).
