from pathlib import Path
from bs4 import BeautifulSoup
import json,hashlib,datetime,re,shutil
R=Path(__file__).resolve().parents[5];O=Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,j):
 p=O/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');return sha(p)
assert not (O/'source-binding.json').exists(),'Do not renew a final verification silently'
ledger=json.loads((O/'source-ledger.json').read_text());rights=json.loads((O/'figures-rights.json').read_text());browser=json.loads((O/'browser-report.json').read_text());assert browser['passed']
files={str(p.relative_to(R)):sha(p) for p in sorted((R/'chapters/D77').glob('*.html'))};final=dict(files);final['glossary/d77.py']=sha(R/'glossary/d77.py')
for f in rights['figures']:final[f['path']]=sha(R/f['path'])
preview='D77-apercu-autonome.html';ph=sha(O/preview)
raw='\n'.join((R/p).read_text() for p in files);(O/'monographie-source.html').write_text(raw);soup=BeautifulSoup(raw,'html.parser')
limits=[
'Auto-relectures explicites self_review par Sol-Hématologie-D77 ; aucune validation médicale humaine ni revue indépendante globale. Les contrôles ciblés de structure sont distincts.',
'27 lectures ciblées, dont plusieurs passages d’un même document ; pas 27 documents intégralement lus. Les textes complets restent hors Git, avec métadonnées et paraphrases publiées.',
'La monographie développe l’inclusion explicite fibrose splénique de schistosomiase dans D77*, sans réduire toute la catégorie à cette seule cause. Aucun sous-code D77.x dans la nomenclature suisse 2024 lue.',
'Aucune incidence suisse directe D77 retenue. Séries HSS sélectionnées, chiffres d’infection et cas migrants ne donnent pas une fréquence populationnelle de fibrose splénique.',
'Les repères adultes de numération HUG 2019 sont datés ; les références du laboratoire priment. Aucun seuil pédiatrique, gravidique, transfusionnel ou de geste n’est inventé.',
'La HSS est présinusoïdale et peut préserver relativement la fonction hépatique. Les mécanismes de cytopénie ne sont pas réduits à une destruction immune ; l’anémie peut associer d’autres causes.',
'Sérologie persistante, négativité d’un prélèvement et absence d’éosinophilie ont des limites. Aucun retraitement universel à 28 jours, ni seuil plaquettes/rate excluant universellement les varices.',
'Liste Swissmedic au 30 septembre 2026 et recherches AmiKo sans entrée praziquantel/Biltricide : constat daté, sans preuve d’indisponibilité définitive. Conditions d’importation et produit réel à vérifier.',
'Deux FI suisses exactes : Propranolol Zentiva janvier 2023 et Carvedilol Spirig HC octobre 2023. Biltricide ANSM 30 mai 2024 est un RCP français, sans statut de FI suisse.',
'Le RCP français et l’OMS 2022 diffèrent notamment pour grossesse/allaitement et cadre pédiatrique ; chaque formulation est attribuée, sans moyenne ni assimilation au produit accessible.',
'Pas de posologie portale de carvédilol tirée de sa FI cardiovasculaire, ni préférence HSS déduite de la cirrhose. EASL 2026 consulté pour l’exclusion de schistosomiase de la définition PSVD, sans transposer tous ses traitements.',
'Splénectomie, chirurgie et TIPS restent des décisions spécialisées avec preuves HSS hétérogènes. Pas de geste sur le seul chiffre de numération ; prévention d’asplénie distincte d’une simple splénomégalie.',
'CHUV 2024 est un protocole institutionnel daté. Aucun calendrier vaccinal actuel universel, voie pour thrombocytopénie ou dose antibiotique sans FI du produit n’est imposé.',
'Cinq originaux humains effectivement vus, 10 occurrences et 32 repères HTML ; pixels inchangés. Images normales distinctes du cas D77, œuf distinct de la preuve de fibrose ou de viabilité.',
'CDC utilisé seulement pour une photographie de 1979, pas comme recommandation clinique américaine. OpenStax 2016 CC BY 4.0 propre à la figure, sans importer les images actuelles NC.',
'Bandeau hérité du moteur S06 : SSP 154,171. Le contenu explicite d’autres tâches pertinentes PROFILES 2017 ; aucune prétention à une tâche officielle unique D77. Métadonnée partagée hors mission non modifiée.',
'Chromium local avec URL HTTP interceptée et toutes autres requêtes avortées. Ces vérifications ne démontrent ni déploiement public, ni remboursement, ni validation clinique.'
]
checks=[
'Quatorze points, vingt rubriques, examens, six sciences/neuf sections sémiologiques et pharmacologie confrontés aux passages réellement lus.',
'Libellé OFS D77*, inclusion B65.-†, absence de sous-code et distinction manifestation/cause vérifiés ; volume, fibrose, hypersplénisme et asplénie séparés.',
'Exposition à l’eau douce, preuve d’œufs, sérologie et activité distinguées ; HSS/uro-génital et aigu/chronique différenciés. Aucune photographie normale présentée comme preuve individuelle.',
'Hématémèse/méléna et retentissement priorisés ; enzymes peu perturbées ou absence d’ascite non rassurantes à elles seules. Tachycardie masquée sous propranolol explicitée.',
'Doppler et endoscopie complémentaires ; pas de seuil plaquettes/rate universel, de biopsie splénique automatique ou de PSVD attribuée à toute hypertension portale non cirrhotique.',
'Praziquantel : RCP français 40 mg/kg S. haematobium, 40 ou 2×20 mansoni/intercalatum, 60 ou 2×30 japonicum ; 4–6 h entre prises répétées le même jour, repas, moins d’un an sécurité non établie, formes aiguës/neuro spécialisées.',
'Rifampicine contre-indiquée, autres interactions et atteinte hépatique/HSS vérifiées ; grossesse/allaitement RCP distincts de l’OMS. Aucun algorithme rénal numérique inventé.',
'Propranolol suisse adulte HTP : 20 mg deux fois/jour, titration/objectif relatif 25 %, 80 mg deux fois/jour et maximum exceptionnel 160 mg deux fois/jour ; pas d’augmentation à 50–55/min, pression/tolérance et contre-indications. Rainure décorative 40/80 mg conservée.',
'Carvédilol sans indication portale dans la FI lue ; restriction avant 18 ans et grossesse/allaitement/foie vérifiées, sans transplantation de doses cardiovasculaires.',
'Suivi parasitaire et hépatoportal distincts ; trois mois attribués au consensus espagnol, contrôle anticipé si complication et possibilité de régression partielle de fibrose sans promesse.',
'Prévention post-splénectomie attribuée CHUV, fièvre urgente et plan individuel ; aucune dose antibiotique ou voie vaccinale non vérifiée. Pas d’assimilation splénomégalie/asplénie.',
'Sources des fenêtres dérivées des sections pertinentes ; calculs fictifs mg/kg et baisse relative de fréquence explicites, quiz sans statut fédéral officiel.',
'Sept règles sémiologiques natives, première section exacte, aria et neuf marqueurs avec liens https dans sources ; navigation, Livre 24 px, 34 fenêtres et quatre quiz vérifiés aux deux largeurs.'
]
base=dict(reviewer='astra_nephrologie',production_name='Sol-Hématologie-D77',runtime_name='sol_nephrologie',model='gpt-6.1-sol',reasoning='high',mode='self_review',independent=False,reviewed_at=now,canonical_files=files,glossary_sha256=final['glossary/d77.py'],preview_sha256=ph,medical_human_validation=False,clinical_certification=False,requirements_reviewed=dict(fundamental_analytical_semiology=True))
reviews={}
for kind in ['medical','language','visual_desktop','visual_mobile']:
 j=dict(base)
 if kind=='medical':j.update(scope='Auto-relecture des six surfaces finales et des passages ciblés, deux FI suisses et un RCP français ; aucune revue médicale indépendante revendiquée.',checks=checks,limitations=limits)
 elif kind=='language':j.update(scope='Auto-relecture du français, des unités, des négations, des populations, des fenêtres, des quiz et légendes.',checks=['Progression exposition → gravité → preuves → retentissement → soins.','D77*, B65.-†, mg/kg, g/L et G/L conservés ; pas de séparation automatique entre lettres et chiffres.','RCP étranger, FI suisse et recommandation attribués sans confusion.','Glossaire D77 limité aux notions employées, avec cibles de fenêtres réelles.'],limitations=limits[:2])
 else:
  width=1440 if kind=='visual_desktop' else 390
  j.update(scope=f'Chromium {width}px sur aperçu natif autonome final.',checks=next(v for v in browser['viewports'] if v['width']==width),visual_inspection='Captures ouverture, cinq originaux annotés, sémiologie, fenêtre et Livre 24 px réellement examinées. Les repères situent des structures de provenance connue sans créer de lésion.',limitations=limits[-3:])
 h=save('reviews/'+kind+'.json',j);reviews[kind]=dict(path='reviews/'+kind+'.json',reviewer='astra_nephrologie',mode='self_review',sha256=h)
anchors=['d77-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]
semio=dict(base,kind='SEMIO',requirement='fundamental_analytical_semiology',status='closed',source_files_sha256=files,reviewed_files_sha256=final,unresolved_blockers=[],section_anchors=anchors,evidence=['audit-sciences.json','browser-report.json','source-ledger.json'],findings='Neuf sections substantielles, liens de sources et premier onglet visible ; ponts science vers clinique, examen et traitement. Contrôle ciblé de structure distinct de l’auto-relecture médicale, sans validation humaine.')
sh=save('reviews/SEMIO.json',semio)
images=[]
for f in rights['figures']:
 p=O/'images'/Path(f['path']).name;p.parent.mkdir(exist_ok=True);shutil.copyfile(R/f['path'],p)
 images.append(dict(f,path=str(p.relative_to(O)),canonical_path=f['path'],medical_review='Original et repères effectivement vus ; auto-relecture Sol-Hématologie-D77 sans certification médicale humaine.'))
def section_sources(a):
 return list(dict.fromkeys(''.join(str(x) for x in link.find_all(string=True)).split(' — ')[0] for link in soup.find(id=a).select('a[data-reference-source]')))
titles=['Définition','Épidémiologie','Physiopathologie','Démarche clinique','Anamnèse','Examen clinique','Syndromes','Diagnostic positif','Explorations','Arbre diagnostique et différentiels','Prise en charge','Prévention, suivi et pronostic','Points clés','Pièges']
monograph=[]
for i,t in enumerate(titles,1):
 q=soup.find(id=f'd77-{i}');text=' '.join(str(x) for x in q.find_all(string=True))
 monograph.append(dict(point=i,title=t,anchor=f'd77-{i}',sources=section_sources(f'd77-{i}'),coverage_explanation=text[:500]))
rt=['Question clinique/enjeu fédéral','Définition/périmètre CIM','Classifications','Épidémiologie','Normal vers pathologique','Étiologies/risques','Anamnèse/symptômes','Examen clinique','Urgences','Examens','Différentiels','Prise en charge suisse','Complications/pronostic','Suivi/prévention','Populations particulières','Spécificités suisses','Critères formels','Paramètres chiffrés','Sous-codes','Examen fédéral']
ra=['d77-question','d77-1','d77-7','d77-2','d77-semio-normal','d77-3','d77-5','d77-6','d77-4','d77-e-parasite','d77-10','d77-11','d77-12','d77-12','d77-p-populations','d77-p-status','d77-8','d77-p-prazi','d77-1','d77-entrainement']
af={a:p for p in files for a in re.findall(r'\bid="([^"]+)"',(R/p).read_text())};matrix=[];rubrics=[]
for i,(title,a) in enumerate(zip(rt,ra),1):
 assert a in af;ss=section_sources(a);assert ss
 ev=[dict(file=af[a],anchor=a)]+[dict(file='source-ledger.json',source_id=sid,json_pointer='/sources/'+str(next(k for k,x in enumerate(ledger['sources']) if x['id']==sid))) for sid in ss]
 matrix.append(dict(point=i,title=title,status='covered',evidence=ev,coverage_scope='Contenu pédagogique et limites explicites, sans certification clinique.'))
 rubrics.append(dict(rubric=i,title=title,anchor=a,content_present=True,current_verification='Auto-relecture des octets finaux et limites attribuées.'))
save('findings-final.json',dict(code='D77',reviewed_at=now,blocking_findings=[],corrected_findings=['Conteneur scientifique stabs remplacé par sci-bar après échec navigateur exploratoire, puis reconstruction et contrôle complets.','Repère médullaire déplacé sur la barre d’échelle originale pour éviter une localisation chromatique ambiguë.','Anciennes fenêtres et chiffres non vérifiés du glossaire D77 remplacés par des définitions locales sourcées.'],transparent_limits=limits))
save('lesson-manifest.json',dict(code='D77',author='astra_nephrologie',production_name='Sol-Hématologie-D77',active_specialty='hematologie',runtime_name='sol_nephrologie',recorded_at=now,branch='codex/alpha77/d77-integrate-g1',base='8a512893acbab9caa0dcfdd0e8682a44ea72fda6',monograph=monograph,medina_rubrics=rubrics,matrix20=matrix,sources=ledger['sources'],images=images,semiology=dict(section_anchors=anchors),scientific_subtabs=['Sémiologie fondamentale et analytique','Anatomie','Histologie','Physiologie','Biochimie','Immunologie'],reviews=reviews,audits=dict(MED=reviews['medical'],LANG=reviews['language'],SEMIO=dict(path='reviews/SEMIO.json',sha256=sh)),blocking_findings=[],medical_human_validation=False,clinical_certification=False,tokens_actual=None,cost_actual=None,canonical_files=files,source_glossary_sha256=final['glossary/d77.py'],catalogue_entry_sha256=sha(R/'chapters.json'),preview=dict(path=preview,sha256=ph),limitations=limits,closure_status='self_reviewed_project_delivery_not_clinically_certified'))
save('source-binding.json',dict(code='D77',verified_at=now,preview=preview,preview_sha256=ph,final_sources=final,checks=['test-static.txt','audit-sciences.json','browser-report.json','figures-rights.json','findings-final.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json','reviews/SEMIO.json'],clinical_certification=False))
(O/'README.md').write_text('''# D77 — Sol-Hématologie-D77

14 points, 20 rubriques, six sciences, neuf sections sémiologiques, 27 lectures ciblées, deux FI suisses et un RCP français distinct, cinq originaux humains, 10 occurrences/32 repères, 34 fenêtres et quatre quiz. Aperçu autonome : D77-apercu-autonome.html.

Auto-relectures explicitement self_review, sans validation médicale humaine. Textes complets hors Git ; métadonnées et paraphrases dans source-ledger.json. Limites et corrections dans findings-final.json. Aucun autre cours, catalogue ou moteur partagé modifié. Aucune PR/main ni publication publique revendiquée.
''')
print('D77 : manifeste 14/20 et première liaison finale aux octets vérifiés créés.')
