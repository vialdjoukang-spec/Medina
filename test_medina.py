from playwright.sync_api import sync_playwright
import sys
F='file:///home/claude/medina/MEDINA.html'
code=sys.argv[1] if len(sys.argv)>1 else 'I50'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1300,'height':900});er=[]
    pg.on('pageerror',lambda e:er.append(str(e)));pg.on('console',lambda m:m.type=='error' and er.append(m.text))
    pg.goto(F);pg.wait_for_timeout(1200);pg.screenshot(path='t_home.png')
    pg.goto(F+'#/entry/'+code);pg.wait_for_timeout(1200);pg.screenshot(path='t_course.png')
    print('mc',pg.locator('.mc').count(),'ab',pg.locator('.mc .mc-ab').count(),'w',pg.locator('.mc .mc-w').count())
    pg.locator('.mc .mc-ab').first.click();pg.wait_for_timeout(300);print('dlg',pg.eval_on_selector('dialog.mc-dlg','d=>d.open'),pg.inner_text('#mc-dlg-t'))
    pg.screenshot(path='t_ab.png')
    inner=pg.locator('dialog.mc-dlg .mc-dlg-b .mc-ab')
    print('abs in dialog',inner.count())
    if inner.count():
        inner.first.click();pg.wait_for_timeout(300);print('nested',pg.inner_text('#mc-dlg-t'),'back',pg.is_visible('.mc-back'))
    pg.keyboard.press('Escape');pg.wait_for_timeout(200)
    w=pg.locator('.mc .mc-w').first; w.click();pg.wait_for_timeout(300);print('green',pg.inner_text('#mc-dlg-t'));pg.keyboard.press('Escape')
    # abbreviation inside green span opens abbreviation not green
    ab_in_w=pg.locator('.mc .mc-w .mc-ab')
    if ab_in_w.count():
        ab_in_w.first.click();pg.wait_for_timeout(300);print('ab-in-green ->',pg.inner_text('#mc-dlg-t'));pg.keyboard.press('Escape')
    pg.locator('.mc-toc [data-go]').nth(3).click();pg.wait_for_timeout(500);print('url after toc',pg.url[-30:])
    pg.click('.mc-book');pg.wait_for_timeout(400);pg.screenshot(path='t_book.png');print('pager',pg.inner_text('.mc-panel:not([hidden]) .mc-pager span'))
    for tab in ['pE','pS','pP']:
        pg.click(f'.mc-tabs button[data-p="{tab}"]');pg.wait_for_timeout(300);print(tab,pg.inner_text('.mc-panel:not([hidden]) .mc-pager span'))
    pg.click('.mc-book')
    pg.select_option('.mc-font',index=2);pg.wait_for_timeout(200);print('font',pg.evaluate("getComputedStyle(document.querySelector('.mc-ilot')).fontFamily")[:30])
    pg.goto(F+'#/entry/I21');pg.wait_for_timeout(800);print('I21 plan',pg.locator('.mc').count(),pg.locator('.plan-grid').count())
    pg.goto(F+'#/entry/'+code+'?view=plan');pg.wait_for_timeout(800);print('plan view',pg.locator('.mc').count(),pg.locator('.plan-grid').count())
    m=b.new_page(viewport={'width':390,'height':844});m.goto(F+'#/entry/'+code);m.wait_for_timeout(1200);m.screenshot(path='t_mobile.png')
    print('mobile overflow',m.evaluate('document.documentElement.scrollWidth'))
    print('errors',er);b.close()
