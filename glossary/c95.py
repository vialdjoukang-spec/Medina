from cardio_1 import a, G
# C95 — Leucémie à cellules non précisées (H-08-Hématologie). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
def d(k, lit, full, df, ref=None):
    if k not in G:
        a(k, lit, full, '<p>' + df + '</p>', ref)

def code(k, full, df, ref='c95-categorie'):
    d(k, [(k, 'code de la CIM-10-GM 2024 ; ce code n’est pas développable lettre à lettre')], full, df, ref)

for key,label in [('C95.10','Leucémie chronique à cellules non précisées, sans mention de rémission complète'),('C95.11','Leucémie chronique à cellules non précisées, en rémission complète'),('C95.70','Autres leucémies à cellules non précisées, sans mention de rémission complète'),('C95.71','Autres leucémies à cellules non précisées, en rémission complète'),('C95.90','Leucémie sans précision, sans mention de rémission complète'),('C95.91','Leucémie sans précision, en rémission complète')]:
    code(key,label,'CIM-10-GM 2024 ; caractère final 0 incluant rémission partielle ou statut inconnu, 1 pour rémission complète documentée.','c95-cim-5e')

for key,parts,label,definition,ref in [
 ('MEBEKO',[('ME','Medizinal'),('BE','Berufe'),('KO','Kommission')],'Commission des professions médicales','Autorité suisse dont les exigences de l’examen 2026 renvoient à PROFILES 2017.','c95-profiles'),
 ('EVOLVE',[('EVOLVE','nom d’une étude, non développé arbitrairement')],'Série EVOLVE de changements de lignée','Les 70 cas décrits sont sélectionnés pour un changement de lignée ; ce dénominateur ne mesure pas le risque de tous les patients traités.','c95-lineage-switch'),
 ('P2RY8',[('P2RY','P2Y receptor'),('8','numéro 8')],'Récepteur purinergique P2Y8','Partenaire de fusion de CRLF2 dans le cas B/myéloïde de la figure3 publiée ; pas une anomalie obligatoire de LAPM.','c95-cytometrie'),
 ('CRLF2',[('C','Cytokine'),('R','Receptor'),('L','Like'),('F','Factor'),('2','numéro 2')],'Facteur2 de type récepteur de cytokine','Gène impliqué dans la fusion du cas cytométrique illustré ; interprétation avec le profil complet.','c95-cytometrie'),
 ('iBFM',[('i','international'),('BFM','Berlin–Francfort–Münster')],'Groupe coopératif international BFM','Consortium de l’étude pédiatrique rétrospective de233patients ; décisions adultes non automatiquement extrapolées.','c95-ibfm'),
 ('OAMal',[('O','Ordonnance'),('AMal','sur l’assurance-maladie')],'Ordonnance sur l’assurance-maladie','Articles71a–71d : prise en charge de médicaments dans certains cas particuliers, à vérifier individuellement.','c95-hors-etiquette'),
 ('BCL-2',[('BCL','B-cell lymphoma'),('2','numéro 2')],'Protéine BCL-2','Protéine impliquée dans la régulation de l’apoptose, cible du vénétoclax ; la cible ne définit pas seule une indication LAPM.','c95-hors-etiquette')]:
    d(key,parts,label,definition,ref)

code('C95.0', 'Leucémie aiguë à cellules non précisées (C95.0-)', 'Sous-catégorie de C95 : leucémie aiguë dont la lignée n’est pas attribuée, avec la leucémie aiguë biphénotypique, bilinéale ou de lignée mixte. Le cinquième caractère indique la rémission.')
code('C95.1', 'Leucémie chronique à cellules non précisées (C95.1-)', 'Sous-catégorie pour une leucémie chronique dont la lignée n’est pas attribuée ou attribuable ; pas un protocole unique et pas nécessairement un statut temporaire.')
code('C95.7', 'Autres leucémies à cellules non précisées (C95.7-)', 'Sous-catégorie de C95 sans entité clinique décrite dans les sources lues.')
code('C95.8', 'Leucémie réfractaire au traitement d’induction standard (C95.8!)', 'Code additionnel (point d’exclamation) qui s’ajoute au code d’une leucémie ; il n’a pas de cinquième caractère.', 'c95-c958')
code('C95.9', 'Leucémie sans précision (C95.9-)', 'Leucémie sans précision suffisante dans le dossier ; préciser lorsque les données le permettent, sans inventer une lignée ni supposer un statut toujours temporaire.')
code('C95.00', 'Leucémie aiguë à cellules non précisées, sans mention de rémission complète', 'Cinquième caractère 0 : sans mention de rémission complète, incluant rémission partielle ou statut inconnu.', 'c95-cim-5e')
code('C95.01', 'Leucémie aiguë à cellules non précisées, en rémission complète', 'Cinquième caractère 1 : rémission complète documentée.', 'c95-cim-5e')
code('C94.8', 'Code C94.8! cité pour la crise blastique de la leucémie myéloïde chronique', 'Code cité par la recherche pour la crise blastique de la leucémie myéloïde chronique ; à vérifier dans la classification en vigueur.')
code('C92.1', 'Leucémie myéloïde chronique (C92.1-)', 'Catégorie de la leucémie myéloïde chronique dans la CIM-10-GM.')

d('LMA', [('L','Leucémie'),('M','Myéloïde'),('A','Aiguë')], 'Leucémie myéloïde aiguë', 'Leucémie aiguë dont les blastes sont de lignée myéloïde ; au moins 20 % de blastes, sauf règles génétiques définissantes OMS/ICC (Onkopedia LMA septembre 2025).')
d('LLA', [('L','Leucémie'),('L','Lymphoblastique'),('A','Aiguë')], 'Leucémie lymphoblastique aiguë', 'Leucémie aiguë dont les blastes sont de lignée lymphoïde B ou T ; Onkopedia 2026.')
d('LLA-T', [('LLA','Leucémie Lymphoblastique Aiguë'),('T','de lignée T')], 'Leucémie lymphoblastique aiguë de lignée T', 'LLA de lignée T ; dans une suspicion de lignée ambiguë, CD3 spécifique est définissant et CD7 seul ne suffit pas. Un profil CD3 négatif exige une réévaluation.', 'c95-cd3neg')
d('LLA-B', [('LLA','Leucémie Lymphoblastique Aiguë'),('B','de lignée B')], 'Leucémie lymphoblastique aiguë de lignée B', 'LLA dont les blastes expriment le CD19 avec CD10, CD22 ou CD79a ; elle peut basculer vers une autre lignée sous CAR-T ou blinatumomab.', 'c95-lineage-switch')
d('LAPM', [('L','Leucémie'),('A','Aiguë'),('P','à Phénotype'),('M','Mixte')], 'Leucémie aiguë à phénotype mixte', 'Leucémie aiguë remplissant les critères définissants de plusieurs lignées, après exclusions classificatoires ; biphénotypique ou bilinéale. Des marqueurs associés isolés ne suffisent pas.', 'c95-lapm')
d('LAI', [('L','Leucémie'),('A','Aiguë'),('I','Indifférenciée')], 'Leucémie aiguë indifférenciée', 'Leucémie aiguë dont les blastes n’expriment aucun marqueur définissant une lignée.', 'c95-lai')
d('LALA', [('L','Leucémie'),('A','Aiguë'),('L','de Lignée'),('A','Ambiguë')], 'Leucémie aiguë de lignée ambiguë', 'Regroupe notamment LAPM, LAI et certaines formes de lignée ambiguë sans autre précision biologique ; en anglais ALAL.', 'c95-lapm')
d('LMC', [('L','Leucémie'),('M','Myéloïde'),('C','Chronique')], 'Leucémie myéloïde chronique', 'Néoplasie myéloproliférative, indication suisse de l’hydroxycarbamide ; sa crise blastique est une imitation de la LALA.', 'c95-d-hydroxycarbamide')
d('LAP', [('L','Leucémie'),('A','Aiguë'),('P','Promyélocytaire')], 'Leucémie aiguë promyélocytaire', 'Leucémie aiguë promyélocytaire, classiquement PML::RARA ; urgence spécialisée avec ATRA dès suspicion et bilan confirmatoire, distincte des LALA.')
d('ATRA', [('A','All'),('T','Trans'),('R','Retinoic'),('A','Acid')], 'Acide tout-trans rétinoïque', 'Médicament de la leucémie aiguë promyélocytaire, débuté sans attendre la confirmation génétique en cas de suspicion (Onkopedia LAP janvier 2026).')
d('ETP', [('E','Early'),('T','T-cell'),('P','Precursor')], 'Précurseur T précoce (leucémie lymphoblastique T précoce)', 'Forme immature de LLA-T, à distinguer de la LALA par l’immunophénotype complet.')
d('ICC', [('I','International'),('C','Consensus'),('C','Classification')], 'Classification internationale de consensus (2022)', 'Classification des tumeurs hématopoïétiques qui définit, comme l’OMS, la LALA par au moins 20 % de blastes et des critères de lignée.', 'c95-who-icc')
d('EGIL', [('E','European'),('G','Group for the'),('I','Immunological'),('L','characterization of Leukemias')], 'Groupe européen pour la caractérisation immunologique des leucémies', 'Critères historiques de la leucémie aiguë biphénotypique, cités par Onkopedia LLA 2026.')
d('EHA', [('E','European'),('H','Hematology'),('A','Association')], 'Association européenne d’hématologie', 'Association européenne d’hématologie ; les sources et limites de cette recherche ciblée sont détaillées dans la fiche, sans prétendre à une recherche exhaustive.', 'c95-sources-guides')
d('SAKK', [('S','Schweizerische'),('A','Arbeitsgemeinschaft'),('K','für Klinische'),('K','Krebsforschung')], 'Groupe suisse de recherche clinique sur le cancer', 'Groupe suisse de recherche clinique sur le cancer ; le cours ne prétend pas établir une liste exhaustive de ses études actives.', 'c95-sources-guides')
d('GMALL', [('G','German'),('M','Multicenter'),('A','Acute'),('L','Lymphoblastic'),('L','Leukemia')], 'Groupe allemand multicentrique sur la leucémie lymphoblastique aiguë', 'Sa nomenclature retient 25 % de blastes médullaires pour la LLA (Onkopedia 2026).', 'c95-blastes')
d('SEER', [('S','Surveillance'),('E','Epidemiology and'),('E','End'),('R','Results')], 'Registre américain de surveillance, d’épidémiologie et de résultats finaux', 'Registre nord-américain du cancer ; ses chiffres sur la LALA sont descriptifs et ne fondent aucune conduite.', 'c95-pronostic')
d('ALWP', [('A','Acute'),('L','Leukemia'),('W','Working'),('P','Party')], 'Groupe de travail sur les leucémies aiguës (de l’EBMT)', 'Auteur des deux études rétrospectives sur l’allogreffe dans la LAPM.', 'c95-ebmt')
d('iBFM-AMBI2012', [('iBFM-AMBI2012','nom de l’étude coopérative internationale sur les leucémies de lignée ambiguë de l’enfant ; développement littéral non fourni par les sources lues')], 'Étude iBFM-AMBI2012', 'Étude observationnelle de 233 enfants atteints de leucémie de lignée ambiguë.', 'c95-ibfm')
d('FLAG', [('F','Fludarabine'),('L','(et)'),('A','Ara-C, cytarabine à forte dose'),('G','G-CSF')], 'Schéma FLAG (fludarabine, cytarabine, G-CSF)', 'Schéma de chimiothérapie cité dans des cas rapportés de LALA avec le vénétoclax, hors étiquette.', 'c95-hors-etiquette')
d('FLAG-Ida', [('FLAG','Fludarabine, cytarabine, G-CSF'),('Ida','Idarubicine')], 'Schéma FLAG avec idarubicine', 'Variante du schéma FLAG citée dans des cas rapportés de LALA avec le vénétoclax.', 'c95-hors-etiquette')
d('RC', [('R','Rémission'),('C','Complète')], 'Rémission complète', 'Réponse définie par le protocole. Critères LMA ELN : blastes médullaires <5 %, absence de blastes sanguins et maladie extramédullaire, neutrophiles ≥1 G/L et plaquettes ≥100 G/L ; ne signifie pas MRD négative.', 'c95-rc')
d('RC1', [('RC','Rémission Complète'),('1','première')], 'Première rémission complète', 'Première rémission complète ; moment de discussion d’allogreffe chez certains adultes éligibles, selon biologie, réponse, risques et préférences.', 'c95-ebmt')
d('RCh', [('RC','Rémission Complète'),('h','avec récupération hématologique partielle')], 'Rémission complète avec récupération hématologique partielle', 'Catégorie de réponse LMA ELN avec récupération des numérations distincte de la RC ; critères exacts à vérifier dans le protocole utilisé.', 'c95-rc')
d('RCi', [('RC','Rémission Complète'),('i','avec récupération hématologique incomplète')], 'Rémission complète avec récupération hématologique incomplète', 'Catégorie de réponse LMA ELN avec récupération des numérations distincte de la RC ; critères exacts à vérifier dans le protocole utilisé.', 'c95-rc')
d('MLFS', [('M','Morphologic'),('L','Leukemia-'),('F','Free'),('S','State')], 'État sans leucémie morphologique', 'Statut de réponse défini par Onkopedia (critères ELN).', 'c95-rc')
d('MRD', [('M','Measurable'),('R','Residual'),('D','Disease')], 'Maladie résiduelle mesurable', 'Maladie détectable par une méthode sensible ; préciser cible, échantillon, sensibilité et moment. Négative ne signifie pas absence absolue de maladie.', 'c95-mrd')
d('ITK', [('I','Inhibiteur de'),('T','Tyrosine'),('K','Kinase')], 'Inhibiteur de tyrosine kinase', 'Médicament qui bloque l’activité kinase de BCR::ABL1 ; imatinib et ponatinib sont des ITK.', 'c95-bcrabl1')
d('T315I', [('T','Thréonine'),('315','en position 315'),('I','remplacée par une Isoleucine')], 'Mutation T315I de la kinase ABL1', 'Mutation qui rend inefficaces plusieurs ITK ; le ponatinib est indiqué dans la LLA Ph+ avec cette mutation.', 'c95-d-ponatinib')
d('CIVD', [('C','Coagulation'),('I','Intra'),('V','Vasculaire'),('D','Disséminée')], 'Coagulation intravasculaire disséminée', 'Consommation de facteurs de coagulation avec saignements ; complication des leucémies, urgence si décompensée.', 'c95-civd')
d('FISH', [('F','Fluorescence'),('I','In'),('S','Situ'),('H','Hybridization')], 'Hybridation in situ en fluorescence', 'Technique qui repère un réarrangement chromosomique à l’aide d’une sonde fluorescente.', 'c95-fgfr1')
for k,lit,full in [
 ('CD10',[('CD','Cluster de Différenciation'),('10','numéro 10')],'Cluster de différenciation 10'),
 ('CD11c',[('CD','Cluster de Différenciation'),('11c','numéro 11c')],'Cluster de différenciation 11c'),
 ('CD14',[('CD','Cluster de Différenciation'),('14','numéro 14')],'Cluster de différenciation 14'),
 ('CD22',[('CD','Cluster de Différenciation'),('22','numéro 22')],'Cluster de différenciation 22'),
 ('CD34',[('CD','Cluster de Différenciation'),('34','numéro 34')],'Cluster de différenciation 34'),
 ('CD64',[('CD','Cluster de Différenciation'),('64','numéro 64')],'Cluster de différenciation 64'),
 ('CD79a',[('CD','Cluster de Différenciation'),('79a','numéro 79a')],'Cluster de différenciation 79a'),
 ('CD123',[('CD','Cluster de Différenciation'),('123','numéro 123')],'Cluster de différenciation 123')]:
    d(k,lit,full,'Marqueur de surface ou intracellulaire utilisé en cytométrie en flux pour attribuer une lignée ou reconnaître un phénotype.','c95-cytometrie')
d('TdT', [('T','Terminal'),('d','deoxynucleotidyl'),('T','Transferase')], 'Désoxynucléotidyl transférase terminale', 'Enzyme utilisée comme marqueur d’immaturité ; son absence n’exclut pas à elle seule une LAI. Le panel complet et la génétique sont nécessaires.', 'c95-lai')
d('TCL1', [('T','T-Cell'),('L','Leukemia/lymphoma'),('1','numéro 1')], 'Protéine T-cell leukemia/lymphoma 1', 'Marqueur évoqué avec le CD4, le CD56 et le CD123 dans la néoplasie à cellules dendritiques plasmacytoïdes blastiques.')
for k,lit,full,ref in [
 ('BCR',[('B','Breakpoint'),('C','Cluster'),('R','Region')],'Gène de la région de regroupement des points de cassure','c95-bcrabl1'),
 ('ABL1',[('ABL','Abelson (homologue de l’oncogène viral de la leucémie murine)'),('1','numéro 1')],'Gène ABL1 (tyrosine kinase)','c95-bcrabl1'),
 ('KMT2A',[('K','lysine (symbole K)'),('M','Méthyl'),('T','Transférase'),('2A','2A')],'Gène de la lysine méthyltransférase 2A','c95-kmt2a'),
 ('ZNF384',[('ZNF','Zinc Finger (doigt de zinc)'),('384','numéro 384')],'Gène à doigt de zinc 384','c95-znf384'),
 ('BCL11B',[('BCL','B-Cell Lymphoma (lymphome B)'),('11B','numéro 11B')],'Gène du lymphome B 11B','c95-bcl11b'),
 ('FGFR1',[('F','Fibroblast'),('G','Growth'),('F','Factor'),('R','Receptor'),('1','numéro 1')],'Récepteur 1 du facteur de croissance des fibroblastes','c95-fgfr1'),
 ('ASXL1',[('A','Additional'),('S','Sex'),('X','combs'),('L','Like'),('1','numéro 1')],'Gène ASXL1 (mutation liée à la myélodysplasie)','c95-exclusion'),
 ('RUNX1',[('RUNX','RUNt-related transcription factor'),('1','numéro 1')],'Gène du facteur de transcription apparenté à Runt 1','c95-exclusion'),
 ('TP53',[('TP','Tumor Protein'),('53','p53')],'Gène de la protéine tumorale p53','c95-exclusion'),
 ('PML',[('P','Pro'),('M','Myelocytic'),('L','Leukemia')],'Gène de la leucémie promyélocytaire','c95-civd'),
 ('RARA',[('R','Retinoic'),('A','Acid'),('R','Receptor'),('A','Alpha')],'Gène du récepteur alpha de l’acide rétinoïque','c95-civd'),
 ('CBFB',[('C','Core'),('B','Binding'),('F','Factor'),('B','subunit Beta')],'Gène de la sous-unité bêta du facteur de liaison au cœur','c95-exclusion'),
 ('RUNX1T1',[('RUNX1','RUNX1'),('T1','Translocation partner 1')],'Gène partenaire de translocation de RUNX1','c95-exclusion'),
 ('BCOR',[('B','BCL6'),('COR','COrepressor')],'Gène du corépresseur de BCL6','c95-exclusion'),
 ('EZH2',[('E','Enhancer'),('Z','of Zeste'),('H','Homolog'),('2','numéro 2')],'Gène homologue 2 de l’activateur de Zeste','c95-exclusion'),
 ('SF3B1',[('SF','Splicing Factor'),('3B1','3B sous-unité 1')],'Gène du facteur d’épissage 3B1','c95-exclusion'),
 ('SRSF2',[('SRSF','Serine/aRginine-rich Splicing Factor'),('2','numéro 2')],'Gène du facteur d’épissage riche en sérine et arginine 2','c95-exclusion'),
 ('STAG2',[('STAG','STromal Antigen'),('2','numéro 2')],'Gène de l’antigène stromal 2','c95-exclusion'),
 ('U2AF1',[('U2','U2 small nuclear RNA'),('AF','Auxiliary Factor'),('1','numéro 1')],'Gène du facteur auxiliaire 1 de l’ARN nucléaire U2','c95-exclusion'),
 ('ZRSR2',[('ZRSR','Zinc finger CCCH-type, RNA binding motif and Serine/aRginine-rich'),('2','numéro 2')],'Gène ZRSR2 (mutation liée à la myélodysplasie)','c95-exclusion')]:
    d(k,lit,full,'Gène cité par les sources lues dans le bilan génétique des leucémies aiguës ; voir la fenêtre pour sa place dans le diagnostic.',ref)
