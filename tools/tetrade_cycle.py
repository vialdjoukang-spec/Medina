"""Garde du cycle explicitement autorisé, en complément des gardes historiques.

Les contrats structurés attestent des preuves de revue IA, jamais une validation
médicale. Le contenu des passages et leur applicabilité restent à auditer.
"""
import hashlib
import json
import re
from datetime import datetime

REGISTRY = "organisation/tetrade_cycle_status.json"
AUTHORITY = "docs/collaboration/instructions/CYCLE_01_EXECUTION_VIAL_2026-10-11.md"
PROTOCOL = "tetrade-chapitres-2026-10-11"
CLARITY_AUTHORITY = "docs/collaboration/instructions/CLARTE_BASES_CALCULS_VIAL_2026-10-11.md"
PROMPTS = ("PROMPT_MEDINA.md", "PROMPT_TRANSITION.md", "docs/STYLE_REDACTION.md", AUTHORITY, CLARITY_AUTHORITY)
MISSIONS = (
    ("I63", "S08", "NEUR", "HEM"), ("E11", "S05", "ENDO", "NEPH"),
    ("N17", "S04", "NEPH", "ENDO"), ("D50", "S06", "HEM", "NEUR"),
)
STATES = ("EN_PRODUCTION", "EN_AUDIT_CROISE", "EN_CONTRE_AUDIT", "EN_CONTROLE", "PRET_A_INJECTER", "INJECTE", "PUBLIE_VERIFIE")
DIMENSIONS = {"redaction", "medecine", "sources", "frontend"}


class CycleError(ValueError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise CycleError(message)


def read_json(tree, path, required=True):
    raw = tree.read(path, required=required)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except (ValueError, UnicodeError) as error:
        raise CycleError(f"JSON illisible : {path}") from error


def proof(tree, reference, description):
    require(isinstance(reference, dict), f"{description} : preuve absente")
    raw = tree.read(reference.get("path"))
    require(reference.get("sha256") == digest(raw), f"{description} : empreinte de preuve différente")
    try:
        return json.loads(raw)
    except ValueError as error:
        raise CycleError(f"{description} : preuve structurée requise") from error


def dated(value):
    try:
        date = datetime.fromisoformat(value)
        require(date.tzinfo is not None, "Date avec fuseau requise")
        return date
    except (ValueError, TypeError):
        raise CycleError("Date ISO avec fuseau requise") from None


def managed(path, codes):
    return any(path.startswith(f"chapters/{code}/") or path == f"glossary/{code.lower()}.py" for code in codes)


def records(tree):
    data = read_json(tree, REGISTRY, False)
    if data is None:
        return None
    require(data.get("schema_version") == 1 and data.get("protocol") == PROTOCOL,
            "Cycle : protocole ou schéma invalide")
    require(data.get("cycle") == 1 and data.get("authorized_cycles") == [1] and data.get("authority") == AUTHORITY,
            "Seul le cycle 1 est autorisé")
    require(data.get("coordinator") == "Codex — coordinateur du fil", "Coordinateur du cycle incorrect")
    tree.read(AUTHORITY)
    require(data.get("state") in {"ACTIF", "CLOTURE"}, "État du cycle invalide")
    chapters = data.get("chapters")
    require(isinstance(chapters, list) and len(chapters) == 4, "Quatre missions requises")
    for row, (code, fragment, tag, crossed) in zip(chapters, MISSIONS):
        require(isinstance(row, dict) and (row.get("code"), row.get("fragment_id")) == (code, fragment),
                "Identité ou ordre d'une mission modifié")
        expected = {"writer": f"C01-R-{tag}", "cross_reviewer": f"C01-R-{crossed}", "counter_reviewer": f"C01-CA-{tag}"}
        require(all(row.get(key) == value for key, value in expected.items()), f"{code} : agents ou indépendance invalides")
        require(row.get("status") in STATES, f"{code} : état invalide")
        for key in ("author", "cross_audit", "counter_audit", "control", "injection", "publication"):
            require(key in row and (row[key] is None or isinstance(row[key], dict)), f"{code} : champ {key} absent")
    return data


def source_files(tree, row, roots=("livraisons/Livraison Codex/",)):
    files = row.get("files")
    code = row["code"]
    require(isinstance(files, dict) and files, f"{code} : fichiers finaux absents")
    minimum = {f"chapters/{code}/{code}_{suffix}.html" for suffix in ("a", "b", "c", "d", "pop1", "pop2")} | {f"glossary/{code.lower()}.py"}
    require(minimum.issubset(files) and all(managed(path, [code]) for path in files), f"{code} : chapitre incomplet ou source étrangère")
    directory = row.get("source_dir")
    require(isinstance(directory, str) and directory.startswith(tuple(roots)) and ".." not in directory.split("/") and f"/CYCLE_{row.get('production_cycle', 1):02d}_{code}" in directory,
            f"{code} : dossier de livraison isolé requis")
    for path, sha in files.items():
        require(isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha), f"{code} : SHA-256 invalide")
        require(digest(tree.read(directory + "/" + path)) == sha, f"{code} : sources livrées différentes des empreintes")
    return files


def prompt_gate(tree, gate, actor, description, prompts=PROMPTS):
    require(isinstance(gate, dict) and gate.get("actor") == actor and gate.get("verdict") == "conforme",
            f"{description} : application du Prompt non conforme")
    require(gate.get("prompt_files") == {path: digest(tree.read(path)) for path in prompts},
            f"{description} : Prompt non relu dans sa version finale")
    dated(gate.get("checked_at"))
    checks = gate.get("checks")
    expected = {"autorisation", "perimetre_provenance", "sources_lues", "contexte_suisse", "independance", "contrat_cours", "honnetete"}
    require(isinstance(checks, list) and {c.get("id") for c in checks if isinstance(c, dict)} == expected,
            f"{description} : matrice d'application incomplète")
    for check in checks:
        require(check.get("status") == "conforme" and isinstance(check.get("evidence"), list) and check["evidence"],
                f"{description} : exigence non vérifiée {check.get('id')}")
        for item in check["evidence"]:
            require(isinstance(item, dict) and isinstance(item.get("explanation"), str) and item["explanation"].strip(),
                    f"{description} : explication d'application absente")
            require(digest(tree.read(item.get("path"))) == item.get("sha256"), f"{description} : preuve d'application invalide")


def review(tree, row, key, actor, files, prompts=PROMPTS):
    data = proof(tree, row[key], f"{row['code']} {key}")
    require(data.get("code") == row["code"] and data.get("actor") == actor and data.get("medical_human_validation") is False,
            f"{row['code']} : identité de {key} ou qualification incorrecte")
    prompt_gate(tree, data.get("entry"), actor, f"{row['code']} {key} entrée", prompts)
    prompt_gate(tree, data.get("exit"), actor, f"{row['code']} {key} sortie", prompts)
    if row["code"] == "N17":
        try:
            from n17_calcium_import import AUTHORITY as supplement, authority as import_authority
        except ModuleNotFoundError:
            from tools.n17_calcium_import import AUTHORITY as supplement, authority as import_authority
        if tree.read(supplement, required=False) is not None:
            expected = import_authority(tree)
            for name in ("entry", "exit"):
                require(data[name].get("supplemental_prompt_files") == {expected["path"]: expected["sha256"]},
                        f"N17 {key} : instruction ciblée du calcium non lue à {name}")
    require(dated(data["entry"]["checked_at"]) <= dated(data["exit"]["checked_at"]), "Sortie antérieure à l'entrée")
    require(data.get("final_files") == files and data.get("blocking_reserves") == [], f"{row['code']} {key} : réserves ou empreintes différentes")
    require(isinstance(data.get("runtime_agent_id"), str) and data["runtime_agent_id"], f"{row['code']} : agent réel non identifié")
    if key in {"cross_audit", "counter_audit"}:
        passes = data.get("passes")
        require(isinstance(passes, list) and len(passes) == 2 and [p.get("number") for p in passes] == [1, 2],
                f"{row['code']} {key} : deux passes distinctes requises")
        for passage in passes:
            report = proof(tree, passage.get("report"), f"{row['code']} {key} passe {passage['number']}")
            require(report.get("actor") == actor and report.get("code") == row["code"] and report.get("pass") == passage["number"],
                    "Passe : identité incorrecte")
            require(set(report.get("dimensions", {})) == DIMENSIONS and all(isinstance(v, str) and v.strip() for v in report["dimensions"].values()),
                    "Passe : les quatre dimensions exigent des observations")
            require(isinstance(report.get("numerical_checks"), list) and len(report["numerical_checks"]) >= 10,
                    "Passe : dix vérifications numériques primaires requises")
            require(len({c.get("claim") for c in report["numerical_checks"]}) >= 10,
                    "Passe : dix données distinctes requises")
            for check in report["numerical_checks"]:
                require(all(isinstance(check.get(field), str) and check[field].strip() for field in ("claim", "source", "section", "passage", "finding")),
                        "Passe : vérification numérique insuffisamment documentée")
            require(dated(report.get("started_at")) <= dated(report.get("finished_at")),
                    "Passe : fin antérieure au début")
            if passage["number"] == 2:
                require(report.get("verdict") == "favorable" and report.get("blocking_reserves") == [] and report.get("final_files") == files,
                        "Seconde passe : verdict ou fichiers finaux non conformes")
                require(report.get("score") == 20,
                        "Seconde passe : 20/20 requis par l'instruction de clarté")
        first = proof(tree, passes[0]["report"], "Passe1")
        second = proof(tree, passes[1]["report"], "Passe2")
        require(dated(first["finished_at"]) <= dated(second["started_at"]), "Les deux passes se chevauchent")
    return data


def capture_proof(tree, captures, minimum=None):
    """Default: exactly opening + explanation. With ``minimum``: that many distinct real captures."""
    if minimum is None:
        require(isinstance(captures, list) and [c.get("kind") for c in captures] == ["opening", "explanation"],
                "Deux captures réelles, ouverture et fenêtre, requises")
    else:
        require(isinstance(captures, list) and len(captures) >= minimum and all(isinstance(c, dict) for c in captures),
                f"{minimum} captures réelles à des endroits distincts requises")
        kinds = [c.get("kind") for c in captures]
        require(all(isinstance(k, str) and k.strip() for k in kinds) and len(set(kinds)) == len(kinds) and
                len({c.get("path") for c in captures}) == len(captures) and len({c.get("sha256") for c in captures}) == len(captures),
                f"{minimum} captures réelles à des endroits distincts requises")
    for capture in captures:
        raw = tree.read(capture.get("path"))
        require(raw.startswith(b"\x89PNG\r\n\x1a\n") and len(raw) > 5000 and digest(raw) == capture.get("sha256"),
                "Capture PNG absente, invalide ou différente")


def source_ledger_proof(tree, row, author, files):
    """Registre des sources réellement lues, attaché à la revue auteur."""
    ledger = proof(tree, author.get("source_ledger"), f"{row['code']} sources réellement lues")
    require(ledger.get("code") == row["code"] and ledger.get("final_files") == files and ledger.get("unverified_claims") == [],
            "Registre des sources : affirmations non vérifiées ou sources finales différentes")
    require(set(ledger.get("covered_files", [])) == set(files), "Registre des sources : toutes les surfaces du cours sont requises")
    require(isinstance(ledger.get("claims"), list) and ledger["claims"], "Registre des sources : aucune affirmation documentée")
    for claim in ledger["claims"]:
        require(isinstance(claim, dict) and all(isinstance(claim.get(field), str) and claim[field].strip() for field in
                    ("claim", "location", "source_url", "source_title", "version_date", "section", "source_passage_summary", "population", "limits", "accessed_on")),
                "Registre des sources : passage, population ou limites absents")
        require(claim["source_url"].startswith("https://") and re.fullmatch(r"[0-9a-f]{64}", claim.get("download_sha256", "")),
                "Registre des sources : URL ou empreinte du texte lu absente")
    return ledger


def technical_proof(tree, row, control, files, captures=None):
    """Contrôles techniques réels du coordinateur (bureau, mobile, fenêtres, JS, abréviations, captures)."""
    technical = proof(tree, control.get("technical_checks"), f"{row['code']} contrôles techniques")
    require(technical.get("final_files") == files and technical.get("result") == "passed" and
            technical.get("desktop") is True and technical.get("mobile") is True and
            technical.get("missing_windows") == [] and technical.get("javascript_errors") == [] and
            technical.get("uncovered_abbreviations") == [] and technical.get("horizontal_overflow") is False,
            "Contrôle final : tests ou rendu réels incomplets")
    capture_proof(tree, technical.get("captures"), captures)
    return technical


def ready(tree, row, rows=None, prompts=PROMPTS, cross_completed_at=None,
          control_actor="Codex — coordinateur du fil", captures=None, source_roots=None):
    files = source_files(tree, row) if source_roots is None else source_files(tree, row, source_roots)
    author = review(tree, row, "author", row["writer"], files, prompts)
    source_ledger_proof(tree, row, author, files)
    crossed = review(tree, row, "cross_audit", row["cross_reviewer"], files, prompts)
    counter = review(tree, row, "counter_audit", row["counter_reviewer"], files, prompts)
    control = review(tree, row, "control", control_actor, files, prompts)
    all_rows = rows if rows is not None else records(tree)["chapters"]
    last_crossed_exit = cross_completed_at or max(dated(proof(tree, r["cross_audit"], "Audit croisé du cycle")["exit"]["checked_at"]) for r in all_rows)
    last_counter_exit = max(dated(proof(tree, r["counter_audit"], "Contre-audit du cycle")["exit"]["checked_at"]) for r in all_rows)
    require(dated(counter["entry"]["checked_at"]) >= last_crossed_exit, "Contre-audit engagé avant clôture de tous les binômes")
    require(dated(control["entry"]["checked_at"]) >= last_counter_exit, "Contrôle engagé avant clôture des quatre contre-audits")
    technical_proof(tree, row, control, files, captures)
    require(len({x["runtime_agent_id"] for x in (author, crossed, counter, control)}) == 4, "Auteur, auditeurs et coordinateur doivent être distincts")
    require(counter.get("fresh_context") is True and (cross_completed_at or dated(crossed["exit"]["checked_at"])) <= dated(counter["entry"]["checked_at"]),
            "Contre-audit : contexte neuf et démarrage différé requis")
    require(dated(counter["exit"]["checked_at"]) <= dated(control["entry"]["checked_at"]), "Contrôle final prématuré")
    # Reuse the existing Swiss gate without weakening its historical scope.
    try:
        from espace import swiss_context_proof
    except ModuleNotFoundError:
        from tools.espace import swiss_context_proof
    swiss = control.get("swiss_context")
    swiss_context_proof(tree, {"swiss_context": swiss}, row["fragment_id"], files, scope="chapter", chapter_code=row["code"])
    return files


def validate_cycle_guard(before, after, authorized_catalog_codes=()):
    # Explicit bounded exception: keep the STOP receipt as history, publish
    # current sources and allow traced Claude corrections without a prior CA.
    if __package__ == "tools":
        from tools.cycle1_claude import validate as validate_claude_exception
    else:
        from cycle1_claude import validate as validate_claude_exception
    deferred = validate_claude_exception(before, after, authorized_catalog_codes=authorized_catalog_codes)
    if deferred is not None:
        return deferred
    # Latest explicit owner order: publish the four reviewed chapters now, then
    # STOP. Keep this bounded exception distinct from the completed audit chain.
    try:
        from cycle_stop import validate as validate_stop
    except ModuleNotFoundError:
        from tools.cycle_stop import validate as validate_stop
    stopped = validate_stop(before, after)
    if stopped is not None:
        return stopped
    old, new = records(before), records(after)
    if old is None and new is None:
        return {}, set()
    require(new is not None, "Suppression du registre de cycle interdite")
    codes = [row[0] for row in MISSIONS]
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    cycle_paths = {p for p in changed if managed(p, codes)}
    if old is None:
        require(not cycle_paths and "chapters.json" not in changed, "Activation : aucune injection simultanée autorisée")
        require(new["state"] == "ACTIF" and all(r["status"] == "EN_PRODUCTION" and all(r[k] is None for k in ("author", "cross_audit", "counter_audit", "control", "injection", "publication")) for r in new["chapters"]),
                "Activation : aucun audit ou injection préétabli")
        return {}, set(codes)
    for key in ("schema_version", "protocol", "cycle", "authorized_cycles", "authority", "coordinator"):
        require(old[key] == new[key], "Autorisation ou identité du cycle modifiée")
    require(before.read(AUTHORITY) == after.read(AUTHORITY), "Autorité du cycle modifiée pendant son exécution")
    try:
        from n17_calcium_import import AUTHORITY as supplement, authority as import_authority
    except ModuleNotFoundError:
        from tools.n17_calcium_import import AUTHORITY as supplement, authority as import_authority
    previous_supplement = before.read(supplement, required=False)
    next_supplement = after.read(supplement, required=False)
    if previous_supplement is not None:
        require(previous_supplement == next_supplement, "Instruction ciblée du calcium modifiée ou supprimée")
    if next_supplement is not None:
        import_authority(after)
    require(old["state"] != "CLOTURE" or old == new, "Cycle clôturé immuable")
    injected = []
    authorized = {}
    for previous, row in zip(old["chapters"], new["chapters"]):
        code = row["code"]
        require(STATES.index(row["status"]) >= STATES.index(previous["status"]), f"{code} : régression d'état non tracée interdite")
        if STATES.index(row["status"]) >= STATES.index("EN_AUDIT_CROISE"):
            require(all(r["author"] is not None for r in new["chapters"]), "Les quatre productions doivent précéder l'audit croisé")
        if STATES.index(row["status"]) >= STATES.index("EN_CONTRE_AUDIT"):
            require(all(r["cross_audit"] is not None for r in new["chapters"]), "Les quatre audits croisés doivent précéder les contre-audits")
        if STATES.index(row["status"]) >= STATES.index("EN_CONTROLE"):
            require(all(r["counter_audit"] is not None for r in new["chapters"]), "Les quatre contre-audits doivent précéder le contrôle")
        stage = STATES.index(row["status"])
        if 1 <= stage < STATES.index("PRET_A_INJECTER"):
            files = source_files(after, row)
            review(after, row, "author", row["writer"], files)
            if stage >= STATES.index("EN_CONTRE_AUDIT"):
                review(after, row, "cross_audit", row["cross_reviewer"], files)
            if stage >= STATES.index("EN_CONTROLE"):
                review(after, row, "counter_audit", row["counter_reviewer"], files)
        if STATES.index(previous["status"]) >= STATES.index("INJECTE"):
            require(all(row[k] == previous[k] for k in row if k not in {"status", "publication"}), f"{code} : sources ou audits injectés immuables")
            for path, sha in previous["files"].items():
                require(before.read(path) == after.read(path) and digest(after.read(path)) == sha, f"{code} : source injectée modifiée")
        if row["status"] in {"PRET_A_INJECTER", "INJECTE", "PUBLIE_VERIFIE"}:
            files = ready(after, row)
            if STATES.index(previous["status"]) < STATES.index("INJECTE") and row["status"] in {"INJECTE", "PUBLIE_VERIFIE"}:
                injected.append(row)
                require(previous["status"] == "PRET_A_INJECTER", f"{code} : contrôle préexistant avant injection requis")
                require(row["status"] == "INJECTE" and row["publication"] is None, "Publication distincte de l'injection requise")
                injection = proof(after, row["injection"], f"{code} injection")
                require(injection.get("code") == code and injection.get("files") == files and injection.get("injector") == new["coordinator"], "Reçu d'injection incorrect")
                for path, sha in files.items():
                    require(digest(after.read(path)) == sha, f"{code} : injection différente des fichiers audités")
                    authorized[path] = sha
        if row["status"] == "PUBLIE_VERIFIE":
            publication = proof(after, row["publication"], f"{code} publication")
            require(publication.get("code") == code and publication.get("deployment_status") == "success" and publication.get("readback") is True and publication.get("gauges") is True,
                    f"{code} : publication et relecture non établies")
            require(re.fullmatch(r"[0-9a-f]{40}", publication.get("main_sha", "")) and publication.get("public_url", "").startswith("https://vialdjoukang-spec.github.io/Medina/fragments/"), "Publication : SHA ou URL absent")
    require(len(injected) <= 1, "Un seul chapitre peut être injecté à la fois")
    if injected:
        row = injected[0]; index = codes.index(row["code"])
        require(all(p["status"] == "PUBLIE_VERIFIE" for p in old["chapters"][:index]), "Publication du chapitre précédent requise")
        require(all(p["status"] == "PRET_A_INJECTER" for p in old["chapters"][index:]), "Les quatre chapitres doivent être prêts après tous les audits")
        require(cycle_paths == set(authorized), "Injection : fichiers manquants, supplémentaires ou plusieurs chapitres")
        require("chapters.json" in changed, "Enregistrement du chapitre requis")
        original = read_json(before, "chapters.json"); registered = read_json(after, "chapters.json")
        additions = [r for r in registered if r not in original]
        require(len(registered) == len(original) + 1 and all(r in registered for r in original) and len(additions) == 1,
                "chapters.json : ajout unique, sans modification des entrées existantes")
        addition = additions[0]
        require(addition.get("code") == row["code"] and addition.get("covers") == [row["code"]] and addition.get("integrated") is True,
                "Enregistrement : un seul chapitre et une seule catégorie démontrée")
        authorized["chapters.json"] = digest(after.read("chapters.json"))
    else:
        require(not cycle_paths, "Source du cycle modifiée sans injection contrôlée")
        if "chapters.json" in changed:
            old_chapters = read_json(before, "chapters.json"); new_chapters = read_json(after, "chapters.json")
            require([r for r in old_chapters if r.get("code") in codes] == [r for r in new_chapters if r.get("code") in codes], "Entrée du cycle modifiée sans injection")
    if new["state"] == "CLOTURE":
        require(all(r["status"] == "PUBLIE_VERIFIE" for r in new["chapters"]), "Clôture avant quatre publications interdite")
        receipt = proof(after, new.get("closure"), "Clôture du cycle")
        require(receipt.get("blocking_reserves") == [] and receipt.get("next_cycle_authorized") is False, "Clôture : réserves ou cycle suivant non autorisé")
    return authorized, set(codes)
