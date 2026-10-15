"""Abréviations E30 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e30', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('PPC', [('P', 'Puberté'), ('P', 'Précoce'), ('C', 'Centrale')], 'Puberté précoce centrale',
              'Activation prématurée de l’axe hypothalamo-hypophyso-gonadique, dépendante des gonadotrophines, avant 8 ans chez la fille et avant 9 ans chez le garçon.', 'e30-ppc')
add_if_absent('PPP', [('P', 'Puberté'), ('P', 'Précoce'), ('P', 'Périphérique')], 'Puberté précoce périphérique',
              'Puberté précoce indépendante des gonadotrophines : les stéroïdes sexuels viennent de la gonade, de la surrénale, d’une tumeur ou d’un apport exogène.', 'e30-ppp')
add_if_absent('GnRH', [('Gn', 'Gonadotropin (gonadotrophines)'), ('R', 'Releasing (de libération)'), ('H', 'Hormone')], 'Hormone de libération des gonadotrophines',
              'Hormone hypothalamique sécrétée de façon pulsatile ; le début de cette sécrétion marque le début de la puberté.', 'e30-gnrh')
add_if_absent('LH', [('L', 'Luteinizing (lutéinisante)'), ('H', 'Hormone')], 'Hormone lutéinisante',
              'Hormone hypophysaire qui stimule la production gonadique d’œstradiol ou de testostérone.', 'e30-lh-fsh')
add_if_absent('FSH', [('F', 'Follicle (folliculo)'), ('S', 'Stimulating (stimulante)'), ('H', 'Hormone')], 'Hormone folliculostimulante',
              'Hormone hypophysaire libérée avec la LH sous l’effet de la GnRH ; son rapport avec la LH sert dans le test de stimulation.', 'e30-lh-fsh')
add_if_absent('hCG', [('h', 'human (humaine)'), ('C', 'Chorionic (chorionique)'), ('G', 'Gonadotropin (gonadotrope)')], 'Hormone chorionique gonadotrope humaine',
              'Hormone sécrétée par certaines tumeurs (germinome, tératome, choriocarcinome, hépatoblastome), cause de puberté précoce périphérique.', 'e30-hcg')
add_if_absent('hMG', [('h', 'human (humaine)'), ('M', 'Menopausal (ménopausique)'), ('G', 'Gonadotropin (gonadotrophine)')], 'Gonadotrophine ménopausique humaine',
              'Préparation citée par la DGKED dans le test associé à l’hCG chez la fille.', 'e30-dgked')
add_if_absent('DHEAS', [('DHEA', 'Déhydroépiandrostérone'), ('S', 'Sulfate')], 'Sulfate de déhydroépiandrostérone',
              'Androgène surrénalien dosé dans le bilan d’une puberté précoce ; très élevé, il évoque un corticosurrénalome.', 'e30-adrenarche')
add_if_absent('RCCP', [('R', 'Retard'), ('C', 'Constitutionnel'), ('C', 'de Croissance'), ('P', 'et de Puberté')], 'Retard constitutionnel de croissance et de puberté',
              'Retard du rythme de maturation, diagnostic d’exclusion confirmé par l’entrée spontanée en puberté.', 'e30-rccp')
add_if_absent('DGKED', [('DG', 'Deutsche Gesellschaft (société allemande)'), ('KED', 'für Kinderendokrinologie und -diabetologie (d’endocrinologie et de diabétologie pédiatriques)')], 'Société allemande d’endocrinologie et de diabétologie pédiatriques',
              'Elle a publié en 2021, avec l’AWMF, la recommandation de consensus d’experts sur la puberté tardive et l’hypogonadisme.', 'e30-dgked')
add_if_absent('SIAMS', [('S', 'Società'), ('I', 'Italiana'), ('A', 'di Andrologia'), ('M', 'e Medicina'), ('S', 'della Sessualità')], 'Société italienne d’andrologie et de médecine de la sexualité',
              'Elle a publié en 2024 une recommandation sur les troubles andrologiques de l’enfance à la transition, qui ne concerne que les garçons.', 'e30-siams')
add_if_absent('Endo-ERN', [('Endo', 'endocrinien'), ('ERN', 'European Reference Network (réseau européen de référence)')], 'Réseau européen de référence en endocrinologie',
              'Ce réseau a publié en 2022 une recommandation sur l’induction pubertaire et la transition vers le traitement hormonal adulte.', 'e30-dgked')
add_if_absent('LA', [('L', 'Long'), ('A', 'Acting (à action prolongée)')], 'Longue action',
              'Élément du nom Pamorelin LA : formulation à libération prolongée, injectée toutes les 24 semaines.', 'e30-pamorelin')
add_if_absent('MKRN3', [('MKRN3', 'symbole officiel de gène, développement non fourni par les sources lues')], 'Gène MKRN3',
              'Gène soumis à empreinte paternelle ; ses variants à perte de fonction sont une cause monogénique fréquente de puberté précoce centrale familiale.', 'e30-genetique')
add_if_absent('DLK1', [('DLK1', 'symbole officiel de gène, développement non fourni par les sources lues')], 'Gène DLK1',
              'Gène soumis à empreinte paternelle, dont les variants à perte de fonction causent une puberté précoce centrale familiale.', 'e30-genetique')
add_if_absent('KISS1', [('KISS1', 'symbole officiel de gène, développement non fourni par les sources lues')], 'Gène KISS1',
              'Gène dont des variants à gain de fonction sont rapportés dans la puberté précoce centrale.', 'e30-genetique')
add_if_absent('KISS1R', [('KISS1R', 'symbole officiel de gène, développement non fourni par les sources lues')], 'Gène KISS1R',
              'Gène du récepteur associé à KISS1 ; des variants à gain de fonction sont rapportés dans la puberté précoce centrale.', 'e30-genetique')
add_if_absent('GNAS', [('GNAS', 'symbole officiel de gène, développement non fourni par les sources lues')], 'Gène GNAS',
              'Gène dont une mutation activatrice cause le syndrome de McCune-Albright.', 'e30-mcune')
add_if_absent('XY', [('X', 'chromosome sexuel X'), ('Y', 'chromosome sexuel Y')], 'Chromosomes sexuels X et Y',
              'Désigne la formule chromosomique masculine ; la mosaïque 45,X/46,XY est une cause d’hypogonadisme hypergonadotrope.', 'e30-hypergonado')
add_if_absent('McCune-Albright', [('McCune-Albright', 'noms des deux médecins qui ont décrit le syndrome')], 'Syndrome de McCune-Albright',
              'Cause de puberté précoce périphérique par mutation activatrice de GNAS, orientée par les taches café au lait.', 'e30-mcune')
add_if_absent('Silver-Russell', [('Silver-Russell', 'noms des deux médecins qui ont décrit le syndrome')], 'Syndrome de Silver-Russell',
              'Syndrome associé à la puberté précoce centrale dans le guide danois.', 'e30-ppc')
add_if_absent('Wyk-Grumbach', [('Wyk-Grumbach', 'second élément du nom Van Wyk-Grumbach, noms des médecins qui ont décrit le syndrome')], 'Syndrome de Van Wyk-Grumbach',
              'Association d’une hypothyroïdie profonde, d’un kyste ovarien et d’une puberté précoce.', 'e30-mcune')
add_if_absent('Testosteron-Mepha', [('Testosteron-Mepha', 'nom commercial suisse, non une abréviation')], 'Testosteron-Mepha (undécanoate de testostérone)',
              'Préparation suisse non indiquée avant la puberté.', 'e30-testomepha')
add_if_absent('ICD-10-GM', [('ICD', 'International Classification of Diseases'), ('10', 'dixième révision'), ('GM', 'German Modification (modification allemande)')], 'Classification internationale des maladies, 10e révision, modification allemande',
              'Version allemande de la classification, publiée par le BfArM, dont la version 2024 a servi à délimiter le périmètre du cours.', 'e30-dgked')
