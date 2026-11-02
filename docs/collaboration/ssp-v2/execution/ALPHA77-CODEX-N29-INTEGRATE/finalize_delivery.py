"""Assemble preuves finales après tests et inspection visuelle réels ; ne certifie pas la médecine."""
from pathlib import Path
import json,hashlib,datetime,shutil,re,subprocess
ROOT=Path(__file__).resolve().parents[5];OUT=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):p=OUT/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');return sha(p)
ledger=json.loads((OUT/'source-ledger.json').read_text());rights=json.loads((OUT/'figures-rights.json').read_text());browser=json.loads((OUT/'browser-report.json').read_text());assert browser['passed']
files={str(p.relative_to(ROOT)):sha(p) for p in sorted((ROOT/'chapters/N29').glob('*.html'))}
final=dict(files);final['glossary/n29.py']=sha(ROOT/'glossary/n29.py')
for f in rights['figures']:final[f['path']]=sha(ROOT/f['path'])
preview='N29-apercu-autonome.html';ph=sha(OUT/preview)
(OUT/'monographie-source.html').write_text('\n'.join((ROOT/p).read_text() for p in files))
limits=[
'Auto-relectures de l’auteur, sans revue médicale indépendante globale ni validation humaine.',
'Les références héritées restent attribuées à Claude (14 octobre 2026) ; les 31 lectures de cette reprise portent sur des sections ciblées, pas sur tous les ouvrages intégraux.',
'Aucune incidence rénale suisse ne peut être déduite des chiffres nationaux de tuberculose ou de syphilis ; les populations étrangères restent étiquetées.',
'Les recommandations consultées ne fournissent pas de présentation ni de critère validé propre à la gomme rénale tertiaire. Le cours enseigne la distinction avec la glomérulopathie, la preuve de syphilis et l’évaluation spécialisée de causalité, sans inventer ces données rares.',
'Praziquantel : revue clinique suisse et RCP français exact ; produit disponible et accès suisse à confirmer. Aucun résultat AmiKo ne prouve une indisponibilité.',
'Indométacine dans la cystinose : schéma international spécialisé, non indication de la FI suisse Indocid-Retard ; formulation pédiatrique adaptée non documentée.',
'Divergences EAU/revue 2021 pour culture, FI/guide suisse pour antituberculeux, FI/recommandations 2026 pour Procysbi conservées explicitement ; aucun arbitrage automatique par date.',
'Navigation native contrôlée sur origine HTTP interceptée, autres requêtes bloquées ; aucun déploiement public ni navigation réseau réelle n’est revendiqué.',
'PROFILES 2017 : correspondance pédagogique de situations cliniques ; pas une liste officielle de catégories CIM ni de questions d’examen.',
'Photographie PHIL 34 diffusée par la source en 700×467 ; aucune transformation des pixels. Une coupe ne permet ni typage exhaustif des cellules ni mesure de charge parasitaire.'
]
medical_checks=[
'Tuberculose : culture répétée et PCR complémentaire, sensibilité hétérogène et limites d’exclusion ; chirurgie individualisée, distinction drainage/reconstruction.',
'Schistosomiase : dénominateurs de cohorte, proportions positives distinctes de sensibilité, suivi à dénominateurs variables sans taux d’échec inféré.',
'Syphilis : forme tardive possiblement latente ; tests tréponémiques et non tréponémiques distingués ; atteintes neuro/oculaires/otiques hors schéma retard IM.',
'Cystinose : bénéfice possible du traitement avant deux mois sur Fanconi, cristaux parfois absents avant deux ans, atteinte tubulaire malgré créatinine normale.',
'Rifater contre-indiqué sous 30 mL/min ; Myambutol contrôle oculaire hebdomadaire en insuffisance rénale et doses FI/guide distinguées ; Pyrazinamide FI sous 50 mL/min opposée au guide sans prescription automatique.',
'Procysbi : leucocytes mixtes, cible <1 nmol hémicystine/mg protéine, prélèvement 30 min après dose du matin/12,5 h après soir, conversion FI 100% versus recommandation internationale 80%.',
'Doxycyclin-Mepha 100 mg deux fois par jour pendant 28 jours chez adulte non enceinte allergique ; Extencilline strictement IM, jamais IV ; Cystadrops plus de six mois.',
'Jarisch–Herxheimer : prophylaxie corticoïde discutée, faible preuve ; observation après injection distincte de surveillance clinique prolongée.',
'Praziquantel/rifampicine contre-indiqués ensemble dans RCP français ; indométacine pédiatrique distinguée de capsule retard suisse non recommandée chez enfant.',
'Classification OFS relue : inclusions N29.1/N29.8 explicites, N08.0/N16.3 distincts, libellé A52.7 corrigé ; annexe après conclusion clinique.',
'Lectures des six fichiers et des résumés/Pareto ; les erreurs à risque identifiées ont été corrigées sur les surfaces retrouvées. Les citations héritées ne sont pas présentées comme entièrement revalidées.'
]
reviewbase=dict(reviewer='astra_nephrologie',mode='self_review',independent=False,reviewed_at=NOW,canonical_files=files,glossary_sha256=final['glossary/n29.py'],preview_sha256=ph,medical_human_validation=False,clinical_certification=False)
reviews={}
for kind in ['medical','language','visual_desktop','visual_mobile']:
 r=dict(reviewbase)
 if kind=='medical':r.update(scope='Auto-relecture clinique des six surfaces, corrections ciblées confrontées aux passages lus et neuf FI suisses exactes ; héritage conservé et attribué.',checks=medical_checks,limitations=limits)
 elif kind=='language':r.update(scope='Auto-relecture du français et des formulations des six fichiers, y compris fenêtres et tableaux.',checks=['Distinction observation/recommandation, population et temporalité explicitée.','Espaces des unités, décimales françaises et termes scientifiques corrigés.','Anciennes phrases incompatibles dans fenêtres et résumés recherchées et corrigées.','Le correcteur typographique avait altéré le CSS : défaut corrigé, protection style/script ajoutée, validation visuelle renouvelée.','Test statique : abréviations couvertes, fenêtres et quiz résolus.'],limitations=['Pas de relecture humaine ou indépendante ; la passe automatique ne remplace pas la relecture sémantique.'])
 else:
  width=1440 if kind=='visual_desktop' else 390;v=next(x for x in browser['viewports'] if x['width']==width)
  r.update(scope=f'Chromium {width}px, aperçu autonome, images vues après chargement et décodage.',checks=v,visual_inspection=['Quatre originaux humains inspectés avec les annotations : cortex/pyramide/bassinet/uretère ; tubule proximal/anse ascendante/collecteur ; œufs et infiltrat ; vessie/utérus/pubis.','La première capture avait révélé des repères non superposés malgré test fonctionnel favorable. CSS réparé ; test final vérifie la position absolue dans l’image.','Six disciplines, neuf sections de sémiologie, fenêtre, mode Livre 24px et absence de débordement horizontal vérifiés.'],limitations=['Aucun déploiement public ; requêtes externes bloquées.','Le bouton flottant Plan peut recouvrir une petite zone de légende dans certaines captures mobiles ; la lecture reste accessible en défilant.'])
 h=save('reviews/'+kind+'.json',r);reviews[kind]=dict(path='reviews/'+kind+'.json',reviewer='astra_nephrologie',mode='self_review',sha256=h)
images=[]
for f in rights['figures']:
 dest=OUT/'images'/Path(f['path']).name;dest.parent.mkdir(exist_ok=True);shutil.copyfile(ROOT/f['path'],dest)
 images.append(dict(f,path=str(dest.relative_to(OUT)),canonical_path=f['path'],medical_review='Auto-relecture visuelle IA : original et annotations vus ; figures-rights.json et reviews/visual_desktop.json ; aucune validation humaine.'))
monorows=[
(1,'Définition','n29-1',['CH-TB-DX','EU-CYST-MECA'],'Périmètre clinique de quatre maladies générales et distinction obstacle, tubulopathie et atteinte glomérulaire ; classification déplacée en annexe après la synthèse.'),
(2,'Épidémiologie','n29-2',['CH-TB-EPI','CH-SYPH-EPI','EU-SCH-COHORT','EU-CYST-MECA'],'Données suisses puis cohortes étrangères attribuées ; absence de fréquence rénale suisse explicitée et aucune extrapolation des proportions de migrants à la population générale.'),
(3,'Physiopathologie','n29-3',['TB-MECA','SCH-MECA','EU-CYST-MECA'],'Dissémination tuberculeuse, réaction aux œufs, complexes immuns et défaut lysosomal distingués ; six sciences relient fonction normale, lésion, signe, exploration et traitement.'),
(4,'Démarche clinique','n29-7',['CH-TB-DX','EU-TB-DX','EU-SYPH-DX'],'La démarche distingue preuve de la maladie causale et mesure du retentissement, avec limites des tests, diagnostics concurrents et prise en compte d’infections associées.'),
(5,'Anamnèse','n29-5',['TB-MECA','CH-SCH-PEC','EU-SYPH-DX','EU-CYST-MECA'],'Expositions, origine, chronologie infectieuse, eau douce, antécédents thérapeutiques et présentation pédiatrique organisent la probabilité avant les examens sans remplacer la confirmation.'),
(6,'Examen clinique','n29-6',['TB-MECA','CH-SCH-PEC','EU-CYST-MECA'],'État général, signes vitaux, appareil urinaire/génital, croissance, hydratation et signes extrarénaux ; limites d’un examen normal approfondies dans la sémiologie analytique.'),
(7,'Syndromes','n29-syndromes',['EU-TB-DX','CH-SCH-PEC','EU-CYST-MECA'],'Syndromes irritatif, obstructif, de Fanconi et glomérulaire sont différenciés pour localiser la lésion ; créatinine et fonction tubulaire ne sont pas considérées équivalentes.'),
(8,'Diagnostic positif','n29-12',['CH-TB-DX','EU-SYPH-DX','EU-CYST-MECA'],'Critères microbiologiques, sérologiques et métaboliques, avec méthodes et limites : aucun critère rénal tertiaire inventé et aucune attribution d’organe à une sérologie isolée.'),
(9,'Explorations','n29-e-1',['EU-TB-DX','EU-SCH-COHORT','EU-CYST-MECA'],'Sept sections d’examens relient question, prélèvement, statut, performance et interprétation ; méthode de cystine, imagerie et limites d’exclusion sont distinguées.'),
(10,'Arbre diagnostique (différentiels)','n29-arbre',['EU-TB-DX','CH-SCH-PEC','EU-SYPH-DX'],'Parcours explicite de cinq étapes selon gravité, hématurie, lésion persistante, tubulopathie ou sérologie positive ; tumeur, infection usuelle et causalités concurrentes restent ouvertes.'),
(11,'PEC','n29-9',['CH-TB-TX','CH-SCH-PEC','EU-SYPH-TX','FI-PROCYSBI'],'Traitements étiologiques et soutien séparés, produits suisses exacts vérifiés, adaptations et contre-indications visibles ; divergences avec recommandations discutées sans ordonnance automatique.'),
(12,'Prévention/suivi/pronostic','n29-suivi-actualise',['CH-SCH-PEC','EU-SYPH-DX','EU-SYPH-TX','EU-CYST-TX'],'Objectifs de suivi microbiologique, urologique, sérologique et métabolique, prévention des expositions et poursuite de cystéamine après greffe ; délais contextualisés selon maladie et âge.'),
(13,'Points clés','n29-conclusion',['CH-TB-DX','CH-SCH-PEC','EU-CYST-MECA'],'Synthèse clinique, paramètres et exercices originaux conservent le raisonnement à partir des symptômes ; correspondance PROFILES 2017 explicitement pédagogique et non question officielle.'),
(14,'Pièges','n29-pieges',['EU-TB-DX','EU-SCH-COHORT','FI-PROCYSBI','FR-PRAZI'],'Pièges diagnostiques et médicamenteux regroupés : positivité versus sensibilité, culture négative, prescription selon formulation, interactions et atteintes syphilitiques spécialisées.')]
monograph=[dict(point=n,title=title,anchor=a,sources=s,coverage_explanation=e) for n,title,a,s,e in monorows]
old=json.loads(Path('/workspace/Medina-nephrologie/docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-N04-INTEGRATE/lesson-manifest.json').read_text())
anchors=['n29-0','n29-1','n29-3','n29-2','n29-semio-normal','n29-4','n29-5','n29-6','n29-8','n29-e-1','n29-arbre','n29-9','n29-8','n29-suivi-actualise','n29-11','n29-produits-ch','n29-12','n29-12','n29-annexe-cim','n29-federal']
rubrics=[];matrix=[]
anchorfiles={}
for path in files:
 for a in re.findall(r'\bid="([^"]+)"',(ROOT/path).read_text()):anchorfiles[a]=path
for i,(a,oldrow) in enumerate(zip(anchors,old['medina_rubrics']),1):
 assert a in anchorfiles,a
 rubrics.append(dict(rubric=i,title=oldrow['title'],anchor=a,content_present=True,current_verification='Auto-relecture avec passages ciblés actuels et références héritées attribuées',limits='Les limites de population, source, rareté et produit sont conservées explicitement ; voir source-ledger et réserves.'))
 source_map=[['CH-PROFILES-2017'],['CH-CIM'],['EU-SYPH-DX','EU-CYST-MECA'],['CH-TB-EPI','CH-SYPH-EPI','EU-SCH-COHORT'],['NORMAL-KIDNEY','EU-CYST-MECA'],['TB-MECA','SCH-MECA'],['EU-TB-DX','CH-SCH-PEC'],['EU-CYST-MECA','CH-SCH-PEC'],['EU-TB-PEC','FI-MYAMBUTOL'],['EU-TB-DX','EU-CYST-MECA'],['EU-TB-DX','EU-SYPH-DX'],['CH-TB-TX','CH-SCH-PEC','FI-EXTENCILLINE','FI-PROCYSBI'],['SCH-MECA','EU-CYST-TX'],['CH-SCH-PEC','EU-SYPH-TX','EU-CYST-TX'],['FI-RIFATER','FI-PYRAZINAMIDE','FI-DOXY'],['CH-TB-TX','FI-PROCYSBI','FI-INDOCID'],['CH-TB-DX','EU-SYPH-DX','EU-CYST-MECA'],['EU-TB-DX','FI-PROCYSBI'],['CH-CIM'],['CH-PROFILES-2017','CH-MEBEKO-2026']]
 evidence=[dict(file=anchorfiles[a],anchor=a)]+[dict(file='source-ledger.json',json_pointer='/sources/'+str(next(j for j,s in enumerate(ledger['sources']) if s['id']==sid)),source_id=sid) for sid in source_map[i-1]]
 matrix.append(dict(point=i,title=oldrow['title'],status='covered',evidence=evidence,coverage_scope='Couverture pédagogique effective de la rubrique, sans certification clinique ni prétention à une donnée absente.'))
initial=json.loads((OUT/'findings-initial.json').read_text());closed=[]
for f in initial['findings']:closed.append(dict(f,status='corrected_and_self_reviewed',review='reviews/medical.json',verification='test-static.txt; audit-sciences.json; browser-report.json',final_sources=files))
save('findings-final.json',dict(code='N29',reviewed_at=NOW,findings=closed,additional_findings=['Jarisch–Herxheimer : prophylaxie et durée de surveillance clarifiées.','Indocid-Retard : usage pédiatrique non recommandé distingué du schéma international.','CSS altéré par passe typographique : défaut corrigé et contrôle géométrique ajouté.'],blocking_findings=[],transparent_limits=limits))
manifest=dict(code='N29',author='astra_nephrologie',recorded_at=NOW,branch='codex/alpha77/n29-integrate-g1',base='8a512893acbab9caa0dcfdd0e8682a44ea72fda6',monograph=monograph,medina_rubrics=rubrics,matrix20=matrix,sources=ledger['sources'],images=images,semiology=dict(section_anchors=['n29-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]),scientific_subtabs=['Sémiologie fondamentale et analytique','Anatomie','Histologie','Physiologie','Biochimie','Immunologie et génétique'],reviews=reviews,blocking_findings=[],medical_human_validation=False,clinical_certification=False,tokens_actual=None,cost_actual=None,canonical_files=files,source_glossary_sha256=final['glossary/n29.py'],preview=dict(path=preview,sha256=ph),limitations=limits,remaining_transparent_limits=limits,closure_status='reviewed_project_delivery_not_clinically_certified')
save('lesson-manifest.json',manifest)
save('source-binding.json',dict(code='N29',verified_at=NOW,preview=preview,preview_sha256=ph,final_sources=final,checks=['test-static.txt','audit-sciences.json','browser-report.json','figures-rights.json','findings-final.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json'],clinical_certification=False))
print('Preuves assemblées : 14 points,20 rubriques,31 lectures,9 FI,4 originaux ; aucune certification clinique.')
