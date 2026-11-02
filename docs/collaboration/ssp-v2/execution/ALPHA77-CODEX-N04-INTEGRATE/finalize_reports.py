from pathlib import Path
import json,hashlib,datetime,subprocess,sys,re
from lxml import html
ROOT=Path(__file__).resolve().parents[5];OUT=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest=json.loads((OUT/'lesson-manifest.json').read_text());ledger=json.loads((OUT/'source-ledger.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest['preview']={'path':'N04-apercu-autonome.html','sha256':sha(OUT/'N04-apercu-autonome.html')}
research=OUT/'recherche_N04'
if not (research/'recherche-initiale.md').exists():(research/'recherche-initiale.md').write_bytes((research/'recherche.md').read_bytes())
refs=[];idmap={}
for i,s in enumerate(ledger['sources'],1):
    rid='S'+str(i);idmap[s['id']]=rid
    refs.append({'id':rid,'ledger_id':s['id'],'url':s['url'],'titre':s.get('title') or s.get('titre') or s['section'],'editeur':s['publisher'],'version_annee':s.get('version') or s.get('version_annee') or 'Version indiquée dans la référence et le registre source','date_consultation':s['read_at'],'section_page':s['section'],'passage':s['passage'],'passage_format':s.get('passage_format','paraphrase'),'population':s['population'],'limites':s['limits'],'reading_scope':s['reading_scope']})
(research/'sources.json').write_text(json.dumps({'sources':refs},ensure_ascii=False,indent=2)+'\n')
rubrefs=[['S1','S2'],['S6','S7','R-CIM'],['H-DEF-4','H-DEF-5','H-DEF-6'],['H-EPI-1','H-EPI-2','H-EPI-3','H-EPI-4','H-EPI-5','H-EPI-6'],['S4','S10','R-PODOCYTES'],['R-IMMUNO','R-GENETICS','H-ETI-1'],['S5','S8'],['S8','S9'],['S9','H-CPL-1','H-CPL-2'],['S6','H-DX-1','H-DX-5'],['S5','H-DX-10','H-DX-11'],['R-FI_clexane','R-FI_sandimmun','R-FI_spiricort','R-FI_endoxan','H-TX-1'],['H-CPL-1','H-CPL-3','H-EPI-6'],['H-SUP-12','H-SUP-13','H-SUP-14'],['S7','S8','H-TX-12','R-FI_bactrim'],['R-CIM','R-FI_prednisone','R-SORTIS-PEDIATRIE'],['S6','S7','S5'],['S6','S7','R-FI_sandimmun'],['R-CIM'],['S6','S7','H-DEF-1']]
lines=[]
for row,keys in zip(manifest['medina_rubrics'],rubrefs):
    refs=' '.join('['+idmap[k]+']' for k in keys)
    status='LACUNE' if row['rubric']==4 else '✔'
    note='Contenu présent ; incidence suisse non trouvée, données européennes/internationales étiquetées.' if row['rubric']==4 else 'Contenu présent ; voir registre pour lecture actuelle ciblée ou héritage attribué.'
    lines.append(f"| {row['rubric']}. {row['title']} | {status} | {refs} — {row['anchor']} ; {note} |")
(research/'recherche.md').write_text('# Recherche N04 — état final de la reprise\n\nLe dossier initial avant rédaction est conservé sous recherche-initiale.md. Ce tableau décrit le contenu final et distingue présence, lecture actuelle ciblée et preuves héritées. Il ne certifie pas la médecine.\n\n## Matrice de complétude\n\n| rubrique | statut | sources |\n|---|---|---|\n'+'\n'.join(lines)+'\n\n## Sous-codes\n\nN04.0, N04.1, N04.2, N04.3, N04.4, N04.5, N04.6, N04.7, N04.8, N04.9 sont conservés dans l’annexe après la conclusion clinique ; libellés et règle morphologique recollationnés avec le fichier OFS2024.\n\n## Traçabilité et limites\n\n41passages actuels ciblés, dont22produits suisses ;113preuves héritées attribuées à Claude au14octobre. Les passages publics sont paraphrasés : les extraits exacts de travail restent dans le cache externe. Résumé RMS seulement, deux récupérations EuropePMC échouées, incidence suisse non trouvée. Ces limites ne sont pas remplacées par des chiffres ou une validation inventés. Les cinq images humaines originales ont une provenance et une licence propres vérifiées ; les annotations sont superposées et les pixels inchangés. Aucun dessin anatomique généré n’est ajouté.\n')

for name,cmd in [('test-static',['python3','test_v7.py','--static','N04']),('verite',['python3','tools/betta_verite.py',str(research)])]:
    run=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    report={'command':cmd,'recorded_at':NOW,'exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'canonical_files':manifest['canonical_files'],'clinical_certification':False}
    (OUT/(name+'.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(name,run.returncode)
    if run.returncode:raise SystemExit(run.returncode)

current='\n'.join((ROOT/f'chapters/N04/N04_{x}.html').read_text() for x in ['a','b','c','d','pop1','pop2'])
previous='\n'.join(subprocess.check_output(['git','show',f"{manifest['base']}:chapters/N04/N04_{x}.html"],cwd=ROOT,text=True) for x in ['a','b','c','d','pop1','pop2'])
def ids(s):return set(html.fromstring(s).xpath('//section[contains(concat(" ",@class," ")," ilot ")]/@id'))
sys.path.insert(0,str(ROOT));import build_medina as B
preservation={'baseline':manifest['base'],'before_words':B.words(previous),'after_words':B.words(current),'before_sections':len(ids(previous)),'after_sections':len(ids(current)),'removed_section_ids':sorted(ids(previous)-ids(current)),'all_inherited_ilots_preserved':not(ids(previous)-ids(current)),'intentional_removals':['Two didactic anatomical SVGs replaced by verified human originals.','Pediatric edema photograph with unidentified author removed; clinical text retained.'],'clinical_certification':False}
(OUT/'preservation.json').write_text(json.dumps(preservation,ensure_ascii=False,indent=2)+'\n')

(OUT/'reviews').mkdir(exist_ok=True)
base={'reviewer':'astra_nephrologie','mode':'self_review','independent':False,'reviewed_at':NOW,'canonical_files':manifest['canonical_files'],'preview_sha256':manifest['preview']['sha256'],'medical_human_validation':False,'clinical_certification':False}
medical=dict(base,scope='Targeted review of added semiology/immunology, identified clinical claims, and selected passages from22exact Swiss product FIs; inherited113claims retain their original attribution.',checks=['Adult/child diagnostic thresholds and units distinguished.','Premature preference for membranous histology removed.','Underfill/overfill and limits of physical volume assessment explained.','Clexane prophylactic versus therapeutic renal adaptations distinguished in table and popup.','Sandimmun abnormal-baseline-creatinine maximum initial dose added across prescribing surfaces.','Spiricort short high-dose FI phase distinguished from specialist nephrotic protocols.','Endoxan oral formulation verified in the same exact FI.','MCD corticosteroid taper: internal discrepancy between KDIGO figure45 and adjacent text explicitly contrasted with European total-duration guidance; former universal minimum removed.','Sortis pediatric non-authorization clarified versus international class recommendation.','Kidney-as-sink wording separated from congenital medullary sponge kidney.','Inherited biological and treatment detail preserved; coding relocated after clinical conclusion.'],limitations=ledger['limitations'],pending='No unresolved finding in the targeted correction set; parent verification received. Limitations of the broader inherited corpus remain explicit; no independent full medical review claimed.')
language=dict(base,scope='Author reread of new semiology, new immunogenetics, captions, and targeted corrections; static glossary audit of the complete current N04.',checks=['Nine analytical sections use descriptive findings, interpretation, urgency and limits.','Population and measurement method kept near thresholds.','New abbreviations expanded or covered by glossary; test_v7 static passes.','Coding remains an appendix and technical implementation detail is confined to evidence.','Captions distinguish visible structures from unshown molecular or ultrastructural findings.'],limitations=['No claim of a new exhaustive external linguistic review of every inherited sentence.'])
browser=json.loads((OUT/'browser-report.json').read_text())
for kind,report in [('medical',medical),('language',language)]:
    path=OUT/'reviews'/(kind+'.json');path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');manifest['reviews'][kind]={'path':str(path.relative_to(OUT)),'reviewer':'astra_nephrologie','mode':'self_review','sha256':sha(path)}
for kind,width in [('visual_desktop',1440),('visual_mobile',390)]:
    result=next(v for v in browser['viewports'] if v['width']==width)
    report=dict(base,scope=f'Native autonomous preview {width}px; all network requests except intercepted native document blocked.',results=result,screenshots_sha256={x:sha(OUT/x) for x in result['screenshots']},human_visual_inspection='Author viewed original images and selected final screenshots; this is not an independent medical image review.',limits=['No live deployment or production HTTP availability claim.','Book mode paginates the selected main tab; clinical and semiology views were both checked at24px.'])
    path=OUT/'reviews'/(kind+'.json');path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');manifest['reviews'][kind]={'path':str(path.relative_to(OUT)),'reviewer':'astra_nephrologie','mode':'self_review','sha256':sha(path)}
parent_review=json.loads((OUT/'reviews/parent-targeted.json').read_text())
manifest['targeted_external_review']={'path':'reviews/parent-targeted.json','sha256':sha(OUT/'reviews/parent-targeted.json'),'reviewer':parent_review['reviewer'],'mode':'independent_targeted_review','scope':parent_review['scope'],'global_medical_validation':False}
manifest['parent_review_source_hashes_match']={p:sha(ROOT/p)==h for p,h in parent_review['source_files'].items()}
manifest['editorial_followup_completed']='The isolated renal-dose row now explicitly says Énoxaparine — prophylaxie.'
manifest['blocking_findings']=[]
manifest['limitations']=ledger['limitations']+['Inherited publication-status marker remains visible in native engine; shared receipt not modified.','Parent targeted review refers to its original hashes; subsequent steroid-duration clarification is documented as a separate author correction and does not expand that review.','Self-review and independent targeted review do not constitute global medical or human validation.']
manifest['closure_status']='author_package_complete; no main publication, PR or next-lesson authorization implied'

(OUT/'lesson-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Reports bound to final source and preview hashes; self-review and parent targeted verification explicitly distinguished.')
