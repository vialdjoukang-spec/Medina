from playwright.sync_api import sync_playwright
from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).parent;url='http://127.0.0.1:8876/MEDINA_S05_endocrinien-metabolique.html#/entry/E05';results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(1365,950),(390,844)]:
  page=b.new_page(viewport={'width':width,'height':height});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url);page.wait_for_selector('.mc');page.locator('.mc-tabs [data-p="pS"]').click();page.wait_for_timeout(200)
  sem=page.locator('.mc #e05-s-semio');assert sem.is_visible();assert page.locator('.mc-sci-bar button').count()==6
  assert page.locator('.mc-sci-bar button').first.get_attribute('id')=='e05-tab-semio';assert page.locator('.mc .mc-sci:not([hidden])').count()==1
  assert page.locator('.mc [data-semiology]').count()==9
  page.screenshot(path=str(D/'captures'/f'e05-{width}-semio.png'),full_page=False);page.locator('.mc #e05-semio-normal').evaluate("e=>e.scrollIntoView({block:'start'})");page.screenshot(path=str(D/'captures'/f'e05-{width}-semio-contenu.png'))
  page.locator('.mc #e05-tab-s01').click();assert page.locator('.mc #e05-s01-pane').is_visible();assert not sem.is_visible()
  tab=page.locator('.mc #e05-tab-semio');tab.focus();page.keyboard.press('Enter');assert sem.is_visible();assert tab.get_attribute('aria-selected')=='true'
  page.locator('.mc #e05-tab-s01').click();tab.focus();page.keyboard.press('Space');assert sem.is_visible()
  sem.locator('[data-k="e05-loglineaire"]').click();assert page.locator('#mc-dialog').is_visible();assert 'Fiche absente' not in page.locator('#mc-dialog').inner_text();page.screenshot(path=str(D/'captures'/f'e05-{width}-popup.png'));page.keyboard.press('Escape')
  page.locator('.mc-size-toggle').click();page.locator('.mc-size-range').focus();page.keyboard.press('End');page.locator('.mc-size-toggle').click();assert page.locator('.mc').evaluate("e=>getComputedStyle(e).getPropertyValue('--mc-fs').trim()")=='24px';page.locator('.mc #e05-tab-semio').scroll_into_view_if_needed();page.screenshot(path=str(D/'captures'/f'e05-{width}-police24.png'))
  # Each original image is decoded by a browser Image object; SVG wrappers do not draw anatomy.
  image_results=page.locator('.mc svg image').evaluate_all("async es=>await Promise.all(es.map(e=>new Promise(resolve=>{const i=new Image();i.onload=()=>resolve({url:e.getAttribute('href'),width:i.naturalWidth,ok:true});i.onerror=()=>resolve({url:e.getAttribute('href'),ok:false});i.src=e.getAttribute('href')})))")
  assert all(x['ok'] for x in image_results),image_results
  page.locator('.mc-book').click();page.wait_for_timeout(150);assert page.locator('.mc').evaluate("e=>e.classList.contains('book')");page.locator('.mc #e05-tab-semio').click();page.locator('.mc #e05-semio-normal').evaluate("e=>e.scrollIntoView({block:'start'})");page.screenshot(path=str(D/'captures'/f'e05-{width}-livre24.png'))
  sem.evaluate('e=>e.scrollTop=e.scrollHeight');assert sem.evaluate('e=>e.scrollTop>0');page.screenshot(path=str(D/'captures'/f'e05-{width}-livre-fin.png'));
  page.locator('.mc-navigo-trigger').click();assert page.locator('.mc-navigo-panel').is_visible();page.locator('.mc-navigo-search').fill('mécanisme');assert page.locator('.mc-navigo-list button:visible').count()>0;page.locator('.mc-navigo-close').click()
  overflow=page.evaluate('({viewport:innerWidth,document:document.documentElement.scrollWidth})')
  results.append({'viewport':[width,height],'initial_semiology':True,'nine_sections':True,'six_tabs':True,'native_keyboard_Enter_Space':True,'popup':True,'font_px':24,'book':True,'navigo':True,'images':image_results,'pageerrors':errors,'overflow':overflow});page.close()
 b.close()
report={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'build_sha256':hashlib.sha256(Path('/workspace/scratch/e05-integrate/build/fragments/MEDINA_S05_endocrinien-metabolique.html').read_bytes()).hexdigest(),'results':results};(D/'navigateur.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
