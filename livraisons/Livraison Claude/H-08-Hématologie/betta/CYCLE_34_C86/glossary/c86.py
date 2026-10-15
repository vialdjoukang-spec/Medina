"""Abréviations C86 ; ajouts conditionnels, sans mutation des glossaires existants (modèle glossary/n17.py)."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'c86', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}


def L(spec):
    """'E=Epstein;B=Barr' -> [['E','Epstein'],['B','Barr']]"""
    out = []
    for part in spec.split(';'):
        k, v = part.split('=', 1)
        out.append([k.strip(), v.strip()])
    return out


def add(key, spec, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': L(spec), 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}


# --- Familles et entités -----------------------------------------------------
add('PTCL', 'P=Peripheral;T=T-;CL=Cell Lymphoma', 'Lymphome T périphérique (Peripheral T-Cell Lymphoma)',
    'Lymphome agressif dont les cellules ont le phénotype de lymphocytes T post-thymiques matures ou de cellules NK, nodal ou extranodal.', 'c86-famille')
add('PTCL-NOS', 'PTCL=Peripheral T-Cell Lymphoma;NOS=Not Otherwise Specified (sans autre spécification)', 'Lymphome T périphérique sans autre spécification',
    'Lymphome T périphérique qui ne relève d’aucune entité plus précise de la classification. Il est l’un des sous-types les plus fréquents en Europe.', 'c86-chop')
add('ENKTL', 'E=Extranodal;NK=Natural Killer;T=T-;CL=Cell Lymphoma', 'Lymphome extranodal NK/T',
    'Entité correspondant au sous-code C86.0 ; l’EBV est présent dans les cellules tumorales.', 'c86-enktl')
add('HSTL', 'H=Hepato;S=Spleno;T=T-;CL=Cell Lymphoma', 'Lymphome T hépatosplénique (Hepatosplenic T-Cell Lymphoma)',
    'Entité correspondant au sous-code C86.1 : splénomégalie, hépatomégalie, atteinte médullaire presque constante, sans adénopathie.', 'c86-hstl')
add('EATL', 'E=Enteropathy;A=Associated;T=T-;CL=Cell Lymphoma', 'Lymphome T associé à une entéropathie (Enteropathy-Associated T-Cell Lymphoma)',
    'Entité correspondant au sous-code C86.2, issue le plus souvent d’une maladie cœliaque réfractaire.', 'c86-eatl')
add('MEITL', 'M=Monomorphic;E=Epitheliotropic;I=Intestinal;T=T-;CL=Cell Lymphoma', 'Lymphome T intestinal épithéliotrope monomorphe',
    'Entité séparée de l’EATL, sans lien avec la maladie cœliaque, à mutations SETD2 et JAK3/STAT5B.', 'c86-eatl')
add('SPTCL', 'S=Subcutaneous;P=Panniculitis-like;T=T-;CL=Cell Lymphoma', 'Lymphome T sous-cutané de type panniculite',
    'Entité correspondant au sous-code C86.3, réservée au phénotype alpha-bêta.', 'c86-sptcl')
add('BPDCN', 'B=Blastic;P=Plasmacytoid;D=Dendritic;C=Cell;N=Neoplasm', 'Néoplasme blastique à cellules dendritiques plasmacytoïdes',
    'Entité correspondant au sous-code C86.4, dérivée des précurseurs des cellules dendritiques plasmacytoïdes.', 'c86-bpdcn')
add('nTFHL-AI', 'n=nodal;TFH=T Follicular Helper;L=Lymphoma;AI=Angio-Immunoblastic (type angio-immunoblastique)', 'Lymphome T folliculaire helper nodal, type angio-immunoblastique',
    'Entité correspondant au sous-code C86.5, nouveau nom de l’ancien AITL.', 'c86-ntfh')
add('AITL', 'A=Angio;I=Immunoblastic;T=T-;L=Lymphoma', 'Lymphome T angio-immunoblastique (ancien nom)',
    'Ancien nom du nTFHL-AI dans la classification de l’OMS avant sa 5e édition.', 'c86-ntfh')
add('LyP', 'Ly=Lymphomatoid;P=Papulosis', 'Papulose lymphomatoïde (Lymphomatoid Papulosis)',
    'Prolifération lymphoïde T cutanée CD30 positive, à papules récidivantes qui régressent seules ; survie spécifique à cinq ans de 99 %.', 'c86-cd30')
add('pcALCL', 'pc=primary cutaneous;A=Anaplastic;L=Large;C=Cell;L=Lymphoma', 'Lymphome anaplasique à grandes cellules cutané primitif',
    'Prolifération T cutanée CD30 positive à nodule solitaire ou groupé ; relève du sous-code C86.6.', 'c86-cd30')
add('ALCL', 'A=Anaplastic;L=Large;C=Cell;L=Lymphoma', 'Lymphome anaplasique à grandes cellules',
    'Lymphome T dont les cellules expriment CD30. Systémique, il relève de C84.6 (ALK positif) ou C84.7 (ALK négatif) ; cutané primitif, de C86.6.', 'c86-cd30')
add('BIA-ALCL', 'BIA=Breast Implant-Associated;ALCL=Anaplastic Large Cell Lymphoma', 'Lymphome anaplasique à grandes cellules associé à un implant mammaire',
    'Entité distincte, hors du code C86.', 'c86-classif')
add('TFH', 'T=T-;F=Follicular;H=Helper', 'Lymphocyte T folliculaire helper',
    'Lymphocyte exprimant CD10, BCL6, PD1, ICOS et CXCL13.', 'c86-tfh')
add('SLH', 'S=Syndrome;L=d’activation Lympho-;H=Histiocytaire', 'Syndrome d’activation lymphohistiocytaire',
    'Emballement immunitaire, complication fréquente des lymphomes T agressifs ; 17 % des SPTCL alpha-bêta.', 'c86-slh')
add('HLH-2004', 'HLH=HemophagocyticLymphoHistiocytosis (lymphohistiocytose hémophagocytaire);2004=année de publication des critères', 'Critères HLH-2004',
    'Critères diagnostiques du syndrome d’activation lymphohistiocytaire ; non lus dans le dossier de sources de ce cours.', 'c86-slh')
add('RCD-II', 'RCD=Refractory Coeliac Disease (maladie cœliaque réfractaire);II=type II', 'Maladie cœliaque réfractaire de type II',
    'Villosités atrophiques malgré un régime sans gluten strict de plus de 12 mois et lymphocytes intraépithéliaux aberrants supérieurs à 20 %.', 'c86-rcd')
add('LEMP', 'L=Leuco-;E=Encéphalopathie;M=Multifocale;P=Progressive', 'Leucoencéphalopathie multifocale progressive',
    'Complication neurologique décrite dans l’information professionnelle suisse du brentuximab védotine.', 'c86-bv')
add('SMD', 'S=Syndrome;M=Myélo-;D=Dysplasique', 'Syndrome myélodysplasique', 'Diagnostic différentiel du HSTL, car la dysmyélopoïèse médullaire peut le simuler.', 'c86-hstl')
add('SNC', 'S=Système;N=Nerveux;C=Central', 'Système nerveux central', 'Siège possible de l’atteinte dans l’ENKTL et le BPDCN.', 'c86-tep')

# --- Codes CIM -----------------------------------------------------------------
for code, txt, win in [
    ('C86.0', 'lymphome extranodal à cellules T/NK, type nasal', 'c86-enktl'),
    ('C86.1', 'lymphome hépatosplénique à cellules T', 'c86-hstl'),
    ('C86.2', 'lymphome à cellules T de type entéropathique', 'c86-eatl'),
    ('C86.3', 'lymphome sous-cutané à cellules T de type panniculite', 'c86-sptcl'),
    ('C86.4', 'lymphome blastique à cellules NK (néoplasme blastique à cellules dendritiques plasmacytoïdes)', 'c86-bpdcn'),
    ('C86.5', 'lymphome angio-immunoblastique à cellules T', 'c86-ntfh'),
    ('C86.6', 'syndrome lymphoprolifératif cutané primitif à cellules T, CD30 positif', 'c86-cd30'),
    ('C84.5', 'autres lymphomes à cellules T/NK matures', 'c86-famille'),
    ('C84.6', 'lymphome anaplasique à grandes cellules, ALK positif', 'c86-cd30'),
    ('C84.7', 'lymphome anaplasique à grandes cellules, ALK négatif', 'c86-cd30'),
]:
    add(code, code + '=code de la CIM-10-GM 2024', 'Code ' + code + ' de la CIM-10-GM 2024', 'Code de la CIM-10-GM 2024 : ' + txt + '.', win)
add('C86.x', 'C86.x=n’importe quel sous-code de C86.0 à C86.6', 'Sous-code quelconque de C86', 'Désigne l’un des sept sous-codes C86.0 à C86.6.', 'c86-famille')
add('H-08-Hématologie', 'H=Hématologie (initiale de la spécialité);08=ordre de production;Hématologie=nom littéral du fragment', 'Fragment H-08-Hématologie',
    'Libellé du fragment selon organisation/fragments.json : initiale de spécialité, ordre de production, nom littéral.', 'c86-famille')

# --- Virus, protéines, gènes --------------------------------------------------
add('EBV', 'E=Epstein;B=Barr;V=Virus', 'Virus d’Epstein-Barr', 'Virus présent dans pratiquement toutes les cellules tumorales de l’ENKTL, en latence II.', 'c86-ebv')
add('EBER', 'EB=Epstein-Barr virus;E=Encoded;R=small RNAs (petits ARN codés)', 'ARN codés par le virus d’Epstein-Barr',
    'Marqueur d’hybridation in situ qui montre le virus dans les cellules tumorales ; critère de l’ENKTL.', 'c86-ebv')
add('LMP1', 'L=Latent;M=Membrane;P=Protein;1=numéro 1', 'Protéine membranaire latente 1 du virus d’Epstein-Barr', 'Oncoprotéine exprimée par les cellules de l’ENKTL en latence II.', 'c86-ebv')
add('TIA1', 'T=T-cell;I=Intracellular;A=Antigen;1=numéro 1', 'Antigène intracellulaire de cellule T 1', 'Protéine des granules cytotoxiques des cellules NK.', 'c86-pgp')
add('HAVCR2', 'H=Hepatitis;A=A;V=Virus;C=Cellular;R=Receptor;2=numéro 2', 'Gène du récepteur cellulaire 2 du virus de l’hépatite A', 'Gène qui code TIM-3 ; ses variants de perte de fonction sont retrouvés dans environ 60 % des SPTCL.', 'c86-havcr2')
add('TIM-3', 'T=T-cell;I=Immunoglobulin;M=Mucin-domain;3=containing 3', 'Protéine à domaines immunoglobuline et mucine des cellules T, numéro 3', 'Protéine codée par HAVCR2 ; son défaut d’expression membranaire entretient une activation immunitaire persistante.', 'c86-havcr2')
add('TET2', 'TET=Ten-Eleven Translocation;2=numéro 2', 'Gène Ten-Eleven Translocation 2', 'Gène muté tôt, dans la cellule souche hématopoïétique, dans le nTFHL-AI.', 'c86-tfh')
add('DNMT3A', 'DNMT=DNA MethylTransferase (ADN méthyltransférase);3=numéro 3;A=alpha', 'Gène de l’ADN méthyltransférase 3 alpha', 'Gène muté tôt, dans la cellule souche hématopoïétique, dans le nTFHL-AI.', 'c86-tfh')
add('RHOA', 'RHO=Ras Homolog family;A=membre A', 'Gène du membre A de la famille des homologues Ras', 'Gène porteur de la mutation G17V dans la cellule TFH tumorale (jusqu’à 80 % des nTFHL-AI).', 'c86-tfh')
add('G17V', 'G=glycine;17=position 17;V=remplacée par la valine', 'Mutation glycine 17 valine', 'Notation d’une substitution d’acide aminé : la glycine en position 17 est remplacée par la valine.', 'c86-tfh')
add('IDH2', 'IDH=Isocitrate DeHydrogenase;2=numéro 2', 'Gène de l’isocitrate déshydrogénase 2', 'Gène muté (R172) dans environ un tiers des nTFHL-AI.', 'c86-tfh')
add('R172', 'R=arginine;172=position 172', 'Mutation en position arginine 172', 'Notation de la mutation d’IDH2 : l’arginine en position 172 est modifiée.', 'c86-tfh')
add('JAK1', 'JAK=Janus Kinase;1=numéro 1', 'Janus kinase 1', 'Gène muté, avec STAT3, dans l’EATL.', 'c86-eatl')
add('JAK3', 'JAK=Janus Kinase;3=numéro 3', 'Janus kinase 3', 'Gène muté, avec STAT5B, dans le MEITL.', 'c86-eatl')
add('STAT5B', 'STAT=Signal Transducer and Activator of Transcription;5B=numéro 5B', 'Transducteur de signal et activateur de transcription 5B', 'Gène muté, avec JAK3, dans le MEITL.', 'c86-eatl')
add('SETD2', 'SET=Su(var)3-9, Enhancer-of-zeste, Trithorax;D2=Domain containing 2', 'Gène contenant le domaine SET 2', 'Gène muté dans le MEITL.', 'c86-eatl')
add('DUSP22-IRF4', 'DUSP22=Dual Specificity Phosphatase 22;IRF4=Interferon Regulatory Factor 4', 'Réarrangement DUSP22-IRF4', 'Réarrangement retrouvé dans environ 25 % des pcALCL.', 'c86-cd30')
add('BCL6', 'BCL=B-Cell Lymphoma;6=numéro 6', 'Lymphome B 6', 'Marqueur des cellules TFH.', 'c86-tfh')
add('PD1', 'PD=Programmed cell Death;1=protein 1', 'Protéine de mort cellulaire programmée 1', 'Marqueur des cellules TFH.', 'c86-tfh')
add('ICOS', 'ICOS=Inducible T-cell COStimulator', 'Costimulateur inductible des cellules T', 'Marqueur des cellules TFH.', 'c86-tfh')
add('CXCL13', 'CXCL=C-X-C motif chemokine Ligand;13=numéro 13', 'Ligand 13 de chimiokine à motif C-X-C', 'Marqueur des cellules TFH.', 'c86-tfh')
add('TCL1', 'TCL=T-Cell Leukemia/lymphoma;1=numéro 1', 'Leucémie/lymphome T 1', 'Marqueur du BPDCN.', 'c86-bpdcn')
add('BET', 'BET=Bromodomain and Extra-Terminal domain', 'Bromodomaine et domaine extra-terminal', 'Famille de protéines visée par des inhibiteurs en investigation dans le BPDCN.', 'c86-tagra')
add('p.Ile97Met', 'p.=protéine;Ile=isoleucine;97=position 97;Met=remplacée par la méthionine', 'Variant isoleucine 97 méthionine de TIM-3', 'Variant de HAVCR2 prédominant chez les patients d’ascendance européenne.', 'c86-havcr2')
add('p.Tyr82Cys', 'p.=protéine;Tyr=tyrosine;82=position 82;Cys=remplacée par la cystéine', 'Variant tyrosine 82 cystéine de TIM-3', 'Variant de HAVCR2 prédominant en Asie de l’Est.', 'c86-havcr2')

# --- Marqueurs CD -----------------------------------------------------------
for n in ['2', '4', '5', '7', '8', '10', '33', '123', '303']:
    add('CD' + n, 'CD=Cluster of Differentiation (groupe de différenciation);%s=numéro attribué à l’antigène' % n,
        'Antigène CD' + n, 'Antigène de surface servant au phénotypage des cellules lymphomateuses.', 'c86-biopsie')

# --- Index, organismes, revues ------------------------------------------------
add('IPI', 'I=International;P=Prognostic;I=Index', 'Index pronostique international', 'Cinq facteurs : âge supérieur à 60 ans, LDH, ECOG de 2 à 4, stade III ou IV, plus d’un site extranodal.', 'c86-index')
add('PIT', 'P=Prognostic;I=Index for;T=T-cell lymphoma', 'Index pronostique des lymphomes T', 'Âge, état général, LDH et atteinte médullaire.', 'c86-index')
add('mPIT', 'm=modifié;PIT=Prognostic Index for T-cell lymphoma', 'Index pronostique des lymphomes T modifié', 'PIT auquel s’ajoute le Ki-67.', 'c86-index')
add('PINK', 'P=Prognostic;I=Index of;N=Natural;K=Killer lymphoma', 'Index pronostique du lymphome NK', 'Âge supérieur à 60 ans, stade III ou IV, atteinte ganglionnaire à distance, sous-type non nasal.', 'c86-index')
add('PINK-E', 'PINK=Prognostic Index of Natural Killer lymphoma;E=EBV (ADN d’EBV détectable)', 'Index PINK avec ADN d’EBV', 'PINK auquel s’ajoute un ADN d’EBV détectable.', 'c86-index')
add('ICC', 'I=International;C=Consensus;C=Classification', 'Classification consensuelle internationale 2022', 'Classification des tumeurs hématolymphoïdes largement superposable à l’OMS 5e édition.', 'c86-classif')
add('ISCL', 'I=International;S=Society for;C=Cutaneous;L=Lymphomas', 'Société internationale des lymphomes cutanés', 'Co-auteur, avec l’EORTC, de la classification TNM des lymphomes cutanés non mycosis fongoïde.', 'c86-stad-cutanee')
add('USCLC', 'U=United;S=States;C=Cutaneous;L=Lymphoma;C=Consortium', 'Consortium américain des lymphomes cutanés', 'Co-signataire du consensus de 2011 ; utilisé ici pour sa composante européenne.', 'c86-lyp-trt')
add('EORTC', 'E=European;O=Organisation for;R=Research and;T=Treatment of;C=Cancer', 'Organisation européenne pour la recherche et le traitement du cancer', 'Source de la classification OMS-EORTC et de l’étude de 83 cas de SPTCL.', 'c86-stad-cutanee')
add('EHA', 'E=European;H=Hematology;A=Association', 'Association européenne d’hématologie', 'Co-auteur, avec l’ESMO, de la recommandation de 2025.', 'c86-famille')
add('DGHO', 'D=Deutsche;G=Gesellschaft für;H=Hämatologie und;O=Onkologie', 'Société allemande d’hématologie et d’oncologie médicale', 'Co-éditrice d’Onkopedia.', 'c86-famille')
add('OeGHO', 'Oe=Österreichische;G=Gesellschaft für;H=Hämatologie und;O=Onkologie', 'Société autrichienne d’hématologie et d’oncologie médicale', 'Co-éditrice d’Onkopedia.', 'c86-famille')
add('SGMO', 'S=Schweizerische;G=Gesellschaft für;M=Medizinische;O=Onkologie', 'Société suisse d’oncologie médicale', 'Co-éditrice d’Onkopedia.', 'c86-famille')
add('SZO', 'S=Schweizer;Z=Zeitschrift für;O=Onkologie', 'Revue suisse d’oncologie', 'Revue qui a publié, en 2021, la seule synthèse suisse sur le traitement des lymphomes T lue dans ce cours.', 'c86-famille')
add('NICER', 'N=National;I=Institute for;C=Cancer;E=Epidemiology and;R=Registration', 'Institut national pour l’épidémiologie et l’enregistrement du cancer', 'Registre dont les données sont citées par la revue SZO 2021.', 'c86-famille')
add('GTIN', 'G=Global;T=Trade;I=Item;N=Number', 'Numéro mondial d’article commercial', 'Identifiant du produit dans la base des informations professionnelles suisses.', 'c86-statut-ch')
add('HemaSphere', 'HemaSphere=nom propre d’une revue, non une abréviation', 'HemaSphere', 'Revue de l’Association européenne d’hématologie.', 'c86-famille')

# --- Schémas et traitements ---------------------------------------------------
add('CHOP', 'C=Cyclophosphamide;H=doxorubicine (Hydroxydaunorubicine);O=vincristine (Oncovin);P=Prednisone', 'Cyclophosphamide, doxorubicine, vincristine, prednisone',
    'Schéma de référence des lymphomes T périphériques ; inefficace dans l’ENKTL.', 'c86-chop')
add('CHOEP', 'CHOP=Cyclophosphamide, doxorubicine, vincristine, prednisone;E=Étoposide', 'CHOP avec étoposide', 'Variante du CHOP à laquelle l’étoposide est ajouté ; le développement de la lettre E est usuel et non précisé par les sources lues.', 'c86-chop')
add('CHP', 'C=Cyclophosphamide;H=doxorubicine (Hydroxydaunorubicine);P=Prednisone', 'Cyclophosphamide, doxorubicine, prednisone', 'CHOP sans vincristine, associé au brentuximab védotine dans le BV-CHP.', 'c86-chop')
add('BV', 'BV=Brentuximab Védotine', 'Brentuximab védotine', 'Médicament dirigé contre CD30 (Adcetris).', 'c86-bv')
add('BV-CHP', 'BV=Brentuximab Védotine;CHP=Cyclophosphamide, doxorubicine, prednisone', 'Brentuximab védotine plus CHP', 'Schéma sans vincristine, évalué dans l’étude ECHELON-2.', 'c86-bv')
add('ECHELON-2', 'ECHELON-2=nom d’essai, non développable lettre à lettre', 'Étude ECHELON-2', 'Essai comparant le BV-CHP au CHOP dans le lymphome T périphérique CD30 positif.', 'c86-chop')
add('CHOP-like', 'CHOP=Cyclophosphamide, doxorubicine, vincristine, prednisone;like=du type de', 'Schéma de type CHOP', 'Schémas voisins du CHOP, proposés au patient fragile atteint d’EATL.', 'c86-eatl')
add('ICE', 'I=Ifosfamide;C=Carboplatine;E=Étoposide', 'Ifosfamide, carboplatine, étoposide', 'Schéma préféré dans le HSTL (IV, B) ; développement usuel du sigle, non détaillé par les sources lues.', 'c86-ice')
add('IVE', 'IVE=sigle de schéma, développement non établi par les sources lues', 'Schéma IVE', 'Schéma alterné avec du méthotrexate à dose intermédiaire dans l’EATL.', 'c86-eatl')
add('DDGP', 'DDGP=sigle de schéma, développement non établi par les sources lues', 'Schéma DDGP', 'Schéma à base d’asparaginase pour l’ENKTL de stade III–IV chez le patient éligible à la greffe.', 'c86-asp')
add('SMILE', 'SMILE=sigle de schéma, développement non établi par les sources lues', 'Schéma SMILE', 'Schéma à base d’asparaginase : réponse globale de 81 % et survie à cinq ans de 50 %.', 'c86-asp')
add('mSMILE', 'm=modifié;SMILE=sigle de schéma, développement non établi par les sources lues', 'Schéma SMILE modifié', 'Variante du SMILE pour l’ENKTL de stade III–IV chez le patient éligible à la greffe.', 'c86-asp')
add('AspaMetDex', 'AspaMetDex=sigle de schéma, développement non établi par les sources lues', 'Schéma AspaMetDex', 'Schéma à base d’asparaginase pour l’ENKTL chez le patient non éligible à la greffe.', 'c86-asp')
add('P-GemOx', 'P-GemOx=sigle de schéma, développement non établi par les sources lues', 'Schéma P-GemOx', 'Schéma à base d’asparaginase pour l’ENKTL chez le patient non éligible à la greffe.', 'c86-asp')
add('DeVIC', 'DeVIC=sigle de schéma, développement non établi par les sources lues', 'Schéma DeVIC', 'Chimiothérapie associée à 50–56 Gy de radiothérapie dans l’ENKTL (rémission complète 77 %).', 'c86-rt')
add('non-CHOP', 'non=autre que;CHOP=Cyclophosphamide, doxorubicine, vincristine, prednisone', 'Schéma autre que le CHOP', 'Désigne les schémas plus intensifs que le CHOP dans la méta-analyse du HSTL.', 'c86-ice')
add('ISRT', 'I=Involved;S=Site;R=Radiation;T=Therapy', 'Radiothérapie de site impliqué', 'Technique utilisée à 30–40 Gy dans le nTFHL-AI limité.', 'c86-rt')
add('PUVA', 'P=Psoralène;UVA=Ultraviolets de type A', 'Photochimiothérapie PUVA', 'Rémission complète 26 %, rechute 84 % dans la papulose lymphomatoïde.', 'c86-lyp-trt')
add('RC', 'R=Rémission;C=Complète', 'Rémission complète', 'Disparition de toute maladie détectable.', 'c86-lyp-trt')
add('RCc', 'R=Rémission;C=Complète;c=suffixe défini par l’information professionnelle, non développé dans le dossier lu', 'Rémission complète, sous-catégorie c', 'Utilisée avec RC pour exprimer la réponse au tagraxofusp (56,9 % chez 65 patients).', 'c86-tagra')
