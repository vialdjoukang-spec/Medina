from pathlib import Path
import json,hashlib,datetime
from playwright.sync_api import sync_playwright
out=Path('/workspace/work/medina-cycle1/docs/collaboration/reviews/2026-10-11/CYCLE_01/CONTROLE_TITRES_FENETRES')
url='http://127.0.0.1:8769/fragments/MEDINA_S06_hematopoietique-lymphatique.html#/entry/D50'
r={'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'CSS uniquement, copie HTML au payload inchangé. Aucun verdict médical ni injection.','url':url,'viewports':[],'failures':[]}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for width,height in [(1440,1000),(390,844)]:
  pg=b.new_page(viewport={'width':width,'height':height});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(url,wait_until='domcontentloaded');pg.wait_for_function('window.MDN_READY===true');pg.locator('.mc[data-code="D50"]').wait_for();pg.evaluate('document.fonts.ready')
  pg.locator('.mc-tabs button[data-p="pA"]').click()
  state={'width':width,'height':height,'active_cycle':pg.locator('html').get_attribute('data-medina-active-cycle')}
  state['font_loaded']=pg.evaluate('document.fonts.check("16px Atkinson Hyperlegible Next")')
  state['course_body']=pg.locator('.mc #d50-0 p').first.evaluate('e=>({color:getComputedStyle(e).color,font:getComputedStyle(e).fontFamily})')
  state['term']=pg.locator('.mc .mc-w').first.evaluate('e=>({color:getComputedStyle(e).color,font:getComputedStyle(e).fontFamily})')
  state['gauges']=pg.locator('.nosology-progress[data-mcg-filter] progress').evaluate_all('els=>els.map(e=>({border:getComputedStyle(e).borderColor,appearance:getComputedStyle(e).appearance}))')
  pg.evaluate('window.scrollTo(0,0)');pg.screenshot(path=str(out/f'd50-{width}-ouverture.png'))
  pg.locator('[data-k="d50-ferritine"]').first.evaluate('e=>e.click()');pg.locator('#mc-dialog[open]').wait_for()
  state['headings']=pg.locator('#mc-dialog :is(h1,h2,h3,h4,h5,h6)').evaluate_all('els=>els.map(e=>({text:e.textContent,color:getComputedStyle(e).color,font:getComputedStyle(e).fontFamily}))')
  state['window_body']=pg.locator('.mc-dlg-b p').first.evaluate('e=>({color:getComputedStyle(e).color,font:getComputedStyle(e).fontFamily})')
  state['window_terms']=pg.locator('.mc-dlg-b :is(.mc-w,.mc-ab,a)').evaluate_all('els=>els.map(e=>({text:e.textContent,color:getComputedStyle(e).color}))')
  state['overflow']=pg.evaluate('document.documentElement.scrollWidth>innerWidth+2')
  pg.screenshot(path=str(out/f'd50-{width}-explication.png'))
  state['javascript_errors']=errs
  if state['active_cycle']!='1' or not state['font_loaded']:r['failures'].append(f'cycle/font {width}')
  if len(state['headings'])<3 or any(h['color']!='rgb(179, 38, 30)' for h in state['headings']):r['failures'].append(f'heading {width}')
  if state['window_body']['color']!='rgb(23, 62, 137)' or state['course_body']['color']!='rgb(23, 62, 137)':r['failures'].append(f'body {width}')
  if state['term']['color']!='rgb(155, 57, 0)' or any(t['color']!='rgb(155, 57, 0)' for t in state['window_terms']):r['failures'].append(f'term {width}')
  if not state['gauges'] or any(g['border']!='rgb(255, 255, 255)' or g['appearance']!='none' for g in state['gauges']):r['failures'].append(f'gauge {width}')
  if state['overflow'] or errs:r['failures'].append(f'overflow/errors {width}')
  r['viewports'].append(state);pg.close()
 b.close()
r['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();r['verdict']='pass' if not r['failures'] else 'fail'
r['files']={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in out.glob('*.png')}
(out/'verification.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(r,ensure_ascii=False,indent=2))
assert r['verdict']=='pass'
