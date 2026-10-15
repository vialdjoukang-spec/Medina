#!/usr/bin/env python3
"""MEDINA: scan, alert and scoped delegation; never edits contributor branches."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

PREFIX = "<!-- medina-unblock:v1 "
UTC = dt.timezone.utc
POLICY = "docs/collaboration/instructions/PUBLICATION_EN_ETAT_PARITE_2026-10-15.md"


def in_scope(pr, config):
    # Prefixes select work queues only; they prove no identity or permission.
    head = pr.get("head", {})
    repository = head.get("repo") or {}
    return (head.get("ref", "").startswith(("claude/", "codex/"))
            and repository.get("full_name", "").lower() == config["repository"].lower())


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
        out.append("conflit de fusion: reconciliation par l'auteur responsable dans son propre checkout")
    elif pr.get("mergeable") is None:
        out.append("fusionnabilite encore inconnue: ne pas deduire un conflit")
    failed = [c["name"] for c in checks if c.get("conclusion") in {"failure", "timed_out", "cancelled", "action_required"}]
    failed += [s["context"] for s in statuses if s.get("state") in {"error", "failure"}]
    if failed:
        out.append("controles a examiner: " + ", ".join(sorted(set(failed))))
    if not checks and not statuses:
        out.append("aucune preuve CI disponible sur cette tete; ne pas annoncer de reussite")
    return out


def marker(comment):
    body = comment.get("body", "")
    if comment.get("user", {}).get("login") != "github-actions[bot]" or not body.startswith(PREFIX):
        return None
    try:
        return json.loads(body[len(PREFIX):body.index(" -->")])
    except (ValueError, KeyError):
        return None


def decide(pr, checks, statuses, comments, config, now):
    if not in_scope(pr, config):
        return None
    problems = findings(pr, checks, statuses)
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
    # Every human owner response is conservative veto, including either AI on a shared account.
    if any(c.get("user", {}).get("login") == config["owner"] and c.get("user", {}).get("type") != "Bot" and stamp(c["created_at"]) >= stamp(first["created_at"]) for c in comments):
        return None
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


def message(action, pr):
    meta = {k: action[k] for k in ("key", "stage")}
    title = "Alerte preventive" if action["stage"] == "notice" else "Delegation operationnelle disponible pour l'auteur responsable"
    detail = ("Delai minimal de cinq minutes ouvert a Vial; aucune action sur les sources ni branches."
              if action["stage"] == "notice" else
              "Au moins cinq minutes ecoulees sans reponse du compte proprietaire dans ce fil. L'auteur responsable peut choisir et appliquer un correctif operationnel reversible, sur son propre travail, selon la politique commune. Le delai ne vaut pas accord du proprietaire et ne cree aucun droit GitHub. Ceci n'est ni une fusion ni une validation medicale.")
    return (PREFIX + json.dumps(meta) + " -->\n" + "### " + title + "\n\n"
            + f"Branche `{pr['head']['ref']}`, tete `{pr['head']['sha']}`.\n\n"
            + "\n".join("- " + x for x in action["problems"]) + "\n\n" + detail
            + f"\n\nInstruction: `{POLICY}`. "
            + "Les prefixes de branche ne prouvent aucune identite ni permission. "
            + "Arret global: `/medina off` dans l'issue de controle. Aucun lancement automatique de session Codex ou Claude.")


def run(config, api, now, dry_run=False):
    control = api.pages(f"issues/{config['control_issue']}/comments")
    if not enabled(config, control):
        print("Moteur desactive; aucune notification ni delegation.")
        return []
    # Inventory every branch and PR, paginated; never check out or execute PR code.
    branches = api.pages("branches")
    prs = api.pages("pulls?state=open")
    print(json.dumps({"branches": len(branches), "open_prs": len(prs)}))
    actions = []
    for item in prs:
        if not in_scope(item, config):
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
        action = decide(pr, checks, list(latest.values()), comments, config, now)
        if not action:
            continue
        # Recheck controls and both refs immediately before an external write.
        if not enabled(config, api.pages(f"issues/{config['control_issue']}/comments")):
            break
        fresh = api.request(f"pulls/{number}")
        if fresh["state"] != "open" or fresh["head"]["sha"] != sha or fresh["base"]["sha"] != pr["base"]["sha"]:
            continue
        action = decide(fresh, checks, list(latest.values()), api.pages(f"issues/{number}/comments"), config, now)
        if not action:
            continue
        if not dry_run:
            api.request(f"issues/{number}/comments", {"body": message(action, pr)})
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
