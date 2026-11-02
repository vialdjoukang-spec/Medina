"""Abréviations I64 ; ajouts conditionnels, sans mutation des glossaires partagés."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'i64', '__init__'}:
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
add_if_absent('NFS', [('NFS', 'Numération formule sanguine')], 'Numération formule sanguine', 'Analyse des cellules sanguines ; les plaquettes participent à l’évaluation du risque hémorragique.', 'i64-anticoagulant')
add_if_absent('CEN', [('CEN', 'Collège des enseignants de neurologie')], 'Collège des enseignants de neurologie', 'Source pédagogique française dont les passages relus sont identifiés.', 'i64-imagerie')
add_if_absent('DHPC', [('DHPC', 'Direct Healthcare Professional Communication')], 'Direct Healthcare Professional Communication', 'Communication de sécurité destinée aux professionnels de santé ; celle de Konakion date de juillet 2026.', 'i64-pcc')
add_if_absent('CI', [('CI', 'Contre-indication')], 'Contre-indication', 'Situation où le produit ne doit pas être utilisé selon la FI ; distinguer une précaution.', 'i64-lyse')
add_if_absent('ECT', [('ECT', 'Ecarin clotting time')], 'Ecarin clotting time', 'Temps de coagulation à l’écarine, utilisé pour évaluer l’activité du dabigatran selon contexte.', 'i64-praxbind')
add_if_absent('FIX', [('FIX', 'Facteur IX')], 'Facteur IX', 'Facteur dont les unités servent à exprimer la dose du PCC Beriplex.', 'i64-pcc')
add_if_absent('HIT', [('HIT', 'Heparin-induced thrombocytopenia')], 'Heparin-induced thrombocytopenia', 'Thrombopénie induite par l’héparine ; antécédent à vérifier avant un produit en contenant.', 'i64-pcc')
add_if_absent('OPC', [('OPC', 'One point cut')], 'One point cut', 'Ampoule à point de rupture marqué ; respecter le geste d’ouverture et inspecter la solution.', 'i64-pcc')
add_if_absent('IAM', [('IAM', 'Infarctus aigu du myocarde')], 'Infarctus aigu du myocarde', 'Indication avec des schémas de thrombolyse différents de ceux de l’AVC.', 'i64-alteplase')
add_if_absent('EPA', [('EPA', 'Entrustable Professional Activity')], 'Entrustable Professional Activity', 'Activité professionnelle pouvant être confiée à un apprenant ; les repères PROFILES de cette leçon sont des correspondances pédagogiques.', 'i64-formation')
add_if_absent('MEBEKO', [('MEBEKO', 'Commission fédérale des professions médicales')], 'Commission fédérale des professions médicales', 'Commission fixant les exigences de l’examen fédéral suisse ; la version 2026 consultée mentionne 265 situations de départ.', 'i64-formation')
add_if_absent('AVC', [('AVC', 'Accident vasculaire cérébral')], 'Accident vasculaire cérébral', 'Atteinte neurologique d’origine vasculaire ; la nature ischémique ou hémorragique exige une évaluation clinique et radiologique.', 'i64-cim')
add_if_absent('CIM-10-GM', [('CIM-10-GM', 'Classification internationale des maladies, dixième révision, modification allemande')], 'Classification internationale des maladies, dixième révision, modification allemande', 'La version allemande 2024 relue définit I64 ; elle ne certifie pas les règles de facturation suisse 2026.', 'i64-cim')
add_if_absent('ESO', [('ESO', 'European Stroke Organisation')], 'European Stroke Organisation', 'Société européenne publiant des recommandations et synthèses sur l’AVC ; leur date et leur population restent attachées aux conclusions.', 'i64-lyse')
add_if_absent('EANS', [('EANS', 'European Association of Neurosurgical Societies')], 'European Association of Neurosurgical Societies', 'Association européenne de neurochirurgie, partenaire de la recommandation HIC 2025 consultée dans sa présentation officielle.', 'i64-hic')
add_if_absent('BfArM', [('BfArM', 'Bundesinstitut für Arzneimittel und Medizinprodukte')], 'Bundesinstitut für Arzneimittel und Medizinprodukte', 'Institut fédéral allemand publiant la CIM-10-GM consultée.', 'i64-cim')
add_if_absent('AMM', [('AMM', 'Autorisation de mise sur le marché')], 'Autorisation de mise sur le marché', 'Cadre d’autorisation d’un produit ; une recommandation clinique peut discuter une stratégie distincte, qui doit être explicitée.', 'i64-lyse')
add_if_absent('FI', [('FI', 'Information professionnelle')], 'Information professionnelle', 'Document du médicament exact : indication, dose, contre-indications, précautions, administration et surveillance.', 'i64-alteplase')
add_if_absent('NIHSS', [('NIHSS', 'National Institutes of Health Stroke Scale')], 'National Institutes of Health Stroke Scale', 'Échelle du déficit neurologique ; un faible total n’exclut pas un handicap majeur ou une atteinte postérieure.', 'i64-nihss')
add_if_absent('mRS', [('mRS', 'Modified Rankin Scale')], 'Modified Rankin Scale', 'Échelle de handicap global de 0 à 6 ; compléter par les fonctions cognitives, la fatigue et les objectifs personnels.', 'i64-mrs')
add_if_absent('INR', [('INR', 'International Normalized Ratio')], 'International Normalized Ratio', 'Rapport standardisé utilisé notamment pour surveiller les AVK ; ne permet pas d’exclure toute activité d’un anticoagulant direct.', 'i64-anticoagulant')
add_if_absent('AVK', [('AVK', 'Antivitamine K')], 'Antivitamine K', 'Anticoagulant réduisant l’activité de facteurs dépendants de vitamine K ; réversion urgente selon produit et contexte.', 'i64-pcc')
add_if_absent('PCC', [('PCC', 'Prothrombin complex concentrate')], 'Prothrombin complex concentrate', 'Concentré de complexe prothrombinique ; la dose et les unités dépendent du produit exact.', 'i64-pcc')
add_if_absent('HIC', [('HIC', 'Hémorragie intracérébrale')], 'Hémorragie intracérébrale', 'Sang dans le parenchyme cérébral ; expansion, effet de masse et extension ventriculaire peuvent aggraver le tableau.', 'i64-hic')
add_if_absent('IVT', [('IVT', 'Intravenous thrombolysis')], 'Intravenous thrombolysis', 'Thrombolyse intraveineuse ; en français également TIV. Nécessite sélection et produit exact.', 'i64-lyse')
add_if_absent('TIV', [('TIV', 'Thrombolyse intraveineuse')], 'Thrombolyse intraveineuse', 'Traitement fibrinolytique d’un infarctus éligible après exclusion de l’hémorragie.', 'i64-lyse')
add_if_absent('LVO', [('LVO', 'Large vessel occlusion')], 'Large vessel occlusion', 'Occlusion d’un gros vaisseau, à caractériser par l’imagerie dans la discussion de reperfusion.', 'i64-thrombectomie')
add_if_absent('MeVO', [('MeVO', 'Medium vessel occlusion')], 'Medium vessel occlusion', 'Occlusion d’un vaisseau de moyen calibre ; les essais récents ne justifient pas une thrombectomie systématique.', 'i64-thrombectomie')
add_if_absent('IRM', [('IRM', 'Imagerie par résonance magnétique')], 'Imagerie par résonance magnétique', 'Modalité associant notamment diffusion, FLAIR et séquences sensibles au sang selon la question clinique.', 'i64-imagerie')
add_if_absent('DWI', [('DWI', 'Diffusion-weighted imaging')], 'Diffusion-weighted imaging', 'Imagerie pondérée en diffusion ; confronter au coefficient ADC, au territoire et au contexte.', 'i64-imagerie')
add_if_absent('ADC', [('ADC', 'Apparent diffusion coefficient')], 'Apparent diffusion coefficient', 'Coefficient apparent de diffusion ; sa diminution aide à identifier une restriction de diffusion.', 'i64-imagerie')
add_if_absent('FLAIR', [('FLAIR', 'Fluid-attenuated inversion recovery')], 'Fluid-attenuated inversion recovery', 'Séquence IRM avec suppression du signal du liquide libre, utilisée notamment pour analyser les lésions parenchymateuses.', 'i64-imagerie')
add_if_absent('DWI-FLAIR', [('DWI-FLAIR', 'Diffusion et FLAIR')], 'Diffusion et FLAIR', 'Le mismatch entre diffusion positive et FLAIR non marquée peut sélectionner certaines thrombolyses au réveil ; ce n’est pas une heure exacte de début.', 'i64-mismatch')
add_if_absent('anti-Xa', [('anti-Xa', 'Activité dirigée contre le facteur X activé')], 'Activité dirigée contre le facteur X activé', 'Le dosage et son interprétation dépendent du médicament et de la méthode ; aucun seuil universel de lyse n’est ajouté ici.', 'i64-anticoagulant')
add_if_absent('ARIA', [('ARIA', 'Amyloid-related imaging abnormalities')], 'Amyloid-related imaging abnormalities', 'Anomalies d’imagerie liées à l’amyloïde pouvant comporter œdème ou hémorragie, notamment sous anticorps anti-amyloïdes.', 'i64-aria')
add_if_absent('DSC', [('DSC', 'Débit sanguin cérébral')], 'Débit sanguin cérébral', 'Débit dépendant de la pression de perfusion et des résistances ; la réserve vasculaire et les collatérales modifient la réponse.', 'i64-autoregulation')
add_if_absent('PPC', [('PPC', 'Pression de perfusion cérébrale')], 'Pression de perfusion cérébrale', 'Pression participant au maintien du débit cérébral ; elle ne se confond pas avec une cible thérapeutique de PA unique.', 'i64-autoregulation')
add_if_absent('RVC', [('RVC', 'Résistances vasculaires cérébrales')], 'Résistances vasculaires cérébrales', 'Résistances modifiées notamment par le calibre vasculaire dans l’autorégulation.', 'i64-autoregulation')
add_if_absent('ATP', [('ATP', 'Adénosine triphosphate')], 'Adénosine triphosphate', 'Support énergétique cellulaire dont la diminution participe aux perturbations de l’ischémie.', 'i64-energie')
add_if_absent('NMDA', [('NMDA', 'N-méthyl-D-aspartate')], 'N-méthyl-D-aspartate', 'Type de récepteur glutamatergique impliqué dans l’excitotoxicité ; mécanisme expérimental ne valant pas indication thérapeutique humaine.', 'i64-energie')
add_if_absent('INTERACT4', [('INTERACT4', 'Essai INTERACT4')], 'Essai INTERACT4', 'Essai chinois de baisse tensionnelle préhospitalière ; population et sous-groupes ne permettent pas de normaliser indistinctement la PA de tout AVC suspecté.', 'i64-pression')
