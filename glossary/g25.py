"""Abréviations G25 — autres syndromes extrapyramidaux et troubles de la motricité ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
_root = next((p for p in _here.parents if (p / 'build_medina.py').exists()), None)
_dirs = [_here] + ([_root / 'glossary'] if _root else [])
_existing = {}
for _d in _dirs:
    if str(_d) not in sys.path:
        sys.path.append(str(_d))
    for _path in sorted(_d.glob('*.py')):
        if _path.stem in {'g25', '__init__'}:
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


add_if_absent('RLS', [('R', 'Restless'), ('L', 'Legs'), ('S', 'Syndrome')], 'Restless legs syndrome', 'Syndrome des jambes sans repos : cinq critères cliniques, pas diagnostic sur polysomnographie seule.', 'g25-rls')
add_if_absent('SJSR', [('S', 'Syndrome des'), ('J', 'Jambes'), ('S', 'Sans'), ('R', 'Repos')], 'Syndrome des jambes sans repos', 'Besoin de bouger au repos, soulagé par mouvement et à prédominance soir/nuit, sans explication intégrale par un imitateur.', 'g25-criteria')
add_if_absent('PLMS', [('P', 'Periodic'), ('L', 'Limb'), ('M', 'Movements in'), ('S', 'Sleep')], 'Periodic limb movements in sleep', 'Mouvements périodiques pendant le sommeil ; association possible au RLS, sans équivalence avec une maladie PLMD.', 'g25-plms')
add_if_absent('PLMD', [('P', 'Periodic'), ('L', 'Limb'), ('M', 'Movement'), ('D', 'Disorder')], 'Periodic limb movement disorder', 'Trouble clinique qui ne se diagnostique ni ne se traite sur un index polysomnographique seul.', 'g25-plms')
add_if_absent('EMG', [('É', 'Électro'), ('M', 'Myo'), ('G', 'Graphie')], 'Électromyographie', 'Enregistrement de l’activité musculaire, à adapter aux muscles et à la condition déclenchante.', 'g25-emg')
add_if_absent('EEG', [('É', 'Électro'), ('E', 'Encéphalo'), ('G', 'Graphie')], 'Électroencéphalographie', 'Enregistrement de l’activité électrique cérébrale ; le couplage avec EMG peut aider dans les myoclonies.', 'g25-eeg')
add_if_absent('GAD65', [('GAD', 'Glutamate décarboxylase'), ('65', 'masse nominale de 65 kilodaltons')], 'Glutamate décarboxylase 65', 'Isoforme codée par GAD2, participant à la synthèse du GABA ; un anticorps isolé ne diagnostique pas le syndrome de la personne raide.', 'g25-gad')
add_if_absent('GAD2', [('GAD2', 'symbole du gène de la glutamate décarboxylase 2')], 'Glutamate décarboxylase 2', 'Gène humain codant l’isoforme GAD65 ; annotation de biochimie normale, pas protocole thérapeutique.', 'g25-gad')
add_if_absent('PCP4', [('PCP', 'Purkinje cell protein'), ('4', 'identifiant de la protéine')], 'Purkinje cell protein 4', 'Marqueur immunohistochimique de l’illustration humaine ; distinct de GAD65 et du dosage d’anticorps du patient.', 'g25-gad')
add_if_absent('SV2A', [('SV', 'Synaptic vesicle'), ('2A', 'protéine 2A')], 'Protéine vésiculaire synaptique 2A', 'Cible de liaison du lévétiracétam contribuant à son mécanisme antiépileptique, sans indication universelle pour les myoclonies.', 'g25-eeg')
add_if_absent('TSAT', [('T', 'Transferrin'), ('SAT', 'Saturation')], 'Saturation de la transferrine', 'Paramètre du bilan martial à interpréter avec ferritine, unités et contexte clinique.', 'g25-iron')
add_if_absent('ClCr', [('Cl', 'Clairance'), ('Cr', 'Créatinine')], 'Clairance de la créatinine', 'Paramètre utilisé par les tables de dose rénale ; vérifier méthode, unités et indexation du produit exact.', 'g25-pregabalin')
add_if_absent('SPS', [('S', 'Stiff'), ('P', 'Person'), ('S', 'Syndrome')], 'Stiff person syndrome', 'Syndrome de la personne raide : raideur et spasmes avec démarche spécialisée, pas diagnostic par anticorps seul.', 'g25-sps')
add_if_absent('IAPRD', [('I', 'International'), ('A', 'Association of'), ('P', 'Parkinsonism and'), ('R', 'Related'), ('D', 'Disorders')], 'International Association of Parkinsonism and Related Disorders', 'Consensus de classification des myoclonies, axes clinique, neurophysiologique et étiologique ; résumé primaire 2025 consulté.', 'g25-phenotype')
add_if_absent('ER', [('ER', 'Extended release')], 'Libération prolongée', 'Forme retard ; la FI Sifrol ER ne constitue pas une indication RLS de la forme immédiate.', 'g25-prami')
add_if_absent('ET', [('E', 'Essential'), ('T', 'Tremor')], 'Essential tremor', 'Tremblement essentiel, syndrome défini par critères cliniques et durée.', 'g25-essential')
add_if_absent('ET+', [('ET', 'Essential tremor'), ('+', 'signes discrets additionnels')], 'Essential tremor plus', 'Signes discrets insuffisants pour un autre syndrome neurologique défini, à décrire et réévaluer.', 'g25-etplus')
add_if_absent('GABA', [('G', 'Gamma'), ('A', 'Amino'), ('B', 'Butyric'), ('A', 'Acid')], 'Acide gamma-aminobutyrique', 'Neurotransmetteur inhibiteur ; prégabaline, clonazépam et lévétiracétam n’ont pas la même cible.', 'g25-gad')
add_if_absent('α2δ', [('α2δ', 'sous-unité alpha-2-delta')], 'Sous-unité alpha-2-delta de canal calcique', 'Cible de liaison de la prégabaline ; ne signifie pas agoniste GABA direct.', 'g25-pregabalin')

add_if_absent('PSG', [('P', 'Poly'), ('S', 'Somno'), ('G', 'Graphie')], 'Polysomnographie', 'Enregistrement du sommeil, à demander pour une question clinique ; non obligatoire pour tout diagnostic de jambes sans repos.', 'g25-rls')
add_if_absent('ESSTS', [('E', 'European'), ('S', 'Society for the'), ('S', 'Study of'), ('T', 'Tourette'), ('S', 'Syndrome')], 'European Society for the Study of Tourette Syndrome', 'Société européenne des recommandations de tics version 2.0, publication en ligne 2021 et numéro 2022.', 'g25-tic')
add_if_absent('DGSM', [('D', 'Deutsche'), ('G', 'Gesellschaft für'), ('S', 'Schlafforschung und'), ('M', 'Schlafmedizin')], 'Société allemande de recherche sur le sommeil et de médecine du sommeil', 'Cosignataire avec la DGN de la recommandation abrégée RLS 2024.', 'g25-rls')
add_if_absent('GPe', [('GP', 'Globus pallidus'), ('e', 'externe')], 'Segment externe du globus pallidus', 'Repère anatomique distinct du segment interne sur l’original humain ; pas mesure d’activité chez le patient.', 'g25-phenotype')
add_if_absent('STN', [('S', 'Sub'), ('T', 'Thalamic'), ('N', 'Nucleus')], 'Noyau sous-thalamique', 'Structure nommée sur le schéma humain de référence ; l’image n’établit pas une lésion G25.', 'g25-phenotype')
add_if_absent('SN', [('S', 'Substantia'), ('N', 'Nigra')], 'Substance noire', 'Repère du schéma de référence ; ni quantité de dopamine ni concentration de fer mesurée.', 'g25-phenotype')
add_if_absent('G25.0', [('G25.0', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.0', 'tremblement essentiel/familial. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.1', [('G25.1', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.1', 'tremblement médicamenteux. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.2', [('G25.2', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.2', 'autres tremblements précisés. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.3', [('G25.3', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.3', 'myoclonies, hors épilepsie myoclonique G40.-. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.4', [('G25.4', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.4', 'chorée médicamenteuse. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.5', [('G25.5', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.5', 'autres chorées, hors Huntington et Sydenham. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.6', [('G25.6', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.6', 'tics médicamenteux ou autres organiques, hors Tourette et tic sans précision. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.8', [('G25.8', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.8', 'catégorie des autres syndromes précisés, subdivisée dans la version suisse consultée. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.80', [('G25.80', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.80', 'mouvements périodiques des jambes pendant le sommeil. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.81', [('G25.81', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.81', 'syndrome des jambes sans repos. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.88', [('G25.88', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.88', 'autres syndromes précisés, dont akathisie et personne raide. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.9', [('G25.9', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.9', 'syndrome extrapyramidal et trouble de la motricité sans précision. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G51.4', [('G51.4', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G51.4', 'myokymie faciale, exclue de G25.3. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('F95.2', [('F95.2', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : F95.2', 'syndrome de Gilles de la Tourette, exclu de G25.6. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('F95.9', [('F95.9', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : F95.9', 'tic sans précision, exclu de G25.6. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
add_if_absent('G25.82', [('G25.82', 'notation de nomenclature à interpréter dans la version suisse consultée')], 'Nomenclature : G25.82', 'sous-code absent de l’entrée suisse consultée, non utilisé dans ce cours. La conclusion clinique précède le codage ; ce libellé ne choisit aucun traitement.', 'g25-definition')
