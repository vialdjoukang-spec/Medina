/* Visual access, specialty isolation and working courses in the rebuilt frontends. */
const fs=require('node:fs'), path=require('node:path'), http=require('node:http'), assert=require('node:assert/strict');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright();
const root=path.resolve(__dirname,'..'), directory=path.resolve(process.env.MEDINA_OUT||path.join(root,'dist'));
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'audits/FRONTENDS_2026-10-08'));
const registry=JSON.parse(fs.readFileSync(path.join(root,'fragments.json')));
const checks=[],errors=[],outside=[];
const ATKINSON="'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif", GEORGIA="Georgia,'Times New Roman',serif";
fs.mkdirSync(out,{recursive:true});
function check(name,result,detail){assert.ok(result,name+(detail?' : '+JSON.stringify(detail):''));checks.push(name)}
function payload(source){return JSON.parse(source.match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/)[1])}
async function noOverflow(page,label){const size=await page.evaluate(()=>({width:innerWidth,document:document.documentElement.scrollWidth}));check(label+' : pas de débordement',size.document<=size.width+1,size)}
async function readableSurface(page,selector){return page.locator(selector).first().evaluate(el=>{
 const rgb=s=>(s.match(/[\d.]+/g)||[]).map(Number),luminance=values=>{const v=values.slice(0,3).map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4});return v[0]*.2126+v[1]*.7152+v[2]*.0722};
 let background=[255,255,255],parent=el;
 while(parent){const color=rgb(getComputedStyle(parent).backgroundColor);if(color.length>=3&&(color.length===3||color[3]===1)){background=color;break}parent=parent.parentElement}
 const foreground=luminance(rgb(getComputedStyle(el).color)),light=luminance(background);
 return {background,luminance:light,ratio:(Math.max(foreground,light)+.05)/(Math.min(foreground,light)+.05)};
})}
async function noReadingPatterns(page,label){
 const patterns=await page.evaluate(()=>[...document.querySelectorAll('html,body,#content,.mcg-cover,.mcg-block-heading,.mc-panel,.mc-ilot')].flatMap(el=>[null,'::before','::after'].flatMap(pseudo=>{const style=getComputedStyle(el,pseudo);return /url\(|repeating-|radial-gradient|conic-gradient/.test(style.backgroundImage)&&(!pseudo||!['none','normal'].includes(style.content))?[{tag:el.tagName,class:el.className,pseudo,image:style.backgroundImage}]:[]})));
 check(label+' : surfaces de lecture sans motifs',patterns.length===0,patterns);
}
async function homeInteractions(page,url,organisation,label,keyboard=false){
 await page.goto(url+'#/home');await page.locator('.mcg-cover').waitFor();
 const search=page.locator('.mcg-home-search'),input=search.locator('input[type="search"]');
 check(label+' : recherche accessible depuis l’accueil',await search.getAttribute('role')==='search'&&await input.isVisible());
 const bounds=await search.evaluate(el=>{const r=el.getBoundingClientRect();return [...el.querySelectorAll('input,button')].map(control=>{const c=control.getBoundingClientRect();return {left:c.left,right:c.right,inside:c.left>=r.left-1&&c.right<=r.right+1&&c.left>=-1&&c.right<=innerWidth+1}})});
 check(label+' : recherche et bouton restent dans leur cadre',bounds.every(control=>control.inside),bounds);
 const lesson=organisation.blocks.flatMap(block=>block.lessons)[0];
 if(lesson){
  await input.fill(lesson.code);if(keyboard)await input.press('Enter');else await search.locator('button[type="submit"]').click();
  await page.locator('.mcg-search-heading').waitFor();
  check(label+' : soumettre la recherche ouvre ses résultats',await page.locator('[data-mcg-lesson="'+lesson.code+'"]').count()>0&&(await page.locator('.mcg-search-heading h1').innerText()).includes(lesson.code));
  await noOverflow(page,label+' recherche');
  await page.goto(url+'#/home');await page.locator('.mcg-cover').waitFor();
 }
 await page.locator('[data-mcg-explore]').click();
 await page.waitForFunction(()=>document.activeElement?.id==='mcg-categories-title');
 const position=await page.locator('#mcg-categories-title').evaluate(el=>({top:el.getBoundingClientRect().top,bottom:el.getBoundingClientRect().bottom,topbar:document.querySelector('.topbar').getBoundingClientRect().bottom,height:innerHeight}));
 check(label+' : Explorer atteint les catégories avec le clavier',position.top>=position.topbar-1&&position.bottom<=position.height,position);
 await noOverflow(page,label+' catégories');
}
async function navigoInteractions(page,label){
 await page.setViewportSize({width:1440,height:1000});await page.evaluate(()=>scrollTo(0,0));
 const panel=page.locator('.mc-navigo-panel'),trigger=page.locator('.mc-navigo-trigger');
 check(label+' : Navigo démarre fermé à 1440',!await panel.isVisible());
 await trigger.click();check(label+' : Navigo ouvre le plan à 1440',await panel.isVisible()&&await trigger.getAttribute('aria-expanded')==='true');
 await page.locator('.mc-navigo-close').click();check(label+' : Navigo se referme par son bouton',!await panel.isVisible()&&await trigger.getAttribute('aria-expanded')==='false');
 await trigger.click();await page.keyboard.press('Escape');check(label+' : Navigo se referme avec Échap et rend le focus',!await panel.isVisible()&&await trigger.evaluate(el=>document.activeElement===el));
 await trigger.click();const first=panel.locator('.mc-navigo-item:visible').first();check(label+' : le plan contient des titres accessibles',await first.count()>0);await first.click();
 await page.waitForFunction(()=>document.activeElement?.matches('.mc-ilot h2,.mc-ilot h3,.mc-ilot h4,.mc-sci>h2'));
 await page.waitForFunction(()=>{const heading=document.activeElement,rect=heading.getBoundingClientRect(),bar=document.querySelector('.topbar').getBoundingClientRect();return rect.top>=bar.bottom-1&&rect.bottom<=innerHeight});
 check(label+' : Navigo rejoint un titre visible sous la barre',!await panel.isVisible());
 await page.evaluate(()=>scrollTo(0,0));await page.setViewportSize({width:1480,height:1000});
 await panel.waitFor({state:'visible'});check(label+' : plan permanent dès 1480',await panel.isVisible()&&!await trigger.isVisible());
 const layout=await page.locator('.mc-chap-head h1').evaluate(el=>{const title=el.getBoundingClientRect(),rail=document.querySelector('.mc-navigo-panel').getBoundingClientRect();return {title:title.toJSON(),rail:rail.toJSON(),width:innerWidth}});
 check(label+' : le rail laisse le titre du cours lisible',layout.title.right<=layout.rail.left+1&&layout.title.left>=-1&&layout.rail.right<=layout.width+1,layout);
 await page.keyboard.press('Escape');check(label+' : Échap conserve le rail permanent',await panel.isVisible());await noOverflow(page,label+' rail 1480');
 await page.setViewportSize({width:1440,height:1000});await panel.waitFor({state:'hidden'});
}
async function readerPreferences(page,url,lesson,label){
 const text=page.locator('.mc-panel:not([hidden]) p').first();
 await page.locator('.mc-font').selectOption(GEORGIA);
 const before=await text.evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
 await page.locator('.mc-size-toggle').click();await page.locator('.mc-size-range').evaluate(el=>el.value=24);await page.locator('.mc-size-range').dispatchEvent('input');await page.keyboard.press('Escape');
 check(label+' : le réglage agrandit le texte',await text.evaluate(el=>parseFloat(getComputedStyle(el).fontSize))>before);
 check(label+' : police choisie appliquée au texte',(await text.evaluate(el=>getComputedStyle(el).fontFamily)).startsWith('Georgia'));
 check(label+' : Navigo suit la police choisie',(await page.locator('.mc-navigo-title').evaluate(el=>getComputedStyle(el).fontFamily)).startsWith('Georgia'));
 await noOverflow(page,label+' texte agrandi');
 await page.reload();await page.locator('.mc[data-code="'+lesson.code+'"]').waitFor();
 check(label+' : police et taille conservées à la réouverture',await page.locator('.mc-font').inputValue()===GEORGIA&&await page.locator('.mc-size-range').inputValue()==='24');
 const word=page.locator('.mc-panel:not([hidden]) .mc-w[data-k]').first();
 if(await word.count()){
  await word.click();await page.locator('.mc-dlg[open]').waitFor();
  check(label+' : fenêtre explicative accessible',(await page.locator('.mc-dlg[open] .mc-dlg-b').innerText()).trim()!=='');
  check(label+' : fenêtre suit la police choisie',(await page.locator('.mc-dlg[open] .mc-dlg-b').evaluate(el=>getComputedStyle(el).fontFamily)).startsWith('Georgia'));
  await page.keyboard.press('Escape');
 }
 await page.evaluate(()=>scrollTo(0,0));await page.locator('.mc-font').selectOption(ATKINSON);await page.locator('.mc-size-toggle').click();await page.locator('.mc-size-reset').click();await page.keyboard.press('Escape');
 await page.locator('.mc-book').click();check(label+' : mode livre accessible',await page.locator('.mc.book').count()===1&&await page.locator('.mc-book').getAttribute('aria-pressed')==='true');
 const body=page.locator('.mc-panel:not([hidden]) .mc-body'),pager=page.locator('.mc-panel:not([hidden]) .mc-pager');
 check(label+' : pagination du livre visible',await pager.isVisible());
 if(await body.evaluate(el=>el.children.length>1)){
  await pager.locator('.mc-next').click();await page.waitForFunction(()=>document.querySelector('.mc-panel:not([hidden]) .mc-body').scrollLeft>0);
  check(label+' : livre passe à la page suivante',await body.evaluate(el=>el.scrollLeft)>0);
  await pager.locator('.mc-prev').click();await page.waitForFunction(()=>document.querySelector('.mc-panel:not([hidden]) .mc-body').scrollLeft<=1);
 }
 await noOverflow(page,label+' mode livre');await page.reload();await page.locator('.mc.book').waitFor();
 check(label+' : mode livre conservé à la réouverture',await page.locator('.mc-book').getAttribute('aria-pressed')==='true');await page.locator('.mc-book').click();
 await page.goto(url+'#/home');await page.locator('.mcg-resume').waitFor();
 check(label+' : reprendre pointe vers la dernière lecture réelle',await page.locator('.mcg-resume').getAttribute('href')===lesson.url&&(await page.locator('.mcg-resume').innerText()).includes(lesson.code));
 await page.locator('.mcg-resume').click();await page.locator('.mc[data-code="'+lesson.code+'"]').waitFor();
 check(label+' : reprendre rouvre ce cours',await page.locator('.mc').getAttribute('data-code')===lesson.code);
}
async function cardContrast(page,selector){return page.locator(selector).evaluateAll(cards=>{
 const luminance=color=>{const values=color.match(/[\d.]+/g).slice(0,3).map(Number).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4});return values[0]*.2126+values[1]*.7152+values[2]*.0722};
 return cards.map(card=>{const title=card.querySelector('h2,h3'),fg=luminance(getComputedStyle(title).color),bg=luminance(getComputedStyle(card).backgroundColor);return {title:title.textContent,ratio:(Math.max(fg,bg)+.05)/(Math.min(fg,bg)+.05)}});
})}
const server=http.createServer((req,res)=>{const name=decodeURIComponent(new URL(req.url,'http://local').pathname).replace(/^\//,'')||'index.html';const file=path.resolve(directory,name);if(!file.startsWith(directory+path.sep)||!fs.existsSync(file)){res.writeHead(404);res.end();return}res.setHeader('Content-Type','text/html;charset=utf-8');res.end(fs.readFileSync(file))});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const origin='http://127.0.0.1:'+server.address().port, browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'dark',reducedMotion:'reduce'});
  await context.addInitScript(()=>{localStorage.setItem('medora.atlas.v3',JSON.stringify({theme:'night'}));localStorage.setItem('medina.theme','dark')});
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
   const visual=await page.evaluate(()=>({font:getComputedStyle(document.querySelector('.mcg-cover h1')).fontFamily,scheme:getComputedStyle(document.documentElement).colorScheme})),surface=await readableSurface(page,'body');
   check(f.id+' : clair même avec système et préférence sombres',visual.scheme.includes('light')&&!visual.scheme.includes('dark')&&surface.luminance>=.75,{...visual,...surface});
   check(f.id+' : Atkinson Hyperlegible Next affichée',visual.font.includes('Atkinson Hyperlegible Next'),visual);
   const brand=await readableSurface(page,'.brand strong');check(f.id+' : marque lisible',brand.ratio>=4.5,brand);
   const contrasts=await cardContrast(page,'.mcg-category-card');check(f.id+' : toutes les catégories atteignent 4,5:1',contrasts.every(card=>card.ratio>=4.5),contrasts.filter(card=>card.ratio<4.5));
   await noOverflow(page,f.id+' accueil bureau');
   await noReadingPatterns(page,f.id+' accueil');await homeInteractions(page,url,O,f.id+' bureau');
   await page.goto(url+'#/home');await page.locator('.mcg-cover').waitFor();
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
    check(f.id+' : police du cours par défaut',await page.locator('.mc-font').inputValue()===ATKINSON);
    check(f.id+' : texte du cours rendu en Atkinson',(await page.locator('.mc-panel:not([hidden]) p').first().evaluate(p=>getComputedStyle(p).fontFamily)).includes('Atkinson Hyperlegible Next'));
    const text=await readableSurface(page,'.mc-panel:not([hidden]) p');check(f.id+' : texte du cours lisible',text.ratio>=4.5,text);await noReadingPatterns(page,f.id+' cours');
    for(let i=0;i<4;i++){await page.locator('.mc-tabs button').nth(i).click();check(f.id+' : onglet '+(i+1)+' lisible',await page.locator('.mc-panel:not([hidden])').count()===1);await noOverflow(page,f.id+' onglet '+(i+1))}
    await page.locator('.mc-tabs button').first().click();
    await navigoInteractions(page,f.id);await readerPreferences(page,url,l,f.id);
   }
   await page.goto(url+'#/method');await page.locator('.mcg-search-heading').waitFor();
   check(f.id+' : repères de lecture propres à la spécialité',(await page.locator('#content').innerText()).includes(O.fragment.display_name)&&!(await page.locator('#content').innerText()).includes('67 spécialités'));
   await page.setViewportSize({width:390,height:844});await page.goto(url+'#/home');await page.locator('.mcg-cover').waitFor();await noOverflow(page,f.id+' accueil mobile');
   await homeInteractions(page,url,O,f.id+' mobile',true);await page.goto(url+'#/home');await page.locator('.mcg-cover').waitFor();
   await page.locator('#menu-toggle').click();check(f.id+' : menu mobile accessible',await page.locator('#menu-toggle').getAttribute('aria-expanded')==='true');
   await page.keyboard.press('Escape');check(f.id+' : menu mobile refermable',await page.locator('#menu-toggle').getAttribute('aria-expanded')==='false');
   if(['T1','S01','S02'].includes(f.id)){await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(out,f.id+'-mobile.png')});await page.setViewportSize({width:1440,height:1100});await page.screenshot({path:path.join(out,f.id+'-desktop.png')});}
   await page.setViewportSize({width:1440,height:1000});
  }
  await page.goto(origin+'/index.html');await page.evaluate(()=>document.fonts.ready);
  const links=page.locator('a[href^="fragments/"]');check('Accueil : '+registry.length+' accès distincts',await links.count()===registry.length);
  check('Accueil : police Atkinson affichée',(await page.locator('.hero h1').evaluate(p=>getComputedStyle(p).fontFamily)).includes('Atkinson Hyperlegible Next'));
  const contrasts=await cardContrast(page,'.specialty-card');check('Accueil : toutes les couleurs atteignent 4,5:1',contrasts.length===registry.length&&contrasts.every(card=>card.ratio>=4.5),contrasts.filter(card=>card.ratio<4.5));
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
})().catch(error=>{fs.writeFileSync(path.join(out,'result.json'),JSON.stringify({result:'failed',checks:checks.length,fragments:registry.length,errors,outside,failure:error.message},null,2)+'\n');console.error(error);server.close();process.exitCode=1});
