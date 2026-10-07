const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {loadPlaywright,browserOptions}=require('../../tests/browser_runtime.cjs');
const {chromium}=loadPlaywright();
const file=path.resolve('dist/fragments/MEDINA_S01_cardiovasculaire.html');
const codes=['I47','I71','I80','Q21'];
const checks=[],errors=[],views=[];
const progressFile=path.resolve('audits/CLAUDE_TEN_2026-10-07/lot5_four/BROWSER_PROGRESS.json');
const digest=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
if(fs.existsSync(progressFile)){const saved=JSON.parse(fs.readFileSync(progressFile));if(saved.sha256===digest){checks.push(...saved.checks);errors.push(...saved.errors);views.push(...saved.views);}}
const normal=s=>String(s).replace(/\u00ad/g,'').normalize('NFC').replace(/\s+/g,' ').trim();
function check(label,ok,detail){assert.ok(ok,label+' '+JSON.stringify(detail??''));checks.push(label);}
const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(file));});
async function reveal(page,key){
 const b=page.locator('.mc .mc-w[data-k="'+key+'"],.mc .mc-pareto-btn[data-k="'+key+'"]').first();
 const c=await b.evaluate(e=>({panel:e.closest('.mc-panel')?.id,science:e.closest('.mc-sci')?.id}));
 if(c.panel)await page.locator('.mc-tabs button[data-p="'+c.panel+'"]').click();
 if(c.science)await page.locator('.mc-sci-bar button[data-s="'+c.science+'"]').click();
 const inFeedback=await b.evaluate(e=>!!e.closest('.mc-fb[hidden]'));
 if(inFeedback){const quiz=b.locator('xpath=ancestor::*[contains(concat(" ",normalize-space(@class)," ")," mc-quiz ")]');await quiz.locator('.mc-opt[data-ok="1"]').first().click();}
 try{await b.scrollIntoViewIfNeeded({timeout:3000});}catch(error){console.error(JSON.stringify({key,context:c,trigger:await b.evaluate(e=>e.outerHTML)}));throw error;}return b;
}
async function body(page,label){
 const dlg=page.locator('.mc-dlg[open]');await dlg.waitFor({state:'visible'});
 const text=await dlg.locator('.mc-dlg-b').innerText();check(label+' : explication disponible',text.length>30&&!text.includes('Fiche absente.'));
 const box=await dlg.boundingBox();check(label+' : fenêtre dans la largeur',box.x>=-1&&box.x+box.width<=(await page.evaluate(()=>innerWidth))+1);
 return dlg;
}
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const browser=await chromium.launch(browserOptions(chromium));
 try{
  for(const width of [1360,390])for(const code of codes){
   if(views.some(v=>v.code===code&&v.width===width))continue;
   const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'}),page=await context.newPage();
   page.on('pageerror',e=>errors.push(code+' '+e.message));page.on('console',m=>{if(m.type()==='error')errors.push(code+' '+m.text());});
   await page.goto('http://127.0.0.1:'+server.address().port+'/#/entry/'+code);await page.waitForFunction(()=>window.MDN_READY===true);
   await page.locator('.mc[data-code="'+code+'"]').waitFor();
   const expected=await page.locator('template[data-pop^="'+code.toLowerCase()+'-"],template[data-pop^="pareto-'+code.toLowerCase()+'-"]').evaluateAll(es=>es.map(e=>e.dataset.pop));
   const keys=[...new Set(await page.locator('.mc .mc-w[data-k],.mc .mc-pareto-btn[data-k]').evaluateAll(es=>es.map(e=>e.dataset.k)))],visited=new Set();
   async function walk(key,depth=0){
    visited.add(key);const dlg=await body(page,code+' '+width+' '+key);
    const title=await page.locator('template[data-pop="'+key+'"]').getAttribute('data-title');
    check(key+' : fenêtre clinique correcte',normal(await dlg.locator('#mc-dlg-t').innerText())===normal(title));
    if(depth>=8)return;
    const children=[...new Set(await dlg.locator('.mc-dlg-b [data-k]').evaluateAll(es=>es.map(e=>e.dataset.k)))];
    for(const child of children){
     if(visited.has(child))continue;const text=await dlg.locator('.mc-dlg-b').innerText();
     await dlg.locator('.mc-dlg-b [data-k="'+child+'"]').first().click();await walk(child,depth+1);
     const back=page.locator('.mc-back:not([hidden])');check(child+' : retour disponible',await back.isVisible());await back.click();
     check(child+' : parent restitué',(await dlg.locator('.mc-dlg-b').innerText())===text);
    }
   }
   for(const key of keys){
    const trigger=await reveal(page,key);await trigger.click();await walk(key);await page.keyboard.press('Escape');
    await page.locator('.mc-dlg').waitFor({state:'hidden'});await page.waitForFunction(e=>document.activeElement===e,await trigger.elementHandle(),{timeout:3000});
    check(code+' '+width+' '+key+' : focus restitué',await trigger.evaluate(e=>document.activeElement===e));
   }
   check(code+' '+width+' : aucun débordement de page',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
   await page.evaluate(()=>scrollTo(0,0));await page.locator('.mc-size-toggle').click();
   await page.locator('.mc-size-range').evaluate(e=>{e.value=24;e.dispatchEvent(new Event('input',{bubbles:true}));});await page.keyboard.press('Escape');
   check(code+' '+width+' : police 24 px',await page.locator('.mc').evaluate(e=>e.style.getPropertyValue('--mc-fs'))==='24px');
   await page.locator('.mc-tabs button[data-p="pS"]').click();
   for(const tab of await page.locator('.mc-sci-bar button').all()){
    await tab.click();check(code+' '+width+' : sciences à 24 px sans débordement',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
   }
   views.push({code,width,trigger_keys:keys.length,expected_windows:expected.length,opened_keys:[...visited],unopened_windows:expected.filter(k=>!visited.has(k))});
   fs.writeFileSync(progressFile,JSON.stringify({sha256:digest,checks,errors,views},null,2)+'\n');
   console.log(JSON.stringify({progress:code,width,opened:visited.size,unopened:views.at(-1).unopened_windows,checks:checks.length}));
   await context.close();
  }
  check('Aucune erreur JavaScript',errors.length===0,errors);
  const report={result:'passed',checks,errors,views,input:{file,sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')}};
  fs.writeFileSync(path.resolve('audits/CLAUDE_TEN_2026-10-07/lot5_four/BROWSER.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({result:'passed',checks:checks.length,courses:codes.length,views:views.length,errors}));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1});
