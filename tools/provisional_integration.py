"""Narrow, documented C-01 exception requested by Vial on 8 October 2026.

This validates recorded provenance, scope, hashes and visible reservation
markup, not clinical safety or whether a reported browser check really ran.
It never constitutes final fragment review, completion or an INJECTE state.
The normal fragment guard remains authoritative for terminal fragment locks.
"""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import PurePosixPath
import re
import subprocess


REGISTRY = "organisation/provisional_integrations.json"
KIND = "exception_c01_vial_2026-10-08"
STATUS = "PROVISOIRE_AVEC_RESERVES"
FRAGMENT = "S01"
LABEL = "C-01-Cardiologie"
# Only the received PR16 additions and its one I70 cross-reference correction.
# Another fragment or chapter requires another explicit protocol decision.
COURSES = frozenset({"I51", "I73", "I77", "I85", "I89", "I95", "I97", "R00", "R02", "I70"})
CHECKS = frozenset({"unit", "static", "build", "desktop", "mobile"})


class ProvisionalError(ValueError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise ProvisionalError("Provisoire : chemin relatif sûr requis.")
    path = PurePosixPath(value)
    if (path.is_absolute() or str(path) != value or
            any(part in {".", ".."} for part in path.parts) or
            re.match(r"^[A-Za-z]:", value) or any(c in value for c in "\r\n\x00")):
        raise ProvisionalError("Provisoire : chemin relatif sûr requis.")
    return value


def digest(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ProvisionalError("Provisoire : empreinte SHA-256 invalide.")
    return value


def read_json(tree, path, required=True):
    raw = tree.read(path, required=required)
    if raw is None:
        return None
    try:
        return json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeError) as error:
        raise ProvisionalError(f"Provisoire : JSON UTF-8 illisible : {path}.") from error


def document(tree, path, expected):
    path = safe_path(path)
    raw = tree.read(path)
    if not raw.strip() or sha(raw) != digest(expected):
        raise ProvisionalError(f"Provisoire : preuve vide ou empreinte différente : {path}.")
    return raw


def records(tree):
    value = read_json(tree, REGISTRY, required=False)
    if value is None:
        return []
    if (not isinstance(value, dict) or value.get("schema_version") != 1 or
            value.get("kind") != KIND or not isinstance(value.get("integrations"), list)):
        raise ProvisionalError("Provisoire : registre ou schéma invalide.")
    items = value["integrations"]
    if any(not isinstance(item, dict) for item in items):
        raise ProvisionalError("Provisoire : chaque preuve doit être un objet.")
    identifiers = [item.get("id") for item in items]
    if (any(not isinstance(ident, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", ident) for ident in identifiers) or
            len(identifiers) != len(set(identifiers))):
        raise ProvisionalError("Provisoire : identifiant absent, invalide ou dupliqué.")
    return items


def course_catalog(tree):
    values = read_json(tree, "chapters.json")
    if (not isinstance(values, list) or
            any(not isinstance(item, dict) or not isinstance(item.get("code"), str) for item in values)):
        raise ProvisionalError("Provisoire : catalogue des cours invalide.")
    result = {item.get("code"): item for item in values}
    if any(not isinstance(code, str) for code in result) or len(result) != len(values):
        raise ProvisionalError("Provisoire : codes de cours absents ou dupliqués.")
    return result


def fragment_courses(tree):
    values = read_json(tree, "fragments.json")
    if not isinstance(values, list):
        raise ProvisionalError("Provisoire : catalogue de fragments invalide.")
    fragment = next((item for item in values if isinstance(item, dict) and item.get("id") == FRAGMENT), None)
    if fragment is None or not isinstance(fragment.get("rattachements"), list):
        raise ProvisionalError("Provisoire : appartenance documentaire C-01 absente.")
    return {code for code in fragment["rattachements"] if isinstance(code, str) and re.fullmatch(r"[A-Z][0-9]{2}", code)}


class ReservationMarkup(HTMLParser):
    """Inspect the authored marker itself; actual rendering is browser evidence."""

    def __init__(self, marker_id, reservation_id):
        super().__init__(convert_charrefs=True)
        self.marker_id, self.reservation_id = marker_id, reservation_id
        self.matches, self.depth, self.text = [], 0, []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id") == self.marker_id:
            self.matches.append((tag, attributes))
            self.depth = 1
        elif self.depth and tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.depth += 1

    def handle_startendtag(self, tag, attrs):
        # A self-closing marker has no explanatory text and is rejected.
        if dict(attrs).get("id") == self.marker_id:
            self.matches.append((tag, dict(attrs)))

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.text.append(data)

    def validate(self):
        if len(self.matches) != 1:
            raise ProvisionalError(f"Provisoire : marque de réserve absente ou dupliquée : {self.marker_id}.")
        tag, attributes = self.matches[0]
        style = re.sub(r"\s+", "", attributes.get("style", "")).lower()
        text = " ".join(" ".join(self.text).split()).casefold()
        if (tag != "div" or "alert" not in attributes.get("class", "").split() or
                attributes.get("data-claude-reservation") != self.reservation_id or
                attributes.get("data-reservation-status") != "open" or
                "hidden" in attributes or attributes.get("aria-hidden", "").lower() == "true" or
                "display:none" in style or "visibility:hidden" in style or "opacity:0" in style or
                len(text) < 40 or "réserve" not in text or "clinique" not in text):
            raise ProvisionalError(f"Provisoire : réserve explicite non masquée requise : {self.marker_id}.")


def validate_provisional(before, after, old_fragments, new_fragments):
    """Return hashes authorized by newly appended, narrowly scoped proofs.

    Previous proofs remain immutable. A new proof validates the exact delta
    from the CI base, with staged copies and current clinical reservation
    markers. Unrelated files never receive authorization from this ledger.
    """
    old, new = records(before), records(after)
    if len(new) < len(old) or new[:len(old)] != old:
        raise ProvisionalError("Provisoire : retrait, réécriture ou réordonnancement d'une preuve interdit.")
    if not new:
        return {}
    additions = new[len(old):]
    if additions:
        if old_fragments.get(FRAGMENT) != new_fragments.get(FRAGMENT):
            raise ProvisionalError("Provisoire : cette exception ne modifie pas le statut final ou l'attribution du fragment.")
        if old_fragments[FRAGMENT]["status"] == "INJECTE":
            raise ProvisionalError("Provisoire : aucune exception sur un fragment INJECTE immuable.")
        if old_fragments[FRAGMENT]["status"] not in {"A_COMPLETER", "EN_PRODUCTION"}:
            raise ProvisionalError("Provisoire : exception réservée à un fragment encore en production.")
    authorized = {}
    changed_courses = set()
    old_catalog, new_catalog = course_catalog(before), course_catalog(after)
    old_attachments, new_attachments = fragment_courses(before), fragment_courses(after)
    if additions and old_attachments != new_attachments:
        raise ProvisionalError("Provisoire : les rattachements documentaires restent inchangés.")
    baseline = subprocess.run(["git", "rev-parse", "--verify", f"{before.revision}^{{commit}}"],
                              cwd=before.root, check=True, capture_output=True, text=True).stdout.strip()
    for index, item in enumerate(new):
        is_new = index >= len(old)
        courses = item.get("courses")
        if (item.get("fragment_id") != FRAGMENT or item.get("label") != LABEL or
                item.get("status") != STATUS or not isinstance(courses, list) or not courses or
                any(not isinstance(code, str) or code not in COURSES for code in courses) or
                len(courses) != len(set(courses))):
            raise ProvisionalError("Provisoire : exception limitée aux cours de la remise C-01 PR16 et à I70.")
        if not isinstance(item.get("base_commit"), str) or not re.fullmatch(r"[0-9a-f]{40}", item["base_commit"]):
            raise ProvisionalError("Provisoire : SHA de baseline complet requis.")
        if is_new and item["base_commit"] != baseline:
            raise ProvisionalError("Provisoire : baseline différente de la tête avant le changement.")
        authority = item.get("authority")
        if not isinstance(authority, dict) or authority.get("requested_by") != "Vial":
            raise ProvisionalError("Provisoire : instruction exceptionnelle explicite de Vial requise.")
        document(after, authority.get("request_path"), authority.get("request_sha256"))
        document(after, item.get("report_path"), item.get("report_sha256"))
        checks = item.get("checks")
        if (not isinstance(checks, list) or any(not isinstance(check, dict) for check in checks) or
                any(not isinstance(check.get("kind"), str) for check in checks) or
                {check.get("kind") for check in checks} != CHECKS):
            raise ProvisionalError("Provisoire : contrôles unitaires, statiques, construction, bureau et mobile requis.")
        for check in checks:
            if check.get("result") != "passed":
                raise ProvisionalError("Provisoire : contrôle obligatoire non réussi.")
            document(after, check.get("evidence_path"), check.get("evidence_sha256"))
        source_dir = safe_path(item.get("source_dir"))
        if source_dir.startswith(("chapters/", "glossary/")) or source_dir in {"chapters", "glossary"}:
            raise ProvisionalError("Provisoire : copies adaptées séparées des sources canoniques requises.")
        files = item.get("files")
        if not isinstance(files, dict) or not files:
            raise ProvisionalError("Provisoire : inventaire des adaptations vide.")
        covered = set()
        for target, proof in files.items():
            target = safe_path(target)
            if not isinstance(proof, dict) or set(proof) != {"before_sha256", "sha256"}:
                raise ProvisionalError("Provisoire : empreintes avant/après explicites requises.")
            digest(proof["sha256"])
            if proof["before_sha256"] is not None:
                digest(proof["before_sha256"])
            parts = PurePosixPath(target).parts
            if target == "chapters.json":
                code = None
            elif len(parts) == 3 and parts[0] == "chapters" and parts[1] in courses and re.fullmatch(re.escape(parts[1]) + r"_[A-Za-z0-9][A-Za-z0-9_.-]*\.(?:html|json)", parts[2]):
                code = parts[1]
            elif len(parts) == 2 and parts[0] == "glossary" and parts[1].endswith(".py") and parts[1][:-3].upper() in courses:
                code = parts[1][:-3].upper()
            else:
                raise ProvisionalError(f"Provisoire : fichier hors périmètre C-01 autorisé : {target}.")
            if code:
                covered.add(code)
            if code and is_new:
                course = new_catalog.get(code)
                if (not course or course.get("integrated") is not True or not course.get("title") or
                        course.get("complete") is True or course.get("icd11_complete") is True or
                        course.get("status") == "INJECTE"):
                    raise ProvisionalError(f"Provisoire : cours, code et titre non déclarés : {code}.")
                # Existing ownership must not move; a new grouped course needs
                # explicit C-01 ownership, including I85 with digestive content.
                if code in old_catalog:
                    if old_catalog[code].get("owner", FRAGMENT if code in old_attachments else None) != FRAGMENT:
                        raise ProvisionalError(f"Provisoire : ancien cours d'un autre fragment : {code}.")
                if course.get("owner", FRAGMENT if code in old_attachments else None) != FRAGMENT:
                    raise ProvisionalError(f"Provisoire : appartenance explicite C-01 absente : {code}.")
            document(after, f"{source_dir}/{target}", proof["sha256"])
            if is_new:
                original = before.read(target, required=False)
                original_digest = sha(original) if original is not None else None
                if original_digest != proof["before_sha256"]:
                    raise ProvisionalError(f"Provisoire : source de baseline modifiée : {target}.")
                current = after.read(target)
                if sha(current) != proof["sha256"]:
                    raise ProvisionalError(f"Provisoire : source injectée différente de l'adaptation : {target}.")
                if target in authorized:
                    raise ProvisionalError(f"Provisoire : fichier autorisé deux fois dans la même itération : {target}.")
                authorized[target] = proof["sha256"]
        if covered != set(courses):
            raise ProvisionalError("Provisoire : chaque cours annoncé doit avoir une adaptation inventoriée.")
        reservations = item.get("reservations")
        if not isinstance(reservations, list) or not reservations:
            raise ProvisionalError("Provisoire : réserves cliniques ouvertes et repérables requises.")
        reservation_ids = set()
        for reservation in reservations:
            if not isinstance(reservation, dict):
                raise ProvisionalError("Provisoire : réserve structurée requise.")
            ident = reservation.get("id")
            if (not isinstance(ident, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", ident) or
                    ident in reservation_ids or reservation.get("course") not in courses or
                    reservation.get("status") != "open" or
                    not isinstance(reservation.get("reason"), str) or not reservation["reason"].strip() or
                    not isinstance(reservation.get("action"), str) or not reservation["action"].strip()):
                raise ProvisionalError("Provisoire : réserve ouverte, motif et action Claude explicites requis.")
            reservation_ids.add(ident)
            targets = reservation.get("targets")
            if not isinstance(targets, list) or not targets:
                raise ProvisionalError("Provisoire : localisation de réserve absente.")
            for target in targets:
                if not isinstance(target, dict):
                    raise ProvisionalError("Provisoire : cible de réserve structurée requise.")
                path, marker_id = safe_path(target.get("path")), target.get("marker_id")
                if (path not in files or not path.startswith(f"chapters/{reservation['course']}/") or
                        not path.endswith(".html") or not isinstance(marker_id, str) or
                        not re.fullmatch(reservation["course"].lower() + r"-[A-Za-z0-9_-]+", marker_id)):
                    raise ProvisionalError("Provisoire : marque hors du cours et du fichier adapté.")
                markup = ReservationMarkup(marker_id, ident)
                markup.feed(after.read(f"{source_dir}/{path}").decode("utf-8"))
                markup.validate()
                if is_new:
                    live = ReservationMarkup(marker_id, ident)
                    live.feed(after.read(path).decode("utf-8"))
                    live.validate()
        if is_new:
            changed_courses.update(courses)
    if "chapters.json" in authorized:
        for code in old_catalog.keys() | new_catalog.keys():
            if old_catalog.get(code) != new_catalog.get(code) and code not in changed_courses:
                raise ProvisionalError(f"Provisoire : catalogue modifiant un cours tiers : {code}.")
        if not set(old_catalog).issubset(new_catalog):
            raise ProvisionalError("Provisoire : suppression d'un ancien cours interdite.")
    return authorized
