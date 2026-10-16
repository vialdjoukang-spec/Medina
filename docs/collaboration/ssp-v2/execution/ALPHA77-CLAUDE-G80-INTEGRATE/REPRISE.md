# Reprise ALPHA77-CLAUDE-G80-INTEGRATE (sauvegarde du 16.10.2026)

Réservation acquise et `start` réussi (base 8a512893acbab9caa0dcfdd0e8682a44ea72fda6, branche claude/alpha77/g80-integrate-g1). Réservation non libérée.

## Étape atteinte
- Lecture complète des 7 fichiers G80 (empreintes identiques à celles des audits ALPHA1 : sources inchangées).
- Lecture des audits existants : origin/claude/alpha1/g80-med-g1 (0 BLOQUANT, 9 MAJEUR, 11 MINEUR, 5 ENRICHISSEMENT ; calculs 470/471, 17 faux) et origin/claude/alpha1/g80-lang-g1 (74 propositions fond_inchange, 13 renvois).
- Vérifications de sources refaites et CONFIRMÉES (16.10.2026) :
  - FI Liorésal (janv. 2025, AmiKo 7680360830184) : indications SEP et spasticité médullaire seulement (PC hors indication) ; enfant dès 12 mois, 0,3 mg/kg/j en 4 prises, entretien 0,75–2 mg/kg/j, max 40 mg/j < 8 ans, 60 mg/j > 8 ans ; comprimés 10 mg sécables en 2, 25 mg non divisibles ; épilepsie (seuil abaissé) ; IR : surdosage > 5 mg/j ; interactions : dépresseurs SNC (tizanidine, opiacés, alcool — la FI NE cite PAS le diazépam : corriger la proposition C08), tricycliques, antihypertenseurs, médicaments affectant la fonction rénale, lithium, lévodopa.
  - FI Liorésal intrathécal (avr. 2024, 7680525350267) : titration cérébrale 5–15 %, entretien 5–20 % ; dose initiale = double de la dose test sur 24 h ; crises 10,4 % ; sevrage en heures à jours (cathéter, réservoir) ; < 6 ans données très limitées, < 4 ans sécurité non démontrée.
  - FI Dysport (mai 2026, 7680550570029) : enfant MS 16 U/kg ou 640 U / 21 U/kg ou 840 U ; MI 15/30 U/kg, 500 U/jambe, 1000 U ou 30 U/kg ; réinjection ≥ 16 sem. MS, ≥ 12 sem. MI (16–22 sem. dans les études) ; aminoglycosides, curares.
  - SSGO avis n° 66 (16.12.2019, PDF lu) : 24+0–32+0 SA, bolus unique 4 g en 15 min, idéalement ≥ 4 h avant naissance, entretien non recommandé, répétition une fois.
  - Novak 2017 (texte intégral via NCBI efetch PMC9641643) : DAYC « 83 % C index » ; HINE < 73 (6, 9, 12 mois) haut risque, < 40 presque toujours PC ; 50–73 unilatéral, < 50 bilatéral ; 86 % des parents ; < 5 % faux positifs ; ~10 % IRM normale ; signes à 9 mois.
  - Morgan 2019 (PMC6912336, résumé) et Cochrane 2026 (PMC13539583, résumé : NNT 60, IC 41–158 ; décès ou PC RR 0,87, 0,77–0,98).
- AUCUNE modification des chapitres encore faite.

## Suite exacte
1. Appliquer par script les 74 propositions LANG (vérifier unicité de chaque « ancien »).
2. Appliquer les propositions MED (dossier propositions/ de la branche med), en retirant les marqueurs [Sx] (citer auteur/année ou FI comme G72) et en corrigeant C08 (pas de diazépam dans la FI).
3. Sous-onglet sémiologie sur le modèle G72 : bouton id="g80-tab-semio" type="button" en tête, div.sci role="tabpanel" aria-labelledby, 9 îlots data-semiology (normal, signs, mechanisms, examination, interpretation, differentials, urgency, limits, sources avec liens https), premier h3 exact ; section pA data-semiology-clinical="G80" ; fenêtres g80-sm-* dans pop1/pop2 (pas de _pop3).
4. Au moins 6 boutons data-s : ajouter une 5e discipline (proposée : biostatistique du diagnostic — Se, Sp, RV, indice C, NNT ; sources BMJ Deeks-Altman 2004, Altman-Bland 1994 à lire).
5. Compléter physio/génétique/biochimie ≥ 280 mots avec les 4 libellés (Science → clinique/examen/traitement, À retenir).
6. Retirer la Figure 2 (ANATOMIQUE_IA) → tableau Reimers (Hägglund 2007) ; corriger Figure 3 ; redessiner les SVG pour lisibilité à 390 px.
7. Glossaire : AI, OIC-DFI, DFI, SSGO, RV, NNT… ; build_medina.audit() == {} ; supprimer la définition non sourcée de 37 SA.
8. Contrôles (test_v7 --static, audit_sciences, build fragment S08, captures bureau/390 px), revue/MED.json, LANG.json, SEMIO.json, integration/corrections.json, controles.json, generer_recu.py (modèle G72), reçu organisation/alpha-publications/Claude/G80/0001.json, merge origin/main, check, push, PR.
