#!/usr/bin/env python3
"""Real browser checks: responsive plan, HTTP refresh, simulated stale clock.

Intercepted local HTTP origin; no claim of public deployment. Requires Playwright.
"""
from pathlib import Path
import json
import hashlib
import datetime
from playwright.sync_api import sync_playwright

HERE=Path(__file__).resolve().parent
def main():
    content=(HERE/'dashboard.html').read_bytes();data=json.loads((HERE/'status.json').read_text())
    out=HERE/'evidence';out.mkdir(exist_ok=True)
    receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'html_sha256':hashlib.sha256(content).hexdigest(),'mode':'Intercepted HTTP origin; external requests blocked','views':[],'errors':[]}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        pages=[]
        for width,height in [(1440,900),(390,844)]:
            page=browser.new_page(viewport={'width':width,'height':height});page.clock.install();calls=[]
            page.on('pageerror',lambda e:receipt['errors'].append(str(e)))
            def route(r,request,calls=calls):
                if '/status.json' in r.request.url:
                    calls.append(r.request.url);r.fulfill(body=json.dumps(data),content_type='application/json')
                elif r.request.url.endswith('/dashboard.html'):r.fulfill(body=content,content_type='text/html')
                else:r.abort()
            page.route('**/*',route);page.goto('https://medina-harness.test/dashboard.html')
            assert page.locator('#cards article').count()==4
            assert page.locator('#futureplan .card').count()==4
            assert page.locator('#futureplan tbody tr').count()==340
            assert page.evaluate('document.documentElement.scrollWidth-innerWidth')==0
            page.locator('#search').fill('C85')
            assert page.locator('#futureplan tbody tr').count()>=1
            page.locator('#search').fill('')
            page.screenshot(path=str(out/f'dashboard-{width}.png'))
            pages.append((page,width,calls))
        for page,width,calls in pages:
            page.clock.fast_forward(60001)
            page.wait_for_timeout(150)
        for page,width,calls in pages:
            assert len(calls)>=2,'Initial and scheduled HTTP refresh missing'
            page.evaluate("Date.now=()=>Date.parse(D.generated_at)+1300000;paint()")
            assert 'périmé' in page.locator('#gate').inner_text()
            assert page.locator('#cards .good').count()==0
            receipt['views'].append({'width':width,'four_agents':True,'four_systems':True,'historical_and_current_rows':340,'overflow':0,'filter':True,'http_refresh_calls':len(calls),'scheduled_refresh_timer':'60s advanced with browser clock','stale_warning':True,'stale_agents_not_green':True})
            page.close()
        browser.close()
    assert not receipt['errors'],receipt['errors']
    (out/'browser.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False))
if __name__=='__main__':main()
