"""Abréviations E54 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'e54', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('ESPEN', [('E', 'European'), ('S', 'Society for'), ('P', 'Parenteral and'), ('E', 'Enteral'), ('N', 'Nutrition')],
              'Société européenne de nutrition clinique et métabolisme (sigle conservé de l’ancien nom : nutrition parentérale et entérale)',
              'Cette société savante européenne a publié en 2022 des recommandations sur les micronutriments. Son chapitre sur la vitamine C fournit les seuils plasmatiques, les règles de dosage et les doses en nutrition artificielle.', 'e54-seuils')
add_if_absent('D-A-CH', [('D', 'Deutschland (Allemagne)'), ('A', 'Austria (Autriche)'), ('CH', 'Confoederatio Helvetica (Suisse)')],
              'Valeurs de référence nutritionnelles communes à l’Allemagne, à l’Autriche et à la Suisse',
              'Les sociétés de nutrition de ces trois pays publient des valeurs de référence communes, utilisées en Suisse. Elles décrivent un apport préventif chez la personne saine, non une dose thérapeutique.', 'e54-dach')
add_if_absent('DGE', [('D', 'Deutsche'), ('G', 'Gesellschaft'), ('E', 'für Ernährung (pour la nutrition)')],
              'Société allemande de nutrition',
              'Cette société est, avec l’ÖGE et la SGE, éditrice commune des valeurs de référence D-A-CH.', 'e54-dach')
add_if_absent('ÖGE', [('Ö', 'Österreichische (autrichienne)'), ('G', 'Gesellschaft'), ('E', 'für Ernährung (pour la nutrition)')],
              'Société autrichienne de nutrition',
              'Cette société est, avec la DGE et la SGE, éditrice commune des valeurs de référence D-A-CH.', 'e54-dach')
add_if_absent('SGE', [('S', 'Schweizerische (suisse)'), ('G', 'Gesellschaft'), ('E', 'für Ernährung (pour la nutrition)')],
              'Société suisse de nutrition',
              'Cette société est, avec la DGE et l’ÖGE, éditrice commune des valeurs de référence D-A-CH.', 'e54-dach')
add_if_absent('HIF-1', [('H', 'Hypoxia'), ('I', 'Inducible'), ('F', 'Factor (facteur induit par l’hypoxie)'), ('1', 'type 1')],
              'Facteur induit par l’hypoxie de type 1',
              'Ce facteur de transcription commande la réponse cellulaire à l’hypoxie. La vitamine C intervient dans sa dégradation ; son déficit pourrait favoriser un remodelage vasculaire pulmonaire, mécanisme plausible mais non démontré.', 'e54-hp')
add_if_absent('HPLC', [('H', 'High'), ('P', 'Performance (haute performance)'), ('L', 'Liquid (liquide)'), ('C', 'Chromatography (chromatographie)')],
              'Chromatographie liquide à haute performance',
              'Cette technique sépare et mesure l’acide ascorbique dans le plasma. ESPEN la retient pour l’analyse, après un prélèvement protégé de la lumière et congelé.', 'e54-preanalytique')
add_if_absent('LOVIT', [('L', 'Lessening'), ('O', 'Organ dysfunction with (dysfonction d’organe avec)'), ('VIT', 'VITamin C (vitamine C)')],
              'Essai LOVIT (vitamine C à haute dose dans le sepsis)',
              'Cet essai n’est connu dans les sources que par une mention secondaire d’origine américaine. Il relève des soins intensifs et ne fonde aucune conduite dans ce cours.', 'e54-nutrition-art')
add_if_absent('Möller-Barlow', [('Möller-Barlow', 'noms propres de deux médecins, non une abréviation')],
              'Maladie de Möller-Barlow, scorbut du nourrisson',
              'Cette expression désigne le scorbut infantile. Les informations professionnelles suisses la nomment parmi les indications de la vitamine C.', 'e54-enfants')
add_if_absent('Raynaud-Simon', [('Raynaud-Simon', 'nom propre d’un auteur, non une abréviation')],
              'Raynaud-Simon, auteur de l’étude gériatrique parisienne',
              'Cette étude de l’hôpital Bichat porte sur 145 patients gériatriques consécutifs.', 'e54-geriatrie')
