from pathlib import Path
import json,datetime,hashlib
from playwright.sync_api import sync_playwright
O=Path(__file__).resolve().parent;f=O/'D65-apercu-autonome.html';h=hashlib.sha256(f.read_bytes()).hexdigest();v=json.loads((O/'verification.json').read_text());assert h==v['preview_sha256'];rows=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1440,900),(390,844)]:
  page=b.new_page(viewport={'width':width,'height':height});page.route('**/*',lambda r:r.fulfill(body=f.read_bytes(),content_type='text/html') if r.request.url=='http://medina.local/d65' else r.abort());page.goto('http://medina.local/d65');page.evaluate("location.hash='#/entry/D65'");page.wait_for_timeout(600);page.locator('.mc-tabs [data-p="pS"]').click();e=page.locator('#d65-semio-normal');e.scroll_into_view_if_needed();e.screenshot(path=str(O/f'captures/D65-{width}-semio-body-final.png'))
  page.locator('.mc-tabs [data-p="pA"]').click();page.locator('.mc-book').click();page.locator('.mc-size-toggle').click();page.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=24;r.dispatchEvent(new Event('input'))})()");page.keyboard.press('Escape');page.locator('.mc-tabs [data-p="pS"]').click();page.locator('[data-s="d65-s-anat"]').click();e=page.locator('#d65-science-sem-annotations');e.scroll_into_view_if_needed();px=e.locator('p').evaluate('(e)=>parseFloat(getComputedStyle(e).fontSize)');assert px>=23;overflow=page.evaluate('document.documentElement.scrollWidth-innerWidth');assert overflow==0;e.screenshot(path=str(O/f'captures/D65-{width}-annotations-livre24-final.png'));rows.append({'width':width,'annotation_paragraph_font_px':px,'root_horizontal_overflow':overflow});page.close()
 b.close()
(O/'book24-check.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preview_sha256':h,'rows':rows,'source_binding_created':False,'clinical_certification':False},indent=2)+'\n');print(rows)
