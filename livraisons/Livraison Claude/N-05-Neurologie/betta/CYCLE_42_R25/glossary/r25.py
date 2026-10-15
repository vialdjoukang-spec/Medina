"""Abréviations R25 — ajouts conditionnels, sans écraser un terme déjà défini ailleurs."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'r25', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def a(key, lit, full, definition, ref=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in lit], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': ref}

def code(key, label, ref='r25-codage'):
    a(key, [(key[0], 'Lettre du chapitre de la CIM-10-GM'), (key[1:], 'numéro de catégorie et de sous-code')], 'Code CIM-10-GM ' + key,
      'Code de la classification CIM-10-GM 2024 : ' + label + '.', ref)

a('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies',
  'Classification de l’Organisation mondiale de la santé. Le catalogue du dépôt suit la CIM-10-GM 2024 ; la correspondance avec la CIM-11 n’est pas établie.', 'r25-codage')
a('XVIII', [('XVIII', 'dix-huitième chapitre (en chiffres romains) de la CIM-10-GM')], 'Chapitre XVIII de la CIM-10-GM',
  'Chapitre de la CIM-10-GM 2024 qui contient la catégorie de symptômes R25. Le cours en retient que R25 décrit un symptôme et non une maladie.', 'r25-codage')
code('R25.0', 'mouvements anormaux de la tête')
code('R25.1', 'tremblement, sans précision')
code('R25.2', 'crampe et spasme')
code('R25.3', 'fasciculation')
code('R25.8', 'mouvements involontaires anormaux, autres et non précisés')
code('G25.0', 'tremblement essentiel, exclu de R25.1')
code('G25.2', 'tremblement intentionnel, exclu de R25.1')
code('G25.5', 'chorée sans précision, exclue de R25.1')
code('R29.0', 'spasmes carpopédaux, exclus de R25.2')
code('G40.4', 'spasmes infantiles, exclus de R25.2')
code('F44.4', 'tremblement hystérique, exclu de R25.1')
code('F98.4', 'stéréotypies motrices, exclues de R25')
a('SGSSC', [('SGSSC', 'sigle de la société savante suisse du sommeil citée par la ligne directrice ; son développement n’est pas donné par les sources lues')], 'Société suisse du sommeil citée par la ligne directrice',
  'Société qui a approuvé, avec la Société suisse de neurologie, la ligne directrice sur le syndrome des jambes sans repos.', 'r25-sjsr')
a('CASPR2', [('CASPR', 'Contactin-ASsociated PRotein (protéine associée à la contactine)'), ('2', 'numéro de la protéine de la famille')], 'Contactin-associated protein-like 2',
  'Protéine de la membrane des axones. Les anticorps qui la ciblent sont directement pathogènes et définissent un spectre d’hyperexcitabilité nerveuse.', 'r25-caspr2')
a('anti-CASPR2', [('anti-', 'dirigé contre'), ('CASPR2', 'Contactin-associated protein-like 2')], 'Anticorps dirigé contre CASPR2',
  'Anticorps à doser devant une hyperexcitabilité nerveuse périphérique auto-immune, de préférence aux anciens anticorps « VGKC ».', 'r25-caspr2')
a('LGI1', [('LGI', 'Leucine-rich Glioma-Inactivated (riche en leucine, inactivé dans le gliome)'), ('1', 'numéro de la protéine')], 'Leucine-rich glioma-inactivated 1',
  'Protéine cible d’anticorps à doser avec CASPR2 dans les syndromes d’hyperexcitabilité nerveuse.', 'r25-caspr2')
a('anti-LGI1', [('anti-', 'dirigé contre'), ('LGI1', 'Leucine-rich glioma-inactivated 1')], 'Anticorps dirigé contre LGI1',
  'Anticorps à doser avec les anticorps anti-CASPR2 plutôt que les anticorps « VGKC ».', 'r25-caspr2')
a('VGKC', [('V','Voltage'),('G','Gated'),('K','Potassium (symbole K)'),('C','Channel')], 'Voltage-gated potassium channel (canal potassique voltage-dépendant)',
  'Ancienne cible des anticorps de l’hyperexcitabilité nerveuse. Les sources lues recommandent de doser plutôt CASPR2 et LGI1.', 'r25-caspr2')
a('anti-VGKC', [('anti-', 'dirigé contre'), ('VGKC', 'Voltage-gated potassium channel')], 'Anticorps dirigé contre les canaux potassiques voltage-dépendants',
  'Présent dans un tiers des syndromes crampes-fasciculations, avec les anticorps anti-CASPR2.', 'r25-caspr2')
a('GABAergique', [('GABA', 'Gamma-AminoButyric Acid (acide gamma-aminobutyrique)'), ('ergique', 'qui agit par ce neurotransmetteur')], 'Qui agit par l’acide gamma-aminobutyrique',
  'Se dit d’un neurone ou d’une synapse inhibitrice qui utilise le GABA.', 'r25-myoclonie')
a('GABAergiques', [('GABA', 'Gamma-AminoButyric Acid (acide gamma-aminobutyrique)'), ('ergiques', 'qui agissent par ce neurotransmetteur (pluriel)')], 'Qui agissent par l’acide gamma-aminobutyrique',
  'Se dit des interneurones inhibiteurs dont la dysfonction est liée à la myoclonie corticale.', 'r25-myoclonie')
a('HANAC', [('H','Hereditary'),('A','Angiopathy with'),('N','Nephropathy,'),('A','Aneurysms and muscle'),('C','Cramps')], 'Hereditary angiopathy with nephropathy, aneurysms and muscle cramps',
  'Syndrome héréditaire cité par la ligne directrice parmi les causes génétiques de crampes.', 'r25-med-crampes')
a('McArdle', [('McArdle', 'nom propre du médecin qui a décrit la maladie ; ce n’est pas une abréviation')], 'Maladie de McArdle',
  'Maladie citée par la ligne directrice parmi les causes génétiques de crampes et de contracture myogène.', 'r25-myopathie')
a('RFC1', [('RFC', 'Replication Factor C (facteur de réplication C)'), ('1', 'sous-unité numéro 1')], 'Replication factor C subunit 1',
  'Gène dont de rares mutations ont été décrites dans le syndrome crampes-fasciculations.', 'r25-caspr2')
a('DaT', [('Da', 'Dopamine'), ('T', 'Transporter (transporteur)')], 'Transporteur de la dopamine',
  'Cible de l’imagerie DaT-SPECT, demandée en cas de doute entre un parkinsonisme et un tremblement fonctionnel.', 'r25-fonctionnel')
a('fT3', [('f','free (libre)'),('T3','triiodothyronine')], 'Triiodothyronine libre', 'Hormone thyroïdienne dosée dans le bilan élargi des crampes.', 'r25-bio-crampes')
a('fT4', [('f','free (libre)'),('T4','thyroxine')], 'Thyroxine libre', 'Hormone thyroïdienne dosée dans le bilan élargi des crampes.', 'r25-bio-crampes')
a('FAR', [('F','Faiblesse'),('A','Amyotrophie'),('R','Réflexes vifs')], 'Faiblesse, amyotrophie, réflexes vifs',
  'Aide pédagogique, non critère officiel : les trois signes à chercher devant une fasciculation.', 'r25-mnemo')
