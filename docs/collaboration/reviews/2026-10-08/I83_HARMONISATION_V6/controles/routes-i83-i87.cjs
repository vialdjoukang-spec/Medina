const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const root = process.env.I83_CONTROL_ROOT, output = process.env.I83_CONTROL_OUT;
const controls = process.env.I83_CONTROL_REPORTS;
const {loadPlaywright, browserOptions} = require(path.join(root, 'tests/browser_runtime.cjs'));
const {chromium} = loadPlaywright();
const file = path.join(output, 's01/fragments/MEDINA_S01_cardiovasculaire.html');
const report = {result:'pending',started_at:new Date().toISOString(),file,
  transport:'HTTP loopback with external HTTP(S) destinations blocked',
  scope:'S01 routes I83 and I87, desktop and mobile viewports, four panels, page errors and horizontal overflow',
  checks:[],cases:[],errors:[]};
const check = (name, value, detail) => {
  assert.ok(value,name+(detail===undefined?'':': '+JSON.stringify(detail)));
  report.checks.push({name,detail});
};
(async()=>{
 const browser=await chromium.launch(browserOptions(chromium));
 report.browser=await browser.version();
 try {
  const context=await browser.newContext({reducedMotion:'reduce'});
  await context.route(/^https?:/,route=>route.abort());
  const page=await context.newPage();
  page.on('pageerror',error=>report.errors.push(error.message));
  for(const width of [1360,390]) {
   await page.setViewportSize({width,height:width===390?844:900});
   for(const routeCode of ['I83','I87']) {
    await page.goto(pathToFileURL(file).href+'#/entry/'+routeCode);
    await page.waitForFunction(()=>window.MDN_READY===true);
    await page.locator('.mc[data-code="I83"]').waitFor();
    const prefix=width+' / '+routeCode;
    const counts={all:await page.locator('.mc').count(),I83:await page.locator('.mc[data-code="I83"]').count()};
    check(prefix+' : un seul cours primaire I83',counts.all===1&&counts.I83===1,counts);
    const tabs=page.locator('.mc[data-code="I83"] .mc-tabs button');
    check(prefix+' : quatre onglets',await tabs.count()===4);
    const panels=[];
    for(let index=0;index<4;index++) {
     const button=tabs.nth(index),panel=await button.getAttribute('data-p');
     await button.click();
     check(prefix+' : onglet '+panel+' accessible',await page.locator('#'+panel).isVisible()
      &&await button.getAttribute('aria-selected')==='true');
     const sizes=await page.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth}));
     check(prefix+' : aucun débordement dans '+panel,sizes.document<=sizes.viewport+1,sizes);
     panels.push({panel,visible:true,sizes});
    }
    report.cases.push({width,height:width===390?844:900,requested_route:routeCode,primary_course:'I83',counts,panels});
   }
  }
  check('Aucune erreur JavaScript',report.errors.length===0,report.errors);
  report.result='passed';
 } finally {await browser.close();}
})().catch(error=>{report.result='failed';report.failure=String(error.stack||error);process.exitCode=1;})
.finally(()=>{
 report.finished_at=new Date().toISOString();
 fs.writeFileSync(path.join(controls,'routes-i83-i87.json'),JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({result:report.result,checks:report.checks.length,cases:report.cases.length,errors:report.errors}));
});
