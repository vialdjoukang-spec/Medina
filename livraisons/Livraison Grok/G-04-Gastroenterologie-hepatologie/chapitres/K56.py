# RAPPEL VERITE : vraies images uniquement · doses exactes (sources suisses/europeennes verifiees) · codes CIM-10-GM verifies · connecteurs logiques · termes et fenetres interactifs · aucune invention.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medina_gen import *
from images import credit

C = Chapter('K56', 'Iléus paralytique et occlusion intestinale sans hernie',
    'K56 — Iléus paralytique et occlusion intestinale sans hernie · CIM-10-GM 2024 · Côlon et intestin grêle',
    'Adulte · occlusion du grêle sur brides, occlusion colique (cancer, volvulus du sigmoïde), iléus paralytique, invagination et iléus biliaire signalés · rédaction du 09.10.2026 · référentiels WSES Bologne 2017 (occlusion sur brides), WSES 2023 (volvulus du sigmoïde), WSES 2017 (urgences du cancer colorectal), information professionnelle suisse',
    'Pharmacologie de l’occlusion')
w = C.w
BOL = ('ten Broek R.P.G. et al., Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update of the evidence-based guidelines from the WSES ASBO working group, World J Emerg Surg 2018;13:24', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6006983/')
SV = ('Tian B.W.C.A. et al., WSES consensus guidelines on sigmoid volvulus management, World J Emerg Surg 2023;18:34', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10186802/')
CRC = ('Pisano M. et al., 2017 WSES guidelines on colon and rectal cancer emergencies: obstruction and perforation, World J Emerg Surg 2018;13:36', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6090779/')
FI = lambda n: ('Information professionnelle suisse ' + n + ', Swissmedic (AIPS), consultée le 09.10.2026', 'https://www.swissmedicinfo.ch/')
TDM = credit({'auteur': 'Hellerhoff', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Bridenileus_mit_Hungerdarm_75M_-_CT_axial_und_coronar_KM_pv_-_001_-_Annotation.jpg'})
ASP = credit({'auteur': 'James Heilman, MD', 'licence': 'CC BY-SA 3.0', 'url': 'https://commons.wikimedia.org/wiki/File:Upright_X-ray_demonstrating_small_bowel_obstruction.jpg'})
VOL = credit({'auteur': 'Mont4nha', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Sigmoidvolvulus.jpg'})
INV = credit({'auteur': 'Cerevisae', 'licence': 'CC BY-SA 4.0', 'url': 'https://commons.wikimedia.org/wiki/File:Ultrasound_of_target_sign_in_intussusception_of_the_right_bowel.png'})

C.a(0, 'Question clinique et objectifs', P(
 'Un homme de 75 ans, opéré du côlon il y a huit ans, consulte pour des douleurs abdominales en coliques depuis la veille, des vomissements, un ballonnement et l’absence de gaz. <b>La question est donc double : s’agit-il d’une ' + w('k56-osb', 'occlusion du grêle sur brides') + ', et faut-il opérer tout de suite ou tenter d’abord un traitement non opératoire ?</b>',
 'Pour y répondre, le médecin doit savoir : reconnaître le tableau occlusif et ses pièges ; chercher les signes qui imposent la chirurgie (' + w('k56-strang', 'strangulation') + ', ischémie, péritonite) ; demander le bon examen, c’est-à-dire le ' + w('k56-tdm', 'scanner') + ' avec ' + w('k56-hydro', 'produit de contraste hydrosoluble') + ' ; ensuite, conduire le traitement non opératoire et savoir quand il échoue ; enfin, distinguer l’occlusion colique, le volvulus et l’iléus paralytique, qui ne se traitent pas de la même façon.')
 + P('<i>Pourquoi ce cas ?</i> En effet, l’occlusion sur brides est l’urgence chirurgicale type : le retard diagnostique y représente 70 % des plaintes pour faute médicale selon la WSES. Ainsi, contrairement à un manuel figé qui juxtapose les causes, ce cours suit le raisonnement au lit du malade : chaque mot vert ouvre le critère, le seuil ou l’image correspondante, si bien que la décision peut être refaite pas à pas.')
 + key('Coliques + vomissements + ballonnement + arrêt du transit chez un opéré : penser brides → chercher les signes de gravité → scanner → traitement non opératoire si aucun signe d’alarme.', 'Point de départ.'))

C.a(1, 'Définitions et épidémiologie', P(
 'L’' + w('k56-occl', 'occlusion intestinale') + ' est un obstacle au passage du contenu digestif ; elle se traduit par une douleur abdominale, des vomissements, une distension et un arrêt des matières et des gaz (WSES Bologne 2017). Or, l’obstacle peut être mécanique (bride, tumeur, volvulus, invagination, calcul) ou fonctionnel : on parle alors d’' + w('k56-ileus', 'iléus paralytique') + ', où l’intestin est perméable mais immobile.',
 'De plus, les adhérences postopératoires sont la première cause d’occlusion du grêle : elles en expliquent environ 60 %. Ainsi, au Royaume-Uni, l’occlusion du grêle motivait 51 % des laparotomies en urgence ; par ailleurs, chaque épisode d’occlusion sur brides entraîne en moyenne 8 jours d’hospitalisation et une mortalité hospitalière de 3 % (WSES Bologne 2017). Enfin, la récidive est fréquente : 12 % des patients traités sans chirurgie sont réhospitalisés dans l’année, et 20 % à 5 ans, contre 8 % et 16 % après traitement chirurgical.')
 + table(['Mécanisme', 'Exemples'], [
   ['Fonctionnel (pas d’obstacle)', 'Iléus paralytique'],
   ['Télescopage d’un segment', w('k56-invag', 'Invagination')],
   ['Torsion sur l’axe du méso', w('k56-volv', 'Volvulus') + ', par exemple du sigmoïde'],
   ['Calcul biliaire migré dans le grêle', 'Iléus biliaire'],
   ['Adhérences après chirurgie', 'Brides avec occlusion'],
   ['Autres obstacles', 'Tumeur, bézoard, maladie inflammatoire']])
 + P('<i>Lecture du tableau.</i> Chaque ligne correspond à un mécanisme physique différent ; or, c’est le mécanisme, et non le symptôme, qui commande le traitement. En effet, une bride simple peut céder avec le repos digestif, alors qu’une torsion ou une anse fermée étrangle le mésentère et impose un geste rapide. C’est pourquoi l’enjeu du bilan est d’identifier le mécanisme, puis de chercher la souffrance de l’intestin.')
 + key('Occlusion = obstacle mécanique ou iléus fonctionnel ; brides ≈ 60 % des occlusions du grêle ; 8 jours d’hospitalisation, 3 % de mortalité par épisode ; récidive 12 % à 1 an, 20 % à 5 ans sans chirurgie.')
 + src(BOL))

C.a(2, 'Physiopathologie : de la distension à l’ischémie', P(
 'En amont de l’obstacle, le gaz avalé et les sécrétions digestives s’accumulent ; ainsi, les anses se distendent, alors que l’intestin d’aval se vide et devient plat, c’est le « grêle de famine ». Ensuite, la distension élève la pression dans la paroi et gêne d’abord le retour veineux ; par conséquent, la paroi s’œdématie, le liquide passe dans la lumière et dans le péritoine, et le patient se déshydrate. De plus, les vomissements font perdre de l’eau, du sodium, du chlore et du potassium ; c’est pourquoi l’hypokaliémie et l’insuffisance rénale aiguë fonctionnelle sont fréquentes, comme le souligne la WSES.',
 'Cependant, le danger principal est vasculaire. En effet, dans une ' + w('k56-anse', 'anse fermée') + ', occluse à ses deux extrémités, ou dans une torsion, le mésentère est comprimé : la circulation artérielle s’arrête, la paroi devient ischémique, puis nécrotique, et elle finit par se perforer. Dès lors, une occlusion « simple » peut devenir une occlusion « étranglée » en quelques heures, d’où la règle de la WSES : chercher d’emblée les signes de strangulation, d’ischémie et de péritonite, qui contre-indiquent le traitement non opératoire.')
 + C.img('k56_bride_tdm.gif', 'Scanner abdominal injecté, coupes axiale et coronale annotées : anses grêles très dilatées en haut, changement brutal de calibre, puis anses grêles vides en aval.', 'Occlusion du grêle sur bride au scanner (homme de 75 ans) : anses dilatées en amont, changement brutal de calibre au niveau de la bride, puis « grêle de famine » vide en aval.', TDM)
 + P('<i>Lecture de l’image.</i> Le contraste entre les anses pleines et les anses vides localise l’obstacle : c’est le changement de calibre. Or, la bride elle-même n’est presque jamais visible, même au scanner, comme le rappelle la WSES ; c’est pourquoi on la déduit de ce changement de calibre et de l’absence d’autre cause (tumeur, hernie, volvulus). En outre, le radiologue cherche dans la même série les signes de souffrance : paroi mal rehaussée, anse fermée, liquide libre.')
 + key('Distension d’amont → œdème pariétal et pertes hydroélectrolytiques → si anse fermée ou torsion : ischémie → nécrose → perforation ; la bride se déduit du changement de calibre.')
 + src(BOL))

C.a(3, 'Présentation clinique et pièges', P(
 'Classiquement, l’occlusion sur brides associe des douleurs abdominales intermittentes en coliques, une distension et des nausées, avec ou sans vomissements, et avec ou sans arrêt des selles (WSES Bologne 2017). Ainsi, l’anamnèse recherche les causes possibles : opérations antérieures, radiothérapie ; de plus, elle évalue l’état nutritionnel et les signes de déshydratation.',
 'Cependant, la WSES décrit des pièges qui retardent le diagnostic. En effet, une occlusion incomplète peut donner une diarrhée aqueuse, faussement rassurante, qui fait croire à une gastroentérite ; de même, des selles peuvent persister si l’obstacle est haut et le patient vu tôt. Par ailleurs, chez le sujet âgé, la douleur est souvent moins marquée. Enfin, l’examen recherche une péritonite et une hernie de la paroi ou de l’aine ; toutefois, sa sensibilité pour détecter une strangulation n’est que de 48 %, même chez un clinicien expérimenté.')
 + trap('Une diarrhée n’exclut pas une occlusion : l’obstacle incomplet laisse passer du liquide. De même, un ventre peu douloureux chez une personne âgée n’exclut pas une strangulation, puisque l’examen n’en détecte qu’environ la moitié.', 'Piège')
 + quiz('Chez un patient occlus, l’examen clinique ne montre ni défense ni contracture. Que peut-on en conclure sur la strangulation ?',
   [('Elle est exclue', False), ('Elle n’est pas exclue : la sensibilité de l’examen n’est que de 48 %', True), ('Elle est exclue si le patient a encore des selles', False)],
   'Selon la WSES, l’examen clinique ne détecte la strangulation qu’une fois sur deux ; c’est pourquoi le scanner est demandé dès qu’un doute existe.')
 + key('Coliques + distension + nausées ± vomissements ± arrêt des selles ; pièges : diarrhée de l’occlusion incomplète, selles de l’obstacle haut, sujet âgé peu douloureux ; examen : sensibilité 48 % pour la strangulation ; toujours examiner les orifices herniaires.')
 + src(BOL))

C.a(4, 'Biologie et imagerie', P(
 'Le bilan biologique minimal comprend une formule sanguine, le ' + w('k56-lact', 'lactate') + ', les électrolytes, la CRP, l’urée et la créatinine. Ainsi, une CRP supérieure à 75 et des leucocytes au-delà de 10 000/mm³ peuvent évoquer une péritonite, même si leur sensibilité et leur spécificité restent faibles ; de plus, le potassium est souvent bas et doit être corrigé (WSES Bologne 2017).',
 'Ensuite, l’imagerie oriente la décision. Or, la ' + w('k56-asp', 'radiographie de l’abdomen') + ' a une valeur limitée (sensibilité d’environ 70 %) et ne renseigne ni sur la cause ni sur la strangulation ; c’est pourquoi la WSES ne la recommande pas (IIC). En revanche, le scanner prédit la strangulation et le besoin de chirurgie urgente avec une exactitude d’environ 90 % ; il est donc l’examen de choix en cas de doute sur la cause ou de signe pouvant imposer la chirurgie. Par ailleurs, l’échographie et l’IRM servent dans des situations particulières, comme la grossesse.')
 + C.img('k56_asp.gif', 'Radiographie de l’abdomen debout : nombreux niveaux hydroaériques horizontaux dans des anses grêles dilatées.', 'Occlusion du grêle sur radiographie debout : multiples niveaux hydroaériques dans des anses grêles distendues.', ASP)
 + P('<i>Lecture de l’image.</i> Debout, le gaz monte et le liquide stagne au fond des anses ; ainsi, chaque anse distendue dessine un niveau horizontal. Cependant, cette image confirme seulement qu’il y a une occlusion : elle ne dit ni pourquoi, ni si l’intestin souffre. C’est précisément pourquoi le scanner l’a remplacée dans la décision.')
 + key('Biologie : formule, lactate, électrolytes, CRP, urée et créatinine ; corriger le potassium ; radiographie peu utile (non recommandée) ; scanner ≈ 90 % d’exactitude pour la strangulation et l’indication chirurgicale.')
 + src(BOL))

C.a(5, 'Signes qui imposent la chirurgie', P(
 'La première décision est donc de savoir si l’intestin souffre. Ainsi, selon la WSES, les contre-indications au traitement non opératoire sont la péritonite, la strangulation et l’ischémie ; de plus, au scanner, une anse fermée, des signes d’ischémie et du liquide libre font opérer sans délai.',
 'Par ailleurs, des scores aident à prédire le besoin de chirurgie. En effet, le score de ' + w('k56-zielinski', 'Zielinski') + ' associe trois signes, l’œdème du mésentère, l’absence de signe des fèces dans le grêle et l’arrêt complet des matières et des gaz ; il prédisait le recours à la chirurgie avec un indice de concordance de 0,77 sur 100 cas. De même, un modèle plus complexe, combinant imagerie, critères de sepsis et comorbidités, atteignait une aire sous la courbe de 0,80 sur 351 cas (WSES Bologne 2017). Toutefois, ces scores complètent le jugement clinique et ne le remplacent pas.')
 + alert('Péritonite, strangulation, ischémie (clinique ou scanner : anse fermée, paroi non rehaussée, liquide libre) : pas de traitement non opératoire, exploration chirurgicale sans délai. De plus, un lactate élevé fait craindre une ischémie.', 'Gravité d’abord.')
 + key('Contre-indications au traitement non opératoire : péritonite, strangulation, ischémie ; au scanner : anse fermée, ischémie, liquide libre ; score de Zielinski (œdème mésentérique, pas de signe des fèces, arrêt complet) : indice 0,77.')
 + src(BOL))

C.a(6, 'Traitement non opératoire de l’occlusion sur brides', P(
 'En l’absence de ces signes, le traitement non opératoire est la stratégie de choix (WSES IIC) ; en effet, il réussit chez environ 70 à 90 % des patients. Ainsi, il repose sur la mise à jeun, la ' + w('k56-sng', 'décompression par sonde nasogastrique') + ' ou par sonde intestinale longue, la réhydratation intraveineuse, la correction des électrolytes, le soutien nutritionnel et la prévention de l’inhalation.',
 'De plus, le produit de contraste hydrosoluble est à la fois un test et peut-être un traitement. En effet, on l’administre par la sonde, puis on fait une radiographie à 24 heures : si le contraste a atteint le côlon, l’occlusion se lève ; s’il ne l’a pas atteint, l’échec du traitement non opératoire est très probable (WSES IB). Par ailleurs, plusieurs études montrent qu’il prédit bien le besoin de chirurgie et raccourcit l’hospitalisation ; certains auteurs lui prêtent même un effet thérapeutique. Enfin, la durée du traitement non opératoire n’est pas fixée par des preuves solides, mais la WSES considère une période de 72 heures comme sûre (IIB) ; en revanche, prolonger au-delà de 72 heures, en cas de débit élevé de la sonde sans autre signe d’aggravation, reste débattu.')
 + trap('Retarder la chirurgie augmente la morbidité et la mortalité : le traitement non opératoire est un essai encadré, avec réévaluations répétées, contraste à 24 heures et limite de 72 heures, et non une attente indéfinie. De plus, chez le diabétique, une intervention plus précoce pourrait être nécessaire (WSES, niveau C).', 'Piège')
 + key('À jeun + sonde de décompression + réhydratation + électrolytes + nutrition ; contraste hydrosoluble puis radiographie à 24 h (côlon atteint = levée) ; succès 70-90 % ; durée sûre ≈ 72 h.')
 + src(BOL))

C.a(7, 'Traitement chirurgical et prévention des récidives', P(
 'Quand le traitement non opératoire échoue, ou d’emblée en cas de signe de gravité, le chirurgien libère les brides : c’est l’' + w('k56-adhesio', 'adhésiolyse') + '. Ainsi, historiquement par laparotomie, elle se fait de plus en plus par laparoscopie ; en effet, celle-ci pourrait réduire la morbidité chez des patients sélectionnés (WSES IIC). Cependant, des anses très dilatées et des adhérences multiples exposent à des plaies intestinales, rapportées chez 6,3 à 26,9 % des patients opérés par laparoscopie ; c’est pourquoi la sélection est essentielle.',
 'Par ailleurs, la WSES cite les éléments prédictifs d’une laparoscopie réussie : au plus deux laparotomies antérieures, une appendicectomie comme seule opération antérieure, pas d’incision médiane et une bride unique. Enfin, la prévention vise les opérations futures : la chirurgie mini-invasive et les barrières anti-adhérences réduisent les adhérences, et le hyaluronate-carboxyméthylcellulose diminue les réopérations pour occlusion après chirurgie colorectale (RR 0,49 ; WSES IA). De plus, les sujets jeunes, dont le risque cumulé est le plus long, en tirent le plus grand bénéfice.')
 + key('Échec ou gravité : adhésiolyse ; laparoscopie chez des patients sélectionnés (≤ 2 laparotomies, pas d’incision médiane, bride unique) ; plaies intestinales 6,3-26,9 % ; prévention : mini-invasif et barrières anti-adhérences.')
 + src(BOL))

C.a(8, 'Occlusion colique et volvulus du sigmoïde', P(
 'L’occlusion du côlon pose d’autres questions. En effet, chez l’adulte, sa cause est souvent un cancer colorectal, et le scanner est la meilleure technique pour évaluer l’occlusion et la perforation du gros intestin (WSES 2017). Ainsi, pour le cancer du côlon gauche occlusif, la résection avec anastomose d’emblée est préférable à l’intervention de Hartmann si le patient et le chirurgien le permettent ; de plus, la ' + w('k56-sems', 'prothèse colique métallique') + ' posée en pont vers une chirurgie programmée donne de meilleurs résultats à court terme et moins de stomies, mais elle n’est pas le traitement de choix en raison d’incertitudes oncologiques (risque de perforation jusqu’à 13 %).',
 'Par ailleurs, le volvulus du sigmoïde est une torsion du côlon sigmoïde autour de son méso. Ainsi, selon la WSES 2023, le bilan initial associe examen clinique, gaz du sang et lactate, à la recherche d’une ischémie (1C) ; ensuite, la radiographie de l’abdomen montre classiquement le ' + w('k56-grain', 'signe du grain de café') + ' (1C), et le scanner sert en cas de doute ou de suspicion d’ischémie ou de perforation (1C). Enfin, sans ischémie ni perforation, la détorsion par endoscopie souple est le premier geste (1C) ; elle est suivie d’une sigmoïdectomie, si possible pendant la même hospitalisation, pour éviter la récidive (1C). En revanche, l’échec de la détorsion, un côlon non viable ou perforé imposent la résection urgente (1C).')
 + C.img('k56_volvulus.gif', 'Radiographie de l’abdomen d’un enfant : énorme anse colique distendue en forme de U inversé, occupant l’abdomen.', 'Volvulus du sigmoïde sur radiographie de l’abdomen (enfant de 10 ans) : anse sigmoïde géante distendue, en « grain de café ».', VOL)
 + P('<i>Lecture de l’image.</i> L’anse tordue est fermée à ses deux pieds ; ainsi, elle se remplit de gaz sans pouvoir se vider, et ses deux jambages accolés dessinent le sillon du grain de café. Or, c’est une anse fermée par définition : la torsion du méso comprime aussi ses vaisseaux, d’où le risque d’ischémie qui justifie le lactate et, au moindre doute, le scanner. Par ailleurs, ce cliché provient d’un enfant ; chez l’adulte, la WSES 2023 décrit le même signe.')
 + key('Occlusion colique : scanner ; cancer gauche : résection-anastomose si possible, prothèse en pont dans des cas choisis ; volvulus du sigmoïde : lactate, grain de café, détorsion endoscopique puis sigmoïdectomie ; ischémie ou échec : résection urgente.')
 + src(CRC, SV))

C.a(9, 'Iléus paralytique, invagination et iléus biliaire', P(
 'À côté des obstacles mécaniques, l’iléus paralytique (K56.0) est un arrêt du péristaltisme sans obstacle ; ainsi, le grêle et le côlon sont distendus de façon diffuse, sans changement de calibre. Il survient typiquement après une chirurgie abdominale ou par réflexe au cours d’une inflammation abdominale ou de troubles électrolytiques ; par conséquent, son traitement vise la cause, et l’on corrige notamment le potassium. Toutefois, aucune recommandation dédiée à l’iléus postopératoire n’a été lue pour ce cours : ses critères et son traitement spécifique restent à compléter (TODO).',
 'Par ailleurs, l’invagination est le télescopage d’un segment intestinal dans le segment voisin ; ainsi, l’échographie montre une image en cible, faite des couches concentriques des deux segments emboîtés. De plus, l’iléus biliaire est l’occlusion du grêle par un gros calcul passé de la vésicule dans l’intestin ; il est rattaché au cours K80. Enfin, la prise en charge spécifique de ces deux causes, en particulier chez l’enfant, n’est pas traitée ici faute de recommandation lue (TODO).')
 + C.img('k56_invag_echo.gif', 'Échographie avec Doppler couleur : image ronde faite d’anneaux concentriques, peu vascularisée.', 'Invagination intestinale en échographie : image en cible faite des couches concentriques des segments emboîtés ; le Doppler y montre peu de flux.', INV)
 + P('<i>Lecture de l’image.</i> Chaque anneau correspond à une paroi intestinale : celle du segment qui reçoit et celle du segment invaginé ; ainsi, la coupe transversale dessine une cible. De plus, le méso entraîné dans le télescopage est comprimé ; c’est pourquoi le Doppler, qui montre ici peu de flux, renseigne sur la vitalité de l’intestin.')
 + key('Iléus paralytique : distension diffuse sans changement de calibre, traiter la cause ; invagination : image en cible ; iléus biliaire : voir K80 ; traitement spécifique : TODO.')
 + C.pareto('pareto-k56-clinique', 'Occlusion intestinale', ['k56-3', 'k56-4', 'k56-5', 'k56-6', 'k56-8'],
     ['Chercher d’emblée péritonite, strangulation, ischémie.',
      'Scanner plutôt que radiographie.',
      'Brides sans gravité : à jeun, sonde, réhydratation, potassium.',
      'Contraste hydrosoluble : radiographie à 24 h.',
      'Limite du traitement non opératoire ≈ 72 h.',
      'Volvulus du sigmoïde : détorsion endoscopique puis sigmoïdectomie.'])
 + src(BOL, SV))

C.a(10, 'Synthèse et retour au cas', P(
 'Pour conclure, reprenons le patient du début. L’examen ne montre pas de péritonite et les orifices herniaires sont libres ; cependant, comme l’examen manque la moitié des strangulations, un scanner est fait. Il montre des anses grêles dilatées, un changement de calibre et un grêle d’aval vide, sans anse fermée, sans défaut de rehaussement ni liquide libre : il s’agit donc d’une occlusion du grêle sur bride non compliquée.',
 'Dès lors, la conduite suit la WSES. D’abord, il est mis à jeun, une sonde nasogastrique décomprime l’estomac, et une perfusion corrige la déshydratation et l’hypokaliémie. Ensuite, du contraste hydrosoluble est donné par la sonde, et une radiographie à 24 heures le montre dans le côlon : l’occlusion se lève. En revanche, si le contraste n’avait pas progressé, ou si un signe de souffrance était apparu, l’adhésiolyse aurait été indiquée, sans dépasser environ 72 heures d’essai.')
 + key('Examen rassurant mais insuffisant → scanner : bride simple → à jeun, sonde, réhydratation, potassium → contraste : côlon atteint à 24 h → levée ; sinon chirurgie.')
 + src(BOL))

C.a(11, 'Critères formels et paramètres clés', alert(
 '<p><b>Contre-indications au traitement non opératoire (WSES).</b> Péritonite, strangulation, ischémie ; au scanner : anse fermée, ischémie, liquide libre. <b>Traitement non opératoire.</b> À jeun, décompression, réhydratation, électrolytes, nutrition, prévention de l’inhalation ; contraste hydrosoluble et radiographie à 24 h ; durée sûre ≈ 72 h.</p>', 'Critères.')
 + '<div class="key"><b>Paramètres clés.</b> Brides ≈ 60 % des occlusions du grêle ; mortalité 3 % par épisode ; succès du traitement non opératoire 70-90 % ; sensibilité de l’examen pour la strangulation 48 % ; scanner ≈ 90 % ; radiographie ≈ 70 % ; CRP > 75 et leucocytes > 10 000/mm³ : péritonite possible ; récidive 12 % à 1 an.</div>'
 + src(BOL))

# ---------------- Examens
C.e(1, 'Hiérarchie des examens', P(
 'Chaque examen répond à une question précise ; c’est pourquoi leur ordre importe.')
 + table(['Question', 'Examen', 'Recommandation'], [
   ['Retentissement ? souffrance ?', 'Formule, ' + w('k56-lact', 'lactate') + ', électrolytes, CRP, urée, créatinine', 'Bilan minimal (WSES IID)'],
   ['Occlusion ? cause ? strangulation ?', w('k56-tdm', 'Scanner injecté'), 'Examen de choix en cas de doute (WSES)'],
   ['Levée de l’occlusion ?', w('k56-hydro', 'Contraste hydrosoluble') + ' puis radiographie à 24 h', 'WSES IB'],
   ['Radiographie seule ?', w('k56-asp', 'Radiographie de l’abdomen'), 'Non recommandée (WSES IIC), sauf volvulus du sigmoïde (WSES 2023)'],
   ['Grossesse ?', 'Échographie, puis IRM', 'Situations particulières (WSES)']])
 + P('<i>Lecture du tableau.</i> La biologie mesure le retentissement, mais seule l’imagerie montre le mécanisme et la vitalité de l’intestin ; ainsi, le scanner décide de la chirurgie, et le contraste à 24 heures juge l’évolution. En revanche, la radiographie garde une place dans le volvulus du sigmoïde, où le grain de café est très parlant.')
 + key('Biologie → scanner (si doute ou gravité) → contraste et radiographie à 24 h ; radiographie seule : surtout le volvulus.')
 + src(BOL, SV))

C.e(2, 'Lire le scanner d’une occlusion', P(
 'Le compte rendu doit répondre à cinq questions : y a-t-il une occlusion, et du grêle ou du côlon ? où est le changement de calibre ? quelle est la cause (bride présumée, tumeur, hernie, volvulus, invagination, calcul) ? y a-t-il une anse fermée ? enfin, y a-t-il des signes d’ischémie ou du liquide libre ? Ainsi, il fournit directement la décision : essai non opératoire ou chirurgie.')
 + C.img('k56_bride_tdm.gif', 'Scanner axial et coronal annoté : anses dilatées, changement de calibre, grêle de famine.', 'Changement de calibre et grêle de famine : signature d’une bride.', TDM)
 + P('<i>Lecture de l’image.</i> On suit les anses dilatées jusqu’au point où elles deviennent brusquement plates ; or, si aucune masse ni hernie n’est visible à ce niveau, la bride devient le diagnostic le plus probable. Ensuite, on regarde le rehaussement de la paroi et le liquide entre les anses ; en effet, ce sont eux qui distinguent l’occlusion simple de l’occlusion étranglée.')
 + key('Occlusion ? siège ? cause ? anse fermée ? ischémie et liquide libre ? → décision.')
 + C.pareto('pareto-k56-examens', 'Examens', ['k56-e-1', 'k56-e-2'],
     ['Lactate et potassium.',
      'Scanner en cas de doute ou de gravité.',
      'Contraste hydrosoluble : contrôle à 24 h.',
      'Volvulus : grain de café sur la radiographie.'])
 + src(BOL))

# ---------------- Sciences
C.s('anat', 'Anatomie', 'Anatomie : brides et mésentère', P(
 'Les adhérences sont des tissus fibreux qui relient des surfaces péritonéales normalement séparées ; ainsi, une bride tendue entre deux points peut couder une anse ou l’enfermer. Or, le mésentère porte les vaisseaux de l’intestin : si une anse se tord ou est prise dans un anneau, ses vaisseaux sont comprimés en même temps qu’elle. C’est pourquoi l’anse fermée et le volvulus sont les formes les plus dangereuses.')
 + key('Bride = fibrose péritonéale ; anse fermée et torsion = compression du mésentère = ischémie.', 'Science → clinique.'))
C.s('physio', 'Physiologie', 'Physiologie : pertes liquidiennes et électrolytiques', P(
 'L’intestin sécrète chaque jour plusieurs litres de liquide qu’il réabsorbe normalement en aval ; or, en cas d’occlusion, ce liquide reste dans les anses d’amont ou est vomi. Ainsi, le patient perd de l’eau et des électrolytes, en particulier du potassium, et il peut faire une insuffisance rénale aiguë, d’où la surveillance de l’urée et de la créatinine demandée par la WSES. De plus, la distension elle-même freine la motricité et entretient l’accumulation.')
 + key('Occlusion = troisième secteur intestinal + vomissements → déshydratation, hypokaliémie, insuffisance rénale.', 'Science → biologie.'))
C.s('histo', 'Histologie', 'Histologie : de la cicatrisation à l’adhérence', P(
 'Après une agression du péritoine, la réparation normale restaure une surface lisse ; en revanche, une cicatrisation pathologique laisse des ponts fibreux, qui deviennent des adhérences (WSES). Ainsi, tout ce qui lèse davantage le péritoine, corps étrangers comme certains filets ou l’électrocoagulation monopolaire, favorise les adhérences. C’est pourquoi les barrières anti-adhérences agissent comme des intercalaires, qui séparent les surfaces lésées le temps qu’elles cicatrisent.')
 + key('Adhérence = cicatrisation péritonéale pathologique ; barrière = intercalaire temporaire.', 'Science → prévention.'))
C.s('radio', 'Physique de l’imagerie', 'Physique de l’imagerie : niveaux et contraste', P(
 'Sur un cliché debout, le gaz, plus léger, surmonte le liquide ; ainsi, chaque anse distendue forme un niveau horizontal. Par ailleurs, le produit de contraste hydrosoluble est très dense aux rayons X : sa progression jusqu’au côlon prouve que la lumière est perméable. De plus, au scanner, l’iode injecté rehausse la paroi vivante ; par conséquent, une paroi qui ne se rehausse pas signe une ischémie.')
 + key('Niveaux = gaz sur liquide ; contraste dans le côlon = perméabilité ; paroi non rehaussée = ischémie.', 'Science → lecture.'))

# ---------------- Pharmacologie
C.p(1, 'Stratégie et classes', P(
 'Dans l’occlusion, les médicaments soutiennent le traitement mais ne le remplacent pas ; en effet, le cœur du traitement non opératoire est mécanique (décompression) et hydroélectrolytique.')
 + table(['Situation', 'Moyen', 'Source', 'Fenêtre'], [
   ['Déshydratation, pertes digestives', 'Réhydratation intraveineuse, correction des électrolytes', 'WSES', w('k56-sng', 'Fiche')],
   ['Test et peut-être traitement de l’occlusion sur brides', 'Produit de contraste hydrosoluble oral', 'WSES IB', w('k56-hydro', 'Fiche')],
   ['Nausées et vomissements', 'Pas de prokinétique : le métoclopramide est contre-indiqué', 'FI Paspertin®', w('k56-d-mcp', 'Monographie')],
   ['Prévention des récidives après chirurgie', 'Barrière anti-adhérences', 'WSES IA-IIB', w('k56-adhesio', 'Fiche')]])
 + P('<i>Lecture du tableau.</i> Chaque ligne traite une conséquence de l’occlusion, non l’obstacle lui-même ; or, accélérer le péristaltisme contre un obstacle augmenterait la pression d’amont. C’est pourquoi les prokinétiques n’ont pas leur place.')
 + key('Décompression + réhydratation + électrolytes ; contraste hydrosoluble ; pas de métoclopramide en cas d’occlusion.')
 + src(BOL, FI('Paspertin®')))

C.p(2, 'Doses et statut réglementaire', P(
 'Les recommandations lues ne donnent pas de dose de produit de contraste hydrosoluble ; de plus, aucune information professionnelle suisse de produit de contraste oral à l’amidotrizoate n’a été trouvée dans la base AIPS consultée. Par conséquent, la dose et le produit utilisés suivent le protocole local de radiologie (TODO : source suisse à compléter à l’audit).')
 + table(['Médicament', 'Donnée suisse', 'Statut dans l’occlusion', 'Source'], [
   ['Métoclopramide (Paspertin®)', 'Dose maximale 30 mg/j ou 0,5 mg/kg/j ; intervalle ≥ 6 h', 'Contre-indiqué : occlusion ou perforation intestinale', 'FI Paspertin®'],
   ['Contraste hydrosoluble oral', 'Aucune FI trouvée (AIPS 08.10.2026)', 'Recommandé par la WSES (IB)', 'WSES 2017'],
   ['Potassium, solutés', 'Selon la kaliémie et l’état d’hydratation', 'Correction recommandée, sans dose précisée', 'WSES 2017']])
 + P('<i>Lecture du tableau.</i> La seule donnée réglementaire nette concerne ce qu’il ne faut pas donner : l’information professionnelle du métoclopramide le contre-indique en cas d’occlusion, notamment lorsque la stimulation de la motricité représente un danger. Ainsi, l’antiémétique éventuel doit être choisi sans effet prokinétique ; toutefois, aucune source lue ne désigne une molécule précise (TODO).')
 + trap('Donner du métoclopramide à un patient occlus pour ses vomissements est une erreur : la molécule stimule la motricité digestive et est contre-indiquée en cas d’occlusion ou de perforation (FI Paspertin®).', 'Piège')
 + key('Métoclopramide contre-indiqué ; contraste : dose selon protocole local (aucune FI suisse trouvée) ; potassium corrigé selon la biologie.')
 + src(FI('Paspertin®'), BOL))

C.p(3, 'Surveillance', alert(
 'Pendant l’essai non opératoire, il faut réévaluer régulièrement la douleur, l’abdomen, le débit de la sonde, la diurèse, le potassium, la créatinine et le lactate ; de plus, toute apparition de péritonite, de fièvre ou d’élévation du lactate fait reconsidérer la chirurgie. Enfin, les complications médicales habituelles sont la déshydratation avec insuffisance rénale, les troubles électrolytiques, la dénutrition et l’inhalation (WSES).', 'Sécurité.')
 + P('Par ailleurs, chez le sujet âgé à jeun, l’arrêt des traitements oraux habituels pose un problème encore peu étudié, comme le souligne la WSES ; ainsi, chaque médicament interrompu doit être revu, et remplacé par une forme parentérale si nécessaire.')
 + key('Réévaluer abdomen, sonde, diurèse, électrolytes, lactate ; aggravation → chirurgie ; revoir les traitements interrompus du sujet âgé.')
 + C.pareto('pareto-k56-pharma', 'Pharmacologie', ['k56-p-1', 'k56-p-2', 'k56-p-3'],
     ['Réhydratation et potassium.',
      'Contraste hydrosoluble, contrôle à 24 h.',
      'Pas de métoclopramide.',
      'Surveillance du lactate et de la diurèse.'])
 + src(BOL))

# ---------------- Fenêtres
L = lab
C.pop('k56-osb', 'Occlusion du grêle sur brides', L(('Définition', 'Obstacle au passage du contenu du grêle causé par des adhérences, le plus souvent postopératoires.'), ('Fréquence', '≈ 60 % des occlusions du grêle ; 3 % de mortalité hospitalière par épisode.'), ('Traitement', 'Non opératoire en l’absence de péritonite, strangulation ou ischémie (70-90 % de succès).')) + C.img('k56_bride_tdm.gif', 'Scanner : anses dilatées, changement de calibre, grêle vide.', 'Bride au scanner : changement de calibre.', TDM) + src(BOL))
C.pop('k56-occl', 'Occlusion intestinale', L(('Signes', 'Douleur, vomissements, distension, arrêt des matières et des gaz.'), ('Mécanique', 'Bride, tumeur, volvulus, invagination, calcul, hernie.'), ('Fonctionnelle', 'Iléus paralytique : pas d’obstacle.')) + src(BOL))
C.pop('k56-ileus', 'Iléus paralytique', L(('Définition', 'Arrêt du péristaltisme sans obstacle.'), ('Imagerie', 'Distension diffuse sans changement de calibre.'), ('Traitement', 'Celui de la cause ; correction électrolytique ; critères et traitement spécifiques : TODO.')))
C.pop('k56-invag', 'Invagination', L(('Définition', 'Télescopage d’un segment intestinal dans le segment voisin.'), ('Échographie', 'Image en cible.')) + C.img('k56_invag_echo.gif', 'Échographie : image en cible.', 'Image en cible de l’invagination.', INV))
C.pop('k56-volv', 'Volvulus du sigmoïde', L(('Mécanisme', 'Torsion du sigmoïde autour de son méso : anse fermée.'), ('Diagnostic', 'Radiographie : grain de café ; scanner si doute, ischémie ou perforation (WSES 2023, 1C).'), ('Traitement', 'Détorsion endoscopique, puis sigmoïdectomie pendant la même hospitalisation ; résection urgente si échec, ischémie ou perforation.')) + C.img('k56_volvulus.gif', 'Radiographie : anse sigmoïde géante.', 'Grain de café.', VOL) + src(SV))
C.pop('k56-grain', 'Signe du grain de café', L(('Aspect', 'Anse sigmoïde géante distendue, dont les deux jambages accolés dessinent un sillon.'), ('Valeur', 'Signe radiographique classique du volvulus du sigmoïde (WSES 2023).')) + C.img('k56_volvulus.gif', 'Radiographie : grain de café.', 'Volvulus du sigmoïde.', VOL) + src(SV))
C.pop('k56-strang', 'Strangulation', L(('Définition', 'Occlusion avec compromission de la vascularisation de l’anse.'), ('Clinique', 'L’examen n’en détecte que 48 %.'), ('Imagerie', 'Scanner ≈ 90 % d’exactitude ; anse fermée, paroi non rehaussée, liquide libre.'), ('Conduite', 'Chirurgie sans délai.')) + src(BOL))
C.pop('k56-anse', 'Anse fermée', L(('Définition', 'Segment intestinal occlus à ses deux extrémités.'), ('Danger', 'Distension sans décompression possible et compression du mésentère : ischémie.'), ('Conduite', 'Chirurgie sans délai (WSES).')) + src(BOL))
C.pop('k56-tdm', 'Scanner de l’occlusion', L(('Place', 'Examen de choix en cas de doute sur la cause ou de signe de gravité.'), ('Performance', '≈ 90 % d’exactitude pour la strangulation et l’indication chirurgicale.'), ('À chercher', 'Changement de calibre, cause, anse fermée, ischémie, liquide libre.')) + C.img('k56_bride_tdm.gif', 'Scanner d’une bride.', 'Changement de calibre.', TDM) + src(BOL))
C.pop('k56-asp', 'Radiographie de l’abdomen', L(('Aspect', 'Niveaux hydroaériques, anses grêles distendues, côlon vide.'), ('Limites', 'Sensibilité ≈ 70 % ; ni cause ni strangulation ; non recommandée (WSES IIC).'), ('Exception', 'Volvulus du sigmoïde : grain de café (WSES 2023).')) + C.img('k56_asp.gif', 'Radiographie debout : niveaux hydroaériques.', 'Niveaux hydroaériques.', ASP) + src(BOL, SV))
C.pop('k56-hydro', 'Produit de contraste hydrosoluble', L(('Usage', 'Par la sonde, puis radiographie à 24 h.'), ('Interprétation', 'Côlon atteint : levée de l’occlusion ; non atteint : échec très probable du traitement non opératoire.'), ('Effets', 'Prédit la chirurgie, raccourcit le séjour, peut-être thérapeutique (WSES IB).'), ('Dose', 'Non précisée par la WSES ; aucune FI suisse trouvée (TODO).')) + src(BOL))
C.pop('k56-lact', 'Lactate', L(('Place', 'Bilan minimal de l’occlusion (WSES) et du volvulus (WSES 2023).'), ('Sens', 'Marqueur d’hypoperfusion : son élévation fait craindre une ischémie intestinale.')) + src(BOL, SV))
C.pop('k56-zielinski', 'Score de Zielinski', L(('Éléments', 'Œdème du mésentère, absence de signe des fèces dans le grêle, arrêt complet des matières et des gaz.'), ('Performance', 'Indice de concordance 0,77 (100 cas).'), ('Limite', 'Aide à la décision, ne remplace pas la clinique.')) + src(BOL))
C.pop('k56-sng', 'Traitement non opératoire', L(('Composantes', 'À jeun, sonde nasogastrique ou intestinale longue, réhydratation intraveineuse, électrolytes, nutrition, prévention de l’inhalation.'), ('Durée', '≈ 72 h considérées comme sûres (WSES IIB).'), ('Succès', '70-90 %.')) + src(BOL))
C.pop('k56-adhesio', 'Adhésiolyse et prévention', L(('Geste', 'Section des adhérences, par laparotomie ou laparoscopie chez des patients sélectionnés.'), ('Risque', 'Plaies intestinales 6,3-26,9 % en laparoscopie.'), ('Prévention', 'Chirurgie mini-invasive ; hyaluronate-carboxyméthylcellulose (RR 0,49 de réopération, chirurgie colorectale) ; icodextrine 4 %.')) + src(BOL))
C.pop('k56-sems', 'Prothèse colique métallique', L(('Indication', 'Cancer du côlon gauche occlusif : palliation, ou pont vers une chirurgie programmée dans des cas choisis.'), ('Bénéfices', 'Moins de stomies, meilleurs résultats à court terme.'), ('Risques', 'Perforation jusqu’à 13 % ; incertitude oncologique.')) + src(CRC))
C.pop('k56-d-mcp', 'Métoclopramide (Paspertin®)', L(('Mécanisme', 'Antiémétique prokinétique.'), ('Contre-indication', 'Hémorragie digestive, occlusion ou perforation intestinale, notamment quand la stimulation de la motricité est dangereuse.'), ('Dose maximale', '30 mg/j ou 0,5 mg/kg/j ; au moins 6 h entre deux prises.')) + src(FI('Paspertin®')))

C.termes = [
 (r'occlusion du grêle sur brides?', 'k56-osb'), (r'iléus paralytique', 'k56-ileus'), (r'strangulation', 'k56-strang'), (r'anse fermée', 'k56-anse'),
 (r'scanner', 'k56-tdm'), (r'radiographie de l’abdomen', 'k56-asp'), (r'contraste hydrosoluble', 'k56-hydro'), (r'lactate', 'k56-lact'),
 (r'Zielinski', 'k56-zielinski'), (r'traitement non opératoire', 'k56-sng'), (r'adhésiolyse', 'k56-adhesio'), (r'prothèse', 'k56-sems'),
 (r'volvulus du sigmoïde', 'k56-volv'), (r'grain de café', 'k56-grain'), (r'invagination', 'k56-invag'), (r'métoclopramide', 'k56-d-mcp'),
]

C.write()
