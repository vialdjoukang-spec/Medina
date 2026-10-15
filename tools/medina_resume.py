#!/usr/bin/env python3
"""Reprise MEDINA en lecture seule, sans réseau ni Git ; aucune publication déduite du catalogue."""
import argparse
import json
import os
from pathlib import Path

PLAN = "organisation/plan_tetrade_30_cycles.json"
CATALOG = "chapters.json"
REGISTRY = "organisation/CYCLES_CLAUDE.json"
NOVO = "organisation/novo_12/PLAN_NOVO_12.json"
BETTA = "organisation/betta_status.json"
BETTA_NOVO_PLAN = "organisation/progression/plan-novo12.json"
BETTA_NOVO_STATUS = "organisation/novo12_status.json"
TETRAD_SYSTEMS = {"S08", "S05", "S04", "S06"}


def read_json(root, path, kind, warnings):
    try:
        value = json.loads((root / path).read_text(encoding="utf-8"))
        if not isinstance(value, kind):
            raise ValueError("type JSON inattendu")
        return value
    except (OSError, UnicodeError, ValueError) as error:
        warnings.append(f"{path} : indisponible ou invalide ({error})")
        return None


def planned_codes(plan):
    systems = plan.get("systems")
    if not isinstance(systems, list) or len(systems) != 4:
        raise ValueError("quatre systèmes requis")
    if {system.get("id") for system in systems} != TETRAD_SYSTEMS:
        raise ValueError("seuls S08/S05/S04/S06 composent la tétrade")
    codes = []
    for system in systems:
        lessons = system.get("chapters")
        if not isinstance(lessons, list) or len(lessons) != 30:
            raise ValueError("trente leçons par système requises")
        for row in lessons:
            if not isinstance(row, list) or not row or not isinstance(row[0], str):
                raise ValueError("code de leçon absent")
            codes.append(row[0])
    if len(set(codes)) != 120:
        raise ValueError("120 codes distincts requis")
    return set(codes)


def novo_batches(plan, original):
    """Novo Tétrade seulement, distinct du Novo Betta cycles 42–125."""
    if plan.get("id") != "NOVO_12" or not isinstance(plan.get("cycles"), list):
        raise ValueError("plan Novo Tétrade absent")
    batches, seen = [], set()
    for index, batch in enumerate(plan["cycles"], 1):
        numbers = list(range(4 + (index - 1) * 3, 7 + (index - 1) * 3))
        systems = batch.get("systems", [])
        if batch.get("novo") != index or batch.get("tetrad_cycles") != numbers or len(systems) != 4:
            raise ValueError("lot Novo Tétrade incohérent")
        codes = []
        for system, source in zip(systems, original["systems"]):
            expected = [source["chapters"][n - 1][0] for n in numbers]
            if system.get("id") != source.get("id") or system.get("lessons") != expected:
                raise ValueError("attributions Novo différentes de la tétrade")
            codes.extend(expected)
        if len(set(codes)) != 12 or seen.intersection(codes):
            raise ValueError("leçons Novo dupliquées")
        seen.update(codes)
        batches.append({"novo": index, "anchor": numbers[0], "tetrad_cycles": numbers,
                        "lesson_count": len(codes)})
    if len(batches) != 9 or len(seen) != 108:
        raise ValueError("neuf lots et 108 leçons Novo Tétrade requis")
    return batches


def cycle_rows(registry, original):
    raw = registry.get("cycles")
    if not isinstance(raw, list):
        raise ValueError("liste des cycles Claude absente")
    result, seen = [], set()
    for cycle in raw:
        number, rows = cycle.get("cycle"), cycle.get("chapters")
        numbers = cycle.get("tetrad_cycles") if cycle.get("novo") else [number]
        if (type(number) is not int or not isinstance(rows, list)
                or not isinstance(numbers, list) or not numbers or numbers[0] != number
                or any(type(n) is not int or not 1 <= n <= 30 for n in numbers)):
            raise ValueError("identité ou contenu du cycle Claude invalide")
        novo = cycle.get("novo")
        if novo is not None and (type(novo) is not int or not 1 <= novo <= 9
                                  or number != 4 + (novo - 1) * 3
                                  or len(numbers) != 3 or len(rows) != 12
                                  or numbers != list(range(number, number + 3))):
            raise ValueError("un lot Novo Tétrade représente trois anciens cycles et douze leçons")
        if seen.intersection(numbers) or len(set(numbers)) != len(numbers):
            raise ValueError("cycles Claude dupliqués ou chevauchants")
        seen.update(numbers)
        lessons = []
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("code"), str) or not isinstance(row.get("status"), str):
                raise ValueError("statut de leçon Claude invalide")
            lessons.append({"code": row["code"], "status": row["status"]})
        expected = {system["chapters"][n - 1][0] for system in original["systems"] for n in numbers}
        if len(lessons) != len(expected) or {row["code"] for row in lessons} != expected:
            raise ValueError("leçons Claude différentes des cycles tétrade annoncés")
        if not isinstance(cycle.get("state", "INCONNU"), str):
            raise ValueError("état de cycle Claude invalide")
        result.append({"anchor": number, "novo": cycle.get("novo"), "tetrad_cycles": numbers,
                       "state": cycle.get("state", "INCONNU"), "lessons": lessons})
    return result


def betta_counts(status):
    cycles = status.get("cycles")
    if not isinstance(cycles, dict):
        raise ValueError("cycles Betta absents")
    counts = {"cycles": 0, "lessons": 0, "delivered_including_injected": 0, "injected": 0,
              "transferred_to_novo": 0}
    seen = set()
    for number, cycle in cycles.items():
        if not str(number).isdigit() or int(number) < 31 or not isinstance(cycle, dict):
            raise ValueError("identité de cycle Betta invalide")
        lessons = cycle.get("lessons")
        if not isinstance(lessons, dict):
            raise ValueError("leçons Betta absentes")
        if (any(not isinstance(code, str) or not code for code in lessons)
                or seen.intersection(lessons)):
            raise ValueError("codes de leçons Betta invalides ou dupliqués")
        seen.update(lessons)
        if cycle.get("state") == "TRANSFERE_NOVO12":
            # Ces leçons appartiennent maintenant au Novo Betta, pas aux deux jauges.
            counts["transferred_to_novo"] += len(lessons)
            continue
        counts["cycles"] += 1
        for lesson in lessons.values():
            state = lesson.get("state") if isinstance(lesson, dict) else lesson
            if not isinstance(state, str):
                raise ValueError("état de leçon Betta absent")
            counts["lessons"] += 1
            counts["delivered_including_injected"] += state in {"LIVRE", "INJECTE"}
            counts["injected"] += state == "INJECTE"
    return counts


def novo_betta_counts(plan, status):
    """Comptes du Novo Betta, jamais additionnés au Novo Tétrade 4–30."""
    first, last = plan.get("first"), plan.get("last")
    if (plan.get("id") != "novo12" or type(first) is not int or type(last) is not int
            or first < 42 or last < first or not isinstance(plan.get("cycles"), list)):
        raise ValueError("plan Novo Betta invalide")
    cycles = status.get("cycles")
    if status.get("plan") != BETTA_NOVO_PLAN or not isinstance(cycles, dict):
        raise ValueError("statut Novo Betta non lié au plan")
    expected_numbers = list(range(first, last + 1))
    if ([cycle.get("number") for cycle in plan["cycles"]] != expected_numbers
            or set(cycles) != {str(n) for n in expected_numbers}):
        raise ValueError("cycles Novo Betta incomplets ou différents du plan")
    counts = {"first": first, "last": last, "cycles": len(cycles), "lessons": 0,
              "delivered_including_injected": 0, "injected": 0}
    seen = set()
    for cycle in plan["cycles"]:
        codes = [lesson["code"] for agent in cycle["agents"] for lesson in agent["lessons"]]
        if (not codes or any(not isinstance(code, str) for code in codes) or len(codes) > 12
                or cycle.get("lessons") != len(codes) or len(set(codes)) != len(codes)
                or seen.intersection(codes)):
            raise ValueError("leçons Novo Betta absentes, dupliquées ou incohérentes")
        seen.update(codes)
        recorded = cycles[str(cycle["number"])].get("lessons")
        if not isinstance(recorded, dict) or set(recorded) != set(codes):
            raise ValueError("leçons Novo Betta différentes du plan")
        for code in codes:
            lesson = recorded[code]
            state = lesson.get("state") if isinstance(lesson, dict) else lesson
            if not isinstance(state, str):
                raise ValueError("état de leçon Novo Betta absent")
            counts["lessons"] += 1
            counts["delivered_including_injected"] += state in {"LIVRE", "INJECTE"}
            counts["injected"] += state == "INJECTE"
    if plan.get("total_lessons") != counts["lessons"]:
        raise ValueError("total Novo Betta différent des leçons planifiées")
    return counts


def summarize(root):
    warnings = []
    original = read_json(root, PLAN, dict, warnings)
    catalog = read_json(root, CATALOG, list, warnings)
    registry = read_json(root, REGISTRY, dict, warnings)
    novo = read_json(root, NOVO, dict, warnings)
    betta = read_json(root, BETTA, dict, warnings)
    result = {"sequence_1_30": {"planned": None, "canonical_catalogue": None,
                               "public_confirmed": None, "claude_cycles": None, "novo_batches": None},
              "betta_31_plus": None, "novo_betta": None, "warnings": warnings,
              "limits": "Lecture locale seule : catalogue intégré et statuts déclarés, ni relecture médicale ni vérification publique. Aucun audit ni validation médicale humaine n'est déduit de ces compteurs."}
    sequence, codes = result["sequence_1_30"], None
    if original is not None:
        try:
            codes = planned_codes(original)
            sequence["planned"] = len(codes)
        except (ValueError, KeyError, TypeError, AttributeError) as error:
            warnings.append(f"{PLAN} : {error}")
    if catalog is not None and codes is not None:
        try:
            if any(not isinstance(row, dict) or not isinstance(row.get("code"), str) for row in catalog):
                raise ValueError("entrée de catalogue invalide")
            canonical = {row["code"] for row in catalog if row.get("integrated") is True}
            sequence["canonical_catalogue"] = len(canonical.intersection(codes))
        except ValueError as error:
            warnings.append(f"{CATALOG} : {error}")
    if registry is not None and codes is not None:
        try:
            sequence["claude_cycles"] = cycle_rows(registry, original)
        except (ValueError, KeyError, IndexError, TypeError, AttributeError) as error:
            warnings.append(f"{REGISTRY} : {error}")
    if novo is not None and codes is not None:
        try:
            sequence["novo_batches"] = novo_batches(novo, original)
        except (ValueError, KeyError, IndexError, TypeError, AttributeError) as error:
            warnings.append(f"{NOVO} : {error}")
    if betta is not None:
        try:
            result["betta_31_plus"] = betta_counts(betta)
        except (ValueError, TypeError, AttributeError) as error:
            warnings.append(f"{BETTA} : {error}")
    # Extension optionnelle : son absence dans un ancien clone n'est pas une panne.
    if any((root / path).exists() for path in (BETTA_NOVO_PLAN, BETTA_NOVO_STATUS)):
        plan = read_json(root, BETTA_NOVO_PLAN, dict, warnings)
        status = read_json(root, BETTA_NOVO_STATUS, dict, warnings)
        if plan is not None and status is not None:
            try:
                result["novo_betta"] = novo_betta_counts(plan, status)
            except (ValueError, KeyError, TypeError, AttributeError) as error:
                warnings.append(f"Novo Betta : {error}")
    return result


def ratio(value, total):
    return f"{value}/{total}" if value is not None and total is not None else "indisponible"


def status_line(report):
    sequence = report["sequence_1_30"]
    first = "Tétrade 1–30 : " + ratio(sequence["canonical_catalogue"], sequence["planned"]) + " canoniques au catalogue"
    betta = report["betta_31_plus"]
    second = (f"Betta 31+ : {betta['delivered_including_injected']}/{betta['lessons']} livrées (dont {betta['injected']} injectées)"
              if betta is not None else "Betta 31+ : indisponible")
    novo = report["novo_betta"]
    third = (f"Novo Betta {novo['first']}–{novo['last']} : {novo['delivered_including_injected']}/{novo['lessons']} livrées (dont {novo['injected']} injectées)"
             if novo is not None else "Novo Betta : non configuré ou indisponible")
    return " | ".join((first, second, third, "public non vérifié ici")) + (" | réserves" if report["warnings"] else "")


def cycle_label(cycle):
    return (f"Novo Tétrade {cycle['novo']} (anciens cycles " + ", ".join(map(str, cycle["tetrad_cycles"])) + ")"
            if cycle["novo"] else f"Cycle {cycle['anchor']}")


def cycle_progress(cycle):
    """Cases exclusives du registre : une injection n'est pas une publication."""
    states = [row["status"] for row in cycle["lessons"]]
    return {"total": len(states), "published_declared": states.count("PUBLIE_VERIFIE"),
            "injected_pending_public": states.count("INJECTE"), "ready": states.count("PRET_A_INJECTER"),
            "other": sum(state not in {"PUBLIE_VERIFIE", "INJECTE", "PRET_A_INJECTER"} for state in states)}


def chat_progress(report):
    """Relevé copiable dans le chat ; ni pilotage du chat ni vérification distante."""
    sequence = report["sequence_1_30"]
    lines = ["Tétrade 1–30 — 🟦 " + ratio(sequence["canonical_catalogue"], sequence["planned"])
             + " canoniques au catalogue ; public non vérifié ici.",
             f"Sources : {CATALOG} + {PLAN}."]
    cycles = sequence["claude_cycles"]
    if cycles is None:
        lines.extend(["", "⚪ Registre Claude indisponible : aucun avancement public n'est déduit."])
    else:
        covered = sorted({number for cycle in cycles for number in cycle["tetrad_cycles"]})
        lines.extend(["", "Couverture du registre Claude : " + (", ".join(map(str, covered)) or "aucun cycle") + "."])
        if 1 not in covered:
            lines.append("Cycle 1 absent de ce registre : non compté ici, sans présumer son état.")
        active = [cycle for cycle in cycles if cycle["state"] == "ACTIF"]
        if not active:
            lines.append("Aucun cycle ACTIF déclaré dans ce registre.")
        colors = {"PUBLIE_VERIFIE": "🟩", "INJECTE": "🟦", "PRET_A_INJECTER": "🟨"}
        for cycle in active:
            counts = cycle_progress(cycle)
            total = counts["total"]
            lines.extend(["", cycle_label(cycle) + f" — {total} leçons au registre :",
                          "".join(colors.get(row["status"], "⬜") for row in cycle["lessons"]),
                          f"🟩 Déclarées publiées {counts['published_declared']}/{total} ; "
                          f"🟦 Injectées, publication non encore déclarée {counts['injected_pending_public']}/{total} ; "
                          f"🟨 Prêtes à injecter {counts['ready']}/{total}."])
            if counts["other"]:
                lines.append(f"⬜ Autres états {counts['other']}/{total}.")
            lines.append(" ; ".join(f"{row['code']}={row['status']}" for row in cycle["lessons"]) + ".")
    lines.append(f"Source des états déclarés : {REGISTRY} ; couverture partielle, pas de total public sur 120.")
    batches = sequence["novo_batches"]
    if batches is None:
        lines.extend(["", "⚪ Novo Tétrade : plan indisponible."])
    else:
        lines.extend(["", f"📋 Novo Tétrade : {len(batches)} lots / {sum(batch['lesson_count'] for batch in batches)} leçons planifiées, pas publiées par présomption.",
                      f"Source : {NOVO} ; lot 1 = cycles 4–6, distinct du Novo Betta."])
    betta = report["betta_31_plus"]
    if betta is None:
        lines.append("⚪ Betta 31+ historique : état indisponible.")
    else:
        lines.extend([f"🟪 Betta 31+ historique : {betta['delivered_including_injected']}/{betta['lessons']} livrées déclarées, dont {betta['injected']} injectées.",
                      f"{betta['transferred_to_novo']} leçons transférées au Novo Betta, exclues de la jauge historique."])
    lines.append(f"Source : {BETTA}.")
    novo = report["novo_betta"]
    if novo is None:
        lines.append("⚪ Novo Betta : non configuré ou état indisponible.")
    else:
        lines.append(f"🟧 Novo Betta {novo['first']}–{novo['last']} : {novo['delivered_including_injected']}/{novo['lessons']} livrées déclarées, dont {novo['injected']} injectées.")
    lines.extend([f"Sources Novo Betta : {BETTA_NOVO_PLAN} + {BETTA_NOVO_STATUS}.",
                  "", "Limites : " + report["limits"],
                  "Les couleurs décrivent des statuts locaux, pas une certification médicale. Ce relevé n'écrit rien et ne contrôle pas le chat Claude."])
    if report["warnings"]:
        lines.extend(["", "Réserves :", *("- " + warning for warning in report["warnings"])])
    return "\n".join(lines)


def render(report):
    lines = ["MEDINA — reprise dynamique, lecture seule", "", status_line(report), "", report["limits"]]
    sequence = report["sequence_1_30"]
    for cycle in sequence["claude_cycles"] or []:
        label = cycle_label(cycle)
        lines.extend(["", f"{label} : {cycle['state']} au registre.",
                      "; ".join(f"{row['code']}={row['status']}" for row in cycle["lessons"])])
    batches = sequence["novo_batches"]
    if batches:
        first = batches[0]
        lines.extend(["", f"Novo Tétrade : {len(batches)} lots / {sum(b['lesson_count'] for b in batches)} leçons planifiées.",
                      f"Lot 1 = anciens cycles {first['tetrad_cycles']} ; {first['lesson_count']} leçons ; ancre technique {first['anchor']}.",
                      "Planification déclarée ; ce relevé ne donne aucun ordre de démarrage et n'applique aucun verrou de publication."])
    betta = report["betta_31_plus"]
    if betta and betta["transferred_to_novo"]:
        lines.extend(["", f"Betta historique : {betta['transferred_to_novo']} leçons transférées au Novo Betta, exclues de la jauge historique."])
    if report["novo_betta"]:
        lines.append("Novo Betta 42+ est une piste distincte ; ses nombres ne sont jamais ajoutés au Novo Tétrade 4–30.")
    if report["warnings"]:
        lines.extend(["", "Réserves :", *("- " + warning for warning in report["warnings"])])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[1]))
    parser.add_argument("--status-line", action="store_true", help="Pistes Tétrade, Betta et Novo Betta séparées ; le JSON d'entrée est ignoré.")
    parser.add_argument("--chat-progress", action="store_true", help="Jauges colorées par cycle actif, sources et limites, à copier dans le chat.")
    parser.add_argument("--json", action="store_true", help="Afficher le relevé structuré sans écrire de fichier.")
    args = parser.parse_args(argv)
    # stdin n'est pas une source d'avancement : les événements Claude Code sont ignorés.
    report = summarize(args.root)
    print(status_line(report) if args.status_line else chat_progress(report) if args.chat_progress
          else json.dumps(report, ensure_ascii=False, indent=2) if args.json else render(report))
    return 0 if args.status_line or not report["warnings"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
