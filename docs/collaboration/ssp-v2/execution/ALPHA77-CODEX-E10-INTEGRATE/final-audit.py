from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,shutil
from lxml import html
OUT=Path(__file__).parent
RAW=Path('/workspace/scratch/E10-integrate-sources')
BASE='3131a5cbf6cc003ead358e25152073959c53c4d9'
now=datetime.now(timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
core=[f'chapters/E10/E10_{x}.html' for x in ['a','b','c','d','pop1','pop2']]+['glossary/e10.py']
paths=core+['assets/img/e10/alpha/codex/e10-ketogenesis-original.jpg']
base={p:sha(subprocess.check_output(['git','show',BASE+':'+p])) for p in core}
final={p:sha(Path(p).read_bytes()) for p in paths}
notice='Révision Alpha en cours : certaines réserves thérapeutiques et sources héritées restent à vérifier ; les audits finaux de cette version ne sont pas clos.'
assert notice in html.fromstring(Path(core[0]).read_text()).text_content()
claims=[]
def read(id,fn,start,length,url,publisher,version,section,population,limits,locations):
 s=(RAW/(fn+'.txt')).read_text();i=s.index(start);passage=s[i:i+length]
 claims.append(dict(id=id,source_id=fn,url=url,publisher=publisher,version=version,consulted_at=now,reading_method='Lecture ciblée indépendante du texte de source acquis localement; pas réattribution de la lecture auteur',section=section,actual_passage=passage,text_sha256=sha(s.encode()),population=population,limitations=limits,locations=locations,reading_level='section'))
read('FINAL-PREG-ASPART','S5','Grossesse, allaitement',1280,'https://amiko.oddb.org/fr/fi?gtin=7680550450024','Swissmedic/AIPS via AmiKo','avril 2026','Grossesse/allaitement','Diabète et grossesse','Pas de pourcentage universel de modification de dose',['e10-a11-partie-4'])
read('FINAL-PREG-DEGLUDEC','S6','Grossesse, allaitement',1520,'https://amiko.oddb.org/fr/fi?gtin=7680625620017','Swissmedic/AIPS via AmiKo','décembre 2024','Grossesse/allaitement','Type1 et grossesse','Traitement envisagé sur indication clinique; allaitement déconseillé dans cette FI',['e10-a11-partie-4'])
read('FINAL-PREG-SSED','S1','There is an increased hypoglycemia rate early in pregnancy',760,'https://www.sgedssed.ch/SgedSsed/fileadmin/6_Diabetologie/61_Empfehlungen_Facharzt/2025_Swiss_Diabetes_and_Technology_Recommendations_inkl_Table_E.pdf','SSED','25 février 2025','p24, conclusion pregnancy','Grossesse sous insuline','La synthèse propose bien des pourcentages, retirés ici de la prescription générique au profit des FI exactes',['e10-a11-partie-4'])
read('FINAL-QUALITY','QUALITY2017','HbA1c',1700,'https://www.sgedssed.ch/SgedSsed/fileadmin/6_Diabetologie/64_Ressourcen_Hausarzt/Diabetes_Kriterien_2017_SGED_def.pdf','SSED','23 août 2017','Tableau de critères, page unique','Diabète en premier recours','Critères de qualité populationnels anciens; ne prouve pas un échéancier individuel actuel type1',['e10-a09','e10-a11'])
read('FINAL-CLASSIFICATION','S8','1.1.1',2540,'https://www.nice.org.uk/guidance/ng17/chapter/Recommendations','NICE','NG17, amendements 2022','1.1.1–1.1.9','Adultes','Complément européen; pas protocole pédiatrique ou organisation NHS importée',['e10-semio-signs','e10-semio-interpretation','e10-semio-differentials'])
read('FINAL-DKA','S9','Diagnosis of DKA\n',500,'https://abcd.care/sites/default/files/site_uploads/JBDS_Guidelines_Current/JBDS_02_DKA_Guideline_with_QR_code_March_2023.pdf','JBDS','mars 2023','p10, critères','Adultes hospitalisés','Trois composantes réunies; critères attribués, distincts de la fiche RMS',['e10-semio-interpretation'])
read('FINAL-EXAM','S9','Differential diagnosis\nIt',3000,'https://abcd.care/sites/default/files/site_uploads/JBDS_Guidelines_Current/JBDS_02_DKA_Guideline_with_QR_code_March_2023.pdf','JBDS','mars 2023','p12, differentials et bedside monitoring','Adultes hospitalisés','Méthode et qualité analytique; pas nouvelle posologie',['e10-semio-examination','e10-semio-differentials'])
read('FINAL-HYPO','S2','En cas de suspicion',430,'https://www.hug.ch/vdoc/HUG_000000812.pdf','HUG','2 septembre 2022','p1 suspicion','Adulte hospitalisé','Protocole institutionnel; doses hospitalières historiques hors périmètre de cette relecture',['e10-semio-signs','e10-semio-urgency'])
read('FINAL-RMS','RMS','Critères de suspicion clinique',850,'https://www.revmed.ch/view/415288/3626033/RMS_639_449.pdf','Revue Médicale Suisse','2019','p449, suspicion et prise en charge initiale','Ambulatoire suisse','Règle de triage; ne permet pas exclusion d’une forme euglycémique',['e10-semio-urgency'])
read('FINAL-PHYSIOLOGY','FIG6','The pancreatic exocrine function',520,'https://med.libretexts.org/Bookshelves/Anatomy_and_Physiology/Anatomy_and_Physiology_1e_%28OpenStax%29/Unit_3%3A_Regulation_Integration_and_Control/17%3A_The_Endocrine_System/17.09%3A_The_Endocrine_Pancreas','OpenStax via LibreTexts','13 mai 2022','Figure1 et endocrine pancreas','Physiologie générale','Source pédagogique pour mécanismes; aucune recommandation thérapeutique américaine',['e10-semio-normal','e10-semio-mechanisms'])
read('FINAL-KETOGENESIS','PMC8656040','The release of fatty acids',1400,'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8656040/fullTextXML','Kolb et al., BMC Medicine','2021','Ketogenesis, figure1','Physiologie','Revue mécanistique; pas régime proposé type1',['e10-semio-mechanisms'])
read('FINAL-GLUCAGON','S7','Indications/Possibilités',1250,'https://amiko.oddb.org/fr/fi?gtin=7680674650010','Swissmedic/AIPS via AmiKo','mars 2026','Indication et posologie','Diabète dès1an','Produit nasal exact, pas transfert à glucagon injectable',['e10-p02'])
dump(OUT/'final-claim-mapping.json',dict(actor='Codex',code='E10',kind='independent_final_source_reading',medical_human_validation=False,claims=claims,failed_access=[dict(url='https://www.medix.ch/wissen/guidelines/endokrinologie/diabetes-mellitus/',result='HTTP301 redirect loop lors du contrôle final; aucune lecture revendiquée')]))
findings=[dict(id='FINAL-PREGNANCY',status='resolved',severity='MAJEUR',finding='Les pourcentages génériques de modification insulinique pendant la grossesse ne reposaient pas sur une FI du produit exact. Retirés de A11; adaptation individuelle sourcée NovoRapid/Tresiba.',evidence=['final-claim-mapping.json#FINAL-PREG-ASPART','final-claim-mapping.json#FINAL-PREG-DEGLUDEC','chapters/E10/E10_b.html#e10-a11-partie-4']),dict(id='ALPHA1-M01-M05-L01',status='resolved',finding='Corrections vasculaire, urgence, digestif, cétogenèse et unités présentes. Les débits IV humains sans FI sont retirés; aucun débit aspart substitué.',evidence=['reprise-propositions.json','correction-insuline-iv.json','claim-mapping.json']),dict(id='FOLLOWUP2017',status='non_blocking',finding='Le document suisse2017 a été effectivement rouvert; HbA1c au moins2/an, rein/pieds au moins1/an, yeux au moins tous2ans confirmés comme critères populationnels2017.',evidence=['final-claim-mapping.json#FINAL-QUALITY']),dict(id='SEMIO-CONTRACT',status='resolved',finding='Premier onglet, neuf sections, clinique pA, chaînes mécanisme→signe→mesure→décision et limites présents. Vérification frontend réelle jointe.',evidence=['chapters/E10/E10_c.html#e10-s-semio','browser-check.json','source-verification.json']),dict(id='REMAINING-SOURCES',status='open',severity='MAJEUR',finding='Restent : OFS applicable, stades présymptomatiques et épidémiologie type1, confirmation diagnostique asymptomatique suisse actuelle, échéancier individuel actuel, remboursement2026, revalidation exhaustive biochimie/immunologie héritées et figures historiques autres que6/8/9. Les sources relues ne ferment pas ces lacunes.',evidence=['rapport.md#matrice-de-complétude-et-réserves','figures-provenance.json','final-claim-mapping.json#failed_access'])]
evidence=[dict(type='source_passages',path=str(OUT/'final-claim-mapping.json'),sha256=sha((OUT/'final-claim-mapping.json').read_bytes()),actual_passages=claims),dict(type='frontend',path=str(OUT/'browser-check.json'),sha256=sha((OUT/'browser-check.json').read_bytes()),scope='Chromium1360et390; premieronglet, sixsélections, neufsections, Entrée/Espace, popup,24px,Livre'),dict(type='verification',paths=['final-build.log','final-static.log','source-verification.json'],limitation='audit_sciences historique en échec conservé; aucune modification du test partagé')]
for kind in ['MED','SEMIO']:
 report=dict(schema_version=1,actor='Codex',code='E10',kind=kind,status='provisional',medical_human_validation=False,reviewer_role='auditeur médical final IA distinct de l’auteur/intégrateur',reviewed_at=now,base_sha=BASE,source_files_sha256=base,reviewed_files_sha256=final,requirements_reviewed=dict(fundamental_analytical_semiology=True),findings=findings,evidence=evidence,unresolved_blockers=[notice],review_scope='Relecture ciblée indépendante des corrections Alpha1, de la sémiologie nouvelle et de la pharmacologie; pas certification exhaustive de chaque assertion/figure historique.')
 if kind=='SEMIO':report['requirement']='fundamental_analytical_semiology'
 dump(OUT/(kind+'.json'),report)
# Refresh deliveries and all pre-existing source hash metadata to final bytes.
for p in paths:
 d=OUT/'delivery'/p;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,d)
f=json.loads((OUT/'source-files.json').read_text())
for r in f['source_files']:r['sha256']=r['snapshot_sha256']=final[r['path']]
f['final_med_semio_audit']='provisional';dump(OUT/'source-files.json',f)
for name in ['source-verification.json','build-evidence.json']:
 f=json.loads((OUT/name).read_text());f['source_files_sha256']=final
 if name=='build-evidence.json':
  f['built_file']='/workspace/scratch/e10-final-render/fragments/MEDINA_S05_endocrinien-metabolique.html';f['sha256']=sha(Path(f['built_file']).read_bytes());f['command']='MEDINA_OUT=/workspace/scratch/e10-final-render python3 build_front.py --fragment S05'
 dump(OUT/name,f)
dump(OUT/'final-hashset.json',dict(base_sha=BASE,source_files_sha256=base,reviewed_files_sha256=final,hashset_sha256=sha(json.dumps(final,sort_keys=True,separators=(',',':')).encode())))
# Evidence manifest excludes itself, no circular hashes.
dump(OUT/'evidence-files.json',dict(schema_version=1,generated_at=now,source_files_sha256=final,evidence_files=[dict(path=str(p),sha256=sha(p.read_bytes())) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name not in ['evidence-files.json','LANG.json','lang-final-proposals.json'] and 'publication-evidence' not in p.parts]))
print('final reports provisional; final hashset',json.loads((OUT/'final-hashset.json').read_text())['hashset_sha256'])
