# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K57', 'Maladie diverticulaire de l’intestin : diverticulose et diverticulite aiguë',
    'K57 — Maladie diverticulaire de l’intestin · CIM-10-GM 2024 · Côlon et intestin grêle',
    'Adulte · diverticulose, diverticulite aiguë du côlon gauche et droit, non compliquée et compliquée (abcès, perforation, péritonite) · rédaction du 09.10.2026 · référentiels WSES diverticulite aiguë 2020, guide d’antibiothérapie empirique du CHUV 2022, informations professionnelles suisses',
    'Pharmacologie de la diverticulite')
w = C.w
WSES = ('Sartelli M. et al., 2020 update of the WSES guidelines for the management of acute colonic diverticulitis in the emergency setting, World J Emerg Surg 2020;15:32', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7206757/')
CHUV = ('Service des maladies infectieuses et Pharmacie du CHUV, Guide d’antibiothérapie empirique chez l’adulte, version de mai 2022 (infections intra-abdominales, p. 22-23 ; posologies usuelles, p. 52)', 'https://www.chuv.ch/fileadmin/sites/min/552801_22_DM_DAM_guide_antibiotherapie_version_mai_2022.pdf')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')
CT = credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:03-Sigmadivertikulitis_CT_ax_001_Kleiner_Abszess.png'})

C.a(0, 'Question clinique et objectifs', P(
 'Une femme de 62 ans, sans immunosuppression, a depuis deux jours une douleur de la fosse iliaque gauche, une fièvre à 38,0 °C et une CRP à 85 mg/l ; elle boit et s’alimente. <b>La question est donc de savoir s’il s’agit d’une ' + w('k57-dva', 'diverticulite aiguë') + ', si elle est compliquée, et si elle a vraiment besoin d’antibiotiques et d’une hospitalisation.</b>',
 'Pour y répondre, le médecin doit savoir : ne pas poser le diagnostic sur le seul examen clinique ; demander un ' + w('k57-tdm', 'scanner abdominal injecté') + ' ; classer l’épisode selon la ' + w('k57-classif', 'classification WSES') + ' ; ensuite, renoncer aux antibiotiques dans la forme non compliquée de l’immunocompétent, traiter l’abcès selon sa taille, et opérer la péritonite ; enfin, décider de la coloscopie et de la chirurgie à froid.')
 + P('<i>Pourquoi ce cas ?</i> En effet, il réunit les trois décisions qui changent le pronostic : imagerie, antibiotiques et lieu de prise en charge. Ainsi, contrairement à un manuel figé, chaque mot vert ouvre le critère exact et sa source, si bien que le raisonnement peut être refait au lit du patient.')
 + key('Douleur de la fosse iliaque gauche + fièvre + CRP : scanner injecté → classification WSES → traitement selon le stade.', 'Point de départ.'))

C.a(1, 'Définitions et épidémiologie', P(
 'La ' + w('k57-dvose', 'diverticulose') + ' désigne la présence de diverticules, petites hernies de la muqueuse à travers la paroi colique ; or, elle est le plus souvent asymptomatique. En revanche, la diverticulite est l’inflammation, souvent infectieuse, d’un ou de plusieurs diverticules ; elle est dite non compliquée si l’inflammation reste dans la paroi colique, et compliquée si le processus infectieux dépasse le côlon (WSES 2020).',
 'Par ailleurs, la prévalence de la diverticulose augmente partout dans le monde, probablement en raison du mode de vie ; de plus, son incidence progresse chez les sujets jeunes. Ainsi, le risque, au cours de la vie, de faire une diverticulite gauche est d’environ 4 % chez les porteurs de diverticules, et jusqu’à un cinquième des patients atteints ont moins de 50 ans dans les populations occidentales. Enfin, le côlon sigmoïde est le siège le plus fréquent, alors que la diverticulite droite est plus rare en Occident mais prédomine dans certaines régions du monde (WSES 2020).')
 + C.img('k57_piece.gif', 'Pièce opératoire de côlon ouverte : nombreux petits orifices ronds alignés dans la muqueuse, chacun menant à un diverticule.', 'Diverticulose colique, pièce opératoire : chaque orifice de la muqueuse ouvre un diverticule, poche qui traverse la musculeuse.', credit({'auteur': 'Mikael Häggström', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Gross_pathology_of_diverticulosis.jpg'}))
 + P('<i>Lecture de l’image.</i> Les orifices sont alignés ; en effet, les diverticules naissent aux points faibles de la paroi, là où les vaisseaux droits traversent la musculeuse pour gagner la muqueuse. Ainsi, une poche sans couche musculaire propre se forme, qui se vide mal ; c’est pourquoi elle peut s’enflammer (diverticulite) ou éroder le vaisseau voisin (hémorragie diverticulaire).')
 + key('Diverticulose = poches ; diverticulite = inflammation ; non compliquée = limitée à la paroi ; compliquée = au-delà du côlon ; risque ≈ 4 % chez les porteurs ; sigmoïde le plus souvent.')
 + src(WSES))

C.a(2, 'Physiopathologie : de la poche à la péritonite', P(
 'La diverticulite naît d’une poche qui se draine mal ; ainsi, l’inflammation débute dans la paroi du diverticule, puis gagne la graisse péricolique. Ensuite, si la paroi cède, une perforation contenue produit des bulles de gaz près du côlon, puis un abcès ; enfin, si la perforation est libre, l’air et le pus, voire les selles, diffusent dans le péritoine. Par conséquent, chaque stade de la classification WSES correspond à une étape anatomique de cette progression.',
 'Cependant, la défense locale suffit souvent. En effet, la WSES rappelle que la diverticulite non compliquée peut être une maladie autolimitée, que les défenses de l’hôte contrôlent sans antibiotique chez l’immunocompétent. En revanche, l’immunodéprimé ne contient pas l’infection : il fait plus souvent des formes compliquées et échoue davantage au traitement non opératoire, si bien qu’il est considéré à haut risque (WSES 2020).')
 + table(['Étape anatomique', 'Traduction au scanner', 'Stade WSES'], [
   ['Inflammation pariétale et péricolique', 'Paroi épaissie, graisse infiltrée', '0'],
   ['Perforation couverte', 'Bulles de gaz péricoliques', '1a'],
   ['Abcès au contact', 'Abcès < 4 cm', '1b'],
   ['Abcès pelvien', 'Abcès > 4 cm dans le pelvis', '2a'],
   ['Abcès à distance', 'Abcès hors du pelvis', '2b'],
   ['Perforation libre', 'Pneumopéritoine abondant et/ou liquide libre', '3 et 4']])
 + P('<i>Lecture du tableau.</i> Chaque ligne descend d’un étage dans la diffusion de l’infection ; or, plus l’infection s’éloigne du côlon, moins l’organisme peut la circonscrire. C’est pourquoi le traitement passe de la simple surveillance à l’antibiothérapie, puis au drainage, puis à la chirurgie.')
 + key('Poche mal drainée → inflammation → perforation couverte → abcès → perforation libre ; l’immunocompétent contient souvent seul la forme simple ; l’immunodéprimé non.')
 + src(WSES))

C.a(3, 'Présentation clinique et diagnostic', P(
 'Classiquement, la diverticulite gauche se traduit par une douleur ou une sensibilité aiguë du quadrant inférieur gauche, avec une élévation de la CRP et des leucocytes. Cependant, le diagnostic clinique manque de précision ; en effet, dans une série prospective de 802 patients, sa valeur prédictive positive n’était que de 0,65, contre 0,95 après imagerie en coupes. C’est pourquoi la WSES suggère une évaluation complète, associant anamnèse, examen, marqueurs inflammatoires et imagerie, et déconseille de conclure sur l’examen seul (WSES 2020).',
 'Par ailleurs, la CRP renseigne sur la gravité. Ainsi, dans une étude citée par la WSES, une CRP initiale supérieure à 173 mg/l prédisait un stade supérieur à Hinchey Ib avec une sensibilité et une spécificité de 90,9 % ; de plus, tous les patients drainés ou opérés avaient une CRP au-delà de ce seuil. Toutefois, ce seuil provient d’une seule étude et ne remplace pas l’imagerie.')
 + quiz('Une femme de 62 ans a une douleur de la fosse iliaque gauche typique, une fièvre et une CRP élevée. Que suggère la WSES ?',
   [('Traiter sur le seul tableau clinique, typique', False), ('Compléter par une imagerie, de préférence un scanner injecté', True), ('Faire une coloscopie en urgence', False)],
   'La valeur prédictive positive de la clinique seule est faible (0,65) ; le scanner injecté est l’imagerie de premier choix (WSES 2020, recommandation 2B).')
 + key('Douleur du quadrant inférieur gauche + CRP + leucocytes ; jamais de diagnostic sur la clinique seule ; CRP > 173 mg/l : forme probablement compliquée (donnée d’une étude).')
 + src(WSES))

C.a(4, 'Imagerie et classification WSES', P(
 'L’imagerie confirme donc le diagnostic et fixe le stade. Ainsi, le scanner abdominal injecté est l’examen de premier choix (recommandation 2B) ; cependant, l’' + w('k57-echo', 'échographie') + ' peut être utilisée en premier par un opérateur expert, avec un scanner si elle est non concluante ou négative (recommandation 2B). Ensuite, le compte rendu classe l’épisode selon la classification WSES, fondée sur le scanner.',
 'En effet, cette classification distingue la forme non compliquée (stade 0 : diverticules, paroi épaissie, densification de la graisse) des formes compliquées : 1a, bulles de gaz localisées ; 1b, abcès de moins de 4 cm ; 2a, abcès pelvien de plus de 4 cm ; 2b, abcès à distance hors du pelvis ; 3, péritonite purulente diffuse ; 4, péritonite stercorale (WSES 2020). Par conséquent, la taille et le siège de l’abcès, ainsi que la quantité d’air et de liquide libres, commandent le traitement.')
 + C.img('k57_abces.gif', 'Scanner abdominal en coupe axiale : côlon sigmoïde à paroi épaissie, porteur de multiples diverticules, avec une petite collection au contact.', 'Diverticulite sigmoïdienne au scanner axial : diverticules multiples, perforation couverte et petit abcès au contact du côlon (stade WSES 1b).', CT)
 + P('<i>Lecture de l’image.</i> La paroi épaissie traduit l’inflammation ; de plus, la petite collection signe la perforation couverte, que la graisse péricolique a cloisonnée. Ainsi, l’abcès étant petit, un traitement par antibiotiques seuls est tenté d’abord ; en revanche, au-delà de 4 à 5 cm, le drainage percutané devient la règle.')
 + key('Scanner injecté en premier (échographie si expert) ; WSES 0 = simple ; 1a gaz ; 1b abcès < 4 cm ; 2a abcès pelvien > 4 cm ; 2b à distance ; 3 péritonite purulente ; 4 stercorale.')
 + src(WSES))

C.a(5, 'Traitement de la diverticulite non compliquée', P(
 'Dans la forme non compliquée, la stratégie s’est allégée. Ainsi, chez l’immunocompétent sans signe d’inflammation systémique, la WSES recommande de ne pas prescrire d’antibiotique (recommandation forte, 1A) ; en effet, dans l’essai DIABOLO, la surveillance sans antibiotique n’a pas prolongé la guérison d’un premier épisode prouvé au scanner. De même, le CHUV admet une approche sans antibiotique si le scanner montre une inflammation péricolique sans abcès ni complication, sans sepsis ni immunosuppression, avec un suivi ambulatoire rapproché.',
 'Par ailleurs, le patient sans comorbidité qui boit et se gère seul peut être traité en ambulatoire, avec une réévaluation dans les 7 jours, ou plus tôt s’il s’aggrave (recommandation 2B). En revanche, lorsque des antibiotiques sont nécessaires, la voie orale est recommandée chaque fois que possible (recommandation forte, 1B) ; le CHUV propose alors l’' + w('k57-d-coamox', 'amoxicilline-acide clavulanique') + ' pendant 7 jours. Enfin, le CHUV conseille d’éviter les AINS.')
 + trap('« Pas d’antibiotique » ne veut pas dire « pas de suivi » : l’abstention n’est sûre que chez l’immunocompétent, sans sepsis, avec une forme prouvée non compliquée au scanner et une réévaluation dans les 7 jours.', 'Piège')
 + key('Non compliquée, immunocompétent, sans inflammation systémique : pas d’antibiotique (1A) ; ambulatoire si possible, contrôle ≤ 7 jours ; si antibiotique : per os, co-amoxicilline 7 jours (CHUV) ; éviter les AINS.')
 + src(WSES, CHUV))

C.a(6, 'Formes localement compliquées : gaz et abcès', P(
 'Dès que l’infection dépasse la paroi, les antibiotiques deviennent la base. Ainsi, en cas de gaz extraluminal péricolique, un traitement non opératoire par antibiotiques est suggéré (recommandation 2C). De plus, pour un ' + w('k57-abces', 'abcès') + ' de moins de 4 à 5 cm, un essai initial d’antibiotiques seuls est suggéré (2C) ; en revanche, un gros abcès relève d’un drainage percutané associé aux antibiotiques, ou, si le drainage est impossible, d’antibiotiques seuls si l’état le permet, sinon d’une intervention (2C).',
 'Ensuite, en cas d’air libre à distance sans liquide intra-abdominal diffus, un traitement non opératoire n’est suggéré que chez des patients sélectionnés et étroitement surveillés (2D). Par ailleurs, après un abcès traité sans chirurgie, une évaluation colique précoce, à 4 à 6 semaines, est suggérée (2C) ; en effet, un cancer peut simuler un abcès diverticulaire. En revanche, après une diverticulite non compliquée prouvée au scanner, la coloscopie systématique n’est pas recommandée (2B) : dans une revue de 1 468 coloscopies, la prévalence du cancer colorectal était de 1,16 %.')
 + key('Gaz péricolique ou abcès < 4-5 cm : antibiotiques ; gros abcès : drainage percutané + antibiotiques ; abcès traité sans chirurgie : coloscopie à 4-6 semaines ; forme simple : pas de coloscopie systématique.')
 + src(WSES))

C.a(7, 'Péritonite diverticulaire', P(
 'La perforation libre impose en revanche la chirurgie. Ainsi, l’' + w('k57-hartmann', 'intervention de Hartmann') + ' est recommandée pour la péritonite diffuse du patient en état critique ou porteur de multiples comorbidités (recommandation forte) ; cependant, chez le patient stable sans comorbidité, une résection avec anastomose d’emblée, protégée ou non par une stomie, est suggérée (2B). De plus, la sigmoïdectomie laparoscopique en urgence n’est suggérée que si l’expertise et l’équipement sont disponibles (2C).',
 'Par ailleurs, le lavage péritonéal laparoscopique n’est pas un traitement de première ligne ; il est réservé à des patients très sélectionnés (2A). Enfin, chez le patient instable, une chirurgie de contrôle des dommages, avec laparotomies itératives, est suggérée (2C) : la première intervention contrôle le sepsis, et la suivante rétablit la continuité digestive.')
 + key('Péritonite : Hartmann si critique ou comorbide ; résection-anastomose si stable ; laparoscopie si expertise ; lavage seul exceptionnel ; contrôle des dommages si instable.')
 + src(WSES))

C.a(8, 'Antibiothérapie des formes compliquées', P(
 'Le choix de l’antibiotique dépend de l’état du patient, des germes présumés et des facteurs de résistance (recommandation forte, 1B). Ainsi, le CHUV propose, sans critère de gravité, l’amoxicilline-acide clavulanique, ou la ciprofloxacine associée au métronidazole en cas d’allergie, pendant 7 jours ; en revanche, en cas d’infection sévère ou de risque de Pseudomonas aeruginosa, la ' + w('k57-d-pipt', 'pipéracilline-tazobactam') + ' ou un carbapénème, réservé aux germes multirésistants documentés.',
 'Ensuite, après une chirurgie avec contrôle adéquat de la source, une antibiothérapie postopératoire de 4 jours est suggérée (2B). De même, pour la péritonite secondaire communautaire, le CHUV envisage l’arrêt après 3 jours si le contrôle chirurgical est optimal, l’apyrexie dure depuis au moins un jour, le transit a repris et l’inflammation diminue. Enfin, un sepsis persistant au-delà de 5 à 7 jours d’antibiothérapie adaptée impose de chercher un foyer résiduel (WSES 2020).')
 + key('Sans gravité : co-amoxicilline (ou ciprofloxacine + métronidazole) 7 jours ; sévère : pipéracilline-tazobactam ; après chirurgie et source contrôlée : ≈ 4 jours ; sepsis > 5-7 jours : chercher un foyer.')
 + src(WSES, CHUV))

C.a(9, 'Après l’épisode : récidive et chirurgie à froid', P(
 'Après l’épisode aigu, la question est celle de la récidive. Or, elle est plus rare qu’on ne le pensait : ainsi, une étude prospective rapporte 1,7 % de récidive sur 5 ans après un épisode non compliqué, et une étude anglaise de plus de 65 000 patients, 11,2 % à 4 ans, avec des colectomies en urgence de 0,9 % et programmées de 0,75 %. De plus, le sexe féminin, le jeune âge, le tabac, l’obésité et un premier épisode compliqué prédisposent à la réhospitalisation.',
 'C’est pourquoi la WSES suggère de fonder la ' + w('k57-sigmo', 'sigmoïdectomie programmée') + ' sur les facteurs propres au patient, et non sur le nombre d’épisodes (2D) ; ainsi, elle la propose chez le patient à haut risque, comme l’immunodéprimé (2D). Enfin, la diverticulite droite suit les mêmes principes que la gauche (WSES 2020).')
 + key('Récidive après forme simple : 1,7 % à 5 ans (prospectif) à 11,2 % à 4 ans ; chirurgie à froid selon le patient (immunodéprimé), pas selon le nombre d’épisodes ; côlon droit : mêmes principes.')
 + C.pareto('pareto-k57-clinique', 'Maladie diverticulaire', ['k57-3', 'k57-4', 'k57-5', 'k57-6', 'k57-7', 'k57-9'],
     ['Jamais de diagnostic sur la clinique seule.',
      'Scanner injecté ; classification WSES.',
      'Forme simple, immunocompétent : pas d’antibiotique, suivi ≤ 7 jours.',
      'Abcès < 4-5 cm : antibiotiques ; plus gros : drainage.',
      'Péritonite : Hartmann ou résection-anastomose.',
      'Chirurgie à froid selon le patient, pas selon le nombre d’épisodes.'])
 + src(WSES))

C.a(10, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons la patiente du début. Le scanner injecté montre un sigmoïde épaissi avec des diverticules et une densification de la graisse, sans gaz ni abcès : il s’agit donc d’une diverticulite non compliquée, stade WSES 0. De plus, elle est immunocompétente, sans signe de sepsis, et peut boire.',
 'Dès lors, la conduite est simple. D’abord, elle rentre à domicile sans antibiotique, avec du paracétamol et sans AINS. Ensuite, elle est revue dans les 7 jours, ou plus tôt si la douleur ou la fièvre augmente. Enfin, aucune coloscopie systématique n’est prévue pour cet épisode, mais le dépistage du cancer colorectal reste proposé selon son âge.')
 + key('Scanner → WSES 0 → immunocompétente → ambulatoire sans antibiotique → contrôle ≤ 7 jours → pas de coloscopie systématique.')
 + src(WSES, CHUV))

C.a(11, 'Critères formels et paramètres clés', alert(
 '<p><b>Classification WSES (scanner).</b> 0 : paroi épaissie, graisse densifiée ; 1a : bulles de gaz localisées ; 1b : abcès < 4 cm ; 2a : abcès pelvien > 4 cm ; 2b : abcès hors du pelvis ; 3 : péritonite purulente diffuse ; 4 : péritonite stercorale. <b>Abstention antibiotique (CHUV).</b> Inflammation péricolique sans abcès ni complication, sans sepsis, sans immunosuppression, suivi rapproché.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Risque de diverticulite ≈ 4 % chez les porteurs ; VPP de la clinique 0,65 contre 0,95 avec imagerie ; abcès : seuil 4-5 cm ; coloscopie à 4-6 semaines après abcès ; antibiotiques postopératoires ≈ 4 jours ; récidive 1,7-11,2 %.</div>'
 + src(WSES, CHUV))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Recommandation'], [
   ['Inflammation ?', 'CRP, leucocytes', 'Évaluation complète (WSES 2D)'],
   ['Diagnostic et stade ?', w('k57-tdm', 'Scanner abdominal injecté'), 'Premier choix (WSES 2B)'],
   ['Alternative ?', w('k57-echo', 'Échographie par un expert'), 'Puis scanner si non concluante (2B)'],
   ['Gros abcès ?', 'Drainage percutané guidé', 'Avec antibiotiques (2C)'],
   ['Cancer associé ?', 'Coloscopie à 4-6 semaines', 'Après abcès traité sans chirurgie (2C)']])
 + P('<i>Lecture du tableau.</i> La biologie mesure l’inflammation, mais seule l’imagerie voit où est l’infection ; ainsi, le scanner décide du traitement, et la coloscopie, faite à distance, cherche un cancer que l’inflammation pourrait masquer.')
 + key('CRP → scanner (ou échographie experte) → drainage si gros abcès → coloscopie à distance si abcès.')
 + src(WSES))

C.e(2, 'Lire le scanner et l’endoscopie', P(
 'Le compte rendu de scanner doit répondre à quatre questions : y a-t-il des diverticules et une paroi épaissie ? du gaz extraluminal, et où ? un abcès, de quelle taille et dans quel siège ? du liquide ou de l’air libres en quantité ? Ainsi, il fournit directement le stade WSES. De plus, à distance de l’épisode, l’endoscopie montre les orifices diverticulaires et cherche une tumeur.')
 + C.img('k57_endo.gif', 'Image d’endoscopie colique : plusieurs orifices ronds et sombres dans la muqueuse, ouvertures des diverticules.', 'Diverticulose en coloscopie : orifices diverticulaires ronds et sombres ; la coloscopie se fait à distance de la poussée, jamais en pleine diverticulite.', credit({'auteur': 'Samir (The Scope)', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Diverticulosis_2.jpg'}))
 + P('<i>Lecture de l’image.</i> Chaque orifice sombre est l’entrée d’une poche ; or, en phase aiguë, insuffler de l’air dans un côlon inflammatoire risquerait d’aggraver une perforation couverte. C’est pourquoi l’endoscopie est différée de 4 à 6 semaines après un abcès.')
 + key('Scanner : diverticules, paroi, gaz, abcès (taille, siège), liquide libre → stade WSES ; endoscopie à distance.')
 + C.pareto('pareto-k57-examens', 'Examens', ['k57-e-1', 'k57-e-2'],
     ['CRP et leucocytes.',
      'Scanner injecté en premier.',
      'Stade WSES dans le compte rendu.',
      'Coloscopie à 4-6 semaines après abcès.'])
 + src(WSES))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : les points faibles de la paroi colique', P(
 'La musculeuse colique est traversée par les vaisseaux droits qui vont irriguer la muqueuse ; ainsi, chaque point de passage est une zone de moindre résistance. Lorsque la pression intraluminale s’élève, la muqueuse et la sous-muqueuse font hernie à travers ces orifices, formant un faux diverticule, sans musculeuse propre. Par conséquent, le vaisseau longe le dôme de la poche, ce qui explique à la fois l’hémorragie diverticulaire et la position des diverticules en rangées.')
 + key('Point de passage vasculaire = point faible → faux diverticule → hémorragie possible par le vaisseau voisin.', 'Science → clinique.'))
C.s('physio', 'Physiologie', 'Physiologie : pression et segmentation du sigmoïde', P(
 'Le sigmoïde, de petit calibre, se contracte par segments pour faire progresser des selles déshydratées ; ainsi, il peut générer de fortes pressions dans des segments fermés. Or, selon la loi de Laplace, la tension pariétale dépend du rayon : un petit calibre exige de plus fortes pressions pour un même effet. C’est pourquoi le sigmoïde est le siège le plus fréquent des diverticules en Occident.')
 + key('Petit calibre + segmentation → hautes pressions → hernies muqueuses au sigmoïde.', 'Science → topographie.'))
C.s('immuno', 'Immunologie', 'Immunologie : pourquoi l’immunodéprimé échoue', P(
 'La diverticulite simple est souvent contenue par la réponse inflammatoire locale, qui cloisonne l’infection dans la graisse péricolique ; ainsi, elle peut guérir sans antibiotique. En revanche, chez l’immunodéprimé, ce cloisonnement est défaillant et la réponse clinique est atténuée. Par conséquent, la maladie est découverte plus tard et plus souvent compliquée, d’où la règle de la WSES : haut risque d’échec, et chirurgie programmée à discuter.')
 + key('Défenses locales efficaces → abstention possible ; immunosuppression → formes graves et masquées.', 'Science → décision.'))
C.s('micro', 'Microbiologie', 'Microbiologie : une flore mixte', P(
 'La diverticulite infectieuse met en jeu la flore colique, aérobie et anaérobie ; ainsi, l’antibiothérapie empirique doit couvrir les deux. C’est pourquoi le CHUV choisit l’amoxicilline-acide clavulanique, ou associe la ciprofloxacine au métronidazole en cas d’allergie. De plus, la pipéracilline-tazobactam élargit le spectre dans les formes sévères ou en cas de risque de Pseudomonas.')
 + key('Flore mixte → spectre mixte ; escalade seulement si gravité ou risque de résistance.', 'Science → antibiothérapie.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, le premier choix est souvent de ne pas en donner.')
 + table(['Situation', 'Médicament', 'Source', 'Fenêtre'], [
   ['Forme simple, immunocompétent', 'Aucun antibiotique', 'WSES 1A, CHUV', w('k57-dva', 'Fiche')],
   ['Forme simple nécessitant un antibiotique, forme compliquée sans gravité', 'Amoxicilline-acide clavulanique', 'CHUV', w('k57-d-coamox', 'Monographie')],
   ['Allergie', 'Ciprofloxacine + métronidazole', 'CHUV', w('k57-d-cipro', 'Fiche')],
   ['Infection sévère, risque de Pseudomonas', 'Pipéracilline-tazobactam', 'CHUV', w('k57-d-pipt', 'Monographie')]])
 + P('<i>Lecture du tableau.</i> On monte d’une ligne seulement si l’état du patient l’exige ; ainsi, la pression de sélection sur les résistances reste minimale.')
 + key('Abstention si possible ; co-amoxicilline ; allergie : ciprofloxacine + métronidazole ; sévère : pipéracilline-tazobactam.')
 + src(WSES, CHUV))

C.p(2, 'Doses et statut réglementaire', P('Les doses suivantes proviennent du guide du CHUV et des informations professionnelles suisses ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Dose', 'Durée', 'Source'], [
   ['Amoxicilline-acide clavulanique', 'i.v. 1 200 à 2 200 mg toutes les 6-8 h ; per os 1 000 mg toutes les 8-12 h', '7 jours (diverticulite)', 'CHUV 2022'],
   ['Ciprofloxacine', 'i.v. 400 mg/12 h ; per os 500 mg/12 h ; 400 mg i.v. 3 ×/j dans les formes sévères', '7 jours', 'CHUV 2022'],
   ['Métronidazole', '500 mg toutes les 8 h, i.v. ou per os', '7 jours', 'CHUV 2022'],
   ['Pipéracilline-tazobactam', '4 500 mg toutes les 8 h ; toutes les 6 h en cas de choc ou de neutropénie', '7 jours', 'CHUV 2022']])
 + P('<i>Lecture du tableau.</i> Les doses varient selon la gravité ; ainsi, la co-amoxicilline intraveineuse passe de 1 200 mg à 2 200 mg dans les infections graves, ce que confirme l’information professionnelle suisse (1 200 mg 3-4 ×/j dans les infections modérées, 2 200 mg 3-4 ×/j dans les infections graves).')
 + trap('L’information professionnelle de la co-amoxicilline intraveineuse cite la péritonite mais pas la diverticulite : son usage dans la diverticulite non perforée suit donc le guide du CHUV. De plus, la perfusion de 2 200 mg est interdite si la clairance de la créatinine est < 30 ml/min. À valider à l’audit.', 'Point à valider')
 + key('Co-amoxicilline 1 000 mg per os /8-12 h ou 1 200-2 200 mg i.v. /6-8 h ; ciprofloxacine + métronidazole 500 mg/8 h ; pipéracilline-tazobactam 4 500 mg/8 h.')
 + src(CHUV, FI('Co-Amoxi-Mepha i.v.')))

C.p(3, 'Surveillance et effets indésirables', alert(
 'L’amoxicilline-acide clavulanique est contre-indiquée en cas d’hypersensibilité aux pénicillines ou aux céphalosporines et après un ictère ou une atteinte hépatique sous cette association (FI Augmentin®). De plus, le CHUV rappelle qu’une antibiothérapie prolongée sélectionne des souches résistantes et favorise les colites à Clostridioides difficile.', 'Sécurité.')
 + P('Par ailleurs, la surveillance est surtout clinique : la douleur, la fièvre et la CRP doivent diminuer en quelques jours ; en revanche, leur persistance fait chercher un abcès ou un foyer résiduel par un nouveau scanner. Enfin, le CHUV conseille d’éviter les AINS pendant la diverticulite.')
 + key('Allergie et antécédent hépatique sous co-amoxicilline ; durée courte ; pas d’AINS ; persistance du sepsis → nouvelle imagerie.')
 + C.pareto('pareto-k57-pharma', 'Pharmacologie', ['k57-p-1', 'k57-p-2', 'k57-p-3'],
     ['Pas d’antibiotique dans la forme simple de l’immunocompétent.',
      'Co-amoxicilline 7 jours si nécessaire.',
      'Sévère : pipéracilline-tazobactam 4 500 mg/8 h.',
      'Éviter les AINS.'])
 + src(FI('Augmentin®'), CHUV))

# ---------------- Fenêtres
L = lab
C.pop('k57-dva', 'Diverticulite aiguë', L(('Définition', 'Inflammation, souvent infectieuse, d’un ou de plusieurs diverticules.'), ('Non compliquée', 'Limitée au côlon ; souvent autolimitée chez l’immunocompétent.'), ('Compliquée', 'Infection au-delà du côlon : gaz, abcès, péritonite.')) + src(WSES))
C.pop('k57-dvose', 'Diverticulose', L(('Définition', 'Présence de diverticules, souvent asymptomatique.'), ('Mécanisme', 'Hernie de la muqueuse aux points de passage vasculaires de la musculeuse.'), ('Risque', 'Diverticulite chez ≈ 4 % des porteurs au cours de la vie.')) + C.img('k57_endo.gif', 'Coloscopie : orifices diverticulaires ronds et sombres.', 'Orifices diverticulaires en coloscopie.', credit({'auteur': 'Samir (The Scope)', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Diverticulosis_2.jpg'})) + src(WSES))
C.pop('k57-classif', 'Classification WSES de la diverticulite', L(('0', 'Diverticules, paroi épaissie, graisse densifiée.'), ('1a / 1b', 'Bulles de gaz localisées / abcès < 4 cm.'), ('2a / 2b', 'Abcès pelvien > 4 cm / abcès hors du pelvis.'), ('3 / 4', 'Péritonite purulente / stercorale (pneumopéritoine abondant, liquide libre).')) + C.img('k57_abces.gif', 'Scanner axial : sigmoïde épaissi avec petit abcès.', 'Exemple de stade 1b : petit abcès au contact du sigmoïde.', CT) + src(WSES))
C.pop('k57-tdm', 'Scanner abdominal injecté', L(('Place', 'Imagerie de premier choix (WSES 2B).'), ('Apport', 'VPP 0,95 et VPN 0,99 contre 0,65 et 0,98 pour la clinique seule.')) + src(WSES))
C.pop('k57-echo', 'Échographie', L(('Place', 'Évaluation initiale par un opérateur expert ; scanner si non concluante ou négative (2B).')) + src(WSES))
C.pop('k57-abces', 'Abcès diverticulaire', L(('< 4-5 cm', 'Antibiotiques seuls d’abord (2C).'), ('Plus gros', 'Drainage percutané + antibiotiques ; sinon antibiotiques seuls si l’état le permet, ou chirurgie.'), ('Ensuite', 'Coloscopie à 4-6 semaines.')) + src(WSES))
C.pop('k57-hartmann', 'Intervention de Hartmann', L(('Principe', 'Résection du sigmoïde, fermeture du moignon rectal et colostomie terminale.'), ('Indication', 'Péritonite diffuse chez le patient critique ou comorbide (WSES, forte).'), ('Alternative', 'Résection-anastomose ± stomie chez le patient stable.')) + src(WSES))
C.pop('k57-sigmo', 'Sigmoïdectomie programmée', L(('Décision', 'Selon les facteurs du patient, non selon le nombre d’épisodes (2D).'), ('Exemple', 'Immunodéprimé après un épisode traité médicalement.')) + src(WSES))
C.pop('k57-d-coamox', 'Amoxicilline-acide clavulanique', L(('Dose (CHUV)', 'i.v. 1 200-2 200 mg/6-8 h ; per os 1 000 mg/8-12 h.'), ('FI i.v.', '1 200 mg 3-4 ×/j (modérée), 2 200 mg 3-4 ×/j (grave) ; pas de 2 200 mg si ClCr < 30 ml/min.'), ('Contre-indications', 'Allergie aux pénicillines ou céphalosporines ; ictère antérieur sous co-amoxicilline.')) + src(CHUV, FI('Co-Amoxi-Mepha i.v.'), FI('Augmentin®')))
C.pop('k57-d-cipro', 'Ciprofloxacine + métronidazole', L(('Place', 'Allergie aux bêta-lactamines.'), ('Doses (CHUV)', 'Ciprofloxacine i.v. 400 mg/12 h ou per os 500 mg/12 h ; métronidazole 500 mg/8 h.')) + src(CHUV))
C.pop('k57-d-pipt', 'Pipéracilline-tazobactam', L(('Place', 'Infection sévère ou risque de Pseudomonas aeruginosa.'), ('Dose (CHUV)', '4 500 mg/8 h ; 4 500 mg/6 h si choc ou neutropénie.')) + src(CHUV))

C.termes = [
 (r'diverticulite aiguë', 'k57-dva'), (r'diverticulose', 'k57-dvose'), (r'classification WSES', 'k57-classif'), (r'scanner', 'k57-tdm'),
 (r'échographie', 'k57-echo'), (r'abcès', 'k57-abces'), (r'Hartmann', 'k57-hartmann'), (r'sigmoïdectomie', 'k57-sigmo'),
 (r'amoxicilline-acide clavulanique', 'k57-d-coamox'), (r'co-amoxicilline', 'k57-d-coamox'), (r'ciprofloxacine', 'k57-d-cipro'), (r'pipéracilline-tazobactam', 'k57-d-pipt'),
]

C.write()
