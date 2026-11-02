from pathlib import Path
import json,hashlib,datetime
from playwright.sync_api import sync_playwright
O=Path(__file__).resolve().parent;N=O/'G25-apercu-autonome.html';CAP=O/'captures'
preview_hash=hashlib.sha256(N.read_bytes()).hexdigest()
d=json.loads((O/'browser-report.json').read_text());assert d['passed'] and d['preview_sha256']==preview_hash
out=dict(mode='Additional normal scroll captures to inspect long figures/captions below fixed shared navigation; no CSS or original image mutation',preview_sha256=preview_hash,started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),captures=[])
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1440,900),(390,844)]:
  page=b.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  def route(r):
   if r.request.url=='http://medina.local/native.html':r.fulfill(body=N.read_bytes(),content_type='text/html')
   else:r.abort()
  page.route('**/*',route);page.goto('http://medina.local/native.html',wait_until='domcontentloaded');page.evaluate("location.hash='#/entry/G25'");page.wait_for_timeout(1200)
  def shot(name):
   page.wait_for_timeout(180);f=CAP/f'G25-{width}-reading-{name}.png';page.screenshot(path=str(f));out['captures'].append(dict(path=str(f.relative_to(O)),width=width,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
  def place(locator,offset=185):
   y=locator.evaluate('(x)=>x.getBoundingClientRect().top+scrollY');page.evaluate('y=>scrollTo(0,y)',max(0,y-offset))
  page.locator('.mc-tabs button[data-p="pS"]').click();page.locator('.mc-sci-bar button[data-s="g25-s-semio"]').click();place(page.locator('[id="g25-semio-normal"]'));shot('semio')
  page.locator('.mc-sci-bar button[data-s="g25-s-histo"]').click();fig=page.locator('[id="g25-s-histo"] [data-g25-figure="histo"]');im=fig.locator('img');im.evaluate('(x)=>x.decode()');place(im);shot('histo-top')
  y=im.evaluate('(x)=>x.getBoundingClientRect().top+scrollY+x.getBoundingClientRect().height*.42');page.evaluate('y=>scrollTo(0,y)',max(0,y-185));shot('histo-middle')
  place(fig.locator('figcaption'));shot('histo-caption')
  page.locator('.mc-tabs button[data-p="pA"]').click();fig=page.locator('[id="pA"] [data-g25-figure="motor"]');place(fig.locator('figcaption'));shot('motor-caption')
  page.locator('.mc-tabs button[data-p="pP"]').click();place(page.locator('[id="g25-p-sifrol"]'));shot('sifrol')
  page.close()
 b.close()
out['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();assert hashlib.sha256(N.read_bytes()).hexdigest()==preview_hash
(O/'supplemental-visual-captures.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Captures complémentaires de lecture produites, à examiner réellement par IA avant revue finale.')
