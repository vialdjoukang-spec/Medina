/* Categories in the original fragments, preserving the medical course engines. */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright(),root=path.resolve(__dirname,'..');
const directory=path.resolve(process.env.MEDINA_FRAGMENTS||path.join(root,'dist/fragments'));
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'audits/CATEGORIES_2026-10-07'));
const targeted=process.argv.includes('--targeted'),fragments=JSON.parse(fs.readFileSync(path.join(root,'fragments.json'),'utf8'));
const names=new Map(JSON.parse(fs.readFileSync(path.join(root,'organisation/fragments.json'),'utf8')).map(item=>[item.id,item]));
const checks=[],errors=[],requests=[];fs.mkdirSync(path.join(out,'captures'),{recursive:true});
const check=(name,ok,detail)=>{assert.ok(ok,name+(detail===undefined?'':': '+JSON.stringify(detail)));checks.push(name)};
const colourParts=value=>value.match(/[\d.]+/g).slice(0,3).map(Number);
const luminance=rgb=>rgb.map(value=>{const s=value/255;return s<=.04045?s/12.92:((s+.055)/1.055)**2.4}).reduce((sum,value,i)=>sum+value*[.2126,.7152,.0722][i],0);
const contrast=(a,b)=>(Math.max(luminance(a),luminance(b))+.05)/(Math.min(luminance(a),luminance(b))+.05);
async function overflow(page,label){const sizes=await page.evaluate(()=>({window:innerWidth,document:document.documentElement.scrollWidth}));check(label,sizes.document<=sizes.window+1,sizes)}
async function go(page,hash,selector){await page.evaluate(value=>{location.hash=value},hash);await page.locator(selector).first().waitFor()}
(async()=>{
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
  await context.route(/^https?:/,route=>{requests.push(route.request().url());return route.abort()});
  const page=await context.newPage();page.on('pageerror',error=>errors.push(error.message));
  const requested=process.env.MEDINA_CATEGORY_FRAGMENT_IDS?.split(',');
  const selected=requested?fragments.filter(item=>requested.includes(item.id)):targeted?fragments.filter(item=>['S01','S02','S07','S03','T2'].includes(item.id)):fragments;
  for(const fragment of selected){
   const file=path.join(directory,`MEDINA_${fragment.id}_${fragment.slug}.html`),source=fs.readFileSync(file,'utf8');
   const match=source.match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/);
   check(fragment.id+' : navigation catégorielle embarquée',!!match);
   const data=JSON.parse(match[1]),catalogue=JSON.parse(source.match(/<script id="medora-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
   const codes=data.blocks.flatMap(block=>block.lessons.flatMap(lesson=>lesson.variants.map(variant=>variant.code))),expected=catalogue.entries.map(entry=>entry.code);
   check(fragment.id+' : toutes les catégories conservées sans doublon',JSON.stringify([...codes].sort())===JSON.stringify([...expected].sort())&&new Set(codes).size===codes.length);
   check(fragment.id+' : noms conformes au registre',data.fragment.label===names.get(fragment.id).label&&data.version==='CIM-10-GM 2024');
   check(fragment.id+' : ordre continu des catégories et chapitres',data.blocks.every((block,i)=>block.order===i+1&&block.lessons.every((lesson,j)=>lesson.order===j+1&&lesson.code&&lesson.title)));
   await page.goto(pathToFileURL(file).href);await page.waitForFunction(()=>window.MEDINA_CATEGORY_ORGANISATION&&document.querySelector('.mcg-home'));
   check(fragment.id+' : nom du fragment visible',(await page.locator('.mcg-cover h1').innerText()).replace(/\.$/,'')===(data.fragment.display_name||data.fragment.label));
   check(fragment.id+' : un bouton par catégorie',await page.locator('[data-mcg-category]').count()===data.blocks.length);
   check(fragment.id+' : catégories présentes dans la bande latérale',await page.locator('[data-mcg-sidebar-category]').count()===data.blocks.length);
   await overflow(page,fragment.id+' : accueil bureau sans débordement');
   if(!data.blocks.length){check(fragment.id+' : absence de catalogue explicitée',(await page.locator('#content').innerText()).includes('Aucune catégorie CIM rattachée'));continue}
   const colours=await page.locator('.mcg-category-card').evaluateAll(cards=>cards.map(card=>({bg:getComputedStyle(card).backgroundColor,fg:getComputedStyle(card.querySelector('h2')).color})));
   check(fragment.id+' : une couleur distincte par catégorie',new Set(colours.map(c=>c.bg)).size===data.blocks.length);
   check(fragment.id+' : titres à contraste AA',colours.every(c=>contrast(colourParts(c.bg),colourParts(c.fg))>=4.5));
   const sideCodes=await page.locator('.mcg-sidebar-block>summary>small').evaluateAll(items=>items.map(item=>({bg:getComputedStyle(item).backgroundColor,fg:getComputedStyle(item).color,opacity:getComputedStyle(item).opacity})));
   check(fragment.id+' : codes latéraux lisibles',sideCodes.every(c=>c.opacity==='1'&&contrast(colourParts(c.bg),colourParts(c.fg))>=4.5));
   const corners=await page.locator('.mcg-category-card').evaluateAll(cards=>cards.map(card=>{const p=card.getBoundingClientRect(),c=card.querySelector('.mcg-code').getBoundingClientRect(),t=card.querySelector('h2').getBoundingClientRect();return c.bottom<t.top&&p.right-c.right>=5&&p.right-c.right<=20&&c.top-p.top>=5&&c.top-p.top<=20}));
   check(fragment.id+' : code en haut à droite sans chevauchement',corners.every(Boolean));
   for(const block of (targeted?data.blocks.slice(0,3):data.blocks)){
    await go(page,'#/home?category='+encodeURIComponent(block.code),'[data-mcg-block]');
    await page.waitForFunction(code=>document.querySelector('[data-mcg-block]')?.dataset.mcgBlock===code,block.code);
    const rows=await page.locator('[data-mcg-lesson]').evaluateAll(items=>items.map(item=>({code:item.dataset.mcgLesson,title:item.querySelector('.mcg-lesson-title').textContent,rank:item.querySelector('.mcg-lesson-rank').textContent})));
    check(fragment.id+' / '+block.code+' : chapitres nommés et numérotés',JSON.stringify(rows)===JSON.stringify(block.lessons.map(lesson=>({code:lesson.code,title:lesson.title,rank:lesson.order+'.'}))));
   }
   const available=new Map(data.blocks.flatMap(block=>block.lessons.filter(lesson=>lesson.integrated&&lesson.source_fragment_id===fragment.id).map(lesson=>[lesson.code,lesson])));
   if(available.size){await page.waitForFunction(()=>window.MDN_READY===true);for(const lesson of (targeted?[available.values().next().value]:available.values())){
    await go(page,'#/entry/'+lesson.code,'.mc[data-code="'+lesson.code+'"]');
    check(fragment.id+' / '+lesson.code+' : cours et quatre onglets préservés',await page.locator('.mc-tabs button').count()===4&&await page.locator('.mc-ilot').count()>0);
    check(fragment.id+' / '+lesson.code+' : fil d’Ariane nommé',(await page.locator('.mcg-breadcrumbs').innerText()).includes(lesson.code+' — '+lesson.title));
   }}
   if(fragment.id==='S02'){
    const bronchitis=data.blocks.flatMap(block=>block.lessons).filter(lesson=>lesson.code==='J40');
    if(bronchitis.length){check('Bronchite : un cours canonique et ses renvois',bronchitis.filter(lesson=>!lesson.reference).length===1&&bronchitis.every(lesson=>lesson.title==='Bronchite'&&['J40','J41','J42'].every(code=>lesson.covers.some(variant=>variant.code===code))));await go(page,'#/search?q=Bronchite','[data-mcg-lesson="J40"]');check('Recherche : une seule carte Bronchite',await page.locator('[data-mcg-lesson="J40"]').count()===1);if(available.has('J40')){const searchedCodes=await page.locator('[data-mcg-lesson="J40"] [data-mcg-variant]').evaluateAll(items=>items.map(item=>item.dataset.mcgVariant));check('Recherche : les quatre aspects Bronchite restent nommés',JSON.stringify(searchedCodes)===JSON.stringify(['J20','J40','J41','J42']))}}
    await go(page,'#/search?q=J45','[data-mcg-lesson="J45"]');check('Recherche : Asthme nommé',(await page.locator('[data-mcg-lesson="J45"]').innerText()).includes('Asthme'));
    await go(page,'#/entry/J46','.mc[data-code="J45"]');check('J46 ouvre le cours Asthme',await page.locator('.mc[data-code="J45"]').count()===1);
    await go(page,'#/entry/J43','.mc[data-code="J44"]');check('J43 ouvre le cours Bronchopneumopathie chronique obstructive',await page.locator('.mc[data-code="J44"]').count()===1&&(await page.locator('.mcg-breadcrumbs').innerText()).includes('J44 — Bronchopneumopathie chronique obstructive'));
    if(available.has('J40'))for(const code of ['J20','J41','J42']){await go(page,'#/entry/'+code,'.mc[data-code="J40"]');check(code+' ouvre le même cours Bronchite',await page.locator('.mc[data-code="J40"]').count()===1)}
    await go(page,'#/home','.mcg-category-card');await page.screenshot({path:path.join(out,'captures/pneumologie_categories_desktop.png')});
    await page.locator('[data-mcg-category="J40-J47"]').click();await page.locator('[data-mcg-block="J40-J47"]').waitFor();await page.screenshot({path:path.join(out,'captures/pneumologie_chapitres_desktop.png')});
   }
   const planned=data.blocks.flatMap(block=>block.lessons.map(lesson=>({block,lesson}))).find(item=>!item.lesson.integrated);
   if(planned){await go(page,'#/home?category='+encodeURIComponent(planned.block.code)+'&lesson='+encodeURIComponent(planned.lesson.code),'#mcg-planned-title');check(fragment.id+' : chapitre absent marqué à produire',(await page.locator('.mcg-planned-panel').innerText()).includes('Cours à produire')&&(await page.locator('#mcg-planned-title').innerText())===planned.lesson.title)}
   await page.setViewportSize({width:390,height:844});await go(page,'#/home','.mcg-category-card');await overflow(page,fragment.id+' : accueil mobile sans débordement');await page.locator('.mcg-category-card').first().click();await page.locator('[data-mcg-block]').waitFor();await overflow(page,fragment.id+' : chapitres mobiles sans débordement');if(fragment.id==='S02')await page.screenshot({path:path.join(out,'captures/pneumologie_chapitres_mobile.png')});await page.setViewportSize({width:1440,height:1000});
  }
  const cardio=fragments.find(fragment=>fragment.id==='S01');await page.goto(pathToFileURL(path.join(directory,`MEDINA_S01_${cardio.slug}.html`)).href+'#/entry/I21');await page.waitForFunction(()=>window.MDN_READY===true);await page.locator('.mc[data-code="I21"]').waitFor();
  check('Navigo permanent conservé',await page.locator('.mc-navigo-panel').isVisible());await page.locator('.mc-tabs button').nth(1).click();const quiz=page.locator('.mc-panel:not([hidden]) .mc-quiz').first();await quiz.locator('.mc-opt').first().click();check('Correction du QCM conservée',await quiz.locator('.mc-fb').isVisible());await page.locator('.mc-tabs button').first().click();await page.locator('.mc-panel:not([hidden]) .mc-w[data-k]').first().click();check('Fenêtre interactive conservée',await page.locator('.mc-dlg[open]').isVisible());await page.locator('.mc-dlg .mc-x').click();await page.locator('.mc-size-toggle').click();await page.locator('.mc-size-range').evaluate(element=>{element.value='21';element.dispatchEvent(new Event('input',{bubbles:true}))});check('Taille de lecture conservée',await page.locator('.mc').evaluate(element=>element.style.getPropertyValue('--mc-fs'))==='21px');await page.keyboard.press('Escape');await page.locator('.mc-book').click();check('Mode Livre conservé',await page.locator('.mc.book').count()===1);await go(page,'#/clinical-skills','.cs-page');check('Sémiologie CS conservée',await page.locator('.cs-page').count()===1);
  check('Aucune ressource distante demandée',requests.length===0,requests);check('Aucune erreur JavaScript',errors.length===0,errors);
  fs.writeFileSync(path.join(out,targeted?'targeted_categories.json':'categories_results.json'),JSON.stringify({result:'OK',targeted,fragments:selected.length,checks,errors,requests},null,2)+'\n');console.log(JSON.stringify({result:'OK',targeted,fragments:selected.length,checks:checks.length,errors}));
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
