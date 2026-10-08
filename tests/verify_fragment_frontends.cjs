/* Visual access, specialty isolation and working courses in the rebuilt frontends. */
const fs=require('node:fs'), path=require('node:path'), http=require('node:http'), assert=require('node:assert/strict');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright();
const root=path.resolve(__dirname,'..'), directory=path.resolve(process.env.MEDINA_OUT||path.join(root,'dist'));
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'audits/FRONTENDS_2026-10-08'));
const registry=JSON.parse(fs.readFileSync(path.join(root,'fragments.json')));
const checks=[],errors=[],outside=[];
fs.mkdirSync(out,{recursive:true});
function check(name,result,detail){assert.ok(result,name+(detail?' : '+JSON.stringify(detail):''));checks.push(name)}
function payload(source){return JSON.parse(source.match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/)[1])}
async function noOverflow(page,label){const size=await page.evaluate(()=>({width:innerWidth,document:document.documentElement.scrollWidth}));check(label+' : pas de débordement',size.document<=size.width+1,size)}
const server=http.createServer((req,res)=>{const name=decodeURIComponent(new URL(req.url,'http://local').pathname).replace(/^\//,'')||'index.html';const file=path.resolve(directory,name);if(!file.startsWith(directory+path.sep)||!fs.existsSync(file)){res.writeHead(404);res.end();return}res.setHeader('Content-Type','text/html;charset=utf-8');res.end(fs.readFileSync(file))});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const origin='http://127.0.0.1:'+server.address().port, browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'dark',reducedMotion:'reduce'});
  await context.route(/^https?:/,route=>{if(new URL(route.request().url()).origin===origin)return route.continue();outside.push(route.request().url());return route.abort()});
  const page=await context.newPage();page.on('pageerror',error=>errors.push(error.message));
  for(const f of registry){
   const file=path.join(directory,'fragments','MEDINA_'+f.id+'_'+f.slug+'.html'),source=fs.readFileSync(file,'utf8'),O=payload(source);
   const available=new Map(O.blocks.flatMap(b=>b.lessons.filter(l=>l.integrated).map(l=>[l.code,l])));
   check(f.id+' : les cours appartiennent uniquement à la spécialité',O.blocks.every(b=>b.lessons.every(l=>l.source_fragment_id===f.id&&(!l.integrated||l.url.startsWith('#/entry/')))));
   check(f.id+' : police exacte embarquée',source.includes('id="medina-typography"')&&source.includes('data:font/woff2;base64,'));
   const url=origin+'/fragments/'+path.basename(file);await page.goto(url);
   await page.waitForFunction(()=>document.querySelector('.mcg-cover')&&(!document.querySelector('#mdn-pack')||window.MDN_READY));await page.evaluate(()=>document.fonts.ready);
   check(f.id+' : accueil de la bonne spécialité',(await page.locator('.mcg-cover h1').innerText()).replace(/\.$/,'')===O.fragment.display_name);
   check(f.id+' : toutes les catégories sont visibles',await page.locator('.mcg-category-card').count()===O.blocks.length);
   check(f.id+' : un frontend distinct',await page.locator('html').getAttribute('data-medina-fragment')===f.id);
   const visual=await page.evaluate(()=>({font:getComputedStyle(document.querySelector('.mcg-cover h1')).fontFamily,scheme:getComputedStyle(document.documentElement).colorScheme,body:getComputedStyle(document.body).backgroundColor,brand:getComputedStyle(document.querySelector('.brand strong')).color}));
   check(f.id+' : clair même avec système sombre',!visual.scheme.includes('dark')&&visual.body==='rgb(250, 249, 246)',visual);
   check(f.id+' : Anthropic Serif affichée',visual.font.includes('Anthropic Serif'),visual);
   check(f.id+' : marque lisible',visual.brand==='rgb(41, 40, 33)',visual);
   await noOverflow(page,f.id+' accueil bureau');
   if(O.blocks.length){
    const b=O.blocks[0];await page.locator('.mcg-category-card').first().click();await page.locator('[data-mcg-block]').waitFor();
    check(f.id+' : catégorie ouvre ses chapitres',await page.locator('.mcg-lesson').count()===b.lessons.length);
    check(f.id+' : nom de catégorie sobre',await page.locator('.mcg-block-heading h2').innerText()===b.title);
    const planned=b.lessons.find(l=>!l.integrated);if(planned){await page.locator('[data-mcg-lesson="'+planned.code+'"] .mcg-lesson-main').click();await page.locator('#mcg-planned-title').waitFor();check(f.id+' : chapitre annoncé en préparation',(await page.locator('.mcg-planned-panel').innerText()).toLocaleLowerCase('fr').includes('en préparation'))}
   }
   await page.goto(url+'#/search?available=1');await page.locator('.mcg-search-heading').waitFor();
   check(f.id+' : accès direct aux cours',await page.locator('.mcg-lesson').count()===available.size);
   if(available.size){
    const l=[...available.values()][0];await page.goto(url+'#/entry/'+l.code);await page.locator('.mc[data-code="'+l.code+'"]').waitFor();
    check(f.id+' : les quatre onglets restent disponibles',await page.locator('.mc-tabs button').count()===4);
    check(f.id+' : police du cours par défaut',await page.locator('.mc-font').inputValue()==="'Anthropic Serif',Georgia,serif");
    for(let i=0;i<4;i++){await page.locator('.mc-tabs button').nth(i).click();check(f.id+' : onglet '+(i+1)+' lisible',await page.locator('.mc-panel:not([hidden])').count()===1);await noOverflow(page,f.id+' onglet '+(i+1))}
    await page.locator('.mc-tabs button').first().click();
    const word=page.locator('.mc-panel:not([hidden]) .mc-w[data-k]').first();if(await word.count()){await word.click();await page.locator('.mc-dlg[open]').waitFor();check(f.id+' : fenêtre explicative accessible',await page.locator('.mc-dlg[open] .mc-dlg-b').innerText()!=='');await page.keyboard.press('Escape')}
   }
   await page.goto(url+'#/method');await page.locator('.mcg-search-heading').waitFor();
   check(f.id+' : repères de lecture propres à la spécialité',(await page.locator('#content').innerText()).includes(O.fragment.display_name)&&!(await page.locator('#content').innerText()).includes('67 spécialités'));
   await page.setViewportSize({width:390,height:844});await page.goto(url+'#/home');await page.locator('.mcg-cover').waitFor();await noOverflow(page,f.id+' accueil mobile');
   await page.locator('#menu-toggle').click();check(f.id+' : menu mobile accessible',await page.locator('#menu-toggle').getAttribute('aria-expanded')==='true');
   await page.keyboard.press('Escape');check(f.id+' : menu mobile refermable',await page.locator('#menu-toggle').getAttribute('aria-expanded')==='false');
   if(['T1','S01','S02'].includes(f.id)){await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(out,f.id+'-mobile.png')});await page.setViewportSize({width:1440,height:1100});await page.screenshot({path:path.join(out,f.id+'-desktop.png')});}
   await page.setViewportSize({width:1440,height:1000});
  }
  await page.goto(origin+'/index.html');await page.evaluate(()=>document.fonts.ready);
  const links=page.locator('a[href^="fragments/"]');check('Accueil : 22 accès distincts',await links.count()===22);
  await noOverflow(page,'Portail bureau');await page.screenshot({path:path.join(out,'accueil-desktop.png')});
  await page.setViewportSize({width:390,height:844});await noOverflow(page,'Portail mobile');await page.screenshot({path:path.join(out,'accueil-mobile.png')});
  const preview=path.join(directory,'apercus/infectiologie.html');if(fs.existsSync(preview)){
   await page.goto(origin+'/apercus/infectiologie.html#/entry/A41');await page.locator('.mc[data-code="A41"]').waitFor();
   check('Aperçu : statut de rédaction explicite',(await page.locator('body').innerText()).includes('Version de travail'));
   check('Aperçu : aucune validation finale annoncée',await page.evaluate(()=>window.MEDINA_WORK_PREVIEW.final_validation===false&&window.MEDINA_COMPLETE.length===0));
   check('Aperçu : quatre onglets',await page.locator('.mc-tabs button').count()===4);await noOverflow(page,'Aperçu mobile');
   await page.setViewportSize({width:1440,height:1050});await page.screenshot({path:path.join(out,'cours-en-redaction.png')});
  }
  check('Aucune erreur JavaScript',errors.length===0,errors);check('Aucune ressource distante pour consulter',outside.length===0,outside);
  fs.writeFileSync(path.join(out,'result.json'),JSON.stringify({result:'passed',checks:checks.length,fragments:registry.length,browser:await browser.version(),errors,outside},null,2)+'\n');
  console.log(JSON.stringify({result:'passed',checks:checks.length,fragments:registry.length,out}));
 }finally{await browser.close();server.close()}
})().catch(error=>{console.error(error);server.close();process.exitCode=1});
