"""Garde des cycles Betta (31+), instruction de Vial du 14 octobre 2026."""
import hashlib, json

PLAN = "organisation/progression/plan-betta-cycles.json"
STATUS = "organisation/betta_status.json"
TETRADE = "organisation/plan_tetrade_30_cycles.json"


class BettaError(ValueError):
    pass


def _req(cond, msg):
    if not cond:
        raise BettaError("Betta : " + msg)


def _json(tree, path):
    raw = tree.read(path, required=False)
    return json.loads(raw.decode("utf-8")) if raw else None


def managed(path, codes):
    return any(path.startswith(f"chapters/{c}/") or path == f"glossary/{c.lower()}.py" for c in codes)


def validate(before, after):
    plan, status = _json(after, PLAN), _json(after, STATUS)
    if plan is None or status is None:
        return {}, set()
    codes = {l["code"]: c["number"] for c in plan["cycles"] for a in c["agents"] for l in a["lessons"]}
    tetrade = _json(after, TETRADE)
    if tetrade:
        _req(not set(codes) & {ch[0] for s in tetrade["systems"] for ch in s["chapters"]}, "code commun aux 30 cycles")
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    authorized, injected = {}, set()
    for n, cyc in status["cycles"].items():
        for code, st in cyc["lessons"].items():
            _req(codes.get(code) == int(n), f"{code} hors plan")
            if isinstance(st, dict) and st.get("state") == "INJECTE":
                injected.add(code)
                for p, sha in st["canonical"].items():
                    _req(managed(p, {code}), f"{p} hors périmètre")
                    authorized[p] = sha
    for p in changed:
        if managed(p, codes):
            data = after.read(p, required=False)
            _req(data is not None and authorized.get(p) == hashlib.sha256(data).hexdigest(), f"fichier non enregistré : {p}")
    for row in json.loads(after.read("chapters.json").decode("utf-8")):
        if row.get("code") in codes:
            _req(row["code"] in injected and row.get("integrated") is True and row.get("covers") == [row["code"]] and
                 row.get("production_cycle") == codes[row["code"]] and row.get("betta") is True and
                 row.get("audit_status") == "audit_differe_non_effectue", f"ligne invalide : {row['code']}")
    return authorized, injected
