"""Native MEDINA preview exercised through an intercepted HTTP origin; assets embedded.
This is not a claim of HTTP deployment, remote availability, or medical review.
"""
from pathlib import Path
from urllib.parse import urlparse, unquote
import json, mimetypes
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
NATIVE=OUT/'C85-apercu-autonome.html'
CAP=OUT/'captures'; CAP.mkdir(exist_ok=True)
report={'mode':'Chromium intercepted HTTP URL: autonomous native HTML only, all other requests aborted; original figure bytes embedded unchanged; no deployment claim','viewports':[],'errors':[]}
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    for width,height in [(1440,900),(390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        page.on('pageerror',lambda e:report['errors'].append(str(e)))
        def route(req):
            path=unquote(urlparse(req.request.url).path).lstrip('/')
            local=ROOT/path
            if path == 'native.html':
                req.fulfill(body=NATIVE.read_bytes(),content_type='text/html')
            else:
                req.abort()
        page.route('**/*',route)
        page.goto('http://medina.local/native.html',wait_until='domcontentloaded',timeout=60000)
        page.evaluate("location.hash='#/entry/C85'")
        page.wait_for_timeout(1500)
        item={'width':width,'course_visible':page.locator('.mc').count()==1,'screenshots':[]}
        if not item['course_visible']:
            item['body_sample']=page.inner_text('body')[:1000];report['viewports'].append(item);continue
        page.locator('.mc-tabs button[data-p="pS"]').click()
        page.wait_for_timeout(300)
        item['science_buttons']=page.locator('.mc-sci-bar button').all_text_contents()
        item['semio_visible']=page.locator('[id="c85-s-semio"]').is_visible()
        item['semio_sections']=page.locator('[data-semiology]').count()
        item['images_before_lazy_scroll']=page.locator('figure:has(img) img').evaluate_all('(xs)=>xs.map(x=>({embedded:x.getAttribute("src").startsWith("data:"),loaded:x.complete&&x.naturalWidth>0,width:x.naturalWidth}))')
        path=CAP/f'C85-{width}-semio.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        page.locator('figure:has(img)').filter(visible=True).first.scroll_into_view_if_needed()
        page.wait_for_timeout(400)
        path=CAP/f'C85-{width}-figure.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        item['originals_checked']=[]
        for tab,figure in [('c85-s-semio','c85-semio-scanner'),('c85-s-anat','c85-figure-originale-mediastin'),('c85-s-histo','c85-figure-originale-histologie'),('c85-s-physio','c85-physio-scanner')]:
            page.locator(f'[data-s="{tab}"]').click()
            image=page.locator(f'#{figure} img');image.scroll_into_view_if_needed()
            image.evaluate('(i)=>i.decode()')
            state=image.evaluate('(i)=>({width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0})')
            state['figure']=figure;item['originals_checked'].append(state)
            path=CAP/f'C85-{width}-{tab}.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
            assert state['loaded'],figure
        item['horizontal_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth')
        item['annotations_visible']=page.locator('figcaption b').filter(visible=True).count()
        for panel in ['pE','pP','pA','pS']:
            page.locator(f'.mc-tabs button[data-p="{panel}"]').click();page.wait_for_timeout(80)
        page.locator('.mc-tabs button[data-p="pA"]').click()
        page.locator('[data-k="c85-ssp-g2"]').click();page.wait_for_timeout(100)
        scoped=page.locator('.mc-dlg-b').inner_text().replace('\u00ad','')
        item['profiles_g2_scoped']='Masse et adénopathie' in scoped and '60 à 89' not in scoped
        assert item['profiles_g2_scoped'],'PROFILES G2 opened unexpected content: '+scoped[:400]
        page.keyboard.press('Escape')
        popup=page.locator('.mc-w').filter(visible=True).first
        popup.click();page.wait_for_timeout(150)
        item['popup_visible']=page.locator('.mc-dlg-b').is_visible()
        item['popup_missing']='Fiche absente' in page.inner_text('.mc-dlg-b')
        path=CAP/f'C85-{width}-popup.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        page.keyboard.press('Escape')
        page.locator('.mc-book').click();page.wait_for_timeout(150)
        item['book_active']='book' in page.locator('.mc').get_attribute('class').split()
        page.locator('.mc-size-toggle').click()
        page.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=24;r.dispatchEvent(new Event('input'))})()")
        page.keyboard.press('Escape');page.wait_for_timeout(200)
        item['book_font']=page.evaluate("getComputedStyle(document.querySelector('.mc')).getPropertyValue('--mc-fs').trim()")
        item['book_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth')
        path=CAP/f'C85-{width}-livre24.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        report['viewports'].append(item);page.close()
    browser.close()
(OUT/'browser-report-autonomous.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
