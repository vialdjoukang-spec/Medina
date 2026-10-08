# Rapport — rôle Pathologie et rédaction — J45 — Asthme (P-02-Pneumologie)

Revue du 08.10.2026. Référentiel : **GINA 2026** (rapport du 5 mai 2026, guide de synthèse de juillet 2026), PDF intégraux lus (`dl_gina/`) ; aucune version postérieure.

## 1. Fichiers modifiés
- `chapters/J45/J45_a.html` (en-tête, îlots 0–6) : statut daté ; annonces directes ; phrases nominales et infinitives réécrites ; tableaux introduits et commentés ; « À retenir » aux îlots 1, 4, 5, 6. Identifiants, `data-k`, Pareto et ancres de `J45_justifications.json` conservés.
- `chapters/J45/J45_pop1.html` : 20 fenêtres réécrites (mécanisme, interprétation, limites, conduite, Source), clés inchangées.
- Originaux : `j45_rapports/pathologie_orig/`.

## 2. Matrice des corrections (GINA 2026 = texte intégral lu le 08.10.2026, sauf mention)

| Passage | Problème → correction | Source |
|---|---|---|
| a, îlot 0 | « principal facteur évitable » (causalité) → association en population vs preuve des essais ; tolérance au BACA ; 6–11 ans inclus | guide p. 15, 21 |
| a, § 1.2 | question « secours » pour tout secours → réservée au BACA ; contrôle ≠ risque | guide tab. 2 |
| a, § 1.3 | sévère = « palier 4–5, dose moyenne ou forte » → sévère = forte dose ICS-BALA ; difficile = moyenne ou forte ; modéré = palier 3–4 | rapport p. 48 |
| a, piège 1.3 | « un tiers des décès chez les légers » → jusqu’à 30 % des exacerbations et décès chez patients peu symptomatiques | rapport p. 49 |
| a, § 1.5 | rémission « ≥ 12 mois » → aucune définition imposée ; pas une guérison | rapport p. 55-57 |
| a, § 1.6 | 5e caractère « contrôle et exacerbation » → contrôle **et sévérité** ; J46 « asthme aigu sévère » | CIM-10-GM (pro.medcode.ch), page lue |
| a, îlot 2 | prévalence non datée ; mortalité ; remodelage → Ligue pulmonaire déc. 2023 (lue) ; 96 % des décès hors pays riches ; données observationnelles, aucun essai ; cartouches de 200 doses | guide p. 5, 15 ; rapport p. 25, 55 |
| a, § 4.1 | « parent ×2–3 », causalité implicite → RC 3,0/2,4 ; VRS, trafic, ferme = associations | Lim 2010, doi:10.1371/journal.pone.0010134 (résumé) ; rapport p. 231 |
| a, § 4.2-4.3 | « GINA 2026 ajoute chaleur/froid » ; reflux ; « le phénotype prédit la réponse » → météo extrême ; reflux asymptomatique non traité ; phénotype peu prédictif hors asthme sévère ; endotype ; N-ERD 7 %/15 % | rapport p. 25, 137, 139 |
| a, îlot 5 | liste défavorable ancienne ; « 5–15 min » ; « 80 % » → liste 2026 ; aggravation après l’arrêt ; 70–80 % ; encadré `alert` des antécédents à risque vital | encadrés 1-2, 9-1 ; p. 117 |
| a, îlot 6 | saturation sans limites → peau foncée, altitude ; « ni parler, ni boire, ni s’allonger » | guide fig. 9 |
| pop eos / feno | « bas le matin » ; seuils mal situés → plus élevés le matin ; 150/300 dans l’asthme sévère ; strongyloïdose dès 300 | annexe A |
| pop control | ACQ < 0,75/> 1,5 → ≤ 0,75/≥ 1,5, pivot 1,0 ; différences minimales 0,5 et 3 | p. 39-40 |
| pop plan / tech | 80 %, 48 h, « dose maximale » → > 12 inhalations/24 h, 2–3 jours ; agiter avant chaque bouffée | guide p. 33-34 ; encadré 5-2 |
| pop nerd | « 30 min à 3 h » → minutes à 1–2 h ; test en centre | p. 137-138 |
| pop abpa | IgE « > 500 » ; EGPA incomplet → ≥ 500 + 2 critères ; score ACR/EULAR 2022 ≥ 6 ; itraconazole | doi:10.1183/13993003.00061-2024 ; doi:10.1136/annrheumdis-2021-221794 (résumés) |
| pop gaz / mnemo | PaCO₂ > 42 mmHg ; saturation < 90 % → PaO₂ < 60 et PaCO₂ > 45 mmHg ; PaCO₂ « normale » = menace ; < 92 % ; acidose lactique | p. 185-186 ; BTS/SIGN 158 (page lue) |
| pop pro | cadre suisse imprécis → LAA art. 9, OPA art. 78 et 86 | jurisprudence (partiel) |
| pop t2 | « moitié à deux tiers » → GINA + Woodruff 2009 (n = 42) | doi:10.1164/rccm.200903-0392OC (résumé) |

## 3. Confirmés sans changement
Définition GINA ; quatre questions de contrôle ; FeNO > 50/> 35 ppb et bornes ATS 2011 ; mécanismes de type 2 ; asthme au froid ; figure 1 ; timolol ; obstruction laryngée ; thorax silencieux ; sibilants.

## 4. Propositions hors périmètre
Texte exact dans `j45_rapports/pathologie_propositions.md` (P1–P11) : J45_b § 9.1, 9.2, 11.3, 12.1–12.4 et piège MART (« temporairement » erroné pour le béclométasone-formotérol) ; Pareto `pareto-j45-clin` de J45_pop4 ; seuil 42 mmHg (pop4, J45_c ligne 84). Le propriétaire de J45_b avait déjà aligné l’îlot 8 sur GINA 2026. Aucune entrée de glossaire nécessaire.

## 5. Réserves
- Non relus en texte intégral : catégories PD20 de l’ERS 2017 (accès 403 ; exemple chiffré retiré) ; pouls paradoxal > 25 mmHg (attribution historique signalée dans la fenêtre) ; prick-test ≥ 3 mm (signalé) ; ANCA « minorité » ; prédominance masculine avant la puberté (revue, résumé seul).
- OFSP et Société suisse de pneumologie non consultés ; aucune série suisse récente de mortalité (lacune nommée).
- Volume : J45_a passe de 3 240 à 5 780 mots ; pop1 passe de 11 900 à 29 600 caractères. Ces ajouts portent les justifications et les mises à jour GINA 2026 ; une relecture de concision reste utile.

## 6. Contrôles
- `verifier_sigles.py` sur J45_a + pop1 : `{}`.
- `test_v7.py --static J45` : OK après ma passe ; l’échec actuel provient d’autres fichiers en cours (sigles DailyMed, EMA, SMART… ; fenêtres j45-d-ipra/laba/o2 de J45_d).
- Balises HTML équilibrées.
