"""G45 — ajouts conditionnels, sans remplacer une clé commune existante."""
from cardio_1 import a, G
def add(k,literal,full,definition,ref):
    if k not in G:
        a(k,literal,full,'<p>'+definition+'</p>',ref)
add('AIT',[('A','Accident'),('I','Ischémique'),('T','Transitoire')],'Accident ischémique transitoire','Épisode focal transitoire compatible avec une ischémie ; la définition tissulaire bernoise précise l’absence de lésion concordante en diffusion. La récupération ne retire pas l’urgence.','g45-definition')
add('AVC',[('A','Accident'),('V','Vasculaire'),('C','Cérébral')],'Accident vasculaire cérébral','Un déficit focal aigu peut relever d’un événement vasculaire cérébral ; sa nature et son mécanisme nécessitent une évaluation urgente.','g45-parcours')
add('ABCD2',[('A','Age : âge'),('B','Blood pressure : pression artérielle'),('C','Clinical features : signes cliniques'),('D','Duration : durée ; Diabetes : diabète'),('2','Deux domaines commençant par D')],'Score clinique après un accident ischémique transitoire','Le total va de zéro à sept. Il ne constitue ni un diagnostic ni une règle isolée de sortie ; les variables et le calcul sont expliqués dans la fenêtre locale.','g45-score')
add('IRM',[('I','Imagerie'),('R','Résonance'),('M','Magnétique')],'Imagerie par résonance magnétique','Les séquences répondent à des questions tissulaires ou vasculaires distinctes. Une diffusion négative n’exclut pas tout événement ischémique.','g45-diffusion')
add('DWI',[('D','Diffusion'),('W','Weighted'),('I','Imaging')],'Diffusion-weighted imaging : imagerie pondérée en diffusion','La séquence est confrontée au coefficient apparent de diffusion et au contexte clinique.','g45-diffusion')
add('ADC',[('A','Apparent'),('D','Diffusion'),('C','Coefficient')],'Apparent diffusion coefficient : coefficient apparent de diffusion','La carte complète la lecture de la diffusion ; une diminution concordante aide à caractériser une restriction.','g45-diffusion')
add('ESO',[('E','European'),('S','Stroke'),('O','Organisation')],'European Stroke Organisation','La recommandation 2021 utilisée ici définit ses populations et ses niveaux de preuve.','g45-contentieux')
add('FI',[('F','Fach'),('I','Information')],'Fachinformation : information professionnelle suisse','La fiche du produit exact décrit ses indications, formes, doses, exclusions et interactions. Une recommandation clinique distincte doit être attribuée.','g45-monographies')
add('ADP',[('A','Adénosine'),('D','Di'),('P','Phosphate')],'Adénosine diphosphate','Ce nucléotide intervient notamment dans la signalisation plaquettaire.','g45-plaquette')
add('ATP',[('A','Adénosine'),('T','Tri'),('P','Phosphate')],'Adénosine triphosphate','L’énergie disponible conditionne les transports ioniques et la recapture des neurotransmetteurs.','g45-energie')
add('CYP2C19',[('CYP','Cytochrome P450'),('2','Famille 2'),('C','Sous-famille C'),('19','Membre 19')],'Cytochrome P450 2C19','Cette enzyme participe à l’activation du clopidogrel. Une interaction ou une variabilité métabolique ne justifie pas une dose supérieure empirique universelle.','g45-genetique')
add('CYP3A4',[('CYP','Cytochrome P450'),('3','Famille 3'),('A','Sous-famille A'),('4','Membre 4')],'Cytochrome P450 3A4','Cette voie métabolique intervient dans des interactions dont la conduite dépend du produit suisse exact.','g45-interactions')
add('P2Y12',[('P2Y','Famille de récepteurs purinergiques P2Y'),('12','Sous-type 12')],'Récepteur purinergique P2Y12','Le métabolite actif du clopidogrel inhibe ce récepteur plaquettaire ; il ne s’agit pas d’une dose ni d’un score.','g45-plavix')
add('HMG-CoA',[('H','Hydroxy'),('M','Méthyl'),('G','Glutaryl'),('CoA','Coenzyme A')],'3-hydroxy-3-méthylglutaryl-coenzyme A','L’atorvastatine inhibe la réductase de cette voie et diminue la synthèse hépatique du cholestérol.','g45-sortis')
add('CA1',[('CA','Cornu Ammonis : corne d’Ammon'),('1','Champ 1')],'Champ CA1 de l’hippocampe','La recommandation sur l’amnésie globale transitoire décrit des foyers ponctuels parfois détectés dans cette région.','g45-reseaux')
add('CA3',[('CA','Cornu Ammonis : corne d’Ammon'),('3','Champ 3')],'Champ CA3 de l’hippocampe','Ce champ figure parmi les connexions hippocampiques de l’illustration publiée.','g45-reseaux')
for key,meaning,ref in [
 ('EXPRESS','Étude d’organisation rapide après accident transitoire ou mineur','g45-risque'),
 ('CHANCE','Essai de double antiagrégation précoce après événement mineur ou transitoire à haut risque','g45-plavix'),
 ('POINT','Essai de double antiagrégation après événement mineur ou transitoire à haut risque','g45-plavix'),
 ('CAPRIE','Essai comparant clopidogrel et aspirine en prévention vasculaire','g45-plavix'),
 ('ARISTOTLE','Essai comparant apixaban et warfarine dans la fibrillation auriculaire','g45-eliquis'),
 ('SPARCL','Essai comparant atorvastatine intensive et placebo après événement cérébrovasculaire','g45-sortis')]:
 add(key,[(key,'Nom propre d’un essai ; aucun développement littéral non vérifié n’est inventé')],meaning,'La fenêtre décrit la population, la comparaison et les limites effectivement lues dans la source.',''+ref)
add('cAMP',[('c','Cyclique'),('A','Adénosine'),('M','Mono'),('P','Phosphate')],'Adénosine monophosphate cyclique','Nucléotide identifié dans la carte de signalisation ; nomenclature vérifiée dans ChEBI, entrée 17489.','g45-plaquette')
add('vWF',[('v','von'),('W','Willebrand'),('F','Factor : facteur')],'Facteur von Willebrand','Nom de la protéine indiqué dans la figure plaquettaire ; nomenclature VWF vérifiée auprès du comité HGNC.','g45-plaquette')
add('PTGS1',[('PTGS','Symbole officiel : prostaglandin-endoperoxide synthase'),('1','Membre 1')],'Prostaglandine-endoperoxyde synthase 1','Le comité HGNC donne cyclooxygenase-1 parmi les noms associés. Le symbole désigne une enzyme de la figure, pas une indication thérapeutique.','g45-plaquette')
add('PLA2',[('P','Phospho'),('L','Lipase'),('A2','Type A2')],'Phospholipase A2','Libellé de famille enzymatique dans la figure ; il ne spécifie pas à lui seul une isoforme ni une prescription.','g45-plaquette')
add('TXA2',[('TX','Thromboxane'),('A2','Type A2')],'Thromboxane A2','La fiche Aspirine Cardio décrit la diminution de sa synthèse plaquettaire.','g45-aspirine')
add('PG',[('P','Prosta'),('G','Glandine')],'Prostaglandines','Famille désignée par ces lettres dans la figure ; les suffixes distinguent les molécules représentées.','g45-plaquette')
for key,lit,full in [
 ('LPGH',[('L','Last'),('P','Proof of'),('G','Good'),('H','Health')],'Last proof of good health : dernière preuve de bon état'),
 ('LVO',[('L','Large'),('V','Vessel'),('O','Occlusion')],'Large vessel occlusion : occlusion d’un gros vaisseau'),
 ('RACE',[('R','Rapid'),('A','Arterial'),('C','oCclusion'),('E','Evaluation')],'Rapid Arterial Occlusion Evaluation : score de tri préhospitalier'),
 ('SU',[('S','Stroke'),('U','Unit')],'Stroke unit : unité neurovasculaire'),
 ('SC',[('S','Stroke'),('C','Center')],'Stroke center : centre neurovasculaire'),
 ('EVT',[('EV','EndoVascular'),('T','Treatment')],'Endovascular treatment : traitement endovasculaire'),
 ('DIDO',[('D','Door'),('I','In'),('D','Door'),('O','Out')],'Door-in-door-out : délai entre entrée et sortie de l’hôpital')]:
 add(key,lit,full,'Abréviation conservée dans la figure suisse originale de 2021. La légende traduit le terme ; la portée concerne le tri préhospitalier, pas une règle de sortie après AIT.','g45-parcours')
# Ajouts C02-R-NEUR (14.10.2026) : symboles de la figure plaquettaire PharmGKB, vérifiés auprès du HGNC et de ChEBI.
for key,lit,full,definition in [
 ('TBXA2',[('TBX','ThromBoXane'),('A2','A2')],'Thromboxane A2 (molécule)','Eicosanoïde plaquettaire, entrée ChEBI 15627. C’est la molécule produite par la voie que l’aspirine interrompt ; elle n’est ni l’enzyme qui la fabrique ni son récepteur.'),
 ('TBXAS1',[('TBX','ThromBoXane'),('A','A'),('S','Synthase'),('1','membre 1')],'Thromboxane A synthase 1 (enzyme)','Symbole officiel HGNC 11609. Cette enzyme transforme la prostaglandine H2 en thromboxane A2.'),
 ('TBXA2R',[('TBX','ThromBoXane'),('A2','A2'),('R','Récepteur')],'Récepteur du thromboxane A2','Symbole officiel HGNC 11608. Récepteur plaquettaire qui reçoit le thromboxane A2 et amplifie l’activation ; l’aspirine ne le bloque pas.'),
 ('P2RY12',[('P2','Purinergique de type 2'),('R','Récepteur'),('Y','famille Y, couplée aux protéines G'),('12','sous-type 12')],'Récepteur purinergique P2Y12','Symbole officiel HGNC 18124 du récepteur noté P2Y12 dans le cours. Le métabolite actif du clopidogrel le bloque.'),
 ('P2RY1',[('P2','Purinergique de type 2'),('R','Récepteur'),('Y','famille Y, couplée aux protéines G'),('1','sous-type 1')],'Récepteur purinergique P2Y1','Symbole officiel HGNC 8539. Second récepteur plaquettaire de l’adénosine diphosphate, que le clopidogrel ne vise pas.'),
 ('P2RX1',[('P2','Purinergique de type 2'),('R','Récepteur'),('X','famille X, canal ionique'),('1','sous-type 1')],'Récepteur purinergique P2X1','Symbole officiel HGNC 8533 ; ancien nom : canal ionique activé par ligand. Il laisse entrer le calcium sous l’effet de l’adénosine triphosphate.'),
 ('F2R',[('F2','Facteur II de la coagulation, thrombine'),('R','Récepteur')],'Récepteur de la thrombine','Symbole officiel HGNC 3537, appelé aussi récepteur activé par les protéases 1. Il relie la coagulation à l’activation plaquettaire.'),
 ('ADCY3',[('AD','ADénylate'),('CY','CYclase'),('3','membre 3')],'Adénylate cyclase 3','Symbole officiel HGNC 234. Enzyme qui produit l’adénosine monophosphate cyclique à partir de l’adénosine triphosphate.'),
 ('GNAS',[('G','protéine G'),('N','Nucléotide guanine, liaison'),('A','sous-unité Alpha'),('S','Stimulatrice')],'Locus complexe GNAS','Symbole officiel HGNC 4392 ; l’ancien nom HGNC développe les lettres : guanine nucleotide binding protein, alpha stimulating. Il code la sous-unité alpha stimulatrice d’une protéine G.'),
 ('IP3',[('I','Inositol'),('P','Phosphate'),('3','trois groupements, positions 1, 4 et 5')],'Inositol 1,4,5-trisphosphate','Messager intracellulaire, entrée ChEBI 16595 ; sur la figure plaquettaire, il conduit à l’élévation du calcium.'),
 ('PGG2',[('PG','ProstaGlandine'),('G','série G'),('2','indice 2')],'Prostaglandine G2','Entrée ChEBI 27647. Intermédiaire formé par la cyclo-oxygénase à partir de l’acide arachidonique.'),
 ('PGH2',[('PG','ProstaGlandine'),('H','série H'),('2','indice 2')],'Prostaglandine H2','Entrée ChEBI 15554. Précurseur que la thromboxane synthase transforme en thromboxane A2.'),
 ('PGD2',[('PG','ProstaGlandine'),('D','série D'),('2','indice 2')],'Prostaglandine D2','Entrée ChEBI 15555 ; elle agit sur les récepteurs des prostaglandines de la figure.'),
 ('PGI2',[('PG','ProstaGlandine'),('I','série I'),('2','indice 2')],'Prostaglandine I2 ou prostacycline','Entrée ChEBI 15552 ; sur la figure, elle participe à la rétroaction négative de l’activation plaquettaire.'),
 ('PGE2',[('PG','ProstaGlandine'),('E','série E'),('2','indice 2')],'Prostaglandine E2','Entrée ChEBI 15551 ; elle agit sur les récepteurs des prostaglandines de la figure.'),
 ('VWF',[('V','von'),('W','Willebrand'),('F','Facteur')],'Facteur von Willebrand','Symbole officiel HGNC 12726, écrit vWF dans d’autres textes. Protéine d’adhésion qui fixe la plaquette au sous-endothélium.')]:
 add(key,lit,full,definition,'g45-plaquette')
