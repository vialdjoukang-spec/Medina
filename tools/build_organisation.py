#!/usr/bin/env python3
"""Construit le tableau de bord autonome depuis les sources canoniques MEDINA."""
import argparse
import importlib.util
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
try:
    from .production_plan import load_plan
except ImportError:
    from production_plan import load_plan

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/vialdjoukang-spec/Medina"
ONLINE = "https://vialdjoukang-spec.github.io/Medina/"


def load_data(generated_at):
    registry = json.loads((ROOT / "organisation/fragments.json").read_text())
    fragments = json.loads((ROOT / "fragments.json").read_text())
    chapters = [c for c in json.loads((ROOT / "chapters.json").read_text()) if c.get("integrated")]
    spec = importlib.util.spec_from_file_location("organisation_fragment_surface", ROOT / "fragment_surface.py")
    surface = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(surface)
    catalogue, owner, _ = surface.frontend_catalog(ROOT)
    entries = catalogue["entries"]
    names = {f["id"]: f for f in registry}
    assert len(names) == len(fragments) == 23
    assert set(names) == {f["id"] for f in fragments}
    assert sorted(f["order"] for f in registry) == list(range(1, 24))
    by_code = {e["code"]: e for e in entries}
    assert set(owner) == set(by_code), "Catégories non rattachées"
    production, assignments = load_plan(ROOT, owner)
    fragment_by_id = {f["id"]: f for f in fragments}
    def fragment_url(ident):
        f = fragment_by_id[ident]
        return ONLINE + f"fragments/MEDINA_{ident}_{f['slug']}.html"
    course_by_code = {}
    for c in chapters:
        ident = owner[c["code"]]
        ref = {"code": c["code"], "title": c["title"], "url": fragment_url(ident) + "#/entry/" + c["code"],
               "fragment_label": names[ident]["label"], "fragment_id": ident}
        for code in c.get("covers", [c["code"]]):
            assert code not in course_by_code or course_by_code[code]["code"] == c["code"], code
            course_by_code[code] = ref
    result = []
    for n in registry:
        ident = n["id"]
        local = [e for e in entries if owner[e["code"]] == ident]
        priority = [x for x in n["priority_codes"] if x in by_code and owner[x] == ident]
        ordered = list(dict.fromkeys(priority + sorted(e["code"] for e in local)))
        ranks = {code: i + 1 for i, code in enumerate(ordered)}
        groups = defaultdict(list)
        for e in local:
            ref = course_by_code.get(e["code"])
            groups[(e["block"], e["blockTitle"])].append({
                "code": e["code"], "title": e["title"], "order": ranks[e["code"]],
                "status": "primary" if ref and ref["code"] == e["code"] else "covered" if ref else "planned",
                "course": ref,
            })
        folder = quote(n["label"], safe="")
        related = []
        for i, code in enumerate(n["priority_codes"], 1):
            if code in owner and owner[code] != ident:
                e = by_code[code]; other = owner[code]
                related.append({"code": code, "title": e["title"], "fragment_label": names[other]["label"],
                                "order": i, "status": "available" if code in course_by_code else "planned",
                                "url": "#fragment=" + other + "&block=" + quote(e["block"], safe="") + "&category=" + code})
        result.append({"id": ident, "label": n["label"], "specialty": n["specialty"], "order": n["order"],
                       "url": fragment_url(ident), "source_url": REPO + "/tree/main/livraisons/Livraison%20Codex/" + folder + "/sources",
                       "delivery_codex_url": REPO + "/tree/main/livraisons/Livraison%20Codex/" + folder,
                       "delivery_claude_url": REPO + "/tree/main/livraisons/Livraison%20Claude/" + folder,
                       "integrated_count": sum(owner[c["code"]] == ident for c in chapters),
                       "category_count": len(local), "related": related,
                       "production": assignments.get(ident),
                       "blocks": [{"code": b, "title": t, "categories": sorted(es, key=lambda e: e["order"])}
                                  for (b, t), es in sorted(groups.items())]})
    return {"generated_at": generated_at,
            "production": {"allocation": production["allocation"], "assignment_unit": production["assignment_unit"],
                           "agents": production["agents"], "rules": production["rules"]},
            "catalogue": {"version": "Catalogue historique MEDINA — CIM-10-GM 2024", "total_categories": len(entries),
                          "integrated_courses": len(chapters), "full_cim11": False},
            "links": {"online": ONLINE + "organisation.html", "repository": REPO,
                      "html": REPO + "/blob/main/organisation/MEDINA_Organisation.html",
                      "codex": REPO + "/tree/main/livraisons/Livraison%20Codex",
                      "claude": REPO + "/tree/main/livraisons/Livraison%20Claude",
                      "protocol": REPO + "/blob/main/docs/collaboration/DELIVERY_PROTOCOL.md"},
            "fragments": result}


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "organisation/MEDINA_Organisation.html")
    parser.add_argument("--data-output", type=Path)
    parser.add_argument("--generated-at", default=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    args = parser.parse_args()
    data = load_data(args.generated_at)
    template = (ROOT / "organisation/dashboard_template.html").read_text()
    assert template.count("__MEDINA_DATA__") == 1
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(template.replace("__MEDINA_DATA__", payload))
    if args.data_output:
        args.data_output.parent.mkdir(parents=True, exist_ok=True)
        args.data_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"{args.output}: {len(data['fragments'])} fragments, {data['catalogue']['total_categories']} catégories, {data['catalogue']['integrated_courses']} cours")


if __name__ == "__main__":
    main()
