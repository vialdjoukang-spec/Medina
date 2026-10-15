# Rapport de rédaction — D63 Anémie au cours de maladies chroniques classées ailleurs (H-08-Hématologie)

Cycle Betta 31, agent C31-A4-HEM, leçon 1 (Sonnet 5.5). Date : 14.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers livrés (dossier CYCLE_31_D63)
- chapters/D63/D63_a.html (26 Ko) : en-tête, quatre onglets, Pathologie îlots 0 à 6.
- chapters/D63/D63_b.html (33 Ko) : Pathologie îlots 7 à 14 (algorithme, gravité, traitement, contextes, suivi, limites, critères formels `alert` puis paramètres clés `key`).
- chapters/D63/D63_c.html (29 Ko) : Examens (5 îlots, 6 fiches d'interprétation, tableau des configurations, 3 quiz) et Sciences (Physiologie, Biochimie, Hématologie cellulaire, Immunologie ; 3 schémas SVG noir et blanc légendés).
- chapters/D63/D63_d.html (11 Ko) : Pharmacologie (5 îlots).
- chapters/D63/D63_pop1.html (16 Ko), D63_pop2.html (13 Ko) : 36 fenêtres dont 12 Pareto (clés `d63-…`, `pareto-d63-…`).
- glossary/d63.py : codes D63.0/D63.8/D63.1, CIM-10-CM, N18.3 à N18.5, G3, PU.1, Bence-Jones (entrées conditionnelles).
- Environ 14 000 mots ; 8 quiz de cas pédagogiques fictifs (dont 4 dans la Pathologie, 3 dans l’onglet Examens, 1 en Pharmacologie).

## Sources utilisées (toutes issues de sources.json, consultées le 14.10.2026)
Weiss 2019 (Blood) ; Celi 2011 (Revue Médicale Suisse, algorithme genevois) ; Nendaz et Samii 2011 (HUG) ; Delphi suisse 2019 ; BfArM CIM-10-GM 2024 (D63.0*, D63.8*, pas de D63.1) ; KDIGO 2026 (illustrations centrales) ; ESC 2023 (carence martiale) ; informations professionnelles Eprex (août 2021) et Ferinject (juin 2025) ; recherche AIPS (HIF-PHI non retrouvés).
Aucune donnée hors dossier. Les quelques articulations de raisonnement du cours (par exemple le rôle de la protéine C réactive comme pivot, la lecture des lignes du tableau des configurations) sont signalées comme telles dans le texte.

## Lacunes explicites (reprises dans l'îlot 13 et la fenêtre « Sources »)
ESMO 2018 non lu ; ECCO 2015 non lu ; seuils OMS 2024 non lus ; aucun seuil transfusionnel chiffré ; aucune source suisse récente (SSH, Forum Médical Suisse) ; KDIGO lu par ses illustrations (terminologie et rythme de surveillance de l'hémoglobine à confirmer) ; informations professionnelles Aranesp, Mircera, Recormon, Venofer non lues, remboursement non vérifié ; posologie initiale de l'époétine et formule de Ganzoni non reproduites ; aucune sémiologie propre à l'anémie inflammatoire ; aucune donnée épidémiologique suisse récente ; sens des régulateurs de l'hepcidine autres que l'inflammation non détaillé.

## Auto-contrôle du cahier W
- Quatre onglets pA, pE, pS, pP ; dernier îlot de la pathologie = critères formels (`div.alert`) puis paramètres clés (`div.key`) ; Pareto en fin de chaque grande partie.
- HTML bien formé (analyse de pile balises : aucune erreur), ids uniques et préfixés `d63-`, toutes les clés `data-k` ont leur fenêtre (36 fenêtres, 0 manquante, 0 inutilisée).
- Glossaire : `build_medina.audit` renvoie « D63 non couvertes: 0 ».
- Aperçu navigateur (harnais isolé hors dépôt, copie des fichiers) : cours affiché, fenêtres, quatre onglets, mode livre : OK (l'erreur de module `lesson-core.js` du script d'origine est propre à l'environnement et a été ignorée).
- Rien n'a été modifié dans chapters/ racine, glossary/ racine, chapters.json ni git.
