from pathlib import Path
from bs4 import BeautifulSoup
import json,hashlib,datetime,re,shutil
R=Path(__file__).resolve().parents[5];O=Path(__file__).resolve().parent;now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,j):p=O/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');return sha(p)
ledger=json.loads((O/'source-ledger.json').read_text());rights=json.loads((O/'figures-rights.json').read_text());browser=json.loads((O/'browser-report.json').read_text());assert browser['passed']
files={str(p.relative_to(R)):sha(p) for p in sorted((R/'chapters/N05').glob('*.html'))};final=dict(files);final['glossary/n05.py']=sha(R/'glossary/n05.py')
for f in rights['figures']:final[f['path']]=sha(R/f['path'])
preview='N05-apercu-autonome.html';ph=sha(O/preview);raw='\n'.join((R/p).read_text() for p in files);(O/'monographie-source.html').write_text(raw);soup=BeautifulSoup(raw,'html.parser')
limits=[
'Auto-relectures Sol explicites self_review ; aucune validation humaine ni revue médicale indépendante globale. Les revues ciblées restent distinctes de cette livraison.',
'33 lectures ciblées/réutilisations attribuées du même bloc N02/N03 et nouvelles lectures N05 distinguées ; pas 33 documents intégralement lus. Textes complets hors Git, seuls métadonnées et paraphrases publiés.',
'Aucune incidence suisse directe N05 retenue. Données MRC, IRA ou biopsie non transformées en fréquence de ce libellé sans précision.',
'Page officielle AKI/AKD consultée : projet2026 encore préparé pour publication ; dernière directive adoptée trouvée2012 repriseCUEN2025. Extraction fournisseur acquise30octobre2026 ; pas preuve absolue d’absence de publication ultérieure. Ni projet ni diapositivesFinal utilisés comme directive adoptée.',
'SGN17.03.2025 pour MRC suisse établie ; systolique120–129 individualisée distincte deKDIGO<120standardisé. Ces cibles ne deviennent pas celles d’une urgence ou d’une fonction instable.',
'SixFI exactes : RamiprilZentiva décembre2021,Cosaar avril2025,Forxiga août2026,Norvasc avril2023,Lasix40 oral mai2025 et ampoule20mg mars2025. Indications,populations,voies et contre-indications distinctes ; néphroprotection conditionnelle après clarification/stabilisation.',
'Pas d’immunosuppression universelle surN05. Syndrome,temporalité,fonction,lésion et cause séparés ; complications traitées sans attendre la précision finale.',
'Cinq originaux humains vus, neuf occurrences/30repèresHTML ; pixels inchangés. LePAS en croissant ne démontre pas la fluorescenceIgG rapportée par sa provenance et ne mesure pas la trajectoire du patient.',
'Pas de droit universel déduit pourLS,OFSP,AI,Suva ou aptitude. PDFKDIGO2024 direct403 : texte fournisseur horsGit, empreinte de texte distincte duPDF.',
'Bandeau hérité shellSSP63 alors que l’hématurie relèveSSP64 dansPROFILES2017 ; métadonnée partagée horsmission, réserve signalée au parent. Aucun ancien cours ou moteur partagé modifié.',
'Chromium local surHTTPintercepté,toutes autres requêtes avortées ; ne prouve aucun déploiement public ni validation clinique.'
]
checks=[
'Quatorze points,examens,sixsciences/neufsections sémiologiques,sixFI,34fenêtres/14Pareto et4quiz relus avec populations et limites.',
'OFSN05 : néphrite/glomérulonéphrite/glomérulopathieSAI ; distinctionN28.9sansmorphologie etN12tubulo-interstitiel ; dixsuffixes morphologiques aprèsconclusionclinique.',
'Sans précision ne prouve ni bénignité ni étiologie ; pas detoutecréatinineélevée=N05. Aigu/chronique/aigusurchronique recherchés ; seuilMRC3mois jamais délai imposé aux soins.',
'IRA :≥26,5µmol/L48h,≥1,5fois7jours oudiurèse<0,5mL/kg/h6h ; uncritèresuffit. Fonctioninstable : équations non traitées comme mesureinstantanée ; critèresIRA ne donnent pas la cause.',
'Hyperkaliémie/ECG,acidose,surcharge etsyndromepulmonaire–rénal : évaluationurgente. Épurationpourmenaceclinique,pascréatinineseule. Pasprotocoleimmuneuniversel.',
'HUG2024 dysmorphie>60%/acanthocytes>5%/cylindres, sensibilitélimitée ;26/µLlocal distinctCUEN10/µL, méthodesetunitésattribuées.',
'Biopsie : cause,activité,chronicité et techniquescomplémentaires. CroissantPAS,fluorescence etprogressionrapide nonconfondus ; rechercheinfectieuse etimmunologieorientées.',
'Ramipril néphropathie>3g/j :1,25→max5mg/j ; HTAmax10 distinct ; organes,enfant,grossesse etARNI36h. Cosaar indicationrénaleT2DHTA+ACR≥300,50→100,25hypovolémie.',
'ForxigaMRCadult10mg/j,introductionnonrecommandée<25 malgréclasse20 ;foiesévère5→10 ;limitesimmunosuppression,dialyse/greffe ;grossesse etchirurgie≥3joursavecplanreprise. Norvasc5→10,prudencefoie,enfantnonextrapolé,simvastatine20.',
'Lasixoralmai2025 distinctIVmars2025 :oral20–80début/20–40entretien ;IV≥15ans20–40,+20toutes2h ;OAP40puis20–40à20min ;≤4mg/min,≤2,5siCr>5mg/dL. EnfantIVcritique1mg/kgmax20/j distinctoral2mg/kgmax40/j. Plafond1500exceptionnel,anurie/volume/NaK etallaitementCI ;pasKautomatique.',
'COL4A3/COL4A4/COL4A5/CYP3A4 préservés ;espacementciblé,sansrègle généraleséparant chiffres/lettres. N02historique intact.',
'Premieragrégatnavigateur attendait33repèresN03 ;inventaireN05réel30, attente corrigée puis parcoursfinalréel auxdeuxlargeurs.'
]
base=dict(reviewer='astra_nephrologie',runtime_name='sol_nephrologie',model='gpt-6.1-sol',reasoning='high',mode='self_review',independent=False,reviewed_at=now,canonical_files=files,glossary_sha256=final['glossary/n05.py'],preview_sha256=ph,medical_human_validation=False,clinical_certification=False,requirements_reviewed=dict(fundamental_analytical_semiology=True))
reviews={}
for kind in ['medical','language','visual_desktop','visual_mobile']:
 j=dict(base)
 if kind=='medical':j.update(scope='Auto-relecture des six surfaces finales et passages ciblés/sixFI ; aucun audit indépendant revendiqué.',checks=checks,limitations=limits)
 elif kind=='language':j.update(scope='Auto-relecture français,unités,négations,populations,fenêtres,quiz,légendes et nomenclatures.',checks=['Progression syndrome→gravité→temporalité→cause→plan.','Unités/voies,cadresMRC/IRA et statutdeprojet attribués.','Concaténations corrigées sans altérerCOL4A3/4/5,CYP3A4 ou identifiants.','Sources desfenêtres tirées deleurssections, sanssourceuniqueinsuffisante.'],limitations=[limits[0]])
 else:
  width=1440 if kind=='visual_desktop' else 390;j.update(scope=f'Chromium{width}px HTTPintercepté suraperçufinal.',checks=next(v for v in browser['viewports'] if v['width']==width),visual_inspection='Cinq originaux réellement vus puis capturesouverture,figures/repères,fenêtre,Livre24px examinées ;9occurrences/30repères,6onglets,34fenêtres et4quiz.',limitations=limits[-2:])
 h=save('reviews/'+kind+'.json',j);reviews[kind]=dict(path='reviews/'+kind+'.json',reviewer='astra_nephrologie',mode='self_review',sha256=h)
anchors=['n05-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]
semio=dict(base,kind='SEMIO',requirement='fundamental_analytical_semiology',status='closed',source_files_sha256=files,reviewed_files_sha256=final,unresolved_blockers=[],section_anchors=anchors,evidence=['audit-sciences.json','browser-report.json','source-ledger.json'],findings='Neufsections substantielles,premierongletvisible,scienceversclinique/examen/traitement ;navigationexclusive/aria/clavier et1440/390 réellementcontrôlés. Auto-relecture sansvalidationhumaine.')
sh=save('reviews/SEMIO.json',semio)
images=[]
for f in rights['figures']:
 p=O/'images'/Path(f['path']).name;p.parent.mkdir(exist_ok=True);shutil.copyfile(R/f['path'],p);images.append(dict(f,path=str(p.relative_to(O)),canonical_path=f['path'],medical_review='Originaux et annotations effectivement vus parSol ; auto-relecture sanscertificationmédicalehumaine.'))
titles=['Définition','Épidémiologie','Physiopathologie','Démarche clinique','Anamnèse','Examen clinique','Syndromes','Diagnostic positif','Explorations','Arbre diagnostique et différentiels','Prise en charge','Prévention,suivi etpronostic','Points clés','Pièges']
exp=['Profilnéphritique décrit puis séparé de l’informationmanquante, de lacause et ducode ; exclusionsOFS etlimites expliquées.','Absenced’incidenceN05directe conservée ; MRCglobale et sériesdebiopsies ne deviennent pas une fréquenceinventée dececadre.','Filtrenormal,perméabilité,filtration,rétention et lésions reliés auxsignes ; deuxoriginaux attribués et limitesPAS expliqués.','Sécurisation,datation,localisation et recherchedecauses avecplan decontrôle ; aucun délaiadministratif ne retarde uneurgence.','Chronologie,urines,volume,signessystémiques,infection,famille,médicaments etterrain orientent leshypothèses avecdonnéesdatées.','Pression,volume,respiration etmanifestationsguidées confrontés ; objectifsMRC/urgence,populations etfragilité distincts.','Syndromes,temporalité,IRA,MRC,CGA etmorphologie comparés commeaxescomplémentaires, avecunités etlimitesdefonctioninstable.','Preuvedessignes,fonctiondatée,causes etincertitudes explicites ; critèresIRAadoptés et statutprojet2026attribués séparément.','Biologie,urines,imagerie,immunologie,infection,tissu etgénétique répondent àdesquestions ;urgenceprogressionrapide etlimitesconservées.','Arbrepargravité,réalité,compartiment,durée,cause etplan ;discordances etdiagnosticsassociés rouvrentl’enquête.','Complicationsmenaçantes traitées sansattentefinale ;traitementcausal,volume,pression etnéphroprotectionconditionnelle avecsixFIexactes.','Suiviréduitincertitudes,documenterécupération/séquelles etrisque ;repèresMRC,prévention etpopulationsne remplacentpasurgence.','Synthèseclinique parsyndrome,gravité,hypothèses etplan ;PROFILES/MEBEKO,quatrecas etquatrequizoriginaux sansstatutofficiel.','Raccourcis surgravité,temporalité,codage,croissants,corticoïdes,diurèse,voies etprojetdocumentaire corrigés avecconséquences.']
urlmap={x['url']:[] for x in ledger['sources']}
for x in ledger['sources']:urlmap[x['url']].append(x['id'])
def section_sources(a):return list(dict.fromkeys(z for a in soup.find(id=a).select('a[data-reference-source]') for z in urlmap[a['href']]))
monograph=[dict(point=i,title=t,anchor=f'n05-{i}',sources=section_sources(f'n05-{i}'),coverage_explanation=exp[i-1]) for i,t in enumerate(titles,1)]
rt=['Questionclinique/enjeufédéral','Définition/périmètreCIM','Classifications','Épidémiologie','Normalverspathologique','Étiologies/risques','Anamnèse/symptômes','Examenclinique','Urgences','Examens','Différentiels','Priseenchargesuisse','Complications/pronostic','Suivi/prévention','Populationsparticulières','Spécificitéssuisses','Critèresformels','Paramètreschiffrés','Sous-codes','Examenfédéral']
ra=['n05-question','n05-1','n05-7','n05-2','n05-semio-normal','n05-10','n05-5','n05-6','n05-4','n05-e-urines','n05-10','n05-11','n05-12','n05-12','n05-p-populations','n05-p-populations','n05-8','n05-e-fonction','n05-annexe-cim','n05-13']
af={a:p for p in files for a in re.findall(r'\bid="([^"]+)"',(R/p).read_text())};matrix=[];rubrics=[]
for i,(title,a) in enumerate(zip(rt,ra),1):
 assert a in af;ids=section_sources(a);assert ids
 ev=[dict(file=af[a],anchor=a)]+[dict(file='source-ledger.json',source_id=sid,json_pointer='/sources/'+str(next(k for k,x in enumerate(ledger['sources']) if x['id']==sid))) for sid in ids]
 matrix.append(dict(point=i,title=title,status='covered',evidence=ev,coverage_scope='Contenu pédagogique et limites présents,sanscertificationclinique.'));rubrics.append(dict(rubric=i,title=title,anchor=a,content_present=True,current_verification='Auto-relecture desoctetsfinaux et limitesexplicites.'))
save('findings-final.json',dict(code='N05',reviewed_at=now,blocking_findings=[],corrected_findings=['Attentenavigateur héritée33repères remplacée par inventaireN05réel30 ; premièrepreuveconservée et passefinaleréexécutée.','Espacement cibléunités/sigles,sansséparation desnomenclaturesscientifiques.'],transparent_limits=limits))
save('lesson-manifest.json',dict(code='N05',author='astra_nephrologie',runtime_name='sol_nephrologie',recorded_at=now,branch='codex/alpha77/n05-integrate-g1',base='8a512893acbab9caa0dcfdd0e8682a44ea72fda6',monograph=monograph,medina_rubrics=rubrics,matrix20=matrix,sources=ledger['sources'],images=images,semiology=dict(section_anchors=anchors),scientific_subtabs=['Sémiologie fondamentale et analytique','Anatomie','Histologie','Physiologie','Biochimie','Immunologie'],reviews=reviews,audits=dict(MED=reviews['medical'],LANG=reviews['language'],SEMIO=dict(path='reviews/SEMIO.json',sha256=sh)),blocking_findings=[],medical_human_validation=False,clinical_certification=False,tokens_actual=None,cost_actual=None,canonical_files=files,source_glossary_sha256=final['glossary/n05.py'],catalogue_entry_sha256=sha(R/'chapters.json'),preview=dict(path=preview,sha256=ph),limitations=limits,closure_status='self_reviewed_project_delivery_not_clinically_certified'))
save('source-binding.json',dict(code='N05',verified_at=now,preview=preview,preview_sha256=ph,final_sources=final,checks=['test-static.txt','audit-sciences.json','browser-report.json','figures-rights.json','findings-final.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json','reviews/SEMIO.json'],clinical_certification=False))
(O/'README.md').write_text('# N05 — Syndrome néphritique, sans précision\n\nAperçu autonome : N05-apercu-autonome.html, ouvert parHTTPintercepté.\n\n14points,20rubriques,6sciences,9sectionssémiologiques,33lecturesciblées/réutilisationsattribuées,6FI,5originauxhumains,9occurrences/30repères,34fenêtres et4quiz. Auto-relectures explicites,sansvalidationmédicalehumaine niPR/main.\n\nSourcescomplètes horsGit ;métadonnées/paraphrases danssource-ledger.json. Limites/corrections : findings-final.json. AKI/AKD2026projet distinctduréférentieladopté. RéserveSSP63shell/SSP64PROFILES horsmissionpartagée,signaléeauparent.\n')
print('N05 manifeste14/20 et source-bindingfinal créés ; aucune certificationclinique.')
