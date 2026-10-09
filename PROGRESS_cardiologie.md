# Progression — C-01-Cardiologie (branche course/cardiologie)

Inventaire (9.10.2026) : 24 cours cardiologiques intégrés et scellés (I00, I10, I21, I25, I26, I27, I30, I33, I34, I35, I40, I42, I44, I46, I47, I48, I49, I50, I51, I70, I71, I80, I83, Q21) ; non modifiés ici.
Catégories prioritaires du registre sans cours (`organisation/fragments.json`, S01) : I73, I89, I95.

| Cours | État | Images |
| --- | --- | --- |
| I73 — Phénomène de Raynaud, thromboangéite oblitérante et autres acrosyndromes vasculaires (C-01-Cardiologie) | Rédigé ; règles connecteurs et interactivité appliquées (15 fenêtres) ; glossaire 0 non couverte ; frontend S01 contrôlé | i73_raynaud_phases_photo.gif, i73_raynaud_photo.gif, i73_arcade_palmaire_gray.gif, i73_capillaroscopie_figure.gif |
| I95 — Hypotension (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (20 fenêtres) ; glossaire 0 non couverte ; frontend S01 contrôlé | i95_tilt_tachycardie_posturale.gif, i95_baroreflexe_openstax.gif |
| I89 — Lymphoedème et autres atteintes non infectieuses des lymphatiques (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (16 fenêtres) ; glossaire 0 non couverte ; frontend S01 contrôlé | i89_capillaires_lymphatiques_openstax.gif, i89_lymphoedeme_photo.gif, i89_lymphoscintigraphie.gif, i89_capillaire_collecteur.gif, i89_stades_collecteurs.gif |
| I77 — Dysplasie fibromusculaire et autres atteintes des artères (couvre I77, I79) (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (19 fenêtres) ; glossaire 0 non couvert | i77_dfm_renale_angiographie.gif, i77_dfm_carotide_angiographie.gif, i77_dfm_angioscanner.gif, i77_compression_tronc_coeliaque.gif |
| I78 — Télangiectasie hémorragique héréditaire et autres maladies des capillaires (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (16 fenêtres, 3 quiz) ; glossaire 0 non couvert | i78_telangiectasies_levres.gif, i78_telangiectasies_langue.gif, i78_telangiectasies_visage.gif, i78_mavp_histologie.gif, i78_foie_scanner.gif |
| I97 — Troubles circulatoires après un acte médical (couvre I97, I98, I99) (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (12 fenêtres, 3 quiz) ; glossaire 0 non couvert ; renvois I30, I48, I89 sans duplication | i97_epanchement_pericardique_echo.gif, i97_doppler_mitral_respiratoire.gif, i97_bandage_lymphologique_bras.gif |
| I85 — Varices œsophagiennes et varices d’autres localisations (couvre I85, I86) (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (81 termes, 77 fenêtres, 3 quiz), images aussi dans 3 fenêtres ; renvoi K74 ; glossaire 0 non couvert ; test_v7 OK | i85_varices_oesophagiennes_scanner.gif, i85_ulceres_post_ligature_endoscopie.gif, i85_varices_gastriques_endoscopie.gif, i85_varices_signes_rouges_endoscopie.gif, i85_caput_medusae_scanner.gif |

| R00 — Palpitations, anomalies du rythme et souffles cardiaques (couvre R00, R01) (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (56 termes, 76 fenêtres, 3 quiz), images aussi dans 2 fenêtres ; glossaire 0 non couvert ; test_v7 OK | r00_tachycardie_sinusale_ecg.gif, r00_holter_patiente.gif, r00_phonocardiogramme.gif, r00_ecg_preexcitation_12d.gif, r00_onde_delta_ecg.gif |

| R02 — Gangrène, non classée ailleurs (C-01-Cardiologie) | Rédigé ; connecteurs et interactivité (57 termes, 3 quiz), images aussi dans 3 fenêtres ; glossaire 0 non couvert ; test_v7 OK | r02_gangrene_seche_orteils_diabete.gif, r02_gangrene_humide_pied.gif, r02_gangrene_gazeuse_radiographie.gif, r02_clostridium_gram.gif |

Restent sans cours dans le catalogue S01 (hors registre prioritaire) : I88, R03, S26, S35–S95, Z95 (I77 et I79 couverts par le cours I77 ; I78 et I97 (couvre I97–I99) rédigés le 9.10.2026).

État (9.10.2026, 22 h 20) : registre prioritaire S01 achevé (I73, I95, I89) ; prêt pour audit.

Règle image du propriétaire (9.10.2026) : images générées interdites ; toutes les figures C-01 sont des images réelles sous licence libre (PROVENANCE.json).

## Balayage rétroactif obligatoire (ordre du propriétaire, 10.10.2026)

Méthode : détecteur de phrases sans verbe conjugué (spaCy fr, /workspace/sweep_c01/audit2.py) sur paragraphes, listes, encadrés et fenêtres, puis réécriture manuelle en phrases complètes avec justification (« car », « parce que ») ; contrôle des images (toutes réelles, PROVENANCE.json) ; images réelles ajoutées dans les fenêtres ; suppression des styles en ligne ; test_v7 --static.

| Cours | Scellé | Phrases nominales | Images dans les fenêtres | Styles en ligne | État du balayage |
| --- | --- | --- | --- | --- | --- |
| I73 | non | 34 segments réécrits (fenêtres, Pareto, encadrés, mesures, contre-indications) | 2 (capillaroscopie, crise) | 4 retirés | Fait |
| I95 | non | 42 segments réécrits (fenêtres, Pareto, encadrés, critères, doses) | 2 (baroréflexe, inclinaison) | 2 retirés | Fait |
| I89 | non | 37 segments réécrits (fenêtres, Pareto, encadrés, seuils, contre-indications, piège) ; faux positifs vérifiés à la main | 2 (scintigraphie, lymphangion) | 5 retirés | Fait |
| I77 | non | 39 segments réécrits (objectifs, pièges, fenêtres, Pareto) ; faux positifs vérifiés à la main | 2 (collier de perles, tronc cœliaque) | 4 retirés | Fait |
| I78 | non | à faire (≈ 68) | 2 (langue, MAV pulmonaire) | 5 retirés | Partiel |
| I97 | non | à faire (≈ 48) | 2 (épanchement, Doppler) | 0 | Partiel |
| I85, R00, R02 | non | à faire (≈ 175, 197, 92) | déjà 3, 2, 3 | 0 | Partiel |
| I00 … R05 (26 cours, dont I26, I27, I51) | oui (`organisation/SCELLES.json`) | non balayés | — | — | Bloqué : la garde `tools/espace.py garde` (CI espace.yml et pages.yml) refuse toute modification d’une source scellée hors branche claude/* ; décision du propriétaire requise |
