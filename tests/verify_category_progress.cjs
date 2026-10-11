/* Independent browser evidence for per-category progress and compact curriculum views. */
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright(),root=path.resolve(__dirname,'..');
const directory=path.resolve(process.env.MEDINA_OUT||path.join(root,'dist'));
const baseline=process.env.MEDINA_BASELINE?path.resolve(process.env.MEDINA_BASELINE):null;
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'work/frontend-categories'));
const captureOut=path.join(out,'captures');fs.mkdirSync(captureOut,{recursive:true});
const allFragments=JSON.parse(fs.readFileSync(path.join(root,'fragments.json'),'utf8')),requestedIds=process.env.MEDINA_CATEGORY_FRAGMENT_IDS?.split(',');
const registry=requestedIds?allFragments.filter(fragment=>requestedIds.includes(fragment.id)):allFragments;
const compact=process.env.MEDINA_TEST_COMPACT==='1';
const checks=[],errors=[],fragments=[];let courseComparisons=0,categoriesChecked=0,starChecks=0,modalOpenedBy=null;
const digest=value=>crypto.createHash('sha256').update(JSON.stringify(value)).digest('hex');
function check(name,value,detail){assert.ok(value,name+(detail===undefined?'':' : '+JSON.stringify(detail)));checks.push(name);}
function equal(name,value,expected){check(name,JSON.stringify(value)===JSON.stringify(expected),JSON.stringify({value,expected}).length>2000?{valueHash:digest(value),expectedHash:digest(expected)}:{value,expected});}
function payload(file){return JSON.parse(fs.readFileSync(file,'utf8').match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);}
function expectations(O,block){
 // Category membership comes from the canonical catalogue, not a course's anatomical alias block.
 // Every lesson counts once per category; a shared course may legitimately belong to two categories.
 const inventory=new Map(O.nosology.lessons.filter(lesson=>!lesson.code.includes('.')).map(lesson=>[lesson.code,lesson]));
 const codes=[...new Set(block.lessons.map(lesson=>lesson.code).filter(code=>!code.includes('.')))];
 const all=codes.map(code=>inventory.get(code)).filter(Boolean),federal=all.filter(lesson=>lesson.gold_star?.enabled);
 const fraction=lessons=>{const filled=lessons.filter(lesson=>lesson.state==='filled').length,total=lessons.length;
  // Two decimals with even tie rounding, independently derived from the exact fraction.
  const scaled=10000*filled,units=total?Math.floor(scaled/total):0,remainder=total?scaled%total:0;
  const rounded=units+(total&&(2*remainder>total||(2*remainder===total&&units%2))?1:0);
  return {filled,total,percent:rounded/100};};
 return {federal_exam:fraction(federal),global:fraction(all)};
}
const server=http.createServer((req,res)=>{
 const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname),isBaseline=pathname.startsWith('/__baseline__/');
 const base=isBaseline?baseline:directory;if(!base){res.writeHead(404).end();return;}
 const relative=isBaseline?pathname.slice('/__baseline__'.length):pathname;
 const file=path.resolve(base,'.'+relative);if(!file.startsWith(base+path.sep)){res.writeHead(403).end();return;}
 fs.readFile(file,(error,data)=>{if(error){res.writeHead(404).end();return;}res.setHeader('Content-Type',file.endsWith('.html')?'text/html; charset=utf-8':file.endsWith('.woff2')?'font/woff2':'application/octet-stream');res.end(data);});
});
async function ready(page){await page.waitForFunction(()=>window.MEDINA_CATEGORY_ORGANISATION&&(!document.querySelector('#mdn-pack')||window.MDN_READY===true));}
async function go(page,hash){await page.evaluate(value=>location.hash=value,hash);await page.waitForFunction(value=>location.hash===value,hash);await page.waitForTimeout(60);}
async function noOverflow(page,label){const size=await page.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth}));check(label+' sans débordement',size.width<=size.viewport+1,size);}
async function metricData(scope){return scope.locator('[data-mcg-progress-kind]').evaluateAll(nodes=>nodes.map(node=>({kind:node.dataset.mcgProgressKind,count:node.querySelector('[data-mcg-progress-count]')?.textContent,percent:node.querySelector('[data-mcg-progress-percent]')?.textContent,filled:Number(node.querySelector('progress')?.value),max:Number(node.querySelector('progress')?.max)})));}
async function verifyMetrics(scope,label,expected){
 check(label+' métriques sans contrôles interactifs',await scope.locator('a,button,[tabindex],[onclick]').count()===0&&(await scope.getAttribute('tabindex'))===null&&(await scope.getAttribute('onclick'))===null);
 const metrics=await metricData(scope);equal(label+' deux métriques dans ordre fédéral/global',metrics.map(metric=>metric.kind),['federal_exam','global']);
 for(const metric of metrics){const wanted=expected[metric.kind],match=metric.count?.match(/(\d+)\s*\/\s*(\d+)/);check(label+' '+metric.kind+' fraction lisible',!!match,metric.count);equal(label+' '+metric.kind+' A/B exact',[Number(match[1]),Number(match[2])],[wanted.filled,wanted.total]);
  const shown=Number((metric.percent||'').replace(/[^\d,.-]/g,'').replace(',','.'));equal(label+' '+metric.kind+' pourcentage exact',shown,wanted.percent);equal(label+' '+metric.kind+' jauge exacte',[metric.filled,metric.max],[wanted.filled,Math.max(1,wanted.total)]);
 }
}
async function courseSnapshot(page,code){
 await page.locator('.mc[data-code="'+code+'"]').waitFor();await page.waitForFunction(()=>[...document.querySelectorAll('.mc .mc-panel')].every(panel=>{const ol=panel.querySelector('.mc-toc ol'),n=parseInt(panel.querySelector('.mc-ilot h2 .mc-n')?.textContent,10);return !ol||Number.isNaN(n)||ol.children.length!==panel.querySelectorAll(':scope .mc-body>.mc-ilot').length||ol.start===n;}));
 return page.locator('.mc').evaluate(element=>({heading:element.querySelector('.mc-chap-head h1')?.textContent.trim(),tabs:[...element.querySelectorAll('.mc-tabs button')].map(node=>node.textContent),panels:[...element.querySelectorAll('.mc-panel')].map(node=>node.innerHTML),dialogs:[...element.querySelectorAll('.mc-dlg')].map(node=>node.innerHTML),paragraphStyles:[...element.querySelectorAll('.mc-body p')].slice(0,5).map(node=>{const style=getComputedStyle(node);return {family:style.fontFamily,size:style.fontSize,lineHeight:style.lineHeight,color:style.color,weight:style.fontWeight};})}));
}
async function verifyStars(page,O,label){
 const flags=new Map(O.blocks.flatMap(block=>block.lessons).map(lesson=>[lesson.code,!!lesson.gold_star?.enabled])),titles=new Map(O.blocks.flatMap(block=>block.lessons).map(lesson=>[lesson.code,lesson.title.trim()]));
 const rows=await page.locator('[data-mcg-lesson] .mcg-lesson-title,.mcg-sidebar-title:visible,.mc-chap-head h1').evaluateAll(titles=>titles.map(title=>{
  const star=title.querySelector('.nosology-gold'),code=title.closest('[data-mcg-lesson]')?.dataset.mcgLesson||title.closest('[data-mcg-sidebar-lesson]')?.dataset.mcgSidebarLesson||title.closest('.mc')?.dataset.code;const reader=title.matches('.mc-chap-head h1');
  if(!star)return {code,reader,marked:false,text:title.textContent.trim()};
  const walker=document.createTreeWalker(title,NodeFilter.SHOW_TEXT),nodes=[];let node;while((node=walker.nextNode()))if(!node.parentElement.closest('.nosology-gold')&&node.data.trim())nodes.push(node);
  const last=nodes.at(-1);let lastRect=null;if(last){const index=last.data.search(/\S\s*$/),range=document.createRange();range.setStart(last,Math.max(0,index));range.setEnd(last,Math.max(0,index)+1);lastRect=range.getBoundingClientRect().toJSON();}
  return {code,reader,marked:true,text:nodes.map(n=>n.data).join('').trim(),superscript:!!star.closest('sup'),decorativeSvg:!!star.querySelector('svg'),star:star.getBoundingClientRect().toJSON(),last:lastRect,title:title.getBoundingClientRect().toJSON(),clipped:getComputedStyle(title).textOverflow==='ellipsis'||getComputedStyle(title).webkitLineClamp!=='none'};
 }));
 for(const row of rows){if(!row.reader)equal(label+' '+row.code+' titre intégral conservé',row.text,titles.get(row.code));equal(label+' '+row.code+' étoile liée aux métadonnées',row.marked,flags.get(row.code));if(!row.marked)continue;
  check(label+' '+row.code+' étoile en exposant à droite du dernier caractère',row.superscript&&row.last&&row.star.left>=row.last.right-2&&row.star.top<=row.last.top+3&&row.star.bottom<=row.last.bottom+3&&row.star.right<=row.title.right+3,row);
  check(label+' '+row.code+' symbole réaliste visible sans titre tronqué',row.decorativeSvg&&row.star.width>=8&&row.star.width<=30&&row.star.height>=8&&!row.clipped,row);starChecks++;
 }
}
async function compactCards(page,label){
 const cards=await page.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(node=>{const heading=node.querySelector('h2'),style=getComputedStyle(heading),rect=node.getBoundingClientRect(),title=heading.getBoundingClientRect(),box=getComputedStyle(node);return {code:node.dataset.mcgCategory,height:rect.height,padding:parseFloat(box.paddingTop)+parseFloat(box.paddingBottom),font:parseFloat(style.fontSize),lineClamp:style.webkitLineClamp,ellipsis:style.textOverflow==='ellipsis',inside:title.left>=rect.left-1&&title.right<=rect.right+1&&title.bottom<=rect.bottom+1};}));
 check(label+' titres des cartes lisibles et complets',cards.every(card=>card.font>=15&&(!compact||card.font<=19)&&!card.ellipsis&&card.lineClamp==='none'&&card.inside),cards.filter(card=>card.font<15||(compact&&card.font>19)||card.ellipsis||card.lineClamp!=='none'||!card.inside));
 return cards;
}
async function compactHeading(page,label){
 const geometry=await page.locator('.mcg-block-heading').evaluate(node=>{const heading=node.querySelector('h2'),style=getComputedStyle(heading),rect=node.getBoundingClientRect(),title=heading.getBoundingClientRect(),box=getComputedStyle(node);return {height:rect.height,titleHeight:title.height,font:parseFloat(style.fontSize),padding:parseFloat(box.paddingTop)+parseFloat(box.paddingBottom),ellipsis:style.textOverflow==='ellipsis',lineClamp:style.webkitLineClamp,inside:title.left>=rect.left-1&&title.right<=rect.right+1&&title.bottom<=rect.bottom+1};});
 check(label+' en-tête compact sans perte de titre',geometry.font>=20&&(!compact||(geometry.font<=25&&geometry.padding<=36))&&!geometry.ellipsis&&geometry.lineClamp==='none'&&geometry.inside,geometry);return geometry;
}
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const origin='http://127.0.0.1:'+server.address().port,browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1050},reducedMotion:'reduce'}),page=await context.newPage(),before=baseline?await context.newPage():null;page.on('pageerror',error=>errors.push({url:page.url(),message:error.message}));if(before)before.on('pageerror',error=>errors.push({baseline:before.url(),message:error.message}));
  for(const fragment of registry){
   const file='fragments/MEDINA_'+fragment.id+'_'+fragment.slug+'.html',O=payload(path.join(directory,file)),url=origin+'/'+file,expected=new Map(O.blocks.map(block=>[block.code,expectations(O,block)]));
   for(const block of O.blocks){equal(fragment.id+' '+block.code+' données progress exactes depuis inventaire',block.progress,expected.get(block.code));categoriesChecked++;}
   await page.goto(url+'#/home');await ready(page);await page.locator('.mcg-home').waitFor();await noOverflow(page,fragment.id+' accueil bureau');await compactCards(page,fragment.id+' accueil bureau');
   for(const block of O.blocks){await verifyMetrics(page.locator('[data-mcg-category="'+block.code+'"]').locator('[data-mcg-category-progress="'+block.code+'"]'),fragment.id+' carte '+block.code,expected.get(block.code));}
   for(const filter of ['frequent','federal_exam']){
    await go(page,'#/home?filter='+filter);await page.locator('.mcg-filter-notice').waitFor();const shown=await page.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(node=>node.dataset.mcgCategory));
    for(const code of shown)await verifyMetrics(page.locator('[data-mcg-category="'+code+'"]').locator('[data-mcg-category-progress="'+code+'"]'),fragment.id+' carte '+filter+' '+code,expected.get(code));
    await verifyStars(page,O,fragment.id+' '+filter+' bureau');await noOverflow(page,fragment.id+' '+filter+' bureau');
   }
   for(const block of O.blocks){
    await go(page,'#/home?category='+encodeURIComponent(block.code));await page.locator('[data-mcg-block="'+block.code+'"]').waitFor();await verifyMetrics(page.locator('[data-mcg-block="'+block.code+'"] [data-mcg-category-progress="'+block.code+'"]'),fragment.id+' page '+block.code,expected.get(block.code));await compactHeading(page,fragment.id+' '+block.code+' bureau');await verifyStars(page,O,fragment.id+' '+block.code+' bureau');await noOverflow(page,fragment.id+' '+block.code+' bureau');
    await page.setViewportSize({width:390,height:844});await compactHeading(page,fragment.id+' '+block.code+' mobile');await verifyStars(page,O,fragment.id+' '+block.code+' mobile');await noOverflow(page,fragment.id+' '+block.code+' mobile');
    if(fragment.id==='T1'&&['A00-A09','A30-A49','B15-B19'].includes(block.code)){await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(captureOut,'categorie-'+block.code+'-mobile.png')});await page.setViewportSize({width:1440,height:1050});await page.screenshot({path:path.join(captureOut,'categorie-'+block.code+'-desktop.png')});}else await page.setViewportSize({width:1440,height:1050});
   }
   await go(page,'#/home');await page.setViewportSize({width:390,height:844});await compactCards(page,fragment.id+' accueil mobile');await noOverflow(page,fragment.id+' accueil mobile');await page.setViewportSize({width:1440,height:1050});
   if(before){
    const sample=O.blocks.flatMap(block=>block.lessons).find(lesson=>lesson.integrated&&lesson.source_fragment_id===fragment.id);
    if(sample){await before.goto(origin+'/__baseline__/'+file+'#/entry/'+sample.code);await ready(before);const oldCourse=await courseSnapshot(before,sample.code);await go(page,'#/entry/'+sample.code);equal(fragment.id+' '+sample.code+' cours, fenêtres, police et taille strictement inchangés',await courseSnapshot(page,sample.code),oldCourse);courseComparisons++;await verifyStars(page,O,fragment.id+' '+sample.code+' lecteur');}
    if(fragment.id==='T1'&&O.blocks.length){const block=O.blocks.find(item=>item.code==='A00-A09')||O.blocks[0];for(const [width,height,label]of [[1440,1050,'desktop'],[390,844,'mobile']]){await before.setViewportSize({width,height});await page.setViewportSize({width,height});await before.goto(origin+'/__baseline__/'+file+'#/home?category='+encodeURIComponent(block.code));await ready(before);await before.locator('[data-mcg-block="'+block.code+'"]').waitFor();await go(page,'#/home?category='+encodeURIComponent(block.code));const original=await before.locator('.mcg-block-heading').boundingBox(),current=await page.locator('.mcg-block-heading').boundingBox();if(compact)check('T1 '+label+' en-tête réellement réduit',current.height<original.height,{before:original.height,after:current.height});await before.screenshot({path:path.join(captureOut,'avant-categorie-'+label+'.png')});await page.screenshot({path:path.join(captureOut,'apres-categorie-'+label+'.png')});}await before.setViewportSize({width:1440,height:1050});await page.setViewportSize({width:1440,height:1050});}
   }
   if(fragment.id==='T1'){
    await go(page,'#/home?filter=frequent');await page.keyboard.press('Control+k');check('T1 raccourci Ctrl+K focalise la recherche',await page.locator('#global-search').evaluate(node=>document.activeElement===node));
    const command=page.locator('#command-btn');if(await command.isVisible()){modalOpenedBy='visible-button';await command.click();}else{modalOpenedBy='existing-runtime-helper';await page.evaluate(()=>showCommandPalette());}
    await page.locator('#modal[open]').waitFor();const body=page.locator('#modal-body'),selected=new Set(O.nosology.filters.frequent),wanted=O.blocks.filter(block=>block.lessons.some(lesson=>selected.has(lesson.code)));
    equal('T1 modale respecte les catégories du filtre',await body.locator('[data-mcg-category]').evaluateAll(nodes=>nodes.map(node=>node.dataset.mcgCategory)),wanted.map(block=>block.code));
    await compactCards(body,'T1 cartes de la modale');for(const block of wanted)await verifyMetrics(body.locator('[data-mcg-category="'+block.code+'"] [data-mcg-category-progress="'+block.code+'"]'),'T1 modale '+block.code,expected.get(block.code));
    const sizes=await body.evaluate(node=>({client:node.clientWidth,scroll:node.scrollWidth}));check('T1 modale sans débordement horizontal',sizes.scroll<=sizes.client+1,sizes);await page.screenshot({path:path.join(captureOut,'modale-categories-desktop.png')});await page.keyboard.press('Escape');await page.locator('#modal').waitFor({state:'hidden'});check('T1 Échap referme la modale',!(await page.locator('#modal').evaluate(node=>node.open)));
   }
   fragments.push({id:fragment.id,categories:O.blocks.length});fs.writeFileSync(path.join(out,'category-progress-progress.json'),JSON.stringify({fragments:fragments.length,categoriesChecked,checks:checks.length,last:fragment.id}));
  }
  check('aucune erreur JavaScript',errors.length===0,errors);const result={result:'passed',fragments:fragments.length,categoriesChecked,checks:checks.length,starChecks,courseComparisons,baseline:!!baseline,compact,subset:!!requestedIds,modalOpenedBy,browser:await browser.version(),errors};fs.writeFileSync(path.join(out,'category-progress-results.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close();server.close();}
})().catch(error=>{fs.writeFileSync(path.join(out,'category-progress-results.json'),JSON.stringify({result:'failed',fragments:fragments.length,categoriesChecked,checks:checks.length,starChecks,courseComparisons,errors,error:error.message},null,2)+'\n');console.error(error.message);server.close();process.exitCode=1;});
