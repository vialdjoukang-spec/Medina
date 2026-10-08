const fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright();
const file=process.env.F, out=process.env.OUT;
(async()=>{
 const server=http.createServer((q,r)=>{r.setHeader('Content-Type','text/html; charset=utf-8');r.end(fs.readFileSync(file))});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const base='http://127.0.0.1:'+server.address().port+'/S01.html';
 const browser=await chromium.launch(browserOptions(chromium));
 const jobs=[['I21','pc',0,'#i21-16'],['I21','mob',1,'#i21-e-2 table'],['I21','mob',0,'#i21-16 .mc-key, #i21-16 .key'],['I25','pc',0,'#i25-16'],['I25','mob',1,'#i25-e-6 table'],['I21','mob',2,'.mc-sci:not([hidden]) .mc-key, .sci:not([hidden]) .key']];
 for(const [code,vpn,tab,sel] of jobs){
   const vp=vpn==='pc'?{width:1440,height:1000}:{width:390,height:844};
   const ctx=await browser.newContext({viewport:vp,reducedMotion:'reduce'}); const page=await ctx.newPage();
   await page.goto(base+'#/entry/'+code); await page.waitForFunction(()=>window.MDN_READY===true); await page.waitForTimeout(500);
   await page.locator('.mc-tabs button').nth(tab).click(); await page.waitForTimeout(300);
   const loc=page.locator(sel).first(); const n=await page.locator(sel).count();
   if(n){await loc.scrollIntoViewIfNeeded(); await loc.screenshot({path:path.join(out,`el_${code}_${vpn}_${sel.replace(/[^a-z0-9]/gi,'_').slice(0,30)}.jpg`),type:'jpeg',quality:70});}
   else console.log('missing',sel);
   await ctx.close();
 }
 // dialogs on mobile
 for(const [code,tab,k] of [['I21',0,'i21-algo'],['I25',0,'i25-rfcl'],['I25',1,'i25-hautrisque']]){
   const ctx=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'}); const page=await ctx.newPage();
   await page.goto(base+'#/entry/'+code); await page.waitForFunction(()=>window.MDN_READY===true); await page.waitForTimeout(500);
   await page.locator('.mc-tabs button').nth(tab).click(); await page.waitForTimeout(300);
   await page.evaluate(k=>{const pid=document.querySelector('.mc-tabs [aria-selected="true"]').getAttribute('data-p');document.querySelector('#'+pid+' [data-k="'+k+'"]').click()},k);
   await page.waitForTimeout(300); await page.screenshot({path:path.join(out,`dlg_${k}.jpg`),type:'jpeg',quality:70});
   await ctx.close();
 }
 await browser.close(); server.close();
})().catch(e=>{console.error(e);process.exit(1)});
