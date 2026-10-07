# I83 — rédacteur D (onglet Pharmacologie) : sources hors § 4 du plan et réserves

Rédaction du 8 octobre 2026. Fichiers : `I83_d.html`, `I83_pop4.html`, `../glossary_i83_d.py`.

## Données chiffrées ajoutées (absentes du § 4 du plan)

| Donnée | Source vérifiée |
|---|---|
| Effets par molécule (douleur, lourdeur, etc.) | ESVS 2022, tableau 8, lu sur `src/esvs2022_cvd.txt` (version en colonnes) |
| Fraction flavonoïque purifiée micronisée : 7 essais, 1 692 patients ; ulcère + 32 % à 6 mois ; Cochrane 2013 RR 1,37 | ESVS 2022 §§ 3.3.2 et 6.6 |
| Dobésilate : 10 essais, 778 patients ; 4 essais, 1 165 patients | ESVS 2022 § 3.3.3 |
| Oxérutines : 15 essais, 1 643 participants ; ulcère RR 1,7 | ESVS 2022 §§ 3.3.5 et 6.6 |
| Vigne rouge : essais de 260 et 248 patients ; marronnier : Cochrane 17 essais, 1 593 patients | ESVS 2022 §§ 3.3.4 et 3.3.6 |
| Sulodexide : 13 études, 1 901 participants ; ulcère 49 % contre 30 %, RR 1,66 | ESVS 2022 §§ 3.3.7 et 6.6 |
| Pentoxifylline : 12 essais, 864 participants ; RR 1,70 ; 1,56 avec compression ; effets indésirables RR 1,56, 72 % digestifs | Jull et al., Cochrane 2012, PMID 23235582 (résumé PubMed) |
| Polidocanol : succès 95 % (veines réticulaires et télangiectasies) ; mousse ≥ 2 fois plus efficace, 4 à 5 fois moins de produit | ESVS 2022 §§ 4.2.2.2 et 4.5.1 |
| Tumescence : 445 + 50 + 5 mL ; 15 mg/kg ; 36 % à 35 mg/kg ; calcul 1 mg/mL et 1 µg/mL (déduit de la composition) | ESVS 2022 § 4.1.3 |
| Prophylaxie de 7 à 10 jours chez le patient à haut risque | ESVS 2022 § 4.1.6 |
| Westin et al. : occlusion 92 % contre 95 % | ESVS 2022 § 8.2.3 |
| Amlodipine : œdèmes très fréquents (11,1 %) | Information professionnelle suisse de Norvasc (avril 2023), swissmedicinfo.ch, autorisation 50044 |
| Mécanisme de l’œdème des antagonistes calciques (dilatation sélective du versant afférent du réseau capillaire) | Lindeman et al., Clin Toxicol 2020, PMID 32114860 (résumé PubMed) |
| IEC ou ARA ajouté : œdème − 38 % (RR 0,62), 25 essais | Makani et al., Am J Med 2011, PMID 21295192 (résumé PubMed) |
| Prégabaline : œdème périphérique 5,7 % | Information professionnelle suisse de Lyrica (juillet 2026), autorisation 57057 |
| Pioglitazone : rétention hydrique, œdème fréquent, association aux anti-inflammatoires non stéroïdiens | Information professionnelle suisse d’Actos (mai 2021), autorisation 55378 |
| Signes de toxicité de la lidocaïne ; pic 20–30 min après surdosage ; doses plus faibles si insuffisance hépatique | Information professionnelle suisse de Rapidocain avec épinéphrine (juillet 2024), autorisation 20272 |
| Disponibilité en Suisse (Venostasin, Aesculaforce forte Venen, Aesculamed forte Venen, génériques diosmine-hespéridine ; absence de pentoxifylline, sulodexide, Ruscus, tétradécylsulfate, Fibrovein, Trental) | `src/swissmedic_ham.xlsx`, état au 30.09.2026, recherche par nom de produit |

Les informations professionnelles de Norvasc, Lyrica, Actos et Rapidocain ont été lues sur `https://www.swissmedicinfo.ch/ShowText.aspx?textType=FI&lang=FR&authNr=<numéro>` (simple consultation publique, aucune donnée transmise) ; copies non versionnées dans le bloc-notes de la session.

## Réserves

1. **Venostasin et autres extraits de marronnier d’Inde** : information professionnelle introuvable (swissmedicinfo et compendium sans résultat). Aucune posologie n’est écrite.
2. **Liste des spécialités** (remboursement des veinotropes) : application de l’Office fédéral de la santé publique inaccessible par script. Le texte n’affirme aucun statut de remboursement ; il renvoie au contrôle au moment de la prescription. Catégories de remise B et D vérifiées.
3. **Mousse d’Aethoxysklerol** : non mentionnée dans l’information suisse ; le texte le dit.
4. **Tension entre ESVS et informations suisses** : l’ESVS discute le traitement concomitant des collatérales (recommandation 48), alors que les informations d’Aethoxysklerol et de Sclerovein demandent d’attendre 1 à 2 jours après une exérèse chirurgicale d’un tronc (effet anesthésique local additif). Le texte cite l’information suisse sans trancher pour l’ablation endoveineuse.
5. **Contre-indication « diabète sucré »** de la sclérothérapie : présente dans les deux informations suisses, absente du fait F50 du plan ; ajoutée selon la source primaire.
6. **Diurétiques** : le paragraphe repose sur un raisonnement mécanistique (pas de rétention sodée dans l’œdème veineux ni dans celui de l’amlodipine), sans chiffre ; aucune source primaire chiffrée.
7. **Interférence dobésilate–créatinine et dose des AOD** : conséquence déduite (formulée au conditionnel), non tirée d’une source.
8. **Nomenclature** : le libellé « C-01-Cardiologie » est signalé comme sigle par le vérificateur ; entrée ajoutée dans `glossary_i83_d.py` (à fusionner ; A et B l’emploient aussi).
9. Les oxérutines n’ont pas d’effet démontré sur l’œdème dans le tableau 8 de l’ESVS, alors que leur information suisse le revendique : le texte signale l’écart.
