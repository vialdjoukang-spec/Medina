#!/usr/bin/env python3
"""Codex_Sentinella: receive Claude deliveries and notify the Codex coordinator.

The existing claude_watch scanner reads remote Git objects in an isolated bare
store. This entry point adds a durable GitHub issue per delivery SHA, plus a
machine-readable work order. Discovery never performs an audit or injection.
GitHub Actions is best effort; it cannot wake an inactive Codex session.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

import claude_watch


SHA = re.compile(r"[0-9a-f]{40}\Z")
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
ISSUE_PREFIX = "Codex_Sentinella : livraison Claude "
ISSUE_LABEL = "codex-sentinella"


class NotificationError(Exception):
    """Public diagnostic with no token, URL, or remote response body."""

    def __init__(self, category: str):
        self.category = category
        super().__init__(category)


def _request(repository: str, token: str, method: str, route: str, payload=None):
    if not REPOSITORY.fullmatch(repository):
        raise NotificationError("invalid_repository")
    if not token:
        raise NotificationError("missing_github_token")
    base = "https://api.github.com/repos/" + repository
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        base + route, data=data, method=method,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "MEDINA-Codex-Sentinella",
            **({"Content-Type": "application/json"} if data is not None else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise NotificationError("github_http_" + str(error.code)) from None
    except (urllib.error.URLError, OSError, ValueError):
        raise NotificationError("github_unavailable_or_invalid_response") from None


def _existing_issue_shas(repository: str, token: str) -> set[str]:
    """Read every page, including closed issues, before creating a notification."""
    found = set()
    page = 1
    while True:
        route = "/issues?" + urllib.parse.urlencode({
            "state": "all", "per_page": 100, "page": page,
        })
        issues = _request(repository, token, "GET", route)
        if not isinstance(issues, list):
            raise NotificationError("invalid_issues_response")
        for issue in issues:
            title = issue.get("title", "") if isinstance(issue, dict) else ""
            if isinstance(title, str) and title.startswith(ISSUE_PREFIX):
                sha = title[len(ISSUE_PREFIX):]
                if SHA.fullmatch(sha):
                    found.add(sha)
        if len(issues) < 100:
            return found
        page += 1


def _ensure_label(repository: str, token: str) -> None:
    try:
        _request(repository, token, "GET", "/labels/" + ISSUE_LABEL)
        return
    except NotificationError as error:
        if error.category != "github_http_404":
            raise
    try:
        _request(repository, token, "POST", "/labels", {
            "name": ISSUE_LABEL,
            "color": "267568",
            "description": "Livraisons Claude à lire et ordonner par Codex",
        })
    except NotificationError as error:
        # Another serialized or external process can create it after our GET.
        if error.category != "github_http_422":
            raise


def _candidate_order(candidate: dict) -> dict:
    sha = candidate.get("commit")
    if not isinstance(sha, str) or not SHA.fullmatch(sha):
        raise ValueError("invalid candidate SHA")
    scopes = candidate.get("scopes", [])
    fragments = sorted({scope.get("fragment_label") for scope in scopes
                        if isinstance(scope, dict) and isinstance(scope.get("fragment_label"), str)})
    refs = [ref for ref in candidate.get("refs", []) if isinstance(ref, str)]
    delivery_paths = sorted(path for path in candidate.get("delivery_paths", [])
                            if isinstance(path, str))
    return {
        "sha": sha,
        "refs": sorted(refs),
        "fragments_suggested": fragments,
        "delivery_path_count": len(delivery_paths),
        "delivery_paths_sample": delivery_paths[:12],
        "full_inventory": "queue.json artifact at the same workflow run",
        "state": "detected_pending_codex_reading",
        "next_action": "coordinator_read_diff_manifest_and_receipt",
        "agent_orders": [
            "lecture_provenance_et_perimetre",
            "audit_independant_du_fragment_entier_apres_preuves_de_completude",
            "correction_et_injection_par_codex_apres_audit_sans_reserve_bloquante",
        ],
        "gates": {
            "fragment_entier_auto_revu": "not_verified",
            "audit_croise_unique": "not_performed",
            "injection": "not_performed",
            "medical_validation_human": "not_performed",
        },
    }


def _incoming_claude(candidate: dict) -> bool:
    """Ignore Codex PR heads that merely carry copies of Claude files."""
    refs = candidate.get("advertised_refs") or candidate.get("refs") or []
    branches = [ref for ref in refs if isinstance(ref, str) and ref.startswith("refs/heads/")]
    return not branches or any(not ref.startswith(("refs/heads/codex/", "refs/heads/main",
                                                  "refs/heads/master")) for ref in branches)


def _issue_body(order: dict) -> str:
    # Only the SHA is used in the title. JSON escapes remote path characters.
    serialized = json.dumps(order, ensure_ascii=False, indent=2).replace("`", "\\u0060")
    return (
        "# Réception Codex_Sentinella\n\n"
        f"Livraison Claude détectée au commit `{order['sha']}`. "
        "Codex doit lire le diff et le rapport avant d'ordonner les agents.\n\n"
        "**Statut : détecté, lecture en attente.** La détection ne vaut ni audit, "
        "ni validation médicale, ni autorisation d'injection.\n\n"
        "Ordre proposé au coordinateur : lecture de la provenance et du périmètre ; "
        "si le fragment entier est achevé et auto-revu, audit croisé indépendant ; "
        "correction puis injection par Codex seulement après levée des réserves et "
        "vérification du SHA final. Un chapitre isolé reste en production interne.\n\n"
        "Données de réception :\n\n```json\n" + serialized + "\n```\n"
    )


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    try:
        temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def run(repo_root: Path, state_dir: Path, *, remote="origin", integration_branch="main",
        notify=False, repository="", token="") -> dict:
    scan = claude_watch.scan_once(repo_root, state_dir, remote, integration_branch)
    result = {
        "schema_version": 1,
        "tool": "Codex_Sentinella",
        "scan_status": scan["status"],
        "scan_error": scan.get("error"),
        "notifications": {"created": [], "already_present": [], "error": None},
        "automatic_agent_dispatch": False,
        "automatic_audit": False,
        "automatic_injection": False,
        "entries": [],
    }
    if scan["status"] != "ok":
        _write_json(state_dir / "sentinella.json", result)
        return result
    queue = json.loads((state_dir / "queue.json").read_text(encoding="utf-8"))
    candidates = queue.get("candidates", [])
    result["entries"] = [_candidate_order(item) for item in candidates
                         if item.get("currently_advertised") and
                         not item.get("reachable_from_integration") and
                         _incoming_claude(item)]
    if notify:
        try:
            _ensure_label(repository, token)
            existing = _existing_issue_shas(repository, token)
            for order in result["entries"]:
                sha = order["sha"]
                if sha in existing:
                    result["notifications"]["already_present"].append(sha)
                    continue
                _request(repository, token, "POST", "/issues", {
                    "title": ISSUE_PREFIX + sha,
                    "body": _issue_body(order),
                    "labels": [ISSUE_LABEL],
                })
                result["notifications"]["created"].append(sha)
                existing.add(sha)
        except NotificationError as error:
            result["notifications"]["error"] = error.category
    _write_json(state_dir / "sentinella.json", result)
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--state-dir", type=Path, required=True)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--integration-branch", default="main")
    parser.add_argument("--notify", action="store_true", help="Create one GitHub issue per new SHA.")
    args = parser.parse_args(argv)
    try:
        result = run(args.repo_root, args.state_dir, remote=args.remote,
                     integration_branch=args.integration_branch, notify=args.notify,
                     repository=os.environ.get("GITHUB_REPOSITORY", ""),
                     token=os.environ.get("GH_TOKEN", ""))
    except (ValueError, OSError, json.JSONDecodeError):
        result = {"tool": "Codex_Sentinella", "scan_status": "degraded",
                  "scan_error": {"category": "invalid_local_state_or_paths"},
                  "notifications": {"created": [], "already_present": [], "error": None},
                  "automatic_agent_dispatch": False,
                  "automatic_audit": False,
                  "automatic_injection": False,
                  "entries": []}
    print(json.dumps({
        "tool": result["tool"], "scan_status": result["scan_status"],
        "scan_error": result["scan_error"],
        "entry_count": len(result.get("entries", [])),
        "shas": [entry["sha"] for entry in result.get("entries", [])],
        "notifications": result.get("notifications"),
        "state_path": str(args.state_dir / "sentinella.json"),
    }, ensure_ascii=False))
    return 0 if result["scan_status"] == "ok" and not result["notifications"]["error"] else 2


if __name__ == "__main__":
    sys.exit(main())
