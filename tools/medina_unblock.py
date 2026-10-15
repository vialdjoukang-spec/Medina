#!/usr/bin/env python3
"""MEDINA: scan, alert and scoped delegation; never edits contributor branches."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request

PREFIX = "<!-- medina-unblock:v1 "
UTC = dt.timezone.utc


def stamp(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def enabled(config, comments):
    result = config.get("enabled") is True
    for c in sorted(comments, key=lambda c: (c["created_at"], c["id"])):
        if c.get("user", {}).get("login") != config["owner"] or c.get("user", {}).get("type") == "Bot":
            continue
        command = c.get("body", "").strip()
        if command == "/medina off":
            result = False
        elif command == "/medina on":
            result = True
    return result


def findings(pr, checks, statuses):
    out = []
    if pr.get("draft"):
        out.append("brouillon: aucune publication automatique")
    if pr.get("mergeable") is False:
        out.append("conflit de fusion: reconciliation par Claude dans son propre checkout")
    elif pr.get("mergeable") is None:
        out.append("fusionnabilite encore inconnue: ne pas deduire un conflit")
    failed = [c["name"] for c in checks if c.get("conclusion") in {"failure", "timed_out", "cancelled", "action_required"}]
    failed += [s["context"] for s in statuses if s.get("state") in {"error", "failure"}]
    if failed:
        out.append("controles a examiner: " + ", ".join(sorted(set(failed))))
    if not checks and not statuses:
        out.append("aucune preuve CI disponible sur cette tete; ne pas annoncer de reussite")
    return out


_PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|Lorem ipsum|à compléter|à renseigner)\b", re.IGNORECASE)


def lesson_suggestions(files):
    """Report only literal placeholder signals in changed lesson/evidence files.

    These are triage suggestions, not a medical or editorial audit and never a
    merge gate. Missing patches are deliberately not interpreted as defects.
    """
    out = []
    for item in files:
        path = item.get("filename", "")
        lower = path.lower()
        relevant = lower.endswith((".html", ".htm", "recherche.md", "rapport.md", "sources.json"))
        if not relevant:
            continue
        patch = item.get("patch")
        if not patch:
            continue
        added = "\n".join(line[1:] for line in patch.splitlines() if line.startswith("+") and not line.startswith("+++"))
        markers = sorted(set(match.group(0) for match in _PLACEHOLDER.finditer(added)))
        if markers:
            out.append(f"suggestion non bloquante — `{path}` : marqueur provisoire explicite ({', '.join(markers)}); vérifier puis corriger ou conserver avec justification.")
        if item.get("status") == "added" and item.get("additions") == 0:
            out.append(f"suggestion non bloquante — `{path}` : fichier ajouté vide selon la métadonnée GitHub; confirmer s'il s'agit d'un squelette volontaire.")
    return out


def marker(comment):
    body = comment.get("body", "")
    if comment.get("user", {}).get("login") != "github-actions[bot]" or not body.startswith(PREFIX):
        return None
    try:
        return json.loads(body[len(PREFIX):body.index(" -->")])
    except (ValueError, KeyError):
        return None


def decide(pr, checks, statuses, comments, config, now, suggestions=()):
    # Claude ownership is a branch hint, not an identity inferred from shared login.
    if not pr["head"]["ref"].startswith("claude/") or pr["head"]["repo"]["full_name"].lower() != config["repository"].lower():
        return None
    problems = findings(pr, checks, statuses) + list(suggestions)
    if not problems:
        return None
    key = hashlib.sha256(json.dumps([pr["head"]["sha"], pr["base"]["sha"], problems], sort_keys=True).encode()).hexdigest()
    notices = [(c, marker(c)) for c in comments]
    notices = [(c, m) for c, m in notices if m and m.get("key") == key]
    if any(m.get("stage") == "delegated" for _, m in notices):
        return None
    if not notices:
        return {"key": key, "stage": "notice", "problems": problems}
    first = min((c for c, _ in notices), key=lambda c: c["created_at"])
    # PR-thread replies no longer veto delegation. The central /medina off
    # control issue remains the explicit pause mechanism.
    if (now - stamp(first["created_at"])).total_seconds() < config["grace_seconds"]:
        return None
    return {"key": key, "stage": "delegated", "problems": problems}


class GitHub:
    def __init__(self, repo, token):
        self.repo, self.token = repo, token

    def request(self, path, data=None):
        url = "https://api.github.com/repos/" + self.repo + "/" + path
        payload = None if data is None else json.dumps(data).encode()
        req = urllib.request.Request(url, payload, headers={
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "MEDINA-scoped-unblock", "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)

    def pages(self, path, key=None):
        out, page = [], 1
        while True:
            data = self.request(path + ("&" if "?" in path else "?") + f"per_page=100&page={page}")
            items = data[key] if key else data
            out.extend(items)
            if len(items) < 100:
                return out
            page += 1


def message(action, pr, config=None):
    config = config or {"medical_audits": "suspended"}
    meta = {k: action[k] for k in ("key", "stage")}
    title = "Alerte preventive" if action["stage"] == "notice" else "Delegation operationnelle disponible pour Claude"
    detail = ("Délai minimal de cinq minutes ouvert; constats et suggestions seulement, aucune action du moteur sur les sources ou branches."
              if action["stage"] == "notice" else
              "Au moins cinq minutes écoulées depuis l'alerte. Claude peut examiner, accepter ou rejeter les suggestions et décider de la suite sur son propre travail. Le moteur n'effectue aucune correction, fusion ou validation médicale.")
    audit_note = ("\n\n**Audits médicaux : suspendus jusqu’à nouvel ordre.** Un audit absent ou différé reste non réalisé; les statuts techniques détectés sont rapportés sans être transformés en veto du moteur. "
                  if config.get("medical_audits") == "suspended" else "")
    truth_note = ("\n\nAvant toute production de cours, Claude et chaque agent qui ouvre une leçon doivent lire le [Prompt de vérité](../blob/main/docs/collaboration/betta/PROMPT_VERITE.md) et satisfaire la porte pré-rédaction prévue. Le moteur ne prétend pas vérifier cette lecture.")
    return (PREFIX + json.dumps(meta) + " -->\n" + "### " + title + "\n\n"
            + f"Branche `{pr['head']['ref']}`, tete `{pr['head']['sha']}`.\n\n"
            + "\n".join("- " + x for x in action["problems"]) + "\n\n" + detail
            + audit_note + truth_note
            + "\n\nInstruction: `docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md`. "
            + "Arret global: `/medina off` dans l'issue de controle. Aucun lancement automatique de session Claude.")


def branch_inventory(api):
    """Return paginated branch refs, falling back on Git refs after API 403."""
    try:
        return api.pages("branches")
    except urllib.error.HTTPError as exc:
        if exc.code != 403:
            raise
    try:
        refs = api.pages("git/matching-refs/heads/")
        print("Avertissement: /branches refusé (403); inventaire relu via git/matching-refs/heads/.")
        return [{"name": ref["ref"].removeprefix("refs/heads/")} for ref in refs]
    except urllib.error.HTTPError as exc:
        print(f"Avertissement: inventaire des branches indisponible (HTTP {exc.code}); le scan des PR continue.")
        return None


def run(config, api, now, dry_run=False):
    control = api.pages(f"issues/{config['control_issue']}/comments")
    if not enabled(config, control):
        print("Moteur desactive; aucune notification ni delegation.")
        return []
    # Inventory every branch and PR, paginated; never check out or execute PR code.
    branches = branch_inventory(api)
    prs = api.pages("pulls?state=open")
    print(json.dumps({"branches": None if branches is None else len(branches), "open_prs": len(prs)}))
    actions = []
    for item in prs:
        if not item["head"]["ref"].startswith("claude/"):
            continue
        number = item["number"]
        pr = api.request(f"pulls/{number}")
        sha = pr["head"]["sha"]
        checks = api.pages(f"commits/{sha}/check-runs?filter=latest", "check_runs")
        statuses = api.pages(f"commits/{sha}/statuses")
        # REST statuses can contain historical repetitions; only newest per context applies.
        latest = {}
        for s in statuses:
            latest.setdefault(s["context"], s)
        comments = api.pages(f"issues/{number}/comments")
        try:
            changed_files = api.pages(f"pulls/{number}/files")
            suggestions = lesson_suggestions(changed_files)
        except urllib.error.HTTPError as exc:
            print(f"Avertissement: fichiers PR #{number} non analysés (HTTP {exc.code}); aucun défaut n'est déduit.")
            suggestions = []
        action = decide(pr, checks, list(latest.values()), comments, config, now, suggestions)
        if not action:
            continue
        # Recheck controls and both refs immediately before an external write.
        if not enabled(config, api.pages(f"issues/{config['control_issue']}/comments")):
            break
        fresh = api.request(f"pulls/{number}")
        if fresh["state"] != "open" or fresh["head"]["sha"] != sha or fresh["base"]["sha"] != pr["base"]["sha"]:
            continue
        action = decide(fresh, checks, list(latest.values()), api.pages(f"issues/{number}/comments"), config, now, suggestions)
        if not action:
            continue
        if not dry_run:
            api.request(f"issues/{number}/comments", {"body": message(action, pr, config)})
        actions.append({"pr": number, **action})
    print(json.dumps(actions, ensure_ascii=False))
    return actions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    cfg = json.loads(Path("organisation/deblocage_vial.json").read_text())
    if cfg["repository"] != "vialdjoukang-spec/Medina" or cfg["grace_seconds"] < 300:
        raise SystemExit("Configuration hors perimetre refusee")
    run(cfg, GitHub(cfg["repository"], os.environ["GH_TOKEN"]), dt.datetime.now(UTC), args.dry_run)
