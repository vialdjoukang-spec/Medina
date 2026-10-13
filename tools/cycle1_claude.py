"""Exception explicite du 13 octobre : publication du cycle 1, audit Claude différé.

Les preuves historiques restent figées. Les sources courantes sont consultables
et corrigibles avec traçabilité ; aucun contre-audit n'est présumé effectué.
"""
import json

AUTHORITY = "docs/collaboration/instructions/CYCLE_01_EXCEPTION_CLAUDE_VIAL_2026-10-13.md"
RECEIPT = "organisation/CYCLE_01_REPRISE_CLAUDE_2026-10-13.json"
HISTORY = "docs/collaboration/reviews/2026-10-13/CYCLE_01/etat_avant_exception.json"
STOP_RECEIPT = "organisation/CYCLE_01_INJECTION_STOP_2026-10-12.json"
CODES = ("I63", "E11", "N17", "D50")


def validate(before, after, authorized_catalog_codes=()):
    if __package__ == "tools":
        from tools.tetrade_cycle import CycleError, digest, proof, read_json, require, records
    else:
        from tetrade_cycle import CycleError, digest, proof, read_json, require, records
    data = read_json(after, RECEIPT, False)
    previous = read_json(before, RECEIPT, False)
    if data is None:
        require(previous is None, "Exception Claude : reçu supprimé")
        return None
    require(data.get("schema_version") == 1 and data.get("cycle") == 1,
            "Exception Claude : périmètre invalide")
    require(data.get("authority") == AUTHORITY and
            data.get("authority_sha256") == digest(after.read(AUTHORITY)),
            "Exception Claude : instruction différente")
    require(data.get("state") == "INJECTE_AUDIT_CLAUDE_DIFFERE" and
            data.get("execution_stopped") is False and data.get("open_for_claude") is True,
            "Exception Claude : reprise non ouverte")
    require(data.get("counter_audits_performed") is False and
            data.get("medical_final_control_performed") is False and
            data.get("medical_human_validation") is False and
            data.get("audit_assigned_to") == "Claude",
            "Exception Claude : audit non effectué présenté comme réalisé")
    history = proof(after, data.get("historical_state"), "État historique du cycle 1")
    require(data["historical_state"]["path"] == HISTORY,
            "Exception Claude : emplacement historique incorrect")
    stop = proof(after, data.get("historical_stop"), "Reçu historique STOP")
    require(data["historical_stop"]["path"] == STOP_RECEIPT,
            "Exception Claude : reçu historique incorrect")
    if previous is None:
        require(after.read(HISTORY) == before.read("organisation/tetrade_cycle_status.json"),
                "Exception Claude : historique différent de la base")
    else:
        for key in ("authority", "authority_sha256", "historical_state", "historical_stop", "baseline_files"):
            require(data.get(key) == previous.get(key), "Exception Claude : historique modifié")
        require(after.read(AUTHORITY) == before.read(AUTHORITY), "Exception Claude : autorité modifiée")
        require(after.read(HISTORY) == before.read(HISTORY), "Exception Claude : historique modifié")
    require(after.read(STOP_RECEIPT) == before.read(STOP_RECEIPT), "Exception Claude : ancien reçu STOP modifié")
    state = records(after)
    require(state.get("execution_stopped") is False, "Exception Claude : ancien STOP encore actif")
    files = data.get("files")
    baseline = {p: sha for row in history["chapters"] for p, sha in row["files"].items()}
    require(data.get("baseline_files") == baseline == stop.get("files"), "Exception Claude : baseline différente")
    require(isinstance(files, dict) and set(files) == set(baseline), "Exception Claude : seuls les 28 fichiers du cycle 1")
    for row, historical in zip(state["chapters"], history["chapters"]):
        # These attestations retain their original coverage and Prompt version.
        for key in ("code", "fragment_id", "files", "source_dir", "writer", "cross_reviewer", "counter_reviewer", "author", "cross_audit"):
            require(row.get(key) == historical.get(key), "Exception Claude : revue historique modifiée")
        require(row["counter_audit"] is None and row["control"] is None,
                "Exception Claude : audit historique fictif")
        for path, sha in historical["files"].items():
            require(digest(after.read(historical["source_dir"] + "/" + path)) == sha,
                    "Exception Claude : original livré modifié")
        for key in ("author", "cross_audit"):
            review = proof(after, historical[key], "Revue historique " + row["code"])
            require(review.get("final_files") == historical["files"], "Exception Claude : portée historique différente")
    for path, sha in files.items():
        require(digest(after.read(path)) == sha, "Exception Claude : empreinte courante différente : " + path)
    changes = proof(after, data.get("change_report"), "Traçabilité des corrections du cycle 1")
    base = baseline if previous is None else previous["files"]
    updated = {p for p in files if files[p] != base[p]}
    if previous is None or updated:
        require(changes.get("actor") == ("Codex" if previous is None else "Claude") and
                set(changes.get("files", {})) == updated,
                "Exception Claude : corrections non tracées")
        for path in updated:
            entry = changes["files"][path]
            require(entry.get("before") == base[path] and entry.get("after") == files[path] and
                    isinstance(entry.get("reason"), str) and entry["reason"].strip(),
                    "Exception Claude : correction sans provenance")
    technical = proof(after, data.get("technical_checks"), "Contrôle technique du cycle 1")
    require(technical.get("files") == files and technical.get("result") == "passed" and
            technical.get("desktop") is True and technical.get("mobile") is True and
            technical.get("javascript_errors") == [] and technical.get("missing_windows") == [],
            "Exception Claude : contrôle technique incomplet ou périmé")
    old_catalog, catalog = read_json(before, "chapters.json"), read_json(after, "chapters.json")
    require([r for r in old_catalog if r.get("code") not in set(CODES) | set(authorized_catalog_codes)] ==
            [r for r in catalog if r.get("code") not in set(CODES) | set(authorized_catalog_codes)], "Exception Claude : catalogue hors périmètre modifié")
    current_rows = [r for r in catalog if r.get("code") in CODES]
    require(len(current_rows) == 4 and {r["code"] for r in current_rows} == set(CODES),
            "Exception Claude : quatre cours enregistrés requis")
    for row in current_rows:
        require(row.get("integrated") is True and row.get("covers") == [row["code"]] and
                row.get("provisional_injection") is True and row.get("production_cycle") == 1,
                "Exception Claude : qualification de publication incorrecte")
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    scoped = {p for p in changed if any(p.startswith("chapters/" + c + "/") or p == "glossary/" + c.lower() + ".py" for c in CODES)}
    require(scoped.issubset(files), "Exception Claude : source ajoutée hors périmètre")
    authorised = dict(files)
    authorised["chapters.json"] = digest(after.read("chapters.json"))
    return authorised, set(CODES)
