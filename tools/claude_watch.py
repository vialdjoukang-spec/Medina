#!/usr/bin/env python3
"""Observe Claude deliveries without modifying the canonical repository.

Uses native Git authentication and an isolated bare object store. Discovery is
never an audit, an approval, an injection, or proof of publication. A running
loop lasts only while this process and its execution environment remain alive.
Only the Python standard library and the installed Git executable are used.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import time

DEFAULT_INTEGRATION = "codex/sciences-cs-fragments-20261007"
DEFAULT_STATE_DIR = "/workspace/medina-env/claude-watch"
SHA = re.compile(r"[0-9a-f]{40}\Z")
CODE = re.compile(r"[A-Z][0-9]{2}(?:\.[0-9A-Za-z]+)?\Z")


class ScanError(Exception):
    """A diagnostic that deliberately contains no raw Git output or URL."""

    def __init__(self, stage, category, returncode=None):
        self.details = {"stage": stage, "category": category}
        if returncode is not None:
            self.details["returncode"] = returncode
        super().__init__(category)


def _now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _git(cwd, args, stage, allowed=(0,), timeout=120):
    env = os.environ.copy()
    # Preserve injected proxy/credential configuration. Never dump the env.
    env.update(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
    try:
        result = subprocess.run(
            ["git", "-c", "core.hooksPath=/dev/null", "-c", "gc.auto=0",
             "-c", "maintenance.auto=false", *args], cwd=cwd, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise ScanError(stage, "git_timeout") from None
    except OSError:
        raise ScanError(stage, "git_unavailable") from None
    if result.returncode not in allowed:
        raise ScanError(stage, "git_failed", result.returncode)
    return result.returncode, result.stdout


def _json_file(path, default):
    if not path.exists():
        return default
    if path.is_symlink():
        raise ScanError("state", "state_symlink")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeError):
        raise ScanError("state", "state_unreadable") from None


def _atomic_json(path, data):
    if path.is_symlink():
        raise ScanError("state", "state_symlink")
    temp = None
    try:
        with tempfile.NamedTemporaryFile("w", dir=path.parent, encoding="utf-8",
                                         prefix=".watch-", delete=False) as out:
            temp = Path(out.name)
            json.dump(data, out, ensure_ascii=False, indent=2)
            out.write("\n")
            out.flush()
            os.fsync(out.fileno())
        os.replace(temp, path)
    except OSError:
        raise ScanError("state", "state_write_failed") from None
    finally:
        if temp is not None:
            temp.unlink(missing_ok=True)


def _save_bundle(directory, documents):
    """Publish consistent artifacts; restore previous files on a write failure."""
    backups, written = {}, []
    try:
        for name in documents:
            path = directory / name
            if path.is_symlink():
                raise ScanError("state", "state_symlink")
            backups[name] = path.read_bytes() if path.exists() else None
        for name, data in documents.items():
            _atomic_json(directory / name, data)
            written.append(name)
    except (ScanError, OSError):
        for name in reversed(written):
            path = directory / name
            original = backups[name]
            try:
                if original is None:
                    path.unlink(missing_ok=True)
                else:
                    with tempfile.NamedTemporaryFile("wb", dir=directory,
                                                     prefix=".restore-", delete=False) as out:
                        temporary = Path(out.name)
                        out.write(original)
                        out.flush()
                        os.fsync(out.fileno())
                    try:
                        os.replace(temporary, path)
                    finally:
                        temporary.unlink(missing_ok=True)
            except OSError:
                # No filesystem can guarantee rollback if it also rejects the
                # restore. Report this distinct storage failure, without data.
                raise ScanError("state", "state_restore_failed") from None
        raise ScanError("state", "state_bundle_write_failed") from None


def _remote_refs(root, remote, integration_branch):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", remote) or remote.startswith("-"):
        raise ScanError("configuration", "invalid_remote_name")
    if not integration_branch or integration_branch.startswith("-"):
        raise ScanError("configuration", "invalid_integration_branch")
    _git(root, ["check-ref-format", "refs/heads/" + integration_branch], "configuration")
    # Resolve locally but never persist or display a possibly authenticated URL.
    _, raw_url = _git(root, ["remote", "get-url", remote], "remote_configuration")
    url = raw_url.decode("utf-8", "strict").strip()
    if not url or "\n" in url or url.startswith("-"):
        raise ScanError("configuration", "invalid_remote_url")
    _, raw = _git(root, ["ls-remote", "--refs", url,
                        "refs/heads/*", "refs/pull/*/head"], "remote_inventory")
    refs = {}
    for line in raw.decode("utf-8", "strict").splitlines():
        parts = line.split("\t")
        if len(parts) != 2 or not SHA.fullmatch(parts[0]):
            raise ScanError("remote_inventory", "invalid_ref_listing")
        sha, ref = parts
        if not (ref.startswith("refs/heads/") or re.fullmatch(r"refs/pull/[0-9]+/head", ref)):
            raise ScanError("remote_inventory", "unexpected_ref")
        refs[ref] = sha
    target_ref = "refs/heads/" + integration_branch
    if target_ref not in refs:
        raise ScanError("remote_inventory", "integration_branch_missing")
    return url, refs, target_ref


def _acquire(root, state_dir, remote, integration_branch):
    url, refs, target_ref = _remote_refs(root, remote, integration_branch)
    # Historical Claude deliveries may use a neutral branch name and no PR.
    # Inspect all advertised heads rather than infer absence from their names.
    selected = dict(refs)
    bare = state_dir / "git"
    if bare.is_symlink():
        raise ScanError("object_store", "state_symlink")
    if not bare.exists():
        _git(state_dir, ["init", "--bare", str(bare)], "object_store_initialization")
    _, check = _git(bare, ["rev-parse", "--is-bare-repository"], "object_store")
    if check.strip() != b"true":
        raise ScanError("object_store", "object_store_not_bare")
    # Only the isolated object store is mutated; no canonical remote refs move.
    # Fetch every selected ref and verify its object against the inventory SHA.
    refspecs = ["+" + ref + ":refs/watch/" + ref[5:] for ref in sorted(selected)]
    for start in range(0, len(refspecs), 100):
        _git(bare, ["fetch", "--no-tags", "--no-write-fetch-head", url,
                    *refspecs[start:start + 100]], "fetch_delivery_objects")
    for ref, sha in selected.items():
        _, actual = _git(bare, ["rev-parse", "refs/watch/" + ref[5:] + "^{commit}"], "verify_remote_head")
        if actual.decode("ascii").strip() != sha:
            raise ScanError("verify_remote_head", "remote_changed_during_scan")
    return bare, refs, selected, refs[target_ref]


def _catalog(root):
    """Read stable local JSON metadata, never import or execute project code."""
    chapters, labels, owners, primary, titles = [], {}, {}, {}, {}
    notes = []
    try:
        chapters = json.loads((root / "chapters.json").read_text(encoding="utf-8"))
        registry = json.loads((root / "organisation/fragments.json").read_text(encoding="utf-8"))
        fragments = json.loads((root / "fragments.json").read_text(encoding="utf-8"))
        labels = {item["id"]: item["label"] for item in registry}
        shell = (root / "shell/medina_front.html").read_text(encoding="utf-8")
        match = re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', shell, re.S)
        entries = json.loads(match.group(1))["entries"]
        explicit = {code: fragment["id"] for fragment in fragments
                    for code in fragment.get("rattachements", []) if CODE.fullmatch(code)}
        for entry in entries:
            code = entry["code"]
            titles[code] = entry["title"]
            matches = [f["id"] for f in fragments if code in f.get("rattachements", []) or
                       (code not in explicit and entry.get("system") in f.get("rattachements", []))]
            if len(matches) == 1:
                owners[code] = matches[0]
        for chapter in chapters:
            if chapter.get("integrated", True):
                titles[chapter["code"]] = chapter["title"]
                for covered in chapter.get("covers", [chapter["code"]]):
                    primary[covered] = chapter["code"]
    except (OSError, ValueError, UnicodeError, KeyError, TypeError, AttributeError):
        notes.append("local_catalogue_incomplete; scopes_require_manual_confirmation")
    return {"labels": labels, "owners": owners, "primary": primary, "titles": titles}, notes


def _claude_path(path):
    low = path.lower()
    if low.startswith("livraisons/livraison claude/"):
        return True
    name = PurePosixPath(low).name
    if name in {"claude.md", "claude_fragments_cahier_des_charges.md",
                "mechanisms_claude.md", "claude_review_scope_2026-10-07.json"}:
        return False
    # Older reports may be flat, nested or outside the new delivery directory.
    if "claude" in low and low.endswith((".md", ".json", ".patch", ".diff")):
        return True
    if low.startswith("docs/collaboration/reviews/"):
        return True
    return False


def _source_path(path):
    return path.startswith(("chapters/", "glossary/", "modules/")) or path in {
        "chapters.json", "fragments.json", "organisation/course_groups.json",
    }


def _paths(bare, target, head):
    code, raw = _git(bare, ["merge-base", target, head], "comparison_base", allowed=(0, 1))
    if code == 1:
        _, paths = _git(bare, ["ls-tree", "-r", "--name-only", "-z", head], "unrelated_history_paths")
        return None, "unrelated_history", paths.decode("utf-8", "strict").split("\0")[:-1]
    base = raw.decode("ascii").strip()
    _, paths = _git(bare, ["diff", "--no-ext-diff", "--no-textconv", "--name-only",
                          "--no-renames", "-z", base, head, "--"], "delivery_diff")
    return base, "merge_base", paths.decode("utf-8", "strict").split("\0")[:-1]


def _safe_codes(value):
    return [str(code) for code in value if isinstance(code, str) and CODE.fullmatch(code)]


def _scopes(bare, head, paths, catalog):
    codes, manifests, scope_hints = set(), [], {}
    for path in paths:
        parts = PurePosixPath(path).parts
        for i, part in enumerate(parts[:-1]):
            if part == "chapters" and CODE.fullmatch(parts[i + 1]):
                codes.add(parts[i + 1])
        if _claude_path(path):
            for code in re.findall(r"(?<![A-Za-z0-9])([A-Z][0-9]{2})(?![A-Za-z0-9])", parts[-1]):
                if code in catalog["titles"]:
                    codes.add(code)
        if path.startswith("glossary/"):
            glossary_code = PurePosixPath(path).stem.upper()
            if glossary_code in catalog["titles"]:
                codes.add(glossary_code)
        # Do not treat README/template availability as a medical delivery proof.
        if parts and parts[-1] == "livraison.json" and _claude_path(path):
            ret, raw = _git(bare, ["show", head + ":" + path], "manifest_read", allowed=(0, 128))
            if ret != 0:
                manifests.append({"path": path, "validation": "deleted_or_unreadable"})
                continue
            try:
                data = json.loads(raw.decode("utf-8"))
                fragment = data.get("fragment", {})
                fid = fragment.get("id") if isinstance(fragment, dict) else None
                declared = _safe_codes([c.get("code") if isinstance(c, dict) else c
                                        for c in data.get("chapters", [])])
                for entry in data.get("files", []):
                    if isinstance(entry, dict):
                        match = re.search(r"(?:^|/)chapters/([A-Z][0-9]{2})/", str(entry.get("target_path", "")))
                        if match:
                            declared.append(match.group(1))
                declared = sorted(set(declared))
                manifests.append({"path": path, "fragment_id": fid if fid in catalog["labels"] else None,
                                  "declared_codes": declared, "validation": "not_performed"})
                codes.update(declared)
                for code in declared:
                    if fid in catalog["labels"]:
                        scope_hints[code] = fid
            except (ValueError, UnicodeError, TypeError, AttributeError):
                manifests.append({"path": path, "validation": "invalid_json_or_structure"})
    scopes = []
    for code in sorted(codes):
        primary = catalog["primary"].get(code, code)
        fid = catalog["owners"].get(primary) or scope_hints.get(primary)
        title = catalog["titles"].get(primary)
        label = catalog["labels"].get(fid)
        item = {"code": primary, "title": title, "fragment_id": fid, "fragment_label": label,
                "display_name": f"{primary} — {title} ({label})" if title and label else None}
        if primary != code:
            item["consumer_category"] = code
            item["consumer_fragment_id"] = catalog["owners"].get(code)
            item["consumer_fragment_label"] = catalog["labels"].get(catalog["owners"].get(code))
            item["consumer_title"] = catalog["titles"].get(code)
            if item["consumer_title"] and item["consumer_fragment_label"]:
                item["consumer_display_name"] = (
                    f"{code} — {item['consumer_title']} ({item['consumer_fragment_label']})"
                )
        if item not in scopes:
            scopes.append(item)
    return scopes, manifests


def _initial_state():
    return {"schema_version": 1, "last_success_at": None, "integration_commit": None,
            "seen_commits": [], "candidates": []}


def _validate_state(state):
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        raise ScanError("state", "unsupported_state")
    if not isinstance(state.get("candidates"), list) or not isinstance(state.get("seen_commits"), list):
        raise ScanError("state", "invalid_state")
    if any(not isinstance(c, dict) or not isinstance(c.get("commit"), str) or
           not SHA.fullmatch(c["commit"]) for c in state["candidates"]):
        raise ScanError("state", "invalid_candidate_state")
    if any(not isinstance(sha, str) or not SHA.fullmatch(sha) for sha in state["seen_commits"]):
        raise ScanError("state", "invalid_seen_commits")


def _scan_locked(root, state_dir, remote, integration_branch):
    state_path = state_dir / "state.json"
    previous = _json_file(state_path, _initial_state())
    _validate_state(previous)
    context = {"repository_root": str(root), "remote_name": remote, "integration_branch": integration_branch}
    if previous.get("context") is not None and previous["context"] != context:
        raise ScanError("configuration", "state_repository_context_mismatch")
    bare, refs, selected, target = _acquire(root, state_dir, remote, integration_branch)
    catalog, notes = _catalog(root)
    _, root_sha = _git(root, ["rev-parse", "HEAD"], "local_catalogue_commit")
    grouped = {}
    for ref, sha in selected.items():
        if ref == "refs/heads/" + integration_branch:
            continue
        grouped.setdefault(sha, []).append(ref)
    # Build entirely in memory; failures cannot replace the last successful state.
    candidates = {item["commit"]: dict(item) for item in previous["candidates"]}
    seen = set(previous["seen_commits"])
    at, new_count = _now(), 0
    for candidate in candidates.values():
        candidate["currently_advertised"] = False
        candidate["advertised_refs"] = []
    for head, advertised in sorted(grouped.items()):
        coordinator_only = all(ref in {"refs/heads/main", "refs/heads/master"} or
                               ref.startswith("refs/heads/codex/") for ref in advertised)
        if coordinator_only:
            # Published/coordinator heads can contain copies of old Claude
            # packets. Those heads are not new incoming Claude deliveries.
            continue
        ancestor, _ = _git(bare, ["merge-base", "--is-ancestor", head, target], "integration_ancestry", allowed=(0, 1))
        if head in candidates:
            candidate = candidates[head]
            candidate["refs"] = sorted(set(candidate.get("refs", [])) | set(advertised))
            candidate["advertised_refs"] = sorted(advertised)
            candidate["currently_advertised"] = True
            candidate["reachable_from_integration"] = ancestor == 0
            candidate["last_seen_at"] = at
        if ancestor == 0 or head in seen:
            continue
        base, comparison, changed = _paths(bare, target, head)
        delivery_paths = [path for path in changed if _claude_path(path)]
        claude_branch = any(ref.startswith("refs/heads/") and "claude" in ref.lower() for ref in advertised)
        medical_paths = [path for path in changed if _source_path(path)]
        if not delivery_paths and not (claude_branch and medical_paths):
            # This SHA has no identifiable Claude delivery. A future commit is
            # scanned anew; no absence of unrelated reports is inferred here.
            continue
        scopes, manifests = _scopes(bare, head, changed, catalog)
        candidate = {
            "commit": head, "refs": sorted(advertised), "advertised_refs": sorted(advertised),
            "currently_advertised": True, "reachable_from_integration": False,
            "integration_commit_at_detection": target, "comparison_base": base,
            "comparison": comparison, "changed_paths": sorted(changed),
            "delivery_paths": sorted(delivery_paths), "scopes": scopes, "manifests": manifests,
            "status": "detected_pending_audit", "first_seen_at": at, "last_seen_at": at,
            "audit": "not_performed", "injection": "not_performed", "publication": "not_verified",
        }
        candidates[head] = candidate
        seen.add(head)
        new_count += 1
    # An integrated/disappeared ref is graph evidence only, not an audit result.
    result = {"schema_version": 1, "last_success_at": at, "integration_commit": target,
              "integration_branch": integration_branch,
              "context": context,
              "catalogue_commit": root_sha.decode("ascii").strip(),
              "seen_commits": sorted(seen), "candidates": list(candidates.values()), "notes": notes}
    queue = {"schema_version": 1, "integration_commit": target, "last_success_at": at,
             "candidates": result["candidates"], "notes": notes}
    summary = {"status": "ok", "last_success_at": at, "integration_commit": target,
               "branches_seen": sum(ref.startswith("refs/heads/") for ref in refs),
               "pull_heads_seen": sum(ref.startswith("refs/pull/") for ref in refs),
               "new_candidates": new_count, "candidate_count": len(candidates),
               "outstanding_candidates": sum(c["currently_advertised"] and not c["reachable_from_integration"]
                                             for c in candidates.values()),
               "queue_path": str(state_dir / "queue.json"), "status_path": str(state_dir / "status.json"),
               "error": None, "notes": notes, "automatic_audit": False, "automatic_injection": False}
    _save_bundle(state_dir, {"queue.json": queue, "state.json": result, "status.json": summary})
    return summary


def scan_once(repo_root, state_dir, remote="origin", integration_branch=DEFAULT_INTEGRATION):
    """One locked scan; Git errors return degraded and preserve previous state."""
    root, directory = Path(repo_root).resolve(), Path(state_dir).resolve()
    if directory == root or root in directory.parents:
        # Never create even a status file inside the canonical checkout.
        raise ValueError("state_dir must be outside repo_root")
    directory.mkdir(parents=True, exist_ok=True)
    lock_path = directory / ".scan.lock"
    if lock_path.is_symlink():
        raise ValueError("state lock must not be a symlink")
    with lock_path.open("a+") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return {"status": "busy", "new_candidates": 0, "error": {"stage": "lock", "category": "scan_already_running"},
                    "queue_path": str(directory / "queue.json"), "status_path": str(directory / "status.json")}
        try:
            return _scan_locked(root, directory, remote, integration_branch)
        except (ScanError, OSError, UnicodeError) as error:
            details = error.details if isinstance(error, ScanError) else {"stage": "scan", "category": "local_io_or_encoding_error"}
            try:
                previous = _json_file(directory / "state.json", _initial_state())
                _validate_state(previous)
            except ScanError:
                previous = _initial_state()
            summary = {"status": "degraded", "attempted_at": _now(),
                       "last_success_at": previous.get("last_success_at"),
                       "integration_commit": previous.get("integration_commit"),
                       "new_candidates": 0, "candidate_count": len(previous.get("candidates", [])),
                       "queue_path": str(directory / "queue.json"), "status_path": str(directory / "status.json"),
                       "error": details, "automatic_audit": False, "automatic_injection": False}
            try:
                _atomic_json(directory / "status.json", summary)
            except ScanError:
                summary["status_write_failed"] = True
            return summary
        finally:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("/workspace/Medina"))
    parser.add_argument("--state-dir", type=Path, default=Path(DEFAULT_STATE_DIR))
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--integration-branch", default=DEFAULT_INTEGRATION)
    parser.add_argument("--once", action="store_true", help="Scan once, print a JSON summary and exit.")
    parser.add_argument("--interval", type=int, default=300, help="Seconds between scans, at least 60 (default 300).")
    parser.add_argument("--iterations", type=int, help="Optional positive bound for the watcher loop.")
    args = parser.parse_args(argv)
    if args.interval < 60 or (args.iterations is not None and args.iterations < 1):
        parser.error("interval must be at least 60; iterations must be positive")
    iterations = 1 if args.once else args.iterations
    count, exit_code = 0, 0
    try:
        while iterations is None or count < iterations:
            try:
                summary = scan_once(args.repo_root, args.state_dir, args.remote, args.integration_branch)
            except (ValueError, OSError):
                summary = {"status": "degraded", "new_candidates": 0,
                           "error": {"stage": "configuration", "category": "invalid_paths_or_state"},
                           "automatic_audit": False, "automatic_injection": False}
            print(json.dumps(summary, ensure_ascii=False), flush=True)
            exit_code = 0 if summary["status"] == "ok" else 2
            count += 1
            if iterations is None or count < iterations:
                time.sleep(args.interval)
    except KeyboardInterrupt:
        return 130
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
