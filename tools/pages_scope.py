#!/usr/bin/env python3
"""Skip Pages only when a verified Git diff changes non-site metadata.

Unknown paths and unavailable/malformed comparisons always request a full build.
The fragment guard is a separate workflow and is never disabled here. No cached
audit or browser result is substituted for a control of changed site sources.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess


# Exact allowlist, not broad docs/** or organisation/** exclusions: those trees
# also contain published plans, figures, catalogues and browser evidence.
METADATA_FILES = frozenset({
    "AGENTS.md", "CLAUDE.md", "REPRISE_SESSION.md",
    "organisation/CYCLES_CLAUDE_journal.jsonl",
    "organisation/execution-20261014/journal.jsonl",
    "organisation/execution-20261014/status.json",
    "organisation/execution-20261014/infrastructure-publication.json",
})
CLAUDE_REGISTRY = "organisation/CYCLES_CLAUDE.json"
RECEIPTS_PREFIX = "organisation/execution-20261014/publications/"


def transferred_codes(content):
    """Project exactly the Claude-registry field read by publication_manifest.

    Ordinary status/proof updates do not change the site. A transfer can change
    publication eligibility, so its effective code set must still trigger Pages.
    Refuse to optimise an invalid/missing registry or an unrecognised shape.
    """
    data = json.loads(content)
    if not isinstance(data, dict) or not isinstance(data.get("cycles"), list):
        raise ValueError("Registre Claude non reconnu")
    result = set()
    for cycle in data["cycles"]:
        if not isinstance(cycle, dict) or not isinstance(cycle.get("chapters"), list):
            raise ValueError("Cycle Claude non reconnu")
        for chapter in cycle["chapters"]:
            if not isinstance(chapter, dict) or not isinstance(chapter.get("code"), str) or not chapter["code"]:
                raise ValueError("Chapitre Claude non reconnu")
            if cycle.get("transferred_from") == "Codex":
                result.add(chapter["code"])
    return result


def classify(changed, before_registry=None, after_registry=None):
    """Return (build_required, reasons); only positively known metadata skips."""
    reasons = []
    for path in changed:
        if path in METADATA_FILES or path.startswith(RECEIPTS_PREFIX):
            continue
        if path == CLAUDE_REGISTRY:
            try:
                same = transferred_codes(before_registry) == transferred_codes(after_registry)
            except (TypeError, ValueError, KeyError):
                same = False
            if same:
                continue
            reasons.append(path + " (transfert modifié ou registre non vérifiable)")
        else:
            reasons.append(path)
    return bool(reasons), reasons


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.PIPE)


def read_registry(root, ref):
    try:
        return git(root, "show", ref + ":" + CLAUDE_REGISTRY)
    except subprocess.CalledProcessError:
        return None


def determine_scope(root, base, head="HEAD", force=False):
    """Use the whole push range, including deletions and both sides of renames."""
    if force:
        return True, ["Exécution manuelle : reconstruction complète"]
    if not base or base == "0" * 40:
        return True, ["Base du push indisponible : reconstruction complète"]
    try:
        # Resolving to object IDs also avoids ambiguous branch names/filenames.
        before = git(root, "rev-parse", "--verify", base + "^{commit}").decode().strip()
        after = git(root, "rev-parse", "--verify", head + "^{commit}").decode().strip()
        changed = git(root, "diff", "--name-only", "--no-renames", "-z", before, after, "--").decode().split("\0")
        changed = [path for path in changed if path]
        return classify(changed, read_registry(root, before) if CLAUDE_REGISTRY in changed else None,
                        read_registry(root, after) if CLAUDE_REGISTRY in changed else None)
    except (subprocess.CalledProcessError, UnicodeError, OSError):
        return True, ["Comparaison Git indisponible : reconstruction complète"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default=os.environ.get("BASE_SHA"))
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    required, reasons = determine_scope(Path(__file__).resolve().parents[1], args.base, args.head, args.force)
    print(json.dumps({"build": required, "reasons": reasons,
                      "scope": "site à reconstruire" if required else "métadonnées seules ; garde séparée inchangée"},
                     ensure_ascii=False))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write("build=" + str(required).lower() + "\n")


if __name__ == "__main__":
    main()
