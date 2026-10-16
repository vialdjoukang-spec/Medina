/* Real Chromium checks of the per-view category numbering (global, frequent, federal_exam).
 * Usage: MEDINA_FRAGMENTS=<dir with MEDINA_<ID>_<slug>.html> MEDINA_RENUMBER_FRAGMENT_IDS=S08,S02 \
 *        MEDINA_QA_OUT=<captures dir> node tests/verify_category_renumbering.cjs
 */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright(),root=path.resolve(__dirname,'..');
const directory=path.resolve(process.env.MEDINA_FRAGMENTS||path.join(root,'dist/fragments'));
const out=path.resolve(process.env.MEDINA_QA_OUT||path.join(root,'work/renumerotation'));
const ids=(process.env.MEDINA_RENUMBER_FRAGMENT_IDS||'S08').split(',').filter(Boolean);
const registry=JSON.parse(fs.readFileSync(path.join(root,'fragments.json'),'utf8'));
const checks=[],errors=[],requests=[],captures=[];fs.mkdirSync(out,{recursive:true});
const check=(name,ok,detail)=>{assert.ok(ok,name+(detail===undefined?'':' : '+JSON.stringify(detail)));checks.push(name)};
const equal=(name,value,expected)=>check(name,JSON.stringify(value)===JSON.stringify(expected),{value,expected});
const VIEWS=['','frequent','federal_exam'],LABEL={'':'global',frequent:'frequent',federal_exam:'federal_exam'};
const NOTE={'':null,frequent:'Ordre : leçons fréquentes d’abord, puis ordre global',federal_exam:'Ordre : leçons fédérales d’abord, puis ordre global'};
// Independent oracle of the specification, computed from the embedded data only.
function expectedView(O,view){
 if(!view)return O.blocks.map(b=>({code:b.code,weight:null,global:b.order}));
 const selected=new Set(O.nosology.filters[view]);
 return O.blocks.map(b=>({code:b.code,global:b.order,weight:new Set(b.lessons.filter(l=>selected.has(l.code)).map(l=>l.code)).size}))
  .filter(b=>b.weight).sort((a,b)=>b.weight-a.weight||a.global-b.global);
}
const hashFor=(view,extra='')=>'#/home'+(view||extra?'?':'')+[extra,view?'filter='+view:''].filter(Boolean).join('&');
async function go(page,hash){await page.evaluate(value=>{location.hash=value},hash);await page.waitForFunction(value=>location.hash===value&&document.querySelector('.mcg-home'),hash);}
async function snapshot(page){return page.evaluate(()=>({
 cards:[...document.querySelectorAll('#content [data-mcg-category]')].map(c=>({code:c.dataset.mcgCategory,rank:c.dataset.mcgRank,number:c.querySelector('.mcg-category-number').textContent,aria:c.getAttribute('aria-label'),weight:c.querySelector('[data-mcg-view-weight]')?.dataset.mcgViewWeight??null})),
 side:[...document.querySelectorAll('#spec-nav [data-mcg-sidebar-category]')].map(s=>({code:s.dataset.mcgSidebarCategory,rank:s.dataset.mcgRank,number:s.querySelector('summary [data-mcg-rank-value]').textContent})),
 note:document.querySelector('#content .mcg-order-note')?{view:document.querySelector('#content .mcg-order-note').dataset.mcgOrderView,text:document.querySelector('#content .mcg-order-note').textContent}:null}));}
(async()=>{
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  for(const id of ids){
   const fragment=registry.find(f=>f.id===id);assert.ok(fragment,'fragment inconnu '+id);
   const file=path.join(directory,`MEDINA_${fragment.id}_${fragment.slug}.html`),source=fs.readFileSync(file,'utf8');
   const O=JSON.parse(source.match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
   check(id+' : ordre global embarqué continu (block.order===i+1)',O.blocks.every((b,i)=>b.order===i+1));
   for(const motion of ['reduce','no-preference']){
    const context=await browser.newContext({viewport:{width:1280,height:900},reducedMotion:motion});
    await context.route(/^https?:/,route=>{requests.push(route.request().url());return route.abort()});
    const page=await context.newPage();page.on('pageerror',error=>errors.push(id+' '+motion+' : '+error.message));
    await page.goto(pathToFileURL(file).href+'#/home');await page.waitForFunction(()=>window.MEDINA_CATEGORY_ORGANISATION&&document.querySelector('.mcg-home'));
    if(motion==='reduce'){
     for(const view of VIEWS){
      const tag=id+' '+LABEL[view],expected=expectedView(O,view);
      await go(page,hashFor(view));const s=await snapshot(page);
      equal(tag+' : cartes dans l’ordre de la vue',s.cards.map(c=>c.code),expected.map(b=>b.code));
      equal(tag+' : numéros des cartes continus 1..n',s.cards.map(c=>[c.rank,c.number]),expected.map((b,i)=>[String(i+1),(i+1)+'.']));
      check(tag+' : aria-label cohérent avec le numéro',s.cards.every((c,i)=>c.aria.startsWith('Catégorie '+(i+1)+(view?' sur '+expected.length+' · ':' : '))&&c.aria.endsWith('— '+c.code)),s.cards.map(c=>c.aria));
      equal(tag+' : barre latérale même ordre et mêmes numéros',s.side.map(x=>[x.code,x.rank,x.number]),s.cards.map(c=>[c.code,c.rank,c.number]));
      if(view){equal(tag+' : poids affiché propre à la vue',s.cards.map(c=>c.weight),expected.map(b=>String(b.weight)));check(tag+' : note d’ordre adaptée',s.note&&s.note.view===view&&s.note.text===NOTE[view],s.note);}
      else{check(tag+' : note d’ordre globale inchangée',s.note&&s.note.view==='global'&&s.note.text===O.category_order.label,s.note);check(tag+' : poids global inchangé',s.cards.every(c=>c.weight===null));}
      for(const [i,b] of expected.entries()){
       await go(page,hashFor(view,'category='+encodeURIComponent(b.code)));
       const head=await page.evaluate(()=>({code:document.querySelector('[data-mcg-block]')?.dataset.mcgBlock,rank:document.querySelector('[data-mcg-block]')?.dataset.mcgRank,eyebrow:document.querySelector('.mcg-block-heading .mcg-eyebrow')?.textContent,side:document.querySelector('#spec-nav [data-mcg-sidebar-category][open]')?.dataset.mcgRank}));
       equal(tag+' '+b.code+' : en-tête de bloc et lien profond',head,{code:b.code,rank:String(i+1),eyebrow:'Catégorie '+(i+1)+' · '+b.code,side:String(i+1)});
      }
      await page.evaluate(()=>document.fonts.ready);await go(page,hashFor(view));await page.evaluate(()=>{document.getElementById('mcg-categories-title')?.scrollIntoView({block:'start'});window.scrollBy(0,-24);document.querySelector('#spec-nav')?.scrollIntoView({block:'start'});});
      const capture=path.join(out,`${id.toLowerCase()}_vue_${LABEL[view]}_1280.png`);await page.screenshot({path:capture});captures.push(capture);
     }
     // The same category keeps its code in every view; only the displayed number changes.
     const probe=expectedView(O,'frequent')[0]||expectedView(O,'federal_exam')[0];
     if(probe){const ranks={};for(const view of VIEWS){await go(page,hashFor(view,'category='+encodeURIComponent(probe.code)));ranks[LABEL[view]]=await page.locator('[data-mcg-block]').evaluate(el=>[el.dataset.mcgBlock,el.dataset.mcgRank]);}
      equal(id+' '+probe.code+' : code stable, numéro propre à chaque vue',ranks,Object.fromEntries(VIEWS.map(v=>[LABEL[v],[probe.code,String(expectedView(O,v).findIndex(b=>b.code===probe.code)+1)]])));}
     await go(page,hashFor(''));await go(page,hashFor('frequent'));
     check(id+' : mouvement réduit, aucune animation de renumérotation',await page.evaluate(()=>document.getAnimations().filter(a=>a.effect?.target?.matches('[data-mcg-category],[data-mcg-sidebar-category],[data-mcg-rank-value]')).length)===0);
    }else{
     const movedTo=expectedView(O,'frequent');
     if(movedTo.length&&movedTo.some((b,i)=>b.global!==i+1)){
      await go(page,hashFor(''));
      // Read animations synchronously right after the hash change triggers render().
      const result=await page.evaluate(view=>new Promise(resolve=>{addEventListener('hashchange',()=>setTimeout(()=>{const list=document.getAnimations().filter(a=>a.effect?.target?.matches('#content [data-mcg-category],#spec-nav [data-mcg-sidebar-category],[data-mcg-rank-value]'));resolve({count:list.length,max:Math.max(0,...list.map(a=>Number(a.effect.getTiming().duration)+Number(a.effect.getTiming().delay||0))),cards:list.filter(a=>a.effect.target.matches('#content [data-mcg-category]')).length,side:list.filter(a=>a.effect.target.matches('#spec-nav [data-mcg-sidebar-category]')).length,numbers:list.filter(a=>a.effect.target.matches('[data-mcg-rank-value]')).map(a=>[a.effect.target.closest('[data-mcg-rank]').dataset.mcgRank,a.effect.target.dataset.mcgRankFrom])})},0),{once:true});location.hash=view;}),hashFor('frequent'));
      check(id+' : transition FLIP des cartes',result.cards>0,result);
      check(id+' : transition FLIP de la barre latérale',result.side>0,result);
      check(id+' : durée ≤ 220 ms',result.max>0&&result.max<=220,result);
      check(id+' : numéros changés visiblement (ancien → nouveau)',result.numbers.length>0&&result.numbers.every(([to,from])=>to!==from),result.numbers);
      await page.waitForTimeout(300);check(id+' : animations terminées',await page.evaluate(()=>document.getAnimations().filter(a=>a.effect?.target?.matches('[data-mcg-category],[data-mcg-sidebar-category],[data-mcg-rank-value]')).length)===0);
      equal(id+' : état final identique après animation',(await snapshot(page)).cards.map(c=>c.rank),movedTo.map((b,i)=>String(i+1)));
     }
    }
    await context.close();
   }
  }
  check('aucune ressource distante demandée',requests.length===0,requests);
  check('aucune erreur JavaScript',errors.length===0,errors);
  const result={result:'OK',fragments:ids,checks:checks.length,captures};
  fs.writeFileSync(path.join(out,'renumbering_results.json'),JSON.stringify({...result,names:checks},null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
