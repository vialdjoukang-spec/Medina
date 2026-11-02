from pathlib import Path
import json,datetime,hashlib
from playwright.sync_api import sync_playwright
D=Path(__file__).resolve().parent;F=D/'E07-apercu-autonome.html';html=F.read_text();report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preview_sha256':hashlib.sha256(F.read_bytes()).hexdigest(),'method':'Origine interceptée, requêtes externes bloquées. Pour les captures diagnostiques seulement, contrôles fixed/sticky masqués en mémoire afin de voir tous les pixels et repères. Les captures normales restent conservées. Aucun HTML ou asset modifié.','figures':[]}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for w,h in [(1440,960),(390,844)]:
  c=b.new_context(viewport={'width':w,'height':h});pg=c.new_page();pg.route('**/*',lambda r:r.abort());pg.route('https://medina-preview.test/',lambda r:r.fulfill(status=200,content_type='text/html',body=html));pg.goto('https://medina-preview.test/',wait_until='domcontentloaded');pg.wait_for_selector('.mc')
  for panel,tab,ident in [('pA',None,'clinique'),('pS','anat','compression'),('pS','histo','histologie')]:
   pg.locator('.mc-tabs [data-p="'+panel+'"]').click()
   if tab:pg.locator('[data-s="e07-s-'+tab+'"]').click()
   fig=pg.locator('#e07-figure-'+ident);fig.scroll_into_view_if_needed();fig.locator('img').evaluate('(im)=>im.decode()')
   hide=pg.evaluate('''()=>{let xs=[];for(let e of document.querySelectorAll('*'))if(['fixed','sticky'].includes(getComputedStyle(e).position)){xs.push([e,e.style.visibility]);e.style.visibility='hidden'}window.__captureHidden=xs;return xs.length}''')
   fn=f'{w}-{ident}-diagnostic-figure.png';fig.screenshot(path=str(D/fn));markers=fig.locator('.e07-pin').count();assert markers==(2 if ident=='compression' else 4)
   report['figures'].append({'viewport':[w,h],'figure':ident,'markers':markers,'capture':fn,'fixed_controls_hidden':hide,'natural':fig.locator('img').evaluate('(im)=>[im.naturalWidth,im.naturalHeight,im.complete]')})
   pg.evaluate('()=>{for(let [e,v] of window.__captureHidden)e.style.visibility=v}')
  c.close()
 b.close()
(D/'figure-capture-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('Six captures diagnostiques, pixels originaux et repères visibles.')
