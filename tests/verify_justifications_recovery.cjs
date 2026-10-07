/* Real-browser checks of authored mechanisms, native triggers and Bronchite. */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright(),root=path.resolve(__dirname,'..');
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'audits/MECANISMES_2026-10-07/browser_recovery'));
const directory=path.resolve(process.env.MEDINA_FRAGMENTS||path.join(root,'dist/fragments'));
const targeted=process.argv.includes('--targeted');
const expected=['I10','I21','I25','I26','I50','I70','J18','J44','J45','D84','M06','M31','M32','T78','A41'];
const requested=process.env.MEDINA_JUSTIFICATION_CODES?.split(',').filter(Boolean);
const codes=requested||(targeted?['I50']:expected);
const compiledRoutes=new Map();
for(const name of fs.readdirSync(directory).filter(name=>name.endsWith('.html'))){
 const file=path.join(directory,name),html=fs.readFileSync(file,'utf8');
 const payload=html.match(/<script[^>]*id="medina-category-organisation-data"[^>]*>([\s\S]*?)<\/script>/);
 if(!payload)continue;
 const organisation=JSON.parse(payload[1]);
 for(const block of organisation.blocks||[])for(const lesson of block.lessons||[]){
  if(lesson.integrated&&!lesson.reference&&lesson.source_fragment_id===organisation.fragment.id){
   if(compiledRoutes.has(lesson.code))assert.equal(compiledRoutes.get(lesson.code),file,'Two original fragments for '+lesson.code);
   compiledRoutes.set(lesson.code,file);
  }
 }
}
const checks=[],errors=[],courses=[],inputs={};
fs.mkdirSync(path.join(out,'captures'),{recursive:true});
const normal=s=>String(s).replace(/\u00ad/g,'').normalize('NFC').replace(/\s+/g,' ').trim();
const check=(label,ok,detail)=>{assert.ok(ok,label+(detail===undefined?'':': '+JSON.stringify(detail)));checks.push(label)};
const digest=s=>crypto.createHash('sha256').update(s).digest('hex');
function fileFor(code){
 const file=compiledRoutes.get(code);
 assert.ok(file,'Fragment original compilé introuvable : '+code);
 assert.ok(fs.existsSync(file),'Fragment compilé absent : '+file);
 inputs[file]=digest(fs.readFileSync(file));return file;
}
async function course(page,code){
 await page.goto(pathToFileURL(fileFor(code)).href+'#/entry/'+code);
 await page.waitForFunction(()=>window.MDN_READY===true);
 await page.locator('.mc[data-code="'+code+'"]').waitFor();
 const book=page.locator('.mc-book');if(await page.locator('.mc.book').count())await book.click();
}
async function reveal(page,selector){
 const loc=page.locator(selector).first();assert.ok(await loc.count(),'Déclencheur natif absent : '+selector);
 const context=await loc.evaluate(el=>({panel:el.closest('.mc-panel')?.id,science:el.closest('.mc-sci')?.id}));
 if(context.panel)await page.locator('.mc-tabs button[data-p="'+context.panel+'"]').click();
 if(context.science)await page.locator('.mc-sci-bar button[data-s="'+context.science+'"]').click();
 await loc.scrollIntoViewIfNeeded();await loc.waitFor({state:'visible'});return loc;
}
async function closeAndFocus(page,trigger,label){
 await page.keyboard.press('Escape');await page.locator('.mc-dlg').waitFor({state:'hidden'});
 await page.waitForFunction(el=>document.activeElement===el,await trigger.elementHandle());
 check(label+' : Escape ferme et restitue le focus',await trigger.evaluate(el=>document.activeElement===el));
}
async function popup(page,trigger,label){
 await trigger.click();const dialog=page.locator('.mc-dlg[open]');await dialog.waitFor({state:'visible'});
 const text=normal(await dialog.locator('.mc-dlg-b').innerText());
 check(label+' : fenêtre rédigée',text.length>40&&!text.includes('Fiche absente.'));
 return {dialog,text};
}
async function overflow(page,label,dialog){
 const size=await page.evaluate(()=>({width:innerWidth,document:document.documentElement.scrollWidth}));
 check(label+' : page sans débordement',size.document<=size.width+1,size);
 if(dialog){const r=await dialog.boundingBox();check(label+' : fenêtre dans la largeur',r.x>=-1&&r.x+r.width<=size.width+1,r)}
}
async function nested(page,dialog,label){
 const child=dialog.locator('.mc-dlg-b [data-ab],.mc-dlg-b button[data-k],.mc-dlg-h [data-ab]').first();
 if(!await child.count())return false;
 const heading=normal(await dialog.locator('#mc-dlg-t').innerText()),body=normal(await dialog.locator('.mc-dlg-b').innerText());
 await child.click();await page.locator('.mc-back:not([hidden])').waitFor({state:'visible'});
 check(label+' : approfondissement imbriqué',normal(await dialog.locator('.mc-dlg-b').innerText()).length>0&&!normal(await dialog.locator('.mc-dlg-b').innerText()).includes('Fiche absente.'));
 await dialog.locator('.mc-back').click();
 check(label+' : Retour restitue la fenêtre parente',normal(await dialog.locator('#mc-dlg-t').innerText())===heading&&normal(await dialog.locator('.mc-dlg-b').innerText())===body);
 return true;
}
async function findNativePath(page,key){
 return page.evaluate(target=>{
  const direct=[...document.querySelectorAll('.mc button[data-k]')].map(b=>b.dataset.k);
  const queue=direct.map(k=>[k]),seen=new Set();
  while(queue.length){const chain=queue.shift(),k=chain[chain.length-1];if(k===target)return chain;if(seen.has(k))continue;seen.add(k);
   const template=[...document.querySelectorAll('template[data-pop]')].find(t=>t.dataset.pop===k);
   if(template)for(const child of template.content.querySelectorAll('button[data-k]'))queue.push([...chain,child.dataset.k]);
  }return null;
 },key);
}
async function openCitation(page,link,label){
 const expected=await link.getAttribute('href'),url=new URL(expected).href.split('#')[0];
 const context=page.context(),request=context.waitForEvent('request',{predicate:r=>r.isNavigationRequest()&&r.url().split('#')[0]===url,timeout:10000});
 const newTab=page.waitForEvent('popup',{timeout:10000});
 const before=normal(await page.locator('.mc-dlg[open] .mc-dlg-b').innerText());
 await link.click();
 const [navigation,tab]=await Promise.all([request,newTab]);
 check(label+' : la citation ouvre sa propre URL',navigation.url().split('#')[0]===url);
 await tab.close();await page.bringToFront();
 check(label+' : la citation conserve la fenêtre médicale',normal(await page.locator('.mc-dlg[open] .mc-dlg-b').innerText())===before);
}
async function bankEntry(page,code,entry,width,nestingState){
 const label=code+' / '+entry.id+' / '+width;
 const selector='.mc button[data-justification][data-k="'+entry.id+'"]';
 let trigger;
 if(await page.locator(selector).count())trigger=await reveal(page,selector);
 else{
  const chain=await findNativePath(page,entry.id);check(label+' : chemin natif vers la cible',chain?.length>1,chain);
  trigger=await reveal(page,'.mc button[data-k="'+chain[0]+'"]');await trigger.click();
  for(const key of chain.slice(1,-1))await page.locator('.mc-dlg[open] button[data-k="'+key+'"]').first().click();
  await page.locator('.mc-dlg[open] button[data-justification][data-k="'+entry.id+'"]').first().click();
 }
 const opened=await page.locator('.mc-dlg[open]').count()?{dialog:page.locator('.mc-dlg[open]'),text:normal(await page.locator('.mc-dlg[open] .mc-dlg-b').innerText())}:await popup(page,trigger,label);
 const {dialog,text}=opened;
 check(label+' : texte intégral attendu',[...entry.explanation,...entry.mechanism,entry.implication,...entry.limits].every(part=>text.includes(normal(part))));
 check(label+' : mécanisme et conséquence visibles',text.includes('Mécanisme physiopathologique')&&text.includes('Conséquence clinique'));
 check(label+' : rubrique de limites conforme au contenu',text.includes('Limites et contexte')===Boolean(entry.limits.length));
 const links=await dialog.locator('[data-justification-sources] a').evaluateAll(a=>a.map(x=>({url:x.getAttribute('href'),title:x.textContent,target:x.target,rel:x.rel})));
 check(label+' : toutes les sources présentes',links.length===entry.sources.length&&entry.sources.every(s=>links.some(l=>l.url===s.url&&normal(l.title)===normal(s.title)&&l.target==='_blank'&&l.rel.includes('noopener'))),links);
 check(label+' : sources sans boutons parasites',await dialog.locator('[data-justification-sources] [data-ab]').count()===0);
 if(links.length)await openCitation(page,dialog.locator('[data-justification-sources] a').first(),label);
 if(code==='I50'&&!nestingState.done)nestingState.done=await nested(page,dialog,label);
 if(['i50-j-anemie','i50-j-sodium','i50-j-potassium'].includes(entry.id)){await overflow(page,label,dialog);await page.screenshot({path:path.join(out,'captures',entry.id+'_'+width+'.png')})}
 await closeAndFocus(page,trigger,label);
}
async function bronchitis(page,width){
 await course(page,'J40');const source=fs.readFileSync(path.join(root,'chapters/J40/J40_pop.html'),'utf8');
 const keys=[...source.matchAll(/<template data-pop="([^"]+)"/g)].map(m=>m[1]);
 check('J40 / '+width+' : 40 fenêtres dont 6 Pareto',keys.length===40&&keys.filter(k=>k.startsWith('pareto-')).length===6,keys.length);
 const unique=await page.locator('.mc button[data-k]').evaluateAll(buttons=>[...new Set(buttons.map(b=>b.dataset.k))]);
 check('J40 / '+width+' : toutes les fenêtres ont un déclencheur natif',keys.every(k=>unique.includes(k)));
 for(const key of keys){const label='J40 / '+key+' / '+width,trigger=await reveal(page,'.mc button[data-k="'+key+'"]');const {dialog,text}=await popup(page,trigger,label);
  if(key.startsWith('j40-'))check(label+' : mécanisme et limite rédigés',text.toLocaleLowerCase('fr').includes('mécanisme de l’affirmation')&&text.toLocaleLowerCase('fr').includes('conséquence clinique')&&text.toLocaleLowerCase('fr').includes('limite.'));
  else check(label+' : synthèse calculée',await dialog.locator('.mc-ratio').count()===1&&text.includes('%')&&await dialog.locator('li').count()>1);
  if(['j40-anemie','j40-sodium','j40-potassium'].includes(key)){await overflow(page,label,dialog);await page.screenshot({path:path.join(out,'captures',key+'_'+width+'.png')})}
  await closeAndFocus(page,trigger,label);
 }
 await page.locator('.mc-tabs button[data-p="pS"]').click();const tabs=page.locator('.mc-sci-bar button[data-s]');
 check('J40 / '+width+' : cinq disciplines',await tabs.count()===5);
 for(let i=0;i<await tabs.count();i++){await tabs.nth(i).click();check('J40 / '+width+' : figure accessible '+i,await page.locator('.mc-sci:not([hidden]) svg[role="img"][aria-label]').count()===1);await overflow(page,'J40 science '+i+' / '+width)}
 await page.locator('.mc-tabs button[data-p="pE"]').click();const quizzes=page.locator('.mc-quiz');check('J40 / '+width+' : trois cas',await quizzes.count()===3);
 // Click the native option padding: glossary links inside an answer intentionally open their own window.
 for(let i=0;i<3;i++){const q=quizzes.nth(i);await q.locator('[data-ok="0"]').first().click({position:{x:8,y:8}});check('J40 / '+width+' : correction de la réponse incorrecte '+i,await q.locator('.mc-fb').isVisible());await q.locator('[data-ok="1"]').click({position:{x:8,y:8}});check('J40 / '+width+' : correction de la réponse correcte '+i,await q.locator('.mc-fb').isVisible())}
}
(async()=>{
 const banks=codes.map(code=>{const file=path.join(root,'chapters',code,code+'_justifications.json');check(code+' : banque présente',fs.existsSync(file));const source=fs.readFileSync(file,'utf8');inputs[file]=digest(source);return {code,bank:JSON.parse(source)}});
 if(!targeted&&!requested)check('Jeu complet : quinze cours Codex',banks.length===15);
 if(!targeted&&!requested){const plan=JSON.parse(fs.readFileSync(path.join(root,'docs/collaboration/MECHANISMS_PLAN.json'),'utf8'));check('Jeu complet : fenêtres et cibles conformes au plan',banks.reduce((n,b)=>n+b.bank.entries.length,0)===plan.targeted_windows_total&&banks.reduce((n,b)=>n+b.bank.entries.reduce((m,e)=>m+e.match.length,0),0)===plan.targeted_matches_total);}
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1360,height:900},reducedMotion:'reduce'});
  await context.route(/^https?:/,route=>route.abort()); // Navigation URLs are observed; no external page is downloaded.
  const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
  for(const {code,bank} of banks){await course(page,code);const state={done:false};
   for(const entry of bank.entries)await bankEntry(page,code,entry,1360,state);
   if(code==='I50')check('I50 bureau : navigation imbriquée vérifiée',state.done);
   courses.push({code,entries:bank.entries.length,targets:bank.entries.reduce((n,e)=>n+e.match.length,0)});
   console.log(JSON.stringify({progress:code,entries:bank.entries.length,checks:checks.length}));
  }
  await bronchitis(page,1360);
  await page.setViewportSize({width:390,height:844});await course(page,'I50');const i50=banks.find(b=>b.code==='I50')?.bank||JSON.parse(fs.readFileSync(path.join(root,'chapters/I50/I50_justifications.json'),'utf8')),state={done:false};
  for(const entry of i50.entries)await bankEntry(page,'I50',entry,390,state);
  check('I50 mobile : navigation imbriquée vérifiée',state.done);await bronchitis(page,390);
  check('Aucune erreur JavaScript',errors.length===0,errors);
  for(const [file,hash] of Object.entries(inputs))check('Entrée stable pendant le contrôle : '+path.relative(root,file),digest(fs.readFileSync(file))===hash);
  const report={result:'passed',targeted:targeted||!!requested,coverage:'Every mechanism entry in selected banks; every native J40 mechanism and Pareto on desktop and mobile; I50 text/sources/keyboard/focus/nested navigation on both viewports. The first citation of every bank entry is clicked and its navigation URL is observed without downloading the external page.',codes,courses,desktop_entries:courses.reduce((n,c)=>n+c.entries,0),mobile_i50_entries:i50.entries.length,j40_windows_per_viewport:40,j40_pareto_per_viewport:6,checks,errors,inputs};
  fs.writeFileSync(path.join(out,targeted||requested?'targeted_justifications_results.json':'justifications_results.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({result:report.result,targeted:report.targeted,courses:courses.length,desktop_entries:report.desktop_entries,checks:checks.length,errors}));
 }finally{await browser.close()}
})().catch(error=>{fs.writeFileSync(path.join(out,'failed_justifications_results.json'),JSON.stringify({result:'failed',targeted:targeted||!!requested,codes,checks,errors,inputs,error:String(error.stack||error)},null,2)+'\n');console.error(error);process.exitCode=1});
