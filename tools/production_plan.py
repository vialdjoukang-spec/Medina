"""Validate the shared allocation and the single active chapter recorded per agent."""
import json
import importlib.util
import re
from pathlib import Path
from pathlib import PurePosixPath

AGENTS = {"Claude": 12, "Codex": 10}
STAGES = {"writing", "review", "checks", "integration", "blocked"}


def validate_plan(plan, registry, category_owners=None, courses=None, titles=None):
    if plan.get("assignment_unit") != "fragment":
        raise ValueError("La répartition attribue des fragments entiers à leurs responsables.")
    names = {fragment["id"]: fragment for fragment in registry}
    if plan.get("allocation") != AGENTS or set(plan.get("agents", {})) != set(AGENTS):
        raise ValueError("La répartition doit être de 12 fragments Claude et 10 Codex.")
    if plan.get("excluded_fragments") != ["S01"]:
        raise ValueError("Seule la cardiologie est exclue des 22 fragments restants.")
    rules = plan.get("rules", {})
    for key in ("max_active_chapters_per_agent", "max_active_fragments_per_agent"):
        if rules.get(key) != 1:
            raise ValueError("Un seul chapitre et un seul fragment actifs par agent.")
    if rules.get("delivery_unit") != "fragment" or rules.get("cross_audit_rounds") != 1:
        raise ValueError("Remettre un fragment entier pour un seul tour d’audit croisé.")
    if rules.get("injected_fragment_immutable") is not True or rules.get("output_theme") != "light_only":
        raise ValueError("Un fragment injecté est immuable ; le HTML utilise exclusivement le thème clair.")
    assignments = {}
    active_codes = set()
    for agent, count in AGENTS.items():
        queue = plan["agents"][agent].get("queue", [])
        if len(queue) != count or len(set(queue)) != count:
            raise ValueError("File invalide pour " + agent)
        if any(ident not in names or ident == "S01" or ident in assignments for ident in queue):
            raise ValueError("Fragment inconnu, exclu ou attribué deux fois.")
        if queue != sorted(queue, key=lambda ident: names[ident]["order"]):
            raise ValueError("La file doit suivre les rangs de production du registre.")
        for rank, ident in enumerate(queue, 1):
            assignments[ident] = {"owner": agent, "queue_order": rank, "queue_size": count}
        active = plan["agents"][agent].get("active_chapter")
        if active is not None:
            fields = ("code", "title", "fragment_id", "stage", "base_commit", "report_path")
            if not isinstance(active, dict) or any(
                not isinstance(active.get(key), str) or not active[key].strip() for key in fields
            ):
                raise ValueError("Le chapitre actif doit être unique, nommé par code et intitulé.")
            if not re.fullmatch(r"[0-9a-fA-F]{40}", active["base_commit"]):
                raise ValueError("Le commit de départ doit être un SHA complet.")
            report = PurePosixPath(active["report_path"])
            if report.is_absolute() or ".." in report.parts or "\\" in active["report_path"]:
                raise ValueError("Le rapport doit avoir un chemin relatif sûr dans le dépôt.")
            if active.get("fragment_id") not in queue or active.get("stage") not in STAGES:
                raise ValueError("Le chapitre actif doit appartenir à la file de son agent et avoir un état explicite.")
            code = active["code"]
            if courses is not None and courses.get(code, code) != code:
                raise ValueError("Réserver le cours primaire, pas une catégorie déjà couverte par ce cours.")
            if category_owners is not None and category_owners.get(code) != active["fragment_id"]:
                raise ValueError("Le code du chapitre n’appartient pas au fragment déclaré dans le catalogue.")
            if titles is not None and titles.get(code) != active["title"]:
                raise ValueError("L’intitulé du chapitre doit être celui des sources canoniques.")
            if active["code"] in active_codes:
                raise ValueError("Un même chapitre ne peut être actif chez les deux agents.")
            active_codes.add(active["code"])
    if set(assignments) != set(names) - {"S01"}:
        raise ValueError("Les 22 fragments restants doivent tous être attribués.")
    return assignments


def load_plan(root, category_owners=None):
    root = Path(root)
    plan = json.loads((root / "organisation/production_plan.json").read_text())
    registry = json.loads((root / "organisation/fragments.json").read_text())
    source = (root / "shell/medina_front.html").read_text()
    entries = json.loads(re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', source, re.S).group(1))["entries"]
    if category_owners is None:
        # The isolated frontends own category placement. Legacy anatomical
        # attachments still describe B18 as hepatic, while its frontend is T1.
        spec = importlib.util.spec_from_file_location("production_plan_surface", root / "fragment_surface.py")
        surface = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(surface)
        category_owners = surface.frontend_catalog(root)[1]
    chapters = [c for c in json.loads((root / "chapters.json").read_text()) if c.get("integrated")]
    courses = {code: chapter["code"] for chapter in chapters for code in chapter.get("covers", [chapter["code"]])}
    titles = {entry["code"]: entry["title"] for entry in entries}
    titles.update({chapter["code"]: chapter["title"] for chapter in chapters})
    return plan, validate_plan(plan, registry, category_owners, courses, titles)


if __name__ == "__main__":
    plan, assignments = load_plan(Path(__file__).resolve().parents[1])
    print(f"OK : {len(assignments)} attributions ; Claude 11 / Codex 10 ; remise par fragment entier, un audit croisé, HTML clair.")
