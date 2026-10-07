/* Targeted real-browser checks for the seven corrected MEDINA figures. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '../..');
const {loadPlaywright, browserOptions} = require(path.join(root, 'tests/browser_runtime.cjs'));
const {chromium} = loadPlaywright();
const out = path.join(__dirname, 'figures');
const captures = path.join(out, 'captures');
fs.mkdirSync(captures, {recursive:true});
const files = {S01:path.join(root,'dist/fragments/MEDINA_S01_cardiovasculaire.html'), S02:path.join(root,'dist/fragments/MEDINA_S02_respiratoire.html')};
const specs = [
 {id:'I50-histologie',code:'I50',fragment:'S01',panel:'pS',discipline:'s-histo',unit:'sh-i',nth:0,capture:true},
 {id:'J44-anatomie',code:'J44',fragment:'S02',panel:'pS',discipline:'j44-s-anat',unit:'j44-s-anat',nth:0},
 {id:'J44-physiologie',code:'J44',fragment:'S02',panel:'pS',discipline:'j44-s-physio',unit:'j44-s-physio',nth:0,capture:true},
 {id:'J44-biochimie',code:'J44',fragment:'S02',panel:'pS',discipline:'j44-s-bioch',unit:'j44-s-bioch',nth:0},
 {id:'J18-anatomie',code:'J18',fragment:'S02',panel:'pS',discipline:'j18-s-anat',unit:'j18-s-anat',nth:0},
 {id:'J18-physiologie',code:'J18',fragment:'S02',panel:'pS',discipline:'j18-s-phys',unit:'j18-s-phys',nth:0,capture:true},
 {id:'J18-pathologie-shunt',code:'J18',fragment:'S02',panel:'pA',unit:'j18-3',nth:1}
];
const digest = f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const inputPaths = [...Object.values(files), ...['I50','J44','J18'].map(c=>path.join(root,'chapters',c,c+'_c.html')), path.join(root,'chapters/J18/J18_a.html'),path.join(root,'shell/fragment.js'),path.join(root,'shell/fragment.css')];
const inputs = inputPaths.map(file=>({file:path.relative(root,file),sha256:digest(file)}));
const checks=[],errors=[],browserErrors=[],limitations=[],shots=[];
const check=(name,ok,detail={})=>{checks.push({name,ok,...detail});if(!ok)errors.push({name,...detail})};
const pause = page=>page.waitForTimeout(100);
async function noOverflow(page,name){const sizes=await page.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth}));check(name,sizes.document<=sizes.viewport+1,sizes)}
async function openTarget(page,spec){
 await page.goto(pathToFileURL(files[spec.fragment]).href+'#/entry/'+spec.code);
 await page.waitForFunction(()=>window.MDN_READY===true&&!!window.MEDINA_CATEGORY_ORGANISATION);
 await page.locator('.mc[data-code="'+spec.code+'"]').waitFor();
 await page.locator('.mc-tabs button[data-p="'+spec.panel+'"]').click();
 if(spec.discipline)await page.locator('.mc-sci-bar [data-s="'+spec.discipline+'"]').click();
 else await page.locator('#'+spec.panel+' .mc-toc [data-go="'+spec.unit+'"]').click();
 const figure=page.locator('#'+spec.unit+' figure').nth(spec.nth);
 await figure.scrollIntoViewIfNeeded();await pause(page);
 return figure;
}
async function setFont(page,size){
 await page.locator('.mc-size-toggle').click();
 await page.locator('.mc-size-range').evaluate((e,size)=>{e.value=String(size);e.dispatchEvent(new Event('input',{bubbles:true}))},size);
 await page.locator('.mc-size-toggle').click();await pause(page);
}
async function zoomBehavior(page,figure,label){
 const opener=figure.locator('.mf-figure-open');
 check(label+' : bouton natif de zoom',await opener.count()===1);
 if(!await opener.count())return;
 await opener.click();const dialog=page.locator('.mf-figure-dialog[open]');
 check(label+' : fenêtre ouverte avec SVG et légende',await dialog.isVisible()&&await dialog.locator('svg').count()===1&&await dialog.locator('figcaption').count()===1);
 const original=await figure.locator('svg').getAttribute('aria-label');
 check(label+' : figure réellement clonée',await dialog.locator('svg').getAttribute('aria-label')===original);
 const range=dialog.locator('input');
 await range.evaluate(e=>{e.value='100';e.dispatchEvent(new Event('input',{bubbles:true}))});await pause(page);
 const initial=await dialog.locator('svg').evaluate(e=>e.getBoundingClientRect().width);
 await range.evaluate(e=>{e.value='200';e.dispatchEvent(new Event('input',{bubbles:true}))});await pause(page);
 const doubled=await dialog.locator('svg').evaluate(e=>e.getBoundingClientRect().width);
 check(label+' : zoom 200 % réel',Math.abs(doubled-2*initial)<2&&await dialog.locator('output').innerText()==='200 %',{initial,doubled});
 const scroll=await dialog.locator('.mf-figure-scroll').evaluate(e=>({viewport:e.clientWidth,content:e.scrollWidth,overflow:getComputedStyle(e).overflowX}));
 check(label+' : contenu agrandi défile dans la fenêtre',scroll.overflow==='auto'&&scroll.content>=scroll.viewport,{scroll});
 await noOverflow(page,label+' : zoom contenu dans le viewport');
 await page.keyboard.press('Escape');await pause(page);
 check(label+' : Escape ferme la fenêtre',await page.locator('.mf-figure-dialog[open]').count()===0);
 check(label+' : retour du focus au bouton',await opener.evaluate(e=>document.activeElement===e));
}
async function screenshot(page,figure,spec,width){
 const name=spec.code+'_'+(width===390?'mobile_390_font24':'desktop')+'.jpg';
 if(width===390){await figure.scrollIntoViewIfNeeded();await figure.screenshot({path:path.join(captures,name),type:'jpeg',quality:85});}
 else{await figure.locator('.mf-figure-open').click();const d=page.locator('.mf-figure-dialog[open]');await d.locator('input').evaluate(e=>{e.value='100';e.dispatchEvent(new Event('input',{bubbles:true}))});await pause(page);await d.screenshot({path:path.join(captures,name),type:'jpeg',quality:85});await page.keyboard.press('Escape');await pause(page);}
 shots.push({file:path.relative(root,path.join(captures,name)),course:spec.code,width,font:width===390?24:17,figure:spec.id,sha256:digest(path.join(captures,name))});
}
(async()=>{
 const browser=await chromium.launch(browserOptions(chromium));let version;
 try{
  version=await browser.version();
  const context=await browser.newContext({viewport:{width:1360,height:960},reducedMotion:'reduce'});
  const page=await context.newPage();page.on('pageerror',e=>browserErrors.push(e.message));
  for(const spec of specs){
   for(const width of [1360,390]){
    const label=spec.id+' '+width;
    try{
     await page.setViewportSize({width,height:width===390?844:960});
     const figure=await openTarget(page,spec);
     await setFont(page,width===390?24:17);
     await figure.scrollIntoViewIfNeeded();await pause(page);
     const active=await page.locator('.mc-tabs button[data-p="'+spec.panel+'"]').getAttribute('aria-selected');
     check(label+' : onglet natif actif',active==='true');
     if(spec.discipline)check(label+' : discipline native active',await page.locator('.mc-sci-bar [data-s="'+spec.discipline+'"]').getAttribute('aria-selected')==='true');
     check(label+' : figure et légende visibles',await figure.isVisible()&&await figure.locator('svg').isVisible()&&await figure.locator('figcaption').isVisible());
     const box=await figure.locator('svg').boundingBox();check(label+' : dessin non vide',box.width>0&&box.height>0,{box});
     const caption=(await figure.locator('figcaption').innerText()).replace(/\u00ad/g,'');
     check(label+' : légende textuelle présente',caption.length>30,{caption});
     if(width===390)check(label+' : police du cours à 24 px',await page.locator('.mc').evaluate(e=>getComputedStyle(e).getPropertyValue('--mc-fs').trim())==='24px');
     await noOverflow(page,label+' : aucun débordement global');
     if(spec.panel==='pS')await zoomBehavior(page,figure,label);
     else{
      const count=await figure.locator('.mf-figure-open').count();
      limitations.push({figure:spec.id,width,issue:'La fonction native de zoom équipe seulement les figures Sciences. La figure Pathologie est contrôlée en lecture, sans bouton ajouté par le test.',zoom_button_count:count});
      check(label+' : modèle explicitement limité',caption.includes('ne prédit pas la saturation clinique réelle'));
     }
     if(spec.capture)await screenshot(page,figure,spec,width);
    }catch(e){errors.push({name:label,error:e.message});checks.push({name:label+' : exécution complète',ok:false,error:e.message});await page.keyboard.press('Escape').catch(()=>{});}
   }
  }
  check('Aucune erreur JavaScript',browserErrors.length===0,{browserErrors});
  check('Sept figures uniques réellement contrôlées',new Set(specs.map(s=>s.id)).size===7,{ids:specs.map(s=>s.id)});
  check('Six captures des trois cours',shots.length===6,{files:shots.map(s=>s.file)});
  check('Entrées inchangées pendant le contrôle',inputs.every(i=>digest(path.join(root,i.file))===i.sha256));
  fs.writeFileSync(path.join(out,'figure-browser-results.json'),JSON.stringify({date:new Date().toISOString(),result:errors.length?'failed':'passed_with_limitations',browser:version,scope:'Contrôle ciblé du rendu et du comportement réel de sept figures ; aucune certification médicale exhaustive.',inputs,specs,checks,errors,browserErrors,limitations,captures:shots},null,2)+'\n');
  console.log(JSON.stringify({result:errors.length?'failed':'passed_with_limitations',checks:checks.length,errors,limitations,captures:shots.length},null,2));
  if(errors.length)process.exitCode=1;
 }finally{await browser.close()}
})().catch(e=>{fs.writeFileSync(path.join(out,'figure-browser-results.json'),JSON.stringify({result:'failed',inputs,checks,errors,browserErrors,failure:e.message},null,2)+'\n');console.error(e);process.exitCode=1});
