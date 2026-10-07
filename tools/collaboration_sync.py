#!/usr/bin/env python3
"""Repère les contributions MEDINA ; ne fusionne ni ne publie aucun changement.

GitHub : pagination de toutes les branches, PR et listes de fichiers des PR.
Hors réseau : --snapshot fournit les mêmes données. Les rapports portent sur
la cible déclarée ; une branche repérée ou reçue n'est jamais présumée intégrée.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_REPO = "vialdjoukang-spec/Medina"
DEFAULT_TARGET = "codex/sciences-cs-fragments-20261007"


class GitHubClient:
    def __init__(self, repository, token=None, request=None):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ValueError("Dépôt invalide ; format attendu : propriétaire/dépôt.")
        self.repository = repository
        self.token = token
        self.request = request or self._request

    def _request(self, path, params=None):
        url = "https://api.github.com/repos/" + self.repository + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "MEDINA-collaboration-sync"}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=45) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            # Les en-têtes et le jeton ne sont jamais inclus dans les diagnostics.
            raise RuntimeError(f"GitHub HTTP {error.code} sur {path}") from None
        except urllib.error.URLError:
            raise RuntimeError(f"GitHub inaccessible sur {path}") from None

    def pages(self, path, **params):
        result = []
        page = 1
        while True:
            batch = self.request(path, dict(params, per_page=100, page=page))
            if not isinstance(batch, list):
                raise ValueError(f"Liste attendue pour {path}")
            result.extend(batch)
            if len(batch) < 100:
                return result
            page += 1

    def content(self, path, commit):
        """Octets du fichier à un SHA ; Blob API pour les grandes coques HTML."""
        resource = self.request("/contents/" + urllib.parse.quote(path, safe="/"), {"ref": commit})
        if resource.get("encoding") == "base64" and resource.get("content"):
            return base64.b64decode(resource["content"])
        blob = self.request("/git/blobs/" + resource["sha"])
        if blob.get("encoding") != "base64":
            raise ValueError("Contenu GitHub non disponible : " + path)
        return base64.b64decode(blob["content"])

    def catalog(self, commit):
        chapters = json.loads(self.content("chapters.json", commit))
        fragments = json.loads(self.content("fragments.json", commit))
        shell = self.content("shell/medina_front.html", commit).decode("utf-8")
        return normalize_catalog(chapters, fragments, systems_from_shell(shell), "github:" + commit)

    def receipts(self, commit):
        receipts = []
        notes = []
        try:
            listing = self.request("/contents/docs/collaboration/receipts", {"ref": commit})
        except RuntimeError as error:
            if "HTTP 404" in str(error):
                return receipts, ["Aucun dossier de reçus à la cible ; réception non confirmée."], True
            return receipts, ["Lecture des reçus impossible : " + str(error)], False
        if not isinstance(listing, list):
            return receipts, ["La liste des reçus de la cible est indisponible."], False
        complete = len(listing) < 1000
        if not complete:
            notes.append("Liste des reçus potentiellement limitée à 1 000 fichiers ; examiner l'arbre Git.")
        for item in listing:
            if item.get("type") != "file" or not item.get("path", "").endswith(".json"):
                continue
            try:
                receipts.extend(receipt_records(json.loads(self.content(item["path"], commit))))
            except (RuntimeError, ValueError, KeyError) as error:
                notes.append("Reçu non lisible " + item["path"] + " : " + str(error))
                complete = False
        return receipts, notes, complete

    def collect(self, integration_branch):
        branches = self.pages("/branches")
        pull_requests = self.pages("/pulls", state="all")
        target = next((b for b in branches if b["name"] == integration_branch), None)
        if target is None:
            raise ValueError("La branche d'intégration n'est pas présente dans les branches distantes.")
        target_sha = target["commit"]["sha"]
        comparisons = {}
        notes = []
        complete = True
        for pr in pull_requests:
            try:
                pr["files"] = self.pages(f"/pulls/{pr['number']}/files")
                if len(pr["files"]) >= 3000:
                    pr["files_error"] = "Liste de fichiers de PR potentiellement limitée à 3 000 ; diff Git local requis."
                    notes.append(f"PR #{pr['number']} : " + pr["files_error"])
                    complete = False
            except (RuntimeError, ValueError) as error:
                pr["files_error"] = str(error)
                notes.append(str(error))
                complete = False
        heads = {b["commit"]["sha"] for b in branches}
        heads.update(p["head"]["sha"] for p in pull_requests)
        for head in sorted(heads):
            if head == target_sha:
                comparisons[head] = {"status": "identical", "files": [], "ahead_by": 0, "behind_by": 0}
                continue
            try:
                comparison = self.request("/compare/" + target_sha + "..." + head)
                # GitHub compare limite sa liste de fichiers à 300. Les PR sont
                # paginées séparément ; une branche seule reste explicitement partielle.
                if len(comparison.get("files", [])) >= 300:
                    comparison["files_may_be_truncated"] = True
                    notes.append(f"Diff de branche potentiellement limité à 300 fichiers : {head}.")
                    complete = False
                comparisons[head] = comparison
            except (RuntimeError, ValueError) as error:
                comparisons[head] = {"error": str(error)}
                notes.append(str(error))
                complete = False
        catalog = None
        try:
            catalog = self.catalog(target_sha)
        except (RuntimeError, ValueError, KeyError) as error:
            notes.append("Catalogue cible indisponible : " + str(error))
            complete = False
        receipts, receipt_notes, receipts_complete = self.receipts(target_sha)
        notes.extend(receipt_notes)
        complete = complete and receipts_complete
        for receipt in receipts:
            commit = receipt.get("integration_commit")
            if not commit or commit == target_sha or commit in comparisons:
                continue
            try:
                comparisons[commit] = self.request("/compare/" + target_sha + "..." + commit)
            except (RuntimeError, ValueError) as error:
                comparisons[commit] = {"error": str(error)}
                notes.append("Preuve du commit d'intégration indisponible : " + str(error))
                complete = False
        return {"repository": self.repository, "integration_branch": integration_branch,
                "integration_commit": target_sha, "branches": branches,
                "pull_requests": pull_requests, "comparisons": comparisons,
                "scan_complete": complete, "notes": notes, "catalog": catalog, "receipts": receipts}


def systems_from_shell(source):
    match = re.search(r'<script id="medora-data"[^>]*>(.*?)</script>', source, re.S)
    return {e["code"]: e.get("system") for e in json.loads(match.group(1)).get("entries", [])} if match else {}


def normalize_catalog(chapters, fragments, systems, basis):
    return {"chapters": {c["code"]: c for c in chapters} if isinstance(chapters, list) else chapters,
            "fragments": fragments, "systems": systems, "basis": basis}


def git_commit_available(root, commit):
    if commit and re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        try:
            return subprocess.run(["git", "-C", str(root), "cat-file", "-e", commit + "^{commit}"], capture_output=True).returncode == 0
        except OSError:
            pass
    return False


def receipt_records(payload):
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict) and "receipts" in payload:
        records = payload["receipts"]
    elif isinstance(payload, dict):
        records = [payload]
    else:
        raise ValueError("Reçu JSON : objet ou liste attendus.")
    if not isinstance(records, list) or not all(isinstance(r, dict) for r in records):
        raise ValueError("Liste de reçus invalide.")
    return records


def load_receipts(root, commit=None):
    """Reçus de la cible Git ; fichiers locaux uniquement si le SHA manque."""
    notes = []
    receipts = []
    pinned = git_commit_available(root, commit)
    if pinned:
        listing = subprocess.run(["git", "-C", str(root), "ls-tree", "-r", "--name-only", commit,
                                  "docs/collaboration/receipts/"], capture_output=True, text=True)
        paths = [p for p in listing.stdout.splitlines() if p.endswith(".json")]
    else:
        paths = [str(p.relative_to(root)) for p in (root / "docs/collaboration/receipts").glob("*.json")]
        notes.append("Reçus lus dans les fichiers locaux : SHA cible indisponible ; fournir receipts dans le snapshot pour les figer.")
    for path in paths:
        try:
            if pinned:
                content = subprocess.check_output(["git", "-C", str(root), "show", commit + ":" + path], text=True)
            else:
                content = (root / path).read_text(encoding="utf-8")
            receipts.extend(receipt_records(json.loads(content)))
        except (OSError, ValueError, subprocess.CalledProcessError) as error:
            notes.append("Reçu local non lisible " + path + " : " + str(error))
    return receipts, notes


def load_catalog(root, commit=None):
    """Lit les sources locales d'intégration ; aucun module du dépôt n'est exécuté."""
    pinned = git_commit_available(root, commit)
    def read_text(path):
        if pinned:
            result = subprocess.run(["git", "-C", str(root), "show", commit + ":" + path], capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else ""
        p = root / path
        return p.read_text(encoding="utf-8") if p.exists() else ""
    def read_json(path, default):
        content = read_text(path)
        return json.loads(content) if content else default
    chapters = read_json("chapters.json", [])
    fragments = read_json("fragments.json", [])
    return normalize_catalog(chapters, fragments, systems_from_shell(read_text("shell/medina_front.html")),
                             "git:" + commit if pinned else "local_files_fallback")


def chapter_routes(code, catalog):
    fragments = catalog["fragments"]
    explicit = {x for f in fragments for x in f.get("rattachements", []) if re.fullmatch(r"[A-Z][0-9]{2}", x)}
    routes = []
    for fragment in fragments:
        attachments = fragment.get("rattachements", [])
        if code in attachments or (code not in explicit and catalog["systems"].get(code) in attachments):
            routes.append(fragment["id"])
    return routes


def route_file(path, catalog):
    item = {"path": path, "kind": "unknown", "routes": [], "warnings": []}
    if path.startswith("livraisons/"):
        if "/sources/" in path:
            canonical = path.split("/sources/", 1)[1]
            source = route_file(canonical, catalog)
            item.update(kind="delivery_source", routes=source["routes"], canonical_path=canonical,
                        warnings=source["warnings"] + ["Source déposée ; vérifier et injecter dans le chemin canonique avant reconstruction."])
            if source.get("course"):
                item["course"] = source["course"]
        else:
            item.update(kind="delivery_report", routes=["GLOBAL"])
    elif path == "organisation/MEDINA_Organisation.html":
        item.update(kind="derived", routes=["GLOBAL"], warnings=["Tableau reconstruit depuis le registre et tools/build_organisation.py."])
    elif path.startswith("organisation/"):
        item.update(kind="consultation_source", routes=["GLOBAL"])
    elif path.startswith(("dist/", "_site/", "preview/")) or re.fullmatch(r"MEDINA[^/]*\.(html|json|zip)", path):
        item.update(kind="derived", warnings=["Sortie dérivée ; intégrer les sources puis reconstruire."])
    elif path == "modules/ecg.json":
        item.update(kind="derived", routes=["S01"], warnings=["Tracés générés : vérifier modules/ecg.py et régénérer."])
    elif path.endswith((".zip", ".sha256")) and path.startswith("deliverables/"):
        item.update(kind="derived", warnings=["Archive ou empreinte de livraison ; ne remplace pas les sources."])
    elif path.startswith("chapters/SYSTEM") or path.startswith("modules/systems/") or path == "data/system-atlas.json":
        item.update(kind="system", routes=["SYSTEM"], warnings=["Adaptateur requis : assets/system-atlas.js est retiré des fragments courses-v1."])
    elif path.startswith("chapters/"):
        parts = path.split("/")
        code = parts[1] if len(parts) > 2 else ""
        item.update(kind="course_source", course=code, routes=chapter_routes(code, catalog))
        chapter = catalog["chapters"].get(code)
        if chapter is None:
            item["warnings"].append("Cours absent de chapters.json de la cible ; déclaration à intégrer.")
        elif not chapter.get("integrated"):
            item["warnings"].append("Cours non activé dans chapters.json de la cible.")
        if not item["routes"]:
            item["warnings"].append("Aucun rattachement de fragment dans la cible.")
        for f in catalog["fragments"]:
            groups = [c for g in f.get("categories", []) for c in g.get("chapters", [])]
            if f.get("surface") == "courses-v1":
                count = groups.count(code)
                if f["id"] in item["routes"] and count != 1:
                    item["warnings"].append(f"{f['id']} : le cours doit figurer exactement une fois dans categories[].chapters.")
                elif f["id"] not in item["routes"] and count:
                    item["warnings"].append(f"{f['id']} : rubrique contenant le cours sans rattachement correspondant.")
    elif path.startswith("glossary/") and path.endswith(".py"):
        item.update(kind="glossary_source", routes=["GLOBAL"], warnings=["Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py."])
    elif path.startswith("modules/cardiovascular_cs."):
        item.update(kind="clinical_skills_source", routes=["S01", "CS"])
    elif path.startswith("docs/collaboration/reviews/") or path.startswith("audits/"):
        # Accepte les anciens rapports plats, sans imposer un dossier date/CODE.
        tokens = re.findall(r"(?<![A-Z0-9])([A-Z][0-9]{1,2})(?![A-Z0-9])", path.upper())
        known_fragments = {f["id"] for f in catalog["fragments"]}
        fragment_ids = list(dict.fromkeys(t for t in tokens if t in known_fragments))
        declared_courses = [t for t in tokens if t in catalog["chapters"]]
        # S01 est à la fois un identifiant de fragment et un code CIM historique.
        # Dans le nom d'un rapport, le fragment connu prime sur le code de cours.
        item.update(kind="review_report", routes=fragment_ids or
                    (chapter_routes(declared_courses[0], catalog) if declared_courses else ["GLOBAL"]))
        if fragment_ids:
            item["fragments"] = fragment_ids
        elif declared_courses:
            item["course"] = declared_courses[0]
        if "SYSTEM" in path.upper():
            item["routes"] = ["SYSTEM"]
        elif re.search(r"(?:^|[/_.-])CS(?:[/_.-]|$)", path.upper()):
            item["routes"] = ["S01", "CS"]
    elif path in ("chapters.json", "fragments.json", "shell/data.py"):
        item.update(kind="registration_source", routes=["GLOBAL"], warnings=["Vérifier titres, covers, activation, rattachements et rubriques après intégration."])
    elif path.startswith(("shell/", "engine/", "tools/", "tests/", ".github/")) or path in ("build_front.py", "build_medina.py", "fragment_surface.py", "build_index.py", "pack_v7.py"):
        item.update(kind="integration_source", routes=["GLOBAL"])
        if path == "shell/medina_front.html":
            item["warnings"].append("Coque historique et ressources embarquées : contrôler SYSTEM et les fragments séparément.")
    elif path.startswith("docs/") or path.endswith(".md"):
        item.update(kind="documentation", routes=["GLOBAL"])
    elif path in ("deliverables/review-2026-10-07/index.html", "deliverables/build_review_bundle.py",
                  "site/index_template.html", "site/qcm.html"):
        item.update(kind="consultation_source", routes=["GLOBAL"])
    else:
        item["warnings"].append("Chemin sans route de build connue ; examen manuel requis.")
    return item


def build_report(snapshot, catalog):
    target = snapshot.get("integration_branch", DEFAULT_TARGET)
    branches = snapshot.get("branches", [])
    target_sha = snapshot.get("integration_commit") or next((b.get("commit", {}).get("sha") for b in branches if b["name"] == target), None)
    comparisons = snapshot.get("comparisons", {})
    receipts = snapshot.get("receipts", [])
    candidates = {}
    for branch in branches:
        if branch["name"] == target:
            continue
        sha = branch.get("commit", {}).get("sha", "")
        candidate = candidates.setdefault(sha, {"head_sha": sha, "branches": [], "pull_requests": []})
        candidate["branches"].append(branch["name"])
    for pr in snapshot.get("pull_requests", []):
        sha = pr.get("head", {}).get("sha", "")
        if not sha:
            continue
        candidate = candidates.setdefault(sha, {"head_sha": sha, "branches": [], "pull_requests": []})
        candidate["pull_requests"].append(pr)
        name = pr.get("head", {}).get("ref")
        if name and name not in candidate["branches"]:
            candidate["branches"].append(name)
    result = []
    for sha, candidate in candidates.items():
        comparison = comparisons.get(sha)
        if comparison is None:
            comparison = next((comparisons[name] for name in candidate["branches"] if name in comparisons), {})
        status = comparison.get("status")
        ancestry = status in ("behind", "identical") or (sha == target_sha and bool(sha))
        files = {}
        for f in comparison.get("files", []):
            files[f["filename"]] = dict(f, diff_basis="integration_target")
        for pr in candidate["pull_requests"]:
            for f in pr.get("files", []):
                files.setdefault(f["filename"], dict(f, diff_basis="pull_request_base"))
        routed = []
        for path, metadata in sorted(files.items()):
            route = route_file(path, catalog)
            route.update(change=metadata.get("status", "unknown"), diff_basis=metadata["diff_basis"])
            if metadata.get("previous_filename"):
                route["previous_path"] = metadata["previous_filename"]
                route["previous_route"] = route_file(metadata["previous_filename"], catalog)
            routed.append(route)
        matching = [r for r in receipts if r.get("head_sha") == sha]
        received = any(r.get("received_at") for r in matching)
        integrated = ancestry
        integration_commits = []
        proven_integration_commits = []
        for receipt in matching:
            commit = receipt.get("integration_commit")
            if commit:
                integration_commits.append(commit)
                proof = comparisons.get(commit, {})
                if commit == target_sha or proof.get("status") in ("behind", "identical"):
                    integrated = True
                    proven_integration_commits.append(commit)
        verified = any(integrated and bool(r.get("verification_commit"))
                       and r.get("verification_commit") in ([target_sha] + proven_integration_commits)
                       and r.get("checks") and all(c.get("passed") is True for c in r["checks"]) for r in matching)
        warnings = list(dict.fromkeys(w for f in routed for w in f["warnings"]))
        if comparison.get("error"):
            warnings.append(comparison["error"])
        if not comparison and sha != target_sha:
            warnings.append("Comparaison à la cible indisponible ; intégration non démontrée.")
        if comparison.get("files_may_be_truncated"):
            warnings.append("Diff de branche potentiellement tronqué ; consulter tous les fichiers de la PR ou un diff Git local.")
        if not files and not ancestry:
            warnings.append("Aucun fichier de contribution identifié ; lecture de la branche requise.")
        for pr in candidate["pull_requests"]:
            if pr.get("base", {}).get("ref") != target:
                warnings.append(f"PR #{pr['number']} vise {pr.get('base', {}).get('ref')} ; comparaison à la cible MEDINA requise.")
            if pr.get("files_error"):
                warnings.append(pr["files_error"])
        result.append({"delivery_id": "head-" + sha, "head_sha": sha,
                       "branches": sorted(candidate["branches"]),
                       "pull_requests": [{k: p.get(k) for k in ("number", "title", "state", "html_url", "base", "head", "merged_at")} for p in candidate["pull_requests"]],
                       "received": received, "integrated": integrated, "verified": verified,
                       "integration_evidence": "head_ancestor_of_target" if ancestry else ("recorded_integration_commit_in_target" if integrated else None),
                       "integration_commits": integration_commits, "files": routed,
                       "routes": sorted({r for f in routed for r in f["routes"]}),
                       "warnings": list(dict.fromkeys(warnings))})
    return {"schema_version": 1, "scanned_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "repository": snapshot.get("repository", DEFAULT_REPO), "integration_branch": target,
            "integration_commit": target_sha, "scan_complete": snapshot.get("scan_complete", False),
            "notes": snapshot.get("notes", []), "catalog_basis": catalog.get("basis", "provided"),
            "limits": ["Les rapports et les tests déclarés ne constituent pas une vérification médicale indépendante.",
                       "Le routage est contrôlé contre les sources locales de la cible, avant les changements proposés.",
                       "Aucune branche n'est fusionnée, aucun reçu créé et aucun commit publié par ce scanner."],
            "deliveries": sorted(result, key=lambda d: (d["integrated"], d["branches"]))}


def markdown(report):
    def safe(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    lines = ["# MEDINA — livraisons repérées", "", "Branche d'intégration : `" + report["integration_branch"] + "`.",
             "Commit cible : `" + str(report["integration_commit"]) + "`.", "",
             "Scan : " + ("complet selon les données fournies" if report["scan_complete"] else "partiel ; réserves ci-dessous") + ".",
             "Une livraison repérée ou reçue n'est pas présumée intégrée. Une intégration ne prouve pas une vérification.", "",
             "| Branche / PR | Tête | Reçu | Intégré dans la cible | Vérifié | Routage |", "| --- | --- | --- | --- | --- | --- |"]
    for d in report["deliveries"]:
        prs = ", ".join("#" + str(p["number"]) for p in d["pull_requests"])
        name = ", ".join(d["branches"]) + (" · " + prs if prs else "")
        lines.append("| " + " | ".join([safe(name), "`" + d["head_sha"][:12] + "`", "Oui" if d["received"] else "Non confirmé",
                                      "Oui, preuve enregistrée" if d["integrated"] else "Non démontré",
                                      "Oui, contrôles enregistrés" if d["verified"] else "Non démontré", safe(", ".join(d["routes"]) or "À préciser")]) + " |")
    for d in report["deliveries"]:
        lines.extend(["", "## " + safe(", ".join(d["branches"]) or d["head_sha"][:12]), ""])
        for w in d["warnings"]:
            lines.append("- " + safe(w))
        if d["files"]:
            lines.extend(["", "| Fichier | Nature | Routage | Diff |", "| --- | --- | --- | --- |"])
            for f in d["files"]:
                lines.append("| " + " | ".join(["`" + safe(f["path"]) + "`", f["kind"], safe(", ".join(f["routes"])), f["diff_basis"]]) + " |")
    lines.extend(["", "## Limites", ""])
    lines.extend("- " + safe(x) for x in report["notes"] + report["limits"])
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--integration-branch", default=DEFAULT_TARGET)
    parser.add_argument("--snapshot", type=Path, help="JSON hors réseau ; aucun appel GitHub dans ce mode.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, default=Path("docs/collaboration"))
    args = parser.parse_args(argv)
    if args.snapshot:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    else:
        client = GitHubClient(args.repo, os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"))
        snapshot = client.collect(args.integration_branch)
    target_sha = snapshot.get("integration_commit") or next((b.get("commit", {}).get("sha") for b in snapshot.get("branches", []) if b["name"] == snapshot.get("integration_branch", DEFAULT_TARGET)), None)
    if "receipts" not in snapshot:
        snapshot["receipts"], receipt_notes = load_receipts(args.root, target_sha)
        snapshot.setdefault("notes", []).extend(receipt_notes)
    else:
        snapshot["receipts"] = receipt_records(snapshot["receipts"])
    raw_catalog = snapshot.get("catalog")
    if raw_catalog:
        catalog = normalize_catalog(raw_catalog.get("chapters", []), raw_catalog.get("fragments", []),
                                    raw_catalog.get("systems", {}), raw_catalog.get("basis", "snapshot_catalog"))
    else:
        catalog = load_catalog(args.root, target_sha)
        if catalog["basis"] == "local_files_fallback":
            snapshot.setdefault("notes", []).append("Catalogue lu dans les fichiers locaux : le SHA cible n'est pas disponible localement. Vérifier leurs empreintes ou fournir catalog dans le snapshot.")
    report = build_report(snapshot, catalog)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "DELIVERIES_LATEST.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.out / "DELIVERIES_LATEST.md").write_text(markdown(report), encoding="utf-8")
    print(f"{len(report['deliveries'])} têtes repérées ; rapports : {args.out}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError, KeyError) as error:
        print("Synchronisation impossible : " + str(error), file=sys.stderr)
        raise SystemExit(1)
