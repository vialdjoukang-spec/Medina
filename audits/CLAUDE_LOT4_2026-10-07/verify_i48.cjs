const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {loadPlaywright,browserOptions}=require('../../tests/browser_runtime.cjs');
const {chromium}=loadPlaywright();
const file=path.resolve('dist/fragments/MEDINA_S01_cardiovasculaire.html');
const out=path.resolve('audits/CLAUDE_LOT4_2026-10-07');
const checks=[],errors=[],views=[];
function check(label,ok,detail){assert.ok(ok,label+' '+JSON.stringify(detail??''));checks.push(label);}
const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(file));});
async function reveal(page,key){
 const b=page.locator('.mc .mc-w[data-k="'+key+'"],.mc .mc-pareto-btn[data-k="'+key+'"]').first();
 const context=await b.evaluate(e=>({panel:e.closest('.mc-panel')?.id,science:e.closest('.mc-sci')?.id}));
 if(context.panel)await page.locator('.mc-tabs button[data-p="'+context.panel+'"]').click();
 if(context.science)await page.locator('.mc-sci-bar button[data-s="'+context.science+'"]').click();
 await b.scrollIntoViewIfNeeded();await b.waitFor({state:'visible'});return b;
}
async function body(page,key){
 const dlg=page.locator('.mc-dlg[open]');await dlg.waitFor({state:'visible'});
 const text=await dlg.locator('.mc-dlg-b').innerText();
 check(key+' : explication disponible',text.length>30&&!text.includes('Fiche absente.'));
 const box=await dlg.boundingBox();check(key+' : fenêtre dans la largeur',box.x>=-1&&box.x+box.width<=(await page.evaluate(()=>innerWidth))+1);
 return dlg;
}
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  for(const width of [1360,390]){
   const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'});
   const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
   page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
   await page.goto('http://127.0.0.1:'+server.address().port+'/#/entry/I48');
   await page.waitForFunction(()=>window.MDN_READY===true);await page.locator('.mc[data-code="I48"]').waitFor();
   const keys=[...new Set(await page.locator('.mc .mc-w[data-k],.mc .mc-pareto-btn[data-k]').evaluateAll(es=>es.map(e=>e.dataset.k)))];
   const expected=await page.locator('template[data-pop^="i48-"],template[data-pop^="pareto-i48-"]').evaluateAll(es=>es.map(e=>e.dataset.pop));
   const visited=new Set(),nested=new Set();
   async function walk(key,depth=0){
    visited.add(key);const dlg=await body(page,width+'px '+key);
    const expectedTitle=await page.locator('template[data-pop="'+key+'"]').getAttribute('data-title');
    check(key+' : bonne fenêtre clinique',(await dlg.locator('#mc-dlg-t').innerText()).replace(/\u00ad/g,'')===expectedTitle);
    if(depth>=8)return;
    const children=[...new Set(await dlg.locator('.mc-dlg-b [data-k]').evaluateAll(es=>es.map(e=>e.dataset.k)))];
    for(const child of children){
     if(visited.has(child))continue;
     const original=await dlg.locator('.mc-dlg-b').innerText();
     await dlg.locator('.mc-dlg-b [data-k="'+child+'"]').first().click();nested.add(child);
     await walk(child,depth+1);
     const back=page.locator('.mc-back:not([hidden])');check(child+' : retour imbriqué disponible',await back.isVisible());
     await back.click();check(child+' : contenu parent restauré',(await page.locator('.mc-dlg-b').innerText())===original);
    }
   }
   for(const key of keys){
    const trigger=await reveal(page,key);await trigger.click();await walk(key);
    await page.keyboard.press('Escape');await page.locator('.mc-dlg').waitFor({state:'hidden'});
    try{await page.waitForFunction(e=>document.activeElement===e,await trigger.elementHandle(),{timeout:3000});}
    catch(error){console.error(JSON.stringify({key,focus:await page.evaluate(()=>({active:document.activeElement?.outerHTML,trigger:MC_trigger?.outerHTML})),button:await trigger.evaluate(e=>e.outerHTML)}));throw error;}
    check(width+'px '+key+' : focus restitué',await trigger.evaluate(e=>document.activeElement===e));
   }
   check(width+'px : 101 fenêtres I48 compilées',expected.length===101,expected.length);
   check(width+'px : toutes les fenêtres I48 ouvertes',expected.every(k=>visited.has(k)),expected.filter(k=>!visited.has(k)));
   check(width+'px : comparaison ESC 2026 ouverte',visited.has('i48-esc-2026-comparaison'));
   check(width+'px : page sans débordement',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
   await page.evaluate(()=>scrollTo(0,0));await page.locator('.mc-size-toggle').click();
   await page.locator('.mc-size-range').evaluate(e=>{e.value=24;e.dispatchEvent(new Event('input',{bubbles:true}));});
   await page.keyboard.press('Escape');check(width+'px : police 24 px',await page.locator('.mc').evaluate(e=>e.style.getPropertyValue('--mc-fs'))==='24px');
   const comparator=await reveal(page,'i48-esc-2026-comparaison');await comparator.click();await body(page,width+'px comparaison à 24px');await page.keyboard.press('Escape');
   views.push({width,native_keys:keys.length,opened_keys:[...visited],nested_keys:[...nested],unopened_I48:expected.filter(k=>!visited.has(k))});
   await page.goto('http://127.0.0.1:'+server.address().port+'/#/entry/I50');await page.locator('.mc[data-code="I50"]').waitFor();
   const link=await reveal(page,'i50-esc-2026-comparaison');await link.click();const comparison=await body(page,width+'px I50 comparaison');
   const text=await comparison.innerText();check('I50 : les deux classifications sont comparables',text.includes('41–49')&&text.includes('50 %'));
   await page.keyboard.press('Escape');await context.close();
  }
  check('Aucune erreur JavaScript',errors.length===0,errors);
  fs.writeFileSync(path.join(out,'BROWSER.json'),JSON.stringify({result:'passed',checks,errors,views,input:{file,sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')}},null,2)+'\n');
  console.log(JSON.stringify({result:'passed',checks:checks.length,errors,views:views.map(v=>({width:v.width,native_keys:v.native_keys,opened:v.opened_keys.length,unopened_I48:v.unopened_I48}))}));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exit(1);});
