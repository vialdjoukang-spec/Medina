"""Garde des cycles Betta (31+), instruction de Vial du 14 octobre 2026."""
import hashlib, json, re

PLAN = "organisation/progression/plan-betta-cycles.json"
STATUS = "organisation/betta_status.json"
TETRADE = "organisation/plan_tetrade_30_cycles.json"
NOVO_PLAN = "organisation/progression/plan-novo12.json"
NOVO_STATUS = "organisation/novo12_status.json"


class BettaError(ValueError):
    pass


def _req(cond, msg):
    if not cond:
        raise BettaError("Betta : " + msg)


def _json(tree, path):
    raw = tree.read(path, required=False)
    try:
        return json.loads(raw.decode("utf-8")) if raw else None
    except (ValueError, UnicodeError):
        raise BettaError("Betta : JSON illisible : " + path) from None


def managed(path, codes):
    return any(path.startswith(f"chapters/{c}/") or path == f"glossary/{c.lower()}.py" for c in codes)


def _state(value):
    return value.get("state") if isinstance(value, dict) else value


def _transferred(before, after, novo_codes):
    """Keep archived Betta identities, but never authorise their moved missions."""
    status = _json(after, STATUS) or {"cycles": {}}
    previous = (_json(before, STATUS) or {"cycles": {}})["cycles"]
    moved = set()
    for n, cycle in status["cycles"].items():
        if cycle.get("state") != "TRANSFERE_NOVO12":
            continue
        for code, row in cycle["lessons"].items():
            old = previous.get(n, {}).get("lessons", {}).get(code)
            _req(_state(row) != "INJECTE" and _state(old) != "INJECTE",
                 f"{code} : transfert d'une leçon injectée interdit")
            _req(code in novo_codes, f"{code} : transfert sans mission Novo_12")
            moved.add(code)
    return moved


def _legacy(before, after, moved):
    """Historical Betta contract, except explicit non-injected transfers."""
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
            if code in moved:
                continue
            if isinstance(st, dict) and st.get("state") == "INJECTE":
                injected.add(code)
                for p, sha in st["canonical"].items():
                    _req(managed(p, {code}), f"{p} hors périmètre")
                    authorized[p] = sha
    for p in changed:
        if managed(p, set(codes) - moved):
            data = after.read(p, required=False)
            _req(data is not None and authorized.get(p) == hashlib.sha256(data).hexdigest(), f"fichier non enregistré : {p}")
    for row in json.loads(after.read("chapters.json").decode("utf-8")):
        if row.get("code") in set(codes) - moved:
            _req(row["code"] in injected and row.get("integrated") is True and row.get("covers") == [row["code"]] and
                 row.get("production_cycle") == codes[row["code"]] and row.get("betta") is True and
                 row.get("audit_status") == "audit_differe_non_effectue", f"ligne invalide : {row['code']}")
    return authorized, injected


def _novo_missions(plan, status):
    """Use the declared list verbatim: no invented redistribution to four agents."""
    _req(isinstance(plan, dict) and plan.get("id") == "novo12" and isinstance(plan.get("cycles"), list),
         "plan Novo_12 non reconnu")
    _req(isinstance(status, dict) and status.get("plan") == NOVO_PLAN and isinstance(status.get("cycles"), dict),
         "registre Novo_12 non reconnu")
    missions, groups = {}, {}
    for cycle in plan["cycles"]:
        n = cycle.get("number")
        _req(type(n) is int and n >= 42 and n not in groups and isinstance(cycle.get("agents"), list),
             "cycle Novo_12 invalide ou dupliqué")
        codes = []
        for agent in cycle["agents"]:
            _req(isinstance(agent.get("lessons"), list), "missions Novo_12 absentes")
            for lesson in agent["lessons"]:
                code = lesson.get("code")
                _req(isinstance(code, str) and re.fullmatch(r"[A-Z][0-9]{2}", code) and code not in missions,
                     "code Novo_12 invalide ou dupliqué")
                _req(lesson.get("fragment") == agent.get("fragment") and lesson.get("label") == agent.get("label") and
                     isinstance(lesson.get("title"), str) and lesson["title"].strip() and
                     isinstance(agent.get("fragment"), str) and agent["fragment"].strip() and
                     isinstance(agent.get("label"), str) and agent["label"].strip() and "/" not in agent["label"] and
                     "\\" not in agent["label"] and not any(c in agent["label"] for c in "\n\r\x00") and
                     agent["label"] not in {".", ".."},
                     f"{code} : fragment, libellé ou intitulé incohérent")
                missions[code] = (n, lesson)
                codes.append(code)
        _req(codes and cycle.get("lessons") == len(codes), "effectif Novo_12 différent de la liste déclarée")
        groups[n] = codes
    numbers = list(groups)
    _req(numbers and numbers == list(range(plan.get("first", 0), plan.get("last", -1) + 1)) and
         plan.get("total_lessons") == len(missions), "numérotation ou total Novo_12 incohérent")
    _req(set(status["cycles"]) == {str(n) for n in groups}, "cycles du registre Novo_12 différents du plan")
    for n, codes in groups.items():
        cycle = status["cycles"][str(n)]
        _req(isinstance(cycle, dict) and isinstance(cycle.get("lessons"), dict) and set(cycle["lessons"]) == set(codes),
             f"C{n} : leçons du registre Novo_12 différentes du plan")
        _req(cycle.get('state') in {'A_FAIRE', 'EN_COURS', 'LIVRE', 'INJECTE'}, f"C{n} : état de cycle Novo_12 inconnu")
        for code, row in cycle["lessons"].items():
            _req(_state(row) in {"A_FAIRE", "EN_COURS", "LIVRE", "INJECTE"}, f"{code} : état Novo_12 inconnu")
            _req(_state(row) not in {"LIVRE", "INJECTE"} or isinstance(row, dict), f"{code} : preuve Novo_12 absente")
        _req((cycle.get('state') == 'INJECTE') == all(_state(row) == 'INJECTE' for row in cycle['lessons'].values()),
             f"C{n} : état INJECTE du cycle différent de ses leçons")
    return missions, groups


def _read(tree, path):
    raw = tree.read(path, required=False)
    _req(raw is not None, "source ou preuve absente : " + path)
    entry = tree.entries.get(path)
    _req(entry and entry[0] in {"100644", "100755"}, "source non régulière : " + path)
    return raw


def _novo_sources(tree, code, n, lesson, row, sealed=False):
    directory = row.get('dir') if sealed else f"livraisons/Livraison Claude/{lesson['label']}/novo12/CYCLE_{n}_{code}"
    prefix, suffix = 'livraisons/Livraison Claude/', f'/novo12/CYCLE_{n}_{code}'
    _req(isinstance(directory, str) and directory.startswith(prefix) and directory.endswith(suffix),
         f"{code} : dossier Novo_12 hors mission")
    label = directory[len(prefix):-len(suffix)]
    _req(label and '/' not in label and '\\' not in label and label not in {'.', '..'} and
         not any(c in label for c in '\n\r\x00') and row.get('dir') == directory, f"{code} : dossier Novo_12 hors mission")
    files = row.get("files")
    _req(isinstance(files, dict) and files, f"{code} : manifeste des sources absent")
    minimum = {f"chapters/{code}/{code}_{s}.html" for s in ("a", "b", "c", "d", "pop1", "pop2")}
    minimum |= {f"glossary/{code.lower()}.py", "rapport.md", "recherche.md", "sources.json"}
    _req({directory + "/" + p for p in minimum}.issubset(files), f"{code} : manifeste incomplet")
    actual = {p for p in tree.entries if p.startswith(directory + "/")}
    _req(set(files) == actual, f"{code} : sources et manifeste différents")
    for path, sha in files.items():
        _req(path.startswith(directory + "/") and ".." not in path.split("/") and "\\" not in path and
             isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha), f"{code} : chemin ou empreinte invalide")
        _req(hashlib.sha256(_read(tree, path)).hexdigest() == sha, f"{code} : source différente du manifeste : {path}")
    canonical = {path[len(directory) + 1:]: sha for path, sha in files.items()
                 if managed(path[len(directory) + 1:], {code})}
    _req(row.get("canonical") == canonical, f"{code} : manifeste canonique absent ou différent des sources")
    for path, sha in canonical.items():
        _req(hashlib.sha256(_read(tree, path)).hexdigest() == sha, f"{code} : injection différente des sources : {path}")
    try:
        from tools.betta_verite import controler_contenu
    except ModuleNotFoundError:
        from betta_verite import controler_contenu
    sources = _json(tree, directory + "/sources.json")
    _req(isinstance(sources, dict), f"{code} : registre des sources invalide")
    try:
        errors = controler_contenu(_read(tree, directory + "/recherche.md").decode("utf-8"), sources.get("sources"), code)
    except (TypeError, UnicodeError, AttributeError):
        raise BettaError(f"Betta : {code} : recherche ou sources mal formées") from None
    _req(not errors, f"{code} : porte de vérité : " + "; ".join(errors))
    return canonical


def _novo(before, after, plan, status, missions, groups):
    previous = _json(before, NOVO_STATUS)
    old_missions = _novo_missions(_json(before, NOVO_PLAN), previous)[0] if previous is not None else {}
    old_cycles = previous.get("cycles", {}) if previous else {}
    catalog = _json(after, "chapters.json")
    original = _json(before, "chapters.json") or []
    _req(isinstance(catalog, list) and all(isinstance(r, dict) for r in catalog), "catalogue invalide")
    old_codes = {r.get("code") for r in original} | {c for r in original for c in r.get("covers", [])}
    injected, authorized, fresh = set(), {}, {}
    for n, cycle in old_cycles.items():
        for code, prior in cycle['lessons'].items():
            if _state(prior) == 'INJECTE':
                _req(code in missions and code in old_missions and
                     (missions[code][0], missions[code][1]['fragment']) ==
                     (old_missions[code][0], old_missions[code][1]['fragment']),
                     f"{code} : attribution d'une leçon injectée modifiée")
    for code, (n, lesson) in missions.items():
        row = status["cycles"][str(n)]["lessons"][code]
        prior = old_cycles.get(str(n), {}).get("lessons", {}).get(code)
        if _state(prior) == "INJECTE":
            _req(row == prior, f"{code} : preuve d'injection historique réécrite")
            for path in prior["canonical"]:
                _req(before.read(path, required=False) == after.read(path, required=False), f"{code} : cours injecté modifié")
        if _state(row) != "INJECTE":
            continue
        canonical = _novo_sources(after, code, n, lesson, row, sealed=_state(prior) == 'INJECTE')
        if _state(prior) != "INJECTE":
            _req(previous is not None, "activation Novo_12 et injection simultanées interdites")
            _req(code not in old_codes and all(before.read(p, required=False) is None for p in canonical),
                 f"{code} : cours existant ou couvert, remplacement interdit")
            fresh[code] = n
        injected.add(code)
        authorized.update(canonical)
        entries = [r for r in catalog if r.get("code") == code]
        _req(len(entries) == 1, f"{code} : ligne catalogue absente ou dupliquée")
        entry = entries[0]
        if _state(prior) == 'INJECTE':
            _req([entry] == [r for r in original if r.get('code') == code], f"{code} : catalogue injecté réécrit")
        _req(entry.get("integrated") is True and entry.get("covers") == [code] and entry.get("production_cycle") == n and
             entry.get("novo12") is True and not entry.get("betta") and entry.get("owner") == lesson["fragment"] and
             (_state(prior) == 'INJECTE' or entry.get("title") == lesson["title"]) and entry.get("provisional_injection") is True and
             entry.get("audit_status") == "audit_differe_non_effectue", f"{code} : ligne catalogue Novo_12 invalide")
    _req(all(r.get("code") not in missions or r.get("code") in injected for r in catalog),
         "catalogue Novo_12 sans injection enregistrée")
    if fresh:
        identity = lambda data: {code: (number, lesson['fragment']) for code, (number, lesson) in data.items()}
        _req(identity(missions) == identity(old_missions), "affectations Novo_12 modifiées pendant l'injection")
        numbers = set(fresh.values())
        _req(len(numbers) == 1, "plusieurs cycles Novo_12 injectés simultanément")
        n = next(iter(numbers))
        _req(set(fresh) == set(groups[n]), "cycle Novo_12 partiellement injecté : utiliser la liste déclarée entière")
        _req(all(_state(status["cycles"][str(k)]["lessons"][c]) == "INJECTE" for k in groups if k < n for c in groups[k]),
             "injection Novo_12 avant les cycles précédents")
        _req(all(r in catalog for r in original) and len(catalog) == len(original) + len(fresh),
             "catalogue historique modifié pendant l'injection Novo_12")
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    for path in changed:
        if managed(path, missions):
            _req(path in authorized and hashlib.sha256(_read(after, path)).hexdigest() == authorized[path],
                 "fichier Novo_12 non enregistré : " + path)
    return authorized, injected


def validate(before, after):
    """Separate Novo42+ from both historical Betta31+ and the tetrad1–30."""
    plan, status = _json(after, NOVO_PLAN), _json(after, NOVO_STATUS)
    prior_plan, prior_status = _json(before, NOVO_PLAN), _json(before, NOVO_STATUS)
    _req((plan is None) == (status is None), "plan ou registre Novo_12 absent")
    _req(prior_plan is None or plan is not None, "suppression du plan Novo_12 interdite")
    _req(prior_status is None or status is not None, "suppression du registre Novo_12 interdite")
    missions, groups = _novo_missions(plan, status) if plan is not None else ({}, {})
    moved = _transferred(before, after, missions)
    legacy_plan = _json(after, PLAN)
    active_legacy = {l["code"] for c in (legacy_plan or {}).get("cycles", []) for a in c["agents"] for l in a["lessons"]} - moved
    _req(not active_legacy.intersection(missions), "code commun à Betta actif et Novo_12")
    tetrade = _json(after, TETRADE)
    _req(not missions or isinstance(tetrade, dict), "plan tétrade absent pour vérifier les exclusions Novo_12")
    if tetrade:
        _req(not set(missions).intersection(ch[0] for s in tetrade["systems"] for ch in s["chapters"]),
             "code Novo_12 commun aux 30 cycles")
    authorized, injected = _legacy(before, after, moved)
    if missions:
        novo_authorized, novo_injected = _novo(before, after, plan, status, missions, groups)
        _req(not set(authorized).intersection(novo_authorized), "autorisations Betta/Novo_12 contradictoires")
        authorized.update(novo_authorized)
        injected.update(novo_injected)
    return authorized, injected
