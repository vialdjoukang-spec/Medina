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
audit=json.loads((O/'audit-sciences.json').read_text());words=audit['totals']['after']['words'];assert audit['result']=='passed'
files={str(p.relative_to(R)):sha(p) for p in sorted((R/'chapters/G24').glob('*.html'))};final=dict(files);final['glossary/g24.py']=sha(R/'glossary/g24.py')
for f in rights['figures']:final[f['path']]=sha(R/f['path'])
preview='G24-apercu-autonome.html';ph=sha(O/preview)
raw='\n'.join((R/p).read_text() for p in files);(O/'monographie-source.html').write_text(raw);soup=BeautifulSoup(raw,'html.parser')
limits=[
 'Auto-relectures explicites self_review par Sol-Neurologie-G24 ; aucune validation médicale humaine ni revue indépendante globale. Contrôles ciblés de structure distincts.',
 '41 lectures ciblées/réutilisations attribuées, plusieurs passages d’un même document ; pas 41 documents intégralement lus. Sources complètes hors Git, métadonnées et paraphrases publiées.',
 'OFS CIM-10-GM 2024 : G24.0/.1/.2/.3/.4/.5/.8/.9 et frontières G80.3/M43.6 réellement lues. Inclusion administrative de dyskinésie tardive ne prescrit pas un anticholinergique ; pas code automatique sur toute posture.',
 'Consensus international MDS 2025, DOI10.1002/mds.30220 : classification et terminologie, pas directive nationale américaine ni protocole pharmacologique exhaustif. Texte CC BY-NC-ND ; aucune figure adaptée/importée.',
 'Distribution 2025 : généralisée pas simple seuil>3régions, tronc pas toujours requis. Exemples tronc+deux régions ou trois/quatre membres hors hémidystonie. Cou/épaules focal par convention ; douleur/anxiété seules ne rendent pas combinée.',
 'HUG page de service mise à jour8juillet2026 ; USZ information clinique19février2026 et page thérapeutique sans version explicite. Pas guidelines nationales de doses. Estimation USZ40/100000 pas enquête nationale G24.',
 'ESDE, pas ESEMED : résumé primaire viaEuropePMC seulement, PMID11127535, DOI10.1007/s004150070094. Dystonie primaire repérée en cliniques adultes de huit pays1996–1997, prévalence152/million, sous-détection et variabilité de méthode ; ni incidence ni données suisses2026.',
 'Arbres ERN publiés2février2026 : adulte révisé2025, branche enfant fondée sur2015. Deux pages effectivement vues ; version du document ne rend pas chaque branche scientifiquement nouvelle.',
 'Algorithme thérapeutique ERN actualisé4juin2025 avec figure source2018 copyrightSpringer, non importée ni adaptée. Options listées ne prouvent pas toutes efficacité, autorisation suisse ou indication pour chaque population.',
 'AWMF1septembre2026 = Anmeldung v5.0, pas nouvelle guideline achevée. Deux PDF DGN2021 ont renvoyé500 et miroir public403 ; aucun contournement et aucune lecture intégrale fictive.',
 'Revue ERN/EJN2026 monogénique, DOI10.1111/ene.70490 : génétique avant stimulation et mesures pré/post, avec hétérogénéité, données manquantes et risque de biais non quantifiable globalement. Pas taux universel de succès ou garantie individuelle.',
 'EASL-ERN2025 Wilson, cache partagé G22 mais lectures propres G24 de diagnostic et p708 réellement vue : traitement causal et symptomatique complémentaires, preuves souvent observations. Pas traitement anti-cuivre au seul codeG24. BorneREC divergente non publiée dans G24.',
 'BOTOX FI mai2025, Xeomin FI mars2026, Dysport FI mai2026 : unités spécifiques, pas substitution mécanique. Disponibilité de chaque emballage non affirmée.',
 'BOTOX cervical adulte première≤200U, total≤300U,≤50U/site, SCM≤100U/nonbilatéral, intervalle≥10semaines ; blépharo>12ans initial≤25U/œil et total≤100U/12semaines. Pas dose cervicale enfant extrapolée.',
 'Xeomin dystonies adultes : cervical usuellement≤200U, maximum300U,≤50U/site et intervalle≥8semaines. Blépharo initial≤25U/œil,total≤100U. Myasthénie/Lambert-Eaton CI ; indication sialorrhée pédiatrique ne devient pas indication dystonique enfant.',
 'Dysport cervical adulte500U initial puis250–500U, plafond500U de cette FI suisse, SCM≤300U ; adapter si maigreur/âge/hypotrophie, intervalle≥12semaines. Blépharo40U/œil initial,max120U/œil. Pas plafond cervical1000U importé d’un autre pays.',
 'BOTOX/Dysport maladies neuromusculaires sous précautions spécialisées versus CI Xeomin ; rédaction des CI non harmonisée silencieusement. Diffusion, aspiration, faiblesse, hypersensibilité et interactions de transmission neuromusculaire vérifiées.',
 'Exemple fictif Dysport500U+2,5mL=200U/mL, quantité40U déjà retenue=0,2mL. Calcul ne choisit ni dose, ni muscle, ni fréquence ; préparation, solvant et conservation restent spécifiques.',
 'Akineton FI mai2022 : adulte aigu2,5–5mg IM/IV très lente, répétition30min si besoin,max10–20mg/j ;5mg/mL donc2,5mg=0,5mL si dose déjà choisie. Oral non médicamenteux début2mg puis hausse2mg/semaine, entretien spécialisé ; plafond Parkinson16mg pas universel, retardmax12mg et ne pas fractionner/écraser.',
 'Akineton peut aggraver dyskinésie tardive ; cognition/charge anticholinergique, CI, grossesse/allaitement et absence d’expérience rénale/hépatique attribués. Pas très haute dose ou dose pédiatrique automatique, pas anticholinergique devant toute rigidité confuse/fébrile.',
 'Madopar FI juin2023 : indication parkinsonienne sauf médicamenteuse et CI<25ans. Essai pédiatrique de dopa-sensibilité spécialisé pas application automatique de cette FI ; aucune dose universelle ni substitution de produit inventée.',
 'Paspertin FI janvier2020, sixième FI causale : métoclopramide peut causer dystonie/crise oculogyre même après une dose, notamment enfant/adulte jeune ; formes tardives et syndrome malin distincts. Maximum général5jours, indications pédiatriques propres, CI<1an ; aucune dose antiémétique recommandée dans G24.',
 'UniProt/Swiss-Prot GCH1 etTH entrées humaines révisées2septembre2026 : science biochimique normale, pas protocole clinique. Formulation de base sans effets secondaires non recopiée ; pigment H&E ne mesure pas dopamine/BH4/GCH1.',
 'OpenStax américain utilisé seulement en science normale, aucune image importée ni recommandation clinique américaine utilisée comme fondement. Pas barrière immunitaire absolue ou raccourci ATP recopié.',
 'Cinq originaux humains effectivement vus et droits propres vérifiés ; pixels inchangés, dix occurrences/34repères HTML. Photo JamesHeilman2010 avec consentement verbal/écrit de publication et CC déclaré, patient décrit médicamenteux sans agent/dose/génotype. Photo au nom Writer’s Cramp rejetée car plateau de film.',
 'Gray384 coupe humaineC6 etGray764 voie humaine, édition1918 ; AndrewGillies2005 deux niveaux coronaux ; Tulemo2021 neurone humain H&E,barre20µm,statut clinique donneur inconnu. Planches de référence, pas lésions diagnostiques ni guide de trajectoire d’aiguille.',
 f'Six sciences {words} mots, neuf rubriques sémiologiques avec lienshttps et marqueur clinique sur prose.66fenêtres/14Pareto/quatre cas/quiz,1440/390 etLivre24px réellement exercés ; navigateur local HTTP intercepté et autres requêtes avortées, aucun déploiement public revendiqué.',
 'Cas/quiz originaux fictifs, pas items officiels fédéraux ; bandeau partagé S08 hérité et compteurs hors mandat. Identifiants GCH1,BH4,SNAP-25 préservés par espaces textuels explicites, aucune règle générique chiffre-vers-lettre.',
 'Incident sparse hérité G21 : premier start conservé sans conformité rétroactive, restauration complète/propre seulement G24 puis second start et claim réels. Incident de message Betta17:26:29 prématuré corrigé17:26:58 après vrai passage ; aucune rédaction canonique avant Betta réel, preuves et tests distincts conservés.',
 'Cours scellés et réserves historiques conservés : N02 typographie/génération refusée,N04/N29sémiologie,N00actualisation,E40lienClaML,N17concurrent. Aucun catalogue ou moteur partagé modifié ; aucune PR/main.'
]
checks=[
 'OFS G24 et sous-codes, exclusions et inclusion tardive ; code distinct de décision thérapeutique.',
 'Consensus2025 : définition, phénoménologie, deux axes, distribution révisée et isolée/combinée ; pas preuve sur anxiété ou IRM normale seule.',
 'Sources CH puis européennes et consensus international attribués ; versions ERN2026/branche2015 et schéma2018 réédité2025 explicites ; AWMF inscription seule.',
 'Épidémiologie ESDE historique/résumé et USZ estimation publique sans fausse incidence suisse actuelle.',
 'Cinq FI thérapeutiques et une causale exactes : unités, doses, intervalles, âges, CI/precautions et reproduction conservés.',
 'BOTOX/Xeomin/Dysport intervalles cervicaux10/8/12semaines ; plafond suisse Dysport500U, pas conversion de puissance.',
 'Bipéridène aigu versus nonmédicamenteux oral/retard, risques cognitifs et tardifs, rein/foie données absentes ; pas hautes doses universelles.',
 'Dopa-sensibilité pédiatrique spécialisée distinguée de CI Madopar<25ans ; Wilson causal/symptomatique, pas traitement sur code seul.',
 'Calcul Dysport500U/2,5mL et40U=0,2mL, Akineton2,5mg/5mg/mL=0,5mL ; exercices après choix clinique, pas prescription.',
 'Cinq originaux humains, licences et consentement déclaré photo ; anatomie/échelles/contextes et limites réellement examinés.',
 f'Six sciences {words} mots, neuf sémiologie et sept règles natives ;66fenêtres/14Pareto/quatre quiz/cas,dix occurrences/34repères,1440/390,Livre24px et absence de débordement horizontal.'
]
base=dict(reviewer='astra_nephrologie',production_name='Sol-Neurologie-G24',runtime_name='sol_nephrologie',model='gpt-6.1-sol',reasoning='high',mode='self_review',independent=False,reviewed_at=now,canonical_files=files,glossary_sha256=final['glossary/g24.py'],preview_sha256=ph,medical_human_validation=False,clinical_certification=False,requirements_reviewed=dict(fundamental_analytical_semiology=True))
reviews={}
for kind in ['medical','language','visual_desktop','visual_mobile']:
 j=dict(base)
 if kind=='medical':j.update(scope='Auto-relecture des six surfaces finales et passages ciblés ; aucune revue médicale indépendante revendiquée.',checks=checks,limitations=limits)
 elif kind=='language':j.update(scope='Auto-relecture du français, unités, négations, populations, fenêtres, quiz et légendes.',checks=['Définition → syndrome → cause → décision, avec versions et populations attribuées.','GCH1,BH4,SNAP-25 et identifiants scientifiques préservés ; espaces explicites de mots/unités, pas règle générique chiffre-vers-lettre.','ESDE distinct d’ESEMED, définitions2025 et intervalles de produit non fusionnés.','Cibles du glossaire et66fenêtres résolues, réponses de quiz rédigées sans sigles cliquables parasites.'],limitations=limits[:2])
 else:
  width=1440 if kind=='visual_desktop' else 390
  j.update(scope=f'Chromium {width}px sur aperçu natif autonome final.',checks=next(v for v in browser['viewports'] if v['width']==width),visual_inspection='Captures ouverture, cinq originaux annotés, sémiologie, fenêtre et Livre24px réellement examinées par IA ; positions et légendes relues sans diagnostic inventé.',limitations=limits[-4:])
 h=save('reviews/'+kind+'.json',j);reviews[kind]=dict(path='reviews/'+kind+'.json',reviewer='astra_nephrologie',mode='self_review',sha256=h)
anchors=['g24-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]
semio=dict(base,kind='SEMIO',requirement='fundamental_analytical_semiology',status='closed',source_files_sha256=files,reviewed_files_sha256=final,unresolved_blockers=[],section_anchors=anchors,evidence=['audit-sciences.json','browser-report.json','source-ledger.json'],findings='Neuf rubriques substantielles, lienshttps, premier sous-onglet et titre/aria exacts, marqueur clinique sur prose. Contrôle ciblé de structure distinct de self_review médical, sans validation humaine.')
sh=save('reviews/SEMIO.json',semio);images=[]
for f in rights['figures']:
 p=O/'images'/Path(f['path']).name;p.parent.mkdir(exist_ok=True);shutil.copyfile(R/f['path'],p);images.append(dict(f,path=str(p.relative_to(O)),canonical_path=f['path'],medical_review='Original et repères effectivement vus ; auto-relecture IA Sol-Neurologie-G24, sans certification médicale humaine.'))
def section_sources(a):return list(dict.fromkeys(''.join(str(x) for x in link.find_all(string=True)).split(' — ')[0] for link in soup.find(id=a).select('a[data-reference-source]')))
titles=['Définition','Épidémiologie','Physiopathologie','Démarche clinique','Anamnèse','Examen clinique','Syndromes','Diagnostic positif','Explorations','Arbre diagnostique et différentiels','Prise en charge','Prévention, suivi et pronostic','Points clés','Pièges'];monograph=[]
for i,t in enumerate(titles,1):
 q=soup.find(id=f'g24-{i}');text=' '.join(str(x) for x in q.find_all(string=True));monograph.append(dict(point=i,title=t,anchor=f'g24-{i}',sources=section_sources(f'g24-{i}'),coverage_explanation=text[:500]))
rt=['Question clinique/enjeu fédéral','Définition/périmètre CIM','Classifications','Épidémiologie','Normal vers pathologique','Étiologies/risques','Anamnèse/symptômes','Examen clinique','Urgences','Examens','Différentiels','Prise en charge suisse','Complications/pronostic','Suivi/prévention','Populations particulières','Spécificités suisses','Critères formels','Paramètres chiffrés','Sous-codes','Examen fédéral']
ra=['g24-question','g24-1','g24-7','g24-2','g24-semio-normal','g24-3','g24-5','g24-6','g24-4','g24-e-purpose','g24-10','g24-11','g24-12','g24-12','g24-p-causal','g24-p-plan','g24-8','g24-p-calculation','g24-1','g24-entrainement']
af={a:p for p in files for a in re.findall(r'\bid="([^"]+)"',(R/p).read_text())};matrix=[];rubrics=[]
for i,(title,a) in enumerate(zip(rt,ra),1):
 assert a in af;ss=section_sources(a);assert ss
 ev=[dict(file=af[a],anchor=a)]+[dict(file='source-ledger.json',source_id=sid,json_pointer='/sources/'+str(next(k for k,x in enumerate(ledger['sources']) if x['id']==sid))) for sid in ss]
 matrix.append(dict(point=i,title=title,status='covered',evidence=ev,coverage_scope='Contenu pédagogique et limites attribuées, sans certification clinique.'));rubrics.append(dict(rubric=i,title=title,anchor=a,content_present=True,current_verification='Auto-relecture des octets finaux et limites attribuées.'))
save('matrice-20.json',dict(code='G24',matrix20=matrix))
save('findings-final.json',dict(code='G24',reviewed_at=now,blocking_findings=[],corrected_findings=['Héritage réorganisé en14points/20rubriques/sixsciences/neufsémiologie avec sources réellement lues.','Anatomies SVG héritées remplacées par cinq originaux humains licenciés, pixels inchangés et annotationsHTML.','Classification2025, doses et intervalles suisses distincts, fenêtre d’âge Madopar explicite ; pas fausse nouveauté AWMF2026.','Photo de film rejetée, données et méthode ESDE corrigées, identifiants scientifiques conservés.','Incidents sparse et message Betta prématuré conservés et corrigés avec événements réels, sans conformité rétroactive.'],transparent_limits=limits))
save('lesson-manifest.json',dict(code='G24',author='astra_nephrologie',production_name='Sol-Neurologie-G24',active_specialty='mouvements anormaux',runtime_name='sol_nephrologie',recorded_at=now,branch='codex/alpha77/g24-integrate-g1',base='8a512893acbab9caa0dcfdd0e8682a44ea72fda6',monograph=monograph,medina_rubrics=rubrics,matrix20=matrix,sources=ledger['sources'],images=images,semiology=dict(section_anchors=anchors),scientific_subtabs=['Sémiologie fondamentale et analytique','Anatomie','Histologie','Physiologie','Biochimie','Immunologie et physiopathologie'],reviews=reviews,audits=dict(MED=reviews['medical'],LANG=reviews['language'],SEMIO=dict(path='reviews/SEMIO.json',sha256=sh)),blocking_findings=[],medical_human_validation=False,clinical_certification=False,tokens_actual=None,cost_actual=None,canonical_files=files,source_glossary_sha256=final['glossary/g24.py'],catalogue_entry_sha256=sha(R/'chapters.json'),preview=dict(path=preview,sha256=ph),limitations=limits,closure_status='self_reviewed_project_delivery_not_clinically_certified'))
save('source-binding.json',dict(code='G24',verified_at=now,preview=preview,preview_sha256=ph,final_sources=final,checks=['test-static.txt','audit-sciences.json','browser-report.json','figures-rights.json','findings-final.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json','reviews/SEMIO.json'],clinical_certification=False))
(O/'README.md').write_text(f'# G24 — Sol-Neurologie-G24\n\n14 points, 20 rubriques, 41 lectures ciblées/réutilisations, cinq FI thérapeutiques et une causale, six sciences de {words} mots, neuf rubriques sémiologiques, cinq originaux humains, dix occurrences/34 repères, 66 fenêtres/14 Pareto/quatre cas et quiz. Aperçu : G24-apercu-autonome.html.\n\nAuto-relectures IA self_review, sans validation médicale humaine ni revue indépendante globale. Contrôles ciblés distincts. Sources complètes hors Git ; métadonnées et paraphrases publiées. Limites dans findings-final.json. Incidents sparse et message Betta prématuré conservés sans conformité rétroactive. Aucun autre cours, catalogue ou moteur partagé modifié ; aucune PR/main ni publication publique.\n')
print('G24 : manifeste14/20 et première liaison finale créés.')
