from pathlib import Path
import json,hashlib,datetime
from playwright.sync_api import sync_playwright
D=Path(__file__).resolve().parent;F=D/'E07-apercu-autonome.html';html=F.read_text();out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preview_sha256':hashlib.sha256(F.read_bytes()).hexdigest(),'checks':[],'mode':'Origine interceptée ; toutes autres requêtes bloquées ; contrôles visibles réels.'}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(1440,960),(390,844)]:
  c=b.new_context(viewport={'width':width,'height':height});pg=c.new_page();pg.route('**/*',lambda r:r.abort());pg.route('https://medina-preview.test/',lambda r:r.fulfill(status=200,content_type='text/html',body=html));pg.goto('https://medina-preview.test/',wait_until='domcontentloaded');pg.wait_for_selector('.mc');seen={}
  for panel in ['pA','pE','pS','pP']:
   pg.locator('.mc-tabs [data-p="'+panel+'"]').click()
   for tab in range(6) if panel=='pS' else [None]:
    if tab is not None:pg.locator('.mc-sci-bar [data-s]').nth(tab).click()
    keys=list(dict.fromkeys(pg.locator('.mc-ab:visible').evaluate_all('(xs)=>xs.map(x=>x.dataset.ab)')))
    for key in keys:
     if key in seen:continue
     pg.locator('.mc-ab[data-ab="'+key+'"]:visible').first.click();dlg=pg.locator('.mc-dlg-b');assert dlg.is_visible(),key;txt=dlg.inner_text().replace('\u00ad','');assert len(txt)>10;seen[key]=txt;pg.keyboard.press('Escape')
  out['checks'].append({'viewport':[width,height],'windows':seen});c.close()
 b.close()
out['result']='passed';(D/'abbreviation-browser-report.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print([(x['viewport'],len(x['windows'])) for x in out['checks']])
