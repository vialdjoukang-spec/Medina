/* Real Chromium checks for both curriculum filters, all fragment routes and immutable course views. */
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright(),root=path.resolve(__dirname,'..');
const directory=path.resolve(process.env.MEDINA_OUT||path.join(root,'dist'));
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'work/a6-ui'));
const registry=JSON.parse(fs.readFileSync(path.join(root,'fragments.json'),'utf8'));
const frequency=new Set(JSON.parse(fs.readFileSync(path.join(root,'nosology/frequency.json'),'utf8')).codes);
const checks=[],errors=[],traces=[],fragments=[];fs.mkdirSync(out,{recursive:true});
const check=(name,value,detail)=>{assert.ok(value,name+(detail===undefined?'':' : '+JSON.stringify(detail)));checks.push(name)};
const equal=(name,value,expected)=>{const actual=JSON.stringify(value),original=JSON.stringify(expected);let detail={value,expected};if(actual.length+original.length>3000){let first=0;while(first<Math.min(actual.length,original.length)&&actual[first]===original[first])first++;detail={actualLength:actual.length,expectedLength:original.length,firstMismatch:first};if(actual!==original)fs.writeFileSync(path.join(out,'snapshot-discrepancy.json'),JSON.stringify({name,value,expected}));}check(name,actual===original,detail);};
const payload=source=>JSON.parse(source.match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
const mime={'.html':'text/html; charset=utf-8','.woff2':'font/woff2','.css':'text/css','.js':'text/javascript'};
const server=http.createServer((req,res)=>{
 const file=path.resolve(directory,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
 if(!file.startsWith(directory+path.sep)){res.writeHead(403).end();return;}
 fs.readFile(file,(error,data)=>{if(error){res.writeHead(404).end();return;}res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');
  // Force a painted interval before fragment runtime, reproducing slow delivery.
  const marker=Buffer.from('<script id="medina-fragment-runtime">'),split=data.indexOf(marker);
  if(req.url.includes('slow=1')&&split>0){res.write(data.subarray(0,split));setTimeout(()=>res.end(data.subarray(split)),300);}else res.end(data);
 });
});
async function waitHome(page){await page.locator('.mcg-home').waitFor();await page.waitForFunction(()=>window.MEDINA_CATEGORY_ORGANISATION&&(!document.querySelector('#mdn-pack')||window.MDN_READY===true));}
async function route(page,hash){await page.evaluate(value=>location.hash=value,hash);await page.waitForFunction(value=>location.hash===value,hash);await page.waitForTimeout(40);}
async function overflow(page,label){const size=await page.evaluate(()=>({viewport:innerWidth,actual:document.documentElement.scrollWidth}));check(label,size.actual<=size.viewport+1,size);}
async function courseSnapshot(page,code){await page.locator('.mc[data-code="'+code+'"]').waitFor();
 // Existing polish.js numbers each table of contents after a debounced mutation observer.
 // Wait for that real UI lifecycle rather than comparing its transient pre-polish DOM.
 await page.waitForFunction(()=>[...document.querySelectorAll('.mc .mc-panel')].every(panel=>{const ol=panel.querySelector('.mc-toc ol'),n=parseInt(panel.querySelector('.mc-ilot h2 .mc-n')?.textContent,10);return !ol||Number.isNaN(n)||ol.children.length!==panel.querySelectorAll(':scope .mc-body>.mc-ilot').length||ol.start===n;}));return page.locator('.mc').evaluate(el=>({tabs:[...el.querySelectorAll('.mc-tabs button')].map(b=>b.textContent),panels:[...el.querySelectorAll('.mc-panel')].map(p=>p.innerHTML),dialogs:[...el.querySelectorAll('.mc-dlg')].map(d=>d.innerHTML)}));}
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const origin='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1050},reducedMotion:'reduce'});
  await context.addInitScript(()=>{
   window.__fragmentPaints=[];const record=()=>{const el=document.getElementById('content');if(el){const style=getComputedStyle(el),v={t:Math.round(performance.now()),visible:!el.hidden&&style.visibility!=='hidden'&&style.display!=='none',heading:el.querySelector('h1,h2')?.textContent||'',home:!!el.querySelector('.mcg-home'),filterNotice:!!el.querySelector('.mcg-filter-notice'),text:el.innerText.slice(0,180)};const last=window.__fragmentPaints.at(-1);if(!last||last.heading!==v.heading||last.visible!==v.visible||last.text!==v.text||last.filterNotice!==v.filterNotice||last.home!==v.home)window.__fragmentPaints.push(v);}requestAnimationFrame(record)};requestAnimationFrame(record);
  });
  const page=await context.newPage();page.on('pageerror',error=>errors.push({url:page.url(),message:error.message}));
  for(const fragment of registry){
   const file='fragments/MEDINA_'+fragment.id+'_'+fragment.slug+'.html',O=payload(fs.readFileSync(path.join(directory,file),'utf8')),url=origin+'/'+file;
   const categories=O.nosology.lessons.filter(l=>!l.code.includes('.'));
   const expectedSets={frequent:categories.filter(l=>l.icd10gm.codes.some(code=>frequency.has(code))).map(l=>l.code),federal_exam:categories.filter(l=>l.gold_star.enabled).map(l=>l.code)};
   for(const filter of Object.keys(expectedSets)){equal(fragment.id+' '+filter+' catalogue correspond aux critères sources',[...O.nosology.filters[filter]].sort(),expectedSets[filter].sort());check(fragment.id+' '+filter+' jauge correspond',O.nosology.gauges[filter].total===expectedSets[filter].length);}
   await page.goto(url+'?slow=1');await waitHome(page);
   const paints=await page.evaluate(()=>window.__fragmentPaints);traces.push({fragment:fragment.id,route:'default',paints});
   const foreign=paints.filter(p=>p.visible&&p.heading&&!p.heading.includes(O.fragment.display_name||O.fragment.label));
   check(fragment.id+' aucun accueil étranger peint malgré arrivée retardée',foreign.length===0,foreign);
   equal(fragment.id+' accueil défaut complet',await page.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgCategory)),O.blocks.map(b=>b.code));
   const atlasGauge='.sidebar-note .nosology-progress:not([data-mcg-filter]):not([data-mcg-global])';
   const globals=await page.locator(atlasGauge).allTextContents();
   check(fragment.id+' jauge de tout MEDINA informative',globals.length===1&&await page.locator(atlasGauge+' :is(a,button,[tabindex],[onclick]),'+atlasGauge+':is(a,button,[tabindex],[onclick])').count()===0);
   check(fragment.id+' avancement global du fragment cliquable',await page.locator('.sidebar-note a[data-mcg-global][href="#/home"]').count()===1);
   check(fragment.id+' deux jauges filtrantes latérales',await page.locator('.sidebar-note a[data-mcg-filter]').count()===2);
   check(fragment.id+' symbole Filtre non interactif',await page.locator('.mcg-filter-heading a,.mcg-filter-heading button,.mcg-filter-heading [tabindex]').count()===0&&await page.locator('svg.mcg-filter-symbol[aria-hidden="true"][focusable="false"]').count()>0);
   if(fragment.id==='T1'){await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(out,'apres-infectiologie-accueil-desktop.png')});await page.locator('.sidebar-note').screenshot({path:path.join(out,'apres-jauges-accueil.png')});await page.setViewportSize({width:1366,height:768});await page.locator('.sidebar-note').scrollIntoViewIfNeeded();const rail=await page.locator('.sidebar-note').evaluate(el=>{const r=el.getBoundingClientRect();return {top:r.top,bottom:r.bottom,height:innerHeight}});check('T1 jauges latérales visibles sur ordinateur portable',rail.top>=0&&rail.bottom<=rail.height+1,rail);await page.screenshot({path:path.join(out,'apres-infectiologie-portable.png')});await page.setViewportSize({width:1440,height:1050});}
   const heading=page.locator('.sidebar-note .mcg-filter-heading');const hash=await page.evaluate(()=>location.hash);await heading.click();equal(fragment.id+' clic label sans navigation',await page.evaluate(()=>location.hash),hash);
   const sample=O.blocks.flatMap(b=>b.lessons).find(l=>l.integrated&&l.source_fragment_id===fragment.id&&Object.values(expectedSets).some(codes=>codes.includes(l.code)));
   let original;
   if(sample){await route(page,'#/entry/'+sample.code);original=await courseSnapshot(page,sample.code);}
   for(const filter of ['frequent','federal_exam']){
    await route(page,'#/home');await page.locator('.mcg-cover').waitFor();const trigger=page.locator('.sidebar-note [data-mcg-filter="'+filter+'"]');await trigger.focus();await page.keyboard.press('Enter');await page.locator('.mcg-filter-notice').waitFor();
    check(fragment.id+' '+filter+' activation clavier',new URLSearchParams((await page.evaluate(()=>location.hash)).split('?')[1]).get('filter')===filter);
    const selected=new Set(expectedSets[filter]),expectedBlocks=O.blocks.map(b=>({...b,lessons:b.lessons.filter(l=>selected.has(l.code))})).filter(b=>b.lessons.length);
    equal(fragment.id+' '+filter+' catégories conservées dans ordre original',await page.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgCategory)),expectedBlocks.map(b=>b.code));
    equal(fragment.id+' '+filter+' barre latérale restreinte',await page.locator('[data-mcg-sidebar-lesson]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgSidebarLesson)),expectedBlocks.flatMap(b=>b.lessons.map(l=>l.code)));
    const links=await page.locator('[data-mcg-category],[data-mcg-sidebar-lesson],.mcg-lesson-main').evaluateAll(nodes=>nodes.map(n=>n.getAttribute('href')));check(fragment.id+' '+filter+' liens conservent filtre',links.every(href=>new URLSearchParams(href.split('?')[1]).get('filter')===filter));
    if(expectedBlocks.length){await page.locator('[data-mcg-category]').first().click();await page.locator('[data-mcg-block="'+expectedBlocks[0].code+'"]').waitFor();check(fragment.id+' '+filter+' clic catégorie conserve filtre',(await page.evaluate(()=>location.hash)).includes('filter='+filter));}
    equal(fragment.id+' '+filter+' jauge atlas identique',await page.locator(atlasGauge).allTextContents(),globals);
    check(fragment.id+' '+filter+' état actif exposé',await page.locator('.sidebar-note [data-mcg-filter="'+filter+'"]').getAttribute('aria-current')==='page');
    for(const block of expectedBlocks){
     await route(page,'#/home?filter='+filter+'&category='+encodeURIComponent(block.code));await page.locator('[data-mcg-block="'+block.code+'"]').waitFor();
     equal(fragment.id+' '+filter+' '+block.code+' leçons exactes',await page.locator('[data-mcg-block] [data-mcg-lesson]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgLesson)),block.lessons.map(l=>l.code));
     equal(fragment.id+' '+filter+' '+block.code+' titre préservé',(await page.locator('.mcg-block-heading h2').innerText()),block.title);
    }
    await page.goto(url+'#/home?filter='+filter);await waitHome(page);await page.locator('.mcg-filter-notice').waitFor();await page.reload();await waitHome(page);
    equal(fragment.id+' '+filter+' accès direct et actualisation',await page.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgCategory)),expectedBlocks.map(b=>b.code));
    await route(page,'#/search?filter='+filter);await page.locator('.mcg-search-heading').waitFor();const searchCodes=await page.locator('[data-mcg-lesson]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgLesson));check(fragment.id+' '+filter+' recherche reste dans sélection',searchCodes.every(code=>selected.has(code)),searchCodes.filter(code=>!selected.has(code)));
    if(sample&&selected.has(sample.code)){await route(page,'#/entry/'+sample.code+'?filter='+filter);equal(fragment.id+' '+filter+' corps cours intégral inchangé',await courseSnapshot(page,sample.code),original);check(fragment.id+' '+filter+' quatre onglets',await page.locator('.mc-tabs button').count()===4);const back=page.locator('.mc-toolbar > a.btn.tiny').first(),href=await back.getAttribute('href'),params=new URLSearchParams(href.split('?')[1]);check(fragment.id+' '+filter+' retour du lecteur conserve catégorie et filtre',params.get('filter')===filter&&expectedBlocks.some(block=>block.code===params.get('category')&&block.lessons.some(lesson=>lesson.code===sample.code)),href);await back.click();await page.locator('[data-mcg-block="'+params.get('category')+'"]').waitFor();check(fragment.id+' '+filter+' retour lecteur affiche catégorie filtrée',await page.locator('.mcg-filter-notice').count()===1);}
    await page.goto(url+'#/home?filter='+filter);await waitHome(page);await page.setViewportSize({width:390,height:844});await overflow(page,fragment.id+' '+filter+' mobile sans débordement');
    // Mobile's visible home gauges provide the same real navigation as desktop's rail.
    const mobileTrigger=page.locator('#content [data-mcg-filter="'+(filter==='frequent'?'federal_exam':'frequent')+'"]');await mobileTrigger.click();await page.waitForFunction(f=>location.hash.includes('filter='+f),filter==='frequent'?'federal_exam':'frequent');
    if(fragment.id==='T1'){await route(page,'#/home?filter='+filter);await page.screenshot({path:path.join(out,'apres-infectiologie-'+filter+'-mobile.png')});}
    await page.setViewportSize({width:1440,height:1050});await route(page,'#/home?filter='+filter);
    if(fragment.id==='T1'){await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(out,'apres-infectiologie-'+filter+'-desktop.png')});await page.locator('.sidebar-note').screenshot({path:path.join(out,'apres-jauges-'+filter+'.png')});if(expectedBlocks.length){await route(page,'#/home?filter='+filter+'&category='+encodeURIComponent(expectedBlocks[0].code));await page.screenshot({path:path.join(out,'apres-categorie-'+filter+'.png')});}}
    const globalLink=page.locator('.sidebar-note [data-mcg-global]');await globalLink.focus();await page.keyboard.press('Enter');await page.waitForFunction(()=>location.hash==='#/home'&&!document.querySelector('.mcg-filter-notice'));await page.locator('.mcg-cover').waitFor();equal(fragment.id+' '+filter+' avancement global rend organisation intégrale',await page.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(n=>n.dataset.mcgCategory)),O.blocks.map(b=>b.code));
   }
   await page.goto(url+'?slow=1#/home?filter=frequent');await waitHome(page);const filterPaints=await page.evaluate(()=>window.__fragmentPaints);traces.push({fragment:fragment.id,route:'frequent-direct',paints:filterPaints});check(fragment.id+' filtre direct aucun accueil global intermédiaire',filterPaints.every(p=>!p.visible||((!p.heading||p.heading.includes(O.fragment.display_name||O.fragment.label))&&(!p.home||p.filterNotice))),filterPaints);
   fragments.push({id:fragment.id,categories:O.blocks.length,frequent:expectedSets.frequent.length,federal_exam:expectedSets.federal_exam.length});fs.writeFileSync(path.join(out,'filters-progress.json'),JSON.stringify({fragments:fragments.length,checks:checks.length,lastFragment:fragment.id}));
  }
  check('aucune erreur JavaScript',errors.length===0,errors);
  const result={result:'passed',fragments:fragments.length,checks:checks.length,browser:await browser.version(),fragmentDetails:fragments,errors};fs.writeFileSync(path.join(out,'filters-results.json'),JSON.stringify(result,null,2)+'\n');fs.writeFileSync(path.join(out,'paint-traces.json'),JSON.stringify(traces,null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close();server.close()}
})().catch(error=>{fs.writeFileSync(path.join(out,'filters-results.json'),JSON.stringify({result:'failed',checks:checks.length,fragments:fragments.length,errors,error:error.message},null,2)+'\n');fs.writeFileSync(path.join(out,'paint-traces.json'),JSON.stringify(traces,null,2)+'\n');console.error(error);server.close();process.exitCode=1});
