from pathlib import Path
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright
import json
OUT=Path(__file__).parent
BASE='http://127.0.0.1:8779/MEDINA_S05_endocrinien-metabolique.html'
result={'checked_at':datetime.now(timezone.utc).isoformat(),'url':BASE,'browser':'Chromium /usr/bin/chromium','viewports':[],'errors':[]}
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium')
 for width,height in [(1360,950),(390,844)]:
  pg=b.new_page(viewport={'width':width,'height':height});js=[];bad=[]
  pg.on('pageerror',lambda e:js.append(str(e)))
  pg.on('response',lambda r:bad.append({'url':r.url,'status':r.status}) if r.status>=400 else None)
  pg.goto(BASE+'#/entry/E10');pg.wait_for_function('window.MDN_READY===true');pg.locator('.mc').wait_for()
  assert pg.locator('#e10-alpha-warning').inner_text()=='Révision Alpha en cours : certaines réserves thérapeutiques et sources héritées restent à vérifier ; les audits finaux de cette version ne sont pas clos.'
  if width==1360: pg.screenshot(path=str(OUT/'e10-1360-ouverture.png'))
  pg.locator('.mc-tabs [data-p=pS]').click();pg.wait_for_timeout(150)
  row={'width':width,'height':height,'initial_selected':pg.locator('.mc-sci-bar button[aria-selected=true]').get_attribute('data-s'),'initial_visible':pg.locator('.mc-sci:not([hidden])').get_attribute('id'),'visible_provisional_notice':True,'nine_sections':pg.locator('#e10-s-semio [data-semiology]').count(),'tabs':[]}
  assert row['initial_selected']==row['initial_visible']=='e10-s-semio'
  assert row['nine_sections']==9
  for button in pg.locator('.mc-sci-bar button').all():
   target=button.get_attribute('data-s');button.click();pg.wait_for_timeout(80)
   visible=pg.locator('.mc-sci:not([hidden])')
   assert visible.count()==1 and visible.get_attribute('id')==target
   assert button.get_attribute('aria-selected')=='true'
   row['tabs'].append(target)
  tab=pg.locator('#e10-tab-semio');tab.focus();pg.keyboard.press('Enter');assert pg.locator('#e10-s-semio').is_visible()
  pg.locator('.mc-sci-bar button[data-s=e10-s02-pane]').click();tab.focus();pg.keyboard.press('Space');assert pg.locator('#e10-s-semio').is_visible()
  row['keyboard_enter_space']=True
  row['document_width']=pg.evaluate('document.documentElement.scrollWidth')
  assert row['document_width']<=width+2
  row['svg_images']=pg.locator('#e10-s-semio svg image').evaluate_all('(xs)=>xs.map(x=>({href:x.getAttribute("href"),width:x.getBoundingClientRect().width,height:x.getBoundingClientRect().height}))')
  pg.locator('.mc-sci-bar').evaluate('(x)=>window.scrollTo(0,window.scrollY+x.getBoundingClientRect().top-85)');pg.wait_for_timeout(150)
  pg.screenshot(path=str(OUT/f'e10-{width}-semio.png'))
  pg.locator('.mc-size-toggle').click();pg.locator('.mc-size-range').evaluate('(r)=>{r.value=24;r.dispatchEvent(new Event("input",{bubbles:true}))}')
  assert pg.locator('.mc-size-value').inner_text()=='24 px'
  pg.keyboard.press('Escape');pg.locator('.mc-book').click();pg.wait_for_timeout(200)
  assert pg.locator('.mc.book').count()==1
  row['font_24_book']=True;row['book_document_width']=pg.evaluate('document.documentElement.scrollWidth')
  assert row['book_document_width']<=width+2
  pg.locator('#e10-tab-semio').click();assert pg.locator('#e10-s-semio').is_visible()
  pg.locator('#e10-s-semio').evaluate('(x)=>window.scrollTo(0,window.scrollY+x.getBoundingClientRect().top-90)');pg.wait_for_timeout(150)
  row['book_panel']=pg.locator('#e10-s-semio').evaluate('(x)=>({clientWidth:x.clientWidth,scrollWidth:x.scrollWidth,clientHeight:x.clientHeight,scrollHeight:x.scrollHeight})')
  assert row['book_panel']['scrollWidth']<=row['book_panel']['clientWidth']+2
  row['book_bottom_reachable']=pg.locator('#e10-s-semio').evaluate('(x)=>{x.scrollTop=x.scrollHeight;const reached=x.scrollTop+x.clientHeight>=x.scrollHeight-2;x.scrollTop=0;return reached}')
  assert row['book_bottom_reachable']
  pg.screenshot(path=str(OUT/f'e10-{width}-livre-24.png'))
  pg.locator('.mc-book').click();pg.locator('.mc-tabs [data-p=pA]').click()
  trigger=pg.locator('.mc [data-k=e10-a03-fenetre-2]').first;trigger.click();pg.wait_for_timeout(120)
  assert pg.locator('#mc-dialog').is_visible();assert 'Fiche absente' not in pg.locator('.mc-dlg-b').inner_text()
  row['popup']='e10-a03-fenetre-2';pg.screenshot(path=str(OUT/f'e10-{width}-popup.png'));pg.keyboard.press('Escape')
  row['js_errors']=js;row['failed_http']=bad
  if js:result['errors'].extend(js)
  if bad:result['errors'].extend(bad)
  result['viewports'].append(row);pg.close()
 b.close()
result['result']='passed' if not result['errors'] else 'failed'
(OUT/'browser-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(result['errors']))
