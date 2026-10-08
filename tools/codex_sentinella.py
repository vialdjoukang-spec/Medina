#!/usr/bin/env python3
"""Codex_Sentinella: receive Claude handoffs and notify the Codex coordinator.

The existing claude_watch scanner reads remote Git objects in an isolated bare
store. This entry point adds a durable GitHub issue per content fingerprint for
fragment handoffs or Claude coordination instructions. A branch head containing
only new drafts cannot recreate an issue for unchanged handoff content.
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
INSTRUCTION_PREFIX = "Codex_Sentinella : consignes Claude "
ISSUE_LABEL = "codex-sentinella"
FRAGMENT = "fragment_delivery"
INSTRUCTION = "claude_instruction"


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


def _existing_issue_identifiers(repository: str, token: str) -> tuple[dict[str, set[str]], set[str]]:
    """Read every page, including old SHA issues and closed notifications."""
    fingerprints = {FRAGMENT: set(), INSTRUCTION: set()}
    legacy_shas = set()
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
                    fingerprints[FRAGMENT].add(fingerprint)
            if isinstance(title, str) and title.startswith(INSTRUCTION_PREFIX):
                fingerprint = title[len(INSTRUCTION_PREFIX):]
                if re.fullmatch(r"[0-9a-f]{64}", fingerprint):
                    fingerprints[INSTRUCTION].add(fingerprint)
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


def _is_instruction_artifact(path: str) -> bool:
    if path in {"AGENTS.md", "CLAUDE.md", "COORDINATION.md", "docs/STYLE_REDACTION.md",
                "docs/collaboration/SIGNAUX_CODEX.json"}:
        return True
    if path.startswith("docs/collaboration/instructions/"):
        return True
    if not path.startswith("docs/collaboration/"):
        return False
    name = path.rsplit("/", 1)[-1].upper()
    return name.endswith((".MD", ".JSON", ".PDF")) and name.startswith((
        "LEADERSHIP_CLAUDE", "CHAINE_INTERNE_CLAUDE", "CONSIGNES_", "INSTRUCTIONS_",
    ))


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
        if _is_delivery_artifact(path) or _is_instruction_artifact(path):
            artifacts[path] = oid.decode("ascii")
    return artifacts


def _artifact_fingerprint(bare: Path, head: str, integration: str,
                          kind: str = FRAGMENT) -> dict | None:
    """Hash monitored blobs changed since the comparison base."""
    if kind not in {FRAGMENT, INSTRUCTION}:
        raise ValueError("invalid notification kind")
    current = _artifact_map(bare, head)
    baseline = _artifact_map(bare, integration)
    matches = _is_delivery_artifact if kind == FRAGMENT else _is_instruction_artifact
    changed = {path: oid for path, oid in current.items()
               if matches(path) and baseline.get(path) != oid}
    if not changed:
        return None
    canonical = json.dumps(sorted(changed.items()), ensure_ascii=False,
                           separators=(",", ":")).encode("utf-8")
    domain = b"Codex_Sentinella_v2\0" if kind == FRAGMENT else b"Codex_Sentinella_instructions_v1\0"
    return {
        "fingerprint": hashlib.sha256(domain + canonical).hexdigest(),
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


def _candidate_order(candidate: dict, artifact: dict, kind: str = FRAGMENT) -> dict:
    sha = candidate.get("commit")
    if not isinstance(sha, str) or not SHA.fullmatch(sha):
        raise ValueError("invalid candidate SHA")
    scopes = candidate.get("scopes", [])
    fragments = sorted({scope.get("fragment_label") for scope in scopes
                        if isinstance(scope, dict) and isinstance(scope.get("fragment_label"), str)})
    refs = [ref for ref in candidate.get("refs", []) if isinstance(ref, str)]
    delivery_paths = sorted(path for path in candidate.get("delivery_paths", [])
                            if isinstance(path, str))
    order = {
        "kind": kind,
        "sha": sha,
        "delivery_fingerprint": artifact["fingerprint"],
        "artifact_count": artifact["artifact_count"],
        "artifact_paths_sample": artifact["artifact_paths_sample"],
        "comparison_base": candidate.get("comparison_base"),
        "refs": sorted(refs),
        "fragments_suggested": fragments,
        "delivery_path_count": len(delivery_paths),
        "delivery_paths_sample": delivery_paths[:12],
        "full_inventory": "queue.json artifact at the same workflow run",
        "state": "detected_pending_codex_reading",
    }
    if kind == INSTRUCTION:
        order.update({
            "next_action": "coordinator_read_instruction_provenance_and_priority",
            "agent_orders": [
                "lecture_du_diff_et_de_la_provenance_des_consignes",
                "verification_de_priorite_face_aux_instructions_directes_utilisateur",
                "alignement_du_plan_et_des_agents_apres_lecture",
            ],
            "gates": {"medical_fragment_delivery": "not_claimed",
                      "audit_croise_unique": "not_applicable",
                      "injection": "not_applicable"},
        })
    else:
        order.update({
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
        })
    return order


def _advertised_candidates(repo_root: Path, bare: Path, remote: str, branch: str,
                           target: str, queued: list[dict]) -> list[dict]:
    """Include instruction-only Claude heads omitted by the legacy scanner."""
    _, refs, target_ref = claude_watch._remote_refs(repo_root, remote, branch)
    grouped = {}
    for ref, sha in refs.items():
        if ref != target_ref:
            grouped.setdefault(sha, []).append(ref)
    known = {item["commit"]: item for item in queued if isinstance(item, dict) and
             isinstance(item.get("commit"), str) and SHA.fullmatch(item["commit"])}
    result = []
    for sha, advertised in sorted(grouped.items()):
        # A head may move after claude_watch fetched its objects. Retry next run.
        present, _ = claude_watch._git(bare, ["cat-file", "-e", sha + "^{commit}"],
                                       "verify_instruction_head", allowed=(0, 1))
        if present == 1:
            continue
        ancestor, _ = claude_watch._git(bare, ["merge-base", "--is-ancestor", sha, target],
                                        "integration_ancestry", allowed=(0, 1))
        if ancestor == 0:
            continue
        candidate = dict(known.get(sha, {}))
        candidate.update({"commit": sha, "refs": sorted(set(candidate.get("refs", [])) | set(advertised)),
                          "advertised_refs": sorted(advertised),
                          "currently_advertised": True, "reachable_from_integration": False})
        if not (isinstance(candidate.get("comparison_base"), str) and
                SHA.fullmatch(candidate["comparison_base"])):
            code, raw = claude_watch._git(bare, ["merge-base", target, sha],
                                          "instruction_comparison_base", allowed=(0, 1))
            candidate["comparison_base"] = raw.decode("ascii").strip() if code == 0 else target
        result.append(candidate)
    return result


def _incoming_claude(candidate: dict) -> bool:
    """Ignore Codex PR heads that merely carry copies of Claude files."""
    refs = candidate.get("advertised_refs") or candidate.get("refs") or []
    branches = [ref for ref in refs if isinstance(ref, str) and ref.startswith("refs/heads/")]
    return not branches or any(not ref.startswith(("refs/heads/codex/", "refs/heads/main",
                                                  "refs/heads/master")) for ref in branches)


def _issue_body(order: dict) -> str:
    # The title uses the content fingerprint. JSON escapes remote path characters.
    serialized = json.dumps(order, ensure_ascii=False, indent=2).replace("`", "\\u0060")
    if order["kind"] == INSTRUCTION:
        return (
            "# Signal de coordination Codex_Sentinella\n\n"
            f"Consignes Claude modifiées au commit `{order['sha']}`, empreinte "
            f"`{order['delivery_fingerprint']}`. Codex doit lire la provenance, "
            "le diff et la priorité des instructions. Les instructions directes de "
            "Vial prévalent.\n\n"
            "**Statut : signal détecté, lecture en attente.** Ce signal n'est pas "
            "une remise médicale de fragment et n'ouvre ni audit croisé ni injection.\n\n"
            "Données de réception :\n\n```json\n" + serialized + "\n```\n"
        )
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
        advertised = _advertised_candidates(repo_root, bare, remote, integration_branch,
                                            integration, candidates)
        for item in advertised:
            if not _incoming_claude(item):
                continue
            baseline = item["comparison_base"]
            for kind in (FRAGMENT, INSTRUCTION):
                artifact = _artifact_fingerprint(bare, item["commit"], baseline, kind)
                if artifact is not None:
                    result["entries"].append(_candidate_order(item, artifact, kind))
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
            for order in result["entries"]:
                kind = order["kind"]
                fingerprint = order["delivery_fingerprint"]
                for legacy_sha in legacy_shas:
                    try:
                        artifact = _artifact_fingerprint(bare, legacy_sha,
                                                         order["comparison_base"], kind)
                    except (claude_watch.ScanError, ValueError):
                        # An old head may no longer be reachable after force-push.
                        continue
                    if artifact is not None:
                        existing[kind].add(artifact["fingerprint"])
                if fingerprint in existing[kind]:
                    result["notifications"]["already_present"].append(fingerprint)
                    continue
                _request(repository, token, "POST", "/issues", {
                    "title": (FINGERPRINT_PREFIX if kind == FRAGMENT else INSTRUCTION_PREFIX)
                             + fingerprint,
                    "body": _issue_body(order),
                    "labels": [ISSUE_LABEL],
                })
                result["notifications"]["created"].append(fingerprint)
                existing[kind].add(fingerprint)
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
    parser.add_argument("--notify", action="store_true", help="Create one GitHub issue per new handoff fingerprint.")
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
        "entries": [{"sha": entry["sha"], "kind": entry["kind"],
                     "fingerprint": entry["delivery_fingerprint"]}
                    for entry in result.get("entries", [])],
        "notifications": result.get("notifications"),
        "state_path": str(args.state_dir / "sentinella.json"),
    }, ensure_ascii=False))
    return 0 if result["scan_status"] == "ok" and not result["notifications"]["error"] else 2


if __name__ == "__main__":
    sys.exit(main())
