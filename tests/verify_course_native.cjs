/* Generic course native popup checks, including in-memory justification injection.
 * No build, content edits or external downloads. This does not validate medicine.
 * MEDINA_NATIVE_CODE=I50 node tests/verify_course_native.cjs (or pass the code).
 * MEDINA_CHROMIUM_PATH selects Chromium; MEDINA_QA_CAPTURE=1 saves sample captures.
 */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {execFileSync}=require('node:child_process');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const root=path.resolve(__dirname,'..');
const code=process.env.MEDINA_NATIVE_CODE||process.argv[2]||'I50';
assert.match(code,/^[A-Z]\d{2}(?:\.\d+)?$/,'Code CIM invalide');
const folder=path.join(root,'chapters',code),bankFile=path.join(folder,code+'_justifications.json');
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'audits/MECANISMES_2026-10-07',code.toLowerCase()+'_native_browser'));
const directory=path.resolve(process.env.MEDINA_FRAGMENTS||path.join(root,'dist/fragments'));
let file,sources;
const selector='.mc[data-code="'+code+'"]';
const normal=s=>String(s).replace(/\u00ad/g,'').normalize('NFC').replace(/\s+/g,' ').trim();
const digest=value=>crypto.createHash('sha256').update(value).digest('hex');
const checks=[],failures=[],errors=[],viewports=[],citations=[],captures=[],inputs=[];
const report={code,route:'#/entry/'+code,
 scope:'Technical interaction checks only. The original consuming fragment is discovered from compiled organisation metadata. Every native green direct trigger on desktop and mobile; breadth-first search determines paths to all canonical and injected templates, then every authored nested trigger is clicked with a return to each parent. Expected titles and complete authored text, except computed Pareto ratios, come from canonical HTML with tools/insert_justifications.load_course_justifications applied in memory, never from the compiled course DOM. Shared external templates are reported separately and use their compiled title and text only for their interaction check. This does not validate medicine or exhaustive medical justification.',
 external_downloads:false,checks,failures,errors,inputs,viewports,citations,captures};
function check(label,ok,detail){assert.ok(ok,label+(detail===undefined?'':': '+JSON.stringify(detail)));checks.push(label)}
function originalFragment(){
 const candidates=[];
 for(const name of fs.readdirSync(directory).filter(name=>name.endsWith('.html'))){const candidate=path.join(directory,name),html=fs.readFileSync(candidate,'utf8');
  const embedded=html.match(/<script[^>]*id="medina-category-organisation-data"[^>]*>([\s\S]*?)<\/script>/);if(!embedded)continue;
  const organisation=JSON.parse(embedded[1]);
  for(const block of organisation.blocks||[])for(const lesson of block.lessons||[])if(lesson.code===code&&lesson.integrated&&!lesson.reference&&lesson.source_fragment_id===organisation.fragment.id)candidates.push({file:candidate,lesson,fragment:organisation.fragment});
 }
 check(code+' : un fragment original compilé',candidates.length===1,candidates.map(candidate=>({file:path.relative(root,candidate.file),fragment:candidate.fragment.id})));
 const chosen=candidates[0];report.lesson=code+' — '+chosen.lesson.title;report.fragment=chosen.fragment.label;report.fragment_id=chosen.fragment.id;return chosen.file;
}
function expectedSources(){
 const program=`import json,sys\nfrom pathlib import Path\nroot,code,folder=Path(sys.argv[1]),sys.argv[2],Path(sys.argv[3])\nsys.path.insert(0,str(root/'tools'))\nfrom insert_justifications import load_course_justifications\nraw={p.name:p.read_text(encoding='utf-8') for p in sorted(folder.glob('*.html'))}\nloaded=load_course_justifications(code,folder)\ntransformed,templates,injection=loaded if loaded else (raw,'',None)\nbank_path=folder/(code+'_justifications.json')\nbank=json.loads(bank_path.read_text(encoding='utf-8')) if bank_path.exists() else None\nprint(json.dumps({'sources':[{'name':name,'html':transformed[name]} for name in sorted(transformed)],'justification_templates':templates,'injection':injection,'injected_ids':[entry['id'] for entry in bank['entries']] if bank else []},ensure_ascii=False))`;
 const expected=JSON.parse(execFileSync('python3',['-c',program,root,code,folder],{cwd:root,encoding:'utf8',maxBuffer:16*1024*1024,env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'}}));
 check(code+' : sources attendues injectées en mémoire',expected.sources.length===sources.length&&expected.sources.every(source=>sources.some(file=>path.basename(file)===source.name)));
 report.expectation={provider:'tools/insert_justifications.load_course_justifications',canonical_html_sources:sources.map(source=>path.relative(root,source)),injection:expected.injection,injected_ids:expected.injected_ids};
 if(fs.existsSync(bankFile))check(code+' : toute la banque injectée',!!expected.injection&&expected.injection.entries===expected.injected_ids.length&&expected.injection.windows===expected.injected_ids.length&&expected.injected_ids.every(id=>expected.justification_templates.includes('data-pop="'+id+'"')));
 return expected;
}
async function attempt(label,operation,page){
 try{await operation()}catch(error){failures.push({label,error:String(error.stack||error)});console.error(JSON.stringify({failed:label,error:String(error.message||error)}))}
 finally{if(page&&!page.isClosed()&&await page.locator('.mc-dlg[open]').count())await page.keyboard.press('Escape')}
}
function snapshotInputs(){
 for(const input of [file,...sources,...(fs.existsSync(bankFile)?[bankFile]:[])]){check('Entrée présente : '+path.relative(root,input),fs.existsSync(input));const bytes=fs.readFileSync(input);inputs.push({path:path.relative(root,input),bytes:bytes.length,sha256_before:digest(bytes)})}
}
function finishInputs(){
 for(const input of inputs){const absolute=path.join(root,input.path);input.sha256_after=fs.existsSync(absolute)?digest(fs.readFileSync(absolute)):null;input.stable=input.sha256_before===input.sha256_after;
  if(input.stable)checks.push('Entrée stable : '+input.path);else failures.push({label:'Entrée modifiée pendant le contrôle',path:input.path,before:input.sha256_before,after:input.sha256_after})}
}
async function course(page){
 await page.goto(pathToFileURL(file).href+'#/entry/'+code);await page.waitForFunction(()=>window.MDN_READY===true);
 await page.locator(selector).waitFor();
 if(await page.locator('.mc.book').count())await page.locator('.mc-book').click();
}
// Adapted from verify_justifications_recovery.cjs: reveal through actual course tabs.
async function reveal(page,index){
 const trigger=page.locator(selector+' [data-k]').nth(index);
 const context=await trigger.evaluate(el=>({panel:el.closest('.mc-panel')?.id,science:el.closest('.mc-sci')?.id,
  hiddenFeedback:el.closest('.mc-fb')?.hidden,quiz:[...el.closest('.mc').querySelectorAll('.mc-quiz')].indexOf(el.closest('.mc-quiz'))}));
 if(context.panel)await page.locator('.mc-tabs button[data-p="'+context.panel+'"]').click();
 if(context.science)await page.locator('.mc-sci-bar button[data-s="'+context.science+'"]').click();
 if(context.hiddenFeedback&&context.quiz>=0)await page.locator(selector+' .mc-quiz').nth(context.quiz).locator('.mc-opt[data-ok="1"],button[data-ok="1"]').first().click({position:{x:8,y:8}});
 await trigger.scrollIntoViewIfNeeded();await trigger.waitFor({state:'visible'});return trigger;
}
async function closeAndFocus(page,trigger,label){
 await page.keyboard.press('Escape');await page.locator('.mc-dlg').waitFor({state:'hidden'});
 await page.waitForFunction(el=>document.activeElement===el,await trigger.elementHandle());
 check(label+' : Escape ferme et restitue le focus',await trigger.evaluate(el=>document.activeElement===el));
}
async function triggerClean(trigger,label){
 const attributes=await trigger.evaluate(el=>({ab:el.getAttribute('data-ab'),nested:el.querySelectorAll('[data-ab]').length,tag:el.tagName,role:el.getAttribute('role'),tabindex:el.tabIndex,key:el.dataset.k}));
 check(label+' : déclencheur accessible sans data-ab parasite',(attributes.tag==='BUTTON'||attributes.role==='button'&&attributes.tabindex>=0)&&attributes.ab===null&&attributes.nested===0,attributes);
}
async function overflow(page,label){
 const sizes=await page.evaluate(()=>{const dialog=document.querySelector('.mc-dlg[open]'),body=dialog?.querySelector('.mc-dlg-b'),r=dialog?.getBoundingClientRect();
  return {viewport:innerWidth,document:document.documentElement.scrollWidth,dialog:r?{x:r.x,width:r.width}:null,body:body?{width:body.clientWidth,scroll:body.scrollWidth}:null}});
 check(label+' : page sans débordement horizontal',sizes.document<=sizes.viewport+1,sizes);
 if(sizes.dialog)check(label+' : fenêtre sans débordement horizontal',sizes.dialog.x>=-1&&sizes.dialog.x+sizes.dialog.width<=sizes.viewport+1&&sizes.body.scroll<=sizes.body.width+1,sizes);
}
async function clickCitation(page,link,label){
 const expected=await link.getAttribute('href'),url=new URL(expected).href.split('#')[0],context=page.context();
 const request=context.waitForEvent('request',{predicate:r=>r.isNavigationRequest()&&r.url().split('#')[0]===url,timeout:10000});
 const popup=page.waitForEvent('popup',{timeout:10000});
 const before=await dialogState(page);await link.click();
 const [navigation,tab]=await Promise.all([request,popup]);
 check(label+' : citation ouvre son URL HTTPS',navigation.url().split('#')[0]===url);
 await tab.close();await page.bringToFront();
 check(label+' : citation conserve la fenêtre parente',JSON.stringify(await dialogState(page))===JSON.stringify(before));
 citations.push({label,url,navigation_observed:true,external_downloaded:false});
}
async function dialogState(page){
 return page.locator('.mc-dlg[open]').evaluate(dialog=>({title:dialog.querySelector('#mc-dlg-t').textContent,body:dialog.querySelector('.mc-dlg-b').textContent}));
}
// Glossary navigation is separate from canonical/injected template text checks.
// It supplies a real nested interaction even when authored templates have no child data-k.
async function glossaryNavigation(page,trigger,rootKey,label,width,summary){
 if(summary.glossary_navigation.length)return false;
 const child=page.locator('.mc-dlg[open] .mc-dlg-b [data-ab],.mc-dlg[open] .mc-dlg-h [data-ab]').first();
 if(!await child.count())return false;
 const abbreviation=await child.getAttribute('data-ab'),parent=await dialogState(page);
 check(label+' : glossaire imbriqué accessible',await child.evaluate(el=>el.getAttribute('role')==='button'&&el.tabIndex>=0),abbreviation);
 await child.click();await page.locator('.mc-back:not([hidden])').waitFor({state:'visible'});
 const title=normal(await page.locator('.mc-dlg[open] #mc-dlg-t').innerText()),body=normal(await page.locator('.mc-dlg[open] .mc-dlg-b').innerText());
 check(label+' : définition de la bonne abréviation',title.startsWith(normal(abbreviation)+' — ')&&body.length>40&&!body.includes('Fiche absente.'),{abbreviation,title});
 if(width===390)await overflow(page,label+' / glossaire');
 await page.locator('.mc-back').click();check(label+' : Retour du glossaire conserve titre et texte parent',JSON.stringify(await dialogState(page))===JSON.stringify(parent));
 check(label+' : Retour du glossaire masqué à la racine',await page.locator('.mc-back').isHidden());
 // Reopen through the same native trigger; Escape must clear the nested stack and focus the course trigger.
 await child.click();await page.locator('.mc-back:not([hidden])').waitFor({state:'visible'});await closeAndFocus(page,trigger,label+' / Escape imbriqué');
 summary.glossary_navigation.push({root_key:rootKey,abbreviation,title,return_verified:true,nested_escape_focus_verified:true,scope:'glossary interaction only; outside canonical/injected template expectations'});
 return true;
}
async function verifyDialog(page,key,label,templates,width,sourceChecks){
 const expected=templates.get(key);check(label+' : clé de template canonique présente',!!expected,key);
 const dialog=page.locator('.mc-dlg[open]');await dialog.waitFor({state:'visible'});
 const content=await dialog.evaluate(el=>{const body=el.querySelector('.mc-dlg-b'),clone=body.cloneNode(true);clone.querySelectorAll('.mc-ratio,.ratio').forEach(node=>node.remove());
  return {title:el.querySelector('#mc-dlg-t').textContent,complete:clone.textContent,visible:body.innerText,
   sources:body.querySelectorAll('[data-justification-sources]').length,
   links:[...body.querySelectorAll('a[href]')].map(a=>({href:a.getAttribute('href'),title:a.textContent,target:a.target,rel:a.rel,parasites:a.querySelectorAll('[data-ab]').length}))}});
 check(label+' : titre attendu pour '+key,normal(content.title)===expected.title,{expected:expected.title,actual:normal(content.title)});
 check(label+' : contenu complet attendu',normal(content.complete)===expected.text,{expected_sha256:digest(expected.text),actual_sha256:digest(normal(content.complete))});
 check(label+' : aucune Fiche absente et contenu visible',normal(content.visible).length>40&&!content.visible.includes('Fiche absente.'));
 const sourceLinks=content.links.map((link,index)=>({...link,index})).filter(link=>/^https?:/i.test(link.href));
 check(label+' : liens de sources conformes aux canoniques',JSON.stringify(content.links.map(({href,target,rel})=>({href,target,rel})))===JSON.stringify(expected.links));
 check(label+' : attribut de sources conservé',content.sources===expected.sourceAttributes,{expected:expected.sourceAttributes,actual:content.sources});
 if(expected.sourceAttributes)check(label+' : sources déclarées présentes',sourceLinks.length>0&&await dialog.locator('[data-justification-sources] [data-ab]').count()===0,sourceLinks);
 for(const [index,link] of sourceLinks.entries())check(label+' : source HTTPS protégée '+index,new URL(link.href).protocol==='https:'&&link.target==='_blank'&&link.rel.split(/\s+/).includes('noopener')&&link.parasites===0,link);
 if(!sourceChecks.has(key)){sourceChecks.add(key);for(const [index,link] of sourceLinks.entries())await clickCitation(page,dialog.locator('a[href]').nth(link.index),label+' / source '+index)}
 if(width===390)await overflow(page,label);
 if(process.env.MEDINA_QA_CAPTURE==='1'&&width===390&&/bilan|an[ée]mie|sodium|potassium/i.test(key+' '+expected.title)&&!captures.some(c=>c.key===key)){
  const capture=path.join(out,'captures',key+'_390.png');fs.mkdirSync(path.dirname(capture),{recursive:true});await page.screenshot({path:capture});captures.push({key,path:path.relative(root,capture)})}
 return {key,kind:expected.kind,title:normal(content.title),text_sha256:digest(normal(content.complete)),source_links:sourceLinks.length};
}
async function inventory(page,expected){
 return page.evaluate(({expected,code})=>{
  const normal=s=>String(s).replace(/\u00ad/g,'').normalize('NFC').replace(/\s+/g,' ').trim();
  const text=root=>{const clone=root.cloneNode(true);clone.querySelectorAll('.ratio,.mc-ratio').forEach(el=>el.remove());return normal(clone.textContent)};
  const source=new DOMParser().parseFromString(expected.sources.map(s=>s.html).join('\n')+'\n'+expected.justification_templates,'text/html');
  const chapter=source.querySelector('[id="ch-'+code+'"]');if(!chapter)throw new Error('Le template canonique ch-'+code+' est absent');
  const injected=new Set(expected.injected_ids);
  const templates=[...source.querySelectorAll('template[data-pop]')].map(template=>({key:template.dataset.pop,kind:injected.has(template.dataset.pop)?'injected':'canonical',title:normal(template.dataset.title),text:text(template.content),
   sourceAttributes:template.content.querySelectorAll('[data-justification-sources]').length,
   links:[...template.content.querySelectorAll('a[href]')].map(a=>({href:a.getAttribute('href'),target:a.target,rel:a.rel})),
   children:[...template.content.querySelectorAll('[data-k]')].map((el,index)=>({index,key:el.dataset.k,text:normal(el.textContent)}))}));
  const direct=[...chapter.content.querySelectorAll('[data-k]')].map((el,index)=>({index,key:el.dataset.k,text:normal(el.textContent),green:el.classList.contains('w')}));
  const runtime=[...document.querySelectorAll('.mc[data-code="'+code+'"] [data-k]')].map((el,index)=>({index,key:el.dataset.k,text:normal(el.textContent),green:el.classList.contains('mc-w'),panel:el.closest('.mc-panel')?.id,science:el.closest('.mc-sci')?.id}));
  const compiled=templates.map(template=>{const found=[...document.querySelectorAll('template[data-pop]')].filter(el=>el.dataset.pop===template.key);return {key:template.key,count:found.length,title:found[0]?normal(found[0].dataset.title):null,text:found[0]?text(found[0].content):null}});
  const declared=new Set(templates.map(template=>template.key)),referenced=new Set([...direct.map(trigger=>trigger.key),...templates.flatMap(template=>template.children.map(child=>child.key))]);
  const dependencies=[...referenced].filter(key=>!declared.has(key)).map(key=>{const found=[...document.querySelectorAll('template[data-pop]')].filter(el=>el.dataset.pop===key),template=found[0];
   return {key,kind:'shared_external',count:found.length,title:template?normal(template.dataset.title):null,text:template?text(template.content):null,children:[],
    sourceAttributes:template?.content.querySelectorAll('[data-justification-sources]').length||0,
    links:template?[...template.content.querySelectorAll('a[href]')].map(a=>({href:a.getAttribute('href'),target:a.target,rel:a.rel})):[]}});
  return {templates,direct,runtime,compiled,dependencies};
 },{expected,code});
}
function nativePaths(direct,templates){
 const paths=new Map(),queue=direct.map(trigger=>({key:trigger.key,directIndex:trigger.index,edges:[]}));
 while(queue.length){const item=queue.shift();if(paths.has(item.key))continue;paths.set(item.key,item);
  for(const child of templates.get(item.key)?.children||[])queue.push({key:child.key,directIndex:item.directIndex,edges:[...item.edges,{parent:item.key,...child}]})}
 return paths;
}
async function sweep(page,width,expected){
 await course(page);const data=await inventory(page,expected),templates=new Map(data.templates.map(template=>[template.key,template]));
 check(width+' : templates canoniques sans doublon',templates.size===data.templates.length);
 check(width+' : toutes les fenêtres injectées dans l’attendu source',expected.injected_ids.every(key=>templates.get(key)?.kind==='injected'));
 for(const dependency of data.dependencies){check(width+' : template partagé présent une fois / '+dependency.key,dependency.count===1,dependency.count);templates.set(dependency.key,dependency)}
 check(width+' : tous les mots verts directs canoniques compilés',JSON.stringify(data.runtime.map(({key,text,green})=>({key,text,green})))===JSON.stringify(data.direct.map(({key,text,green})=>({key,text,green}))),{canonical:data.direct.length,compiled:data.runtime.length});
 const summary={width,height:width===390?844:900,emulation:'viewport only; desktop Chromium context',direct_triggers:data.runtime.length,green_direct_triggers:data.runtime.filter(trigger=>trigger.green).length,expected_templates:data.templates.length,
  canonical_templates:data.templates.filter(template=>template.kind==='canonical').length,injected_templates:data.templates.filter(template=>template.kind==='injected').length,
  shared_external_templates:data.dependencies.map(({key,title,text})=>({key,title,text_sha256:digest(text),expectation:'compiled shared template; outside canonical/injected course expectation'})),direct_results:[],nested_results:[],glossary_navigation:[],unreachable:[],mobile_examples:{}};viewports.push(summary);
 for(const compiled of data.compiled)await attempt(width+' / compilation / '+compiled.key,async()=>{const template=templates.get(compiled.key);check(width+' : template compilé une fois / '+compiled.key,compiled.count===1,compiled.count);check(width+' : titre et texte compilés conformes / '+compiled.key,compiled.title===template.title&&compiled.text===template.text)});
 const paths=nativePaths(data.runtime,templates),sourceChecks=new Set();
 summary.unreachable=data.templates.filter(template=>!paths.has(template.key)).map(template=>({key:template.key,title:template.title,
  source:template.kind==='injected'?path.relative(root,bankFile):expected.sources.find(source=>source.html.includes('data-pop="'+template.key+'"'))?.name,
  referenced_by:data.templates.filter(parent=>parent.children.some(child=>child.key===template.key)).map(parent=>parent.key)}));
 if(summary.unreachable.length)failures.push({label:width+' : templates sans chemin natif depuis les mots verts',templates:summary.unreachable});
 for(const trigger of data.runtime){const label=width+' / direct '+trigger.index+' / '+trigger.key;await attempt(label,async()=>{
  const native=await reveal(page,trigger.index);await triggerClean(native,label);await native.click();
  const result=await verifyDialog(page,trigger.key,label,templates,width,sourceChecks);
  const closed=await glossaryNavigation(page,native,trigger.key,label,width,summary);if(!closed)await closeAndFocus(page,native,label);summary.direct_results.push({...trigger,...result});
 },page);if((trigger.index+1)%25===0)console.log(JSON.stringify({progress:width,direct:trigger.index+1,total:data.runtime.length,failures:failures.length}))}
 const nestedRoutes=data.templates.flatMap(parent=>{const route=paths.get(parent.key);return route?parent.children.map(child=>({key:child.key,directIndex:route.directIndex,edges:[...route.edges,{parent:parent.key,...child}]})):[]});
 summary.authored_nested_triggers=nestedRoutes.length;
 for(const route of nestedRoutes){const key=route.key,last=route.edges.at(-1),label=width+' / imbriqué / '+last.parent+' / '+last.index+' / '+key;await attempt(label,async()=>{
  const native=await reveal(page,route.directIndex);await triggerClean(native,label);await native.click();await verifyDialog(page,data.runtime[route.directIndex].key,label+' / racine',templates,width,sourceChecks);
  const parents=[];
  for(const edge of route.edges){parents.push(await dialogState(page));const child=page.locator('.mc-dlg[open] .mc-dlg-b [data-k]').nth(edge.index);
   check(label+' : clé native imbriquée attendue',await child.getAttribute('data-k')===edge.key,edge);await triggerClean(child,label+' / '+edge.key);await child.click();
   await verifyDialog(page,edge.key,label+' / '+edge.key,templates,width,sourceChecks);await page.locator('.mc-back:not([hidden])').waitFor({state:'visible'})}
  for(const parent of parents.reverse()){await page.locator('.mc-back').click();check(label+' : Retour restitue titre et contenu parent',JSON.stringify(await dialogState(page))===JSON.stringify(parent))}
  check(label+' : Retour masqué à la racine',await page.locator('.mc-back').isHidden());await closeAndFocus(page,native,label);
  summary.nested_results.push({key,parent:last.parent,child_index:last.index,direct_index:route.directIndex,chain:[data.runtime[route.directIndex].key,...route.edges.map(edge=>edge.key)]});
 },page)}
 const covered=new Set([...summary.direct_results.map(result=>result.key),...summary.nested_results.map(result=>result.key)]);
 summary.covered_keys=[...covered].sort();summary.templates_covered=data.templates.filter(template=>covered.has(template.key)).length;
 summary.injected_covered=expected.injected_ids.filter(key=>covered.has(key));
 check(width+' : toutes les fenêtres source et injectées réellement ouvertes',summary.templates_covered===data.templates.length&&summary.injected_covered.length===expected.injected_ids.length,{expected:data.templates.length,covered:summary.templates_covered,injected:summary.injected_covered});
 if(code==='I50')check(width+' : Retour et Escape depuis un glossaire imbriqué vérifiés',summary.glossary_navigation.length===1);
 for(const [example,pattern] of [['bilan',/bilan/i],['anemie',/an[ée]mie/i],['sodium',/sodium|natr[ée]mie/i],['potassium',/potassium|kali[ée]mie/i]]){
  const titles=data.templates.filter(template=>pattern.test(template.key+' '+template.title)),candidates=titles.length?titles:data.templates.filter(template=>pattern.test(template.text));
  summary.mobile_examples[example]={matched_in:titles.length?'key or title':'authored body',keys:candidates.map(template=>template.key),covered:candidates.filter(template=>covered.has(template.key)).map(template=>template.key)};
  check(width+' : exemple '+example+' couvert si repérable',candidates.every(template=>covered.has(template.key)),summary.mobile_examples[example]);
 }
 await overflow(page,width+' / cours final');
 console.log(JSON.stringify({progress:width,direct_passed:summary.direct_results.length,nested_passed:summary.nested_results.length,templates_covered:summary.templates_covered,failures:failures.length}));
}
(async()=>{
 fs.mkdirSync(out,{recursive:true});file=originalFragment();
 sources=fs.readdirSync(folder).filter(name=>name.endsWith('.html')).sort().map(name=>path.join(folder,name));
 check(code+' : quatre panneaux sources présents',['a','b','c','d'].every(part=>sources.includes(path.join(folder,code+'_'+part+'.html'))));
 check(code+' : sources de fenêtres présentes',sources.length>4);
 snapshotInputs();const expected=expectedSources();
 const {chromium}=loadPlaywright(),browser=await chromium.launch(browserOptions(chromium));
 try{const context=await browser.newContext({viewport:{width:1360,height:900},reducedMotion:'reduce'});await context.route(/^https?:/,route=>route.abort());
  const page=await context.newPage();page.setDefaultTimeout(10000);page.on('pageerror',error=>errors.push(error.message));
  for(const width of [1360,390]){await page.setViewportSize({width,height:width===390?844:900});await attempt(width+' / cours complet',()=>sweep(page,width,expected),page)}
  if(errors.length)failures.push({label:'Erreurs JavaScript',errors});else checks.push('Aucune erreur JavaScript');
 }finally{await browser.close()}
})().catch(error=>failures.push({label:'Contrôle interrompu',error:String(error.stack||error)})).finally(()=>{
 finishInputs();report.result=failures.length?'failed':'passed';report.completed_at=new Date().toISOString();
 const target=path.join(out,(report.result==='passed'?'':'failed_')+code.toLowerCase()+'_native_results.json');
 fs.mkdirSync(out,{recursive:true});fs.writeFileSync(target,JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({result:report.result,checks:checks.length,failures:failures.length,report:path.relative(root,target)}));if(failures.length)process.exitCode=1;
});
