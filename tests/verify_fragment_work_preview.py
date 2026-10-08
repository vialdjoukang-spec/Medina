#!/usr/bin/env python3
"""Read-only interaction evidence for a stable internal T1 consultation HTML."""
import argparse
import asyncio
import ast
from collections import deque
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
from playwright.async_api import async_playwright


ATKINSON = "'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif"
NORMAL = lambda value: re.sub(r"\s+", " ", value.replace("\u00ad", "")).strip()
REPORT = {"scope": "Technical consultation interactions; no medical or final fragment certification.", "checks": [], "failures": [], "viewports": {}}


def check(label, condition, detail=None):
    REPORT["checks"].append(label)
    if not condition:
        REPORT["failures"].append({"label": label, "detail": detail})
        print(f"FAIL {label}: {str(detail)[:600]}", flush=True)


def internal_glossary_definitions(path):
    """Read literal glossary definitions without executing authored Python."""
    result = {}
    for statement in ast.parse(path.read_text()).body:
        if isinstance(statement, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "G" for target in statement.targets):
            try:
                result.update(ast.literal_eval(statement.value))
            except (ValueError, TypeError):
                pass
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            call = statement.value
            if isinstance(call.func, ast.Name) and call.func.id == "a" and len(call.args) >= 3:
                try:
                    values = [ast.literal_eval(arg) for arg in call.args]
                    result[values[0]] = {"lit": values[1], "full": values[2], "def": values[3] if len(values) > 3 else "", "ref": values[4] if len(values) > 4 else None}
                except (ValueError, TypeError):
                    pass
    return result


async def overflow(page, label, dialog=False):
    sizes = await page.evaluate("""() => {
      const d=document.querySelector('.mc-dlg[open]'),b=d?.querySelector('.mc-dlg-b'),r=d?.getBoundingClientRect();
      return {width:innerWidth,scroll:document.documentElement.scrollWidth,dialog:r?{x:r.x,width:r.width}:null,
       body:b?{width:b.clientWidth,scroll:b.scrollWidth}:null};
    }""")
    check(label + ": document reflow", sizes["scroll"] <= sizes["width"] + 1, sizes)
    if dialog:
        check(label + ": dialog reflow", bool(sizes["dialog"]) and sizes["dialog"]["x"] >= -1 and
              sizes["dialog"]["x"] + sizes["dialog"]["width"] <= sizes["width"] + 1 and
              sizes["body"]["scroll"] <= sizes["body"]["width"] + 1, sizes)


async def actual_font(page, selector):
    session = await page.context.new_cdp_session(page)
    try:
        await session.send("DOM.enable")
        await session.send("CSS.enable")
        doc = await session.send("DOM.getDocument")
        node = await session.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": selector})
        return (await session.send("CSS.getPlatformFontsForNode", {"nodeId": node["nodeId"]}))["fonts"]
    finally:
        await session.detach()


async def contrast(page, selector):
    return await page.locator(selector).first.evaluate("""el => {
      const rgb=s=>(s.match(/[0-9.]+/g)||[]).map(Number), lum=c=>{
        const v=c.slice(0,3).map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4});
        return .2126*v[0]+.7152*v[1]+.0722*v[2];};
      let parent=el,bg;
      while(parent){const value=getComputedStyle(parent).backgroundColor,c=rgb(value);
       if(c.length>=3&&(c.length===3||c[3]>0)){bg=c;break}parent=parent.parentElement;}
      const fg=rgb(getComputedStyle(el).color),a=lum(fg),b=lum(bg||[255,255,255]);
      return {foreground:getComputedStyle(el).color,background:bg,ratio:(Math.max(a,b)+.05)/(Math.min(a,b)+.05)};
    }""")


async def click_text_trigger(trigger):
    """Hit a painted inline fragment, rather than an empty corner of its union."""
    await trigger.scroll_into_view_if_needed()
    position = await trigger.evaluate("""el => {
      const outer=el.getBoundingClientRect();
      for(const r of el.getClientRects()){
        const left=Math.max(0,r.left),right=Math.min(innerWidth,r.right);
        const top=Math.max(0,r.top),bottom=Math.min(innerHeight,r.bottom);
        if(right>left && bottom>top)
          return {x:(left+right)/2-outer.left,y:(top+bottom)/2-outer.top};
      }
      throw new Error('No visible painted rectangle for the text trigger');
    }""")
    await trigger.click(position=position)


async def reveal(page, code, index):
    trigger = page.locator(f'.mc[data-code="{code}"] [data-k]').nth(index)
    context = await trigger.evaluate("""el => ({panel:el.closest('.mc-panel')?.id,science:el.closest('.mc-sci')?.id,
      feedback:el.closest('.mc-fb')?.hidden,quiz:[...el.closest('.mc').querySelectorAll('.mc-quiz')].indexOf(el.closest('.mc-quiz'))})""")
    if context.get("panel"):
        await page.locator(f'.mc-tabs button[data-p="{context["panel"]}"]').click()
    if context.get("science"):
        await page.locator(f'.mc-sci-bar button[data-s="{context["science"]}"]').click()
    if context.get("feedback") and context["quiz"] >= 0:
        await page.locator(f'.mc[data-code="{code}"] .mc-quiz').nth(context["quiz"]).locator('[data-ok="1"]').first.click(position={"x": 5, "y": 5})
    await click_text_trigger(trigger)
    await page.locator('.mc-dlg[open]').wait_for()
    return trigger


async def quiz_checks(page, code, viewport):
    quizzes = page.locator(f'.mc[data-code="{code}"] .mc-quiz')
    results = []
    for index in range(await quizzes.count()):
        quiz = quizzes.nth(index)
        context = await quiz.evaluate("el=>({panel:el.closest('.mc-panel')?.id,science:el.closest('.mc-sci')?.id})")
        if context.get("panel"):
            await page.locator(f'.mc-tabs button[data-p="{context["panel"]}"]').click()
        if context.get("science"):
            await page.locator(f'.mc-sci-bar button[data-s="{context["science"]}"]').click()
        answers = quiz.locator('[data-ok="1"]')
        check(f"{viewport}/{code}/quiz{index}: correct answer present", await answers.count() > 0)
        if not await answers.count():
            continue
        wrong = quiz.locator('[data-ok="0"]')
        if await wrong.count():
            await wrong.first.click(position={"x": 5, "y": 5})
            check(f"{viewport}/{code}/quiz{index}: incorrect answer feedback", await quiz.locator('.mc-fb').is_visible())
        await answers.first.click(position={"x": 5, "y": 5})
        visible = await quiz.locator('.mc-fb').is_visible()
        check(f"{viewport}/{code}/quiz{index}: correct answer feedback", visible)
        results.append({"index": index, "context": context, "feedback_visible": visible})
    return results


async def course_probe(page, code, name, output):
    await page.goto(ARGS.url.split("#")[0] + "#/entry/" + code)
    await page.wait_for_function("window.MDN_READY===true")
    await page.locator(f'.mc[data-code="{code}"]').wait_for()
    if await page.locator('.mc.book').count():
        await page.locator('.mc-book').click()
    await page.evaluate("document.fonts.ready")
    result = {"tabs": [], "science_tabs": [], "windows": [], "quizzes": []}
    check(f"{name}/{code}: work title", (await page.title()).endswith("Version de travail"))
    check(f"{name}/{code}: Atkinson default", await page.locator('.mc-font').input_value() == ATKINSON)
    await page.locator('.mc-tabs button[data-p="pA"]').click()
    font = await actual_font(page, '.mc-panel:not([hidden]) p')
    result["actual_font"] = font
    check(f"{name}/{code}: genuine embedded Atkinson glyphs", any("Atkinson" in item["familyName"] and item["isCustomFont"] and item["glyphCount"] > 0 for item in font), font)
    text_contrast = await contrast(page, '.mc-panel:not([hidden]) p')
    result["text_contrast"] = text_contrast
    check(f"{name}/{code}: course text contrast", text_contrast["ratio"] >= 4.5, text_contrast)
    for panel in ("pA", "pE", "pS", "pP"):
        await page.locator(f'.mc-tabs button[data-p="{panel}"]').click()
        state = await page.locator(f'.mc-panel[id="{panel}"]').evaluate("el=>({hidden:el.hidden,length:el.innerText.length})")
        check(f"{name}/{code}: tab {panel}", not state["hidden"] and state["length"] > 20, state)
        await overflow(page, f"{name}/{code}/{panel}")
        result["tabs"].append(panel)
    await page.locator('.mc-tabs button[data-p="pS"]').click()
    sciences = await page.locator('.mc-sci-bar button[data-s]').evaluate_all("els=>els.map(el=>({id:el.dataset.s,title:el.textContent}))")
    check(f"{name}/{code}: declared science tabs", len(sciences) == 6 if code == "B24" else len(sciences) > 0, sciences)
    for science in sciences:
        await page.locator(f'.mc-sci-bar button[data-s="{science["id"]}"]').click()
        visible = await page.locator(f'.mc-sci[id="{science["id"]}"]').evaluate("el=>!el.hidden&&el.innerText.length>20")
        check(f"{name}/{code}: science {science['id']}", visible)
        await overflow(page, f"{name}/{code}/{science['id']}")
        result["science_tabs"].append(science)
    await page.screenshot(path=str(output / f"{name}-{code}-science.png"))
    result["quizzes"] = await quiz_checks(page, code, name)
    inventory = await page.evaluate(r"""code=>{
      const norm=s=>s.replace(/\u00ad/g,'').replace(/\s+/g,' ').trim();
      const content=root=>{const copy=root.cloneNode(true);copy.querySelectorAll('.mc-ratio').forEach(x=>x.remove());return norm(copy.textContent)};
      return {templates:[...document.querySelectorAll('template[data-pop]')].map(t=>({key:t.dataset.pop,title:norm(t.dataset.title||''),
       text:content(t.content),children:[...t.content.querySelectorAll('[data-k]')].map(el=>el.dataset.k)})),
       direct:[...document.querySelectorAll('.mc[data-code="'+code+'"] [data-k]')].map((el,index)=>({index,key:el.dataset.k})),
       glossary:JSON.parse(document.querySelector('#medina-glossary').textContent),
       anchors:[...document.querySelectorAll('.mc[data-code="'+code+'"] a[href^="#"]')].map(a=>({href:a.getAttribute('href'),
        found:a.getAttribute('href').startsWith('#/')||!!document.getElementById(a.getAttribute('href').slice(1))}))};
    }""", code)
    if ARGS.sources and code == "B24":
        internal_glossary = internal_glossary_definitions(ARGS.sources / "glossary/b24.py")
        for term in ("VIH", "CD8", "ARN", "ADN", "CD3", "CD4"):
            expected, actual = internal_glossary.get(term), inventory["glossary"].get(term)
            check(f"{name}/{code}: internal glossary definition {term} prevails", bool(expected) and bool(actual) and
                  actual.get("full") == expected.get("full") and actual.get("def") == expected.get("def"), actual)
            if actual:
                check(f"{name}/{code}: no foreign specialty message in {term}", not re.search(r"myocardite|transthyr|anticoagulants? oraux? directs?|\bAOD\b", actual.get("def", ""), re.I), actual.get("def"))
    check(f"{name}/{code}: internal anchors resolve", all(row["found"] for row in inventory["anchors"]), [row for row in inventory["anchors"] if not row["found"]])
    templates = {row["key"]: row for row in inventory["templates"]}
    paths, queue = {}, deque()
    for trigger in inventory["direct"]:
        if trigger["key"] not in paths:
            paths[trigger["key"]] = {"index": trigger["index"], "children": []}
            queue.append(trigger["key"])
    while queue:
        key = queue.popleft()
        for child in templates.get(key, {}).get("children", []):
            if child not in paths:
                paths[child] = {"index": paths[key]["index"], "children": paths[key]["children"] + [child]}
                queue.append(child)
    owned = {key for key in templates if code.lower() in key.lower()}
    orphaned = sorted(owned - paths.keys())
    result["orphan_windows"] = orphaned
    check(f"{name}/{code}: every authored popup reachable", not orphaned, orphaned)
    for key, path in paths.items():
        if key not in templates:
            check(f"{name}/{code}: popup exists {key}", False)
            continue
        label = f"{name}/{code}/popup/{key}"
        try:
            trigger = await reveal(page, code, path["index"])
            for child in path["children"]:
                await click_text_trigger(page.locator(f'.mc-dlg[open] [data-k="{child}"]').first)
            state = await page.locator('.mc-dlg[open]').evaluate("""el=>{const clone=el.querySelector('.mc-dlg-b').cloneNode(true);
              clone.querySelectorAll('.mc-ratio').forEach(x=>x.remove());return {title:el.querySelector('#mc-dlg-t').textContent,
              text:clone.textContent,visible:el.querySelector('.mc-dlg-b').innerText}}""")
            check(label + ": expected title", NORMAL(state["title"]) == templates[key]["title"], state["title"])
            check(label + ": full authored content", NORMAL(state["text"]) == templates[key]["text"], {"expected_length": len(templates[key]["text"]), "actual_length": len(NORMAL(state["text"]))})
            check(label + ": visible explanation", len(NORMAL(state["visible"])) > 20 and "Fiche absente." not in state["visible"])
            if not result["windows"]:
                popup_font = await actual_font(page, '.mc-dlg[open] .mc-dlg-b')
                result["actual_popup_font"] = popup_font
                check(label + ": embedded Atkinson popup glyphs", any("Atkinson" in item["familyName"] and item["isCustomFont"] and item["glyphCount"] > 0 for item in popup_font), popup_font)
            await overflow(page, label, dialog=True)
            for qi in range(await page.locator('.mc-dlg[open] .mc-quiz').count()):
                quiz = page.locator('.mc-dlg[open] .mc-quiz').nth(qi)
                correct = quiz.locator('[data-ok="1"]')
                if await correct.count():
                    await correct.first.click(position={"x": 5, "y": 5})
                    check(label + f": popup quiz {qi}", await quiz.locator('.mc-fb').is_visible())
            if key.startswith("pareto-"):
                check(label + ": Pareto accessible", "Pareto" in state["title"] or len(state["visible"]) > 20)
            await page.keyboard.press("Escape")
            await page.locator('.mc-dlg').wait_for(state="hidden")
            await page.wait_for_function("el=>document.activeElement===el", arg=await trigger.element_handle())
            check(label + ": Escape and focus", await page.locator('.mc-dlg[open]').count() == 0 and await trigger.evaluate("el=>document.activeElement===el"))
            result["windows"].append({"key": key, "nested_steps": len(path["children"]), "title": NORMAL(state["title"]), "chars": len(NORMAL(state["text"]))})
        except Exception as error:
            check(label + ": native interaction", False, str(error))
            await page.keyboard.press("Escape")
    await page.locator('.mc-tabs button[data-p="pA"]').click()
    await page.evaluate("scrollTo(0,0)")
    await page.locator('.mc-size-toggle').click()
    await page.locator('.mc-size-range').evaluate("el=>el.value=24")
    await page.locator('.mc-size-range').dispatch_event("input")
    check(f"{name}/{code}: reader size applied", await page.locator('.mc').evaluate("el=>el.style.getPropertyValue('--mc-fs')") == "24px")
    await page.keyboard.press("Escape")
    await overflow(page, f"{name}/{code}/24px")
    await page.locator('.mc-font').select_option("Georgia,'Times New Roman',serif")
    check(f"{name}/{code}: reader font preference applied", (await page.locator('.mc-panel:not([hidden]) p').first.evaluate("el=>getComputedStyle(el).fontFamily")).startswith("Georgia"))
    check(f"{name}/{code}: Navigo follows font", (await page.locator('.mc-navigo-title').evaluate("el=>getComputedStyle(el).fontFamily")).startswith("Georgia"))
    await page.locator('.mc-font').select_option(ATKINSON)
    await page.locator('.mc-size-toggle').click()
    await page.locator('.mc-size-reset').click()
    await page.keyboard.press("Escape")
    drawer = page.locator('.mc-navigo-panel')
    if not await drawer.is_visible():
        await page.locator('.mc-navigo-trigger').click()
    check(f"{name}/{code}: Navigo visible", await drawer.is_visible())
    nav = await page.locator('.mc-navigo-panel').evaluate("el=>({rect:el.getBoundingClientRect().toJSON(),items:el.querySelectorAll('.mc-navigo-item').length})")
    check(f"{name}/{code}: Navigo usable", nav["items"] > 0 and nav["rect"]["x"] >= -1 and nav["rect"]["right"] <= page.viewport_size["width"] + 1, nav)
    if await page.locator('.mc-navigo-close').is_visible():
        await page.locator('.mc-navigo-close').click()
    await page.evaluate("scrollTo(0,0)")
    await page.screenshot(path=str(output / f"{name}-{code}-reader.png"))
    result["navigo"] = nav
    return result


async def main():
    ARGS.output.mkdir(parents=True, exist_ok=True)
    input_before = {path.relative_to(ARGS.sources).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in ARGS.sources.rglob("*") if path.is_file()} if ARGS.sources else {}
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(executable_path=str(ARGS.browser_executable) if ARGS.browser_executable else None,
                                                   headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        REPORT["browser"] = browser.version
        for name, viewport in (("desktop", {"width": 1440, "height": 1050}), ("mobile", {"width": 390, "height": 844})):
            context = await browser.new_context(viewport=viewport, color_scheme="dark", reduced_motion="reduce")
            await context.add_init_script("localStorage.setItem('medora.atlas.v3',JSON.stringify({theme:'night'}));localStorage.setItem('medina.theme','dark')")
            requests, errors = [], []
            origin = urlparse(ARGS.url).netloc
            async def restrict(route):
                if urlparse(route.request.url).netloc == origin or route.request.url.startswith("data:"):
                    await route.continue_()
                else:
                    requests.append(route.request.url)
                    await route.abort()
            await context.route("**/*", restrict)
            page = await context.new_page()
            page.set_default_timeout(7000)
            page.on("pageerror", lambda error: errors.append(str(error)))
            await page.goto(ARGS.url.split("#")[0] + "#/home")
            await page.wait_for_function("window.MDN_READY===true&&window.MEDINA_WORK_PREVIEW")
            await page.evaluate("document.fonts.ready")
            home = await page.evaluate("""() => ({work:window.MEDINA_WORK_PREVIEW,complete:window.MEDINA_COMPLETE,
              data:JSON.parse(document.querySelector('#medora-data').textContent),organisation:window.MEDINA_CATEGORY_ORGANISATION,
              courses:[...document.querySelectorAll('template[id^="ch-"]')].map(x=>x.id.slice(3)),
              featured_codes:[...document.querySelectorAll('.mcg-featured-grid .mcg-code')].map(x=>x.textContent.trim()),
              scheme:getComputedStyle(document.documentElement).colorScheme,bg:getComputedStyle(document.body).backgroundColor,
              banner:document.querySelector('#medina-work-preview-banner').getBoundingClientRect().toJSON(),
              title:document.title})""")
            check(name + ": exact work chapter codes", home["work"]["chapter_codes"] == ARGS.codes, home["work"]["chapter_codes"])
            if ARGS.sources:
                declared = {row["path"]: row["sha256"] for row in home["work"]["source_files"]}
                check(name + ": compiled source fingerprints match current draft", declared == input_before,
                      {"compiled_files": len(declared), "current_files": len(input_before)})
            check(name + ": no final certification", home["complete"] == [] and all(home["work"].get(flag) is False for flag in ("fragment_complete", "final_validation", "external_audit", "canonical_injection")))
            check(name + ": exclusive T1 catalogue", home["data"]["fragment"]["id"] == "T1" and len(home["data"]["specialties"]) == 1 and len(home["data"]["entries"]) == 184, len(home["data"]["entries"]))
            check(name + ": no foreign mounted course", sorted(home["courses"]) == sorted(ARGS.codes), home["courses"])
            check(name + ": every work course has a home card", sorted(home["featured_codes"]) == sorted(ARGS.codes), home["featured_codes"])
            check(name + ": light under dark OS and saved night", "light" in home["scheme"] and "dark" not in home["scheme"] and home["bg"] == "rgb(238, 240, 243)", {"scheme": home["scheme"], "bg": home["bg"]})
            check(name + ": visible banner", home["banner"]["x"] >= -1 and home["banner"]["right"] <= viewport["width"] + 1 and home["banner"]["top"] >= -1 and home["banner"]["bottom"] <= viewport["height"], home["banner"])
            await overflow(page, name + "/home")
            await page.screenshot(path=str(ARGS.output / f"{name}-home.png"))
            section = {"home": {key: value for key, value in home.items() if key not in ("data", "organisation")}, "courses": {}}
            for code in ARGS.codes:
                try:
                    section["courses"][code] = await course_probe(page, code, name, ARGS.output)
                    print(f"{name}/{code}: {len(section['courses'][code]['windows'])} native popup paths checked", flush=True)
                except Exception as error:
                    check(name + "/" + code + ": course probe", False, str(error))
            check(name + ": zero JS errors", not errors, errors)
            check(name + ": no external asset request", not requests, requests)
            section.update(page_errors=errors, external_requests=requests)
            REPORT["viewports"][name] = section
            await context.close()
        await browser.close()
    input_after = {path: hashlib.sha256((ARGS.sources / path).read_bytes()).hexdigest() for path in input_before}
    check("Draft source bytes unchanged by browser probe", input_before == input_after)
    REPORT["sources_checked"] = len(input_before)
    REPORT["result"] = "passed" if not REPORT["failures"] else "failed"
    (ARGS.output / "browser-proof.json").write_text(json.dumps(REPORT, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": REPORT["result"], "checks": len(REPORT["checks"]), "failures": REPORT["failures"]}, ensure_ascii=False), flush=True)
    return 0 if not REPORT["failures"] else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--codes", nargs="+")
    parser.add_argument("--output", type=Path, default=Path("work/fragment-preview-browser"))
    parser.add_argument("--sources", type=Path)
    parser.add_argument("--browser-executable", type=Path, help="Explicit browser binary; otherwise use Playwright’s installed Chromium")
    ARGS = parser.parse_args()
    if ARGS.codes is None:
        ARGS.codes = json.loads((ARGS.sources.parent / "manifest_interne.json").read_text())["chapter_codes"] if ARGS.sources else ["A41", "B24"]
    try:
        status = asyncio.run(main())
    except Exception as error:
        REPORT["result"] = "failed"
        REPORT["failures"].append({"label": "Browser probe could not complete", "detail": str(error)})
        ARGS.output.mkdir(parents=True, exist_ok=True)
        (ARGS.output / "browser-proof.json").write_text(json.dumps(REPORT, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(str(error), file=sys.stderr)
        status = 1
    sys.exit(status)
