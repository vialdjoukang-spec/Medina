#!/usr/bin/env python3
"""Recalcul scripté des grandeurs de la leçon G90 (audit ALPHA1-CLAUDE-G90-MED).
Usage : python3 verifier.py  (lit inventaire.json du même dossier, écrit resultats.json)
Chaque contrôle porte : formule, données de l'énoncé, valeur attendue (source [Sx] de sources.json),
valeur trouvée dans la leçon, tolérance, verdict CORRECT | ARRONDI | FAUX | NON_VERIFIABLE.
Les occurrences de l'inventaire sont rattachées aux contrôles par motifs ; les occurrences restantes
sont classées « non calculables » avec un motif explicite."""
import json, math, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
inv = json.load(open(os.path.join(HERE, "inventaire.json"), encoding="utf-8"))
R = []
def chk(id, objet, formule, attendu, trouve, source, motifs, tol=0.0, verdict=None, note="", calculable=True):
    if verdict is None:
        if isinstance(attendu, (int, float)) and isinstance(trouve, (int, float)):
            ecart = abs(attendu - trouve)
            verdict = "CORRECT" if ecart <= 1e-9 else ("ARRONDI" if ecart <= tol else "FAUX")
        else:
            verdict = "CORRECT" if attendu == trouve else "FAUX"
    ecart = (round(abs(attendu - trouve), 6) if isinstance(attendu, (int, float)) and isinstance(trouve, (int, float)) else None)
    R.append(dict(id=id, objet=objet, formule=formule, attendu=attendu, trouve=trouve, ecart=ecart, tolerance=tol,
                  verdict=verdict, source=source, motifs=motifs, note=note, calculable=calculable, occurrences=[]))

# ---------- 1. Vignettes et cas corrigés (recalcul à partir de l'énoncé) ----------
pas, pad = 148, 112; fc0, fc1 = 70, 73
d_pas = pas - pad; d_fc = fc1 - fc0
chk("K01", "Vignette g90-0 : baisse systolique", "148 − 112", d_pas, 36, "énoncé ; seuil ≥ 20 mmHg [S1 §4.2.2.1]", [r"148", r"112", r"= 36"])
chk("K02", "Vignette g90-0 : critère d'hypotension orthostatique", "36 ≥ 20", d_pas >= 20, True, "[S1 §4.2.2.1]", [r"seuil de 20 mmHg"])
chk("K03", "Vignette g90-0 : accélération cardiaque", "73 − 70", d_fc, 3, "énoncé", [r"73 par minute", r"70 par minute", r"de 3 battements"])
chk("K04", "Vignette g90-0 : critère neurogène (ESC « usually not > 10 b.p.m. »)", "3 ≤ 10", d_fc <= 10, True, "[S1 §4.2.2.1]", [r"plus de 10\. Cette"])
chk("K05", "Vignette g90-0 : rapport ΔFC/ΔPAS (< 0,5 bpm/mmHg en faveur du neurogène)", "3 / 36", round(d_fc/d_pas, 3), round(3/36, 3),
    "[S3 Tableau 1, note c]", [], note="Critère absent de la leçon ; recalcul de cohérence : 0,083 < 0,5, concordant avec la conclusion.")
chk("K06", "Vignette g90-0 : temps de repos et de station", "5 min couché ≥ 5 ; 3 min debout ≤ 3", True, True, "[S3 « Active standing test »]", [r"cinq minutes", r"trois minutes debout"])
a, b, f0, f1 = 150, 110, 68, 72
chk("K07", "Cas 1 : baisse systolique", "150 − 110", a-b, 40, "énoncé", [r"150 mmHg couché", r"110 mmHg à 3 minutes", r"baisse de 40 mmHg"])
chk("K08", "Cas 1 : accélération cardiaque", "72 − 68", f1-f0, 4, "énoncé ; [S1]", [r"68 à 72", r"accélération de 4"])
chk("K09", "Cas 1 : lecture « neurogène probable »", "40 ≥ 20 et 4 ≤ 10 (ΔFC/ΔPAS = 0,10 < 0,5)", (a-b) >= 20 and (f1-f0) <= 10 and (f1-f0)/(a-b) < 0.5, True, "[S1 ; S3]", [r"inférieure à 50 mmHg", r"dépasse le seuil de 20", r"inférieure à 10"])
def grade(s, d):
    # consensus : sévérité définie par la systolique OU la diastolique ; on retient la classe la plus haute
    gs = 3 if s >= 180 else 2 if s >= 160 else 1 if s >= 140 else 0
    gd = 3 if d >= 110 else 2 if d >= 100 else 1 if d >= 90 else 0
    return max(gs, gd)
chk("K10", "Cas 2 : grade d'hypertension de décubitus 168/104 après 6 min", "max(classe(168), classe(104))", grade(168, 104), 2,
    "[S2 « Definitions » : mild 140–159 or 90–99 ; moderate 160–179 or 100–109 ; severe ≥ 180 or ≥ 110]", [r"168/104", r"après 6 minutes", r"140–159", r"160–179", r"100–109", r"180/≥ 110", r"90–99"])
chk("K11", "Cas 2 : repos suffisant", "6 ≥ 5 min", 6 >= 5, True, "[S2]", [r"5 minutes de repos"])
chk("K12", "Cas 4 : niveau lésionnel T5 au-dessus ou au niveau de T6", "5 ≤ 6", 5 <= 6, True, "[S5 §2.1]", [r"5e segment thoracique", r"210/120"])
chk("K13", "Cas 4 : hausse systolique au-dessus de la base (20–40 mmHg chez l'adulte)", "210 − base inconnue", None, None, "[S5 §2.2]", [],
    verdict="NON_VERIFIABLE", note="Pression de base absente de l'énoncé : la définition (hausse par rapport à la base) ne peut être recomptée. Constat M08.")
chk("K14", "Cas 5 : critères de Budapest", "symptômes : 2 catégories < 3 requises ; signes : 2 catégories (œdème, température) ≥ 2", (2 >= 3) and (2 >= 2), False,
    "[S6 Figure 1 ; S7]", [r"3 catégories sur 4", r"3 des 4 catégories", r"2 catégories", r"deux catégories"])
chk("K15", "Cas 6 : pause de 4 s au massage", "4 > 3 s ⇒ hypersensibilité ; pas de syncope ⇒ pas de syndrome", 4 > 3, True, "[S1 §4.2.1]", [r"pause de 4 secondes", r"supérieure à 3 secondes", r"68 ans sans syncope"])
chk("K16", "Cas 7 : intervalle dernière prise de midodrine – coucher", "22 h − 21 h", 22-21, 1, "[S11 Posologie : ≥ 4 h]", [r"21 h", r"22 h", r"175/100"],
    note="1 h < 4 h : violation de la FI, correction juste. 175/100 = grade modéré (K10).")
chk("K17", "Cas 7 : dose quotidienne", "3 × 2,5 mg", 3*2.5, 7.5, "[S11 c) dose initiale 3 × 2,5 mg]", [r"3 × 2,5 mg"])
chk("K18", "Cas 8 : pression debout 88 mmHg", "88 < 90 ⇒ critère ESC rempli", 88 < 90, True, "[S1 §4.2.2.1]", [r"88 mmHg"])
# ---------- 2. Rapports et pourcentages calculés depuis des effectifs ----------
chk("K19", "Massage sinocarotidien : AIT ou AVC", "21 / 8 720 × 100", round(21/8720*100, 2), 0.24, "[S1 §4.2.1 : 21 (0,24 %) sur 8 720]", [r"0,24 %", r"21 sur 8", r"8 720"], tol=0.005)
chk("K20", "Horner isolé : cause identifiée", "18 / 88 × 100 = 20,45", round(18/88*100, 1), 20.0, "[S4 « Imaging Strategies »]", [r"chez 20 %", r"identifiée chez 20"], tol=0.5)
chk("K21", "Horner isolé : dissections", "7 / 88 = 8,0 % ; 6 / 7 douloureuses = 85,7 %", round(7/88*100, 1), 8.0, "[S4]", [r"88 Horner", r"7 étaient", r"6 douloureu", r"7 dissections"], tol=0.05,
    note="La leçon donne les effectifs bruts (7/88, 6/7), conformes ; pourcentages recalculés pour information.")
chk("K22", "Critères de Budapest : proportion de faux positifs", "1 − 0,68", round(1-0.68, 2), 0.32, "[S7 : « in 32 % of the cases »]", [r"0,68", r"0,99"],
    note="Sensibilité 0,99 et spécificité 0,68 conformes à S6 et S7. 1 − spécificité = proportion de sujets SANS la maladie qui remplissent les critères ; ce n'est pas la proportion de faux diagnostics parmi les patients positifs (valeur prédictive), qui dépend de la prévalence.")
chk("K23", "Dysautonomie familiale : risque d'un enfant malade si les deux parents sont porteurs (autosomique récessif)", "1/2 × 1/2", 0.25, 0.25,
    "[S9 : autosomique récessif ; fréquence 1/30]", [r"1 sur 30|sur 30|1/30", r"99,5 %"], calculable=True,
    note="Calcul non écrit dans la leçon (conseil génétique « les deux parents sont porteurs ») ; incidence attendue chez deux conjoints de la population de référence = (1/30)² × 1/4 = 1/3 600 naissances (estimation de Hardy-Weinberg, hypothèse d'union au hasard).")
# ---------- 3. Seuils et définitions (contrôle contre la source, cohérence inter-fichiers) ----------
chk("K24", "Hypotension orthostatique : seuils", "ΔPAS ≥ 20 ou ΔPAD ≥ 10 ou PAS < 90 mmHg", "20/10/<90", "20/10/<90", "[S1 §4.2.2.1 ; S3 Tableau 1, note b]",
    [r"20 mmHg", r"10 mmHg", r"90 mmHg", r"−20", r"−10", r"< 90", r"inférieure à 90", r"vingt-dix"], calculable=False)
chk("K25", "Seuil de 90 mmHg utile si PAS couchée < 110 mmHg", "—", 110, 110, "[S1 : « especially in patients with a supine BP < 110 mmHg »]", [r"110 mmHg"], calculable=False)
chk("K26", "Hypotension orthostatique neurogène : seuil 30 mmHg si hypertension de décubitus, 3 min, ≥ 60°", "—", "30/3 min/60°", "30/3 min/60°",
    "[S2 Introduction (définition de 2011 reprise)]", [r"30 mmHg", r"≥ 30", r"60°", r"3 minutes", r"3 premières minutes", r"dans les 3 minutes"], calculable=False,
    note="Valeurs exactes ; attribution à corriger (définition du consensus de 2011 citée par S2), constat M14.")
chk("K27", "Accélération neurogène ≤ 10 bpm", "—", 10, 10, "[S1 §4.2.2.1]", [r"10 battements", r"≤ 10"], calculable=False)
chk("K28", "Hypertension de décubitus : ≥ 140 et/ou ≥ 90 après ≥ 5 min ; grades", "—", "140/90/5 min", "140/90/5 min", "[S2 Definitions]",
    [r"140 mmHg", r"140/90", r"140, 160 et 180", r"au moins 180/110", r"180/110", r"5 minutes"], calculable=False,
    note="Le consensus définit chaque grade par la systolique OU la diastolique ; l'écriture « 180/110 » est ambiguë (constat M04).")
chk("K29", "Perte de la baisse nocturne ≥ 10 %", "—", 10, 10, "[S2 « Nocturnal hypertension »]", [r"d’au moins 10 %"], calculable=False)
chk("K30", "Lit incliné ≈ 12° (S2) ; tête > 10° (S1)", "élévation = L × sin(θ) ; L = 2,0 m", round(2.0*math.sin(math.radians(12))*100, 1), 41.6,
    "[S2 « Diagnostic work-up » ; S1 §5.3.6]", [r"12°", r"10°", r"> 10°"], tol=0.1,
    note="Recalcul d'aide pratique non écrit dans la leçon : pour un lit de 2,0 m, 12° ≈ 41,6 cm et 10° ≈ 34,7 cm de surélévation de la tête du lit.")
chk("K31", "Mesures non médicamenteuses : 2–3 L, 10 g de NaCl", "Na = 10 g / 58,44 g/mol", round(10/58.44*1000), 171, "[S1 §5.3.2]",
    [r"2 à 3 litres", r"2–3 litres", r"10 g de chlorure"], tol=0.5,
    note="Équivalence non écrite dans la leçon : 10 g de NaCl ≈ 171 mmol ≈ 3,9 g de sodium.")
chk("K32", "Massage : pause > 3 s, chute > 50 mmHg, asystolie > 6 s, > 40 ans, ≤ 40 % sans syncope", "—", "3/50/6/40/40", "3/50/6/40/40",
    "[S1 §4.2.1, message clé 6]", [r"3 s", r"> 3", r"50 mmHg", r"> 6 s", r"6 secondes", r"40 ans", r"40 %", r"plus de 40"], calculable=False)
chk("K33", "Index expiration/inspiration ≥ 15 bpm après 50 ans", "—", 15, 15, "[S1 §4.2.3.2]", [r"15 battements", r"≥ 15"], calculable=False)
chk("K34", "Mesures au sphygmomanomètre : > 4 par minute impossibles", "intervalle minimal = 60/4 s", 60/4, 15.0, "[S1 §4.2.2.1]", [r"4 mesures par minute"],
    note="Au mieux une mesure toutes les 15 s ; S3 indique « one measurement per minute at best » : divergence entre sources, sans conséquence décisionnelle.")
# ---------- 4. Posologies (FI suisses) ----------
chk("K35", "Midodrine : dose initiale formes sévères", "3 × 2,5 mg = 7,5 mg/j", 7.5, 7.5, "[S11 Posologie c)]", [r"3 × 2,5", r"2,5 mg"])
chk("K36", "Midodrine : maximum quotidien", "≤ 30 mg/j en 3 prises = 3 × 10 mg", 30, 30, "[S11 : « supérieure à 30 mg … ne peut être recommandée »]", [r"30 mg"])
chk("K37", "Midodrine ESC 2,5–10 mg × 3 cohérente avec le maximum suisse", "10 × 3 = 30 ≤ 30", 10*3 <= 30, True, "[S1 §5.3.7 ; S11]", [r"2,5 à 10 mg"])
chk("K38", "Midodrine : dernière prise ≥ 4 h avant le coucher ; prise 30–45 min avant le lever ; contrôle ≥ 2×/semaine ; titration hebdomadaire ; PAS à 3 min", "—",
    "4 h/30–45 min/2/semaine/3 min", "4 h/30–45 min/2/semaine/3 min", "[S11 Posologie]", [r"4 heures", r"≥ 4 h", r"30 à 45 minutes", r"2 fois par semaine", r"Hebdomadaire", r"3 minutes après le lever"], calculable=False)
chk("K39", "Midodrine gouttes (Gutron 10 mg/mL, 30 gouttes/mL) : équivalence de 7 gouttes", "7 × 10/30 mg", round(7*10/30, 2), 2.5, "[S12 Composition, Posologie a)]", [], tol=0.2,
    verdict="ARRONDI", note="Forme absente de la leçon (enrichissement E04) : 7 gouttes = 2,33 mg ≈ 2,5 mg ; 15 gouttes = 5,0 mg.")
chk("K40", "Fludrocortisone : posologie suisse 0,1 mg 3×/semaine à 0,2 mg/j ; ≤ 0,05 mg/j si hypertension", "0,1 × 3 / 7 = 0,043 mg/j moyen",
    round(0.1*3/7, 3), 0.043, "[S13 Posologie usuelle]", [r"0,1 mg trois fois", r"0,2 mg par jour", r"0,05 mg"], tol=0.001,
    note="0,05 mg = ½ comprimé de 0,1 mg ; la FI n'indique pas de comprimé sécable (non vérifiable).")
chk("K41", "Fludrocortisone ESC 0,1–0,3 mg/j versus norme suisse 0,1 mg/j, maximum usuel 0,2 mg/j", "0,3 > 0,2", 0.3 > 0.2, True,
    "[S1 §5.3.8 ; S13]", [r"0,1 à 0,3 mg", r"0,1–0,3 mg"], calculable=True,
    note="La borne haute de l'ESC dépasse la posologie usuelle maximale de la FI suisse ; la leçon ne le signale pas (constat M06).")
chk("K42", "Apraclonidine 0,5 % (30–45 min ; surveiller 2 h ; < 6 mois), cocaïne 2–10 % (≥ 0,8 mm à 45 min), hydroxyamphétamine 0,5 % (2–3 semaines), phényléphrine 1 % (Se 81 %, Sp 100 %)",
    "—", "conforme", "conforme", "[S4 Apraclonidine, Cocaine, Hydroxyamphetamine, Phenylephrine]",
    [r"0,5 %", r"2 à 10 %", r"0,8 mm", r"45 minutes", r"30–45 minutes", r"2 heures", r"6 mois", r"1 %", r"81 %", r"100 %", r"16 jours", r"3 ans", r"2–3 premières"], calculable=False)
chk("K43", "Nitroglycérine pâte 2 % (dysréflexie)", "—", "pâte 2 % : aucune FI suisse trouvée ; CI inhibiteurs PDE5 (24 h)", "pâte 2 % sans CI",
    "[S5 §4.1 ; S14 Contre-indications, Interactions ; S21]", [r"2 %"], calculable=False, verdict="FAUX",
    note="Valeur conforme à la source américaine, mais forme non commercialisée en Suisse selon AmiKo et contre-indication PDE5 omise : constat C02.")
# ---------- 5. Données épidémiologiques et pronostiques (contrôle contre la source) ----------
for id_, obj, att, src, mot in [
    ("K44", "Horner : myosis 98 %, ptosis 88 %, anhidrose 4 % (n = 450)", "98/88/4/450", "[S4 « Clinical presentation »]", [r"98 %", r"88 %", r"4 %", r"450"]),
    ("K45", "Müller : 2–3 mm ; retard de dilatation ≈ 5 s", "2–3 mm/5 s", "[S4 « Ptosis », « Miosis »]", [r"2 à 3 mm", r"2 à 3 mm", r"5 secondes", r"Müller 2 à 3"]),
    ("K46", "Horner : malignité jusqu'à 25 % (préganglionnaire) ; neuroblastome 3,5–13 %", "≤ 25/3,5–13", "[S4]", [r"25 %", r"3,5 à 13"]),
    ("K47", "Imagerie jusqu'à T4–T5 ; centre C8–T2 ; ganglion C2–C3", "T4–T5/C8–T2/C2–C3", "[S4 « Anatomy », « Imaging »]", [r"4e–5e", r"8e segment cervical", r"2e thoracique", r"2e au 3e"]),  # ordinaux classés « repères » dans l'inventaire : contrôle par lecture
    ("K48", "Dysréflexie : 48–91 % ≥ T6 ; 325 mmHg ; 88 % céphalée-sudation ; 5,7 % 1er mois ; 3–6 mois ; 20–40 adulte, 15–20 enfant ; PA /2–5 min", "conforme", "[S5 §2.1–2.2, §4]",
     [r"48 à 91", r"48–91", r"325", r"88 % des cas", r"5,7 %", r"3 à 6 mois", r"20 à 40", r"15 à 20", r"2 à 5 minutes", r"6e segment"]),
    ("K49", "Vessie ≈ 85 % des dysréflexies", "85", "[S15 résumé]", [r"85 %"]),
    ("K50", "Hypertension de décubitus : PD 34–46 %, AMS 37 %, perte du dipping AMS ≤ 75 %, dysautonomie pure 48–70 %", "conforme", "[S2 « Epidemiology »]", [r"34 à 46", r"37 %", r"75 %", r"48 à 70"]),
    ("K51", "SDRC : 5,5–26,2/100 000 ; 7 % après fracture ; ≈ 5 % sans traumatisme ; 18 mois ; 2 mois ; 40 % ; 15–20 %", "conforme", "[S6 ; S7]",
     [r"5,5 à 26,2", r"5,5–26,2", r"7 %", r"5 %", r"18 mois", r"2 mois", r"40 %", r"15 à 20"]),
    ("K52", "POTS : 15–45 ans, ≈ 80 % de femmes, 0,2–1,0 %, ≈ 50 % de guérison en 1–3 ans", "conforme", "[S8 résumé]", [r"15 à 45", r"15–45", r"80 %", r"0,2 à 1", r"0,2–1", r"50 %", r"1 à 3 ans"]),
    ("K53", "Horner après chirurgie thyroïdienne endoscopique 0,03–0,48 % ; correction du ptosis au-delà d'un an", "conforme", "[S16 Discussion]", [r"0,03 à 0,48", r"un an"]),
    ("K54", "Dysautonomie familiale : 1/30 porteurs ; 99,5 % homozygotes ; exon 20", "conforme", "[S9 résumé]", [r"99,5"]),
]:
    chk(id_, obj, "lecture de la source", att, att, src, mot, calculable=False)
chk("K55", "SDRC : « environ 15 % ne sont pas améliorés à 2 ans »", "recherche du chiffre dans S6 et S7", "absent (S6 : SDRC non résolu ≈ 15–20 %, sans horizon de 2 ans)", "15 % à 2 ans",
    "[S6 « Long-term management » ; S7]", [r"15 % ne sont pas", r"15 % non améliorés"], calculable=False, verdict="FAUX",
    note="Chiffre non retrouvé dans les sources citées ; probable confusion avec 15–20 % de SDRC non résolu. Constat M01.")
chk("K56", "Figure 3 : « malignité dans 25 % »", "S4 : « up to 25 % »", "jusqu'à 25 %", "dans 25 %", "[S4 « Preganglionic »]", [r"dans 25 %"], calculable=False, verdict="FAUX",
    note="Borne présentée comme une valeur : constat M02.")
chk("K57", "Test d'inclinaison ≥ 60° ; repos ≥ 5 min ; 3 min debout ; équipement ≥ 1 dérivation", "—", "conforme", "conforme", "[S3]", [r"≥ 1 dérivation", r"au moins une dérivation", r"≥ 60°", r"au moins 60°"], calculable=False)

chk("K58", "Dosage commercialisé : Florinef comprimés 0,1 mg ; Midodrin Substipharm 2,5 et 5 mg", "—", "0,1 mg ; 2,5/5 mg", "0,1 mg ; 2,5 mg",
    "[S13 Forme pharmaceutique ; S11 Forme pharmaceutique]", [r"Florinef 0,1 mg"], calculable=False, verdict="CORRECT")
# ---------- 6. Calculs des propositions de l'audit (cas nouveaux, non présents dans la leçon) ----------
chk("P01", "Proposition, cas A : 132 → 104 mmHg ; 64 → 71/min", "ΔPAS = 28 ≥ 20 ; ΔFC = 7 ≤ 10 ; ΔFC/ΔPAS = 0,25 < 0,5",
    (132-104, 71-64, round((71-64)/(132-104), 2)), (28, 7, 0.25), "[S1 §4.2.2.1 ; S3 Tableau 1 note c]", [], note="propositions/G90_c_semio.html, cas A")
chk("P02", "Proposition, cas B : 22 ans, FC 72 → 108/min à 8 min, PAS 118 → 112 mmHg", "ΔFC = 36 > 30 (seuil adulte ≥ 20 ans) ; ΔPAS = 6 < 20 ; 8 ≤ 10 min",
    (108-72 > 30, 118-112 < 20, 8 <= 10), (True, True, True), "[S3 Tableau 1, notes d et e]", [], note="propositions/G90_c_semio.html, cas B")
chk("P03", "Proposition, cas B bis : même profil à 16 ans", "ΔFC = 36 ≤ 40 (seuil 12–19 ans) ⇒ critère non rempli", 108-72 > 40, False, "[S3 Tableau 1, note e]", [],
    note="propositions/G90_c_semio.html, fenêtre g90-sm-pots")
chk("P04", "Proposition, OH initiale : 140 → 92 mmHg à 10 s puis récupération", "ΔPAS = 48 > 40 en ≤ 15 s", (140-92 > 40, 10 <= 15), (True, True), "[S3 Tableau 1]", [],
    note="propositions/G90_b_1.html")
chk("P05", "Proposition, hospitalisé : couché 168, assis 150 mmHg", "différence 18 > 10 ⇒ mesurer debout", 168-150 > 10, True, "[S2 « Diagnostic work-up »]", [],
    note="propositions/G90_mineurs.html")
chk("P06", "Proposition M08 : cas 4 avec pression habituelle 100/60 mmHg", "210 − 100 = 110 ≥ 20–40 mmHg", 210-100 >= 20, True, "[S5 §2.2]", [],
    note="propositions/remplacements.json, M08 : l'énoncé corrigé rend la définition vérifiable.")
chk("P07", "Proposition E03 : Gutron, gouttes nécessaires pour 2,5 mg et 5 mg", "dose / (10 mg / 30 gouttes)", (round(2.5/(10/30), 1), round(5/(10/30), 1)), (7.5, 15.0), "[S12]", [],
    note="La FI arrondit à 7 gouttes (2,33 mg) et 15 gouttes (5,0 mg) ; la proposition écrit « 7 gouttes apportent 2,3 mg ».")
# Occurrences non calculables par nature (motif explicite)
NONCALC = [
    (r"chapitre 6", "renvoi interne à un îlot"),
    (r"Elongator-1|'1'|protein 1|ELP1', \[", "nom de protéine ou de gène (Elongator-1, ELP1)"),
    (r"consultées le 15 octobre", "date de consultation"),
    (r"réévaluation à 3 mois", "distracteur de quiz (option volontairement fausse, sans calcul)"),
    (r"patient de 72 ans", "âge d'un cas fictif, sans calcul"),
    (r"symptômes dans 3 catégories, signes dans 2", "rappel Pareto du critère de Budapest (contrôlé en K14)"),
    (r"N-05-Neurologie", "identifiant de fragment"),
    (r"(1\. Cause médicamenteuse|4\. Contention)", "numéro d'étape d'un tableau"),
]
# ---------- rattachement des occurrences ----------
vals = [o for o in inv["occurrences"] if o["nature"] == "valeur"]
for o in vals:
    o["controles"] = [r["id"] for r in R if any(re.search(m, o["contexte"]) for m in r["motifs"])]
    for r in R:
        if r["id"] in o["controles"]:
            r["occurrences"].append(o["id"])
for o in vals:
    if not o["controles"]:
        o["non_calculable"] = next((m for r_, m in NONCALC if re.search(r_, o["contexte"])), None)
non_rattachees = [o for o in vals if not o["controles"] and not o.get("non_calculable")]
non_calc_expl = [o for o in vals if not o["controles"] and o.get("non_calculable")]
calc = [r for r in R if r["calculable"]]
res = {
    "script": "calculs/verifier.py",
    "inventaire": "calculs/inventaire.json",
    "total_releves": inv["total_releves"],
    "reperes_non_calculables": inv["reperes_non_calculables"],
    "valeurs": len(vals),
    "valeurs_rattachees_a_un_controle": sum(1 for o in vals if o["controles"]),
    "valeurs_non_calculables_motivees_n": len(non_calc_expl),
    "valeurs_non_calculables_motivees": [{"id": o["id"], "fichier": o["fichier"], "valeur": o["valeur"] + " " + o["unite"], "motif": o["non_calculable"]} for o in non_calc_expl],
    "valeurs_non_rattachees": [{"id": o["id"], "fichier": o["fichier"], "ancre": o["ancre"], "valeur": o["valeur"] + " " + o["unite"], "contexte": o["contexte"]} for o in non_rattachees],
    "controles": len(R),
    "calculables": len(calc),
    "recalcules": len(calc),
    "controles_contre_source": len(R) - len(calc),
    "correct": sum(1 for r in R if r["verdict"] == "CORRECT"),
    "arrondi": sum(1 for r in R if r["verdict"] == "ARRONDI"),
    "faux": sum(1 for r in R if r["verdict"] == "FAUX"),
    "non_verifiables": sum(1 for r in R if r["verdict"] == "NON_VERIFIABLE"),
    "resultats": [{k: v for k, v in r.items() if k != "motifs"} for r in R],
}
json.dump(res, open(os.path.join(HERE, "resultats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ("resultats", "valeurs_non_rattachees", "valeurs_non_calculables_motivees")}, ensure_ascii=False))
print("non rattachées :", len(non_rattachees))
for o in non_rattachees: print(" ", o["id"], o["fichier"].split("/")[-1], o["ancre"], "|", o["valeur"], o["unite"], "|", o["contexte"][:110])
