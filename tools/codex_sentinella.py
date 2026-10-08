#!/usr/bin/env python3
"""Codex_Sentinella: receive Claude deliveries and notify the Codex coordinator.

The existing claude_watch scanner reads remote Git objects in an isolated bare
store. This entry point adds a durable GitHub issue per delivery-artifact
fingerprint, plus a machine-readable work order. A branch head containing only
new drafts cannot recreate an issue for an unchanged fragment handoff.
Discovery never performs an audit or injection.
GitHub Actions is best effort; it cannot wake an inactive Codex session.
"""
from __future__ import annotations

import argparse
import hashlib
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
FINGERPRINT_PREFIX = "Codex_Sentinella : remise "
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


def _existing_issue_identifiers(repository: str, token: str) -> tuple[set[str], set[str]]:
    """Read every page, including old SHA issues and closed notifications."""
    fingerprints, legacy_shas = set(), set()
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
                    legacy_shas.add(sha)
            if isinstance(title, str) and title.startswith(FINGERPRINT_PREFIX):
                fingerprint = title[len(FINGERPRINT_PREFIX):]
                if re.fullmatch(r"[0-9a-f]{64}", fingerprint):
                    fingerprints.add(fingerprint)
        if len(issues) < 100:
            return fingerprints, legacy_shas
        page += 1


def _is_delivery_artifact(path: str) -> bool:
    parts = path.split("/")
    if (len(parts) == 4 and parts[:2] ==
            ["espace_partage", "FRAGMENTS_CLAUDE_A_AUDITER_PAR_CODEX"]):
        return parts[3] in {"MANIFESTE.json", "REMISE.md"}
    if len(parts) < 4 or parts[:2] != ["livraisons", "Livraison Claude"]:
        return False
    # Historical archives and unfinished working copies are retained in Git
    # but are not new fragment handoffs. Active legacy lots remain detectable.
    return ((len(parts) == 4 and parts[3] in {"livraison.json", "MANIFESTE.json", "REMISE.md"})
            or (len(parts) == 6 and parts[3] == "lots" and parts[5] == "livraison.json"))


def _artifact_map(bare: Path, commit: str) -> dict[str, str]:
    if not SHA.fullmatch(commit):
        raise ValueError("invalid commit SHA")
    _, raw = claude_watch._git(bare, ["ls-tree", "-r", "-z", commit], "delivery_artifact_tree")
    artifacts = {}
    for row in raw.split(b"\0"):
        if not row:
            continue
        header, path_bytes = row.split(b"\t", 1)
        mode, kind, oid = header.split(b" ")
        if kind != b"blob" or mode not in {b"100644", b"100755"}:
            continue
        path = path_bytes.decode("utf-8", "strict")
        if _is_delivery_artifact(path):
            artifacts[path] = oid.decode("ascii")
    return artifacts


def _artifact_fingerprint(bare: Path, head: str, integration: str) -> dict | None:
    """Hash active handoff blobs that differ from the current integration tree."""
    current = _artifact_map(bare, head)
    baseline = _artifact_map(bare, integration)
    changed = {path: oid for path, oid in current.items() if baseline.get(path) != oid}
    if not changed:
        return None
    canonical = json.dumps(sorted(changed.items()), ensure_ascii=False,
                           separators=(",", ":")).encode("utf-8")
    return {
        "fingerprint": hashlib.sha256(b"Codex_Sentinella_v2\0" + canonical).hexdigest(),
        "artifact_count": len(changed),
        "artifact_paths_sample": sorted(changed)[:12],
    }


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


def _candidate_order(candidate: dict, artifact: dict) -> dict:
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
        "delivery_fingerprint": artifact["fingerprint"],
        "artifact_count": artifact["artifact_count"],
        "artifact_paths_sample": artifact["artifact_paths_sample"],
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
    # The title uses the content fingerprint. JSON escapes remote path characters.
    serialized = json.dumps(order, ensure_ascii=False, indent=2).replace("`", "\\u0060")
    return (
        "# Réception Codex_Sentinella\n\n"
        f"Remise Claude détectée au commit `{order['sha']}`, empreinte "
        f"`{order['delivery_fingerprint']}`. "
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
    integration = queue["integration_commit"]
    bare = state_dir / "git"
    try:
        for item in candidates:
            if (not item.get("currently_advertised") or
                    item.get("reachable_from_integration") or not _incoming_claude(item)):
                continue
            artifact = _artifact_fingerprint(bare, item["commit"], integration)
            if artifact is not None:
                result["entries"].append(_candidate_order(item, artifact))
    except claude_watch.ScanError:
        result["scan_status"] = "degraded"
        result["scan_error"] = {"category": "delivery_artifact_scan_failed"}
        result["entries"] = []
        _write_json(state_dir / "sentinella.json", result)
        return result
    if notify and result["entries"]:
        try:
            _ensure_label(repository, token)
            existing, legacy_shas = _existing_issue_identifiers(repository, token)
            for legacy_sha in legacy_shas:
                try:
                    artifact = _artifact_fingerprint(bare, legacy_sha, integration)
                except (claude_watch.ScanError, ValueError):
                    # An old head may no longer be reachable after force-push.
                    continue
                if artifact is not None:
                    existing.add(artifact["fingerprint"])
            for order in result["entries"]:
                fingerprint = order["delivery_fingerprint"]
                if fingerprint in existing:
                    result["notifications"]["already_present"].append(fingerprint)
                    continue
                _request(repository, token, "POST", "/issues", {
                    "title": FINGERPRINT_PREFIX + fingerprint,
                    "body": _issue_body(order),
                    "labels": [ISSUE_LABEL],
                })
                result["notifications"]["created"].append(fingerprint)
                existing.add(fingerprint)
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
    parser.add_argument("--notify", action="store_true", help="Create one GitHub issue per new delivery fingerprint.")
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
