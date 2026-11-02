"""Consignation manuelle après inspection effective. Jamais appelée par la veille."""
from pathlib import Path
import datetime, hashlib, json, shutil, sys
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not (OUT/'source-binding.json').exists(), 'Reçu existant : aucun renouvellement'
v=read(OUT/'verification.json')
assert v['ok'] and all(c['passed'] for c in v['checks'])
for n,h in v['final_sources'].items(): assert sha(ROOT/n)==h,n
assert sha(ROOT/'chapters.json')==v['catalog_sha256']
assert sha(OUT/'D65-apercu-autonome.html')==v['preview_sha256']
assert read(OUT/'semiology-final.json')['passed']
browser=read(OUT/'browser-report-autonomous.json')
assert not browser['errors']
for b in browser['viewports']:
    assert len(b['windows_checked'])==40 and len(b['quiz_checked'])==4
    assert len(b['originals_checked'])==3 and len(b['causal_diagrams_checked'])==7
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
captures=['D65-1440-accueil.png','D65-1440-semio.png','D65-1440-d65-science-sem-legende.png','D65-390-d65-science-sem-legende.png','D65-1440-d65-science-blood.png','D65-390-d65-science-blood-legende.png','D65-1440-d65-calcul-fib-popup.png','D65-390-d65-calcul-txa-popup.png','D65-390-d65-causal-consumption.png','D65-390-d65-causal-bio.png','D65-390-d65-causal-immuno.png','D65-390-quiz-dose.png','D65-1440-semio-body-final.png','D65-390-semio-body-final.png','D65-1440-annotations-livre24-final.png','D65-390-annotations-livre24-final.png']
captures=['captures/'+n for n in captures]
visual={'code':'D65','recorded_at':now,'actually_seen':True,'mode':'self_review','reviewer':'Codex Hématologie','preview_sha256':v['preview_sha256'],'captures':captures,'sha256':{n:sha(OUT/n) for n in captures},'clinical_certification':False,'notes':['Douze captures finales inspectées ; les cinq modifiées par la correction des espaces ont été revues, sept empreintes sont restées identiques (visual-hash-comparison.json).','Quatre captures supplémentaires de sémiologie et des repères en Livre24 vues le 2 novembre après17:42UTC. Une sortie antérieure tronquée ne sert pas de preuve visuelle.','Repères adjacents lisibles à17px et24px, pixels des deux originaux conservés. Les barres fixes et le boutonPlan hérités peuvent recouvrir une portion des longues captures mobiles ; défilement nécessaire.','Titres et crédits en légende plus petits ; corps des annotations dans un bloc natif distinct. Aucune revue humaine indépendante.']}
write(OUT/'visual-inspection.json',visual)
plan=read(OUT/'recherche_D65/plan.json')
mono=[{'point':r['point'],'title':r['title'],'status':'covered','anchor':r['anchor'],'sources':r['sources'],'coverage_explanation':r['coverage']} for r in plan['monographic_plan']]
anchors=['d65-4','d65-1','d65-7','d65-2','d65-s-semio','d65-2','d65-5','d65-6','d65-4','d65-e-1','d65-7','d65-p-1','d65-2','d65-12','d65-12','d65-12','d65-14','d65-13','d65-1','d65-14']
matrix=[{'point':r['point'],'title':r['title'],'status':'covered','anchor':a,'sources':r['sources'],'evidence':'Rubrique enseignée avec références et limites explicites ; ne signifie pas disponibilité de toutes les données quantitatives.','research_status_preserved':r['status']} for r,a in zip(plan['matrix20'],anchors)]
write(OUT/'monograph-14.json',{'code':'D65','points':mono})
write(OUT/'matrix-20.json',{'code':'D65','rubrics':matrix,'meaning':'covered = rubrique traitée, y compris lacune déclarée ; aucune note médicale20/20.'})
coverage='# Couverture finale D65\n\nPlan monographique respecté ; pas de certification médicale.\n\n|Point|Rubrique|Ancre|Couverture|\n|---|---|---|---|\n'
for r in mono: coverage+=f'|{r["point"]}|{r["title"]}|{r["anchor"]}|{r["coverage_explanation"]}|\n'
coverage+='\n## Matrice20\n\n|Point|Rubrique|Ancre|Limite conservée|\n|---|---|---|---|\n'
for r in matrix: coverage+=f'|{r["point"]}|{r["title"]}|{r["anchor"]}|{r["research_status_preserved"]}|\n'
(OUT/'coverage-final.md').write_text(coverage)
limits_text=[
 'Quatre revues obligatoires effectuées en self_review par le parent ; une revue distincte IA limitée à quatre questions est conservée séparément. Aucune validation humaine.',
 'Incidence nationaleD65, fréquences des symptômes et performances isolées non établies par la recherche ; lacunes explicites, sans extrapolation de cohortes.',
 'ScoreISTH2025 : diagnostic manifeste avec cause compatible, pas prescription ; SIC réservé au contexte septique, pas score universel précoce.',
 'FIHaemocomplettanavril2026 et cibles obstétricales ne formulent pas le même objectif ; divergence explicitée, décision spécialisée et protocole local.',
 'Kybernin : indication héréditaire de laFI lue, sans transposition automatique à laCIVD acquise ; absence de médicament universel démontré.',
 'HNF : indicationFI et exception à la contre-indication hémorragique ne constituent pas un protocole curatif universel ; thromboprophylaxie et traitement séparés.',
 'TXA : majorité desCIVD exclue, exception spécialisée d’hyperfibrinolyse prédominante avec saignement sévère ; voieIVexclusive, débit et contre-indications conservés.',
 'Trauma, obstétrique etAPL ont des objectifs distincts ; pas de protocole pédiatrique exhaustif ni de doseATRA/antibiotique improvisée.',
 'Deux photographies de structures sanguines, pas images diagnostiques deCIVD. Statut clinique des sujets non établi par les notices ; pixels intacts et repères français adjacents.',
 'Sept schémas causaux non anatomiques sourcés ; aucune anatomie dessinée parIA.',
 'Tab/Entrée fonctionne ; navigation par flèches absente du moteur hérité. Les barres fixes peuvent recouvrir une partie des captures mobiles longues, surtout enLivre24.',
 'PROFILES88/152/174 vérifiés dans les passages2017 ; compteurs globaux du frontend hérité ne constituent pas des statistiques de cette campagne.',
 'Aperçu testé parHTTP intercepté sans accès externe ; aucun déploiement ni testfile:// revendiqué.',
 'Délais de conduite, Suva et garanties de remboursement spécifiquesD65 non établis ; revue utilisateur avant toutePR/main. Tokens et coûts non mesurés.'
]
limits=[{'id':f'D65-L{i}','text':t,'blocking':False} for i,t in enumerate(limits_text,1)]
points=[
 'D65.0/.1/.2/.9 et exclusions obstétricales/néonatales expliqués ; codage et mécanisme clinique distingués.',
 'ISTH2025 : Ddimères strictement>3/>7LSN, exactement7 donne2points ; PTprolongé en secondes, fibrinogène<1g/L, total≥5 avec cause compatible.',
 'SIC : total≥4 ET plaquettes+INR>2, quatre domainesSOFA ; fibrinogène normal ou élevé n’exclut pas la phase précoce.',
 'Normal→pathologique : compartimentation, endothélium, facteur tissulaire, thrombine, fibrine, anticoagulants et fibrinolyse ; neuf unités sémiologiques reliées aux examens.',
 'DifférentielsMAT, foie, dilution/perte et anticoagulants sans règle exclusiveVIII/rein ; schizocytes non spécifiques et urgence contextuelle.',
 'Source du sepsis à contrôler, recommandation2026 contextualisée ; causalité, soutien des organes et hémostase traités en parallèle.',
 'Haemocomplettan20mg/mL, initial1–2g individualisés, maximum5mL/min ; 2g=100mL≥20min. LibelléFI sur limite inférieure normale200–450mg/dL et divergence obstétricale explicités.',
 'Kybernin50UI/mL, maximum4mL/min, dose30–50UI/kg dans indication héréditaire ; pas routineCIVD ni formule mal imprimée reproduite.',
 'HNF : prévention et curatif distincts, risqueTIH/saignement/terrain ; aucune injectionIM et aucune réexposition ancienne transformée en règle actuelle.',
 'TXA100mg/mL IV≤1mL/min ; 1g≥10min. ExceptionCIVD étroite, CI rénale sévère et neuraxiales, pas tableauFI utilisé pour annuler uneCI.',
 'Seuil diagnostique1g/L, trauma≤1,5g/L et cible obstétricale2–2,5g/L ne sont pas interchangeables ; APL30–50G/L et100–150mg/dL restent attribués à ce contexte.',
 'Deux originaux effectivement vus et légendes finales inspectées ; aucune normalité clinique ni activation plaquettaire quantitative déduite de la photo.',
 'Corrections avant liaison : abréviations, espaces, repères mobile ; tentative de styleenligne refusée puis remplacée par composant natif autorisé. Échecs conservés et tests repassés.'
]
pack=OUT/'review-package';pack.mkdir(exist_ok=True)
(pack/'content.html').write_text('\n'.join((ROOT/n).read_text() for n in v['final_sources'] if n.startswith('chapters/D65/') and n.endswith('.html')))
review={'code':'D65','reviewer':'Codex Hématologie','mode':'self_review','reviewed_at':now,'source_snapshot':v['final_sources'],'catalog_sha256':v['catalog_sha256'],'preview_sha256':v['preview_sha256'],'clinical_certification':False,'medical':{'scope':'Relecture ciblée des décisions, mécanismes et doses rédigés ; pas revue humaine exhaustive.','points_checked':points,'blocking_findings':[],'limitations':limits},'language':{'scope':'Terminologie, calculs, unités, formulations conditionnelles et espaces ; absence absolue d’erreur non garantie.','findings_fixed':['Abréviations locales et références explicites.','Espaces et signes de ponctuation corrigés et relus.','Légendes reformulées sans diagnostic clinique déduit des images.']},'visual_desktop':{'scope':'Captures sélectionnées1440px et parcours interactif distinct.','captures':[n for n in captures if '-1440-' in n]},'visual_mobile':{'scope':'Captures sélectionnées390px, sémiologie, repères, calculs, schémas etLivre24.','captures':[n for n in captures if '-390-' in n]},'captures_inspected':captures,'verification':{'windows_per_viewport':40,'quizzes_per_viewport':4,'science_tabs':6,'semiology_sections':9,'originals':2,'original_occurrences':3,'caption_markers':12,'non_anatomical_causal_diagrams':7,'browser_errors':[],'source_binding_preexisting':False}}
write(pack/'self-review.json',review)
images=[]
for x in read(ROOT/'assets/img/d65/alpha/codex/provenance.json')['images']:
 src=ROOT/x['file'];shutil.copyfile(src,pack/src.name)
 images.append({'path':'review-package/'+src.name,'source_path':x['file'],'title':x['title'],'original_url':x['source_url'],'author':x['credit'],'license':x['license'],'license_url':x['license_url'],'sha256':sha(src),'changes':'Pixels intacts ; repères français adjacents.','annotations':x['annotations'],'medical_review':'Self_review, aucune validation humaine.'})
sources=[]
for x in read(OUT/'recherche_D65/sources.json')['sources']:
 sources.append({'id':x['id'],'url':x['url'],'publisher':x['editeur'],'title':x['titre'],'read_at':x['date_consultation'],'section':x['section_page'],'passage':x['passage_paraphrase'],'population':x['population'],'limits':x['limites'],'reading_depth':x['niveau_lecture'],'cache_sha256':x['cache_sha256'],'reuse_attributed':x.get('reuse_attributed'),'read_in_this_lesson':x.get('read_in_this_lesson'),'additional_read_reference':'recherche_D65/additional-research.json'})
target=pack/'targeted-review-sol-endocrinologie.json'
assert target.exists()
manifest={'code':'D65','author':'Codex Hématologie','monograph':mono,'matrix20':matrix,'matrix20_reference':'matrix-20.json','sources':sources,'images':images,'semiology':{'section_anchors':['d65-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]},'reviews':{k:{'path':'review-package/self-review.json','sha256':sha(pack/'self-review.json'),'reviewer':'Codex Hématologie','mode':'self_review'} for k in ['medical','language','visual_desktop','visual_mobile']},'targeted_external_review':{'path':'review-package/targeted-review-sol-endocrinologie.json','sha256':sha(target),'reviewer':'/root/sol_endocrinologie','mode':'targeted_distinct_ai_review','scope':'ScoreISTH2025, Haemocomplettan, Kybernin etTXA ; ni revue complète ni validation humaine.'},'blocking_findings':[],'limitations':limits,'clinical_certification':False,'closure_status':'ready_for_project_gate_and_user_review'}
write(OUT/'lesson-manifest.json',manifest);write(pack/'lesson-manifest.json',manifest);write(OUT/'images-provenance.json',images)
sys.path.insert(0,'/workspace/Medina-harness/harness')
import medina_harness
check=medina_harness.validate_lesson(OUT)
write(OUT/'contract-validation.json',check)
assert check['technical_contract_pass'],check
write(OUT/'source-binding.json',{'code':'D65','verified_at':v['finished_at'],'reviewed_at':now,'preview':'D65-apercu-autonome.html','preview_sha256':v['preview_sha256'],'final_sources':v['final_sources'],'checks':['verification.json','browser-report-autonomous.json','sciences-final.json','semiology-final.json','visual-inspection.json','book24-check.json','coverage-final.md','recherche_D65/recherche.md','recherche_D65/additional-research.json','review-package/targeted-review-sol-endocrinologie.json'],'clinical_certification':False})
print(json.dumps({'reviewed_at':now,'manifest_sha256':sha(OUT/'lesson-manifest.json'),'binding_sha256':sha(OUT/'source-binding.json'),'preview_sha256':v['preview_sha256'],'clinical_certification':False,'completed':False}))
