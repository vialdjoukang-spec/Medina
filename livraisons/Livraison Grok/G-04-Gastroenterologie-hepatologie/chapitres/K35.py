# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K35', 'Appendicite aiguë',
    'K35 — Appendicite aiguë · CIM-10-GM 2024 · Appendice',
    'Adulte (avec repères pour l’enfant et la grossesse) · appendicite aiguë non compliquée et compliquée (perforation, phlegmon, abcès, péritonite) · rédaction du 09.10.2026 · référentiels WSES Jérusalem 2020, guide d’antibiothérapie empirique du CHUV 2022, informations professionnelles suisses',
    'Pharmacologie de l’appendicite')
w = C.w
WSES = ('Di Saverio S. et al., Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines, World J Emerg Surg 2020;15:27', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7386163/')
CHUV = ('Service des maladies infectieuses et Pharmacie du CHUV, Guide d’antibiothérapie empirique chez l’adulte, version de mai 2022 (infections intra-abdominales, p. 22-23 ; posologies usuelles, p. 52)', 'https://www.chuv.ch/fileadmin/sites/min/552801_22_DM_DAM_guide_antibiotherapie_version_mai_2022.pdf')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 24 ans consulte aux urgences pour une douleur abdominale apparue depuis 18 heures, désormais localisée dans la fosse iliaque droite, avec des nausées et une fièvre à 38,1 °C. <b>La question est donc de savoir s’il a une ' + w('k35-aa', 'appendicite aiguë') + ', si elle est compliquée, et s’il faut l’opérer ou la traiter par antibiotiques.</b>',
 'Pour y répondre, le médecin doit savoir : calculer un ' + w('k35-scores', 'score clinique') + ' pour classer le risque ; choisir l’imagerie selon ce risque, en commençant par l’' + w('k35-echo', 'échographie') + ' ; distinguer l’' + w('k35-simple', 'appendicite non compliquée') + ' de l’' + w('k35-compliquee', 'appendicite compliquée') + ' ; ensuite, proposer une ' + w('k35-lap', 'appendicectomie laparoscopique') + ' dans les 24 heures ou discuter un ' + w('k35-nom', 'traitement antibiotique premier') + ' ; enfin, doser l’antibiothérapie au juste nécessaire.')
 + key('Douleur de la fosse iliaque droite, fièvre, nausées : score clinique → imagerie selon le risque → chirurgie ou antibiotiques.', 'Point de départ.'))

C.a(1, 'Définition et épidémiologie', P(
 'L’appendicite aiguë est l’inflammation aiguë de l’appendice vermiforme ; or, elle reste l’une des urgences chirurgicales abdominales les plus fréquentes. En effet, son incidence culmine entre 10 et 30 ans, et le risque de la présenter au cours de la vie est d’environ 8 % en Europe, contre 9 % aux États-Unis et 2 % en Afrique (WSES 2020).',
 'Par ailleurs, la gravité varie beaucoup. Ainsi, la perforation survient dans 16 à 40 % des cas, plus souvent chez les jeunes (40 à 57 %) et après 50 ans (55 à 70 %). De plus, la mortalité est inférieure à 0,1 % dans l’appendicite non gangréneuse, atteint 0,6 % dans la forme gangréneuse et environ 5 % en cas de perforation (WSES 2020). C’est pourquoi distinguer les formes simples des formes compliquées est l’enjeu central.')
 + key('Pic 10-30 ans ; risque vie entière ≈ 8 % en Europe ; perforation 16-40 % ; mortalité < 0,1 % (simple), 0,6 % (gangréneuse), ≈ 5 % (perforée).')
 + src(WSES))

C.a(2, 'Physiopathologie et formes évolutives', P(
 'L’obstruction de la lumière appendiculaire, par exemple par un ' + w('k35-stercolithe', 'stercolithe') + ', a longtemps été tenue pour le moteur unique de la maladie ; cependant, la WSES souligne que la perforation n’en est pas l’issue obligatoire. En effet, des données croissantes indiquent que toutes les appendicites n’évoluent pas vers la perforation, et que la résolution spontanée pourrait même être fréquente.',
 'Dès lors, on distingue deux formes. D’une part, l’appendicite non compliquée, inflammatoire, sans gangrène ni perforation. D’autre part, l’appendicite compliquée, avec gangrène, perforation, ' + w('k35-phlegmon', 'phlegmon') + ', abcès périappendiculaire ou péritonite. Par conséquent, la présence d’un stercolithe compte : elle augmente le risque d’échec du traitement antibiotique, si bien que la chirurgie est recommandée dans ce cas chez l’enfant (WSES 2020, énoncé 2.2).')
 + key('Simple ou compliquée (gangrène, perforation, phlegmon, abcès, péritonite) ; la perforation n’est pas inéluctable ; le stercolithe prédit l’échec des antibiotiques.')
 + src(WSES))

C.a(3, 'Présentation clinique et scores', P(
 'Le diagnostic clinique est difficile ; en effet, chaque signe isolé a une faible valeur, si bien que la WSES recommande une démarche individualisée selon la probabilité, le sexe et l’âge (recommandation 1.1). C’est pourquoi les scores cliniques sont au centre de la démarche. Ainsi, les scores d’Alvarado, ' + w('k35-air', 'AIR') + ' et ' + w('k35-aas', 'AAS') + ' sont assez sensibles pour exclure l’appendicite et identifier les patients à risque intermédiaire qui ont besoin d’une imagerie (recommandation 1.2.1).',
 'Cependant, ces scores n’ont pas la même valeur. En effet, le score d’' + w('k35-alvarado', 'Alvarado') + ' n’est pas assez spécifique pour confirmer le diagnostic chez l’adulte (recommandation 1.3, contre son usage dans ce but) ; en revanche, les scores AIR et AAS ont le meilleur pouvoir discriminant et sont recommandés (recommandation 1.4, forte). Par ailleurs, chez la femme enceinte, le diagnostic ne repose jamais sur les seuls symptômes : la biologie et la CRP sont toujours demandées (recommandation 1.2.2).')
 + quiz('Un homme de 24 ans a un score AIR de 10 et un score AAS de 17. Que dit la WSES 2020 de l’imagerie ?',
   [('Un scanner est obligatoire avant toute chirurgie', False), ('Le scanner peut être évité avant une laparoscopie, car le risque est élevé et l’âge inférieur à 40 ans', True), ('Le score d’Alvarado doit d’abord confirmer le diagnostic', False)],
   'Chez le patient à haut risque de moins de 40 ans (AIR 9-12, Alvarado 9-10, AAS ≥ 16), l’imagerie en coupes peut être évitée avant la laparoscopie diagnostique et thérapeutique (recommandation 1.9, faible).')
 + key('Scores pour stratifier : AIR et AAS recommandés ; Alvarado pour exclure, non pour confirmer ; grossesse : biologie et CRP toujours.')
 + src(WSES))

C.a(4, 'Démarche diagnostique et imagerie', P(
 'Une fois le risque estimé, l’imagerie suit cette classe. Ainsi, le patient à risque intermédiaire bénéficie d’une imagerie rapide et systématique (recommandation 1.8) ; en revanche, le patient à haut risque de moins de 40 ans peut aller en laparoscopie sans scanner préalable (recommandation 1.9). De plus, la combinaison des scores cliniques et de l’échographie améliore la sensibilité et la spécificité (recommandation 1.7, forte).',
 'Ensuite, le choix de la technique est précis. En effet, l’' + w('k35-echo', 'échographie au lit du patient') + ' est l’examen de première ligne chez l’adulte comme chez l’enfant (recommandation 1.10, forte). Si elle est négative chez l’adolescent ou l’adulte jeune, un ' + w('k35-tdm', 'scanner injecté à faible dose') + ' est préféré au scanner à dose standard (recommandation 1.11, forte). Enfin, chez la femme enceinte, l’échographie par compression graduée vient d’abord, puis l’IRM si elle n’est pas concluante (recommandations 1.13.1 et 1.13.2).')
 + C.img('k35_us.gif', 'Échographie de la fosse iliaque droite : structure tubulaire borgne, à paroi épaissie, de l’appendice vermiforme.', 'Échographie de l’appendice vermiforme : structure tubulaire borgne, non compressible lorsqu’elle est inflammatoire ; c’est l’examen de première ligne selon la WSES.', credit({'auteur': 'Nevit Dilmen', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Ultrasound_Scan_ND_0228090213_0912330.jpg'}))
 + C.img('k35_ct.gif', 'Scanner abdominopelvien injecté en coupe coronale : appendice à paroi épaissie, entouré d’une infiltration de la graisse.', 'Appendicite aiguë au scanner injecté (coupe coronale) : paroi appendiculaire épaissie et infiltration de la graisse périappendiculaire.', credit({'auteur': 'Goleisureintl', 'licence': 'CC BY 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Contrast-enhanced_CT_scan_(coronal)_of_abdomen_and_pelvis_showing_acute_appendicitis.jpg'}))
 + key('Risque intermédiaire : imagerie systématique ; échographie en premier ; scanner faible dose si échographie négative ; grossesse : échographie puis IRM.')
 + src(WSES))

C.a(5, 'Douleur persistante et imagerie négative', P(
 'Il reste le patient dont les examens sont normaux, mais dont la douleur de la fosse iliaque droite ne cède pas. Dans ce cas, la WSES recommande une imagerie en coupes avant toute chirurgie (recommandation 1.12) ; en effet, elle évite des appendicectomies inutiles. Ensuite, après une imagerie négative, une prise en charge non opératoire initiale est appropriée.',
 'Cependant, si la douleur progresse ou persiste, une laparoscopie exploratrice est recommandée pour établir ou exclure l’appendicite ou un autre diagnostic. De plus, si l’appendice paraît « normal » pendant l’intervention et qu’aucune autre cause n’est trouvée chez un patient symptomatique, son ablation est suggérée (recommandation 5.3), car le jugement macroscopique des formes débutantes est peu fiable.')
 + key('Douleur persistante, bilan normal : imagerie en coupes ; si négative, surveillance ; si douleur progressive, laparoscopie exploratrice.')
 + src(WSES))

C.a(6, 'Traitement de l’appendicite non compliquée', P(
 'Pour l’appendicite non compliquée, deux options existent. D’abord, l’appendicectomie laparoscopique est l’approche préférée à la voie ouverte, pour les formes simples comme compliquées, si l’équipement et l’expertise sont disponibles (recommandation 4.1, forte). De plus, elle est programmée sur le prochain programme opératoire disponible, dans les 24 heures (recommandation 3.1, forte), et ne doit pas être retardée au-delà de 24 heures après l’admission (recommandation 3.2, forte). Par ailleurs, une appendicectomie ambulatoire est suggérée si un parcours défini existe (recommandation 4.5).',
 'Ensuite, le traitement antibiotique premier est une alternative sûre chez des patients sélectionnés sans stercolithe, à condition de les informer du risque d’échec et d’une appendicite compliquée méconnue (recommandation 2.1.1, forte). En effet, la récidive atteint jusqu’à 39 % à 5 ans ; ainsi, dans l’essai APPAC, 27,3 % des patients traités par antibiotiques ont été opérés dans l’année. En revanche, ce traitement n’est pas suggéré pendant la grossesse (recommandation 2.1.2). Enfin, il commence par voie intraveineuse, avec un relais oral selon l’état clinique (recommandation 2.3, forte).')
 + trap('Un stercolithe visible à l’imagerie fait renoncer au traitement antibiotique premier : la WSES le réserve aux formes non compliquées sans stercolithe.', 'Piège')
 + key('Laparoscopie dans les 24 h (pas au-delà) ; ou antibiotiques premiers si non compliquée et sans stercolithe, avec information (récidive jusqu’à 39 % à 5 ans) ; pas pendant la grossesse.')
 + src(WSES))

C.a(7, 'Appendicite compliquée : phlegmon, abcès, péritonite', P(
 'L’appendicite compliquée change la stratégie. Ainsi, chez l’enfant, l’appendicectomie de la forme compliquée doit être faite dans les 8 heures (recommandation 3.3). De plus, en cas de phlegmon ou d’abcès, l’approche laparoscopique est le traitement de choix lorsque l’expertise avancée est disponible, avec un seuil de conversion bas (recommandation 6.2) ; en revanche, sans cette expertise, un traitement non opératoire par antibiotiques, avec drainage percutané si possible, est suggéré (recommandation 6.1).',
 'Après un traitement non opératoire, la récidive survient chez 12 à 24 % des patients. C’est pourquoi l’appendicectomie d’intervalle n’est pas recommandée en routine chez l’adulte jeune de moins de 40 ans et chez l’enfant ; elle l’est seulement en cas de symptômes récidivants (recommandation 6.3, forte). Cependant, après 40 ans, la fréquence des ' + w('k35-neo', 'tumeurs appendiculaires') + ' atteint 3 à 17 % dans les formes compliquées ; par conséquent, une coloscopie et un scanner injecté de contrôle sont suggérés (recommandation 6.4).')
 + C.img('k35_histo.gif', 'Coupe histologique d’appendice à faible grossissement : muqueuse ulcérée et infiltrat inflammatoire qui traverse toute l’épaisseur de la paroi.', 'Appendicite aiguë, coloration hématoxyline-éosine : ulcération muqueuse complète et inflammation transmurale ; l’examen histologique de la pièce est systématique.', credit({'auteur': 'CoRus13', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Acute_appendicitis,_low_mag.2.jpg'}))
 + key('Phlegmon ou abcès : laparoscopie si expertise, sinon antibiotiques ± drainage ; pas d’appendicectomie d’intervalle systématique avant 40 ans ; ≥ 40 ans : coloscopie + scanner.')
 + src(WSES))

C.a(8, 'Gestes opératoires et histologie', P(
 'Pendant l’intervention, plusieurs gestes sont précisés. Ainsi, la laparoscopie conventionnelle à trois trocarts est recommandée plutôt que la voie à incision unique (recommandation 4.3) ; de plus, l’aspiration seule est préférée au lavage péritonéal dans les formes compliquées (recommandation 4.8). En outre, le moignon est fermé par anses, ligature ou clips polymères (recommandation 4.10), et la ligature simple est préférée à l’enfouissement (recommandation 4.11, forte).',
 'Par ailleurs, le drainage après une appendicite compliquée n’est pas recommandé chez l’adulte (recommandation 4.12, forte), car il ne prévient pas les abcès et allonge le séjour. Ensuite, l’examen histologique de la pièce est systématique (recommandation 5.1, forte), afin de ne pas méconnaître une lésion inattendue. Enfin, un ' + w('k35-grade', 'système de grading peropératoire') + ', comme celui de la WSES 2015 ou de l’AAST, est suggéré (recommandation 5.2).')
 + key('Trois trocarts ; aspiration sans lavage ; ligature simple du moignon ; pas de drain chez l’adulte ; histologie systématique ; grading peropératoire.')
 + src(WSES))

C.a(9, 'Antibiothérapie périopératoire', P(
 'L’antibiothérapie suit la gravité. D’abord, une dose unique d’antibiotique à large spectre est administrée avant l’incision, de 0 à 60 minutes avant (énoncé 7.1) ; en revanche, aucun antibiotique postopératoire n’est recommandé dans l’appendicite non compliquée (recommandation 7.1, forte). Le guide du CHUV va dans le même sens : la prophylaxie peropératoire en dose unique suffit.',
 'Ensuite, dans l’appendicite compliquée, une antibiothérapie postopératoire est suggérée, surtout si le contrôle de la source est incomplet ; cependant, elle ne doit pas dépasser 3 à 5 jours après un contrôle adéquat (recommandation 7.2, forte). Ainsi, le CHUV propose l’' + w('k35-d-coamox', 'amoxicilline-acide clavulanique') + ' intraveineuse, ou la ' + w('k35-d-cipro', 'ciprofloxacine') + ' associée au ' + w('k35-d-metro', 'métronidazole') + ' en cas d’allergie, avec un arrêt possible après 3 jours si le contrôle chirurgical est optimal, l’apyrexie dure depuis au moins un jour, le transit a repris et l’inflammation diminue. Enfin, chez l’enfant, le relais oral est précoce, après 48 heures, pour une durée totale inférieure à 7 jours (recommandation 7.3).')
 + key('Dose unique préopératoire ; rien après une forme simple ; forme compliquée : 3-5 jours au plus (CHUV : arrêt possible à J3) ; amoxicilline-clavulanate ou ciprofloxacine + métronidazole.')
 + C.pareto('pareto-k35-clinique', 'Appendicite aiguë', ['k35-3', 'k35-4', 'k35-6', 'k35-7', 'k35-9'],
     ['Scores AIR et AAS pour stratifier.',
      'Échographie d’abord ; scanner faible dose ensuite.',
      'Laparoscopie dans les 24 h.',
      'Antibiotiques premiers : forme simple sans stercolithe.',
      'Abcès : laparoscopie ou antibiotiques ± drainage ; ≥ 40 ans : coloscopie.',
      'Dose unique ; 3-5 jours au plus si compliquée.'])
 + src(WSES, CHUV))

C.a(10, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons le patient du début. Son score AIR est de 10 et son score AAS de 17 : il est donc à haut risque, et comme il a moins de 40 ans, le scanner n’est pas indispensable. Ainsi, une échographie au lit montre un appendice épaissi et non compressible, sans stercolithe ni collection.',
 'Dès lors, deux options lui sont exposées. D’une part, l’appendicectomie laparoscopique dans les 24 heures, avec une dose unique préopératoire d’amoxicilline-acide clavulanique et sans antibiotique ensuite si la forme est simple. D’autre part, un traitement antibiotique premier, en l’informant d’un risque de récidive pouvant atteindre 39 % à 5 ans. Il choisit la chirurgie, et l’histologie confirme une appendicite aiguë non compliquée.')
 + key('Haut risque < 40 ans → échographie → laparoscopie < 24 h → dose unique → histologie.')
 + src(WSES, CHUV))

C.a(11, 'Critères formels et paramètres clés', alert(
 '<p><b>Haut risque (WSES 1.9).</b> AIR 9-12, Alvarado 9-10, AAS ≥ 16 : imagerie en coupes évitable avant 40 ans. <b>AAS.</b> ≥ 16 : forte probabilité ; < 11 : faible probabilité. <b>Appendicite compliquée.</b> Gangrène, perforation, phlegmon, abcès, péritonite. <b>Arrêt des antibiotiques (CHUV).</b> Contrôle optimal de la source, apyrexie ≥ 1 jour, reprise du transit, baisse de l’inflammation.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Risque vie entière ≈ 8 % (Europe) ; perforation 16-40 % ; chirurgie < 24 h ; enfant compliqué < 8 h ; récidive après antibiotiques jusqu’à 39 % à 5 ans ; récidive après phlegmon traité 12-24 % ; tumeurs 3-17 % après 40 ans ; antibiotiques postopératoires ≤ 3-5 jours.</div>'
 + src(WSES, CHUV))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Recommandation WSES 2020'], [
   ['Quel est le risque ?', w('k35-scores', 'Scores AIR ou AAS'), '1.4 (forte)'],
   ['Inflammation ?', 'Leucocytes, neutrophiles, CRP', 'Systématique chez l’enfant et la femme enceinte'],
   ['Première imagerie ?', w('k35-echo', 'Échographie au lit du patient'), '1.10 (forte)'],
   ['Échographie négative, adulte jeune ?', w('k35-tdm', 'Scanner injecté à faible dose'), '1.11 (forte)'],
   ['Grossesse, échographie non concluante ?', 'IRM', '1.13.2'],
   ['Après l’appendicectomie ?', 'Histologie de la pièce', '5.1 (forte)']])
 + P('Le tableau se lit de haut en bas : ainsi, le score décide de l’imagerie, et l’imagerie décide du traitement, jusqu’à l’histologie qui conclut.')
 + key('Score → biologie → échographie → scanner faible dose ou IRM → histologie.')
 + src(WSES))

C.e(2, 'Lire l’échographie et le scanner', P(
 'À l’échographie, l’appendice inflammatoire apparaît comme une structure tubulaire borgne, épaissie et non compressible ; de plus, un stercolithe ou une collection modifie la stratégie. Au scanner, la paroi est épaissie et la graisse voisine infiltrée ; or, l’absence de stercolithe, d’abcès et de perforation fait classer la forme comme non compliquée. Par conséquent, le compte rendu doit répondre à trois questions : appendicite ou non, stercolithe ou non, complication ou non.')
 + key('Compte rendu utile : appendicite ? stercolithe ? complication (abcès, perforation) ?')
 + C.pareto('pareto-k35-examens', 'Examens', ['k35-e-1', 'k35-e-2'],
     ['Score d’abord.',
      'Échographie en première ligne.',
      'Scanner faible dose si échographie négative.',
      'Stercolithe et complication à rechercher.',
      'Histologie systématique.'])
 + src(WSES))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : l’appendice et ses positions', P(
 'L’appendice vermiforme naît du cæcum, à la convergence des bandelettes coliques ; or, sa pointe peut occuper plusieurs positions, rétrocæcale, pelvienne ou sous-hépatique. Ainsi, une appendicite sous-hépatique ou pelvienne donne une douleur atypique. Par conséquent, les signes cliniques isolés ont une valeur faible, ce qui justifie les scores et l’imagerie.')
 + key('Position variable → présentation variable → scores et imagerie plutôt que signes isolés.', 'Science → diagnostic.'))
C.s('histo', 'Histologie', 'Histologie : de l’inflammation muqueuse à la transmuralité', P(
 'La paroi appendiculaire comprend une muqueuse riche en follicules lymphoïdes, une sous-muqueuse, une musculeuse et une séreuse ; ainsi, l’inflammation débute dans la muqueuse puis gagne toute la paroi. Lorsque l’infiltrat devient transmural et que la paroi se nécrose, la gangrène puis la perforation deviennent possibles. C’est pourquoi l’histologie confirme le diagnostic et peut révéler une tumeur inattendue.')
 + key('Muqueuse → transmuralité → gangrène → perforation ; histologie systématique.', 'Science → anatomopathologie.'))
C.s('micro', 'Microbiologie', 'Microbiologie : une flore mixte', P(
 'L’appendice contient une flore colique mixte, aérobie et anaérobie ; ainsi, l’infection périappendiculaire est polymicrobienne. Par conséquent, l’antibiothérapie empirique doit couvrir les deux types de germes, ce que fait l’amoxicilline-acide clavulanique ; en revanche, en cas d’allergie, le CHUV associe toujours la ciprofloxacine au métronidazole, qui apporte la couverture anaérobie (CHUV 2022).')
 + key('Flore aérobie et anaérobie → spectre mixte : amoxicilline-clavulanate, ou ciprofloxacine + métronidazole.', 'Science → antibiothérapie.'))
C.s('pharmaco', 'Pharmacologie fondamentale', 'Pharmacologie fondamentale : l’inhibiteur de bêta-lactamase', P(
 'L’amoxicilline est une aminopénicilline inactivée par les bêta-lactamases ; or, l’acide clavulanique inhibe ces enzymes. Ainsi, l’association est active sur les germes producteurs de bêta-lactamase, résistants à l’amoxicilline seule (FI Co-Amoxi-Mepha i.v.). De plus, la forme intraveineuse peut être relayée par la forme orale.')
 + key('Clavulanate = protection de l’amoxicilline contre les bêta-lactamases.', 'Science → choix du médicament.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Les principes posés, il reste à choisir les médicaments ; or, ils servent trois buts distincts : prophylaxie, traitement d’une forme compliquée et traitement antibiotique premier.')
 + table(['Classe', 'Exemple disponible en Suisse', 'Place', 'Fenêtre'], [
   ['Aminopénicilline + inhibiteur de bêta-lactamase', 'Amoxicilline-acide clavulanique (Co-Amoxi-Mepha i.v.®, Augmentin®)', '1er choix (CHUV)', w('k35-d-coamox', 'Monographie')],
   ['Fluoroquinolone', 'Ciprofloxacine', 'Allergie, avec métronidazole', w('k35-d-cipro', 'Fiche')],
   ['Nitro-imidazolé', 'Métronidazole', 'Couverture anaérobie, avec ciprofloxacine', w('k35-d-metro', 'Fiche')]])
 + P('Le tableau se lit par la colonne « Place » : ainsi, la ciprofloxacine n’est jamais utilisée seule : le CHUV l’associe au métronidazole pour couvrir les anaérobies.')
 + key('Amoxicilline-clavulanate d’abord ; si allergie : ciprofloxacine + métronidazole.')
 + src(CHUV))

C.p(2, 'Doses et statut réglementaire', P('Les doses suivantes proviennent du guide du CHUV et des informations professionnelles suisses ; de plus, les écarts sont signalés.')
 + table(['Médicament', 'Situation', 'Dose', 'Source'], [
   ['Amoxicilline-acide clavulanique i.v.', 'Prophylaxie de chirurgie abdominale', 'Dose unique à l’induction, répétée si intervention longue', 'FI Co-Amoxi-Mepha i.v.'],
   ['Amoxicilline-acide clavulanique i.v.', 'Infection modérée / grave', '1 200 mg 3-4 ×/j / 2 200 mg 3-4 ×/j (perfusion ≥ 30 min)', 'FI Co-Amoxi-Mepha i.v.'],
   ['Amoxicilline-acide clavulanique', 'Posologie usuelle CHUV', 'i.v. 1 200 à 2 200 mg toutes les 6-8 h ; per os 1 000 mg toutes les 8-12 h', 'CHUV 2022'],
   ['Ciprofloxacine', 'Allergie', 'i.v. 400 mg toutes les 12 h ; per os 500 mg toutes les 12 h', 'CHUV 2022'],
   ['Métronidazole', 'Avec ciprofloxacine', '500 mg toutes les 8 h, i.v. ou per os', 'CHUV 2022']])
 + P('Par exemple, chez le patient du début, une dose unique intraveineuse est donnée à l’induction ; ensuite, si la forme s’avère perforée, le traitement est poursuivi par voie intraveineuse puis orale, et arrêté au troisième jour si les critères du CHUV sont réunis.')
 + trap('L’information professionnelle de l’amoxicilline-acide clavulanique cite la péritonite et la prophylaxie en chirurgie abdominale, mais pas le traitement antibiotique premier de l’appendicite non compliquée : cet usage, recommandé par la WSES, sort donc du libellé explicite. De plus, la clairance de la créatinine < 30 ml/min interdit la perfusion de 2 200 mg. À valider à l’audit.', 'Point à valider')
 + key('Co-amoxicilline i.v. 1 200-2 200 mg toutes les 6-8 h ; ciprofloxacine 400 mg i.v./12 h + métronidazole 500 mg/8 h ; dose unique en prophylaxie.')
 + src(FI('Co-Amoxi-Mepha i.v.'), CHUV, WSES))

C.p(3, 'Surveillance et effets indésirables', alert(
 'L’amoxicilline-acide clavulanique est contre-indiquée en cas d’hypersensibilité connue aux pénicillines ou aux céphalosporines, et après un ictère ou une atteinte hépatique survenus lors d’un traitement antérieur par cette association (FI Augmentin®). C’est pourquoi l’allergie est recherchée avant la première dose.', 'Sécurité.')
 + P('Par ailleurs, la durée courte est elle-même une mesure de sécurité. En effet, le CHUV rappelle qu’une antibiothérapie prolongée favorise la sélection de souches résistantes et les colites à Clostridioides difficile, ainsi que les effets indésirables et les coûts ; ainsi, l’arrêt au troisième jour est envisagé dès que les critères sont remplis.')
 + key('Allergie aux bêta-lactamines et antécédent hépatique sous co-amoxicilline : contre-indications ; durée courte pour limiter résistances et C. difficile.')
 + C.pareto('pareto-k35-pharma', 'Pharmacologie', ['k35-p-1', 'k35-p-2', 'k35-p-3'],
     ['Dose unique préopératoire.',
      'Co-amoxicilline i.v. en premier choix.',
      'Allergie : ciprofloxacine + métronidazole.',
      'Arrêt à J3 si critères réunis.'])
 + src(FI('Augmentin®'), CHUV))

# ---------------- Fenêtres
L = lab
C.pop('k35-aa', 'Appendicite aiguë', L(('Définition', 'Inflammation aiguë de l’appendice vermiforme.'), ('Épidémiologie', 'Pic 10-30 ans ; risque vie entière ≈ 8 % en Europe.')) + src(WSES))
C.pop('k35-simple', 'Appendicite non compliquée', L(('Définition', 'Inflammation sans gangrène, perforation, phlegmon, abcès ni péritonite.'), ('Options', 'Laparoscopie < 24 h ou antibiotiques premiers si pas de stercolithe.')) + src(WSES))
C.pop('k35-compliquee', 'Appendicite compliquée', L(('Définition', 'Gangrène, perforation, phlegmon, abcès périappendiculaire ou péritonite.'), ('Mortalité', '≈ 5 % en cas de perforation.')) + src(WSES))
C.pop('k35-scores', 'Scores cliniques de l’appendicite', L(('Recommandés', 'AIR et AAS (recommandation 1.4, forte).'), ('Alvarado', 'Utile pour exclure ; ne pas l’utiliser pour confirmer chez l’adulte (1.3).'), ('Haut risque', 'AIR 9-12, Alvarado 9-10, AAS ≥ 16.')) + src(WSES))
C.pop('k35-air', 'Score AIR', L(('Nom', 'Appendicitis Inflammatory Response score (Andersson, 2008).'), ('Haut risque', '9-12.'), ('Place', 'Score recommandé, avec l’AAS (1.4).')) + src(WSES))
C.pop('k35-aas', 'Score AAS', L(('Nom', 'Adult Appendicitis Score.'), ('Seuils', '≥ 16 : forte probabilité (spécificité 93 % dans l’étude citée) ; < 11 : faible probabilité.')) + src(WSES))
C.pop('k35-alvarado', 'Score d’Alvarado', L(('Haut risque', '9-10.'), ('Limite', 'Pas assez spécifique pour confirmer chez l’adulte (recommandation 1.3).')) + src(WSES))
C.pop('k35-echo', 'Échographie au lit du patient', L(('Place', 'Première ligne chez l’adulte et l’enfant si une imagerie est indiquée (1.10, forte).'), ('Grossesse', 'Échographie par compression graduée en premier (1.13.1).')) + src(WSES))
C.pop('k35-tdm', 'Scanner injecté à faible dose', L(('Place', 'Adolescent et adulte jeune avec échographie négative (1.11, forte).'), ('Avant 40 ans à haut risque', 'Peut être évité avant la laparoscopie (1.9).')) + src(WSES))
C.pop('k35-lap', 'Appendicectomie laparoscopique', L(('Place', 'Approche préférée pour les formes simples et compliquées (4.1, forte).'), ('Délai', 'Dans les 24 h, pas au-delà (3.1, 3.2).'), ('Technique', 'Trois trocarts ; ligature simple du moignon ; pas de drain chez l’adulte.')) + src(WSES))
C.pop('k35-nom', 'Traitement antibiotique premier', L(('Indication', 'Appendicite non compliquée sans stercolithe, patient sélectionné et informé (2.1.1, forte).'), ('Risque', 'Récidive jusqu’à 39 % à 5 ans ; APPAC : 27,3 % opérés dans l’année.'), ('Contre', 'Grossesse (2.1.2).')) + src(WSES))
C.pop('k35-stercolithe', 'Stercolithe (appendicolithe)', L(('Définition', 'Concrétion fécale calcifiée dans la lumière appendiculaire.'), ('Portée', 'Augmente l’échec des antibiotiques ; chirurgie recommandée chez l’enfant dans ce cas.')) + src(WSES))
C.pop('k35-phlegmon', 'Phlegmon appendiculaire', L(('Définition', 'Masse inflammatoire périappendiculaire sans collection drainable.'), ('Traitement', 'Laparoscopie si expertise ; sinon antibiotiques (6.1, 6.2).')) + src(WSES))
C.pop('k35-neo', 'Tumeurs appendiculaires', L(('Fréquence', '3-17 % chez l’adulte ≥ 40 ans avec appendicite compliquée.'), ('Conduite', 'Coloscopie et scanner injecté d’intervalle après traitement non opératoire (6.4).')) + src(WSES))
C.pop('k35-grade', 'Grading peropératoire', L(('Exemples', 'Score WSES 2015 ou score AAST de chirurgie générale d’urgence.'), ('Intérêt', 'Corrèle mieux que l’histologie avec la morbidité ; guide la suite (5.2).')) + src(WSES))
C.pop('k35-d-coamox', 'Amoxicilline-acide clavulanique', L(('Indications suisses (i.v.)', 'Notamment péritonite et prophylaxie en chirurgie abdominale.'), ('Doses (FI)', '1 200 mg 3-4 ×/j (modérée) ; 2 200 mg 3-4 ×/j (grave) ; prophylaxie : dose unique à l’induction.'), ('Contre-indications', 'Allergie aux pénicillines ou céphalosporines ; ictère antérieur sous co-amoxicilline.')) + src(FI('Co-Amoxi-Mepha i.v.'), FI('Augmentin®')))
C.pop('k35-d-cipro', 'Ciprofloxacine', L(('Place', 'Allergie aux bêta-lactamines, toujours avec le métronidazole.'), ('Dose (CHUV)', 'i.v. 400 mg/12 h ; per os 500 mg/12 h.')) + src(CHUV))
C.pop('k35-d-metro', 'Métronidazole', L(('Rôle', 'Couverture des anaérobies.'), ('Dose (CHUV)', '500 mg toutes les 8 h, i.v. ou per os.')) + src(CHUV))

C.termes = [
 (r'appendicite aiguë', 'k35-aa'), (r'non compliquée', 'k35-simple'), (r'compliquée', 'k35-compliquee'), (r'AIR', 'k35-air'), (r'AAS', 'k35-aas'),
 (r'Alvarado', 'k35-alvarado'), (r'échographie', 'k35-echo'), (r'scanner', 'k35-tdm'), (r'laparoscopi', 'k35-lap'), (r'stercolithe', 'k35-stercolithe'),
 (r'phlegmon', 'k35-phlegmon'), (r'antibiotique premier', 'k35-nom'), (r'amoxicilline-acide clavulanique', 'k35-d-coamox'), (r'ciprofloxacine', 'k35-d-cipro'),
 (r'métronidazole', 'k35-d-metro'), (r'grading', 'k35-grade'), (r'tumeurs appendiculaires', 'k35-neo'),
]

C.write()
