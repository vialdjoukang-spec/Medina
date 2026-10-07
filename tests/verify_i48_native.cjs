/* Independent read-only QA for native I48 windows in the built S01 artifact. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname,'..');
const {loadPlaywright, browserOptions} = require('./browser_runtime.cjs');
const {chromium} = loadPlaywright();
const file = path.resolve(process.env.MEDINA_I48_NATIVE_FILE || path.join(root,'dist/fragments/MEDINA_S01_cardiovasculaire.html'));
const out = path.resolve(process.env.MEDINA_QA_OUT || path.join(root,'audits/INTEGRATION_I48_LOT4_2026-10-07/native_browser'));
const report = {
  course:'I48 — Fibrillation et flutter auriculaires', artifact:file,
  started_at:new Date().toISOString(), checks:[], failures:[], page_errors:[], console_errors:[],
  windows:[], occurrences:[], nested_edges:[], widths:[], captures:[], interaction_caveats:[], activation_modes:{pointer:0,keyboard:0}, result:'running'
};
const norm = s => String(s||'').replace(/[\u00ad]/g,'').replace(/\s+/g,' ').trim();
function check(name, ok, details) {
  report.checks.push({name,ok:!!ok,...(details===undefined?{}:{details})});
  if (!ok) report.failures.push({name,details});
}
function writeReport() { fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'results.json'),JSON.stringify(report,null,2)+'\n'); }
async function unit(name,fn) {
  try { await fn(); }
  catch(error) {check(name,false,error.message);}
}

(async()=>{
  if (!fs.existsSync(file)) throw new Error('Construction S01 absente : '+file);
  report.artifact_sha256=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
  report.source_sha256=Object.fromEntries([
    ...fs.readdirSync(path.join(root,'chapters/I48')).filter(n=>n.endsWith('.html')).sort().map(n=>'chapters/I48/'+n),
    'glossary/i48.py','engine/medina_course.js','engine/medina_course.css'
  ].map(relative=>[relative,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,relative))).digest('hex')]));
  fs.mkdirSync(out,{recursive:true});
  const browser=await chromium.launch(browserOptions(chromium));
  report.browser=await browser.version();
  try {
    const context=await browser.newContext({viewport:{width:1360,height:900},reducedMotion:'reduce'});
    const page=await context.newPage();page.setDefaultTimeout(8000);
    page.on('pageerror',e=>report.page_errors.push(e.message));
    page.on('console',m=>{if(m.type()==='error')report.console_errors.push(m.text())});
    await page.goto(pathToFileURL(file).href+'#/entry/I48');
    await page.waitForFunction(()=>window.MDN_READY===true);
    await page.locator('.mc[data-code="I48"]').waitFor();
    await page.waitForTimeout(200);
    check('Cours I48 ouvert',await page.locator('.mc[data-code="I48"]').count()===1);
    const mainSelector='.mc .mc-w[data-k], .mc .mc-pareto-btn[data-k]';
    const metadata=await page.evaluate((selector)=>{
      const normalize=s=>String(s||'').replace(/[\u00ad]/g,'').replace(/\s+/g,' ').trim();
      const mc=document.querySelector('.mc');
      const quizzes=[...mc.querySelectorAll('.mc-quiz')];
      const occurrences=[...document.querySelectorAll(selector)].map((e,index)=>({
        index,key:e.dataset.k,text:normalize(e.textContent),panel:e.closest('.mc-panel')?.id,
        science:e.closest('.mc-sci')?.id||null,quiz:quizzes.indexOf(e.closest('.mc-quiz')),
        pareto:e.classList.contains('mc-pareto-btn')
      }));
      const allTemplates=[...document.querySelectorAll('template[data-pop]')];
      const keys=new Set(occurrences.map(e=>e.key));
      allTemplates.filter(t=>/^(?:i48-|pareto-i48-)/.test(t.dataset.pop)).forEach(t=>keys.add(t.dataset.pop));
      const queue=[...keys];
      for(let i=0;i<queue.length;i++){
        const template=allTemplates.find(t=>t.dataset.pop===queue[i]);
        if(template)for(const link of template.content.querySelectorAll('[data-k]')){
          if(!keys.has(link.dataset.k)){keys.add(link.dataset.k);queue.push(link.dataset.k)}
        }
      }
      const templates=queue.map(key=>{
        const matches=allTemplates.filter(t=>t.dataset.pop===key),t=matches[0];
        return {key,count:matches.length,title:t?.dataset.title||'',text:t?normalize(t.content.textContent):'',
          links:t?[...t.content.querySelectorAll('[data-k]')].map((e,index)=>({index,key:e.dataset.k,text:normalize(e.textContent)})):[]};
      });
      return {occurrences,templates,tabs:[...mc.querySelectorAll('.mc-tabs [data-p]')].map(e=>({panel:e.dataset.p,text:normalize(e.textContent)})),
        sciences:[...mc.querySelectorAll('.mc-sci-bar [data-s]')].map(e=>({id:e.dataset.s,text:normalize(e.textContent)}))};
    },mainSelector);
    report.occurrences=metadata.occurrences;
    report.windows=metadata.templates.map(t=>({key:t.key,title:t.title,definitions:t.count,words:t.text.split(' ').length,links:t.links.length}));
    const templates=new Map(metadata.templates.map(t=>[t.key,t]));
    const reachable=new Map();
    for(const t of metadata.templates) {
      check('Définition unique '+t.key,t.count===1,{count:t.count});
      check('Fenêtre écrite '+t.key,t.text.length>30,{characters:t.text.length});
    }
    check('Quatre onglets natifs',JSON.stringify(metadata.tabs.map(t=>t.panel))==='["pA","pE","pS","pP"]',metadata.tabs);
    check('Occurrence de mots verts natifs',metadata.occurrences.filter(e=>!e.pareto).length>0);
    check('Occurrence des synthèses Pareto',metadata.occurrences.filter(e=>e.pareto).length>0);

    async function layout(name,modal=false) {
      const sizes=await page.evaluate((modal)=>{
        const d=document.querySelector('dialog.mc-dlg'),b=d?.querySelector('.mc-dlg-b'),r=d?.getBoundingClientRect();
        return {width:innerWidth,document:document.documentElement.scrollWidth,...(modal?{dialog:{x:r.x,right:r.right,width:r.width},body:{clientWidth:b.clientWidth,scrollWidth:b.scrollWidth}}:{})};
      },modal);
      check(name+' : largeur du document',sizes.document<=sizes.width+1,sizes);
      if(modal){
        check(name+' : fenêtre dans le viewport',sizes.dialog.x>=-1&&sizes.dialog.right<=sizes.width+1,sizes);
        check(name+' : corps sans débordement horizontal',sizes.body.scrollWidth<=sizes.body.clientWidth+1,sizes);
      }
      report.widths.push({name,...sizes});
    }
    async function shot(name){const target=path.join(out,name+'.png');await page.screenshot({path:target});report.captures.push(target);}
    async function close(mode='button') {
      if(!await page.locator('dialog.mc-dlg[open]').count())return;
      if(mode==='escape')await page.keyboard.press('Escape');
      else await page.locator('dialog.mc-dlg .mc-x').click();
      // Native dialog close queues its close event; focus restoration happens there.
      await page.waitForFunction(()=>!document.querySelector('dialog.mc-dlg').open&&MC_stack.length===0);
    }
    async function activateNative(element) {
      // Click the natural element centre. Never route around nested abbreviations.
      await element.click();report.activation_modes.pointer++;
    }
    async function expose(descriptor) {
      await close();
      await page.locator('.mc-tabs [data-p="'+descriptor.panel+'"]').click();
      if(descriptor.science)await page.locator('.mc-sci-bar [data-s="'+descriptor.science+'"]').click();
      if(descriptor.quiz>=0){
        const quiz=page.locator('.mc .mc-quiz').nth(descriptor.quiz);
        await quiz.locator('.mc-opt[data-ok="1"]').first().click();
      }
      return page.locator(mainSelector).nth(descriptor.index);
    }
    async function verifyWindow(key,label) {
      const expected=templates.get(key);
      const state=await page.evaluate(()=>({open:document.querySelector('dialog.mc-dlg').open,
        title:document.querySelector('#mc-dlg-t').textContent,body:document.querySelector('.mc-dlg-b').textContent,
        depth:MC_stack.length,backHidden:document.querySelector('.mc-back').hidden}));
      check(label+' : ouverture',state.open);
      check(label+' : titre conforme',!!expected&&norm(state.title)===expected.title,{expected:expected?.title,actual:norm(state.title)});
      check(label+' : contenu natif conforme',!!expected&&norm(state.body)===expected.text,{expectedCharacters:expected?.text.length,actualCharacters:norm(state.body).length});
      check(label+' : aucune fiche absente',!norm(state.body).includes('Fiche absente'));
      return state;
    }
    async function openPath(item) {
      const descriptor=metadata.occurrences[item.main];
      const element=await expose(descriptor);await activateNative(element);
      for(const step of item.steps)await activateNative(page.locator('.mc-dlg-b [data-k]').nth(step.index));
    }
    async function back(parentKey,label) {
      check(label+' : retour disponible',await page.locator('.mc-back').isVisible());
      await page.locator('.mc-back').click();
      await verifyWindow(parentKey,label+' : retour');
    }

    for(const tab of metadata.tabs){
      await page.locator('.mc-tabs [data-p="'+tab.panel+'"]').click();
      check('Onglet '+tab.panel+' : panneau actif',await page.locator('#'+tab.panel).isVisible());
      check('Onglet '+tab.panel+' : sélection unique',await page.locator('.mc-tabs [aria-selected="true"]').count()===1);
      await layout('Desktop '+tab.panel);
    }
    await page.locator('.mc-tabs [data-p="pS"]').click();
    for(const science of metadata.sciences){
      await page.locator('.mc-sci-bar [data-s="'+science.id+'"]').click();
      check('Discipline '+science.id+' : panneau actif',await page.locator('#'+science.id).isVisible());
      await layout('Desktop '+science.id);
    }

    for(const descriptor of metadata.occurrences) {
      await unit('Mot natif '+descriptor.index+' '+descriptor.key,async()=>{
        const element=await expose(descriptor);await activateNative(element);
        const state=await verifyWindow(descriptor.key,'Mot natif '+descriptor.index+' '+descriptor.key);
        check('Mot natif '+descriptor.index+' : pile initiale',state.depth===1&&state.backHidden);
        if(!reachable.has(descriptor.key))reachable.set(descriptor.key,{main:descriptor.index,steps:[]});
        if(descriptor.pareto)await layout('Desktop Pareto '+descriptor.key,true);
        await close(descriptor.index%2===0?'button':'escape');
        check('Mot natif '+descriptor.index+' : fermeture',!await page.locator('dialog.mc-dlg[open]').count());
        check('Mot natif '+descriptor.index+' : focus rendu',await element.evaluate(e=>document.activeElement===e));
      });
      if(descriptor.index%50===0)console.log('Native I48 : '+descriptor.index+'/'+metadata.occurrences.length+' occurrences');
    }

    const nestedAbKeys=new Set();
    for(const descriptor of metadata.occurrences){
      if(nestedAbKeys.has(descriptor.key))continue;
      const element=await expose(descriptor),child=element.locator('.mc-ab').first();
      if(!await child.count())continue;
      nestedAbKeys.add(descriptor.key);
      await unit('Priorité du mot vert '+descriptor.key,async()=>{
        await child.click();await verifyWindow(descriptor.key,'Clic sur abréviation imbriquée '+descriptor.key);
        await close();
        const colors=await element.evaluate(e=>({outer:getComputedStyle(e).color,inner:getComputedStyle(e.querySelector('.mc-ab')).color}));
        check('Couleur verte homogène '+descriptor.key,colors.outer===colors.inner,colors);
        if(await child.getAttribute('tabindex')==='0')await child.focus();else await element.focus();
        await page.keyboard.press('Enter');report.activation_modes.keyboard++;
        await verifyWindow(descriptor.key,'Enter sur mot vert imbriqué '+descriptor.key);await close();
        if(await child.getAttribute('tabindex')==='0')await child.focus();else await element.focus();
        await page.keyboard.press('Space');report.activation_modes.keyboard++;
        await verifyWindow(descriptor.key,'Espace sur mot vert imbriqué '+descriptor.key);await close();
      });
    }
    report.nested_abbreviation_parent_keys=[...nestedAbKeys].sort();
    await page.locator('.mc-tabs [data-p="pA"]').click();
    const standalone=await page.locator('.mc .mc-ab').evaluateAll(es=>es.findIndex(e=>!e.closest('.mc-w')&&[...e.getClientRects()].some(r=>r.width>0&&r.height>0)));
    if(standalone>=0)await unit('Abréviation autonome',async()=>{
      const abbreviation=page.locator('.mc .mc-ab').nth(standalone),key=await abbreviation.getAttribute('data-ab');
      await abbreviation.click();
      check('Abréviation autonome : définition distincte',norm(await page.locator('#mc-dlg-t').innerText()).startsWith(key+' — '));
      await close();
      check('Abréviation autonome : focus rendu',await abbreviation.evaluate(e=>document.activeElement===e));
    });

    const queue=[...reachable.keys()];
    for(let q=0;q<queue.length;q++){
      const parentKey=queue[q],parentPath=reachable.get(parentKey),template=templates.get(parentKey);
      if(!template)continue;
      await unit('Fenêtre '+parentKey,async()=>{
        await openPath(parentPath);await verifyWindow(parentKey,'Fenêtre '+parentKey);
        const count=await page.locator('.mc-dlg-b [data-k]').count();
        check('Fenêtre '+parentKey+' : renvois présents',count===template.links.length,{expected:template.links.length,actual:count});
        for(const edge of template.links){
          await unit('Renvoi '+parentKey+' → '+edge.key+' #'+edge.index,async()=>{
            await activateNative(page.locator('.mc-dlg-b [data-k]').nth(edge.index));
            const state=await verifyWindow(edge.key,'Renvoi '+parentKey+' → '+edge.key+' #'+edge.index);
            check('Renvoi '+parentKey+' #'+edge.index+' : pile et retour',state.depth===parentPath.steps.length+2&&!state.backHidden);
            report.nested_edges.push({from:parentKey,to:edge.key,index:edge.index,desktop:true});
            if(!reachable.has(edge.key)){
              reachable.set(edge.key,{main:parentPath.main,steps:[...parentPath.steps,{index:edge.index,key:edge.key}]});queue.push(edge.key);
            }
            await back(parentKey,'Renvoi '+parentKey+' #'+edge.index);
          });
        }
        await close();
      });
    }
    report.reachable_window_keys=[...reachable.keys()].sort();
    const registeredI48=metadata.templates.filter(t=>/^(?:i48-|pareto-i48-)/.test(t.key));
    report.unreachable_i48_windows=registeredI48.filter(t=>!reachable.has(t.key)).map(t=>t.key);
    check('Toutes les fenêtres I48 accessibles par mots natifs',report.unreachable_i48_windows.length===0,report.unreachable_i48_windows);

    await page.setViewportSize({width:390,height:844});
    for(const font of [17,24]){
      await page.locator('.mc-size-range').evaluate((e,size)=>{e.value=String(size);e.dispatchEvent(new Event('input',{bubbles:true}))},font);
      for(const tab of metadata.tabs){
        await page.locator('.mc-tabs [data-p="'+tab.panel+'"]').click();
        await layout('Mobile 390 px '+font+' px '+tab.panel);
        if(font===17){await page.evaluate(()=>scrollTo(0,0));await shot('mobile_'+tab.panel);}
      }
      await page.locator('.mc-tabs [data-p="pS"]').click();
      for(const science of metadata.sciences){
        await page.locator('.mc-sci-bar [data-s="'+science.id+'"]').click();
        await layout('Mobile 390 px '+font+' px '+science.id);
      }
    }
    await page.locator('.mc-size-range').evaluate(e=>{e.value='17';e.dispatchEvent(new Event('input',{bubbles:true}))});
    for(const key of reachable.keys()) {
      await unit('Mobile fenêtre '+key,async()=>{
        await openPath(reachable.get(key));await verifyWindow(key,'Mobile fenêtre '+key);
        await layout('Mobile fenêtre '+key,true);
        if(['i48-noeudav','i48-infraclin','pareto-i48-exam'].includes(key))await shot('mobile_fenetre_'+key);
        const template=templates.get(key);
        for(const edge of template.links){
          await activateNative(page.locator('.mc-dlg-b [data-k]').nth(edge.index));
          await verifyWindow(edge.key,'Mobile renvoi '+key+' → '+edge.key+' #'+edge.index);
          await back(key,'Mobile renvoi '+key+' #'+edge.index);
        }
        await close();
      });
    }
    await close();
    check('Aucune erreur JavaScript',report.page_errors.length===0,report.page_errors);
    check('Aucune erreur console',report.console_errors.length===0,report.console_errors);
    check('Artifact stable durant QA',report.artifact_sha256===crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'));
    for(const [relative,hash] of Object.entries(report.source_sha256))check('Source stable durant QA '+relative,hash===crypto.createHash('sha256').update(fs.readFileSync(path.join(root,relative))).digest('hex'));
    report.result=report.failures.length?'failed':'passed';
    report.finished_at=new Date().toISOString();
    writeReport();
    console.log(JSON.stringify({result:report.result,checks:report.checks.length,occurrences:report.occurrences.length,windows:reachable.size,nestedEdges:report.nested_edges.length,activation_modes:report.activation_modes,interaction_caveats:report.interaction_caveats,failures:report.failures.slice(0,8),failure_count:report.failures.length,report:path.join(out,'results.json')},null,2));
    if(report.failures.length)process.exitCode=1;
  }finally{await browser.close();}
})().catch(error=>{report.result='failed';report.failures.push({name:'Fatal',details:error.stack});report.finished_at=new Date().toISOString();writeReport();console.error(error.stack);process.exitCode=1;});
