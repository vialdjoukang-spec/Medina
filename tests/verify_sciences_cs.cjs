/* Real-browser science reading, five fragment scopes, and 3D clinical skills. */
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const {loadPlaywright, browserOptions} = require('./browser_runtime.cjs');
const {chromium} = loadPlaywright();
const out = path.resolve(process.env.MEDINA_QA_OUT || 'audits/SCIENCES_CS_2026-10-07');
const manifest = JSON.parse(fs.readFileSync('fragments.json','utf8')).filter(f=>f.surface==='courses-v1');
const checks=[], errors=[], files={};
fs.mkdirSync(path.join(out,'captures'),{recursive:true});
const check=(name,ok,detail)=>{assert.ok(ok,name+(detail?': '+JSON.stringify(detail):''));checks.push(name)};
const pause=page=>page.waitForTimeout(100);
async function ready(page){await page.waitForFunction(()=>window.MDN_READY===true);await pause(page)}
async function route(page,hash){await page.evaluate(h=>location.hash=h,hash);await pause(page)}
async function overflow(page,name){const sizes=await page.evaluate(()=>({window:innerWidth,document:document.documentElement.scrollWidth}));check(name,sizes.document<=sizes.window+1,sizes)}
async function shot(page,name){await page.screenshot({path:path.join(out,'captures',name+'.jpg'),type:'jpeg',quality:85})}

(async()=>{
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  const context=await browser.newContext({viewport:{width:1360,height:900},reducedMotion:'reduce'});
  const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
  for(const fragment of manifest){
   const file=path.resolve('dist/fragments/MEDINA_'+fragment.id+'_'+fragment.slug+'.html');files[fragment.id]=file;
   await page.goto(pathToFileURL(file).href);await ready(page);
   const codes=fragment.categories.flatMap(g=>g.chapters);
   check(fragment.id+' : cours uniques de l’accueil',await page.locator('[data-s01-course]').count()===codes.length);
   check(fragment.id+' : catégories complètes',await page.locator('.s01-category').count()===fragment.categories.length);
   check(fragment.id+' : spécialité isolée',await page.evaluate(s=>JSON.stringify(DATA.specialties.map(x=>x.id))===JSON.stringify([s]),fragment.specialty));
   if(fragment.id!=='S01'){
    check(fragment.id+' : sémiologie cardiovasculaire absente',await page.locator('a[href="#/clinical-skills"]').count()===0);
    await route(page,'#/clinical-skills');check(fragment.id+' : route CS retourne à l’accueil',await page.locator('.s01-home').count()===1);
   }
   await overflow(page,fragment.id+' : accueil desktop');
   for(const code of codes){
    await route(page,'#/entry/'+code);await page.locator('.mc[data-code="'+code+'"]').waitFor();
    await page.locator('.mc-tabs button').filter({hasText:'Sciences'}).click();
    const tabs=page.locator('.mc-sci-bar [data-s]'),count=await tabs.count();
    check(code+' : disciplines accessibles',count>=3);
    for(let i=0;i<count;i++){
     await tabs.nth(i).click();
     const unit=page.locator('.mc-sci:not([hidden])');
     check(code+' : discipline '+(i+1)+' avec figure et liens',await unit.count()===1&&await unit.locator('figure svg[role="img"][aria-label]').count()>0&&(await unit.innerText()).replace(/\u00ad/g,'').includes('Science → traitement.'));
    }
    await tabs.first().click();
    const figure=page.locator('.mc-sci:not([hidden]) .mf-figure-open').first();
    await figure.click();const dialog=page.locator('.mf-figure-dialog[open]');
    check(code+' : fenêtre du schéma',await dialog.isVisible()&&await dialog.locator('figcaption').count()===1);
    const size=await dialog.locator('svg').evaluate(e=>e.getBoundingClientRect().width);
    await dialog.locator('input').evaluate(e=>{e.value='200';e.dispatchEvent(new Event('input',{bubbles:true}))});await pause(page);
    check(code+' : zoom réel du schéma',await dialog.locator('svg').evaluate(e=>e.getBoundingClientRect().width)>size);
    await page.keyboard.press('Escape');await pause(page);
    check(code+' : retour du focus après le schéma',await figure.evaluate(e=>document.activeElement===e));
    const link=page.locator('.mc-sci .mc-w[data-k]').first();
    if(await link.count()){
     const unitId=await link.evaluate(e=>e.closest('.mc-sci').id);
     await page.locator('.mc-sci-bar [data-s="'+unitId+'"]').click();
     await link.click();check(code+' : fenêtre scientifique écrite',(await page.locator('.mc-dlg[open] .mc-dlg-b').innerText()).replace(/\u00ad/g,'')!=='Fiche absente.');await page.locator('.mc-dlg .mc-x').click();
    }
    await page.setViewportSize({width:390,height:844});
    await page.locator('.mc-size-range').evaluate(e=>{e.value='24';e.dispatchEvent(new Event('input',{bubbles:true}))});
    for(let i=0;i<count;i++){await tabs.nth(i).click();await overflow(page,code+' : mobile 24 px, discipline '+(i+1))}
    await page.locator('.mc-size-range').evaluate(e=>{e.value='17';e.dispatchEvent(new Event('input',{bubbles:true}))});
    if(['I71','J44','D84','M06','A41'].includes(code))await shot(page,'sciences_'+code+'_mobile');
    if(code==='J44'){
     await tabs.first().click();await page.locator('.mf-figure-open').first().click();await overflow(page,'J44 : schéma en fenêtre sur mobile');await shot(page,'schema_mobile');await page.keyboard.press('Escape');
    }
    const quizzes=page.locator('#pS .mc-quiz');
    if(await quizzes.count()){
     const quiz=quizzes.first(),unitId=await quiz.evaluate(q=>q.closest('.mc-sci').id);
     await page.locator('.mc-sci-bar [data-s="'+unitId+'"]').click();await quiz.locator('[data-ok="1"]').first().click();
     check(code+' : cas scientifique corrigé',await quiz.locator('.mc-fb').isVisible());
    }
    await page.setViewportSize({width:1360,height:900});
   }
   await route(page,'#/home');await page.setViewportSize({width:390,height:844});await overflow(page,fragment.id+' : accueil mobile');
   if(fragment.id!=='S01')await shot(page,'accueil_'+fragment.id+'_mobile');
   await page.setViewportSize({width:1360,height:900});
  }
  await page.goto(pathToFileURL(files.S01).href+'#/clinical-skills');await ready(page);
  check('CS : dix étapes et sources',await page.locator('.cs-section').count()===11);
  await page.locator('[data-cs-jump="cs-auscultation"]').click();
  check('CS : plan et focus du titre',await page.evaluate(()=>document.activeElement.id==='cs-h-auscultation'));
  await shot(page,'cs_parcours_desktop');
  const models={thorax:7,neck:4,pulses:6,heart:8};
  for(const width of [1360,390]){
   await page.setViewportSize({width,height:width===390?844:900});
   for(const [id,count] of Object.entries(models)){
    const opener=page.locator('[data-cs-model="'+id+'"]').first();await opener.click();const dialog=page.locator('.cs-dialog[open]'),canvas=dialog.locator('canvas');
    await page.waitForFunction(()=>document.querySelector('.cs-dialog canvas')?.dataset.csYaw!==undefined);
    check('CS '+id+' '+width+' : scène et repères',await dialog.isVisible()&&await dialog.locator('[data-cs-select]').count()===count);
    await dialog.locator('[data-cs-select]').last().click();
    check('CS '+id+' '+width+' : explication sélectionnée',await dialog.locator('.cs-point-detail p').count()===2&&await dialog.locator('[aria-pressed="true"]').count()===1);
    await dialog.locator('[data-cs-view="front"]').click();await pause(page);
    await dialog.locator('[data-cs-rotate="right"]').click();await pause(page);
    check('CS '+id+' '+width+' : rotation effective',Number(await canvas.getAttribute('data-cs-yaw'))>0);
    await canvas.focus();await page.keyboard.press('ArrowUp');await pause(page);
    check('CS '+id+' '+width+' : clavier 3D',Number(await canvas.getAttribute('data-cs-pitch'))<0);
    await dialog.locator('input[type="range"]').evaluate(e=>{e.value='125';e.dispatchEvent(new Event('input',{bubbles:true}))});await pause(page);
    check('CS '+id+' '+width+' : zoom',await canvas.getAttribute('data-cs-zoom')==='1.25');
    await dialog.locator('[data-cs-reset]').click();await pause(page);
    check('CS '+id+' '+width+' : réinitialisation',await canvas.getAttribute('data-cs-zoom')==='1.00'&&await canvas.getAttribute('data-cs-yaw')==='0.000');
    if(id==='thorax'&&width===1360){
     const rect=await canvas.boundingBox();await page.mouse.move(rect.x+rect.width/2,rect.y+rect.height/2);await page.mouse.down();await page.mouse.move(rect.x+rect.width/2+55,rect.y+rect.height/2+12,{steps:5});await page.mouse.up();await pause(page);
     check('CS : rotation réelle par glissement',Number(await canvas.getAttribute('data-cs-yaw'))>.4);
     for(let i=0;i<25;i++){await page.keyboard.press('Tab');check('CS : focus contenu dans la fenêtre '+i,await dialog.evaluate(e=>e.contains(document.activeElement)))}
    }
    if(id==='pulses'){
     await dialog.locator('[data-cs-select="3"]').click();await pause(page);
     check('CS : pouls poplité en vue postérieure '+width,Math.abs(Number(await canvas.getAttribute('data-cs-yaw'))-Math.PI)<.01);
    }
    await overflow(page,'CS '+id+' '+width+' : fenêtre contenue');
    await shot(page,'cs_'+id+'_'+width);
    await page.keyboard.press('Escape');await pause(page);
    check('CS '+id+' '+width+' : fermeture et focus',await opener.evaluate(e=>document.activeElement===e)&&await page.locator('.cs-dialog[open]').count()===0);
   }
  }
  const checkbox=page.locator('[data-cs-check="preparation"]');await checkbox.check();
  await route(page,'#/home');await route(page,'#/clinical-skills');
  check('CS : entraînement conservé après navigation',await checkbox.isChecked());
  await page.locator('.cs-reset-checklist').click();check('CS : remise à zéro explicite',await page.locator('[data-cs-check]:checked').count()===0);
  const quizzes=page.locator('.cs-quiz');
  for(let i=0;i<await quizzes.count();i++){
   const quiz=quizzes.nth(i),answer=await quiz.getAttribute('data-cs-answer');
   await quiz.locator('[data-cs-choice]:not([data-cs-choice="'+answer+'"])').click();
   check('CS : correction de la réponse incorrecte '+i,await quiz.locator('.cs-feedback').getAttribute('data-cs-result')==='incorrect');
   await quiz.locator('[data-cs-choice="'+answer+'"]').click();
   check('CS : correction de la réponse correcte '+i,await quiz.locator('.cs-feedback').getAttribute('data-cs-result')==='correct');
  }
  await page.locator('[data-cs-model="thorax"]').first().click();
  await page.evaluate(()=>document.documentElement.classList.add('mdn-dark'));await shot(page,'cs_thorax_sombre');await overflow(page,'CS : fenêtre en thème sombre');
  await route(page,'#/entry/I21');check('CS : changement de route ferme la scène',await page.locator('.cs-dialog[open]').count()===0);
  const fallback=await context.newPage();fallback.on('pageerror',e=>errors.push(e.message));
  await fallback.addInitScript(()=>{HTMLCanvasElement.prototype.getContext=()=>null});
  await fallback.goto(pathToFileURL(files.S01).href+'#/clinical-skills');await ready(fallback);await fallback.locator('[data-cs-model="heart"]').first().click();
  check('CS : explications accessibles sans Canvas',await fallback.locator('.cs-canvas-fallback').isVisible());
  await fallback.locator('[data-cs-select="5"]').click();check('CS : valve mitrale accessible sans rendu',await fallback.locator('.cs-point-detail').getAttribute('data-cs-selected')==='mitral-valve');
  check('Aucune erreur JavaScript',errors.length===0,errors);
  fs.writeFileSync(path.join(out,'science-cs-browser-results.json'),JSON.stringify({browser:await browser.version(),files,checks,errors,result:'passed'},null,2)+'\n');
  console.log(JSON.stringify({result:'passed',checks:checks.length,errors},null,2));
 }catch(e){fs.writeFileSync(path.join(out,'science-cs-browser-results.json'),JSON.stringify({checks,errors,result:'failed',failure:e.message},null,2)+'\n');throw e}
 finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
